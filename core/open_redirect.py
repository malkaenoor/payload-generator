import json, os

def list_redirect():
    return json.load(open(os.path.join("templates", "open_redirect.json")))

def get_redirect_by_id(pid):
    return next((p for p in list_redirect() if p["id"] == pid), None)
