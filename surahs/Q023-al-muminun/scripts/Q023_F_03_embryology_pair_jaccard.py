#!/usr/bin/env python3
"""
Q023-F-03 — embryology pericope Q 23:12-14 vs Q 22:5 Jaccard vs length-matched null.

Pre-reg locked at SHA256 below. Verified at runtime.
"""

import hashlib
import json
import random
import re
import sys
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PRE_REG = REPO / "surahs/Q023-al-muminun/preregs/Q023-F-03-embryology-pair-q22-q23-prereg.md"
EXPECTED_SHA = "4518ad85b89225a206d2042b13e1af25205de29474fa7c3612c2eb74a44e9c80"

QURAN_NT = REPO / "quran-text/quran-no-tashkeel.json"
OUT = REPO / "surahs/Q023-al-muminun/csv/Q023-F-03.json"

SEED = 20260509
N_PERMS = 10000


def verify_sha():
    actual = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}")
        sys.exit(1)
    print(f"[ok] Pre-reg SHA256 verified: {actual}")


def tokenize(text):
    """Orthographic-token split on whitespace; drop punctuation."""
    text = re.sub(r"[^؀-ۿ\s]", " ", text)
    toks = [t for t in text.split() if t]
    return toks


def light_stem(tok):
    """Drop common Arabic clitic prefixes ال / و / ف / ب / ل / ك (single-letter), with priority order."""
    # Recursively strip up to a small number of clitics
    s = tok
    for _ in range(3):
        if s.startswith("ال") and len(s) > 3:
            s = s[2:]
        elif s[:1] in ("و", "ف", "ب", "ل", "ك") and len(s) > 2:
            s = s[1:]
        else:
            break
    return s


def get_verses(quran, sid, start, end):
    """Return list of verse-strings for surah sid, verses [start, end] inclusive (1-indexed)."""
    s_obj = next(x for x in quran if int(x["id"]) == sid)
    return [v.get("text", "") for v in s_obj["verses"][start-1:end]]


def jaccard(A, B):
    sA = set(A)
    sB = set(B)
    if not (sA | sB):
        return 0.0
    return len(sA & sB) / len(sA | sB)


