#!/usr/bin/env python3
"""
H-NEW-2030 — Within-surah ring-composition / chiastic-symmetry detection.

Tests whether verse i resembles verse (n+1-i) more than a permuted verse-order
would produce (chiasm). Verse content = QAC v0.4 STEM-ROOT sets; similarity =
Jaccard. Null = 10,000 within-surah verse-order permutations, seed 20260509.

Outputs JSON to findings/phase-b-hypotheses/csv/h-new-2030.json.

Rules-tuple: (no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root Jaccard,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).

Single-author: Waiel Al-Shujaa, Quran Decipherment Project.
"""
import hashlib
import json
import os
import re
import sys

import numpy as np

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2030-ring-composition.md")
PREREG_SHA = "0999b43f0ce72b084f51584124ef4d2f142b2793ece904b61535649de9b39a8e"
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2030.json")

BASE_SEED = 20260509
N_PERM = 10000
ALPHA_RAW = 0.05
K_BON = 114
ALPHA_BON = ALPHA_RAW / K_BON

# Pre-specified targets (secondary tests)
FARRIN_Q = 2
CUYPERS_Q = 5
BLOCK_BS = [5, 7, 9]  # S3 block-level granularities


def verify_sha():
    with open(PREREG, "rb") as fh:
        actual = hashlib.sha256(fh.read()).hexdigest()
    if actual != PREREG_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH\n expected {PREREG_SHA}\n actual   {actual}\n"
                 "Pre-registration was modified after locking. ABORT (pre-commit discipline).")
    print(f"[ok] pre-reg SHA verified: {actual}")


# QAC data line: (s:v:w:seg)\tform\tPOS\tFEATURES   where FEATURES may contain ROOT:xxx
LINE_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t[^\t]*\t[^\t]*\t(.*)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def load_verse_roots():
    """Return dict surah_id -> list of root-sets, ordered by verse (1..n)."""
    per = {}  # surah -> {verse -> set(roots)}
    with open(QAC, encoding="utf-8") as fh:
        for line in fh:
            m = LINE_RE.match(line.rstrip("\n"))
            if not m:
                continue
            s, v, w, seg = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            feats = m.group(5)
            if "STEM" not in feats:
                continue
            rm = ROOT_RE.search(feats)
            if not rm:
                continue
            root = rm.group(1).strip()
            per.setdefault(s, {}).setdefault(v, set()).add(root)
    surahs = {}
    for s in sorted(per):
        nverses = max(per[s])
        # build ordered list; verses with no roots become empty sets
        surahs[s] = [per[s].get(v, set()) for v in range(1, nverses + 1)]
    return surahs


def jaccard(a, b):
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def chiasm_score(rootsets):
    """Mean Jaccard over disjoint mirror pairs (i, n+1-i), excluding center."""
    n = len(rootsets)
    npairs = n // 2
    if npairs == 0:
        return None, 0
    tot = 0.0
    for i in range(npairs):  # 0-indexed: pair (i, n-1-i)
        tot += jaccard(rootsets[i], rootsets[n - 1 - i])
    return tot / npairs, npairs


def chiasm_score_from_order(rootsets, order):
    n = len(order)
    npairs = n // 2
    tot = 0.0
    for i in range(npairs):
        tot += jaccard(rootsets[order[i]], rootsets[order[n - 1 - i]])
    return tot / npairs


def permutation_test(rootsets, c_obs, surah_id):
    n = len(rootsets)
    npairs = n // 2
    if npairs == 0:
        return None, None, None
    rng = np.random.default_rng(BASE_SEED + surah_id)
    idx = np.arange(n)
    ge = 0
    perm_scores = np.empty(N_PERM)
    for k in range(N_PERM):
        rng.shuffle(idx)
        sc = chiasm_score_from_order(rootsets, idx.tolist())
        perm_scores[k] = sc
        if sc >= c_obs - 1e-12:
            ge += 1
    p = (1 + ge) / (N_PERM + 1)
    mu = float(perm_scores.mean())
    sd = float(perm_scores.std(ddof=1))
    z = (c_obs - mu) / sd if sd > 0 else 0.0
    return p, mu, z


