# utils.py
import json
try:
    import pyperclip
except Exception:
    pyperclip = None

def export_to_json(payloads, filename):
    data = {"payloads": payloads}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return filename

def export_to_txt(payloads, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for p in payloads:
            f.write(p + "\n")
    return filename

def copy_to_clipboard(text):
    if pyperclip:
        pyperclip.copy(text)
        return True
    return False
