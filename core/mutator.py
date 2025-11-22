import random
import string

class Mutator:

    # 1. Flip case (a→A , B→b)
    @staticmethod
    def case_flip(payload: str) -> str:
        return ''.join(
            char.lower() if char.isupper() else char.upper()
            for char in payload
        )

    # 2. Insert random characters
    @staticmethod
    def random_insert(payload: str, count: int = 3) -> str:
        for _ in range(count):
            pos = random.randint(0, len(payload))
            payload = payload[:pos] + random.choice(string.ascii_letters) + payload[pos:]
        return payload

    # 3. Unicode obfuscation
    @staticmethod
    def unicode_obfuscate(payload: str) -> str:
        return ''.join(f'\\u{ord(c):04x}' for c in payload)

    # 4. Remove whitespace
    @staticmethod
    def strip_whitespace(payload: str) -> str:
        return ''.join(payload.split())

    # 5. Reverse payload
    @staticmethod
    def reverse(payload: str) -> str:
        return payload[::-1]

    # Dispatcher
    @staticmethod
    def mutate(payload: str, method: str) -> str:
        methods = {
            "case-flip": Mutator.case_flip,
            "random-insert": Mutator.random_insert,
            "unicode": Mutator.unicode_obfuscate,
            "strip": Mutator.strip_whitespace,
            "reverse": Mutator.reverse,
        }

        if method not in methods:
            raise ValueError(f"Unknown mutation method: {method}")

        return methods[method](payload)
