# Comprehensive AI Agent Skills & Tools Directory (Deep Research Edition)

This directory provides an exhaustive, structured overview of all available AI Agent Skills, Tools, and Plugins across the broader AI agent ecosystem in 2026. 

While "skills" (procedural logic) and "tools" (functional capabilities) are technically distinct, modern agent frameworks often use the terms interchangeably alongside "plugins." This document covers the global repositories, framework-specific tools, and a categorized master list of capabilities.

---

## 1. Global Skill Registries & Universal Protocols

The agent ecosystem has evolved from fragmented, framework-specific tools to universal protocols.

### 🌐 Model Context Protocol (MCP)
MCP has become the universal standard for providing skills and tools to agents. Instead of writing custom integrations, agents can connect to MCP servers.
*   **File & Desktop Servers:** `sqlite-mcp`, `postgres-mcp`, `github-mcp`, `filesystem-mcp`.
*   **Web & API Servers:** `slack-mcp`, `notion-mcp`, `google-drive-mcp`.
*   *(Note: For a full list of MCP servers, refer to the [MCP Directory 2.md](file:///c:/Users/Girish%20Lade/OneDrive/Desktop/MCP-Directory/MCP%20Directory%202.md))*

### 📚 Global Open-Source Registries
*   **[Awesome-Agent-Skills (VoltAgent/GitHub)](https://github.com/VoltAgent/awesome-agent-skills):** 1,000+ curated skills from Anthropic, Google, and Vercel.
*   **[Explainx.ai](https://www.explainx.ai/):** A search engine indexing over 10,000 vetted and ranked skills.
*   **[Skills.sh](https://skills.sh/):** A package manager-like registry hosting over 57,000 public skill entries (`SKILL.md` files).
*   **[OpenAgentSkill](https://www.openagentskill.com/):** Filters open-source skill candidates by GitHub quality and safety metrics.

---

## 2. The "Big 5" Agent Frameworks: Available Tools & Skills

Every major AI Agent framework provides a massive suite of pre-built tools. Here is what is available across the big 5 platforms.

### A. LangChain & LangGraph (Community Tools)
LangChain has the largest ecosystem of API wrappers and tools, primarily found in the `langchain-community` package.
*   **Search:** `TavilySearch`, `GoogleSearch`, `DuckDuckGoSearch`, `Wikipedia`, `ArXiv`.
*   **File & System:** `ListDirectoryTool`, `ReadFileTool`, `WriteFileTool`, `PythonREPLTool` (Code execution).
*   **Toolkits (Bundled Skills):** `SQLDatabaseToolkit`, `GitHubToolkit`, `JiraToolkit`, `GmailToolkit`, `Office365Toolkit`.
*   **Directory Link:** [LangChain Tool Integrations](https://python.langchain.com/docs/integrations/tools/)

### B. LlamaIndex & LlamaHub
LlamaHub is the central registry for connecting LLMs to external data (RAG) and APIs.
*   **Data Loaders (Readers):** Ingest data from `GoogleDocs`, `Notion`, `Slack`, `Discord`, `PDFs`, and local file directories.
*   **Agent Tools (ToolSpecs):** `OpenAPI`, `Gmail`, `GoogleCalendar`, `ElevenLabs`, `DatabaseQueries`.
*   **LlamaPacks:** Ready-to-use templates for common application patterns.
*   **Directory Link:** [LlamaHub](https://llamahub.ai/)

### C. CrewAI (`crewai-tools`)
CrewAI provides highly specialized tools designed for multi-agent workflows and role-based execution.
*   **Scraping & Browsing:** `ScrapeWebsiteTool`, `SeleniumScrapingTool`.
*   **Search & Research:** `SerperDevTool`, `EXASearchTool`.
*   **Database & Data:** `MySQLSearchTool`, `PGSearchTool`, `MongoDBVectorSearchTool`, `QdrantVectorSearchTool`.
*   **Document Analysis:** `PDFSearchTool`, `CSVSearchTool`, `JSONSearchTool`.
*   **Directory Link:** [crewai-tools Repository](https://github.com/crewAIInc/crewai-tools)

### D. AutoGen
Microsoft's AutoGen focuses heavily on secure code execution and conversable agents.
*   **Code Execution:** `PythonCodeExecutionTool` (Runs python securely in Docker).
*   **Search & RAG:** `LocalSearchTool` & `GlobalSearchTool` (for GraphRAG integration).
*   **API Interactions:** `FunctionTool` (Wraps any Python function), `HttpTool`, `LangChainToolAdapter` (imports LangChain tools).
*   **Directory Link:** [AutoGen Documentation](https://microsoft.github.io/autogen/)

### E. Semantic Kernel (Plugins)
Semantic Kernel treats skills as "Plugins" that are added to the agent's core engine.
*   **Core Plugins:** `TimePlugin` (date/time logic), `TextPlugin` (string manipulation), `HttpPlugin`, `MathPlugin`.
*   **Integration Plugins:** Bing Search, Microsoft Graph, OpenAPI-imported endpoints.
*   **Custom Functions:** Native C#/Python code decorated with `[KernelFunction]` / `@kernel_function`.

---

## 3. Categorized Master List of Agent Skills (Procedural Capabilities)

When agents use the tools listed above, they execute **Skills**. Here is an exhaustive list of the most popular procedural skills agents are configured to perform today.

### 🛠️ Software Engineering & Development
*   **`tdd-implementation`**: Write tests -> run tests (fail) -> write code -> run tests (pass).
*   **`code-reviewer`**: Analyze pull requests, check security constraints, enforce DRY (Don't Repeat Yourself) principles.
*   **`repo-scaffolder`**: Generate boilerplates, `package.json`, Dockerfiles, and CI/CD `.github/workflows`.
*   **`legacy-refactor`**: Traverse directory, locate deprecated syntax, and iteratively rewrite code while maintaining tests.
*   **`bug-hunter`**: Trace execution logs, identify stack traces, propose patches, and write regression tests.
*   **`doc-generator`**: Parse codebase structure and output `README.md`, `CONTRIBUTING.md`, and inline docstrings.
*   **`api-designer`**: Generate OpenAPI specifications based on natural language requirements.
*   **`ui-component-builder`**: Convert Figma designs or text descriptions into accessible React/Vue components.
*   **`db-migration-manager`**: Analyze schema changes and generate safe Prisma/Alembic migration scripts.

### ☁️ DevOps & Infrastructure
*   **`dockerize-app`**: Analyze dependencies and automatically generate optimized, multi-stage `Dockerfile` and `docker-compose.yml` configs.
*   **`k8s-manifest-builder`**: Generate standard Kubernetes deployments, ingress routes, and Helm charts.
*   **`log-analyzer`**: Fetch logs via API (AWS CloudWatch, Datadog), parse for anomalies, and summarize root causes.
*   **`terraform-planner`**: Read architecture requirements and draft HCL (Terraform) scripts for AWS/Azure/GCP.
*   **`incident-responder`**: Ping failing services, scale up instances via AWS CLI, and alert teams via Slack/PagerDuty.
*   **`cost-optimizer`**: Analyze AWS billing logs and suggest right-sizing for underutilized EC2/RDS instances.

### 📊 Data Analysis & Data Engineering
*   **`sql-query-generator`**: Read database schema, take user natural language request, and output complex JOINs/Aggregations.
*   **`csv-summarizer`**: Read `.csv` files locally, parse columns, detect anomalies, and output statistical profiles.
*   **`data-cleaner`**: Impute missing data, normalize date formats, and strip special characters from datasets.
*   **`viz-creator`**: Write Python (matplotlib/seaborn) or React components to generate charts based on provided data.
*   **`web-scraper-pipeline`**: Navigate to URL, extract DOM text, convert to markdown, and store in vector DB.
*   **`etl-pipeline-builder`**: Generate Airflow or Prefect DAGs to move and transform data between databases.

### 🛡️ Security & Compliance
*   **`threat-discovery`**: Run static analysis on codebases looking for OWASP Top 10 vulnerabilities.
*   **`secret-scanner`**: Search git history and active files for hardcoded API keys, JWTs, and passwords.
*   **`compliance-checker`**: Audit configuration files against GDPR, SOC2, or HIPAA requirements.
*   **`phishing-analyzer`**: Parse email headers and URLs in sandboxed environments to detect malicious intent.
*   **`iam-policy-generator`**: Generate least-privilege AWS IAM JSON policies based on application needs.

### ✍️ Content & Marketing
*   **`seo-optimizer`**: Read markdown/HTML, inject LSI keywords, generate meta descriptions, and check readability scores.
*   **`brand-voice-enforcer`**: Review draft text against a style guide (e.g., "professional but conversational") and rewrite.
*   **`technical-writer`**: Take raw JSON/API responses and format them into readable Swagger/OpenAPI docs or blog tutorials.
*   **`social-media-scheduler`**: Draft thread content, format for Twitter/LinkedIn, and interact with scheduling APIs.
*   **`email-campaign-manager`**: Generate A/B test variations for cold outreach and format for Mailchimp/HubSpot.

### 💰 Finance & Accounting (NEW)
*   **`invoice-processor`**: Read PDFs/images via OCR, extract line items, and format as JSON for QuickBooks/Xero.
*   **`expense-categorizer`**: Analyze bank statement CSVs and automatically tag rows (e.g., "Software", "Travel") based on ML models.
*   **`financial-forecaster`**: Take historical revenue data and generate predictive ARIMA models in Python.
*   **`tax-compliance-auditor`**: Review transaction logs against local tax rules to flag missing VAT/GST deductions.

### 🤝 Customer Support & Sales (NEW)
*   **`ticket-triage`**: Read incoming Zendesk/Jira tickets, assign priority levels, and route to the correct engineering department.
*   **`crm-updater`**: Extract action items from meeting transcripts and update Salesforce/HubSpot deal stages automatically.
*   **`refund-processor`**: Verify Stripe transaction IDs and execute partial/full refunds based on company policy rules.
*   **`sentiment-analyzer`**: Scan daily support emails and generate a mood/sentiment report for the customer success team.

### 🧑‍💼 Human Resources & Recruiting (NEW)
*   **`resume-screener`**: Parse PDFs of candidate resumes and score them against the skills required in a job description.
*   **`interview-scheduler`**: Read Google Calendar availability across multiple team members and draft scheduling emails.
*   **`onboarding-coordinator`**: Automatically generate Slack accounts, email addresses, and Jira access for new hires.
*   **`policy-qna-bot`**: Answer employee questions by vector-searching the company employee handbook (RAG).

### 🎓 Research & Academia (NEW)
*   **`arxiv-literature-reviewer`**: Search ArXiv for a topic, download the top 10 PDFs, and generate a synthesized literature review.
*   **`citation-formatter`**: Take raw URLs and output properly formatted APA, MLA, or Chicago style bibliography entries.
*   **`hypothesis-tester`**: Write R or Python pandas scripts to perform ANOVA or T-tests on provided experimental data.
*   **`grant-proposal-drafter`**: Format scientific findings into structured grant applications adhering to NSF/NIH guidelines.

### ⚡ Productivity & Personal Assistance (NEW)
*   **`email-inbox-zero`**: Categorize unread Gmail messages, draft replies for routine questions, and archive newsletters.
*   **`travel-itinerary-planner`**: Query flight/hotel APIs, check weather data, and generate a day-by-day markdown schedule.
*   **`meeting-summarizer`**: Take raw `.vtt` or `.txt` transcripts and extract key decisions, action items, and owners.

### 🏠 IoT & Smart Home Automation (NEW)
*   **`home-assistant-routine-builder`**: Generate YAML automations for Home Assistant (e.g., "if motion detected after 10 PM, turn on lights to 20%").
*   **`energy-monitor`**: Read smart plug wattage data and suggest routines to reduce vampire power draw.

---

## 4. How to Create and Integrate Your Own Skills

If the exact skill you need isn't available in the directories above, you can build your own.

### The Universal `SKILL.md` Format
To create a portable skill for your agent (like Claude Code, Cursor, or a local terminal agent), create a folder with a `SKILL.md` file:

```markdown
---
name: my-custom-skill
description: Triggers when the user asks to summarize a PDF.
required_tools: [read_file, write_to_file]
---

# Instructions
1. Use `read_file` to open the PDF.
2. Extract the text and summarize the key findings into bullet points.
3. Use `write_to_file` to save the summary as `summary.md`.
```

### Safety and Execution Limits
*   **Vetting:** Always review open-source skills or tools before allowing an agent to use them.
*   **Isolation:** Run code-execution tools (like AutoGen's Python Code tool) inside Docker.
*   **Human-in-the-Loop:** For tools that modify infrastructure, push code to Git, or send emails, configure the agent to require manual user approval before execution.
