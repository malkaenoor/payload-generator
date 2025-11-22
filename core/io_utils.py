import json
from pathlib import Path
from typing import List

def load_json(filepath: str):
    p = Path(filepath)
    if not p.exists():
        return []
    return json.loads(p.read_text(encoding='utf-8'))

def export_to_txt(items: List[dict], outpath: str):
    lines = []
    for it in items:
        lines.append(f\"ID: {it.get('id')} - {it.get('desc')}\\nPLACEHOLDER: {it.get('example_safe')}\\nDANGER: {it.get('danger_level')}\")
    Path(outpath).write_text('\\n\\n'.join(lines), encoding='utf-8')
