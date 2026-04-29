#!/usr/bin/env python3
"""H-NEW-193 — Q 1 al-Fātiḥa's 7 verses as individual attractors in verse-twin network.

Char-trigram Jaccard similarity. For each of Q 1's 7 verses, find top-10
nearest neighbors across the corpus. Count distinct surahs touched in
the union. Null = random 7-verse sets (N=10000).

Seed 20260419. Bonferroni k=2.
"""
import hashlib
import json
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
N_NULL = 10000
TOPK_PRIMARY = 10
TOPK_SECONDARY = 50

CORPUS_FILE = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-193-q1-attractors-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-193.json'

# ---------------------------------------------------------------------------
# Pre-reg integrity
# ---------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------
# Strip Quranic pause marks and any remaining combining marks; collapse
# whitespace. Already no-tashkeel text.
PAUSE_MARKS = set('ۛۖۗۚۘۙۜ۞۩ۭۣۣ۠ۢۖۗۘۚۛۜ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬')
# Use a general approach: drop ALL non-letter Arabic characters except
# letters / hamzah / alif-maddah / etc. We'll keep only Arabic letters
# U+0621..U+064A plus U+066E..U+06D3 range, drop marks.
def normalize(text: str) -> str:
    out = []
    for ch in text:
        code = ord(ch)
        # Keep Arabic letters (Presentation forms excluded; source is basic)
        # Arabic letters: 0x0621..0x063A, 0x0640..0x064A, 0x066E..0x06D3 (common)
        if 0x0621 <= code <= 0x064A:
            if code == 0x0640:  # tatweel — skip
                continue
            out.append(ch)
        elif 0x066E <= code <= 0x06D3:
            out.append(ch)
        # else skip: spaces, pause marks, diacritics, punctuation
    return ''.join(out)


def trigrams(s: str) -> set:
    if len(s) < 3:
        return set()
    return {s[i:i+3] for i in range(len(s) - 2)}


# ---------------------------------------------------------------------------
# Load corpus
# ---------------------------------------------------------------------------
with open(CORPUS_FILE, encoding='utf-8') as f:
    corpus = json.load(f)

# Flat list: (global_idx, surah_id, verse_id, normalized_text, trigram_set)
verses = []
for surah in corpus:
    sid = surah['id']
    for v in surah['verses']:
        vid = v['id']
        norm = normalize(v['text'])
        tri = trigrams(norm)
        verses.append((sid, vid, norm, tri))

N = len(verses)
print(f"Loaded {N} verses", file=sys.stderr)
assert N == 6236, f"Expected 6236 verses, got {N}"

# Index Q 1's 7 verses
q1_indices = [i for i, (s, v, _, _) in enumerate(verses) if s == 1]
print(f"Q 1 verse indices: {q1_indices}", file=sys.stderr)
assert len(q1_indices) == 7

# ---------------------------------------------------------------------------
# Compute top-K nearest neighbors for every verse by Jaccard
# ---------------------------------------------------------------------------
# O(N^2) = ~38M pairs. Each Jaccard: set intersection ~ few hundred trigrams.
# Use sorted-by-hash fast intersection via frozenset; still ~a few minutes.
# Preconvert to frozensets.
tri_sets = [frozenset(t) for (_, _, _, t) in verses]
tri_sizes = [len(t) for t in tri_sets]

# We need: for every verse i, top-K nearest neighbors by Jaccard (excluding i).
# K_max = max(TOPK_PRIMARY, TOPK_SECONDARY) = 50.
import heapq

K = TOPK_SECONDARY
top_neighbors = [None] * N  # list of (jaccard, j) length-K

print(f"Computing pairwise Jaccard (N^2/2 = {N*(N-1)//2} pairs)...", file=sys.stderr)

# Build inverted index: trigram -> list of verse indices containing it.
# Then for each verse i, iterate only over verses sharing >=1 trigram.
inv = defaultdict(list)
for i, ts in enumerate(tri_sets):
    for t in ts:
        inv[t].append(i)

