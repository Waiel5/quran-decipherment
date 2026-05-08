#!/usr/bin/env python3
"""
Q068-F-02 — letter ن self-reference frequency in Q 68 vs corpus baseline.
Direction-locked POSITIVE.
"""
import hashlib, json, os, random, re, sys, math

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q068-al-qalam/preregs/Q068-F-02-nun-letter-self-reference-prereg.md'
EXPECTED_SHA = '506e0277dc25ff5bafac7fce935f58449e4716c681d5800ed0f49a06cbadc8ee'

with open(PREREG, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')

SEED = 20260507
N_PERM = 10000

# Load Quran
with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    quran = json.load(f)

ARABIC_LETTER = re.compile(r'[ء-ي]')

def normalize_letters(s):
    """Strip non-letters, normalize alif/yaa/taa-marbutaah."""
    s = s.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
    s = s.replace('ى', 'ي').replace('ة', 'ه')
    return ''.join(ARABIC_LETTER.findall(s))

# Q 68 letter stream
q68_verses = quran[67]['verses']
q68_text = ''
for v in q68_verses:
    txt = v if isinstance(v, str) else v.get('text', '')
    q68_text += normalize_letters(txt)

q68_total = len(q68_text)
q68_nun = q68_text.count('ن')
q68_rate = q68_nun / q68_total if q68_total else 0

# Rest of corpus stream
rest_text = ''
for s_idx, s in enumerate(quran):
    if s_idx == 67:
        continue
    for v in s['verses']:
        txt = v if isinstance(v, str) else v.get('text', '')
        rest_text += normalize_letters(txt)

rest_total = len(rest_text)
rest_nun = rest_text.count('ن')
rest_rate = rest_nun / rest_total if rest_total else 0

# Permutation null: random contiguous segments of size q68_total from rest
rng = random.Random(SEED)
ge_count = 0
sample_rates = []
for _ in range(N_PERM):
    start = rng.randint(0, rest_total - q68_total)
    seg = rest_text[start:start + q68_total]
    seg_rate = seg.count('ن') / q68_total
    sample_rates.append(seg_rate)
    if seg_rate >= q68_rate:
        ge_count += 1

p_perm = ge_count / N_PERM

# Binomial parametric backup
def binomial_p_ge(n, k, p):
    # P(X >= k) = sum_{i=k..n} C(n,i) p^i (1-p)^(n-i)
    # use lgamma for stability
    if k <= 0: return 1.0
    if p <= 0: return 0.0
    if p >= 1: return 1.0
    log_p = math.log(p); log_q = math.log1p(-p)
    total = 0.0
    for i in range(k, n+1):
        lc = math.lgamma(n+1) - math.lgamma(i+1) - math.lgamma(n-i+1)
        total += math.exp(lc + i*log_p + (n-i)*log_q)
    return total

p_binom = binomial_p_ge(q68_total, q68_nun, rest_rate)

direction_reversed = q68_rate < rest_rate
if direction_reversed:
    verdict = 'NULL_DIRECTION_REVERSED'
    interp = (f"Q 68 ن-rate ({q68_rate:.4f}) < corpus-rest ({rest_rate:.4f}); pre-commit violation, "
              f"published as NULL with prominence per Protocol §1.3.")
elif p_perm < 0.05:
    verdict = 'VINDICATED'
    interp = (f"Q 68 ن-rate ({q68_rate:.4f}) > corpus-rest ({rest_rate:.4f}) at p_perm={p_perm:.4f} < 0.05. "
              f"Singleton-letter self-reference signal POSITIVE on permutation null.")
elif p_perm < 0.10:
    verdict = 'DIRECTIONAL'
    interp = (f"Q 68 ن-rate marginally > corpus-rest at p_perm={p_perm:.4f}.")
else:
    verdict = 'NULL'
    interp = (f"Q 68 ن-rate ({q68_rate:.4f}) NOT distinguishable from corpus-rest ({rest_rate:.4f}); p_perm={p_perm:.4f}.")

# Sample-rate distribution stats
sample_rates_sorted = sorted(sample_rates)
percentile_q68 = sum(1 for r in sample_rates if r < q68_rate) / N_PERM * 100

output = {
    'finding_id': 'Q068-F-02',
    'prereg_sha256': actual,
    'date_run': '2026-05-07',
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'q68_letter_total': q68_total,
    'q68_nun_count': q68_nun,
    'q68_nun_rate': q68_rate,
    'corpus_rest_letter_total': rest_total,
    'corpus_rest_nun_count': rest_nun,
    'corpus_rest_nun_rate': rest_rate,
    'rate_ratio_q68_over_rest': q68_rate / rest_rate if rest_rate else None,
    'permutation_p_value_one_sided': p_perm,
    'binomial_p_value_one_sided': p_binom,
    'q68_percentile_in_perm_distribution': percentile_q68,
    'perm_distribution_summary': {
        'mean': sum(sample_rates)/N_PERM,
        'min': sample_rates_sorted[0],
        'max': sample_rates_sorted[-1],
        'p25': sample_rates_sorted[N_PERM//4],
        'p50': sample_rates_sorted[N_PERM//2],
        'p75': sample_rates_sorted[3*N_PERM//4],
    },
    'alpha': 0.05,
    'verdict': verdict,
    'interpretation': interp,
}

out_path = f'{PROJECT}/surahs/Q068-al-qalam/csv/Q068-F-02.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q068-F-02: VERDICT={verdict}')
print(f'  Q 68 ن-rate: {q68_rate:.5f} ({q68_nun}/{q68_total})')
print(f'  Corpus-rest ن-rate: {rest_rate:.5f} ({rest_nun}/{rest_total})')
print(f'  Ratio: {q68_rate/rest_rate:.4f}x')
print(f'  Permutation p: {p_perm:.4f}; Binomial p: {p_binom:.4f}')
print(f'  Percentile of Q 68 in perm distribution: {percentile_q68:.2f}')
print(f'  Output: {out_path}')
