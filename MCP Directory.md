# MCP Integration with AI Coding Tools and IDEs

The **Model Context Protocol (MCP)** is an open standard that lets LLM-based tools (like Qwen Code, Gemini CLI, Claude Code, Cursor, Antigravity, VS Code, etc.) connect to external data and services. In practice, each tool can be configured to call one or more MCP servers, which “expose” APIs or resources to the LLM agent【1†L294-L302】【3†L346-L354】. For example, Qwen and Gemini CLIs use a `settings.json` file with an `mcpServers` section to list servers, while Claude Code provides `claude mcp add/list/remove` commands【44†L12-L15】【16†L175-L183】. Once configured, the AI can use the server’s tools (e.g. query a database, call a cloud API, fetch files) as if they were built into the assistant. 

## Qwen Code CLI Integration

In Qwen Code (Qwen CLI), you configure MCP servers via the `mcpServers` field in `settings.json`. For example: 

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

This tells Qwen to launch `mcp_server.py` as a local STDIO server and to connect to an HTTP server on port 8000.  Qwen Code’s docs explain that the CLI “iterates through configured servers from your `settings.json` `mcpServers` configuration” and connects over the appropriate transport【44†L12-L15】.  The CLI also supports commands like `qwen mcp add --stdio` or `--http` to automate adding entries (with scope flags for user/global config)【44†L49-L58】. Once running, Qwen can discover and invoke the server’s tools during a coding session.

## Gemini CLI Integration

Gemini CLI uses a very similar mechanism.  In your Gemini CLI `settings.json`, add an `mcpServers` object with each server’s details. For example, Gemini’s docs show:

```json
{
  "mcpServers": {
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    },
    "local-scripts": {
      "command": "node",
      "args": ["server.js"]
    }
  }
}
``` 

Gemini then discovers and connects to those servers when started. Alternatively, use the CLI commands `gemini mcp add --transport http <name> <url>` or `--transport stdio -- <command>` to add servers interactively【5†L443-L452】. Once added, you can list (`gemini mcp list`), view (`gemini mcp get <name>`), or remove (`gemini mcp remove <name>`) servers. In short, Gemini CLI’s integration is handled via its `mcpServers` settings just like Qwen’s【5†L443-L452】.

## Claude Code Integration

Anthropic’s **Claude Code** (Claude Desktop) likewise supports MCP.  You register servers using `claude mcp add` commands. For example, the Claude docs show:

```
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport stdio --env AIRTABLE_API_KEY=KEY airtable -- npx -y airtable-mcp-server
``` 

This adds an HTTP server named “notion” and a local stdio server named “airtable”【16†L175-L183】. Claude then auto-discovers the server’s tools. You can manage servers with `claude mcp list`, `claude mcp get`, and `claude mcp remove`【16†L231-L239】, or use the `/mcp` slash command inside a Claude chat to check status. Claude Code supports dynamic updates (`list_changed` events) and automatic reconnect, making it easy to plug in services like Notion, Airtable, GitHub, etc.【16†L231-L239】. 

## Cursor CLI Integration

Cursor’s Agent Mode uses MCP in much the same way. The Cursor CLI stores MCP configs in `.cursor/mcp.json`. You can either click “Add to Cursor” links (in services’ docs) or edit this JSON manually. A typical snippet might be:

```json
{
  "mcpServers": {
    "my-server": {
      "url": "http://localhost:3000/mcp",
      "headers": {
        "API_KEY": "xxxx"
      }
    }
  }
}
``` 

This example is drawn from Cursor’s docs【29†L159-L168】. Cursor also allows installing community servers via its UI: each listed integration has an “Add to Cursor” button that populates this JSON. In your project, Cursor reads `.cursor/mcp.json` on startup and connects to each server over HTTP or stdio (Cursor supports both transports)【29†L159-L168】【29†L269-L272】. After configuration, you can invoke the server’s tools directly from the Cursor command line (e.g. `/tool help`) or let the agent use them during a `/build` task.

## Google Antigravity IDE Integration

The new Google **Antigravity** IDE has built-in MCP support via its Agent Manager. Inside Antigravity, open the Agent Manager panel, switch to the **MCP Servers** view, and click “Install” on a desired server from the directory or upload one. For example, the Stitch design tool has an MCP plugin. After adding, Antigravity will prompt for any credentials (API keys) and then list the server under your workspace.  The Antigravity docs note: *“Antigravity supports the Model Context Protocol (MCP), a standard that allows the editor to securely connect to your local tools, databases, and external services.”*  As shown in Google’s Stitch-to-code codelab, you simply search for “Stitch” (or another service) and click **Install**, then paste in your API key【21†L163-L172】【21†L173-L181】. Once configured, the Antigravity agent can fetch external context (like Figma/Stitch design data, databases, etc.) on demand, thanks to MCP.

