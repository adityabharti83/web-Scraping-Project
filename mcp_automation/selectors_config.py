# mcp_automation/selectors_config.py

SELECTORS = {
    "amazon": {
        "search_box": "input#twotabsearchtextbox",
        "search_button": "input#nav-search-submit-button",
        "product_container": "div.s-main-slot div[data-component-type='s-search-result']",
        "product_title": "h2 span",
        "product_price": ".a-price-whole"
    },
    "flipkart": {
        "search_box": "input[name='q']",
        "product_container": "div._1AtVbE",
        "product_title": "div._4rR01T, a.s1Q9rs",
        "product_price": "div._30jeq3"
    }
}
