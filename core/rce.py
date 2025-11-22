import json
import os

def list_rce():
    path = os.path.join("templates", "rce.json")
    return json.load(open(path))

def get_rce_by_id(pid):
    for p in list_rce():
        if p["id"] == pid:
            return p
    return None
