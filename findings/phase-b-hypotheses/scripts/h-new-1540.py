#!/usr/bin/env python3
"""H-NEW-1540 — Hapax legomenon distribution across 114 surahs.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-1540-hapax-distribution.md
SHA-locked. Direction one-tailed upper. Bonferroni alpha_corr = 0.0167 (k=3 cells).
"""

import hashlib
import json
import random
import sys
from pathlib import Path
from statistics import mean, pstdev

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1540-hapax-distribution.md"
EXPECTED_SHA = "a8cecf09831dd054eb4e7b64cf1981f03998691e02e32ab5cc0b07a63b299a44"
ROOT_INDEX = ROOT / "data/morphology/root-index.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1540.json"
SEED = 20260509
N_PERM = 10_000
RATIO_THRESHOLD = 2.0
ALPHA_BONF = 0.05 / 3.0


def main():
    actual_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual_sha != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")

    ri = json.loads(ROOT_INDEX.read_text())
    text = json.loads(QURAN.read_text())

    # Hapax set = roots with exactly 1 attestation
    hapax_roots = {k: v for k, v in ri.items() if len(v) == 1}
    n_hapax_roots = len(hapax_roots)

    # Per-surah hapax count
    hapax_count = {s: 0 for s in range(1, 115)}
    for root, attests in hapax_roots.items():
        sid = int(attests[0][0])
        hapax_count[sid] += 1
    n_hapax_tokens = sum(hapax_count.values())

    # Per-surah word count
    word_count = {}
    for e in text:
        sid = int(e["id"])
        words = sum(len(v["text"].split()) for v in e["verses"])
        word_count[sid] = words

    total_words = sum(word_count.values())
    baseline = n_hapax_tokens / total_words

    # Per-surah density + ratio
    per_surah = []
    for s in range(1, 115):
        wc = word_count[s]
        hc = hapax_count[s]
        dens = hc / wc if wc > 0 else 0.0
        per_surah.append({
            "s": s,
            "word_count": wc,
            "hapax_count": hc,
            "density": dens,
            "ratio": dens / baseline if baseline > 0 else 0.0,
        })

    densities = [r["density"] for r in per_surah]
    obs_CV = pstdev(densities) / mean(densities)
    obs_max_density = max(densities)
    obs_max_surah = per_surah[densities.index(obs_max_density)]["s"]
    obs_n_above_2x = sum(1 for r in per_surah if r["ratio"] >= RATIO_THRESHOLD)

    # Length-proportional null:
    # Distribute n_hapax_tokens across 114 surahs with probability ~ word_count.
    weights = [word_count[s] for s in range(1, 115)]
    rng = random.Random(SEED)

    null_CV = []
    null_max = []
    null_count = []

    for _ in range(N_PERM):
        counts = [0] * 114
        for _t in range(n_hapax_tokens):
            # random.choices is weighted; use single-draw form for determinism via rng.choices
            idx = rng.choices(range(114), weights=weights, k=1)[0]
            counts[idx] += 1
        dens_null = [counts[i] / weights[i] for i in range(114)]
        cv = pstdev(dens_null) / mean(dens_null) if mean(dens_null) > 0 else 0.0
        mx = max(dens_null)
        ratio_null = [d / baseline for d in dens_null]
        cnt = sum(1 for r in ratio_null if r >= RATIO_THRESHOLD)
        null_CV.append(cv)
        null_max.append(mx)
        null_count.append(cnt)

    p_CV = sum(1 for x in null_CV if x >= obs_CV) / N_PERM
    p_max = sum(1 for x in null_max if x >= obs_max_density) / N_PERM
    p_count = sum(1 for x in null_count if x >= obs_n_above_2x) / N_PERM

    pass_CV = p_CV <= ALPHA_BONF
    pass_max = p_max <= ALPHA_BONF
    pass_count = p_count <= ALPHA_BONF

    n_passing = sum([pass_CV, pass_max, pass_count])
    if n_passing == 3 and obs_n_above_2x >= 3:
        verdict = "PASS-DIRECTED"
    elif n_passing == 2:
        verdict = "PARTIAL"
    elif n_passing == 1:
        verdict = "DESCRIPTIVE-ONLY"
    else:
        verdict = "NULL"

    # Reverse-direction check
    reverse_flag = False
    if obs_CV < mean(null_CV):
        reverse_flag = True
        verdict = "NULL (pre-commit reverse direction: CV below null mean)"

    # Sensitivity: equal-probability null
    null_CV_eq = []
    null_max_eq = []
    null_count_eq = []
    rng2 = random.Random(SEED + 1)
    for _ in range(N_PERM):
        counts = [0] * 114
        for _t in range(n_hapax_tokens):
            idx = rng2.randrange(114)
            counts[idx] += 1
        dens_null = [counts[i] / weights[i] for i in range(114)]
        cv = pstdev(dens_null) / mean(dens_null) if mean(dens_null) > 0 else 0.0
        ratio_null = [d / baseline for d in dens_null]
        null_CV_eq.append(cv)
        null_max_eq.append(max(dens_null))
        null_count_eq.append(sum(1 for r in ratio_null if r >= RATIO_THRESHOLD))

    p_CV_eq = sum(1 for x in null_CV_eq if x >= obs_CV) / N_PERM
    p_max_eq = sum(1 for x in null_max_eq if x >= obs_max_density) / N_PERM
    p_count_eq = sum(1 for x in null_count_eq if x >= obs_n_above_2x) / N_PERM

    top10 = sorted(per_surah, key=lambda r: -r["density"])[:10]
    bottom10 = sorted(per_surah, key=lambda r: r["density"])[:10]

    def pct(arr, p):
        a = sorted(arr)
        return a[int(p * len(a))]

    out = {
        "id": "H-NEW-1540",
        "title": "Hapax legomenon distribution across 114 surahs",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "n_hapax_roots": n_hapax_roots,
        "n_hapax_tokens": n_hapax_tokens,
        "n_total_roots": len(ri),
        "n_total_words": total_words,
        "baseline_density": baseline,
        "ratio_threshold": RATIO_THRESHOLD,
        "alpha_bonf": ALPHA_BONF,
        "obs_CV": obs_CV,
        "obs_max_density": obs_max_density,
        "obs_max_surah": obs_max_surah,
        "obs_n_above_2x": obs_n_above_2x,
        "cell_CV": {
            "p": p_CV,
            "null_mean": mean(null_CV),
            "null_p95": pct(null_CV, 0.95),
            "null_p99": pct(null_CV, 0.99),
            "pass": pass_CV,
        },
        "cell_max": {
            "p": p_max,
            "null_mean": mean(null_max),
            "null_p95": pct(null_max, 0.95),
            "null_p99": pct(null_max, 0.99),
            "pass": pass_max,
        },
        "cell_count": {
            "p": p_count,
            "null_mean": mean(null_count),
            "null_p95": pct(null_count, 0.95),
            "null_p99": pct(null_count, 0.99),
            "pass": pass_count,
        },
        "equal_probability_null_sensitivity": {
            "p_CV": p_CV_eq,
            "p_max": p_max_eq,
            "p_count": p_count_eq,
        },
        "reverse_direction_flag": reverse_flag,
        "verdict": verdict,
        "top10_by_density": top10,
        "bottom10_by_density": bottom10,
        "per_surah": per_surah,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print(f"H-NEW-1540 verdict: {verdict}")
    print(f"  n_hapax_roots = {n_hapax_roots}")
    print(f"  n_hapax_tokens = {n_hapax_tokens}")
    print(f"  baseline_density = {baseline:.6f}")
    print(f"  obs_CV = {obs_CV:.4f}  p={p_CV:.4f}  pass={pass_CV}")
    print(f"  obs_max_density = {obs_max_density:.6f} (Q{obs_max_surah})  p={p_max:.4f}  pass={pass_max}")
    print(f"  obs_n_above_2x = {obs_n_above_2x}  p={p_count:.4f}  pass={pass_count}")
    print(f"  Top 10 by hapax density:")
    for r in top10:
        print(f"    Q{r['s']:>3}  wc={r['word_count']:>5}  hapax={r['hapax_count']:>3}  density={r['density']:.5f}  ratio={r['ratio']:.2f}x")
    print(f"  Bottom 10 by hapax density:")
    for r in bottom10:
        print(f"    Q{r['s']:>3}  wc={r['word_count']:>5}  hapax={r['hapax_count']:>3}  density={r['density']:.5f}  ratio={r['ratio']:.2f}x")


if __name__ == "__main__":
    main()
