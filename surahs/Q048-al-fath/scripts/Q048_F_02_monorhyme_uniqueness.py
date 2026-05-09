#!/usr/bin/env python3
"""
Q048-F-02 — Q 48 al-Fatḥ perfect-alif-monorhyme uniqueness test (descriptive).

Pre-reg: ../preregs/Q048-F-02-perfect-monorhyme-uniqueness-prereg.md
SHA-locked: 5f595679370381c7c20ed309906c294b5bbfc0eecf4e915a0095c23a107130af
Seed: 20260509
"""
import json
import csv
import hashlib
import os
import sys

PRE_REG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                            'Q048-F-02-perfect-monorhyme-uniqueness-prereg.md')
EXPECTED_SHA = "5f595679370381c7c20ed309906c294b5bbfc0eecf4e915a0095c23a107130af"
SEED = 20260509

H700_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json"
REVELATION_ORDER_PATH = "/Users/grey/Downloads/quran/data/revelation-order.csv"
OUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q048-F-02.json')


def verify_prereg_sha():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        print(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}", file=sys.stderr)
        sys.exit(1)
    return sha


def load_revelation():
    out = {}
    with open(REVELATION_ORDER_PATH) as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            mushaf = int(r['mushaf_order'])
            out[mushaf] = {'period': r['period'], 'noldeke_phase': r['noldeke_phase']}
    return out


def main():
    sha = verify_prereg_sha()
    print(f"Pre-reg SHA verified: {sha}")

    with open(H700_PATH) as f:
        d = json.load(f)
    diags = d['rhyme']['rhyme_letter_diagnostics']

    rev = load_revelation()

    # All perfect-monorhymes (frac == 1.0)
    perfect = []
    for r in diags:
        if r['frac'] == 1.0:
            s = r['surah']
            entry = {
                'surah': s,
                'top_letter': r['top_letter'],
                'n_verses': r['n_verses'],
                'period': rev.get(s, {}).get('period', 'unknown'),
                'noldeke_phase': rev.get(s, {}).get('noldeke_phase', 'unknown'),
            }
            perfect.append(entry)

    # Sort by n_verses desc
    perfect_sorted = sorted(perfect, key=lambda x: -x['n_verses'])

    # Q 48 status
    q48_entry = next((p for p in perfect if p['surah'] == 48), None)
    q48_is_perfect = q48_entry is not None

    # Filter Medinan + length ≥ 28
    candidates = [p for p in perfect if p['period'] == 'Medinan' and p['n_verses'] >= 28]
    n_candidates = len(candidates)

    # Test
    t1_q48_is_perfect = q48_is_perfect
    t2_unique_in_subset = (n_candidates == 1 and candidates[0]['surah'] == 48)
    t2_singleton_or_pair = (n_candidates <= 2 and any(c['surah'] == 48 for c in candidates))

    if t1_q48_is_perfect and t2_unique_in_subset:
        verdict = "CONFIRMED"
    elif t1_q48_is_perfect and t2_singleton_or_pair:
        verdict = "DIRECTIONAL"
    elif t1_q48_is_perfect:
        verdict = "DIRECTIONAL-WEAK"
    else:
        verdict = "NULL"

    # Also report relaxed (Medinan as period OR noldeke_phase)
    candidates_relaxed = [p for p in perfect
                          if (p['period'] == 'Medinan' or p['noldeke_phase'] == 'Medinan')
                          and p['n_verses'] >= 28]

    result = {
        "test_id": "Q048-F-02",
        "H_NEW": "H-NEW-1261",
        "title": "Q 48 al-Fatḥ — perfect alif-monorhyme uniqueness among Medinan v ≥ 28",
        "pre_reg_sha": sha,
        "seed": SEED,
        "rules_tuple": "(min-tashkeel, verse-final-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "alpha_bon": 0.05,
        "bonferroni_k": 1,
        "all_perfect_monorhyme_surahs": perfect_sorted,
        "n_perfect_monorhyme_total": len(perfect),
        "q48_perfect_monorhyme": q48_is_perfect,
        "q48_top_letter": q48_entry['top_letter'] if q48_entry else None,
        "q48_n_verses": q48_entry['n_verses'] if q48_entry else None,
        "candidates_medinan_v28plus": candidates,
        "n_candidates": n_candidates,
        "candidates_relaxed_medinan": candidates_relaxed,
        "n_candidates_relaxed": len(candidates_relaxed),
        "test_t1_q48_perfect": t1_q48_is_perfect,
        "test_t2_q48_unique_in_subset": t2_unique_in_subset,
        "test_t2_q48_in_at_most_pair": t2_singleton_or_pair,
        "verdict": verdict,
        "honest_limits": [
            "Q 76 al-Insān (31 verses, alif) is classified Medinan in Tanzil-Egyptian (revelation rank 98) but some classical chains label it Meccan.",
            "If Q 76 is treated as Medinan, the 'unique in subset' claim becomes 'pair: Q 48 + Q 76' (not strict singleton).",
            "Test is descriptive-categorical, not frequentist; verdict reflects the categorical claim's empirical realization.",
        ],
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"Result written to {OUT_PATH}")
    print(f"Verdict: {verdict}")
    print(f"  Total perfect-monorhyme surahs: {len(perfect)}")
    print(f"  Q 48 perfect: {q48_is_perfect}")
    print(f"  Medinan v ≥ 28 perfect candidates (strict): {n_candidates}")
    for c in candidates:
        print(f"    Q{c['surah']}: {c['top_letter']} | {c['n_verses']} v | {c['period']}")
    print(f"  Medinan v ≥ 28 perfect (relaxed): {len(candidates_relaxed)}")
    for c in candidates_relaxed:
        print(f"    Q{c['surah']}: {c['top_letter']} | {c['n_verses']} v")


if __name__ == "__main__":
    main()
