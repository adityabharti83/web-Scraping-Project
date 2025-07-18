from playwright.sync_api import sync_playwright
from config import HEADLESS_BROWSER

def launch_browser():
    """
    Launches a Chromium browser using Playwright.
    Returns the playwright instance and browser object.
    """
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=HEADLESS_BROWSER)
    return p, browser

def perform_mcp_command(page, command: dict):
    """
    Perform a browser action based on the Model Context Protocol (MCP) command.
    Supported actions: goto, fill, click, wait_for
    """
    try:
        if command["action"] == "goto":
            page.goto(command["url"])
        elif command["action"] == "fill":
            page.fill(command["selector"], command["value"])
        elif command["action"] == "click":
            page.click(command["selector"])
        elif command["action"] == "wait_for":
            page.wait_for_selector(command["selector"])
    except Exception as e:
        print(f"❌ MCP Command Error: {e}")
