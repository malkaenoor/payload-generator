# --- AUTO EXPORT FOR CLI ---
def xss_payloads():
    from pathlib import Path
    import json
    BASE = Path(__file__).resolve().parent.parent / "templates" / "xss_templates.json"
    if BASE.exists():
        return json.loads(BASE.read_text())
    return []
x
