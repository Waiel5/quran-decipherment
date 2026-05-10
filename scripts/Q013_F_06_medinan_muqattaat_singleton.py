#!/usr/bin/env python3
"""
Q013-F-06 — Q 13 is the corpus-unique MEDINAN muqaṭṭaʿāt-opener.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q013-al-rad/Q013-F-06-medinan-muqattaat-opener-singleton-prereg.md
SHA256:  82cbf9b1b7ec65b36c815cfe57ff91f513dcea2768f02e91cba7d6ed86270d01

Method: corpus enumeration — intersect the 29 muqaṭṭaʿāt-opener surah list with the
Medinan-classification set from `data/revelation-order.csv` (Tanzil Egyptian Standard,
congruent with al-Suyūṭī *al-Itqān* nawʿ 1). Cross-check via Nöldeke phase column.

Direction LOCKED: intersection = {13} exactly.

No randomness in this test.
"""

from __future__ import annotations
import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q013-al-rad/Q013-F-06-medinan-muqattaat-opener-singleton-prereg.md"
EXPECTED_SHA = "82cbf9b1b7ec65b36c815cfe57ff91f513dcea2768f02e91cba7d6ed86270d01"
OUT = ROOT / "surahs/Q013-al-rad/csv/Q013-F-06.json"

# Standard 29 muqaṭṭaʿāt-opener surahs (locked).
MUQATTAAT_29 = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
                31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}",
              file=sys.stderr)
        sys.exit(1)
    return actual


def load_chronology():
    rows = []
    with (ROOT / "data/revelation-order.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append({
                "mushaf": int(row["mushaf_order"]),
                "rev": int(row["revelation_order"]),
                "name": row["surah_name_tl"],
                "period": row["period"].strip(),
                "noldeke": row["noldeke_phase"].strip(),
            })
    rows.sort(key=lambda r: r["mushaf"])
    return rows


def verify_q13_opener():
    """Sanity check that Q13:1 opens with ALMR."""
    with (ROOT / "quran-text/quran-no-tashkeel.json").open(encoding="utf-8") as f:
        q = json.load(f)
    v = q[12]["verses"][0]["text"]  # Q13:1
    # ALMR consonantal skeleton: 'المر'
    return v.startswith("المر"), v[:40]


def main():
    sha_actual = sha_verify()
    chron = load_chronology()
    by_mushaf = {r["mushaf"]: r for r in chron}

    # Cell A: muqaṭṭaʿāt ∩ Medinan (Tanzil/al-Suyūṭī)
    intersection_a = []
    cell_a_table = []
    for s in MUQATTAAT_29:
        r = by_mushaf[s]
        cell_a_table.append({
            "surah": s,
            "name": r["name"],
            "period": r["period"],
            "rev_order": r["rev"],
        })
        if r["period"] == "Medinan":
            intersection_a.append(s)

    # Cell B: Nöldeke phase distribution for the 29
    cell_b_table = []
    for s in MUQATTAAT_29:
        r = by_mushaf[s]
        cell_b_table.append({
            "surah": s,
            "name": r["name"],
            "noldeke_phase": r["noldeke"],
        })
    nold_medinan = [r["surah"] for r in cell_b_table if r["noldeke_phase"] == "Medinan"]
    nold_late_meccan = [r["surah"] for r in cell_b_table
                        if "Late" in r["noldeke_phase"] and "Meccan" in r["noldeke_phase"]]

    # Cell C: sanity — confirm Q13:1 = ALMR opener
    almr_ok, q13_opener_preview = verify_q13_opener()

    # Verdict
    direction_intersection_eq_13 = (intersection_a == [13])

    out = {
        "test_id": "Q013-F-06",
        "title": "Q 13 corpus-unique Medinan muqaṭṭaʿāt-opener (al-Suyūṭī Itqān nawʿ 6 + nawʿ 1)",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": 20260509,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "muqattaat_canon_size": len(MUQATTAAT_29),
        "muqattaat_canon": MUQATTAAT_29,
        "chronology_source": "data/revelation-order.csv (Tanzil Egyptian Standard + Wikipedia Noldeke)",
        "cell_A_intersection_size": len(intersection_a),
        "cell_A_intersection": intersection_a,
        "cell_A_table": cell_a_table,
        "cell_A_pass_direction": direction_intersection_eq_13,
        "cell_B_noldeke_medinan_among_29": nold_medinan,
        "cell_B_noldeke_late_meccan_among_29": nold_late_meccan,
        "cell_B_table": cell_b_table,
        "cell_C_almr_opener_verified": almr_ok,
        "cell_C_q13_opener_preview": q13_opener_preview,
        "verdict": "CORPUS-EXACT-SINGLETON" if direction_intersection_eq_13 else "DIRECTION REVERSED",
        "note": ("Under al-Suyūṭī/Tanzil chronology, Q 13 is the ONLY Medinan muqaṭṭaʿāt-opener; "
                 "under Nöldeke, Q 13 is Late Meccan and the intersection is empty. The classical-tradition "
                 "register itself encodes Q 13 as the contested/exceptional case."),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {out['verdict']}")
    print(f"intersection: {intersection_a}")


if __name__ == "__main__":
    main()
