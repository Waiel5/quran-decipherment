#!/usr/bin/env python3
"""H-NEW-730: window-level content × rhyme anti-correlation test."""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
H_NEW_700 = ROOT / "findings/phase-b-hypotheses/csv/h-new-700.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-730-content-rhyme-anticorrelation-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-730.json"
SEED = 20260442
N_PERMS = 10000


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def mean_pairwise(D, subset):
    return sum(D[a][b] for a, b in combinations(subset, 2)) / max(1, len(list(combinations(subset, 2))))


def pearson_r(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    dx = math.sqrt(sum((x[i]-mx)**2 for i in range(n)))
    dy = math.sqrt(sum((y[i]-my)**2 for i in range(n)))
    return num/(dx*dy) if dx > 0 and dy > 0 else 0.0


def spearman_rho(x, y):
    def ranks(v):
        sorted_pairs = sorted(enumerate(v), key=lambda p: p[1])
        r = [0]*len(v)
        i = 0
        while i < len(sorted_pairs):
            j = i
            while j+1 < len(sorted_pairs) and sorted_pairs[j+1][1] == sorted_pairs[i][1]:
                j += 1
            avg_rank = (i + j) / 2 + 1  # 1-indexed
            for k in range(i, j+1):
                r[sorted_pairs[k][0]] = avg_rank
            i = j + 1
        return r
    rx, ry = ranks(x), ranks(y)
    return pearson_r(rx, ry)


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-730 (Content × Rhyme anti-correlation) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    # Load content d̄_window
    D = load_D()
    K = 15
    starts = list(range(1, 101))
    d_content = []
    for s in starts:
        sub = list(range(s, s + K))
        d_content.append(mean_pairwise(D, sub))

    # Load rhyme d̄_window from h-new-700
    with open(H_NEW_700) as f:
        h700 = json.load(f)
    d_rhyme = h700["rhyme"]["d_observed"]
    d_phoneme = h700["phoneme"]["d_observed"]
    print(f"Loaded: content N={len(d_content)}, rhyme N={len(d_rhyme)}, phoneme N={len(d_phoneme)}")
    assert len(d_content) == len(d_rhyme), f"length mismatch: {len(d_content)} vs {len(d_rhyme)}"

    # Pearson + Spearman: content vs rhyme
    r_cr = pearson_r(d_content, d_rhyme)
    rho_cr = spearman_rho(d_content, d_rhyme)
    print(f"\n--- CONTENT × RHYME ---")
    print(f"  Pearson r = {r_cr:+.4f}")
    print(f"  Spearman ρ = {rho_cr:+.4f}")

    # Pearson + Spearman: content vs phoneme
    r_cp = pearson_r(d_content, d_phoneme)
    rho_cp = spearman_rho(d_content, d_phoneme)
    print(f"\n--- CONTENT × PHONEME ---")
    print(f"  Pearson r = {r_cp:+.4f}")
    print(f"  Spearman ρ = {rho_cp:+.4f}")

    # Pearson + Spearman: rhyme vs phoneme (sanity check — same direction)
    r_rp = pearson_r(d_rhyme, d_phoneme)
    rho_rp = spearman_rho(d_rhyme, d_phoneme)
    print(f"\n--- RHYME × PHONEME (sanity, expect positive) ---")
    print(f"  Pearson r = {r_rp:+.4f}")
    print(f"  Spearman ρ = {rho_rp:+.4f}")

    # Permutation null on r_cr
    print(f"\n--- PERMUTATION NULL on r(content × rhyme) ({N_PERMS} perms) ---")
    rng = random.Random(SEED)
    null_rs = []
    for _ in range(N_PERMS):
        shuffled = d_rhyme[:]
        rng.shuffle(shuffled)
        null_rs.append(pearson_r(d_content, shuffled))
    p_emp = sum(1 for r in null_rs if r <= r_cr) / len(null_rs)  # one-sided lower (negative direction)
    print(f"  p(r ≤ observed) = {p_emp:.5f}")

    # Verdict
    alpha_bon = 0.025
    strict = r_cr <= -0.60 and p_emp <= alpha_bon and rho_cr <= -0.55
    directional = r_cr <= -0.40 and p_emp <= 0.05
    if strict:
        verdict = f"STRICT PASS — anti-twinning empirically locked: r={r_cr:.4f}, ρ={rho_cr:.4f}, p={p_emp:.5f}"
    elif directional:
        verdict = f"DIRECTIONAL — anti-twinning supported: r={r_cr:.4f}, ρ={rho_cr:.4f}, p={p_emp:.5f}"
    else:
        verdict = f"NULL — r={r_cr:.4f}, p={p_emp:.5f}"
    print(f"\n=== VERDICT (content × rhyme): {verdict} ===")

    # Best/worst windows by joint anti-twin signature
    # iʿjāz signature = (high d_rhyme) − (high d_content), normalized
    # Convert to z-scores
    def zscore(arr):
        m = sum(arr)/len(arr)
        sd = math.sqrt(sum((x-m)**2 for x in arr)/len(arr))
        return [(x-m)/sd for x in arr]
    z_content = zscore(d_content)
    z_rhyme = zscore(d_rhyme)
    # Anti-twin score: high z_rhyme + low z_content
    iʿjāz_signature = [z_rhyme[i] - z_content[i] for i in range(len(d_content))]
    pairs = sorted(enumerate(iʿjāz_signature), key=lambda p: -p[1])
    print(f"\n--- TOP-5 highest iʿjāz-signature windows (rhyme dispersed + content cohesive) ---")
    for rank, (i, sig) in enumerate(pairs[:5], 1):
        s = starts[i]
        print(f"  #{rank}: window Q{s}-{s+K-1}: content d̄={d_content[i]:.4f}, rhyme d̄={d_rhyme[i]:.4f}, z-sum={sig:+.3f}")
    print(f"\n--- BOTTOM-5 lowest iʿjāz-signature (anti-iʿjāz: rhyme uniform + content dispersed) ---")
    for rank, (i, sig) in enumerate(pairs[-5:], 1):
        s = starts[i]
        print(f"  #{len(pairs)-5+rank}: window Q{s}-{s+K-1}: content d̄={d_content[i]:.4f}, rhyme d̄={d_rhyme[i]:.4f}, z-sum={sig:+.3f}")

    out = {
        "id": "H-NEW-730",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "starts": starts,
        "d_content": d_content,
        "d_rhyme": d_rhyme,
        "d_phoneme": d_phoneme,
        "content_x_rhyme": {"pearson_r": r_cr, "spearman_rho": rho_cr, "perm_p": p_emp, "alpha_bon": alpha_bon},
        "content_x_phoneme": {"pearson_r": r_cp, "spearman_rho": rho_cp},
        "rhyme_x_phoneme_sanity": {"pearson_r": r_rp, "spearman_rho": rho_rp},
        "iʿjāz_signature": iʿjāz_signature,
        "iʿjāz_top5_windows": [{"start": starts[pairs[i][0]], "z_sum": pairs[i][1]} for i in range(5)],
        "iʿjāz_bottom5_windows": [{"start": starts[pairs[-i-1][0]], "z_sum": pairs[-i-1][1]} for i in range(5)],
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
