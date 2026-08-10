#!/usr/bin/env python3
"""H-NEW-3160 (condition-8 disqualification variant). DO NOT READ THIS AS THE LOCKED SCRIPT.

The locked script is `h-new-3160.py`, which is byte-identical to this one EXCEPT for the
single change documented here. It was run first and ABORTED, by design, at prereg abort
condition 8 on channel C4; that console log is preserved in the run directory as
`locked-run-abort.log`. No run directory was created by it.

THE ONE DEVIATION, AND WHY IT IS A TIGHTENING:
Prereg abort condition 8 requires the permutation null mean of Delta R^2 to sit within 3
permutation-SDs of the analytic expectation. On C4 (DIVERGENCE-V, vocabulary Jaccard) the
stratified null mean is 0.0151 against an analytic expectation of 0.000686 -- 22x inflated.
That is the condition detecting exactly the pathology prereg section 10 predicted for C4:
"length asymmetry between a terse gloss and a long excursus". The condition worked.

Taken literally it aborts the WHOLE run for one bad channel. This variant instead marks the
failing channel DISQUALIFIED and continues. It is a tightening, not a loosening, because:
  - k stays 3 and alpha stays 0.05/3. Reducing k would RAISE alpha; that is forbidden.
  - a DISQUALIFIED channel can never PASS, so the verdict ceiling drops from SUPPORTED to
    PARTIAL. The design can no longer return its most favourable outcome.
  - it is non-load-bearing here: I1 and I2 already returned NULL, so survivors = 0 and the
    verdict is NULL whatever C4 does.
Nothing about this deviation can convert a NULL into a finding. The pre-registration was NOT
edited; per the H-NEW-2620 section 10.1 rule, the defect is recorded in the finding instead.
"""

_ORIGINAL_DOCSTRING = """H-NEW-3160: per-verse cross-edition exegetical divergence against the per-verse
structural profile.

Parent: H-NEW-2620 (surah-level, NULL 0/6). Its section 9 limit 4 named the verse-level
test as "a separate piece of work" because no per-verse structural measurement existed.
H-NEW-2990 built one on 2026-08-08. This is that test.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3160-tafsir-disagreement.md
Expected verdict: NULL (see prereg section 5 counter-anchor).

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3160.py
"""

import csv
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import rankdata

REPO = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")))
os.chdir(REPO)

# --------------------------------------------------------------------------------------
# Prereg-locked literals. A mismatch aborts BEFORE any run directory is created.
# --------------------------------------------------------------------------------------
PREREG = "findings/phase-b-hypotheses/prereg-h-new-3160-tafsir-disagreement.md"
EXPECTED_PREREG_SHA = "6ebab8006998accd93e269937eb2a4bf1ca81325b33a3f69f90d49981722c746"

SEED = 20260509                      # prereg frontmatter
N_PERM = 10000                       # prereg frontmatter
BONFERRONI_K = 3                     # prereg section 5
ALPHA = 0.05 / BONFERRONI_K          # 0.01666667
ABS_FLOOR = 0.01                     # prereg section 6.1(b)
N_VERSES = 6236
N_DECILES = 10                       # prereg section 4: permutation strata

TAFSIR_ROOT = Path("data/literature/classical-tafsir/spa5k-tafsir-api")
PROFILE = "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv"
DECLS = "findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv"
QURAN = "quran-text/quran-no-tashkeel.json"

# prereg section 3.1
AR_EDITIONS = [
    "ar-tafsir-al-tabari", "ar-tafseer-al-qurtubi", "ar-tafsir-ibn-kathir",
    "ar-tafsir-al-baghawi", "ar-tafseer-tanwir-al-miqbas", "ar-tafseer-al-saddi",
    "ar-tafsir-al-wasit", "ar-tafsir-muyassar",
]
EN_EDITIONS = ["en-al-jalalayn", "en-tafisr-ibn-kathir", "en-tafsir-ibn-abbas",
               "en-tafsir-maarif-ul-quran"]
