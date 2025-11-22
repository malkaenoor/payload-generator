import json
from pathlib import Path
from .io_utils import load_json
from typing import Dict

class SafeGenerator:
    def __init__(self, templates_dir='payloads', mode='safe'):
        self.templates_dir = Path(templates_dir)
        self.mode = mode  # 'safe' or 'lab' (lab mode disabled by default in CLI)
        self.template_files = {
            'xss': self.templates_dir / 'xss_templates.json',
            'sqli': self.templates_dir / 'sqli_templates.json',
            'cmdinj': self.templates_dir / 'cmdinj_templates.json'
        }

    def list_templates(self, ttype: str):
        fp = self.template_files.get(ttype)
        if not fp or not fp.exists():
            return []
        return load_json(str(fp))

    def generate(self, ttype: str, tid: str, encode=None):
        """
        Returns a dict with metadata and a safe placeholder.
        Never returns real exploit strings when mode == 'safe'.
        """
        templates = self.list_templates(ttype)
        item = next((t for t in templates if t.get('id') == tid), None)
        if not item:
            raise ValueError('Template not found')

        output = {
            'id': item['id'],
            'type': item['type'],
            'desc': item['desc'],
            'danger_level': item.get('danger_level'),
            'example': item['example_safe'],
            'note': 'This is a safe placeholder. Replace in authorised lab only.',
        }

        # optionally encode the placeholder string
        if encode:
            # lazy import to avoid hard dependency on encoders at import time
            from src.core import encoders as enc
            raw = output['example']
            if encode == 'base64':
                output['encoded'] = enc.to_base64(raw)
            elif encode == 'url':
                output['encoded'] = enc.url_encode(raw)
            elif encode == 'hex':
                output['encoded'] = enc.to_hex(raw)
            elif encode == 'unicode':
                output['encoded'] = enc.to_unicode_escape(raw)
            else:
                output['encoded'] = None
        return output
