#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2770 — Does H-NEW-125's chronology-content map survive a null that matches verse
length, or is it the denominator?

H-NEW-125 reports 11 of 15 content axes correlating with Nöldeke revelation rank. Nine of
the eleven survivors are densities of the form `100 * count / n_verses` — per VERSE — and
its own axis 2, mean_verse_length, correlates with Nöldeke rank at rho = +0.904 and rises
4.4x across the sequence. Its null free-shuffles Nöldeke rank across all 114 surahs, so it
cannot separate chronology from length. That is the H-NEW-740 shape.

  * The AXES and the CORRELATION are lifted verbatim from the frozen
    scripts/h_new_125_chronology_content.py as two SHA-checked source regions.
  * The PARTITION is lifted verbatim from findings/.../scripts/h-new-2680.py, same three
    fragments and same digests H-NEW-2720 and H-NEW-2730 verified.

Pre-reg : findings/phase-b-hypotheses/prereg-h-new-2770-chronology-content-length-nuisance.md
          SHA-256 embedded below, verified at runtime; mismatch -> SystemExit.
Seeds   : 20260509 primary / 20260519 replication.
Author  : Waiel Al-Shujaa.  Bismillāhi al-Raḥmāni al-Raḥīm.

stdlib only. No numpy.
"""
import hashlib
import json
import math
import os
import platform
import random
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # findings/phase-b-hypotheses
REPO = os.path.dirname(os.path.dirname(ROOT))     # repo root
CSVDIR = os.path.join(ROOT, "csv")

PREREG_REL = ("findings/phase-b-hypotheses/"
              "prereg-h-new-2770-chronology-content-length-nuisance.md")
PREREG_SHA256 = "da1c747d759a4da3ead662e263d38e8a4fe036057a10f041b524caf408894817"

SRC125_REL = "scripts/h_new_125_chronology_content.py"
SRC2680_REL = "findings/phase-b-hypotheses/scripts/h-new-2680.py"

FROZEN = {
    "quran-text/quran-no-tashkeel.json":
        "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    "data/revelation-order.csv":
        "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7",
    "data/morphology/quranic-corpus-morphology-0.4.txt":
        "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    "data/asma-al-husna.txt":
        "f607eb3882074d2c2011b17d0edc754fe0899a34ffb39ce0b8b27a8c80781220",
    "data/loanwords/jeffery-1938-loanwords.tsv":
        "d12ebac9d4bb62bbc1a8c810d7e2c069195e20113a77fb04505a84dfd4674b94",
    SRC125_REL:
        "57d8289c7754ebc920df10d748a98b830cced399a03053e31861177a1f91e941",
    SRC2680_REL:
        "57d6b214344ea81433e9f840524e6259953657fbf60e8fd54fdd8d2706b88497",
    "data/baseline-corpora/raw/bukhari-noquran.txt":
        "0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100",
    "data/baseline-corpora/raw/jahiz-hayawan.txt":
        "419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd",
}
POETRY_FILES = [
    "diwan-amr-ibn-kulthum.txt", "diwan-antara.txt", "diwan-harith.txt",
    "diwan-imru-al-qais.txt", "diwan-labid.txt", "diwan-tarafa.txt",
    "diwan-zuhayr.txt", "muallaqa-amr-bin-kulthum.txt", "muallaqa-antara.txt",
    "muallaqa-harith.txt", "muallaqa-imru-al-qais.txt", "muallaqa-labid.txt",
    "muallaqa-tarafa.txt", "muallaqa-zuhayr.txt",
]
POETRY_SHA = "f6c5525ddfa8d06ca974cbc937ad1f7f96839418e2eabdd3b94f8fce66fb983a"

SEED, SEED_REPL = 20260509, 20260519
N_PERM = 10000
BONF_K = 5
ALPHA_BON = 0.05 / BONF_K            # 0.01, prereg §7
ALPHA_AXIS = 0.05 / 15               # 0.003333, H-NEW-125's own per-axis bar
N_SURROGATE = 20                     # replicates per axis per corpus, prereg §4 A4
FREQ_TOL = 0.02                      # surrogate pooled-count match tolerance

# The eleven per-verse density axes (prereg §1). surah_length and mean_verse_length are the
# nuisance itself; muq_cardinality and rhyme_letter_diversity are not densities.
DENSITY_AXES = [
    "allah_density", "qul_density", "prophet_narrative_density", "legal_term_density",
    "eschatological_density", "book_reference_density", "oath_density",
    "divine_name_density", "personal_pronoun_density", "refrain_density",
    "loanword_density",
]
# published rho, for the instrument gate (prereg §3)
PUBLISHED_RHO = {
    "surah_length": 0.390, "mean_verse_length": 0.904, "muq_cardinality": 0.255,
    "allah_density": 0.852, "qul_density": 0.542, "prophet_narrative_density": 0.530,
    "legal_term_density": 0.704, "eschatological_density": 0.710,
    "book_reference_density": 0.574, "oath_density": -0.004,
    "divine_name_density": 0.897, "personal_pronoun_density": 0.496,
    "rhyme_letter_diversity": 0.179, "refrain_density": 0.002,
    "loanword_density": 0.833,
}
# density axes that pass Bonferroni-15 as published (prereg §6: S_pub = 9)
PUBLISHED_PASSING_DENSITIES = [
    "allah_density", "qul_density", "prophet_narrative_density", "legal_term_density",
    "eschatological_density", "book_reference_density", "divine_name_density",
    "personal_pronoun_density", "loanword_density",
]
S_PUB = len(PUBLISHED_PASSING_DENSITIES)


def P(rel):
    return os.path.join(REPO, rel)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def die(msg):
    raise SystemExit("[FATAL] " + msg)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ===========================================================================
# 0. LOCKS
# ===========================================================================
got = sha256_file(P(PREREG_REL))
if got != PREREG_SHA256:
    die("PRE-REG SHA MISMATCH\n  expected %s\n  got      %s" % (PREREG_SHA256, got))
log("[lock] pre-reg %s VERIFIED" % PREREG_SHA256[:16])
for rel, want in sorted(FROZEN.items()):
    g = sha256_file(P(rel))
    if g != want:
        die("FROZEN INPUT MISMATCH %s\n  expected %s\n  got %s" % (rel, want, g))
_h = hashlib.sha256()
for f in POETRY_FILES:
    with open(P("data/baseline-corpora/raw/" + f), "rb") as fh:
        _h.update(fh.read())
if _h.hexdigest() != POETRY_SHA:
    die("POETRY CORPUS SHA MISMATCH: %s" % _h.hexdigest())
log("[lock] %d frozen inputs + poetry corpus VERIFIED" % len(FROZEN))

# ===========================================================================
# 1. AXES + CORRELATION — LIFTED VERBATIM FROM H-NEW-125 (prereg §3)
# ===========================================================================
_S125 = open(P(SRC125_REL), encoding="utf-8").read()
_A = _S125.index("# ==========================================================\n# 0. Corpus load")
_B = _S125.index("# ==========================================================\n# 5. Spearman")
_R_AXES = _S125[_A:_B].rstrip() + "\n"
_C = _S125.index("def rank_array(values):")
_D = _S125.index("axes_list = [")
_R_STAT = _S125[_C:_D].rstrip() + "\n"

_EXPECT_125 = {"axes_region": "b9f6139658df1470", "stats_region": "bc91f8f4548c7ad4"}
for _n, _t in (("axes_region", _R_AXES), ("stats_region", _R_STAT)):
    _g = hashlib.sha256(_t.encode()).hexdigest()[:16]
    if _g != _EXPECT_125[_n]:
        die("MW-6 FAIL: 125 %s changed (sha %s, expected %s)" % (_n, _g, _EXPECT_125[_n]))

import csv as _csv
from pathlib import Path as _Path
_NS125 = {"__name__": "h125lift", "csv": _csv, "json": json, "math": math,
          "random": random, "re": re, "sys": sys, "Counter": Counter,
          "defaultdict": defaultdict, "Path": _Path, "ROOT": _Path(REPO),
          "SEED": 20260417}
random.seed(20260417)
exec(compile(_R_AXES, "<h-new-125:axes>", "exec"), _NS125)
exec(compile(_R_STAT, "<h-new-125:stats>", "exec"), _NS125)

spearman_rho = _NS125["spearman_rho"]
rank_array = _NS125["rank_array"]
SURAHS = _NS125["surahs"]
NOLDEKE_RANK = _NS125["noldeke_rank"]
NOLDEKE_PHASE = _NS125["noldeke_phase"]
SIDS = sorted(SURAHS)

_AXIS_INDEX = [
    (1, "surah_length"), (2, "mean_verse_length"), (3, "muq_cardinality"),
    (4, "allah_density"), (5, "qul_density"), (6, "prophet_narrative_density"),
    (7, "legal_term_density"), (8, "eschatological_density"),
    (9, "book_reference_density"), (10, "oath_density"), (11, "divine_name_density"),
    (12, "personal_pronoun_density"), (13, "rhyme_letter_diversity"),
    (14, "refrain_density"), (15, "loanword_density"),
]
AXES = {name: _NS125["axis_%d" % i] for i, name in _AXIS_INDEX}
# raw counts behind each density, needed to re-normalise (prereg §4 A1)
RAW_COUNTS = {
    "allah_density": None,  # filled below from the axis and n_verses
}
log("[MW-6] H-NEW-125 axes + Spearman lifted verbatim, 2 regions SHA-verified")

N_VERSES = {s: SURAHS[s]["n_verses"] for s in SIDS}
N_WORDS = {s: sum(v["wc"] for v in SURAHS[s]["verses"]) for s in SIDS}

# recover each density's integer numerator exactly: count = density * n_verses / 100
COUNTS = {}
for a in DENSITY_AXES:
    COUNTS[a] = {s: AXES[a][s] * N_VERSES[s] / 100.0 for s in SIDS}

# ===========================================================================
# 2. PARTITION — LIFTED VERBATIM FROM H-NEW-2680 (prereg §3)
# ===========================================================================
_S2680 = open(P(SRC2680_REL), encoding="utf-8").read()


def _grab2680(name):
    m = re.search(r"^def %s\(.*?(?=\n\ndef |\n\n# ===|\Z)" % name, _S2680, re.S | re.M)
    if not m:
        die("MW-6 FAIL: could not locate %s() in the frozen 2680 source" % name)
    return m.group(0).rstrip() + "\n"


_regex_block = re.search(r"AR_DIAC = .*?\nNON_AR = .*?\n", _S2680, re.S).group(0)
_FRAG = {"regex": _regex_block, "normalise_words": _grab2680("normalise_words"),
         "build_pseudo_corpus": _grab2680("build_pseudo_corpus")}
_EXPECT_2680 = {"regex": "2cd4d0ca289fd137", "normalise_words": "8e49ae080acc6335",
                "build_pseudo_corpus": "6931e0863f09a79c"}
for _k, _t in _FRAG.items():
    _g = hashlib.sha256(_t.encode()).hexdigest()[:16]
    if _g != _EXPECT_2680[_k]:
        die("MW-6 FAIL: 2680 fragment %r changed (sha %s, expected %s)"
            % (_k, _g, _EXPECT_2680[_k]))
_PART = {"re": re}
for _k in ("regex", "normalise_words", "build_pseudo_corpus"):
    exec(compile(_FRAG[_k], "<h-new-2680:%s>" % _k, "exec"), _PART)
normalise_words = _PART["normalise_words"]
_build_pseudo = _PART["build_pseudo_corpus"]
log("[MW-6] H-NEW-2680 partition lifted verbatim, 3 fragments SHA-verified "
    "(same digests as H-NEW-2720 and H-NEW-2730)")

QURAN_NT = json.load(open(P("quran-text/quran-no-tashkeel.json"), encoding="utf-8"))
NV_PROFILE = [len(s["verses"]) for s in QURAN_NT]
QVERSE_WLEN = [len(v["text"].split()) for s in QURAN_NT for v in s["verses"]]
_PART["QVERSE_WLEN"] = QVERSE_WLEN
STARTS = [0]
for n in NV_PROFILE[:-1]:
    STARTS.append(STARTS[-1] + n)


# ===========================================================================
# 3. STATISTICS
# ===========================================================================
def perm_p(x, y, seed, n_perm=None, strata=None):
    """Two-sided permutation p for Spearman(x, y), permuting y (optionally within strata).

    n_perm resolves from the module global at CALL time, not at def time — a default of
    `n_perm=N_PERM` would bind 10000 permanently and silently ignore the --smoke override.
    """
    if n_perm is None:
        n_perm = N_PERM
    obs = spearman_rho(x, y)
    rng = random.Random(seed)
    n = len(y)
    if strata is None:
        groups = [list(range(n))]
    else:
        g = defaultdict(list)
        for i, s in enumerate(strata):
            g[s].append(i)
        groups = list(g.values())
    ge = 0
    yy = list(y)
    for _ in range(n_perm):
        for idx in groups:
            vals = [yy[i] for i in idx]
            rng.shuffle(vals)
            for i, v in zip(idx, vals):
                yy[i] = v
        if abs(spearman_rho(x, yy)) >= abs(obs) - 1e-15:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)


def quintiles(values, k=5):
    """Stratum id per element, by k-quantile of `values` (ties -> same rank ordering)."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    out = [0] * len(values)
    per = len(values) / k
    for pos, i in enumerate(order):
        out[i] = min(k - 1, int(pos / per))
    return out