def block_chiasm(rootsets, B):
    """S3: partition verses into B contiguous equal blocks, pool roots, test
    block-mirror Jaccard vs block-order permutation. Returns (c_obs, p, z)."""
    n = len(rootsets)
    if n < B:
        return None
    # contiguous near-equal blocks
    bounds = np.linspace(0, n, B + 1).round().astype(int)
    blocks = []
    for b in range(B):
        s = set()
        for v in range(bounds[b], bounds[b + 1]):
            s |= rootsets[v]
        blocks.append(s)
    npairs = B // 2
    if npairs == 0:
        return None

    def score(order):
        tot = 0.0
        for i in range(npairs):
            tot += jaccard(blocks[order[i]], blocks[order[B - 1 - i]])
        return tot / npairs

    c_obs = score(list(range(B)))
    rng = np.random.default_rng(BASE_SEED + 100000 + B)
    idx = np.arange(B)
    ge = 0
    perms = np.empty(N_PERM)
    for k in range(N_PERM):
        rng.shuffle(idx)
        sc = score(idx.tolist())
        perms[k] = sc
        if sc >= c_obs - 1e-12:
            ge += 1
    p = (1 + ge) / (N_PERM + 1)
    mu, sd = float(perms.mean()), float(perms.std(ddof=1))
    z = (c_obs - mu) / sd if sd > 0 else 0.0
    return {"B": B, "c_obs": c_obs, "p": p, "z": z, "null_mean": mu}


