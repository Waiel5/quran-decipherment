#!/usr/bin/env python3
"""
Q067-F-01 — Architectural rank cross-comparison.
Tests whether high-recitation-tradition surahs (Q67, Q36, Q112, Q18) cluster
high or low on UAS rankings. Pre-registration LOCKED.
"""
import hashlib, json, os, sys

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-01-architectural-rank-cross-comparison-prereg.md'
EXPECTED_SHA = '591775e3a0683d27917b40208cb2f32e5bf91afc5d92a760c26a46741e79fd3a'

# Verify pre-reg integrity at runtime
with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-840.json') as f:
    d = json.load(f)

# Sort surahs by UAS descending; rank=1 is highest
sorted_uas = sorted(d['all_uas'], key=lambda x: -x['UAS'])
rank = {entry['surah']: i+1 for i, entry in enumerate(sorted_uas)}
uas = {entry['surah']: entry['UAS'] for entry in d['all_uas']}

target_surahs = [67, 36, 112, 18]
results = {}
for s in target_surahs:
    results[s] = {'rank': rank[s], 'uas': uas[s]}

ranks = [results[s]['rank'] for s in target_surahs]
median_rank = sorted(ranks)[len(ranks)//2] if len(ranks) % 2 == 1 else (
    (sorted(ranks)[len(ranks)//2 - 1] + sorted(ranks)[len(ranks)//2]) / 2.0
)

# Pre-registered direction: median > 50 = vindication of orthogonality
# 30 < median <= 50 = directional
# median <= 30 = NULL

if median_rank > 50 and all(r > 30 for r in ranks):
    verdict = 'VINDICATED'
    interpretation = 'Recitation-tradition surahs do NOT cluster high on UAS — orthogonality of theological-iʿjāz and architectural-iʿjāz axes confirmed.'
elif 30 <= median_rank <= 50:
    verdict = 'DIRECTIONAL'
    interpretation = 'Mixed support for orthogonality.'
else:
    verdict = 'NULL'
    interpretation = 'Recitation-tradition surahs DO cluster high on UAS — orthogonality prediction FAILS.'

# Reference: top 5 UAS (structural-iʿjāz cell) for contrast
top5 = sorted_uas[:5]
top5_summary = [(e['surah'], e['UAS']) for e in top5]

output = {
    'finding_id': 'Q067-F-01',
    'prereg_sha256': actual_sha,
    'pre_reg_path': PREREG_PATH,
    'date_run': '2026-04-28',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
    'target_surahs': target_surahs,
    'per_surah': results,
    'ranks': ranks,
    'median_rank_of_target_surahs': median_rank,
    'pre_reg_threshold_orthogonality_vindicated': 'median_rank > 50 AND all > 30',
    'verdict': verdict,
    'interpretation': interpretation,
    'top5_UAS_for_contrast': top5_summary,
    'recitation_tradition_predicts_UAS': median_rank <= 30,
    'cross_finding_ref': 'cross-finding-026-iʿjāz-architecture',
    'h_new_ref': 'h-new-840-unified-architectural-score',
}

out_path = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-01.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q067-F-01: VERDICT={verdict}')
print(f'  Q67 rank={results[67]["rank"]}/114, UAS={results[67]["uas"]:.4f}')
print(f'  Q36 rank={results[36]["rank"]}/114, UAS={results[36]["uas"]:.4f}')
print(f'  Q112 rank={results[112]["rank"]}/114, UAS={results[112]["uas"]:.4f}')
print(f'  Q18 rank={results[18]["rank"]}/114, UAS={results[18]["uas"]:.4f}')
print(f'  median rank={median_rank}')
print(f'  interpretation: {interpretation}')
print(f'  Output: {out_path}')
