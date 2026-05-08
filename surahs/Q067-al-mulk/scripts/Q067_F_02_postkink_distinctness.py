#!/usr/bin/env python3
"""
Q067-F-02 — Post-Hijra-kink distinctness test.
Compares Q67's empirical mean_content_distance and rhyme_entropy vs the
post-kink law-prediction (H-NEW-660 + H-NEW-700).
"""
import hashlib, json, os, sys

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-02-postkink-distinctness-prereg.md'
EXPECTED_SHA = 'f9f2d651034d8773d130d7d6ae2fa9f01265ed3e8227fd20012f0d16ed9113a7'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

with open(f'{PROJECT}/findings/phase-b-hypotheses/csv/h-new-750.json') as f:
    d750 = json.load(f)

q67_metrics = None
for e in d750['per_surah']:
    if e['surah'] == 67:
        q67_metrics = e
        break

s = 67
# H-NEW-660 prediction: d̄_content(s) ≈ 0.96 - 0.012 * max(0, s-50)
predicted_content = 0.96 - 0.012 * max(0, s - 50)
# H-NEW-700 prediction: d̄_rhyme(s) ≈ 0.36 + 0.0041 * max(0, s-50)
predicted_rhyme = 0.36 + 0.0041 * max(0, s - 50)

empirical_content = q67_metrics['mean_content_distance']
empirical_rhyme_entropy_nats = q67_metrics['rhyme_entropy_nats']
# Note: rhyme_entropy nats != predicted d̄_rhyme (these are different metrics)
# We use mean_content_distance vs predicted as the primary comparison

residual_content = empirical_content - predicted_content

# Rough SE estimate: for the H-NEW-660 fit, R²=0.986 over 114 surahs
# residual standard deviation around the law is approximately sqrt(1-R²) * sd(d_content) ~ 0.05-0.08
# Use 0.05 as conservative SE for the law-prediction
SE_content = 0.05
within_2_se = abs(residual_content) <= 2 * SE_content

if within_2_se:
    verdict = 'VINDICATED'
    interpretation = (
        f'Q67 mean_content_distance ({empirical_content:.4f}) is within 2 SE of the post-kink law-prediction ({predicted_content:.4f}). '
        f'Residual = {residual_content:+.4f}; SE ≈ {SE_content}. '
        f'Q67 is a TYPICAL post-kink surah, not architecturally distinct. '
        f'This is a NULL on architectural-distinctness, vindicating the pre-registered orthogonality prediction.'
    )
elif residual_content > 2 * SE_content:
    verdict = 'DIRECTIONAL_ENHANCED'
    interpretation = f'Q67 mean_content_distance is {residual_content:+.4f} above prediction (>2 SE) — architecturally enhanced.'
else:
    verdict = 'DIRECTIONAL_DEPLETED'
    interpretation = f'Q67 mean_content_distance is {residual_content:+.4f} below prediction (>2 SE) — architecturally depleted.'

output = {
    'finding_id': 'Q067-F-02',
    'prereg_sha256': actual_sha,
    'date_run': '2026-04-28',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
    'surah_position_s': s,
    'kink_position': 50,
    'h_new_660_law_prediction_content_distance': predicted_content,
    'h_new_700_law_prediction_rhyme_dispersion': predicted_rhyme,
    'q67_empirical_mean_content_distance': empirical_content,
    'q67_empirical_rhyme_entropy_nats': empirical_rhyme_entropy_nats,
    'q67_top_final_letter': q67_metrics['top_final_letter'],
    'q67_top_final_letter_frac': q67_metrics['top_final_letter_frac'],
    'residual_content': residual_content,
    'SE_used': SE_content,
    'within_2_SE': within_2_se,
    'verdict': verdict,
    'interpretation': interpretation,
    'pre_registered_direction': 'NULL — Q67 expected to track law (typical post-kink)',
}

out_path = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-02.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q067-F-02: VERDICT={verdict}')
print(f'  predicted d_content = {predicted_content:.4f}')
print(f'  empirical d_content = {empirical_content:.4f}')
print(f'  residual = {residual_content:+.4f} (SE={SE_content})')
print(f'  {interpretation}')
print(f'  Output: {out_path}')