print(f"Built inverted index: {len(inv)} distinct trigrams", file=sys.stderr)

def top_k_neighbors(i):
    """Return list of (jaccard, j) length-K sorted desc."""
    ts_i = tri_sets[i]
    size_i = tri_sizes[i]
    if size_i == 0:
        return []
    # Count shared trigrams with each candidate via inverted index
    shared = defaultdict(int)
    for t in ts_i:
        for j in inv[t]:
            if j != i:
                shared[j] += 1
    # Convert to Jaccard and heap-select top-K
    heap = []  # min-heap of (jaccard, j); size<=K
    for j, cnt in shared.items():
        size_j = tri_sizes[j]
        union = size_i + size_j - cnt
        if union == 0:
            continue
        jac = cnt / union
        if len(heap) < K:
            heapq.heappush(heap, (jac, j))
        elif jac > heap[0][0]:
            heapq.heapreplace(heap, (jac, j))
    heap.sort(reverse=True)
    return heap

# Precompute for all verses
for i in range(N):
    top_neighbors[i] = top_k_neighbors(i)
    if i % 500 == 0:
        print(f"  {i}/{N}", file=sys.stderr)

print("Pairwise top-K done", file=sys.stderr)

# ---------------------------------------------------------------------------
# Q 1 observed statistics
# ---------------------------------------------------------------------------
def distinct_surahs_top10(verse_indices):
    """Union of surahs appearing in top-10 neighbors for any index in list."""
    surahs = set()
    for i in verse_indices:
        for (jac, j) in top_neighbors[i][:TOPK_PRIMARY]:
            surahs.add(verses[j][0])
    return surahs

def avg_top10_jaccard(verse_indices):
    """Average Jaccard across the top-10 neighbors of each seed verse."""
    jacs = []
    for i in verse_indices:
        for (jac, j) in top_neighbors[i][:TOPK_PRIMARY]:
            jacs.append(jac)
    return statistics.mean(jacs) if jacs else 0.0

q1_surahs = distinct_surahs_top10(q1_indices)
q1_distinct = len(q1_surahs)
q1_avg_jac = avg_top10_jaccard(q1_indices)

print(f"Q 1 distinct surahs touched (top-10 union): {q1_distinct}", file=sys.stderr)
print(f"Q 1 surahs touched list: {sorted(q1_surahs)}", file=sys.stderr)
print(f"Q 1 avg top-10 Jaccard: {q1_avg_jac:.4f}", file=sys.stderr)

# Top-10 per verse (diagnostic)
q1_per_verse = []
for i in q1_indices:
    row = {
        'q1_verse': verses[i][1],
        'top10': [
            {'surah': verses[j][0], 'verse': verses[j][1], 'jaccard': round(jac, 4)}
            for (jac, j) in top_neighbors[i][:TOPK_PRIMARY]
        ],
    }
    q1_per_verse.append(row)

