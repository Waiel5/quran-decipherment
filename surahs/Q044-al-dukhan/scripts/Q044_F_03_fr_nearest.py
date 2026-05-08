#!/usr/bin/env python3
"""Q044-F-03: Q 44's FR-roots nearest neighbors are short eschatological mufaṣṣal surahs.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-03-fr-nearest-eschatological-prereg.md
Pre-reg SHA256 (locked): 2c0d46d9b0e90a09c03ffdba10b3e494b5d0cd7b83a20f43cd77d564fb15e0bb
"""

import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-03-fr-nearest-eschatological-prereg.md"
PREREG_SHA_EXPECTED = "2c0d46d9b0e90a09c03ffdba10b3e494b5d0cd7b83a20f43cd77d564fb15e0bb"

OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-03.json"
FR_SOURCE = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"

# Locked operationalizations (pre-reg):
HM7 = {40, 41, 42, 43, 45, 46}  # Q44's HM-7 siblings (excluding self)
ESCHATO_MUFASSAL = set([32] + list(range(51, 115)))  # Q32 + all Q51-114

K = 7


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    actual = sha256_of(PREREG_PATH)
    if actual != PREREG_SHA_EXPECTED:
        print(f"FAIL: SHA mismatch\n  expected: {PREREG_SHA_EXPECTED}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA verified: {actual}")

    d = json.load(open(FR_SOURCE))
    mat = d["D_matrix_upper_triangular"]  # list of [i, j, dist] triples (1-indexed)
    D = {}
    for triple in mat:
        i, j, dist = triple
        D[(i, j)] = dist
        D[(j, i)] = dist

    # Q44 distances
    dists = []
    for s in range(1, 115):
        if s == 44:
            continue
        key = (44, s) if (44, s) in D else (s, 44)
        if key in D:
            dists.append((s, D[key]))
    dists.sort(key=lambda x: x[1])

    top7 = dists[:K]
    bot5 = dists[-5:]
    hm7_partners = {}
    for s in [40, 41, 42, 43, 45, 46]:
        key = (44, s) if (44, s) in D else (s, 44)
        hm7_partners[s] = D[key]

    # Classification
    in_eschato = sum(1 for s, _ in top7 if s in ESCHATO_MUFASSAL)
    in_hm7 = sum(1 for s, _ in top7 if s in HM7)

    print(f"\nQ44 top-{K} FR-nearest neighbors:")
    for s, dist in top7:
        cls = []
        if s in HM7:
            cls.append("HM7-sibling")
        if s in ESCHATO_MUFASSAL:
            cls.append("eschato-mufaṣṣal")
        cls_s = "+".join(cls) if cls else "other"
        print(f"  Q{s:>3} FR={dist:.4f}  [{cls_s}]")

    print(f"\nIn eschato-mufaṣṣal: {in_eschato}/{K}")
    print(f"In HM7-sibling: {in_hm7}/{K}")
    print(f"\nQ44 ↔ HM7 partners (mean = {sum(hm7_partners.values())/len(hm7_partners):.4f}):")
    for s, dist in sorted(hm7_partners.items(), key=lambda x: x[1]):
        print(f"  Q{s}: {dist:.4f}")

    # Verdict
    if in_eschato >= 4 and in_hm7 <= 1:
        verdict = "VINDICATED"
    elif in_eschato >= 3:
        verdict = "DIRECTIONAL"
    elif in_hm7 >= 4:
        verdict = "PRE-COMMIT VIOLATION (H₀ wins)"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "Q044-F-03",
        "prereg_sha": actual,
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "K": K,
        "top_K_nearest": [{"surah": s, "fr_dist": dist,
                            "in_HM7": s in HM7,
                            "in_eschato_mufassal": s in ESCHATO_MUFASSAL} for s, dist in top7],
        "bottom_5_farthest": [{"surah": s, "fr_dist": dist} for s, dist in bot5],
        "hm7_partners": [{"surah": s, "fr_dist": dist} for s, dist in sorted(hm7_partners.items(), key=lambda x: x[1])],
        "in_eschato_mufassal_top7": in_eschato,
        "in_HM7_top7": in_hm7,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w"), indent=2, ensure_ascii=False)
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
