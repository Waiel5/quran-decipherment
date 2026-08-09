#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-3010 — Realis vs irrealis conditionals are register-coded?

Runs the test locked in
    findings/phase-b-hypotheses/prereg-h-new-3010-conditional-register.md

The pre-registration's SHA-256 is embedded below as a literal and verified at
runtime; on mismatch the script exits non-zero without computing anything.

Stdlib only.  Write-once run directory; the script never overwrites a file
inside its own run directory and performs no checkpointing.

Usage:  python3 findings/phase-b-hypotheses/scripts/h-new-3010.py
        (run from the repository root)
"""

import os
import sys
import re
import json
import math
import bisect
import random
import hashlib
import datetime
import platform
import collections
from operator import add

# --------------------------------------------------------------------------
# 0.  PRE-REGISTRATION LOCK
# --------------------------------------------------------------------------

EXPECTED_PREREG_SHA = "2b1718af47814c1eebc38178977074eba2631e45a7ff43e0ff0e98ad8c11fe93"

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PREREG_REL = "findings/phase-b-hypotheses/prereg-h-new-3010-conditional-register.md"
SCRIPT_REL = "findings/phase-b-hypotheses/scripts/h-new-3010.py"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    path = os.path.join(REPO, PREREG_REL)
    if not os.path.exists(path):
        raise SystemExit("FATAL: pre-registration not found at %s" % path)
    got = sha256_file(path)
    if got != EXPECTED_PREREG_SHA:
        raise SystemExit(
            "FATAL: pre-registration SHA-256 mismatch.\n"
            "  expected %s\n  got      %s\n"
            "The pre-registration has been modified. Refusing to run."
            % (EXPECTED_PREREG_SHA, got)
        )
    return got


# --------------------------------------------------------------------------
# 1.  LOCKED PARAMETERS  (prereg sections 2, 3, 5, 6)
# --------------------------------------------------------------------------

SEED = 20260509
N_PERM = 10000

# prereg 2.3 -- particle sets, RULES-TUPLE AXIS 1
TUPLES = {
    "T1": {"irrealis": {"law", "lawolaA^"},
           "realis":   {"<in", "<iyn", "<il~am", "<im~aA"}},
    "T2": {"irrealis": {"law"},
           "realis":   {"<in"}},
}
TUPLE_ORDER = ["T1", "T2"]

# prereg 5.1 -- length channels and bin widths
CHANNELS = ["log_word_count", "verse_count", "mean_verse_length"]
BINS = [5, 10]

# prereg 5.3 -- host-verse-length quintiles
N_VQ = 5

# prereg 5.5 -- power guard
MIN_TOKENS = 20

# prereg 6 -- family and alpha
K_FAMILY = 12
ALPHA_BON = 0.05 / K_FAMILY

# prereg 1.1 -- locked directions.  +1 == locked positive, -1 == locked negative
HYPOTHESES = ["H1", "H2", "H3"]
LOCKED_SIGN = {"H1": +1, "H2": -1, "H3": +1}
PRIMARY = ("H1", "M1", "T1")

CELLS = [("M1", "T1"), ("M1", "T2"), ("M2", "T1"), ("M2", "T2")]
MAPPINGS = ["M1", "M2"]

DATA_QAC = "data/morphology/quranic-corpus-morphology-0.4.txt"
DATA_TSV = "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
DATA_HVC = "data/hafs-verse-counts.tsv"
DATA_REV = "data/revelation-order.csv"
FROZEN_INPUTS = [DATA_QAC, DATA_TSV, DATA_HVC, DATA_REV]


# --------------------------------------------------------------------------
# 2.  LOAD QAC  (prereg 2.1, 5.1)
# --------------------------------------------------------------------------

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
LEM_RE = re.compile(r"LEM:([^|]+)")


def load_qac(path):
    """Return (cond_tokens, word_count, verse_count, verse_word_len)."""
    cond = []                                   # (surah, verse, word, lemma)
    words = collections.defaultdict(set)        # surah -> {(verse, word)}
    verses = collections.defaultdict(set)       # surah -> {verse}
    vwords = collections.defaultdict(set)       # (surah, verse) -> {word}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feat = parts[0], parts[1], parts[2], parts[3]
            m = LOC_RE.match(loc)
            if not m:
                raise SystemExit("FATAL: unparseable QAC location %r" % loc)
            s, v, w, _g = (int(x) for x in m.groups())
            words[s].add((v, w))
            verses[s].add(v)
            vwords[(s, v)].add(w)
            if tag == "COND":
                lm = LEM_RE.search(feat)
                if lm:
                    cond.append((s, v, w, lm.group(1)))
    word_count = {s: len(x) for s, x in words.items()}
    verse_count = {s: len(x) for s, x in verses.items()}
    verse_word_len = {k: len(x) for k, x in vwords.items()}
    return cond, word_count, verse_count, verse_word_len


# --------------------------------------------------------------------------
# 3.  LOAD REGISTER LABELS  (prereg 3)
# --------------------------------------------------------------------------

def map_M1(label):
    """LEGAL-PRECEDENCE CONTAINMENT (prereg 3.3)."""
    l = label.lower()
    if "legal" in l:
        return "LEGAL"
    if "eschatolog" in l or "polemic" in l:
        return "IRR"
    return "OTHER"


def map_M2(label):
    """FIRST-TOKEN DOMINANCE (prereg 3.3)."""
    t = label.lower().split("-")[0]
    if t == "legal":
        return "LEGAL"
    if t in ("polemical", "eschatological"):
        return "IRR"
    return "OTHER"


MAPPERS = {"M1": map_M1, "M2": map_M2}


def load_genre(path):
    raw = {}
    with open(path, encoding="utf-8") as fh:
        rows = [ln.rstrip("\n").split("\t") for ln in fh if not ln.startswith("#")]
    header = rows[0]
    i_num = header.index("surah_number")
    i_sin = header.index("sinai_genre")
    i_neu = header.index("neuwirth_genre")
    for r in rows[1:]:
        if not r or not r[0].strip():
            continue
        s = int(r[0])
        sinai = r[i_sin].strip() if len(r) > i_sin else ""
        neu = r[i_neu].strip() if len(r) > i_neu else ""
        if not sinai:
            raise SystemExit(
                "FATAL: surah %d has an empty sinai_genre; the pre-registration "
                "(sec 3.1) records that all 114 are non-empty and locks no fallback." % s
            )
        raw[s] = {"sinai": sinai, "neuwirth": neu}
    if sorted(raw) != list(range(1, 115)):
        raise SystemExit("FATAL: genre TSV does not cover surahs 1..114 exactly")
    return raw


# --------------------------------------------------------------------------
# 4.  SMALL STATS HELPERS  (stdlib only, no parametric tests anywhere)
# --------------------------------------------------------------------------

def rankdata(xs):
    """Average ranks, ties averaged."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(a, b):
    n = len(a)
    if n < 2:
        return None
    ma = sum(a) / n
    mb = sum(b) / n
    va = sum((x - ma) ** 2 for x in a)
    vb = sum((x - mb) ** 2 for x in b)
    if va <= 0 or vb <= 0:
        return None
    cov = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    return cov / math.sqrt(va * vb)


