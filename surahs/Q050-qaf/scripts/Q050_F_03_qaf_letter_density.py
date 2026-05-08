#!/usr/bin/env python3
"""
Q050-F-03 — letter-ق density audit (with singleton-letter cohort replication).

Tests host-letter density for Q 50 (ق), Q 38 (ص), Q 68 (ن) against
length-matched random rest-of-corpus contiguous-verse windows.

Bonferroni-3 across the singleton-letter cohort.
"""
import hashlib, json, sys, random

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q050-qaf/preregs/Q050-F-03-qaf-letter-density-prereg.md'
EXPECTED_SHA = '66c22536f23c87e5d15ca99192c3ba30fc027632bf210380e33aedaaaa1c8e2e'

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

# Build flat verse list with strip-marks
flat_verses = []
for q in qd:
    s = q['id']
    for v in q['verses']:
        flat_verses.append((s, v['id'], strip_marks(v['text'])))

def count_letter_in_verses(verses_subset, letter):
    """Count letter occurrences and total Arabic-letter graphemes."""
    n_letter = 0
    n_total = 0
    for (s, vid, t) in verses_subset:
        for c in t:
            if c.isalpha():
                n_total += 1
                if c == letter:
                    n_letter += 1
    return n_letter, n_total

def run_test(target_surah, host_letter):
    """Run the density test for one (surah, host-letter) pair."""
    surah_verses = [v for v in flat_verses if v[0] == target_surah]
    n_verses_target = len(surah_verses)
    obs_letter, obs_total = count_letter_in_verses(surah_verses, host_letter)
    obs_rate = obs_letter / obs_total if obs_total > 0 else 0.0

    # Null pool: contiguous-verse windows of size K=n_verses_target, no overlap with target surah
    rng = random.Random(SEED + target_surah)
    n_total_v = len(flat_verses)
    null_rates = []
    for it in range(N_PERM):
        while True:
            start = rng.randint(0, n_total_v - n_verses_target)
            window = flat_verses[start:start + n_verses_target]
            if not any(v[0] == target_surah for v in window):
                break
        nl, nt = count_letter_in_verses(window, host_letter)
        rate = nl / nt if nt > 0 else 0.0
        null_rates.append(rate)

    n_ge = sum(1 for r in null_rates if r >= obs_rate)
    p_value = (n_ge + 1) / (N_PERM + 1)
    null_mean = sum(null_rates) / N_PERM
    null_sd = (sum((r - null_mean)**2 for r in null_rates) / N_PERM) ** 0.5
    z = (obs_rate - null_mean) / null_sd if null_sd > 0 else None

    return {
        'surah': target_surah,
        'host_letter': host_letter,
        'n_verses': n_verses_target,
        'obs_host_letter_count': obs_letter,
        'obs_total_letter_count': obs_total,
        'obs_rate': round(obs_rate, 6),
        'null_mean_rate': round(null_mean, 6),
        'null_sd_rate': round(null_sd, 6),
        'z': round(z, 4) if z is not None else None,
        'p_value_one_sided': round(p_value, 6),
    }

# Run all 3 sub-tests
results = []
for (s, letter) in [(50, 'ق'), (38, 'ص'), (68, 'ن')]:
    r = run_test(s, letter)
    results.append(r)
    print(f'Q{s} ({letter}): obs_rate={r["obs_rate"]:.5f}, null_mean={r["null_mean_rate"]:.5f}, '
          f'z={r["z"]}, p={r["p_value_one_sided"]:.6f}')

# Bonferroni-3
ALPHA_BON = 0.05 / 3
verdicts = []
for r in results:
    if r['p_value_one_sided'] < ALPHA_BON:
        v = 'CONFIRMED'
    elif r['p_value_one_sided'] < 0.05:
        v = 'DIRECTIONAL_RAW_POSITIVE_BON_FAIL'
    else:
        v = 'NULL'
    verdicts.append(v)

n_confirmed = sum(1 for v in verdicts if v == 'CONFIRMED')
if n_confirmed == 3:
    cohort_verdict = 'COHORT-CONFIRMED'
elif n_confirmed == 2:
    cohort_verdict = 'PARTIAL-2/3'
elif n_confirmed == 1:
    cohort_verdict = 'PARTIAL-1/3-(individual-only)'
else:
    cohort_verdict = 'NULL'

output = {
    'finding_id': 'Q050-F-03',
    'prereg_sha256': actual_sha,
    'date_run': '2026-05-07',
    'rules_tuple': '(no-tashkeel, grapheme-counting, mushaf-marks-stripped, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)',
    'seed': SEED,
    'n_perm': N_PERM,
    'bonferroni_k': 3,
    'alpha_bonferroni': round(ALPHA_BON, 6),
    'per_surah_results': results,
    'per_surah_verdicts': verdicts,
    'cohort_verdict': cohort_verdict,
}

out_path = f'{PROJECT}/surahs/Q050-qaf/csv/Q050-F-03.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q050-F-03: COHORT_VERDICT={cohort_verdict}')
print(f'  Verdicts: {verdicts}')
print(f'  Output: {out_path}')