def partial_rho(x, y, z):
    """Spearman partial correlation of x and y controlling z (rank-level residuals)."""
    rxy, rxz, ryz = spearman_rho(x, y), spearman_rho(x, z), spearman_rho(y, z)
    d = math.sqrt(max(1e-15, (1 - rxz ** 2) * (1 - ryz ** 2)))
    return (rxy - rxz * ryz) / d


# ===========================================================================
# 4. INSTRUMENT GATE (prereg §3)
# ===========================================================================
NOLD = [NOLDEKE_RANK[s] for s in SIDS]
MVL = [AXES["mean_verse_length"][s] for s in SIDS]
NW = [N_WORDS[s] for s in SIDS]
NVv = [N_VERSES[s] for s in SIDS]

gate_rows, gate_bad = [], []
for name in PUBLISHED_RHO:
    r = spearman_rho([AXES[name][s] for s in SIDS], NOLD)
    ok = abs(r - PUBLISHED_RHO[name]) <= 0.005
    gate_rows.append({"axis": name, "reproduced": round(r, 4),
                      "published": PUBLISHED_RHO[name], "ok": ok})
    if not ok:
        gate_bad.append(name)
if gate_bad:
    die("INSTRUMENT GATE FAILED on %s (prereg §3)" % gate_bad)
