#!/usr/bin/env python3
"""
Q050-F-07 — Q 50 ق-letter density rank among 16 Meccan 30-50-verse surahs.

Pre-reg: surahs/Q050-qaf/preregs/Q050-F-07-qaf-density-vs-meccan-30-50-prereg.md
Pre-reg SHA256 (locked): 6a5530552dd610e3d995740a6771735f215f33c45f421f14f9e3eb8e8d97da54

Direction-locked: Q 50 RANK = 1 in this 16-surah class.
"""

import hashlib
import json
import random
import re
import sys
from pathlib import Path

# ---------------- SHA lock ----------------
PRE_REG = Path(__file__).resolve().parents[1] / "surahs" / "Q050-qaf" / "preregs" / "Q050-F-07-qaf-density-vs-meccan-30-50-prereg.md"
EXPECTED_SHA = "6a5530552dd610e3d995740a6771735f215f33c45f421f14f9e3eb8e8d97da54"
actual_sha = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
if actual_sha != EXPECTED_SHA:
    print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual_sha}")
    sys.exit(1)

SEED = 20260509
N_PERM = 10000

ROOT = Path(__file__).resolve().parents[1]
TEXT = ROOT / "quran-text" / "quran-no-tashkeel.json"
data = json.loads(TEXT.read_text())

# Build class: Meccan, 30 <= total_verses <= 50
CLASS = []
for s in data:
    if s.get("type") == "meccan" and 30 <= s["total_verses"] <= 50:
        CLASS.append(s)
class_ids = sorted([s["id"] for s in CLASS])
assert 50 in class_ids, "Q 50 must be in class"

# Letter counting: count ق grapheme, count all Arabic-script graphemes excluding whitespace/digits/punctuation
# Strip Tatweel U+0640.
TARGET = "ق"
TATWEEL = "ـ"
# Arabic letter Unicode block: U+0621..U+064A (excluding diacritics 064B-065F).
# no-tashkeel text already has tashkeel removed, but we strip any stray non-letters.
def is_arabic_letter(ch):
    code = ord(ch)
    return 0x0621 <= code <= 0x064A or code == 0x0671  # include alif wasla

def count_letters(text):
    text = text.replace(TATWEEL, "")
    total = 0
    qaf = 0
    for ch in text:
        if is_arabic_letter(ch):
            total += 1
            if ch == TARGET:
                qaf += 1
    return qaf, total

# Compute per-surah rate
per_surah = []
for s in CLASS:
    qaf_total = 0
    letter_total = 0
    for v in s["verses"]:
        # Basmala: only counted in Q 1. The no-tashkeel file does NOT prepend basmala to v1 of other surahs (verified separately).
        qaf_v, total_v = count_letters(v["text"])
        qaf_total += qaf_v
        letter_total += total_v
    rate = qaf_total / letter_total if letter_total > 0 else 0.0
    per_surah.append({
        "surah": s["id"],
        "name": s["transliteration"],
        "n_verses": s["total_verses"],
        "qaf_count": qaf_total,
        "letter_count": letter_total,
        "qaf_rate": rate,
    })

# Sort by qaf_rate descending
per_surah_sorted = sorted(per_surah, key=lambda r: -r["qaf_rate"])
q50_rank = next(i + 1 for i, r in enumerate(per_surah_sorted) if r["surah"] == 50)
q50_rate = next(r["qaf_rate"] for r in per_surah if r["surah"] == 50)

# Permutation null: randomly reassign qaf totals across surahs of the class (keeping each surah's letter_count fixed)
# That tests: under uniform-mixing of ق across the class's surface, how often does Q 50 land at rank 1?
rng = random.Random(SEED)
qaf_counts_pool = [r["qaf_count"] for r in per_surah]
letter_counts = [r["letter_count"] for r in per_surah]
ids = [r["surah"] for r in per_surah]
q50_idx = ids.index(50)

n_q50_rank_1 = 0
for _ in range(N_PERM):
    perm = qaf_counts_pool[:]
    rng.shuffle(perm)
    rates = [perm[i] / letter_counts[i] for i in range(len(perm))]
    max_rate = max(rates)
    if rates[q50_idx] == max_rate and rates.count(max_rate) == 1:
        n_q50_rank_1 += 1
perm_p_rank_1 = n_q50_rank_1 / N_PERM

# Verdict
if q50_rank == 1:
    verdict = "CONFIRMED-RANK-1"
elif q50_rank in (2, 3):
    verdict = "DIRECTIONAL-TOP-3"
else:
    verdict = "NULL"

pre_commit_violation = q50_rank > 8  # below median of 16

if pre_commit_violation:
    verdict += "-PRE-COMMIT-VIOLATION"

out = {
    "finding_id": "Q050-F-07",
    "prereg_sha256": EXPECTED_SHA,
    "date_run": "2026-05-09",
    "rules_tuple": "(no-tashkeel, grapheme-counting, mushaf-marks-stripped, basmala-not-counted-outside-Q1, Hafs-Kufan, Mashriqi)",
    "seed": SEED,
    "n_perm": N_PERM,
    "bonferroni_k": 1,
    "alpha": 0.05,
    "class_definition": "Meccan surahs with 30 <= total_verses <= 50",
    "class_size": len(per_surah),
    "class_ids": class_ids,
    "per_surah_sorted_desc": [
        {"rank": i + 1, **r, "qaf_rate": round(r["qaf_rate"], 6)}
        for i, r in enumerate(per_surah_sorted)
    ],
    "q50_rank": q50_rank,
    "q50_rate": round(q50_rate, 6),
    "q50_qaf_count": next(r["qaf_count"] for r in per_surah if r["surah"] == 50),
    "q50_letter_count": next(r["letter_count"] for r in per_surah if r["surah"] == 50),
    "perm_p_rank_1": round(perm_p_rank_1, 6),
    "pre_commit_violation": pre_commit_violation,
    "verdict": verdict,
}
OUT = ROOT / "surahs" / "Q050-qaf" / "csv" / "Q050-F-07.json"
OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"Q050-F-07: VERDICT={verdict}")
print(f"  Q 50 rank = {q50_rank} / {len(per_surah)}; rate = {q50_rate:.5f}")
print(f"  perm_p_rank_1 = {perm_p_rank_1:.4f}")
print(f"  output: {OUT.relative_to(ROOT)}")
