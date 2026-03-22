<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=26&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&width=780&lines=Ojas+Shukla;Senior+Data+Engineer;GCP+%E2%80%A2+AWS+%E2%80%A2+Kafka+%E2%80%A2+dbt+%E2%80%A2+Snowflake+%E2%80%A2+DuckDB+%7C+Real-time+%26+batch+%7C+OSS" alt="Typing Animation" />

<br>

<a href="https://portfolio-ojas-shuklas-projects-7dc8ad06.vercel.app/" target="_blank">
  <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white&labelColor=000000" alt="Portfolio" />
</a>
<a href="https://medium.com/@ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white&labelColor=12100E" alt="Medium" />
</a>
<a href="https://www.linkedin.com/in/ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0077B5" alt="LinkedIn" />
</a>
<a href="mailto:ojasshukla01@gmail.com" target="_blank">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=D14836" alt="Email" />
</a>

<br><br>

[![Profile Views](https://komarev.com/ghpvc/?username=ojasshukla01&label=Profile%20views&color=0e75b6&style=flat-square)](https://github.com/ojasshukla01)
[![Profile README last commit](https://img.shields.io/github/last-commit/ojasshukla01/ojasshukla01?label=profile%20README%20updated&logo=github&color=1a1b27&style=flat-square)](https://github.com/ojasshukla01/ojasshukla01/commits/main)

</div>

---

### Navigate

[About](#about-me) · [Architecture view](#data-platform-mental-model) · [Stack](#technical-expertise) · [Featured](#featured-projects) · [All repos](#more-repositories) · [Analytics](#github-analytics) · [Connect](#connect-with-me)

---

<details>
<summary><strong>Contributor note</strong> — how this profile README is built (fork-friendly)</summary>

This file is plain **GitHub Flavored Markdown** in the special repository [`ojasshukla01/ojasshukla01`](https://github.com/ojasshukla01/ojasshukla01). Nothing here is a proprietary template; it is assembled from small, composable pieces you can reuse:

| Piece | Role | Source |
|------|------|--------|
| Typing header / footer | Animated SVG text | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) |
| Skill strip | One-glance toolchain | [skillicons.dev](https://skillicons.dev) |
| Stats / top languages | Live GitHub API (public instance; rate limits apply) | [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) |
| Contribution streak | Streak card (Demolab mirror) | [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) |
| Activity graph | Commit timeline SVG | [Ashutosh00710/github-readme-activity-graph](https://github.com/Ashutosh00710/github-readme-activity-graph) |
| Badges | Version / link chips | [Shields.io](https://shields.io) |
| Profile views | Hit counter | [antonkomarev/github-profile-views-counter](https://github.com/antonkomarev/github-profile-views-counter) |
| Diagram below | Rendered natively by GitHub | [Mermaid](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/) |

**Icons:** Section markers use **Unicode emoji** only (no hotlinked icon CDNs), so the page stays readable even when third-party image proxies fail.

**If you fork this layout:** swap `username` in URLs, self-host **github-readme-stats** if you need `include_all_commits` or private-repo metrics (requires a token), and keep attributions to the upstream projects above.

</details>

---

<div align="center">

## About Me

> **Senior Data Engineer** with **6+ years** designing cloud-native data platforms on **AWS**, **GCP**, **Azure**, and **Snowflake**—heavy on **Kafka**, **dbt**, **DuckDB**, and lakehouse patterns. I build **real-time and batch** pipelines, observability and governance, and **open-source** tooling: **schema-aware synthetic data** ([Data Forge](https://github.com/ojasshukla01/data-forge)), **safe SQL for AI agents via MCP** ([SQLSense](https://github.com/ojasshukla01/sqlsense)), and a **local-first token lifecycle CLI** ([token-doctor](https://github.com/ojasshukla01/token-doctor)).

</div>

```text
# quick context (same story, systems shape)
role            = senior_data_engineer
lanes           = streaming | batch | governance | synthetic_data | agent_safety
warehouses      = snowflake | bigquery | duckdb | lakehouse
orchestration   = airflow | cicd | infra_as_code
```

---

## Data platform mental model

High-level pattern I use when designing pipelines and platforms (illustrative, not project-specific):

```mermaid
flowchart LR
  subgraph sources[Sources]
    A[Events APIs files SaaS]
  end
  subgraph lake[Lakehouse]
    B[Bronze raw append]
    C[Silver conformed tested]
    D[Gold metrics marts]
  end
  subgraph serve[Serve and observe]
    E[BI apps reverse ETL]
    F[Quality lineage SLAs]
  end
  A --> B --> C --> D
  D --> E
  C -.-> F
  D -.-> F
```

---

## Technical Expertise

<div align="center">

**Stack snapshot** (icons are generated from [skillicons.dev](https://skillicons.dev); not every tool above has an icon there)

<img src="https://skillicons.dev/icons?i=py,gcp,aws,docker,kubernetes,terraform,kafka,postgres,nextjs,react,tailwind,git,githubactions,fastapi&perline=8" alt="Skill icons: Python, GCP, AWS, Docker, Kubernetes, Terraform, Kafka, Postgres, Next.js, React, Tailwind, Git, GitHub Actions, FastAPI" />

<br><br>

### 💻 Programming Languages
<a href="https://python.org" target="_blank">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=3776AB" alt="Python" />
</a>
<a href="https://www.microsoft.com/en-us/sql-server" target="_blank">
  <img src="https://img.shields.io/badge/-SQL-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white&labelColor=CC2927" alt="SQL" />
</a>
<a href="https://javascript.info" target="_blank">
  <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&labelColor=F7DF1E" alt="JavaScript" />
</a>
<a href="https://www.r-project.org" target="_blank">
  <img src="https://img.shields.io/badge/-R-276DC3?style=for-the-badge&logo=r&logoColor=white&labelColor=276DC3" alt="R" />
</a>
<a href="https://scala-lang.org" target="_blank">
  <img src="https://img.shields.io/badge/-Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white&labelColor=DC322F" alt="Scala" />
</a>

<br><br>

### ☁️ Cloud Platforms
<a href="https://cloud.google.com" target="_blank">
  <img src="https://img.shields.io/badge/-Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white&labelColor=4285F4" alt="Google Cloud" />
</a>
<a href="https://aws.amazon.com" target="_blank">
  <img src="https://img.shields.io/badge/-AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white&labelColor=FF9900" alt="AWS" />
</a>
<a href="https://azure.microsoft.com" target="_blank">
  <img src="https://img.shields.io/badge/-Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white&labelColor=0078D4" alt="Azure" />
</a>
<a href="https://snowflake.com" target="_blank">
  <img src="https://img.shields.io/badge/-Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white&labelColor=29B5E8" alt="Snowflake" />
</a>

<br><br>

### 🗄️ Data Platforms & Tools
<a href="https://spark.apache.org" target="_blank">
  <img src="https://img.shields.io/badge/-Apache%20Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white&labelColor=E25A1C" alt="Apache Spark" />
</a>
<a href="https://databricks.com" target="_blank">
  <img src="https://img.shields.io/badge/-Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white&labelColor=FF3621" alt="Databricks" />
</a>
<a href="https://cloud.google.com/bigquery" target="_blank">
  <img src="https://img.shields.io/badge/-BigQuery-4285F4?style=for-the-badge&logo=google-bigquery&logoColor=white&labelColor=4285F4" alt="BigQuery" />
</a>
<a href="https://kafka.apache.org" target="_blank">
  <img src="https://img.shields.io/badge/-Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white&labelColor=231F20" alt="Apache Kafka" />
</a>
<a href="https://airflow.apache.org" target="_blank">
  <img src="https://img.shields.io/badge/-Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white&labelColor=017CEE" alt="Apache Airflow" />
</a>
<a href="https://getdbt.com" target="_blank">
  <img src="https://img.shields.io/badge/-dbt-FF6944?style=for-the-badge&logo=dbt&logoColor=white&labelColor=FF6944" alt="dbt" />
</a>
<a href="https://duckdb.org" target="_blank">
  <img src="https://img.shields.io/badge/-DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black&labelColor=FFF000" alt="DuckDB" />
</a>

<br><br>

### ⚙️ DevOps & Infrastructure
<a href="https://docker.com" target="_blank">
  <img src="https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=2496ED" alt="Docker" />
</a>
<a href="https://terraform.io" target="_blank">
  <img src="https://img.shields.io/badge/-Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white&labelColor=7B42BC" alt="Terraform" />
</a>
<a href="https://github.com/features/actions" target="_blank">
  <img src="https://img.shields.io/badge/-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white&labelColor=2088FF" alt="GitHub Actions" />
</a>
<a href="https://kubernetes.io" target="_blank">
  <img src="https://img.shields.io/badge/-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white&labelColor=326CE5" alt="Kubernetes" />
</a>

</div>

---

<div align="center">

## Featured Projects

*Aligned with [pinned repositories](https://github.com/ojasshukla01?tab=repositories) and flagship data-engineering work. On any public repo here: **issues and PRs welcome** where the project has a license and contribution guidelines.*

<table>
<tr>
<td width="50%" align="left">

<div align="center">

### 🌿 [OpenCompliance ESG](https://github.com/ojasshukla01/opencompliance-esg)

</div>

**ESG data pipeline and analytics**

- Real-time ESG metrics dashboard
- Automated PDF reporting
- End-to-end data quality monitoring

**Tech Stack:** `Streamlit` `FastAPI` `DuckDB` `Python`

</td>
<td width="50%" align="left">

<div align="center">

### 📊 [Data Forge](https://github.com/ojasshukla01/data-forge)

</div>

**Time-aware synthetic data platform**

- Schema-driven generation (DDL, JSON Schema, OpenAPI); FKs and business rules
- Snapshot, incremental, and CDC-style flows; exports to Parquet, warehouses, and dbt seeds
- Next.js product UI + Python API—local-first, privacy-safe test data

**Tech Stack:** `Python` `Next.js` `FastAPI` `DuckDB` `PostgreSQL` `Snowflake` `BigQuery`

</td>
</tr>
<tr>
<td width="50%" align="left">

<div align="center">

### 🧠 [LLM Learning Path Generator](https://github.com/ojasshukla01/llm-learning-path-generator)

</div>

**AI-powered learning roadmaps**

- Personalized paths with LLMs, skill-gap analysis, adaptive recommendations

**Tech Stack:** `Streamlit` `LangChain` `DuckDB` `OpenAI`

</td>
<td width="50%" align="left">

<div align="center">

### 🔑 [token-doctor](https://github.com/ojasshukla01/token-doctor)

</div>

**Local-first API token lifecycle CLI**

- Validate tokens, infer JWT expiry, track 50+ platform changelogs and sunsets
- OS keychain storage, ICS calendar exports, Markdown/JSON reports—no telemetry

**Tech Stack:** `Python` `SQLite` CLI

</td>
</tr>
<tr>
<td width="50%" align="left">

<div align="center">

### 🛡️ [SQLSense](https://github.com/ojasshukla01/sqlsense)

</div>

**Safe, audited SQL for AI agents (MCP)**

- Guardrails, read-only by default, audit log, auto-`LIMIT`, column blocklists
- SQLite, PostgreSQL, SQL Server, Snowflake

**Tech Stack:** `Python` `MCP`

</td>
<td width="50%" align="left">

<div align="center">

### 🏥 [Health Analytics BI Dashboard](https://github.com/ojasshukla01/health-analytics-bi-dashboard)

</div>

**Healthcare analytics and BI**

- KPI dashboards and reporting patterns with Power BI

**Tech Stack:** `Power BI` `Analytics`

</td>
</tr>
</table>

</div>

---

## Portfolio & Writing

<div align="center">

### 🌐 [Professional Portfolio](https://portfolio-ojas-shuklas-projects-7dc8ad06.vercel.app/)
**Interactive Data Engineering Showcase**

Modern, responsive design with integrated project galleries, case studies, and professional experience details.

**Tech Stack:** `React` `Next.js` `Tailwind CSS` `Vercel`

---

### ✍️ [Technical Writing](https://medium.com/@ojasshukla01)
**Data Engineering Blog & Industry Insights**

In-depth technical articles, best practices, tutorials, industry insights on data engineering, and skillful portfolio design strategies.

**Platform:** `Medium` `Technical Writing` `Community`

</div>

---

## More Repositories

**Data platforms and pipelines**

- **🏭 [Lakehouse360](https://github.com/ojasshukla01/lakehouse360)** — Ingestion, transformation, data quality, Streamlit + DuckDB + dbt
- **📈 [Data Engineering Case Studies](https://github.com/ojasshukla01/data-engineering-case-studies)** — Batch/streaming patterns, BigQuery, Airflow, dbt
- **🗺️ [auto-map-au](https://github.com/ojasshukla01/auto-map-au) (AutoMap360)** — Suburb→region geospatial pipeline (AU, NZ, IN), shapefiles, Streamlit QA
- **📦 [data-pipeline](https://github.com/ojasshukla01/data-pipeline)** — Data engineering pipeline project
- **▶️ [BharatStream SQL](https://github.com/ojasshukla01/bharatstream-sql)** — SQL backend with analytics
- **🎬 [streaming-platform](https://github.com/ojasshukla01/streaming-platform)** — Video streaming stack with React

**Apps, tooling, and experiments**

- **💬 [prompt-hub](https://github.com/ojasshukla01/prompt-hub)** — Community-driven prompt sharing and management
- **🔧 [git-activity-simulator](https://github.com/ojasshukla01/git-activity-simulator)** — CLI to simulate commits, PRs, and activity for demos and learning
- **🌐 [ojas-portfolio](https://github.com/ojasshukla01/ojas-portfolio)** — Portfolio site source
- **📄 [sop_generator_app](https://github.com/ojasshukla01/sop_generator_app)** / **[sop-generator-frontend](https://github.com/ojasshukla01/sop-generator-frontend)** — SOP generator (Python + JS)
- **🔒 [web-bases-analysis-intrusion-detection-system](https://github.com/ojasshukla01/web-bases-analysis-intrusion-detection-system)** — Web-based intrusion detection analysis
- **🧪 [sql-injection](https://github.com/ojasshukla01/sql-injection)** — SQL injection lab (C#)
- **🧲 [Torrent_automate](https://github.com/ojasshukla01/Torrent_automate)** — Automation utilities
- **🤗 [hug-lite](https://github.com/ojasshukla01/hug-lite)** — Lightweight Hugging Face–related experiment

---

## GitHub Analytics

<div align="center">

<a href="https://github.com/ojasshukla01">
  <img src="https://github-readme-stats.vercel.app/api?username=ojasshukla01&show_icons=true&theme=tokyonight&hide_border=true&custom_title=GitHub%20Statistics" alt="GitHub Stats" />
</a>

<br><br>

<a href="https://github.com/ojasshukla01">
  <img src="https://streak-stats.demolab.com/?user=ojasshukla01&theme=tokyonight&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="GitHub Streak" />
</a>

<br><br>

<a href="https://github.com/ojasshukla01">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ojasshukla01&layout=compact&theme=tokyonight&hide_border=true&langs_count=8&custom_title=Most%20Used%20Languages" alt="Top Languages" />
</a>

<br><br>

<a href="https://github.com/ojasshukla01">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=ojasshukla01&theme=tokyo-night&color=00d4ff&line=00d4ff&point=ffffff&area=true&hide_border=true&custom_title=Contribution%20timeline%20(last%20year)" alt="GitHub contribution activity graph" />
</a>

</div>

---

## Professional Philosophy

<div align="center">

<table>
<tr>
<td width="25%" align="center">

### 💡 Innovation
*Driving technological advancement through creative problem-solving*

</td>
<td width="25%" align="center">

### ⭐ Excellence
*Maintaining highest standards in code quality and system design*

</td>
<td width="25%" align="center">

### 🤝 Collaboration
*Fostering knowledge sharing and team growth*

</td>
<td width="25%" align="center">

### 📈 Growth
*Continuous learning and adaptation to emerging technologies*

</td>
</tr>
</table>

</div>

---

## Personal Interests

<div align="center">

<table>
<tr>
<td width="33%" align="center">

### 🏊 Swimming
*Maintaining physical fitness and mental clarity*

</td>
<td width="33%" align="center">

### 🎮 Strategic Gaming
*Enhancing problem-solving skills through Dota 2*

</td>
<td width="33%" align="center">

### 📚 Continuous Learning
*Exploring LLMs and emerging data technologies*

</td>
</tr>
</table>

</div>

---

## Connect with Me

<div align="center">

I'm always open to discussing data engineering challenges, innovative projects, or collaboration opportunities.

<br>

<a href="https://portfolio-ojas-shuklas-projects-7dc8ad06.vercel.app/">
  <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white&labelColor=000000" alt="Portfolio" />
</a>
<a href="https://medium.com/@ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white&labelColor=12100E" alt="Medium" />
</a>
<a href="https://www.linkedin.com/in/ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0077B5" alt="LinkedIn" />
</a>
<a href="mailto:ojasshukla01@gmail.com" target="_blank">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=D14836" alt="Email" />
</a>
<a href="https://github.com/ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=181717" alt="GitHub" />
</a>

</div>

---

## Current Availability

<div align="center">

<table>
<tr>
<td width="25%" align="center">

### 💼 Full-time Roles
*Senior Data Engineering positions*

</td>
<td width="25%" align="center">

### 🤝 Consulting
*Contract and project-based work*

</td>
<td width="25%" align="center">

### ✍️ Writing
*Technical content and documentation*

</td>
<td width="25%" align="center">

### 🎓 Mentoring
*Knowledge sharing and guidance*

</td>
</tr>
</table>

### 📍 **Sydney, Australia** 🇦🇺

</div>

---

## Support My Work

<div align="center">

If you find my projects helpful or enjoy my content, consider supporting my work:

  <a href="https://buymeacoffee.com/ojasshuklav" target="_blank">
  <img src="https://img.shields.io/badge/-Buy%20me%20a%20coffee-ea4aaa?style=flat-square&logo=buy-me-a-coffee&logoColor=white" alt="Buy Me A Coffee"/>
</a>

*Your support helps me create more open-source projects and technical content!*

</div>

---

<div align="center">

> *"Excellence in data engineering is not just about building systems—it's about architecting solutions that scale, adapt, and deliver measurable business value."*

**Ojas Shukla** | Senior Data Engineer

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&duration=4000&pause=2000&color=00D4FF&center=true&vCenter=true&width=600&lines=Building+the+future+of+data+engineering;One+pipeline+at+a+time;Let's+connect+and+collaborate!" alt="Footer Animation" />

---

### 🎯 Quick Actions

<a href="mailto:ojasshukla01@gmail.com?subject=Data Engineering Collaboration&body=Hi Ojas, I'd like to discuss a potential collaboration opportunity." target="_blank">
  <img src="https://img.shields.io/badge/Send%20Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Send Email" />
</a>

<a href="https://www.linkedin.com/in/ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-Network-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" />
</a>

<a href="https://medium.com/@ojasshukla01" target="_blank">
  <img src="https://img.shields.io/badge/Read%20My%20Articles-Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Read Articles" />
</a>

</div>
