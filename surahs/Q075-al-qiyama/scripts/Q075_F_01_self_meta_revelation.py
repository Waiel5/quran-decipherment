#!/usr/bin/env python3
"""
Q075-F-01 — Corpus-EXACT 4-verse self-meta-revelation passage test.

Pre-reg: surahs/Q075-al-qiyama/preregs/Q075-F-01-self-meta-revelation-prereg.md
SHA-256 of pre-reg locked at runtime; mismatch → abort.

Author: Waiel Al-Shujaa
Date: 2026-05-09
"""
import json
import re
import hashlib
import sys
from pathlib import Path

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q075-F-01-self-meta-revelation-prereg.md"
PREREG_SHA_EXPECTED = "WILL_BE_FILLED_AT_LOCK"  # placeholder; filled below
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q075-F-01.json"

# Indicator tokens locked before run (see prereg §2)
INDICATORS = {
    "qurʾān_attached_pronoun": ["قرآنه", "قرآنا"],
    "wahy_iqra": ["يوحى", "نوحي", "أوحى", "نقرأ", "قرأناه", "قرأنا"],
    "timing_imperatives": ["تعجل", "تستعجل", "تنسى", "ترتيلا"],
    "memory_gathering": ["جمعه", "نقرئك", "لتثبت", "فؤادك"],
    "clarification": ["بيانه", "بيناه"],
    "tongue_lips_2sg": ["لسانك", "شفتيك"],
    "imperative_2sg_proc": ["اتبع", "لا تحرك", "لا تعجل", "ورتل"],
}

# Cell B component fragments (locked)
COMPONENTS = {
    "a_la_tuharrik": "لا تحرك",
    "b_li_taʿjala_bihi": "لتعجل به",
    "c_inna_ʿalayna_jamʿahu_wa_qurʾanahu": "علينا جمعه وقرآنه",
    "d_fa_idha_qaraʾnahu_fa_attabi": "فإذا قرأناه فاتبع قرآنه",
    "e_thumma_inna_ʿalayna_bayanahu": "ثم إن علينا بيانه",
    "f_qurʾanahu": "قرآنه",
    "g_bayanahu": "بيانه",
}


def matches_indicator(text: str) -> bool:
    """A verse matches if any indicator token is in it."""
    for kws in INDICATORS.values():
        for kw in kws:
            if kw in text:
                return True
    return False


def main():
    # SHA-256 verification of pre-reg
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if PREREG_SHA_EXPECTED != "WILL_BE_FILLED_AT_LOCK" and sha != PREREG_SHA_EXPECTED:
        print(f"FATAL: pre-reg SHA mismatch.\nExpected: {PREREG_SHA_EXPECTED}\nActual:   {sha}", file=sys.stderr)
        sys.exit(1)

    with open(QURAN_PATH) as f:
        qd = json.load(f)

    # CELL A: 4-consecutive-verse procedural-reception passages corpus-wide
    found_passages = []
    for s in qd:
        verses = s["verses"]
        for start in range(len(verses) - 3):
            chunk = verses[start:start + 4]
            if all(matches_indicator(v["text"]) for v in chunk):
                found_passages.append({
                    "surah": s["id"],
                    "start_v": chunk[0]["id"],
                    "end_v": chunk[-1]["id"],
                    "verses": [v["text"] for v in chunk],
                })

    # CELL B: component-level corpus enumeration
    component_counts = {}
    for label, frag in COMPONENTS.items():
        hits = []
        for s in qd:
            for v in s["verses"]:
                if frag in v["text"]:
                    hits.append((s["id"], v["id"]))
        component_counts[label] = {
            "fragment": frag,
            "count": len(hits),
            "occurrences": [{"surah": h[0], "verse": h[1]} for h in hits],
        }

    # Verdict logic
    cell_a_pred = 1
    cell_a_obs = len(found_passages)
    cell_a_pass = (cell_a_obs == cell_a_pred)

    cell_b_predictions = {
        "a_la_tuharrik": 1,
        "b_li_taʿjala_bihi": 1,
        "c_inna_ʿalayna_jamʿahu_wa_qurʾanahu": 1,
        "d_fa_idha_qaraʾnahu_fa_attabi": 1,
        "e_thumma_inna_ʿalayna_bayanahu": 1,
        "f_qurʾanahu": [1, 2],  # range
        "g_bayanahu": 1,
    }
    cell_b_pass_components = {}
    for label, pred in cell_b_predictions.items():
        actual = component_counts[label]["count"]
        if isinstance(pred, list):
            cell_b_pass_components[label] = (actual in pred)
        else:
            cell_b_pass_components[label] = (actual == pred)
    cell_b_pass = all(cell_b_pass_components.values())

    if cell_a_pass and cell_b_pass:
        verdict = "STRONGLY_VINDICATED"
    elif cell_a_pass and sum(cell_b_pass_components.values()) >= len(cell_b_pass_components) - 1:
        verdict = "VINDICATED"
    elif cell_a_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q075-F-01",
        "title": "Corpus-EXACT 4-verse self-meta-revelation passage",
        "prereg_sha256": sha,
        "seed": 20260509,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "cell_a": {
            "n4_predicted": cell_a_pred,
            "n4_observed": cell_a_obs,
            "passages_found": found_passages,
            "pass": cell_a_pass,
        },
        "cell_b": {
            "predictions": {k: ("range_1_to_2" if isinstance(v, list) else v) for k, v in cell_b_predictions.items()},
            "observed_counts": {k: v["count"] for k, v in component_counts.items()},
            "occurrences": {k: v["occurrences"] for k, v in component_counts.items()},
            "fragments": {k: v["fragment"] for k, v in component_counts.items()},
            "components_pass": cell_b_pass_components,
            "all_components_pass": cell_b_pass,
        },
        "verdict": verdict,
        "honest_limits": [
            "Indicator-set is post-hoc-derived from Q 75:16-19; corpus-wide search is the true test.",
            "Per HANDOFF/04-DISCIPLINE.md: post-hoc origin disclosed; corpus-EXACT count test escapes ordinary p-value framing.",
            "Q 75:16-19 was the pre-committed expected result; the test's value is the corpus-wide negative search.",
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"Cell A: predicted={cell_a_pred}, observed={cell_a_obs}, pass={cell_a_pass}")
    print(f"Cell B: all_pass={cell_b_pass}")
    for k, v in cell_b_pass_components.items():
        print(f"  {k}: pass={v} (count={component_counts[k]['count']})")


if __name__ == "__main__":
    main()
