#!/usr/bin/env python3
"""H-NEW-93 — Q 29 al-ʿAnkabūt + Q 30 al-Rūm TEST-AND-PROPHECY sub-pattern.

Pre-reg:
    findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern-prereg.md

Design: 4-cell permutation test (seed=20260417, 10,000 perms each).
  (a) test-of-believers root density: {ftn, blw, mHn, Sbr}
  (b) historical-prophecy root density: {glb, nSr, kwn(past-perf lemma kaAna), ywm}
      secondary: glb-only; glb+nSr-only
  (c) Allah-density control: {Alh}
  (d) eschatological density: {Axr, bEv, Hsb, jzy}

Per-cell: target (Q29+30) vs (1) other-الم (Q2,3,31,32), (2) Meccan non-muq (n=60).
MW-5 positive control: other-الم vs Meccan non-muq for cells (a) and (b).

Bonferroni-4, α_bon = 0.0125.
Single-test α = 0.05 cap (post-hoc-noticed).
Verdict ceiling: PASS-DIRECTED until independent replication.
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(ROOT / "analysis"))
from tools.loader import load_quran  # noqa: E402

SEED = 20260417
N_PERM = 10000
BON_K = 4
ALPHA_BON = 0.05 / BON_K
ALPHA_SINGLE_CAP = 0.05

# Locked groups
TARGET = (29, 30)                # Q29 al-ʿAnkabūt, Q30 al-Rūm
OTHER_ALIF_LAM_MIM = (2, 3, 31, 32)

MUQ_SURAHS = frozenset({
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68
})

# --- paths ---
QAC = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
ROOT_STATS = ROOT / "data/morphology/root-stats.csv"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-93.json"

# --- Root cells (pre-reg-locked) ---
CELL_A_TEST = frozenset({"ftn", "blw", "mHn", "Sbr"})
CELL_B_HIST_FULL = frozenset({"glb", "nSr", "kwn", "ywm"})
CELL_B_HIST_GLB_ONLY = frozenset({"glb"})
CELL_B_HIST_GLB_NSR = frozenset({"glb", "nSr"})
CELL_C_ALLAH = frozenset({"Alh"})
CELL_D_ESCHATO = frozenset({"Axr", "bEv", "Hsb", "jzy"})

# kwn filter: only count tokens whose LEMMA is 'kaAna' (past-tense copula/historical).
# This is pre-committed in the pre-reg.
KWN_LEMMA_FILTER = frozenset({"kaAna"})


# --- Parse QAC ---

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")


def parse_qac(path: Path):
    """Return {sid: [(root, lemma), ...]} for all STEM tokens."""
    per_surah = defaultdict(list)
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            lm = LEM_RE.search(feat)
            root = rm.group(1)
            lemma = lm.group(1) if lm else ""
            per_surah[sid].append((root, lemma))
    return per_surah


# --- Density computation ---

def surah_density(tokens, root_set, lemma_filter=None, root_lemma_map=None):
    """Return (hits, total) for tokens whose ROOT is in root_set.

    root_lemma_map: optional {root: set-of-allowed-lemmas}. If root is in this map,
                    tokens with that root are only counted if their lemma is in the
                    allowed set.
    """
    total = len(tokens)
    if total == 0:
        return 0, 0, 0.0
    hits = 0
    for (rt, lm) in tokens:
        if rt in root_set:
            if root_lemma_map and rt in root_lemma_map:
                if lm not in root_lemma_map[rt]:
                    continue
            hits += 1
    return hits, total, (hits / total) if total else 0.0


# --- Permutation test ---

def perm_mean_diff(values_A, values_B, n_perm, seed, direction="two-sided"):
    """values_A, values_B: list of floats.
    Returns {observed_diff, p_two, p_one_A_gt_B, p_one_A_lt_B, null_diffs_summary}.
    """
    rng = random.Random(seed)
    n_A = len(values_A)
    pooled = list(values_A) + list(values_B)
    n_total = len(pooled)
    obs = (sum(values_A) / n_A) - (sum(values_B) / len(values_B))

    ge_abs = 0
    ge_signed = 0  # A > B
    le_signed = 0  # A < B
    for _ in range(n_perm):
        rng.shuffle(pooled)
        a = pooled[:n_A]
        b = pooled[n_A:]
        d = (sum(a) / n_A) - (sum(b) / len(b))
        if abs(d) >= abs(obs) - 1e-15:
            ge_abs += 1
        if d >= obs - 1e-15:
            ge_signed += 1
        if d <= obs + 1e-15:
            le_signed += 1
    # add-one smoothing for perms
    return {
        "observed_diff": obs,
        "mean_A": sum(values_A) / n_A,
        "mean_B": sum(values_B) / len(values_B),
        "n_A": n_A,
        "n_B": len(values_B),
        "p_two_sided": (ge_abs + 1) / (n_perm + 1),
        "p_one_sided_A_gt_B": (ge_signed + 1) / (n_perm + 1),
        "p_one_sided_A_lt_B": (le_signed + 1) / (n_perm + 1),
    }


# --- Verdict logic ---

def cell_verdict(p_two, p_one_pred, direction_predicted, alpha_bon, alpha_cap):
    """Apply Bonferroni-4 + single-test cap + direction-lock."""
    bon_pass = p_two < alpha_bon
    cap_pass = p_two < alpha_cap
    if not cap_pass:
        return "NULL"
    # Check direction via p_one_pred
    if p_one_pred >= 0.5:
        # reverse direction observed
        return "EXPLORATORY-REVERSE"
    if bon_pass:
        return "STRONG-PASS-DIRECTED"
    else:
        return "WEAK-PASS-DIRECTED-single-test-only"


# --- Main ---

def main():
    print("[H-NEW-93] loading QAC morphology ...", file=sys.stderr)
    qac = parse_qac(QAC)
    assert len(qac) == 114, f"expected 114 surahs in QAC, got {len(qac)}"

    # Load quran JSON for Meccan/Medinan metadata
    print("[H-NEW-93] loading quran JSON ...", file=sys.stderr)
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == 114
    stype = {s.id: s.type for s in surahs}
    sname = {s.id: s.transliteration for s in surahs}

    # Build Meccan non-muqaṭṭāʿat baseline
    meccan_ids = [sid for sid in range(1, 115) if stype[sid].lower() == "meccan"]
    meccan_non_muq = [sid for sid in meccan_ids if sid not in MUQ_SURAHS]
    print(f"[H-NEW-93] Meccan surahs: {len(meccan_ids)}; "
          f"Meccan non-muq: {len(meccan_non_muq)}", file=sys.stderr)

    # Sanity: check target/control group types
    for sid in TARGET + OTHER_ALIF_LAM_MIM:
        print(f"  Q{sid} ({sname[sid]:<15}) type={stype[sid]} "
              f"muq={sid in MUQ_SURAHS}", file=sys.stderr)

    # All density cells
    cells = {
        "a_test": {
            "label": "TEST-of-believers density",
            "roots": sorted(CELL_A_TEST),
            "root_set": CELL_A_TEST,
            "direction": "target > baseline",
            "pred_higher": True,
        },
        "b_hist_full": {
            "label": "HISTORICAL-PROPHECY density (full 4-root)",
            "roots": sorted(CELL_B_HIST_FULL),
            "root_set": CELL_B_HIST_FULL,
            "direction": "target > baseline",
            "pred_higher": True,
            "lemma_filter": {"kwn": KWN_LEMMA_FILTER},
        },
        "c_allah": {
            "label": "ALLAH-density control",
            "roots": sorted(CELL_C_ALLAH),
            "root_set": CELL_C_ALLAH,
            "direction": "target ≈ baseline (no difference predicted)",
            "pred_higher": None,
        },
        "d_eschato": {
            "label": "ESCHATOLOGICAL density (Axr/bEv/Hsb/jzy)",
            "roots": sorted(CELL_D_ESCHATO),
            "root_set": CELL_D_ESCHATO,
            "direction": "target ≈ baseline (no difference predicted)",
            "pred_higher": None,
        },
    }

    # Secondary b variants
    cells_b_secondary = {
        "b_hist_glb_only": {
            "label": "HIST glb-only (ghalaba alone)",
            "roots": sorted(CELL_B_HIST_GLB_ONLY),
            "root_set": CELL_B_HIST_GLB_ONLY,
            "direction": "target > baseline",
            "pred_higher": True,
        },
        "b_hist_glb_nsr": {
            "label": "HIST glb+nSr (ghalaba + naṣr)",
            "roots": sorted(CELL_B_HIST_GLB_NSR),
            "root_set": CELL_B_HIST_GLB_NSR,
            "direction": "target > baseline",
            "pred_higher": True,
        },
    }

    # Compute densities for all surahs
    print("[H-NEW-93] computing cell densities ...", file=sys.stderr)
    per_cell_density = {}  # cell -> {sid: density}
    per_cell_counts = {}   # cell -> {sid: (hits, total)}

    all_cells = {**cells, **cells_b_secondary}
    for cell_name, cell in all_cells.items():
        per_cell_density[cell_name] = {}
        per_cell_counts[cell_name] = {}
        lemma_filter = cell.get("lemma_filter")
        for sid in range(1, 115):
            tokens = qac[sid]
            hits, total, dens = surah_density(
                tokens, cell["root_set"],
                root_lemma_map=lemma_filter,
            )
            per_cell_density[cell_name][sid] = dens
            per_cell_counts[cell_name][sid] = (hits, total)

    # Per-surah report for target + other-الم
    print("[H-NEW-93] per-surah density snapshot:", file=sys.stderr)
    for sid in list(TARGET) + list(OTHER_ALIF_LAM_MIM):
        line = f"  Q{sid:3d} ({sname[sid]:<15})"
        for cn in ["a_test", "b_hist_full", "b_hist_glb_only", "b_hist_glb_nsr",
                   "c_allah", "d_eschato"]:
            h, t = per_cell_counts[cn][sid]
            line += f" | {cn}={h:3d}/{t:4d}={per_cell_density[cn][sid]*1000:.2f}‰"
        print(line, file=sys.stderr)

    # Run permutation tests
    print("[H-NEW-93] running permutation tests ...", file=sys.stderr)
    target_ids = list(TARGET)
    other_alm_ids = list(OTHER_ALIF_LAM_MIM)
    baseline_ids = list(meccan_non_muq)

    results = {}
    for cell_name, cell in all_cells.items():
        dens = per_cell_density[cell_name]
        target_vals = [dens[sid] for sid in target_ids]
        other_alm_vals = [dens[sid] for sid in other_alm_ids]
        baseline_vals = [dens[sid] for sid in baseline_ids]

        # Comparison 1: target vs other-الم
        r1 = perm_mean_diff(target_vals, other_alm_vals, N_PERM,
                            seed=SEED + hash(cell_name + "_vs_otheralm") % 10000)
        # Comparison 2: target vs Meccan non-muq
        r2 = perm_mean_diff(target_vals, baseline_vals, N_PERM,
                            seed=SEED + hash(cell_name + "_vs_meccan") % 10000)
        # MW-5 positive control: other-الم vs Meccan non-muq (only meaningful for a, b cells)
        r_mw5 = perm_mean_diff(other_alm_vals, baseline_vals, N_PERM,
                               seed=SEED + hash(cell_name + "_MW5") % 10000)

        # Verdict for primary comparison (target vs Meccan non-muq)
        if cell.get("pred_higher") is True:
            p_pred = r2["p_one_sided_A_gt_B"]
            verdict = cell_verdict(r2["p_two_sided"], p_pred, "higher",
                                   ALPHA_BON, ALPHA_SINGLE_CAP)
        elif cell.get("pred_higher") is False:
            p_pred = r2["p_one_sided_A_lt_B"]
            verdict = cell_verdict(r2["p_two_sided"], p_pred, "lower",
                                   ALPHA_BON, ALPHA_SINGLE_CAP)
        else:
            # pred_higher is None ⇒ null-expected control cell
            if r2["p_two_sided"] < 0.05:
                verdict = "CONTROL-VIOLATED"
            else:
                verdict = "CONTROL-CONFIRMED"
            p_pred = None

        results[cell_name] = {
            "label": cell["label"],
            "roots": cell["roots"],
            "direction": cell["direction"],
            "target_vs_other_alm": r1,
            "target_vs_meccan_non_muq": r2,
            "mw5_other_alm_vs_meccan": r_mw5,
            "verdict": verdict,
            "p_pred": p_pred,
        }

        print(f"  [{cell_name:<20}] {cell['label']}", file=sys.stderr)
        print(f"    target-mean={r2['mean_A']*1000:.3f}‰ "
              f"meccan-mean={r2['mean_B']*1000:.3f}‰ "
              f"p2={r2['p_two_sided']:.4f} → {verdict}",
              file=sys.stderr)
        print(f"    target vs other-الم: p2={r1['p_two_sided']:.4f} "
              f"(mean_A={r1['mean_A']*1000:.3f}‰ mean_B={r1['mean_B']*1000:.3f}‰)",
              file=sys.stderr)
        print(f"    MW-5 other-الم vs meccan: p2={r_mw5['p_two_sided']:.4f} "
              f"(mean_A={r_mw5['mean_A']*1000:.3f}‰ mean_B={r_mw5['mean_B']*1000:.3f}‰)",
              file=sys.stderr)

    # Headline composite verdict on primary 4 cells
    primary_cells = ["a_test", "b_hist_full", "c_allah", "d_eschato"]
    p_vals_primary = [results[c]["target_vs_meccan_non_muq"]["p_two_sided"]
                      for c in primary_cells]

    # "Full target-pattern" requires: (a)+(b) PASS-DIRECTED, (c)+(d) CONTROL-CONFIRMED
    a_pass = results["a_test"]["verdict"].startswith(("STRONG-PASS", "WEAK-PASS"))
    b_pass = results["b_hist_full"]["verdict"].startswith(("STRONG-PASS", "WEAK-PASS"))
    c_ok = results["c_allah"]["verdict"] == "CONTROL-CONFIRMED"
    d_ok = results["d_eschato"]["verdict"] == "CONTROL-CONFIRMED"

    # MW-5 check for (a) and (b)
    mw5_a = results["a_test"]["mw5_other_alm_vs_meccan"]["p_two_sided"]
    mw5_b = results["b_hist_full"]["mw5_other_alm_vs_meccan"]["p_two_sided"]
    mw5_pass_a = mw5_a > 0.05  # other-الم should NOT be elevated
    mw5_pass_b = mw5_b > 0.05
    mw5_all_pass = mw5_pass_a and mw5_pass_b

    if a_pass and b_pass and c_ok and d_ok and mw5_all_pass:
        composite = "FULL-TARGET-PATTERN-PASS-DIRECTED"
    elif (a_pass or b_pass) and c_ok and mw5_all_pass:
        composite = "PARTIAL-TARGET-PATTERN-WEAK-PASS-DIRECTED"
    elif not mw5_all_pass:
        composite = "NULL-BROKEN-on-specificity-MW5-fail"
    elif not c_ok:
        composite = "INCONCLUSIVE-CONFOUND-on-Allah-density"
    elif not (a_pass or b_pass):
        composite = "NULL-full-target-pattern-rejected"
    else:
        composite = "INCONCLUSIVE"

    # Pre-reg SHA
    preg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-93",
        "title": "Q 29 al-ʿAnkabūt + Q 30 al-Rūm TEST-AND-PROPHECY sub-pattern",
        "run_date": "2026-04-17",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "alpha_single_test_cap": ALPHA_SINGLE_CAP,
        "prereg_path": str(PREREG),
        "prereg_sha256": preg_sha,
        "data_variant": "no-tashkeel",
        "rules_tuple": "hafs-kūfan; no-tashkeel; QAC v0.4 STEM-ROOT tokens",
        "target_surahs": list(TARGET),
        "other_alm_surahs": list(OTHER_ALIF_LAM_MIM),
        "meccan_non_muq_baseline_n": len(meccan_non_muq),
        "meccan_non_muq_baseline_ids": meccan_non_muq,
        "per_cell_results": results,
        "composite_verdict": composite,
        "mw5_positive_control": {
            "cell_a_p": mw5_a,
            "cell_b_p": mw5_b,
            "cell_a_pass": mw5_pass_a,
            "cell_b_pass": mw5_pass_b,
            "overall_pass": mw5_all_pass,
        },
        "verdict_ceiling": "PASS-DIRECTED (post-hoc-noticed sub-cluster)",
        "note": "Independent replication required for promotion beyond PASS-DIRECTED",
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[H-NEW-93] wrote {OUT_JSON}", file=sys.stderr)
    print(f"[H-NEW-93] composite verdict: {composite}", file=sys.stderr)
    print(f"[H-NEW-93] primary p-values: "
          f"a_test={p_vals_primary[0]:.4f} "
          f"b_hist_full={p_vals_primary[1]:.4f} "
          f"c_allah={p_vals_primary[2]:.4f} "
          f"d_eschato={p_vals_primary[3]:.4f}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
