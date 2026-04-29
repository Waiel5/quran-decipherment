#!/usr/bin/env python3
"""H-NEW-123 — Heap's law type-token exponent β for Quran vs Arabic baselines.

Implements the pre-registered analysis at
`findings/phase-b-hypotheses/h-new-123-heap-law-prereg.md`.

Outputs JSON to `findings/phase-b-hypotheses/csv/h-new-123.json`.

Rules tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-surah-1, hafs-kufan, mashriqi).
"""
from __future__ import annotations

import json
import math
import os
import random
import re
import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(ROOT))

from analysis.tools.loader import load_quran  # noqa: E402

# ---------------------------------------------------------------------------
# Normalization (same as data/baseline-corpora/analyze.py)
# ---------------------------------------------------------------------------
ARABIC_LETTERS = set()
for cp in range(0x0621, 0x064B):
    ARABIC_LETTERS.add(chr(cp))
for cp in range(0x0671, 0x06D4):
    ARABIC_LETTERS.add(chr(cp))

REC_MARKS = set(chr(c) for c in range(0x06D6, 0x06EE))
TASHKEEL = set(chr(c) for c in range(0x064B, 0x0660))
TASHKEEL |= {chr(0x0670), chr(0x0640)}


def normalize(s: str) -> str:
    out = []
    for ch in s:
        if ch in TASHKEEL or ch in REC_MARKS:
            continue
        if ch in ARABIC_LETTERS:
            out.append(ch)
        else:
            out.append(" ")
    s = "".join(out)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokenize(s: str) -> List[str]:
    return [t for t in normalize(s).split() if t]


# ---------------------------------------------------------------------------
# Corpus builders
# ---------------------------------------------------------------------------
def quran_tokens() -> List[str]:
    surahs = load_quran("no-tashkeel")
    toks: List[str] = []
    for s in sorted(surahs, key=lambda x: x.id):
        for v in sorted(s.verses, key=lambda x: x.id):
            toks.extend(tokenize(v.text))
    return toks


def quran_tokens_by_surah() -> dict[int, List[str]]:
    surahs = load_quran("no-tashkeel")
    out: dict[int, List[str]] = {}
    for s in surahs:
        toks: List[str] = []
        for v in sorted(s.verses, key=lambda x: x.id):
            toks.extend(tokenize(v.text))
        out[s.id] = toks
    return out


def file_tokens(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return tokenize(text)


def muallaqat_tokens() -> List[str]:
    raw = ROOT / "data" / "baseline-corpora" / "raw"
    files = sorted(raw.glob("muallaqa-*.txt"))
    # restrict to the cleaned (.txt) files, exclude .raw.txt
    files = [f for f in files if not f.name.endswith(".raw.txt")]
    toks: List[str] = []
    for f in files:
        toks.extend(file_tokens(f))
    return toks


# ---------------------------------------------------------------------------
# Heap's law fit
# ---------------------------------------------------------------------------
STEP = 50
START = 100


def vocab_curve(tokens: List[str], step: int = STEP, start: int = START) -> Tuple[List[int], List[int]]:
    seen: set[str] = set()
    ns: List[int] = []
    vs: List[int] = []
    for i, tok in enumerate(tokens, start=1):
        seen.add(tok)
        if i >= start and (i - start) % step == 0:
            ns.append(i)
            vs.append(len(seen))
    # append final N if not already
    if ns and ns[-1] != len(tokens):
        ns.append(len(tokens))
        vs.append(len(seen))
    elif not ns:
        ns.append(len(tokens))
        vs.append(len(seen))
    return ns, vs


def fit_heap(tokens: List[str]) -> Tuple[float, float, int, int]:
    """Return (beta, K, N_total, V_total). log-log OLS on (log N, log V)."""
    ns, vs = vocab_curve(tokens)
    if len(ns) < 3:
        return float("nan"), float("nan"), len(tokens), len(set(tokens))
    xs = [math.log(n) for n in ns]
    ys = [math.log(v) for v in vs]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(len(xs)))
    den = sum((xs[i] - mx) ** 2 for i in range(len(xs)))
    slope = num / den if den > 0 else float("nan")
    intercept = my - slope * mx
    K = math.exp(intercept)
    return slope, K, len(tokens), len(set(tokens))


