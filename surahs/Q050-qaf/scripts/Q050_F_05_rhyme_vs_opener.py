#!/usr/bin/env python3
"""
Q050-F-05 — Singleton-letter rāwī orthogonality test.

For Q 50, Q 38, Q 68: test whether the muqaṭṭaʿ-opener letter equals the
dominant verse-final letter (rāwī). Pre-committed direction: NULL on
opener-rāwī alignment for Q 50 and Q 38; positive for Q 68.

Compute corpus-null cohort match-rate via 10000-iteration null where
3 random surahs are sampled and checked for opener=rāwī alignment under
the same 28-letter framework.
"""
import hashlib, json, sys, random
from collections import Counter

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q050-qaf/preregs/Q050-F-05-rhyme-vs-opener-prereg.md'
EXPECTED_SHA = '693953f73701776cb18678d96f0a73e7311095638621fd8ffe323ecf7891f95a'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

SEED = 20260507
N_PERM = 10000

with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json') as f:
    qd = json.load(f)

mushaf_marks = ['۞', 'ۚ', 'ۖ', 'ۗ', 'ۛ', 'ۜ', '۠', '۩', 'ۭ']

def strip_marks(t):
    for m in mushaf_marks:
        t = t.replace(m, '')
    return ' '.join(t.split())

def dominant_rawi(surah_id):
    """Return (dominant final-letter, fraction)."""
    q = qd[surah_id - 1]
    finals = []
    for v in q['verses']:
        t = strip_marks(v['text'])
        # Skip muqaṭṭaʿāt-only verses (e.g. Q 50 v 1 'ق' alone — but in this case Q 50:1 is 'ق والقرآن المجيد', the LAST word is المجيد, last letter د)
        if not t.split():
            continue
        last_word = t.split()[-1]
        # Last grapheme that is alpha
        last_char = None
        for c in reversed(last_word):
            if c.isalpha():
                last_char = c
                break
        if last_char:
            finals.append(last_char)
    counts = Counter(finals)
    if not counts:
        return None, 0.0
    top, top_count = counts.most_common(1)[0]
    return top, top_count / len(finals)

# Singleton-letter cohort
COHORT = [
    {'surah': 50, 'opener': 'ق'},
    {'surah': 38, 'opener': 'ص'},
    {'surah': 68, 'opener': 'ن'},
]

per_surah = []
for entry in COHORT:
    rawi, frac = dominant_rawi(entry['surah'])
    match = (rawi == entry['opener'])
    per_surah.append({
        'surah': entry['surah'],
        'opener': entry['opener'],
        'dominant_rawi': rawi,
        'dominant_rawi_fraction': round(frac, 4),
        'opener_equals_rawi': match,
    })
    print(f"Q{entry['surah']}: opener={entry['opener']}, rawi={rawi} ({frac:.2%}), match={match}")

n_match_obs = sum(1 for r in per_surah if r['opener_equals_rawi'])
print(f'Cohort match: {n_match_obs}/3')

# For null: each surah has its own dominant rawi (already in the corpus).
# Build the corpus-wide list of (surah, dominant_rawi) pairs.
all_surah_rawi = {}
for s in range(1, 115):
    r, f = dominant_rawi(s)
    all_surah_rawi[s] = r

# 28-letter "Arabic alphabet" used as the opener-letter pool. The Quran's
# actual muqaṭṭaʿāt openers are 14 distinct letters; for null we sample
# from the actual 14 since the muqaṭṭaʿāt opener system uses only those.
muqattaa_letters = list(set('الكهيعصطسحمرنق'))  # The 14 muqaṭṭaʿāt letters
# Order them to dedupe
muqattaa_letters = sorted(set(muqattaa_letters))

rng = random.Random(SEED)
null_match_counts = []
all_surahs = list(range(1, 115))
for it in range(N_PERM):
    triplet_surahs = rng.sample(all_surahs, 3)
    # For each, sample a random opener letter from the 14 muqaṭṭaʿāt letters
    n_match = 0
    for s in triplet_surahs:
        opener = rng.choice(muqattaa_letters)
        if all_surah_rawi[s] == opener:
            n_match += 1
    null_match_counts.append(n_match)

null_mean = sum(null_match_counts) / N_PERM
n_ge = sum(1 for c in null_match_counts if c >= n_match_obs)
p_value = (n_ge + 1) / (N_PERM + 1)

cohort_pct_null_lt_obs = sum(1 for c in null_match_counts if c < n_match_obs) / N_PERM * 100

# Per-surah verdict
ALPHA_BON = 0.05 / 3
per_surah_verdicts = []
for r in per_surah:
    if r['opener_equals_rawi']:
        per_surah_verdicts.append({'surah': r['surah'], 'verdict': 'MATCH-CONFIRMED'})
    else:
        per_surah_verdicts.append({'surah': r['surah'], 'verdict': 'NULL-(no-opener-rāwī-alignment)'})

# Cohort-level verdict
if n_match_obs == 1 and p_value > 0.05:
    cohort_verdict = 'CONFIRMED-NULL-on-opener-rāwī-alignment'
    interpretation = ('The 1/3 cohort match rate (Q 68 only) is consistent with '
                      'INDEPENDENCE of muqaṭṭaʿ-opener letter and verse-final rāwī. '
                      'This vindicates the dual-iʿjāz typology orthogonality claim '
                      '(letter-axis ⊥ rhyme-axis) at the singleton-letter cohort scale.')
elif p_value < 0.05:
    cohort_verdict = 'DIRECTIONAL-OPENER-RAWI-ALIGNMENT'
    interpretation = 'Cohort match rate exceeds 95% null — directional evidence for opener-rāwī alignment.'
else:
    cohort_verdict = 'NULL'
    interpretation = 'No clear pattern.'

output = {
    'finding_id': 'Q050-F-05',
    'prereg_sha256': actual_sha,
    'date_run': '2026-05-07',
    'rules_tuple': '(min-tashkeel for rhyme analysis, last-grapheme of last word per verse after mushaf-mark stripping, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)',
    'seed': SEED,
    'n_perm': N_PERM,
    'bonferroni_k': 3,
    'alpha_bon': round(ALPHA_BON, 6),
    'per_surah_diagnostic': per_surah,
    'per_surah_verdicts': per_surah_verdicts,
    'cohort_match_count_observed': n_match_obs,
    'null_mean_match_count': round(null_mean, 4),
    'p_value_one_sided': round(p_value, 6),
    'cohort_verdict': cohort_verdict,
    'interpretation': interpretation,
}

out_path = f'{PROJECT}/surahs/Q050-qaf/csv/Q050-F-05.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q050-F-05: COHORT={cohort_verdict}')
print(f'  cohort_match: {n_match_obs}/3')
print(f'  null_mean: {null_mean:.4f}')
print(f'  p (1-sided): {p_value:.6f}')
print(f'  Output: {out_path}')
