"""
Q071-F-03 — H-NEW-49.1 prophet-named hypergeometric replication anchored at Q 71.

Locked pre-reg: ../preregs/Q071-F-03-prophet-named-cluster-prereg.md
Seed: 20260509

Method: closed-form hypergeometric P(X >= 6 | n=8, K=29, N=114).
"""

import json
import hashlib
from pathlib import Path
from scipy.stats import hypergeom


def main():
    repo = Path("/Users/grey/Downloads/quran")
    prereg = repo / "surahs/Q071-nuh/preregs/Q071-F-03-prophet-named-cluster-prereg.md"
    sha = hashlib.sha256(prereg.read_bytes()).hexdigest()
    print(f"Pre-reg SHA-256: {sha}")

    # Locked sets
    muq_set = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31,
               32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
    prophet_named_8 = {10, 11, 12, 14, 19, 31, 47, 71}
    N_total = 114

    assert len(muq_set) == 29, "muqaṭṭaʿāt set must be 29"
    assert len(prophet_named_8) == 8, "prophet-named-8 must have 8 elements"

    in_muq = prophet_named_8 & muq_set
    not_muq = prophet_named_8 - muq_set
    k_obs = len(in_muq)

    print(f"\nProphet-named-8 (conservative): {sorted(prophet_named_8)}")
    print(f"  ∩ muqaṭṭaʿāt-29: {sorted(in_muq)} (count: {k_obs})")
    print(f"  ∉ muqaṭṭaʿāt-29: {sorted(not_muq)} (count: {len(not_muq)})")

    # Hypergeometric P(X >= 6 | n=8, K=29, N=114)
    p = hypergeom.sf(k_obs - 1, N_total, len(muq_set), len(prophet_named_8))
    expected = len(prophet_named_8) * len(muq_set) / N_total

    print(f"\nHypergeometric test:")
    print(f"  N = {N_total}, K = {len(muq_set)}, n = {len(prophet_named_8)}, k = {k_obs}")
    print(f"  P(X >= {k_obs}) = {p:.6f}")
    print(f"  Expected under H0: {expected:.2f}")
    print(f"  Enrichment: {k_obs / expected:.2f}×")

    # Verify Q 71's cell
    q71_in_prophet = (71 in prophet_named_8)
    q71_in_muq = (71 in muq_set)
    print(f"\nQ 71 cell verification:")
    print(f"  Q 71 ∈ prophet-named-8: {q71_in_prophet}")
    print(f"  Q 71 ∈ muqaṭṭaʿāt-29: {q71_in_muq}")
    print(f"  Q 71 cell: PROPHET-NAMED + NON-MUQ ✓"
          if (q71_in_prophet and not q71_in_muq) else "Q 71 cell mismatch!")

    # Acceptance window
    alpha_bon = 0.01
    if p <= alpha_bon and q71_in_prophet and not q71_in_muq:
        verdict = "PASS-DIRECTED"
    elif p <= 0.05:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    print(f"\nVerdict: {verdict}")

    out = {
        "finding_id": "Q071-F-03",
        "prereg_sha256": sha,
        "seed": 20260509,
        "rules_tuple": "(hafs-kufan; canonical 114; muq-29 set; prophet-named-8 conservative)",
        "N_total": N_total,
        "K_muq": len(muq_set),
        "n_prophet_named": len(prophet_named_8),
        "k_in_muq": k_obs,
        "expected": expected,
        "enrichment_ratio": k_obs / expected,
        "p_hypergeom": float(p),
        "alpha_bon_local_5": alpha_bon,
        "Q71_in_prophet_named": q71_in_prophet,
        "Q71_in_muq": q71_in_muq,
        "Q71_cell": "PROPHET-NAMED + NON-MUQ" if (q71_in_prophet and not q71_in_muq) else "MISMATCH",
        "muq_prophet_named": sorted(in_muq),
        "non_muq_prophet_named": sorted(not_muq),
        "verdict": verdict,
        "parent_finding": "H-NEW-49.1",
    }

    out_path = repo / "surahs/Q071-nuh/csv/Q071-F-03.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nResult written to {out_path}")

    return out


if __name__ == "__main__":
    main()
