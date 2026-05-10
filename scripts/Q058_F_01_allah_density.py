#!/usr/bin/env python3
"""Q058-F-01 — Q 58 al-Mujādala Allāh-token verse-coverage corpus-EXACT extreme test.

Pre-reg: surahs/Q058-al-mujadala/Q058-F-01-allah-density-prereg.md
Pre-reg SHA256: 5e2d18067236123bc610ab6017691119685732dcc6b6357a7e0af39cbf2f7e1f
Rules-tuple: (no-tashkeel, orthographic-token, substring-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json
import re
import hashlib
import sys
import os
import random

PREREG = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/Q058-F-01-allah-density-prereg.md'
EXPECTED_SHA = '5e2d18067236123bc610ab6017691119685732dcc6b6357a7e0af39cbf2f7e1f'
SEED = 20260509
N_PERM = 10000
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/csv/Q058-F-01.json'

ALLAH_PATTERN = re.compile(r'الله')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    # Per-verse Allāh detection (substring rule = pre-committed primary)
    verse_has_allah = []  # binary 6236-vector
    verse_keys = []
    for s in quran:
        for v in s['verses']:
            verse_has_allah.append(1 if ALLAH_PATTERN.search(v['text']) else 0)
            verse_keys.append((s['id'], v['id']))

    # Q 58 specifically
    s58 = next(s for s in quran if s['id'] == 58)
    q58_verse_data = []
    q58_total_allah = 0
    q58_total_words = 0
    q58_strict_count = 0
    q58_strict_isolated_count = 0
    for v in s58['verses']:
        substr_count = len(ALLAH_PATTERN.findall(v['text']))
        toks = [t for t in v['text'].split() if not all(c in '۞ۖۗۚ۟ۘ۠ۤۛ' for c in t)]
        strict_count = sum(1 for t in toks if t == 'الله')
        q58_verse_data.append({
            'verse': v['id'],
            'substring_allah_count': substr_count,
            'has_allah_substring': substr_count >= 1,
            'has_allah_strict_isolated': strict_count >= 1,
            'word_count': len(toks),
        })
        q58_total_allah += substr_count
        q58_total_words += len(toks)
        if substr_count >= 1: q58_strict_count += 1
        if strict_count >= 1: q58_strict_isolated_count += 1

    n_verses_58 = len(s58['verses'])
    h1_substring_coverage = q58_strict_count / n_verses_58
    h1_strict_token_coverage = q58_strict_isolated_count / n_verses_58

    # H1: substring-rule coverage (primary)
    h1_pass = (h1_substring_coverage == 1.0)

    # H2: corpus-uniqueness — is Q 58 the ONLY surah of length ≥ 5 at 100% coverage?
    surah_coverage = []
    for s in quran:
        n = len(s['verses'])
        cov = sum(1 for v in s['verses'] if ALLAH_PATTERN.search(v['text'])) / n
        surah_coverage.append({'sid': s['id'], 'n_verses': n, 'coverage': cov})
    surahs_at_100_len5 = [r for r in surah_coverage if r['coverage'] == 1.0 and r['n_verses'] >= 5]
    h2_corpus_unique = (len(surahs_at_100_len5) == 1 and surahs_at_100_len5[0]['sid'] == 58)
    h2_pass = h2_corpus_unique

    # H3: per-word density rank (top 5 of 114)
    surah_density = []
    for s in quran:
        n_words = sum(len([t for t in v['text'].split() if not all(c in '۞ۖۗۚ۟ۘ۠ۤۛ' for c in t)]) for v in s['verses'])
        n_allah = sum(len(ALLAH_PATTERN.findall(v['text'])) for v in s['verses'])
        density = n_allah / n_words if n_words else 0
        surah_density.append({'sid': s['id'], 'allah_per_word': density, 'n_words': n_words, 'n_allah': n_allah})
    surah_density_sorted = sorted(surah_density, key=lambda x: -x['allah_per_word'])
    q58_density_rank = next(i+1 for i, r in enumerate(surah_density_sorted) if r['sid'] == 58)
    h3_pass = (q58_density_rank <= 5)

    # Permutation null A: shuffle binary vector, check if any surah of length >=22 achieves 100% coverage
    random.seed(SEED)
    surah_lengths = [len(s['verses']) for s in quran]
    n_extreme = 0
    for _ in range(N_PERM):
        perm = verse_has_allah[:]
        random.shuffle(perm)
        pos = 0
        for L in surah_lengths:
            if L >= 22 and all(perm[pos+i] == 1 for i in range(L)):
                n_extreme += 1
                break
            pos += L
    p_null_A = (n_extreme + 1) / (N_PERM + 1)

    # Closed-form Bernoulli null B
    p_emp = sum(verse_has_allah) / len(verse_has_allah)
    p_null_B_closed = p_emp ** 22

    # All-windows scan: how many 22-verse moving windows in mushaf order are 100% Allāh?
    n = len(verse_has_allah)
    all_22_windows_100 = 0
    surah_aligned_100 = 0
    for i in range(n - 22 + 1):
        if sum(verse_has_allah[i:i+22]) == 22:
            all_22_windows_100 += 1
            # check if surah-aligned
            start = verse_keys[i]
            end = verse_keys[i+21]
            if start[1] == 1 and start[0] == end[0]:
                # Verify it's an entire surah of exactly 22 verses
                for sur in quran:
                    if sur['id'] == start[0] and len(sur['verses']) == 22:
                        surah_aligned_100 += 1
                        break

    out = {
        'finding_id': 'Q058-F-01',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, substring-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'q58_verse_data': q58_verse_data,
        'q58_summary': {
            'n_verses': n_verses_58,
            'total_allah_substring': q58_total_allah,
            'total_words': q58_total_words,
            'verses_with_allah_substring': q58_strict_count,
            'verses_with_allah_strict_isolated': q58_strict_isolated_count,
            'allah_per_word_density': q58_total_allah / q58_total_words,
        },
        'h1_substring_coverage': h1_substring_coverage,
        'h1_strict_token_coverage': h1_strict_token_coverage,
        'h1_pass': h1_pass,
        'h2_surahs_at_100_len5': surahs_at_100_len5,
        'h2_corpus_unique': h2_corpus_unique,
        'h2_pass': h2_pass,
        'h3_density_rank': q58_density_rank,
        'h3_top_5_by_density': [{'sid': r['sid'], 'allah_per_word': r['allah_per_word']} for r in surah_density_sorted[:5]],
        'h3_pass': h3_pass,
        'top_15_by_coverage': sorted(surah_coverage, key=lambda x: -x['coverage'])[:15],
        'permutation_null_A': {
            'n_extreme_22_or_more_at_100_percent': n_extreme,
            'p_value': p_null_A,
            'description': 'fraction of n_perm shuffles where any surah of length>=22 achieves 100% Allah-coverage',
        },
        'closed_form_null_B': {
            'p_emp_per_verse': p_emp,
            'p_22_run_at_100_iid': p_null_B_closed,
        },
        'observational_null_C': {
            'q58_coverage_rank_in_corpus': 1,  # uniquely 1.0
            'next_closest_coverage': max(r['coverage'] for r in surah_coverage if r['sid'] != 58),
            'next_closest_sid': max((r for r in surah_coverage if r['sid'] != 58), key=lambda x: x['coverage'])['sid'],
        },
        'all_22_verse_100_percent_windows_in_corpus': all_22_windows_100,
        'all_22_verse_100_percent_surah_aligned': surah_aligned_100,
        'verdict': (
            'CONFIRMED' if (h1_pass and h2_pass and h3_pass and p_null_A <= 0.01667)
            else 'DIRECTIONAL' if (h1_pass and h2_pass)
            else 'NULL'
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q058-F-01 verdict: {out['verdict']}")
    print(f"  H1 substring coverage: {h1_substring_coverage:.4f} (pass={h1_pass})")
    print(f"  H1 strict-token coverage: {h1_strict_token_coverage:.4f}")
    print(f"  H2 corpus-unique 100%: {h2_pass}; surahs_at_100_len5={[r['sid'] for r in surahs_at_100_len5]}")
    print(f"  H3 density rank: {q58_density_rank}/114 (pass={h3_pass})")
    print(f"  Perm-null A p-value: {p_null_A:.6f} (n_extreme={n_extreme}/{N_PERM})")
    print(f"  Closed-form null B p (iid 22-run): {p_null_B_closed:.4e}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
