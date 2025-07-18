def clean_text(text):
    return text.replace("\n", "").strip()

def safe_int(text):
    try:
        return int(text.replace(",", "").replace("₹", "").strip())
    except:
        return None
