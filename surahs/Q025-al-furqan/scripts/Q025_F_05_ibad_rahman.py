#!/usr/bin/env python3
"""
Q025-F-05 — ʿIbād al-Raḥmān (Q 25:63-77) self-similarity + Q23:1-11 twin test.
Pre-reg SHA256: 8593ef9ff8aa3ec463dcbdcba1a6d686fe39b6720b1d375a2de84a797061fe8e
Seed: 20260507; Bonferroni-3; α_bon = 0.01666.
"""

import json, hashlib, re, math, random
from collections import Counter

PRE_REG_SHA256 = "8593ef9ff8aa3ec463dcbdcba1a6d686fe39b6720b1d375a2de84a797061fe8e"
PRE_REG_PATH = "/Users/grey/Downloads/quran/surahs/Q025-al-furqan/Q025-F-05-ibad-rahman-portrait-prereg.md"
SEED = 20260507
N_PERM = 10000
ALPHA_BON = 0.05 / 3
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

def tokenize(t):
    t = re.sub(r'[^ء-ي\s]', ' ', t)
    return [tok for tok in t.split() if tok]

def get_verses(s_id, v_start, v_end):
    s = qd[s_id-1]
    return [s['verses'][v-1]['text'] for v in range(v_start, v_end+1)]

# Block definitions
ibad_block = get_verses(25, 63, 77)  # 15 verses
muminun_block = get_verses(23, 1, 11)  # 11 verses
control_block_q70 = get_verses(70, 22, 35)  # 14 verses musallin portrait

print(f"Q25:63-77 = {len(ibad_block)} verses")
print(f"Q23:1-11 = {len(muminun_block)} verses")
print(f"Q70:22-35 = {len(control_block_q70)} verses")

# ----- Cell A: Q25:63-77 self-similarity vs Q25-internal random windows -----
all_q25 = [q['text'] for q in qd[24]['verses']]
n_q25 = len(all_q25)

# TF-IDF on Q25-internal vocabulary
def vec(verse_list, idf):
    counters = []
    for v in verse_list:
        toks = tokenize(v)
        c = Counter(toks)
        counters.append({tok: c[tok] * idf.get(tok, 0.0) for tok in c})
    return counters

def build_idf(verse_list):
    df = Counter()
    for v in verse_list:
        for tok in set(tokenize(v)):
            df[tok] += 1
    n = len(verse_list)
    return {tok: math.log(n / df[tok]) for tok in df}

q25_idf = build_idf(all_q25)
ibad_vecs = vec(ibad_block, q25_idf)

def cosine(v1, v2):
    common = set(v1) & set(v2)
    if not common:
        return 0.0
    num = sum(v1[t]*v2[t] for t in common)
    n1 = math.sqrt(sum(x*x for x in v1.values()))
    n2 = math.sqrt(sum(x*x for x in v2.values()))
    if n1==0 or n2==0:
        return 0.0
    return num/(n1*n2)

def mean_pairwise_cosine(vecs):
    n = len(vecs)
    if n < 2:
        return 0.0
    sims = [cosine(vecs[i], vecs[j]) for i in range(n) for j in range(i+1,n)]
    return sum(sims)/len(sims)

ibad_self_sim = mean_pairwise_cosine(ibad_vecs)
print(f"Q25:63-77 mean pairwise cosine: {ibad_self_sim:.4f}")

# Permutation: 1000+ random size-15 windows from Q25's other verses
other_indices = [i for i in range(n_q25) if not (62 <= i <= 76)]  # 0-indexed; Q25:63-77 = 62..76
rng = random.Random(SEED + 1)
n_a_geq = 0
null_sims = []
for _ in range(N_PERM):
    sample_idx = rng.sample(other_indices, min(15, len(other_indices)))
    sample = [all_q25[i] for i in sample_idx]
    sample_vecs = vec(sample, q25_idf)
    sim = mean_pairwise_cosine(sample_vecs)
    null_sims.append(sim)
    if sim >= ibad_self_sim:
        n_a_geq += 1
