#!/usr/bin/env python3
"""H-NEW-245 — Cross-chronology consensus ordering vs mushaf.

Pre-registered tests (Bonferroni k=3, α_bon=0.0167):
  CELL A — Kendall τ(consensus, mushaf) > max_c τ(c, mushaf) (chronology-shuffle null)
  CELL B — L_FR(consensus) < min_c L_FR(c)                   (uniform-perm null)
  CELL C — pairwise Kendall τ matrix (descriptive only)

Inputs (de-duplicated, 5 distinct chronologies, Weighting-A = primary):
  Nöldeke 1860, Egyptian/Suyūṭī/Tanzil, Bell 1937, Blachère 1947, Ibn ʿAbbās.
Weighting-B (raw-6, secondary) adds Suyūṭī + Tanzil as separate slots.

Reuses D matrix from h-new-111.json (Fisher-Rao angular distance).
Reuses Ibn ʿAbbās, Suyūṭī, Tanzil orderings from h-new-222.json.
Reuses Bell, Blachère dicts from scripts/h_new_212_alt_chronology_fisher_rao.py.
Seed 20260419.
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-245-chronology-consensus-prereg.md'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
H212_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-212.json'
H222_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-222.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-245.json'

# -----------------------------------------------------------------------------
# Pre-reg tamper-evidence
# -----------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
h222_sha = hashlib.sha256(H222_JSON.read_bytes()).hexdigest()
print(f"prereg SHA-256:  {prereg_sha}", file=sys.stderr)
print(f"h-new-111 D source SHA-256: {h111_sha}", file=sys.stderr)
print(f"h-new-222 chronology source SHA-256: {h222_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 1. Load D matrix
# -----------------------------------------------------------------------------
print("\nLoading D matrix from h-new-111.json ...", file=sys.stderr)
h111 = json.loads(H111_JSON.read_text())
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
assert len(D_up) == 114 * 113 // 2

L_mushaf_h111 = float(h111['primary']['L_mushaf'])


def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L


# -----------------------------------------------------------------------------
# 2. Load chronologies: ranks (mushaf_id -> rank) and orderings (list[mushaf_id])
# -----------------------------------------------------------------------------
# 2a. Egyptian + Nöldeke from revelation-order.csv
mushaf_to_egyptian = {}
mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        mushaf_to_egyptian[msid] = int(row['revelation_order'])
        mushaf_to_noldeke[msid] = int(row['noldeke_order'])

egyptian_order = sorted(range(1, 115), key=lambda s: (mushaf_to_egyptian[s], s))
noldeke_order = sorted(range(1, 115), key=lambda s: (mushaf_to_noldeke[s], s))

# 2b. Bell + Blachère: hard-coded from h_new_212 (copied verbatim)
BELL_RANK = {
    1: 45, 2: 91, 3: 97, 4: 100, 5: 114, 6: 89, 7: 87, 8: 95, 9: 113, 10: 84,
    11: 75, 12: 77, 13: 90, 14: 76, 15: 52, 16: 73, 17: 72, 18: 68, 19: 58,
    20: 55, 21: 65, 22: 107, 23: 64, 24: 105, 25: 66, 26: 56, 27: 67, 28: 79,
    29: 81, 30: 74, 31: 82, 32: 69, 33: 103, 34: 85, 35: 86, 36: 60, 37: 51,
    38: 59, 39: 80, 40: 78, 41: 70, 42: 62, 43: 61, 44: 53, 45: 71, 46: 88,
    47: 96, 48: 108, 49: 112, 50: 54, 51: 48, 52: 22, 53: 30, 54: 49, 55: 28,
    56: 23, 57: 99, 58: 106, 59: 102, 60: 110, 61: 98, 62: 94, 63: 104, 64: 93,
    65: 101, 66: 109, 67: 63, 68: 50, 69: 24, 70: 32, 71: 52, 72: 62, 73: 33,
    74: 2, 75: 27, 76: 34, 77: 25, 78: 26, 79: 20, 80: 17, 81: 15, 82: 15,
    83: 35, 84: 19, 85: 42, 86: 9, 87: 16, 88: 21, 89: 41, 90: 39, 91: 7,
    92: 14, 93: 4, 94: 5, 95: 10, 96: 1, 97: 29, 98: 92, 99: 11, 100: 13,
    101: 12, 102: 31, 103: 6, 104: 38, 105: 40, 106: 3, 107: 8, 108: 37,
    109: 44, 110: 111, 111: 36, 112: 43, 113: 46, 114: 47,
}
BLACHERE_RANK = {
    1: 5, 2: 87, 3: 89, 4: 92, 5: 112, 6: 55, 7: 39, 8: 88, 9: 113, 10: 51,
    11: 52, 12: 53, 13: 96, 14: 72, 15: 54, 16: 70, 17: 50, 18: 69, 19: 44,
    20: 45, 21: 73, 22: 103, 23: 74, 24: 102, 25: 42, 26: 47, 27: 48, 28: 49,
    29: 85, 30: 84, 31: 57, 32: 75, 33: 90, 34: 58, 35: 43, 36: 41, 37: 56,
    38: 38, 39: 59, 40: 60, 41: 61, 42: 53, 43: 63, 44: 64, 45: 65, 46: 66,
    47: 95, 48: 111, 49: 106, 50: 34, 51: 67, 52: 76, 53: 23, 54: 37, 55: 97,
    56: 46, 57: 94, 58: 105, 59: 101, 60: 91, 61: 109, 62: 110, 63: 104,
    64: 108, 65: 99, 66: 107, 67: 77, 68: 2, 69: 78, 70: 79, 71: 71, 72: 40,
    73: 3, 74: 4, 75: 31, 76: 98, 77: 33, 78: 80, 79: 81, 80: 24, 84: 24,
    81: 82, 82: 86, 83: 83, 85: 27, 86: 36, 87: 8, 88: 68, 89: 10, 90: 35,
    91: 26, 92: 9, 93: 11, 94: 12, 95: 28, 96: 1, 97: 25, 98: 100, 99: 93,
    100: 14, 101: 30, 102: 16, 103: 13, 104: 32, 105: 19, 106: 29, 107: 17,
    108: 15, 109: 18, 110: 114, 111: 6, 112: 22, 113: 20, 114: 21,
}
bell_order = sorted(range(1, 115), key=lambda s: (BELL_RANK[s], s))
blachere_order = sorted(range(1, 115), key=lambda s: (BLACHERE_RANK[s], s))

# 2c. Ibn ʿAbbās, Suyūṭī, Tanzil from h-new-222
h222 = json.loads(H222_JSON.read_text())
ibn_abbas_order = h222['orderings_full']['ibn_abbas']
suyuti_order = h222['orderings_full']['suyuti_itqan']
tanzil_order = h222['orderings_full']['tanzil']

# Sanity: Suyūṭī == Tanzil (per H-NEW-222 §3.2)
assert suyuti_order == tanzil_order, "H-NEW-222 claim: Suyūṭī == Tanzil"
# Sanity: Tanzil list == Egyptian list (per H-NEW-222 §3.2)
assert tanzil_order == egyptian_order, (
    f"H-NEW-222 claim: Tanzil == Egyptian\n"
    f"  tanzil[:5]={tanzil_order[:5]}\n"
    f"  egyptian[:5]={egyptian_order[:5]}")

# Build rank dicts (mushaf_id -> rank) from orderings
def order_to_ranks(order):
    return {sid: i + 1 for i, sid in enumerate(order)}

ibn_abbas_rank = order_to_ranks(ibn_abbas_order)

# -----------------------------------------------------------------------------
# 3. Chronology family
# -----------------------------------------------------------------------------
CHRONOLOGIES_5 = {
    'noldeke_1860':  {'ranks': mushaf_to_noldeke,   'order': noldeke_order},
    'egyptian_1924': {'ranks': mushaf_to_egyptian,  'order': egyptian_order},
    'bell_1937':     {'ranks': BELL_RANK,           'order': bell_order},
    'blachere_1947': {'ranks': BLACHERE_RANK,       'order': blachere_order},
    'ibn_abbas':     {'ranks': ibn_abbas_rank,      'order': ibn_abbas_order},
}

# Weighting-B: 7 slots (Nöldeke, Egyptian, Bell, Blachère, Ibn ʿAbbās, Suyūṭī, Tanzil)
# Suyūṭī and Tanzil are numerically identical to Egyptian. Weighting-B
# effectively triple-weights the Egyptian/Suyūṭī/Tanzil tradition.
CHRONOLOGIES_7 = dict(CHRONOLOGIES_5)
CHRONOLOGIES_7['suyuti_itqan'] = {'ranks': order_to_ranks(suyuti_order), 'order': suyuti_order}
CHRONOLOGIES_7['tanzil']       = {'ranks': order_to_ranks(tanzil_order), 'order': tanzil_order}

# -----------------------------------------------------------------------------
# 4. Borda-count consensus
# -----------------------------------------------------------------------------
def borda_consensus(chronos):
    """chronos: dict name -> {'ranks': {sid: rank}}. Returns ordering list[sid]."""
    borda = {sid: 0 for sid in range(1, 115)}
    for name, d in chronos.items():
        r = d['ranks']
        for sid in range(1, 115):
            borda[sid] += r[sid]
    # Lower borda sum = earlier = better consensus rank
    ordering = sorted(range(1, 115), key=lambda sid: (borda[sid], sid))
    return ordering, borda

consensus_A_order, borda_A = borda_consensus(CHRONOLOGIES_5)
consensus_B_order, borda_B = borda_consensus(CHRONOLOGIES_7)

print(f"\nConsensus-A (5 de-duplicated): first10={consensus_A_order[:10]}",
      file=sys.stderr)
print(f"Consensus-B (7 raw):             first10={consensus_B_order[:10]}",
      file=sys.stderr)

# -----------------------------------------------------------------------------
# 5. Kemeny heuristic (local search from Borda)
# -----------------------------------------------------------------------------
def kendall_tau_distance(order_a, order_b):
    """Number of discordant pairs. Both are permutations of same 114 IDs."""
    rank_a = {sid: i for i, sid in enumerate(order_a)}
    rank_b = {sid: i for i, sid in enumerate(order_b)}
    n = len(order_a)
    ids = sorted(rank_a.keys())
    discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = ids[i], ids[j]
            # pair ordering in a
            oa = 1 if rank_a[a] < rank_a[b] else -1
            ob = 1 if rank_b[a] < rank_b[b] else -1
            if oa != ob:
                discordant += 1
    return discordant


def kendall_tau(order_a, order_b):
    """Normalized Kendall τ in [-1, 1]."""
    n = len(order_a)
    n_pairs = n * (n - 1) // 2
    disc = kendall_tau_distance(order_a, order_b)
    conc = n_pairs - disc
    return (conc - disc) / n_pairs


def total_kemeny_distance(candidate, chronos):
    """Total Kendall-τ distance from candidate ordering to all input chronologies."""
    return sum(kendall_tau_distance(candidate, d['order']) for d in chronos.values())


def kemeny_local_search(init_order, chronos, max_sweeps=3):
    """Adjacent-swap local search from init_order. Returns improved ordering."""
    current = list(init_order)
    current_dist = total_kemeny_distance(current, chronos)
    print(f"  Kemeny init dist = {current_dist}", file=sys.stderr)
    for sweep in range(max_sweeps):
        improved = False
        for i in range(len(current) - 1):
            cand = current[:]
            cand[i], cand[i + 1] = cand[i + 1], cand[i]
            d = total_kemeny_distance(cand, chronos)
            if d < current_dist:
                current = cand
                current_dist = d
                improved = True
        print(f"  Kemeny sweep {sweep+1}: dist={current_dist} improved={improved}",
              file=sys.stderr)
        if not improved:
            break
    return current, current_dist

print("\nKemeny local-search (from Borda, Weighting-A) ...", file=sys.stderr)
kemeny_A_order, kemeny_A_dist = kemeny_local_search(consensus_A_order, CHRONOLOGIES_5)

borda_A_dist = total_kemeny_distance(consensus_A_order, CHRONOLOGIES_5)
print(f"  Borda-A total Kendall-distance = {borda_A_dist}", file=sys.stderr)
print(f"  Kemeny-A total Kendall-distance = {kemeny_A_dist}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. Cell A: Kendall τ vs mushaf
# -----------------------------------------------------------------------------
mushaf_order = list(range(1, 115))

print("\n=== Cell A: Kendall τ vs mushaf ===", file=sys.stderr)
tau_results = {}
for name, d in CHRONOLOGIES_5.items():
    t = kendall_tau(d['order'], mushaf_order)
    tau_results[name] = t
    print(f"  τ({name:18s}, mushaf) = {t:+.4f}", file=sys.stderr)

tau_borda_A = kendall_tau(consensus_A_order, mushaf_order)
tau_borda_B = kendall_tau(consensus_B_order, mushaf_order)
tau_kemeny_A = kendall_tau(kemeny_A_order, mushaf_order)

print(f"  τ(Borda-A consensus,  mushaf) = {tau_borda_A:+.4f}", file=sys.stderr)
print(f"  τ(Borda-B consensus,  mushaf) = {tau_borda_B:+.4f}", file=sys.stderr)
print(f"  τ(Kemeny-A consensus, mushaf) = {tau_kemeny_A:+.4f}", file=sys.stderr)

max_c_tau = max(tau_results.values())
max_c_tau_abs = max(abs(v) for v in tau_results.values())
max_c_tau_name = max(tau_results, key=lambda k: tau_results[k])
print(f"  max_c τ       = {max_c_tau:+.4f}  (at {max_c_tau_name})", file=sys.stderr)
print(f"  max_c |τ|     = {max_c_tau_abs:+.4f}", file=sys.stderr)

# Direction note: all chronologies correlate NEGATIVELY with mushaf (τ < 0).
# "Closer to mushaf" means less-negative (larger τ, closer to 0). Consensus
# "closer" iff τ(consensus, mushaf) > max_c τ(c, mushaf).
cell_A_pass = tau_borda_A > max_c_tau
# Additional framing: |τ| closer to zero = closer to independence
# (not anti-correlated with mushaf).
cell_A_pass_abs = abs(tau_borda_A) < min(abs(v) for v in tau_results.values())

# -----------------------------------------------------------------------------
# 7. Cell B: FR path length
# -----------------------------------------------------------------------------
print("\n=== Cell B: Fisher-Rao path length ===", file=sys.stderr)
L_mushaf = path_length(mushaf_order)
L_per_chrono = {}
for name, d in CHRONOLOGIES_5.items():
    L_per_chrono[name] = path_length(d['order'])
    print(f"  L_{name:18s} = {L_per_chrono[name]:.4f}", file=sys.stderr)

L_borda_A = path_length(consensus_A_order)
L_borda_B = path_length(consensus_B_order)
L_kemeny_A = path_length(kemeny_A_order)
print(f"  L_mushaf              = {L_mushaf:.4f}  (reference)", file=sys.stderr)
print(f"  L_consensus_borda_A   = {L_borda_A:.4f}", file=sys.stderr)
print(f"  L_consensus_borda_B   = {L_borda_B:.4f}", file=sys.stderr)
print(f"  L_consensus_kemeny_A  = {L_kemeny_A:.4f}", file=sys.stderr)

min_c_L = min(L_per_chrono.values())
min_c_L_name = min(L_per_chrono, key=lambda k: L_per_chrono[k])
print(f"  min_c L               = {min_c_L:.4f}  (at {min_c_L_name})", file=sys.stderr)

cell_B_pass_vs_best_chrono = L_borda_A < min_c_L
cell_B_pass_vs_mushaf = L_borda_A < L_mushaf

# -----------------------------------------------------------------------------
# 8. Null: uniform-perm for L (10K perms, seed 20260419) — same as H-NEW-212
# -----------------------------------------------------------------------------
print(f"\nUniform-permutation null: {PERMS} perms, seed {SEED} ...", file=sys.stderr)
rng = random.Random(SEED)
null_L = []
base = list(range(1, 115))
for p in range(PERMS):
    perm = base[:]
    rng.shuffle(perm)
    null_L.append(path_length(perm))
null_mean = statistics.mean(null_L)
null_sd = statistics.stdev(null_L)
print(f"  null mean={null_mean:.4f} sd={null_sd:.4f}", file=sys.stderr)


def p_lower(L):
    n_le = sum(1 for x in null_L if x <= L)
    return (n_le + 1) / (PERMS + 1), n_le


p_borda_A, _ = p_lower(L_borda_A)
z_borda_A = (L_borda_A - null_mean) / null_sd
print(f"  L_consensus_borda_A p_1sided_lower = {p_borda_A:.6f}  z={z_borda_A:+.3f}",
      file=sys.stderr)

# -----------------------------------------------------------------------------
# 9. Cell A null: chronology-rank-shuffle null
# -----------------------------------------------------------------------------
print(f"\nChronology-rank-shuffle null for Cell A: {PERMS} perms ...", file=sys.stderr)
rng = random.Random(SEED)
null_tau = []
chrono_names = list(CHRONOLOGIES_5.keys())
n_chronos = len(chrono_names)
for p in range(PERMS):
    # For each input chronology, shuffle its ranks
    shuffled_chronos = {}
    for name in chrono_names:
        perm_order = base[:]
        rng.shuffle(perm_order)
        shuffled_chronos[name] = {
            'ranks': order_to_ranks(perm_order),
            'order': perm_order,
        }
    shuf_consensus_order, _ = borda_consensus(shuffled_chronos)
    null_tau.append(kendall_tau(shuf_consensus_order, mushaf_order))
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

null_tau_mean = statistics.mean(null_tau)
null_tau_sd = statistics.stdev(null_tau)
null_tau_max = max(null_tau)
null_tau_min = min(null_tau)
print(f"  null τ mean={null_tau_mean:+.4f} sd={null_tau_sd:.4f}", file=sys.stderr)
print(f"  null τ range [{null_tau_min:+.4f}, {null_tau_max:+.4f}]", file=sys.stderr)

# One-sided upper test: is observed τ(consensus,mushaf) larger than null
# (i.e., closer to mushaf than a random-consensus)?
n_ge = sum(1 for x in null_tau if x >= tau_borda_A)
p_tau_upper = (n_ge + 1) / (PERMS + 1)
# Two-sided: is |τ| larger than null?
n_ge_abs = sum(1 for x in null_tau if abs(x) >= abs(tau_borda_A))
p_tau_abs = (n_ge_abs + 1) / (PERMS + 1)
z_tau = (tau_borda_A - null_tau_mean) / null_tau_sd if null_tau_sd > 0 else 0.0
print(f"  p_upper(τ_consensus_A ≥ null_τ) = {p_tau_upper:.6f}", file=sys.stderr)
print(f"  p_twosided(|τ_consensus_A| ≥ |null_τ|) = {p_tau_abs:.6f}", file=sys.stderr)
print(f"  z(τ vs null)  = {z_tau:+.3f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 10. MW-5 negative control: shuffled chronology inputs → consensus should collapse
# -----------------------------------------------------------------------------
print("\nMW-5 negative control (shuffled chronology inputs) ...", file=sys.stderr)
rng = random.Random(SEED + 1)  # independent seed for MW-5
shuffled_chronos = {}
for name in chrono_names:
    perm_order = base[:]
    rng.shuffle(perm_order)
    shuffled_chronos[name] = {
        'ranks': order_to_ranks(perm_order),
        'order': perm_order,
    }
mw5_consensus_order, _ = borda_consensus(shuffled_chronos)
mw5_tau = kendall_tau(mw5_consensus_order, mushaf_order)
mw5_L = path_length(mw5_consensus_order)
print(f"  MW-5 τ(shuffled-consensus, mushaf) = {mw5_tau:+.4f}  "
      f"(expected near 0)", file=sys.stderr)
print(f"  MW-5 L(shuffled-consensus)         = {mw5_L:.4f}  "
      f"(expected near null mean {null_mean:.2f})", file=sys.stderr)

# -----------------------------------------------------------------------------
# 11. Cell C: pairwise Kendall τ matrix (descriptive)
# -----------------------------------------------------------------------------
print("\n=== Cell C: pairwise Kendall τ matrix ===", file=sys.stderr)
all_entities = dict(CHRONOLOGIES_5)  # copies, don't mutate
all_entities['mushaf'] = {'order': mushaf_order, 'ranks': {s: s for s in range(1, 115)}}
all_entities['CONSENSUS_BORDA_A'] = {
    'order': consensus_A_order,
    'ranks': order_to_ranks(consensus_A_order),
}
all_entities['CONSENSUS_BORDA_B'] = {
    'order': consensus_B_order,
    'ranks': order_to_ranks(consensus_B_order),
}
all_entities['CONSENSUS_KEMENY_A'] = {
    'order': kemeny_A_order,
    'ranks': order_to_ranks(kemeny_A_order),
}

tau_matrix = {}
names_all = list(all_entities.keys())
for i, a in enumerate(names_all):
    for j, b in enumerate(names_all):
        if i >= j:
            continue
        t = kendall_tau(all_entities[a]['order'], all_entities[b]['order'])
        tau_matrix[f"{a} vs {b}"] = t

# Print as readable matrix
print(f"  {'':22s} " + " ".join(f"{n[:8]:>9s}" for n in names_all), file=sys.stderr)
for a in names_all:
    row = [f"  {a:22s}"]
    for b in names_all:
        if a == b:
            row.append(f"{'1.000':>9s}")
        else:
            key = f"{a} vs {b}" if names_all.index(a) < names_all.index(b) else f"{b} vs {a}"
            row.append(f"{tau_matrix[key]:>+9.3f}")
    print(" ".join(row), file=sys.stderr)

# Identify clusters: Nöldeke/Egyptian/Suyūṭī cluster, Ibn ʿAbbās outlier?
# In Weighting-A, Suyūṭī/Tanzil collapsed into egyptian_1924.
# Check clustering among (noldeke, egyptian, bell, blachere, ibn_abbas)
print("\nChronology-to-chronology Kendall τ (in Weighting-A family):",
      file=sys.stderr)
chrono_pair_taus = {}
for i, a in enumerate(chrono_names):
    for j, b in enumerate(chrono_names):
        if i >= j:
            continue
        t = kendall_tau(CHRONOLOGIES_5[a]['order'], CHRONOLOGIES_5[b]['order'])
        chrono_pair_taus[f"{a} vs {b}"] = t
        print(f"  τ({a:18s}, {b:18s}) = {t:+.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 12. Spearman ρ for completeness (mirrors h-new-212 output style)
# -----------------------------------------------------------------------------
def spearman(ranks_a, ranks_b):
    sids = sorted(ranks_a.keys())
    a = [ranks_a[s] for s in sids]
    b = [ranks_b[s] for s in sids]
    n = len(sids)
    mean_a = sum(a) / n
    mean_b = sum(b) / n
    num = sum((a[i] - mean_a) * (b[i] - mean_b) for i in range(n))
    da = math.sqrt(sum((a[i] - mean_a) ** 2 for i in range(n)))
    db = math.sqrt(sum((b[i] - mean_b) ** 2 for i in range(n)))
    return num / (da * db) if da * db > 0 else 0.0

print("\nSpearman ρ consensus vs mushaf / each chronology:", file=sys.stderr)
consensus_A_ranks = order_to_ranks(consensus_A_order)
rho_consA_mushaf = spearman(consensus_A_ranks, {s: s for s in range(1, 115)})
print(f"  ρ(Borda-A consensus, mushaf) = {rho_consA_mushaf:+.4f}", file=sys.stderr)
for name, d in CHRONOLOGIES_5.items():
    r = spearman(consensus_A_ranks, d['ranks'])
    print(f"  ρ(Borda-A consensus, {name:18s}) = {r:+.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 13. Write JSON
# -----------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-245',
    'title': 'Cross-chronology consensus ordering (Borda + Kemeny)',
    'parent': 'h-new-222',
    'pre_reg_sha256': prereg_sha,
    'h_new_111_source_sha256': h111_sha,
    'h_new_222_source_sha256': h222_sha,
    'seed': SEED,
    'permutations': PERMS,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'rules_tuple': ('(no-tashkeel, QAC-STEM root tokens, QAC v0.4, '
                    'basmala-counted-only-in-surah-1, Hafs-Kufan, '
                    'Borda-count primary, Kemeny local-search secondary, '
                    'D-inherited-from-H-NEW-111)'),
    'chronology_inputs_A': list(CHRONOLOGIES_5.keys()),
    'chronology_inputs_B': list(CHRONOLOGIES_7.keys()),
    'consensus_borda_A_first20': consensus_A_order[:20],
    'consensus_borda_A_last20': consensus_A_order[-20:],
    'consensus_borda_A_full': consensus_A_order,
    'consensus_borda_B_first20': consensus_B_order[:20],
    'consensus_borda_B_full': consensus_B_order,
    'consensus_kemeny_A_first20': kemeny_A_order[:20],
    'consensus_kemeny_A_full': kemeny_A_order,
    'borda_A_total_kendall_dist': borda_A_dist,
    'kemeny_A_total_kendall_dist': kemeny_A_dist,
    'cell_A': {
        'tau_consensus_borda_A_vs_mushaf': tau_borda_A,
        'tau_consensus_borda_B_vs_mushaf': tau_borda_B,
        'tau_consensus_kemeny_A_vs_mushaf': tau_kemeny_A,
        'tau_per_chronology_vs_mushaf': tau_results,
        'max_c_tau': max_c_tau,
        'max_c_tau_name': max_c_tau_name,
        'cell_A_pass_strict': cell_A_pass,
        'cell_A_pass_by_abs_closer_to_zero': cell_A_pass_abs,
        'null_tau_mean': null_tau_mean,
        'null_tau_sd': null_tau_sd,
        'null_tau_min': null_tau_min,
        'null_tau_max': null_tau_max,
        'p_upper_tau_vs_chronology_shuffle_null': p_tau_upper,
        'p_twosided_abs_tau_vs_null': p_tau_abs,
        'z_tau_vs_null': z_tau,
        'interpretation': (
            'All 5 chronologies have NEGATIVE Kendall τ with mushaf (known; '
            'see h-new-212 Spearman ρ). A "closer-to-mushaf" consensus means '
            'τ(consensus, mushaf) > max_c τ(c, mushaf) i.e. less negative.'),
    },
    'cell_B': {
        'L_mushaf': L_mushaf,
        'L_consensus_borda_A': L_borda_A,
        'L_consensus_borda_B': L_borda_B,
        'L_consensus_kemeny_A': L_kemeny_A,
        'L_per_chronology': L_per_chrono,
        'min_c_L': min_c_L,
        'min_c_L_name': min_c_L_name,
        'cell_B_pass_vs_best_chronology': cell_B_pass_vs_best_chrono,
        'cell_B_pass_vs_mushaf': cell_B_pass_vs_mushaf,
        'null_mean_L': null_mean,
        'null_sd_L': null_sd,
        'p_lower_L_consensus_borda_A': p_borda_A,
        'z_L_consensus_borda_A': z_borda_A,
    },
    'cell_C': {
        'pairwise_kendall_tau_matrix': tau_matrix,
        'chronology_pair_taus': chrono_pair_taus,
    },
    'MW5_negative_control': {
        'tau_shuffled_consensus_mushaf': mw5_tau,
        'L_shuffled_consensus': mw5_L,
        'tau_expected_near_0': True,
        'L_expected_near_null_mean': True,
        'tau_passes_MW5': abs(mw5_tau) < 0.15,
        'L_passes_MW5': abs(mw5_L - null_mean) < 3 * null_sd,
    },
    'spearman_consensus_borda_A': {
        'vs_mushaf': rho_consA_mushaf,
        'vs_chronologies': {
            name: spearman(consensus_A_ranks, d['ranks'])
            for name, d in CHRONOLOGIES_5.items()
        },
    },
    'verdict_primary': {
        'cell_A_pass': cell_A_pass,
        'cell_B_pass_vs_best_chrono': cell_B_pass_vs_best_chrono,
        'cell_B_pass_vs_mushaf': cell_B_pass_vs_mushaf,
        'both_pass': cell_A_pass and cell_B_pass_vs_best_chrono,
        'interpretation': (
            'PASS-BOTH → moderated-tawqīfī (Ibn Taymiyya); '
            'FAIL-BOTH → uniquely-tawqīfī (mushaf not a chronology blend); '
            'MIXED → split verdict reported honestly.'),
    },
}
summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 14. Final summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-245 SUMMARY", file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  Cell A: τ(Borda-A, mushaf)={tau_borda_A:+.4f}  vs "
      f"max_c τ={max_c_tau:+.4f} ({max_c_tau_name})", file=sys.stderr)
print(f"          PASS (closer-to-mushaf)? {cell_A_pass}", file=sys.stderr)
print(f"  Cell B: L(Borda-A)={L_borda_A:.4f}  vs "
      f"min_c L={min_c_L:.4f} ({min_c_L_name})  "
      f"vs L_mushaf={L_mushaf:.4f}", file=sys.stderr)
print(f"          PASS vs best chrono? {cell_B_pass_vs_best_chrono}  "
      f"PASS vs mushaf? {cell_B_pass_vs_mushaf}", file=sys.stderr)
print(f"  MW-5:   τ_shuf_consensus={mw5_tau:+.4f}  "
      f"L_shuf_consensus={mw5_L:.4f} (null mean {null_mean:.2f})",
      file=sys.stderr)
print("=" * 72, file=sys.stderr)
