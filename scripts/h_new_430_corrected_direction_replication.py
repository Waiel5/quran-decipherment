#!/usr/bin/env python3
"""H-NEW-430: corrected-direction replication of H-NEW-420 + Q 62 NC."""
import hashlib, json, random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-430-corrected-direction-replication-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-430.json"
SEED = 20260510
N_PERMS = 10000
ALPHA_BON = 0.05 / 6

TARGETS = {
    9: ("al-Tawbah", "novel", -15.0),
    12: ("Yūsuf", "novel", -15.0),
    24: ("al-Nūr", "novel", -15.0),
    33: ("al-Aḥzāb", "novel", -15.0),
    55: ("al-Raḥmān", "PC", -5.0),   # loose-PC
    62: ("al-Jumuʿa", "NC", None),   # NC: |delta| < 5pp
}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

def mean_pairwise(D, subset):
    xs = list(subset)
    vals = [D[a][b] for a, b in combinations(xs, 2)]
    return sum(vals) / len(vals) if vals else 0.0

def percentile_in_null(D, observed, size, n_perms, rng):
    all_surahs = list(range(1, 115))
    below = 0
    for _ in range(n_perms):
        sub = rng.sample(all_surahs, size)
        if mean_pairwise(D, sub) <= observed:
            below += 1
    return 100.0 * below / n_perms

def test_target(D, k, role, threshold, rng):
    block = [n for n in [k-2, k-1, k, k+1, k+2] if 1 <= n <= 114]
    block_exc = [n for n in block if n != k]
    d_full = mean_pairwise(D, block)
    d_exc = mean_pairwise(D, block_exc)
    p_full = percentile_in_null(D, d_full, len(block), N_PERMS, rng)
    p_exc = percentile_in_null(D, d_exc, len(block_exc), N_PERMS, rng)
    delta = p_exc - p_full

    if role == "novel":
        passed = delta <= threshold
        strict = delta <= -15.0
    elif role == "PC":
        passed = delta <= threshold  # loose
        strict = delta <= -15.0  # strict-PC
    elif role == "NC":
        passed = abs(delta) < 5.0
        strict = abs(delta) < 5.0

    return {
        "surah": k, "name": TARGETS[k][0], "role": role,
        "block_full": block, "block_exc": block_exc,
        "d_full": d_full, "d_exc": d_exc,
        "percentile_full": p_full, "percentile_exc": p_exc,
        "delta_pp": delta,
        "passed": passed, "strict_passed": strict,
    }

def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-430 (corrected-direction replication) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\nα_bon: {ALPHA_BON:.6f}")
    D = load_D()
    rng = random.Random(SEED)

    results = []
    for k, (name, role, thresh) in TARGETS.items():
        print(f"\n--- Q {k} {name} [{role}] ---")
        r = test_target(D, k, role, thresh, rng)
        results.append(r)
        print(f"  block_full={r['block_full']}  d̄={r['d_full']:.4f}  pct={r['percentile_full']:.2f}%")
        print(f"  block_exc ={r['block_exc']}  d̄={r['d_exc']:.4f}  pct={r['percentile_exc']:.2f}%")
        print(f"  delta_pp={r['delta_pp']:+.2f}  PASS={r['passed']}  STRICT={r['strict_passed']}")

    novel_confirm = [r for r in results if r["role"] == "novel" and r["passed"]]
    novel_strict = [r for r in results if r["role"] == "novel" and r["strict_passed"]]
    pc_result = next(r for r in results if r["role"] == "PC")
    nc_result = next(r for r in results if r["role"] == "NC")

    print(f"\n=== AGGREGATE VERDICT ===")
    print(f"Novel CONFIRM (≤-15pp): {len(novel_confirm)}/4")
    print(f"PC-PASS (Q55 loose ≤-5): {pc_result['passed']}  |  strict ≤-15: {pc_result['strict_passed']}")
    print(f"NC-PASS (Q62 |delta|<5): {nc_result['passed']}  (delta={nc_result['delta_pp']:+.2f}pp)")

    aggregate_h1 = (len(novel_confirm) >= 4) and pc_result["passed"] and nc_result["passed"]
    print(f"\nAGGREGATE H1 (≥4/4 novel CONFIRM + PC-PASS + NC-PASS): {aggregate_h1}")
    print(f"Instrument-status: {'VALIDATED' if nc_result['passed'] else 'BROKEN (NC fails)'}")

    out = {
        "id": "H-NEW-430", "prereg_sha": prereg_sha,
        "seed": SEED, "n_permutations": N_PERMS,
        "alpha_bon": ALPHA_BON,
        "results": results,
        "novel_confirmed": len(novel_confirm),
        "novel_strict_confirmed": len(novel_strict),
        "pc_pass": pc_result["passed"],
        "pc_strict": pc_result["strict_passed"],
        "nc_pass": nc_result["passed"],
        "nc_delta": nc_result["delta_pp"],
        "aggregate_h1_pass": aggregate_h1,
        "instrument_validated": nc_result["passed"],
    }
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
