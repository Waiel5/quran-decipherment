#!/usr/bin/env python3
"""H-NEW-3070 POST-HOC — NOT PRE-REGISTERED. These probes can only WEAKEN the locked verdict.

The locked run returned PASS. Four things it surfaced need interrogation, and none of them was
registered, so none of them can rescue or upgrade anything:

  P1  the phase profile is NOT monotone (Middle-Meccan trough) — is the gradient just "Medinan"?
  P2  drop Medinan entirely: is there any gradient WITHIN Mecca?
  P3  drop the `ulaa'ika` group-verdict lemma (prereg SS1.1 anchor 3 predicted it drives this)
  P4  per-lemma distal profile by phase, descriptive

Reuses the locked run's instruments by import so no rule is re-implemented.
"""
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("h3070", os.path.join(HERE, "h-new-3070.py"))
m = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]          # keep the imported module's argparse quiet
spec.loader.exec_module(m)

RUN_ROOT = "findings/phase-b-hypotheses/runs/h-new-3070-posthoc"


def cells_for(tokens, chron, channels, dfield="deixis_kaf", chron_field="noldeke_phase_ord"):
    """All 9 length settings for both hypotheses, exactly as the locked run does it."""
    surahs, nd, npx = m.token_table(tokens, dfield)
    if len(surahs) == 0:
        return None, None
    phase = np.array([chron[s][chron_field] for s in surahs], dtype=float)
    ch = {c: np.array([channels[s][c] for s in surahs], dtype=float) for c in m.CHANNELS[:3]}
    ch["L4_dem_count"] = nd + npx
    settings = [("L0_unstratified", None)]
    for c in m.CHANNELS:
        for bname, nb in m.BIN_WIDTHS.items():
            settings.append((f"{c}|{bname}", m.strata_of(ch[c], nb)))
    out = {}
    for hyp in ("H1", "H2"):
        for sname, strata in settings:
            rng = np.random.default_rng(m.SEED_PRIMARY)
            cell = m.run_cell(hyp, phase, nd, npx, strata, m.N_PERM, rng)
            if cell:
                out[f"{hyp}|{sname}"] = cell
    meta = {"n_surahs": len(surahs), "n_tokens": int((nd + npx).sum()),
            "n_distal": int(nd.sum()), "n_proximal": int(npx.sum())}
    return out, meta


def worst(cells, hyp):
    ps = [v["p"] for k, v in cells.items() if k.startswith(hyp + "|")]
    return max(ps) if ps else None


