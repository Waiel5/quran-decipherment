#!/usr/bin/env python3
"""Q039-F-02 — Q 39 خلص (xlS) sincere-devotion root concentration.

Pre-reg: surahs/Q039-al-zumar/preregs/Q039-F-02-mukhlis-root-concentration-prereg.md
Pre-reg SHA: 092aed7c34f1223b3aae2c48f17e2c34ea1433dfa8eb9ccf4bfc4f7a39760b9b
Seed: 20260509  |  α_bon: 0.0125

Counts xlS root tokens per surah from QAC v0.4 morphology, computes Q 39 density
vs corpus baseline, and tests Late-Meccan concentration via Nöldeke phase.
"""

import csv
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[3]
PREREG_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "preregs" / "Q039-F-02-mukhlis-root-concentration-prereg.md"
EXPECTED_SHA = "092aed7c34f1223b3aae2c48f17e2c34ea1433dfa8eb9ccf4bfc4f7a39760b9b"
OUT_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "csv" / "Q039-F-02.json"
QAC_PATH = PROJECT_ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
QURAN_JSON = PROJECT_ROOT / "quran-text" / "quran-no-tashkeel.json"
REVELATION_CSV = PROJECT_ROOT / "data" / "revelation-order.csv"

SEED = 20260509
N_PERM = 10_000
ALPHA_BON = 0.0125
TARGET_ROOT = "xlS"
LATE_MECCAN_THRESHOLD = 65  # Nöldeke rank ≥ this is late-Middle Meccan or later


def verify_prereg_sha() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  found:    {sha}\n"
        )
        sys.exit(1)
    return sha


def load_xls_per_surah() -> tuple[dict[int, int], list[tuple[int, int]]]:
    """Returns (counts_per_surah, [(surah, verse), ...])."""
    counts: dict[int, int] = defaultdict(int)
    locations: list[tuple[int, int]] = []
    loc_re = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
    root_re = re.compile(r"ROOT:" + re.escape(TARGET_ROOT) + r"(?:\b|\|)")

    with QAC_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            m = loc_re.match(parts[0])
            if not m:
                continue
            features = parts[3]
            if not root_re.search(features):
                continue
            s, v = int(m.group(1)), int(m.group(2))
            counts[s] += 1
            locations.append((s, v))
    return dict(counts), locations


def load_words_per_surah() -> dict[int, int]:
    with QURAN_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    waqf_marks = set("ۚۖۗۘۙۛۜ۞")
    for entry in data:
        sid = entry["id"]
        total = 0
        for verse in entry["verses"]:
            text = verse["text"]
            clean = "".join(
                c for c in text
                if not (0x064B <= ord(c) <= 0x065F) and c not in waqf_marks
            )
            total += len([w for w in clean.split() if w.strip()])
        out[sid] = total
    return out


def load_noldeke_ranks() -> dict[int, int]:
    out = {}
    with REVELATION_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            out[int(row["mushaf_order"])] = int(row["noldeke_order"])
    return out


def load_verse_counts() -> dict[int, int]:
    with QURAN_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    return {entry["id"]: entry["total_verses"] for entry in data}