# Sensitivity: verses 2-7 only (excluding v1 = basmala)
q1_nb_indices = q1_indices[1:]  # drop v1
q1_nb_surahs = distinct_surahs_top10(q1_nb_indices)
q1_nb_distinct = len(q1_nb_surahs)
q1_nb_avg_jac = avg_top10_jaccard(q1_nb_indices)
print(f"Q 1 v2-v7 (no basmala) distinct surahs: {q1_nb_distinct}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Null distribution
# ---------------------------------------------------------------------------
rng = random.Random(SEED)
non_q1_pool = [i for i in range(N) if verses[i][0] != 1]
print(f"Non-Q1 pool size: {len(non_q1_pool)}", file=sys.stderr)

null_distinct = []
null_avg_jac = []
for k in range(N_NULL):
    sample = rng.sample(non_q1_pool, 7)
    null_distinct.append(len(distinct_surahs_top10(sample)))
    null_avg_jac.append(avg_top10_jaccard(sample))
    if k % 1000 == 0:
        print(f"  null {k}/{N_NULL}", file=sys.stderr)

null_distinct_mean = statistics.mean(null_distinct)
null_distinct_median = statistics.median(null_distinct)
null_distinct_sd = statistics.stdev(null_distinct) if len(null_distinct) > 1 else 0.0
null_jac_mean = statistics.mean(null_avg_jac)
null_jac_sd = statistics.stdev(null_avg_jac) if len(null_avg_jac) > 1 else 0.0

# p-values (one-sided, direction = Q 1 > null)
p_primary = sum(1 for x in null_distinct if x >= q1_distinct) / N_NULL
p_secondary = sum(1 for x in null_avg_jac if x >= q1_avg_jac) / N_NULL

# MW-5: compare Q 1 to null median (should exceed by >= 1sd)
z_primary = ((q1_distinct - null_distinct_mean) / null_distinct_sd) if null_distinct_sd > 0 else 0.0
z_secondary = ((q1_avg_jac - null_jac_mean) / null_jac_sd) if null_jac_sd > 0 else 0.0

alpha_bon = 0.05 / 2
pass_primary = p_primary < alpha_bon
pass_secondary = p_secondary < alpha_bon
mw5_pass = q1_distinct > null_distinct_median

if pass_primary and pass_secondary and mw5_pass:
    verdict = "ATTRACTORS-CONFIRMED"
elif pass_primary:
    verdict = "PARTIAL-PRIMARY-ONLY"
else:
    verdict = "FAIL"

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
result = {
    'id': 'H-NEW-193',
    'prereg_sha256': prereg_sha,
    'seed': SEED,
    'n_null': N_NULL,
    'n_verses_corpus': N,
    'bonferroni_k': 2,
    'alpha_bon': alpha_bon,
    'q1_distinct_surahs_top10': q1_distinct,
    'q1_surahs_touched': sorted(q1_surahs),
    'q1_avg_top10_jaccard': round(q1_avg_jac, 4),
    'q1_no_basmala_distinct_surahs_top10': q1_nb_distinct,
    'q1_no_basmala_avg_top10_jaccard': round(q1_nb_avg_jac, 4),
    'null_distinct_mean': round(null_distinct_mean, 3),
    'null_distinct_median': null_distinct_median,
    'null_distinct_sd': round(null_distinct_sd, 3),
    'null_jac_mean': round(null_jac_mean, 4),
    'null_jac_sd': round(null_jac_sd, 4),
    'p_primary': p_primary,
    'p_secondary': p_secondary,
    'z_primary': round(z_primary, 3),
    'z_secondary': round(z_secondary, 3),
    'pass_primary': pass_primary,
    'pass_secondary': pass_secondary,
    'mw5_pass': mw5_pass,
    'verdict': verdict,
    'q1_per_verse_top10': q1_per_verse,
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n=== RESULT ===", file=sys.stderr)
print(f"Q1 distinct surahs (top-10 union): {q1_distinct}", file=sys.stderr)
print(f"Null mean ± sd: {null_distinct_mean:.2f} ± {null_distinct_sd:.2f}  median={null_distinct_median}", file=sys.stderr)
print(f"p_primary = {p_primary:.4f}", file=sys.stderr)
print(f"Q1 avg top-10 Jaccard: {q1_avg_jac:.4f}  null {null_jac_mean:.4f} ± {null_jac_sd:.4f}", file=sys.stderr)
print(f"p_secondary = {p_secondary:.4f}", file=sys.stderr)
print(f"verdict: {verdict}", file=sys.stderr)

print(json.dumps({
    'q1_distinct': q1_distinct,
    'null_mean': null_distinct_mean,
    'null_median': null_distinct_median,
    'null_sd': null_distinct_sd,
    'p_primary': p_primary,
    'p_secondary': p_secondary,
    'verdict': verdict,
}))
