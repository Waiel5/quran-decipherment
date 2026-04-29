#!/usr/bin/env python3
"""Q027-F-03 — Sulaymān-token concentration in Q 27 vs corpus.

Pre-reg: surahs/Q027-al-naml/Q027-F-03-sulayman-token-concentration-prereg.md
Pre-reg SHA256: 03dd2f12bcc9755b8f2db1bb5ce0960d4fe7c163c9878ba3a81a73c0160493c2
"""
import json, re, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q027-al-naml/Q027-F-03-sulayman-token-concentration-prereg.md'
EXPECTED_SHA = '03dd2f12bcc9755b8f2db1bb5ce0960d4fe7c163c9878ba3a81a73c0160493c2'
SULAYMAN_SUBSTRINGS = ('سليمان', 'سليمن')

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
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    per_surah = []
    attestations = []
    for s in d:
        toks = []
        for v in s['verses']:
            for t in tokens(v['text']):
                toks.append(t)
                if any(sub in t for sub in SULAYMAN_SUBSTRINGS):
                    attestations.append({'surah': s['id'], 'verse': v['id'], 'token': t})
        n_count = sum(1 for t in toks if any(sub in t for sub in SULAYMAN_SUBSTRINGS))
        per_surah.append({'surah': s['id'], 'name': s['transliteration'],
                          'n_words': len(toks), 'sulayman_count': n_count})

    total = sum(x['sulayman_count'] for x in per_surah)
    q27_count = next(x['sulayman_count'] for x in per_surah if x['surah'] == 27)
    concentration = q27_count / total if total else 0.0

    # Find max and rank
    sorted_per = sorted(per_surah, key=lambda x: -x['sulayman_count'])
    rank_q27 = next(i + 1 for i, x in enumerate(sorted_per) if x['surah'] == 27)
    is_max = (rank_q27 == 1)

    # Permutation null
    rng = random.Random(42)
    weights = [x['n_words'] for x in per_surah]
    total_words = sum(weights)
    cumprob = []
    s_acc = 0.0
    for w in weights:
        s_acc += w / total_words
        cumprob.append(s_acc)

    n_perm = 10000
    perm_q27_shares = []
    perm_max_shares = []
    for _ in range(n_perm):
        counts = [0] * len(per_surah)
        for _i in range(total):
            r = rng.random()
            lo, hi = 0, len(cumprob)
            while lo < hi:
                mid = (lo + hi) // 2
                if r < cumprob[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            counts[lo] += 1
        perm_q27_shares.append(counts[26] / total)  # surah 27 is index 26
        perm_max_shares.append(max(counts) / total)

    p_perm_q27 = (1 + sum(1 for c in perm_q27_shares if c >= concentration)) / (1 + n_perm)
    p_perm_max = (1 + sum(1 for c in perm_max_shares if c >= concentration)) / (1 + n_perm)

    # Verdict
    if is_max and p_perm_q27 < 0.0125 and concentration < 0.92:
        verdict = 'CONFIRMED'
    elif is_max and p_perm_q27 < 0.0125:
        verdict = 'CONFIRMED_HIGH_CONCENTRATION'
    elif is_max:
        verdict = 'DIRECTIONAL_MAX_NOT_NULL_SIG'
    else:
        verdict = 'NULL_OR_DIRECTIONAL'

    out = {
        'finding_id': 'Q027-F-03',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-substring-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'orthographic substring match for "سليمان" / "سليمن"; permutation null over surah lengths',
        'substrings_matched': list(SULAYMAN_SUBSTRINGS),
        'total_attestations': total,
        'q27_count': q27_count,
        'q27_concentration': concentration,
        'q27_rank_among_all_surahs': rank_q27,
        'is_max_surah': is_max,
        'all_attestations': attestations,
        'per_surah_nonzero': [x for x in per_surah if x['sulayman_count'] > 0],
        'n_perm': n_perm,
        'seed': 42,
        'p_perm_q27_share_one_sided_upper': p_perm_q27,
        'p_perm_max_share_one_sided_upper': p_perm_max,
        'bonferroni_k': 4,
        'alpha_bonferroni': 0.0125,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/Q027-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q027-F-03: total Sulayman = {total}, Q27 = {q27_count}, "
          f"concentration = {concentration:.4f}, rank_q27 = {rank_q27}, "
          f"p_perm_q27 = {p_perm_q27:.4f}, verdict = {verdict}")


if __name__ == '__main__':
    main()
