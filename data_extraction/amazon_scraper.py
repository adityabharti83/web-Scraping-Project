from bs4 import BeautifulSoup
from mcp_automation.workflows import execute_amazon_workflow
from mcp_automation.selectors_config import SELECTORS

def scrape_amazon(page, intent):
    product_name = intent.get("product", "")
    max_price = intent["filters"].get("max_price")

    print("🔎 Scraping Amazon for:", product_name)

    execute_amazon_workflow(page, product_name)
    page.wait_for_timeout(5000)

    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    products = []
    for item in soup.select(SELECTORS["amazon"]["product_container"]):
        title = item.select_one(SELECTORS["amazon"]["product_title"])
        price = item.select_one(SELECTORS["amazon"]["product_price"])

        if title and price:
            try:
                price_value = int(price.text.replace(",", "").strip())
                if not max_price or price_value <= max_price:
                    products.append({
                        "title": title.text.strip(),
                        "price": price_value,
                        "source": "Amazon"
                    })
            except:
                continue
    return products
