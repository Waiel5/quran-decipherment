#!/usr/bin/env python3
"""
Q025-F-04 — *qālū / qāla* polemic-quotative density of Q 25 vs corpus.
Pre-reg SHA256: 61ce8ac21bc80d8e7c2bf979687c3a82c6fa67e0339525e397ae2c8f7165d3cc
Seed: 20260507; Bonferroni-2; α_bon = 0.025.
Direction: TOP quartile rank for Q25 on both cells.
"""

import json, hashlib, re, random
from collections import Counter

PRE_REG_SHA256 = "61ce8ac21bc80d8e7c2bf979687c3a82c6fa67e0339525e397ae2c8f7165d3cc"
PRE_REG_PATH = "/Users/grey/Downloads/quran/surahs/Q025-al-furqan/Q025-F-04-qalu-polemic-density-prereg.md"
SEED = 20260507
N_PERM = 10000
ALPHA_BON = 0.05 / 2
TOP_QUARTILE_RANK = 28
N_SURAHS = 114

def verify_prereg():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PRE_REG_SHA256:
        raise SystemExit(f"PRE-REG SHA MISMATCH: expected {PRE_REG_SHA256}, got {sha}")
    print(f"[OK] Pre-reg SHA verified.")
verify_prereg()

random.seed(SEED)

qd = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

# Cell A: targeted polemic regex (disbeliever-attribution context)
# Pattern: قالوا alone (most common attribution to plural-others), or قال followed by الذين كفروا / الظالمون / المشركون
CELL_A_PAT = re.compile(r'(و)?قالوا|قال\s+(الذين\s+كفروا|الظالمون|المشركون|للذين)')
# Cell A2: broader قال / يقول / قل surface (POS-blind)
CELL_A2_PAT = re.compile(r'(?:^|\s)(?:قال|قالوا|قالت|قلن|قلت|قلتم|قلنا|يقول|يقولون|يقولوا|تقول|نقول|قل|قولوا|يقال|قالا|قائل|قائلون)(?=\s|$)')

per_surah_a = {}
per_surah_a2 = {}
for s in qd:
    sid = s['id']
    nv = len(s['verses'])
    n_a = sum(1 for v in s['verses'] if CELL_A_PAT.search(v['text']))
    # For A2: count tokens
    text = ' '.join(v['text'] for v in s['verses'])
    n_a2 = len(CELL_A2_PAT.findall(' ' + text + ' '))
    per_surah_a[sid] = (n_a / nv * 100, n_a, nv)
    per_surah_a2[sid] = (n_a2 / nv * 100, n_a2, nv)

# Q25 ranks
def rank_descending(d, key):
    sorted_items = sorted(d.items(), key=lambda x: -x[1][0])
    return next(i+1 for i, (sid, _) in enumerate(sorted_items) if sid == key)

q25_a = per_surah_a[25]
q25_a2 = per_surah_a2[25]
q25_a_rank = rank_descending(per_surah_a, 25)
q25_a2_rank = rank_descending(per_surah_a2, 25)

print(f"Cell A — Q25 polemic-attribution count: {q25_a[1]}/{q25_a[2]} verses, density={q25_a[0]:.2f}/100v, rank={q25_a_rank}/{N_SURAHS}")
print(f"Cell A2 — Q25 broader قال/يقول count: {q25_a2[1]}/{q25_a2[2]} verses, density={q25_a2[0]:.2f}/100v, rank={q25_a2_rank}/{N_SURAHS}")

# Permutation null on rank
def perm_null(per_surah_d, target_sid, n_perm, seed_offset):
    rng = random.Random(SEED + seed_offset)
    densities = [v[0] for v in per_surah_d.values()]
    target_density = per_surah_d[target_sid][0]
    n_geq = 0
    for _ in range(n_perm):
        # Random sample: random density assigned to Q25
        rng.shuffle(densities)
        if densities[0] >= target_density:  # any random surah sampled
            pass
        # Actually a proper permutation null: shuffle and take a random one as Q25
        candidate = rng.choice(densities)
        if candidate >= target_density:
            n_geq += 1
    return n_geq / n_perm

