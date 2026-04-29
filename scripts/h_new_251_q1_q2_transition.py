#!/usr/bin/env python3
"""H-NEW-251 — Characterise the Q 1 → Q 2 structural hinge across 4 feature axes.

Parent: H-NEW-238 (identified Q 1 → Q 2 as rank 114 / 114 cycle-max Fisher-Rao edge).
Pre-reg: findings/phase-b-hypotheses/h-new-251-q1-q2-transition-prereg.md

Cells:
  A. Root-FR distance (inherited from H-NEW-111 D-matrix) among 113 consecutive pairs.
  B. Char-4-gram FR distance (inherited from H-NEW-111b D-matrix).
  C. Rhyme-ending (last 2 chars of last word per verse) FR distance, computed here.
  D. Phonological (9-dim mean-tajwīd) Euclidean distance, computed here per H-NEW-165 codebook.

PASS per cell: rank(Q 1→Q 2) ≤ 5 / 113. Bonferroni k=4, α_bon = 0.0125.
Seed: 20260419.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
BONFERRONI_K = 4
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.0125
RANK_PASS_THRESHOLD = 5  # top-5 / 113

H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
H111B_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111b.json'
PREREG_MD = ROOT / 'findings/phase-b-hypotheses/h-new-251-q1-q2-transition-prereg.md'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-251.json'

print(f"SEED = {SEED}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}  α_bon = {ALPHA_BON}", file=sys.stderr)
print(f"PASS rank threshold = top-{RANK_PASS_THRESHOLD} / 113", file=sys.stderr)

prereg_sha = hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()
print(f"pre-reg SHA-256 = {prereg_sha[:16]}...", file=sys.stderr)

# The 3 established universal hinges from H-NEW-130 / 142 for comparison
UNIVERSAL_HINGES = [(14, 15), (49, 50), (56, 57)]
TEST_EDGE = (1, 2)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_D_upper_triangular(path):
    d = json.loads(path.read_text())
    D_up = d['D_matrix_upper_triangular']
    D = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in D_up:
        D[i][j] = float(dist)
        D[j][i] = float(dist)
    return D


def consecutive_distances(D):
    """Return list of 113 consecutive d(Q_k, Q_{k+1}) in mushaf order, k=1..113."""
    return [D[k][k + 1] for k in range(1, 114)]


def rank_of_pair(D, a, b):
    """Rank of D[a][b] among 113 consecutive pairs, descending (rank 1 = largest)."""
    target = D[a][b]
    all_d = consecutive_distances(D)
    # Rank 1 = largest distance
    sorted_desc = sorted(all_d, reverse=True)
    # count ≥ target with index of target = 1 + #strictly greater
    rank = 1 + sum(1 for d in all_d if d > target)
    return rank, target, sorted_desc


# ---------------------------------------------------------------------------
# Cell A — root-FR D-matrix from H-NEW-111
# ---------------------------------------------------------------------------
print("\n[Cell A] Loading H-NEW-111 root-FR D-matrix...", file=sys.stderr)
D_root = load_D_upper_triangular(H111_JSON)
rank_A, d_A, sorted_A_desc = rank_of_pair(D_root, *TEST_EDGE)
print(f"  d_FR_root(Q 1, Q 2) = {d_A:.4f}  rank {rank_A}/113", file=sys.stderr)

# Per-cell stats
def edge_stats(consec):
    return {
        'min': min(consec),
        'max': max(consec),
        'mean': statistics.mean(consec),
        'median': statistics.median(consec),
        'sd': statistics.stdev(consec),
    }


consec_root = consecutive_distances(D_root)
stats_A = edge_stats(consec_root)

# Also get rank of the 3 universal hinges for comparison
def comparator_ranks(D, pairs):
    out = {}
    all_d = consecutive_distances(D)
    for a, b in pairs:
        target = D[a][b]
        rank = 1 + sum(1 for d in all_d if d > target)
        out[f'Q{a}→Q{b}'] = {'distance': target, 'rank_desc': rank}
    return out


comp_A = comparator_ranks(D_root, UNIVERSAL_HINGES + [TEST_EDGE])

# ---------------------------------------------------------------------------
# Cell B — char-4-gram FR D-matrix from H-NEW-111b
# ---------------------------------------------------------------------------
print("\n[Cell B] Loading H-NEW-111b char-4-gram FR D-matrix...", file=sys.stderr)
D_c4g = load_D_upper_triangular(H111B_JSON)
rank_B, d_B, sorted_B_desc = rank_of_pair(D_c4g, *TEST_EDGE)
print(f"  d_FR_c4g(Q 1, Q 2) = {d_B:.4f}  rank {rank_B}/113", file=sys.stderr)
consec_c4g = consecutive_distances(D_c4g)
stats_B = edge_stats(consec_c4g)
comp_B = comparator_ranks(D_c4g, UNIVERSAL_HINGES + [TEST_EDGE])

# ---------------------------------------------------------------------------
# Cell C — Rhyme-ending FR distance
# ---------------------------------------------------------------------------
print("\n[Cell C] Computing rhyme-ending FR distances...", file=sys.stderr)

quran = json.loads(QURAN_JSON.read_text())
assert len(quran) == 114, f"Expected 114 surahs, got {len(quran)}"

# For each surah, collect last-bigram of last word of each verse
per_surah_bigrams = defaultdict(list)
for surah_obj in quran:
    sid = surah_obj['id']
    for v in surah_obj['verses']:
        text = v['text'].strip()
        if not text:
            continue
        # Last orthographic word
        last_word = text.split()[-1]
        # Keep only Arabic letters (strip punctuation)
        # Last 2 chars of last word
        if len(last_word) >= 2:
            bigram = last_word[-2:]
        else:
            bigram = last_word  # 1-char fallback
        per_surah_bigrams[sid].append(bigram)

# Closed vocabulary of all bigrams observed
all_bigrams = set()
for sid in range(1, 115):
    all_bigrams.update(per_surah_bigrams[sid])
bigram_list = sorted(all_bigrams)
bigram_idx = {b: i for i, b in enumerate(bigram_list)}
V = len(bigram_list)
print(f"  rhyme-bigram vocabulary |V| = {V}", file=sys.stderr)

# Build per-surah count vector
counts_rhyme = [[0.0] * V for _ in range(115)]
for sid in range(1, 115):
    for b in per_surah_bigrams[sid]:
        counts_rhyme[sid][bigram_idx[b]] += 1.0

# Dirichlet α=0.5 smoothing + L1 normalise
DIRICHLET_ALPHA = 0.5
prob_rhyme = [[0.0] * V for _ in range(115)]
for sid in range(1, 115):
    row = counts_rhyme[sid]
    smoothed = [c + DIRICHLET_ALPHA for c in row]
    s = sum(smoothed)
    prob_rhyme[sid] = [x / s for x in smoothed]
    assert abs(sum(prob_rhyme[sid]) - 1.0) < 1e-9

sqrt_rhyme = [[math.sqrt(p) for p in prob_rhyme[sid]] for sid in range(115)]


def fr_rhyme(i, j):
    if i == j:
        return 0.0
    bc = sum(sqrt_rhyme[i][k] * sqrt_rhyme[j][k] for k in range(V))
    bc = min(1.0, max(-1.0, bc))
    return 2.0 * math.acos(bc)


# Build 114×114 D_rhyme
D_rhyme = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_rhyme(i, j)
        D_rhyme[i][j] = d
        D_rhyme[j][i] = d

rank_C, d_C, sorted_C_desc = rank_of_pair(D_rhyme, *TEST_EDGE)
print(f"  d_FR_rhyme(Q 1, Q 2) = {d_C:.4f}  rank {rank_C}/113", file=sys.stderr)
consec_rhyme = consecutive_distances(D_rhyme)
stats_C = edge_stats(consec_rhyme)
comp_C = comparator_ranks(D_rhyme, UNIVERSAL_HINGES + [TEST_EDGE])

# ---------------------------------------------------------------------------
# Cell D — Phonological (tajwīd) Euclidean distance
# ---------------------------------------------------------------------------
print("\n[Cell D] Computing phonological Euclidean distances...", file=sys.stderr)

# H-NEW-165-style classical tajwīd feature codebook for Arabic letters.
# Features per letter: makhraj (1-8 ordinal, Khalīl), voice (0/1), emphatic (0/1),
# pharyngeal (0/1), sonorant (0/1), continuant (0/1), idhlāq (0/1).
# Standardise later; keep as raw dict first.

# Makhraj 1-8 (al-Khalīl): 1=jawf, 2=ḥalq-deep (ه، أ), 3=ḥalq-mid (ع، ح), 4=ḥalq-upper (غ، خ),
#   5=lisān-back (ق، ك), 6=lisān-mid (ج، ش، ي), 7=lisān-front (ض، ل، ن، ر، ط، د، ت، ص، ز، س، ظ، ذ، ث),
#   8=shafatān (ف، ب، م، و)
MAKHRAJ = {
    'ا': 1, 'ى': 1, 'ي': 6, 'و': 8, 'ء': 2, 'أ': 2, 'إ': 2, 'آ': 2, 'ؤ': 8, 'ئ': 6,
    'ه': 2, 'ة': 2, 'ح': 3, 'ع': 3, 'غ': 4, 'خ': 4,
    'ق': 5, 'ك': 5,
    'ج': 6, 'ش': 6,
    'ض': 7, 'ل': 7, 'ن': 7, 'ر': 7, 'ط': 7, 'د': 7, 'ت': 7, 'ص': 7, 'ز': 7, 'س': 7,
    'ظ': 7, 'ذ': 7, 'ث': 7,
    'ف': 8, 'ب': 8, 'م': 8,
}
# Voiced (majhūra) = 1; mahmūsa = 0
VOICED = {l: 1 for l in 'ابجدذرزضطظعغلمنوي'}
for l in 'تحخسشصفقكهث':
    VOICED[l] = 0
# Normalisation variants
for alias, target in [('ا', 'ا'), ('ى', 'ا'), ('أ', 'ا'), ('إ', 'ا'), ('آ', 'ا'),
                      ('ؤ', 'و'), ('ئ', 'ي'), ('ة', 'ه')]:
    VOICED.setdefault(alias, VOICED.get(target, 1))
# Emphatic (tafkhīm / mustaʿliya) = {خ، ص، ض، غ، ط، ق، ظ}
EMPHATIC_LETTERS = set('خصضغطقظ')
# Pharyngeal/uvular/guttural (ʾaṣwāt al-ḥalq + uvulars) = {ء، ه، ع، ح، غ، خ، ق}
PHARYNGEAL_LETTERS = set('ءأإآهحعغخق')
# Sonorants ≈ nasals + liquids + glides: {م، ن، ل، ر، و، ي، ء}
SONORANT_LETTERS = set('منلرويءأإآىؤئ')
# Continuants (fricatives + madd): everything except stops
STOP_LETTERS = set('بتدطضقكءأإآ')  # approximate stops
CONTINUANT_LETTERS = set('ابتثجحخدذرزسشصضطظعغفقكلمنهويىة') - STOP_LETTERS
# Idhlāq (light / idhlāq letters): {ف، ر، م، ن، ل، ب} "فر من لب"
IDHLAQ_LETTERS = set('فرمنلب')
# Qalqala: {ق، ط، ب، ج، د}
QALQALA_LETTERS = set('قطبجد')


def letter_feature(ch):
    """Return 7-dim tajwīd feature vector for letter ch, or None if non-Arabic."""
    if ch not in MAKHRAJ:
        return None
    mk = MAKHRAJ[ch]
    v = VOICED.get(ch, 0)
    em = 1 if ch in EMPHATIC_LETTERS else 0
    ph = 1 if ch in PHARYNGEAL_LETTERS else 0
    so = 1 if ch in SONORANT_LETTERS else 0
    co = 1 if ch in CONTINUANT_LETTERS else 0
    idh = 1 if ch in IDHLAQ_LETTERS else 0
    qlq = 1 if ch in QALQALA_LETTERS else 0
    # 8-dim vector: (makhraj, voice, emphatic, pharyngeal, sonorant, continuant, idhlāq, qalqala)
    return [mk, v, em, ph, so, co, idh, qlq]


# Build per-surah mean feature vector (only Arabic letters; exclude whitespace/digits)
per_surah_phono_mean = [[0.0] * 8 for _ in range(115)]
per_surah_phono_count = [0 for _ in range(115)]
for surah_obj in quran:
    sid = surah_obj['id']
    sums = [0.0] * 8
    n = 0
    for v in surah_obj['verses']:
        for ch in v['text']:
            feat = letter_feature(ch)
            if feat is None:
                continue
            for k in range(8):
                sums[k] += feat[k]
            n += 1
    if n == 0:
        continue
    per_surah_phono_mean[sid] = [x / n for x in sums]
    per_surah_phono_count[sid] = n

# Standardise each of the 8 features across 114 surahs (z-score)
feature_mat = [per_surah_phono_mean[sid] for sid in range(1, 115)]
n_sur = 114
n_feat = 8
feat_means = [statistics.mean([feature_mat[s][f] for s in range(n_sur)]) for f in range(n_feat)]
feat_sds = [statistics.stdev([feature_mat[s][f] for s in range(n_sur)]) for f in range(n_feat)]
# Replace zero sd with 1 to avoid divide-by-zero
feat_sds = [sd if sd > 1e-12 else 1.0 for sd in feat_sds]
std_mat = [[0.0] * n_feat for _ in range(115)]
for sid in range(1, 115):
    for f in range(n_feat):
        std_mat[sid][f] = (per_surah_phono_mean[sid][f] - feat_means[f]) / feat_sds[f]


def phono_euclid(i, j):
    return math.sqrt(sum((std_mat[i][f] - std_mat[j][f]) ** 2 for f in range(n_feat)))


D_phono = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = phono_euclid(i, j)
        D_phono[i][j] = d
        D_phono[j][i] = d

rank_D, d_D, sorted_D_desc = rank_of_pair(D_phono, *TEST_EDGE)
print(f"  d_phono_euclid(Q 1, Q 2) = {d_D:.4f}  rank {rank_D}/113", file=sys.stderr)
consec_phono = consecutive_distances(D_phono)
stats_D = edge_stats(consec_phono)
comp_D = comparator_ranks(D_phono, UNIVERSAL_HINGES + [TEST_EDGE])

# ---------------------------------------------------------------------------
# MW-5 cheat: shuffled-null test
# ---------------------------------------------------------------------------
print("\n[MW-5] Shuffled-null test on each cell...", file=sys.stderr)
rng = random.Random(SEED + 1)
N_SHUFFLE = 1000


def shuffled_rank_null(D, n_shuffle=N_SHUFFLE):
    """Under a random relabeling of surahs, rank of the edge between (labels 1, 2)
    in the shuffled 113-consecutive-pair list. Should be ~ uniform. Returns mean rank
    and fraction at rank ≤ 5."""
    ranks = []
    for _ in range(n_shuffle):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        # perm[0] is new surah at position 1, perm[1] at position 2
        # "Q 1 → Q 2" under this relabel is the edge D[perm[0]][perm[1]]
        target = D[perm[0]][perm[1]]
        consec = [D[perm[k]][perm[k + 1]] for k in range(113)]
        rank = 1 + sum(1 for d in consec if d > target)
        ranks.append(rank)
    return {
        'mean_rank': statistics.mean(ranks),
        'median_rank': statistics.median(ranks),
        'frac_top5': sum(1 for r in ranks if r <= 5) / len(ranks),
        'n_shuffle': n_shuffle,
    }


mw5 = {
    'cell_A_root': shuffled_rank_null(D_root),
    'cell_B_c4g': shuffled_rank_null(D_c4g),
    'cell_C_rhyme': shuffled_rank_null(D_rhyme),
    'cell_D_phono': shuffled_rank_null(D_phono),
}
for c, m in mw5.items():
    print(f"  {c}: mean_rank={m['mean_rank']:.1f} frac_top5={m['frac_top5']:.3f} "
          f"(expected ~{5/113:.3f})", file=sys.stderr)

# ---------------------------------------------------------------------------
# Content-bridge analysis — Q 1 ↔ Q 2:1-5 root overlap (HDY bridge)
# ---------------------------------------------------------------------------
print("\n[Content-bridge] Extracting Q 1 vs Q 2:1-5 root overlap...", file=sys.stderr)

# Parse QAC STEM roots for Q 1 (all verses) and Q 2:1-5
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
import re
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

q1_roots_by_verse = defaultdict(list)
q2_roots_by_verse = defaultdict(list)
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        vid = int(m.group(2))
        if sid not in (1, 2):
            continue
        if sid == 2 and vid > 5:
            continue
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        r = rm.group(1)
        if sid == 1:
            q1_roots_by_verse[vid].append(r)
        else:
            q2_roots_by_verse[vid].append(r)

q1_roots = set()
for v in q1_roots_by_verse.values():
    q1_roots.update(v)
q2_1_5_roots = set()
for v in q2_roots_by_verse.values():
    q2_1_5_roots.update(v)
shared = q1_roots & q2_1_5_roots

# Check specific HDY bridge: Q 1:6 ihdinā; Q 2:2 hudan
hdy_in_q1 = 'hdy' in q1_roots_by_verse.get(6, [])  # Q 1:6 "ihdinā"
hdy_in_q2v2 = 'hdy' in q2_roots_by_verse.get(2, [])  # Q 2:2 "hudan"
print(f"  Q 1 roots (all 7 verses): |{len(q1_roots)}|", file=sys.stderr)
print(f"  Q 2:1-5 roots: |{len(q2_1_5_roots)}|", file=sys.stderr)
print(f"  Shared roots: |{len(shared)}| = {sorted(shared)}", file=sys.stderr)
print(f"  HDY in Q 1:6? {hdy_in_q1}  HDY in Q 2:2? {hdy_in_q2v2}", file=sys.stderr)

# Jaccard + container fractions
union = q1_roots | q2_1_5_roots
jaccard = len(shared) / len(union) if union else 0.0
frac_q1_in_shared = len(shared) / len(q1_roots) if q1_roots else 0.0
frac_q2v15_in_shared = len(shared) / len(q2_1_5_roots) if q2_1_5_roots else 0.0

# ---------------------------------------------------------------------------
# Verdicts
# ---------------------------------------------------------------------------
def verdict_cell(rank, label):
    if rank <= RANK_PASS_THRESHOLD:
        return 'PASS'
    return 'NULL'


cells = {
    'A_root_FR': {'d': d_A, 'rank': rank_A, 'threshold': RANK_PASS_THRESHOLD,
                  'verdict': verdict_cell(rank_A, 'A'), 'stats': stats_A, 'comparators': comp_A},
    'B_char4gram_FR': {'d': d_B, 'rank': rank_B, 'threshold': RANK_PASS_THRESHOLD,
                       'verdict': verdict_cell(rank_B, 'B'), 'stats': stats_B, 'comparators': comp_B},
    'C_rhyme_FR': {'d': d_C, 'rank': rank_C, 'threshold': RANK_PASS_THRESHOLD,
                   'verdict': verdict_cell(rank_C, 'C'), 'stats': stats_C, 'comparators': comp_C,
                   'vocabulary_size': V},
    'D_phono_euclid': {'d': d_D, 'rank': rank_D, 'threshold': RANK_PASS_THRESHOLD,
                       'verdict': verdict_cell(rank_D, 'D'), 'stats': stats_D, 'comparators': comp_D},
}

pass_count = sum(1 for c in cells.values() if c['verdict'] == 'PASS')
if pass_count == 4:
    overall = 'UNIVERSAL-HINGE'
    interp = 'Q 1→Q 2 is top-5 on all 4 axes; add as 4th universal hinge.'
elif pass_count == 3:
    overall = 'STRONG-HINGE'
    interp = f'Q 1→Q 2 is top-5 on 3 of 4 axes; strong-hinge, axis-specific universality.'
elif pass_count == 2:
    overall = 'MODERATE-HINGE'
    interp = f'Q 1→Q 2 is top-5 on 2 of 4 axes; moderate-hinge, feature-specific.'
elif pass_count == 1:
    overall = 'AXIS-SPECIFIC'
    interp = f'Q 1→Q 2 is top-5 on 1 of 4 axes; effect is feature-specific.'
else:
    overall = 'NULL'
    interp = 'Q 1→Q 2 is not top-5 on any axis; not generally hinge-like.'

print(f"\n{'=' * 72}", file=sys.stderr)
print(f"OVERALL VERDICT: {overall}  ({pass_count}/4 cells PASS)", file=sys.stderr)
print(f"Interpretation: {interp}", file=sys.stderr)
print(f"{'=' * 72}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Build summary + write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-251',
    'title': 'Q 1 → Q 2 structural-hinge characterisation across 4 feature axes',
    'prereg_sha256': prereg_sha,
    'parent': 'H-NEW-238',
    'related': ['H-NEW-130', 'H-NEW-130b', 'H-NEW-142', 'H-NEW-155',
                'H-NEW-192', 'H-NEW-244'],
    'seed': SEED,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'rank_pass_threshold': RANK_PASS_THRESHOLD,
    'rules_tuple': ('(no-tashkeel; Hafs-Kūfan; FR arccos-Bhattacharyya Dirichlet '
                    'α=0.5 for A/B/C; H-NEW-165-style 8-dim phonological Euclidean '
                    'for D; 113 consecutive mushaf edges; seed 20260419)'),
    'test_edge': 'Q 1 → Q 2',
    'cells': cells,
    'pass_count': pass_count,
    'overall_verdict': overall,
    'interpretation': interp,
    'mw5_shuffled_null': mw5,
    'content_bridge': {
        'q1_all_roots': sorted(q1_roots),
        'q2_v1_5_roots': sorted(q2_1_5_roots),
        'shared_roots': sorted(shared),
        'n_q1_roots': len(q1_roots),
        'n_q2_v1_5_roots': len(q2_1_5_roots),
        'n_shared': len(shared),
        'jaccard': jaccard,
        'frac_q1_in_shared': frac_q1_in_shared,
        'frac_q2v15_in_shared': frac_q2v15_in_shared,
        'hdy_in_q1_v6_ihdina': hdy_in_q1,
        'hdy_in_q2_v2_hudan': hdy_in_q2v2,
        'q1_roots_by_verse': {k: v for k, v in q1_roots_by_verse.items()},
        'q2_roots_by_verse': {k: v for k, v in q2_roots_by_verse.items()},
    },
    'comparator_summary': {
        'note': 'Rank (desc) of Q 1→Q 2, Q 14→15, Q 49→50, Q 56→57 in each cell',
        'cell_A_root': comp_A,
        'cell_B_c4g': comp_B,
        'cell_C_rhyme': comp_C,
        'cell_D_phono': comp_D,
    },
    'date': '2026-04-17',
}


def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o


summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Final stdout summary
# ---------------------------------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-251 SUMMARY", file=sys.stderr)
print("=" * 72, file=sys.stderr)
for cell_id, c in cells.items():
    print(f"  Cell {cell_id}: d = {c['d']:.4f}  rank {c['rank']:>3d}/113  -> {c['verdict']}",
          file=sys.stderr)
print(f"\n  Overall: {overall}  ({pass_count}/4 PASS)", file=sys.stderr)
print(f"  Content-bridge: Q 1 roots = {len(q1_roots)}, Q 2:1-5 roots = {len(q2_1_5_roots)}, "
      f"shared = {len(shared)} (Jaccard = {jaccard:.3f})", file=sys.stderr)
print(f"  HDY (ihdinā/hudan) bridge Q 1:6 → Q 2:2: "
      f"{'CONFIRMED' if hdy_in_q1 and hdy_in_q2v2 else 'NOT_CONFIRMED'}", file=sys.stderr)
print("=" * 72, file=sys.stderr)