def main():
    verify_sha()
    with open(QURAN_NT) as f:
        quran = json.load(f)

    # Targets
    Q23_12_14 = get_verses(quran, 23, 12, 14)
    Q22_5 = get_verses(quran, 22, 5, 5)
    Q75_37_40 = get_verses(quran, 75, 37, 40)

    Q23_toks_raw = sum((tokenize(v) for v in Q23_12_14), [])
    Q22_toks_raw = sum((tokenize(v) for v in Q22_5), [])
    Q75_toks_raw = sum((tokenize(v) for v in Q75_37_40), [])
    Q23_toks_stem = [light_stem(t) for t in Q23_toks_raw]
    Q22_toks_stem = [light_stem(t) for t in Q22_toks_raw]
    Q75_toks_stem = [light_stem(t) for t in Q75_toks_raw]

    # Observed
    J_obs_raw = jaccard(Q23_toks_raw, Q22_toks_raw)
    J_obs_stem = jaccard(Q23_toks_stem, Q22_toks_stem)
    J_q23_q75_raw = jaccard(Q23_toks_raw, Q75_toks_raw)
    J_q22_q75_raw = jaccard(Q22_toks_raw, Q75_toks_raw)
    # Control: Q 23:1-3 (non-embryology) vs Q 22:5
    Q23_1_3 = get_verses(quran, 23, 1, 3)
    Q23_1_3_toks = sum((tokenize(v) for v in Q23_1_3), [])
    J_control_raw = jaccard(Q23_1_3_toks, Q22_toks_raw)

    print(f"[info] Q 23:12-14 tokens: {len(Q23_toks_raw)} raw / {len(set(Q23_toks_raw))} unique")
    print(f"[info] Q 22:5    tokens: {len(Q22_toks_raw)} raw / {len(set(Q22_toks_raw))} unique")
    print(f"[info] J_obs (Q 23:12-14 ↔ Q 22:5, raw): {J_obs_raw:.6f}")
    print(f"[info] J_obs (Q 23:12-14 ↔ Q 22:5, stem): {J_obs_stem:.6f}")
    print(f"[info] J (Q 23:12-14 ↔ Q 75:37-40, raw): {J_q23_q75_raw:.6f}")
    print(f"[info] J (Q 22:5 ↔ Q 75:37-40, raw): {J_q22_q75_raw:.6f}")
    print(f"[info] J_control (Q 23:1-3 ↔ Q 22:5, raw): {J_control_raw:.6f}")

    # Build flat verse index: list of (sid, vnum, text)
    verses_flat = []
    for s in quran:
        sid = int(s["id"])
        for vidx, v in enumerate(s["verses"], start=1):
            verses_flat.append((sid, vidx, v.get("text", "")))
    n_verses = len(verses_flat)
    print(f"[info] corpus has {n_verses} verses total")

    # Build per-(sid) start indices for contiguous 3-verse picks
    rng = random.Random(SEED)
    # Length-matched null:
    # V_A = 3-verse contiguous block from anywhere
    # V_B = single verse from anywhere
    # exclude exact target pair
    target_A = (23, 12, 14)
    target_B = (22, 5)
    null_raw = []
    null_stem = []
    valid = 0
    attempts = 0
    while valid < N_PERMS and attempts < N_PERMS * 5:
        attempts += 1
        # pick 3-verse block
        block_start_idx = rng.randrange(0, n_verses - 2)
        sid0, v0, _ = verses_flat[block_start_idx]
        sid1, v1, _ = verses_flat[block_start_idx + 1]
        sid2, v2, _ = verses_flat[block_start_idx + 2]
        # require same surah
        if not (sid0 == sid1 == sid2):
            continue
        # build block texts
        A_texts = [verses_flat[block_start_idx + k][2] for k in range(3)]
        # pick 1-verse
        b_idx = rng.randrange(0, n_verses)
        sidB, vB, B_text = verses_flat[b_idx]
        # exclude exact target match
        if sid0 == 23 and v0 == 12 and sidB == 22 and vB == 5:
            continue
        A_toks = sum((tokenize(t) for t in A_texts), [])
        B_toks = tokenize(B_text)
        if not A_toks or not B_toks:
            continue
        null_raw.append(jaccard(A_toks, B_toks))
        null_stem.append(jaccard([light_stem(t) for t in A_toks], [light_stem(t) for t in B_toks]))
        valid += 1

    def upper_tail_p(obs, null):
        k = sum(1 for v in null if v >= obs)
        return (k + 1) / (len(null) + 1)

    p_raw = upper_tail_p(J_obs_raw, null_raw)
    p_stem = upper_tail_p(J_obs_stem, null_stem)

    null_raw_sorted = sorted(null_raw)
    null_stem_sorted = sorted(null_stem)
    pct95_raw = null_raw_sorted[int(0.95 * len(null_raw))]
    median_raw = null_raw_sorted[len(null_raw) // 2]
    median_stem = null_stem_sorted[len(null_stem) // 2]

    verdict = (
        "PASS-DIRECTED" if p_raw <= 0.05 and J_obs_raw > median_raw
        else "PRE-COMMIT-VIOLATION-NULL" if J_obs_raw < median_raw
        else "NULL"
    )

    result = {
        "finding_id": "Q023-F-03",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_perms_valid": valid,
        "n_perms_attempts": attempts,
        "primary_pair": {"A": "Q 23:12-14", "B": "Q 22:5"},
        "J_obs_raw": J_obs_raw,
        "J_obs_stem": J_obs_stem,
        "J_q23_q75_raw": J_q23_q75_raw,
        "J_q22_q75_raw": J_q22_q75_raw,
        "J_control_q23_1_3_q22_5_raw": J_control_raw,
        "Q23_12_14_tokens_unique": len(set(Q23_toks_raw)),
        "Q22_5_tokens_unique": len(set(Q22_toks_raw)),
        "intersection_tokens": sorted(set(Q23_toks_raw) & set(Q22_toks_raw)),
        "null_raw": {
            "n": len(null_raw),
            "mean": sum(null_raw) / len(null_raw),
            "median": median_raw,
            "p95": pct95_raw,
            "min": min(null_raw),
            "max": max(null_raw),
        },
        "null_stem": {
            "n": len(null_stem),
            "median": median_stem,
            "mean": sum(null_stem) / len(null_stem),
        },
        "p_upper_tail_raw": p_raw,
        "p_upper_tail_stem": p_stem,
        "verdict": verdict,
        "bonferroni_family_alpha": 0.05 / 3,
        "verdict_bonferroni": (
            "PASS-DIRECTED-BONF" if p_raw <= 0.05/3 and J_obs_raw > median_raw else "NOT-PASS-BONF"
        ),
        "rules_tuple": "(no-tashkeel, orthographic-token-Jaccard, Hafs-Kufan)",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps({
        "finding_id": result["finding_id"],
        "verdict": result["verdict"],
        "J_obs_raw": J_obs_raw,
        "p_upper_tail_raw": p_raw,
        "null_raw_median": median_raw,
        "null_raw_p95": pct95_raw,
        "intersection_size": len(set(Q23_toks_raw) & set(Q22_toks_raw)),
    }, indent=2, ensure_ascii=False))
    print(f"\n[ok] wrote {OUT}")


if __name__ == "__main__":
    main()