## Visual Studio Code Integration

VS Code’s Agent Mode/Chat UI also supports MCP servers. You can install servers in two ways:  

- **Extension Gallery:** Open Extensions (⇧⌘X) and search for `@mcp`. Install a server extension (e.g. Playwright, GitHub) into your profile or workspace【23†L492-L502】. VS Code will then auto-start the server when you open the chat.  

- **Manual config:** Create or edit a file `.vscode/mcp.json` in your project (or use the “Open User Configuration” command for a global mcp.json). For example:
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
      }
    }
  }
  ``` 
  This tells VS Code to run an HTTP-based GitHub server and a local Playwright server【23†L541-L550】. You can also run `MCP: Add Server` from the Command Palette to interactively add one. Once set up, VS Code’s Chat can invoke any tools exposed by these servers (e.g. browser automation via Playwright, GitHub API calls)【23†L492-L502】【23†L541-L550】. 

VS Code provides an “MCP Server Gallery” where many popular services are listed. When you install one, VS Code discovers its capabilities and lets you call them from the chat (for example, the Playwright example in VS Code’s docs takes a screenshot via the MCP tools)【23†L462-L471】【23†L474-L482】.

## Popular MCP Servers and Extensions

Many MCP servers have been published to enhance AI coding. **Reference/official servers** include basic tools like **Everything** (a test server), **Fetch** (web page retrieval), **Filesystem** (secure file I/O), **Git** (local repo search/manipulation), **Memory** (vector/persistent memory), **Time** (datetime utilities) and **Sequential Thinking** (advanced reasoning)【42†L327-L334】. These are provided as examples by the MCP community. 

Beyond reference servers, developers often use production-ready integrations for common platforms. For example:  

- **Code and DevOps:** GitHub/GitLab (repo management), VS Code or Azure DevOps (CI pipelines), Docker, Kubernetes, Terraform.  
- **Databases and Storage:** PostgreSQL, MySQL, SQLite, BigQuery, Supabase, AWS S3, Azure Cosmos DB – letting agents inspect schemas and run queries.  
- **Project Management:** Jira/Confluence (Atlassian), Trello, Asana, Linear, ClickUp – managing issues, boards, tasks.  
- **Communication/Collaboration:** Slack, Discord, Teams – reading channels, sending messages; Email (Gmail API) for sending and summarizing mail.  
- **Design and Content:** Figma, Google Drive, Dropbox, Box – fetch design specs or docs; Contentful, Notion.  
- **APIs and Tools:** Postman (APIs/tests)【47†L232-L238】, Datadog (monitoring)【41†L470-L478】, Cloudinary (media), Firebase (Google Cloud services)【47†L163-L168】, Stripe/Chargebee (payments), Twilio (SMS/voice) – exposing these to LLMs.  
- **Specialized:** Chroma (vector DB), Pinecone, Supabase (embedded DB), FlightRadar, FantasyLeague, Crypto (CoinMarketCap, Crypto Fear/Greed, CoinAPI)【40†L410-L418】【41†L458-L466】.  
- **AI Services:** Hugging Face, Anthropic’s own Claude or ChatGPT (for chaining multiple LLMs), ElevenLabs (speech), Weaviate/Chroma (vector search).  

Many of these have open-source MCP servers on GitHub. For example, there are MCP servers for **Airtable** (remote spreadsheet access)【40†L349-L353】, **Algorand blockchain** (on-chain queries)【40†L343-L346】, **Amadeus flight API**【40†L353-L356】, **Ableton Live** (music DAW control)【40†L337-L340】, **Chess.com** stats, **Contentful CMS**【41†L450-L452】, and hundreds more.  A growing “awesome MCP” list catalogs **hundreds of community servers** (for things like Shopify, Dropbox, Domo, Databricks, etc.)【40†L337-L344】【41†L470-L479】.  Notable examples include Figma integration (agents can pull design specs)【47†L64-L66】, Slack and Discord bots, Airtable databases, and more. 

In short, the MCP ecosystem already contains *dozens* of useful servers. A non-exhaustive sample: Git, Fetch, Filesystem, Slack, Trello, Jira, Notion, Google Drive, GitHub, GitLab, Airtable, Postman, Datadog, Firebase, ClickUp, Salesforce, Stripe, Chroma, Figma, Confluence, etc. (see lists on GitHub and the **official MCP Registry**【35†L291-L299】 for hundreds more). Each server’s GitHub repo (or registry entry) includes its purpose and setup instructions. For example, the **Advanced Trello MCP Server** (for Cursor) provides ~35 Trello tools and runs via Node.js (install, build, then add it to Cursor’s config)【25†L278-L287】【27†L341-L349】. Similarly, a Postman MCP server (in Cursor’s marketplace) lets the AI run API tests and code-gen via natural chat【47†L232-L238】. 

## Installing and Configuring MCP Servers

To install an MCP server, follow these general steps (adjusted per tool):

- **Find the server and code:** Most MCP servers are open-source. Get the GitHub repo or NPM package. For example, `@microsoft/mcp-server-playwright` (VS Code example) or `cursor-cli-mcp` (Cursor example).  

- **Set up credentials:** Some servers require API keys (e.g. `TRELLO_API_KEY`, Airtable key, OAuth tokens). Export these as environment vars or paste into the GUI prompts.  

- **Launch/register the server:**
  - *Local servers:* Run the server process (e.g. `node server.js` or `npx @some/mcp-server`). Then add it to your client. For CLI clients: use `--transport stdio` or edit JSON as above. For VSCode: add a `"command"` entry in `mcp.json`. For Cursor: point `"url": "http://localhost:<port>/mcp"` in `.cursor/mcp.json`.  
  - *Remote/HTTP servers:* Simply supply the HTTP endpoint. E.g. in Claude: `claude mcp add --transport http myremote https://example.com/mcp`【16†L175-L183】; in Gemini: `gemini mcp add --transport http myremote https://example.com/mcp`. In VS Code/Chat: add a `"url"` entry in `mcp.json` or pick from the extension gallery【23†L492-L502】【23†L541-L550】.  

