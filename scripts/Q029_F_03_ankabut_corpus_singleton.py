#!/usr/bin/env python3
"""Q029-F-03 — *ʿankabūt* (spider) corpus-uniqueness verification.

Pre-reg: surahs/Q029-al-ankabut/preregs/Q029-F-03-ankabut-corpus-singleton-prereg.md
Pre-reg SHA256: 2718837da9e3c5dce8d955da9752a38f654c9cd100f30b81f5751f46b0a2d6a7
Rules-tuple: (QAC v0.4 LEM-tag + ROOT-tag, no-tashkeel, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)
"""
import hashlib
import json
import os
import sys
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/preregs/Q029-F-03-ankabut-corpus-singleton-prereg.md'
EXPECTED_SHA = '2718837da9e3c5dce8d955da9752a38f654c9cd100f30b81f5751f46b0a2d6a7'
MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/csv/Q029-F-03.json'

TARGET_LEM = 'Eankabuwt'
TARGET_ROOT = 'Enkb'

COMPARATOR_LEMS = [
    ('n~aHol', 'bee', 'Q 16:68'),
    ('namolap', 'an ant (one specific ant)', 'Q 27:18'),
    ('n~amol', 'ant(s) — collective', 'Q 27:18 + Q 27:18'),
    ('*ubaAb', 'fly', 'Q 22:73'),
]


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def scan_qac_for_lem_and_root():
    """Returns: per-lemma {lem: [(s,v,w,seg)]}, per-root {root: [(s,v,w,seg)]}."""
    lem_attest = defaultdict(list)
    root_attest = defaultdict(list)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('LEM:'):
                    lem = tok[len('LEM:'):]
                    lem_attest[lem].append((s, v, w, seg))
                elif tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    root_attest[root].append((s, v, w, seg))
    return lem_attest, root_attest


def summarize(attest_list):
    if not attest_list:
        return {'n_tokens': 0, 'n_distinct_surahs': 0, 'n_distinct_verses': 0,
                'surahs': [], 'verses': [], 'attestations': []}
    surahs = sorted(set(a[0] for a in attest_list))
    verses = sorted(set((a[0], a[1]) for a in attest_list))
    return {
        'n_tokens': len(attest_list),
        'n_distinct_surahs': len(surahs),
        'n_distinct_verses': len(verses),
        'surahs': surahs,
        'verses': [f'Q {s}:{v}' for s, v in verses],
        'attestations': [{'s': s, 'v': v, 'w': w, 'seg': seg} for s, v, w, seg in attest_list],
    }


def main():
    verify_sha()
    lem_attest, root_attest = scan_qac_for_lem_and_root()

    target_lem = summarize(lem_attest.get(TARGET_LEM, []))
    target_root = summarize(root_attest.get(TARGET_ROOT, []))

    # Decision rule
    if target_lem['n_distinct_surahs'] == 1 and target_lem['n_distinct_verses'] == 1:
        verdict = 'PASS-DIRECTED — corpus-singleton (lemma)'
    elif target_lem['n_distinct_surahs'] == 1 and target_lem['n_distinct_verses'] >= 2:
        verdict = 'PASS-DIRECTED — surah-singleton, verse-near-singleton'
    elif target_lem['n_distinct_surahs'] == 0:
        verdict = 'NULL — lemma absent from QAC v0.4'
    else:
        verdict = 'NULL — pre-commit violated (lemma in >1 surah)'

    # Comparators (descriptive)
    comp = []
    for lem, gloss, ref in COMPARATOR_LEMS:
        comp.append({
            'lem': lem, 'english_gloss': gloss, 'attested_at': ref,
            'attest_summary': summarize(lem_attest.get(lem, [])),
        })

    out = {
        'finding_id': 'Q029-F-03',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(QAC v0.4 LEM-tag + ROOT-tag, no-tashkeel, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)',
        'target_lem': TARGET_LEM,
        'target_root': TARGET_ROOT,
        'lemma_attestation': target_lem,
        'root_attestation': target_root,
        'verdict': verdict,
        'comparators': comp,
        'a_priori_prediction': 'corpus-singleton (1 surah, 1 verse)',
        'note': 'corpus-singleton is a deterministic count-fact; no permutation null applies.',
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q029-F-03 — {TARGET_LEM} corpus-uniqueness:")
    print(f"  Lemma attestations: {target_lem['n_tokens']} tokens across "
          f"{target_lem['n_distinct_surahs']} surah(s), "
          f"{target_lem['n_distinct_verses']} verse(s): {target_lem['verses']}")
    print(f"  Root {TARGET_ROOT} attestations: {target_root['n_tokens']} tokens across "
          f"{target_root['n_distinct_surahs']} surah(s)")
    print(f"  Verdict: {verdict}")
    print(f"  Comparators (animal-parable lemmas):")
    for c in comp:
        s = c['attest_summary']
        print(f"    {c['lem']:12s} ({c['english_gloss']:35s}): "
              f"{s['n_tokens']} tokens, {s['n_distinct_surahs']} surah(s), "
              f"verses={s['verses'][:3]}{'...' if len(s['verses'])>3 else ''}")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
