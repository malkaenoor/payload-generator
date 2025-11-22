# obfuscate.py
import random

def insert_comments(s: str) -> str:
    # benign example: insert "/**/" between some tokens
    parts = s.split()
    return "/**/".join(parts) if parts else s

def random_spacing(s: str) -> str:
    # insert random spaces between chars (example only)
    out = []
    for ch in s:
        out.append(ch)
        if random.random() < 0.15:
            out.append(" ")
    return "".join(out)

def case_swap(s: str) -> str:
    return "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))