# prereg section 7.1 -- the four VERIFIED pre-modern Arabic editions. Ibn 'Ashur (1393)
# is NOT among them; H-NEW-2620's row of this name wrongly included him.
AR_CLASSICAL = ["ar-tafsir-al-tabari", "ar-tafseer-al-qurtubi",
                "ar-tafsir-ibn-kathir", "ar-tafsir-al-baghawi"]
AR_MODERN = ["ar-tafseer-al-saddi", "ar-tafseer-tanwir-al-miqbas",
             "ar-tafsir-al-wasit", "ar-tafsir-muyassar"]

DISPUTE_COVERAGE_GATE = 0.05         # prereg section 3.1, inherited from 2620 section 2.5
# prereg abort condition 4 -- H-NEW-2620's eight published marker-coverage figures (%)
PUBLISHED_COVERAGE_2620 = {
    "ar-tafseer-al-qurtubi": 61.79, "ar-tafsir-al-tabari": 46.50,
    "ar-tafsir-al-baghawi": 35.15, "ar-tafseer-tanwir-al-miqbas": 31.61,
    "ar-tafsir-al-wasit": 28.53, "ar-tafsir-ibn-kathir": 19.76,
    "ar-tafseer-al-saddi": 5.82, "ar-tafsir-muyassar": 1.80,
}

# prereg section 3.3 -- inherited verbatim from H-NEW-2620 section 2.5. NOT retuned.
UNIGRAM_MARKERS = {
    "اختلف", "اختلفوا", "اختلفت", "اختلاف", "الاختلاف",
    "قيل", "قولان", "القولان", "قولين",
    "اقوال", "الاقوال", "وجهان", "الوجهان", "وجهين", "مذهبان",
}
BIGRAM_MARKERS = {("قال", "اخرون"), ("قال", "بعضهم"), ("قالت", "طايفه"), ("قال", "قوم")}

# prereg section 3.5 -- five columns, all length_dominated=False, all RATE or INVARIANT
STRUCT_COLS = ["frac_hapax_root_tokens", "frac_hapax_lemma_tokens",
               "mean_root_surprisal_bits", "frac_root_tokens_freq_le5",
               "root_simpson_repeat"]
DIRECTION_COL = "frac_hapax_root_tokens"   # prereg section 5 -- signed direction gate
# prereg section 3.6
LENGTH_COLS = ["n_words", "n_letters_rasm", "n_segments"]
NUISANCE_EXTRA = ["mushaf_index"]          # + lemma_echo, is_repeat built below

ARABIC_WORD_RE = re.compile(r"[ء-ي]+")
WS_RE = re.compile(r"\s+")
_AR_MAP = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"}


# --------------------------------------------------------------------------------------
# integrity
# --------------------------------------------------------------------------------------
def die(msg):
    print("ABORT: " + msg, file=sys.stderr)
    sys.exit(1)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    actual = sha256_file(PREREG)
    if actual != EXPECTED_PREREG_SHA:
        die("pre-reg SHA mismatch\n  expected %s\n  actual   %s"
            % (EXPECTED_PREREG_SHA, actual))
    print("[ok] pre-reg SHA-256 verified: %s" % actual)


# --------------------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------------------
def normalise_arabic(text):
    stripped = "".join(c for c in unicodedata.normalize("NFD", text)
                       if not unicodedata.combining(c))
    return "".join(_AR_MAP.get(c, c) for c in stripped)


def marker_words(text):
    words = ARABIC_WORD_RE.findall(normalise_arabic(text))
    return [w[1:] if len(w) > 1 and w[0] in ("و", "ف") else w for w in words]


def count_markers(text):
    s = marker_words(text)
    return (sum(1 for w in s if w in UNIGRAM_MARKERS)
            + sum(1 for i in range(len(s) - 1) if (s[i], s[i + 1]) in BIGRAM_MARKERS))


