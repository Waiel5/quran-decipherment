#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2550 — Are the 14 muqaṭṭaʿāt letters an articulatory-feature-space optimizer?

Tests the al-Zamakhsharī / al-Suyūṭī "half of each phonetic genus" claim
(al-Kashshāf ad Q 2:1, PageV01P028-029; al-Itqān fawātiḥ nawʿ, PageV03P031)
against the EXACT uniform null over all C(28,14) = 40,116,600 fourteen-letter
subsets of the classical alphabet, and against a corpus-frequency-weighted null.

Pre-registration:
  findings/phase-b-hypotheses/prereg-h-new-2550-muqattaat-phonetic-optimizer.md
Its SHA-256 is embedded below and verified at runtime (fail-fast on mismatch),
per INVESTIGATION-PROTOCOL §1.2.

DEPENDENCY DISCLOSURE (deviation from Protocol §7.1 "stdlib only"): numpy is used.
Justification: the pre-registered null is an EXACT enumeration of every one of the
40,116,600 (resp. 77,558,760) subsets, which is not tractable in pure stdlib Python.
Exactness is strictly stronger than the sampling §7.1's stdlib rule was written to
support. A stdlib-only Monte-Carlo cross-check of the exact result is run as a guard.

Author: Waiel Al-Shujaa
"""

import hashlib
import itertools
import json
import math
import os
import random
import re
import sys
import time
from collections import Counter

import numpy as np

# ----------------------------------------------------------------------------
# 0. PATHS + PRE-REGISTRATION SHA GATE
# ----------------------------------------------------------------------------

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PREREG = os.path.join(ROOT, "findings", "phase-b-hypotheses",
                      "prereg-h-new-2550-muqattaat-phonetic-optimizer.md")
OUT_JSON = os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-2550.json")

PREREG_SHA256 = "3faabc4df31f794db38b6c9495b296501f23fd917c902f0275c9744c38b7d0ed"

SEED = 20260509
SEED_REPLICATION = 20260511
N_MC = 10_000_000
BONFERRONI_K = 20
ALPHA_BON = 0.05 / BONFERRONI_K            # 0.0025


def verify_prereg():
    with open(PREREG, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != PREREG_SHA256:
        raise SystemExit(
            "PRE-REGISTRATION SHA MISMATCH — refusing to run.\n"
            f"  expected {PREREG_SHA256}\n  actual   {got}\n"
            "The pre-registration has been altered since the lock. Per Protocol §1.2 "
            "this run is void."
        )
    print(f"[gate] pre-reg SHA-256 verified: {got}")


# ----------------------------------------------------------------------------
# 1. CORPUS — muqaṭṭaʿāt loci and the 14 letters, DERIVED (never asserted)
# ----------------------------------------------------------------------------

VOCALISATION = set(range(0x064B, 0x0653)) | {0x0670}   # tanwīn..sukūn, superscript alif

# H-NEW-1740 §1 catalogue — used ONLY as an MW-6 cross-check on the derivation.
H1740_SURAHS = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
                36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]

# al-Zamakhsharī's enumerated fourteen (al-Kashshāf ad Q 2:1) — MW-6 cross-check only.
ZAMAKHSHARI_14 = set("الم" "ص" "ر" "ك" "ه" "ي" "ع" "ط" "س" "ح" "ق" "ن")

# al-Zamakhsharī's nine stated intersection counts — MW-6 fail-fast target.
ZAMAKHSHARI_COUNTS = {
    "mahmusa": 5, "majhura": 9, "shadida": 4, "rikhwa": 10, "mutbaqa": 2,
    "munfatiha": 12, "mustaliya": 3, "munkhafida": 11, "qalqala": 2,
}


def derive_muqattaat():
    with open(os.path.join(ROOT, "quran-text", "quran-full-tashkeel.json"), encoding="utf-8") as fh:
        full = json.load(fh)
    with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json"), encoding="utf-8") as fh:
        nt = json.load(fh)

    loci, scanned = [], 0
    for si, srh in enumerate(full):
        for vi in (0, 1):
            if vi >= len(srh["verses"]):
                continue
            scanned += 1
            tok = srh["verses"][vi]["text"].split()[0]
            if not any(ord(c) in VOCALISATION for c in tok):
                loci.append({
                    "surah": srh["id"],
                    "verse": srh["verses"][vi]["id"],
                    "opening": nt[si]["verses"][vi]["text"].split()[0],
                    "opening_vocalised": tok,
                })

    letters = sorted({c for lc in loci for c in lc["opening"]})
    surahs = sorted({lc["surah"] for lc in loci})

    # ---- MW-6 (a,b,c) ------------------------------------------------------
    assert len(loci) == 30, f"MW-6a: expected 30 muqattaat loci, got {len(loci)}"
    assert len(surahs) == 29, f"MW-6a: expected 29 surahs, got {len(surahs)}"
    assert surahs == H1740_SURAHS, "MW-6c: surah catalogue disagrees with H-NEW-1740 §1"
    assert len(letters) == 14, f"MW-6b: expected 14 letters, got {len(letters)}"
    assert set(letters) == ZAMAKHSHARI_14, "MW-6b: derived 14 != al-Zamakhshari's fourteen"
    assert scanned == sum(min(2, len(s["verses"])) for s in full)
    print(f"[MW-6] {len(loci)} loci / {len(surahs)} surahs / 14 letters derived from corpus; "
          f"{scanned} tokens scanned, 0 false positives")
    return loci, letters, surahs


# ----------------------------------------------------------------------------
# 2. LETTER FREQUENCY — reproduces the H-NEW-1810 normalisation exactly
# ----------------------------------------------------------------------------

FOLD = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ت", "ؤ": "و", "ئ": "ي"}

H1810 = {"ا": 59280, "ل": 38191, "ن": 27270, "م": 26735, "ي": 25747, "و": 25486,
         "ه": 14850, "ت": 12864, "ر": 12403, "ب": 11491, "ك": 10497, "ع": 9405,
         "ف": 8747, "ق": 7034, "س": 6012, "د": 5991, "ذ": 4932, "ح": 4140,
         "ج": 3317, "خ": 2497, "ش": 2124, "ص": 2072, "ض": 1686, "ز": 1599,
         "ث": 1414, "ط": 1273, "غ": 1221, "ظ": 853}
H1810_TOTAL, H1810_HAMZA = 329131, 1578


def letter_frequencies():
    with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    c = Counter()
    for srh in d:
        for v in srh["verses"]:
            for ch in v["text"]:
                ch = FOLD.get(ch, ch)
                if "ء" <= ch <= "ي":
                    c[ch] += 1
    hamza = c.pop("ء", 0)
    total = sum(c.values())
    # ---- MW-6 (d) ----------------------------------------------------------
    assert dict(c) == H1810, "MW-6d: letter-frequency table does not reproduce H-NEW-1810"
    assert total == H1810_TOTAL, f"MW-6d: total {total} != {H1810_TOTAL}"
    assert hamza == H1810_HAMZA, f"MW-6d: hamza {hamza} != {H1810_HAMZA}"
    print(f"[MW-6] letter frequencies reproduce H-NEW-1810 exactly "
          f"(28 letters, total {total}, standalone hamza {hamza})")
    return dict(c), hamza


# ----------------------------------------------------------------------------
# 3. THE CLASSICAL PHONETIC FEATURE TABLE (pre-reg §3)
# ----------------------------------------------------------------------------

ALPHABET28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")

MAHMUSA   = set("تثحخسشصفكه")          # 10
SHADIDA   = set("ابتجدطقك")             # 8  (ا = hamza-seat, per al-Zamakhsharī/al-Suyūṭī)
MUTBAQA   = set("صضطظ")                 # 4
MUSTALIYA = set("خصضطظغق")              # 7
QALQALA   = set("بجدطق")                # 5
BAYNIYYA  = set("رعلمن")                # 5 (T-C only)

MAKHRAJ17 = {
    "jawf":          set("ا"),
    "aqsa_al_halq":  set("ه"),
    "wasat_al_halq": set("عح"),
    "adna_al_halq":  set("غخ"),
    "aqsa_al_lisan": set("ق"),
    "kaf":           set("ك"),
    "wasat_al_lisan": set("جشي"),
    "dad":           set("ض"),
    "lam":           set("ل"),
    "nun":           set("ن"),
    "ra":            set("ر"),
    "ta_dal_ta":     set("طدت"),
    "sad_sin_zay":   set("صسز"),
    "za_tha_dhal":   set("ظثذ"),
    "fa":            set("ف"),
    "shafatan":      set("بمو"),
}
# al-Itqān PageV01P346 variant: al-jawf dropped, alif joins aqṣā al-ḥalq.
MAKHRAJ16 = {k: set(v) for k, v in MAKHRAJ17.items() if k != "jawf"}
MAKHRAJ16["aqsa_al_halq"] = set("اه")


def assert_feature_table(muq14):
    """MW-6 (e,f): the table must reproduce al-Zamakhsharī's own nine numbers."""
    S = set(muq14)
    got = {
        "mahmusa":    len(S & MAHMUSA),
        "majhura":    len(S - MAHMUSA),
        "shadida":    len(S & SHADIDA),
        "rikhwa":     len(S - SHADIDA),
        "mutbaqa":    len(S & MUTBAQA),
        "munfatiha":  len(S - MUTBAQA),
        "mustaliya":  len(S & MUSTALIYA),
        "munkhafida": len(S - MUSTALIYA),
        "qalqala":    len(S & QALQALA),
    }
    assert got == ZAMAKHSHARI_COUNTS, (
        "MW-6e: feature table fails to reproduce al-Zamakhshari's stated counts\n"
        f"  stated by al-Zamakhshari: {ZAMAKHSHARI_COUNTS}\n  computed from table:      {got}")
    sizes = (len(MAHMUSA), len(SHADIDA), len(MUTBAQA), len(MUSTALIYA), len(QALQALA), len(BAYNIYYA))
    assert sizes == (10, 8, 4, 7, 5, 5), f"MW-6f: category sizes {sizes}"
    for name, mk in (("17", MAKHRAJ17), ("16", MAKHRAJ16)):
        tot = sum(len(g) for g in mk.values())
        assert tot == 28, f"MW-6f: makhraj-{name} groups cover {tot} letters, not 28"
        union = set().union(*mk.values())
        assert len(union) == 28, f"MW-6f: makhraj-{name} groups overlap"
    assert set(ALPHABET28) == set(H1810), "alphabet/frequency key mismatch"
    print(f"[MW-6] feature table reproduces al-Zamakhshari's nine stated counts: {got}")
    return got


