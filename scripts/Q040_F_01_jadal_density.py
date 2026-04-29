"""
Q040-F-01: Q 40 *jadal* (j-d-l) root density vs corpus baseline.

Pre-reg SHA256: 8905026b7fa0b8d415c037585d4f3d5b1b80306f1ef0220b54a5bb2992dbb752
Pre-reg path: surahs/Q040-ghafir/preregs/Q040-F-01-jadal-density-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys
import re
from collections import Counter

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q040-ghafir/preregs/Q040-F-01-jadal-density-prereg.md"
EXPECTED_SHA = "8905026b7fa0b8d415c037585d4f3d5b1b80306f1ef0220b54a5bb2992dbb752"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q040-ghafir/csv/Q040-F-01.json"

def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")

def parse_qac():
    """Parse QAC v0.4 morphology, returning per-surah token-counts and per-surah j-d-l counts."""
    surah_tokens = Counter()
    surah_jadal = Counter()
    target_root = "jdl"  # Buckwalter for ج-د-ل
    with open(QAC_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # QAC format: location	form	tag	features
            # location like "(2:1:1:1)" — surah:verse:word:segment
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            # Extract surah
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m:
                continue
            surah = int(m.group(1))
            seg = int(m.group(4))
            # Count one token per word (segment 1 only, to avoid double counting)
            if seg == 1:
                surah_tokens[surah] += 1
            # Check root
            # Features are key:val pairs separated by '|'
            # Root token Buckwalter: ROOT:jdl
            root_match = re.search(r"ROOT:([^|]+)", features)
            if root_match:
                root = root_match.group(1)
                if root == target_root:
                    surah_jadal[surah] += 1
    return surah_tokens, surah_jadal

def main():
    verify_prereg()
    surah_tokens, surah_jadal = parse_qac()

    # Compute per-surah jadal-density per 1000 tokens
    densities = {}
    for s in range(1, 115):
        toks = surah_tokens.get(s, 0)
        jad = surah_jadal.get(s, 0)
        densities[s] = (jad / toks * 1000) if toks > 0 else 0.0

    # Q 40 stats
    q40_density = densities[40]

    # Corpus baseline (excluding Q 40)
    other = [d for s, d in densities.items() if s != 40]
    n = len(other)
    mean = sum(other) / n
    var = sum((x - mean) ** 2 for x in other) / n
    sd = var ** 0.5
    z = (q40_density - mean) / sd if sd > 0 else 0.0

    # Top-5 densest surahs
    ranked = sorted(densities.items(), key=lambda kv: -kv[1])[:8]

    # Direction check
    direction_ok = q40_density > mean
    if z > 1.0:
        verdict = "DIRECTIONAL_VINDICATION"
    elif z < -1.0:
        verdict = "PRECOMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q040-F-01",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "Q40_jadal_count": surah_jadal.get(40, 0),
        "Q40_total_tokens": surah_tokens.get(40, 0),
        "Q40_jadal_per_1000": round(q40_density, 4),
        "corpus_mean_excl_Q40": round(mean, 4),
        "corpus_sd_excl_Q40": round(sd, 4),
        "Q40_z_score": round(z, 3),
        "direction_predicted": "Q40 > corpus_mean",
        "direction_observed": "Q40 > corpus_mean" if direction_ok else "Q40 <= corpus_mean",
        "verdict": verdict,
        "top_8_jadal_density_surahs": [(int(s), round(d, 4)) for s, d in ranked],
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