log("[gate] all 15 published rho reproduced to within 0.005")


# ===========================================================================
# 5. ARMS
# ===========================================================================
def run_cell(seed):
    log("\n" + "=" * 76)
    log("CELL seed=%d" % seed)
    log("=" * 76)
    C = {"seed": seed}

    # ---- H2: the nuisance ranking -------------------------------------
    r1, p1 = perm_p(MVL, NOLD, seed)
    r2 = spearman_rho(NW, NOLD)
    r3 = spearman_rho(NVv, NOLD)
    C["H2"] = {"rho_N1_mean_verse_length": round(r1, 4), "p": round(p1, 6),
               "rho_N2_surah_words": round(r2, 4), "rho_N3_verse_count": round(r3, 4),
               "ordering_ok": r1 > r2 > r3 > 0,
               "PASS": (r1 > r2 > r3 > 0) and p1 < ALPHA_BON}
    log("  H2 nuisance ranking: MVL %+0.4f > words %+0.4f > verses %+0.4f -> %s"
        % (r1, r2, r3, C["H2"]["PASS"]))

    # ---- per-axis table: published, per-word, stratified, partial ------
    strata_mvl = quintiles(MVL)
    strata_nw = quintiles(NW)
    strata_nv = quintiles(NVv)
    rows = []
    for name in DENSITY_AXES:
        y_pv = [AXES[name][s] for s in SIDS]
        y_pw = [100.0 * COUNTS[name][s] / max(N_WORDS[s], 1) for s in SIDS]
        r_pv, p_pv = perm_p(y_pv, NOLD, seed)
        r_pw, p_pw = perm_p(y_pw, NOLD, seed)
        _, p_pv_st = perm_p(y_pv, NOLD, seed, strata=strata_mvl)
        _, p_pw_st = perm_p(y_pw, NOLD, seed, strata=strata_mvl)
        _, p_pv_nw = perm_p(y_pv, NOLD, seed, strata=strata_nw)
        _, p_pv_nv = perm_p(y_pv, NOLD, seed, strata=strata_nv)
        rows.append({
            "axis": name,
            "rho_perverse": round(r_pv, 4), "p_perverse": round(p_pv, 6),
            "rho_perword": round(r_pw, 4), "p_perword": round(p_pw, 6),
            "delta_rho": round(r_pw - r_pv, 4),
            "p_perverse_mvl_stratified": round(p_pv_st, 6),
            "p_perword_mvl_stratified": round(p_pw_st, 6),
            "p_perverse_words_stratified": round(p_pv_nw, 6),
            "p_perverse_verses_stratified": round(p_pv_nv, 6),
            "rho_vs_MVL": round(spearman_rho(y_pv, MVL), 4),
            "partial_rho_ctrl_logMVL": round(
                partial_rho(y_pv, NOLD, [math.log(v) for v in MVL]), 4),
            "partial_rho_ctrl_logwords": round(
                partial_rho(y_pv, NOLD, [math.log(v) for v in NW]), 4),
            "published_passing": name in PUBLISHED_PASSING_DENSITIES,
        })
    C["axes"] = rows

    n_pv = sum(1 for r in rows if r["p_perverse"] < ALPHA_AXIS)
    n_pw = sum(1 for r in rows if r["p_perword"] < ALPHA_AXIS)
    n_st = sum(1 for r in rows if r["p_perverse_mvl_stratified"] < ALPHA_AXIS)
    n_pw_st = sum(1 for r in rows if r["p_perword_mvl_stratified"] < ALPHA_AXIS)
    n_st_nw = sum(1 for r in rows if r["p_perverse_words_stratified"] < ALPHA_AXIS)
    n_st_nv = sum(1 for r in rows if r["p_perverse_verses_stratified"] < ALPHA_AXIS)
    C["counts"] = {"S_pub_declared": S_PUB, "per_verse_reproduced": n_pv,
                   "per_word": n_pw, "per_verse_MVL_stratified": n_st,
                   "per_word_MVL_stratified": n_pw_st,
                   "per_verse_words_stratified": n_st_nw,
                   "per_verse_verses_stratified": n_st_nv}
    log("  surviving density axes (of 11): published-form %d | per-WORD %d | "
        "MVL-stratified %d | per-word+stratified %d" % (n_pv, n_pw, n_st, n_pw_st))
    for r in rows:
        log("    %-28s rho %+0.4f -> perword %+0.4f (D %+0.4f)  p_strat %.4f  "
            "partial(logMVL) %+0.4f" % (r["axis"], r["rho_perverse"], r["rho_perword"],
                                        r["delta_rho"], r["p_perverse_mvl_stratified"],
                                        r["partial_rho_ctrl_logMVL"]))

    # ---- A4: genre control / mechanism test ---------------------------
    C["A4"] = run_genre(seed)
    return C


