#!/usr/bin/env python3
"""H-NEW-150 — Liturgical prominence ↔ cluster-network hub-degree.

Pre-registered tests (Bonferroni k=2, α_bon=0.025):
  Primary: Spearman ρ(LITURGICAL_SCORE, cluster_degree) ≥ 0.3, p_perm < 0.025
  Secondary: length-residualized Spearman ρ ≥ 0.2, p_perm < 0.025
  MW-5 control: chronology-rank correlation (should be weaker than liturgical)

Scores LOCKED in pre-reg (see h-new-150-liturgical-hub-prereg.md).
Seed 20260417. 10,000 permutations.
"""
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path
from scipy.stats import spearmanr
import csv

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 10000

QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
CF010_JSON = ROOT / 'findings/phase-b-hypotheses/csv/cross-finding-010.json'
CHRONO_CSV = ROOT / 'data/revelation-order.csv'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-150-liturgical-hub-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-150.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Pre-locked liturgical-prominence scores (from pre-reg)
# ---------------------------------------------------------------------------
LITURGICAL_SCORES = {
    1:   17,  # al-Fatiha: every prayer cycle
    2:   8,   # al-Baqara: last 2 verses nightly + Ayat al-Kursi
    3:   4,   # Al Imran: al-Zahrawan pair with Q 2
    18:  4,   # al-Kahf: Friday (hadith Abu Dawud 1074)
    24:  3,   # al-Nur: Ayat al-Nur common
    32:  3,   # al-Sajda: Fajr Friday
    36:  4,   # Ya-Sin: Friday eve / dying
    40:  1,
    50:  3,   # al-Qaf: Friday/Eid (Sahih Muslim 878)
    55:  2,
    56:  2,
    57:  1,
    59:  3,   # al-Hashr last 3 verses
    62:  3,   # al-Jumu'a: Friday
    63:  3,   # al-Munafiqun: Friday
    67:  3,   # al-Mulk: nightly
    73:  1,
    76:  2,   # al-Insan: Fajr Friday
    87:  2,   # al-A'la: Friday + Eid
    88:  2,   # al-Ghashiya: Friday + Eid
    94:  1,
    97:  1,   # al-Qadr
    109: 1,
    110: 1,
    112: 4,   # al-Ikhlas: 1/3-Quran + morning/evening
    113: 3,   # al-Falaq
    114: 3,   # al-Nas
}
# Fill in zeros for all other surahs
for s in range(1, 115):
    LITURGICAL_SCORES.setdefault(s, 0)

print(f"Liturgical scores locked; nonzero surahs: "
      f"{sorted(s for s, v in LITURGICAL_SCORES.items() if v > 0)}", file=sys.stderr)
