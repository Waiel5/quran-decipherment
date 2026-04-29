#!/usr/bin/env python3
"""H-NEW-155 — Q 1 al-Fātiḥa sui-generis-liturgical classification.

Cell A: Q 1 dispersion vs random 7-verse-window null.
Cell B: Q 1 dispersion vs Q 2:1-7 and Q 112+113:1-2 dispersion.
MW-5: Q 12 (Yūsuf) should show LOW dispersion.

Seed 20260417. 10K perms.
"""
import hashlib, json, random, re, statistics, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_NULL = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-155-q1-sui-generis-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-155.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

# Parse QAC: per-verse STEM roots + per-surah total verses
verse_roots = defaultdict(lambda: defaultdict(set))
root_appears_in_surah = defaultdict(set)  # root -> set of surah ids
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip(): continue
        p = line.rstrip().split('\t')
        if len(p) < 4: continue
        m = LOC_RE.match(p[0])
        if not m: continue
        sid, vid = int(m.group(1)), int(m.group(2))
        if 'STEM' not in p[3]: continue
        rm = ROOT_RE.search(p[3])
        if not rm: continue
        root = rm.group(1)
        verse_roots[sid][vid].add(root)
        root_appears_in_surah[root].add(sid)

# All (sid, vid) pairs with ≥1 STEM root (for random-window sampling)
all_verses = [(s, v) for s in verse_roots for v in verse_roots[s]]
print(f"Total verses with ≥1 STEM root: {len(all_verses)}", file=sys.stderr)

def dispersion_of_root_set(root_set):
    """Average fraction-of-114-surahs-containing across roots in the set."""
    if not root_set:
        return 0.0
    return statistics.mean(len(root_appears_in_surah[r]) / 114 for r in root_set)

def roots_of_verse_set(verse_list):
    """Union of STEM roots across (sid, vid) list."""
    s = set()
    for sid, vid in verse_list:
        s.update(verse_roots[sid].get(vid, set()))
    return s

