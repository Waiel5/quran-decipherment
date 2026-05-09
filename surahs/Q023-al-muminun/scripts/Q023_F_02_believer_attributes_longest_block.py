#!/usr/bin/env python3
"""
Q023-F-02 — believer-attributes longest contiguous enumeration.

Pre-reg locked at SHA256 below. Verified at runtime.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PRE_REG = REPO / "surahs/Q023-al-muminun/preregs/Q023-F-02-believer-attributes-longest-block-prereg.md"
EXPECTED_SHA = "ae48a41c7410b543be980d505c5c0305a6f62e5fd9cce1d242463b3da9e1ef72"

QURAN_NT = REPO / "quran-text/quran-no-tashkeel.json"
OUT = REPO / "surahs/Q023-al-muminun/csv/Q023-F-02.json"


def verify_sha():
    actual = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}")
        sys.exit(1)
    print(f"[ok] Pre-reg SHA256 verified: {actual}")


def load_quran():
    with open(QURAN_NT) as f:
        return json.load(f)


# Markers for "believer-attribute" relative-pronoun continuation
# Locked at pre-reg (strict variant): verse must contain one of
#   - "والذين هم"   (and those who ...)
#   - "الذين هم"    (those who ...)  -- block-opener
#   - "أولئك"       (those!) -- typical block-closer at end of attribute list
#   - "والذين" (followed within a few tokens by a verb) -- coordinated relative
# We measure the LONGEST CONTIGUOUS RUN of verses where each contains the
# strict marker "والذين هم" or "الذين هم". The block-opener may be a verse
# starting with "الذين هم" OR a preceding verse (e.g. v. 1 of Q 23 "قد أفلح المؤمنون")
# whose immediate referent is the *al-muʾminūn / al-muttaqūn* subject.
STRICT_MARKERS = [
    "والذين هم",   # most distinctive plural relative + pronoun
    "الذين هم",    # bare opener
]
LOOSER_MARKERS = STRICT_MARKERS + [
    "والذين ",
    "الذين ",
    "أولئك",
]


def has_marker(text, markers):
    return any(m in text for m in markers)


def longest_contiguous_run_per_surah(quran, markers):
    """For each surah, find the longest contiguous run of verses where each verse contains a marker."""
    results = []
    for s in quran:
        sid = int(s["id"])
        verses = s["verses"]
        run = 0
        best = 0
        best_start = best_end = -1
        cur_start = -1
        for i, v in enumerate(verses):
            text = v.get("text", "")
            if has_marker(text, markers):
                if run == 0:
                    cur_start = i + 1  # verse number
                run += 1
                if run > best:
                    best = run
                    best_start = cur_start
                    best_end = i + 1
            else:
                run = 0
                cur_start = -1
        results.append({
            "surah": sid,
            "name": s.get("transliteration", ""),
            "longest_run_verses": best,
            "start_verse": best_start,
            "end_verse": best_end,
        })
    return results


def disbeliever_runs(quran):
    """Control: longest contiguous *disbeliever* block (الذين كفروا) per surah."""
    markers = ["الذين كفروا", "الذين كذبوا", "والذين كفروا", "والذين كذبوا"]
    return longest_contiguous_run_per_surah(quran, markers)


def main():
    verify_sha()
    quran = load_quran()

    # Comparator-block manual definitions (verse-counts, content-checks)
    # Pre-screened from the pre-reg
    comparators = {
        "Q23:1-11":  {"surah": 23, "start": 1,  "end": 11, "note": "qad aflaha al-muʾminūn opener + 10 trait-clauses"},
        "Q8:2-4":    {"surah": 8,  "start": 2,  "end": 4,  "note": "innama al-muʾminūn alladhīna idhā..."},
        "Q9:71":     {"surah": 9,  "start": 71, "end": 71, "note": "al-muʾminūn wa-al-muʾmināt baʿḍuhum awliyāʾ"},
        "Q70:22-35": {"surah": 70, "start": 22, "end": 35, "note": "illā al-muṣallīn alladhīna hum..."},
        "Q25:63-77": {"surah": 25, "start": 63, "end": 77, "note": "ʿibād al-Raḥmān list"},
        "Q32:15-16": {"surah": 32, "start": 15, "end": 16, "note": "innamā yuʾminu bi-āyātinā..."},
    }

    # Comparator empirical block-measurement (strict markers)
    comp_results = {}
    for name, defn in comparators.items():
        s_obj = next(x for x in quran if int(x["id"]) == defn["surah"])
        block = s_obj["verses"][defn["start"]-1:defn["end"]]
        n_verses = len(block)
        strict_marker_verses = sum(1 for v in block if has_marker(v.get("text", ""), STRICT_MARKERS))
        looser_marker_verses = sum(1 for v in block if has_marker(v.get("text", ""), LOOSER_MARKERS))
        comp_results[name] = {
            "surah": defn["surah"],
            "start": defn["start"],
            "end": defn["end"],
            "n_verses": n_verses,
            "strict_marker_verses": strict_marker_verses,
            "looser_marker_verses": looser_marker_verses,
            "note": defn["note"],
        }

    # Corpus-wide scan (strict markers)
    strict_per_surah = longest_contiguous_run_per_surah(quran, STRICT_MARKERS)
    strict_top5 = sorted(strict_per_surah, key=lambda x: -x["longest_run_verses"])[:5]

    # Corpus-wide scan (looser markers)
    looser_per_surah = longest_contiguous_run_per_surah(quran, LOOSER_MARKERS)
    looser_top5 = sorted(looser_per_surah, key=lambda x: -x["longest_run_verses"])[:5]

    # Disbeliever-attribute control
    disbel_per_surah = disbeliever_runs(quran)
    disbel_top5 = sorted(disbel_per_surah, key=lambda x: -x["longest_run_verses"])[:5]

    # Decision
    Q23_strict = next(x for x in strict_per_surah if x["surah"] == 23)
    Q23_looser = next(x for x in looser_per_surah if x["surah"] == 23)

    is_corpus_max_strict = all(
        Q23_strict["longest_run_verses"] >= x["longest_run_verses"] for x in strict_per_surah
    )
    is_corpus_max_looser = all(
        Q23_looser["longest_run_verses"] >= x["longest_run_verses"] for x in looser_per_surah
    )
    strict_max_value = max(x["longest_run_verses"] for x in strict_per_surah)
    looser_max_value = max(x["longest_run_verses"] for x in looser_per_surah)
    strict_ties = [x for x in strict_per_surah if x["longest_run_verses"] == strict_max_value]
    looser_ties = [x for x in looser_per_surah if x["longest_run_verses"] == looser_max_value]

    verdict = "PASS-DIRECTED-EXACT" if (
        Q23_strict["longest_run_verses"] == strict_max_value
        and len(strict_ties) == 1
    ) else (
        "PASS-DIRECTED-CORPUS-RANK-1-TIED"
        if Q23_strict["longest_run_verses"] == strict_max_value
        else "NULL"
    )

    result = {
        "finding_id": "Q023-F-02",
        "pre_reg_sha256": EXPECTED_SHA,
        "strict_marker_list": STRICT_MARKERS,
        "looser_marker_list": LOOSER_MARKERS,
        "comparators": comp_results,
        "Q23_strict_longest": Q23_strict,
        "Q23_looser_longest": Q23_looser,
        "strict_top5_corpus": strict_top5,
        "looser_top5_corpus": looser_top5,
        "strict_corpus_max": strict_max_value,
        "strict_ties_for_max": strict_ties,
        "looser_corpus_max": looser_max_value,
        "looser_ties_for_max": looser_ties,
        "disbeliever_top5_control": disbel_top5,
        "verdict": verdict,
        "bonferroni_family_alpha": 0.05 / 3,
        "rules_tuple": "(no-tashkeel, orthographic-token, Hafs-Kufan)",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps({
        "finding_id": result["finding_id"],
        "verdict": result["verdict"],
        "Q23_strict_longest_run": Q23_strict["longest_run_verses"],
        "strict_top5_corpus": strict_top5,
        "strict_ties_for_max": [x["surah"] for x in strict_ties],
        "disbeliever_top5_control": disbel_top5[:3],
    }, indent=2, ensure_ascii=False))
    print(f"\n[ok] wrote {OUT}")


if __name__ == "__main__":
    main()
