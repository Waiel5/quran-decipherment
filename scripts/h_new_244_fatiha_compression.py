#!/usr/bin/env python3
"""H-NEW-244 — Q 1 al-Fātiḥa as *umm al-kitāb* information-theoretic compression test.

Cell A: Q 1 vs ~6230 sliding 7-verse char-4-gram KL windows.
Cell B: Q 1 roots' cross-surah presence rate.
Cell C: per-verse-normalized KL rank of Q 1 among 114 surahs.

MW-5: random 7-verse window should NOT rank top-5% on Cell A.

Seed 20260419, Dirichlet α=0.5, Bonferroni-3 α_bon=0.0167.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
ALPHA = 0.5  # Dirichlet smoothing
NGRAM = 4

DATA_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG = ROOT / 'findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-244.json'

prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Load corpus
# ---------------------------------------------------------------------------
with open(DATA_JSON, encoding='utf-8') as f:
    surahs = json.load(f)

# Build flat verse list: [(sid, vid, text), ...]
flat_verses = []
for s in surahs:
    sid = s['id']
    for v in s['verses']:
        flat_verses.append((sid, v['id'], v['text']))
print(f"Total verses: {len(flat_verses)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Char-4-gram helpers
# ---------------------------------------------------------------------------
def ngrams_of(text, n=NGRAM):
    """Return Counter of char-n-grams on text (space-normalised)."""
    t = re.sub(r'\s+', ' ', text.strip())
    c = Counter()
    if len(t) < n:
        return c
    for i in range(len(t) - n + 1):
        c[t[i:i+n]] += 1
    return c

def text_of_verses(vlist):
    """Concatenate verse texts with single-space separator."""
    return ' '.join(txt for _, _, txt in vlist)

# Build global vocabulary = union of all 4-grams in the full corpus
corpus_ng = Counter()
for sid, vid, txt in flat_verses:
    corpus_ng.update(ngrams_of(txt))
V = sorted(corpus_ng.keys())
Vidx = {g: i for i, g in enumerate(V)}
VSIZE = len(V)
CORPUS_TOTAL = sum(corpus_ng.values())
print(f"Global 4-gram vocabulary size: {VSIZE}; total 4-grams: {CORPUS_TOTAL}", file=sys.stderr)

def smoothed_dist_from_counter(counter):
    """Return a dense prob-array of length VSIZE with Dirichlet(ALPHA) smoothing
       over the GLOBAL vocabulary (only 4-grams in V are counted)."""
    counts = [counter.get(g, 0) for g in V]
    denom = sum(counts) + ALPHA * VSIZE
    return [(c + ALPHA) / denom for c in counts]

def kl_divergence(p, q):
    """KL(p || q) in nats. Assumes p, q same length, both >0."""
    s = 0.0
    for a, b in zip(p, q):
        if a > 0:
            s += a * math.log(a / b)
    return s

def counter_of_verse_range(vlist):
    c = Counter()
    for _, _, txt in vlist:
        for g, n in ngrams_of(txt).items():
            if g in Vidx:  # always true given V is global
                c[g] += n
    return c

# Full-corpus smoothed distribution
P_CORPUS = smoothed_dist_from_counter(corpus_ng)

# ---------------------------------------------------------------------------
# Cell A — sliding 7-verse window KL vs rest-of-corpus
# ---------------------------------------------------------------------------
WIN = 7
n_windows = len(flat_verses) - WIN + 1
print(f"Sliding windows (size {WIN}): {n_windows}", file=sys.stderr)

# For efficiency: compute each window's ngram counter incrementally
# then for each window compute KL(p_window || p_rest) with
# p_rest derived by subtracting window counts from corpus counts.

# Pre-compute per-verse 4-gram counters
per_verse_ng = [ngrams_of(txt) for _, _, txt in flat_verses]

def window_counter(start):
    c = Counter()
    for i in range(start, start + WIN):
        c.update(per_verse_ng[i])
    return c

def rest_counter(win_c):
    """Return Counter = corpus_ng - win_c (still positive where corpus > win)."""
    r = Counter(corpus_ng)
    r.subtract(win_c)
    return r

def kl_window_vs_rest(start):
    wc = window_counter(start)
    rc = rest_counter(wc)
    pw = smoothed_dist_from_counter(wc)
    pr = smoothed_dist_from_counter(rc)
    return kl_divergence(pw, pr)

# Locate Q 1 window start index
q1_start = next(i for i, (sid, vid, _) in enumerate(flat_verses) if sid == 1 and vid == 1)
assert flat_verses[q1_start][0] == 1 and flat_verses[q1_start][1] == 1
assert flat_verses[q1_start + 6][0] == 1 and flat_verses[q1_start + 6][1] == 7
print(f"Q 1 window starts at flat index {q1_start}", file=sys.stderr)

# Compute Q 1's window KL, then all window KLs
q1_kl = kl_window_vs_rest(q1_start)
print(f"Q 1 KL(window || rest): {q1_kl:.6f}", file=sys.stderr)

# Now compute ALL window KLs (~6230). This is ~6230 * (VSIZE ops).
# VSIZE likely ~30-40K; 6230 * 40K = 250M ops; doable but slow with pure python.
# Use float lists; keep it straightforward, accept ~30-60 sec.

all_kls = []
for i in range(n_windows):
    all_kls.append(kl_window_vs_rest(i))
    if i % 500 == 0:
        print(f"  window {i}/{n_windows} KL={all_kls[-1]:.4f}", file=sys.stderr)

# Rank of Q 1 (lowest = most representative)
sorted_kls = sorted(all_kls)
q1_rank = sorted([(k, i) for i, k in enumerate(all_kls)])  # [(kl, window_idx), ...]
q1_window_rank = sum(1 for k in all_kls if k < q1_kl) + 1  # 1-indexed; lower KL = lower rank
q1_percentile = q1_window_rank / n_windows
print(f"Q 1 window rank: {q1_window_rank} / {n_windows} ({q1_percentile*100:.2f}%ile, lower = more representative)",
      file=sys.stderr)
pass_A = q1_percentile <= 0.05

# MW-5: random 7-verse window (non-contiguous, just a random start index
# actually we pre-committed "random 7-verse window". Draw a random contiguous
# start index seeded by SEED; also draw a random NON-contiguous 7-verse sample
# to test both.
rng = random.Random(SEED)
random_start = rng.randrange(0, n_windows)
random_contig_kl = all_kls[random_start]
random_contig_rank = sum(1 for k in all_kls if k < random_contig_kl) + 1
random_contig_percentile = random_contig_rank / n_windows
mw5_contig_pass = random_contig_percentile > 0.05
print(f"MW-5 (random contig 7-verse start={random_start}): rank {random_contig_rank} "
      f"({random_contig_percentile*100:.2f}%ile, should NOT be top-5%): "
      f"{'PASS' if mw5_contig_pass else 'FAIL'}", file=sys.stderr)

# Additional MW-5: random non-contiguous 7-verse sample — build its KL freshly
rand_sample_idxs = rng.sample(range(len(flat_verses)), 7)
rand_c = Counter()
for ix in rand_sample_idxs:
    rand_c.update(per_verse_ng[ix])
rand_rest = Counter(corpus_ng)
rand_rest.subtract(rand_c)
rand_kl = kl_divergence(
    smoothed_dist_from_counter(rand_c),
    smoothed_dist_from_counter(rand_rest),
)
# rank within sliding windows (approximate since non-contiguous isn't in distribution)
rand_rank_approx = sum(1 for k in all_kls if k < rand_kl) + 1
rand_percentile_approx = rand_rank_approx / n_windows
mw5_noncontig_pass = rand_percentile_approx > 0.05
print(f"MW-5 (random non-contig 7-verse KL={rand_kl:.4f}): approximate rank {rand_rank_approx} "
      f"({rand_percentile_approx*100:.2f}%ile, should NOT be top-5%): "
      f"{'PASS' if mw5_noncontig_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell B — Q 1 roots' cross-surah presence rate
# ---------------------------------------------------------------------------
# Use QAC morphology if available; else a simple consonantal skeleton stemmer.
# To match H-NEW-155 method, try QAC first.
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'

root_appears_in_surah = defaultdict(set)  # root -> set of surah ids
verse_roots = defaultdict(lambda: defaultdict(set))  # sid -> vid -> {roots}

if QAC_FILE.exists():
    LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
    ROOT_RE = re.compile(r'ROOT:([^|]+)')
    with open(QAC_FILE, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            p = line.rstrip().split('\t')
            if len(p) < 4:
                continue
            m = LOC_RE.match(p[0])
            if not m:
                continue
            sid, vid = int(m.group(1)), int(m.group(2))
            if 'STEM' not in p[3]:
                continue
            rm = ROOT_RE.search(p[3])
            if not rm:
                continue
            root = rm.group(1)
            verse_roots[sid][vid].add(root)
            root_appears_in_surah[root].add(sid)
    print(f"QAC roots loaded; |roots| = {len(root_appears_in_surah)}", file=sys.stderr)
else:
    print("QAC file missing — Cell B fallback not implemented. Skip.", file=sys.stderr)

# Q 1 roots
q1_root_set = set()
for vid in range(1, 8):
    q1_root_set.update(verse_roots[1].get(vid, set()))
print(f"Q 1 distinct STEM roots: {len(q1_root_set)}", file=sys.stderr)

# Cross-surah presence rate:
# For each of the other 113 surahs, what fraction of Q 1's roots appear there?
other_surahs = [s['id'] for s in surahs if s['id'] != 1]
q1_cross_presence = []  # list of fractions
for s in other_surahs:
    surah_roots = set()
    for vid, roots in verse_roots[s].items():
        surah_roots.update(roots)
    frac = len(q1_root_set & surah_roots) / len(q1_root_set) if q1_root_set else 0.0
    q1_cross_presence.append(frac)

q1_mean_cross_presence = sum(q1_cross_presence) / len(q1_cross_presence)
print(f"Q 1 roots' mean cross-surah presence rate: {q1_mean_cross_presence:.4f}", file=sys.stderr)

# Null: for 10K random 7-verse non-contiguous samples, compute THEIR roots
# and THEIR mean cross-surah presence-rate on the other 113 surahs.
all_verses_with_roots = [(s, v) for s in verse_roots for v in verse_roots[s]]
N_NULL_B = 10000
rng_B = random.Random(SEED + 1)
null_means_B = []
for _ in range(N_NULL_B):
    sample = rng_B.sample(all_verses_with_roots, 7)
    sample_roots = set()
    for sid, vid in sample:
        sample_roots.update(verse_roots[sid].get(vid, set()))
    if not sample_roots:
        null_means_B.append(0.0)
        continue
    # same cross-surah presence rate, averaged over the OTHER 113 surahs
    # (if the sample roots are from surahs, we compute over ALL 114 and
    # exclude nothing — mirror Q 1 logic by excluding the surah the verse
    # came from for simplicity use all 114 minus surah-1 for the null too)
    crosses = []
    for s in other_surahs:
        surah_roots = set()
        for vid, roots in verse_roots[s].items():
            surah_roots.update(roots)
        frac = len(sample_roots & surah_roots) / len(sample_roots)
        crosses.append(frac)
    null_means_B.append(sum(crosses) / len(crosses))

null_mean_B = sum(null_means_B) / len(null_means_B)
null_sd_B = (sum((x - null_mean_B)**2 for x in null_means_B) / len(null_means_B)) ** 0.5
n_ge = sum(1 for x in null_means_B if x >= q1_mean_cross_presence)
p_B = (n_ge + 1) / (N_NULL_B + 1)
print(f"Null mean cross-presence: {null_mean_B:.4f} SD {null_sd_B:.4f}; p_upper = {p_B:.4f}",
      file=sys.stderr)
pass_B = p_B < 0.0167

# ---------------------------------------------------------------------------
# Cell C — per-verse-normalized KL rank
# ---------------------------------------------------------------------------
# For each surah s, compute KL(p_s || p_{rest}) on char-4-gram with
# Dirichlet α=0.5, then divide by verse_count.
per_surah_kl = {}
per_surah_verse_kl = {}
for s in surahs:
    sid = s['id']
    verses = s['verses']
    s_counter = Counter()
    for v in verses:
        s_counter.update(ngrams_of(v['text']))
    rest_counter_s = Counter(corpus_ng)
    rest_counter_s.subtract(s_counter)
    kl = kl_divergence(
        smoothed_dist_from_counter(s_counter),
        smoothed_dist_from_counter(rest_counter_s),
    )
    per_surah_kl[sid] = kl
    per_surah_verse_kl[sid] = kl / len(verses)

sorted_by_pv = sorted(per_surah_verse_kl.items(), key=lambda x: x[1])
q1_pv_kl = per_surah_verse_kl[1]
q1_pv_rank = 1 + sum(1 for sid, v in per_surah_verse_kl.items() if v < q1_pv_kl)
q1_pv_percentile = q1_pv_rank / 114
print(f"Q 1 per-verse-KL: {q1_pv_kl:.6f}; rank {q1_pv_rank}/114 ({q1_pv_percentile*100:.2f}%ile)",
      file=sys.stderr)
pass_C = q1_pv_percentile <= 0.05

print("\n--- SUMMARY ---", file=sys.stderr)
print(f"Cell A: rank {q1_window_rank}/{n_windows} = {q1_percentile*100:.2f}%ile → "
      f"{'PASS' if pass_A else 'NULL'} (α_bon=5%)", file=sys.stderr)
print(f"Cell B: p = {p_B:.4f} → {'PASS' if pass_B else 'NULL'} (α_bon=0.0167)", file=sys.stderr)
print(f"Cell C: rank {q1_pv_rank}/114 = {q1_pv_percentile*100:.2f}%ile → "
      f"{'PASS' if pass_C else 'NULL'} (α_bon=5%)", file=sys.stderr)

# Top/bottom windows and surahs for context
top_windows = []
for idx in sorted(range(n_windows), key=lambda i: all_kls[i])[:15]:
    # Describe the window by its first and last (sid, vid)
    sid0, vid0, _ = flat_verses[idx]
    sid1, vid1, _ = flat_verses[idx + 6]
    top_windows.append({
        "window_start": idx,
        "verse_start": f"Q {sid0}:{vid0}",
        "verse_end": f"Q {sid1}:{vid1}",
        "kl": all_kls[idx],
    })

top_surahs_pv = [
    {"sid": sid, "per_verse_kl": v, "raw_kl": per_surah_kl[sid]}
    for sid, v in sorted_by_pv[:15]
]
bottom_surahs_pv = [
    {"sid": sid, "per_verse_kl": v, "raw_kl": per_surah_kl[sid]}
    for sid, v in sorted_by_pv[-10:]
]

# Dump JSON
out = {
    "id": "H-NEW-244",
    "seed": SEED,
    "prereg_sha256": prereg_sha,
    "rules_tuple": "(no-tashkeel, hafs-kufan, 7-verse sliding windows, char-4-gram, Dirichlet α=0.5, seed 20260419)",
    "cell_A": {
        "q1_kl": q1_kl,
        "q1_rank": q1_window_rank,
        "total_windows": n_windows,
        "q1_percentile": q1_percentile,
        "alpha_bon": 0.05,
        "pass": pass_A,
        "top_15_windows_by_low_kl": top_windows,
        "mw5_random_contig_start": random_start,
        "mw5_random_contig_rank": random_contig_rank,
        "mw5_random_contig_percentile": random_contig_percentile,
        "mw5_contig_pass": mw5_contig_pass,
        "mw5_random_noncontig_kl": rand_kl,
        "mw5_random_noncontig_rank_approx": rand_rank_approx,
        "mw5_random_noncontig_percentile_approx": rand_percentile_approx,
        "mw5_noncontig_pass": mw5_noncontig_pass,
    },
    "cell_B": {
        "q1_root_count": len(q1_root_set),
        "q1_mean_cross_presence_rate": q1_mean_cross_presence,
        "null_mean": null_mean_B,
        "null_sd": null_sd_B,
        "p_upper": p_B,
        "n_null": N_NULL_B,
        "alpha_bon": 0.0167,
        "pass": pass_B,
    },
    "cell_C": {
        "q1_per_verse_kl": q1_pv_kl,
        "q1_rank": q1_pv_rank,
        "q1_percentile": q1_pv_percentile,
        "alpha_bon": 0.05,
        "pass": pass_C,
        "top_15_surahs_by_low_per_verse_kl": top_surahs_pv,
        "bottom_10_surahs_by_per_verse_kl": bottom_surahs_pv,
    },
}
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\nResults written to {OUT_JSON}", file=sys.stderr)
