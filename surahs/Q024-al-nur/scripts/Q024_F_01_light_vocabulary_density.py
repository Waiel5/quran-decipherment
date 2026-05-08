#!/usr/bin/env python3
"""Q024-F-01: Light-vocabulary density audit (LOCKED pre-reg).

Computes the corpus-wide hypergeometric significance of Q 24's
light-cluster root-token concentration. Cross-references against Q 33
al-Aḥzāb as the discriminating-control test.

Data sources (no-tashkeel, QAC v0.4 root annotations):
- /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
"""
import re, json, math, hashlib, os, sys
from collections import Counter

# Locked light-cluster (matches pre-reg)
LIGHT_CLUSTER = {'nwr', 'SbH', 'wqd', 'srj', 'qbs', 'shhb', 'mskw', 'zjj',
                 'kwkb', '$jr', 'zyt', 'brk', '$kw', 'drr', 'DwA', 'mvl'}

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-01-light-vocabulary-density-prereg.md"
QAC = f"{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-01.json"

# 1. SHA-check the pre-reg
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256: {sha}")

# 2. Parse QAC roots per surah
roots_per_surah = {}
with open(QAC, encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('): continue
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)\s+\S+\s+\S+\s+(.*)', line)
        if not m: continue
        s = int(m.group(1))
        feat = m.group(5)
        rm = re.search(r'ROOT:([^|\s]+)', feat)
        if rm:
            roots_per_surah.setdefault(s, Counter())[rm.group(1)] += 1

# 3. Compute corpus and Q24 stats
corpus_total = sum(sum(c.values()) for c in roots_per_surah.values())
corpus_light = sum(sum(c.get(r, 0) for r in LIGHT_CLUSTER) for c in roots_per_surah.values())

q24 = roots_per_surah[24]
q24_total = sum(q24.values())
q24_light = sum(q24.get(r, 0) for r in LIGHT_CLUSTER)

# 4. Hypergeometric p-value via log-comb
def lcomb(a, b):
    if b < 0 or b > a: return float('-inf')
    return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)

N, K, n, k = corpus_total, corpus_light, q24_total, q24_light
expected = n * K / N

logp_terms = []
for i in range(k, min(K, n) + 1):
    lp = lcomb(K, i) + lcomb(N - K, n - i) - lcomb(N, n)
    if lp > -700:
        logp_terms.append(lp)

m_max = max(logp_terms)
log_p = m_max + math.log(sum(math.exp(x - m_max) for x in logp_terms))
p_value = math.exp(log_p)
alpha_bonferroni = 0.05 / 114

# 5. Discriminating control on Q33
q33 = roots_per_surah[33]
q33_total = sum(q33.values())
q33_light = sum(q33.get(r, 0) for r in LIGHT_CLUSTER)
q33_expected = q33_total * K / N

logp33 = []
for i in range(q33_light, min(K, q33_total) + 1):
    lp = lcomb(K, i) + lcomb(N - K, q33_total - i) - lcomb(N, q33_total)
    if lp > -700:
        logp33.append(lp)
m33 = max(logp33) if logp33 else float('-inf')
log_p33 = m33 + math.log(sum(math.exp(x - m33) for x in logp33)) if logp33 else float('-inf')
p_value_q33 = math.exp(log_p33) if log_p33 != float('-inf') else 1.0

# 6. Per-surah ranking
ranked_density = []
for s, c in roots_per_surah.items():
    total = sum(c.values())
    lc = sum(c.get(r, 0) for r in LIGHT_CLUSTER)
    ranked_density.append({
        'surah': s, 'light_count': lc, 'total': total,
        'density_per_1000': lc / total * 1000 if total > 0 else 0.0,
    })
ranked_by_count = sorted(ranked_density, key=lambda x: -x['light_count'])
rank_q24_count = next(i + 1 for i, r in enumerate(ranked_by_count) if r['surah'] == 24)
ranked_by_density = sorted(ranked_density, key=lambda x: -x['density_per_1000'])
rank_q24_density = next(i + 1 for i, r in enumerate(ranked_by_density) if r['surah'] == 24)

# 7. Verdict
if p_value < alpha_bonferroni:
    verdict = "VINDICATED"
elif p_value < 0.05:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"

# Q33 should not pass — control test
q33_passes = p_value_q33 < alpha_bonferroni
control_pass = not q33_passes

result = {
    'finding_id': 'Q024-F-01',
    'pre_reg_sha256': sha,
    'verdict': verdict,
    'control_test_pass': control_pass,
    'q24_total_root_tokens': q24_total,
    'q24_light_count': q24_light,
    'corpus_total_root_tokens': corpus_total,
    'corpus_light_count': corpus_light,
    'expected_under_uniform': expected,
    'observed': q24_light,
    'p_value_raw': p_value,
    'log_p': log_p,
    'alpha_bonferroni': alpha_bonferroni,
    'rank_by_count': rank_q24_count,
    'rank_by_density': rank_q24_density,
    'top_15_by_count': ranked_by_count[:15],
    'top_15_by_density': ranked_by_density[:15],
    'control_q33': {
        'q33_total': q33_total, 'q33_light': q33_light,
        'q33_expected': q33_expected, 'p_value': p_value_q33,
        'passes_bonferroni': q33_passes,
    },
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str)

print(json.dumps({k: v for k, v in result.items() if 'top_15' not in k}, indent=2, default=str))
print(f"\nFull output written to {OUT}")
