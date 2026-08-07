#!/usr/bin/env python3
"""H-NEW-2600: muṭāwaʿa lattice with causative reverse-controls.

Extraction, join, statistic and nulls are inherited verbatim from H-NEW-2540 by
importing that script; only the set of form pairs and the locked directions differ.
"""

import argparse, hashlib, importlib.util, itertools, json, math, platform, random
import shlex, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_PREREG_SHA = "f058b852d5e2aadd8301070962759a8391f05f98749b49da78b2214fdf619b10"
SEED_NULL_A = 20260509
SEED_NULL_B = 20260510
N_PERM = 10_000
CONFIRMATORY_INFERENCES = 10
RAW_GATE = 0.05 / CONFIRMATORY_INFERENCES / 10  # 0.0005
ALPHA_BON = 0.05 / CONFIRMATORY_INFERENCES      # 0.005
MIN_TOKENS = 2

# (label, A, B, locked sign) — locked in prereg §5 before computation.
CONFIRMATORY = [
    ("P1_I_to_VII",  "I",   "VII", +1),
    ("P2_I_to_VIII", "I",   "VIII", +1),
    ("P3_IV_to_VII", "IV",  "VII", +1),
    ("N1_I_to_II",   "I",   "II",  -1),
    ("N2_I_to_IV",   "I",   "IV",  -1),
]
REPLICATION = [("R1_II_to_V", "II", "V", +1), ("R2_III_to_VI", "III", "VI", +1)]
FORMS = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")


def sha256(path):
    d = hashlib.sha256()
    with open(path, "rb") as h:
        for chunk in iter(lambda: h.read(1 << 20), b""):
            d.update(chunk)
    return d.hexdigest()


