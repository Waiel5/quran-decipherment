#!/usr/bin/env python3
"""
H-NEW-2570 — cross-corpus Heaps reconciliation against the PARENT finding H-NEW-123.

DESCRIPTIVE ONLY. NO INFERENCE. NO p-VALUES. MW-7 CAPPED.

Required by Amendment 01 (§2.1): the corpus-level Heaps exponent belongs to H-NEW-123
(`findings/phase-b-hypotheses/h-new-123-heap-law.md`, script `scripts/h_new_123_heap_law.py`).
H-NEW-2570 does not re-derive it. This script therefore does three things and nothing else:

  (a) REPRODUCTION — re-runs H-NEW-123's published rows with H-NEW-123's own estimator, to
      confirm the toolchain still reproduces them (Quran beta 0.7468 / V 14,870;
      Bukhari matched-77K beta 0.7472 / V 12,154; Muallaqat beta 0.8313 / N 7,285).
  (b) RECONCILIATION — re-expresses H-NEW-2570's own cross-corpus figures in H-NEW-123's
      estimator so the two findings' numbers are directly comparable, and localises the
      source of any disagreement (normalization rule vs source file).
  (c) ONE CAVEAT RESOLVED — H-NEW-123's caveats flag that its poetry baseline was the
      Muallaqat alone at 7,285 tokens against the Quran's 77,797, a length-curvature artifact
      it could not remove. Adding the seven diwans in data/baseline-corpora/raw/ (which
      H-NEW-123 did not use) permits the fully length-matched poetry comparison. Descriptive,
      MW-7 capped, no p-value.

The estimator is imported, not reimplemented: normalize / tokenize / vocab_curve (linear grid,
step=50, start=100) / fit_heap (log-log OLS) all come from scripts/h_new_123_heap_law.py.

Author: Waiel Al-Shujaa.
"""

import hashlib
import importlib.util
import json
import os
from pathlib import Path

ROOT = "/Users/grey/Downloads/quran"
PARENT_PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md")
AMENDMENT = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2570-amendment-01.md")
PARENT_SHA = "6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b"
AMENDMENT_SHA = "4cd628aaea6c6ce468df47533ffa1a3de80a55366938b6783a2d7cfade49d9ca"
H123 = os.path.join(ROOT, "scripts/h_new_123_heap_law.py")
BASE_RAW = Path(ROOT) / "data" / "baseline-corpora" / "raw"
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2570-heaps-reconciliation.json")

# H-NEW-123 published values, transcribed from findings/phase-b-hypotheses/h-new-123-heap-law.md
H123_PUBLISHED = {
    "quran": {"N": 77797, "V": 14870, "beta": 0.7468, "ci": [0.729, 0.757], "K": 0.724},
    "bukhari_matched77k": {"N": 77797, "V": 12154, "beta": 0.7472, "ci": [0.732, 0.759], "K": 0.605},
    "jahiz_first77k": {"N": 77797, "V": 22984, "beta": 0.8023, "ci": [0.785, 0.811], "K": 0.953},
    "muallaqat_7poems": {"N": 7285, "V": 3843, "beta": 0.8313, "ci": [0.817, 0.849], "K": 1.090},
    "quran_shuffled": {"N": 77797, "V": 14870, "beta": 0.7072, "ci": [0.689, 0.717]},
    "cellB_p": 0.3340,
    "cellA1_p": 0.3826,
}

for path, expect, label in ((PARENT_PREREG, PARENT_SHA, "parent pre-reg"),
                            (AMENDMENT, AMENDMENT_SHA, "amendment 01")):
    with open(path, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != expect:
        raise SystemExit(f"{label} TAMPERED: {got} != {expect}")
    print(f"[ok] {label} SHA-256 verified: {got}")

spec = importlib.util.spec_from_file_location("h123", H123)
h123 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h123)
print(f"[ok] estimator imported from {H123} (step={h123.STEP}, start={h123.START})")


def fit(tokens, label):
    beta, K, N, V = h123.fit_heap(tokens)
    return {"label": label, "N": N, "V": V, "beta": beta, "K": K}


