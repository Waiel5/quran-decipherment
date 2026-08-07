#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2660 — The exactness hunt.

An exhaustive generator over zero-tolerance structural coincidences of five
pre-declared types, each hit carrying its own combinatorial denominator.

Pre-registration : findings/phase-b-hypotheses/prereg-h-new-2660-exactness-hunt.md
                   SHA-256 verified at runtime; mismatch -> SystemExit.
Author           : Waiel Al-Shujaa
Seed             : 20260509 (primary), 20260519 (replication)

Every denominator that can be written in closed form is written in closed form
and evaluated in exact rational arithmetic. Sampling is used only where the
pre-registration says so.
"""

import os
import sys
import json
import csv
import math
import time
import hashlib
import argparse
import collections
from fractions import Fraction
from datetime import datetime, timezone

import numpy as np

# ----------------------------------------------------------------------------
# 0. LOCKS
# ----------------------------------------------------------------------------

ROOT = "/Users/grey/Downloads/quran"

PREREG_PATH = os.path.join(
    ROOT, "findings/phase-b-hypotheses/prereg-h-new-2660-exactness-hunt.md")
PREREG_SHA256 = "aa0696c5d81a3170a6f5d190971e3201d8c2d8fa01ed262f439dae0a2dd39660"

FROZEN_INPUTS = {
    "quran-text/quran-no-tashkeel.json":
        "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    "quran-text/quran-min-tashkeel.json":
        "87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36",
    "quran-text/quran-full-tashkeel.json":
        "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    "data/morphology/quranic-corpus-morphology-0.4.txt":
        "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    "data/hafs-verse-counts.tsv":
        "e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba",
    "data/revelation-order.csv":
        "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7",
    "findings/phase-b-hypotheses/csv/h-new-840.json":
        "e16a0f70aa842fbe650f2b14874a3f27b176193b86d7964fa9c6b76620ff2aa0",
    "findings/phase-b-hypotheses/csv/h-new-750.json":
        "6f2fd5922e0c59506e20e68318c858b73a317cd9944b1d5d2df6565f6df9fe59",
    "findings/phase-b-hypotheses/csv/h-new-111.json":
        "4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc",
    "findings/phase-b-hypotheses/csv/h-new-720.json":
        "0b342b20639aaf6100cf07d17aca9c9c28f89bf4c127aef3ffd059edb51d4c97",
}

SEED = 20260509
SEED_REPLICATION = 20260519
N_MC = 10_000_000
N_SURAHS = 114
RHO_COUPLE = 0.70          # locked MECHANICAL screen threshold
TOPK_LIST = (7, 14, 29)    # locked derived-class sizes


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_locks():
    got = sha256_file(PREREG_PATH)
    if got != PREREG_SHA256:
        raise SystemExit(
            "PRE-REG SHA MISMATCH\n  expected %s\n  got      %s" % (PREREG_SHA256, got))
    for rel, want in FROZEN_INPUTS.items():
        got = sha256_file(os.path.join(ROOT, rel))
        if got != want:
            raise SystemExit(
                "FROZEN INPUT SHA MISMATCH: %s\n  expected %s\n  got      %s"
                % (rel, want, got))
    print("[lock] pre-reg SHA-256 %s  VERIFIED" % PREREG_SHA256[:16])
    print("[lock] %d frozen inputs VERIFIED" % len(FROZEN_INPUTS))


# ----------------------------------------------------------------------------
# 1. EXACT NULL ENGINES
# ----------------------------------------------------------------------------
#
# ENGINE A — "hits" distribution for a uniform random permutation of a value
# vector v against a fixed target vector t, both of length n.
#
#   M = #{ positions s : v_pi(s) == t(s) }
#
# Rook polynomial of the match board (block-diagonal, one n_w x t_w complete
# block per value w):
#       r(x) = prod_w  sum_j  C(n_w,j) C(t_w,j) j! x^j
# Classical hit formula (Riordan):
#       P(M = h) = sum_{k>=h} (-1)^(k-h) C(k,h) r_k (n-k)! / n!
# Evaluated as exact Fractions using  (n-k)!/n! = 1 / fallingfactorial(n,k).
#
# Truncating the alternating sum yields rigorous Bonferroni bounds, used when
# the board degree is too large to expand in full.

def falling(n, k):
    out = 1
    for i in range(k):
        out *= (n - i)
    return out


def _poly_mul_trunc(a, b, kmax):
    out = [0] * (min(len(a) + len(b) - 2, kmax) + 1)
    for i, ai in enumerate(a):
        if ai == 0 or i > kmax:
            continue
        top = min(len(b) - 1, kmax - i)
        for j in range(top + 1):
            bj = b[j]
            if bj:
                out[i + j] += ai * bj
    return out


def rook_coeffs(mult_v, mult_t, kmax):
    """r_k for k = 0..kmax of the block-diagonal match board."""
    poly = [1]
    for w, nw in mult_v.items():
        tw = mult_t.get(w, 0)
        if tw == 0 or nw == 0:
            continue
        jmax = min(nw, tw, kmax)
        blk = [0] * (jmax + 1)
        for j in range(jmax + 1):
            blk[j] = math.comb(nw, j) * math.comb(tw, j) * math.factorial(j)
        poly = _poly_mul_trunc(poly, blk, kmax)
    return poly


def hits_pmf_exact(mult_v, mult_t, n, kmax=None):
    """Exact P(M = h) for h = 0..D. Returns (pmf list of Fractions, exact_flag)."""
    D = sum(min(nw, mult_t.get(w, 0)) for w, nw in mult_v.items())
    if kmax is None:
        kmax = D
    exact = (kmax >= D)
    r = rook_coeffs(mult_v, mult_t, kmax)
    r += [0] * (kmax + 1 - len(r))
    pmf = []
    for h in range(kmax + 1):
        tot = Fraction(0)
        for k in range(h, kmax + 1):
            if r[k] == 0:
                continue
            term = Fraction(math.comb(k, h) * r[k], falling(n, k))
            tot += term if ((k - h) % 2 == 0) else -term
        pmf.append(tot)
    return pmf, exact


def hits_tail_exact(mult_v, mult_t, n, h_obs, kmax_cap=64):
    """
    Exact P(M >= h_obs) when the full board can be expanded; otherwise rigorous
    Bonferroni bounds from the truncated alternating series.
    Returns dict with p, p_lo, p_hi, exact, expectation.
    """
    D = sum(min(nw, mult_t.get(w, 0)) for w, nw in mult_v.items())
    exp_hits = float(sum(nw * mult_t.get(w, 0) for w, nw in mult_v.items())) / n

    if D <= 256:
        pmf, _ = hits_pmf_exact(mult_v, mult_t, n)
        if h_obs > len(pmf) - 1:
            p = Fraction(0)
        else:
            p = sum(pmf[h] for h in range(h_obs, len(pmf)))
        pf = float(p)
        return dict(p=pf, p_lo=pf, p_hi=pf, exact=True,
                    expectation=exp_hits, board_degree=D)

    # Truncated inclusion-exclusion on the "at least h" form:
    #   P(M >= h) = sum_{k>=h} (-1)^(k-h) C(k-1,h-1) r_k (n-k)!/n!
    kmax = min(D, max(h_obs + kmax_cap, kmax_cap))
    r = rook_coeffs(mult_v, mult_t, kmax)
    r += [0] * (kmax + 1 - len(r))
    partials = []
    tot = Fraction(0)
    for k in range(max(h_obs, 0), kmax + 1):
        if h_obs == 0:
            partials.append(Fraction(1))
            break
        if r[k] == 0:
            partials.append(tot)
            continue
        term = Fraction(math.comb(k - 1, h_obs - 1) * r[k], falling(n, k))
        tot += term if ((k - h_obs) % 2 == 0) else -term
        partials.append(tot)
    if h_obs == 0:
        return dict(p=1.0, p_lo=1.0, p_hi=1.0, exact=True,
                    expectation=exp_hits, board_degree=D)
    lo = float(min(partials[-2:] if len(partials) >= 2 else partials))
    hi = float(max(partials[-2:] if len(partials) >= 2 else partials))
    return dict(p=float(partials[-1]), p_lo=max(0.0, lo), p_hi=min(1.0, hi),
                exact=False, expectation=exp_hits, board_degree=D)


# ENGINE B — exact "monochromatic mirror pair" distribution.
#
# Randomly permute a multiset of n=114 values into 114 positions grouped into 57
# fixed disjoint ordered pairs.  M = # pairs whose two entries are equal.
#   q_k = C(57,k) * k! * [y^k] prod_w ( sum_j falling(n_w,2j) y^j / j! )
#   P(M = h) = sum_{k>=h} (-1)^(k-h) C(k,h) q_k (n-2k)! / n!

def mirror_pmf_exact(mult, n=N_SURAHS, npairs=None):
    if npairs is None:
        npairs = n // 2
    kmax = npairs
    poly = [Fraction(1)]
    for w, nw in mult.items():
        jmax = min(nw // 2, kmax)
        if jmax == 0:
            continue
        blk = [Fraction(0)] * (jmax + 1)
        for j in range(jmax + 1):
            blk[j] = Fraction(falling(nw, 2 * j), math.factorial(j))
        new = [Fraction(0)] * (min(len(poly) + len(blk) - 2, kmax) + 1)
        for i, ai in enumerate(poly):
            if ai == 0:
                continue
            for j, bj in enumerate(blk):
                if bj and i + j <= kmax:
                    new[i + j] += ai * bj
        poly = new
    poly += [Fraction(0)] * (kmax + 1 - len(poly))
    q = [math.comb(npairs, k) * math.factorial(k) * poly[k] for k in range(kmax + 1)]
    pmf = []
    for h in range(kmax + 1):
        tot = Fraction(0)
        for k in range(h, kmax + 1):
            if q[k] == 0:
                continue
            term = Fraction(math.comb(k, h)) * q[k] * Fraction(
                math.factorial(n - 2 * k), math.factorial(n))
            tot += term if ((k - h) % 2 == 0) else -term
        pmf.append(tot)
    return pmf


def validate_engines():
    """MW-6(f): validate both exact engines against brute-force enumeration."""
    import itertools
    rng = np.random.default_rng(SEED)
    for trial in range(5):
        n = int(rng.integers(4, 8))
        v = list(rng.integers(0, 3, size=n))
        t = list(rng.integers(0, 3, size=n))
        brute = collections.Counter()
        for perm in itertools.permutations(range(n)):
            brute[sum(1 for s in range(n) if v[perm[s]] == t[s])] += 1
        tot = math.factorial(n)
        pmf, ex = hits_pmf_exact(collections.Counter(v), collections.Counter(t), n)
        if not ex:
            raise SystemExit("MW-6(f) FAIL: engine A not exact on small case")
        for h in range(len(pmf)):
            want = Fraction(brute.get(h, 0), tot)
            if pmf[h] != want:
                raise SystemExit(
                    "MW-6(f) FAIL engine A trial %d h=%d: %s vs %s"
                    % (trial, h, pmf[h], want))
    for trial in range(5):
        npairs = int(rng.integers(2, 4))
        n = 2 * npairs
        vals = list(rng.integers(0, 3, size=n))
        brute = collections.Counter()
        for perm in itertools.permutations(range(n)):
            arr = [vals[p] for p in perm]
            brute[sum(1 for i in range(npairs) if arr[2 * i] == arr[2 * i + 1])] += 1
        tot = math.factorial(n)
        pmf = mirror_pmf_exact(collections.Counter(vals), n=n, npairs=npairs)
        for h in range(len(pmf)):
            want = Fraction(brute.get(h, 0), tot)
            if pmf[h] != want:
                raise SystemExit(
                    "MW-6(f) FAIL engine B trial %d h=%d: %s vs %s"
                    % (trial, h, pmf[h], want))
    print("[MW-6f] exact hit-engine and mirror-engine validated "
          "against full brute-force enumeration on 10 randomised cases")


# ----------------------------------------------------------------------------
# 2. DATA
# ----------------------------------------------------------------------------

AR_LETTERS = set(chr(c) for c in range(0x0621, 0x064B))
VOWEL_MARKS = set(chr(c) for c in range(0x064B, 0x0653)) | {"ٰ"}
NORM_MAP = {"أ": "ا", "إ": "ا", "آ": "ا",
            "ٱ": "ا", "ى": "ي", "ة": "ه",
            "ؤ": "و", "ئ": "ي"}


def normalise(s):
    return "".join(NORM_MAP.get(ch, ch) for ch in s if ch != "ـ")


def strip_marks(s):
    return "".join(ch for ch in s if ch in AR_LETTERS or ch == " ")


def jpath(rel):
    return os.path.join(ROOT, rel)


def load_corpus():
    with open(jpath("quran-text/quran-no-tashkeel.json"), encoding="utf-8") as f:
        plain = json.load(f)
    with open(jpath("quran-text/quran-min-tashkeel.json"), encoding="utf-8") as f:
        mint = json.load(f)
    with open(jpath("quran-text/quran-full-tashkeel.json"), encoding="utf-8") as f:
        full = json.load(f)
    return plain, mint, full


def load_qac():
    """Return per-segment records with root/lemma and (surah, verse) location."""
    import re
    recs = []
    rx_root = re.compile(r"ROOT:([^|]+)")
    rx_lem = re.compile(r"LEM:([^|]+)")
    rx_pos = re.compile(r"POS:([A-Z]+)")
    with open(jpath("data/morphology/quranic-corpus-morphology-0.4.txt"),
              encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            nums = loc.strip("()").split(":")
            if len(nums) != 4:
                continue
            s, v = int(nums[0]), int(nums[1])
            mr = rx_root.search(feats)
            ml = rx_lem.search(feats)
            mp = rx_pos.search(feats)
            recs.append((s, v,
                         mr.group(1) if mr else None,
                         ml.group(1) if ml else None,
                         mp.group(1) if mp else None))
    return recs


def load_verse_counts():
    vc = {}
    with open(jpath("data/hafs-verse-counts.tsv"), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b = line.split("\t")
            vc[int(a)] = int(b)
    return vc


def load_revelation_order():
    rev, nold, period, nphase = {}, {}, {}, {}
    with open(jpath("data/revelation-order.csv"), encoding="utf-8") as f:
        for row in csv.DictReader(f):
            m = int(row["mushaf_order"])
            rev[m] = int(row["revelation_order"])
            nold[m] = int(row["noldeke_order"])
            period[m] = row["period"].strip().lower()
            nphase[m] = row["noldeke_phase"].strip()
    return rev, nold, period, nphase


# ----------------------------------------------------------------------------
# 3. AXES AND METRICS
# ----------------------------------------------------------------------------

def build_surah_features(plain, mint, full, qac, vc, rev, nold, tuple_name):
    """
    tuple_name in {"T-ROOT","T-LEMMA","T-NORM"}.
    Returns (axes dict name->list[114], metrics dict name->list[114] of ints).
    """
    norm = (tuple_name == "T-NORM")
    unit_field = 3 if tuple_name == "T-LEMMA" else 2   # 2=root, 3=lemma

    # --- textual axes -------------------------------------------------------
    n_verses, n_words, n_letters, n_types = [], [], [], []
    for su in plain:
        toks, letters, typeset = 0, 0, set()
        for vs in su["verses"]:
            txt = strip_marks(vs["text"])
            if norm:
                txt = normalise(txt)
            tk = [t for t in txt.split() if t]
            toks += len(tk)
            typeset.update(tk)
            letters += sum(1 for ch in txt if ch != " ")
        n_verses.append(vc[su["id"]])
        n_words.append(toks)
        n_letters.append(letters)
        n_types.append(len(typeset))

    # --- rhyme axes ---------------------------------------------------------
    src = full if norm else mint
    n_rhyme_classes, modal_rhyme_count = [], []
    for su in src:
        finals = []
        for vs in su["verses"]:
            txt = strip_marks(vs["text"])
            if norm:
                txt = normalise(txt)
            txt = txt.strip()
            finals.append(txt[-1] if txt else "?")
        c = collections.Counter(finals)
        n_rhyme_classes.append(len(c))
        modal_rhyme_count.append(max(c.values()) if c else 0)

    # --- morphological axes -------------------------------------------------
    per_surah_units = collections.defaultdict(collections.Counter)
    per_surah_roots = collections.defaultdict(collections.Counter)
    per_surah_lemmas = collections.defaultdict(collections.Counter)
    global_unit_surahs = collections.defaultdict(set)
    for r in qac:
        s = r[0]
        u = r[unit_field]
        if u:
            per_surah_units[s][u] += 1
            global_unit_surahs[u].add(s)
        if r[2]:
            per_surah_roots[s][r[2]] += 1
        if r[3]:
            per_surah_lemmas[s][r[3]] += 1

    n_root_tokens, n_distinct_roots, n_distinct_lemmas = [], [], []
    n_hapax, n_exclusive = [], []
    for s in range(1, N_SURAHS + 1):
        cu = per_surah_units[s]
        n_root_tokens.append(sum(cu.values()))
        n_distinct_roots.append(len(per_surah_roots[s]))
        n_distinct_lemmas.append(len(per_surah_lemmas[s]))
        n_hapax.append(sum(1 for u, c in cu.items() if c == 1))
        n_exclusive.append(sum(1 for u in cu if len(global_unit_surahs[u]) == 1))

    # --- precomputed artefacts ---------------------------------------------
    with open(jpath("findings/phase-b-hypotheses/csv/h-new-840.json"),
              encoding="utf-8") as f:
        d840 = json.load(f)
    uas = {e["surah"]: e["UAS"] for e in d840["all_uas"]}
    maxcost = {e["surah"]: e["max_cost"] for e in d840["all_uas"]}
    with open(jpath("findings/phase-b-hypotheses/csv/h-new-750.json"),
              encoding="utf-8") as f:
        d750 = json.load(f)
    rh_ent = {e["surah"]: e["rhyme_entropy_nats"] for e in d750["per_surah"]}
    mcd = {e["surah"]: e["mean_content_distance"] for e in d750["per_surah"]}
    lcoh = {e["surah"]: e["local_cohesion"] for e in d750["per_surah"]}
    with open(jpath("findings/phase-b-hypotheses/csv/h-new-111.json"),
              encoding="utf-8") as f:
        d111 = json.load(f)
    acc = collections.defaultdict(float)
    cnt = collections.defaultdict(int)
    for i, j, d in d111["D_matrix_upper_triangular"]:
        acc[i] += d; cnt[i] += 1
        acc[j] += d; cnt[j] += 1
    fr_centroid = {s: acc[s] / cnt[s] for s in acc}

    rng = np.random.default_rng(SEED)
    decoy = list(rng.random(N_SURAHS))

    axes = collections.OrderedDict()
    axes["A01_n_verses"] = [float(x) for x in n_verses]
    axes["A02_n_words"] = [float(x) for x in n_words]
    axes["A03_n_letters"] = [float(x) for x in n_letters]
    axes["A04_n_word_types"] = [float(x) for x in n_types]
    axes["A05_n_root_tokens"] = [float(x) for x in n_root_tokens]
    axes["A06_n_distinct_roots"] = [float(x) for x in n_distinct_roots]
    axes["A07_n_distinct_lemmas"] = [float(x) for x in n_distinct_lemmas]
    axes["A08_n_surah_hapax"] = [float(x) for x in n_hapax]
    axes["A09_n_exclusive"] = [float(x) for x in n_exclusive]
    axes["A10_mean_verse_letters"] = [n_letters[i] / n_verses[i] for i in range(N_SURAHS)]
    axes["A11_mean_verse_words"] = [n_words[i] / n_verses[i] for i in range(N_SURAHS)]
    axes["A12_n_rhyme_classes"] = [float(x) for x in n_rhyme_classes]
    axes["A13_modal_rhyme_count"] = [float(x) for x in modal_rhyme_count]
    axes["A14_type_token_ratio"] = [n_types[i] / n_words[i] for i in range(N_SURAHS)]
    axes["A15_revelation_order"] = [float(rev[s]) for s in range(1, 115)]
    axes["A16_noldeke_order"] = [float(nold[s]) for s in range(1, 115)]
    axes["A17_UAS"] = [float(uas[s]) for s in range(1, 115)]
    axes["A18_rhyme_entropy"] = [float(rh_ent[s]) for s in range(1, 115)]
    axes["A19_mean_content_distance"] = [float(mcd[s]) for s in range(1, 115)]
    axes["A20_local_cohesion"] = [float(lcoh[s]) for s in range(1, 115)]
    axes["A21_fr_centroid_dist"] = [float(fr_centroid[s]) for s in range(1, 115)]
    axes["A22_max_neighbour_tsp"] = [float(maxcost[s]) for s in range(1, 115)]
    axes["A23_DECOY"] = decoy

    metrics = collections.OrderedDict()
    metrics["M01_n_verses"] = n_verses
    metrics["M02_n_words"] = n_words
    metrics["M03_n_letters"] = n_letters
    metrics["M04_n_word_types"] = n_types
    metrics["M05_n_root_tokens"] = n_root_tokens
    metrics["M06_n_distinct_roots"] = n_distinct_roots
    metrics["M07_n_distinct_lemmas"] = n_distinct_lemmas
    metrics["M08_n_surah_hapax"] = n_hapax
    metrics["M09_n_exclusive"] = n_exclusive
    metrics["M10_n_rhyme_classes"] = n_rhyme_classes
    metrics["M11_modal_rhyme_count"] = modal_rhyme_count
    metrics["M12_mushaf_position"] = list(range(1, 115))
    metrics["M13_revelation_order"] = [rev[s] for s in range(1, 115)]
    metrics["M14_noldeke_order"] = [nold[s] for s in range(1, 115)]

    return axes, metrics


# ----------------------------------------------------------------------------
# 4. MUQATTA'AT DETECTOR (MW-6d) — never names the letters it seeks
# ----------------------------------------------------------------------------

def detect_muqattaat(full):
    loci, letters, per_surah = [], set(), {}
    scanned = 0
    for su in full:
        for vs in su["verses"][:2]:
            scanned += 1
            first = vs["text"].split()[0] if vs["text"].split() else ""
            if not first:
                continue
            if any(ch in VOWEL_MARKS for ch in first):
                continue
            bare = "".join(ch for ch in first if ch in AR_LETTERS)
            if not bare:
                continue
            loci.append((su["id"], vs["id"], bare))
            letters.update(bare)
            per_surah.setdefault(su["id"], bare)
    return loci, sorted(letters), per_surah, scanned


# ----------------------------------------------------------------------------
# 5. SURAH CLASSES
# ----------------------------------------------------------------------------

def build_classes(plain, full, qac, axes, metrics, muq_per_surah, period, nphase):
    classes = collections.OrderedDict()
    muq = set(muq_per_surah)
    classes["C01_muqattaat"] = muq
    classes["C02_hawamim"] = {s for s, t in muq_per_surah.items() if t == "حم"}
    classes["C03_ALM"] = {s for s, t in muq_per_surah.items()
                          if t == "الم"}
    classes["C04_ALR"] = {s for s, t in muq_per_surah.items()
                          if t == "الر"}
    classes["C05_meccan"] = {s for s in range(1, 115) if period[s] == "meccan"}
    classes["C06_medinan"] = {s for s in range(1, 115) if period[s] == "medinan"}
    for tag, key in (("C07_noldeke_early_meccan", "Early Meccan"),
                     ("C08_noldeke_middle_meccan", "Middle Meccan"),
                     ("C09_noldeke_late_meccan", "Late Meccan"),
                     ("C10_noldeke_medinan", "Medinan")):
        classes[tag] = {s for s in range(1, 115) if nphase[s] == key}
    v1_sbh = set()
    for s, v, root, lem, pos in qac:
        if v == 1 and root == "sbH" and pos == "V":
            v1_sbh.add(s)
    classes["C11_musabbihat"] = v1_sbh
    first_tok = {}
    for su in plain:
        t = su["verses"][0]["text"].split()
        first_tok[su["id"]] = t[0] if t else ""
    classes["C12_opens_qul"] = {s for s, t in first_tok.items() if t == "قل"}
    sajdah = set()
    for su in full:
        if any("۩" in vs["text"] for vs in su["verses"]):
            sajdah.add(su["id"])
    classes["C13_has_sajdah_glyph"] = sajdah
    classes["C14_v1_has_basmala"] = {
        su["id"] for su in plain
        if "بسم الله" in su["verses"][0]["text"]}
    classes["C15_odd_verse_count"] = {
        s for s in range(1, 115) if metrics["M01_n_verses"][s - 1] % 2 == 1}
    classes["C16_v1_starts_waw"] = {s for s, t in first_tok.items()
                                    if t.startswith("و")}
    classes["C17_v1_starts_ya"] = {s for s, t in first_tok.items()
                                   if t.startswith("يا")}
    classes["C18_rhyme_homogeneous"] = {
        s for s in range(1, 115) if metrics["M10_n_rhyme_classes"][s - 1] == 1}

    base_names = list(classes.keys())

    # derived top-k / bottom-k, ties broken by lowest surah number (locked)
    derived_source = {}
    for aname, vals in axes.items():
        order_hi = sorted(range(N_SURAHS), key=lambda i: (-vals[i], i))
        order_lo = sorted(range(N_SURAHS), key=lambda i: (vals[i], i))
        for k in TOPK_LIST:
            nm = "TOP%d_%s" % (k, aname)
            classes[nm] = {order_hi[i] + 1 for i in range(k)}
            derived_source[nm] = aname
            nm = "BOT%d_%s" % (k, aname)
            classes[nm] = {order_lo[i] + 1 for i in range(k)}
            derived_source[nm] = aname
    return classes, base_names, derived_source


# ----------------------------------------------------------------------------
# 6. HELPERS
# ----------------------------------------------------------------------------

def spearman(x, y):
    n = len(x)
    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = ranks(x), ranks(y)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx and dy else 0.0


def extremum_positions(vals, mode):
    """Return (chosen_index, tie_count). Ties -> lowest surah number (locked)."""
    best = max(vals) if mode == "max" else min(vals)
    idxs = [i for i, v in enumerate(vals) if v == best]
    return idxs[0], len(idxs)


def extremum_pmf(t, n=N_SURAHS):
    """
    EXACT distribution of the extremum position under a uniform random
    permutation of the axis's own values, with the locked lowest-index
    tie-break.  The t tied extremal values occupy a uniform random t-subset of
    the n positions and the extremum is that subset's minimum, so
        P(pos = s) = C(n-1-s, t-1) / C(n, t)        (s zero-based)
    For t = 1 this is the uniform 1/n.
    """
    denom = math.comb(n, t)
    return [math.comb(n - 1 - s, t - 1) / denom if (n - 1 - s) >= (t - 1) else 0.0
            for s in range(n)]


def digit_reverse(n):
    return int(str(n)[::-1])


def digit_sum(n):
    return sum(int(c) for c in str(n))


def is_functional(a, b):
    """True iff a determines b (the map a -> b is single-valued)."""
    seen = {}
    for x, y in zip(a, b):
        if x in seen and seen[x] != y:
            return False
        seen[x] = y
    return True


def mechanical_screen(a, b, constructional=False):
    """
    Locked pre-reg §6 screen, applied identically wherever two integer vectors
    are compared for exact equality.

    `constructional` (§6.2) is supplied from the DECLARED source map, never
    inferred: an injective vector such as mushaf position trivially "determines"
    every other vector, so an inferred functional-dependence test would flag
    every M12/M13/M14 cell as mechanical and silently suppress genuinely open
    comparisons (mushaf position vs revelation order among them).  Inferring it
    is therefore anti-conservative for a null-seeking test and is not done.
    """
    ordered = all(x <= y for x, y in zip(a, b)) or all(x >= y for x, y in zip(a, b))
    rho = spearman([float(x) for x in a], [float(x) for x in b])
    return dict(mechanical=(constructional or ordered or abs(rho) >= RHO_COUPLE),
                constructional=constructional, ordered=ordered,
                rho=round(rho, 4))


def hyper_upper_tail(k, j, n=N_SURAHS):
    """Exact P(overlap >= j) for a uniform random k-subset vs a fixed k-subset."""
    tot = math.comb(n, k)
    s = 0
    for i in range(j, k + 1):
        s += math.comb(k, i) * math.comb(n - k, k - i)
    return s / tot


# ----------------------------------------------------------------------------
# 7. THE FOUR SWEEPS
# ----------------------------------------------------------------------------

def sweep_E1(axes, tuple_name, coupled_pairs):
    names = list(axes.keys())
    ext = {}
    for nm in names:
        for mode in ("max", "min"):
            i, t = extremum_positions(axes[nm], mode)
            ext[(nm, mode)] = (i, t, extremum_pmf(t))
    cells, hits = [], []
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            na, nb = names[a], names[b]
            rho = spearman(axes[na], axes[nb])
            coupled = (abs(rho) >= RHO_COUPLE) or ((na, nb) in coupled_pairs) \
                or ((nb, na) in coupled_pairs)
            for ma, mb in (("max", "max"), ("min", "min"),
                           ("max", "min"), ("min", "max")):
                ia, ta, pa = ext[(na, ma)]
                ib, tb, pb = ext[(nb, mb)]
                # EXACT denominator: P(same extremum surah) under independent
                # permutation of each axis, tie-structure respected.
                p_exact = sum(pa[s] * pb[s] for s in range(N_SURAHS))
                cell = dict(tuple=tuple_name, axis_a=na, axis_b=nb,
                            mode_a=ma, mode_b=mb, surah_a=ia + 1, surah_b=ib + 1,
                            rho=round(rho, 4), ties_a=ta, ties_b=tb,
                            p_exact=p_exact, coupled=coupled, hit=(ia == ib))
                cells.append(cell)
                if cell["hit"]:
                    hits.append(cell)
    return cells, hits


def sweep_E1_family(axes, obs, obs_dec, coupled_mask, rng, n_mc=N_MC):
    """
    Family null at the pre-registered 10^7 draws. Extremum positions are drawn
    from their EXACT per-axis distributions (tie-aware), independently across
    axes, which is precisely null N1.
    """
    names = list(axes.keys())
    cdfs = []
    key = {}
    for nm in names:
        for mode in ("max", "min"):
            _, t = extremum_positions(axes[nm], mode)
            key[(nm, mode)] = len(cdfs)
            cdfs.append(np.cumsum(np.array(extremum_pmf(t))))
    cdfs = np.array(cdfs)
    cdfs[:, -1] = 1.0
    ia, ib = [], []
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            for ma, mb in (("max", "max"), ("min", "min"),
                           ("max", "min"), ("min", "max")):
                ia.append(key[(names[a], ma)])
                ib.append(key[(names[b], mb)])
    ia = np.array(ia); ib = np.array(ib)
    dec = np.array(coupled_mask) == False           # noqa: E712
    ge, ge_dec, done = 0, 0, 0
    chunk = 20_000
    n_draw = cdfs.shape[0]
    while done < n_mc:
        b = min(chunk, n_mc - done)
        u = rng.random((b, n_draw))
        pos = np.empty((b, n_draw), dtype=np.int16)
        for j in range(n_draw):
            pos[:, j] = np.searchsorted(cdfs[j], u[:, j], side="left")
        eq = pos[:, ia] == pos[:, ib]
        ge += int((eq.sum(axis=1) >= obs).sum())
        ge_dec += int((eq[:, dec].sum(axis=1) >= obs_dec).sum())
        done += b
    return ge / n_mc, ge_dec / n_mc, len(ia)


BASE_CLASS_SOURCE_AXIS = {
    "C18_rhyme_homogeneous": "A12_n_rhyme_classes",
    "C15_odd_verse_count": "A01_n_verses",
}


def sweep_E2(classes, base_names, derived_source, axes):
    names = list(classes.keys())
    by_size = collections.defaultdict(list)
    for nm in names:
        by_size[len(classes[nm])].append(nm)
    rho_cache = {}

    def axis_rho(a1, a2):
        key = tuple(sorted((a1, a2)))
        if key not in rho_cache:
            rho_cache[key] = spearman(axes[a1], axes[a2])
        return rho_cache[key]

    cells, hits, nearmiss = [], [], []
    for size, group in by_size.items():
        if size == 0 or size == N_SURAHS:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                n1, n2 = group[i], group[j]
                s1, s2 = classes[n1], classes[n2]
                ov = len(s1 & s2)
                jac = ov / len(s1 | s2)
                exact = (s1 == s2)
                p_hit = 1.0 / math.comb(N_SURAHS, size)
                p_near = hyper_upper_tail(size, ov)
                a1 = derived_source.get(n1) or BASE_CLASS_SOURCE_AXIS.get(n1)
                a2 = derived_source.get(n2) or BASE_CLASS_SOURCE_AXIS.get(n2)
                definitional = False
                if a1 and a2:
                    definitional = (a1 == a2) or (abs(axis_rho(a1, a2)) >= RHO_COUPLE)
                rec = dict(class_a=n1, class_b=n2, size=size, overlap=ov,
                           jaccard=round(jac, 4), exact=exact,
                           p_exact=p_hit, p_overlap=p_near,
                           definitional=definitional)
                cells.append(rec)
                if exact:
                    hits.append(rec)
                elif ov >= size - 2:
                    nearmiss.append(rec)
    return cells, hits, nearmiss


def sweep_E3a(metrics, rev, tuple_name):
    fdefs = collections.OrderedDict()
    fdefs["F1_s"] = [s for s in range(1, 115)]
    fdefs["F2_115_minus_s"] = [115 - s for s in range(1, 115)]
    fdefs["F3_2s"] = [2 * s for s in range(1, 115)]
    fdefs["F4_digit_reverse_s"] = [digit_reverse(s) for s in range(1, 115)]
    fdefs["F5_revelation_order"] = [rev[s] for s in range(1, 115)]
    fdefs["F6_115_minus_rev"] = [115 - rev[s] for s in range(1, 115)]
    fdefs["F7_n_verses"] = list(metrics["M01_n_verses"])
    fdefs["F8_digit_sum_s"] = [digit_sum(s) for s in range(1, 115)]

    TAUTOLOGY = {("M01_n_verses", "F7_n_verses"),
                 ("M12_mushaf_position", "F1_s"),
                 ("M13_revelation_order", "F5_revelation_order")}

    # DECLARED constructional sources (pre-reg §6.2): each target function is
    # built from exactly one metric, and only that metric's cells are
    # constructional.
    FUNC_SOURCE = {"F1_s": "M12_mushaf_position",
                   "F2_115_minus_s": "M12_mushaf_position",
                   "F3_2s": "M12_mushaf_position",
                   "F4_digit_reverse_s": "M12_mushaf_position",
                   "F8_digit_sum_s": "M12_mushaf_position",
                   "F5_revelation_order": "M13_revelation_order",
                   "F6_115_minus_rev": "M13_revelation_order",
                   "F7_n_verses": "M01_n_verses"}

    cells, hits, n_cand = [], [], 0
    for mname, mv in metrics.items():
        mult_m = collections.Counter(mv)
        for fname, fv in fdefs.items():
            if (mname, fname) in TAUTOLOGY:
                continue
            n_cand += N_SURAHS
            scr = mechanical_screen(mv, fv,
                                    constructional=(FUNC_SOURCE.get(fname) == mname))
            local = [s for s in range(N_SURAHS) if mv[s] == fv[s]]
            for s in local:
                hits.append(dict(tuple=tuple_name, geometry="E3a", metric=mname,
                                 func=fname, surah=s + 1, value=mv[s],
                                 coupled=scr["mechanical"],
                                 constructional=scr["constructional"],
                                 ordered=scr["ordered"], rho=scr["rho"],
                                 p_exact=mult_m.get(fv[s], 0) / N_SURAHS))
            tail = hits_tail_exact(mult_m, collections.Counter(fv),
                                   N_SURAHS, len(local))
            if not tail["exact"]:
                raise SystemExit("E3a cell (%s,%s) fell off the exact branch"
                                 % (mname, fname))
            cells.append(dict(tuple=tuple_name, geometry="E3a", metric=mname,
                              func=fname, observed=len(local),
                              expected=tail["expectation"], p_cell=tail["p"],
                              exact=True, coupled=scr["mechanical"],
                              constructional=scr["constructional"],
                              deterministic_order=scr["ordered"], rho=scr["rho"],
                              hit_surahs=[s + 1 for s in local]))
    return cells, hits, n_cand


def sweep_E3b(metrics, tuple_name, rng, n_mc):
    cells, hits, n_cand = [], [], 0
    npairs = N_SURAHS // 2
    for mname, mv in metrics.items():
        n_cand += npairs
        local = [i for i in range(npairs) if mv[i] == mv[N_SURAHS - 1 - i]]
        mult = collections.Counter(mv)
        # EXACT per-hit denominator: P(one designated mirror pair is
        # monochromatic) = sum_w n_w(n_w-1) / (114*113).
        p_pair = sum(nw * (nw - 1) for nw in mult.values()) \
            / float(N_SURAHS * (N_SURAHS - 1))
        pmf = mirror_pmf_exact(mult, n=N_SURAHS, npairs=npairs)
        obs = len(local)
        p = float(sum(pmf[h] for h in range(obs, len(pmf)))) if obs < len(pmf) else 0.0
        exp = float(sum(h * pmf[h] for h in range(len(pmf))))
        med, acc = 0, Fraction(0)
        for h in range(len(pmf)):
            acc += pmf[h]
            if acc >= Fraction(1, 2):
                med = h
                break
        # pre-registered 10^7-draw permutation guard
        arr = np.array(mv)
        ge, done, chunk = 0, 0, 50_000
        while done < n_mc:
            b = min(chunk, n_mc - done)
            perm = rng.permuted(np.tile(arr, (b, 1)), axis=1)
            ge += int(((perm[:, :npairs] == perm[:, N_SURAHS - 1::-1][:, :npairs])
                       .sum(axis=1) >= obs).sum())
            done += b
        for i in local:
            hits.append(dict(tuple=tuple_name, geometry="E3b", metric=mname,
                             pair=[i + 1, N_SURAHS - i], value=mv[i],
                             p_exact=p_pair))
        cells.append(dict(tuple=tuple_name, geometry="E3b", metric=mname,
                          observed=obs, expected=exp, median=med, p_cell=p,
                          p_cell_mc=ge / n_mc, n_mc=n_mc, exact=True,
                          hit_pairs=[[i + 1, N_SURAHS - i] for i in local]))
    return cells, hits, n_cand


def sweep_E3c(metrics, tuple_name, ordered_pairs):
    names = list(metrics.keys())
    cells, hits, n_cand = [], [], 0
    for a in range(len(names)):
        for b in range(a + 1, len(names)):
            na, nb = names[a], names[b]
            va, vb = metrics[na], metrics[nb]
            n_cand += N_SURAHS
            scr = mechanical_screen(va, vb)
            rho = scr["rho"]
            coupled = scr["mechanical"] or (na, nb) in ordered_pairs
            mult_a = collections.Counter(va)
            local = [s for s in range(N_SURAHS) if va[s] == vb[s]]
            for s in local:
                hits.append(dict(tuple=tuple_name, geometry="E3c",
                                 metric_a=na, metric_b=nb, surah=s + 1,
                                 value=va[s], rho=round(rho, 4),
                                 coupled=coupled,
                                 p_exact=mult_a.get(vb[s], 0) / N_SURAHS))
            tail = hits_tail_exact(mult_a, collections.Counter(vb),
                                   N_SURAHS, len(local))
            if not tail["exact"]:
                raise SystemExit("E3c cell (%s,%s) fell off the exact branch"
                                 % (na, nb))
            cells.append(dict(tuple=tuple_name, geometry="E3c", metric_a=na,
                              metric_b=nb, rho=rho, coupled=coupled,
                              constructional=scr["constructional"],
                              deterministic_order=scr["ordered"],
                              observed=len(local),
                              expected=tail["expectation"], p_cell=tail["p"],
                              exact=True,
                              hit_surahs=[s + 1 for s in local]))
    return cells, hits, n_cand


def sweep_E4(qac, vc, tuple_name, rng, n_mc):
    unit_field = 3 if tuple_name == "T-LEMMA" else 2
    count = collections.Counter()
    first_s, last_s = {}, {}
    per_unit_surah = collections.defaultdict(collections.Counter)
    for s, v, root, lem, pos in qac:
        u = lem if unit_field == 3 else root
        if not u:
            continue
        count[u] += 1
        if u not in first_s:
            first_s[u] = s
        first_s[u] = min(first_s[u], s)
        last_s[u] = max(last_s.get(u, 0), s)
        per_unit_surah[u][s] += 1

    units = sorted(count)
    N = len(units)
    cvec = [count[u] for u in units]
    modal = {}
    for u in units:
        c = per_unit_surah[u]
        best = max(c.values())
        modal[u] = min(s for s, k in c.items() if k == best)

    Ls = collections.OrderedDict()
    Ls["L1_first_surah"] = [first_s[u] for u in units]
    Ls["L2_last_surah"] = [last_s[u] for u in units]
    Ls["L3_modal_surah"] = [modal[u] for u in units]
    Ls["L4_modal_surah_nverses"] = [vc[modal[u]] for u in units]
    Ls["L5_115_minus_first"] = [115 - first_s[u] for u in units]

    hist = collections.Counter(cvec)
    n_distinct_surahs = np.array([len(per_unit_surah[u]) for u in units])
    order = np.argsort(n_distinct_surahs, kind="stable")
    blocks = np.array_split(order, 10)

    cvec_np = np.array(cvec)
    cells, hits, n_cand = [], [], 0
    for lname, lv in Ls.items():
        n_cand += N
        lv_np = np.array(lv)
        local = [i for i in range(N) if cvec[i] == lv[i]]
        for i in local:
            hits.append(dict(tuple=tuple_name, geometry="E4", unit=units[i],
                             func=lname, count=cvec[i], target=lv[i],
                             p_exact=hist.get(lv[i], 0) / N))
        # EXACT closed-form expectation under N1 (unrestricted permutation).
        tgt_mult = collections.Counter(lv)
        exp_N1 = float(sum(nw * tgt_mult.get(w, 0)
                           for w, nw in hist.items())) / N
        obs = len(local)
        # The exact rook-polynomial TAIL is mathematically correct but
        # numerically infeasible at N = 1642 / 4832 (board degree ~10^3,
        # catastrophic cancellation in the deficit regime).  Disclosed in the
        # finding's garden-of-forking-paths.  Both nulls therefore use seeded
        # permutation sampling; the per-hit denominators above stay exact.
        ge1 = ge2 = 0
        chunk = max(1, min(max(1, 4_000_000 // max(N, 1)), n_mc))
        done = 0
        while done < n_mc:
            b = min(chunk, n_mc - done)
            base = np.tile(cvec_np, (b, 1))
            p1 = rng.permuted(base, axis=1)
            ge1 += int(((p1 == lv_np).sum(axis=1) >= obs).sum())
            p2 = np.tile(cvec_np, (b, 1))
            for blk in blocks:
                p2[:, blk] = rng.permuted(p2[:, blk], axis=1)
            ge2 += int(((p2 == lv_np).sum(axis=1) >= obs).sum())
            done += b
        # exact N2 expectation (block-wise, closed form)
        exp_N2 = 0.0
        for blk in blocks:
            hb = collections.Counter(cvec_np[blk].tolist())
            tb = collections.Counter(lv_np[blk].tolist())
            exp_N2 += sum(nw * tb.get(w, 0) for w, nw in hb.items()) / len(blk)
        cells.append(dict(tuple=tuple_name, geometry="E4", func=lname,
                          n_units=N, observed=obs,
                          expected_N1=exp_N1, expected_N2=exp_N2,
                          p_cell_N1=ge1 / n_mc, p_cell_N2=ge2 / n_mc,
                          exact_expectation=True, exact_tail=False,
                          n_mc=n_mc))
    return cells, hits, n_cand, N, hist


# ----------------------------------------------------------------------------
# 8. MAIN
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--n-mc", type=int, default=N_MC)
    ap.add_argument("--n-mc-e4", type=int, default=N_MC)
    ap.add_argument("--n-mc-e3b", type=int, default=N_MC)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()

    t0 = time.time()
    verify_locks()
    validate_engines()

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    run_dir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2660",
                           stamp + (("-" + args.tag) if args.tag else ""))
    os.makedirs(run_dir, exist_ok=True)
    print("[run] %s" % run_dir)

    plain, mint, full = load_corpus()
    qac = load_qac()
    vc = load_verse_counts()
    rev, nold, period, nphase = load_revelation_order()

    # ---- MW-6 instrument controls (fail-fast) ------------------------------
    mw6 = {}
    assert len(plain) == N_SURAHS and len(vc) == N_SURAHS
    tot_v = sum(vc.values())
    if tot_v != 6236:
        raise SystemExit("MW-6c FAIL: sum of verse counts = %d, expected 6236" % tot_v)
    mw6["sum_verse_counts"] = tot_v

    root_counts = collections.Counter()
    lemma_counts = collections.Counter()
    for s, v, root, lem, pos in qac:
        if root:
            root_counts[root] += 1
        if lem:
            lemma_counts[lem] += 1
    if len(root_counts) != 1642:
        raise SystemExit("MW-6b FAIL: %d distinct roots, expected 1642"
                         % len(root_counts))
    hist_head = collections.Counter(root_counts.values())
    want_head = {1: 395, 2: 197, 3: 121, 4: 96, 5: 89}
    for k, w in want_head.items():
        if hist_head.get(k) != w:
            raise SystemExit("MW-6b FAIL: root-count histogram h(%d)=%s, expected %d"
                             % (k, hist_head.get(k), w))
    if len(hist_head) != 185:
        raise SystemExit("MW-6b FAIL: %d distinct root counts, expected 185"
                         % len(hist_head))
    mw6["n_roots"] = len(root_counts)
    mw6["n_lemmas"] = len(lemma_counts)
    mw6["n_distinct_root_counts"] = len(hist_head)
    mw6["root_hist_head"] = {str(k): hist_head[k] for k in (1, 2, 3, 4, 5)}

    loci, muq_letters, muq_per_surah, scanned = detect_muqattaat(full)
    if len(loci) != 30 or len(muq_per_surah) != 29 or len(muq_letters) != 14:
        raise SystemExit(
            "MW-6d FAIL: %d loci / %d surahs / %d letters (expected 30/29/14)"
            % (len(loci), len(muq_per_surah), len(muq_letters)))
    mw6["muqattaat_loci"] = len(loci)
    mw6["muqattaat_surahs"] = len(muq_per_surah)
    mw6["muqattaat_letters"] = "".join(muq_letters)
    mw6["muqattaat_tokens_scanned"] = scanned
    print("[MW-6] 6236 verses / 1642 roots / 185 counts / 30 loci in 29 surahs "
          "/ 14 letters  VERIFIED")

    # MW-6e: reproduce H-NEW-2090 cells 1, 2 and 6 exactly, from this pipeline
    vcl = [vc[s] for s in range(1, 115)]
    c2090 = {
        "cell1_vc_eq_N": [s for s in range(1, 115) if vcl[s - 1] == s],
        "cell2_vc_eq_2N": [s for s in range(1, 115) if vcl[s - 1] == 2 * s],
        "cell6_vc_eq_digitrev_N": [s for s in range(1, 115)
                                   if vcl[s - 1] == digit_reverse(s)],
    }
    if (len(c2090["cell1_vc_eq_N"]) != 0
            or c2090["cell2_vc_eq_2N"] != [30]
            or len(c2090["cell6_vc_eq_digitrev_N"]) != 0):
        raise SystemExit("MW-6e FAIL: H-NEW-2090 replication mismatch: %s" % c2090)
    mw6["h_new_2090_replication"] = c2090
    print("[MW-6e] H-NEW-2090 cells 1/2/6 reproduced: 0 hits, 1 hit (Q30), 0 hits")

    # ---- build all three rules-tuples --------------------------------------
    TUPLES = ["T-ROOT", "T-LEMMA", "T-NORM"]
    feats = {}
    for tn in TUPLES:
        feats[tn] = build_surah_features(plain, mint, full, qac, vc, rev, nold, tn)

    COUPLED_AXIS_PAIRS = {
        ("A17_UAS", "A22_max_neighbour_tsp"),
        ("A03_n_letters", "A10_mean_verse_letters"),
        ("A01_n_verses", "A10_mean_verse_letters"),
        ("A02_n_words", "A11_mean_verse_words"),
        ("A01_n_verses", "A11_mean_verse_words"),
        ("A04_n_word_types", "A14_type_token_ratio"),
        ("A02_n_words", "A14_type_token_ratio"),
        ("A19_mean_content_distance", "A21_fr_centroid_dist"),
        ("A20_local_cohesion", "A21_fr_centroid_dist"),
    }
    ORDERED_METRIC_PAIRS = {
        ("M04_n_word_types", "M02_n_words"),
        ("M06_n_distinct_roots", "M05_n_root_tokens"),
        ("M11_modal_rhyme_count", "M01_n_verses"),
    }

    rng = np.random.default_rng(args.seed)
    results = dict(id="H-NEW-2660", prereg_sha256=PREREG_SHA256,
                   seed=args.seed, n_mc=args.n_mc, n_mc_e4=args.n_mc_e4,
                   utc=stamp, mw6=mw6, tuples=TUPLES)

    K_cand = 0
    K_cells = 0
    all_hits = {"E1": [], "E2": [], "E3a": [], "E3b": [], "E3c": [], "E4": []}
    all_cells = {"E1": [], "E2": [], "E3a": [], "E3b": [], "E3c": [], "E4": []}
    e2_nearmiss = []
    per_tuple = {}
    e4_cache = {}
    coupled_mask_by_tuple = {}

    for tn in TUPLES:
        axes, metrics = feats[tn]
        print("[%s] building classes ..." % tn)
        classes, base_names, dsrc = build_classes(
            plain, full, qac, axes, metrics, muq_per_surah, period, nphase)

        print("[%s] E1 rank-extremum sweep ..." % tn)
        c1, h1 = sweep_E1(axes, tn, COUPLED_AXIS_PAIRS)
        K_cand += len(c1); K_cells += 1
        all_cells["E1"].extend(c1); all_hits["E1"].extend(h1)
        coupled_mask_by_tuple[tn] = [c["coupled"] for c in c1]

        print("[%s] E2 exact set-coincidence sweep ..." % tn)
        c2, h2, nm2 = sweep_E2(classes, base_names, dsrc, axes)
        K_cand += len(c2); K_cells += 1
        all_cells["E2"].extend(c2); all_hits["E2"].extend(h2)
        e2_nearmiss.extend([dict(nm, tuple=tn) for nm in nm2])

        print("[%s] E3a self-referential sweep ..." % tn)
        c3a, h3a, n3a = sweep_E3a(metrics, rev, tn)
        K_cand += n3a; K_cells += len(c3a)
        all_cells["E3a"].extend(c3a); all_hits["E3a"].extend(h3a)

        print("[%s] E3b mirror-pair sweep (MC guard = %d) ..." % (tn, args.n_mc_e3b))
        c3b, h3b, n3b = sweep_E3b(metrics, tn, rng, args.n_mc_e3b)
        K_cand += n3b; K_cells += len(c3b)
        all_cells["E3b"].extend(c3b); all_hits["E3b"].extend(h3b)

        print("[%s] E3c cross-metric sweep ..." % tn)
        c3c, h3c, n3c = sweep_E3c(metrics, tn, ORDERED_METRIC_PAIRS)
        K_cand += n3c; K_cells += len(c3c)
        all_cells["E3c"].extend(c3c); all_hits["E3c"].extend(h3c)

        print("[%s] E4 count-location sweep (N2 MC = %d) ..." % (tn, args.n_mc_e4))
        # E4 depends only on the morphological unit, so T-ROOT and T-NORM are
        # identical by construction; computed once, reused, and disclosed.
        cache_key = "LEMMA" if tn == "T-LEMMA" else "ROOT"
        if cache_key in e4_cache:
            c4s, h4s, n4, nunits = e4_cache[cache_key]
            c4 = [dict(c, tuple=tn, reused_from=cache_key) for c in c4s]
            h4 = [dict(h, tuple=tn) for h in h4s]
        else:
            c4, h4, n4, nunits, _ = sweep_E4(qac, vc, tn, rng, args.n_mc_e4)
            e4_cache[cache_key] = (c4, h4, n4, nunits)
        K_cand += n4; K_cells += len(c4)
        all_cells["E4"].extend(c4); all_hits["E4"].extend(h4)

        per_tuple[tn] = dict(
            n_classes=len(classes), n_base_classes=len(base_names),
            n_derived_classes=len(classes) - len(base_names),
            E1_candidates=len(c1), E2_candidates=len(c2),
            E3a_candidates=n3a, E3b_candidates=n3b, E3c_candidates=n3c,
            E4_candidates=n4, E4_units=nunits,
            class_sizes={k: len(v) for k, v in classes.items()
                         if not k.startswith(("TOP", "BOT"))})
        print("   candidates so far K=%d" % K_cand)

    alpha_hit = 0.05 / K_cand
    alpha_cell = 0.05 / K_cells
    results["K_candidates"] = K_cand
    results["K_cells"] = K_cells
    results["alpha_hit"] = alpha_hit
    results["alpha_cell"] = alpha_cell
    print("[bonferroni] K_candidates=%d  alpha_hit=%.4g | K_cells=%d alpha_cell=%.4g"
          % (K_cand, alpha_hit, K_cells, alpha_cell))

    # ---- E1 family null (pre-registered 10^7 draws) ------------------------
    obs_e1 = {tn: sum(1 for c in all_cells["E1"] if c["tuple"] == tn and c["hit"])
              for tn in TUPLES}
    obs_e1_dec = {tn: sum(1 for c in all_cells["E1"]
                          if c["tuple"] == tn and c["hit"] and not c["coupled"])
                  for tn in TUPLES}
    e1_family = {}
    for tn in TUPLES:
        tcells = [c for c in all_cells["E1"] if c["tuple"] == tn]
        exp_analytic = sum(c["p_exact"] for c in tcells)
        exp_dec = sum(c["p_exact"] for c in tcells if not c["coupled"])
        # MW-7-capped descriptive diagnostic: a stricter decoupling stratum,
        # chosen AFTER observation. No p-value, no promotion, no cell added.
        strict = [c for c in tcells if abs(c["rho"]) < 0.40]
        p, p_dec, ncell = sweep_E1_family(
            feats[tn][0], obs_e1[tn], obs_e1_dec[tn],
            coupled_mask_by_tuple[tn], np.random.default_rng(args.seed), args.n_mc)
        e1_family[tn] = dict(
            observed=obs_e1[tn], observed_decoupled=obs_e1_dec[tn],
            expected_exact=exp_analytic, expected_decoupled=exp_dec,
            p_family=p, p_family_decoupled=p_dec,
            n_cells=ncell, n_cells_decoupled=sum(1 for c in tcells
                                                 if not c["coupled"]),
            mw7_strict_rho_lt_040=dict(
                cells=len(strict), observed=sum(1 for c in strict if c["hit"]),
                expected=sum(c["p_exact"] for c in strict),
                note="MW-7 descriptive only; no p-value claimed"),
            n_mc=args.n_mc)
        print("[E1 family %s] obs=%d exp=%.3f p=%.6f | decoupled obs=%d exp=%.3f "
              "p=%.6f | MW-7 rho<0.40 obs=%d exp=%.3f"
              % (tn, obs_e1[tn], exp_analytic, p, obs_e1_dec[tn], exp_dec, p_dec,
                 e1_family[tn]["mw7_strict_rho_lt_040"]["observed"],
                 e1_family[tn]["mw7_strict_rho_lt_040"]["expected"]))
    results["E1_family"] = e1_family

    # ---- DECOY control (MW-6a) ---------------------------------------------
    decoy_hits = sum(1 for c in all_cells["E1"]
                     if c["hit"] and "A23_DECOY" in (c["axis_a"], c["axis_b"]))
    decoy_cells = sum(1 for c in all_cells["E1"]
                      if "A23_DECOY" in (c["axis_a"], c["axis_b"]))
    decoy_exp = decoy_cells / N_SURAHS
    results["decoy"] = dict(hits=decoy_hits, cells=decoy_cells,
                            expected=decoy_exp,
                            ratio=(decoy_hits / decoy_exp) if decoy_exp else None)
    print("[MW-6a decoy] %d hits / %d cells (expected %.2f)"
          % (decoy_hits, decoy_cells, decoy_exp))

    # ---- survivor adjudication ---------------------------------------------
    survivors, mechanical, cbm = [], [], []
    for fam in ("E1", "E2", "E3a", "E3b", "E3c", "E4"):
        for h in all_hits[fam]:
            p = h["p_exact"]
            mech = h.get("coupled") or h.get("definitional") or False
            rec = dict(h, family=fam)
            if mech:
                mechanical.append(rec)
            elif p < alpha_hit:
                survivors.append(rec)
            else:
                cbm.append(rec)

    results["counts"] = dict(
        total_hits=sum(len(v) for v in all_hits.values()),
        by_family={k: len(v) for k, v in all_hits.items()},
        survivors=len(survivors), mechanical=len(mechanical), cbm=len(cbm))
    results["survivors"] = survivors
    results["verdict"] = "HUNT-NULL" if len(survivors) == 0 else "HUNT-POSITIVE"

    # ---- cell-level adjudication -------------------------------------------
    cell_excess, cell_deficit = [], []
    for fam in ("E3a", "E3b", "E3c", "E4"):
        for c in all_cells[fam]:
            pc = c.get("p_cell", c.get("p_cell_N1"))
            exp0 = c.get("expected", c.get("expected_N1"))
            if (pc is not None and pc < alpha_cell and c["observed"] > 0
                    and exp0 is not None and c["observed"] > exp0):
                cell_excess.append(dict(c, family=fam))
            exp = c.get("expected", c.get("expected_N1"))
            if exp is not None and c["observed"] < exp:
                cell_deficit.append(dict(family=fam,
                                         cell={k: c[k] for k in c
                                               if k in ("tuple", "metric", "func",
                                                        "metric_a", "metric_b")},
                                         observed=c["observed"], expected=exp))
    results["cell_excess"] = cell_excess
    results["cell_excess_all_mechanical"] = all(
        c.get("coupled", False) for c in cell_excess)
    results["n_cell_deficit"] = len(cell_deficit)
    results["n_cells_scored"] = sum(len(all_cells[f])
                                    for f in ("E3a", "E3b", "E3c", "E4"))

    # aggregate direction: total observed vs total exactly-expected hits
    direction = {}
    for fam in ("E3a", "E3b", "E3c", "E4"):
        o = e = 0.0
        ob = ab = eq = 0
        o_dec = e_dec = 0.0
        for c in all_cells[fam]:
            ex = c.get("expected", c.get("expected_N2", c.get("expected_N1")))
            o += c["observed"]; e += ex
            if not c.get("coupled", False):
                o_dec += c["observed"]; e_dec += ex
            if c["observed"] < ex:
                ob += 1
            elif c["observed"] > ex:
                ab += 1
            else:
                eq += 1
        direction[fam] = dict(observed_total=o, expected_total=round(e, 3),
                              ratio=round(o / e, 4) if e else None,
                              observed_decoupled=o_dec,
                              expected_decoupled=round(e_dec, 3),
                              ratio_decoupled=round(o_dec / e_dec, 4) if e_dec else None,
                              cells_below=ob, cells_above=ab, cells_equal=eq)
    direction["E1"] = dict(
        observed_total=sum(1 for c in all_cells["E1"] if c["hit"]),
        expected_total=round(sum(c["p_exact"] for c in all_cells["E1"]), 3),
        observed_decoupled=sum(1 for c in all_cells["E1"]
                               if c["hit"] and not c["coupled"]),
        expected_decoupled=round(sum(c["p_exact"] for c in all_cells["E1"]
                                     if not c["coupled"]), 3))
    direction["E2"] = dict(
        observed_total=sum(1 for c in all_cells["E2"] if c["exact"]),
        expected_total=sum(c["p_exact"] for c in all_cells["E2"]),
        observed_nondefinitional=sum(1 for c in all_cells["E2"]
                                     if c["exact"] and not c["definitional"]),
        expected_nondefinitional=sum(c["p_exact"] for c in all_cells["E2"]
                                     if not c["definitional"]),
        pairs_scanned=len(all_cells["E2"]))
    results["direction"] = direction
    for k, v in direction.items():
        print("[direction %-3s] obs=%s exp=%s  decoupled obs=%s exp=%s"
              % (k, v.get("observed_total"), v.get("expected_total"),
                 v.get("observed_decoupled", v.get("observed_nondefinitional")),
                 v.get("expected_decoupled", v.get("expected_nondefinitional"))))

    # ---- write everything ---------------------------------------------------
    results["per_tuple"] = per_tuple
    results["e2_nearmiss_top"] = sorted(
        e2_nearmiss, key=lambda r: (-r["overlap"], r["p_overlap"]))[:60]
    results["walltime_sec"] = round(time.time() - t0, 1)

    with open(os.path.join(run_dir, "h-new-2660.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    for fam in all_cells:
        with open(os.path.join(run_dir, "cells-%s.json" % fam), "w",
                  encoding="utf-8") as f:
            json.dump(all_cells[fam], f, ensure_ascii=False)
        with open(os.path.join(run_dir, "hits-%s.json" % fam), "w",
                  encoding="utf-8") as f:
            json.dump(all_hits[fam], f, ensure_ascii=False)
    with open(os.path.join(run_dir, "mechanical.json"), "w", encoding="utf-8") as f:
        json.dump(mechanical, f, ensure_ascii=False)
    with open(os.path.join(run_dir, "cbm.json"), "w", encoding="utf-8") as f:
        json.dump(cbm, f, ensure_ascii=False)
    with open(os.path.join(run_dir, "e2-nearmiss-full.json"), "w",
              encoding="utf-8") as f:
        json.dump(sorted(e2_nearmiss, key=lambda r: -r["overlap"]),
                  f, ensure_ascii=False)

    if not args.tag:
        with open(jpath("findings/phase-b-hypotheses/csv/h-new-2660.json"),
                  "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=1)

    print("\n=========== H-NEW-2660 ===========")
    print("K_candidates      : %d" % K_cand)
    print("alpha_hit         : %.6g" % alpha_hit)
    print("K_cells           : %d   alpha_cell: %.6g" % (K_cells, alpha_cell))
    print("total exact hits  : %d" % results["counts"]["total_hits"])
    print("  by family       : %s" % results["counts"]["by_family"])
    print("  MECHANICAL      : %d" % len(mechanical))
    print("  CBM             : %d" % len(cbm))
    print("  SURVIVORS       : %d" % len(survivors))
    print("cell-level EXCESS : %d of %d cells" % (len(cell_excess),
                                                  results["n_cells_scored"]))
    print("cell-level DEFICIT: %d" % len(cell_deficit))
    print("VERDICT           : %s" % results["verdict"])
    print("walltime          : %.1fs" % results["walltime_sec"])
    print("run dir           : %s" % run_dir)


if __name__ == "__main__":
    main()
