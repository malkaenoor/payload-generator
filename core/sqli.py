# --- AUTO EXPORT FOR CLI ---
def sqli_payloads():
    from pathlib import Path
    import json
    BASE = Path(__file__).resolve().parent.parent / "templates" / "sqli_templates.json"
    if BASE.exists():
        return json.loads(BASE.read_text())
    return []
