#!/usr/bin/env python3
"""Q027-F-01 — Naml-token (ant) concentration in Q 27 vs corpus.

Pre-reg: surahs/Q027-al-naml/Q027-F-01-naml-token-concentration-prereg.md
Pre-reg SHA256: 0e68fc3d2ba709191b738d1228668cc1f40979da0fe5f09ea90be2f4f717aedd
"""
import json, re, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q027-al-naml/Q027-F-01-naml-token-concentration-prereg.md'
EXPECTED_SHA = '0e68fc3d2ba709191b738d1228668cc1f40979da0fe5f09ea90be2f4f717aedd'
NAML_FORMS = {'النمل', 'نمل', 'نملة'}

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
    naml_attestations = []  # list of (surah_id, verse_id, token)
    for s in d:
        toks = []
        for v in s['verses']:
            for t in tokens(v['text']):
                toks.append(t)
                if t in NAML_FORMS:
                    naml_attestations.append((s['id'], v['id'], t))
        n_naml = sum(1 for t in toks if t in NAML_FORMS)
        per_surah.append({'surah': s['id'], 'name': s['transliteration'],
                          'n_words': len(toks), 'naml_count': n_naml})

    total_naml = sum(x['naml_count'] for x in per_surah)
    q27_naml = next(x['naml_count'] for x in per_surah if x['surah'] == 27)
    concentration = q27_naml / total_naml if total_naml else 0.0

    # Permutation null: redistribute total_naml proportional to surah length.
    rng = random.Random(42)
    weights = [x['n_words'] for x in per_surah]
    total_words = sum(weights)
    probs = [w / total_words for w in weights]
    cumprob = []
    s = 0.0
    for p in probs:
        s += p
        cumprob.append(s)

    n_perm = 10000
    perm_concentrations = []
    for _ in range(n_perm):
        counts = [0] * len(per_surah)
        for _i in range(total_naml):
            r = rng.random()
            # bisect
            lo, hi = 0, len(cumprob)
            while lo < hi:
                mid = (lo + hi) // 2
                if r < cumprob[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            counts[lo] += 1
        perm_concentrations.append(max(counts) / total_naml if total_naml else 0)

    p_perm = (1 + sum(1 for c in perm_concentrations if c >= concentration)) / (1 + n_perm)

    # Verdict
    success = (concentration >= 0.80) and (p_perm < 0.0125)
    if concentration >= 0.80:
        if p_perm < 0.0125:
            verdict = 'CONFIRMED'
        else:
            verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL_OR_DIRECTIONAL'

    out = {
        'finding_id': 'Q027-F-01',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'orthographic-exact-match per surah on naml forms; permutation null over per-surah token-length',
        'naml_forms_matched': sorted(NAML_FORMS),
        'total_attestations': total_naml,
        'attestations_full_list': [
            {'surah': a, 'verse': b, 'token': c} for a, b, c in naml_attestations
        ],
        'q27_count': q27_naml,
        'q27_concentration': concentration,
        'per_surah_nonzero': [x for x in per_surah if x['naml_count'] > 0],
        'n_perm': n_perm,
        'seed': 42,
        'p_perm_one_sided_upper': p_perm,
        'bonferroni_k': 4,
        'alpha_bonferroni': 0.0125,
        'success_criteria_met': success,
        'verdict': verdict,
        'note_excluded_form': 'Token "نملي" (Q 3:178) was EXCLUDED — different lexical root (m-l-y, not n-m-l).',
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/Q027-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q027-F-01: total naml = {total_naml}, Q27 = {q27_naml}, "
          f"concentration = {concentration:.4f}, p_perm = {p_perm:.4f}, verdict = {verdict}")


if __name__ == '__main__':
    main()
