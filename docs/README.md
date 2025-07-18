# 🤖 AI Scraper Project

**AI-powered browser automation and multi-site web scraping tool using OpenAI GPT and Playwright.**

This project allows you to enter natural language queries like:

> "Find me laptops under ₹50,000 on Amazon and Flipkart"

And it will:
- Parse the query using OpenAI's GPT model
- Automate browser actions to search and scrape data from sites like Amazon and Flipkart
- Generate a well-structured Excel report with charts and filters

---

## 🚀 Features

- 🔍 Natural Language Query Parsing using OpenAI GPT
- 🌐 Browser Automation with Playwright
- 🛒 Multi-site scraping (Amazon, Flipkart, Travel sites – extendable)
- 📊 Excel Report Generation with charts (via pandas and OpenPyXL)
- 📦 Modular and Scalable Python Codebase
- 🧪 Unit Testing with PyTest
- 🧠 Model Context Protocol (MCP) for intent-to-automation mapping

---

## 📁 Project Structure

ai_scraper_project/
├── main.py
├── config.py
├── requirements.txt
├── setup_and_run.sh
├── llm_module/
│ ├── init.py
│ └── query_parser.py
├── mcp_automation/
│ ├── init.py
│ ├── playwright_mcp.py
│ ├── selectors_config.py
│ └── workflows.py
├── data_extraction/
│ ├── amazon_scraper.py
│ ├── flipkart_scraper.py
│ ├── travel_scraper.py
│ └── utils.py
├── excel_report/
│ ├── init.py
│ ├── report_generator.py
│ └── chart_builder.py
├── tests/
│ ├── init.py
│ ├── test_llm_module.py
│ ├── test_scrapers.py
│ └── test_excel.py
├── docs/
│ ├── README.md
│ ├── WORKFLOW_EXAMPLES.md
│ └── MCP_AUTOMATION.md
└── samples/
└── output_examples.xlsx

yaml
Copy code


---

## 💻 Setup Instructions (Windows)

### ✅ Step 1: Clone the Project

bash
cd E:\Project
git clone https://github.com/adityabharti83/web-Scraping-Project.git
cd ai_scraper_project

Or download and unzip the project into any folder

### ✅ Step 2: Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate

### ✅ Step 3: Install Dependencies
bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt

### ✅ Step 4: Install Playwright Browsers
bash
Copy code
playwright install

### ✅ Step 5: Set OpenAI API Key

Open the config.py file and add your OpenAI key:

python
Copy code
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

### ▶️ How to Run the Project

### ✅ Example Query:
bash
Copy code
python main.py "Find me laptops under ₹50000 on Amazon and Flipkart"
This will:

Launch the browser

Search for the product

Scrape product name and price

Export everything into:
samples/output_examples.xlsx


### 🧪 Running Tests

bash
Copy code
venv\Scripts\activate
pytest tests
🧠 What Is This Project For?
This project is ideal for:

### 📈 Data analysts – Automate collection of pricing/market data

🛍️ E-commerce teams – Monitor product listings across platforms

🤖 AI developers – Build intelligent web automation with LLMs

🧪 Learners & Researchers – Explore GPT + Playwright integration

### ❗ Troubleshooting

Issue	Solution
ImportError or selector errors	Check if the site structure changed; update selectors_config.py
OpenAI error about ChatCompletion	Use the updated OpenAI API format as used in query_parser.py
Browser fails to launch	Run playwright install again
Excel file empty	Scraper may have missed data; inspect HTML changes

### 📚 Additional Documentation
docs/MCP_AUTOMATION.md – Explains Model Context Protocol for browser workflows

docs/WORKFLOW_EXAMPLES.md – Query → Workflow conversion examples

docs/README.md – Main documentation

### 📜 License
This project is licensed under the MIT License.
Free to use, modify, and distribute.