p_a = perm_null(per_surah_a, 25, N_PERM, 1)
p_a2 = perm_null(per_surah_a2, 25, N_PERM, 2)
print(f"Cell A  permutation p (one-sided upper): {p_a:.4f}")
print(f"Cell A2 permutation p (one-sided upper): {p_a2:.4f}")

# MW-5: Q12 (Yusuf) should be in top decile of A2 density
sorted_a2 = sorted(per_surah_a2.items(), key=lambda x: -x[1][0])
q12_rank = next(i+1 for i, (sid, _) in enumerate(sorted_a2) if sid == 12)
mw5_pass = q12_rank <= int(N_SURAHS * 0.10)
print(f"MW-5 control: Q12 Yūsuf A2 rank: {q12_rank}/{N_SURAHS} (top-decile threshold = {int(N_SURAHS*0.10)}); passes: {mw5_pass}")

# Top-10 in each cell
top10_a = sorted(per_surah_a.items(), key=lambda x: -x[1][0])[:10]
top10_a2 = sorted(per_surah_a2.items(), key=lambda x: -x[1][0])[:10]
print(f"\nTop-10 Cell A (polemic-attribution density per 100v):")
for sid, (d, n, nv) in top10_a:
    print(f"  Q{sid}: {d:.2f}/100v ({n}/{nv})")
print(f"\nTop-10 Cell A2 (broad qwl density per 100v):")
for sid, (d, n, nv) in top10_a2:
    print(f"  Q{sid}: {d:.2f}/100v ({n}/{nv})")

cell_a_pass = (q25_a_rank <= TOP_QUARTILE_RANK) and (p_a <= ALPHA_BON)
cell_a2_pass = (q25_a2_rank <= TOP_QUARTILE_RANK) and (p_a2 <= ALPHA_BON)

if cell_a_pass and cell_a2_pass:
    verdict = "PASS-DIRECTED — Q25's polemic-quotative density is structurally elevated"
elif cell_a_pass or cell_a2_pass:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"
print(f"\n=== VERDICT: {verdict} ===")
print(f"  Cell A:  rank {q25_a_rank} ≤ {TOP_QUARTILE_RANK}? {q25_a_rank <= TOP_QUARTILE_RANK}; p ≤ α_bon? {p_a <= ALPHA_BON}; PASS={cell_a_pass}")
print(f"  Cell A2: rank {q25_a2_rank} ≤ {TOP_QUARTILE_RANK}? {q25_a2_rank <= TOP_QUARTILE_RANK}; p ≤ α_bon? {p_a2 <= ALPHA_BON}; PASS={cell_a2_pass}")

out = {
    'finding_id': 'Q025-F-04',
    'pre_reg_sha256': PRE_REG_SHA256,
    'seed': SEED,
    'alpha_bon': ALPHA_BON,
    'top_quartile_threshold': TOP_QUARTILE_RANK,
    'cell_a_polemic_attribution': {
        'q25_density_per_100v': q25_a[0],
        'q25_count': q25_a[1],
        'q25_n_verses': q25_a[2],
        'q25_rank_descending': q25_a_rank,
        'in_top_quartile': q25_a_rank <= TOP_QUARTILE_RANK,
        'p_one_sided_upper': p_a,
        'pass_alpha_bon': p_a <= ALPHA_BON,
        'top10': [(sid, d, n, nv) for sid, (d, n, nv) in top10_a],
    },
    'cell_a2_broad_qwl': {
        'q25_density_per_100v': q25_a2[0],
        'q25_count': q25_a2[1],
        'q25_n_verses': q25_a2[2],
        'q25_rank_descending': q25_a2_rank,
        'in_top_quartile': q25_a2_rank <= TOP_QUARTILE_RANK,
        'p_one_sided_upper': p_a2,
        'pass_alpha_bon': p_a2 <= ALPHA_BON,
        'top10': [(sid, d, n, nv) for sid, (d, n, nv) in top10_a2],
        'mw5_q12_rank': q12_rank,
        'mw5_passes': mw5_pass,
    },
    'verdict': verdict,
}
with open('/Users/grey/Downloads/quran/surahs/Q025-al-furqan/csv/Q025-F-04.json', 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print('[OK] Saved Q025-F-04.json')
