#!/usr/bin/env python3
"""Q096-F-02 — corpus-hapax-root and rare-root density in Q 96.

Pre-reg: Q096-F-02-hapax-density-prereg.md
SHA256:  a2df036101f4086f293bb3a5dc1f4733678d7cdd90c8043575e3d64f37393eb5
Seed:    20260509
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PREREG = REPO / "surahs/Q096-al-alaq/preregs/Q096-F-02-hapax-density-prereg.md"
EXPECTED_SHA = "a2df036101f4086f293bb3a5dc1f4733678d7cdd90c8043575e3d64f37393eb5"
ROOT_INDEX = REPO / "data/morphology/root-index.json"
MORPH = REPO / "data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN = REPO / "quran-text/quran-no-tashkeel.json"
REV = REPO / "data/revelation-order.csv"
OUT = REPO / "surahs/Q096-al-alaq/csv/q096-f-02.json"
SEED = 20260509


def verify_sha():
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        raise SystemExit(f"PREREG SHA mismatch: {sha} != {EXPECTED_SHA}")


def load_root_freqs():
    """Return {root: corpus-frequency}."""
    with open(ROOT_INDEX) as f:
        idx = json.load(f)
    return {r: len(occs) for r, occs in idx.items()}


def load_surah_roots(n_surahs=114):
    """Return {surah_id: list of (verse, word, root)} STEM tokens with ROOT only."""
    out = {s: [] for s in range(1, n_surahs + 1)}
    with open(MORPH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                ref, form, pos, feats = line.split("\t")
            except ValueError:
                continue
            if "STEM" not in feats or "ROOT:" not in feats:
                continue
            ref = ref.strip("()")
            s, v, w, seg = (int(x) for x in ref.split(":"))
            for kv in feats.split("|"):
                if kv.startswith("ROOT:"):
                    root = kv[5:]
                    out[s].append((v, w, root))
                    break
    return out


def load_period_map():
    """Return {surah_id: noldeke_phase}."""
    out = {}
    with open(REV) as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            sid = int(r["mushaf_order"])
            out[sid] = (r.get("period", ""), r.get("noldeke_phase", ""))
    return out


def load_verse_counts():
    with open(QURAN) as f:
        q = json.load(f)
    return {s["id"]: s["total_verses"] for s in q}


def density_for_surah(roots_in_s, root_freq, hapax_thresh=1, rare_thresh=5):
    """Return (n_hapax_token, n_rare_token, n_total_with_root)."""
    n_total = len(roots_in_s)
    n_hapax = sum(1 for (_, _, r) in roots_in_s if root_freq.get(r, 99) <= hapax_thresh)
    n_rare = sum(1 for (_, _, r) in roots_in_s if root_freq.get(r, 99) <= rare_thresh)
    return n_hapax, n_rare, n_total


def run():
    root_freq = load_root_freqs()
    surah_roots = load_surah_roots()
    periods = load_period_map()
    verses = load_verse_counts()

    # Build comparator pool — Meccan-period + verse-count in [15, 25] (locked window)
    pool = []
    for sid in range(1, 115):
        period_label, noldeke_phase = periods.get(sid, ("", ""))
        if period_label != "Meccan":
            continue
        if not (15 <= verses[sid] <= 25):
            continue
        pool.append(sid)

    # Compute density for each pool member
    densities = {}
    for sid in pool:
        n_hapax, n_rare, n_total = density_for_surah(surah_roots[sid], root_freq)
        if n_total == 0:
            continue
        densities[sid] = {
            "frac_hapax": n_hapax / n_total,
            "frac_rare": n_rare / n_total,
            "n_hapax_token": n_hapax,
            "n_rare_token": n_rare,
            "n_total_token": n_total,
        }

    q96 = densities[96]
    pool_ids = sorted(densities.keys())

    # Cell A — frac_hapax rank
    sorted_hapax = sorted(densities.items(), key=lambda x: -x[1]["frac_hapax"])
    rank_hapax = next(i for i, (sid, _) in enumerate(sorted_hapax, start=1) if sid == 96)
    p_A = rank_hapax / len(pool_ids)

    # Cell B — frac_rare rank
    sorted_rare = sorted(densities.items(), key=lambda x: -x[1]["frac_rare"])
    rank_rare = next(i for i, (sid, _) in enumerate(sorted_rare, start=1) if sid == 96)
    p_B = rank_rare / len(pool_ids)

    # MW-5 positive control: Q 113 al-Falaq with [3,7] window
    pc_pool = []
    for sid in range(1, 115):
        period_label, _ = periods.get(sid, ("", ""))
        if period_label != "Meccan":
            continue
        if not (3 <= verses[sid] <= 7):
            continue
        n_hapax, n_rare, n_total = density_for_surah(surah_roots[sid], root_freq)
        if n_total == 0:
            continue
        pc_pool.append((sid, n_hapax / n_total, n_rare / n_total))
    pc_sorted_rare = sorted(pc_pool, key=lambda x: -x[2])
    rank_pc = next(i for i, (sid, _, _) in enumerate(pc_sorted_rare, start=1) if sid == 113)
    p_pc = rank_pc / len(pc_pool)

    pass_a = p_A <= 0.025
    pass_b = p_B <= 0.025
    pass_pc = p_pc <= 0.05  # positive control single-test

    if not pass_pc:
        verdict = "NULL-BROKEN (positive control failed)"
    elif pass_a and pass_b:
        verdict = "PASS-DIRECTED (both cells)"
    elif pass_a:
        verdict = "WEAKER-DIRECTED (Cell A hapax only)"
    elif pass_b:
        verdict = "WEAKER-DIRECTED (Cell B rare only)"
    else:
        verdict = "NULL"

    out = {
        "id": "Q096-F-02",
        "title": "Q 96 corpus-hapax-root and rare-root density",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "comparator_pool_size": len(pool_ids),
        "comparator_pool": pool_ids,
        "q96_metrics": q96,
        "cell_A_hapax": {
            "rank": rank_hapax,
            "out_of": len(pool_ids),
            "p_perm": p_A,
            "alpha_bon": 0.025,
            "pass": pass_a,
        },
        "cell_B_rare": {
            "rank": rank_rare,
            "out_of": len(pool_ids),
            "p_perm": p_B,
            "alpha_bon": 0.025,
            "pass": pass_b,
        },
        "mw5_positive_control_q113": {
            "rank": rank_pc,
            "out_of": len(pc_pool),
            "p_perm": p_pc,
            "pass": pass_pc,
        },
        "bonferroni_k": 2,
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
        "top_5_hapax_density": [
            {"surah": sid, "frac_hapax": d["frac_hapax"], "n_hapax": d["n_hapax_token"], "n_total": d["n_total_token"]}
            for sid, d in sorted_hapax[:5]
        ],
        "top_5_rare_density": [
            {"surah": sid, "frac_rare": d["frac_rare"], "n_rare": d["n_rare_token"], "n_total": d["n_total_token"]}
            for sid, d in sorted_rare[:5]
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(json.dumps(out, indent=2, ensure_ascii=False)[:2000])


if __name__ == "__main__":
    verify_sha()
    run()