def load_words(rel):
    return normalise_words(open(P(rel), encoding="utf-8").read())


def load_poetry():
    txt = "".join(open(P("data/baseline-corpora/raw/" + f), encoding="utf-8").read()
                  for f in POETRY_FILES)
    return normalise_words(txt)


def run_genre(seed):
    """Frequency-matched surrogate vocabulary in matched partitions (prereg §4 A4)."""
    need = sum(QVERSE_WLEN)
    corpora = {}
    for label, words in (("bukhari", load_words("data/baseline-corpora/raw/bukhari-noquran.txt")),
                         ("jahiz", load_words("data/baseline-corpora/raw/jahiz-hayawan.txt")),
                         ("poetry", load_poetry())):
        if len(words) < need:
            log("  A4 %s: insufficient words (%d < %d) — SKIPPED" % (label, len(words), need))
            continue
        units, err = _build_pseudo(words)
        if err:
            die("A4 partition failed for %s: %s" % (label, err))
        groups = [units[STARTS[i]:STARTS[i] + NV_PROFILE[i]] for i in range(114)]
        nv = [len(g) for g in groups]
        nw = [sum(len(u) for u in g) for g in groups]
        mvl = [nw[i] / max(nv[i], 1) for i in range(114)]
        types = Counter(w for u in units for w in u)
        corpora[label] = {"groups": groups, "nv": nv, "nw": nw, "mvl": mvl, "types": types}
        log("  A4 %s: 114 pseudo-surahs, %d words, rho(pseudo-MVL, index) = %+0.4f"
            % (label, len(words), spearman_rho(mvl, list(range(114)))))

    quran_rho_vs_mvl = {a: spearman_rho([AXES[a][s] for s in SIDS], MVL)
                        for a in PUBLISHED_PASSING_DENSITIES}
    median_quran = sorted(quran_rho_vs_mvl.values())[len(quran_rho_vs_mvl) // 2]

    out = {"quran_rho_vs_MVL": {k: round(v, 4) for k, v in quran_rho_vs_mvl.items()},
           "quran_median_rho_vs_MVL": round(median_quran, 4), "corpora": {}}
    for label, C in corpora.items():
        types = C["types"]
        pool = [w for w, c in types.items() if c >= 1]
        per_axis = {}
        for a in PUBLISHED_PASSING_DENSITIES:
            target = int(round(sum(COUNTS[a][s] for s in SIDS)))
            reps = []
            for r in range(N_SURROGATE):
                rng = random.Random(seed * 1000 + r + abs(hash(a + label)) % 997)
                chosen, tot = set(), 0
                order = pool[:]
                rng.shuffle(order)
                for w in order:
                    if tot >= target * (1 - FREQ_TOL):
                        break
                    if tot + types[w] > target * (1 + FREQ_TOL):
                        continue
                    chosen.add(w)
                    tot += types[w]
                if tot < target * (1 - FREQ_TOL) or not chosen:
                    continue
                dens = [100.0 * sum(1 for u in C["groups"][i] for w in u if w in chosen)
                        / max(C["nv"][i], 1) for i in range(114)]
                reps.append({"rho_vs_mvl": spearman_rho(dens, C["mvl"]),
                             "rho_vs_index": spearman_rho(dens, list(range(114))),
                             "matched_tokens": tot})
            if reps:
                rv = sorted(x["rho_vs_mvl"] for x in reps)
                ri = sorted(x["rho_vs_index"] for x in reps)
                per_axis[a] = {"n_reps": len(reps), "target_tokens": target,
                               "median_rho_vs_MVL": round(rv[len(rv) // 2], 4),
                               "min_rho_vs_MVL": round(rv[0], 4),
                               "max_rho_vs_MVL": round(rv[-1], 4),
                               "median_rho_vs_index": round(ri[len(ri) // 2], 4),
                               "quran_rho_vs_MVL": round(quran_rho_vs_mvl[a], 4)}
        meds = sorted(v["median_rho_vs_MVL"] for v in per_axis.values())
        corpus_median = meds[len(meds) // 2] if meds else None
        out["corpora"][label] = {
            "per_axis": per_axis, "corpus_median_rho_vs_MVL": corpus_median,
            "ratio_to_quran_median": (round(corpus_median / median_quran, 4)
                                      if corpus_median is not None and median_quran else None),
            "reaches_half_of_quran": (corpus_median is not None
                                      and corpus_median >= 0.5 * median_quran),
        }
        log("  A4 %-8s surrogate median rho vs pseudo-MVL = %s  (Qurʾān median %+0.4f) "
            "-> reaches half: %s" % (label, corpus_median, median_quran,
                                     out["corpora"][label]["reaches_half_of_quran"]))
    return out


# ===========================================================================
# 6. VERDICT — literal transcription of prereg §6
# ===========================================================================
def label_A1(cell):
    n = cell["counts"]["per_word"]
    if n <= S_PUB // 2:
        return "RENORM-COLLAPSES"
    if n < S_PUB:
        return "RENORM-ATTENUATES"
    if n == S_PUB:
        return "RENORM-NEUTRAL"
    return "RENORM-STRENGTHENS"


def label_A2(cell):
    n = cell["counts"]["per_verse_MVL_stratified"]
    if n <= S_PUB // 2:
        return "STRATIFIED-COLLAPSES"
    if n < S_PUB:
        return "STRATIFIED-ATTENUATES"
    if n == S_PUB:
        return "STRATIFIED-NEUTRAL"
    return "STRATIFIED-STRENGTHENS"


def label_A4(cell):
    n = sum(1 for v in cell["A4"]["corpora"].values() if v["reaches_half_of_quran"])
    if n >= 2:
        return "MECHANISM-GENERIC"
    if n == 0:
        return "MECHANISM-CORPUS-SPECIFIC"
    return "MECHANISM-MIXED"


def overall(a1, a2, a4):
    if a1 == "RENORM-COLLAPSES" or a2 == "STRATIFIED-COLLAPSES":
        return "DOES-NOT-DISCRIMINATE"
    if (a4 == "MECHANISM-GENERIC"
            and (a1 == "RENORM-ATTENUATES" or a2 == "STRATIFIED-ATTENUATES")):
        return "GENRE-SHARED-BUT-LARGER"
    if (a1 in ("RENORM-NEUTRAL", "RENORM-STRENGTHENS")
            and a2 in ("STRATIFIED-NEUTRAL", "STRATIFIED-STRENGTHENS")
            and a4 != "MECHANISM-GENERIC"):
        return "DISCRIMINATES"
    return "ATTENUATED"


# ===========================================================================
# 7. MAIN
# ===========================================================================
def main():
    t0 = time.time()
    smoke = "--smoke" in sys.argv
    global N_PERM, N_SURROGATE
    if smoke:
        N_PERM, N_SURROGATE = 200, 3
        log("[SMOKE] reduced parameters — calibration only, not a result")

    cells = {"PRIMARY": run_cell(SEED), "REPLICATION": run_cell(SEED_REPL)}
    V = {}
    for k, c in cells.items():
        a1, a2, a4 = label_A1(c), label_A2(c), label_A4(c)
        V[k] = {"A1": a1, "A2": a2, "A4": a4, "H2": c["H2"]["PASS"],
                "overall": overall(a1, a2, a4)}
    seed_fragile = any(V["PRIMARY"][x] != V["REPLICATION"][x] for x in ("A1", "A2", "A4"))
    VERDICT = ("SEED-FRAGILE " if seed_fragile else "") + V["PRIMARY"]["overall"]

    log("\n" + "=" * 76)
    log("VERDICT SUMMARY (rules transcribed from prereg §6)")
    log("=" * 76)
    for k in cells:
        log("  %-12s A1=%-20s A2=%-24s A4=%-26s -> %s"
            % (k, V[k]["A1"], V[k]["A2"], V[k]["A4"], V[k]["overall"]))
    log("  seed_fragile: %s" % seed_fragile)
    log("  OVERALL     : %s" % VERDICT)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    RUN = os.path.join(ROOT, "runs", "h-new-2770-SMOKE" if smoke else "h-new-2770", stamp)
    if os.path.exists(RUN):
        die("run dir exists (immutability): %s" % RUN)
    os.makedirs(RUN)

    out = {
        "id": "H-NEW-2770",
        "title": "Does H-NEW-125's chronology-content map survive a null matching verse length?",
        "target_claim": "H-NEW-125", "method_parent": ["H-NEW-2680", "H-NEW-2760"],
        "defect_diagnosed": "null does not match the nuisance parameter (H-NEW-740 shape)",
        "prereg_sha256": PREREG_SHA256,
        "seeds": {"primary": SEED, "replication": SEED_REPL},
        "n_perm": N_PERM, "bonferroni_k": BONF_K, "alpha_bonferroni": ALPHA_BON,
        "alpha_per_axis_bonferroni15": ALPHA_AXIS,
        "S_pub_density_axes_passing": S_PUB,
        "instrument_gate": gate_rows,
        "lifted": {"h_new_125": _EXPECT_125, "h_new_2680": _EXPECT_2680},
        "cells": cells, "verdicts": V, "seed_fragile": seed_fragile,
        "verdict": VERDICT, "wall_seconds": round(time.time() - t0, 1),
    }
    json.dump(out, open(os.path.join(RUN, "result.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"id": "H-NEW-2770", "utc": stamp,
               "script": "findings/phase-b-hypotheses/scripts/h-new-2770.py",
               "script_sha256": sha256_file(os.path.abspath(__file__)),
               "prereg": PREREG_REL, "prereg_sha256": PREREG_SHA256,
               "inputs_sha256": dict(sorted(FROZEN.items())),
               "poetry_corpus_sha256": POETRY_SHA,
               "lifted_fragments": {"h_new_125": _EXPECT_125, "h_new_2680": _EXPECT_2680},
               "python": platform.python_version(), "seeds": [SEED, SEED_REPL],
               "n_perm": N_PERM, "verdict": VERDICT,
               "immutability": "Immutable. Never delete or overwrite, per prereg §8."},
              open(os.path.join(RUN, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    if not smoke:
        json.dump(out, open(os.path.join(CSVDIR, "h-new-2770.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
    log("\n[run] %s" % os.path.relpath(RUN, REPO))
    log("[wall] %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
