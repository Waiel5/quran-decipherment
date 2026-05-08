#!/usr/bin/env python3
"""
Q025-F-01 — True-isolate persistence of Q 25 across 8 alternative similarity instruments.
Pre-reg SHA256: 1653d24f358cc1ce37bf35443944ebdd2dfa61b199d680882a8f38a5380b0330
Seed: 20260507; n_perm: 10000; Bonferroni-8; α_bon = 0.00625.
Direction: one-sided LOWER on mean-top-3-similarity (Q25 isolated).
"""

import json, re, hashlib, math, random
from collections import Counter, defaultdict

PRE_REG_SHA256 = "1653d24f358cc1ce37bf35443944ebdd2dfa61b199d680882a8f38a5380b0330"
PRE_REG_PATH = "/Users/grey/Downloads/quran/surahs/Q025-al-furqan/Q025-F-01-true-isolate-persistence-prereg.md"
SEED = 20260507
N_PERM = 10000
ALPHA_BON = 0.05 / 8  # 0.00625
BOTTOM_QUARTILE_RANK = 28  # ≤ 28/114
N_SURAHS = 114

def verify_prereg():
    with open(PRE_REG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PRE_REG_SHA256:
        raise SystemExit(f"PRE-REG SHA MISMATCH: expected {PRE_REG_SHA256}, got {sha}")
    print(f"[OK] Pre-reg SHA verified: {sha[:16]}...")

verify_prereg()
random.seed(SEED)

# ---------- Load corpus ----------
qd = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
surahs = {}  # 1-indexed
for s in qd:
    sid = s['id']
    surahs[sid] = {
        'name': s['name'],
        'verses': [v['text'] for v in s['verses']],
        'concat': ' '.join(v['text'] for v in s['verses']),
    }
assert len(surahs) == N_SURAHS

# Load QAC roots
qac = json.load(open('/tmp/q25_research/qac_roots_per_surah.json'))
roots_per_surah = {int(k): Counter(v) for k, v in qac['roots_per_surah'].items()}
all_roots = qac['all_roots']

# Load FR-distance from h-new-111
hnew111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
D_fr = [[0.0]*N_SURAHS for _ in range(N_SURAHS)]
for entry in hnew111['D_matrix_upper_triangular']:
    i, j, d = entry
    D_fr[i-1][j-1] = d
    D_fr[j-1][i-1] = d

# Load h-new-700 rhyme top-letter
hnew700 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json'))
rhyme_diag = hnew700['rhyme']['rhyme_letter_diagnostics']
# Build per-surah final-letter histogram
def get_verse_final_letters(s_text_verses):
    finals = []
    for v in s_text_verses:
        # Strip tail punctuation/tashkeel; take last alphabetic
        stripped = re.sub(r'[^ء-ي]', '', v)
        if stripped:
            finals.append(stripped[-1])
    return finals

final_letter_counts = {}
for sid in range(1, N_SURAHS+1):
    finals = get_verse_final_letters(surahs[sid]['verses'])
    final_letter_counts[sid] = Counter(finals)

# Load 99 names of Allah
with open('/Users/grey/Downloads/quran/data/asma-al-husna.txt') as f:
    asma_lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
# Take Arabic surface forms only (heuristic: line tokens with Arabic chars)
asma_arabic = []
for line in asma_lines:
    parts = re.split(r'\s+', line.strip())
    for p in parts:
        if re.search(r'[ء-ي]', p) and len(p) >= 2:
            asma_arabic.append(p.strip('.,;:'))
            break
asma_arabic = list(set(asma_arabic))
print(f"[OK] Loaded {len(asma_arabic)} divine names (Arabic).")

# Per-surah divine-name attestation (orthographic substring match in concat text)
def divine_names_attested(s_concat):
    return set(name for name in asma_arabic if name in s_concat)

dn_attested = {sid: divine_names_attested(surahs[sid]['concat']) for sid in range(1, N_SURAHS+1)}

# ---------- Build similarity matrices ----------
# Tokens per surah (orthographic, no-tashkeel)
def tokenize(text):
    # Strip punctuation
    text = re.sub(r'[^ء-ي\s]', ' ', text)
    return [t for t in text.split() if t]

tokens_per_surah = {sid: tokenize(surahs[sid]['concat']) for sid in range(1, N_SURAHS+1)}

# IDF over tokens
df = Counter()
for sid in range(1, N_SURAHS+1):
    for tok in set(tokens_per_surah[sid]):
        df[tok] += 1
idf = {tok: math.log(N_SURAHS / df[tok]) for tok in df}

# TF-IDF vectors
def tfidf_vec(tokens):
    tf = Counter(tokens)
    return {tok: tf[tok] * idf.get(tok, 0.0) for tok in tf}

tfidf_per_surah = {sid: tfidf_vec(tokens_per_surah[sid]) for sid in range(1, N_SURAHS+1)}

def cosine(v1, v2):
    common = set(v1) & set(v2)
    if not common:
        return 0.0
    num = sum(v1[t] * v2[t] for t in common)
    n1 = math.sqrt(sum(x*x for x in v1.values()))
    n2 = math.sqrt(sum(x*x for x in v2.values()))
    if n1 == 0 or n2 == 0:
        return 0.0
    return num / (n1 * n2)

# Char-trigram and char-5gram sets
def char_ngrams(text, n):
    text = re.sub(r'\s+', ' ', text)
    return set(text[i:i+n] for i in range(len(text)-n+1))

char3_per_surah = {sid: char_ngrams(surahs[sid]['concat'], 3) for sid in range(1, N_SURAHS+1)}
char5_per_surah = {sid: char_ngrams(surahs[sid]['concat'], 5) for sid in range(1, N_SURAHS+1)}

def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / max(1, len(a | b))

def dice(a, b):
    if not a and not b:
        return 0.0
    return 2 * len(a & b) / max(1, len(a) + len(b))

# Final-letter probability vectors
def final_letter_vec(sid):
    counts = final_letter_counts[sid]
    total = sum(counts.values()) or 1
    return {l: counts[l] / total for l in counts}

flv_per_surah = {sid: final_letter_vec(sid) for sid in range(1, N_SURAHS+1)}

# Root frequency for Zipf-overlap
root_corpus_freq = Counter()
for sid in range(1, N_SURAHS+1):
    for root, c in roots_per_surah.get(sid, {}).items():
        root_corpus_freq[root] += c
root_zipf_weight = {r: 1.0 / math.log(1 + root_corpus_freq[r]) for r in root_corpus_freq}

def zipf_weighted_similarity(s1, s2):
    r1 = set(roots_per_surah.get(s1, {}).keys())
    r2 = set(roots_per_surah.get(s2, {}).keys())
    if not r1 or not r2:
        return 0.0
    inter = r1 & r2
    union = r1 | r2
    num = sum(root_zipf_weight.get(r, 0) for r in inter)
    den = sum(root_zipf_weight.get(r, 0) for r in union)
    if den == 0:
        return 0.0
    return num / den

# ---------- 8 instruments ----------
print("[INFO] Computing 8 similarity matrices (114x114) ...")

def root_jaccard(s1, s2):
    r1 = set(roots_per_surah.get(s1, {}).keys())
    r2 = set(roots_per_surah.get(s2, {}).keys())
    return jaccard(r1, r2)

def content_cosine(s1, s2):
    return cosine(tfidf_per_surah[s1], tfidf_per_surah[s2])

def char_trigram_dice(s1, s2):
    return dice(char3_per_surah[s1], char3_per_surah[s2])

def fr_similarity(s1, s2):
    if s1 == s2:
        return 1.0
    return 1.0 / (1.0 + D_fr[s1-1][s2-1])

def rhyme_cosine(s1, s2):
    v1, v2 = flv_per_surah[s1], flv_per_surah[s2]
    common = set(v1) & set(v2)
    if not common:
        return 0.0
    num = sum(v1[t] * v2[t] for t in common)
    n1 = math.sqrt(sum(x*x for x in v1.values()))
    n2 = math.sqrt(sum(x*x for x in v2.values()))
    if n1 == 0 or n2 == 0:
        return 0.0
    return num / (n1 * n2)

def divine_name_jaccard(s1, s2):
    return jaccard(dn_attested[s1], dn_attested[s2])

def char5_one_minus_dice(s1, s2):
    # similarity = dice (so HIGHER = more similar; we use mean-top3-sim convention)
    return dice(char5_per_surah[s1], char5_per_surah[s2])

instruments = {
    'I1_root_jaccard': root_jaccard,
    'I2_content_cosine': content_cosine,
    'I3_char_trigram_dice': char_trigram_dice,
    'I4_fr_similarity': fr_similarity,
    'I5_rhyme_cosine': rhyme_cosine,
    'I6_root_zipf_overlap': zipf_weighted_similarity,
    'I7_divine_name_jaccard': divine_name_jaccard,
    'I8_char_5gram_dice': char5_one_minus_dice,
}

# Build similarity matrix per instrument and compute mean_top3_sim per surah
def mean_top3_for_surah(sim_func, sid):
    sims = []
    for other in range(1, N_SURAHS+1):
        if other == sid:
            continue
        sims.append(sim_func(sid, other))
    sims.sort(reverse=True)
    return sum(sims[:3]) / 3.0

# Per-instrument: get rank of Q25 mean_top3
results = {}
hawamim = [40,41,42,43,44]
for inst_name, inst_func in instruments.items():
    print(f"[INFO] Instrument: {inst_name}")
    mean_top3 = {}
    for sid in range(1, N_SURAHS+1):
        mean_top3[sid] = mean_top3_for_surah(inst_func, sid)
    # Rank ascending (lowest = most isolated = rank 1)
    sorted_surahs = sorted(mean_top3.items(), key=lambda x: x[1])
    rank_of = {sid: i+1 for i, (sid, _) in enumerate(sorted_surahs)}
    q25_rank = rank_of[25]
    q25_value = mean_top3[25]
    # Bottom-quartile?
    in_bq = q25_rank <= BOTTOM_QUARTILE_RANK
    # MW-5 control: ḥawāmīm mean rank should NOT be in bottom-quartile
    haw_ranks = [rank_of[s] for s in hawamim]
    haw_mean_rank = sum(haw_ranks) / len(haw_ranks)
    haw_min_rank = min(haw_ranks)
    mw5_passes = haw_min_rank > BOTTOM_QUARTILE_RANK  # ḥawāmīm should NOT all be isolated
    # Permutation null: shuffle the surah-id ↔ value mapping; how often does a random surah's rank ≤ q25_rank?
    # i.e., probability that under random labeling Q25 ends up at this rank or lower
    # Equivalent to: out of 114 surahs, P(rank ≤ q25_rank) = q25_rank/114 -- so this is a degenerate null
    # The genuine null: if Q25 were a random surah, what fraction of surahs sit at this rank or below?
    # A more meaningful null: shuffle the values across surahs and recompute Q25's rank
    rng = random.Random(SEED + hash(inst_name) % 10000)
    p_count = 0
    values = list(mean_top3.values())
    for _ in range(N_PERM):
        shuffled = values[:]
        rng.shuffle(shuffled)
        # Q25 gets a random value; rank = #values < that value + 1
        q25_perm_value = shuffled[24]  # Q25 is index 24 in a shuffled array
        rk = sum(1 for v in shuffled if v < q25_perm_value) + 1
        if rk <= q25_rank:
            p_count += 1
    p_one_sided_lower = p_count / N_PERM
    results[inst_name] = {
        'q25_mean_top3_sim': q25_value,
        'q25_rank_ascending': q25_rank,
        'q25_in_bottom_quartile': in_bq,
        'p_one_sided_lower': p_one_sided_lower,
        'pass_alpha_bon': p_one_sided_lower <= ALPHA_BON,
        'mw5_hawamim_min_rank': haw_min_rank,
        'mw5_hawamim_mean_rank': haw_mean_rank,
        'mw5_passes': mw5_passes,
        'top10_isolates': [(sid, mean_top3[sid]) for sid, _ in sorted_surahs[:10]],
    }
    print(f"  Q25 rank: {q25_rank}/114, value: {q25_value:.4f}, BQ: {in_bq}, p: {p_one_sided_lower:.4f}, MW5 ḥawāmīm min-rank: {haw_min_rank}")

# Aggregate verdict
n_pass_bq = sum(1 for r in results.values() if r['q25_in_bottom_quartile'])
n_pass_alpha = sum(1 for r in results.values() if r['pass_alpha_bon'])
n_mw5_pass = sum(1 for r in results.values() if r['mw5_passes'])

print()
print(f"=== AGGREGATE ===")
print(f"Bottom-quartile sweeps: {n_pass_bq}/8")
print(f"α_bon sweeps:           {n_pass_alpha}/8")
print(f"MW-5 ḥawāmīm controls passing: {n_mw5_pass}/8")

if n_pass_bq >= 6 and n_pass_alpha >= 6:
    verdict = "PASS-DIRECTED — true-isolate persistence CONFIRMED across instruments"
elif n_pass_bq >= 4:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL — isolate-ness is instrument-specific"

print(f"VERDICT: {verdict}")

out = {
    'finding_id': 'Q025-F-01',
    'pre_reg_sha256': PRE_REG_SHA256,
    'seed': SEED,
    'n_perm': N_PERM,
    'alpha_bon': ALPHA_BON,
    'bottom_quartile_threshold': BOTTOM_QUARTILE_RANK,
    'instruments': results,
    'aggregate': {
        'n_pass_bottom_quartile_8': n_pass_bq,
        'n_pass_alpha_bon_8': n_pass_alpha,
        'n_mw5_pass_8': n_mw5_pass,
        'verdict': verdict,
    },
}
import os
os.makedirs('/Users/grey/Downloads/quran/surahs/Q025-al-furqan/csv', exist_ok=True)
with open('/Users/grey/Downloads/quran/surahs/Q025-al-furqan/csv/Q025-F-01.json', 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print('[OK] Saved Q025-F-01.json')