def main():
    out = {
        "note": "DESCRIPTIVE ONLY — no inference, no p-values, MW-7 capped. "
                "Corpus-level Heaps beta is the property of H-NEW-123; see Amendment 01 §2.1.",
        "parent_finding": "H-NEW-123 (findings/phase-b-hypotheses/h-new-123-heap-law.md)",
        "estimator": "scripts/h_new_123_heap_law.py :: normalize/tokenize/vocab_curve/fit_heap "
                     f"(linear grid step={h123.STEP} start={h123.START}, log-log OLS)",
        "prereg_sha256": PARENT_SHA,
        "amendment_sha256": AMENDMENT_SHA,
        "h_new_123_published": H123_PUBLISHED,
        "reproduction": {},
        "length_matched_poetry": {},
        "ordering_invariance_of_beta": {},
    }

    # ---- (a) REPRODUCTION of H-NEW-123's rows, with H-NEW-123's estimator
    q = h123.quran_tokens()
    N_q = len(q)
    out["reproduction"]["quran"] = fit(q, "Quran (no-tashkeel, surface-form, mushaf order)")

    bukh_h123 = h123.file_tokens(BASE_RAW / "matched-bukhari-77k.txt")[:N_q]
    out["reproduction"]["bukhari_matched77k"] = fit(bukh_h123, "Bukhari matched-77k (H-NEW-123 source file)")

    mu = h123.muallaqat_tokens()
    out["reproduction"]["muallaqat_7poems"] = fit(mu, "Muallaqat, 7 poems (H-NEW-123 corpus)")

    jahiz = h123.file_tokens(BASE_RAW / "jahiz-hayawan.txt")[:N_q]
    out["reproduction"]["jahiz_first77k"] = fit(jahiz, "Jahiz Kitab al-Hayawan, first 77k")

    # ---- (b) RECONCILIATION: the Bukhari source file H-NEW-2570 had used
    bukh_noq = h123.file_tokens(BASE_RAW / "bukhari-noquran.txt")[:N_q]
    out["reproduction"]["bukhari_noquran_sensitivity"] = fit(
        bukh_noq, "Bukhari, Quran quotations stripped (H-NEW-2570 source file) — sensitivity only")

    # ---- (c) ONE CAVEAT RESOLVED: length-matched poetry (Muallaqat + diwans)
    poetry_files = sorted(
        f for f in list(BASE_RAW.glob("muallaqa-*.txt")) + list(BASE_RAW.glob("diwan-*.txt"))
        if not f.name.endswith(".raw.txt") and ".openiti." not in f.name
    )
    poetry = []
    for f in poetry_files:
        poetry.extend(h123.file_tokens(f))
    out["length_matched_poetry"] = {
        "files": [f.name for f in poetry_files],
        "n_files": len(poetry_files),
        "available_tokens": len(poetry),
        "matched_to_quran_N": N_q,
        "fit_matched": fit(poetry[:N_q], "Pre-Islamic poetry (7 muallaqat + 7 diwans), matched to Quran N"),
        "h123_caveat_resolved":
            "H-NEW-123 caveat: its poetry baseline was 7,285 tokens vs the Quran's 77,797, an "
            "early-N length-curvature artifact; it reported a post-hoc matched-length figure of "
            "beta_Q7.3K = 0.801 vs Muallaqat 0.831. This row removes the length mismatch.",
    }

    # ---- beta under two surah orderings: the ordering-invariance H-NEW-123 Cell B implies
    import csv as _csv
    rows = list(_csv.DictReader(open(os.path.join(ROOT, "data/revelation-order.csv"), encoding="utf-8")))
    by_surah = h123.quran_tokens_by_surah()
    rev = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["revelation_order"]))]
    nold = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["noldeke_order"]))]
    for label, order in (("mushaf", list(range(1, 115))), ("revelation", rev), ("noldeke", nold)):
        toks = []
        for s in order:
            toks.extend(by_surah[s])
        out["ordering_invariance_of_beta"][label] = fit(toks, f"Quran surface-form, {label} order")
    out["ordering_invariance_of_beta"]["comment"] = (
        "All three orderings use the identical token multiset, so V and N are identical by "
        "construction and only beta/K can move. H-NEW-123 Cell B (p=0.3340, NULL) already "
        "established that beta is near-invariant to shuffling the token stream; these rows are "
        "the surah-permutation analogue. Descriptive."
    )

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    print("\n--- (a) REPRODUCTION of H-NEW-123 with its own estimator ---")
    for key in ("quran", "bukhari_matched77k", "muallaqat_7poems", "jahiz_first77k"):
        r = out["reproduction"][key]
        p = H123_PUBLISHED.get(key)
        tag = ""
        if p:
            tag = f"   [H-NEW-123 published: beta={p['beta']:.4f} V={p['V']}  Δbeta={r['beta']-p['beta']:+.4f}]"
        print(f"  {key:28s} N={r['N']:6d} V={r['V']:6d} beta={r['beta']:.4f} K={r['K']:.3f}{tag}")
    r = out["reproduction"]["bukhari_noquran_sensitivity"]
    print(f"  {'bukhari_noquran (sens.)':28s} N={r['N']:6d} V={r['V']:6d} beta={r['beta']:.4f} K={r['K']:.3f}")

    print("\n--- (c) length-matched poetry (resolves an H-NEW-123 caveat) ---")
    lm = out["length_matched_poetry"]["fit_matched"]
    print(f"  poetry matched to N={N_q}: V={lm['V']} beta={lm['beta']:.4f} K={lm['K']:.3f} "
          f"(from {out['length_matched_poetry']['available_tokens']} available tokens, "
          f"{out['length_matched_poetry']['n_files']} files)")

    print("\n--- beta by surah ordering (identical multiset) ---")
    for k in ("mushaf", "revelation", "noldeke"):
        r = out["ordering_invariance_of_beta"][k]
        print(f"  {k:11s} N={r['N']} V={r['V']} beta={r['beta']:.4f} K={r['K']:.3f}")

    print(f"\n[written] {OUT}")


if __name__ == "__main__":
    main()
