#!/usr/bin/env python3
"""MW-1-GATE-A — length-residualized H-NEW-20 al-Rāzī Stouffer.

NOTE: Naive "OLS residualization then Stouffer" is mathematically vacuous —
OLS residuals sum to zero by construction, so Stouffer on residuals is always 0.
The correct length-control tests are:

  (1) Stratum-wise Stouffer: compute Stouffer Z within length strata
      (n≤30, 30<n≤100, n>100) separately. A length-driven artifact would
      show a strong gradient with surah length. A genuine effect should
      persist in the SHORT stratum.

  (2) Intercept test: regress z on log(N). If the intercept is strongly
      positive at log(N_min), signal exists independent of length.
      Equivalent: predicted z at mean(log N) minus zero.

  (3) Equal-contribution Stouffer: use the smallest-length stratum only,
      which approximates equal n_pairs per surah.

  (4) Inverse-variance weighting: weight each z by 1/n_pairs so longer
      surahs contribute less. This is the formal null-hypothesis-respecting
      meta-analysis weighting.

Threshold for MW-1 continued contribution: post-residualization |Z| ≥ 10
(per task #52 spec), operationalized as: SHORT-stratum (n≤30) Stouffer Z
AND inverse-variance-weighted Stouffer Z both must exceed 10.

Seed 20260413.
"""
import json, math
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')

CACHED = ROOT / 'scratch/team-discovery/result-razi-biqai.json'
data = json.loads(CACHED.read_text())
per_surah = data['per_surah']
print(f"loaded: {len(per_surah)} surahs from H-NEW-20 cache")

# --- Original Stouffer for comparison ---
def stouffer(zs):
    return sum(zs) / math.sqrt(len(zs)) if zs else 0.0

def ols_residuals(y, X_cols):
    """Manual OLS residuals: y vs design matrix with intercept + X_cols.
    X_cols is list of feature vectors (same length as y).
    Returns residuals list."""
    n = len(y)
    k = len(X_cols) + 1  # intercept + features
    # Build X matrix (n × k), first column all 1s
    X = [[1.0] + [col[i] for col in X_cols] for i in range(n)]
    # Normal equations: β = (X'X)^-1 X'y
    # Build X'X (k × k)
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(k)] for a in range(k)]
    Xty = [sum(X[i][a] * y[i] for i in range(n)) for a in range(k)]
    # Gauss-Jordan inversion
    def inv(M):
        size = len(M)
        A = [row[:] + [1.0 if i == j else 0.0 for j in range(size)] for i, row in enumerate(M)]
        for i in range(size):
            pivot = A[i][i]
            if abs(pivot) < 1e-12:
                for r in range(i + 1, size):
                    if abs(A[r][i]) > 1e-12:
                        A[i], A[r] = A[r], A[i]
                        pivot = A[i][i]
                        break
            for j in range(2 * size):
                A[i][j] /= pivot
            for r in range(size):
                if r != i:
                    factor = A[r][i]
                    for j in range(2 * size):
                        A[r][j] -= factor * A[i][j]
        return [row[size:] for row in A]
    XtX_inv = inv(XtX)
    beta = [sum(XtX_inv[a][b] * Xty[b] for b in range(k)) for a in range(k)]
    fitted = [sum(X[i][a] * beta[a] for a in range(k)) for i in range(n)]
    residuals = [y[i] - fitted[i] for i in range(n)]
    return residuals, beta

def summary_stats(zs, name):
    if not zs:
        return
    m = sum(zs) / len(zs)
    v = sum((z - m) ** 2 for z in zs) / max(1, len(zs) - 1)
    s = math.sqrt(v)
    Z = stouffer(zs)
    pos = sum(1 for z in zs if z > 0)
    print(f"  {name}: n={len(zs)}, mean={m:.3f} ± {s:.3f}, Stouffer Z={Z:.3f}, pos={pos}/{len(zs)}")
    return Z

# --- Extract per-surah data ---
z_r1 = []
z_grad = []
z_ring = []
n_vec = []
r1_vec = []  # raw r1 similarity
for r in per_surah:
    if r['z_r1'] is None or r['z_grad'] is None or r['z_ring'] is None:
        continue
    z_r1.append(r['z_r1'])
    z_grad.append(r['z_grad'])
    z_ring.append(r['z_ring'])
    n_vec.append(r['n'])
    r1_vec.append(r['r1'])

log_n = [math.log(n) for n in n_vec]
log_n_sq = [x ** 2 for x in log_n]

print("\n=== Pre-residualization (original H-NEW-20 Stouffer) ===")
Z0_r1 = summary_stats(z_r1, "z_r1")
Z0_grad = summary_stats(z_grad, "z_grad")
Z0_ring = summary_stats(z_ring, "z_ring")

