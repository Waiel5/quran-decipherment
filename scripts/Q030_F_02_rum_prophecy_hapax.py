#!/usr/bin/env python3
"""Q030-F-02 — Q 30:2-5 Roman-Persian war prophecy lexical uniqueness (hapax count).

Pre-reg: surahs/Q030-al-rum/Q030-F-02-rum-prophecy-hapax-prereg.md
Pre-reg SHA256: 4850caed2dbcda8a9417948a398338c58ae54829b6ce872923c17d3e204c4c99
Rules-tuple: (QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)
"""
import json, re, hashlib, sys, os
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-02-rum-prophecy-hapax-prereg.md'
EXPECTED_SHA = '4850caed2dbcda8a9417948a398338c58ae54829b6ce872923c17d3e204c4c99'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

# Q 30:2-5 candidate lemmas (LEM as in QAC v0.4)
# r~uwm = Romans (Q 30:2)
# biDoE = a few/several years (Q 30:4)
# siniyn = years (Q 30:4)
# galab = noun "defeat" (Q 30:3 "ghalabihim")
# galabu = verb (Q 30:2 "ghulibati"; Q 30:3 "yaghlibūn") — main verb root glb
# >adonaY` = nearer/closer (Q 30:3 "fī adnā")
CANDIDATES_RUM = ['r~uwm', 'biDoE', 'siniyn', 'galab', 'galabu', '>adonaY`']

# Q 27:14 candidate lemmas (for comparison, drawn from surface)
# {jaHadu, AistayoqanatohaA, ZuluM, EuluwwAF, EAqibap, mufosid}
CANDIDATES_Q2714 = ['jaHada', 'AisotayoqanatohaA', 'Zulom', 'Euluw~', 'EAqibap', 'mufosid']


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual={actual}", file=sys.stderr)
        sys.exit(1)


def load_lemma_distribution():
    """Returns dict: lemma -> {'token_count': int, 'surahs': set}"""
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
    """Return classification given {'token_count', 'surahs' (set)}."""
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

    def evaluate(candidates):
        out = []
        for lem in candidates:
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

    rum_results, rum_n_strict, rum_n_corpus, rum_n_near = evaluate(CANDIDATES_RUM)
    q2714_results, q14_n_strict, q14_n_corpus, q14_n_near = evaluate(CANDIDATES_Q2714)

    threshold = 3
    if rum_n_near >= threshold:
        verdict = 'PASS-DIRECTED'
    elif rum_n_near == 2:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q030-F-02',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)',
        'q30_2_5_candidates': rum_results,
        'q30_2_5_summary': {
            'n_strict_hapax': rum_n_strict,
            'n_corpus_hapax_or_stricter': rum_n_corpus,
            'n_near_hapax_or_stricter': rum_n_near,
            'threshold_for_PASS': threshold,
            'verdict': verdict,
        },
        'q27_14_comparison': q2714_results,
        'q27_14_summary': {
            'n_strict_hapax': q14_n_strict,
            'n_corpus_hapax_or_stricter': q14_n_corpus,
            'n_near_hapax_or_stricter': q14_n_near,
        },
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-02 results:")
    print(f"  Q 30:2-5 candidate lemmas:")
    for r in rum_results:
        print(f"    {r['lemma']:18s}  count={r['token_count']:3d}  surahs={r['surahs']}  class={r['class']}")
    print(f"  Summary: strict-hapax={rum_n_strict}, corpus-hapax+={rum_n_corpus}, near-hapax+={rum_n_near}")
    print(f"  Verdict: {verdict} (threshold ≥ {threshold} near-hapax-or-stricter)")
    print(f"\n  Q 27:14 comparison:")
    for r in q2714_results:
        print(f"    {r['lemma']:18s}  count={r['token_count']:3d}  n_surahs={r['n_surahs']:2d}  class={r['class']}")
    print(f"  Summary: strict-hapax={q14_n_strict}, near-hapax+={q14_n_near}")


if __name__ == '__main__':
    main()