- **Verify:** After adding, check that the tools list is visible. In Claude use `/mcp` in chat, in Gemini use `gemini mcp list`, in Qwen use `qwen mcp list` (or watch the startup logs). In VSCode’s Chat view you can configure tools and try a test prompt (as shown in their “Quickstart”【23†L462-L471】). For Cursor, open the settings to see connected servers.  

- **Example (Claude):**  
  ```bash
  # Add a Notion MCP (HTTP) to Claude
  claude mcp add --transport http notion https://mcp.notion.com/mcp
  # Add Airtable (stdio) with a key
  claude mcp add --transport stdio --env AIRTABLE_KEY=KEY airtable -- npx -y airtable-mcp-server
  ```
  Once added, `/mcp list` shows “notion” and “airtable” with their status【16†L175-L183】【16†L233-L242】.  

- **Example (VS Code):**  
  1. Install the Playwright MCP: open Extensions, search `@mcp playwright`, click *Install*【23†L492-L502】.  
  2. Confirm the Chat Customizations if prompted. VS Code will then auto-run `@microsoft/mcp-server-playwright` as defined by the extension.  
  3. Alternatively, manually add to `.vscode/mcp.json`:  
     ```json
     {
       "servers": {
         "playwright": {
           "command": "npx",
           "args": ["-y", "@microsoft/mcp-server-playwright"]
         }
       }
     }
     ```  
     VS Code will discover the tools (e.g. “openUrl”, “screenshot”) and you can test them via the Chat UI【23†L462-L471】【23†L492-L502】.  

- **Example (Cursor):**  
  1. Add BrainGrid server: `npm install -g @braingrid/cli; braingrid login; braingrid init; braingrid setup cursor` as per the BrainGrid docs.  
  2. This will append JSON to your `~/.cursor/mcp.json`. For instance, it might add a section like:  
     ```json
     {
       "mcpServers": {
         "braingrid": { "url": "https://api.braingrid.ai/mcp" }
       }
     }
     ```  
     (See Cursor tutorial【29†L159-L168】.)  
  3. Now Cursor agents can query BrainGrid directly (e.g. turn feature ideas into tasks) using `/build` commands.  

Each environment has documentation and tutorials for specific services. In general, **adding MCP servers is a two-step process**: launch or register the server with the client (via CLI or UI), then authenticate it if needed.  Once set up, your AI assistant gains all the server’s tools, greatly expanding its capabilities for coding, project management, design, etc. 

**Sources:** Official documentation for Qwen, Gemini, and Claude explain MCP usage【44†L12-L15】【5†L443-L452】【16†L175-L183】.  Cursor and Antigravity docs show their UI flows【29†L159-L168】【21†L163-L172】.  The VS Code docs cover extension-based MCP server setup【23†L492-L502】【23†L541-L550】.  Reference and community MCP servers are listed in the MCP GitHub and registry【42†L327-L334】【40†L337-L344】【35†L291-L299】, which we used to compile the examples above. Each cited link provides further details on specific servers and setup steps.