#!/usr/bin/env python3
"""
Q060-F-01 — Q 60 short-Medinan-block (H-NEW-1080) embedding test.

Pre-reg SHA256: 8054270de97a8224de1e0cf229e9d7cbd9842fcd5ac3af128209c38d19401c9c

Hypothesis (locked direction LOWER):
  Q 60's mean Fisher-Rao distance to the other 9 members of Q 57-66 is
  LOWER than the mean distance from Q 60 to a random 9-subset of the corpus.

Decision rule: PASS at α_bon = 0.05 (single-test).
"""
import json
import statistics
import random
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PREREG_SHA = "8054270de97a8224de1e0cf229e9d7cbd9842fcd5ac3af128209c38d19401c9c"
SEED = 20260509
N_PERM = 10000

def verify_prereg_sha(prereg_path):
    h = hashlib.sha256(prereg_path.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        raise RuntimeError(f"Pre-reg SHA mismatch: expected {PREREG_SHA}, got {h}")
    return h

def main():
    prereg_path = REPO_ROOT / "surahs" / "Q060-al-mumtahana" / "preregs" / "Q060-F-01-block-embedding-prereg.md"
    sha_check = verify_prereg_sha(prereg_path)
    print(f"Pre-reg SHA verified: {sha_check[:16]}...")

    h111_path = REPO_ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
    h111 = json.load(open(h111_path))
    D = [[0.0] * 115 for _ in range(115)]
    for a, b, dist in h111["D_matrix_upper_triangular"]:
        D[a][b] = dist
        D[b][a] = dist

    short_medinan = list(range(57, 67))  # Q 57-66
    others_block = [s for s in short_medinan if s != 60]
    obs = statistics.mean(D[60][s] for s in others_block)
    print(f"Q 60 mean-to-block (Q 57-66 minus Q 60): {obs:.4f}")

    random.seed(SEED)
    candidates = [s for s in range(1, 115) if s != 60]
    nulls = []
    for _ in range(N_PERM):
        sample = random.sample(candidates, 9)
        nulls.append(statistics.mean(D[60][s] for s in sample))

    null_mean = statistics.mean(nulls)
    null_sd = statistics.stdev(nulls)
    z = (obs - null_mean) / null_sd
    p_lower = sum(1 for n in nulls if n <= obs) / N_PERM
    print(f"Null mean: {null_mean:.4f}  SD: {null_sd:.4f}")
    print(f"z = {z:.4f}, p_lower = {p_lower:.6f}")

    verdict = "PASS" if p_lower <= 0.05 else "NULL"
    print(f"Verdict: {verdict}")

    # Centrality rank within block
    ranking = []
    for s in short_medinan:
        m = statistics.mean(D[s][x] for x in short_medinan if x != s)
        ranking.append((s, m))
    ranking.sort(key=lambda x: x[1])
    q60_rank = next(r for r, (s, _) in enumerate(ranking, 1) if s == 60)
    print(f"Q 60 within-block centrality rank: {q60_rank}/10 (lower = more central)")

    # Substitutability percentile
    non_block = [s for s in range(1, 115) if s not in short_medinan]
    candidates_means = [(60, obs)] + [
        (X, statistics.mean(D[X][s] for s in others_block)) for X in non_block
    ]
    candidates_means.sort(key=lambda x: x[1])
    sub_rank = next(r for r, (s, _) in enumerate(candidates_means, 1) if s == 60)
    sub_pct = sub_rank / len(candidates_means)
    print(f"Q 60 substitutability rank: {sub_rank}/{len(candidates_means)} ({sub_pct*100:.1f}%-tile)")

    return {
        "obs": obs,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "z": z,
        "p_lower": p_lower,
        "verdict": verdict,
        "centrality_rank": q60_rank,
        "substitutability_rank": sub_rank,
        "substitutability_pct": sub_pct,
    }

if __name__ == "__main__":
    main()