# ----------------------------------------------------------------------------
# 4. TUPLE CONSTRUCTION (pre-reg §4)
# ----------------------------------------------------------------------------

def build_tuples(freq, hamza_count, muq14):
    """Each tuple: inventory (ordered letters), feature list [(name, frozenset)], weights."""
    tuples = {}

    base5 = [("mahmusa", MAHMUSA), ("shadida", SHADIDA), ("mutbaqa", MUTBAQA),
             ("mustaliya", MUSTALIYA), ("qalqala", QALQALA)]

    tuples["T-A"] = dict(
        label="28 letters, al-Zamakhshari's 5 binary sifat (PRIMARY)",
        inventory=list(ALPHABET28),
        features=[(n, frozenset(s)) for n, s in base5],
        weights={k: freq[k] for k in ALPHABET28},
        subset=set(muq14),
    )

    # T-B — hamza ء counted distinct from alif ا (al-Suyuti writes الهمزة).
    inv29 = list(ALPHABET28) + ["ء"]
    # ا as a distinct letter is the madd-alif: majhur, rikhw, munfatih, mustafil, no qalqala.
    # ء carries the shidda that al-Zamakhshari attributed to "the alif".
    shadida_29 = (SHADIDA - {"ا"}) | {"ء"}
    b5 = [("mahmusa", MAHMUSA), ("shadida", shadida_29), ("mutbaqa", MUTBAQA),
          ("mustaliya", MUSTALIYA), ("qalqala", QALQALA)]
    w29 = {k: freq[k] for k in ALPHABET28}
    w29["ء"] = hamza_count
    tuples["T-B"] = dict(
        label="29 letters (hamza distinct from alif), 5 binary sifat",
        inventory=inv29,
        features=[(n, frozenset(s)) for n, s in b5],
        weights=w29,
        subset=set(muq14),          # the attested set takes ا (the corpus grapheme), not ء
    )

    # T-C — later tajwid tripartite manner split.
    rikhw = set(ALPHABET28) - SHADIDA - BAYNIYYA
    c_feats = [("mahmusa", MAHMUSA), ("shadid", SHADIDA), ("bayniyya", BAYNIYYA),
               ("rikhw", rikhw), ("mutbaqa", MUTBAQA), ("mustaliya", MUSTALIYA),
               ("qalqala", QALQALA)]
    tuples["T-C"] = dict(
        label="28 letters, tripartite manner (shadid/bayniyya/rikhw) + 4 other sifat",
        inventory=list(ALPHABET28),
        features=[(n, frozenset(s)) for n, s in c_feats],
        weights={k: freq[k] for k in ALPHABET28},
        subset=set(muq14),
    )

    for key, mk, lab in (("T-D", MAKHRAJ17, "17-makhraj (alif in al-jawf)"),
                         ("T-E", MAKHRAJ16, "16-makhraj (alif in aqsa al-halq)")):
        feats = [(n, frozenset(s)) for n, s in base5]
        feats += [("makhraj:" + n, frozenset(s)) for n, s in sorted(mk.items())]
        tuples[key] = dict(
            label=f"28 letters, 5 binary sifat + {lab}",
            inventory=list(ALPHABET28),
            features=feats,
            weights={k: freq[k] for k in ALPHABET28},
            subset=set(muq14),
        )
    return tuples


