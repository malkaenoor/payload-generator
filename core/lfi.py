# --- LFI Payload Module ---

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "templates" / "lfi_templates.json"

def lfi_payloads():
    """Return list of LFI payload templates"""
    if BASE.exists():
        return json.loads(BASE.read_text(encoding="utf-8"))
    return []

def get_lfi_by_id(pid):
    """Get specific LFI payload by ID"""
    templates = lfi_payloads()
    return next((t for t in templates if t.get("id") == pid), None)
import json, os

def list_lfi():
    return json.load(open(os.path.join("templates", "lfi.json")))

def get_lfi_by_id(pid):
    return next((p for p in list_lfi() if p["id"] == pid), None)
