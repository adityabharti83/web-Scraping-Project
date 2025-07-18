import sys
import os
sys.path.append(os.getcwd())

from mcp_automation.selectors_config import SELECTORS
from mcp_automation.playwright_mcp import perform_mcp_command

def execute_amazon_workflow(page, product_name):
    commands = [
        {"action": "goto", "url": "https://www.amazon.in"},
        {"action": "fill", "selector": SELECTORS["amazon"]["search_box"], "value": product_name},
        {"action": "click", "selector": SELECTORS["amazon"]["search_button"]},
        {"action": "wait_for", "selector": SELECTORS["amazon"]["product_container"]}
    ]
    for cmd in commands:
        perform_mcp_command(page, cmd)

def execute_flipkart_workflow(page, product_name):
    commands = [
        {"action": "goto", "url": "https://www.flipkart.com"},
        {"action": "click", "selector": "button._2KpZ6l._2doB4z"},  # close login popup
        {"action": "fill", "selector": SELECTORS["flipkart"]["search_box"], "value": product_name},
        {"action": "press", "selector": SELECTORS["flipkart"]["search_box"], "key": "Enter"},
        {"action": "wait_for", "selector": SELECTORS["flipkart"]["product_container"]}
    ]
    for cmd in commands:
        perform_mcp_command(page, cmd)
