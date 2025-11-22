# generator_sqli.py
# SQLiGenerator class - reads payload IDs from registry.PAYLOAD_REGISTRY
# NOTE: This uses SAFE placeholder payloads, not exploit strings.

from registry import PAYLOAD_REGISTRY

class SQLiGenerator:
    def __init__(self):
        # Gather all payload IDs starting with SQLI_
        self.ids = [k for k in PAYLOAD_REGISTRY.keys() if k.startswith("SQLI_")]

    def list_ids(self):
        """Return sorted list of all SQLi IDs."""
        return sorted(self.ids)

    def generate_by_id(self, pid):
        """Return placeholder payload string by ID."""
        return PAYLOAD_REGISTRY.get(pid)

    def generate_by_type(self, stype):
        """
        Generate SQLi category-wise.
        You may edit the mapping based on your own module design.
        """
        mapping = {
            "error": [
                "SQLI_ERROR_004",
            ],
            "union": [
                "SQLI_UNION_001",
                "SQLI_UNION_SELECT_007",
            ],
            "blind": [
                "SQLI_BLIND_006",
                "SQLI_BOOLEAN_002",
            ],
            "time": [
                "SQLI_TIME_003",
                "SQLI_SLEEP_014",
            ],
            "bypass": [
                "SQLI_COMMENT_TRUNC_008",
                "SQLI_CLEANSING_009",
                "SQLI_AUTHBYPASS_010",
            ],
        }

        ids = mapping.get(stype.lower(), [])
        return [PAYLOAD_REGISTRY.get(i) for i in ids if i in PAYLOAD_REGISTRY]
