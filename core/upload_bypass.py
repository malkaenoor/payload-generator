import json, os

def list_upload():
    return json.load(open(os.path.join("templates", "upload_bypass.json")))

def get_upload_by_id(pid):
    return next((p for p in list_upload() if p["id"] == pid), None)