def spearman(a, b):
    return pearson(rankdata(a), rankdata(b))


def median(xs):
    if not xs:
        return None
    ys = sorted(xs)
    n = len(ys)
    return ys[n // 2] if n % 2 else (ys[n // 2 - 1] + ys[n // 2]) / 2.0


# --------------------------------------------------------------------------
# 5.  BUILD THE PER-SURAH COUNT VECTORS  (prereg 5.3)
# --------------------------------------------------------------------------
# vec[t][s] = [pooled_irr, pooled_tot,
#              q0_irr, q0_tot, q1_irr, q1_tot, ..., q4_irr, q4_tot]      len 12

VEC_LEN = 2 + 2 * N_VQ


def build_vectors(cond, verse_word_len):
    vecs = {}
    vq_bounds = {}
    vq_sizes = {}
    for tname in TUPLE_ORDER:
        irr_set = TUPLES[tname]["irrealis"]
        real_set = TUPLES[tname]["realis"]
        toks = [(s, v, w, lem) for (s, v, w, lem) in cond
                if lem in irr_set or lem in real_set]
        lens = sorted(verse_word_len[(s, v)] for (s, v, w, lem) in toks)
        n = len(lens)
        # quintile boundaries: fixed ONCE, held fixed across all permutations
        bounds = [lens[(n * i) // N_VQ] for i in range(1, N_VQ)]
        vq_bounds[tname] = bounds
        vec = {s: [0] * VEC_LEN for s in range(1, 115)}
        sizes = [0] * N_VQ
        for (s, v, w, lem) in toks:
            L = verse_word_len[(s, v)]
            q = bisect.bisect_right(bounds, L)
            if q >= N_VQ:
                q = N_VQ - 1
            sizes[q] += 1
            is_irr = 1 if lem in irr_set else 0
            vec[s][1] += 1
            vec[s][3 + 2 * q] += 1
            if is_irr:
                vec[s][0] += 1
                vec[s][2 + 2 * q] += 1
        vecs[tname] = vec
        vq_sizes[tname] = sizes
    return vecs, vq_bounds, vq_sizes


def share(acc):
    return acc[0] / acc[1] if acc[1] > 0 else None


def d_pooled(a, b):
    sa, sb = share(a), share(b)
    if sa is None or sb is None:
        return None
    return sa - sb


def d_verse(a, b):
    num = 0.0
    wsum = 0.0
    for q in range(N_VQ):
        ai, at = a[2 + 2 * q], a[3 + 2 * q]
        bi, bt = b[2 + 2 * q], b[3 + 2 * q]
        if at > 0 and bt > 0:
            w = at + bt
            num += w * (ai / at - bi / bt)
            wsum += w
    return (num / wsum) if wsum > 0 else None


STAT_FNS = {"D_pooled": d_pooled, "D_verse": d_verse}
STAT_ORDER = ["D_pooled", "D_verse"]


def group_accs(labels, vec, total):
    """labels: list of 114 strings indexed by surah-1. Returns (L, I, notL, notI)."""
    accL = [0] * VEC_LEN
    accI = [0] * VEC_LEN
    for i, lab in enumerate(labels):
        if lab == "LEGAL":
            accL = list(map(add, accL, vec[i + 1]))
        elif lab == "IRR":
            accI = list(map(add, accI, vec[i + 1]))
    notL = [total[j] - accL[j] for j in range(VEC_LEN)]
    notI = [total[j] - accI[j] for j in range(VEC_LEN)]
    return accL, accI, notL, notI


def all_statistics(labels, vecs, totals):
    """Returns {(tuple, stat, hyp): value or None}."""
    out = {}
    for tname in TUPLE_ORDER:
        accL, accI, notL, notI = group_accs(labels, vecs[tname], totals[tname])
        pairs = {"H1": (accI, accL), "H2": (accL, notL), "H3": (accI, notI)}
        for sname in STAT_ORDER:
            fn = STAT_FNS[sname]
            for h in HYPOTHESES:
                a, b = pairs[h]
                out[(tname, sname, h)] = fn(a, b)
        out[(tname, "_tokens", "H1")] = (accI[1], accL[1])
        out[(tname, "_tokens", "H2")] = (accL[1], notL[1])
        out[(tname, "_tokens", "H3")] = (accI[1], notI[1])
    return out


# --------------------------------------------------------------------------
# 6.  STRATA + PERMUTATION  (prereg 5.1, 5.2)
# --------------------------------------------------------------------------

def make_strata(channel_vals, n_bins):
    """channel_vals: list of 114 floats. Ties broken by ascending surah number."""
    idx = sorted(range(114), key=lambda i: (channel_vals[i], i))
    cuts = [(i * 114) // n_bins for i in range(n_bins + 1)]
    strata = []
    for b in range(n_bins):
        strata.append(idx[cuts[b]:cuts[b + 1]])
    return strata


def run_permutations(labels, strata, vecs, totals, obs, n_perm, seed):
    """Returns (tail_counts, n_none) keyed by (tuple, stat, hyp)."""
    rng = random.Random(seed)
    keys = [(t, s, h) for t in TUPLE_ORDER for s in STAT_ORDER for h in HYPOTHESES]
    tail = {k: 0 for k in keys}
    nones = {k: 0 for k in keys}
    cur = list(labels)
    for _ in range(n_perm):
        for st in strata:
            vals = [cur[i] for i in st]
            rng.shuffle(vals)
            for i, v in zip(st, vals):
                cur[i] = v
        st_perm = all_statistics(cur, vecs, totals)
        for k in keys:
            pv = st_perm[k]
            ov = obs[k]
            if pv is None or ov is None:
                # Not covered by the pre-registration; resolved CONSERVATIVELY
                # (counted into the tail, which can only inflate p). Logged.
                tail[k] += 1
                nones[k] += 1
                continue
            if LOCKED_SIGN[k[2]] > 0:
                if pv >= ov:
                    tail[k] += 1
            else:
                if pv <= ov:
                    tail[k] += 1
    return tail, nones


# --------------------------------------------------------------------------
# 7.  MAIN
# --------------------------------------------------------------------------

def main():
    prereg_sha = verify_prereg()
    script_sha = sha256_file(os.path.join(REPO, SCRIPT_REL))

    run_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(REPO, "findings/phase-b-hypotheses/runs/h-new-3010", run_utc)
    os.makedirs(rundir, exist_ok=False)          # write-once

    cond, word_count, verse_count, verse_word_len = load_qac(os.path.join(REPO, DATA_QAC))
    genre = load_genre(os.path.join(REPO, DATA_TSV))

    # cross-check verse counts against the Hafs file (prereg 5.1)
    hvc = {}
    with open(os.path.join(REPO, DATA_HVC), encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            p = line.split("\t")
            try:
                hvc[int(p[0])] = int(p[1])
            except (ValueError, IndexError):
                continue
    vc_mismatch = [s for s in range(1, 115) if hvc.get(s) != verse_count[s]]

    # revelation order (descriptive only, enters no statistic)
    period = {}
    with open(os.path.join(REPO, DATA_REV), encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split(",")
        i_m = hdr.index("mushaf_order")
        i_p = hdr.index("period")
        for line in fh:
            p = line.rstrip("\n").split(",")
            if len(p) <= max(i_m, i_p):
                continue
            period[int(p[i_m])] = p[i_p]

    # ---- census of the conditional apparatus -----------------------------
    lem_census = collections.Counter(lem for (_s, _v, _w, lem) in cond)
    used_T1 = TUPLES["T1"]["irrealis"] | TUPLES["T1"]["realis"]
    excluded = {k: v for k, v in lem_census.items() if k not in used_T1}

    # ---- label vectors ---------------------------------------------------
    label_vecs = {}
    for mname in MAPPINGS:
        fn = MAPPERS[mname]
        label_vecs[mname] = [fn(genre[s]["sinai"]) for s in range(1, 115)]

    membership = {
        m: {g: [s for s in range(1, 115) if label_vecs[m][s - 1] == g]
            for g in ("LEGAL", "IRR", "OTHER")}
        for m in MAPPINGS
    }

    # ---- count vectors ---------------------------------------------------
    vecs, vq_bounds, vq_sizes = build_vectors(cond, verse_word_len)
    totals = {t: [sum(vecs[t][s][j] for s in range(1, 115)) for j in range(VEC_LEN)]
              for t in TUPLE_ORDER}

    # ---- channels --------------------------------------------------------
    chan_vals = {
        "log_word_count":    [math.log(word_count[s]) for s in range(1, 115)],
        "verse_count":       [float(verse_count[s]) for s in range(1, 115)],
        "mean_verse_length": [word_count[s] / verse_count[s] for s in range(1, 115)],
    }

    # ======================================================================
    # 7a.  MANDATORY LENGTH DIAGNOSTIC  (prereg 4.2) -- REPORT, NOT A GATE
    # ======================================================================
    diag = {"group_length_profile": {}, "grouping_vs_length": {},
            "outcome_vs_length": {}, "note": "Reported unconditionally. The "
            "stratified nulls are primary regardless of what this shows."}

    for m in MAPPINGS:
        diag["group_length_profile"][m] = {}
        for g in ("LEGAL", "IRR", "OTHER"):
            ss = membership[m][g]
            diag["group_length_profile"][m][g] = {
                "n_surahs": len(ss),
                "median_word_count": median([word_count[s] for s in ss]),
                "mean_word_count": (sum(word_count[s] for s in ss) / len(ss)) if ss else None,
                "median_verse_count": median([verse_count[s] for s in ss]),
                "median_mean_verse_length": median([word_count[s] / verse_count[s] for s in ss]),
            }
        diag["grouping_vs_length"][m] = {}
        for g in ("LEGAL", "IRR"):
            ind = [1.0 if label_vecs[m][s - 1] == g else 0.0 for s in range(1, 115)]
            diag["grouping_vs_length"][m][g] = {
                c: spearman(ind, chan_vals[c]) for c in CHANNELS
            }

    # outcome vs length: per-surah irrealis share, surahs with >= 3 T1 tokens
    for t in TUPLE_ORDER:
        ss = [s for s in range(1, 115) if vecs[t][s][1] >= 3]
        shares = [vecs[t][s][0] / vecs[t][s][1] for s in ss]
        diag["outcome_vs_length"][t] = {
            "n_surahs_with_ge3_tokens": len(ss),
            "spearman": {c: spearman(shares, [chan_vals[c][s - 1] for s in ss])
                         for c in CHANNELS},
        }

    # ======================================================================
    # 7b.  OBSERVED STATISTICS
    # ======================================================================
    observed = {m: all_statistics(label_vecs[m], vecs, totals) for m in MAPPINGS}

    # descriptive per-register tables (reported, not tested)
    descriptive = {}
    for m in MAPPINGS:
        descriptive[m] = {}
        for g in ("LEGAL", "IRR", "OTHER"):
            ss = membership[m][g]
            descriptive[m][g] = {}
            for t in TUPLE_ORDER:
                irr = sum(vecs[t][s][0] for s in ss)
                tot = sum(vecs[t][s][1] for s in ss)
                descriptive[m][g][t] = {
                    "n_irrealis": irr, "n_realis": tot - irr, "n_total": tot,
                    "irrealis_share": (irr / tot) if tot else None,
                }

    # secondary declared arm (prereg 9.3): surah-unweighted mean share
    secondary_unweighted = {}
    for m in MAPPINGS:
        secondary_unweighted[m] = {}
        for t in TUPLE_ORDER:
            row = {}
            for g in ("LEGAL", "IRR", "OTHER"):
                ss = [s for s in membership[m][g] if vecs[t][s][1] >= 3]
                vals = [vecs[t][s][0] / vecs[t][s][1] for s in ss]
                row[g] = {"n_surahs_ge3": len(ss),
                          "mean_share": (sum(vals) / len(vals)) if vals else None,
                          "median_share": median(vals)}
            secondary_unweighted[m][t] = row

    # per-genre-label raw table, including NARRATIVE (descriptive only)
    by_label = {}
    for s in range(1, 115):
        lab = genre[s]["sinai"]
        d = by_label.setdefault(lab, {"surahs": [], "T1_irr": 0, "T1_tot": 0})
        d["surahs"].append(s)
        d["T1_irr"] += vecs["T1"][s][0]
        d["T1_tot"] += vecs["T1"][s][1]
    for lab, d in by_label.items():
        d["irrealis_share"] = (d["T1_irr"] / d["T1_tot"]) if d["T1_tot"] else None

    narrative = [s for s in range(1, 115) if "narrative" in genre[s]["sinai"].lower()
                 or "qaṣaṣ" in genre[s]["sinai"].lower()]
    nar_irr = sum(vecs["T1"][s][0] for s in narrative)
    nar_tot = sum(vecs["T1"][s][1] for s in narrative)
    descriptive["NARRATIVE_descriptive_only"] = {
        "n_surahs": len(narrative), "surahs": narrative,
        "T1_n_irrealis": nar_irr, "T1_n_total": nar_tot,
        "T1_irrealis_share": (nar_irr / nar_tot) if nar_tot else None,
        "note": "No directional prediction was locked for narrative (prereg 9.15). "
                "Descriptive only; may not be promoted into any test.",
    }

    mec_med = {}
    for lbl in ("Meccan", "Medinan"):
        ss = [s for s in range(1, 115) if period.get(s) == lbl]
        irr = sum(vecs["T1"][s][0] for s in ss)
        tot = sum(vecs["T1"][s][1] for s in ss)
        mec_med[lbl] = {"n_surahs": len(ss), "n_irrealis": irr, "n_total": tot,
                        "irrealis_share": (irr / tot) if tot else None}
    descriptive["meccan_medinan_descriptive_only"] = mec_med

    # ======================================================================
    # 7c.  THE 12 STRATIFIED NULLS + 2 UNSTRATIFIED (reported for contrast)
    # ======================================================================
    pvals = {}          # (mapping, channel, bins, tuple, stat, hyp) -> p
    none_log = {}
    configs = [(m, c, b) for m in MAPPINGS for c in CHANNELS for b in BINS]
    for (m, c, b) in configs:
        strata = make_strata(chan_vals[c], b)
        tail, nones = run_permutations(label_vecs[m], strata, vecs, totals,
                                       observed[m], N_PERM, SEED)
        for k, v in tail.items():
            pvals[(m, c, b) + k] = (1 + v) / (1 + N_PERM)
            if nones[k]:
                none_log["|".join(map(str, (m, c, b) + k))] = nones[k]
        sys.stderr.write("  null done: %s / %s / bins=%d\n" % (m, c, b))

    unstrat = {}
    for m in MAPPINGS:
        strata = [list(range(114))]
        tail, _n = run_permutations(label_vecs[m], strata, vecs, totals,
                                    observed[m], N_PERM, SEED)
        for k, v in tail.items():
            unstrat["|".join((m,) + k)] = (1 + v) / (1 + N_PERM)
        sys.stderr.write("  unstratified null done: %s\n" % m)

    # ======================================================================
    # 7d.  PER-TEST AGGREGATION  (prereg 5.4, 5.5)
    # ======================================================================
    tests = {}
    for h in HYPOTHESES:
        for (m, t) in CELLS:
            na, nb = observed[m][(t, "_tokens", h)]
            dp = observed[m][(t, "D_pooled", h)]
            dv = observed[m][(t, "D_verse", h)]
            computable = (na >= MIN_TOKENS) and (nb >= MIN_TOKENS) and (dv is not None)
            if dp is None:
                sign_ok = False
            elif LOCKED_SIGN[h] > 0:
                sign_ok = dp > 0
            else:
                sign_ok = dp < 0
            grid = {}
            for c in CHANNELS:
                for b in BINS:
                    for s in STAT_ORDER:
                        grid["%s|bins=%d|%s" % (c, b, s)] = pvals[(m, c, b, t, s, h)]
            p_test = max(grid.values())
            clears = bool(computable and sign_ok and (p_test < ALPHA_BON))
            tests["%s|%s|%s" % (h, m, t)] = {
                "hypothesis": h, "mapping": m, "tuple": t,
                "locked_sign": LOCKED_SIGN[h],
                "n_tokens_group_a": na, "n_tokens_group_b": nb,
                "D_pooled": dp, "D_verse": dv,
                "computable": computable,
                "not_powered_reason": (None if computable else
                                       ("D_verse undefined" if dv is None
                                        else "group tokens < %d" % MIN_TOKENS)),
                "sign_ok": sign_ok,
                "p_grid": grid,
                "p_min": min(grid.values()),
                "p_test_max": p_test,
                "sig_raw_0.05": bool(p_test < 0.05),
                "sig_bonferroni": bool(p_test < ALPHA_BON),
                "clears": clears,
            }

    # ======================================================================
    # 7e.  VERDICT  -- mirrors prereg section 6 line by line
    # ======================================================================
    n_clear = sum(1 for v in tests.values() if v["clears"])
    pk = "%s|%s|%s" % PRIMARY
    prim = tests[pk]

    if prim["computable"] and prim["D_pooled"] is not None and prim["D_pooled"] < 0:
        verdict = "NULL — PRE-COMMIT VIOLATION (direction reversed)"
    elif n_clear == 12:
        verdict = "PASS"
    elif prim["clears"] and n_clear >= 8:
        verdict = "DIRECTIONAL"
    elif prim["clears"]:
        verdict = "WEAK-DIRECTIONAL"
    else:
        verdict = "NULL"

    # ======================================================================
    # 8.  WRITE (mode 'x' everywhere; never overwritten)
    # ======================================================================
    manifest = {
        "finding_id": "H-NEW-3010",
        "title": "Realis vs irrealis conditionals are register-coded?",
        "run_utc": run_utc,
        "prereg": {"path": PREREG_REL, "sha256": prereg_sha},
        "script": {"path": SCRIPT_REL, "sha256": script_sha},
        "frozen_inputs": [{"path": p, "sha256": sha256_file(os.path.join(REPO, p))}
                          for p in FROZEN_INPUTS],
        "seed": SEED, "n_perm": N_PERM,
        "k_family": K_FAMILY, "alpha_bonferroni": ALPHA_BON,
        "python": platform.python_version(),
        "write_once": True,
    }

    results = {
        "verdict": verdict,
        "n_clear_of_12": n_clear,
        "primary_test": pk,
        "alpha_bonferroni": ALPHA_BON,
        "conditional_census": {
            "total_POS_COND_segments": len(cond),
            "by_lemma": dict(lem_census.most_common()),
            "lemmas_used_T1": sorted(used_T1),
            "lemmas_excluded_by_rule": dict(sorted(excluded.items(),
                                                   key=lambda kv: -kv[1])),
        },
        "corpus_structure": {
            "qac_word_positions": sum(word_count.values()),
            "qac_verses": sum(verse_count.values()),
            "verse_count_mismatches_vs_hafs_tsv": vc_mismatch,
        },
        "verse_length_quintiles": {
            t: {"boundaries": vq_bounds[t], "token_counts": vq_sizes[t]}
            for t in TUPLE_ORDER
        },
        "register_membership": membership,
        "length_diagnostic": diag,
        "descriptive": descriptive,
        "secondary_surah_unweighted_arm": secondary_unweighted,
        "by_genre_label_descriptive": by_label,
        "tests": tests,
        "unstratified_nulls_for_contrast_only": unstrat,
        "none_statistic_log": none_log,
        "implementation_note_not_in_prereg": (
            "If a permuted or observed statistic is undefined (a group with zero "
            "conditional tokens in the relevant cell), the permutation draw is counted "
            "INTO the tail, which can only inflate p. This is a tightening, resolved "
            "conservatively; the count of such draws is in none_statistic_log."
        ),
    }

    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
    with open(os.path.join(rundir, "results.json"), "x", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)

    lines = ["H-NEW-3010 — realis vs irrealis conditionals are register-coded?",
             "run_utc: %s" % run_utc,
             "prereg sha256: %s" % prereg_sha,
             "",
             "VERDICT: %s" % verdict,
             "tests clearing (Bonferroni alpha=%.8f): %d of 12" % (ALPHA_BON, n_clear),
             "",
             "%-16s %-7s %-6s %11s %11s %10s %8s %s"
             % ("test", "sign", "pow", "D_pooled", "D_verse", "p(max)", "clears", "")]
    for h in HYPOTHESES:
        for (m, t) in CELLS:
            v = tests["%s|%s|%s" % (h, m, t)]
            lines.append("%-16s %-7s %-6s %11.5f %11s %10.5f %8s"
                         % ("%s|%s|%s" % (h, m, t),
                            "+" if v["locked_sign"] > 0 else "-",
                            "ok" if v["computable"] else "LOW",
                            v["D_pooled"] if v["D_pooled"] is not None else float("nan"),
                            ("%.5f" % v["D_verse"]) if v["D_verse"] is not None else "undef",
                            v["p_test_max"], "YES" if v["clears"] else "no"))
    with open(os.path.join(rundir, "verdict.txt"), "x", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    print("\nrun dir: %s" % rundir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
