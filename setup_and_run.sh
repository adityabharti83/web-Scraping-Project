#!/bin/bash

echo "🚀 Starting AI Scraper Setup..."

# Virtual Environment
python -m venv venv

# Activate VENV (for Git Bash on Windows)
source venv/Scripts/activate

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browser
python -m playwright install chromium

# Check config.py
if ! grep -q "OPENAI_API_KEY" config.py; then
    echo "❗ Set your OPENAI_API_KEY in config.py"
    exit 1
fi

# Run the project
echo "▶️ Running main.py"
python main.py "Find me laptops under ₹50000"

echo "✅ Done! Check the samples/output_examples.xlsx file"
deactivate
