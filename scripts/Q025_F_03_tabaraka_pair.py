#!/usr/bin/env python3
"""
Q025-F-03 — Q25/Q67 *tabāraka alladhī* opener-pair structural similarity.
Pre-reg SHA256: 0c0f1095a911f5b206d3009f949389ddeba80e722cc3e9fe297e75f7c80a5b40
Seed: 20260507; n_perm: 10000; Bonferroni-4; α_bon = 0.0125.
Direction: HIGHER similarity (Q25, Q67) vs random pairs across 4 instruments.
"""

import json, hashlib, re, math
from collections import Counter

PRE_REG_SHA256 = "0c0f1095a911f5b206d3009f949389ddeba80e722cc3e9fe297e75f7c80a5b40"
PRE_REG_PATH = "/Users/grey/Downloads/quran/surahs/Q025-al-furqan/Q025-F-03-tabaraka-pair-prereg.md"
SEED = 20260507
ALPHA_BON = 0.05 / 4
N_SURAHS = 114

def verify_prereg():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PRE_REG_SHA256:
        raise SystemExit(f"PRE-REG SHA MISMATCH: expected {PRE_REG_SHA256}, got {sha}")
    print(f"[OK] Pre-reg SHA verified.")
verify_prereg()

# Load
qd = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

# I1 — FR similarity
hnew111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
D = [[0.0]*N_SURAHS for _ in range(N_SURAHS)]
for entry in hnew111['D_matrix_upper_triangular']:
    i, j, d = entry
    D[i-1][j-1] = d
    D[j-1][i-1] = d

# I2 — top-rhyme letter
hnew700 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json'))
top_rhyme = {}
diag = hnew700['rhyme']['rhyme_letter_diagnostics']
if isinstance(diag, list):
    for info in diag:
        top_rhyme[info['surah']] = info['top_letter']
else:
    for sid_str, info in diag.items():
        top_rhyme[int(sid_str)] = info['top_letter']

# I3 — opening-word identity (post-bismala)
def first_word(s_dict):
    text = s_dict['verses'][0]['text']
    text = re.sub(r'^بسم\s+الله\s+الرحمن\s+الرحيم\s*', '', text)
    tokens = re.findall(r'[ء-ي]+', text)
    return tokens[0] if tokens else ''
opening = {qd[i]['id']: first_word(qd[i]) for i in range(N_SURAHS)}

# I4 — sig_A (h-new-750)
hnew750 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json'))
sig_A = {}
for r in hnew750['per_surah']:
    sig_A[r['surah']] = r['sig_A']
sig_A_values = list(sig_A.values())
sig_A_range = max(sig_A_values) - min(sig_A_values)

# Compute all pair similarities for each instrument
def i1_sim(a, b):
    return 1.0 / (1.0 + D[a-1][b-1])
def i2_sim(a, b):
    return 1 if top_rhyme[a] == top_rhyme[b] else 0
def i3_sim(a, b):
    return 1 if opening[a] == opening[b] else 0
def i4_sim(a, b):
    return 1 - abs(sig_A[a] - sig_A[b]) / sig_A_range

target_pair = (25, 67)
control_pair = (1, 6)

def all_pairs_dist(sim_func):
    pairs = []
    for a in range(1, N_SURAHS+1):
        for b in range(a+1, N_SURAHS+1):
            pairs.append(((a,b), sim_func(a,b)))
    return pairs

