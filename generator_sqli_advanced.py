# generator_sqli_advanced.py
# Advanced SQLi generator scaffolding — SAFE placeholders only.
# Do NOT add real exploit strings here unless you have written permission and lab target.

from registry import PAYLOAD_REGISTRY
from encoder import Encoder
import obfuscate

enc = Encoder()

def case_swap(s: str) -> str:
    return ''.join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(s))

def insert_comments_style(s: str) -> str:
    # insert SQL-style comment tokens in between tokens as a transform placeholder
    # example transform: "UNION SELECT" -> "UN/**/ION SEL/**/ECT" (placeholder)
    parts = s.split()
    return " /*C*/ ".join(parts)

def random_whitespace(s: str) -> str:
    # insert single spaces or tabs at random positions (deterministic placeholder)
    return " ".join([w for w in s.split()])

class SQLiAdvanced:
    """
    Provides safe templates and transformation helpers for advanced SQLi testing in a lab.
    Returned strings are placeholders/templates — replace with approved payload text before real testing.
    """

    def __init__(self):
        # load available SQLi ids from registry for reference
        self.base_ids = [k for k in PAYLOAD_REGISTRY.keys() if k.startswith("SQLI_")]

    # ---------- Template generators (placeholders) ----------
    def error_based_templates(self):
        """
        Return list of error-based SQLi template placeholders.
        Replace tokens like {MARKER} with actual test values in a lab.
        """
        return [
            "<ERROR_TEMPLATE_1: REPLACE_WITH_FIELD {MARKER}>",
            "<ERROR_TEMPLATE_2: CAST/CONCAT style placeholder {MARKER}>",
        ]

    def union_based_templates(self):
        """
        Return list of union-based SQLi template placeholders.
        """
        return [
            "<UNION_TEMPLATE_1: UNION SELECT ... FROM ... /* replace */>",
            "<UNION_TEMPLATE_2: UNION ALL SELECT ... /* replace */>",
        ]

    def blind_boolean_templates(self):
        """
        Blind boolean-based templates (placeholders only).
        """
        return [
            "<BLIND_BOOL_TEMPLATE_TRUE: marker=? AND 1=1>",
            "<BLIND_BOOL_TEMPLATE_FALSE: marker=? AND 1=2>",
        ]

    def time_based_templates(self):
        """
        Time-based (sleep) templates (placeholders).
        """
        return [
            "<TIME_TEMPLATE_1: SLEEP_PLACEHOLDER({SECONDS})>",
            "<TIME_TEMPLATE_2: BENIGN_DELAY_CHECK({SECONDS})>",
        ]

    # ---------- WAF bypass transformation helpers ----------
    def waf_transform_comment(self, payload: str):
        """Return a version with inline comment markers (placeholder style)."""
        return insert_comments_style(payload)

    def waf_transform_case(self, payload: str):
        """Case-swap transform (placeholder)."""
        return case_swap(payload)

    def waf_transform_hex(self, payload: str):
        """Return hex encoded version using encoder helper (safe)."""
        try:
            return enc.hex_encode(payload)
        except Exception:
            return None

    def waf_transform_url(self, payload: str):
        """URL encode the payload (safe)."""
        return enc.url_encode(payload)

    def waf_transform_unicode_escape(self, payload: str):
        """Return unicode-escape representation (safe)."""
        try:
            return payload.encode('unicode_escape').decode('ascii')
        except Exception:
            return payload

    # ---------- Combined generator ----------
    def generate(self, technique: str, apply_bypass: str = None, obf: str = None):
        """
        technique: 'union', 'error', 'blind', 'time'
        apply_bypass: None | 'comment' | 'case' | 'hex' | 'url' | 'unicode'
        obf: None | 'comments' | 'spacing' | 'caseswap'  (uses obfuscate.py helpers)
        Returns list of safe placeholder strings (transformed per options).
        """
        base_list = []
        t = technique.lower()
        if t == 'union':
            base_list = self.union_based_templates()
        elif t == 'error':
            base_list = self.error_based_templates()
        elif t == 'blind':
            base_list = self.blind_boolean_templates()
        elif t == 'time':
            base_list = self.time_based_templates()
        else:
            return []

        transformed = []
        for p in base_list:
            out = p
            # apply waf bypass transform
            if apply_bypass:
                if apply_bypass == 'comment':
                    out = self.waf_transform_comment(out)
                elif apply_bypass == 'case':
                    out = self.waf_transform_case(out)
                elif apply_bypass == 'hex':
                    # hex returns string without angle brackets; wrap back for clarity
                    hx = self.waf_transform_hex(out)
                    out = "<HEX:"+ (hx if hx else "") + ">"
                elif apply_bypass == 'url':
                    out = "<URL:"+ self.waf_transform_url(out) + ">"
                elif apply_bypass == 'unicode':
                    out = "<UNICODE:"+ self.waf_transform_unicode_escape(out) + ">"

            # apply obfuscation helpers if requested
            if obf:
                if obf == 'comments':
                    out = obfuscate.insert_comments(out)
                elif obf == 'spacing':
                    out = obfuscate.random_spacing(out)
                elif obf == 'caseswap':
                    out = obfuscate.case_swap(out)

            transformed.append(out)

        return transformed

    # ---------- Utility: list base ids ----------
    def list_ids(self):
        return sorted(self.base_ids)

