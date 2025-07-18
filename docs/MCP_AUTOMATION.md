# 🧠 MCP_AUTOMATION.md
## Model Context Protocol for Browser Automation in `ai_scraper_project`

---

### 📌 Overview

**MCP (Model Context Protocol)** in this project is a lightweight design pattern for controlling the browser using **LLM-parsed user intent**. It acts as a middle layer between:
- **LLM output** (parsed user query)
- **Browser control layer** (Playwright workflows)

MCP ensures that structured user intents like `"product_search"` are mapped to a specific browser automation sequence.

---

### ⚙️ MCP Components

| Module | Role |
|--------|------|
| `llm_module/query_parser.py` | Parses natural language to intent JSON |
| `mcp_automation/workflows.py` | Executes browser workflows based on intent |
| `mcp_automation/selectors_config.py` | Central place for per-site selectors |
| `main.py` | Orchestrates everything |

---

### 🔄 How MCP Works

**Example Query:**
