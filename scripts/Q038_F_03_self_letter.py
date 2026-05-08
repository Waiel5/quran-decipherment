#!/usr/bin/env python3
"""Q038-F-03 — Singleton-letter self-reference rate; Bonferroni-3 over Q 38 (ص), Q 50 (ق), Q 68 (ن).

Pre-reg: surahs/Q038-sad/Q038-F-03-self-letter-prereg.md
Pre-reg SHA256: b437c3e2b0f87b375e2bc2a3757ad21225773c46ca03e0b7371faeb42cb41b61
Rules-tuple: (no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-03-self-letter-prereg.md'
EXPECTED_SHA = 'b437c3e2b0f87b375e2bc2a3757ad21225773c46ca03e0b7371faeb42cb41b61'
SEED = 20260507
N_PERM = 10000

# Singletons: surah id -> (letter, surah-name)
SINGLETONS = {
    38: ('ص', 'Sad'),
    50: ('ق', 'Qaf'),
    68: ('ن', 'Nun'),
}
# Multi-letter muq-tokens to strip from openings before counting body letters
MUQ_TOKENS = set(['الم', 'الر', 'المر', 'المص', 'كهيعص', 'طه', 'طسم', 'طس', 'يس',
                  'حم', 'عسق', 'ص', 'ق', 'ن'])
# Diacritic-like codepoints that aren't true letters
NON_LETTERS = set('۞۩ۭۚۖۗۘۙۜۤ ')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def strip_muq_body(verses):
    """For first verse, strip muq token; concatenate remaining text; return raw letter string (no spaces, no separators)."""
    txts = []
    for i, v in enumerate(verses):
        text = v['text']
        # Replace separators with space
        for sep in '۞۩ۭۚۖۗۘۙۜۤ':
            text = text.replace(sep, ' ')
        toks = text.split()
        if i == 0 and toks and toks[0] in MUQ_TOKENS:
            toks = toks[1:]
        txts.append(' '.join(toks))
    body = ' '.join(txts)
    # Strip non-letters and spaces
    return ''.join(ch for ch in body if ch not in NON_LETTERS)


def main():
    verify_sha()
    rng = random.Random(SEED)

    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    # Compute body for every surah (with muq stripped from each surah's opener)
    surah_bodies = {}
    for s in quran:
        surah_bodies[s['id']] = strip_muq_body(s['verses'])

    # Concatenate ALL letters from all surah bodies for the corpus baseline AND for the permutation null
    full_corpus_letters = ''.join(surah_bodies[sid] for sid in sorted(surah_bodies))

    results_per_singleton = {}
    for sid, (L, name) in SINGLETONS.items():
        body = surah_bodies[sid]
        n_body = len(body)
        cnt_L = body.count(L)
        rate_L = cnt_L / n_body if n_body else 0.0

        # Corpus excluding this surah
        corpus_excl = full_corpus_letters[:full_corpus_letters.find(body)] + full_corpus_letters[full_corpus_letters.find(body)+n_body:] \
            if body in full_corpus_letters else full_corpus_letters
        # Cleaner: rebuild from other surahs
        corpus_excl = ''.join(surah_bodies[s] for s in sorted(surah_bodies) if s != sid)
        rate_corpus_L = corpus_excl.count(L) / len(corpus_excl)
        Δ = rate_L - rate_corpus_L
        ratio = rate_L / rate_corpus_L if rate_corpus_L else float('inf')

        # Permutation null: draw 10000 random size-matched substrings from corpus_excl
        n_corpus = len(corpus_excl)
        null_rates = []
        for _ in range(N_PERM):
            start = rng.randrange(0, n_corpus - n_body + 1)
            sub = corpus_excl[start:start+n_body]
            null_rates.append(sub.count(L) / n_body)
        null_rates_sorted = sorted(null_rates)
        # one-tailed p (greater)
        p_greater = sum(1 for r in null_rates if r >= rate_L) / N_PERM
        null_mean = sum(null_rates)/N_PERM
        null_std = (sum((r-null_mean)**2 for r in null_rates)/N_PERM)**0.5

        results_per_singleton[sid] = {
            'surah': sid, 'name': name, 'letter': L,
            'n_body_letters': n_body,
            'count_L': cnt_L,
            'rate_L_in_body': rate_L,
            'rate_L_corpus_excl': rate_corpus_L,
            'delta_pct_pts': (Δ)*100,
            'ratio_self_to_corpus': ratio,
            'permutation_null_mean_rate': null_mean,
            'permutation_null_std': null_std,
            'p_greater_perm': p_greater,
            'direction_locked': 'HIGHER',
            'pre_commit_satisfied': rate_L > rate_corpus_L,
        }

    # Bonferroni-3
    alpha_bon = 0.05/3
    n_pass = sum(1 for r in results_per_singleton.values() if r['p_greater_perm'] < alpha_bon and r['pre_commit_satisfied'])

    direction_locked_satisfied_all = all(r['pre_commit_satisfied'] for r in results_per_singleton.values())

    if direction_locked_satisfied_all and n_pass == 3:
        verdict = 'CONFIRMED'
    elif direction_locked_satisfied_all and n_pass >= 2:
        verdict = 'DIRECTIONAL'
    elif not direction_locked_satisfied_all:
        verdict = 'PRE-COMMIT-VIOLATION'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-03',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, character-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'per-singleton own-letter-rate vs permutation null of size-matched random substrings from corpus excluding self',
        'alpha_bon': alpha_bon,
        'singletons': results_per_singleton,
        'n_pass_of_3': n_pass,
        'direction_locked_satisfied_all': direction_locked_satisfied_all,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    for sid in [38,50,68]:
        r = results_per_singleton[sid]
        print(f"Q{sid} ({r['letter']}): rate_self={r['rate_L_in_body']*100:.3f}%, rate_corpus={r['rate_L_corpus_excl']*100:.3f}%, "
              f"Δ={r['delta_pct_pts']:+.3f}pp, ratio={r['ratio_self_to_corpus']:.2f}x, p_perm={r['p_greater_perm']:.4f}")
    print(f"\nVerdict: {verdict} (n_pass={n_pass}/3 at α_bon={alpha_bon:.4f})")


if __name__ == '__main__':
    main()
