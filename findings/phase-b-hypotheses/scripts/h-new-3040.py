#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-NEW-3040 — The modality axis (deontic vs epistemic/alethic) and its
orthogonality to the cross-finding-028 function-word axis.

Pre-registration : findings/phase-b-hypotheses/prereg-h-new-3040-modality-axis.md
Frontier id      : F-10

VERDICT FUNCTION <-> PRE-REGISTRATION §7 CORRESPONDENCE
(diff this block against the pre-registration's §7 line by line before running)

  prereg §7.1  H1 statistic ....... Delta = mean(M_resid|LEGAL) - mean(M_resid|ESCHAT),
                                    M_resid = M rank-residualised on log surah word count
               H1 null ............ unstratified permutation of the LEGAL/ESCHAT labels
                                    among the 45 labelled surahs, 10000 draws, seed 20260509
               H1 p ............... one-sided, (#{Delta_perm >= Delta_obs} + 1)/(n_perm + 1)
               H1 secondary ....... raw M with quintile-stratified, decile-stratified and
                                    unstratified nulls; all reported
               H1 degeneracy ...... distinct label vectors drawn per stratified null;
                                    < 100 distinct  ->  DEGENERATE, excluded from any verdict
  prereg §5    H1 direction ....... LOCKED Delta > 0.  Delta <= 0 -> PRE-COMMIT VIOLATION
  prereg §7.3  H1 alpha ........... primary family k = 2, alpha_bon = 0.025
               =>  H1 verdict:  Delta <= 0                       -> "PRE-COMMIT VIOLATION"
                                Delta  > 0 and p_primary < 0.025 -> "PASS"
                                Delta  > 0 and p_primary >= 0.025-> "NULL"

  prereg §7.2  H2 statistic ....... rho = Spearman(M, R_B) over all 114 surahs (Arm B)
               H2 interval ........ 10000-resample percentile bootstrap 95% CI, seed 20260509
               H2 bounds .......... delta = 0.25 PRIMARY; 0.20 and 0.30 also reported
               H2 three-way rule .. ORTHOGONAL      iff CI_low >= -delta and CI_high <= +delta
                                    NOT-ORTHOGONAL  iff CI_low  >  +delta or CI_high < -delta
                                    INDETERMINATE   otherwise
               H2 companion ....... two-sided permutation p for rho != 0, 10000, seed 20260509
                                    (this is the k=2 member; alpha_bon = 0.025)
               H2 length control .. partial Spearman rho(M, R | c) for all four channels,
                                    each with its own bootstrap CI and three-way verdict
  prereg §7.4  conditional form ... rho(M, R_B | register), separately named, separately
                                    reported, never substituted for the marginal
  prereg §3.5  arms ............... ARM B (5 features, f_iltifat_type dropped) carries the
                                    orthogonality verdict; ARM A (6 features) reported in full
                                    and may NOT establish an orthogonality verdict
  prereg §7.3  secondary family ... six per-feature rho(M, f_j), k = 6, alpha = 0.008333
  prereg §8    rules-tuples ....... RT-1 primary; RT-2..RT-5 robustness, uncorrected,
                                    may not establish or overturn a verdict
  prereg §6.2  ordering ........... the length-channel block is computed and written to the
                                    results object BEFORE any primary statistic

Rules-tuple RT-1: (no-tashkeel, QAC-v0.4 TAG-field + FEATURES-field, per-surah, trigger
window W=5, E includes l:EMPH prefix and excludes n:EMPH suffix, register = Neuwirth-Sinai
sinai_genre mechanical mapping, M = smoothed log-ratio, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)

Author: Waiel Al-Shujaa   Date: 2026-08-09
"""

import os
import re
import csv
import json
import math
import random
import hashlib
import collections
import datetime

# --------------------------------------------------------------------------
# 0. Paths and the pre-registration lock
# --------------------------------------------------------------------------
ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-3040-modality-axis.md")
EXPECTED_PREREG_SHA = "48e02a04a252e91dac41cd747968e769c6a28379a1cbd85582bf2a2161e353df"

QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
J2530 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2530.json")
J2390 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2390.json")
J2500 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2500.json")
GENRE_TSV = os.path.join(ROOT, "findings/classical-sources/neuwirth-sinai-genre-labels.tsv")

SEED = 20260509
N_PERM = 10000
N_BOOT = 10000
ALPHA_BON_PRIMARY = 0.025          # prereg §7.3, k = 2
ALPHA_SECONDARY = 0.05 / 6.0       # prereg §7.3, k = 6
DELTAS = [0.20, 0.25, 0.30]
DELTA_PRIMARY = 0.25
W_PRIMARY = 5
W_RT4 = 40

CF028_FEATS_A = ["f_idh", "f_lamma", "f_qalu", "f_idha_cascade", "f_doubling", "f_iltifat_type"]
CF028_FEATS_B = ["f_idh", "f_lamma", "f_qalu", "f_idha_cascade", "f_doubling"]


def verify_prereg():
    with open(PREREG, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != EXPECTED_PREREG_SHA:
        raise SystemExit(
            "PREREG SHA MISMATCH\n  expected %s\n  got      %s\n"
            "The pre-registration has been modified. Refusing to run."
            % (EXPECTED_PREREG_SHA, got))
    print("[prereg] SHA-256 verified: %s" % got)
    return got


# --------------------------------------------------------------------------
# 1. Statistics helpers (stdlib only, per INVESTIGATION-PROTOCOL §7.1)
# --------------------------------------------------------------------------
def ranks(a):
    idx = sorted(range(len(a)), key=lambda i: a[i])
    r = [0.0] * len(a)
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[idx[j + 1]] == a[idx[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            r[idx[k]] = avg
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    if n < 3:
        return 0.0
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    dx = sum((x[i] - mx) ** 2 for i in range(n))
    dy = sum((y[i] - my) ** 2 for i in range(n))
    den = math.sqrt(dx * dy)
    return num / den if den > 0 else 0.0


def spearman(x, y):
    return pearson(ranks(x), ranks(y))


def ols_residuals(y, X):
    """Residuals of y on design X (list of column lists) plus intercept.
    Normal equations with Gaussian elimination; stdlib only."""
    n = len(y)
    cols = [[1.0] * n] + [list(c) for c in X]
    p = len(cols)
    A = [[sum(cols[i][k] * cols[j][k] for k in range(n)) for j in range(p)] for i in range(p)]
    b = [sum(cols[i][k] * y[k] for k in range(n)) for i in range(p)]
    for i in range(p):                       # Gaussian elimination w/ partial pivot
        piv = max(range(i, p), key=lambda r: abs(A[r][i]))
        if abs(A[piv][i]) < 1e-12:
            continue
        A[i], A[piv] = A[piv], A[i]
        b[i], b[piv] = b[piv], b[i]
        for r in range(p):
            if r == i:
                continue
            f = A[r][i] / A[i][i]
            if f == 0.0:
                continue
            for c in range(i, p):
                A[r][c] -= f * A[i][c]
            b[r] -= f * b[i]
    beta = [b[i] / A[i][i] if abs(A[i][i]) > 1e-12 else 0.0 for i in range(p)]
    fit = [sum(beta[i] * cols[i][k] for i in range(p)) for k in range(n)]
    return [y[k] - fit[k] for k in range(n)], beta


def rank_residualise(x, controls):
    """Residual of rank(x) on rank(each control). Controls already numeric columns."""
    return ols_residuals(ranks(x), [ranks(c) for c in controls])[0]


def partial_spearman(x, y, controls):
    rx = rank_residualise(x, controls)
    ry = rank_residualise(y, controls)
    return pearson(rx, ry)


def jacobi_eigen(Amat, iters=200):
    """Symmetric eigendecomposition by cyclic Jacobi. Returns (eigvals, eigvecs-as-columns)."""
    n = len(Amat)
    A = [row[:] for row in Amat]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(iters):
        off = math.sqrt(sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < 1e-12:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-15:
                    continue
                theta = (A[q][q] - A[p][p]) / (2.0 * A[p][q])
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p] = c * akp - s * akq
                    A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k] = c * apk - s * aqk
                    A[q][k] = s * apk + c * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p] = c * vkp - s * vkq
                    V[k][q] = s * vkp + c * vkq
    vals = [A[i][i] for i in range(n)]
    return vals, V


def pc1(matrix, feat_names, sign_anchor):
    """First principal component score per row of `matrix` (rows = surahs).
    Columns z-scored; sign fixed so the loading on `sign_anchor` is positive."""
    n = len(matrix)
    p = len(matrix[0])
    Z = []
    stats = []
    for j in range(p):
        col = [matrix[i][j] for i in range(n)]
        m = sum(col) / n
        sd = math.sqrt(sum((v - m) ** 2 for v in col) / (n - 1)) or 1.0
        stats.append((m, sd))
    for i in range(n):
        Z.append([(matrix[i][j] - stats[j][0]) / stats[j][1] for j in range(p)])
    C = [[sum(Z[k][i] * Z[k][j] for k in range(n)) / (n - 1) for j in range(p)] for i in range(p)]
    vals, V = jacobi_eigen(C)
    top = max(range(p), key=lambda j: vals[j])
    load = [V[i][top] for i in range(p)]
    a = feat_names.index(sign_anchor)
    if load[a] < 0:
        load = [-v for v in load]
    scores = [sum(Z[i][j] * load[j] for j in range(p)) for i in range(n)]
    ev = sum(vals)
    return scores, load, (vals[top] / ev if ev > 0 else 0.0)


def multiple_r(y, X):
    """Multiple correlation of y on columns X (z-scored inside), plus LOOCV R^2."""
    n = len(y)
    res, _ = ols_residuals(y, X)
    my = sum(y) / n
    sst = sum((v - my) ** 2 for v in y)
    sse = sum(r * r for r in res)
    r2 = 1.0 - sse / sst if sst > 0 else 0.0
    loo_sse = 0.0
    for i in range(n):
        yy = y[:i] + y[i + 1:]
        XX = [c[:i] + c[i + 1:] for c in X]
        _, beta = ols_residuals(yy, XX)
        pred = beta[0] + sum(beta[j + 1] * X[j][i] for j in range(len(X)))
        loo_sse += (y[i] - pred) ** 2
    loo_r2 = 1.0 - loo_sse / sst if sst > 0 else 0.0
    return math.sqrt(max(0.0, r2)), r2, loo_r2


def percentile(sorted_vals, q):
    if not sorted_vals:
        return float("nan")
    k = (len(sorted_vals) - 1) * q
    lo = int(math.floor(k))
    hi = int(math.ceil(k))
    if lo == hi:
        return sorted_vals[lo]
    return sorted_vals[lo] * (hi - k) + sorted_vals[hi] * (k - lo)


def bootstrap_ci(x, y, controls, seed, n_boot=N_BOOT):
    """Percentile bootstrap 95% CI for (partial) Spearman, resampling units."""
    rng = random.Random(seed)
    n = len(x)
    out = []
    for _ in range(n_boot):
        idx = [rng.randrange(n) for _ in range(n)]
        bx = [x[i] for i in idx]
        by = [y[i] for i in idx]
        if len(set(bx)) < 3 or len(set(by)) < 3:
            continue
        if controls:
            bc = [[c[i] for i in idx] for c in controls]
            try:
                out.append(partial_spearman(bx, by, bc))
            except Exception:
                continue
        else:
            out.append(spearman(bx, by))
    out.sort()
    return percentile(out, 0.025), percentile(out, 0.975), len(out)


def fisher_ci(rho, n):
    if abs(rho) >= 1.0:
        return (rho, rho)
    z = math.atanh(rho)
    se = 1.06 / math.sqrt(n - 3)
    return (math.tanh(z - 1.96 * se), math.tanh(z + 1.96 * se))


def equivalence_verdict(ci_lo, ci_hi, delta):
    """prereg §7.2 three-way decision rule, verbatim."""
    if ci_lo >= -delta and ci_hi <= delta:
        return "ORTHOGONAL"
    if ci_lo > delta or ci_hi < -delta:
        return "NOT-ORTHOGONAL"
    return "INDETERMINATE"


def perm_p_two_sided(x, y, seed, n_perm=N_PERM):
    rng = random.Random(seed)
    obs = spearman(x, y)
    y2 = list(y)
    ge = 0
    for _ in range(n_perm):
        rng.shuffle(y2)
        if abs(spearman(x, y2)) >= abs(obs) - 1e-15:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)


# --------------------------------------------------------------------------
# 2. Corpus load and the modality instrument (prereg §4)
# --------------------------------------------------------------------------
LOCRE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
NEG_LAM = {"lamo", "l~amo"}
NEG_LAN = {"lan", "l~an"}
TRIGGER_PRIORITY = ["prohibition_la", "negation_lam", "negation_lan",
                    "conditional", "sub_an_kay", "purpose"]


def lem_exact(feats, lem):
    return re.search(r"LEM:" + re.escape(lem) + r"(\||$)", feats) is not None


def load_qac():
    word_segs = collections.defaultdict(list)
    verse_words = collections.defaultdict(set)
    nseg = 0
    for line in open(QAC, encoding="utf-8"):
        if not line.startswith("("):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        s, v, w, g = map(int, LOCRE.match(p[0]).groups())
        word_segs[(s, v, w)].append((g, p[1], p[2], p[3]))
        verse_words[(s, v)].add(w)
        nseg += 1
    return word_segs, verse_words, nseg


def trigger_of(word_segs, s, v, w, mood, window):
    """prereg §4.2, verbatim."""
    if mood == "JUS" and any("l:IMPV" in f for (_, _, _, f) in word_segs[(s, v, w)]):
        return "command_lam_amr"
    for d in range(1, window + 1):
        ww = w - d
        if ww < 1:
            break
        found = set()
        for (_, form, tag, f) in word_segs.get((s, v, ww), []):
            if tag == "PRO":
                found.add("prohibition_la")
            elif tag == "NEG" and form in NEG_LAM:
                found.add("negation_lam")
            elif tag == "NEG" and form in NEG_LAN:
                found.add("negation_lan")
            elif tag == "COND":
                found.add("conditional")
            elif tag == "SUB":
                found.add("sub_an_kay")
            elif tag == "P" and (lem_exact(f, "kay") or lem_exact(f, "Hat~aY")):
                found.add("purpose")
        if found:
            for pr in TRIGGER_PRIORITY:
                if pr in found:
                    return pr
    for (_, _, _, f) in word_segs[(s, v, w)]:
        if "PREFIX" in f and ("l:PRP" in f or "l:P" in f):
            return "purpose"
    return "unassigned"


def build_modality(word_segs, window, include_emph_prefix):
    """prereg §4.4. Returns per-surah D, E and the trigger census."""
    D = collections.Counter()
    E = collections.Counter()
    census = collections.Counter()
    census_subj = collections.Counter()
    tag_totals = collections.Counter()
    for (s, v, w), sl in word_segs.items():
        is_jus = any("MOOD:JUS" in f for (_, _, _, f) in sl)
        is_subj = any("MOOD:SUBJ" in f for (_, _, _, f) in sl)
        if is_jus:
            tg = trigger_of(word_segs, s, v, w, "JUS", window)
            census[tg] += 1
            if tg in ("prohibition_la", "command_lam_amr"):
                D[s] += 1
        if is_subj:
            tg = trigger_of(word_segs, s, v, w, "SUBJ", window)
            census_subj[tg] += 1
            if tg == "negation_lan":
                E[s] += 1
        for (_, _, tag, f) in sl:
            if tag == "CERT":
                E[s] += 1
                tag_totals["CERT"] += 1
            elif tag == "FUT":
                E[s] += 1
                tag_totals["FUT"] += 1
            elif tag == "EMPH" and "l:EMPH" in f:
                tag_totals["EMPH_pref"] += 1
                if include_emph_prefix:
                    E[s] += 1
            elif tag == "EMPH" and "n:EMPH" in f:
                tag_totals["EMPH_suf"] += 1
            elif tag == "PRO":
                tag_totals["PRO"] += 1
    return D, E, census, census_subj, tag_totals


def contrast_log(D, E, s):
    return math.log((D[s] + 0.5) / (E[s] + 0.5))


def contrast_bounded(D, E, s):
    return (D[s] - E[s]) / (D[s] + E[s] + 1.0)


# --------------------------------------------------------------------------
# 3. Register labels (prereg §4.6)
# --------------------------------------------------------------------------
def load_labels_neuwirth():
    leg, esc = set(), set()
    with open(GENRE_TSV, encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if not row or not row[0].isdigit():
                continue
            g = row[4].lower()
            if "legal" in g:
                leg.add(int(row[0]))
            if "eschatolog" in g:
                esc.add(int(row[0]))
    return leg, esc


def load_labels_cf028():
    gp = json.load(open(J2500))["genre_proxy"]["surah_genre"]
    leg = {int(k) for k, v in gp.items() if v == "legal_medinan"}
    esc = {int(k) for k, v in gp.items() if v == "eschatological_mufassal"}
    return leg, esc


# --------------------------------------------------------------------------
# 4. H1 (prereg §7.1)
# --------------------------------------------------------------------------
def h1_test(Mvals, S, leg, esc, control_col, seed, mode, n_strata=None):
    """mode: 'residualised' (primary) or 'raw'. n_strata: None = unstratified."""
    labelled = [s for s in S if s in leg or s in esc]
    idx = {s: i for i, s in enumerate(S)}
    if mode == "residualised":
        vals = rank_residualise(Mvals, [control_col])
    else:
        vals = list(Mvals)
    y = [vals[idx[s]] for s in labelled]
    lab = [1 if s in leg else 0 for s in labelled]
    n1 = sum(lab)
    n0 = len(lab) - n1

    def delta(l):
        a = sum(y[i] for i in range(len(y)) if l[i] == 1) / max(1, sum(l))
        b = sum(y[i] for i in range(len(y)) if l[i] == 0) / max(1, len(l) - sum(l))
        return a - b

    obs = delta(lab)
    obs_tuple = tuple(lab)
    n_same = 0
    rng = random.Random(seed)
    if n_strata is None:
        pool = list(lab)
        ge = 0
        seen = set()
        for _ in range(N_PERM):
            rng.shuffle(pool)
            if delta(pool) >= obs - 1e-15:
                ge += 1
            seen.add(tuple(pool))
            if tuple(pool) == obs_tuple:
                n_same += 1
    else:
        ctrl = [control_col[idx[s]] for s in labelled]
        order = sorted(range(len(labelled)), key=lambda i: ctrl[i])
        strata = collections.defaultdict(list)
        for rank_i, i in enumerate(order):
            strata[min(n_strata - 1, rank_i * n_strata // len(order))].append(i)
        ge = 0
        seen = set()
        for _ in range(N_PERM):
            perm = [None] * len(lab)
            for _b, members in strata.items():
                vals_b = [lab[i] for i in members]
                rng.shuffle(vals_b)
                for i, vv in zip(members, vals_b):
                    perm[i] = vv
            if delta(perm) >= obs - 1e-15:
                ge += 1
            seen.add(tuple(perm))
            if tuple(perm) == obs_tuple:
                n_same += 1
    p = (ge + 1) / (N_PERM + 1)
    return {
        "mode": mode, "n_strata": n_strata, "n_legal": n1, "n_eschat": n0,
        "delta_obs": round(obs, 6), "p_one_sided": round(p, 6),
        "n_distinct_permutations": len(seen),
        # prereg §7.1 degeneracy check: "the number of distinct label vectors drawn in
        # 10,000 attempts AND the fraction differing from the observed"
        "frac_differing_from_observed": round(1.0 - n_same / N_PERM, 6),
        "degenerate": (n_strata is not None and len(seen) < 100),
    }


# --------------------------------------------------------------------------
# 5. Main
# --------------------------------------------------------------------------
def main():
    sha = verify_prereg()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3040", stamp)
    os.makedirs(rundir, exist_ok=False)
    print("[run] %s" % rundir)

    word_segs, verse_words, nseg = load_qac()
    S = list(range(1, 115))
    wordcount = collections.Counter()
    versecount = collections.Counter()
    for (s, v, w) in word_segs:
        wordcount[s] += 1
    for (s, v) in verse_words:
        versecount[s] += 1

    j2530 = json.load(open(J2530))
    RAW = {int(k): v for k, v in j2530["raw_feature_vectors"].items()}

    # ---- §2.1 count verification, reproduced in-run --------------------
    counts = collections.Counter()
    for sl in word_segs.values():
        for (_, form, tag, f) in sl:
            if "MOOD:JUS" in f:
                counts["MOOD:JUS"] += 1
            if "MOOD:SUBJ" in f:
                counts["MOOD:SUBJ"] += 1
            if tag in ("PRO", "CERT", "FUT", "EMPH"):
                counts[tag] += 1
    print("[verify] segments=%d words=%d verses=%d" % (nseg, len(word_segs), len(verse_words)))
    print("[verify] " + "  ".join("%s=%d" % (k, counts[k]) for k in
                                  ["MOOD:JUS", "MOOD:SUBJ", "PRO", "CERT", "FUT", "EMPH"]))

    # ---- build the instrument, RT-1 -----------------------------------
    D, E, cens_jus, cens_subj, tag_tot = build_modality(word_segs, W_PRIMARY, True)
    M = [contrast_log(D, E, s) for s in S]

    # ---- cross-finding-028 axes ---------------------------------------
    matA = [[RAW[s][f] for f in CF028_FEATS_A] for s in S]
    matB = [[RAW[s][f] for f in CF028_FEATS_B] for s in S]
    R_A, loadA, evrA = pc1(matA, CF028_FEATS_A, "f_qalu")
    R_B, loadB, evrB = pc1(matB, CF028_FEATS_B, "f_qalu")

    # ---- §6.2 : LENGTH CHANNELS FIRST, BEFORE ANY PRIMARY STATISTIC ----
    channels = collections.OrderedDict([
        ("log_word_count", [math.log(wordcount[s]) for s in S]),
        ("verse_count", [float(versecount[s]) for s in S]),
        ("mean_verse_length", [wordcount[s] / versecount[s] for s in S]),
        ("mushaf_position", [float(s) for s in S]),
    ])
    series = collections.OrderedDict()
    for f in CF028_FEATS_A:
        series[f] = [RAW[s][f] for s in S]
    series["D_deontic_count"] = [float(D[s]) for s in S]
    series["E_epistemic_count"] = [float(E[s]) for s in S]
    series["M_modality_contrast"] = M
    series["R_A_pc1_6feature"] = R_A
    series["R_B_pc1_5feature"] = R_B

    length_block = collections.OrderedDict()
    print("\n=== LENGTH-CHANNEL CORRELATIONS (prereg §6.2; before any primary test) ===")
    print("  %-24s %10s %10s %10s %10s" % ("series", "logWC", "verseN", "meanVL", "mushaf"))
    for name, vals in series.items():
        row = collections.OrderedDict((cn, round(spearman(cv, vals), 6))
                                      for cn, cv in channels.items())
        length_block[name] = row
        print("  %-24s %10.4f %10.4f %10.4f %10.4f"
              % (name, row["log_word_count"], row["verse_count"],
                 row["mean_verse_length"], row["mushaf_position"]))
    chan_x_chan = collections.OrderedDict()
    for a, av in channels.items():
        chan_x_chan[a] = collections.OrderedDict((b, round(spearman(av, bv), 6))
                                                 for b, bv in channels.items())

    results = collections.OrderedDict()
    results["id"] = "H-NEW-3040"
    results["title"] = ("The modality axis (deontic vs epistemic/alethic) and its "
                        "orthogonality to the cross-finding-028 function-word axis")
    results["frontier_id"] = "F-10"
    results["prereg_sha256"] = sha
    results["run_utc"] = stamp
    results["seed"] = SEED
    results["n_perm"] = N_PERM
    results["n_boot"] = N_BOOT
    results["bonferroni_k_primary"] = 2
    results["alpha_bonferroni_primary"] = ALPHA_BON_PRIMARY
    results["delta_primary"] = DELTA_PRIMARY
    results["rules_tuple_primary"] = (
        "(no-tashkeel, QAC-v0.4 TAG-field + FEATURES-field, per-surah, trigger window W=5, "
        "E includes l:EMPH prefix and excludes n:EMPH suffix, register = Neuwirth-Sinai "
        "sinai_genre mechanical mapping, M = smoothed log-ratio, basmala-counted-only-in-Q1, "
        "Hafs-Kufan, Mashriqi)")
    results["corpus_verification"] = {
        "segments": nseg, "words": len(word_segs), "verses": len(verse_words),
        "tag_counts": dict(counts),
    }
    # prereg §6.2: this block's POSITION in the output file is part of the lock
    results["length_channels_measured_first"] = length_block
    results["channel_x_channel"] = chan_x_chan

    # ---- instrument census --------------------------------------------
    results["instrument"] = {
        "jussive_trigger_census_W5": dict(cens_jus),
        "subjunctive_trigger_census_W5": dict(cens_subj),
        "particle_tag_totals": dict(tag_tot),
        "D_total": sum(D.values()), "E_total": sum(E.values()),
        "n_surahs_D_plus_E_zero": sum(1 for s in S if D[s] + E[s] == 0),
        "surahs_D_plus_E_zero": [s for s in S if D[s] + E[s] == 0],
        "pc1_loadings_armA": dict(zip(CF028_FEATS_A, [round(v, 6) for v in loadA])),
        "pc1_loadings_armB": dict(zip(CF028_FEATS_B, [round(v, 6) for v in loadB])),
        "pc1_var_explained_armA": round(evrA, 6),
        "pc1_var_explained_armB": round(evrB, 6),
    }
    print("\n=== INSTRUMENT ===")
    print("  jussive triggers (W=5): %s" % dict(cens_jus))
    print("  D_total=%d  E_total=%d  D+E==0 on %d surahs"
          % (sum(D.values()), sum(E.values()), sum(1 for s in S if D[s] + E[s] == 0)))
    print("  PC1 Arm A loadings: %s  (var expl %.3f)"
          % ({k: round(v, 3) for k, v in zip(CF028_FEATS_A, loadA)}, evrA))
    print("  PC1 Arm B loadings: %s  (var expl %.3f)"
          % ({k: round(v, 3) for k, v in zip(CF028_FEATS_B, loadB)}, evrB))

    # ---- H1 (prereg §7.1) ---------------------------------------------
    leg, esc = load_labels_neuwirth()
    lwc = channels["log_word_count"]
    h1 = collections.OrderedDict()
    h1["primary_residualised_unstratified"] = h1_test(M, S, leg, esc, lwc, SEED, "residualised", None)
    h1["secondary_raw_quintile"] = h1_test(M, S, leg, esc, lwc, SEED, "raw", 5)
    h1["secondary_raw_decile"] = h1_test(M, S, leg, esc, lwc, SEED, "raw", 10)
    h1["secondary_raw_unstratified"] = h1_test(M, S, leg, esc, lwc, SEED, "raw", None)
    prim = h1["primary_residualised_unstratified"]
    if prim["delta_obs"] <= 0:
        h1_verdict = "PRE-COMMIT VIOLATION"
    elif prim["p_one_sided"] < ALPHA_BON_PRIMARY:
        h1_verdict = "PASS"
    else:
        h1_verdict = "NULL"
    h1["verdict"] = h1_verdict
    h1["direction_locked"] = "Delta = mean(M|LEGAL) - mean(M|ESCHAT) > 0"
    h1["legal_surahs"] = sorted(leg)
    h1["eschat_surahs"] = sorted(esc)
    h1["group_means_raw_M"] = {
        "legal": round(sum(M[s - 1] for s in sorted(leg)) / len(leg), 6),
        "eschat": round(sum(M[s - 1] for s in sorted(esc)) / len(esc), 6),
    }
    results["H1_separation"] = h1
    print("\n=== H1 (prereg §7.1) ===")
    for k, v in h1.items():
        if isinstance(v, dict) and "delta_obs" in v:
            print("  %-38s delta=%+.5f  p=%.5f  distinct_perms=%d%s"
                  % (k, v["delta_obs"], v["p_one_sided"], v["n_distinct_permutations"],
                     "  DEGENERATE" if v["degenerate"] else ""))
    print("  raw-M group means: legal=%.4f  eschat=%.4f"
          % (h1["group_means_raw_M"]["legal"], h1["group_means_raw_M"]["eschat"]))
    print("  H1 VERDICT: %s" % h1_verdict)

    # ---- H2 (prereg §7.2) ---------------------------------------------
    def h2_block(Rvals, arm_name):
        blk = collections.OrderedDict()
        rho = spearman(M, Rvals)
        lo, hi, nb = bootstrap_ci(M, Rvals, None, SEED)
        flo, fhi = fisher_ci(rho, len(S))
        _, pperm = perm_p_two_sided(M, Rvals, SEED)
        blk["rho_marginal"] = round(rho, 6)
        blk["boot_ci95"] = [round(lo, 6), round(hi, 6)]
        blk["boot_n_effective"] = nb
        blk["fisher_ci95_crosscheck"] = [round(flo, 6), round(fhi, 6)]
        blk["perm_p_two_sided"] = round(pperm, 6)
        blk["perm_p_below_alpha_bon"] = bool(pperm < ALPHA_BON_PRIMARY)
        blk["equivalence"] = collections.OrderedDict(
            (("delta_%.2f" % d), equivalence_verdict(lo, hi, d)) for d in DELTAS)
        blk["verdict_primary_delta"] = equivalence_verdict(lo, hi, DELTA_PRIMARY)
        # length controls
        part = collections.OrderedDict()
        for cn, cv in channels.items():
            pr = partial_spearman(M, Rvals, [cv])
            plo, phi, pn = bootstrap_ci(M, Rvals, [cv], SEED)
            part[cn] = collections.OrderedDict([
                ("partial_rho", round(pr, 6)),
                ("boot_ci95", [round(plo, 6), round(phi, 6)]),
                ("boot_n_effective", pn),
                ("equivalence", collections.OrderedDict(
                    (("delta_%.2f" % d), equivalence_verdict(plo, phi, d)) for d in DELTAS)),
            ])
        blk["length_partialled"] = part
        return blk

    h2 = collections.OrderedDict()
    h2["ARM_B_5feature_VERDICT_BEARING"] = h2_block(R_B, "B")
    h2["ARM_A_6feature_fidelity_only"] = h2_block(R_A, "A")
    h2["arm_note"] = ("prereg §3.5: ARM B carries the orthogonality verdict; ARM A is the axis "
                      "cross-finding-028 actually uses and is reported in full, but may NOT "
                      "establish an orthogonality verdict because f_iltifat_type is a 2<->3 vs "
                      "3<->1 person contrast and the deontic pole is 91.9% 2nd-person "
                      "(prohibition) / 98.7% 3rd-person (lam al-amr).")

    # §7.4 conditional-on-register form
    reg_d1 = [1.0 if s in leg else 0.0 for s in S]
    reg_d2 = [1.0 if s in esc else 0.0 for s in S]
    cond = collections.OrderedDict()
    for arm_name, Rvals in (("ARM_B", R_B), ("ARM_A", R_A)):
        pr = partial_spearman(M, Rvals, [reg_d1, reg_d2])
        plo, phi, pn = bootstrap_ci(M, Rvals, [reg_d1, reg_d2], SEED)
        cond[arm_name] = collections.OrderedDict([
            ("partial_rho_given_register", round(pr, 6)),
            ("boot_ci95", [round(plo, 6), round(phi, 6)]),
            ("boot_n_effective", pn),
            ("equivalence", collections.OrderedDict(
                (("delta_%.2f" % d), equivalence_verdict(plo, phi, d)) for d in DELTAS)),
        ])
    cond["interpretation_locked"] = ("prereg §7.4: marginal orthogonality asks whether the two "
                                     "axes are unrelated; conditional orthogonality asks whether "
                                     "they carry unrelated information once register is known. "
                                     "A pass on one may not be reported as a pass on the other.")
    h2["conditional_on_register"] = cond

    # secondary family: per-feature rho, k=6
    perfeat = collections.OrderedDict()
    for f in CF028_FEATS_A:
        vals = [RAW[s][f] for s in S]
        r, pp = perm_p_two_sided(M, vals, SEED)
        lo, hi, nb = bootstrap_ci(M, vals, None, SEED)
        perfeat[f] = collections.OrderedDict([
            ("rho", round(r, 6)), ("perm_p_two_sided", round(pp, 6)),
            ("below_alpha_secondary", bool(pp < ALPHA_SECONDARY)),
            ("boot_ci95", [round(lo, 6), round(hi, 6)]),
        ])
    h2["per_feature_secondary_family_k6"] = perfeat
    h2["alpha_secondary"] = round(ALPHA_SECONDARY, 6)
    h2["max_abs_rho_over_features"] = round(max(abs(v["rho"]) for v in perfeat.values()), 6)

    # multiple correlation
    mrA = multiple_r(M, [[RAW[s][f] for s in S] for f in CF028_FEATS_A])
    mrB = multiple_r(M, [[RAW[s][f] for s in S] for f in CF028_FEATS_B])
    h2["multiple_correlation"] = {
        "arm_A_R": round(mrA[0], 6), "arm_A_R2": round(mrA[1], 6), "arm_A_loocv_R2": round(mrA[2], 6),
        "arm_B_R": round(mrB[0], 6), "arm_B_R2": round(mrB[1], 6), "arm_B_loocv_R2": round(mrB[2], 6),
    }
    results["H2_orthogonality"] = h2

    print("\n=== H2 (prereg §7.2) — ARM B is verdict-bearing ===")
    for arm in ["ARM_B_5feature_VERDICT_BEARING", "ARM_A_6feature_fidelity_only"]:
        b = h2[arm]
        print("  %s" % arm)
        print("    rho = %+.5f   boot 95%% CI [%+.5f, %+.5f]   Fisher CI [%+.5f, %+.5f]"
              % (b["rho_marginal"], b["boot_ci95"][0], b["boot_ci95"][1],
                 b["fisher_ci95_crosscheck"][0], b["fisher_ci95_crosscheck"][1]))
        print("    perm p (two-sided) = %.5f   (alpha_bon = %.3f)"
              % (b["perm_p_two_sided"], ALPHA_BON_PRIMARY))
        print("    equivalence: %s" % dict(b["equivalence"]))
        for cn, cv in b["length_partialled"].items():
            print("      | %-18s partial rho=%+.5f  CI [%+.5f, %+.5f]  d=0.25 -> %s"
                  % (cn, cv["partial_rho"], cv["boot_ci95"][0], cv["boot_ci95"][1],
                     cv["equivalence"]["delta_0.25"]))
    print("  conditional on register:")
    for arm in ("ARM_B", "ARM_A"):
        c = cond[arm]
        print("    %s partial rho | register = %+.5f  CI [%+.5f, %+.5f]  d=0.25 -> %s"
              % (arm, c["partial_rho_given_register"], c["boot_ci95"][0], c["boot_ci95"][1],
                 c["equivalence"]["delta_0.25"]))
    print("  per-feature rho (k=6, alpha=%.5f):" % ALPHA_SECONDARY)
    for f, v in perfeat.items():
        print("    %-16s rho=%+.5f  p=%.5f  %s"
              % (f, v["rho"], v["perm_p_two_sided"], "*" if v["below_alpha_secondary"] else ""))
    print("  multiple R: armA=%.4f (LOOCV R2=%.4f)  armB=%.4f (LOOCV R2=%.4f)"
          % (mrA[0], mrA[2], mrB[0], mrB[2]))

    # ---- rules-tuple robustness (prereg §8) ---------------------------
    rt = collections.OrderedDict()

    def run_tuple(name, Dx, Ex, Mx, legx, escx):
        h1x = h1_test(Mx, S, legx, escx, lwc, SEED, "residualised", None)
        rhoB = spearman(Mx, R_B)
        loB, hiB, _ = bootstrap_ci(Mx, R_B, None, SEED)
        rhoA = spearman(Mx, R_A)
        loA, hiA, _ = bootstrap_ci(Mx, R_A, None, SEED)
        rt[name] = collections.OrderedDict([
            ("h1_delta", h1x["delta_obs"]), ("h1_p", h1x["p_one_sided"]),
            ("h1_verdict", "PRE-COMMIT VIOLATION" if h1x["delta_obs"] <= 0
             else ("PASS" if h1x["p_one_sided"] < ALPHA_BON_PRIMARY else "NULL")),
            ("rho_armB", round(rhoB, 6)), ("ci_armB", [round(loB, 6), round(hiB, 6)]),
            ("equiv_armB_d025", equivalence_verdict(loB, hiB, DELTA_PRIMARY)),
            ("rho_armA", round(rhoA, 6)), ("ci_armA", [round(loA, 6), round(hiA, 6)]),
            ("equiv_armA_d025", equivalence_verdict(loA, hiA, DELTA_PRIMARY)),
        ])

    run_tuple("RT-1_primary", D, E, M, leg, esc)
    leg2, esc2 = load_labels_cf028()
    run_tuple("RT-2_cf028_labels", D, E, M, leg2, esc2)
    D3, E3, _, _, _ = build_modality(word_segs, W_PRIMARY, False)
    run_tuple("RT-3_no_EMPH", D3, E3, [contrast_log(D3, E3, s) for s in S], leg, esc)
    D4, E4, cens4, _, _ = build_modality(word_segs, W_RT4, True)
    run_tuple("RT-4_window40", D4, E4, [contrast_log(D4, E4, s) for s in S], leg, esc)
    run_tuple("RT-5_bounded_contrast", D, E, [contrast_bounded(D, E, s) for s in S], leg, esc)
    rt["RT-4_jussive_census_W40"] = dict(cens4)
    results["rules_tuple_robustness"] = rt

    print("\n=== RULES-TUPLE ROBUSTNESS (prereg §8; may not establish or overturn a verdict) ===")
    for k, v in rt.items():
        if "h1_verdict" in v:
            print("  %-24s H1 delta=%+.4f p=%.4f %-22s | armB rho=%+.4f -> %s | armA rho=%+.4f -> %s"
                  % (k, v["h1_delta"], v["h1_p"], v["h1_verdict"], v["rho_armB"],
                     v["equiv_armB_d025"], v["rho_armA"], v["equiv_armA_d025"]))

    # ---- overall verdict ----------------------------------------------
    h2v = h2["ARM_B_5feature_VERDICT_BEARING"]["verdict_primary_delta"]
    results["verdict"] = collections.OrderedDict([
        ("H1_separation", h1_verdict),
        ("H2_orthogonality_armB_delta025", h2v),
        ("H2_orthogonality_armA_delta025",
         h2["ARM_A_6feature_fidelity_only"]["verdict_primary_delta"]),
        ("rules_tuple_fragile_H1", len({v["h1_verdict"] for v in rt.values()
                                        if "h1_verdict" in v}) > 1),
        ("rules_tuple_fragile_H2_armB", len({v["equiv_armB_d025"] for v in rt.values()
                                             if "equiv_armB_d025" in v}) > 1),
    ])
    results["per_surah"] = {str(s): {"D": D[s], "E": E[s], "M": round(M[s - 1], 6),
                                     "R_A": round(R_A[s - 1], 6), "R_B": round(R_B[s - 1], 6),
                                     "words": wordcount[s], "verses": versecount[s]} for s in S}

    # ---- write ONCE, mode 'x' (UNIT-DRIFT-DEFECT §7) -------------------
    with open(os.path.join(rundir, "results.json"), "x", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(rundir, "MANIFEST.txt"), "x", encoding="utf-8") as fh:
        fh.write("H-NEW-3040 run %s\n" % stamp)
        fh.write("prereg sha256 %s\n" % sha)
        fh.write("script findings/phase-b-hypotheses/scripts/h-new-3040.py\n")
        fh.write("seed %d  n_perm %d  n_boot %d\n" % (SEED, N_PERM, N_BOOT))
        fh.write("inputs:\n")
        for p in (QAC, J2530, J2390, J2500, GENRE_TSV):
            fh.write("  %s  sha256=%s\n" % (os.path.relpath(p, ROOT),
                                            hashlib.sha256(open(p, 'rb').read()).hexdigest()))

    print("\n=== VERDICT ===")
    for k, v in results["verdict"].items():
        print("  %-32s %s" % (k, v))
    print("\n[written] %s/results.json" % rundir)


if __name__ == "__main__":
    main()
