#!/usr/bin/env python3
"""H-NEW-1360 — yā-ayyuhā al-nabī 6-surah prophet-vocative cluster Fisher-Rao cohesion.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-1360-prophet-vocative.md
Seed: 20260509; n_perm: 10000; α_bon: 0.025 (k=2 Bonferroni); direction one-sided LOWER.
"""

import hashlib
import json
import random
import re
import sys
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1360-prophet-vocative.md"
EXPECTED_SHA = "b82d6c917feb0a34c9a8f8de30302b7124766d6318736843efccbbd0c8273578"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1360.json"
SEED = 20260509
N_PERM = 10_000

# Locked cluster (verified by regex over no-tashkeel corpus, see pre-reg):
CLUSTER = [8, 9, 33, 60, 65, 66]

# MW-5 PC sub-sample (fixed in dispatch prompt; deterministic):
PC = [69, 97, 101]


def main():
    actual_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual_sha != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")

    # ----- corpus reverify of cluster membership (safety net) -----
    text = json.loads(QURAN.read_text())
    pat = re.compile(r"يا\s*أيها\s*النبي")
    found = sorted({int(s["id"]) for s in text for v in s["verses"] if pat.search(v.get("text", ""))})
    if found != CLUSTER:
        sys.exit(f"Cluster verification failed: corpus regex returned {found}, pre-reg locked {CLUSTER}")

    # ----- load FR matrix -----
    h111 = json.loads(FR_MATRIX.read_text())
    D = [[0.0] * 115 for _ in range(115)]
    for a, b, d in h111["D_matrix_upper_triangular"]:
        D[a][b] = D[b][a] = d
    vc = {int(s["id"]): len(s["verses"]) for s in text}

    def mi(group):
        pairs = [D[a][b] for i, a in enumerate(group) for b in group[i + 1:]]
        return mean(pairs)

    obs = mi(CLUSTER)

    # ----- Cell A: uniform null -----
    rng_a = random.Random(SEED)
    pool = list(range(1, 115))
    a_n = [mi(rng_a.sample(pool, len(CLUSTER))) for _ in range(N_PERM)]
    p_a = sum(1 for x in a_n if x <= obs) / N_PERM

    # ----- Cell B: length-matched null (±20%) -----
    target = sum(vc[s] for s in CLUSTER)
    lo, hi = target * 0.8, target * 1.2
    rng_b = random.Random(SEED + 2)
    b_n = []
    tries = 0
    while len(b_n) < N_PERM and tries < N_PERM * 500:
        s = rng_b.sample(pool, len(CLUSTER))
        if lo <= sum(vc[x] for x in s) <= hi:
            b_n.append(mi(s))
        tries += 1
    p_b = sum(1 for x in b_n if x <= obs) / max(1, len(b_n))

    # ----- MW-5 PC: H-NEW-1190 sub-sample {69, 97, 101} -----
    pc_obs = mi(PC)
    rng_pc = random.Random(SEED + 3)
    pc_n = [mi(rng_pc.sample(pool, len(PC))) for _ in range(N_PERM)]
    p_pc = sum(1 for x in pc_n if x <= pc_obs) / N_PERM

    # ----- verdict -----
    a_pass = p_a <= 0.025
    b_pass = p_b <= 0.025
    pc_pass = p_pc <= 0.05

    if not pc_pass:
        verdict = "NULL-BROKEN (PC failed)"
    elif a_pass and b_pass:
        verdict = "PASS-DIRECTED"
    elif a_pass and not b_pass:
        verdict = "DESCRIPTIVE-ONLY (length confound)"
    elif b_pass and not a_pass:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    # ----- pairwise FR diagnostics inside cluster -----
    pairs_detail = []
    for i, a in enumerate(CLUSTER):
        for b in CLUSTER[i + 1:]:
            pairs_detail.append({"a": a, "b": b, "fr": D[a][b]})
    pairs_detail.sort(key=lambda r: r["fr"])

    out = {
        "id": "H-NEW-1360",
        "title": "yā-ayyuhā al-nabī prophet-vocative 6-surah cluster Fisher-Rao cohesion",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cluster": CLUSTER,
        "cluster_verse_counts": {s: vc[s] for s in CLUSTER},
        "cluster_total_verses": target,
        "obs_intra_mean_fr": obs,
        "cell_A_uniform": {
            "p": p_a,
            "null_mean": mean(a_n),
            "null_p5": sorted(a_n)[int(0.05 * len(a_n))],
            "pass": a_pass,
            "n_perm": len(a_n),
        },
        "cell_B_length_matched": {
            "p": p_b,
            "null_mean": mean(b_n),
            "null_p5": sorted(b_n)[int(0.05 * len(b_n))],
            "pass": b_pass,
            "n_perm": len(b_n),
            "length_window": [lo, hi],
        },
        "MW5_PC": {
            "subsample": PC,
            "pc_obs": pc_obs,
            "p_pc": p_pc,
            "pass": pc_pass,
        },
        "pairs_detail": pairs_detail,
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Verdict: {verdict}")
    print(f"  obs intra-mean FR = {obs:.4f}")
    print(f"  Cell A (uniform)         p = {p_a:.4f}  null_mean = {mean(a_n):.4f}  pass={a_pass}")
    print(f"  Cell B (length-matched)  p = {p_b:.4f}  null_mean = {mean(b_n):.4f}  n={len(b_n)}  pass={b_pass}")
    print(f"  MW-5 PC {{69,97,101}}      p = {p_pc:.4f}  pc_obs = {pc_obs:.4f}  pass={pc_pass}")


if __name__ == "__main__":
    main()
