#!/usr/bin/env python3
"""Q030-F-06 — Lemma biDoE corpus-uniqueness.

Pre-reg: surahs/Q030-al-rum/Q030-F-06-bidc-corpus-uniqueness-prereg.md
Pre-reg SHA256: 45c0bad3d7dd76ba2ea99dc6790fc53743cc501198c84a3702c185c66c68d09b
Rules-tuple: (QAC v0.4 LEM tags, hafs-kufan, no-tashkeel, lemma-token-counts,
              syntactic-adjacency at within-verse-word-index level)
"""
import hashlib, json, os, re, sys
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-06-bidc-corpus-uniqueness-prereg.md'
EXPECTED_SHA = '45c0bad3d7dd76ba2ea99dc6790fc53743cc501198c84a3702c185c66c68d09b'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-06.json'

TARGET_LEM = 'biDoE'
ADJACENT_LEM = 'siniyn'
PREREG_TARGET = {'n_token': 2, 'n_surah': 2, 'frame_match': 2, 'surah_set': [12, 30]}


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac():
    """Return list of dicts: {s, v, w, t, form, pos, lem, root}."""
    rows = []
    pat_loc = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
    with open(QAC) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, pos, attrs = parts
            m = pat_loc.match(loc)
            if not m:
                continue
            s, v, w, t = (int(x) for x in m.groups())
            lm = re.search(r'LEM:([^|]+)', attrs)
            rt = re.search(r'ROOT:([^|]+)', attrs)
            rows.append({
                's': s, 'v': v, 'w': w, 't': t,
                'form': form,
                'pos': pos,
                'lem': lm.group(1) if lm else None,
                'root': rt.group(1) if rt else None,
            })
    return rows


def main():
    verify_sha()
    rows = load_qac()

    # 1) Find all biDoE attestations
    bidoE = [r for r in rows if r['lem'] == TARGET_LEM]
    token_count = len(bidoE)
    surah_set = sorted({r['s'] for r in bidoE})
    n_surah = len(surah_set)

    # 2) For each attestation, check the immediately-following word's lemma
    # "Immediately following" = same surah, same verse, word w+1
    # Build index: (s, v, w) -> first token at that word position
    word_lem_idx = defaultdict(list)
    for r in rows:
        word_lem_idx[(r['s'], r['v'], r['w'])].append(r)

    frame_matches = []
    for r in bidoE:
        s, v, w = r['s'], r['v'], r['w']
        next_word_tokens = word_lem_idx.get((s, v, w + 1), [])
        next_lems = [t['lem'] for t in next_word_tokens if t['lem']]
        next_roots = [t['root'] for t in next_word_tokens if t['root']]
        matches_frame = ADJACENT_LEM in next_lems
        frame_matches.append({
            'location': f"({s}:{v}:{w})",
            'form': r['form'],
            'lem': r['lem'],
            'next_word_position': f"({s}:{v}:{w+1})",
            'next_word_lems': next_lems,
            'next_word_roots': next_roots,
            'frame_biDoE_plus_siniyn': matches_frame,
        })
    n_frame_match = sum(1 for m in frame_matches if m['frame_biDoE_plus_siniyn'])

    # 3) Compare to pre-registered target
    observed = {
        'n_token': token_count,
        'n_surah': n_surah,
        'frame_match': n_frame_match,
        'surah_set': surah_set,
    }
    exact_match = (
        observed['n_token'] == PREREG_TARGET['n_token']
        and observed['n_surah'] == PREREG_TARGET['n_surah']
        and observed['frame_match'] == PREREG_TARGET['frame_match']
        and observed['surah_set'] == PREREG_TARGET['surah_set']
    )
    partial = (
        observed['n_token'] == PREREG_TARGET['n_token']
        and observed['n_surah'] == PREREG_TARGET['n_surah']
        and observed['frame_match'] != PREREG_TARGET['frame_match']
    )
    if exact_match:
        verdict = 'PASS-DIRECTED'
    elif partial:
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    # 4) Diagnostic comparison: count under broader root 'bDE' (different lemma allowed)
    root_bDE = [r for r in rows if r['root'] == 'bDE']
    root_surah_set = sorted({r['s'] for r in root_bDE})
    root_lem_breakdown = defaultdict(lambda: {'tokens': 0, 'surahs': set()})
    for r in root_bDE:
        root_lem_breakdown[r['lem']]['tokens'] += 1
        root_lem_breakdown[r['lem']]['surahs'].add(r['s'])

    out = {
        'finding_id': 'Q030-F-06',
        'prereg_sha': EXPECTED_SHA,
        'target_lemma': TARGET_LEM,
        'prereg_target': PREREG_TARGET,
        'observed': observed,
        'attestation_details': frame_matches,
        'verdict': verdict,
        'diagnostic_root_bDE_breakdown': {
            'total_tokens_under_root': len(root_bDE),
            'distinct_surahs_under_root': root_surah_set,
            'lemma_breakdown': {
                lem: {'tokens': v['tokens'], 'surahs': sorted(v['surahs'])}
                for lem, v in root_lem_breakdown.items()
            },
        },
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-06 results:")
    print(f"  Target lemma: {TARGET_LEM}")
    print(f"  Observed: n_token={token_count}, n_surah={n_surah}, surahs={surah_set}, frame_match={n_frame_match}")
    print(f"  Pre-reg target: {PREREG_TARGET}")
    print(f"  Verdict: {verdict}")
    for m in frame_matches:
        print(f"    {m['location']:14s}  form={m['form']:10s}  next={m['next_word_lems']}  frame={m['frame_biDoE_plus_siniyn']}")
    print(f"  Diagnostic: root 'bDE' lemma breakdown:")
    for lem, v in root_lem_breakdown.items():
        print(f"    {lem:14s}  tokens={v['tokens']:2d}  surahs={sorted(v['surahs'])}")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
