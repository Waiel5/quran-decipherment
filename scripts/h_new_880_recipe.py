#!/usr/bin/env python3
"""H-NEW-880: Reverse-engineer the canonical mushaf's architectural recipe.

For each of seven nested constraint subsets (S1..S7), run a Markov chain over
permutations with hard-constraint rejection plus MH-on-FR-tour-length. Report
the median TSP-residual and verdict per subset.

PRE-REG-STANDARD-04. Pre-reg SHA embedded below.
"""
import hashlib
import json
import math
import random
import time
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-880-recipe-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-880.json"
VERSE_COUNTS = ROOT / "data/hafs-verse-counts.tsv"
REVELATION_CSV = ROOT / "data/revelation-order.csv"
EXPECTED_PREREG_SHA = "5ff0a959d3684aaaf0ee9670da2f9f460eeeb6c0827c783b6295428a6c23df00"

SEED = 20260450

# Per-subset chain parameters (pre-reg locked)
N_BURN = 2000
N_STEPS_POST = 10000
SAMPLE_EVERY = 100
N_SAMPLES_TARGET = 100
MAX_PROPOSALS = 12000  # total cap per subset

# Compression-tail constants (from H-NEW-660/690)
K = 15
KINK = 50
R2_MIN = 0.95
BETA_LO = -0.015
BETA_HI = -0.010
T_MH = 1.0

# Locked from h-new-111.json
L_CANONICAL = 85.759656
L_2OPT = 77.466858
CANONICAL_RESIDUAL = (L_CANONICAL - L_2OPT) / L_2OPT  # ~0.10705

# Architectural-outlier anchors (C6)
C6_ANCHORS = {33: 33, 9: 9, 24: 24, 55: 55}  # surah_id -> canonical_position (1-indexed)

# Muqaṭṭaʿāt (29 surahs, classical list per al-Suyūṭī)
MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36,
             38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

# C5 phase-monotonicity tolerance (calibrated to admit canonical: max canonical
# phase-inversion is 20 in Early Meccan; tol=25 = canonical-baseline + 5 margin).
C5_INVERSION_TOL = 25  # per phase

# C7 muqaṭṭaʿāt head cap (calibrated to admit canonical: max muqaṭṭaʿāt position
# in canonical is Q 68 al-Qalam at position 68).
C7_HEAD_CAP = 68


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def load_verse_counts():
    counts = {}
    with open(VERSE_COUNTS) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            s, n = line.split("\t")
            counts[int(s)] = int(n)
    return counts


def load_phases():
    """Map surah_id (1..114) -> Nöldeke phase."""
    phases = {}
    with open(REVELATION_CSV) as f:
        header = f.readline()
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 7:
                continue
            mushaf = int(parts[1])
            phase = parts[6]
            phases[mushaf] = phase
    return phases


# === Constraint evaluation helpers ===

def window_mean(D, surahs):
    n = len(surahs)
    if n < 2:
        return 0.0
    s = 0.0
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += D[surahs[i]][surahs[j]]
            cnt += 1
    return s / cnt


def all_window_means(D, perm):
    """Return d̄ for windows starting at s=1..100 (1-indexed)."""
    out = []
    for s in range(1, 101):
        sub = perm[s - 1: s - 1 + K]
        out.append(window_mean(D, sub))
    return out


