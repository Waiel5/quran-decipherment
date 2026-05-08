#!/usr/bin/env python3
"""Q018-F-03: Q 18 alif-monorhyme final-letter saturation + v.110 alif-closure (LOCKED pre-reg).

Tests:
  Cell A: Q 18's alif-final-fraction is significantly above corpus mean.
  Cell B: Q 18:110 (final verse) ends in alif.
"""
import json, re, hashlib, math, os

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q018-al-kahf/preregs/Q018-F-03-alif-monorhyme-prereg.md"
QURAN = f"{PROJECT}/quran-text/quran-min-tashkeel.json"
OUT = f"{PROJECT}/surahs/Q018-al-kahf/csv/Q018-F-03.json"

ALPHA_BON = 0.05 / 2

# SHA
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256: {sha}")

# Load
q = json.load(open(QURAN))

MUSHAF_RE = re.compile(r'[۞۩ۚۖۗۛۧۜ]')
TASHKEEL_RE = re.compile(r'[ً-ٰٟـ]')  # all tashkeel + tatweel

def last_letter_of_verse(text):
    text = MUSHAF_RE.sub('', text)
    words = text.split()
    if not words: return None
    last = TASHKEEL_RE.sub('', words[-1])
    if not last: return None
    return last[-1]

# Per-surah alif fraction
results = []
for s in q:
    sid = s['id']
    alif_count = 0
    total = 0
    for v in s['verses']:
        L = last_letter_of_verse(v['text'])
        if L is not None:
            total += 1
            if L == 'ا':
                alif_count += 1
    frac = alif_count / total if total else 0
    results.append({'surah': sid, 'alif_count': alif_count, 'total': total, 'alif_frac': frac})

# Corpus mean
total_alif = sum(r['alif_count'] for r in results)
total_verses = sum(r['total'] for r in results)
corpus_alif_frac = total_alif / total_verses
print(f'Corpus alif-fraction (mean over verses): {corpus_alif_frac:.4f} ({total_alif}/{total_verses})')

q18 = [r for r in results if r['surah'] == 18][0]
print(f'Q 18 alif-fraction: {q18["alif_frac"]:.4f} ({q18["alif_count"]}/{q18["total"]})')

# Cell A: binomial p-value (one-tailed, Q18 > corpus mean)
n = q18['total']  # 110
k = q18['alif_count']  # 109
p0 = corpus_alif_frac
# P(X >= k | n, p0)
def log_comb(n, k):
    if k < 0 or k > n: return float('-inf')
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)

log_terms = []
for i in range(k, n + 1):
    lp = log_comb(n, i) + i * math.log(p0) + (n - i) * math.log(1 - p0)
    if lp > -700:
        log_terms.append(lp)
m = max(log_terms)
log_p_A = m + math.log(sum(math.exp(x - m) for x in log_terms))
p_A = math.exp(log_p_A)
print(f'Cell A binomial p (X >= {k}, n={n}, p0={p0:.4f}): {p_A:.6e}')

# Cell A verdict
if q18['alif_frac'] < corpus_alif_frac:
    verdict_A = 'NULL_PRECOMMIT_VIOLATION'
elif p_A < ALPHA_BON and q18['alif_frac'] >= 0.95:
    verdict_A = 'CONFIRMED'
elif p_A < 0.05 or q18['alif_frac'] >= 0.90:
    verdict_A = 'DIRECTIONAL'
else:
    verdict_A = 'NULL'

# Cell B: v.110 last letter
q18_data = next(s for s in q if s['id'] == 18)
v110 = next(v for v in q18_data['verses'] if v['id'] == 110)
v110_last_letter = last_letter_of_verse(v110['text'])
print(f'v.110 last letter: "{v110_last_letter}" — alif? {v110_last_letter == "ا"}')

if v110_last_letter == 'ا':
    verdict_B = 'CONFIRMED'
else:
    verdict_B = 'NULL'

# Combined
combined = 'CONFIRMED' if verdict_A == 'CONFIRMED' and verdict_B == 'CONFIRMED' else f'{verdict_A}/{verdict_B}'

# Find non-alif verses in Q 18
non_alif_q18 = []
for v in q18_data['verses']:
    L = last_letter_of_verse(v['text'])
    if L != 'ا':
        non_alif_q18.append({'verse': v['id'], 'last_letter': L, 'text_tail': v['text'][-40:]})

# Alif-cluster siblings (for honest-limits comparison)
cluster = [18, 48, 65, 72, 76, 87, 91, 92]
cluster_data = []
for r in results:
    if r['surah'] in cluster:
        cluster_data.append(r)

result_obj = {
    'finding_id': 'Q018-F-03',
    'pre_reg_sha256': sha,
    'verdict_combined': combined,
    'cell_A': {
        'q18_alif_frac': q18['alif_frac'],
        'q18_alif_count': q18['alif_count'],
        'q18_total_verses': q18['total'],
        'corpus_alif_frac': corpus_alif_frac,
        'p_binomial': p_A,
        'alpha_bonferroni': ALPHA_BON,
        'verdict': verdict_A,
    },
    'cell_B': {
        'v110_last_letter': v110_last_letter,
        'v110_text_tail': v110['text'][-50:],
        'verdict': verdict_B,
    },
    'non_alif_verses': non_alif_q18,
    'alif_cluster_data': cluster_data,
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result_obj, f, indent=2, default=str, ensure_ascii=False)
print(f'\nWritten to {OUT}')