# ----------------------------------------------------------------------------
# 5. THE STATISTICS (pre-reg §5)
# ----------------------------------------------------------------------------

def observed(tp):
    """D (unweighted) and D_freq (frequency-weighted) for the attested set."""
    inv, feats, w, S = tp["inventory"], tp["features"], tp["weights"], tp["subset"]
    N, n = len(inv), len(S)
    frac = n / N
    D = Dlit = Dfreq = 0.0
    rows = []
    for name, f in feats:
        k = len(S & f)
        Wf = sum(w[c] for c in f)
        Ws = sum(w[c] for c in (S & f))
        dev = abs(k - len(f) * frac)
        devl = abs(k - len(f) / 2.0)
        devf = abs(Ws / Wf - frac) if Wf else 0.0
        D += dev
        Dlit += devl
        Dfreq += devf
        rows.append({"feature": name, "size": len(f), "in_set": k,
                     "expected_null": round(len(f) * frac, 6),
                     "classical_half": len(f) / 2.0,
                     "abs_dev": round(dev, 6),
                     "mass_share_in_set": round(Ws / Wf, 6) if Wf else None,
                     "mass_share_dev": round(devf, 6)})
    return D, Dlit, Dfreq, rows


def half_tables(letters, feats, w, n_max):
    """For one half of the inventory: per-cardinality arrays of per-feature counts+mass."""
    F = len(feats)
    memb = np.zeros((len(letters), F), dtype=np.int64)
    mass = np.zeros((len(letters), F), dtype=np.float64)
    for i, c in enumerate(letters):
        for t, (_, f) in enumerate(feats):
            if c in f:
                memb[i, t] = 1
                mass[i, t] = w[c]
    out = {}
    for j in range(0, min(len(letters), n_max) + 1):
        idx = list(itertools.combinations(range(len(letters)), j))
        if not idx:
            out[j] = (np.zeros((1, F), np.int64), np.zeros((1, F), np.float64))
            continue
        ar = np.array(idx, dtype=np.int64)
        out[j] = (memb[ar].sum(axis=1), mass[ar].sum(axis=1))
    return out


