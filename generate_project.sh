#!/bin/bash

# Name of your root directory
ROOT_DIR="ai_scraper_project"

echo "📁 Creating project folder: $ROOT_DIR"
mkdir -p $ROOT_DIR

cd $ROOT_DIR

# 1. Top-Level Files
echo "📄 Creating top-level files..."
touch main.py config.py requirements.txt setup_and_run.sh

# 2. Directory structure
echo "📁 Creating folders..."
mkdir -p llm_module mcp_automation data_extraction excel_report tests docs samples

# 3. __init__.py in modules
touch llm_module/__init__.py
touch mcp_automation/__init__.py
touch excel_report/__init__.py
touch tests/__init__.py

# 4. LLM module
cat <<EOF > llm_module/query_parser.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def parse_user_query(query: str) -> dict:
    # Sample LLM parser using OpenAI
    prompt = f"Parse this query: {query} into structured JSON."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return eval(response['choices'][0]['message']['content'])
EOF

# 5. MCP Automation
cat <<EOF > mcp_automation/playwright_mcp.py
from playwright.sync_api import sync_playwright

def launch_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    return p, browser

def perform_mcp_command(page, command: dict):
    if command['action'] == 'goto':
        page.goto(command['url'])
EOF

touch mcp_automation/selectors_config.py
touch mcp_automation/workflows.py

# 6. Data Extraction
touch data_extraction/amazon_scraper.py
touch data_extraction/flipkart_scraper.py
touch data_extraction/travel_scraper.py
touch data_extraction/utils.py

# 7. Excel Reporting
touch excel_report/report_generator.py
touch excel_report/chart_builder.py

# 8. Tests
touch tests/test_llm_module.py
touch tests/test_scrapers.py
touch tests/test_excel.py

# 9. Docs
touch docs/README.md
touch docs/WORKFLOW_EXAMPLES.md
touch docs/MCP_AUTOMATION.md

# 10. Samples
touch samples/output_examples.xlsx

# 11. config.py
cat <<EOF > config.py
# Replace this with your actual OpenAI API key
OPENAI_API_KEY = "your-api-key-here"
EOF

# 12. requirements.txt
cat <<EOF > requirements.txt
openai==1.33.0
playwright==1.44.0
beautifulsoup4==4.12.3
lxml==5.2.1
requests==2.31.0
pandas==2.2.2
openpyxl==3.1.2
tqdm==4.66.4
python-dotenv==1.0.1
pytest==8.2.2
EOF

echo "✅ Project structure created successfully inside $ROOT_DIR"
