#!/usr/bin/env python3
"""Q029-F-01 — Q 29:41 spider parable lexical uniqueness (hapax count).

Pre-reg: surahs/Q029-al-ankabut/Q029-F-01-ankabut-parable-hapax-prereg.md
Pre-reg SHA256: dd9244bd0e00f39b89e2c06c7b1549ce665187ae4af274af4615afa769b38f60
Rules-tuple: (QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)
"""
import json, re, hashlib, sys, os
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/Q029-F-01-ankabut-parable-hapax-prereg.md'
EXPECTED_SHA = 'dd9244bd0e00f39b89e2c06c7b1549ce665187ae4af274af4615afa769b38f60'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

# Q 29:41 candidate lemmas (drawn from QAC LEM annotations of Q 29:41)
# Eankabuwt = spider noun (Q 29:41 — both occurrences)
# >awohan = "made fragile" verb form (specifically the lemma at Q 29:41:13)
# bayot = house (lemma form at Q 29:41:11, 14, 15)
# maval = parable/likeness (lemma at Q 29:41:1, 8)
# waliY~ = protector/ally (lemma at Q 29:41:7)
CANDIDATES = ['Eankabuwt', '>awohan', 'bayot', 'maval', 'waliY~']

# Q 16:75 (slave / free man parable) — for comparison
# {Eabod-slave, $ariyk-share-with, mavalu-likeness}
CANDIDATES_Q1675 = ['Eabod', '$ariyk', 'maval']

# Q 27:18 (ant-valley) — for comparison
# {namolap-ant, waAd-valley, maAlik-king}
CANDIDATES_Q2718 = ['namolap', 'waAd', 'mas`kin']


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual={actual}", file=sys.stderr)
        sys.exit(1)


def load_lemma_distribution():
    lem_data = defaultdict(lambda: {'token_count': 0, 'surahs': set()})
    with open(QAC) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, pos, attrs = parts
            m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
            if not m:
                continue
            s, v, w, t = (int(x) for x in m.groups())
            lm = re.search(r'LEM:([^|]+)', attrs)
            if lm:
                L = lm.group(1)
                lem_data[L]['token_count'] += 1
                lem_data[L]['surahs'].add(s)
    return lem_data


def classify(d):
    n = d['token_count']
    n_s = len(d['surahs'])
    if n == 1:
        return 'strict-hapax'
    if n_s == 1:
        return 'lemma-corpus-hapax'
    if n_s <= 2:
        return 'near-hapax'
    return 'non-hapax'


def main():
    verify_sha()
    lem_data = load_lemma_distribution()

    def evaluate(cands):
        out = []
        for lem in cands:
            d = lem_data.get(lem, {'token_count': 0, 'surahs': set()})
            cls = classify(d) if d['token_count'] > 0 else 'NOT-FOUND'
            out.append({
                'lemma': lem,
                'token_count': d['token_count'],
                'surahs': sorted(d['surahs']),
                'n_surahs': len(d['surahs']),
                'class': cls,
            })
        n_strict = sum(1 for r in out if r['class'] == 'strict-hapax')
        n_corpus_hapax = sum(1 for r in out if r['class'] in ('strict-hapax', 'lemma-corpus-hapax'))
        n_near_or_better = sum(1 for r in out if r['class'] in ('strict-hapax', 'lemma-corpus-hapax', 'near-hapax'))
        return out, n_strict, n_corpus_hapax, n_near_or_better

    res, n_strict, n_corpus, n_near = evaluate(CANDIDATES)
    threshold = 2

    if n_near >= threshold:
        verdict = 'PASS-DIRECTED'
    elif n_near == 1:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    res_q1675, _, _, n_near_q1675 = evaluate(CANDIDATES_Q1675)
    res_q2718, _, _, n_near_q2718 = evaluate(CANDIDATES_Q2718)

    out = {
        'finding_id': 'Q029-F-01',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)',
        'q29_41_candidates': res,
        'q29_41_summary': {
            'n_strict_hapax': n_strict,
            'n_corpus_hapax_or_stricter': n_corpus,
            'n_near_hapax_or_stricter': n_near,
            'threshold_for_PASS': threshold,
            'verdict': verdict,
        },
        'q16_75_comparison': res_q1675,
        'q16_75_summary': {'n_near_hapax_or_stricter': n_near_q1675},
        'q27_18_comparison': res_q2718,
        'q27_18_summary': {'n_near_hapax_or_stricter': n_near_q2718},
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q029-al-ankabut/csv/Q029-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q029-F-01 results:")
    print(f"  Q 29:41 candidate lemmas:")
    for r in res:
        print(f"    {r['lemma']:18s}  count={r['token_count']:3d}  n_surahs={r['n_surahs']:2d}  class={r['class']}")
    print(f"  Summary: strict-hapax={n_strict}, corpus-hapax+={n_corpus}, near-hapax+={n_near}")
    print(f"  Verdict: {verdict} (threshold ≥ {threshold})")
    print(f"\n  Q 16:75 comparison: near-hapax+={n_near_q1675}")
    print(f"  Q 27:18 comparison: near-hapax+={n_near_q2718}")


if __name__ == '__main__':
    main()
