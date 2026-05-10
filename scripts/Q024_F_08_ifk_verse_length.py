#!/usr/bin/env python3
"""Q024-F-08: Ifk pericope (Q 24:11-20) verse-length vs ambient Q 24 (LOCKED pre-reg).

Tests whether the al-ifk narrative pericope has higher mean verse-length
(no-tashkeel orthographic words) than the ambient Q 24 verses.

PRE-REGISTERED DIRECTION: ifk > ambient (narrative expansion).
"""
import json, hashlib, os, random, statistics

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-08-ifk-verse-length-vs-ambient-prereg.md"
EXPECTED_SHA = "1e4caa474df6746b7c5875066dfa010f3aa4b81b743fed1a827a17c599fc13d4"
QURAN = f"{PROJECT}/quran-text/quran-no-tashkeel.json"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-08.json"

SEED = 20260509
N_PERM = 10000
ALPHA_BONF = 0.0125
MUSHAF_MARKS = set('۞ۖۗۚۛۜ')

# 1. SHA-lock
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256:    {sha}")
print(f"Expected:          {EXPECTED_SHA}")
if sha != EXPECTED_SHA:
    raise SystemExit("FAIL: pre-reg SHA mismatch — abort.")
print("OK SHA verified.\n")

# 2. Load Q 24
with open(QURAN) as f:
    quran = json.load(f)
q24 = next(s for s in quran if s['id'] == 24)

# 3. Per-verse word-count
def word_count(text):
    return sum(1 for w in text.split() if w and not all(c in MUSHAF_MARKS for c in w))

verse_lens = {v['id']: word_count(v['text']) for v in q24['verses']}
print(f"Q 24 verse-count: {len(verse_lens)}")

# 4. Partition
ifk_ids = list(range(11, 21))
ambient_ids = [vid for vid in verse_lens if vid not in ifk_ids]
ifk_lens = [verse_lens[v] for v in ifk_ids]
amb_lens = [verse_lens[v] for v in ambient_ids]

mean_ifk = statistics.mean(ifk_lens)
mean_amb = statistics.mean(amb_lens)
median_ifk = statistics.median(ifk_lens)
median_amb = statistics.median(amb_lens)
delta = mean_ifk - mean_amb
print(f"\nifk     (n={len(ifk_lens)}): mean={mean_ifk:.2f}, median={median_ifk}, lens={ifk_lens}")
print(f"ambient (n={len(amb_lens)}): mean={mean_amb:.2f}, median={median_amb}")
print(f"Δ (ifk − ambient): {delta:+.3f}")

# 5. Permutation null: random 10-verse subsets of Q 24
rng = random.Random(SEED)
all_ids = list(verse_lens)
deltas = []
for _ in range(N_PERM):
    subset = set(rng.sample(all_ids, 10))
    s_lens = [verse_lens[v] for v in subset]
    c_lens = [verse_lens[v] for v in all_ids if v not in subset]
    deltas.append(statistics.mean(s_lens) - statistics.mean(c_lens))

# One-sided p (upper tail — pre-registered direction is positive)
p_one_upper = sum(1 for d in deltas if d >= delta) / N_PERM
p_two = sum(1 for d in deltas if abs(d) >= abs(delta)) / N_PERM
print(f"\nPermutation null (n_perm={N_PERM}, seed={SEED}):")
print(f"  p_one_upper (Δ ≥ observed): {p_one_upper:.4f}")
print(f"  p_two_sided:                {p_two:.4f}")
print(f"  Bonferroni α (k=4):         {ALPHA_BONF}")

# 6. Verdict — direction is pre-registered positive
if delta > 0:
    if p_one_upper < ALPHA_BONF:
        verdict = "CONFIRMED"
    elif p_one_upper < 0.05:
        verdict = "DIRECTIONAL"
    else:
        verdict = "WEAK-DIRECTIONAL"
else:
    # Reversed direction = pre-commit violation
    verdict = "NULL-pre-commit-violation"
print(f"\nVerdict: {verdict} (direction Δ {'>' if delta > 0 else '<'} 0)")
if delta < 0:
    print("\n*** PRE-COMMIT VIOLATION ***")
    print(f"    Pre-registered direction: ifk > ambient (positive Δ).")
    print(f"    Observed direction:       ifk < ambient (Δ = {delta:+.3f}).")
    print(f"    Per protocol §1.3 and §1.8, this is published as NULL with prominence.")
    print(f"    The narrative-pericope-expansion hypothesis is FALSIFIED for the al-ifk passage in Q 24.")

# 7. Honest descriptive note
print(f"\nDescriptive notes:")
print(f"  Q 24 has six verses ≥ 30 words (vv. {[v for v in all_ids if verse_lens[v] >= 30]}) — these are dispersed across the surah, not concentrated in the ifk block.")

# 8. Write JSON
out = {
    'finding_id': 'Q024-F-08',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'date': '2026-05-09',
    'rules_tuple': '(no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
    'ifk_verses': ifk_ids,
    'ifk_lens': ifk_lens,
    'ambient_n': len(amb_lens),
    'mean_ifk': mean_ifk,
    'mean_ambient': mean_amb,
    'median_ifk': median_ifk,
    'median_ambient': median_amb,
    'delta_ifk_minus_ambient': delta,
    'p_one_sided_upper': p_one_upper,
    'p_two_sided': p_two,
    'alpha_bonferroni': ALPHA_BONF,
    'n_perm': N_PERM,
    'verse_lens_full_q24': verse_lens,
    'verdict': verdict,
    'pre_committed_direction': 'ifk > ambient (positive Δ)',
    'observed_direction': 'ifk > ambient' if delta > 0 else 'ifk < ambient',
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\nWrote {OUT}")
