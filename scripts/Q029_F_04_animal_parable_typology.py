#!/usr/bin/env python3
"""Q029-F-04 — Q 29:41 spider-web parable typological uniqueness.

Pre-reg: surahs/Q029-al-ankabut/preregs/Q029-F-04-animal-parable-typology-prereg.md
Pre-reg SHA256: 899a4c2201655c2d28e75c8d9c5cde7fa86e65c6a2d2f7794236311453ffebfe
Rules-tuple: (no-tashkeel, orthographic-token, QAC v0.4 LEM, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)
"""
import hashlib
import json
import os
import re
import sys
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/preregs/Q029-F-04-animal-parable-typology-prereg.md'
EXPECTED_SHA = '899a4c2201655c2d28e75c8d9c5cde7fa86e65c6a2d2f7794236311453ffebfe'
MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_NO_TASHKEEL = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/csv/Q029-F-04.json'

# Animal-vehicle lemmas (locked from T2 comparator anchor)
ANIMAL_LEMS = {
    'Eankabuwt': ('spider', 'Q 29:41'),
    'n~aHol':    ('bee',    'Q 16:68'),
    'naHol':     ('bee-alt-lemma', 'Q 16:68'),
    'namolap':   ('an-ant', 'Q 27:18'),
    'n~amol':    ('ant-collective', 'Q 27:18'),
    '*ubaAb':    ('fly',    'Q 22:73'),
}

# Frailty/weakness roots (locked)
FRAILTY_ROOTS = ['whn', 'DEf']

# Shelter lemmas (locked) — bayt / buyūt
SHELTER_LEMS = ['bayot']


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def scan_qac():
    """Scan QAC; return per-verse dict: {(s,v): {'lems': set, 'roots': set, 'tokens': [(s,v,w,seg,form,LEM,ROOT)]}}."""
    verse_data = defaultdict(lambda: {'lems': set(), 'roots': set()})
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
                    verse_data[(s, v)]['lems'].add(tok[len('LEM:'):])
                elif tok.startswith('ROOT:'):
                    verse_data[(s, v)]['roots'].add(tok[len('ROOT:'):])
    return dict(verse_data)


