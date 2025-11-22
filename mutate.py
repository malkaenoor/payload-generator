import random

class Mutator:

    def case_flip(self, payload):
        return ''.join(
            c.upper() if c.islower() else c.lower()
            for c in payload
        )

    def random_upper(self, payload):
        return ''.join(c.upper() if random.random() > 0.5 else c for c in payload)

    def random_lower(self, payload):
        return ''.join(c.lower() if random.random() > 0.5 else c for c in payload)

    def whitespace(self, payload):
        return payload.replace("<", " < ").replace(">", " > ")

    def symbols(self, payload):
        return payload.replace("script", "scr!pt").replace("alert", "al3rt")

    def apply(self, method, payload):
        methods = {
            "case-flip": self.case_flip,
            "random-upper": self.random_upper,
            "random-lower": self.random_lower,
            "whitespace": self.whitespace,
            "symbols": self.symbols,
        }

        if method not in methods:
            return "Invalid method!"

        return methods[method](payload)
class Mutator:

    def case_flip(self, payload: str) -> str:
        return ''.join([c.lower() if c.isupper() else c.upper() for c in payload])

    def unicode_escape(self, payload: str) -> str:
        return ''.join([f"\\u{ord(c):04x}" for c in payload])

    def random_caps(self, payload: str) -> str:
        import random
        return ''.join([c.upper() if random.random() > 0.5 else c.lower() for c in payload])

    def reverse(self, payload: str) -> str:
        return payload[::-1]

    def double_encode(self, payload: str) -> str:
        import base64
        step1 = base64.b64encode(payload.encode()).decode()
        step2 = base64.b64encode(step1.encode()).decode()
        return step2