def fit_two_piece(d_obs, kink=KINK):
    """y = a + b * max(0, x - kink); x in {1..len(d_obs)}."""
    n = len(d_obs)
    xs = list(range(1, n + 1))
    feat = [max(0, x - kink) for x in xs]
    mx = sum(feat) / n
    my = sum(d_obs) / n
    num = sum((feat[i] - mx) * (d_obs[i] - my) for i in range(n))
    den = sum((feat[i] - mx) ** 2 for i in range(n))
    if den < 1e-15:
        return 0.0, 0.0, 0.0
    beta = num / den
    alpha = my - beta * mx
    yhat = [alpha + beta * f for f in feat]
    ss_tot = sum((y - my) ** 2 for y in d_obs)
    ss_res = sum((d_obs[i] - yhat[i]) ** 2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return alpha, beta, r2


def c1_ok(D, perm):
    d_obs = all_window_means(D, perm)
    alpha, beta, r2 = fit_two_piece(d_obs)
    return (r2 >= R2_MIN) and (BETA_LO <= beta <= BETA_HI), r2, beta


def c2_ok(perm):
    return perm[0] == 1


def c3_ok(perm):
    """Q56 and Q57 are adjacent."""
    p56 = perm.index(56)
    p57 = perm.index(57)
    return abs(p56 - p57) == 1


def c4_ok(perm):
    """Q113 at position 113 (index 112), Q114 at position 114 (index 113)."""
    return perm[112] == 113 and perm[113] == 114


def c5_ok(perm, verse_counts, phases):
    """Within each Nöldeke phase, verse-counts in ordering are non-increasing
    with at most C5_INVERSION_TOL inversions per phase."""
    phase_seqs = {}
    for pos, sid in enumerate(perm):
        phase = phases.get(sid, "Unknown")
        phase_seqs.setdefault(phase, []).append(verse_counts[sid])
    for phase, seq in phase_seqs.items():
        # Count adjacent inversions (seq[i] < seq[i+1] indicates inversion)
        inv = sum(1 for i in range(len(seq) - 1) if seq[i] < seq[i + 1])
        if inv > C5_INVERSION_TOL:
            return False
    return True


def c6_ok(perm):
    """Architectural outliers at canonical positions."""
    for sid, target_pos in C6_ANCHORS.items():
        if perm[target_pos - 1] != sid:
            return False
    return True


def c7_ok(perm):
    """All muqaṭṭaʿāt within positions 1..C7_HEAD_CAP (indices 0..C7_HEAD_CAP-1)."""
    head = set(perm[:C7_HEAD_CAP])
    return MUQATTAAT.issubset(head)


def fr_tour_length(D, perm):
    L = 0.0
    for i in range(len(perm) - 1):
        L += D[perm[i]][perm[i + 1]]
    return L


def all_constraints_ok(D, perm, active_set, verse_counts, phases):
    """Return True if perm satisfies all constraints in active_set."""
    if "C1" in active_set:
        ok, _, _ = c1_ok(D, perm)
        if not ok:
            return False
    if "C2" in active_set and not c2_ok(perm):
        return False
    if "C3" in active_set and not c3_ok(perm):
        return False
    if "C4" in active_set and not c4_ok(perm):
        return False
    if "C5" in active_set and not c5_ok(perm, verse_counts, phases):
        return False
    if "C6" in active_set and not c6_ok(perm):
        return False
    if "C7" in active_set and not c7_ok(perm):
        return False
    return True


# === Proposal mechanics ===

def propose_swap(perm, rng):
    p2 = perm[:]
    i, j = rng.sample(range(len(p2)), 2)
    p2[i], p2[j] = p2[j], p2[i]
    return p2


def propose_2opt(perm, rng, max_len=10):
    """Reverse a random subsequence of length 2..max_len."""
    n = len(perm)
    L = rng.randint(2, max_len)
    i = rng.randint(0, n - L)
    p2 = perm[:]
    p2[i:i + L] = p2[i:i + L][::-1]
    return p2


def propose(perm, rng):
    if rng.random() < 0.5:
        return propose_swap(perm, rng)
    return propose_2opt(perm, rng)


# === Chain runner ===

def run_chain(D, active_set, verse_counts, phases, rng,
              start_perm,
              n_burn=N_BURN, n_steps_post=N_STEPS_POST,
              sample_every=SAMPLE_EVERY,
              n_samples_target=N_SAMPLES_TARGET,
              max_proposals=MAX_PROPOSALS):
    """Runs MH chain. Starts from start_perm (must satisfy active constraints)."""
    perm = start_perm[:]

    # Verify start is feasible
    if not all_constraints_ok(D, perm, active_set, verse_counts, phases):
        # Fallback: if canonical doesn't satisfy active set, fail
        return {
            "feasible_start": False,
            "samples": [],
            "proposals_total": 0,
            "accepts_total": 0,
            "constraint_ok_proposals": 0,
        }

    L = fr_tour_length(D, perm)

    samples = []
    proposals_total = 0
    accepts_total = 0
    constraint_ok_proposals = 0
    next_sample_step = n_burn + sample_every

    total_steps = n_burn + n_steps_post
    if total_steps > max_proposals:
        total_steps = max_proposals

    for step in range(1, total_steps + 1):
        p2 = propose(perm, rng)
        proposals_total += 1
        if not all_constraints_ok(D, p2, active_set, verse_counts, phases):
            # Reject, keep perm
            pass
        else:
            constraint_ok_proposals += 1
            L2 = fr_tour_length(D, p2)
            dL = L2 - L
            if dL <= 0 or rng.random() < math.exp(-dL / T_MH):
                perm = p2
                L = L2
                accepts_total += 1

        if step >= next_sample_step and len(samples) < n_samples_target:
            samples.append({
                "step": step,
                "L": L,
                "residual": (L - L_2OPT) / L_2OPT,
            })
            next_sample_step += sample_every

    return {
        "feasible_start": True,
        "samples": samples,
        "proposals_total": proposals_total,
        "accepts_total": accepts_total,
        "constraint_ok_proposals": constraint_ok_proposals,
        "final_L": L,
    }


# === Random + greedy warmup for S1 (replicate H-NEW-690) ===

def random_warmup_s1(D, rng, max_attempts=5000):
    """For S1 only: try random start with greedy descent on R²/β feasibility."""
    n = 114
    perm = list(range(1, 115))
    rng.shuffle(perm)

    def cd(p):
        d_obs = all_window_means(D, p)
        _, beta, r2 = fit_two_piece(d_obs)
        r2_gap = max(0.0, R2_MIN - r2)
        if BETA_LO <= beta <= BETA_HI:
            beta_gap = 0.0
        else:
            beta_gap = min(abs(beta - BETA_LO), abs(beta - BETA_HI))
        return 10.0 * r2_gap + beta_gap

    cur_cd = cd(perm)
    attempts = 0
    while cur_cd > 0.0 and attempts < max_attempts:
        i, j = rng.sample(range(n), 2)
        p2 = perm[:]
        p2[i], p2[j] = p2[j], p2[i]
        cd2 = cd(p2)
        if cd2 < cur_cd:
            perm = p2
            cur_cd = cd2
        attempts += 1
    return perm, cur_cd, attempts


# === Aggregation ===

def percentile(sorted_vals, p):
    if not sorted_vals:
        return None
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    k = (p / 100.0) * (n - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    return sorted_vals[f] + (k - f) * (sorted_vals[c] - sorted_vals[f])


def summarize(samples):
    if not samples:
        return {"n": 0}
    residuals = sorted([s["residual"] for s in samples])
    Ls = sorted([s["L"] for s in samples])
    n = len(residuals)

    n_le_115 = sum(1 for r in residuals if r <= 0.115)
    n_le_120 = sum(1 for r in residuals if r <= 0.120)
    n_le_130 = sum(1 for r in residuals if r <= 0.130)
    n_le_150 = sum(1 for r in residuals if r <= 0.150)
    n_le_canonical = sum(1 for r in residuals if r <= CANONICAL_RESIDUAL)

    return {
        "n": n,
        "median_residual": percentile(residuals, 50),
        "p10": percentile(residuals, 10),
        "p25": percentile(residuals, 25),
        "p75": percentile(residuals, 75),
        "p90": percentile(residuals, 90),
        "min": residuals[0],
        "max": residuals[-1],
        "median_L": percentile(Ls, 50),
        "min_L": Ls[0],
        "max_L": Ls[-1],
        "pct_le_115": n_le_115 / n,
        "pct_le_120": n_le_120 / n,
        "pct_le_130": n_le_130 / n,
        "pct_le_150": n_le_150 / n,
        "canonical_percentile": 100.0 * n_le_canonical / n,
    }


def verdict_for_subset(median_resid):
    if median_resid is None:
        return "INSUFFICIENT-DATA"
    if median_resid <= 0.12:
        return "STRONG-RECIPE"
    if median_resid <= 0.15:
        return "DIRECTIONAL"
    return "NULL"


# === Main ===

def main():
    t0 = time.time()
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-880 (Reverse-engineer the mushaf recipe) ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print("WARNING: pre-reg SHA mismatch — pre-reg has been edited since lock.")
    print(f"Seed: {SEED}\n")

    print("Loading FR distance matrix from H-NEW-111...")
    D = load_D()
    verse_counts = load_verse_counts()
    phases = load_phases()
    print(f"  Loaded {len(verse_counts)} verse counts, {len(phases)} phase entries.")

    # Sanity: canonical
    canonical = list(range(1, 115))
    L_c = fr_tour_length(D, canonical)
    print(f"\nSanity: canonical L = {L_c:.4f}, residual = {(L_c-L_2OPT)/L_2OPT*100:.2f}%")

    # Check which constraints canonical satisfies
    print("\nCanonical constraint satisfaction:")
    c1, r2, beta = c1_ok(D, canonical)
    print(f"  C1 (compression-tail): {c1} (R²={r2:.4f}, β={beta:+.5f})")
    print(f"  C2 (Fātiḥa first): {c2_ok(canonical)}")
    print(f"  C3 (Q56-Q57 adjacent): {c3_ok(canonical)}")
    print(f"  C4 (Q113-Q114 terminal): {c4_ok(canonical)}")
    print(f"  C5 (phase length-monot, tol={C5_INVERSION_TOL}): {c5_ok(canonical, verse_counts, phases)}")
    print(f"  C6 (architectural-outliers at canonical pos): {c6_ok(canonical)}")
    print(f"  C7 (muqaṭṭaʿāt in head 1..50): {c7_ok(canonical)}")

    # Compute C5 inversion counts on canonical for context
    phase_seqs = {}
    for pos, sid in enumerate(canonical):
        phase = phases.get(sid, "Unknown")
        phase_seqs.setdefault(phase, []).append(verse_counts[sid])
    for phase, seq in phase_seqs.items():
        inv = sum(1 for i in range(len(seq) - 1) if seq[i] < seq[i + 1])
        print(f"    canonical inversions in {phase}: {inv}/{len(seq)-1}")

    # Define seven nested subsets
    subsets = [
        ("S1", {"C1"}),
        ("S2", {"C1", "C2"}),
        ("S3", {"C1", "C2", "C3"}),
        ("S4", {"C1", "C2", "C3", "C4"}),
        ("S5", {"C1", "C2", "C3", "C4", "C5"}),
        ("S6", {"C1", "C2", "C3", "C4", "C5", "C6"}),
        ("S7", {"C1", "C2", "C3", "C4", "C5", "C6", "C7"}),
    ]

    rng = random.Random(SEED)

    results = {}
    for name, active in subsets:
        t_start = time.time()
        print(f"\n--- Subset {name}: {sorted(active)} ---")

        if name == "S1":
            # Replicate H-NEW-690 by random warmup
            print("  Random warmup (greedy descent on C1 feasibility)...")
            start_perm, cur_cd, w_attempts = random_warmup_s1(D, rng, max_attempts=5000)
            if cur_cd > 0:
                print(f"  Warmup did not reach feasibility (cd={cur_cd}, attempts={w_attempts}); falling back to canonical.")
                start_perm = list(range(1, 115))
                used_fallback = True
            else:
                print(f"  Warmup feasible after {w_attempts} attempts.")
                used_fallback = False
        else:
            # Start from canonical (pre-reg locked)
            start_perm = list(range(1, 115))
            used_fallback = False

        # Verify start is feasible
        if not all_constraints_ok(D, start_perm, active, verse_counts, phases):
            print(f"  ERROR: start_perm does NOT satisfy {sorted(active)}; skipping subset.")
            results[name] = {
                "active_constraints": sorted(active),
                "feasible_start": False,
                "elapsed_sec": time.time() - t_start,
                "summary": {"n": 0},
                "verdict": "INFEASIBLE-START",
            }
            continue

        chain_result = run_chain(
            D, active, verse_counts, phases, rng,
            start_perm=start_perm,
        )
        elapsed = time.time() - t_start
        summ = summarize(chain_result["samples"])
        v = verdict_for_subset(summ.get("median_residual"))

        if summ.get("n", 0) > 0:
            print(f"  proposals={chain_result['proposals_total']}, "
                  f"constraint-ok={chain_result['constraint_ok_proposals']} "
                  f"({100*chain_result['constraint_ok_proposals']/max(1,chain_result['proposals_total']):.2f}%), "
                  f"accepts={chain_result['accepts_total']}")
            print(f"  n_samples={summ['n']}, "
                  f"median_residual={summ['median_residual']*100:.2f}%, "
                  f"p25={summ['p25']*100:.2f}%, p75={summ['p75']*100:.2f}%, "
                  f"min={summ['min']*100:.2f}%, max={summ['max']*100:.2f}%")
            print(f"  pct_le_115={summ['pct_le_115']*100:.1f}%, "
                  f"canonical_percentile={summ['canonical_percentile']:.1f}%")
            print(f"  VERDICT: {v}")
        else:
            print(f"  No samples collected.")

        results[name] = {
            "active_constraints": sorted(active),
            "feasible_start": chain_result.get("feasible_start", False),
            "used_warmup_fallback": used_fallback if name == "S1" else False,
            "proposals_total": chain_result["proposals_total"],
            "constraint_ok_proposals": chain_result["constraint_ok_proposals"],
            "accepts_total": chain_result["accepts_total"],
            "elapsed_sec": elapsed,
            "summary": summ,
            "verdict": v,
            "samples_compact": chain_result["samples"],
        }

    # Determine minimal recipe
    minimal_recipe = None
    directional_recipe = None
    for name, _ in subsets:
        v = results[name]["verdict"]
        if v == "STRONG-RECIPE" and minimal_recipe is None:
            minimal_recipe = name
        if v in ("STRONG-RECIPE", "DIRECTIONAL") and directional_recipe is None:
            directional_recipe = name

    elapsed_total = time.time() - t0
    print(f"\n=== TOTAL elapsed: {elapsed_total:.1f}s ===")
    print(f"Minimal STRONG recipe: {minimal_recipe}")
    print(f"Earliest DIRECTIONAL recipe: {directional_recipe}")

    out = {
        "id": "H-NEW-880",
        "title": "Reverse-engineer the canonical mushaf's architectural recipe",
        "prereg_sha": prereg_sha,
        "expected_prereg_sha": EXPECTED_PREREG_SHA,
        "prereg_sha_match": prereg_sha == EXPECTED_PREREG_SHA,
        "seed": SEED,
        "date": "2026-04-28",
        "elapsed_seconds": elapsed_total,
        "locked_params": {
            "n_burn": N_BURN,
            "n_steps_post": N_STEPS_POST,
            "sample_every": SAMPLE_EVERY,
            "n_samples_target": N_SAMPLES_TARGET,
            "max_proposals": MAX_PROPOSALS,
            "K": K,
            "kink": KINK,
            "r2_min": R2_MIN,
            "beta_range": [BETA_LO, BETA_HI],
            "T_MH": T_MH,
            "c5_inversion_tol": C5_INVERSION_TOL,
            "c6_anchors": C6_ANCHORS,
            "c7_head_cap": C7_HEAD_CAP,
            "muqattaat_count": len(MUQATTAAT),
        },
        "anchors": {
            "L_canonical": L_CANONICAL,
            "L_2opt": L_2OPT,
            "canonical_residual": CANONICAL_RESIDUAL,
        },
        "canonical_constraint_check": {
            "C1": c1_ok(D, canonical)[0],
            "C2": c2_ok(canonical),
            "C3": c3_ok(canonical),
            "C4": c4_ok(canonical),
            "C5": c5_ok(canonical, verse_counts, phases),
            "C6": c6_ok(canonical),
            "C7": c7_ok(canonical),
        },
        "results_per_subset": results,
        "minimal_strong_recipe": minimal_recipe,
        "earliest_directional_recipe": directional_recipe,
        "bonferroni_k": 7,
        "alpha_bon": 0.05 / 7,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {OUT_JSON}")


if __name__ == "__main__":
    main()
