import json, os

def list_csrf():
    return json.load(open(os.path.join("templates", "csrf.json")))

def get_csrf_by_id(pid):
    return next((p for p in list_csrf() if p["id"] == pid), None)
