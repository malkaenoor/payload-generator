import random

def case_variation(s: str) -> str:
    # Randomly change case of letters (demo only)
    return ''.join(ch.upper() if random.choice([True, False]) else ch.lower() for ch in s)

def insert_spacing(s: str, every_n: int = 2) -> str:
    # Insert a space every N characters (demonstration)
    parts = [s[i:i+every_n] for i in range(0, len(s), every_n)]
    return ' '.join(parts)

def insert_comments(s: str, token='/*X*/', pos_list=None):
    # Insert token at positions (pos_list is list of indices)
    if pos_list is None:
        pos_list = [len(s)//2]
    res = []
    last = 0
    for p in sorted(set([p for p in pos_list if 0 <= p <= len(s)])):
        res.append(s[last:p])
        res.append(token)
        last = p
    res.append(s[last:])
    return ''.join(res)
