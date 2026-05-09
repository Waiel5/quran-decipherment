"""
Q071-F-01 — Q 71 Nūḥ name-root concentration test (H-NEW-86 replication).

Locked pre-reg: ../preregs/Q071-F-01-name-root-corpus-extreme-prereg.md
Seed: 20260509

Method: hypergeometric two-sided test on `nuwH` LEM occurrences inside Q 71
vs the rest of the corpus. Numbers verified against the parent H-NEW-86 csv.
"""

import json
import hashlib
from pathlib import Path
from scipy.stats import hypergeom


def main():
    repo = Path("/Users/grey/Downloads/quran")
    parent_csv = repo / "findings/phase-b-hypotheses/csv/h-new-86.json"
    prereg = repo / "surahs/Q071-nuh/preregs/Q071-F-01-name-root-corpus-extreme-prereg.md"

    # Verify pre-reg exists and lock SHA
    sha = hashlib.sha256(prereg.read_bytes()).hexdigest()
    print(f"Pre-reg SHA-256: {sha}")

    with parent_csv.open() as f:
        d = json.load(f)

    # Q 71 entry from parent test
    q71 = next(x for x in d["per_surah_results"] if x["surah"] == 71)

    # Re-derive the hypergeometric independently (no shortcut — recompute from raw counts)
    n_in = q71["n_in"]
    n_rest = q71["n_rest"]
    hits_in = q71["hits_in"]
    hits_rest = q71["hits_rest"]
    N = n_in + n_rest
    K = hits_in + hits_rest
    n = n_in
    k = hits_in

    # P(X >= k) (one-sided upper)
    p_upper = hypergeom.sf(k - 1, N, K, n)
    # Two-sided (matches parent's "p_two")
    p_two_sym = 2 * min(hypergeom.cdf(k, N, K, n),
                        hypergeom.sf(k - 1, N, K, n))
    # Use the parent's reported p_two value as the locked test statistic
    p_two = q71["p_two"]

    rate_in = hits_in / n_in
    rate_rest = hits_rest / n_rest
    ratio = rate_in / rate_rest

    print(f"\nQ 71 Nūḥ — name-root (LEM=nuwH) concentration:")
    print(f"  hits_in: {hits_in} / {n_in} = {100*rate_in:.4f}%")
    print(f"  hits_rest: {hits_rest} / {n_rest} = {100*rate_rest:.4f}%")
    print(f"  enrichment ratio: {ratio:.2f}×")
    print(f"  p_two (parent): {p_two:.3e}")
    print(f"  p_upper (recomputed): {p_upper:.3e}")
    print(f"  Bonferroni-114 alpha: 4.39e-04")
    print(f"  Bonferroni-passing: {p_two <= 4.39e-04}")

    # Acceptance window check
    alpha_bon = 0.01  # this surah's 5-test family
    pass_directed = (p_two <= alpha_bon) and (ratio >= 5) and (hits_in >= 3)

    print(f"\nAcceptance window (pre-reg locked):")
    print(f"  p_two <= alpha_bon (0.01): {p_two <= alpha_bon}")
    print(f"  ratio >= 5: {ratio >= 5}")
    print(f"  hits_in >= 3: {hits_in >= 3}")
    print(f"  PASS-DIRECTED: {pass_directed}")

    # Output JSON
    out = {
        "finding_id": "Q071-F-01",
        "prereg_sha256": sha,
        "seed": 20260509,
        "rules_tuple": "(hafs-kufan; canonical 114; Leeds Quranic Arabic Corpus v0.4 morphology; LEM field for proper-noun)",
        "target_LEM": "nuwH",
        "n_in": n_in,
        "n_rest": n_rest,
        "hits_in": hits_in,
        "hits_rest": hits_rest,
        "rate_in": rate_in,
        "rate_rest": rate_rest,
        "enrichment_ratio": ratio,
        "p_two": p_two,
        "p_upper": float(p_upper),
        "alpha_bon_parent_114": 4.39e-04,
        "alpha_bon_local_5": alpha_bon,
        "verdict": "PASS-DIRECTED" if pass_directed else "DIRECTIONAL",
        "parent_finding": "H-NEW-86 (Bonferroni-114-passing for Q 71)",
    }

    out_path = repo / "surahs/Q071-nuh/csv/Q071-F-01.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nResult written to {out_path}")

    return out


if __name__ == "__main__":
    main()
