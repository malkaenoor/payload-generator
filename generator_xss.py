# generator_xss.py
# Enhanced XSS generator: supports reflected, stored, dom, and bypass categories.
# ALL payloads are placeholders (lab-approved strings should replace these).
from registry import PAYLOAD_REGISTRY

class XSSGenerator:
    def __init__(self):
        # collect IDs that start with "XSS_"
        self.ids = [k for k in PAYLOAD_REGISTRY.keys() if k.startswith("XSS_")]

    def list_ids(self):
        """Return sorted list of registered XSS payload IDs."""
        return sorted(self.ids)

    def generate_by_id(self, pid):
        """Return payload string for a specific payload ID (or None)."""
        return PAYLOAD_REGISTRY.get(pid)

    def generate_by_type(self, xtype):
        """
        Generate payloads by logical type.
        Supported types:
          - reflected
          - stored
          - dom
          - bypass    (returns a list of bypass variations)
        Note: Returned values are placeholder strings from registry.
        """
        xtype = xtype.lower()
        mapping = {
            "reflected": [
                "XSS_REFLECTED_001",
                "XSS_IMG_ONERROR_002",
                "XSS_SCRIPT_SRC_013",
                "XSS_STYLE_009",
            ],
            "stored": [
                "XSS_TEMPLATE_014",
                "XSS_CUSTOM_015",
                "XSS_INPUT_006",
            ],
            "dom": [
                "XSS_SVG_003",
                "XSS_IFRAME_004",
                "XSS_EVENT_005",
                "XSS_SCRIPT_SRC_013",
            ],
            # bypass returns a curated set of bypass "technique" placeholders
            "bypass": [
                "XSS_SVG_003",       # svg-related placeholder
                "XSS_IMG_SRC_010",   # src-based placeholder
                "XSS_EVENT_005",     # event handler placeholder
                "XSS_TEMPLATE_014",  # template-based placeholder
            ],
        }

        ids = mapping.get(xtype, [])
        # return mapped payload strings (filter missing)
        return [PAYLOAD_REGISTRY.get(i) for i in ids if i in PAYLOAD_REGISTRY]

    def bypass_variations(self, technique=None):
        """
        Return structured bypass variations (placeholders) for study/documentation.
        technique can be: svg, srcdoc, events, nullbyte, waf
        """
        variations = {
            "svg": ["<SVG_BYPASS_PLACEHOLDER_1>", "<SVG_BYPASS_PLACEHOLDER_2>"],
            "srcdoc": ["<SRCDOC_PLACEHOLDER_1>"],
            "events": ["<ONERROR_PLACEHOLDER_1>", "<ONLOAD_PLACEHOLDER_1>", "<ONCLICK_PLACEHOLDER_1>"],
            "nullbyte": ["<NULLBYTE_PLACEHOLDER_1>"],
            "waf": ["<WAF_BYPASS_PLACEHOLDER_COMMENT>", "<WAF_BYPASS_PLACEHOLDER_CASE>"],
        }
        if technique:
            return variations.get(technique.lower(), [])
        return variations  # return dict for documentation