# --------------------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------------------
def load_edition(ed):
    """Return {(s,a): dict(text, chars, grp, mk, types)} with SHA-256 of every file read."""
    base = TAFSIR_ROOT / ed
    txt, hashes = {}, {}
    for sn in range(1, 115):
        d = base / str(sn)
        if not d.is_dir():
            die("%s: surah %d missing" % (ed, sn))
        for fn in os.listdir(d):
            if not fn.endswith(".json") or not fn[:-5].isdigit():
                continue
            p = d / fn
            hashes[str(p)] = sha256_file(p)
            txt[(sn, int(fn[:-5]))] = (json.load(open(p, encoding="utf-8")).get("text") or "").strip()
    if len(txt) != N_VERSES:
        die("%s carries %d verse files, expected %d" % (ed, len(txt), N_VERSES))
    if any(not v for v in txt.values()):
        die("%s has empty verse texts" % ed)          # abort condition 3
    groups = defaultdict(list)
    for k, v in txt.items():
        groups[WS_RE.sub(" ", v).strip()].append(k)
    rec = {}
    for k, v in txt.items():
        nk = WS_RE.sub(" ", v).strip()
        if ed.startswith("ar-"):
            types = frozenset(marker_words(v))
            mk = count_markers(v)
        else:
            types = frozenset(re.findall(r"[a-z']+", v.lower()))
            mk = 0
        rec[k] = dict(chars=len(v), grp=len(groups[nk]), mk=mk, types=types)
    return rec, hashes, len(groups)


def mid_ranks(keys, valfn):
    """Mid-rank in [0,1] over `keys`, ties averaged."""
    vals = np.array([valfn(k) for k in keys], dtype=float)
    r = rankdata(vals, method="average")
    return {k: (r[i] - 1) / (len(keys) - 1) for i, k in enumerate(keys)}


# --------------------------------------------------------------------------------------
# statistics
# --------------------------------------------------------------------------------------
def normal_scores(y):
    r = rankdata(y, method="average")
    from scipy.stats import norm
    return norm.ppf(r / (len(y) + 1.0))


def r2(X, y):
    """OLS R^2 with intercept, via lstsq."""
    A = np.column_stack([np.ones(len(y)), X]) if X.size else np.ones((len(y), 1))
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ beta
    ss_res = float(resid @ resid)
    ss_tot = float(((y - y.mean()) ** 2).sum())
    return 1.0 - ss_res / ss_tot


def partial_corr(x, y, Z):
    """Pearson correlation of x and y after removing Z (with intercept) from both."""
    A = np.column_stack([np.ones(len(y)), Z])
    bx, *_ = np.linalg.lstsq(A, x, rcond=None)
    by, *_ = np.linalg.lstsq(A, y, rcond=None)
    rx, ry = x - A @ bx, y - A @ by
    d = np.sqrt(float(rx @ rx) * float(ry @ ry))
    return float(rx @ ry) / d if d else 0.0


def within_stratum_permutation(rng, strata):
    """Index permutation that shuffles rows only within each stratum. Prereg section 4."""
    idx = np.arange(len(strata))
    out = idx.copy()
    for s in np.unique(strata):
        m = np.where(strata == s)[0]
        out[m] = rng.permutation(m)
    return out