def exact_null(tp, D_obs, Dfreq_obs, row_chunk=1200):
    """EXACT enumeration over every C(N,n) subset. Returns null summaries for H1 and H2."""
    inv, feats, w, n = tp["inventory"], tp["features"], tp["weights"], len(tp["subset"])
    N, F = len(inv), len(feats)
    frac = n / N
    hA = N // 2
    A, B = inv[:hA], inv[hA:]
    ta, tb = half_tables(A, feats, w, n), half_tables(B, feats, w, n)

    sizes = np.array([len(f) for _, f in feats], dtype=np.int64)
    Wf = np.array([sum(w[c] for c in f) for _, f in feats], dtype=np.float64)
    # D*N is a non-negative integer: |k*N - |f|*n| summed. Use it for an exact histogram.
    target_int = sizes * n                       # compare against k*N
    Dint_obs = int(round(D_obs * N))

    hist = Counter()
    total = 0
    f_le = 0
    f_sum = f_sq = 0.0
    f_min, f_minc = math.inf, 0

    for j in range(0, min(len(A), n) + 1):
        k = n - j
        if k < 0 or k > len(B):
            continue
        ac, am = ta[j]
        bc, bm = tb[k]
        if ac.shape[0] == 0 or bc.shape[0] == 0:
            continue
        for lo in range(0, ac.shape[0], row_chunk):
            acs, ams = ac[lo:lo + row_chunk], am[lo:lo + row_chunk]
            Dint = np.zeros((acs.shape[0], bc.shape[0]), dtype=np.int64)
            Df = np.zeros((acs.shape[0], bc.shape[0]), dtype=np.float64)
            for t in range(F):
                kk = acs[:, t, None] + bc[None, :, t]
                Dint += np.abs(kk * N - target_int[t])
                ms = ams[:, t, None] + bm[None, :, t]
                if Wf[t] > 0:
                    Df += np.abs(ms / Wf[t] - frac)
            total += Dint.size
            uv, uc = np.unique(Dint, return_counts=True)
            hist.update({int(a): int(b) for a, b in zip(uv, uc)})
            f_le += int((Df <= Dfreq_obs + 1e-12).sum())
            f_sum += float(Df.sum())
            f_sq += float((Df * Df).sum())
            bmin = float(Df.min())
            if bmin < f_min - 1e-12:
                f_min, f_minc = bmin, int((Df <= bmin + 1e-12).sum())
            elif abs(bmin - f_min) <= 1e-12:
                f_minc += int((Df <= f_min + 1e-12).sum())

    # ---- MW-6 (g) ----------------------------------------------------------
    assert total == math.comb(N, n), f"MW-6g: enumerated {total}, expected C({N},{n})={math.comb(N, n)}"

    vals = np.array(sorted(hist), dtype=np.int64)
    cts = np.array([hist[int(v)] for v in vals], dtype=np.int64)
    dvals = vals / N
    mean = float((dvals * cts).sum() / total)
    sd = float(math.sqrt(max(0.0, (dvals ** 2 * cts).sum() / total - mean ** 2)))
    le = int(cts[vals <= Dint_obs].sum())
    lt = int(cts[vals < Dint_obs].sum())
    dmin = float(dvals[0])
    at_min = int(cts[0])

    h1 = dict(
        n_subsets=total, D_obs=round(D_obs, 6),
        p_exact_le=le / total, p_exact_lt=lt / total,
        percentile=100.0 * le / total,
        null_mean=round(mean, 6), null_sd=round(sd, 6),
        null_min=round(dmin, 6), n_at_null_min=at_min,
        frac_at_null_min=at_min / total,
        obs_is_global_min=bool(abs(D_obs - dmin) < 1e-9),
        null_median=float(dvals[int(np.searchsorted(np.cumsum(cts), total // 2))]),
        distribution={str(round(float(v) / N, 6)): int(c) for v, c in zip(vals, cts)},
    )
    fmean = f_sum / total
    h2 = dict(
        n_subsets=total, D_freq_obs=round(Dfreq_obs, 6),
        p_exact_le=f_le / total, percentile=100.0 * f_le / total,
        null_mean=round(fmean, 6),
        null_sd=round(math.sqrt(max(0.0, f_sq / total - fmean ** 2)), 6),
        null_min=round(f_min, 6), n_at_null_min=f_minc,
        frac_at_null_min=f_minc / total,
        obs_is_global_min=bool(abs(Dfreq_obs - f_min) < 1e-9),
    )
    return h1, h2


def mc_null(tp, D_obs, Dfreq_obs, seed, n_draw=N_MC, chunk=200_000):
    """N2 — corpus-frequency-weighted draws (Gumbel top-k = exact weighted sampling w/o replacement)."""
    inv, feats, w, n = tp["inventory"], tp["features"], tp["weights"], len(tp["subset"])
    N, F = len(inv), len(feats)
    frac = n / N
    Fmat = np.zeros((N, F), dtype=np.float64)
    for i, c in enumerate(inv):
        for t, (_, f) in enumerate(feats):
            if c in f:
                Fmat[i, t] = 1.0
    wv = np.array([w[c] for c in inv], dtype=np.float64)
    logw = np.log(wv)
    sizes = np.array([len(f) for _, f in feats], dtype=np.float64)
    Wf = (wv[:, None] * Fmat).sum(axis=0)
    tcnt = sizes * frac

    rng = np.random.default_rng(seed)
    le = lef = done = 0
    while done < n_draw:
        m = min(chunk, n_draw - done)
        keys = logw[None, :] + rng.gumbel(size=(m, N))
        idx = np.argpartition(-keys, n - 1, axis=1)[:, :n]
        memb = np.zeros((m, N), dtype=np.float64)
        np.put_along_axis(memb, idx, 1.0, axis=1)
        cnt = memb @ Fmat
        mas = (memb * wv[None, :]) @ Fmat
        D = np.abs(cnt - tcnt[None, :]).sum(axis=1)
        Df = np.abs(np.divide(mas, Wf[None, :], out=np.zeros_like(mas), where=Wf[None, :] > 0)
                    - frac).sum(axis=1)
        le += int((D <= D_obs + 1e-9).sum())
        lef += int((Df <= Dfreq_obs + 1e-12).sum())
        done += m
    return {"n_draw": n_draw, "seed": seed,
            "p_h1": (le + 1) / (n_draw + 1), "p_h2": (lef + 1) / (n_draw + 1),
            "n_le_h1": le, "n_le_h2": lef}


def stdlib_guard(tp, D_obs, seed=SEED, n=200_000):
    """Stdlib-only uniform-subset Monte Carlo — independent guard on the exact N1 H1 p-value."""
    inv, feats, k = tp["inventory"], tp["features"], len(tp["subset"])
    N, frac = len(inv), len(tp["subset"]) / len(inv)
    tgt = [len(f) * frac for _, f in feats]
    rnd = random.Random(seed)
    le = 0
    for _ in range(n):
        S = set(rnd.sample(inv, k))
        D = sum(abs(len(S & f) - tgt[t]) for t, (_, f) in enumerate(feats))
        if D <= D_obs + 1e-9:
            le += 1
    return le / n


# ----------------------------------------------------------------------------
# 6. VERDICTS (pre-reg §8)
# ----------------------------------------------------------------------------

def verdict(D_obs, null, reproduces_zamakhshari=False):
    """Locked four-way decision rule (pre-reg §8), applied literally.

    Order matters and follows the pre-reg text:
      OPTIMIZER-CONFIRMED      p_low < alpha_bon
      REVERSED                 p_upper < alpha_bon  (pre-commit violation)
      CONFIRMED-BUT-MEANINGLESS  the per-category counts reproduce al-Zamakhshari's
                               enumeration AND p_low >= alpha_bon. Only tuple T-A uses
                               the categories he actually enumerated, so only T-A can
                               take this label.
      NULL                     p_low >= alpha_bon and D_obs at or above the null median.
    The pre-reg leaves one combination unlabelled (not significant, does not reproduce
    al-Zamakhshari's enumeration, but D_obs BELOW the null median). It is reported with
    the conservative label below; this gap is disclosed in the finding.
    """
    p_low = null["p_exact_le"]
    p_up = 1.0 - null.get("p_exact_lt", 0.0)
    med = null.get("null_median")
    if p_low < ALPHA_BON:
        return "OPTIMIZER-CONFIRMED"
    if p_up < ALPHA_BON:
        return "REVERSED (pre-commit violation)"
    if reproduces_zamakhshari:
        return "CONFIRMED-BUT-MEANINGLESS"
    if med is not None and D_obs >= med:
        return "NULL"
    return "NULL (non-significant; direction-consistent, D below null median)"


def main():
    t0 = time.time()
    verify_prereg()
    loci, muq14, surahs = derive_muqattaat()
    freq, hamza = letter_frequencies()
    zam = assert_feature_table(muq14)
    tuples = build_tuples(freq, hamza, muq14)

    mass_share_total = sum(freq[c] for c in muq14) / sum(freq.values())
    print(f"[desc] muq-14 carry {mass_share_total:.4%} of corpus letter mass "
          f"(H-NEW-1810 T3 = 0.7441)")

    results = {}
    for key in ("T-A", "T-B", "T-C", "T-D", "T-E"):
        tp = tuples[key]
        D, Dlit, Df, rows = observed(tp)
        print(f"\n=== {key}: {tp['label']} ===")
        print(f"    N={len(tp['inventory'])} features={len(tp['features'])} "
              f"D_obs={D:.4f} D_freq_obs={Df:.6f}")
        t = time.time()
        h1, h2 = exact_null(tp, D, Df)
        print(f"    exact null over {h1['n_subsets']:,} subsets in {time.time()-t:.1f}s "
              f"| H1 p={h1['p_exact_le']:.6g} pct={h1['percentile']:.3f} "
              f"min={h1['null_min']} mass@min={h1['frac_at_null_min']:.6g} "
              f"| H2 p={h2['p_exact_le']:.6g}")
        t = time.time()
        mc = mc_null(tp, D, Df, SEED)
        mcr = mc_null(tp, D, Df, SEED_REPLICATION)
        print(f"    freq-weighted MC 2x{N_MC:,} in {time.time()-t:.1f}s "
              f"| H1 p={mc['p_h1']:.6g}/{mcr['p_h1']:.6g} "
              f"| H2 p={mc['p_h2']:.6g}/{mcr['p_h2']:.6g}")
        guard = stdlib_guard(tp, D)
        results[key] = dict(
            label=tp["label"], N=len(tp["inventory"]), n_features=len(tp["features"]),
            D_obs=round(D, 6), D_obs_literal_half=round(Dlit, 6), D_freq_obs=round(Df, 6),
            per_feature=rows,
            N1_exact_H1=h1, N1_exact_H2=h2,
            N2_mc_seed=mc, N2_mc_replication=mcr,
            stdlib_guard_p_h1=guard,
            p_upper_H1_N1=1.0 - h1["p_exact_lt"],
            verdict_H1_N1=verdict(D, h1, reproduces_zamakhshari=(key == "T-A")),
            verdict_H2_N1=("OPTIMIZER-CONFIRMED" if h2["p_exact_le"] < ALPHA_BON else "NULL"),
            verdict_H1_N2=("OPTIMIZER-CONFIRMED" if mc["p_h1"] < ALPHA_BON else "NULL"),
            verdict_H2_N2=("OPTIMIZER-CONFIRMED" if mc["p_h2"] < ALPHA_BON else "NULL"),
        )

    payload = dict(
        finding_id="H-NEW-2550",
        title="Muqattaat-14 as an articulatory-feature-space optimizer — "
              "al-Zamakhshari's 'half of each genus' against the exact C(28,14) null",
        date="2026-08-07", author="Waiel Al-Shujaa",
        prereg_sha256=PREREG_SHA256,
        seed=SEED, seed_replication=SEED_REPLICATION, n_mc=N_MC,
        bonferroni_k=BONFERRONI_K, alpha_bon=ALPHA_BON,
        muqattaat=dict(
            n_loci=len(loci), n_surahs=len(surahs), surahs=surahs,
            letters=muq14, loci=loci,
        ),
        letter_frequency=dict(counts=freq, standalone_hamza=hamza,
                              total=sum(freq.values()),
                              muq14_mass_share=round(mass_share_total, 6)),
        zamakhshari_stated_counts=zam,
        feature_table=dict(
            mahmusa=sorted(MAHMUSA), shadida=sorted(SHADIDA), mutbaqa=sorted(MUTBAQA),
            mustaliya=sorted(MUSTALIYA), qalqala=sorted(QALQALA), bayniyya=sorted(BAYNIYYA),
            makhraj17={k: sorted(v) for k, v in MAKHRAJ17.items()},
            makhraj16={k: sorted(v) for k, v in MAKHRAJ16.items()},
        ),
        results=results,
        runtime_seconds=round(time.time() - t0, 1),
    )
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    print(f"\n[done] {OUT_JSON} ({time.time()-t0:.1f}s total)")


if __name__ == "__main__":
    main()