def main():
    verify_sha()

    verse_data = scan_qac()

    # ===== Sub-claim (a): Eankabuwt corpus-singleton — confirmed by Q029-F-03 =====
    ankabut_verses = sorted([k for k, d in verse_data.items() if 'Eankabuwt' in d['lems']])
    sub_a_pass = (len(ankabut_verses) == 1 and ankabut_verses[0] == (29, 41))

    # ===== Sub-claim (b): >awohan corpus-singleton (LEM) =====
    awohan_verses = sorted([k for k, d in verse_data.items() if '>awohan' in d['lems']])
    sub_b_pass = (len(awohan_verses) == 1 and awohan_verses[0] == (29, 41))

    # ===== Sub-claim (c): joint schema scan =====
    # Schema = animal_lemma + shelter_lemma + frailty_root in the SAME verse
    schema_verses = []
    for (s, v), d in verse_data.items():
        has_animal = any(lem in d['lems'] for lem in ANIMAL_LEMS)
        has_shelter = any(lem in d['lems'] for lem in SHELTER_LEMS)
        has_frailty = any(rt in d['roots'] for rt in FRAILTY_ROOTS)
        if has_animal and has_shelter and has_frailty:
            schema_verses.append({
                's': s, 'v': v,
                'animals': [lem for lem in ANIMAL_LEMS if lem in d['lems']],
                'shelters': [lem for lem in SHELTER_LEMS if lem in d['lems']],
                'frailty_roots': [rt for rt in FRAILTY_ROOTS if rt in d['roots']],
            })
    schema_verses.sort(key=lambda x: (x['s'], x['v']))
    sub_c_pass = (len(schema_verses) == 1 and (schema_verses[0]['s'], schema_verses[0]['v']) == (29, 41))

    # ===== Sub-scans for descriptive context =====
    # Verses that have any animal_lemma (descriptive)
    animal_verses = sorted([k for k, d in verse_data.items() if any(lem in d['lems'] for lem in ANIMAL_LEMS)])
    # Verses with bayot lemma
    shelter_verses = sorted([k for k, d in verse_data.items() if any(lem in d['lems'] for lem in SHELTER_LEMS)])
    # Verses with frailty roots
    frailty_verses = sorted([k for k, d in verse_data.items() if any(rt in d['roots'] for rt in FRAILTY_ROOTS)])
    # Intersection of animal AND shelter
    animal_AND_shelter = [k for k in animal_verses if k in shelter_verses]
    # Intersection of animal AND frailty
    animal_AND_frailty = [k for k in animal_verses if k in frailty_verses]

    # ===== Composite verdict =====
    n_pass = sum([sub_a_pass, sub_b_pass, sub_c_pass])
    if n_pass == 3:
        verdict = 'PASS-DIRECTED — corpus-unique parable schema'
    elif n_pass == 2:
        verdict = 'DIRECTIONAL — partially-unique schema'
    elif n_pass == 1:
        verdict = 'NULL — single sub-claim'
    else:
        verdict = 'NULL'

    # Animal-parable comparator summary
    comparator_anchors = {}
    for lem, (gloss, ref) in ANIMAL_LEMS.items():
        attests = sorted([k for k, d in verse_data.items() if lem in d['lems']])
        comparator_anchors[lem] = {
            'gloss': gloss,
            'attested_verses': [f'Q {s}:{v}' for s, v in attests],
            'n_verses': len(attests),
            'n_surahs': len(set(s for s, _ in attests)),
        }

    out = {
        'finding_id': 'Q029-F-04',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 LEM, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)',
        'sub_claim_a_Eankabuwt_corpus_singleton': {
            'attested_verses': [f'Q {s}:{v}' for s, v in ankabut_verses],
            'pass': sub_a_pass,
        },
        'sub_claim_b_>awohan_corpus_singleton': {
            'attested_verses': [f'Q {s}:{v}' for s, v in awohan_verses],
            'pass': sub_b_pass,
        },
        'sub_claim_c_joint_schema_animal_AND_shelter_AND_frailty': {
            'matching_verses': [f'Q {x["s"]}:{x["v"]}' for x in schema_verses],
            'matches_detail': schema_verses,
            'pass': sub_c_pass,
        },
        'descriptive_context': {
            'verses_with_any_animal_lemma': [f'Q {s}:{v}' for s, v in animal_verses],
            'verses_with_shelter_lemma_bayot': len(shelter_verses),
            'verses_with_frailty_root': len(frailty_verses),
            'verses_animal_AND_shelter': [f'Q {s}:{v}' for s, v in animal_AND_shelter],
            'verses_animal_AND_frailty': [f'Q {s}:{v}' for s, v in animal_AND_frailty],
        },
        'comparator_animal_lemmas': comparator_anchors,
        'n_sub_claims_passed': n_pass,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q029-F-04 — Q 29:41 spider-parable typological uniqueness:")
    print(f"  Sub-claim (a) Eankabuwt corpus-singleton: {sub_a_pass}  attestations={[f'Q {s}:{v}' for s,v in ankabut_verses]}")
    print(f"  Sub-claim (b) >awohan corpus-singleton:   {sub_b_pass}  attestations={[f'Q {s}:{v}' for s,v in awohan_verses]}")
    schema_match_strs = [f"Q {x['s']}:{x['v']}" for x in schema_verses]
    print(f"  Sub-claim (c) animal+shelter+frailty joint schema: {sub_c_pass}  matches={schema_match_strs}")
    print(f"  Verses with any animal_lemma: {[f'Q {s}:{v}' for s, v in animal_verses]}")
    print(f"  Verses animal AND shelter: {[f'Q {s}:{v}' for s, v in animal_AND_shelter]}")
    print(f"  Verses animal AND frailty: {[f'Q {s}:{v}' for s, v in animal_AND_frailty]}")
    print(f"  Verdict: {verdict}  ({n_pass}/3 sub-claims passed)")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