def main():
    verify_sha()
    surahs = load_verse_roots()
    print(f"[ok] loaded {len(surahs)} surahs from QAC")

    results = []
    for s in sorted(surahs):
        rootsets = surahs[s]
        n = len(rootsets)
        c_obs, npairs = chiasm_score(rootsets)
        degenerate = n < 4
        if c_obs is None:
            results.append({"surah": s, "n_verses": n, "n_pairs": 0,
                            "chiasm_score": None, "p_one_sided": None, "z": None,
                            "degenerate": True})
            continue
        p, mu, z = permutation_test(rootsets, c_obs, s)
        results.append({
            "surah": s, "n_verses": n, "n_pairs": npairs,
            "chiasm_score": round(c_obs, 6),
            "null_mean": round(mu, 6),
            "p_one_sided": round(p, 6),
            "z": round(z, 4),
            "degenerate": degenerate,
            "sig_bon": (p < ALPHA_BON) and not degenerate,
            "sig_raw": (p < ALPHA_RAW) and not degenerate,
        })
        print(f"  Q{s:>3}: n={n:>3} C={c_obs:.4f} null={mu:.4f} z={z:+.2f} p={p:.5f}"
              + ("  *BON*" if (p < ALPHA_BON and not degenerate) else
                 ("  *raw*" if (p < ALPHA_RAW and not degenerate) else "")))

    valid = [r for r in results if r["chiasm_score"] is not None and not r["degenerate"]]
    sig_bon = [r for r in valid if r["sig_bon"]]
    sig_raw = [r for r in valid if r["sig_raw"]]
    ranked = sorted(valid, key=lambda r: r["chiasm_score"], reverse=True)
    ranked_z = sorted(valid, key=lambda r: r["z"], reverse=True)

    mean_p = float(np.mean([r["p_one_sided"] for r in valid]))
    mean_z = float(np.mean([r["z"] for r in valid]))

    # Secondary targeted tests
    def get(s):
        return next(r for r in results if r["surah"] == s)
    farrin = get(FARRIN_Q)
    cuypers = get(CUYPERS_Q)

    # S3 block-level on Q2, Q5 + corpus enrichment count of block-significant surahs
    s3 = {"Q2": {}, "Q5": {}}
    for B in BLOCK_BS:
        s3["Q2"][f"B{B}"] = block_chiasm(surahs[FARRIN_Q], B)
        s3["Q5"][f"B{B}"] = block_chiasm(surahs[CUYPERS_Q], B)
    # corpus block-enrichment at B=9 (Farrin's section count)
    block9_sig = 0
    block9_total = 0
    for s in sorted(surahs):
        bc = block_chiasm(surahs[s], 9)
        if bc is not None:
            block9_total += 1
            if bc["p"] < ALPHA_RAW:
                block9_sig += 1

    if len(sig_bon) >= 3:
        verdict = "PASS"
    elif len(sig_bon) >= 1 or len(sig_raw) >= 3:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    summary = {
        "finding_id": "h-new-2030",
        "prereg_sha256": PREREG_SHA,
        "seed": BASE_SEED, "n_perm": N_PERM,
        "k_bonferroni": K_BON, "alpha_raw": ALPHA_RAW, "alpha_bon": ALPHA_BON,
        "verdict": verdict,
        "n_surahs": len(results),
        "n_valid": len(valid),
        "n_sig_bonferroni": len(sig_bon),
        "n_sig_raw": len(sig_raw),
        "sig_bonferroni_surahs": [r["surah"] for r in sig_bon],
        "sig_raw_surahs": [r["surah"] for r in sig_raw],
        "corpus_mean_p": round(mean_p, 4),
        "corpus_mean_z": round(mean_z, 4),
        "top10_by_chiasm_score": [
            {"surah": r["surah"], "C": r["chiasm_score"], "null": r["null_mean"],
             "z": r["z"], "p": r["p_one_sided"], "n": r["n_verses"]}
            for r in ranked[:10]],
        "top10_by_z": [
            {"surah": r["surah"], "C": r["chiasm_score"], "z": r["z"],
             "p": r["p_one_sided"], "n": r["n_verses"]}
            for r in ranked_z[:10]],
        "farrin_q2": {"surah": 2, "C": farrin["chiasm_score"], "null": farrin["null_mean"],
                      "z": farrin["z"], "p": farrin["p_one_sided"], "n": farrin["n_verses"],
                      "sig_raw": farrin["sig_raw"], "sig_bon": farrin["sig_bon"]},
        "cuypers_q5": {"surah": 5, "C": cuypers["chiasm_score"], "null": cuypers["null_mean"],
                       "z": cuypers["z"], "p": cuypers["p_one_sided"], "n": cuypers["n_verses"],
                       "sig_raw": cuypers["sig_raw"], "sig_bon": cuypers["sig_bon"]},
        "s3_block_level": s3,
        "s3_corpus_block9_enrichment": {
            "n_sig_raw": block9_sig, "n_total": block9_total,
            "expected_by_chance": round(0.05 * block9_total, 2)},
        "per_surah": results,
    }

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)

    print("\n=== SUMMARY ===")
    print(f"verdict: {verdict}")
    print(f"sig @ Bonferroni (a={ALPHA_BON:.2e}): {len(sig_bon)} surahs -> {[r['surah'] for r in sig_bon]}")
    print(f"sig @ raw 0.05: {len(sig_raw)} surahs -> {[r['surah'] for r in sig_raw]}")
    print(f"corpus mean p = {mean_p:.4f} (sanity ~0.5 under global null); mean z = {mean_z:+.4f}")
    print("Top-10 by chiasm score:")
    for r in ranked[:10]:
        print(f"  Q{r['surah']:>3} C={r['chiasm_score']:.4f} z={r['z']:+.2f} p={r['p_one_sided']:.5f} (n={r['n_verses']})")
    print(f"Farrin Q2: C={farrin['chiasm_score']:.4f} z={farrin['z']:+.2f} p={farrin['p_one_sided']:.5f}")
    print(f"Cuypers Q5: C={cuypers['chiasm_score']:.4f} z={cuypers['z']:+.2f} p={cuypers['p_one_sided']:.5f}")
    print(f"S3 corpus block-9: {block9_sig}/{block9_total} sig@raw (chance ~{0.05*block9_total:.1f})")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
