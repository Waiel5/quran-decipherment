#!/usr/bin/env python3
"""Q058-F-04 — Q 58 ḥ-z-b "faction" lexical signature corpus distribution.

Pre-reg: surahs/Q058-al-mujadala/Q058-F-04-hizb-faction-vocabulary-prereg.md
Pre-reg SHA256: 9618031240079d8c5aa79cf35aa03ce16dbf178f6b0ffef96eb9d4f109d74703
Rules-tuple: (no-tashkeel, orthographic-token, surface-phrase-and-root-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json
import re
import hashlib
import sys
import os
import random

PREREG = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/Q058-F-04-hizb-faction-vocabulary-prereg.md'
EXPECTED_SHA = '9618031240079d8c5aa79cf35aa03ce16dbf178f6b0ffef96eb9d4f109d74703'
SEED = 20260509
N_PERM = 10000
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/csv/Q058-F-04.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    # ḥ-z-b root patterns
    hizb_patterns = [
        re.compile(r'\bحزب\b'),
        re.compile(r'\bحزبا\b'),
        re.compile(r'\bحزبه\b'),
        re.compile(r'\bحزبهم\b'),
        re.compile(r'\bأحزاب\b'),
        re.compile(r'\bالأحزاب\b'),
        re.compile(r'\bحزبا'),
    ]
    # Phrase patterns
    hizb_shaytan = re.compile(r'حزب الشيطان')
    hizb_allah = re.compile(r'حزب الله')

    # Per-surah ḥ-z-b root counts
    per_surah_root_counts = []
    surahs_with_hizb_shaytan = []
    surahs_with_hizb_allah = []
    total_root_corpus = 0
    q58_root_count = 0
    q58_hits = []

    for s in quran:
        sid = s['id']
        s_hits = []
        for v in s['verses']:
            t = v['text']
            for tok in t.split():
                # use simple stem-membership: tok contains "حزب" as a stem (not part of an unrelated word)
                if 'حزب' in tok:
                    s_hits.append({'verse': v['id'], 'token': tok})
                    total_root_corpus += 1
                    if sid == 58:
                        q58_root_count += 1
                        q58_hits.append({'verse': v['id'], 'token': tok})
            # also handle 'الأحزاب' stem
            for tok in t.split():
                if 'أحزاب' in tok or 'الأحزاب' in tok:
                    if not any(h['token'] == tok and h['verse'] == v['id'] for h in s_hits):
                        s_hits.append({'verse': v['id'], 'token': tok, 'plural': True})
                        total_root_corpus += 1
                        if sid == 58:
                            q58_root_count += 1
                            q58_hits.append({'verse': v['id'], 'token': tok, 'plural': True})
            # phrase-level
            if hizb_shaytan.search(t):
                if sid not in surahs_with_hizb_shaytan:
                    surahs_with_hizb_shaytan.append(sid)
            if hizb_allah.search(t):
                if sid not in surahs_with_hizb_allah:
                    surahs_with_hizb_allah.append(sid)
        if s_hits:
            per_surah_root_counts.append({'sid': sid, 'count': len(s_hits), 'hits': s_hits})

    # Sort by count
    per_surah_root_counts_sorted = sorted(per_surah_root_counts, key=lambda x: -x['count'])

    # H1: Q 58 ≥ 3 ḥ-z-b root tokens
    h1_pass = q58_root_count >= 3

    # H2a: ḥizb al-shayṭān corpus-exclusive to Q 58
    h2a_pass = surahs_with_hizb_shaytan == [58]
    # H2b: ḥizb Allāh in fewer than 3 surahs
    h2b_pass = len(surahs_with_hizb_allah) < 3
    h2_pass = h2a_pass and h2b_pass

    # H3: Q 58 ≥ 30% of corpus ḥ-z-b root tokens
    q58_share = q58_root_count / total_root_corpus if total_root_corpus else 0
    h3_pass = q58_share >= 0.30

    # Permutation null A: length-weighted root re-distribution
    random.seed(SEED)
    surah_lengths = []
    for s in quran:
        n_words = sum(len([t for t in v['text'].split() if not all(c in '۞ۖۗۚ۟ۘ۠ۤۛ' for c in t)]) for v in s['verses'])
        surah_lengths.append((s['id'], n_words))
    total_words = sum(w for _, w in surah_lengths)
    weights = [w / total_words for _, w in surah_lengths]
    surah_ids = [sid for sid, _ in surah_lengths]
    n_extreme = 0
    for _ in range(N_PERM):
        # Distribute total_root_corpus tokens across surahs by length-weighting
        sample = random.choices(surah_ids, weights=weights, k=total_root_corpus)
        q58_simulated = sum(1 for x in sample if x == 58)
        if q58_simulated >= q58_root_count:
            n_extreme += 1
    p_null_A = (n_extreme + 1) / (N_PERM + 1)

    out = {
        'finding_id': 'Q058-F-04',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, surface-phrase-and-root-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'q58_hizb_root_count': q58_root_count,
        'q58_hits': q58_hits,
        'corpus_total_hizb_root': total_root_corpus,
        'q58_share_of_corpus_root': q58_share,
        'top_5_surahs_by_hizb_root_count': [{'sid': r['sid'], 'count': r['count']} for r in per_surah_root_counts_sorted[:5]],
        'all_surahs_with_hizb_root': [{'sid': r['sid'], 'count': r['count']} for r in per_surah_root_counts_sorted],
        'surahs_with_hizb_shaytan_phrase': surahs_with_hizb_shaytan,
        'surahs_with_hizb_allah_phrase': surahs_with_hizb_allah,
        'h1_pass': h1_pass,
        'h2a_hizb_shaytan_corpus_exclusive_to_Q58': h2a_pass,
        'h2b_hizb_allah_in_fewer_than_3_surahs': h2b_pass,
        'h2_pass': h2_pass,
        'h3_q58_share_geq_30_percent': h3_pass,
        'permutation_null_A': {
            'n_extreme_random_q58_at_or_above_observed': n_extreme,
            'p_value': p_null_A,
            'description': 'fraction of length-weighted distributions where Q 58 receives >= q58_root_count root tokens',
        },
        'verdict': (
            'CONFIRMED' if (h1_pass and h2_pass and h3_pass and p_null_A <= 0.01667)
            else 'DIRECTIONAL' if (h1_pass and h2_pass)
            else 'PARTIAL' if (h1_pass or h2_pass)
            else 'NULL'
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q058-F-04 verdict: {out['verdict']}")
    print(f"  H1 Q 58 ḥ-z-b root count: {q58_root_count} (pass={h1_pass})")
    print(f"  H2a ḥizb al-shayṭān corpus-exclusive: {h2a_pass}; surahs={surahs_with_hizb_shaytan}")
    print(f"  H2b ḥizb Allāh in <3 surahs: {h2b_pass}; surahs={surahs_with_hizb_allah}")
    print(f"  H3 Q 58 share: {q58_share:.4f} (target >=0.30, pass={h3_pass})")
    print(f"  Perm-null A p-value: {p_null_A:.6f}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
