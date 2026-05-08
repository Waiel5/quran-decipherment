#!/usr/bin/env python3
"""
Q050-F-02 — Body-part metaphor density audit.

Test whether Q 50 has a body-part-vocabulary token rate (per 1000 word-tokens)
exceeding 95% of length-matched (45-verse contiguous-window) random samples
from the rest-of-corpus.
"""
import hashlib, json, sys, random

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q050-qaf/preregs/Q050-F-02-body-part-density-prereg.md'
EXPECTED_SHA = '8fb095ca71d9727994d7182c614f4df9d3c378ea4b74f1d2891fe1a0945e6b9b'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

SEED = 20260507
N_PERM = 10000
WINDOW_K = 45  # Q 50 has 45 verses

with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json') as f:
    qd = json.load(f)

mushaf_marks = ['۞', 'ۚ', 'ۖ', 'ۗ', 'ۛ', 'ۜ', '۠', '۩', 'ۭ']

def strip_marks(t):
    for m in mushaf_marks:
        t = t.replace(m, '')
    return ' '.join(t.split())

# Locked body-part vocabulary (no-tashkeel substring patterns).
# These are root-stem prefixes that appear inside a token; we test substring containment.
BODY_PART_PATTERNS = [
    'ورد',     # warīd (jugular vein) — but ورد is also "rose"; we narrow below
    'قلب',     # qalb (heart)
    'فؤاد',    # fuʾād (heart)
    'لسان',    # lisān (tongue)
    'نفس',     # nafs (soul)
    'عين',     # ʿayn (eye)
    'سمع',     # samʿ (hearing)
    'بصر',     # baṣar (sight)
    'جلد',     # jild (skin)
    'دم',      # damm (blood)
    'لحم',     # laḥm (flesh)
    'عظم',     # ʿaẓm (bone)
    'رأس',     # raʾs (head)
    'يد',      # yad (hand)
    'رجل',     # rijl (foot/leg) — also "man"; we accept the dual reading
    'فم',      # fam (mouth)
    'اذن',     # ʾudhun (ear)
    'وجه',     # wajh (face)
    'صدر',     # ṣadr (chest)
    'كبد',     # kabd (liver)
    'بطن',     # baṭn (belly)
    'حلق',     # ḥalq (throat)
    'عنق',     # ʿunuq (neck)
    'كتف',     # katf (shoulder)
    'ظهر',     # ẓahr (back)
]
# Note: we use SUBSTRING matching because the canonical text has full-token forms
# like 'الوريد', 'القلب', 'صدورهم'. The patterns are stems.

# Build flat verse list (skip basmala by counting verse 1 of Q 1 as 'الحمد...')
# In the quran-no-tashkeel.json, basmala IS verse 1 of Q 1 only. For Q 2-114,
# basmala is the standard surah header but is NOT a separate verse in the JSON.
# So we use all verses as-is; basmala is auto-counted-only-in-Q1 (default rules-tuple).
flat_verses = []  # list of (surah, verse_idx_in_surah, text_no_marks)
for q in qd:
    s = q['id']
    for v_idx, v in enumerate(q['verses']):
        flat_verses.append((s, v['id'], strip_marks(v['text'])))

def count_body_parts_and_words(verses_subset):
    n_words = 0
    n_body = 0
    for (s, vid, t) in verses_subset:
        tokens = t.split()
        # Skip muqaṭṭaʿāt-letter tokens at start of surah-verse-1 (they are not "words" in normal sense)
        # but for fairness across ALL windows we INCLUDE them; muqaṭṭaʿāt verses are tiny in number.
        n_words += len(tokens)
        for tok in tokens:
            for pat in BODY_PART_PATTERNS:
                if pat in tok:
                    n_body += 1
                    break
    return n_body, n_words

# Q 50 observed
q50_verses = [v for v in flat_verses if v[0] == 50]
q50_body, q50_words = count_body_parts_and_words(q50_verses)
q50_rate_per_1000 = (q50_body / q50_words) * 1000.0
print(f'Q 50: {q50_body} body-part tokens / {q50_words} words = {q50_rate_per_1000:.3f} per 1000')

# Length-matched random null
rng = random.Random(SEED)
null_rates = []
n_total = len(flat_verses)
# Exclude Q 50 verses from the null pool
non_q50_indices = [i for i, v in enumerate(flat_verses) if v[0] != 50]
# We need contiguous K-verse windows. Use consecutive indices but skip ones that overlap Q 50.
for it in range(N_PERM):
    # Pick a random start s.t. start + K is within bounds AND no Q 50 verse in window
    while True:
        start = rng.randint(0, n_total - WINDOW_K)
        window = flat_verses[start:start + WINDOW_K]
        if not any(v[0] == 50 for v in window):
            break
    nb, nw = count_body_parts_and_words(window)
    if nw > 0:
        rate = (nb / nw) * 1000.0
    else:
        rate = 0.0
    null_rates.append(rate)

# Empirical p
n_ge = sum(1 for r in null_rates if r >= q50_rate_per_1000)
p_value = (n_ge + 1) / (N_PERM + 1)

# Percentile
n_le = sum(1 for r in null_rates if r <= q50_rate_per_1000)
percentile = n_le / N_PERM * 100.0

null_mean = sum(null_rates) / N_PERM
null_sd = (sum((r - null_mean)**2 for r in null_rates) / N_PERM) ** 0.5

if p_value < 0.05:
    verdict = 'CONFIRMED'
elif p_value < 0.10:
    verdict = 'DIRECTIONAL'
else:
    verdict = 'NULL'

# Identify the actual body-part hits in Q 50 for transparency
body_hits_q50 = []
for (s, vid, t) in q50_verses:
    for tok in t.split():
        for pat in BODY_PART_PATTERNS:
            if pat in tok:
                body_hits_q50.append({'verse': vid, 'token': tok, 'pattern': pat})
                break

output = {
    'finding_id': 'Q050-F-02',
    'prereg_sha256': actual_sha,
    'date_run': '2026-05-07',
    'rules_tuple': '(no-tashkeel, orthographic-token, exact-substring root-match against pre-locked vocab list, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)',
    'seed': SEED,
    'n_perm': N_PERM,
    'window_k_verses': WINDOW_K,
    'body_part_patterns': BODY_PART_PATTERNS,
    'q50_body_token_count': q50_body,
    'q50_total_word_count': q50_words,
    'q50_body_rate_per_1000_words': round(q50_rate_per_1000, 4),
    'null_mean_rate_per_1000': round(null_mean, 4),
    'null_sd_rate_per_1000': round(null_sd, 4),
    'q50_z_vs_null': round((q50_rate_per_1000 - null_mean) / null_sd, 4) if null_sd > 0 else None,
    'q50_percentile_in_null': round(percentile, 2),
    'p_value_one_sided': round(p_value, 6),
    'verdict': verdict,
    'q50_body_hits_per_verse': body_hits_q50,
}

out_path = f'{PROJECT}/surahs/Q050-qaf/csv/Q050-F-02.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q050-F-02: VERDICT={verdict}')
print(f'  Q50 rate: {q50_rate_per_1000:.3f} per 1000 words')
print(f'  Null mean: {null_mean:.3f} ± {null_sd:.3f}')
print(f'  Q50 percentile: {percentile:.2f}')
print(f'  p (1-sided): {p_value:.6f}')
print(f'  Output: {out_path}')