# ---------------------------------------------------------------------------
# Block bootstrap
# ---------------------------------------------------------------------------
BLOCK = 100
N_BOOT = 1000


def block_bootstrap_beta(tokens: List[str], n_boot: int = N_BOOT,
                         block: int = BLOCK, seed: int = 20260417) -> List[float]:
    rng = random.Random(seed)
    N = len(tokens)
    n_blocks = max(1, N // block)
    betas: List[float] = []
    for _ in range(n_boot):
        starts = [rng.randrange(0, max(1, N - block + 1)) for _ in range(n_blocks)]
        resample: List[str] = []
        for st in starts:
            resample.extend(tokens[st:st + block])
        # trim/pad to N
        if len(resample) > N:
            resample = resample[:N]
        elif len(resample) < N:
            # pad with a final tail
            st = rng.randrange(0, max(1, N - (N - len(resample)) + 1))
            resample.extend(tokens[st:st + (N - len(resample))])
        beta, _, _, _ = fit_heap(resample)
        betas.append(beta)
    return betas


# ---------------------------------------------------------------------------
# Positive controls (MW-5)
# ---------------------------------------------------------------------------
def pos_control_iid_uniform(N: int = 77000, V_star: int = 5000,
                            seed: int = 20260417) -> float:
    rng = random.Random(seed)
    vocab = [f"w{i}" for i in range(V_star)]
    toks = [rng.choice(vocab) for _ in range(N)]
    beta, _, _, _ = fit_heap(toks)
    return beta


def pos_control_all_unique(N: int = 77000) -> float:
    toks = [f"u{i}" for i in range(N)]
    beta, _, _, _ = fit_heap(toks)
    return beta


# ---------------------------------------------------------------------------
# Per-surah analysis
# ---------------------------------------------------------------------------
MUQATTAAT_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
                    31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}


def per_surah_beta() -> list[dict]:
    by_s = quran_tokens_by_surah()
    out = []
    for sid in sorted(by_s):
        toks = by_s[sid]
        beta, K, N, V = fit_heap(toks)
        out.append({
            "surah_id": sid,
            "N": N,
            "V": V,
            "beta": beta,
            "K": K,
            "is_muqattaat": sid in MUQATTAAT_SURAHS,
        })
    return out


