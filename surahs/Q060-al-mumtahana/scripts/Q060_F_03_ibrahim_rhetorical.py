#!/usr/bin/env python3
"""
Q060-F-03 — Q 60 vs Q 14 vs Q 21 Ibrahim-presentation lexical orthogonality.

Pre-reg SHA256: 9c24f9d77ad552e92e93df43c06b3537ad446498e03af665de609e1650e7350b

Hypothesis (joint):
  H1a: Set A (disownment-alliance lexicon) dominates Q 60's Ibrahim pericope.
  H1b: Set B (monotheist-prayer lexicon)    dominates Q 14's pericope.
  H1c: Set C (idol-smasher narrative lexicon) dominates Q 21's pericope.

Lemma sets are LOCKED in the pre-reg before observation.

Decision rule: CONFIRMED if all 3 cells dominate; PARTIAL if 2; NULL if ≤1.
"""
import json
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PREREG_SHA = "9c24f9d77ad552e92e93df43c06b3537ad446498e03af665de609e1650e7350b"

# Pre-committed lemma sets (locked in pre-reg)
SET_A = ["أسوة", "برآء", "بريء", "العداوة", "البغضاء", "مودة", "أولياء", "تتخذوا", "كفرنا", "تتولوا"]
SET_B = ["البلد", "آمنا", "الأصنام", "يقيم الصلاة", "الجبلة", "مهاجر", "الدعاء", "اجعل"]
SET_C = ["كسر", "جذاذا", "فتى", "بردا", "سلاما", "كيدا", "إفك", "آلهة"]

# Pre-committed pericopes (anchored on Ibrahim mentions)
PERICOPES = {
    "Q60": (60, 3, 9),    # vv 3-9 around Ibrahim mention at v 4
    "Q14": (14, 34, 40),  # vv 34-40 around Ibrahim mention at v 35
    "Q21": (21, 50, 74),  # vv 50-74 around Ibrahim mentions at vv 51, 60, 62, 69
}

PREDICTIONS = {"Set A": "Q60", "Set B": "Q14", "Set C": "Q21"}

def verify_prereg_sha(prereg_path):
    h = hashlib.sha256(prereg_path.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        raise RuntimeError(f"Pre-reg SHA mismatch: expected {PREREG_SHA}, got {h}")
    return h

def get_pericope_text(data, surah_id, start, end):
    surah = data[surah_id - 1]
    return " ".join(v["text"] for v in surah["verses"] if start <= v["id"] <= end)

def main():
    prereg_path = REPO_ROOT / "surahs" / "Q060-al-mumtahana" / "preregs" / "Q060-F-03-ibrahim-rhetorical-positioning-prereg.md"
    sha_check = verify_prereg_sha(prereg_path)
    print(f"Pre-reg SHA verified: {sha_check[:16]}...")

    text_path = REPO_ROOT / "quran-text" / "quran-no-tashkeel.json"
    data = json.load(open(text_path))

    pericope_texts = {label: get_pericope_text(data, *v) for label, v in PERICOPES.items()}

    sets = {"Set A": SET_A, "Set B": SET_B, "Set C": SET_C}
    counts = {}
    for set_name, lemmas in sets.items():
        cell = {}
        for label, text in pericope_texts.items():
            total = sum(text.count(lem) for lem in lemmas)
            cell[label] = total
        counts[set_name] = cell

    print("\nCell counts:")
    for set_name, cell in counts.items():
        print(f"  {set_name}: {cell}")

    cells_passing = 0
    print("\nDominance evaluation:")
    for set_name, predicted in PREDICTIONS.items():
        cell = counts[set_name]
        target_count = cell[predicted]
        others_max = max(c for label, c in cell.items() if label != predicted)
        passes = target_count > others_max
        cells_passing += passes
        print(f"  {set_name} → {predicted}: count={target_count}, max-other={others_max}, pass={passes}")

    if cells_passing == 3:
        verdict = "CONFIRMED"
    elif cells_passing == 2:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    print(f"\nCells passing: {cells_passing}/3, verdict: {verdict}")

    return {"counts": counts, "cells_passing": cells_passing, "verdict": verdict}

if __name__ == "__main__":
    main()