p_a = n_a_geq / N_PERM
null_mean_a = sum(null_sims)/len(null_sims)
print(f"Cell A null mean: {null_mean_a:.4f}, p_one_sided_upper: {p_a:.4f}, pass α_bon? {p_a <= ALPHA_BON}")

# MW-5: same test on Q23:1-11 (positive control — should pass)
all_q23 = [q['text'] for q in qd[22]['verses']]
n_q23 = len(all_q23)
q23_idf = build_idf(all_q23)
muminun_vecs = vec(muminun_block, q23_idf)
muminun_self_sim = mean_pairwise_cosine(muminun_vecs)
print(f"\nMW-5: Q23:1-11 mean pairwise cosine: {muminun_self_sim:.4f}")
other_idx_23 = [i for i in range(n_q23) if not (0 <= i <= 10)]
rng2 = random.Random(SEED + 99)
n_geq_23 = 0
for _ in range(N_PERM):
    sample = [all_q23[i] for i in rng2.sample(other_idx_23, min(11, len(other_idx_23)))]
    sample_vecs = vec(sample, q23_idf)
    sim = mean_pairwise_cosine(sample_vecs)
    if sim >= muminun_self_sim:
        n_geq_23 += 1
p_mw5 = n_geq_23 / N_PERM
mw5_passes = p_mw5 <= 0.05
print(f"MW-5 Q23:1-11 self-similarity vs Q23 internal random: p={p_mw5:.4f}, passes (≤0.05): {mw5_passes}")

# ----- Cell B: cross-block similarity Q25:63-77 vs Q23:1-11 -----
# Use union vocabulary IDF
union_verses = ibad_block + muminun_block
union_idf = build_idf(union_verses)
ibad_vecs_u = vec(ibad_block, union_idf)
muminun_vecs_u = vec(muminun_block, union_idf)

def cross_mean(va, vb):
    sims = [cosine(a, b) for a in va for b in vb]
    return sum(sims)/len(sims) if sims else 0.0

cross_sim = cross_mean(ibad_vecs_u, muminun_vecs_u)
print(f"\nCell B: Q25:63-77 × Q23:1-11 cross-block mean cosine: {cross_sim:.4f}")

# Null: random pairs of 15-verse and 11-verse blocks from across the corpus
# Build pool of all verses with their surah IDs
all_verses_with_origin = []
for s_idx in range(N_SURAHS):
    for v in qd[s_idx]['verses']:
        all_verses_with_origin.append((s_idx+1, v['id'], v['text']))

# Helper: random 15-verse window from one random surah (length-matched), then random 11-verse window from another
# More careful: a 15-verse contiguous window from any Q-with-≥15 verses, paired with an 11-verse contiguous from another
eligible15 = [s for s in range(1, N_SURAHS+1) if len(qd[s-1]['verses']) >= 15]
eligible11 = [s for s in range(1, N_SURAHS+1) if len(qd[s-1]['verses']) >= 11]

rng3 = random.Random(SEED + 2)
n_b_geq = 0
null_b_sims = []
for _ in range(N_PERM):
    # Pick two distinct surahs
    sa = rng3.choice(eligible15)
    sb = rng3.choice([s for s in eligible11 if s != sa])
    nv_a = len(qd[sa-1]['verses'])
    nv_b = len(qd[sb-1]['verses'])
    a_start = rng3.randint(0, nv_a - 15)
    b_start = rng3.randint(0, nv_b - 11)
    block_a = [qd[sa-1]['verses'][a_start+i]['text'] for i in range(15)]
    block_b = [qd[sb-1]['verses'][b_start+i]['text'] for i in range(11)]
    union = block_a + block_b
    idf_local = build_idf(union)
    va = vec(block_a, idf_local)
    vb = vec(block_b, idf_local)
    sim = cross_mean(va, vb)
    null_b_sims.append(sim)
    if sim >= cross_sim:
        n_b_geq += 1
p_b = n_b_geq / N_PERM
null_mean_b = sum(null_b_sims)/len(null_b_sims)
print(f"Cell B null mean: {null_mean_b:.4f}, p_one_sided_upper: {p_b:.4f}, pass α_bon? {p_b <= ALPHA_BON}")

