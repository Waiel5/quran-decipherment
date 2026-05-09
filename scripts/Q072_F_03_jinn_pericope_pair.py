#!/usr/bin/env python3
"""Q072-F-03 — Q 72:1-19 ↔ Q 46:29-32 jinn-pericope lexical-similarity vs length-matched null.

Pre-reg: surahs/Q072-al-jinn/preregs/Q072-F-03-jinn-pericope-pair-prereg.md
Pre-reg SHA256: ff4ec27cb7e802f4a090ba3e419466a1d6594d7598a21b1d38ca009cd944f4bc

Rules-tuple: (no-tashkeel, orthographic tokens (whitespace-split, no normalization),
              Jaccard on type-sets, length-matched permutation null over all eligible same-length windows,
              basmala-counted-only-in-Q1, Hafs-Kufan)
Seed: 20260509  |  Perms: 10000  |  Direction: PASS (Jaccard > 95%ile of null)
"""
import hashlib
import json
import os
import random
import statistics
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/preregs/Q072-F-03-jinn-pericope-pair-prereg.md"
EXPECTED_SHA = "ff4ec27cb7e802f4a090ba3e419466a1d6594d7598a21b1d38ca009cd944f4bc"

QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/csv/Q072-F-03.json"

SEED = 20260509
N_PERM = 10000
ALPHA = 0.05

# Diagnostic vocab for the jinn-event narrative
DIAGNOSTIC_TOKENS = ["الجن", "نفر", "نفرا", "استمع", "يستمعون", "سمعنا", "قرآنا", "القرآن",
                    "يهدي", "الهدى", "آمنا", "قومهم", "قومنا", "أحدا"]


def verify_sha():
    actual = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)


def main():
    verify_sha()

    qd = json.load(open(QURAN_NO_TASHKEEL))

    # Flat list of (sid, aid, tokens-list)
    flat = []
    for s in qd:
        for v in s["verses"]:
            flat.append((s["id"], v["id"], v["text"].split()))

    # Build Q 72:1-19 and Q 46:29-32 token sets
    q72_block_words = []
    for sid, aid, toks in flat:
        if sid == 72 and 1 <= aid <= 19:
            q72_block_words.extend(toks)
    q46_block_words = []
    for sid, aid, toks in flat:
        if sid == 46 and 29 <= aid <= 32:
            q46_block_words.extend(toks)

    q72_set = set(q72_block_words)
    q46_set = set(q46_block_words)
    obs_jaccard = jaccard(q72_set, q46_set)
    intersect = sorted(q72_set & q46_set)

    # Diagnostic-token presence in both
    diag_in_both = [t for t in DIAGNOSTIC_TOKENS if t in q72_set and t in q46_set]
    diag_in_q72_only = [t for t in DIAGNOSTIC_TOKENS if t in q72_set and t not in q46_set]
    diag_in_q46_only = [t for t in DIAGNOSTIC_TOKENS if t not in q72_set and t in q46_set]

    # Build null distribution: random verse-windows matching Q 46:29-32's word-count ±25%
    # excluding Q 72:1-19 and Q 46:29-32 themselves
    n_words_q46 = len(q46_block_words)
    lo, hi = int(n_words_q46 * 0.75), int(n_words_q46 * 1.25)

    # Enumerate all contiguous verse-windows in the corpus, indexed by surah
    # For each surah, sliding window of varying length until target word-count in band
    candidate_windows = []
    for s in qd:
        sid = s["id"]
        verses = s["verses"]
        n_v = len(verses)
        word_counts = [len(v["text"].split()) for v in verses]
        for start in range(n_v):
            cum_words = 0
            for end in range(start, n_v):
                cum_words += word_counts[end]
                aid_start = verses[start]["id"]
                aid_end = verses[end]["id"]
                # Skip the two reference blocks
                if sid == 72 and aid_start <= 19 and aid_end >= 1:
                    continue
                if sid == 46 and aid_start <= 32 and aid_end >= 29:
                    continue
                if cum_words > hi:
                    break
                if lo <= cum_words <= hi:
                    # Capture this window
                    toks = []
                    for k in range(start, end + 1):
                        toks.extend(verses[k]["text"].split())
                    candidate_windows.append({"sid": sid, "aid_start": aid_start,
                                              "aid_end": aid_end, "n_words": cum_words,
                                              "tokens": set(toks)})
    n_candidates = len(candidate_windows)

    # Sample 10,000 windows with replacement (since 10000 >> we want a stable null;
    # if n_candidates < N_PERM, sample with replacement)
    rng = random.Random(SEED)
    null_jaccards = []
    for _ in range(N_PERM):
        w = rng.choice(candidate_windows)
        null_jaccards.append(jaccard(q72_set, w["tokens"]))

    null_mean = statistics.mean(null_jaccards)
    null_sd = statistics.stdev(null_jaccards)
    p_one_sided_ge = sum(1 for x in null_jaccards if x >= obs_jaccard) / N_PERM
    z = (obs_jaccard - null_mean) / null_sd if null_sd > 0 else 0.0
    pct = sum(1 for x in null_jaccards if x < obs_jaccard) / N_PERM  # percentile of obs

    # Verdict
    direction_correct = obs_jaccard > null_mean
    primary_pass = p_one_sided_ge <= ALPHA
    if not direction_correct:
        verdict = "NULL (pre-commit-violation: direction-reversed)"
    elif primary_pass:
        verdict = "PASS"
    else:
        verdict = "DIRECTIONAL (direction correct, p>0.05)"

    out = {
        "test_id": "Q072-F-03",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "q72_block": {"surah": 72, "verses": "1-19", "n_words": len(q72_block_words),
                      "n_types": len(q72_set)},
        "q46_block": {"surah": 46, "verses": "29-32", "n_words": n_words_q46,
                      "n_types": len(q46_set)},
        "observed_jaccard": obs_jaccard,
        "intersection_size": len(q72_set & q46_set),
        "intersection_tokens": intersect,
        "diagnostic_tokens_in_both": diag_in_both,
        "diagnostic_tokens_in_q72_only": diag_in_q72_only,
        "diagnostic_tokens_in_q46_only": diag_in_q46_only,
        "null_band_word_count": [lo, hi],
        "n_candidate_windows": n_candidates,
        "null": {
            "mean": null_mean,
            "sd": null_sd,
            "min": min(null_jaccards),
            "max": max(null_jaccards),
            "p_one_sided_ge": p_one_sided_ge,
            "percentile_of_obs": pct,
            "z_score": z,
        },
        "direction_correct": direction_correct,
        "primary_pass": primary_pass,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"Q072-F-03 verdict: {verdict}")
    print(f"  obs Jaccard = {obs_jaccard:.4f}; intersection size = {len(q72_set & q46_set)}")
    print(f"  null mean = {null_mean:.4f}; sd = {null_sd:.4f}; p (one-sided ≥) = {p_one_sided_ge:.4f}; z = {z:.3f}")
    print(f"  n candidate windows = {n_candidates}")
    print(f"  diagnostic in both: {diag_in_both}")
    print(f"Written: {OUT_PATH}")


if __name__ == "__main__":
    main()