def mannwhitney_u(a: List[float], b: List[float]) -> Tuple[float, float]:
    """Two-sample Mann-Whitney U with one-sided p (H1: a < b, via permutation)."""
    import itertools  # noqa: F401
    combined = [(v, 0) for v in a] + [(v, 1) for v in b]
    combined.sort(key=lambda x: x[0])
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    R_a = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 0)
    n_a, n_b = len(a), len(b)
    U_a = R_a - n_a * (n_a + 1) / 2.0
    U_b = n_a * n_b - U_a
    # one-sided H1: a<b → small U_a (a receives low ranks)
    # permutation p-value
    rng = random.Random(20260417)
    N_perm = 10000
    all_vals = list(a) + list(b)
    obs_diff = (sum(a) / n_a) - (sum(b) / n_b)
    count = 0
    for _ in range(N_perm):
        perm = all_vals[:]
        rng.shuffle(perm)
        pa = perm[:n_a]
        pb = perm[n_a:]
        d = sum(pa) / n_a - sum(pb) / n_b
        if d <= obs_diff:
            count += 1
    p_one = (count + 1) / (N_perm + 1)
    return U_a, p_one


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("[H-NEW-123] loading corpora...")
    q_toks = quran_tokens()
    N_q = len(q_toks)
    print(f"  Quran: N={N_q}, V={len(set(q_toks))}")

    bukh_path = ROOT / "data" / "baseline-corpora" / "raw" / "matched-bukhari-77k.txt"
    bukh_toks = file_tokens(bukh_path)[:N_q]
    print(f"  Bukhari-matched: N={len(bukh_toks)}, V={len(set(bukh_toks))}")

    jahiz_path = ROOT / "data" / "baseline-corpora" / "raw" / "jahiz-hayawan.txt"
    jahiz_toks = file_tokens(jahiz_path)[:N_q]
    print(f"  Jahiz: N={len(jahiz_toks)}, V={len(set(jahiz_toks))}")

    mu_toks = muallaqat_tokens()
    # Muallaqat is ~9k tokens, much less than Quran. Use as-is (short poetry corpus),
    # note length-mismatch in findings. For p-test, fit on full muallaqat; report N.
    print(f"  Muallaqat: N={len(mu_toks)}, V={len(set(mu_toks))}")

    # Shuffled Quran
    rng = random.Random(20260417)
    q_shuf = q_toks[:]
    rng.shuffle(q_shuf)
    print(f"  Quran-shuffled: N={len(q_shuf)}, V={len(set(q_shuf))}  (same multiset)")

    # MW-5 positive controls
    print("[H-NEW-123] positive controls...")
    beta_iid = pos_control_iid_uniform(N=N_q, V_star=5000)
    beta_uniq = pos_control_all_unique(N=N_q)
    print(f"  IID-uniform-5000types: β={beta_iid:.4f}  (expect < 0.5)")
    print(f"  All-unique:            β={beta_uniq:.4f}  (expect ≈ 1.0)")
    pos_ok = (beta_iid < 0.5) and (beta_uniq > 0.95)

    # Primary fits
    print("[H-NEW-123] fitting β per corpus...")
    beta_q, K_q, _, V_q = fit_heap(q_toks)
    beta_b, K_b, _, V_b = fit_heap(bukh_toks)
    beta_j, K_j, _, V_j = fit_heap(jahiz_toks)
    beta_m, K_m, _, V_m = fit_heap(mu_toks)
    beta_s, K_s, _, V_s = fit_heap(q_shuf)
    print(f"  β_Quran={beta_q:.4f}, β_Bukhari={beta_b:.4f}, β_Jahiz={beta_j:.4f}, β_Muallaqat={beta_m:.4f}, β_Shuffled={beta_s:.4f}")

    # Bootstrap
    print("[H-NEW-123] bootstrap (this may take a minute)...")
    b_q = block_bootstrap_beta(q_toks, seed=20260417)
    b_b = block_bootstrap_beta(bukh_toks, seed=20260418)
    b_j = block_bootstrap_beta(jahiz_toks, seed=20260419)
    b_m = block_bootstrap_beta(mu_toks, seed=20260420)
    b_s = block_bootstrap_beta(q_shuf, seed=20260421)

    def ci(xs):
        xs_s = sorted(xs)
        return xs_s[int(0.025 * len(xs_s))], xs_s[int(0.975 * len(xs_s))]

    # Cell A one-sided p: fraction of (β_Q_boot - β_base_boot) >= 0, i.e. Quran NOT lower
    def one_sided_p_lower(a, b):
        # H1: a < b; p = fraction of resamples where a >= b
        n = min(len(a), len(b))
        cnt = sum(1 for i in range(n) if a[i] >= b[i])
        return (cnt + 1) / (n + 1)

    def two_sided_p(a, b):
        n = min(len(a), len(b))
        diffs = [a[i] - b[i] for i in range(n)]
        left = sum(1 for d in diffs if d <= 0) / n
        right = sum(1 for d in diffs if d >= 0) / n
        return 2 * min(left, right)

    pA1 = one_sided_p_lower(b_q, b_b)
    pA2 = one_sided_p_lower(b_q, b_j)
    pA3 = one_sided_p_lower(b_q, b_m)
    pB = two_sided_p(b_q, b_s)

    print(f"  Cell A1 (Q<Bukhari): p = {pA1:.4f}")
    print(f"  Cell A2 (Q<Jahiz):   p = {pA2:.4f}")
    print(f"  Cell A3 (Q<Muallaqat): p = {pA3:.4f}")
    print(f"  Cell B (Q vs shuffled): p = {pB:.4f}")

    # Per-surah
    print("[H-NEW-123] per-surah β...")
    surah_rows = per_surah_beta()
    # Restrict ranking to surahs with N >= 200 tokens (β unstable below that)
    surah_ok = [r for r in surah_rows if r["N"] >= 200 and not math.isnan(r["beta"])]
    surah_sorted = sorted(surah_ok, key=lambda r: r["beta"])
    top5_low = surah_sorted[:5]   # most compressed
    top5_high = surah_sorted[-5:][::-1]  # most diverse

    # Muq/nonmuq: restrict to N >= 200 for stability (declared in pre-reg post-hoc? No — pre-reg says "noisy for small surahs")
    # Filter applied to both groups equally.
    muq = [r["beta"] for r in surah_rows
           if r["is_muqattaat"] and r["N"] >= 200 and not math.isnan(r["beta"])]
    nonmuq = [r["beta"] for r in surah_rows
              if not r["is_muqattaat"] and r["N"] >= 200 and not math.isnan(r["beta"])]
    if muq and nonmuq:
        U_c, pC = mannwhitney_u(muq, nonmuq)
        med_muq = sorted(muq)[len(muq) // 2]
        med_non = sorted(nonmuq)[len(nonmuq) // 2]
    else:
        pC, med_muq, med_non = float("nan"), float("nan"), float("nan")

    # ------------------------------------------------------------------
    # Compile results
    # ------------------------------------------------------------------
    result = {
        "id": "H-NEW-123",
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)",
        "bonferroni_k": 4,
        "alpha_bon": 0.0125,
        "fits": {
            "Quran": {"N": len(q_toks), "V": V_q, "beta": beta_q, "K": K_q,
                      "beta_ci95": ci(b_q)},
            "Bukhari_matched77k": {"N": len(bukh_toks), "V": V_b, "beta": beta_b, "K": K_b,
                                   "beta_ci95": ci(b_b)},
            "Jahiz_Hayawan_first77k": {"N": len(jahiz_toks), "V": V_j, "beta": beta_j, "K": K_j,
                                       "beta_ci95": ci(b_j)},
            "Muallaqat_7poems": {"N": len(mu_toks), "V": V_m, "beta": beta_m, "K": K_m,
                                 "beta_ci95": ci(b_m)},
            "Quran_shuffled": {"N": len(q_shuf), "V": V_s, "beta": beta_s, "K": K_s,
                               "beta_ci95": ci(b_s)},
        },
        "positive_controls": {
            "iid_uniform_5000types": {"beta": beta_iid, "expect": "<0.5"},
            "all_unique": {"beta": beta_uniq, "expect": "≈1.0"},
            "pos_ok": pos_ok,
        },
        "primary_cells": {
            "A1_Quran_lt_Bukhari": {"p_one_sided": pA1, "passes": pA1 < 0.0125 and beta_q < beta_b},
            "A2_Quran_lt_Jahiz": {"p_one_sided": pA2, "passes": pA2 < 0.0125 and beta_q < beta_j},
            "A3_Quran_lt_Muallaqat": {"p_one_sided": pA3, "passes": pA3 < 0.0125 and beta_q < beta_m},
            "B_Quran_vs_shuffled": {"p_two_sided": pB, "passes": pB < 0.0125},
        },
        "secondary_muqattaat": {
            "n_muq": len(muq),
            "n_nonmuq": len(nonmuq),
            "median_beta_muq": med_muq,
            "median_beta_nonmuq": med_non,
            "p_one_sided": pC,
            "passes_exploratory": (pC < 0.05) and (med_muq < med_non) if not math.isnan(pC) else False,
        },
        "per_surah_top5_lowest_beta": [
            {"surah_id": r["surah_id"], "N": r["N"], "V": r["V"],
             "beta": r["beta"], "is_muq": r["is_muqattaat"]} for r in top5_low
        ],
        "per_surah_top5_highest_beta": [
            {"surah_id": r["surah_id"], "N": r["N"], "V": r["V"],
             "beta": r["beta"], "is_muq": r["is_muqattaat"]} for r in top5_high
        ],
        "per_surah_full": surah_rows,
    }

    out_path = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-123.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"[H-NEW-123] wrote {out_path}")


if __name__ == "__main__":
    main()
