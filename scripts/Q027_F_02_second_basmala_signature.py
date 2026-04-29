#!/usr/bin/env python3
"""Q027-F-02 — Q 27:30 (second basmala) lexical-signature audit vs Q 1:1 basmala.

Pre-reg: surahs/Q027-al-naml/Q027-F-02-second-basmala-lexical-signature-prereg.md
Pre-reg SHA256: 0a6fb49cd4ccf57a842c07d6f72163cb1a6cdf0ca991657cab47de97031f9a08
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q027-al-naml/Q027-F-02-second-basmala-lexical-signature-prereg.md'
EXPECTED_SHA = '0a6fb49cd4ccf57a842c07d6f72163cb1a6cdf0ca991657cab47de97031f9a08'

PAUSE_RE = re.compile(r'[ۖۚ؛،۔ۗۘۙۛۜ۩]')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch\nexpected {EXPECTED_SHA}\nactual   {actual}", file=sys.stderr)
        sys.exit(1)


def tokens(text):
    return PAUSE_RE.sub(' ', text).split()


def main():
    verify_sha()

    sources = {
        'no_tashkeel': '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json',
        'min_tashkeel': '/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json',
        'full_tashkeel': '/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json',
    }
    results = {}

    for variant, path in sources.items():
        d = json.load(open(path))
        q1_v1 = d[0]['verses'][0]['text']
        q27_v30 = d[26]['verses'][29]['text']
        q1_tokens = tokens(q1_v1)
        q27_30_tokens = tokens(q27_v30)
        # find first token starting with 'بسم' or 'بِسم' or 'بِسۡم' to slice
        # use a robust search: find the index where the token contains "بسم" prefix
        bism_idx = None
        for i, t in enumerate(q27_30_tokens):
            # Strip diacritics for prefix check
            t_strip = re.sub(r'[ً-ٰٟـۜ-ۭ]', '', t)
            if t_strip.startswith('بسم'):
                bism_idx = i
                break
        slice_tokens = q27_30_tokens[bism_idx:] if bism_idx is not None else None

        match_exact = (q1_tokens == slice_tokens) if slice_tokens else False
        # also stripped-diacritic comparison (for full-tashkeel case)
        def strip(s):
            return [re.sub(r'[ً-ٰٟـۜ-ۭ]', '', x) for x in s]
        match_stripped = (strip(q1_tokens) == strip(slice_tokens)) if slice_tokens else False

        # Levenshtein on token sequences
        def lev(a, b):
            if not a:
                return len(b)
            if not b:
                return len(a)
            prev = list(range(len(b) + 1))
            for i, ca in enumerate(a, 1):
                cur = [i] + [0] * len(b)
                for j, cb in enumerate(b, 1):
                    cur[j] = min(cur[j - 1] + 1, prev[j] + 1,
                                 prev[j - 1] + (0 if ca == cb else 1))
                prev = cur
            return prev[-1]

        token_lev = lev(q1_tokens, slice_tokens) if slice_tokens else None
        token_lev_stripped = lev(strip(q1_tokens), strip(slice_tokens)) if slice_tokens else None

        results[variant] = {
            'q1_v1_text': q1_v1,
            'q27_v30_text': q27_v30,
            'q1_tokens': q1_tokens,
            'q27_v30_tokens': q27_30_tokens,
            'q27_30_basmala_slice': slice_tokens,
            'bism_token_index_in_q27_30': bism_idx,
            'match_exact_byte_for_byte': match_exact,
            'match_after_diacritic_strip': match_stripped,
            'token_levenshtein_exact': token_lev,
            'token_levenshtein_stripped': token_lev_stripped,
        }

    # Determine overall verdict
    no_tashkeel_match = results['no_tashkeel']['match_exact_byte_for_byte']
    if no_tashkeel_match:
        verdict = 'CONFIRMED_LEXICAL_MATCH_NO_TASHKEEL'
    else:
        verdict = 'DIVERGENT'

    # Test for diacritic divergence in tashkeel
    tashkeel_divergence = []
    for variant in ['min_tashkeel', 'full_tashkeel']:
        r = results[variant]
        if not r['match_exact_byte_for_byte']:
            tashkeel_divergence.append({
                'variant': variant,
                'token_lev': r['token_levenshtein_exact'],
                'q1_tokens_full': r['q1_tokens'],
                'slice_tokens_full': r['q27_30_basmala_slice'],
            })

    out = {
        'finding_id': 'Q027-F-02',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(orthographic-token, three tashkeel variants, Hafs-Kufan, Mashriqi)',
        'method': 'Slice basmala-phrase from Q 27:30 starting at first token containing بسم; compare to Q 1:1.',
        'results_per_variant': results,
        'verdict_no_tashkeel': verdict,
        'tashkeel_diacritic_divergences': tashkeel_divergence,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/Q027-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q027-F-02: no-tashkeel exact match = {no_tashkeel_match}; min match = {results['min_tashkeel']['match_exact_byte_for_byte']}; full match = {results['full_tashkeel']['match_exact_byte_for_byte']}")


if __name__ == '__main__':
    main()