# ---------------------------------------------------------------------------
# Q 1 stats
# ---------------------------------------------------------------------------
q1_verses = [(1, v) for v in range(1, 8)]
q1_roots = roots_of_verse_set(q1_verses)
q1_disp = dispersion_of_root_set(q1_roots)
print(f"Q 1 distinct STEM roots: {len(q1_roots)} — {sorted(q1_roots)}", file=sys.stderr)
print(f"Q 1 dispersion (avg fraction-of-114-surahs-containing): {q1_disp:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell A: null = random 7-verse windows
# ---------------------------------------------------------------------------
rng = random.Random(SEED)
null_disps_A = []
for _ in range(N_NULL):
    sample = rng.sample(all_verses, 7)
    r_set = roots_of_verse_set(sample)
    null_disps_A.append(dispersion_of_root_set(r_set))

p_A = sum(1 for d in null_disps_A if d >= q1_disp) / N_NULL
print(f"\nCell A: Q 1 dispersion = {q1_disp:.4f}", file=sys.stderr)
print(f"  null mean = {statistics.mean(null_disps_A):.4f}, SD = {statistics.stdev(null_disps_A):.4f}", file=sys.stderr)
print(f"  null 95th percentile = {sorted(null_disps_A)[int(0.95*N_NULL)]:.4f}", file=sys.stderr)
print(f"  p_A = {p_A:.4f}", file=sys.stderr)

cell_A_pass = p_A < 0.025
print(f"  Cell A: {'PASS' if cell_A_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Cell B: Q 2:1-7 and Q 112+113:1-2 comparison
# ---------------------------------------------------------------------------
q2_verses = [(2, v) for v in range(1, 8)]
q2_roots = roots_of_verse_set(q2_verses)
q2_disp = dispersion_of_root_set(q2_roots)

# Q 112 has 4 verses; pad with Q 113:1-3 for 7-verse match
q112_113_verses = [(112, v) for v in range(1, 5)] + [(113, v) for v in range(1, 4)]
q112_113_roots = roots_of_verse_set(q112_113_verses)
q112_113_disp = dispersion_of_root_set(q112_113_roots)

print(f"\nCell B comparison:", file=sys.stderr)
print(f"  Q 1 (7 verses, {len(q1_roots)} roots): dispersion = {q1_disp:.4f}", file=sys.stderr)
print(f"  Q 2:1-7 (7 verses, {len(q2_roots)} roots): dispersion = {q2_disp:.4f}", file=sys.stderr)
print(f"  Q 112+113:1-3 (7 verses, {len(q112_113_roots)} roots): dispersion = {q112_113_disp:.4f}", file=sys.stderr)

cell_B_pass = q1_disp > q2_disp and q1_disp > q112_113_disp

# For inferential claim: permutation p from Cell A's 10K null
# Q 2 and Q 112 are themselves SPECIFIC samples; if Q 1 is higher than both
# AND higher than 97.5% of random null, compound evidence is strong.
n_above_q1 = sum(1 for d in null_disps_A if d >= q1_disp)
n_above_q2 = sum(1 for d in null_disps_A if d >= q2_disp)
n_above_q112 = sum(1 for d in null_disps_A if d >= q112_113_disp)
print(f"  Null samples ≥ Q 1 disp: {n_above_q1}/{N_NULL} = {n_above_q1/N_NULL:.4f}", file=sys.stderr)
print(f"  Null samples ≥ Q 2 disp: {n_above_q2}/{N_NULL} = {n_above_q2/N_NULL:.4f}", file=sys.stderr)
print(f"  Null samples ≥ Q 112 disp: {n_above_q112}/{N_NULL} = {n_above_q112/N_NULL:.4f}", file=sys.stderr)

# Cell B pass condition (per pre-reg): Q 1 > Q 2 AND Q 1 > Q 112 AND p < 0.025
# Use p from Cell A (random 7-window null) for the significance of Q 1 being high
cell_B_pass_strict = cell_B_pass and (p_A < 0.025)
print(f"  Cell B {'PASS' if cell_B_pass_strict else 'FAIL'} "
      f"(Q 1 > Q 2 AND Q 1 > Q 112 AND random-window p < 0.025)", file=sys.stderr)

# ---------------------------------------------------------------------------
# MW-5: Q 12 should show LOWER dispersion (concentrated vocabulary)
# ---------------------------------------------------------------------------
q12_all_verses = [(12, v) for v in verse_roots[12]]
q12_all_roots = roots_of_verse_set(q12_all_verses)
q12_all_disp = dispersion_of_root_set(q12_all_roots)
# Size-matched random null for Q 12 length
null_disps_mw5 = []
n_verses_q12 = len(q12_all_verses)
for _ in range(1000):  # fewer perms for MW-5
    sample = rng.sample(all_verses, n_verses_q12)
    null_disps_mw5.append(dispersion_of_root_set(roots_of_verse_set(sample)))
q12_percentile = sum(1 for d in null_disps_mw5 if d <= q12_all_disp) / len(null_disps_mw5)
print(f"\nMW-5 Q 12 (size-matched {n_verses_q12} verses): dispersion = {q12_all_disp:.4f}", file=sys.stderr)
print(f"  null mean = {statistics.mean(null_disps_mw5):.4f}", file=sys.stderr)
print(f"  Q 12 percentile (lower = more concentrated): {q12_percentile:.4f}", file=sys.stderr)
mw5_pass = q12_percentile < 0.3  # Q 12 should be LESS dispersed than average
print(f"  MW-5 Q 12 LOW-dispersion: {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Final verdict
# ---------------------------------------------------------------------------
if not mw5_pass:
    final = "INSTRUMENT-BROKEN — Q 12 known-concentrated does not show low dispersion; pipeline suspect"
elif cell_A_pass and cell_B_pass_strict:
    final = "SUI-GENERIS-CONFIRMED — Q 1 is empirically distinct as high-dispersion liturgical-central surah"
elif cell_A_pass and not cell_B_pass:
    final = "HIGH-DISPERSION-ONLY — Q 1 dispersed but not distinctively more than hub-liturgical"
elif not cell_A_pass and cell_B_pass:
    final = "DIFFERENTIAL — Q 1 distinctive relative to Q 2/112 but not vs random"
else:
    final = "NULL — sui-generis hypothesis not supported on dispersion axis"

print(f"\n" + "=" * 70, file=sys.stderr)
print(f"Q 1 dispersion = {q1_disp:.4f}", file=sys.stderr)
print(f"Cell A (vs random 7-verse null): p={p_A:.4f} → {'PASS' if cell_A_pass else 'FAIL'}", file=sys.stderr)
print(f"Cell B (vs Q 2/Q 112): Q 1 > Q 2 ({q1_disp:.3f} > {q2_disp:.3f}): "
      f"{q1_disp > q2_disp}; Q 1 > Q 112 ({q1_disp:.3f} > {q112_113_disp:.3f}): "
      f"{q1_disp > q112_113_disp}", file=sys.stderr)
print(f"MW-5 Q 12: {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)
print(f"FINAL: {final}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

summary = {
    'finding_id': 'h-new-155',
    'title': 'Q 1 al-Fātiḥa sui-generis-liturgical classification',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 2, 'alpha_bon': 0.025, 'family': 'h-new-155-q1-sui-generis'},
    'q1_roots': sorted(q1_roots),
    'q1_n_roots': len(q1_roots),
    'q1_dispersion': q1_disp,
    'cell_A': {
        'null_n': N_NULL,
        'null_mean': statistics.mean(null_disps_A),
        'null_sd': statistics.stdev(null_disps_A),
        'null_95th': sorted(null_disps_A)[int(0.95*N_NULL)],
        'p_one_sided_upper': p_A,
        'threshold_alpha_bon': 0.025,
        'pass': cell_A_pass,
    },
    'cell_B': {
        'q1_dispersion': q1_disp,
        'q2_1_7_dispersion': q2_disp,
        'q112_113_1_3_dispersion': q112_113_disp,
        'q1_gt_q2': q1_disp > q2_disp,
        'q1_gt_q112': q1_disp > q112_113_disp,
        'pass_strict': cell_B_pass_strict,
    },
    'mw5_q12_control': {
        'q12_n_verses': n_verses_q12,
        'q12_dispersion': q12_all_disp,
        'percentile_in_null_lower': q12_percentile,
        'pass': mw5_pass,
    },
    'final_verdict': final,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