# --- Residualize z_r1, z_grad, z_ring on log(N) ---
print("\n=== Residualization: z ~ 1 + log(N) ===")
resid_r1, beta_r1 = ols_residuals(z_r1, [log_n])
resid_grad, beta_grad = ols_residuals(z_grad, [log_n])
resid_ring, beta_ring = ols_residuals(z_ring, [log_n])
print(f"  z_r1  intercept={beta_r1[0]:.3f}, log(N) slope={beta_r1[1]:.3f}")
print(f"  z_grad intercept={beta_grad[0]:.3f}, log(N) slope={beta_grad[1]:.3f}")
print(f"  z_ring intercept={beta_ring[0]:.3f}, log(N) slope={beta_ring[1]:.3f}")

print("\n=== Post-residualization Stouffer (z - fitted) ===")
Z1_r1 = summary_stats(resid_r1, "resid_z_r1")
Z1_grad = summary_stats(resid_grad, "resid_z_grad")
Z1_ring = summary_stats(resid_ring, "resid_z_ring")

# --- Alternative: quadratic in log(N) (richer control) ---
print("\n=== Residualization: z ~ 1 + log(N) + log(N)^2 ===")
resid2_r1, _ = ols_residuals(z_r1, [log_n, log_n_sq])
resid2_grad, _ = ols_residuals(z_grad, [log_n, log_n_sq])
resid2_ring, _ = ols_residuals(z_ring, [log_n, log_n_sq])
Z2_r1 = summary_stats(resid2_r1, "resid2_z_r1")
Z2_grad = summary_stats(resid2_grad, "resid2_z_grad")
Z2_ring = summary_stats(resid2_ring, "resid2_z_ring")

# --- Equal-n subsample (option b): restrict to surahs with n < 30 ---
print("\n=== Subsample: n_verses ≤ 30 (equal-ish contribution) ===")
idx_small = [i for i, n in enumerate(n_vec) if n <= 30]
print(f"  {len(idx_small)} surahs")
z_r1_small = [z_r1[i] for i in idx_small]
z_grad_small = [z_grad[i] for i in idx_small]
z_ring_small = [z_ring[i] for i in idx_small]
Z3_r1 = summary_stats(z_r1_small, "z_r1 (n≤30)")
Z3_grad = summary_stats(z_grad_small, "z_grad (n≤30)")
Z3_ring = summary_stats(z_ring_small, "z_ring (n≤30)")

# --- Further subsample: 30 < n ≤ 100 ---
print("\n=== Subsample: 30 < n ≤ 100 ===")
idx_mid = [i for i, n in enumerate(n_vec) if 30 < n <= 100]
print(f"  {len(idx_mid)} surahs")
z_r1_mid = [z_r1[i] for i in idx_mid]
z_grad_mid = [z_grad[i] for i in idx_mid]
z_ring_mid = [z_ring[i] for i in idx_mid]
Z_mid_r1 = summary_stats(z_r1_mid, "z_r1 (mid)")
Z_mid_grad = summary_stats(z_grad_mid, "z_grad (mid)")
Z_mid_ring = summary_stats(z_ring_mid, "z_ring (mid)")

# --- n > 100 ---
print("\n=== Subsample: n > 100 ===")
idx_large = [i for i, n in enumerate(n_vec) if n > 100]
print(f"  {len(idx_large)} surahs")
z_r1_large = [z_r1[i] for i in idx_large]
z_grad_large = [z_grad[i] for i in idx_large]
z_ring_large = [z_ring[i] for i in idx_large]
Z_lg_r1 = summary_stats(z_r1_large, "z_r1 (large)")
Z_lg_grad = summary_stats(z_grad_large, "z_grad (large)")
Z_lg_ring = summary_stats(z_ring_large, "z_ring (large)")

# --- Correlations to document what the length dependency looks like ---
def pearson(x, y):
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    dx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
    dy = math.sqrt(sum((yi - my) ** 2 for yi in y))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0

rho_r1_n = pearson(log_n, z_r1)
rho_grad_n = pearson(log_n, z_grad)
rho_ring_n = pearson(log_n, z_ring)
print("\n=== Correlations (z vs log N) ===")
print(f"  ρ(log_n, z_r1)   = {rho_r1_n:+.3f}")
print(f"  ρ(log_n, z_grad) = {rho_grad_n:+.3f}")
print(f"  ρ(log_n, z_ring) = {rho_ring_n:+.3f}")

# --- Inverse-variance-weighted Stouffer ---
# Each surah's ρ(1) is computed over (n-1) adjacent-pair Jaccard values.
# Under null, per-surah z has approx unit variance by construction, but
# the SIGNAL variance scales with 1/(n-1) pairs. Inverse-variance weighting
# in Stouffer is: Z = Σ(w_i · z_i) / √(Σ w_i²), with w_i = √(n_i - 1).
# Alternative: w_i = 1/√(n_i - 1) de-emphasizes long surahs.

def weighted_stouffer(zs, weights):
    num = sum(w * z for w, z in zip(weights, zs))
    den = math.sqrt(sum(w * w for w in weights))
    return num / den if den > 0 else 0.0

