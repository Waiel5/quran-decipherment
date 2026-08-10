#!/usr/bin/env python3
"""H-NEW-3070 POST-HOC 2 — MDE and power for the NULLs this finding PUBLISHES.

NOT PRE-REGISTERED. Can only weaken.

The headline claim of h-new-3070 §5 is an ABSENCE: "within Mecca there is no deictic trend that
survives a mean-verse-length control." cross-finding-029 §3.2 and ABSENCE-CLAIMS require that a
published NULL state its MDE and power, because "did not detect" and "could not have detected"
are different claims and only a computed MDE distinguishes them.

Two published NULLs are audited here:
  N1  the Meccan-only subset (the load-bearing one — the headline rests on it)
  N2  rules-tuple R2, the Egyptian-standard revelation-order rank

Method: h-new-3030 §3.5 / prereg §9, reusing the parent script's power_block by import.
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
sys.argv = [sys.argv[0]]
spec.loader.exec_module(m)

RUN_ROOT = "findings/phase-b-hypotheses/runs/h-new-3070-posthoc2"


def audit(tokens, chron, channels, chron_field, label):
    """Full 9-setting sweep + the power block at the worst channel."""
    surahs, nd, npx = m.token_table(tokens, "deixis_kaf")
    phase = np.array([chron[s][chron_field] for s in surahs], dtype=float)
    ch = {c: np.array([channels[s][c] for s in surahs], dtype=float) for c in m.CHANNELS[:3]}
    ch["L4_dem_count"] = nd + npx
    settings = [("L0_unstratified", None)]
    for c in m.CHANNELS:
        for bname, nb in m.BIN_WIDTHS.items():
            settings.append((f"{c}|{bname}", m.strata_of(ch[c], nb)))

    cells = {}
    for hyp in ("H1", "H2"):
        for sname, strata in settings:
            rng = np.random.default_rng(m.SEED_PRIMARY)
            cell = m.run_cell(hyp, phase, nd, npx, strata, m.N_PERM, rng)
            if cell:
                cells[f"{hyp}|{sname}"] = cell

    worst_h1 = max((k for k in cells if k.startswith("H1|")), key=lambda k: cells[k]["p"])
    worst_h2 = max((k for k in cells if k.startswith("H2|")), key=lambda k: cells[k]["p"])
    pb = m.power_block(phase, nd, npx,
                       cells[worst_h1]["null_q975"], cells[worst_h2]["null_q975"],
                       cells[worst_h1]["null_sd"], np.random.default_rng(m.SEED_PRIMARY))
    return {
        "label": label,
        "n_surahs": len(surahs), "n_tokens": int((nd + npx).sum()),
        "n_distal": int(nd.sum()), "n_proximal": int(npx.sum()),
        "obs_H1": cells["H1|L0_unstratified"]["obs"],
        "obs_H2": cells["H2|L0_unstratified"]["obs"],
        "worst_setting_H1": worst_h1.split("|", 1)[1], "p_worst_H1": cells[worst_h1]["p"],
        "worst_setting_H2": worst_h2.split("|", 1)[1], "p_worst_H2": cells[worst_h2]["p"],
        "p_best_H1": min(v["p"] for k, v in cells.items() if k.startswith("H1|")),
        "p_best_H2": min(v["p"] for k, v in cells.items() if k.startswith("H2|")),
        "power_at_worst_channel": pb,
        "observed_vs_MDE": {
            "obs_H1": cells["H1|L0_unstratified"]["obs"],
            "MDE_H1_80pct": pb["MDE_H1_simulated_80pct_power"],
            "obs_exceeds_MDE": bool(cells["H1|L0_unstratified"]["obs"]
                                    >= (pb["MDE_H1_simulated_80pct_power"] or np.inf)),
        },
    }


def main():
    rows = m.load_qac()
    chron = m.load_chronology()
    channels = m.surah_channels(rows)
    dem = [r for r in rows if m.has_pos(r["feat"], "DEM")]
    for r in dem:
        r["deixis_kaf"] = m.deixis_kaf(r["form"])
        r["deixis_lemma"] = m.deixis_lemma(r["feat"])

    out = {
        "NOT_PREREGISTERED": True,
        "purpose": "MDE + power for the NULLs h-new-3070 publishes (cross-finding-029 SS3.2)",
        "N1_meccan_only_the_load_bearing_null": audit(
            [r for r in dem if chron[r["s"]]["noldeke_phase_ord"] <= 3],
            chron, channels, "noldeke_phase_ord", "Meccan only (Early+Middle+Late)"),
        "N2_egyptian_revelation_order_tuple_R2": audit(
            dem, chron, channels, "revelation_order", "R2 Egyptian-standard revelation order"),
    }

    run_dir = os.path.join(RUN_ROOT, datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    os.makedirs(run_dir, exist_ok=False)
    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    with open(os.path.join(run_dir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({"script_sha256": m.sha256_of(__file__),
                   "parent_script_sha256": m.sha256_of(os.path.join(HERE, "h-new-3070.py")),
                   "utc": datetime.now(timezone.utc).isoformat()}, fh, indent=2)
    print("run dir:", run_dir)
    for k in ("N1_meccan_only_the_load_bearing_null", "N2_egyptian_revelation_order_tuple_R2"):
        a = out[k]
        p = a["power_at_worst_channel"]
        print(f"\n--- {a['label']} ---")
        print(f"  n_tokens={a['n_tokens']} surahs={a['n_surahs']}")
        print(f"  H1 obs={a['obs_H1']:+.5f}  p_best={a['p_best_H1']:.5f}  "
              f"p_worst={a['p_worst_H1']:.5f} ({a['worst_setting_H1']})")
        print(f"  H2 obs={a['obs_H2']:+.5f}  p_best={a['p_best_H2']:.5f}  "
              f"p_worst={a['p_worst_H2']:.5f} ({a['worst_setting_H2']})")
        print(f"  S*={p['S_star_H1']:.5f}  S_max={p['S_max_H1']:.5f}  "
              f"UNTESTABLE={p['untestable_at_this_n']}")
        print(f"  MDE(80% power) = {p['MDE_H1_simulated_80pct_power']}")
        print(f"  power vs 0.25-unit effect: H1={p['power_at_delta_0.25']['power_h1']:.3f} "
              f"H2={p['power_at_delta_0.25']['power_h2']:.3f}")
        print(f"  observed {a['obs_H1']:.5f} vs MDE -> obs_exceeds_MDE="
              f"{a['observed_vs_MDE']['obs_exceeds_MDE']}")


if __name__ == "__main__":
    main()
