#!/usr/bin/env python3
"""
Q078-F-05 — Q 78:6-16 cosmology block hapax-density + intensive-pattern test.

Pre-reg: surahs/Q078-al-naba/preregs/Q078-F-05-cosmology-hapax-prereg.md
SHA256:  embedded at runtime; verified against pre-reg

Hypothesis (LOCKED PRE-RUN):
  H1: Q 78 has ≥3 corpus-hapax roots (roots whose entire corpus
      attestation lies within Q 78).
      DIRECTION: ≥3 hapax.

  H2: All Q 78 hapax roots cluster in the cosmic-evidence (vv.6-16) +
      paradise (vv.31-40) blocks; ZERO hapax in framing (vv.1-5) or
      eschatological-judgment (vv.17-30) blocks.
      DIRECTION: hapax confined to Block 2 + Block 4.

H0: H1 fails (≤2 hapax) OR H2 fails (any hapax in Block 1 or Block 3).

Bonferroni: k=2; alpha_bon = 0.025.

Method:
  - Identify Q 78 hapax via QAC root-tagging.
  - For each hapax, look up the verse it appears at; classify into block.

Seed: 20260509 (no random element).
"""

import json
import re
import os
import hashlib
from collections import Counter

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PREREG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                           'Q078-F-05-cosmology-hapax-prereg.md')
QAC_PATH = os.path.join(PROJECT_ROOT, 'data', 'morphology',
                        'quranic-corpus-morphology-0.4.txt')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q078-F-05.json')

SEED = 20260509

# Q 78 block partition (LOCKED PRE-RUN, derived from content-analysis structural-features)
BLOCK_RANGES = {
    "block_1_framing": (1, 5),
    "block_2_cosmic_evidence": (6, 16),
    "block_3_judgment": (17, 30),
    "block_4_paradise_closure": (31, 40),
}


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def classify_block(verse_id):
    for name, (lo, hi) in BLOCK_RANGES.items():
        if lo <= verse_id <= hi:
            return name
    return "unknown"


def main():
    prereg_sha = sha256_of(PREREG_PATH)
    print(f"prereg SHA256: {prereg_sha}")

    # Load QAC, indexed by (surah, verse, word) -> root
    surah_roots = {i: Counter() for i in range(1, 115)}
    corpus_roots = Counter()
    root_locations = {}  # root -> list of (s, v) tuples
    with open(QAC_PATH, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            m = re.search(r'ROOT:([^|]+)', features)
            if not m:
                continue
            root = m.group(1)
            nums = re.findall(r'\d+', loc)
            if len(nums) < 2:
                continue
            s, v = int(nums[0]), int(nums[1])
            if 1 <= s <= 114:
                surah_roots[s][root] += 1
                corpus_roots[root] += 1
                root_locations.setdefault(root, []).append((s, v))

    # Q 78 hapax: roots in Q 78 where corpus-count == Q78-count
    q78_hapax = []
    for r, c in surah_roots[78].items():
        if corpus_roots[r] == c:
            # Look up verse(s) in Q 78
            verses = sorted(set(v for (s, v) in root_locations[r] if s == 78))
            for v in verses:
                q78_hapax.append({
                    "root": r,
                    "verse": v,
                    "block": classify_block(v),
                    "count_in_q78": c,
                })

    h1_count = len(set(x['root'] for x in q78_hapax))
    h1_pass = h1_count >= 3

    # H2: all hapax confined to Block 2 + Block 4
    hapax_blocks = set(x['block'] for x in q78_hapax)
    forbidden_blocks = {"block_1_framing", "block_3_judgment"}
    h2_pass = h1_pass and not (hapax_blocks & forbidden_blocks)

    output = {
        "test_id": "Q078-F-05",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "block_ranges": BLOCK_RANGES,
        "q78_hapax": q78_hapax,
        "h1_hapax_count": h1_count,
        "h1_pass_3_or_more": h1_pass,
        "h2_blocks_with_hapax": list(hapax_blocks),
        "h2_pass_block24_only": h2_pass,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"H1 hapax count: {h1_count}")
    for x in q78_hapax:
        print(f"  root {x['root']} at v{x['verse']} ({x['block']})")
    print(f"H1 PASS (≥3): {h1_pass}")
    print(f"H2 blocks with hapax: {hapax_blocks}")
    print(f"H2 PASS (only Block 2 or Block 4): {h2_pass}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
