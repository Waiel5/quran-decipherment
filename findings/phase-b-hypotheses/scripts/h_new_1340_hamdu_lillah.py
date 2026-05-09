#!/usr/bin/env python3
"""H-NEW-1340 — al-ḥamdu li-llāh opener 5-cluster Fisher-Rao cohesion."""

import hashlib, json, random, sys
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1340-hamdu-lillah-cluster-prereg.md"
EXPECTED_SHA = "9f5b5e9427e02c0ba6b7be5742071d3ecb1bd8375b1e646604b2bdfd6d6fa788"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1340.json"
SEED = 20260509
N_PERM = 10_000

CLUSTER = [1, 6, 18, 34, 35]
ADRAKA = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]


def main():
    actual_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual_sha != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual_sha}")
    h111 = json.loads(FR_MATRIX.read_text())
    D = [[0.0]*115 for _ in range(115)]
    for a, b, dist in h111["D_matrix_upper_triangular"]:
        D[a][b] = D[b][a] = dist
    text = json.loads(QURAN.read_text())
    vc = {int(e["id"]): int(e.get("total_verses") or len(e.get("verses", []))) for e in text}

    def mi(g):
        ps = [D[a][b] for i,a in enumerate(g) for b in g[i+1:]]
        return mean(ps)

    obs = mi(CLUSTER)
    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED+2)
    rng_pc = random.Random(SEED+3)
    pool = list(range(1, 115))

    a_n = [mi(rng_a.sample(pool, len(CLUSTER))) for _ in range(N_PERM)]
    p_a = sum(1 for x in a_n if x <= obs) / N_PERM

    target = sum(vc[s] for s in CLUSTER)
    lo, hi = target*0.8, target*1.2
    b_n = []
    tries = 0
    while len(b_n) < N_PERM and tries < N_PERM*200:
        s = rng_b.sample(pool, len(CLUSTER))
        if lo <= sum(vc[x] for x in s) <= hi:
            b_n.append(mi(s))
        tries += 1
    p_b = sum(1 for x in b_n if x <= obs) / max(1, len(b_n))

    pc_pick = sorted(random.Random(SEED).sample(ADRAKA, 5))
    pc_obs = mi(pc_pick)
    pc_n = [mi(rng_pc.sample(pool, 5)) for _ in range(N_PERM)]
    p_pc = sum(1 for x in pc_n if x <= pc_obs) / N_PERM

    pc_pass = p_pc <= 0.05
    a_pass = p_a <= 0.025
    b_pass = p_b <= 0.025

    if not pc_pass:
        v = "NULL-BROKEN (PC failed)"
    elif a_pass and b_pass:
        v = "PASS-DIRECTED"
    elif a_pass and not b_pass:
        v = "DESCRIPTIVE-ONLY (length confound)"
    elif b_pass:
        v = "PARTIAL"
    else:
        v = "NULL"

    out = {
        "id": "H-NEW-1340", "title": "al-ḥamdu li-llāh opener cluster {Q 1, 6, 18, 34, 35}",
        "prereg_sha": EXPECTED_SHA, "seed": SEED, "n_perm": N_PERM,
        "cluster": CLUSTER, "obs": obs, "verse_counts": {s: vc[s] for s in CLUSTER},
        "cell_A": {"p": p_a, "null_mean": mean(a_n), "null_p5": sorted(a_n)[int(0.05*len(a_n))], "pass": a_pass},
        "cell_B": {"p": p_b, "null_mean": mean(b_n), "null_p5": sorted(b_n)[int(0.05*len(b_n))], "pass": b_pass, "n": len(b_n)},
        "MW5_PC": {"subsample": pc_pick, "pc_obs": pc_obs, "p_pc": p_pc, "pass": pc_pass},
        "verdict": v,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Verdict: {v}\n  obs={obs:.4f}  cell A p={p_a:.4f}  cell B p={p_b:.4f}  PC p={p_pc:.4f}")


if __name__ == "__main__":
    main()
