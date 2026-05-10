#!/usr/bin/env python3
"""Q030-F-07 — Bounded-time-window prophetic-prediction structural class corpus-enumeration.

Pre-reg: surahs/Q030-al-rum/Q030-F-07-bounded-time-prediction-class-prereg.md
Pre-reg SHA256: 716ecc65dfab506079db1b94b4f222aa6ec52cf4c7e5b9fa16d821fa04ad947b
Rules-tuple: (QAC v0.4 LEM + POS + segment-level prefix tags, hafs-kufan,
              no-tashkeel, verse-as-unit-of-cooccurrence)
"""
import hashlib, json, os, re, sys
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-07-bounded-time-prediction-class-prereg.md'
EXPECTED_SHA = '716ecc65dfab506079db1b94b4f222aa6ec52cf4c7e5b9fa16d821fa04ad947b'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-07.json'

# LOCKED quantifier lemma set (5 lemmas)
QUANTIFIER_LEMS = {'biDoE', 'siniyn', 'sanap', 'yawom', 'Hiyn'}
# yawom is only counted if modified by a determiner — operationalized below.

PREREG_THRESHOLD_RARE = 10  # < 10 verses → PASS-DIRECTED
PREREG_THRESHOLD_DIRECTIONAL = 20  # 10-20 → DIRECTIONAL


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def parse_qac():
    """Returns list of tokens with (s, v, w, t, form, pos, attrs_raw, lem, root, has_fut_sa)."""
    rows = []
    pat = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
    with open(QAC) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, pos, attrs = parts
            m = pat.match(loc)
            if not m:
                continue
            s, v, w, t = (int(x) for x in m.groups())
            lm = re.search(r'LEM:([^|]+)', attrs)
            rt = re.search(r'ROOT:([^|]+)', attrs)
            # FUT proclitic "sa-" — encoded in QAC as separate token with POS:FUT and form "sa"
            is_fut = (pos == 'FUT' and form in ('sa', '+sa+', 'sa+'))
            # Imperfect verb marker
            is_imperf = (pos == 'V' and 'IMPF' in attrs)
            # PRON suffix or DET prefix detection
            has_det = ('PREFIX|Al+' in attrs) or ('PRON:' in attrs)
            rows.append({
                's': s, 'v': v, 'w': w, 't': t,
                'form': form,
                'pos': pos,
                'attrs': attrs,
                'lem': lm.group(1) if lm else None,
                'root': rt.group(1) if rt else None,
                'is_fut_sa': is_fut,
                'is_imperf_v': is_imperf,
                'has_det_or_pron': has_det,
            })
    return rows


def main():
    verify_sha()
    rows = parse_qac()

    # Group tokens by verse
    by_verse = defaultdict(list)
    for r in rows:
        by_verse[(r['s'], r['v'])].append(r)

    # Identify verses with (a) quantifier LEM + (b) FUT proclitic sa-
    matches = []
    for (s, v), tokens in by_verse.items():
        # Quantifier present
        quant_tokens = []
        for r in tokens:
            if r['lem'] in QUANTIFIER_LEMS:
                if r['lem'] == 'yawom':
                    # Restrict: yawom counts only if it has det or pron suffix
                    # in the SAME word — check word group
                    same_word = [t for t in tokens if t['w'] == r['w']]
                    has_modifier = any(t['has_det_or_pron'] for t in same_word) or len(same_word) > 1
                    if has_modifier:
                        quant_tokens.append(r)
                else:
                    quant_tokens.append(r)
        # FUT sa- present
        fut_tokens = [r for r in tokens if r['is_fut_sa']]
        if quant_tokens and fut_tokens:
            matches.append({
                'surah': s,
                'verse': v,
                'quantifier_lems': sorted({r['lem'] for r in quant_tokens}),
                'quantifier_locs': [f"({r['s']}:{r['v']}:{r['w']})" for r in quant_tokens],
                'fut_sa_locs': [f"({r['s']}:{r['v']}:{r['w']})" for r in fut_tokens],
                'n_fut_in_verse': len(fut_tokens),
            })

    matches.sort(key=lambda x: (x['surah'], x['verse']))
    n_matches = len(matches)
    n_distinct_surahs = len(set(m['surah'] for m in matches))

    # Q 30:2-5 membership
    q30_matches = [m for m in matches if m['surah'] == 30 and 2 <= m['verse'] <= 5]

    # Verdict
    if n_matches < PREREG_THRESHOLD_RARE:
        verdict = 'PASS-DIRECTED'
    elif n_matches <= PREREG_THRESHOLD_DIRECTIONAL:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Per-surah aggregation
    per_surah = defaultdict(int)
    for m in matches:
        per_surah[m['surah']] += 1

    out = {
        'finding_id': 'Q030-F-07',
        'prereg_sha': EXPECTED_SHA,
        'quantifier_lems_locked': sorted(QUANTIFIER_LEMS),
        'n_matches_total': n_matches,
        'n_distinct_surahs': n_distinct_surahs,
        'threshold_rare_lt': PREREG_THRESHOLD_RARE,
        'threshold_directional_lt_or_eq': PREREG_THRESHOLD_DIRECTIONAL,
        'verdict': verdict,
        'all_matches': matches,
        'q30_2_5_matches': q30_matches,
        'per_surah_counts': dict(sorted(per_surah.items())),
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-07 results:")
    print(f"  Quantifier LEM set: {sorted(QUANTIFIER_LEMS)}")
    print(f"  Total verses with (quantifier + FUT sa-) co-occurrence: {n_matches}")
    print(f"  Distinct surahs: {n_distinct_surahs}")
    print(f"  Pre-reg thresholds: <10=PASS-DIRECTED, 10-20=DIRECTIONAL, >20=NULL")
    print(f"  Verdict: {verdict}")
    print(f"  Q 30:2-5 matches: {len(q30_matches)}")
    for m in q30_matches:
        print(f"    Q {m['surah']}:{m['verse']}  quant_lems={m['quantifier_lems']}  fut={len(m['fut_sa_locs'])}")
    print(f"  All matches (first 25):")
    for m in matches[:25]:
        print(f"    Q {m['surah']:3d}:{m['verse']:3d}  quant={m['quantifier_lems']}  fut_count={m['n_fut_in_verse']}")
    print(f"Written: {OUT}")


if __name__ == '__main__':
    main()