print(f"Max score: {max(LITURGICAL_SCORES.values())} (Q 1)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Cluster-network degrees from cross-finding-010
# ---------------------------------------------------------------------------
cf010 = json.loads(CF010_JSON.read_text())
per_surah_degree = {int(k): v for k, v in cf010['product_A_degree_distribution']['per_surah_degree'].items()}
print(f"cluster-network degrees loaded for {len(per_surah_degree)} surahs", file=sys.stderr)
print(f"degree range: [{min(per_surah_degree.values())}, {max(per_surah_degree.values())}]", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Surah metadata (length, chronology)
# ---------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text())
surah_nverses = {s['id']: len(s['verses']) for s in quran}

chronology = {}
with open(CHRONO_CSV, encoding='utf-8') as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        chronology[int(row['mushaf_order'])] = int(row['noldeke_order'])

# ---------------------------------------------------------------------------
# 4. Primary: Spearman ρ + permutation null
# ---------------------------------------------------------------------------
surahs = sorted(range(1, 115))
x_liturgical = [LITURGICAL_SCORES[s] for s in surahs]
y_degree = [per_surah_degree[s] for s in surahs]

rho_primary, p_nominal = spearmanr(x_liturgical, y_degree)
print(f"\nPrimary: Spearman ρ(liturgical, degree) = {rho_primary:.4f}", file=sys.stderr)
print(f"  SciPy nominal p (2-sided) = {p_nominal:.6f}", file=sys.stderr)

# Permutation null
rng = random.Random(SEED)
null_rhos = []
for _ in range(N_PERMS):
    shuffled = x_liturgical[:]
    rng.shuffle(shuffled)
    r, _ = spearmanr(shuffled, y_degree)
    null_rhos.append(r)

p_perm_one_sided = sum(1 for r in null_rhos if r >= rho_primary) / N_PERMS
print(f"  Permutation 1-sided upper p = {p_perm_one_sided:.6f}", file=sys.stderr)

primary_pass = rho_primary >= 0.3 and p_perm_one_sided < 0.025
print(f"  Primary: {'PASS' if primary_pass else 'FAIL'} "
      f"(threshold: ρ ≥ 0.3, p < 0.025)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Secondary: length-residualized
# ---------------------------------------------------------------------------
log_nverses = [math.log(surah_nverses[s]) for s in surahs]

def linregress_residuals(y, x):
    """Return residuals of y after regressing on x (OLS, simple linear)."""
    n = len(y)
    mx = sum(x) / n
    my = sum(y) / n
    var_x = sum((xi - mx) ** 2 for xi in x) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
    slope = cov / var_x if var_x > 0 else 0.0
    intercept = my - slope * mx
    return [y[i] - (slope * x[i] + intercept) for i in range(n)]

resid_liturgical = linregress_residuals(x_liturgical, log_nverses)
resid_degree = linregress_residuals(y_degree, log_nverses)

rho_secondary, _ = spearmanr(resid_liturgical, resid_degree)
print(f"\nSecondary: length-residualized Spearman ρ = {rho_secondary:.4f}", file=sys.stderr)

null_rhos_sec = []
for _ in range(N_PERMS):
    shuffled = resid_liturgical[:]
    rng.shuffle(shuffled)
    r, _ = spearmanr(shuffled, resid_degree)
    null_rhos_sec.append(r)
p_perm_sec = sum(1 for r in null_rhos_sec if r >= rho_secondary) / N_PERMS
print(f"  Permutation 1-sided upper p = {p_perm_sec:.6f}", file=sys.stderr)

secondary_pass = rho_secondary >= 0.2 and p_perm_sec < 0.025
print(f"  Secondary: {'PASS' if secondary_pass else 'FAIL'} "
      f"(threshold: residual ρ ≥ 0.2, p < 0.025)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. MW-5 control: chronology-rank correlation (should be weaker)
# ---------------------------------------------------------------------------
chrono_ranks = [chronology[s] for s in surahs]
rho_chrono, _ = spearmanr(chrono_ranks, y_degree)
print(f"\nMW-5 control: Spearman ρ(chronology, degree) = {rho_chrono:.4f}", file=sys.stderr)
print(f"  |liturgical ρ| vs |chronology ρ|: "
      f"{abs(rho_primary):.3f} vs {abs(rho_chrono):.3f}", file=sys.stderr)
mw5_pass = abs(rho_primary) > abs(rho_chrono)
print(f"  MW-5 (liturgical stronger than chronology): "
      f"{'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Descriptive: top-score surahs and their degrees
# ---------------------------------------------------------------------------
top_liturgical = sorted(LITURGICAL_SCORES.items(), key=lambda x: -x[1])[:15]
print("\nTop-15 liturgical surahs:", file=sys.stderr)
for s, score in top_liturgical:
    print(f"  Q {s}: lit_score={score}, degree={per_surah_degree[s]}", file=sys.stderr)

top_degree = sorted(per_surah_degree.items(), key=lambda x: -x[1])[:15]
print("\nTop-15 cluster-degree surahs:", file=sys.stderr)
for s, d in top_degree:
    print(f"  Q {s}: degree={d}, lit_score={LITURGICAL_SCORES[s]}", file=sys.stderr)

# Overlap
top_lit_set = {s for s, _ in top_liturgical}
top_deg_set = {s for s, _ in top_degree}
overlap = top_lit_set & top_deg_set
print(f"\nTop-15 overlap: {len(overlap)} ({sorted(overlap)})", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Final verdict
# ---------------------------------------------------------------------------
if primary_pass and secondary_pass:
    final = "STRONG-LINK — liturgical prominence predicts hub-status, length-robust"
elif primary_pass and not secondary_pass:
    final = "WEAK-LINK — apparent liturgy-hub link dissolves under length-residualization"
elif not primary_pass and secondary_pass:
    final = "COUNTERINTUITIVE — residual signal but not raw"
else:
    final = "NULL — liturgical-hub hypothesis not empirically supported at pre-reg thresholds"

print("\n" + "=" * 70, file=sys.stderr)
print(f"Primary: ρ = {rho_primary:.4f}, p_perm = {p_perm_one_sided:.4f} → "
      f"{'PASS' if primary_pass else 'FAIL'}", file=sys.stderr)
print(f"Secondary: residual ρ = {rho_secondary:.4f}, p_perm = {p_perm_sec:.4f} → "
      f"{'PASS' if secondary_pass else 'FAIL'}", file=sys.stderr)
print(f"MW-5: |lit ρ| ({abs(rho_primary):.3f}) vs |chrono ρ| ({abs(rho_chrono):.3f}) → "
      f"{'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)
print(f"FINAL: {final}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-150',
    'title': 'Liturgical prominence ↔ cluster-network hub-degree',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 2, 'alpha_bon': 0.025, 'family': 'h-new-150-liturgical-hub'},
    'liturgical_scores': LITURGICAL_SCORES,
    'cluster_degrees': per_surah_degree,
    'primary': {
        'rho_spearman': rho_primary,
        'p_perm_one_sided': p_perm_one_sided,
        'threshold_rho': 0.3,
        'threshold_p': 0.025,
        'pass': primary_pass,
    },
    'secondary_length_residualized': {
        'rho_residual': rho_secondary,
        'p_perm_one_sided': p_perm_sec,
        'threshold_rho': 0.2,
        'threshold_p': 0.025,
        'pass': secondary_pass,
    },
    'mw5_control_chronology': {
        'rho_chronology': rho_chrono,
        'abs_liturgical_rho': abs(rho_primary),
        'abs_chronology_rho': abs(rho_chrono),
        'liturgical_stronger': mw5_pass,
    },
    'descriptive': {
        'top15_liturgical': [(s, score, per_surah_degree[s]) for s, score in top_liturgical],
        'top15_degree': [(s, d, LITURGICAL_SCORES[s]) for s, d in top_degree],
        'top15_overlap': sorted(overlap),
    },
    'final_verdict': final,
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
