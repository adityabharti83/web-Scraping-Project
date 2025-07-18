
---

### ✅ 23. `docs/WORKFLOW_EXAMPLES.md`

```markdown
# 🔄 Workflow Examples

## 📘 Product Search Example

**Query:**  
> "Find me iPhones under ₹70000 on Amazon"

**Parsed Intent (from LLM):**
```json
{
  "intent": "product_search",
  "product": "iPhone",
  "filters": {
    "min_price": null,
    "max_price": 70000,
    "brands": ["Apple"],
    "sites": ["amazon"]
  }
}