def main() -> None:
    sha = verify_prereg_sha()
    print(f"[OK] pre-reg SHA verified: {sha[:16]}...")

    xls_per_surah, xls_locations = load_xls_per_surah()
    words_per_surah = load_words_per_surah()
    noldeke = load_noldeke_ranks()
    verses_per_surah = load_verse_counts()

    total_xls = sum(xls_per_surah.values())
    total_words = sum(words_per_surah.values())
    print(f"[INFO] total corpus xlS root tokens: {total_xls}")
    print(f"[INFO] total corpus orthographic words: {total_words}")
    print(f"[INFO] corpus xlS density per 1000 words: {total_xls/total_words*1000:.4f}")

    q39_xls = xls_per_surah.get(39, 0)
    q39_words = words_per_surah[39]
    q39_density = q39_xls / q39_words * 1000
    rest_xls = total_xls - q39_xls
    rest_words = total_words - q39_words
    rest_density = rest_xls / rest_words * 1000

    print(f"[INFO] Q 39 xlS tokens: {q39_xls}")
    print(f"[INFO] Q 39 words: {q39_words}")
    print(f"[INFO] Q 39 density: {q39_density:.4f}/1000")
    print(f"[INFO] rest-of-corpus density: {rest_density:.4f}/1000")
    print(f"[INFO] Q 39 density / rest density = {q39_density/rest_density:.3f}×")

    # H1: permutation test where xlS-token positions are reshuffled across all 6,236 verses,
    # and we compute the Q 39 density at each shuffle.
    rng = np.random.default_rng(SEED)
    # Build a verse-level distribution of words to sample tokens
    # Each verse_id (s, v) has a known weight = its word count (so dense verses get more tokens)
    verse_word_weights = []
    verse_surahs = []
    for entry in load_quran_struct():
        for v_struct in entry["verses"]:
            text = v_struct["text"]
            clean = "".join(
                c for c in text
                if not (0x064B <= ord(c) <= 0x065F) and c not in set("ۚۖۗۘۙۛۜ۞")
            )
            wc = len([w for w in clean.split() if w.strip()])
            verse_word_weights.append(wc)
            verse_surahs.append(entry["id"])
    verse_word_weights = np.array(verse_word_weights, dtype=np.float64)
    verse_surahs = np.array(verse_surahs)
    weights_norm = verse_word_weights / verse_word_weights.sum()

    null_q39_densities = np.empty(N_PERM)
    for i in range(N_PERM):
        # Distribute total_xls tokens across verses by word-weight; multinomial
        sampled_counts = rng.multinomial(total_xls, weights_norm)
        # Sum into surahs
        per_surah = defaultdict(int)
        for vidx, c in enumerate(sampled_counts):
            if c:
                per_surah[verse_surahs[vidx]] += int(c)
        null_q39 = per_surah.get(39, 0)
        null_q39_densities[i] = null_q39 / q39_words * 1000

    p_h1 = float(np.mean(null_q39_densities >= q39_density))
    h1_pass = p_h1 <= ALPHA_BON

    # H2: Late-Meccan concentration of all corpus xlS tokens
    surahs_late = [s for s in xls_per_surah if noldeke.get(s, 0) >= LATE_MECCAN_THRESHOLD]
    xls_late = sum(xls_per_surah[s] for s in surahs_late)
    pct_xls_late = xls_late / total_xls if total_xls else 0
    # chance fraction = (verses in late-Meccan-or-later surahs) / 6236
    surahs_late_all = [s for s, r in noldeke.items() if r >= LATE_MECCAN_THRESHOLD]
    verses_late_all = sum(verses_per_surah[s] for s in surahs_late_all)
    total_verses = sum(verses_per_surah.values())
    chance_frac = verses_late_all / total_verses

    # Hypergeometric / binomial one-tailed
    from scipy.stats import binomtest
    bt = binomtest(xls_late, total_xls, chance_frac, alternative="greater")
    p_h2 = float(bt.pvalue)
    h2_pass = p_h2 <= ALPHA_BON

    if h1_pass and h2_pass:
        verdict = "CONFIRMED-DIRECTED"
    elif h1_pass or h2_pass:
        verdict = "PASS-DIRECTED"
    else:
        verdict = "NULL"

    # Per-surah density rank
    densities = [
        (s, xls_per_surah.get(s, 0), words_per_surah.get(s, 1),
         (xls_per_surah.get(s, 0) / words_per_surah.get(s, 1) * 1000) if words_per_surah.get(s, 0) > 0 else 0)
        for s in range(1, 115)
    ]
    densities_sorted = sorted(densities, key=lambda x: -x[3])
    q39_rank = next(i + 1 for i, (s, _, _, _) in enumerate(densities_sorted) if s == 39)
    surahs_with_xls = sum(1 for _, c, _, _ in densities if c > 0)

    print(f"\n[RESULT] H1 perm-p (Q 39 density ≥ null): {p_h1:.6f}  (α_bon = {ALPHA_BON})  → {'PASS' if h1_pass else 'FAIL'}")
    print(f"[RESULT] H2 Late-Meccan fraction = {pct_xls_late:.4f} (chance {chance_frac:.4f}); binomial-p = {p_h2:.6f} → {'PASS' if h2_pass else 'FAIL'}")
    print(f"[RESULT] Q 39 xlS density rank: {q39_rank}/114")
    print(f"[VERDICT] {verdict}")

    out = {
        "id": "Q039-F-02",
        "h_new_id": "H-NEW-1280",
        "title": "Q 39 خلص root concentration vs corpus + Late-Meccan distribution test",
        "prereg_path": str(PREREG_PATH.relative_to(PROJECT_ROOT)),
        "prereg_sha": EXPECTED_SHA,
        "prereg_sha_verified": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": 4,
        "bonferroni_family": "Q039-novel-tests",
        "target_root": TARGET_ROOT,
        "corpus_xls_total": total_xls,
        "q39_xls_count": q39_xls,
        "q39_words": q39_words,
        "q39_xls_density_per_1000": q39_density,
        "rest_corpus_density_per_1000": rest_density,
        "q39_xls_density_rank": q39_rank,
        "n_surahs_with_xls": surahs_with_xls,
        "h1_perm_p_q39_density": p_h1,
        "h1_null_mean_density": float(null_q39_densities.mean()),
        "h1_null_q975": float(np.quantile(null_q39_densities, 0.975)),
        "h1_pass": h1_pass,
        "late_meccan_threshold_noldeke": LATE_MECCAN_THRESHOLD,
        "xls_in_late_meccan": xls_late,
        "frac_xls_late_meccan": pct_xls_late,
        "chance_frac_late_meccan_verses": chance_frac,
        "h2_binomial_p": p_h2,
        "h2_pass": h2_pass,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "xls_locations_q39": [
            {"surah": s, "verse": v} for s, v in xls_locations if s == 39
        ],
        "xls_per_surah_top20": [
            {"surah": s, "count": c, "words": w, "density_per_1000": d}
            for s, c, w, d in densities_sorted[:20]
        ],
        "rules_tuple": [
            "no-tashkeel",
            "orthographic-token",
            "graphemes",
            "QAC-v0.4-root",
            "basmala-counted-only-in-Q1",
            "Hafs-Kufan",
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\n[OK] wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")


def load_quran_struct():
    with QURAN_JSON.open(encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    main()
