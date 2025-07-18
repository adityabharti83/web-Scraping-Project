import pytest
from llm_module.query_parser import parse_user_query

def test_parse_user_query():
    query = "Find me phones under ₹20000 on Flipkart"
    result = parse_user_query(query)

    assert isinstance(result, dict)
    assert result["intent"] == "product_search"
    assert "filters" in result
    assert result["filters"]["max_price"] <= 20000
    assert "flipkart" in result["filters"]["sites"]
