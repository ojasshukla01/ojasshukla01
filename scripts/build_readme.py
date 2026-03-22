#!/usr/bin/env python3
"""
Refresh GitHub comment-delimited sections in README.md (Simon Willison pattern).
https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import feedparser

REPOSITORIES_QUERY = """
query ($login: String!, $cursor: String) {
  user(login: $login) {
    repositories(
      first: 100
      after: $cursor
      privacy: PUBLIC
      orderBy: { field: PUSHED_AT, direction: DESC }
    ) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        nameWithOwner
        url
        pushedAt
        releases(first: 1, orderBy: { field: CREATED_AT, direction: DESC }) {
          nodes {
            name
            tagName
            url
            publishedAt
          }
        }
      }
    }
  }
}
"""

# One round trip: starred repos + authored PR search (replaces separate calls).
STARS_AND_PRS_QUERY = """
query ($login: String!, $q: String!) {
  user(login: $login) {
    starredRepositories(first: 16, orderBy: { field: STARRED_AT, direction: DESC }) {
      edges {
        starredAt
        node {
          nameWithOwner
          url
        }
      }
    }
  }
  search(query: $q, type: ISSUE, first: 40) {
    nodes {
      ... on PullRequest {
        title
        url
        state
        mergedAt
        updatedAt
        repository {
          nameWithOwner
        }
      }
    }
  }
}
"""

DEFAULT_MEDIUM_FEED = "https://medium.com/feed/@ojasshukla01"

PR_TITLE_MAX = 88

MAX_HTTP_ATTEMPTS = 3
BACKOFF_SECONDS = 1.5


def canonical_link(url: str) -> str:
    """Drop tracking query strings (e.g. Medium ?source=rss-...)."""
    try:
        p = urlparse((url or "").strip())
        if not p.scheme or not p.netloc:
            return url or "#"
        return urlunparse((p.scheme, p.netloc, p.path, "", "", ""))
    except Exception:
        return url or "#"


def _graphql_once(query: str, variables: dict, token: str) -> dict:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "ojasshukla01-profile-readme-build",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.load(resp)
    except urllib.error.HTTPError as exc:
        if exc.code >= 500:
            raise
        payload_txt = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub HTTP {exc.code}: {payload_txt[:500]}") from exc
    if body.get("errors"):
        raise RuntimeError(json.dumps(body["errors"], indent=2))
    return body["data"]


def graphql(query: str, variables: dict, token: str) -> dict:
    """GraphQL with retries on transient network / HTTP 5xx."""
    delay = BACKOFF_SECONDS
    last: BaseException | None = None
    for attempt in range(MAX_HTTP_ATTEMPTS):
        try:
            return _graphql_once(query, variables, token)
        except (
            urllib.error.URLError,
            urllib.error.HTTPError,
            TimeoutError,
            json.JSONDecodeError,
        ) as exc:
            if isinstance(exc, urllib.error.HTTPError) and exc.code < 500:
                raise
            last = exc
            if attempt == MAX_HTTP_ATTEMPTS - 1:
                break
            time.sleep(delay)
            delay *= 2
    assert last is not None
    raise last


def fetch_public_repositories(login: str, token: str) -> list[dict]:
    repos: list[dict] = []
    cursor: str | None = None
    while True:
        data = graphql(REPOSITORIES_QUERY, {"login": login, "cursor": cursor}, token)
        user = data.get("user")
        if not user:
            raise RuntimeError(f"GitHub user not found or not visible: {login!r}")
        conn = user["repositories"]
        repos.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    return repos


def fetch_stars_and_authored_pull_requests(login: str, token: str) -> tuple[list[dict], list[dict]]:
    search_q = f"is:pr author:{login} sort:updated-desc"
    data = graphql(STARS_AND_PRS_QUERY, {"login": login, "q": search_q}, token)
    user = data.get("user")
    if not user:
        raise RuntimeError(f"GitHub user not found or not visible: {login!r}")
    edges = (user.get("starredRepositories") or {}).get("edges") or []
    nodes = (data.get("search") or {}).get("nodes") or []
    prs = [n for n in nodes if n and n.get("url")]
    return prs, edges


def pr_repo_names_for_star_filter(pr_nodes: list[dict], limit: int = 7) -> set[str]:
    """Repos that appear in the deduped PR list (exclude from stars for less repetition)."""
    seen: set[str] = set()
    names: set[str] = set()
    for pr in pr_nodes:
        repo = pr["repository"]["nameWithOwner"]
        if repo in seen:
            continue
        seen.add(repo)
        names.add(repo)
        if len(names) >= limit:
            break
    return names


def format_releases_md(repos: list[dict], limit: int = 6) -> str:
    rows: list[tuple[str, str]] = []
    for r in repos:
        nodes = (r.get("releases") or {}).get("nodes") or []
        if not nodes:
            continue
        rel = nodes[0]
        published = rel.get("publishedAt") or ""
        tag = rel.get("tagName") or rel.get("name") or "release"
        url = rel.get("url") or r["url"]
        line = f"- [{r['nameWithOwner']} `{tag}`]({url}) — _{published[:10]} · release_"
        rows.append((published, line))
    rows.sort(key=lambda x: x[0], reverse=True)
    lines = [line for _, line in rows[:limit]]
    if not lines:
        return "_No published GitHub releases found on public repositories in this pass._"
    return "\n".join(lines)


def format_recent_repos_md(
    repos: list[dict], owner: str, limit: int = 8, exclude_name: str | None = None
) -> str:
    profile_repo = f"{owner}/{owner}"
    lines: list[str] = []
    for r in repos:
        nwo = r["nameWithOwner"]
        if exclude_name and nwo == exclude_name:
            continue
        if nwo == profile_repo:
            continue
        pushed = (r.get("pushedAt") or "")[:10]
        lines.append(f"- [{nwo}]({r['url']}) — _{pushed}_")
        if len(lines) >= limit:
            break
    if not lines:
        return "_No public repository metadata returned._"
    return "\n".join(lines)


def format_rss_feed_md(feed_url: str, *, limit: int = 6, source_label: str = "Feed") -> str:
    delay = BACKOFF_SECONDS
    feed = None
    last_err: str | None = None
    for attempt in range(MAX_HTTP_ATTEMPTS):
        try:
            feed = feedparser.parse(feed_url)
            break
        except Exception as exc:  # noqa: BLE001
            last_err = str(exc)
            if attempt == MAX_HTTP_ATTEMPTS - 1:
                return f"_{source_label} error: {last_err}_"
            time.sleep(delay)
            delay *= 2
    assert feed is not None
    if getattr(feed, "bozo", False) and not feed.entries:
        return f"_{source_label} could not be parsed or is empty._"
    lines: list[str] = []
    for entry in feed.entries[:limit]:
        title = entry.get("title") or "Untitled"
        link = canonical_link(entry.get("link") or "#")
        lines.append(f"- [{title}]({link})")
    if not lines:
        return f"_{source_label}: no entries._"
    return "\n".join(lines)


def format_prs_md(pr_nodes: list[dict], limit: int = 7) -> str:
    """One row per repository (most recently updated authored PR per repo)."""
    seen_repos: set[str] = set()
    lines: list[str] = []
    for pr in pr_nodes:
        repo = pr["repository"]["nameWithOwner"]
        if repo in seen_repos:
            continue
        seen_repos.add(repo)
        title = (pr.get("title") or "Pull request").replace("\r\n", " ").strip()
        if len(title) > PR_TITLE_MAX:
            title = title[: PR_TITLE_MAX - 1] + "…"
        url = pr["url"]
        merged_at = pr.get("mergedAt")
        state = (pr.get("state") or "").upper()
        when = (merged_at or pr.get("updatedAt") or "")[:10]
        if merged_at:
            status = "merged"
        elif state == "OPEN":
            status = "open"
        elif state == "CLOSED":
            status = "closed"
        else:
            status = "updated"
        lines.append(f"- [{repo}: {title}]({url}) — _{when} · {status}_")
        if len(lines) >= limit:
            break
    if not lines:
        return "_No pull requests returned for this account in this pass._"
    return "\n".join(lines)


def format_starred_md(
    starred_edges: list[dict],
    limit: int = 8,
    exclude_repos: set[str] | None = None,
) -> str:
    exclude_repos = exclude_repos or set()
    lines: list[str] = []
    for edge in starred_edges:
        node = edge["node"]
        nwo = node["nameWithOwner"]
        if nwo in exclude_repos:
            continue
        at = (edge.get("starredAt") or "")[:10]
        lines.append(f"- [{nwo}]({node['url']}) — _{at} · starred_")
        if len(lines) >= limit:
            break
    if not lines:
        return "_No starred repositories returned (after excluding repos already listed under pull requests)._"
    return "\n".join(lines)


def replace_block(text: str, marker: str, body: str) -> str:
    start_tag = f"<!-- {marker} starts -->"
    end_tag = f"<!-- {marker} ends -->"
    start = text.index(start_tag) + len(start_tag)
    end = text.index(end_tag, start)
    middle = "\n" + body.strip() + "\n"
    return text[:start] + middle + text[end:]


def resolve_owner() -> str:
    return (
        os.environ.get("GITHUB_REPOSITORY_OWNER")
        or os.environ.get("PROFILE_README_OWNER")
        or os.environ.get("GITHUB_ACTOR")
        or "ojasshukla01"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Inject dynamic lists into profile README.md")
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "README.md",
        help="Path to README.md",
    )
    parser.add_argument(
        "--medium-feed",
        default="",
        help="Medium RSS URL (default: env MEDIUM_FEED_URL or @ojasshukla01 feed)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated sections only; do not write README.md",
    )
    args = parser.parse_args()

    medium_feed = (
        (args.medium_feed or "").strip()
        or (os.environ.get("MEDIUM_FEED_URL") or "").strip()
        or DEFAULT_MEDIUM_FEED
    )

    token = os.environ.get("GITHUB_TOKEN")
    owner = resolve_owner()

    medium_md = format_rss_feed_md(medium_feed, limit=5, source_label="Medium")

    token_hint = (
        "Set GITHUB_TOKEN for GitHub sections. Examples:\n"
        "  PowerShell:  $env:GITHUB_TOKEN = (gh auth token)\n"
        "  bash:         export GITHUB_TOKEN=$(gh auth token)\n"
        "Or create a classic PAT with at least read access to public repo metadata."
    )

    gh_placeholder = (
        "_Skipped (set `GITHUB_TOKEN` to preview). "
        "PowerShell: `$env:GITHUB_TOKEN = (gh auth token)`_"
    )

    if not token:
        if args.dry_run:
            print("Note: no GITHUB_TOKEN - GitHub sections are placeholders below.\n", file=sys.stderr)
            print(token_hint, file=sys.stderr)
            print(
                "--- releases ---\n",
                gh_placeholder,
                "\n--- medium ---\n",
                medium_md,
                "\n--- pull_requests ---\n",
                gh_placeholder,
                "\n--- starred ---\n",
                gh_placeholder,
                "\n--- repos ---\n",
                gh_placeholder,
            )
            return 0
        print("GITHUB_TOKEN is not set; cannot refresh GitHub sections.", file=sys.stderr)
        print(token_hint, file=sys.stderr)
        return 1

    try:
        repos = fetch_public_repositories(owner, token)
        pr_nodes, starred_edges = fetch_stars_and_authored_pull_requests(owner, token)
    except (urllib.error.URLError, RuntimeError, TimeoutError, ValueError) as exc:
        print(f"GitHub GraphQL failed: {exc}", file=sys.stderr)
        return 1

    releases_md = format_releases_md(repos)
    repos_md = format_recent_repos_md(repos, owner)
    prs_md = format_prs_md(pr_nodes)
    pr_repos = pr_repo_names_for_star_filter(pr_nodes)
    starred_md = format_starred_md(starred_edges, exclude_repos=pr_repos)

    readme_path: Path = args.readme
    text = readme_path.read_text(encoding="utf-8")
    text = replace_block(text, "profile_releases", releases_md)
    text = replace_block(text, "profile_medium", medium_md)
    text = replace_block(text, "profile_prs", prs_md)
    text = replace_block(text, "profile_starred", starred_md)
    text = replace_block(text, "profile_repos", repos_md)

    if args.dry_run:
        print(
            "--- releases ---\n",
            releases_md,
            "\n--- medium ---\n",
            medium_md,
            "\n--- pull_requests ---\n",
            prs_md,
            "\n--- starred ---\n",
            starred_md,
            "\n--- repos ---\n",
            repos_md,
        )
        return 0

    readme_path.write_text(text, encoding="utf-8")
    print(f"Updated {readme_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