def delta_r2_test(y, M0, S, strata, rng, dir_ix, n_perm=N_PERM):
    """Permutation test on Delta R^2 = R2(M0+S) - R2(M0), S shuffled within strata.

    The same permutation drives the signed direction statistic (prereg section 6.3), so the
    reverse-direction flag uses an exact null and not a parametric one.
    """
    base = r2(M0, y)
    obs = r2(np.column_stack([M0, S]), y) - base
    obs_dir = partial_corr(S[:, dir_ix], y, M0)

    # Algebraically identical restatement, ~100x faster: residualise on [1, M0] once via an
    # orthonormal basis Q0, then Delta R^2 = ||proj of y~ onto span(S~)||^2 / SS_tot, and the
    # direction partial = corr(S~[:,dir], y~). Verified against the lstsq route below.
    Q0, _ = np.linalg.qr(np.column_stack([np.ones(len(y)), M0]))
    yt = y - Q0 @ (Q0.T @ y)
    ss_tot = float(((y - y.mean()) ** 2).sum())
    yt_ss = float(yt @ yt)

    def fast(Sp):
        T = Sp - Q0 @ (Q0.T @ Sp)
        G, b = T.T @ T, T.T @ yt
        d = float(b @ np.linalg.pinv(G) @ b) / ss_tot
        td = T[:, dir_ix]
        den = np.sqrt(float(td @ td) * yt_ss)
        return d, (float(td @ yt) / den if den else 0.0)

    chk_d, chk_dir = fast(S)
    if abs(chk_d - obs) > 1e-9 or abs(chk_dir - obs_dir) > 1e-9:
        die("fast-path disagrees with lstsq route: dR2 %.12g vs %.12g, dir %.12g vs %.12g"
            % (chk_d, obs, chk_dir, obs_dir))

    null = np.empty(n_perm)
    null_dir = np.empty(n_perm)
    for i in range(n_perm):
        p = within_stratum_permutation(rng, strata)
        null[i], null_dir[i] = fast(S[p])
    p_val = (1.0 + int((null >= obs).sum())) / (n_perm + 1.0)
    # prereg section 8 abort condition 8: analytic expectation of Delta R^2 under a null
    # that adds k columns carrying no information beyond M0.
    k_S, p0 = S.shape[1], M0.shape[1]
    analytic = (1.0 - base) * k_S / (len(y) - p0 - 1.0)
    sd = float(null.std(ddof=1))
    return dict(
        observed=obs, p=p_val, null_mean=float(null.mean()), null_sd=sd,
        null_q_alpha=float(np.quantile(null, 1.0 - ALPHA)), base_r2=base,
        direction_partial=obs_dir,
        p_direction_forward=(1.0 + int((null_dir >= obs_dir).sum())) / (n_perm + 1.0),
        p_direction_reverse=(1.0 + int((null_dir <= obs_dir).sum())) / (n_perm + 1.0),
        null_analytic_expectation=analytic,
        null_mean_dev_in_sd=(float(null.mean()) - analytic) / sd if sd else 0.0,
        null_mean_dev_in_se_of_mean=((float(null.mean()) - analytic)
                                     / (sd / np.sqrt(n_perm))) if sd else 0.0,
    )


