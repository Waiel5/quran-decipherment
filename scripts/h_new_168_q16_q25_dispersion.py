#!/usr/bin/env python3
"""H-NEW-168 — Q 16-25 isolate-core dispersion investigation.

Uses QAC-STEM roots (same as H-NEW-155). Builds per-surah dispersion;
tests whether Q 16-25 window mean-dispersion is below-median vs
contiguous-window null (Cell A) + permutation null (Cell B) + computes
pairwise Jaccard overlap within Q 16-25 (Cell C).

Seed 20260419.
"""
import hashlib, itertools, json, random, re, statistics, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
N_PERM = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-168-q16-q25-dispersion-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-168.json'
OUT_CSV = ROOT / 'findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

# ---------------------------------------------------------------------------
# Parse QAC: per-surah STEM roots
# ---------------------------------------------------------------------------
surah_roots = defaultdict(set)  # sid -> set of roots
root_appears_in_surah = defaultdict(set)  # root -> set of sids

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
        sid = int(m.group(1))
        if 'STEM' not in p[3]:
            continue
        rm = ROOT_RE.search(p[3])
        if not rm:
            continue
        root = rm.group(1)
        surah_roots[sid].add(root)
        root_appears_in_surah[root].add(sid)

N_SURAHS = 114
assert len(surah_roots) == N_SURAHS, f"Expected 114 surahs, got {len(surah_roots)}"

def dispersion_of_surah(sid):
    """Mean fraction-of-114-surahs-containing across stems in this surah."""
    roots = surah_roots[sid]
    if not roots:
        return 0.0
    return statistics.mean(len(root_appears_in_surah[r]) / N_SURAHS for r in roots)

# ---------------------------------------------------------------------------
# Per-surah dispersion + ranking
# ---------------------------------------------------------------------------
per_surah = []
for sid in range(1, 115):
    d = dispersion_of_surah(sid)
    per_surah.append((sid, d, len(surah_roots[sid])))

# Rank: higher dispersion = rank 1 (most-template)
ranked = sorted(per_surah, key=lambda x: -x[1])
sid_to_rank = {sid: i + 1 for i, (sid, _, _) in enumerate(ranked)}
sid_to_disp = {sid: d for sid, d, _ in per_surah}
sid_to_nstems = {sid: n for sid, _, n in per_surah}

# Write CSV
with open(OUT_CSV, 'w', encoding='utf-8') as f:
    f.write("sid,rank_by_dispersion,dispersion,n_stem_roots\n")
    for sid in range(1, 115):
        f.write(f"{sid},{sid_to_rank[sid]},{sid_to_disp[sid]:.6f},{sid_to_nstems[sid]}\n")

corpus_median = statistics.median(sid_to_disp.values())
corpus_mean = statistics.mean(sid_to_disp.values())
corpus_sd = statistics.stdev(sid_to_disp.values())
print(f"\nCorpus dispersion: mean={corpus_mean:.4f} median={corpus_median:.4f} SD={corpus_sd:.4f}", file=sys.stderr)

# Q 16-25
zone = list(range(16, 26))
zone_disps = [sid_to_disp[s] for s in zone]
zone_ranks = [sid_to_rank[s] for s in zone]
zone_mean_disp = statistics.mean(zone_disps)
zone_mean_rank = statistics.mean(zone_ranks)

print(f"\nQ 16-25 per-surah:", file=sys.stderr)
for s in zone:
    print(f"  Q {s:3d}: disp={sid_to_disp[s]:.4f}  rank={sid_to_rank[s]:3d}/114  n_stems={sid_to_nstems[s]}", file=sys.stderr)
