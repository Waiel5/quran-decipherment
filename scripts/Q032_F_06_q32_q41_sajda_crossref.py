#!/usr/bin/env python3
"""
Q032-F-06 — Q 32:15 ↔ Q 41:37/38 sajda cross-reference within 14-sajda pair distribution.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-06-q32-q41-sajda-crossref-prereg.md
SHA256:  6e3918d8cd80e5d44d7d9565785ca92e1dd17298a82aaaa93d5e16ed7c684d89

Method: compute 14×14 cosine matrix of sajda-verse pairs (C(14,2)=91); rank the test pair.
"""

from __future__ import annotations
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q032-al-sajda/Q032-F-06-q32-q41-sajda-crossref-prereg.md"
EXPECTED_SHA = "6e3918d8cd80e5d44d7d9565785ca92e1dd17298a82aaaa93d5e16ed7c684d89"
OUT = ROOT / "surahs/Q032-al-sajda/csv/Q032-F-06.json"

SAJDA_14 = [(7, 206), (13, 15), (16, 50), (17, 109), (19, 58), (22, 18),
            (25, 60), (27, 26), (32, 15), (38, 24), (41, 38), (53, 62),
            (84, 21), (96, 19)]

# Strip these markers
STRIP_CHARS = "۩ۚۖۗۘۛۜ۠ۡۤۦۭۧۨ"


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    return actual


def tokenize(text: str):
    for ch in STRIP_CHARS:
        text = text.replace(ch, " ")
    return text.split()


def cosine_sim(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    common = set(a) & set(b)
    dot = sum(a[k] * b[k] for k in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def main():
    sha_actual = sha_verify()
    with (ROOT / "quran-text/quran-no-tashkeel.json").open(encoding="utf-8") as f:
        q = json.load(f)

    # Build TF vectors for each sajda-verse
    vecs = {}
    raw_texts = {}
    for (s, v) in SAJDA_14:
        text = q[s - 1]["verses"][v - 1]["text"]
        toks = tokenize(text)
        vecs[(s, v)] = Counter(toks)
        raw_texts[(s, v)] = text

    # Sensitivity: also include Q 41:37 (Maghrebi sajda position)
    text_41_37 = q[40]["verses"][36]["text"]
    vec_41_37 = Counter(tokenize(text_41_37))

    # 14×14 cosine matrix
    n = len(SAJDA_14)
    cosines = {}
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            a, b = SAJDA_14[i], SAJDA_14[j]
            cs = cosine_sim(vecs[a], vecs[b])
            cosines[(a, b)] = cs
            pairs.append({"a": f"{a[0]}:{a[1]}", "b": f"{b[0]}:{b[1]}", "cosine": cs})

    pairs_sorted = sorted(pairs, key=lambda r: -r["cosine"])
    n_pairs = len(pairs)

    test_pair = ((32, 15), (41, 38))
    test_pair_str = ("32:15", "41:38")
    test_cosine = cosines[test_pair]
    test_rank = next(i + 1 for i, r in enumerate(pairs_sorted)
                     if (r["a"] == test_pair_str[0] and r["b"] == test_pair_str[1])
                     or (r["a"] == test_pair_str[1] and r["b"] == test_pair_str[0]))
    test_percentile = 1.0 - (test_rank - 1) / n_pairs

    # Sensitivity: Q 32:15 ↔ Q 41:37
    sens_cosine = cosine_sim(vecs[(32, 15)], vec_41_37)

    pass_a = test_rank <= 5
    pass_b = test_percentile >= 0.80

    if pass_a and pass_b:
        verdict = "PASS-DIRECTED (top-5 rank + top-quintile)"
    elif pass_b:
        verdict = "PARTIAL (top-quintile met; top-5 missed)"
    elif pass_a:
        verdict = "PARTIAL (top-5 met; top-quintile failed)"
    else:
        verdict = "NULL — DIRECTION REVERSED"

    out = {
        "test_id": "Q032-F-06",
        "title": "Q 32:15 ↔ Q 41:38 sajda cross-reference within 14-sajda pair distribution",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": 20260509,
        "alpha_bon": 0.025,
        "n_sajda_verses": n,
        "n_pairs": n_pairs,
        "test_pair_primary": {
            "a": "32:15", "b": "41:38",
            "cosine": test_cosine,
            "rank_descending": test_rank,
            "percentile": test_percentile,
            "pass_top5": pass_a,
            "pass_top_quintile": pass_b,
        },
        "test_pair_sensitivity_v37": {
            "a": "32:15", "b": "41:37",
            "cosine": sens_cosine,
            "note": "Maghrebi sajda position (v 37 instead of v 38). For sensitivity only.",
        },
        "all_91_pairs_descending": pairs_sorted,
        "top10_pairs": pairs_sorted[:10],
        "raw_text_q32_15": raw_texts[(32, 15)],
        "raw_text_q41_38": raw_texts[(41, 38)],
        "raw_text_q41_37": text_41_37,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {verdict}")
    print(f"  Q32:15 ↔ Q41:38: cosine={test_cosine:.4f}, rank={test_rank}/{n_pairs}, percentile={test_percentile:.3f}")
    print(f"  sensitivity Q32:15 ↔ Q41:37: cosine={sens_cosine:.4f}")
    print(f"  top-5 pairs:")
    for r in pairs_sorted[:5]:
        print(f"    {r['a']} ↔ {r['b']}: {r['cosine']:.4f}")


if __name__ == "__main__":
    main()