def load_2540(repo_root):
    path = repo_root / "findings/phase-b-hypotheses/scripts/h-new-2540.py"
    spec = importlib.util.spec_from_file_location("h2540", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, sha256(path)


def signed_perm_test(m, cells, a, b, sign):
    """Null A: root-cell sign-flip. Exact when R<=20, else seeded Monte Carlo."""
    obs = m.weighted_stat(cells, a, b)
    roots = sorted(cells)
    R = len(roots)
    if R == 0:
        return obs, float("nan"), 0, "empty"
    if R <= 20:
        vals = [m.weighted_stat(m.swapped_cells(cells, a, b, mask), a, b)
                for mask in itertools.product((False, True), repeat=R)]
        tail = sum((v >= obs - 1e-15) if sign > 0 else (v <= obs + 1e-15) for v in vals)
        return obs, tail / len(vals), len(vals), "exact"
    rng = random.Random(SEED_NULL_A)
    extreme = 0
    for _ in range(N_PERM):
        mask = [bool(rng.getrandbits(1)) for _ in range(R)]
        v = m.weighted_stat(m.swapped_cells(cells, a, b, mask), a, b)
        extreme += (v >= obs) if sign > 0 else (v <= obs)
    return obs, (extreme + 1) / (N_PERM + 1), N_PERM, "monte-carlo"


def signed_token_test(m, cells, a, b, sign):
    """Null B: within-root token-label reallocation, margin-preserving. PRIMARY."""
    obs = m.weighted_stat(cells, a, b)
    if not cells:
        return obs, float("nan"), 0
    rng = random.Random(SEED_NULL_B)
    extreme = 0
    for _ in range(N_PERM):
        perm = {}
        for root, forms in cells.items():
            na, ya = forms[a]
            nb, yb = forms[b]
            tot = ya + yb
            slots = set(rng.sample(range(na + nb), tot))
            pa = sum(i < na for i in slots)
            perm[root] = {a: (na, pa), b: (nb, tot - pa)}
        v = m.weighted_stat(perm, a, b)
        extreme += (v >= obs) if sign > 0 else (v <= obs)
    return obs, (extreme + 1) / (N_PERM + 1), N_PERM


def arm(m, tokens, label, a, b, sign, confirmatory):
    cells = m.cells_for(tokens, a, b, MIN_TOKENS)
    obs, p_a, size_a, kind_a = signed_perm_test(m, cells, a, b, sign)
    _, p_b, size_b = signed_token_test(m, cells, a, b, sign)
    sign_ok = (obs > 0) if sign > 0 else (obs < 0)
    return {
        "label": label, "forms": [a, b], "locked_sign": "positive" if sign > 0 else "negative",
        "eligible_roots": len(cells), "root_cells": cells,
        "T_weighted": obs,
        "unsmoothed_macro": m.unsmoothed_macro(cells, a, b),
        "mantel_haenszel_or": m.mantel_haenszel_or(cells, a, b),
        "p_null_a": p_a, "null_a_kind": kind_a, "null_a_size": size_a,
        "p_null_b_PRIMARY": p_b, "null_b_size": size_b,
        "p_null_a_bonferroni": min(1.0, CONFIRMATORY_INFERENCES * p_a) if p_a == p_a else None,
        "p_null_b_bonferroni": min(1.0, CONFIRMATORY_INFERENCES * p_b) if p_b == p_b else None,
        "sign_matches_lock": bool(sign_ok),
        "passes_gate": bool(confirmatory and sign_ok and p_a < RAW_GATE and p_b < RAW_GATE),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--eqtb", type=Path, required=True)
    ap.add_argument("--run-id")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-2600-mutawaa-lattice.md"
    got = sha256(prereg)
    if got != EXPECTED_PREREG_SHA:
        raise SystemExit(f"prereg SHA mismatch: expected {EXPECTED_PREREG_SHA}, found {got}")

    m, script_2540_sha = load_2540(repo_root)
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"
    chron = repo_root / "data/revelation-order.csv"
    hashes = {"prereg": got, "qac": sha256(qac), "eqtb": sha256(args.eqtb),
              "chronology": sha256(chron), "script_2540": script_2540_sha,
              "script": sha256(Path(__file__).resolve())}
    for key, exp in (("qac", m.EXPECTED_QAC_SHA), ("eqtb", m.EXPECTED_EQTB_SHA),
                     ("chronology", m.EXPECTED_CHRONOLOGY_SHA)):
        if hashes[key] != exp:
            raise SystemExit(f"{key} SHA mismatch: expected {exp}, found {hashes[key]}")

    qac_verbs, qdup = m.parse_qac(qac)
    eqtb_verbs, edges, edup = m.parse_eqtb(args.eqtb)
    if qdup or edup:
        raise SystemExit(f"duplicate real locations abort the run: qac={len(qdup)} eqtb={len(edup)}")
    joined, unmatched, agreement = m.join_tokens(qac_verbs, eqtb_verbs, edges, m.load_periods(chron))
    if agreement["form_rate"] < 1.0 or agreement["root_rate"] < 1.0:
        raise SystemExit("QAC/EQTB lineage mismatch aborts the run (100% required)")
    active = [t for t in joined if not t["passive"]]

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2600" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    confirm = [arm(m, active, *spec, True) for spec in CONFIRMATORY]
    replic = [arm(m, active, *spec, False) for spec in REPLICATION]

    lattice = []
    for a, b in itertools.permutations(FORMS, 2):
        cells = m.cells_for(active, a, b, MIN_TOKENS)
        if len(cells) >= 5:
            lattice.append({"forms": [a, b], "eligible_roots": len(cells),
                            "T_weighted": m.weighted_stat(cells, a, b),
                            "mantel_haenszel_or": m.mantel_haenszel_or(cells, a, b)})

    muta = {(a, b) for _, a, b, s in CONFIRMATORY if s > 0} | {("II", "V"), ("III", "VI")}
    caus = {(a, b) for _, a, b, s in CONFIRMATORY if s < 0}
    other = [c for c in lattice if tuple(c["forms"]) not in muta | caus]

    p1 = next(c for c in confirm if c["label"] == "P1_I_to_VII")
    n1 = next(c for c in confirm if c["label"] == "N1_I_to_II")
    n2 = next(c for c in confirm if c["label"] == "N2_I_to_IV")
    causatives_reversed = n1["sign_matches_lock"] and n2["sign_matches_lock"]
    positives = [c for c in confirm if c["locked_sign"] == "positive" and c["passes_gate"]]

    if causatives_reversed and positives:
        verdict = "LATTICE-STRUCTURED"
    elif not causatives_reversed and positives:
        verdict = "INSTRUMENT-CONFOUNDED — H-NEW-2540 downgraded to artifact-suspected"
    elif causatives_reversed:
        verdict = "CAUSATIVE CONTROLS HELD; mutawa'a arms NULL"
    else:
        verdict = "NULL"
    if not p1["sign_matches_lock"]:
        verdict += "; P1 REVERSED (pre-commit violation, full prominence)"
    verdict += "; DEPENDENCY-ANNOTATION-LIMITED"

    result = {
        "id": "H-NEW-2600", "verdict": verdict,
        "raw_p_gate": RAW_GATE, "alpha_bonferroni": ALPHA_BON,
        "confirmatory_inferences": CONFIRMATORY_INFERENCES,
        "min_tokens_per_form_per_root": MIN_TOKENS,
        "confirmatory": confirm,
        "replication_not_independent_support": replic,
        "exploratory_lattice": sorted(lattice, key=lambda c: -c["T_weighted"]),
        "lattice_summary": {
            "cells": len(lattice),
            "cells_positive_T": sum(c["T_weighted"] > 0 for c in lattice),
            "non_mutawaa_non_causative_cells": len(other),
            "of_those_positive_T": sum(c["T_weighted"] > 0 for c in other),
            "note": "If positive T were pervasive across unrelated pairs, the instrument "
                    "would be suspect; this counts that directly.",
        },
        "join": {"qac_verbs": len(qac_verbs), "joined_verbs": len(joined),
                 "joined_active_verbs": len(active), "unmatched_qac_verbs": len(unmatched),
                 "qac_eqtb_agreement": agreement},
        "annotation_limit": "Dependency-annotation-limited; Quran-internal (prereg §7).",
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as h:
        json.dump(result, h, ensure_ascii=False, indent=2, sort_keys=True); h.write("\n")

    manifest = {
        "id": "H-NEW-2600", "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root, text=True).strip(),
        "git_status_porcelain": subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_root, text=True).strip(),
        "hashes_sha256": hashes, "python": sys.version, "platform": platform.platform(),
        "seeds": {"null_a": SEED_NULL_A, "null_b": SEED_NULL_B}, "n_permutations": N_PERM,
        "inherits_extraction_from": "scripts/h-new-2540.py",
        "run_directory": str(run_dir.relative_to(repo_root)),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as h:
        json.dump(manifest, h, ensure_ascii=False, indent=2, sort_keys=True); h.write("\n")

    print(json.dumps({"run_dir": str(run_dir), "verdict": verdict}, ensure_ascii=False))
    for c in confirm + replic:
        print(f"  {c['label']:15} {c['forms'][0]:>4}->{c['forms'][1]:<5} roots={c['eligible_roots']:3} "
              f"T={c['T_weighted']:+.4f} OR={c['mantel_haenszel_or']:8.2f} "
              f"pA={c['p_null_a']:.5f} pB={c['p_null_b_PRIMARY']:.5f} "
              f"sign_ok={c['sign_matches_lock']} gate={c['passes_gate']}")
    s = result["lattice_summary"]
    print(f"  lattice: {s['cells_positive_T']}/{s['cells']} cells positive T; "
          f"unrelated pairs {s['of_those_positive_T']}/{s['non_mutawaa_non_causative_cells']} positive")


if __name__ == "__main__":
    main()