print("\n=== Inverse-variance weighted Stouffer (w = 1/√(n-1)) ===")
w_inv = [1.0 / math.sqrt(max(1, n - 1)) for n in n_vec]
Z_iv_r1 = weighted_stouffer(z_r1, w_inv)
Z_iv_grad = weighted_stouffer(z_grad, w_inv)
Z_iv_ring = weighted_stouffer(z_ring, w_inv)
print(f"  z_r1 weighted Z = {Z_iv_r1:.3f}")
print(f"  z_grad weighted Z = {Z_iv_grad:.3f}")
print(f"  z_ring weighted Z = {Z_iv_ring:.3f}")

# Equal weight Stouffer already = Z0_*

# --- Gate verdict ---
THRESHOLD = 10.0
# Primary gate: SHORT-stratum Stouffer (n≤30) — pairs per surah most equal here
# Secondary gate: inverse-variance-weighted Stouffer
gate_short_r1 = abs(Z3_r1) >= THRESHOLD
gate_short_grad = abs(Z3_grad) >= THRESHOLD
gate_iv_r1 = abs(Z_iv_r1) >= THRESHOLD
gate_iv_grad = abs(Z_iv_grad) >= THRESHOLD

# MW-1 contribution requires BOTH tests to pass
gate_r1_pass = gate_short_r1 and gate_iv_r1
gate_grad_pass = gate_short_grad and gate_iv_grad

print(f"\n=== MW-1-GATE-A Verdict (threshold |Z| ≥ {THRESHOLD}, primary + IV-weighted) ===")
print(f"  r1:   short={Z3_r1:.2f} (≥{THRESHOLD}? {gate_short_r1}), IV={Z_iv_r1:.2f} (≥{THRESHOLD}? {gate_iv_r1}) → {'PASS' if gate_r1_pass else 'FAIL'}")
print(f"  grad: short={Z3_grad:.2f} (≥{THRESHOLD}? {gate_short_grad}), IV={Z_iv_grad:.2f} (≥{THRESHOLD}? {gate_iv_grad}) → {'PASS' if gate_grad_pass else 'FAIL'}")

# --- Save ---
out = {
    'seed': 20260413,
    'source_file': str(CACHED),
    'n_surahs': len(z_r1),
    'threshold': THRESHOLD,
    'pre_residualization': {
        'stouffer_z_r1': Z0_r1,
        'stouffer_z_grad': Z0_grad,
        'stouffer_z_ring': Z0_ring,
    },
    'post_residualization_linear': {
        'stouffer_z_r1': Z1_r1,
        'stouffer_z_grad': Z1_grad,
        'stouffer_z_ring': Z1_ring,
        'beta_r1': beta_r1,
        'beta_grad': beta_grad,
        'beta_ring': beta_ring,
    },
    'post_residualization_quadratic': {
        'stouffer_z_r1': Z2_r1,
        'stouffer_z_grad': Z2_grad,
        'stouffer_z_ring': Z2_ring,
    },
    'subsample_n_le_30': {
        'n': len(idx_small),
        'stouffer_z_r1': Z3_r1,
        'stouffer_z_grad': Z3_grad,
        'stouffer_z_ring': Z3_ring,
    },
    'subsample_30_100': {
        'n': len(idx_mid),
        'stouffer_z_r1': Z_mid_r1,
        'stouffer_z_grad': Z_mid_grad,
        'stouffer_z_ring': Z_mid_ring,
    },
    'subsample_n_gt_100': {
        'n': len(idx_large),
        'stouffer_z_r1': Z_lg_r1,
        'stouffer_z_grad': Z_lg_grad,
        'stouffer_z_ring': Z_lg_ring,
    },
    'length_correlations': {
        'rho_logn_z_r1': rho_r1_n,
        'rho_logn_z_grad': rho_grad_n,
        'rho_logn_z_ring': rho_ring_n,
    },
    'inverse_variance_weighted': {
        'weights': 'w=1/sqrt(n-1)',
        'stouffer_z_r1': Z_iv_r1,
        'stouffer_z_grad': Z_iv_grad,
        'stouffer_z_ring': Z_iv_ring,
    },
    'gate_verdict': {
        'short_stratum_r1_pass': gate_short_r1,
        'short_stratum_grad_pass': gate_short_grad,
        'iv_weighted_r1_pass': gate_iv_r1,
        'iv_weighted_grad_pass': gate_iv_grad,
        'joint_r1_pass': gate_r1_pass,
        'joint_grad_pass': gate_grad_pass,
        'threshold': THRESHOLD,
        'note': ('naive OLS-residualization Z always = 0 by construction; '
                 'proper gate = short-stratum Stouffer + inverse-variance-'
                 'weighted Stouffer.'),
    },
}
out_path = ROOT / 'findings/phase-b-hypotheses/csv/mw1-gate-a-h-new-20-residualized.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2))
print(f"\nsaved: {out_path}")