print(f"Q 16-25 window-mean-dispersion: {zone_mean_disp:.4f}", file=sys.stderr)
print(f"Q 16-25 mean-rank: {zone_mean_rank:.1f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# MW-5 controls
# ---------------------------------------------------------------------------
q1_rank = sid_to_rank[1]
q2_rank = sid_to_rank[2]
mw5a_pass = q1_rank <= 12  # top-decile (12 of 114 ≈ 10.5%)
mw5b_pass = q2_rank >= 103  # bottom-decile
print(f"\nMW-5a (Q 1 template-mode): Q 1 rank = {q1_rank}/114, "
      f"disp = {sid_to_disp[1]:.4f}  {'PASS' if mw5a_pass else 'FAIL'}", file=sys.stderr)
print(f"MW-5b (Q 2 concentrator-mode): Q 2 rank = {q2_rank}/114, "
      f"disp = {sid_to_disp[2]:.4f}  {'PASS' if mw5b_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell A: contiguous 10-surah window null
# ---------------------------------------------------------------------------
windows = []
for start in range(1, 115 - 10 + 1):  # 105 windows starting 1..105
    sids = list(range(start, start + 10))
    mean_d = statistics.mean(sid_to_disp[s] for s in sids)
    windows.append((start, mean_d))

# Rank Q 16-25 (start=16) against the 105 windows
target_start = 16
target_mean = next(m for st, m in windows if st == target_start)
assert abs(target_mean - zone_mean_disp) < 1e-9

# One-sided lower-tail: fraction of windows with mean_d ≤ zone_mean_disp
n_below = sum(1 for st, m in windows if m <= target_mean)
p_A = n_below / len(windows)
# Rank-position of target in sorted ascending order
sorted_means = sorted(m for _, m in windows)
target_rank_contig = sorted_means.index(target_mean) + 1  # 1-indexed ascending
print(f"\nCell A (contiguous-window null, 105 windows):", file=sys.stderr)
print(f"  Q 16-25 mean = {target_mean:.4f}", file=sys.stderr)
print(f"  Rank (ascending, lower=more concentrator): {target_rank_contig}/105", file=sys.stderr)
print(f"  p_one_sided_lower = {p_A:.4f}  {'PASS' if p_A < 0.05 else 'FAIL'} (α=0.05)", file=sys.stderr)

# Report all windows for context
print(f"  Window-null stats: min={min(m for _,m in windows):.4f} "
      f"max={max(m for _,m in windows):.4f} "
      f"median={statistics.median(m for _,m in windows):.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell B: 10000-permutation random 10-surah null
# ---------------------------------------------------------------------------
rng = random.Random(SEED)
all_sids = list(range(1, 115))
perm_means = []
for _ in range(N_PERM):
    sample = rng.sample(all_sids, 10)
    perm_means.append(statistics.mean(sid_to_disp[s] for s in sample))

n_below_perm = sum(1 for m in perm_means if m <= zone_mean_disp)
p_B = n_below_perm / N_PERM
perm_mean = statistics.mean(perm_means)
perm_sd = statistics.stdev(perm_means)
print(f"\nCell B (permutation null, n={N_PERM}):", file=sys.stderr)
print(f"  null mean={perm_mean:.4f} SD={perm_sd:.4f}", file=sys.stderr)
print(f"  Q 16-25 mean = {zone_mean_disp:.4f}", file=sys.stderr)
print(f"  p_one_sided_lower = {p_B:.4f}  {'PASS' if p_B < 0.05 else 'FAIL'} (α=0.05)", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell C: pairwise Jaccard overlap within Q 16-25
# ---------------------------------------------------------------------------
def jaccard(a, b):
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0

zone_pairs = list(itertools.combinations(zone, 2))
zone_jaccards = [jaccard(surah_roots[a], surah_roots[b]) for a, b in zone_pairs]
zone_mean_jac = statistics.mean(zone_jaccards)
zone_median_jac = statistics.median(zone_jaccards)

# Null for Jaccard: random 10-surah samples, compute mean pairwise Jaccard
rng2 = random.Random(SEED + 1)
null_jac_means = []
for _ in range(N_PERM):
    sample = rng2.sample(all_sids, 10)
    pairs = list(itertools.combinations(sample, 2))
    jacs = [jaccard(surah_roots[a], surah_roots[b]) for a, b in pairs]
    null_jac_means.append(statistics.mean(jacs))

# Two-sided comparison: is zone Jaccard higher (shared-content) or lower (diverse-content)?
n_above_jac = sum(1 for m in null_jac_means if m >= zone_mean_jac)
p_C_above = n_above_jac / N_PERM  # low = zone is ABOVE null (high-shared-content)
p_C_below = 1 - p_C_above

null_jac_mean = statistics.mean(null_jac_means)
null_jac_sd = statistics.stdev(null_jac_means)

print(f"\nCell C (internal Jaccard overlap):", file=sys.stderr)
print(f"  Q 16-25 pairwise mean Jaccard = {zone_mean_jac:.4f} (median {zone_median_jac:.4f})", file=sys.stderr)
print(f"  null random-10 mean Jaccard = {null_jac_mean:.4f} SD={null_jac_sd:.4f}", file=sys.stderr)
print(f"  p(zone ≥ null, shared-content) = {p_C_above:.4f}", file=sys.stderr)
print(f"  p(zone ≤ null, diverse-content) = {p_C_below:.4f}", file=sys.stderr)

# Show top-5 and bottom-5 pairs for qualitative
sorted_pairs = sorted(zip(zone_pairs, zone_jaccards), key=lambda x: -x[1])
print("  Top-5 most-similar pairs:", file=sys.stderr)
for (a, b), j in sorted_pairs[:5]:
    print(f"    Q{a:3d}-Q{b:3d}: Jaccard={j:.4f}", file=sys.stderr)
print("  Bottom-5 least-similar pairs:", file=sys.stderr)
for (a, b), j in sorted_pairs[-5:]:
    print(f"    Q{a:3d}-Q{b:3d}: Jaccard={j:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------
cell_A_pass = p_A < 0.05
cell_B_pass = p_B < 0.05

if not (mw5a_pass and mw5b_pass):
    verdict = "INSTRUMENT-BROKEN — MW-5 controls failed; pipeline suspect"
elif cell_A_pass and cell_B_pass:
    if p_C_above < 0.05:
        verdict = "CONFIRMED-CONCENTRATOR-INTERNALLY-SIMILAR — Q 16-25 below-median dispersion AND pairs share more than null"
    elif p_C_below < 0.05:
        verdict = "CONFIRMED-CONCENTRATOR-INTERNALLY-DIVERSE — Q 16-25 below-median dispersion; each surah is its own concentrator"
    else:
        verdict = "CONFIRMED-CONCENTRATOR-MIXED — Q 16-25 concentrator-mode; internal overlap indistinguishable from null"
elif cell_A_pass and not cell_B_pass:
    verdict = "WEAK-CONCENTRATOR — contiguous-window only; permutation null not passed"
elif not cell_A_pass and cell_B_pass:
    verdict = "ROBUSTNESS-PARTIAL — permutation only; positional-neighbor artifact"
elif not cell_A_pass and not cell_B_pass:
    # Check reverse direction
    p_A_above = 1 - p_A + 1.0/len(windows)  # approx upper-tail
    if zone_mean_disp > corpus_median:
        verdict = f"REFUTES-CONCENTRATOR — Q 16-25 IS ABOVE-MEDIAN (template-like); isolate-core is NOT dispersion-mode phenomenon"
    else:
        verdict = "NULL — Q 16-25 indistinguishable from null on dispersion axis"
else:
    verdict = "UNDEFINED"

print(f"\n{'='*70}", file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)
print(f"{'='*70}", file=sys.stderr)

# ---------------------------------------------------------------------------
# JSON summary
# ---------------------------------------------------------------------------
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
summary = {
    'finding_id': 'h-new-168',
    'title': 'Q 16-25 isolate-core on H-NEW-163 dispersion axis — TEMPLATE vs CONCENTRATOR',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 1, 'alpha_bon': 0.05, 'family': 'h-new-168-isolate-core-dispersion'},
    'corpus': {'mean_dispersion': corpus_mean, 'median_dispersion': corpus_median, 'sd': corpus_sd},
    'per_surah_q16_q25': {
        s: {'dispersion': sid_to_disp[s], 'rank': sid_to_rank[s], 'n_stems': sid_to_nstems[s]}
        for s in zone
    },
    'zone_summary': {
        'window_mean_dispersion': zone_mean_disp,
        'window_mean_rank': zone_mean_rank,
    },
    'mw5': {
        'q1_rank': q1_rank, 'q1_dispersion': sid_to_disp[1], 'mw5a_pass': mw5a_pass,
        'q2_rank': q2_rank, 'q2_dispersion': sid_to_disp[2], 'mw5b_pass': mw5b_pass,
    },
    'cell_A_contiguous_null': {
        'n_windows': len(windows),
        'q16_q25_rank_ascending': target_rank_contig,
        'p_one_sided_lower': p_A,
        'pass': cell_A_pass,
    },
    'cell_B_permutation_null': {
        'n_perm': N_PERM,
        'null_mean': perm_mean,
        'null_sd': perm_sd,
        'p_one_sided_lower': p_B,
        'pass': cell_B_pass,
    },
    'cell_C_internal_overlap': {
        'n_pairs': len(zone_pairs),
        'zone_mean_jaccard': zone_mean_jac,
        'zone_median_jaccard': zone_median_jac,
        'null_jaccard_mean': null_jac_mean,
        'null_jaccard_sd': null_jac_sd,
        'p_zone_above_null': p_C_above,
        'p_zone_below_null': p_C_below,
        'top_pair': {'pair': list(sorted_pairs[0][0]), 'jaccard': sorted_pairs[0][1]},
        'bottom_pair': {'pair': list(sorted_pairs[-1][0]), 'jaccard': sorted_pairs[-1][1]},
    },
    'verdict': verdict,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
print(f"Wrote: {OUT_CSV}", file=sys.stderr)
