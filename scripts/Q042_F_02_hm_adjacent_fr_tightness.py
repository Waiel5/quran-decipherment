#!/usr/bin/env python3
"""Q042-F-02 — Q 41 ↔ Q 42 is the TIGHTEST adjacent ḥawāmīm pair (direction-locked).

Pre-reg: surahs/Q042-al-shura/preregs/Q042-F-02-hm-adjacent-fr-tightness-prereg.md
Direction: minimum-FR rank #1 among {(40,41),(41,42),(42,43),(43,44),(44,45),(45,46)}.
Reverse direction = pre-commit violation → publish as NULL with prominence.
"""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q042-al-shura/preregs/Q042-F-02-hm-adjacent-fr-tightness-prereg.md"
EXPECTED_SHA = "f737c0d8332e16f0c29922c85e0b5ada107fbca81363104ef2b28120d162107f"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT = ROOT / "surahs/Q042-al-shura/csv/Q042-F-02.json"

ADJ_PAIRS = [(40, 41), (41, 42), (42, 43), (43, 44), (44, 45), (45, 46)]
TARGET = (41, 42)


def main():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual} vs {EXPECTED_SHA}")

    d = json.loads(FR_MATRIX.read_text())
    ut = d["D_matrix_upper_triangular"]
    D = {}
    for a, b, v in ut:
        D[(int(a), int(b))] = float(v)
        D[(int(b), int(a))] = float(v)

    distances = []
    for a, b in ADJ_PAIRS:
        distances.append({"pair": [a, b], "label": f"Q{a}<->Q{b}", "fr": D[(a, b)]})

    sorted_by_fr = sorted(distances, key=lambda x: x["fr"])
    for i, e in enumerate(sorted_by_fr):
        e["rank"] = i + 1

    target_entry = next(e for e in sorted_by_fr if tuple(e["pair"]) == TARGET)
    target_rank = target_entry["rank"]
    target_fr = target_entry["fr"]
    tightest = sorted_by_fr[0]

    if target_rank == 1:
        verdict = "VINDICATED (Q 41<->Q 42 is tightest adjacent ḥawāmīm pair)"
        pre_commit_honored = True
    else:
        verdict = (
            f"NULL — pre-commit violation: Q 41<->Q 42 ranked {target_rank} of 6 "
            f"(tightest = {tightest['label']} at FR={tightest['fr']:.4f})"
        )
        pre_commit_honored = False

    out = {
        "id": "Q042-F-02",
        "title": "Q 41<->Q 42 as tightest adjacent ḥawāmīm pair (FR-distance)",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": "(no-tashkeel, orthographic-token, QAC-stem-roots, FR-distance on h-new-111)",
        "seed": 20260509,
        "fr_distances_adjacent_hm_pairs": sorted_by_fr,
        "target_pair": list(TARGET),
        "target_fr": target_fr,
        "target_rank_of_6": target_rank,
        "tightest_pair": tightest["pair"],
        "tightest_fr": tightest["fr"],
        "pre_commit_honored": pre_commit_honored,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Q042-F-02: {verdict}")
    for e in sorted_by_fr:
        print(f"  rank {e['rank']}: {e['label']:>14s}  FR={e['fr']:.6f}")


if __name__ == "__main__":
    main()
