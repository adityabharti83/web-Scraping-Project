from llm_module.query_parser import parse_user_query
from mcp_automation.playwright_mcp import launch_browser, perform_mcp_command
from data_extraction.amazon_scraper import scrape_amazon
from data_extraction.flipkart_scraper import scrape_flipkart
from excel_report.report_generator import generate_excel_report

def main(query: str):
    intent = parse_user_query(query)
    print(f" Parsed intent: {intent}")

    p, browser = launch_browser()
    context = browser.new_context()
    page = context.new_page()

    all_data = []

    if "amazon" in intent["filters"]["sites"]:
        data = scrape_amazon(page, intent)
        all_data.extend(data)

    if "flipkart" in intent["filters"]["sites"]:
        data = scrape_flipkart(page, intent)
        all_data.extend(data)

    browser.close()
    p.stop()

    if all_data:
        generate_excel_report(all_data, filename="samples/output_examples.xlsx")
        print(" Report generated: samples/output_examples.xlsx")
    else:
        print(" No data found for the query.")

if __name__ == "__main__":
    main("Find me laptops under ₹50000")
