import json, os

def list_ssti():
    return json.load(open(os.path.join("templates", "ssti.json")))

def get_ssti_by_id(pid):
    return next((p for p in list_ssti() if p["id"] == pid), None)

