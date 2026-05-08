#!/usr/bin/env python3
"""Q019-F-02 — KHYʿṢ structural uniqueness FR-neighborhood test.

Tests whether Q 19 KHYʿṢ (singleton 5-letter cluster) has FR-nearest neighbors
predominantly drawn from the multi-prophet narrative + ḥawāmīm clusters.

Pre-reg SHA-256: efe91b7f7d7ef0fec22da88e5bb757d8055a1f932fe450f5d4f8c60f4407154d
"""
import hashlib, json, math, os, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q019-maryam/preregs/Q019-F-02-khyas-structural-uniqueness-prereg.md'
EXPECTED_SHA = 'efe91b7f7d7ef0fec22da88e5bb757d8055a1f932fe450f5d4f8c60f4407154d'
OUT_JSON = ROOT / 'surahs/Q019-maryam/csv/Q019-F-02.json'
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
SEED = 20260428
K_TOP = 500
DIRICHLET_ALPHA = 0.5
N_PERM = 10000

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
if sha != EXPECTED_SHA:
    print(f"PRE-REG SHA MISMATCH: got {sha}, expected {EXPECTED_SHA}", file=sys.stderr)
    sys.exit(1)
print(f"pre-reg SHA verified: {sha}", file=sys.stderr)

# Parse QAC stem-roots
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)
global_root_counts = Counter()
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4: continue
        m = LOC_RE.match(parts[0])
        if not m: continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat: continue
        rm = ROOT_RE.search(feat)
        if not rm: continue
        per_surah_roots[sid].append(rm.group(1))
        global_root_counts[rm.group(1)] += 1

top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
root_idx = {r: i for i, r in enumerate(top_roots)}

def make_prob_vec(sid):
    counts = [DIRICHLET_ALPHA] * K_TOP
    for r in per_surah_roots[sid]:
        if r in root_idx:
            counts[root_idx[r]] += 1
    s = sum(counts)
    return [c / s for c in counts]

vecs = {sid: make_prob_vec(sid) for sid in range(1, 115)}

def fisher_rao(p, q):
    s = sum(math.sqrt(p[i] * q[i]) for i in range(len(p)))
    s = max(0.0, min(1.0, s))
    return 2.0 * math.acos(s)

# Q 19's row
q19 = vecs[19]
distances = [(sid, fisher_rao(q19, vecs[sid])) for sid in range(1, 115) if sid != 19]
distances.sort(key=lambda x: x[1])

top_5 = distances[:5]
top_10 = distances[:10]
top_5_ids = {s[0] for s in top_5}

# Target set: multi-prophet + ḥawāmīm + Anbiyāʾ + ṬSM + YS
TARGET = {21, 27, 28, 36, 40, 41, 42, 43, 44, 45, 46}
SINGLE_LETTER = {38, 50, 68}  # negative-control cluster

target_hits_top5 = sum(1 for sid in top_5_ids if sid in TARGET)
single_hits_top5 = sum(1 for sid, _ in top_5 if sid in SINGLE_LETTER)

# Permutation null
rng = random.Random(SEED)
null_target_hits = []
all_others = [sid for sid in range(1, 115) if sid != 19]
for _ in range(N_PERM):
    sample = rng.sample(all_others, 5)
    null_target_hits.append(sum(1 for sid in sample if sid in TARGET))

null_ge = sum(1 for h in null_target_hits if h >= target_hits_top5) / N_PERM

result = {
    'finding_id': 'Q019-F-02',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': f'(no-tashkeel, QAC-STEM root, K={K_TOP}, Dirichlet alpha={DIRICHLET_ALPHA}, Hafs-Kufan, Mashriqi)',
    'observed': {
        'q19_top5_neighbors': [{'surah': s, 'fr_distance': d} for s, d in top_5],
        'q19_top10_neighbors': [{'surah': s, 'fr_distance': d} for s, d in top_10],
        'target_set': sorted(TARGET),
        'target_hits_top5': target_hits_top5,
        'single_letter_hits_top5': single_hits_top5,
        'mean_fr_to_corpus': sum(d for _, d in distances) / len(distances),
    },
    'null_distribution': {
        'expected_target_hits': sum(null_target_hits) / N_PERM,
        'p_value_ge_observed': null_ge,
        'null_target_hits_p95': sorted(null_target_hits)[int(0.95*N_PERM)],
    },
    'verdict': {
        'direction_locked': 'top-5 hits ≥ 4 in target set, p < 0.0125',
        'pass': target_hits_top5 >= 4 and null_ge < 0.0125,
        'note': f'top-5 target hits = {target_hits_top5}, p = {null_ge:.4f}',
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"output: {OUT_JSON}", file=sys.stderr)
print(f"VERDICT: {'PASS' if result['verdict']['pass'] else 'FAIL'} — top5 hits={target_hits_top5}, p={null_ge:.4f}", file=sys.stderr)