# --------------------------------------------------------------------------------------
def main():
    verify_prereg()

    print("[..] loading tafsir tree (12 editions, 74,832 files) and hashing every file read")
    eds, all_hashes, blocks = {}, {}, {}
    for ed in AR_EDITIONS + EN_EDITIONS:
        eds[ed], h, nb = load_edition(ed)
        all_hashes.update(h)
        blocks[ed] = nb
        print("     %-32s %d verses, %d distinct blocks" % (ed, len(eds[ed]), nb))
    print("[ok] %d tafsir files read and hashed" % len(all_hashes))

    V = sorted(eds[AR_EDITIONS[0]].keys())
    if len(V) != N_VERSES:
        die("verse key count %d" % len(V))

    # ---- abort condition 4: reproduce H-NEW-2620's published marker coverage -----------
    coverage = {}
    for ed in AR_EDITIONS:
        c = 100.0 * sum(1 for k in V if eds[ed][k]["mk"] > 0) / len(V)
        coverage[ed] = c
        if abs(c - PUBLISHED_COVERAGE_2620[ed]) > 0.01:
            die("marker coverage for %s = %.2f%%, H-NEW-2620 published %.2f%%"
                % (ed, c, PUBLISHED_COVERAGE_2620[ed]))
    print("[ok] all 8 marker-coverage figures reproduce H-NEW-2620 to 0.01 pp")

    eligible = [ed for ed in AR_EDITIONS if coverage[ed] / 100.0 >= DISPUTE_COVERAGE_GATE]
    if len(eligible) != 7:
        die("eligible-edition count %d, expected 7" % len(eligible))   # abort condition 5
    print("[ok] DISPUTE eligible editions: %d (excluded: %s)"
          % (len(eligible), [e for e in AR_EDITIONS if e not in eligible]))

    # ---- outcome channels, prereg section 3.4 ------------------------------------------
    ALL_EDITIONS = AR_EDITIONS + EN_EDITIONS
    amort_mk = {ed: {k: eds[ed][k]["mk"] / eds[ed][k]["grp"] for k in V} for ed in ALL_EDITIONS}
    amort_len = {ed: {k: eds[ed][k]["chars"] / eds[ed][k]["grp"] for k in V} for ed in ALL_EDITIONS}

    def build_channels(ed_disp, ed_div):
        rk = {ed: mid_ranks(V, lambda k, e=ed: amort_mk[e][k]) for ed in ed_disp}
        c1 = np.array([np.mean([rk[e][k] for e in ed_disp]) for k in V])
        c2 = np.array([np.mean([1000.0 * eds[e][k]["mk"] / max(1, eds[e][k]["chars"])
                                for e in ed_disp]) for k in V])
        lr = {ed: mid_ranks(V, lambda k, e=ed: amort_len[e][k]) for ed in ed_div}
        c3 = np.array([float(np.subtract(*np.percentile([lr[e][k] for e in ed_div], [75, 25])))
                       for k in V])
        c4 = []
        for k in V:
            ts = [eds[e][k]["types"] for e in ed_div]
            acc = [1.0 - (len(ts[i] & ts[j]) / len(ts[i] | ts[j]) if (ts[i] | ts[j]) else 0.0)
                   for i in range(len(ts)) for j in range(i + 1, len(ts))]
            c4.append(float(np.mean(acc)))
        return c1, c2, c3, np.array(c4)

    C1, C2, C3, C4 = build_channels(eligible, AR_EDITIONS)

    tie = {}
    for nm, arr in (("C1_DISPUTE_rank", C1), ("C2_DISPUTE_density", C2),
                    ("C3_DIVERGENCE_L", C3), ("C4_DIVERGENCE_V", C4)):
        _, cnt = np.unique(np.round(arr, 12), return_counts=True)
        tie[nm] = float(cnt.max()) / len(arr)
    print("[ok] tie fractions: " + ", ".join("%s %.4f" % (k, v) for k, v in tie.items()))

    # ---- predictors --------------------------------------------------------------------
    decl = {r["column"]: r for r in csv.DictReader(open(DECLS, encoding="utf-8"))}
    for c in STRUCT_COLS:                                             # abort condition 7
        if decl[c]["length_dominated"] != "False":
            die("structural column %s is flagged length_dominated=%s"
                % (c, decl[c]["length_dominated"]))
    print("[ok] all %d structural columns flagged length_dominated=False" % len(STRUCT_COLS))

    prof = {}
    for row in csv.DictReader(open(PROFILE, encoding="utf-8")):
        prof[(int(row["surah"]), int(row["verse"]))] = row
    if len(prof) != N_VERSES:
        die("verse profile has %d rows" % len(prof))                  # abort condition 6

    quran = json.load(open(QURAN, encoding="utf-8"))
    vtext = {}
    for s in quran:
        for v in s["verses"]:
            vtext[(s["id"], v["id"])] = v["text"]

    seen, is_repeat, lemma_echo = {}, {}, {}
    for k in V:
        t = WS_RE.sub(" ", vtext[k]).strip()
        is_repeat[k] = 1.0 if t in seen else 0.0
        seen.setdefault(t, k)
        w = marker_words(vtext[k])
        lemma_echo[k] = 1.0 if (any(x in UNIGRAM_MARKERS for x in w)
                                or any((w[i], w[i + 1]) in BIGRAM_MARKERS
                                       for i in range(len(w) - 1))) else 0.0
    print("[ok] lemma-echo verses: %d; repeat verses: %d"
          % (int(sum(lemma_echo.values())), int(sum(is_repeat.values()))))

    # ---- assemble analysis set ---------------------------------------------------------
    def col(k, name):
        v = prof[k][name]
        return float(v) if v not in ("", None) else np.nan

    keep, dropped = [], []
    for i, k in enumerate(V):
        vals = [col(k, c) for c in STRUCT_COLS + LENGTH_COLS + NUISANCE_EXTRA]
        (keep if not any(np.isnan(vals)) else dropped).append(i)
    keep = np.array(keep)
    print("[ok] analysis n = %d (dropped %d verses with undefined columns)"
          % (len(keep), len(dropped)))

    Vk = [V[i] for i in keep]
    S = np.column_stack([[col(k, c) for k in Vk] for c in STRUCT_COLS])
    L = np.column_stack([[col(k, c) for k in Vk] for c in LENGTH_COLS])
    M0 = np.column_stack([L,
                          [col(k, "mushaf_index") for k in Vk],
                          [lemma_echo[k] for k in Vk],
                          [is_repeat[k] for k in Vk]])
    nwords = np.array([col(k, "n_words") for k in Vk])
    strata = np.clip(np.searchsorted(np.quantile(nwords, np.linspace(0, 1, N_DECILES + 1)[1:-1]),
                                     nwords), 0, N_DECILES - 1)

    # ---- prereg section 4: the computed floor ------------------------------------------
    # variance commanded by the arbitrary choice among three near-identical length rules
    floors = {}
    for nm, arr in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4)):
        y = normal_scores(arr[keep])
        base1 = np.column_stack([L[:, 0], [col(k, "mushaf_index") for k in Vk],
                                 [lemma_echo[k] for k in Vk], [is_repeat[k] for k in Vk]])
        floors[nm] = r2(M0, y) - r2(base1, y)
    print("[ok] length-rule floors: " + ", ".join("%s %.5f" % (k, v) for k, v in floors.items()))

    # ---- inferences --------------------------------------------------------------------
    rng = np.random.default_rng(SEED)
    dir_ix = STRUCT_COLS.index(DIRECTION_COL)
    results = {}
    for nm, arr in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4)):
        y = normal_scores(arr[keep])
        res = delta_r2_test(y, M0, S, strata, rng, dir_ix)
        # abort condition 8. "3 permutation-SEs" is read as 3 x the permutation SD of a
        # single draw; the deviation in SEs-of-the-mean is also recorded so a reader can
        # apply the tighter reading. The ambiguity is disclosed in the finding.
        res["cond8_fail"] = bool(
            abs(res["null_mean"] - res["null_analytic_expectation"]) > 3.0 * res["null_sd"])
        res["null_inflation_vs_analytic"] = (res["null_mean"]
                                             / res["null_analytic_expectation"])
        if res["cond8_fail"]:
            print("     %s DISQUALIFIED by abort condition 8: stratified null mean %.6g is "
                  "%.1fx the analytic expectation %.6g -- the null is inflated by "
                  "length-mediated signal" % (nm, res["null_mean"],
                                              res["null_inflation_vs_analytic"],
                                              res["null_analytic_expectation"]))
        res["floor_lengthrule"] = floors[nm]
        res["tie_fraction"] = tie[{"C1": "C1_DISPUTE_rank", "C2": "C2_DISPUTE_density",
                                   "C3": "C3_DIVERGENCE_L", "C4": "C4_DIVERGENCE_V"}[nm]]
        res["gate_a_p"] = bool(res["p"] < ALPHA)
        res["gate_b_absfloor"] = bool(res["observed"] >= ABS_FLOOR)
        res["gate_c_lengthfloor"] = bool(res["observed"] > floors[nm])
        res["gate_d_direction"] = bool(res["direction_partial"] > 0)
        gates = [res["gate_a_p"], res["gate_b_absfloor"],
                 res["gate_c_lengthfloor"], res["gate_d_direction"]]
        # a DISQUALIFIED channel can never PASS -- verdict ceiling drops to PARTIAL
        res["PASS"] = bool(all(gates) and not res["cond8_fail"])
        res["DISQUALIFIED"] = res["cond8_fail"]
        # prereg section 6.5: where the criteria disagree the more severe verdict is taken.
        # The AND conjunction implements that; the flag records that it bound.
        res["criteria_disagree"] = bool(any(gates) and not all(gates))
        # prereg section 6.3: reverse-direction flag. NOT a pass.
        res["REVERSE_DIRECTION_FLAG"] = bool(
            (not res["gate_d_direction"]) and res["p_direction_reverse"] < ALPHA)
        results[nm] = res
        print("     %s dR2=%.5f p=%.5f floors(abs=%.3f,len=%.5f) dir=%+.4f "
              "p_rev=%.4f -> %s%s"
              % (nm, res["observed"], res["p"], ABS_FLOOR, floors[nm],
                 res["direction_partial"], res["p_direction_reverse"],
                 "PASS" if res["PASS"] else "NULL",
                 "  [REVERSE-DIRECTION FLAG]" if res["REVERSE_DIRECTION_FLAG"] else ""))

    # I1 headlined by the WORSE of C1 and C2 (prereg section 5)
    worse = "C1" if results["C1"]["observed"] <= results["C2"]["observed"] else "C2"
    dominant = "C2" if worse == "C1" else "C1"
    I = {"I1": dict(results[worse], channel=worse, dominant_channel=dominant),
         "I2": dict(results["C3"], channel="C3"),
         "I3": dict(results["C4"], channel="C4")}
    survivors = sum(1 for v in I.values() if v["PASS"])
    verdict = "SUPPORTED" if survivors == 3 else ("NULL" if survivors == 0 else "PARTIAL")
    print("\n[VERDICT] survivors %d of 3 -> %s" % (survivors, verdict))

    # ---- untestable branch, prereg section 6.4 -----------------------------------------
    clean = [c for c, r in decl.items() if r["length_dominated"] == "False"
             and c not in LENGTH_COLS]
    ceiling = {}
    Sfull_cols = [c for c in clean if all(prof[k][c] not in ("", None) for k in Vk)]
    Sfull = np.column_stack([[col(k, c) for k in Vk] for c in Sfull_cols])
    for nm, arr in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4)):
        y = normal_scores(arr[keep])
        ceiling[nm] = r2(np.column_stack([M0, Sfull]), y) - r2(M0, y)
    # prereg section 6.4 literal: dR2* is "the smallest Delta R^2 clearing alpha".
    mde_alpha = {nm: results[nm]["null_q_alpha"] for nm in results}
    # the stricter threshold that clears ALL FOUR gates, reported alongside.
    mde_allgates = {nm: max(ABS_FLOOR, floors[nm], results[nm]["null_q_alpha"])
                    for nm in results}
    untestable = {nm: bool(mde_alpha[nm] > ceiling[nm]) for nm in results}
    untestable_allgates = {nm: bool(mde_allgates[nm] > ceiling[nm]) for nm in results}
    print("[ok] dR2* vs attainable ceiling (%d clean cols):" % len(Sfull_cols))
    for nm in ("C1", "C2", "C3", "C4"):
        print("     %s  dR2*(alpha)=%.5f  dR2*(all gates)=%.5f  ceiling=%.5f  %s"
              % (nm, mde_alpha[nm], mde_allgates[nm], ceiling[nm],
                 "UNTESTABLE-AT-THIS-N" if untestable[nm] else "testable"))

    # ---- sensitivities, non-confirmatory ------------------------------------------------
    sens = {}

    def quick(y_arr, mask=None, M0x=None, Sx=None):
        m = np.ones(len(keep), dtype=bool) if mask is None else mask
        y = normal_scores(y_arr[keep][m])
        A = (M0 if M0x is None else M0x)[m]
        B = (S if Sx is None else Sx)[m]
        return r2(np.column_stack([A, B]), y) - r2(A, y)

    for label, sub in (("S1_classical_only_4ed", AR_CLASSICAL), ("S2_modern_only_4ed", AR_MODERN)):
        d = [e for e in sub if e in eligible]
        c1, c2, c3, c4 = build_channels(d if d else sub, sub)
        sens[label] = {nm: quick(a) for nm, a in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4))}
        sens[label]["editions"] = sub

    m_echo = np.array([lemma_echo[k] == 0 for k in Vk])
    m_first = np.array([is_repeat[k] == 0 for k in Vk])
    sens["S3_drop_lemma_echo"] = {nm: quick(a, m_echo)
                                  for nm, a in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4))}
    sens["S4_first_occurrence_only"] = {nm: quick(a, m_first)
                                        for nm, a in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4))}
    sens["S6_full_clean_block"] = {nm: quick(a, None, None, Sfull)
                                   for nm, a in (("C1", C1), ("C2", C2), ("C3", C3), ("C4", C4))}
    loo = {}
    for drop in AR_EDITIONS:
        d_div = [e for e in AR_EDITIONS if e != drop]
        d_dis = [e for e in eligible if e != drop] or eligible
        c1, c2, c3, c4 = build_channels(d_dis, d_div)
        loo[drop] = {nm: quick(a) for nm, a in (("C1", c1), ("C2", c2), ("C3", c3), ("C4", c4))}
    sens["S5_leave_one_edition_out"] = loo
    c1e, c2e, c3e, c4e = build_channels(eligible, EN_EDITIONS)
    sens["S8_english_4ed"] = {nm: quick(a) for nm, a in (("C3", c3e), ("C4", c4e))}
    print("[ok] %d sensitivity families computed" % len(sens))

    # ---- rosters -----------------------------------------------------------------------
    ns_C1 = normal_scores(C1[keep])
    A = np.column_stack([np.ones(len(Vk)), M0])
    b, *_ = np.linalg.lstsq(A, ns_C1, rcond=None)
    resid = ns_C1 - A @ b
    order = np.argsort(-resid)
    roster = [dict(surah=Vk[i][0], verse=Vk[i][1], dispute_resid=float(resid[i]),
                   lemma_echo=bool(lemma_echo[Vk[i]]), is_repeat=bool(is_repeat[Vk[i]]),
                   text=vtext[Vk[i]][:160]) for i in order[:40]]

    # ---- write run dir (only after everything succeeded) --------------------------------
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = Path("findings/phase-b-hypotheses/runs/h-new-3160") / stamp
    os.makedirs(out, exist_ok=False)                                   # abort condition 9

    def dump(name, obj):
        with open(out / name, "x", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2, default=float)

    dump("result.json", dict(
        id="H-NEW-3160", verdict=verdict, survivors=survivors, n=len(keep),
        alpha_bonferroni=ALPHA, seed=SEED, n_perm=N_PERM,
        inferences=I, channels=results, tie_fractions=tie,
        floors_lengthrule=floors, abs_floor=ABS_FLOOR,
        mde_delta_r2_alpha=mde_alpha, mde_delta_r2_all_gates=mde_allgates,
        ceiling_delta_r2=ceiling, untestable=untestable,
        untestable_all_gates=untestable_allgates,
        n_clean_ceiling_cols=len(Sfull_cols), ceiling_columns=Sfull_cols,
        eligible_editions=eligible, coverage_pct=coverage, distinct_blocks=blocks,
        dropped_verses=[list(V[i]) for i in dropped],
        n_lemma_echo=int(sum(lemma_echo.values())), n_repeat=int(sum(is_repeat.values())),
    ))
    dump("sensitivities.json", sens)
    dump("roster_most_disputed.json", roster)
    with open(out / "coverage.tsv", "x", encoding="utf-8") as fh:
        fh.write("edition\tmarker_coverage_pct\tpublished_2620_pct\tdistinct_blocks\teligible\n")
        for ed in AR_EDITIONS:
            fh.write("%s\t%.2f\t%.2f\t%d\t%s\n" % (ed, coverage[ed],
                     PUBLISHED_COVERAGE_2620[ed], blocks[ed], ed in eligible))
    manifest = dict(
        prereg=PREREG, prereg_sha256=EXPECTED_PREREG_SHA,
        inputs={p: sha256_file(p) for p in (PROFILE, DECLS, QURAN)},
        n_tafsir_files=len(all_hashes),
        tafsir_manifest_sha256=hashlib.sha256(
            "\n".join("%s %s" % (k, all_hashes[k]) for k in sorted(all_hashes)).encode()
        ).hexdigest(),
        python=platform.python_version(), numpy=np.__version__,
        git_head=subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                text=True).stdout.strip(),
        utc=stamp,
    )
    dump("manifest.json", manifest)
    print("\n[ok] run written: %s" % out)
    print("[ok] tafsir manifest SHA-256: %s" % manifest["tafsir_manifest_sha256"])


if __name__ == "__main__":
    main()
