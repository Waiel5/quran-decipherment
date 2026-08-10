#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-NEW-3080 — Does quantifier scope (kull vs baʿḍ) separate the community-legal
register from the universal-address register?

Pre-registration : findings/phase-b-hypotheses/prereg-h-new-3080-quantifier-scope.md
Frontier id      : F-14

VERDICT FUNCTION <-> PRE-REGISTRATION CORRESPONDENCE
(diff this block against the pre-registration section by section before running)

  prereg 3.2   U pole ............ lemma kul~  (359 word-tokens, register-blind)
  prereg 3.3   P pole ............ RT-A1 PRIMARY lemma baEoD; RT-A2 adds min+Al-definite
                                   proxy, ROBUSTNESS ONLY, verdict-inert
  prereg 3.4   counting .......... RT-B1 PRIMARY word-token; RT-B2 verse-presence,
                                   ROBUSTNESS ONLY, verdict-inert
  prereg 4.2   exclusion ladder .. EX-0 {} 359 | EX-1 {$aYo'} 238 |
                                   EX-2 PRIMARY {$aYo',nafos} 215 | EX-3 +{>um~ap} 200
                                   a kull token is excluded iff the lemma set of the NEXT
                                   word IN THE SAME VERSE meets the level's set
  prereg 5.1   ARM 1 maps ........ MAP-1 PRIMARY legal / eschatolog|exhort|admonit (17,42)
                                   MAP-2          legal / eschatolog|polemic     (17,36)
                                   both LEGAL-precedence containment
  prereg 5.2   ARM 2 blocks ...... opener = FORM contains >ay~uhaA;
                                   UNIVERSAL if next lemma n~aAs or <insa`n (23)
                                   COMMUNITY if next lemma {l~a*iY and next-next 'aAmana (89)
                                   block = opener verse .. verse before next opener of
                                   either type in the same surah, else surah end
  prereg 6.1   statistic ......... LOR = log( (U_L+.5)(P_V+.5) / ((P_L+.5)(U_V+.5)) )
  prereg 6.2   null .............. permutation of the pole label across units,
                                   per-unit counts fixed, seed 20260509, 10000 draws,
                                   random.Random + rng.shuffle, one generator, fixed order
               p ................. one-sided (#{LOR_perm <= LOR_obs} + 1)/(n_perm + 1)
  prereg 6.3   channels .......... C0 unstratified | C1 log word count quintiles |
                                   C2 verse count quintiles | C3 mean verse length quintiles
               ALL FOUR REPORTED.  p_cell = MAX over non-degenerate channels (the WORST)
               dominant channel .. argmax |Spearman(channel, pole indicator)|,
                                   COMPUTED AND STORED BEFORE ANY PRIMARY STATISTIC
               degeneracy ........ < 100 distinct permuted label vectors -> DEGENERATE,
                                   reported, EXCLUDED from the max
  prereg 6.4   ties .............. tie fraction reported for every cell; > 0.50 on a
                                   primary-family cell -> Fisher exact one-sided replaces p_cell
  prereg 7.1   family ............ k = 6, alpha_bon = 0.05/6 = 0.008333...
                                   cell 1 = ARM1/MAP-1/EX-2 is THE PRIMARY TEST
  prereg 7.2   per-cell verdict ..  LOR_obs >= 0                      -> PRE-COMMIT VIOLATION
                                    LOR_obs <  0 and p < alpha_bon    -> PASS
                                    LOR_obs <  0 and p >= alpha_bon   -> NULL
  prereg 7.3   finding verdict ... cell1 PASS and cell2 PASS -> CONFIRMED
                                   cell2 PASS and cell1 NULL -> CONFIRMED-FORMULAIC
                                   cell1 PASS and cell2 NULL -> CONFIRMED-NON-FORMULAIC
                                   both NULL                 -> NULL
                                   cell1 violation           -> NULL-REVERSED
                                   cells 3-6 qualify, MAY NOT create a verdict
  prereg 7.4   robustness ........ RT-A2, RT-B2, EX-1, EX-3, ARM2 windows W in {3,5},
                                   per-surah secondary, density secondary -- all printed,
                                   all uncorrected, NONE may establish or overturn
  prereg 8     MDE ............... for EVERY NULL cell: binomial thinning of LEGAL-pole
                                   kull with retention 1/r over the locked OR grid,
                                   1000 sims x 2000 inner perms, C0 only, alpha_bon,
                                   numpy.random.default_rng(20260509); MDE = smallest r
                                   at 80% power, else "> 4.0"
  prereg 11    outputs ........... makedirs(exist_ok=False), every file open(...,'x'),
                                   run dir findings/phase-b-hypotheses/runs/h-new-3080/<UTC>/

Rules-tuple RT-1 (primary): (no-tashkeel, QAC v0.4 LEM field, word-grouped by (s:v:w),
Hafs-Kufan, Mashriqi, basmala counted only in Q1, U = kul~, P = baEoD, token counts,
formula-exclusion EX-2, register = Neuwirth-Sinai sinai_genre mechanical mapping MAP-1)

Author: Waiel Al-Shujaa   Date: 2026-08-09
"""

import os
import re
import sys
import json
import math
import random
import hashlib
import datetime
import collections

# --------------------------------------------------------------------------
# 0.  PRE-REGISTRATION LOCK
# --------------------------------------------------------------------------

PREREG = "findings/phase-b-hypotheses/prereg-h-new-3080-quantifier-scope.md"
EXPECTED_PREREG_SHA = "2e2cde58e7fc2e66f34d27d007c3ed8be19d6eeb30550c6a88ec24f7cc4443e4"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    got = sha256_file(PREREG)
    if got != EXPECTED_PREREG_SHA:
        raise SystemExit(
            "FATAL: pre-registration SHA-256 mismatch.\n"
            "  expected %s\n  got      %s\n"
            "The pre-registration has been modified. Refusing to run."
            % (EXPECTED_PREREG_SHA, got)
        )
    return got


# --------------------------------------------------------------------------
# 1.  LOCKED PARAMETERS
# --------------------------------------------------------------------------

SEED = 20260509
N_PERM = 10000
N_BINS = 5                       # prereg 6.3 -- quintiles
MIN_DISTINCT = 100               # prereg 6.3 -- degeneracy guard
TIE_LIMIT = 0.50                 # prereg 6.4
K_FAMILY = 6                     # prereg 7.1
ALPHA_BON = 0.05 / K_FAMILY

LEM_U = "kul~"
LEM_P = "baEoD"
LEM_MIN = "min"

EX_SETS = {
    "EX-0": frozenset(),
    "EX-1": frozenset({"$aYo'"}),
    "EX-2": frozenset({"$aYo'", "nafos"}),
    "EX-3": frozenset({"$aYo'", "nafos", ">um~ap"}),
}
EX_ORDER = ["EX-0", "EX-1", "EX-2", "EX-3"]

CHANNELS = ["C0", "C1", "C2", "C3"]
CHANNEL_KEY = {"C1": "log_word_count", "C2": "verse_count", "C3": "mean_verse_length"}

# prereg 8 -- locked MDE grid
OR_GRID = [1.1, 1.2, 1.3, 1.5, 1.75, 2.0, 2.5, 3.0, 4.0]
MDE_SIMS = 1000
MDE_INNER_PERM = 2000
MDE_POWER = 0.80

# prereg 5.2 -- robustness windows
ARM2_WINDOWS = [3, 5]

DATA_QAC = "data/morphology/quranic-corpus-morphology-0.4.txt"
DATA_TSV = "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
DATA_HVC = "data/hafs-verse-counts.tsv"
FROZEN_INPUTS = [DATA_QAC, DATA_TSV, DATA_HVC]

RUN_ROOT = "findings/phase-b-hypotheses/runs/h-new-3080"


# --------------------------------------------------------------------------
# 2.  LOAD QAC  (prereg 3.1)
# --------------------------------------------------------------------------

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
LEM_RE = re.compile(r"LEM:([^|]+)")


def load_qac(path):
    """Group segments into words keyed (s, v, w), in corpus order."""
    words = collections.OrderedDict()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                raise SystemExit("FATAL: unparseable QAC location %r" % parts[0])
            s, v, w, _g = (int(x) for x in m.groups())
            words.setdefault((s, v, w), []).append((parts[1], parts[2], parts[3]))
    return words


def word_lemmas(segs):
    out = set()
    for _form, _tag, feat in segs:
        m = LEM_RE.search(feat)
        if m:
            out.add(m.group(1))
    return out


def word_form(segs):
    return "".join(f for f, _t, _ft in segs)


def has_definite_article(segs):
    return any(t == "DET" and "Al+" in ft for _f, t, ft in segs)


# --------------------------------------------------------------------------
# 3.  TOKEN EXTRACTION  (prereg 3.2 - 3.4, 4.2)
# --------------------------------------------------------------------------

def extract_tokens(words):
    keys = list(words.keys())
    idx = {k: i for i, k in enumerate(keys)}
    lemsets = {k: word_lemmas(words[k]) for k in keys}

    def next_key(k, step=1):
        i = idx[k] + step
        if i < len(keys) and keys[i][0] == k[0] and keys[i][1] == k[1]:
            return keys[i]
        return None

    u_tokens = []          # (s, v, w, excluded_at_levels frozenset)
    for k in keys:
        if LEM_U not in lemsets[k]:
            continue
        nk = next_key(k)
        nl = lemsets[nk] if nk is not None else frozenset()
        levels = frozenset(lv for lv in EX_ORDER if nl & EX_SETS[lv])
        u_tokens.append((k[0], k[1], k[2], levels))

    p_tokens = [(k[0], k[1], k[2]) for k in keys if LEM_P in lemsets[k]]

    p_min_proxy = []
    for k in keys:
        if LEM_MIN not in lemsets[k]:
            continue
        nk = next_key(k)
        if nk is not None and has_definite_article(words[nk]):
            p_min_proxy.append((k[0], k[1], k[2]))

    return keys, idx, lemsets, u_tokens, p_tokens, p_min_proxy


def surah_metrics(words):
    wc = collections.Counter()
    vs = collections.defaultdict(set)
    for (s, v, _w) in words:
        wc[s] += 1
        vs[s].add(v)
    out = {}
    for s in range(1, 115):
        n_v = len(vs[s])
        out[s] = {
            "word_count": wc[s],
            "verse_count": n_v,
            "log_word_count": math.log(wc[s]),
            "mean_verse_length": wc[s] / n_v,
        }
    return out


# --------------------------------------------------------------------------
# 4.  REGISTER MAPS  (prereg 5.1)
# --------------------------------------------------------------------------

def map_1(label):
    l = label.lower()
    if "legal" in l:
        return "LEGAL"
    if ("eschatolog" in l) or ("exhort" in l) or ("admonit" in l):
        return "UNIV"
    return "OTHER"


def map_2(label):
    l = label.lower()
    if "legal" in l:
        return "LEGAL"
    if ("eschatolog" in l) or ("polemic" in l):
        return "UNIV"
    return "OTHER"


MAPPERS = {"MAP-1": map_1, "MAP-2": map_2}


def load_genre(path):
    rows = [ln.rstrip("\n").split("\t") for ln in open(path, encoding="utf-8")
            if not ln.startswith("#")]
    header = rows[0]
    i_num = header.index("surah_number")
    i_sin = header.index("sinai_genre")
    out = {}
    for r in rows[1:]:
        if not r or not r[i_num].strip():
            continue
        s = int(r[i_num])
        sinai = r[i_sin].strip() if len(r) > i_sin else ""
        if not sinai:
            raise SystemExit("FATAL: surah %d has an empty sinai_genre" % s)
        out[s] = sinai
    if sorted(out) != list(range(1, 115)):
        raise SystemExit("FATAL: genre TSV does not cover surahs 1..114 exactly")
    return out


# --------------------------------------------------------------------------
# 5.  ARM 2 BLOCKS  (prereg 5.2)
# --------------------------------------------------------------------------

def build_blocks(words, keys, idx, lemsets):
    def nth_lemmas(k, step):
        i = idx[k] + step
        if i < len(keys) and keys[i][0] == k[0] and keys[i][1] == k[1]:
            return lemsets[keys[i]]
        return frozenset()

    openers = []
    for k in keys:
        if ">ay~uhaA" not in word_form(words[k]):
            continue
        n1 = nth_lemmas(k, 1)
        n2 = nth_lemmas(k, 2)
        if ("n~aAs" in n1) or ("<insa`n" in n1):
            openers.append((k[0], k[1], "UNIVERSAL"))
        elif ("{l~a*iY" in n1) and ("'aAmana" in n2):
            openers.append((k[0], k[1], "COMMUNITY"))
        else:
            openers.append((k[0], k[1], "NON-DELIMITING"))

    vmax = collections.Counter()
    for (s, v, _w) in keys:
        vmax[s] = max(vmax[s], v)

    by_s = collections.defaultdict(list)
    for s, v, t in openers:
        if t != "NON-DELIMITING":
            by_s[s].append((v, t))

    blocks = []
    for s, lst in by_s.items():
        lst = sorted(set(lst))
        for j, (v, t) in enumerate(lst):
            end = lst[j + 1][0] - 1 if j + 1 < len(lst) else vmax[s]
            if end >= v:
                blocks.append({"surah": s, "v_start": v, "v_end": end, "pole": t})
    blocks.sort(key=lambda b: (b["surah"], b["v_start"]))
    n_nd = sum(1 for o in openers if o[2] == "NON-DELIMITING")
    return blocks, openers, n_nd


def window_blocks(openers, vmax, w):
    by_s = collections.defaultdict(list)
    for s, v, t in openers:
        if t != "NON-DELIMITING":
            by_s[s].append((v, t))
    out = []
    for s, lst in by_s.items():
        lst = sorted(set(lst))
        for j, (v, t) in enumerate(lst):
            end = min(v + w, vmax[s])
            if j + 1 < len(lst):
                end = min(end, lst[j + 1][0] - 1)
            if end >= v:
                out.append({"surah": s, "v_start": v, "v_end": end, "pole": t})
    return out


# --------------------------------------------------------------------------
# 6.  STATISTIC AND NULL  (prereg 6)
# --------------------------------------------------------------------------

def lor(u_l, p_l, u_v, p_v):
    return math.log(((u_l + 0.5) * (p_v + 0.5)) / ((p_l + 0.5) * (u_v + 0.5)))


def pooled_lor(labels, u_counts, p_counts):
    u_l = p_l = u_v = p_v = 0
    for i, lab in enumerate(labels):
        if lab == "LEGAL":
            u_l += u_counts[i]
            p_l += p_counts[i]
        else:
            u_v += u_counts[i]
            p_v += p_counts[i]
    return lor(u_l, p_l, u_v, p_v), (u_l, p_l, u_v, p_v)


def make_strata(vals, n_bins):
    """Contiguous equal-size strata over sorted values; ties broken by index."""
    order = sorted(range(len(vals)), key=lambda i: (vals[i], i))
    strata = [0] * len(vals)
    n = len(vals)
    for rank, i in enumerate(order):
        strata[i] = min(n_bins - 1, rank * n_bins // n)
    return strata


def permute(rng, labels, strata):
    if strata is None:
        out = list(labels)
        rng.shuffle(out)
        return out
    out = list(labels)
    groups = collections.defaultdict(list)
    for i, g in enumerate(strata):
        groups[g].append(i)
    for g in sorted(groups):
        pos = groups[g]
        vals = [labels[i] for i in pos]
        rng.shuffle(vals)
        for i, v in zip(pos, vals):
            out[i] = v
    return out


def spearman(a, b):
    def rank(x):
        order = sorted(range(len(x)), key=lambda i: x[i])
        r = [0.0] * len(x)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and x[order[j + 1]] == x[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    ra, rb = rank(a), rank(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((ra[i] - ma) * (rb[i] - mb) for i in range(n))
    da = math.sqrt(sum((ra[i] - ma) ** 2 for i in range(n)))
    db = math.sqrt(sum((rb[i] - mb) ** 2 for i in range(n)))
    return num / (da * db) if da > 0 and db > 0 else 0.0


def fisher_exact_less(u_l, p_l, u_v, p_v):
    """One-sided Fisher exact: P(U_L <= observed) given margins.

    'Less' is the locked direction: fewer universals in LEGAL than chance.
    """
    row1 = u_l + p_l
    row2 = u_v + p_v
    col1 = u_l + u_v
    total = row1 + row2

    def logC(n, k):
        return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)

    lo = max(0, col1 - row2)
    log_denom = logC(total, col1)
    acc = 0.0
    for x in range(lo, u_l + 1):
        if x > row1 or (col1 - x) > row2:
            continue
        acc += math.exp(logC(row1, x) + logC(row2, col1 - x) - log_denom)
    return min(1.0, acc)


def run_cell(rng, labels, u_counts, p_counts, chan_vals):
    """Full four-channel null for one cell. Returns the cell record."""
    obs, table = pooled_lor(labels, u_counts, p_counts)
    rec = {"LOR_obs": obs, "table": {"U_LEGAL": table[0], "P_LEGAL": table[1],
                                     "U_UNIV": table[2], "P_UNIV": table[3]},
           "n_units": len(labels),
           "n_LEGAL": sum(1 for l in labels if l == "LEGAL"),
           "channels": {}}
    for c in CHANNELS:
        strata = None if c == "C0" else make_strata(chan_vals[CHANNEL_KEY[c]], N_BINS)
        n_le = 0
        n_tie = 0
        seen = set()
        for _ in range(N_PERM):
            perm = permute(rng, labels, strata)
            seen.add(tuple(perm))
            val, _t = pooled_lor(perm, u_counts, p_counts)
            if val <= obs:
                n_le += 1
            if abs(val - obs) < 1e-12:
                n_tie += 1
        distinct = len(seen)
        rec["channels"][c] = {
            "p": (n_le + 1) / (N_PERM + 1),
            "tie_fraction": n_tie / N_PERM,
            "distinct_label_vectors": distinct,
            "degenerate": (c != "C0") and (distinct < MIN_DISTINCT),
        }
    live = [c for c in CHANNELS if not rec["channels"][c]["degenerate"]]
    rec["degenerate_channels"] = [c for c in CHANNELS if rec["channels"][c]["degenerate"]]
    rec["p_cell_permutation"] = max(rec["channels"][c]["p"] for c in live)
    rec["p_cell_channel_argmax"] = max(live, key=lambda c: rec["channels"][c]["p"])
    rec["max_tie_fraction"] = max(rec["channels"][c]["tie_fraction"] for c in CHANNELS)
    rec["fisher_exact_p"] = fisher_exact_less(table[0], table[1], table[2], table[3])
    if rec["max_tie_fraction"] > TIE_LIMIT:
        rec["p_cell"] = rec["fisher_exact_p"]
        rec["p_cell_source"] = "fisher_exact (tie fraction > 0.50, prereg 6.4)"
    else:
        rec["p_cell"] = rec["p_cell_permutation"]
        rec["p_cell_source"] = "permutation max over non-degenerate channels (prereg 6.3)"
    return rec


def verdict_cell(rec):
    """prereg 7.2, line by line."""
    if rec["LOR_obs"] >= 0:
        return "PRE-COMMIT VIOLATION"
    if rec["p_cell"] < ALPHA_BON:
        return "PASS"
    return "NULL"


def verdict_finding(v1, v2):
    """prereg 7.3, line by line."""
    if v1 == "PRE-COMMIT VIOLATION":
        return "NULL-REVERSED"
    if v2 == "PRE-COMMIT VIOLATION":
        base = "CONFIRMED-NON-FORMULAIC" if v1 == "PASS" else "NULL"
        return base + " +CELL-2-REVERSED"
    if v1 == "PASS" and v2 == "PASS":
        return "CONFIRMED"
    if v2 == "PASS" and v1 == "NULL":
        return "CONFIRMED-FORMULAIC"
    if v1 == "PASS" and v2 == "NULL":
        return "CONFIRMED-NON-FORMULAIC"
    if v1 == "NULL" and v2 == "NULL":
        return "NULL"
    raise SystemExit("FATAL: unreachable verdict combination (%r, %r)" % (v1, v2))


# --------------------------------------------------------------------------
# 7.  MDE  (prereg 8)
# --------------------------------------------------------------------------

def mde_for_cell(u_counts, p_counts, labels):
    import numpy as np
    gen = np.random.default_rng(SEED)
    u = np.array(u_counts, dtype=np.int64)
    p = np.array(p_counts, dtype=np.int64)
    is_legal = np.array([1 if l == "LEGAL" else 0 for l in labels], dtype=bool)
    n = len(labels)
    n_l = int(is_legal.sum())
    curve = []
    mde = None
    for r in OR_GRID:
        rejects = 0
        for _ in range(MDE_SIMS):
            u_sim = u.copy()
            u_sim[is_legal] = gen.binomial(u[is_legal], 1.0 / r)
            u_l = int(u_sim[is_legal].sum())
            p_l = int(p[is_legal].sum())
            u_v = int(u_sim[~is_legal].sum())
            p_v = int(p[~is_legal].sum())
            obs = lor(u_l, p_l, u_v, p_v)
            perm_idx = np.argsort(gen.random((MDE_INNER_PERM, n)), axis=1)[:, :n_l]
            ul = u_sim[perm_idx].sum(axis=1)
            pl = p[perm_idx].sum(axis=1)
            uv = u_sim.sum() - ul
            pv = p.sum() - pl
            vals = np.log(((ul + 0.5) * (pv + 0.5)) / ((pl + 0.5) * (uv + 0.5)))
            pv_perm = (int((vals <= obs).sum()) + 1) / (MDE_INNER_PERM + 1)
            if pv_perm < ALPHA_BON:
                rejects += 1
        power = rejects / MDE_SIMS
        curve.append({"OR": r, "power": power})
        if mde is None and power >= MDE_POWER:
            mde = r
    return {"grid": curve, "MDE_at_80pct_power": mde if mde is not None else "> 4.0",
            "sims_per_point": MDE_SIMS, "inner_perms": MDE_INNER_PERM,
            "alpha": ALPHA_BON, "null": "C0 unstratified", "rng": "numpy default_rng(%d)" % SEED}


# --------------------------------------------------------------------------
# 8.  MAIN
# --------------------------------------------------------------------------

def main():
    prereg_sha = verify_prereg()
    started = datetime.datetime.now(datetime.timezone.utc)
    stamp = started.strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(RUN_ROOT, stamp)
    os.makedirs(run_dir, exist_ok=False)

    words = load_qac(DATA_QAC)
    keys, idx, lemsets, u_tokens, p_tokens, p_min_proxy = extract_tokens(words)
    metrics = surah_metrics(words)
    genre = load_genre(DATA_TSV)

    R = collections.OrderedDict()
    R["finding_id"] = "H-NEW-3080"
    R["frontier_id"] = "F-14"
    R["run_utc"] = stamp
    R["prereg_sha256"] = prereg_sha
    R["seed"] = SEED
    R["n_perm"] = N_PERM
    R["k_family"] = K_FAMILY
    R["alpha_bonferroni"] = ALPHA_BON
    R["locked_direction"] = "LOR < 0  (universal/partitive ratio HIGHER in UNIV than in LEGAL)"

    # ---- census (register-blind, reproduces the prereg's locked numbers) ----
    R["census"] = {
        "kull_tokens": len(u_tokens),
        "bad_tokens": len(p_tokens),
        "min_definite_proxy_tokens": len(p_min_proxy),
        "kull_retained_by_level": {lv: sum(1 for t in u_tokens if lv not in t[3])
                                   for lv in EX_ORDER},
    }
    expect = {"EX-0": 359, "EX-1": 238, "EX-2": 215, "EX-3": 200}
    if R["census"]["kull_retained_by_level"] != expect:
        raise SystemExit("FATAL: exclusion ladder does not reproduce the pre-registered "
                         "counts %r; got %r" % (expect, R["census"]["kull_retained_by_level"]))
    if len(u_tokens) != 359 or len(p_tokens) != 157:
        raise SystemExit("FATAL: pole census does not reproduce the pre-registered counts")

    # ---- ARM 1 unit tables -------------------------------------------------
    def arm1_counts(surahs, level, tuple_a, tuple_b):
        u, p = [], []
        for s in surahs:
            if tuple_b == "RT-B1":
                uu = sum(1 for t in u_tokens if t[0] == s and level not in t[3])
                pp = sum(1 for t in p_tokens if t[0] == s)
                if tuple_a == "RT-A2":
                    pp += sum(1 for t in p_min_proxy if t[0] == s)
            else:
                uu = len({(t[0], t[1]) for t in u_tokens if t[0] == s and level not in t[3]})
                pset = {(t[0], t[1]) for t in p_tokens if t[0] == s}
                if tuple_a == "RT-A2":
                    pset |= {(t[0], t[1]) for t in p_min_proxy if t[0] == s}
                pp = len(pset)
            u.append(uu)
            p.append(pp)
        return u, p

    # ---- ARM 2 blocks ------------------------------------------------------
    blocks, openers, n_nd = build_blocks(words, keys, idx, lemsets)
    vmax = collections.Counter()
    for (s, v, _w) in keys:
        vmax[s] = max(vmax[s], v)
    R["arm2_blocks"] = {
        "openers_universal": sum(1 for o in openers if o[2] == "UNIVERSAL"),
        "openers_community": sum(1 for o in openers if o[2] == "COMMUNITY"),
        "openers_non_delimiting": n_nd,
        "n_blocks": len(blocks),
        "verses_universal": sum(b["v_end"] - b["v_start"] + 1
                                for b in blocks if b["pole"] == "UNIVERSAL"),
        "verses_community": sum(b["v_end"] - b["v_start"] + 1
                                for b in blocks if b["pole"] == "COMMUNITY"),
    }
    # prereg 5.2 -- the five locked block integers, asserted against the data
    expect_arm2 = {"openers_universal": 23, "openers_community": 89,
                   "openers_non_delimiting": 38,
                   "verses_universal": 489, "verses_community": 939}
    got_arm2 = {k: R["arm2_blocks"][k] for k in expect_arm2}
    if got_arm2 != expect_arm2:
        raise SystemExit("FATAL: ARM 2 block rule does not reproduce the pre-registered "
                         "integers %r; got %r" % (expect_arm2, got_arm2))

    def block_counts(blks, level, tuple_a, tuple_b):
        u, p, chans = [], [], {"log_word_count": [], "verse_count": [], "mean_verse_length": []}
        wc = collections.Counter()
        for (s, v, _w) in keys:
            wc[(s, v)] += 1
        for b in blks:
            rng_v = range(b["v_start"], b["v_end"] + 1)
            vset = set(rng_v)
            if tuple_b == "RT-B1":
                uu = sum(1 for t in u_tokens
                         if t[0] == b["surah"] and t[1] in vset and level not in t[3])
                pp = sum(1 for t in p_tokens if t[0] == b["surah"] and t[1] in vset)
                if tuple_a == "RT-A2":
                    pp += sum(1 for t in p_min_proxy if t[0] == b["surah"] and t[1] in vset)
            else:
                uu = len({t[1] for t in u_tokens
                          if t[0] == b["surah"] and t[1] in vset and level not in t[3]})
                pset = {t[1] for t in p_tokens if t[0] == b["surah"] and t[1] in vset}
                if tuple_a == "RT-A2":
                    pset |= {t[1] for t in p_min_proxy
                             if t[0] == b["surah"] and t[1] in vset}
                pp = len(pset)
            nw = sum(wc[(b["surah"], v)] for v in rng_v)
            nv = len(vset)
            u.append(uu)
            p.append(pp)
            chans["log_word_count"].append(math.log(nw) if nw > 0 else 0.0)
            chans["verse_count"].append(float(nv))
            chans["mean_verse_length"].append(nw / nv if nv else 0.0)
        return u, p, chans

    # ---- THE LENGTH-CHANNEL BLOCK, COMPUTED AND STORED FIRST (prereg 6.3) --
    R["length_channels"] = {}
    for mp in ("MAP-1", "MAP-2"):
        labelled = [s for s in range(1, 115) if MAPPERS[mp](genre[s]) != "OTHER"]
        labels = [MAPPERS[mp](genre[s]) for s in labelled]
        ind = [1.0 if l == "LEGAL" else 0.0 for l in labels]
        chan_vals = {k: [metrics[s][k] for s in labelled]
                     for k in ("log_word_count", "verse_count", "mean_verse_length")}
        rhos = {k: spearman(chan_vals[k], ind) for k in chan_vals}
        dom = max(rhos, key=lambda k: abs(rhos[k]))
        R["length_channels"][mp] = {
            "n_labelled": len(labelled),
            "n_LEGAL": sum(1 for l in labels if l == "LEGAL"),
            "n_UNIV": sum(1 for l in labels if l == "UNIV"),
            "spearman_channel_vs_LEGAL_indicator": rhos,
            "DOMINANT_channel": dom,
            "median_word_count_LEGAL": sorted(metrics[s]["word_count"]
                                              for s in labelled
                                              if MAPPERS[mp](genre[s]) == "LEGAL")[
                sum(1 for s in labelled if MAPPERS[mp](genre[s]) == "LEGAL") // 2],
            "median_word_count_UNIV": sorted(metrics[s]["word_count"]
                                             for s in labelled
                                             if MAPPERS[mp](genre[s]) == "UNIV")[
                sum(1 for s in labelled if MAPPERS[mp](genre[s]) == "UNIV") // 2],
        }
    _u2, _p2, chans2 = block_counts(blocks, "EX-0", "RT-A1", "RT-B1")
    ind2 = [1.0 if b["pole"] == "COMMUNITY" else 0.0 for b in blocks]
    rhos2 = {k: spearman(chans2[k], ind2) for k in chans2}
    R["length_channels"]["ARM2"] = {
        "n_blocks": len(blocks),
        "spearman_channel_vs_COMMUNITY_indicator": rhos2,
        "DOMINANT_channel": max(rhos2, key=lambda k: abs(rhos2[k])),
    }

    # ---- the primary family (prereg 7.1) -----------------------------------
    rng = random.Random(SEED)
    R["cells"] = collections.OrderedDict()

    family = [
        ("cell-1", "ARM1", "MAP-1", "EX-2"),
        ("cell-2", "ARM1", "MAP-1", "EX-0"),
        ("cell-3", "ARM1", "MAP-2", "EX-2"),
        ("cell-4", "ARM1", "MAP-2", "EX-0"),
        ("cell-5", "ARM2", "BLOCKS", "EX-2"),
        ("cell-6", "ARM2", "BLOCKS", "EX-0"),
    ]

    cell_inputs = {}
    for name, arm, mp, lv in family:
        if arm == "ARM1":
            labelled = [s for s in range(1, 115) if MAPPERS[mp](genre[s]) != "OTHER"]
            labels = [MAPPERS[mp](genre[s]) for s in labelled]
            u, p = arm1_counts(labelled, lv, "RT-A1", "RT-B1")
            chan_vals = {k: [metrics[s][k] for s in labelled]
                         for k in ("log_word_count", "verse_count", "mean_verse_length")}
        else:
            labels = ["LEGAL" if b["pole"] == "COMMUNITY" else "UNIV" for b in blocks]
            u, p, chan_vals = block_counts(blocks, lv, "RT-A1", "RT-B1")
        rec = run_cell(rng, labels, u, p, chan_vals)
        rec["arm"] = arm
        rec["map"] = mp
        rec["exclusion"] = lv
        rec["tuples"] = ["RT-A1", "RT-B1"]
        rec["verdict"] = verdict_cell(rec)
        R["cells"][name] = rec
        cell_inputs[name] = (labels, u, p)

    R["FINDING_VERDICT"] = verdict_finding(R["cells"]["cell-1"]["verdict"],
                                           R["cells"]["cell-2"]["verdict"])

    # ---- MDE for every NULL cell (prereg 8) --------------------------------
    R["mde"] = {}
    for name, rec in R["cells"].items():
        if rec["verdict"] == "NULL":
            labels, u, p = cell_inputs[name]
            R["mde"][name] = mde_for_cell(u, p, labels)
            R["mde"][name]["reference"] = (
                "compare against this corpus's strongest surviving law, "
                "rate ratio 1.27-2.58 (muqattaat book-reference, 2026-08-07 correction)")
            m = R["mde"][name]["MDE_at_80pct_power"]
            R["mde"][name]["underpowered_vs_corpus_effect_scale"] = (
                True if m == "> 4.0" else bool(m > 2.58))

    # ---- robustness set, verdict-inert (prereg 7.4) -------------------------
    R["robustness"] = collections.OrderedDict()
    # prereg 6.2: ONE generator, created once, consumed in fixed order
    rng_rob = rng
    for mp in ("MAP-1", "MAP-2"):
        labelled = [s for s in range(1, 115) if MAPPERS[mp](genre[s]) != "OTHER"]
        labels = [MAPPERS[mp](genre[s]) for s in labelled]
        chan_vals = {k: [metrics[s][k] for s in labelled]
                     for k in ("log_word_count", "verse_count", "mean_verse_length")}
        for lv in EX_ORDER:
            for ta in ("RT-A1", "RT-A2"):
                for tb in ("RT-B1", "RT-B2"):
                    key = "ARM1|%s|%s|%s|%s" % (mp, lv, ta, tb)
                    if key in ("ARM1|MAP-1|EX-2|RT-A1|RT-B1", "ARM1|MAP-1|EX-0|RT-A1|RT-B1",
                               "ARM1|MAP-2|EX-2|RT-A1|RT-B1", "ARM1|MAP-2|EX-0|RT-A1|RT-B1"):
                        continue
                    u, p = arm1_counts(labelled, lv, ta, tb)
                    rec = run_cell(rng_rob, labels, u, p, chan_vals)
                    rec["verdict_inert"] = True
                    R["robustness"][key] = rec
    for w in ARM2_WINDOWS:
        wb = window_blocks(openers, vmax, w)
        labels = ["LEGAL" if b["pole"] == "COMMUNITY" else "UNIV" for b in wb]
        for lv in ("EX-0", "EX-2"):
            u, p, chan_vals = block_counts(wb, lv, "RT-A1", "RT-B1")
            rec = run_cell(rng_rob, labels, u, p, chan_vals)
            rec["verdict_inert"] = True
            rec["n_blocks"] = len(wb)
            R["robustness"]["ARM2|W%d|%s|RT-A1|RT-B1" % (w, lv)] = rec

    # ---- secondaries, verdict-inert (prereg 7.5) ---------------------------
    R["secondary_per_surah"] = {}
    rng_sec = rng
    for mp in ("MAP-1", "MAP-2"):
        labelled = [s for s in range(1, 115) if MAPPERS[mp](genre[s]) != "OTHER"]
        u, p = arm1_counts(labelled, "EX-2", "RT-A1", "RT-B1")
        keep = [i for i in range(len(labelled)) if u[i] + p[i] >= 5]
        ratios = [math.log((u[i] + 0.5) / (p[i] + 0.5)) for i in keep]
        labs = [MAPPERS[mp](genre[labelled[i]]) for i in keep]
        a = [ratios[i] for i in range(len(keep)) if labs[i] == "LEGAL"]
        b = [ratios[i] for i in range(len(keep)) if labs[i] == "UNIV"]
        greater = sum(1 for x in a for y in b if x > y)
        equal = sum(1 for x in a for y in b if x == y)

        # prereg 7.5 -- the same four channel-stratified permutation nulls,
        # statistic = mean(log-ratio | LEGAL) - mean(log-ratio | UNIV), locked negative
        def mean_diff(lv):
            xa = [ratios[i] for i in range(len(keep)) if lv[i] == "LEGAL"]
            xb = [ratios[i] for i in range(len(keep)) if lv[i] == "UNIV"]
            if not xa or not xb:
                return float("nan")
            return sum(xa) / len(xa) - sum(xb) / len(xb)
        chan_keep = {k: [metrics[labelled[i]][k] for i in keep]
                     for k in ("log_word_count", "verse_count", "mean_verse_length")}
        obs_md = mean_diff(labs)
        chan_ps = {}
        for c in CHANNELS:
            strata = None if c == "C0" else make_strata(chan_keep[CHANNEL_KEY[c]], N_BINS)
            n_le = 0
            for _ in range(N_PERM):
                perm = permute(rng_sec, labs, strata)
                if mean_diff(perm) <= obs_md:
                    n_le += 1
            chan_ps[c] = (n_le + 1) / (N_PERM + 1)

        R["secondary_per_surah"][mp] = {
            "n_eligible": len(keep), "n_LEGAL": len(a), "n_UNIV": len(b),
            "mean_log_ratio_LEGAL": (sum(a) / len(a)) if a else None,
            "mean_log_ratio_UNIV": (sum(b) / len(b)) if b else None,
            "mean_difference_LEGAL_minus_UNIV": obs_md,
            "mann_whitney_U_LEGAL_gt_UNIV": greater + 0.5 * equal,
            "channel_p": chan_ps,
            "p_worst_channel": max(chan_ps.values()),
            "note": "verdict-inert; underpowered by construction (prereg 7.5)",
        }
    R["secondary_density_FLAGGED"] = {
        "flag": "UNIT-DRIFT Screens A and B BOTH fire on this statistic. "
                "Reported for the reader; never a verdict input.",
    }
    for mp in ("MAP-1", "MAP-2"):
        labelled = [s for s in range(1, 115) if MAPPERS[mp](genre[s]) != "OTHER"]
        u, p = arm1_counts(labelled, "EX-2", "RT-A1", "RT-B1")
        d = {}
        for pole in ("LEGAL", "UNIV"):
            ii = [i for i, s in enumerate(labelled) if MAPPERS[mp](genre[s]) == pole]
            nw = sum(metrics[labelled[i]]["word_count"] for i in ii)
            d[pole] = {"kull_per_1000w": 1000.0 * sum(u[i] for i in ii) / nw,
                       "bad_per_1000w": 1000.0 * sum(p[i] for i in ii) / nw,
                       "words": nw}
        R["secondary_density_FLAGGED"][mp] = d

    # ---- write ------------------------------------------------------------
    manifest = {
        "finding_id": "H-NEW-3080",
        "title": "Quantifier scope (kull vs bad) and register",
        "run_utc": stamp,
        "prereg": {"path": PREREG, "sha256": prereg_sha},
        "script": {"path": "findings/phase-b-hypotheses/scripts/h-new-3080.py",
                   "sha256": sha256_file("findings/phase-b-hypotheses/scripts/h-new-3080.py")},
        "frozen_inputs": [{"path": p, "sha256": sha256_file(p)} for p in FROZEN_INPUTS],
        "classical_anchor_read": {
            "path": "data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt",
            "lines": "14254-14287", "nawv_from_locator_header": 45},
        "seed": SEED, "n_perm": N_PERM, "k_family": K_FAMILY,
        "alpha_bonferroni": ALPHA_BON,
        "python": sys.version.split()[0], "write_once": True,
    }
    with open(os.path.join(run_dir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
    with open(os.path.join(run_dir, "results.json"), "x", encoding="utf-8") as fh:
        json.dump(R, fh, indent=1, ensure_ascii=False)

    lines = []
    lines.append("H-NEW-3080 — quantifier scope and register — %s" % stamp)
    lines.append("prereg sha256 %s" % prereg_sha)
    lines.append("locked direction: LOR < 0 ; alpha_bon = %.7f (k=%d)" % (ALPHA_BON, K_FAMILY))
    lines.append("")
    lines.append("DOMINANT LENGTH CHANNEL (computed before any primary statistic):")
    for k, v in R["length_channels"].items():
        lines.append("  %-6s dominant=%s  rhos=%s" % (
            k, v["DOMINANT_channel"],
            v.get("spearman_channel_vs_LEGAL_indicator",
                  v.get("spearman_channel_vs_COMMUNITY_indicator"))))
    lines.append("")
    lines.append("PRIMARY FAMILY (p_cell = WORST channel):")
    for name, rec in R["cells"].items():
        lines.append("  %-7s %-5s %-6s %-5s  LOR=%+.4f  p_cell=%.5f [%s via %s]  ties=%.3f  -> %s"
                     % (name, rec["arm"], rec["map"], rec["exclusion"], rec["LOR_obs"],
                        rec["p_cell"], rec["p_cell_channel_argmax"], rec["p_cell_source"].split()[0],
                        rec["max_tie_fraction"], rec["verdict"]))
        lines.append("           channels: " + "  ".join(
            "%s=%.5f%s" % (c, rec["channels"][c]["p"],
                           "(DEGEN)" if rec["channels"][c]["degenerate"] else "")
            for c in CHANNELS))
        lines.append("           2x2: U_LEGAL=%d P_LEGAL=%d U_UNIV=%d P_UNIV=%d ; fisher=%.5f"
                     % (rec["table"]["U_LEGAL"], rec["table"]["P_LEGAL"],
                        rec["table"]["U_UNIV"], rec["table"]["P_UNIV"], rec["fisher_exact_p"]))
    lines.append("")
    for name, m in R["mde"].items():
        lines.append("  MDE %s = %s (80%% power, alpha=%.7f) ; underpowered_vs_corpus_scale=%s"
                     % (name, m["MDE_at_80pct_power"], ALPHA_BON,
                        m["underpowered_vs_corpus_effect_scale"]))
    lines.append("")
    lines.append("ROBUSTNESS SET (prereg 7.4 — uncorrected, VERDICT-INERT, all printed):")
    for key, rec in R["robustness"].items():
        lines.append("  %-34s LOR=%+.4f  p_worst=%.5f [%s]  ties=%.3f  fisher=%.5f  sign=%s"
                     % (key, rec["LOR_obs"], rec["p_cell"], rec["p_cell_channel_argmax"],
                        rec["max_tie_fraction"], rec["fisher_exact_p"],
                        "LOCKED" if rec["LOR_obs"] < 0 else "REVERSED"))
    lines.append("")
    lines.append("SECONDARY — per-surah, verdict-inert (prereg 7.5):")
    for mp, rec in R["secondary_per_surah"].items():
        lines.append("  %-6s n=%d (%d LEGAL / %d UNIV)  mean_diff=%+.4f  p_worst=%.5f  channels=%s"
                     % (mp, rec["n_eligible"], rec["n_LEGAL"], rec["n_UNIV"],
                        rec["mean_difference_LEGAL_minus_UNIV"], rec["p_worst_channel"],
                        {k: round(v, 5) for k, v in rec["channel_p"].items()}))
    lines.append("")
    lines.append("SECONDARY — density per 1000 words, UNIT-DRIFT FLAGGED, verdict-inert:")
    for mp in ("MAP-1", "MAP-2"):
        d = R["secondary_density_FLAGGED"][mp]
        lines.append("  %-6s LEGAL kull=%.3f bad=%.3f (%d w) | UNIV kull=%.3f bad=%.3f (%d w)"
                     % (mp, d["LEGAL"]["kull_per_1000w"], d["LEGAL"]["bad_per_1000w"],
                        d["LEGAL"]["words"], d["UNIV"]["kull_per_1000w"],
                        d["UNIV"]["bad_per_1000w"], d["UNIV"]["words"]))
    lines.append("")
    lines.append("FINDING VERDICT: %s" % R["FINDING_VERDICT"])
    with open(os.path.join(run_dir, "verdict.txt"), "x", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("\nrun dir: %s" % run_dir)


if __name__ == "__main__":
    main()