results = {}
for inst_name, sim_func in [
    ('I1_FR_similarity', i1_sim),
    ('I2_top_rhyme_identity', i2_sim),
    ('I3_opening_word_identity', i3_sim),
    ('I4_sig_A_similarity', i4_sim),
]:
    all_pairs = all_pairs_dist(sim_func)
    target_score = sim_func(*target_pair)
    control_score = sim_func(*control_pair)
    # Rank target among all 6441 pairs (descending = higher rank means MORE similar)
    sorted_pairs = sorted(all_pairs, key=lambda x: -x[1])
    target_rank = next(i+1 for i, (p, s) in enumerate(sorted_pairs) if p == target_pair)
    control_rank = next(i+1 for i, (p, s) in enumerate(sorted_pairs) if p == control_pair)
    n_pairs = len(all_pairs)
    target_pct = target_rank / n_pairs * 100
    control_pct = control_rank / n_pairs * 100
    # One-sided p (upper tail): probability random pair has score ≥ target_score
    n_geq = sum(1 for _, s in all_pairs if s >= target_score)
    p_target = n_geq / n_pairs
    n_geq_c = sum(1 for _, s in all_pairs if s >= control_score)
    p_control = n_geq_c / n_pairs
    in_top_decile = target_pct <= 10
    pass_alpha = p_target <= ALPHA_BON
    results[inst_name] = {
        'target_pair': list(target_pair),
        'target_score': target_score,
        'target_rank': target_rank,
        'target_percentile': target_pct,
        'p_one_sided_upper': p_target,
        'in_top_decile': in_top_decile,
        'pass_alpha_bon': pass_alpha,
        'control_pair': list(control_pair),
        'control_score': control_score,
        'control_rank': control_rank,
        'control_percentile': control_pct,
        'control_in_top_decile': control_pct <= 10,
    }
    print(f"{inst_name}: Q25-Q67 score={target_score:.4f}, rank={target_rank}/{n_pairs} ({target_pct:.2f}%), p={p_target:.4f}, top-decile={in_top_decile}")
    print(f"             MW6 control Q1-Q6 score={control_score:.4f}, rank={control_rank}/{n_pairs} ({control_pct:.2f}%)")

n_top_decile = sum(1 for r in results.values() if r['in_top_decile'])
n_pass_alpha = sum(1 for r in results.values() if r['pass_alpha_bon'])

# Inferential cells = I1, I2, I4 (I3 is constructive)
inferential_keys = ['I1_FR_similarity', 'I2_top_rhyme_identity', 'I4_sig_A_similarity']
n_inferential_pass_alpha = sum(1 for k in inferential_keys if results[k]['pass_alpha_bon'])
n_inferential_top_decile = sum(1 for k in inferential_keys if results[k]['in_top_decile'])

# Verdict
if n_top_decile >= 3 and n_inferential_top_decile >= 2:
    verdict = "PASS-DIRECTED — Q25/Q67 form a structural pair beyond opener"
elif n_top_decile == 2:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL — *tabāraka* opener is surface-only"

# MW-6 control check
mw6_n_top_decile = sum(1 for r in results.values() if r['control_in_top_decile'])
mw6_passes = mw6_n_top_decile >= 1

print(f"\n=== AGGREGATE ===")
print(f"Top-decile sweeps:        {n_top_decile}/4 (inferential: {n_inferential_top_decile}/3)")
print(f"α_bon sweeps:             {n_pass_alpha}/4 (inferential: {n_inferential_pass_alpha}/3)")
print(f"MW-6 control top-decile:  {mw6_n_top_decile}/4 (passes: {mw6_passes})")
print(f"VERDICT: {verdict}")

out = {
    'finding_id': 'Q025-F-03',
    'pre_reg_sha256': PRE_REG_SHA256,
    'seed': SEED,
    'alpha_bon': ALPHA_BON,
    'instruments': results,
    'aggregate': {
        'n_top_decile_4': n_top_decile,
        'n_top_decile_inferential_3': n_inferential_top_decile,
        'n_pass_alpha_bon_4': n_pass_alpha,
        'n_pass_alpha_bon_inferential_3': n_inferential_pass_alpha,
        'mw6_top_decile_4': mw6_n_top_decile,
        'mw6_passes': mw6_passes,
        'verdict': verdict,
    },
}
with open('/Users/grey/Downloads/quran/surahs/Q025-al-furqan/csv/Q025-F-03.json', 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print('[OK] Saved Q025-F-03.json')
