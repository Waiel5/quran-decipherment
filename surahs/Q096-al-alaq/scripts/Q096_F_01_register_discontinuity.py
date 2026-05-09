#!/usr/bin/env python3
"""Q096-F-01 — vv 1-5 vs vv 6-19 register-discontinuity at root distribution.

Pre-reg: Q096-F-01-vv1-5-vs-6-19-register-prereg.md
SHA256:  a00c71629c45f6797fe9093453d7aa20ec553838b66a6e847229a33bbaabfc5f
Seed:    20260509
"""
import hashlib
import json
import math
import random
from collections import Counter
from itertools import combinations
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PREREG = REPO / "surahs/Q096-al-alaq/preregs/Q096-F-01-vv1-5-vs-6-19-register-prereg.md"
EXPECTED_SHA = "a00c71629c45f6797fe9093453d7aa20ec553838b66a6e847229a33bbaabfc5f"
MORPH = REPO / "data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = REPO / "surahs/Q096-al-alaq/csv/q096-f-01.json"
SEED = 20260509
ALPHA = 0.5  # Jeffreys/Dirichlet smoothing

random.seed(SEED)


def verify_sha():
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        raise SystemExit(f"PREREG SHA mismatch: {sha} != {EXPECTED_SHA}")


def load_qac_roots_per_verse(surah, n_verses):
    """Return list of root multisets, one per verse."""
    roots = [[] for _ in range(n_verses)]
    with open(MORPH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if not line.startswith(f"({surah}:"):
                continue
            # (96:1:1:1)\tform\tPOS\tFEATURES
            try:
                ref, form, pos, feats = line.split("\t")
            except ValueError:
                continue
            # only keep STEM tokens with ROOT
            if "STEM" not in feats or "ROOT:" not in feats:
                continue
            ref = ref.strip("()")
            s, v, w, seg = (int(x) for x in ref.split(":"))
            if s != surah:
                continue
            for kv in feats.split("|"):
                if kv.startswith("ROOT:"):
                    root = kv[5:]
                    roots[v - 1].append(root)
                    break
    return roots


def js_divergence(roots_a, roots_b):
    """Jensen-Shannon divergence (in nats) on root multinomials with Dirichlet smoothing."""
    counts_a = Counter(r for v in roots_a for r in v)
    counts_b = Counter(r for v in roots_b for r in v)
    vocab = set(counts_a) | set(counts_b)
    V = len(vocab)
    n_a = sum(counts_a.values()) + ALPHA * V
    n_b = sum(counts_b.values()) + ALPHA * V
    p = {r: (counts_a.get(r, 0) + ALPHA) / n_a for r in vocab}
    q = {r: (counts_b.get(r, 0) + ALPHA) / n_b for r in vocab}
    m = {r: 0.5 * (p[r] + q[r]) for r in vocab}

    def kl(d1, d2):
        return sum(d1[r] * math.log(d1[r] / d2[r]) for r in vocab if d1[r] > 0 and d2[r] > 0)

    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def run_q96():
    n_verses = 19
    verse_roots = load_qac_roots_per_verse(96, n_verses)
    block_a = verse_roots[:5]
    block_b = verse_roots[5:]
    obs_js = js_divergence(block_a, block_b)

    # Cell A — all C(19,5) = 11628 contiguous-block splits (only block-of-5-contiguous against complement)
    contiguous_splits = []
    for start in range(0, n_verses - 4):  # contiguous block of 5
        chosen = list(range(start, start + 5))
        rest = [i for i in range(n_verses) if i not in chosen]
        block_chosen = [verse_roots[i] for i in chosen]
        block_rest = [verse_roots[i] for i in rest]
        d = js_divergence(block_chosen, block_rest)
        contiguous_splits.append((tuple(chosen), d))
    contiguous_sorted = sorted(contiguous_splits, key=lambda x: -x[1])  # descending JS
    # rank of vv 1-5 split
    obs_split = tuple(range(0, 5))
    # find rank (1-based, where rank 1 = highest JS)
    rank_contiguous = next(i for i, (k, _) in enumerate(contiguous_sorted, start=1) if k == obs_split)
    n_contiguous = len(contiguous_splits)
    p_cell_A = rank_contiguous / n_contiguous

    # Cell B — 10000 random non-contiguous 5/14 partitions
    random.seed(SEED)
    n_perm_B = 10000
    n_ge = 0
    for _ in range(n_perm_B):
        chosen = random.sample(range(n_verses), 5)
        rest = [i for i in range(n_verses) if i not in chosen]
        block_chosen = [verse_roots[i] for i in chosen]
        block_rest = [verse_roots[i] for i in rest]
        d = js_divergence(block_chosen, block_rest)
        if d >= obs_js:
            n_ge += 1
    p_cell_B = (n_ge + 1) / (n_perm_B + 1)  # + 1 smoothing

    # MW-5 positive control: Q 19 Maryam vv 1-40 vs vv 41-98
    n_q19 = 98
    q19_roots = load_qac_roots_per_verse(19, n_q19)
    obs_js_q19 = js_divergence(q19_roots[:40], q19_roots[40:])
    # Random 40/58 partition null
    random.seed(SEED + 1)
    n_ge_pc = 0
    for _ in range(n_perm_B):
        chosen = set(random.sample(range(n_q19), 40))
        b1 = [q19_roots[i] for i in chosen]
        b2 = [q19_roots[i] for i in range(n_q19) if i not in chosen]
        d = js_divergence(b1, b2)
        if d >= obs_js_q19:
            n_ge_pc += 1
    p_pc = (n_ge_pc + 1) / (n_perm_B + 1)

    pass_a = p_cell_A <= 0.025
    pass_b = p_cell_B <= 0.025
    pass_pc = p_pc <= 0.025

    if not pass_pc:
        verdict = "NULL-BROKEN (positive control failed)"
    elif pass_a and pass_b:
        verdict = "PASS-DIRECTED (both cells)"
    elif pass_a:
        verdict = "WEAKER-DIRECTED (Cell A only — contiguous-block boundary informative; absolute discontinuity moderate)"
    elif pass_b:
        verdict = "ANOMALOUS (Cell B only — flag for review)"
    else:
        verdict = "NULL"

    out = {
        "id": "Q096-F-01",
        "title": "Q 96 vv 1-5 vs vv 6-19 register-discontinuity",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_verses_q96": n_verses,
        "block_a_verses": list(range(1, 6)),
        "block_b_verses": list(range(6, 20)),
        "obs_js_divergence": obs_js,
        "cell_A_contiguous_block_null": {
            "n_splits": n_contiguous,
            "rank_observed": rank_contiguous,
            "p_perm": p_cell_A,
            "alpha_bon": 0.025,
            "pass": pass_a,
        },
        "cell_B_random_split_null": {
            "n_perm": n_perm_B,
            "n_ge": n_ge,
            "p_perm": p_cell_B,
            "alpha_bon": 0.025,
            "pass": pass_b,
        },
        "mw5_positive_control_q19": {
            "obs_js": obs_js_q19,
            "n_perm": n_perm_B,
            "n_ge": n_ge_pc,
            "p_perm": p_pc,
            "pass": pass_pc,
        },
        "bonferroni_k": 2,
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(json.dumps(out, indent=2, ensure_ascii=False)[:1500])


if __name__ == "__main__":
    verify_sha()
    run_q96()