def main():
    rows = m.load_qac()
    chron = m.load_chronology()
    channels = m.surah_channels(rows)
    dem = [r for r in rows if m.has_pos(r["feat"], "DEM")]
    for r in dem:
        r["deixis_kaf"] = m.deixis_kaf(r["form"])
        r["deixis_lemma"] = m.deixis_lemma(r["feat"])

    res = {}

    # ---- P1: is the gradient carried entirely by Medinan? Test each adjacent phase pair.
    pairs = {}
    for lo, hi in [(1, 2), (2, 3), (3, 4)]:
        sub = [r for r in dem if chron[r["s"]]["noldeke_phase_ord"] in (lo, hi)]
        c, meta = cells_for(sub, chron, channels)
        pairs[f"phase{lo}_vs_phase{hi}"] = {
            "meta": meta,
            "H1_obs": c["H1|L0_unstratified"]["obs"], "H1_p_worst": worst(c, "H1"),
            "H2_obs": c["H2|L0_unstratified"]["obs"], "H2_p_worst": worst(c, "H2"),
        }
    res["P1_adjacent_phase_pairs"] = pairs

    # ---- P2: drop Medinan entirely — any gradient WITHIN Mecca?
    mecca = [r for r in dem if chron[r["s"]]["noldeke_phase_ord"] <= 3]
    c, meta = cells_for(mecca, chron, channels)
    res["P2_meccan_only"] = {
        "meta": meta,
        "H1_obs": c["H1|L0_unstratified"]["obs"], "H1_p_worst": worst(c, "H1"),
        "H1_p_best": min(v["p"] for k, v in c.items() if k.startswith("H1|")),
        "H2_obs": c["H2|L0_unstratified"]["obs"], "H2_p_worst": worst(c, "H2"),
        "H2_p_best": min(v["p"] for k, v in c.items() if k.startswith("H2|")),
        "all_cells": {k: v["p"] for k, v in c.items()},
    }

    # ---- P3: drop the group-verdict lemma `ulaa'ika` (prereg SS1.1 anchor 3)
    ULA = {">uwla`^}ik", ">uwlaA^'"}
    no_ula = [r for r in dem if m.lemma_of(r["feat"]) not in ULA]
    c, meta = cells_for(no_ula, chron, channels)
    res["P3_drop_ulaaika_lemma"] = {
        "meta": meta, "n_dropped": len(dem) - len(no_ula),
        "H1_obs": c["H1|L0_unstratified"]["obs"], "H1_p_worst": worst(c, "H1"),
        "H2_obs": c["H2|L0_unstratified"]["obs"], "H2_p_worst": worst(c, "H2"),
    }
    # and the converse: ONLY ulaa'ika
    only_ula = [r for r in dem if m.lemma_of(r["feat"]) in ULA]
    c2, meta2 = cells_for(only_ula, chron, channels)
    res["P3b_only_ulaaika_lemma"] = {
        "meta": meta2,
        "H1_obs": c2["H1|L0_unstratified"]["obs"] if c2 else None,
        "H1_p_worst": worst(c2, "H1") if c2 else None,
    }

    # ---- P4: descriptive — per-lemma distal share by phase, and phase profile with bootstrap CI
    prof = {}
    rng = np.random.default_rng(m.SEED_PRIMARY)
    for ph in range(1, 5):
        sub = [r for r in dem if chron[r["s"]]["noldeke_phase_ord"] == ph]
        nd_ = sum(1 for r in sub if r["deixis_kaf"] == "DISTAL")
        # surah-clustered bootstrap over the surahs present in this phase
        by_s = {}
        for r in sub:
            by_s.setdefault(r["s"], []).append(r)
        keys = list(by_s)
        boots = []
        for _ in range(5000):
            pick = rng.choice(len(keys), size=len(keys), replace=True)
            toks = [t for i in pick for t in by_s[keys[i]]]
            if toks:
                boots.append(sum(1 for t in toks if t["deixis_kaf"] == "DISTAL") / len(toks))
        prof[ph] = {"n_tokens": len(sub), "distal_share": nd_ / len(sub),
                    "ci95_surah_clustered_bootstrap": [float(np.quantile(boots, 0.025)),
                                                       float(np.quantile(boots, 0.975))]}
    res["P4_phase_profile_with_CI"] = prof

    lem_by_phase = {}
    for lem in ("*a`lik", ">uwla`^}ik", "ha`*aA"):
        row = {}
        for ph in range(1, 5):
            n = sum(1 for r in dem if m.lemma_of(r["feat"]) == lem
                    and chron[r["s"]]["noldeke_phase_ord"] == ph)
            row[ph] = n
        lem_by_phase[lem] = row
    res["P4b_lemma_counts_by_phase"] = lem_by_phase

    run_dir = os.path.join(RUN_ROOT, datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    os.makedirs(run_dir, exist_ok=False)
    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump({"NOT_PREREGISTERED": True,
                   "note": "post-hoc probes; can only weaken the locked PASS",
                   "seed": m.SEED_PRIMARY, "n_permutations": m.N_PERM,
                   "alpha_reference": m.ALPHA_BONFERRONI, "probes": res}, fh,
                  indent=2, ensure_ascii=False)
    with open(os.path.join(run_dir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({"script_sha256": m.sha256_of(__file__),
                   "parent_script_sha256": m.sha256_of(os.path.join(HERE, "h-new-3070.py")),
                   "utc": datetime.now(timezone.utc).isoformat()}, fh, indent=2)
    print("post-hoc run dir:", run_dir)
    print(json.dumps(res, indent=2, ensure_ascii=False)[:4000])


if __name__ == "__main__":
    main()
