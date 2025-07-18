"""
query_parser.py  •  Works with openai>=1.0
--------------------------------------------------
Parse a natural‑language product query into a structured
Python dict that downstream scrapers understand.
If no real API key is set (e.g. during CI tests), we fall
back to a cheap regex‑based parser so unit tests still pass
offline.
"""
from __future__ import annotations
import os
import re
import json
from typing import Dict, Any

import openai
from config import OPENAI_API_KEY

# ---------- 1. Choose strategy ---------------------------------------------
USE_FAKE_PARSER = OPENAI_API_KEY.startswith("sk-") is False

# ---------- 2. LLM‑powered parser (OpenAI ≥1.0) -----------------------------
def _llm_parse(query: str) -> Dict[str, Any]:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

    sys_msg = "You turn product queries into structured JSON."
    user_msg = f"""Convert this query into JSON with keys
    intent, product, and filters (min_price, max_price, brands, sites):
    "{query}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": sys_msg},
            {"role": "user",   "content": user_msg}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    # Some prompting hygiene: force valid JSON
    first_brace = content.find("{")
    last_brace  = content.rfind("}")
    json_blob   = content[first_brace:last_brace+1]
    return json.loads(json_blob)

# ---------- 3. Lightweight regex fallback -----------------------------------
_price_pat  = re.compile(r"₹?(\d[\d,]*)", re.U)
_site_pat   = re.compile(r"\b(amazon|flipkart)\b", re.I)

def _regex_parse(query: str) -> Dict[str, Any]:
    prices = [int(p.replace(",", "")) for p in _price_pat.findall(query)]
    max_price = min(prices) if prices else None

    sites = _site_pat.findall(query.lower()) or ["amazon", "flipkart"]

    return {
        "intent":  "product_search",
        "product": query.split("find me")[-1].split("under")[0].strip()
                   or "product",
        "filters": {
            "min_price": None,
            "max_price": max_price,
            "brands":   [],
            "sites":    [s.lower() for s in sites],
        }
    }

# ---------- 4. Public API ----------------------------------------------------
def parse_user_query(query: str) -> Dict[str, Any]:
    """
    Wrapper that chooses LLM or regex based on whether a real
    OPENAI_API_KEY is present.
    """
    if USE_FAKE_PARSER:
        return _regex_parse(query)
    try:
        return _llm_parse(query)
    except Exception as exc:           # network, quota, etc.
        print("⚠️  LLM parse failed, falling back:", exc)
        return _regex_parse(query)
