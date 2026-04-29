#!/usr/bin/env python3
"""H-NEW-210 secondary: where do the pre-registered classical hotspots actually rank under Levenshtein?"""
import json
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(curr[-1] + 1, prev[j] + 1,
                            prev[j - 1] + (ca != cb)))
        prev = curr
    return prev[-1]


def get(data, s, v):
    for sur in data:
        if sur["id"] == s:
            for ver in sur["verses"]:
                if ver["id"] == v:
                    return ver["text"].strip()
    return None


def main():
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    pairs = [
        ("Prophet-catalog (Q2:136 <-> Q3:84)", 2, 136, 3, 84),
        ("Ablution (Q4:43 <-> Q5:6)", 4, 43, 5, 6),
        ("Kill your children (Q6:151 <-> Q17:31)", 6, 151, 17, 31),
        ("Enter the town (Q2:58 <-> Q7:161)", 2, 58, 7, 161),
        ("Moses rod (Q7:107 <-> Q26:32)", 7, 107, 26, 32),
        ("Moses hand (Q7:108 <-> Q26:33)", 7, 108, 26, 33),
        ("al-Rahman refrain sample (Q55:13 <-> Q55:16)", 55, 13, 55, 16),  # intra
        ("al-Mursalat refrain (Q77:15 <-> Q77:19)", 77, 15, 77, 19),  # intra
    ]
    for label, s1, v1, s2, v2 in pairs:
        t1 = get(data, s1, v1)
        t2 = get(data, s2, v2)
        if t1 is None or t2 is None:
            print(f"{label}: MISSING")
            continue
        d = levenshtein(t1, t2)
        ml = (len(t1) + len(t2)) / 2
        print(f"{label}")
        print(f"  t1 [{len(t1)}ch]: {t1}")
        print(f"  t2 [{len(t2)}ch]: {t2}")
        print(f"  Lev={d}  ratio={d/ml:.3f}  (<0.30 threshold: {d/ml < 0.30})")
        print()


if __name__ == "__main__":
    main()