# MW-6 control: Q70:22-35 × Q23:1-11
control_block_q70_text = control_block_q70  # 14 verses
union_70_23 = control_block_q70_text + muminun_block
idf_70_23 = build_idf(union_70_23)
v70 = vec(control_block_q70_text, idf_70_23)
v23m = vec(muminun_block, idf_70_23)
cross_70_23 = cross_mean(v70, v23m)
print(f"MW-6: Q70:22-35 × Q23:1-11 cross-block mean cosine: {cross_70_23:.4f} (vs Q25-Q23 = {cross_sim:.4f})")

# ----- Cell C: structural marker count -----
def count_alladhina(verses):
    return sum(len(re.findall(r'(?:^|\s)(?:والذين|الذين)(?=\s|$)', ' ' + v + ' ')) for v in verses)

n_alladh_ibad = count_alladhina(ibad_block)
n_alladh_muminun = count_alladhina(muminun_block)
n_alladh_q70 = count_alladhina(control_block_q70_text)

print(f"\nCell C — alladhīna marker counts:")
print(f"  Q25:63-77 (ibād al-Raḥmān): {n_alladh_ibad} occurrences in 15 verses ({n_alladh_ibad/15*100:.1f}/100v)")
print(f"  Q23:1-11 (al-muʾminūn):     {n_alladh_muminun} occurrences in 11 verses ({n_alladh_muminun/11*100:.1f}/100v)")
print(f"  Q70:22-35 (musallīn ctrl):  {n_alladh_q70} occurrences in 14 verses ({n_alladh_q70/14*100:.1f}/100v)")

cell_c_descriptive = n_alladh_ibad >= 6 and n_alladh_muminun >= 6  # both blocks heavily use alladhīna
print(f"  Cell C verifies (both blocks high alladhīna density)? {cell_c_descriptive}")

# Verdict
cell_a_pass = p_a <= ALPHA_BON
cell_b_pass = p_b <= ALPHA_BON

if cell_a_pass and cell_b_pass and cell_c_descriptive:
    verdict = "PASS-DIRECTED — Q25:63-77 is self-cohesive AND structurally twinned with Q23:1-11"
elif cell_a_pass or cell_b_pass:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"
print(f"\n=== VERDICT: {verdict} ===")
print(f"  Cell A: p={p_a:.4f}, pass={cell_a_pass}")
print(f"  Cell B: p={p_b:.4f}, pass={cell_b_pass}")
print(f"  Cell C: descriptive verifies = {cell_c_descriptive}")
print(f"  MW-5 (Q23 self-sim): p={p_mw5:.4f}, passes={mw5_passes}")
print(f"  MW-6 (Q70-Q23 cross): {cross_70_23:.4f}")

out = {
    'finding_id': 'Q025-F-05',
    'pre_reg_sha256': PRE_REG_SHA256,
    'seed': SEED,
    'n_perm': N_PERM,
    'alpha_bon': ALPHA_BON,
    'cell_a_intra_block_self_similarity': {
        'block': 'Q25:63-77',
        'observed_mean_pairwise_cosine': ibad_self_sim,
        'null_mean': null_mean_a,
        'p_one_sided_upper': p_a,
        'pass_alpha_bon': cell_a_pass,
    },
    'cell_b_cross_block_twin_similarity': {
        'pair': 'Q25:63-77 × Q23:1-11',
        'observed_mean_cosine': cross_sim,
        'null_mean': null_mean_b,
        'p_one_sided_upper': p_b,
        'pass_alpha_bon': cell_b_pass,
        'mw6_control_q70_q23': cross_70_23,
    },
    'cell_c_alladhina_marker': {
        'q25_63_77_count': n_alladh_ibad,
        'q23_1_11_count': n_alladh_muminun,
        'q70_22_35_count': n_alladh_q70,
        'descriptive_verifies': cell_c_descriptive,
    },
    'mw5_q23_self_similarity': {
        'observed': muminun_self_sim,
        'p_one_sided_upper': p_mw5,
        'passes': mw5_passes,
    },
    'verdict': verdict,
}
with open('/Users/grey/Downloads/quran/surahs/Q025-al-furqan/csv/Q025-F-05.json', 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print('[OK] Saved Q025-F-05.json')
