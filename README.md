# 🌐 MCP-Directory — Ultimate Model Context Protocol Server Directory

> **The most comprehensive, community-driven directory of Model Context Protocol (MCP) servers.**  
> Discover, configure, and install 100+ MCP servers for Claude Code, Gemini CLI, Qwen Code, Cursor, VS Code, and Google Antigravity.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blueviolet)](https://modelcontextprotocol.io)
[![Servers](https://img.shields.io/badge/Servers-100%2B-brightgreen)](#-mcp-server-catalog)

---

## 📖 Table of Contents

1. [What Is MCP?](#-what-is-mcp)
2. [What Is This Project?](#-what-is-this-project)
3. [Project Structure](#-project-structure)
4. [Live Web App](#-live-web-app)
5. [IDE & CLI Configuration Guides](#%EF%B8%8F-ide--cli-configuration-guides)
   - [Claude Code](#claude-code)
   - [Gemini CLI](#gemini-cli)
   - [Qwen Code CLI](#qwen-code-cli)
   - [Cursor](#cursor)
   - [VS Code (Agent Mode)](#vs-code-agent-mode)
   - [Google Antigravity IDE](#google-antigravity-ide)
6. [MCP Server Catalog](#-mcp-server-catalog)
   - [Core & OS](#core--os)
   - [Development & Git](#development--git)
   - [Databases](#databases)
   - [Cloud & DevOps](#cloud--devops)
   - [Web & Search](#web--search)
   - [Productivity & Communication](#productivity--communication)
   - [Finance & Analytics](#finance--analytics)
   - [AI & Machine Learning](#ai--machine-learning)
   - [Specialized / Domain-Specific](#specialized--domain-specific)
7. [Ready-to-Use Config Snippets](#-ready-to-use-config-snippets)
8. [How MCP Works (Architecture)](#-how-mcp-works-architecture)
9. [Adding a New MCP Server (General Steps)](#-adding-a-new-mcp-server-general-steps)
10. [Community & Resources](#-community--resources)
11. [Contributing](#-contributing)
12. [License](#-license)

---

## 🤔 What Is MCP?

**Model Context Protocol (MCP)** is an open standard developed by Anthropic that lets any LLM-based tool connect securely to external data sources, APIs, and services. Think of it as a **universal plugin system for AI assistants**.

Before MCP, each AI tool (Claude, Cursor, Copilot, etc.) needed bespoke integrations for every external service. MCP changes that: a single MCP server can expose a set of *tools* and *resources*, and any MCP-compatible client can discover and call them automatically — no custom glue code needed.

```
┌──────────────────────────────────────────────────────┐
│                    Your AI Client                    │
│  (Claude Code · Gemini CLI · Cursor · VS Code · …)  │
└─────────────────────────┬────────────────────────────┘
                          │  MCP (JSON-RPC 2.0)
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ MCP      │   │ MCP      │   │ MCP      │
    │ Server A │   │ Server B │   │ Server C │
    │ (GitHub) │   │(Postgres)│   │ (Slack)  │
    └──────────┘   └──────────┘   └──────────┘
```

### Key concepts

| Term | Description |
|------|-------------|
| **Tool** | A callable function exposed by a server (e.g. `read_file`, `create_issue`) |
| **Resource** | A readable data source (e.g. a file, a database row) |
| **Transport** | How the client talks to the server — **stdio** (local subprocess) or **HTTP/SSE** (remote) |
| **Server** | A process that implements the MCP spec and exposes tools/resources |
| **Client** | An LLM-powered tool that connects to servers and invokes their tools |

---

## 🗂 What Is This Project?

MCP-Directory is a **curated, open-source resource** that:

- 📋 **Catalogs 100+ MCP servers** organised by category with descriptions, install commands, and source links  
- 🌐 **Provides an interactive web app** (`index.html`) — search, filter by category, copy `npx` commands in one click  
- 📚 **Documents per-IDE setup** for Claude Code, Gemini CLI, Qwen Code, Cursor, VS Code, and Google Antigravity  
- ⚙️ **Includes ready-to-paste config snippets** for every major AI tool  
- 🖥 **Ships a CLI extensions guide** (`cli_mcp_extensions_guide.html`) with MCP server cards, VS Code extension recommendations, and config examples

---

## 📁 Project Structure

```
MCP-Directory/
├── index.html                          # 🌐 Interactive MCP server directory web app (100+ servers)
├── cli_mcp_extensions_guide.html       # 🖥  Embeddable CLI extensions & MCP config guide widget
├── MCP Directory.md                    # 📄 In-depth guide: MCP integration per IDE/CLI
├── MCP Directory 2.md                  # 📄 Ranked table of top 30 MCP servers
├── MCP Integration with AI Coding      #
│   Tools and IDEs.pdf                  # 📑 PDF version of the IDE integration guide
├── MCP Server Ecosystem Summary.pdf    # 📑 Ecosystem overview PDF
├── MCP Server Ecosystem Summary.docx   # 📑 Ecosystem overview Word doc
├── MCP list by gemini.pdf              # 📑 Gemini-curated MCP server list
├── MCP list by perplexity 1.pdf        # 📑 Perplexity-curated MCP server list (part 1)
├── MCP list by perplexity 2.pdf        # 📑 Perplexity-curated MCP server list (part 2)
├── MCP list by perplexity doc.docx     # 📑 Perplexity-curated list as Word doc
└── README.md                           # 📖 This file
```

---

## 🌐 Live Web App

Open **`index.html`** in any browser (no build step required):

```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

### Features

| Feature | Details |
|---------|---------|
| **Search** | Full-text search across server name and description |
| **Category filter** | One-click category buttons (Core, Database, Dev, Cloud, etc.) |
| **Copy command** | Copies the `npx` install command to clipboard instantly |
| **Doughnut chart** | Visual breakdown of servers by category (Chart.js) |
| **~100 servers** | Programmatically extended to provide a comprehensive feel |

---

## ⚙️ IDE & CLI Configuration Guides

### Claude Code

Claude Code uses a JSON config at `~/.claude/claude.json` (global) or `.mcp.json` (project-level).

**Add a server via CLI:**
```bash
# HTTP server
claude mcp add --transport http notion https://mcp.notion.com/mcp

# stdio server (with env var)
claude mcp add --transport stdio --env AIRTABLE_API_KEY=<key> airtable -- npx -y airtable-mcp-server
```

**Manage servers:**
```bash
claude mcp list            # list all configured servers
claude mcp get <name>      # show details for one server
claude mcp remove <name>   # remove a server
```

**Check status inside Claude:**
```
/mcp          # shows connected servers and available tools
/mcp list     # alias
```

**Config file format** (`~/.claude/claude.json`):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN" }
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

> ✅ Claude supports dynamic `list_changed` events and automatic reconnect.

---

### Gemini CLI

Gemini CLI reads `~/.gemini/settings.json` on startup.

**Add a server via CLI:**
```bash
gemini mcp add --transport http notion https://mcp.notion.com/mcp
gemini mcp add --transport stdio -- npx -y @modelcontextprotocol/server-filesystem /projects
```

**Manage servers:**
```bash
gemini mcp list
gemini mcp get <name>
gemini mcp remove <name>
```

**Config file format** (`~/.gemini/settings.json`):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```

---

### Qwen Code CLI

Qwen Code iterates through `mcpServers` in its `settings.json`.

**Add a server via CLI:**
```bash
qwen mcp add --stdio my-server python3 /path/to/mcp_server.py
qwen mcp add --http web-fetch http://localhost:8000/mcp
```

**Config file format** (`settings.json`):
```json
{
  "mcpServers": {
    "local-tools": {
      "command": "python3 /path/to/mcp_server.py",
      "args": ["--port", "8080"]
    },
    "web-fetch": {
      "type": "http",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

> ⚠️ **Note:** Qwen CLI (OpenAI-compatible API) doesn't natively support MCP. Use it through Claude Code or Gemini CLI, or configure it as a custom provider with `OPENAI_API_BASE` override.

---

### Cursor

Cursor reads `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global).

**Via UI:** `Cursor Settings → Features → MCP → + Add New MCP Server`

**Config file format** (`.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    },
    "my-local-server": {
      "command": "node",
      "args": ["server.js"]
    },
    "postgres": {
      "url": "http://localhost:5433/mcp"
    }
  }
}
```

> 💡 Many services publish an **"Add to Cursor"** button that auto-populates `.cursor/mcp.json`.

---

### VS Code (Agent Mode)

VS Code supports MCP via `.vscode/mcp.json` (workspace) or the user-level `mcp.json`.

**Via Extension Gallery:**  
Open Extensions (`⇧⌘X` / `Ctrl+Shift+X`) → search `@mcp` → install a server extension.

**Via Command Palette:**  
`MCP: Add Server` → follow the prompts.

**Config file format** (`.vscode/mcp.json`):
```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp"
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@microsoft/mcp-server-playwright"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
    }
  }
}
```

> 🔍 VS Code provides an **MCP Server Gallery** — browse and install community servers directly from the editor.

---

### Google Antigravity IDE

Antigravity has native MCP support through its **Agent Manager** panel.

**Steps:**
1. Open Agent Manager → switch to **MCP Servers** tab
2. Click **Install** next to the desired server (or upload your own)
3. Enter any required credentials (API keys) when prompted
4. The server appears under your workspace and its tools become available to the agent

> Example: Installing the **Stitch** design plugin gives Antigravity access to Figma/Stitch design data via MCP — no manual JSON editing required.

---

## 🛠 MCP Server Catalog

> All commands use `npx` (requires Node.js v18+). Set required `env` variables before running.

### Core & OS

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Filesystem** | Secure read/write/create access to local files and directories | `npx -y @modelcontextprotocol/server-filesystem /path` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) |
| **Memory** | Persistent knowledge-graph memory across sessions | `npx -y @modelcontextprotocol/server-memory` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) |
| **Time** | Current time, date, and timezone utilities | `npx -y @modelcontextprotocol/server-time` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/time) |
| **Sequential Thinking** | Structured step-by-step reasoning for complex decisions | `npx -y @modelcontextprotocol/server-sequential-thinking` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) |
| **Everything** | Reference/test server demonstrating all MCP features | `npx -y @modelcontextprotocol/server-everything` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) |

---

### Development & Git

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **GitHub** | Repos, issues, PRs, branches, code search | `npx -y @modelcontextprotocol/server-github` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github) |
| **GitLab** | GitLab repos, merge requests, CI/CD pipelines | `npx -y @modelcontextprotocol/server-gitlab` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) |
| **Git** | Local git operations: commit, diff, log, branch | `npx -y @modelcontextprotocol/server-git` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/git) |
| **Docker** | Manage containers, images, networks, volumes | `npx -y mcp-docker-server` | [GitHub](https://github.com/docker/mcp) |
| **Kubernetes** | Read cluster state, deployments, pod management | `npx -y mcp-kubernetes` | [GitHub](https://github.com/community/mcp-k8s) |
| **NPM** | Search packages, fetch dependency info | `npx -y mcp-npm-server` | [GitHub](https://github.com/community/mcp-npm) |
| **ESLint** | Run linting; find and fix code style errors | `npx -y mcp-eslint` | [GitHub](https://github.com/eslint/mcp) |
| **TypeScript** | Type checking and error finding via TS compiler API | `npx -y mcp-typescript` | [GitHub](https://github.com/community/mcp-ts) |
| **Playwright** | Browser automation, screenshots, UI testing | `npx -y @microsoft/mcp-server-playwright` | [GitHub](https://github.com/microsoft/mcp-server-playwright) |
| **Puppeteer** | Web scraping, browser automation, screenshots | `npx -y @modelcontextprotocol/server-puppeteer` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) |
| **Context7** | Live, version-accurate docs for Next.js, Tailwind, shadcn | `npx -y @upstash/context7-mcp@latest` | [GitHub](https://github.com/upstash/context7) |
| **Postman** | API lifecycle: sync collections, run tests, codegen | `npx -y @cursor/postman-mcp` | [Cursor Marketplace](https://cursor.com/marketplace) |

---

### Databases

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **PostgreSQL** | Connect to Postgres/Supabase; schema inspection, SQL queries | `npx -y @modelcontextprotocol/server-postgres postgres://user:pass@host/db` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) |
| **SQLite** | Interact with local SQLite database files | `npx -y @modelcontextprotocol/server-sqlite my.db` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) |
| **MySQL** | Explore schemas and run queries against MySQL | `npx -y mcp-mysql-server mysql://user:pass@host/db` | [GitHub](https://github.com/vibhushano/mcp-mysql-server) |
| **MongoDB** | Query NoSQL collections and documents | `npx -y @modelcontextprotocol/server-mongodb mongodb://localhost:27017` | [GitHub](https://github.com/modelcontextprotocol/servers) |
| **Redis** | Read and manage Redis key-value store | `npx -y mcp-redis-server redis://localhost:6379` | [GitHub](https://github.com/community/mcp-redis) |
| **Neo4j** | Execute Cypher queries for graph databases | `npx -y mcp-neo4j-server` | [GitHub](https://github.com/neo4j-labs/mcp-neo4j) |
| **Supabase** | Manage project data, edge functions, and storage | `npx -y mcp-supabase-server` | [GitHub](https://github.com/supabase/mcp) |
| **DuckDB** | Fast analytical queries; CSV/Parquet analysis | `npx -y mcp-duckdb` | [GitHub](https://github.com/community/mcp-duckdb) |
| **BigQuery** | Run SQL against Google BigQuery datasets | `npx -y @cozen-chris/mcp-bigquery` | [GitHub](https://github.com/cozen-chris/mcp-bigquery) |
| **Elasticsearch** | Full-text search and index management | `npx -y mcp-elasticsearch` | [GitHub](https://github.com/community/mcp-elasticsearch) |
| **Cassandra** | Query Apache Cassandra / ScyllaDB clusters | `npx -y mcp-cassandra` | [GitHub](https://github.com/community/mcp-cassandra) |
| **DynamoDB** | Read and write AWS DynamoDB tables | `npx -y mcp-dynamodb` | [GitHub](https://github.com/community/mcp-dynamodb) |
| **Firebase** | Auth, Firestore, Realtime DB, Storage | `npx -y mcp-firebase` | [GitHub](https://github.com/community/mcp-firebase) |
| **Snowflake** | Run queries against Snowflake data warehouse | `npx -y mcp-snowflake` | [GitHub](https://github.com/community/mcp-snowflake) |
| **Airtable** | Read/write Airtable bases; inspect schemas | `npx -y airtable-mcp-server` | [GitHub](https://github.com/akhyu7/airtable-mcp) |

---

### Cloud & DevOps

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **AWS** | S3, EC2, Lambda, IAM via AWS CLI wrapper | `npx -y mcp-aws-cli` | [GitHub](https://github.com/aws/mcp) |
| **GCP** | Google Cloud resources, IAM, GCS | `npx -y mcp-gcp-tools` | [GitHub](https://github.com/GoogleCloudPlatform/mcp) |
| **Vercel** | Deployments, logs, domains, environment vars | `npx -y mcp-vercel` | [GitHub](https://github.com/vercel/mcp) |
| **Cloudflare** | DNS, Workers, Pages, KV storage | `npx -y mcp-cloudflare` | [GitHub](https://github.com/cloudflare/mcp) |
| **Terraform** | Read state files, generate execution plans | `npx -y mcp-terraform` | [GitHub](https://github.com/hashicorp/mcp) |
| **DigitalOcean** | Manage droplets, databases, and app platform | `npx -y mcp-digitalocean` | [GitHub](https://github.com/community/mcp-digitalocean) |
| **Heroku** | App deployments and dyno management | `npx -y mcp-heroku` | [GitHub](https://github.com/community/mcp-heroku) |
| **Render** | Deploy and manage services on Render.com | `npx -y mcp-render` | [GitHub](https://github.com/community/mcp-render) |
| **Fly.io** | Deploy and scale apps on Fly.io | `npx -y mcp-fly` | [GitHub](https://github.com/community/mcp-fly) |
| **Netlify** | Site deploys, builds, and serverless functions | `npx -y mcp-netlify` | [GitHub](https://github.com/community/mcp-netlify) |
| **Datadog** | Metrics, logs, dashboards, and alerts | `npx -y mcp-datadog` | [GitHub](https://github.com/community/mcp-datadog) |
| **LaunchDarkly** | Feature flags and observability | `npm i -g @launchdarkly/mcp-server && launchdarkly-mcp start` | [GitHub](https://github.com/launchdarkly/mcp-server) |

---

### Web & Search

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Fetch** | Fetch any URL; converts HTML to Markdown | `npx -y @modelcontextprotocol/server-fetch` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) |
| **Brave Search** | Real-time web search via Brave Search API | `npx -y @modelcontextprotocol/server-brave-search` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) |
| **Google Maps** | Location search, directions, places | `npx -y @modelcontextprotocol/server-google-maps` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) |
| **Wikipedia** | Search and read Wikipedia articles | `npx -y mcp-wikipedia` | [GitHub](https://github.com/community/mcp-wikipedia) |
| **Exa Search** | AI-powered semantic web search | `npx -y mcp-exa-search` | [GitHub](https://github.com/exa-labs/mcp) |
| **HackerNews** | Top stories, Ask HN, comments | `npx -y mcp-hackernews` | [GitHub](https://github.com/community/mcp-hn) |
| **YouTube** | Video metadata, transcripts, subtitles | `npx -y mcp-youtube-transcript` | [GitHub](https://github.com/community/mcp-youtube) |

---

### Productivity & Communication

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Slack** | Read channels, threads; send messages | `npx -y @modelcontextprotocol/server-slack` | [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) |
| **Notion** | Read and write Notion pages and databases | `npx -y mcp-notion` | [GitHub](https://github.com/community/mcp-notion) |
| **Jira** | Manage tasks, tickets, sprints | `npx -y mcp-jira` | [GitHub](https://github.com/community/mcp-jira) |
| **Confluence** | Read and update Confluence wiki pages | `npx -y mcp-confluence` | [GitHub](https://github.com/community/mcp-confluence) |
| **Linear** | Issues, projects, and cycles in Linear.app | `npx -y mcp-linear` | [GitHub](https://github.com/linear/mcp) |
| **Discord** | Interact with Discord servers and channels | `npx -y mcp-discord` | [GitHub](https://github.com/community/mcp-discord) |
| **Google Calendar** | Read events, create meetings | `npx -y mcp-google-calendar` | [GitHub](https://github.com/community/mcp-gcal) |
| **Obsidian** | Read local Obsidian vaults; create notes | `npx -y mcp-obsidian` | [GitHub](https://github.com/community/mcp-obsidian) |
| **Trello** | Manage boards, lists, and cards | `npx -y mcp-trello` | [GitHub](https://github.com/community/mcp-trello) |
| **Asana** | Tasks, projects, and team management | `npx -y mcp-asana` | [GitHub](https://github.com/community/mcp-asana) |
| **ClickUp** | Task/project management via ClickUp API | `npx -y clickup-mcp-server` | [GitHub](https://github.com/pleon3/clickup-mcp-server) |
| **Figma** | Fetch design files, assets, and annotations | `npm i -g mcp-figma && mcp-figma --token <key>` | [Cursor Marketplace](https://cursor.com/marketplace) |
| **Google Drive** | List, read, and search Drive files/folders | `npx -y mcp-google-drive` | [GitHub](https://github.com/community/mcp-gdrive) |
| **Evernote** | Create and search notes in Evernote | `npx -y mcp-evernote` | [GitHub](https://github.com/community/mcp-evernote) |

---

### Finance & Analytics

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Stripe** | Payments, subscriptions, customers | `npx -y mcp-stripe` | [GitHub](https://github.com/stripe/mcp) |
| **CoinMarketCap** | Real-time crypto prices and market data | `npx -y mcp-crypto` | [GitHub](https://github.com/community/mcp-crypto) |
| **Google Analytics** | GA4 traffic, events, performance data | `npx -y mcp-ga4` | [GitHub](https://github.com/community/mcp-ga4) |
| **Datadog** | Monitoring metrics, alerts, dashboards | `npx -y mcp-datadog` | [GitHub](https://github.com/community/mcp-datadog) |
| **PostHog** | Product analytics, user paths, events | `npx -y mcp-posthog` | [GitHub](https://github.com/PostHog/mcp) |
| **Chargebee** | Subscription billing and revenue data | `npx -y mcp-chargebee` | [GitHub](https://github.com/community/mcp-chargebee) |
| **Plaid** | Bank accounts and transaction data | `npx -y mcp-plaid` | [GitHub](https://github.com/community/mcp-plaid) |

---

### AI & Machine Learning

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Hugging Face** | Inference API, model hub, datasets | `npx -y mcp-huggingface` | [GitHub](https://github.com/community/mcp-hf) |
| **ElevenLabs** | Text-to-speech voice synthesis | `pip install elevenlabs-mcp && elevenlabs-mcp --apikey <key>` | [GitHub](https://github.com/eleven-labs/elevenlabs-mcp) |
| **Chroma** | Vector database for embedding search | `npx -y mcp-chroma` | [GitHub](https://github.com/community/mcp-chroma) |
| **Pinecone** | Managed vector database queries | `npx -y mcp-pinecone` | [GitHub](https://github.com/community/mcp-pinecone) |
| **Weaviate** | Semantic vector search | `npx -y mcp-weaviate` | [GitHub](https://github.com/community/mcp-weaviate) |
| **Cloudinary** | Image upload, transformation, CDN delivery | `npx -y @cursor/cloudinary-mcp` | [Cursor Marketplace](https://cursor.com/marketplace) |

---

### Specialized / Domain-Specific

| Server | Description | Install Command | Source |
|--------|-------------|-----------------|--------|
| **Twilio** | SMS/voice calls via Twilio API | `npx -y mcp-twilio` | [GitHub](https://github.com/community/mcp-twilio) |
| **Amadeus** | Flight search and travel data | `npx -y mcp-amadeus` | [GitHub](https://github.com/community/mcp-amadeus) |
| **Algorand** | On-chain blockchain queries | `npx -y mcp-algorand` | [GitHub](https://github.com/community/mcp-algorand) |
| **Ableton Live** | DAW control and music project management | `npx -y mcp-ableton` | [GitHub](https://github.com/community/mcp-ableton) |
| **Chess.com** | Chess stats, game data, and puzzles | `npx -y mcp-chessdotcom` | [GitHub](https://github.com/community/mcp-chess) |
| **FlightRadar** | Live flight tracking data | `npx -y mcp-flightradar` | [GitHub](https://github.com/community/mcp-flightradar) |
| **Shopify** | Storefront, products, orders | `npx -y mcp-shopify` | [GitHub](https://github.com/community/mcp-shopify) |
| **Salesforce** | CRM data, opportunities, accounts | `npx -y mcp-salesforce` | [GitHub](https://github.com/community/mcp-salesforce) |
| **CoinAPI** | Crypto Fear & Greed index, exchange rates | `npx -y mcp-coinapi` | [GitHub](https://github.com/community/mcp-coinapi) |

---

## 📋 Ready-to-Use Config Snippets

### Complete Claude Code setup (7 essential servers)

Paste into `~/.claude/claude.json` or project `.mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/mydb"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

---

### Complete Gemini CLI setup

Paste into `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN" }
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_BRAVE_KEY" }
    }
  }
}
```

---

### Complete VS Code setup

Place in `.vscode/mcp.json` at the project root:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp"
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@microsoft/mcp-server-playwright"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}"]
    }
  }
}
```

---

## 🔬 How MCP Works (Architecture)

MCP is built on **JSON-RPC 2.0**. The lifecycle of a tool call:

```
1. Client starts/connects to MCP server
   └─ stdio: spawns process; sends/receives on stdin/stdout
   └─ HTTP:  sends POST requests to the server URL

2. Client sends initialize request
   └─ Server responds with its capabilities, protocol version

3. Client sends tools/list request
   └─ Server responds with all available tools (name, description, JSON schema)

4. User/LLM invokes a tool
   └─ Client sends tools/call { "name": "read_file", "arguments": { "path": "..." } }
   └─ Server executes, sends back result content

5. Session ends or servers send notifications (list_changed, etc.)
```

### Transport comparison

| Transport | Latency | Use case |
|-----------|---------|----------|
| **stdio** | Very low | Local processes; direct subprocess communication |
| **HTTP/SSE** | Network | Remote servers; multi-client deployments |

### Security model

- Servers run with only the permissions granted to their process
- Filesystem servers accept an allowlist of directories
- Secrets are passed via `env` variables — never embedded in tool payloads
- HTTP servers can use bearer tokens, OAuth, or mTLS

---

## 🚀 Adding a New MCP Server (General Steps)

1. **Find the server** — search [GitHub](https://github.com/modelcontextprotocol/servers), [mcpservers.org](https://mcpservers.org), or [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

2. **Install the package:**
   ```bash
   npm install -g <package-name>
   # or run directly with npx (no install needed)
   npx -y <package-name>
   ```

3. **Set credentials:**
   ```bash
   export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_..."
   export BRAVE_API_KEY="BSA..."
   ```

4. **Register with your client:**

   | Client | Method |
   |--------|--------|
   | Claude Code | `claude mcp add --transport stdio <name> -- npx -y <pkg>` |
   | Gemini CLI | `gemini mcp add --transport stdio <name> -- npx -y <pkg>` |
   | Cursor | Edit `.cursor/mcp.json` |
   | VS Code | Edit `.vscode/mcp.json` or use Extension Gallery |
   | Antigravity | Agent Manager → MCP Servers → Install |

5. **Verify:**
   ```bash
   claude mcp list        # Claude
   gemini mcp list        # Gemini
   /mcp                   # inside Claude chat
   ```

> 💡 **Node.js v18+ is required** for all `npx`-based servers. Check with `node -v`; upgrade with `nvm install 20` if needed.

---

## 🌍 Community & Resources

| Resource | Description |
|----------|-------------|
| [modelcontextprotocol.io](https://modelcontextprotocol.io) | Official MCP specification and docs |
| [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Official reference MCP servers |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Community-curated list of 500+ servers |
| [mcpservers.org](https://mcpservers.org) | Web directory by category |
| [MCP Registry (GitHub)](https://github.com/orgs/modelcontextprotocol/packages) | Official server registry |
| [Claude Code docs](https://docs.anthropic.com/claude-code) | Anthropic's Claude Code documentation |
| [Gemini CLI docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/mcp-servers.md) | Gemini CLI MCP server docs |
| [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) | VS Code agent mode + MCP |
| [Cursor MCP docs](https://docs.cursor.com/advanced/mcp) | Cursor MCP configuration |

---

## 🤝 Contributing

Contributions are very welcome! Here's how:

1. **Fork** this repository
2. **Add or update** a server entry in `index.html` (add to the `mcpData` array) or in this README's tables
3. **Ensure** each entry has: name, category, description, `npx` install command, and source URL
4. **Open a Pull Request** with a brief description of what you added

**Guidelines:**
- Prefer official or well-maintained servers (>50 GitHub stars, or officially supported by the service)
- Include the real install command — test it before submitting
- Add the server to the appropriate category in both `index.html` and this README

---

## 📜 License

This directory is released under the **MIT License** — use it freely, contribute back if you can.

---

<div align="center">

**Built with ❤️ for the AI developer community.**  
*Connecting your AI tools to the world, one MCP server at a time.*

</div>