import pytest
from data_extraction.utils import clean_text, safe_int

def test_clean_text():
    text = "\nHello World \n"
    assert clean_text(text) == "Hello World"

def test_safe_int_valid():
    assert safe_int("₹12,345") == 12345

def test_safe_int_invalid():
    assert safe_int("abc") is None
