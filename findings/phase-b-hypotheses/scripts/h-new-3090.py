#!/usr/bin/env python3
"""
H-NEW-3090 — Biological-kinship vs affiliative vocabulary across the Hijra,
held at fixed discourse register.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3090-kinship-affiliation.md
The digest below is verified at runtime; a mismatch is a hard SystemExit.

Run discipline (STANDING RULES 2026-08-08):
  - immutable run dir via os.makedirs(exist_ok=False)
  - every artefact via open(path, 'x')
  - no run directory is ever deleted
"""

import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

# ----------------------------------------------------------------------------
# 0. Pre-registration lock
# ----------------------------------------------------------------------------

EXPECTED_PREREG_SHA = "c163a0b27c63628a16a313c0d54fab8948dce9d40605036e9bfd12bda76721b8"

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
PREREG = os.path.join(ROOT, "findings", "phase-b-hypotheses",
                      "prereg-h-new-3090-kinship-affiliation.md")

with open(PREREG, "rb") as fh:
    actual = hashlib.sha256(fh.read()).hexdigest()
if actual != EXPECTED_PREREG_SHA:
    raise SystemExit(
        f"PREREG SHA MISMATCH\n  expected {EXPECTED_PREREG_SHA}\n  actual   {actual}\n"
        f"  file     {PREREG}\nRefusing to run.")

# ----------------------------------------------------------------------------
# 1. Locked constants  (prereg §2, §5, §7)
# ----------------------------------------------------------------------------

SEED = 20260509
N_PERM = 10000
K_BONFERRONI = 24
ALPHA_BON = 0.05 / K_BONFERRONI          # 0.00208333...
TIE_THRESHOLD = 0.50

# prereg §2.1 R1
BIO_R1 = {"walad", ">aroHaAm", "nasab"}
AFF_R1 = {"<ixowapN", "waliY~", "mawolaY`", "mawa`liY", "mawa`liy"}
# prereg §2.1 R2
BIO_R2_ROOTS = {"wld", "rHm", "nsb"}
AFF_R2_ROOTS = {"Axw", "wly"}
# prereg §3.1 Rater A
RATER_A_KIN_ROOTS = {"Abw", "Amm", "bny", "zwj", "wld", "nsl", "*rr", "Emm", "xwl", "Axw"}
RATER_A_DIVINE_WINDOW = 3
# prereg §3.2 Rater B
BIO_LEX = {"brother", "brothers", "sister", "sisters", "kinship", "womb", "wombs",
           "parent", "parents", "father", "fathers", "mother", "mothers", "son", "sons",
           "daughter", "daughters", "offspring", "child", "children", "relative",
           "relatives", "kin", "lineage", "born", "beget", "begot", "begotten"}
AFF_LEX = {"ally", "allies", "protector", "protectors", "guardian", "guardians",
           "patron", "patrons", "friend", "friends", "helper", "helpers",
           "supporter", "supporters", "associate", "associates"}
RATER_B_DIVINE_WINDOW = 3

CHANNELS = ["RATIO", "PER_WORD", "PER_VERSE", "MVL_RESID"]
TESTS = ["T1_FULL", "T2_LEGAL_ABLATED", "T3_REGISTER_STRATIFIED"]
VERDICT_TUPLES = ["R1", "R3"]

# MDE (prereg §7.1)
N_MDE_SIM = 200
N_MDE_PERM = 2000
MDE_POWER_TARGET = 0.80

# ----------------------------------------------------------------------------
# 2. Run directory
# ----------------------------------------------------------------------------

STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join(ROOT, "runs", "h-new-3090", STAMP)
os.makedirs(RUNDIR, exist_ok=False)


def wx(name, text):
    with open(os.path.join(RUNDIR, name), "x", encoding="utf-8") as fh:
        fh.write(text)


LOG = []


def log(msg):
    print(msg)
    LOG.append(msg)


log(f"H-NEW-3090  run {STAMP}")
log(f"prereg sha256 = {actual}  VERIFIED")
log(f"seed={SEED} n_perm={N_PERM} k={K_BONFERRONI} alpha_bon={ALPHA_BON:.8f}")

# ----------------------------------------------------------------------------
# 3. Load QAC morphology
# ----------------------------------------------------------------------------

MORPH = os.path.join(ROOT, "data", "morphology", "quranic-corpus-morphology-0.4.txt")
LOC = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")

# tokens[(s,v)] -> ordered list of dicts for STEM segments
verse_stems = defaultdict(list)
words_in_surah = defaultdict(set)
verses_in_surah = defaultdict(set)

with open(MORPH, encoding="utf-8") as fh:
    for line in fh:
        m = LOC.match(line.rstrip("\n"))
        if not m:
            continue
        s, v, w, _seg = (int(m.group(i)) for i in range(1, 5))
        feats = m.group(7)
        words_in_surah[s].add((v, w))
        verses_in_surah[s].add(v)
        if "STEM" not in feats:
            continue
        lem = re.search(r"LEM:([^|]*)", feats)
        rt = re.search(r"ROOT:([^|]*)", feats)
        pos = re.search(r"POS:([^|]*)", feats)
        verse_stems[(s, v)].append({
            "s": s, "v": v, "w": w,
            "i": len(verse_stems[(s, v)]),   # unique position within the verse
            "lem": lem.group(1) if lem else None,
            "root": rt.group(1) if rt else None,
            "pos": pos.group(1) if pos else None,
        })

SURAHS = sorted(words_in_surah)
assert SURAHS == list(range(1, 115)), "expected 114 surahs"
N_VERSES_TOTAL = sum(len(verses_in_surah[s]) for s in SURAHS)
log(f"QAC: {N_VERSES_TOTAL} verses, {sum(len(words_in_surah[s]) for s in SURAHS)} words")
assert N_VERSES_TOTAL == 6236, f"expected 6236 verses, got {N_VERSES_TOTAL}"

W = np.array([len(words_in_surah[s]) for s in SURAHS], dtype=float)
V = np.array([len(verses_in_surah[s]) for s in SURAHS], dtype=float)
MVL = W / V

# cross-check against the canonical text file (prereg §2)
with open(os.path.join(ROOT, "quran-text", "quran-min-tashkeel.json"), encoding="utf-8") as fh:
    qjson = json.load(fh)
log(f"quran-min-tashkeel.json: {len(qjson)} top-level entries (cross-check only)")

# ----------------------------------------------------------------------------
# 4. Phase and register labels
# ----------------------------------------------------------------------------

period = {}
with open(os.path.join(ROOT, "data", "revelation-order.csv"), encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        period[int(r["mushaf_order"])] = r["period"].strip()

IS_MED = np.array([1 if period[s] == "Medinan" else 0 for s in SURAHS], dtype=int)
log(f"phase: {int((IS_MED == 0).sum())} Meccan / {int(IS_MED.sum())} Medinan")


def coarsen(genre):
    """prereg §2 — first-match precedence, verbatim."""
    g = genre.lower()
    if "legal" in g:
        return "LEGAL"
    if "narrative" in g or "qaṣaṣ" in g or "qasas" in g:
        return "NARRATIVE"
    if "eschatolog" in g:
        return "ESCHATOLOGICAL"
    if "scripture-reflective" in g:
        return "SCRIPTURE"
    if any(k in g for k in ("oath", "hymn", "liturgical", "apotropaic", "creedal")):
        return "HYMNIC_OATH"
    return "EXHORT_POLEM"


gpath = os.path.join(ROOT, "findings", "classical-sources", "neuwirth-sinai-genre-labels.tsv")
grows = [l.rstrip("\n").split("\t") for l in open(gpath, encoding="utf-8")
         if not l.startswith("#") and l.strip()]
ghdr = grows[0]
gdata = {int(d["surah_number"]): d for d in (dict(zip(ghdr, r)) for r in grows[1:])}
assert len(gdata) == 114
REGISTER = np.array([coarsen(gdata[s]["neuwirth_genre"]) for s in SURAHS], dtype=object)

ct = Counter((REGISTER[i], "Medinan" if IS_MED[i] else "Meccan") for i in range(114))
strata = sorted(set(REGISTER))
MIXED = [st for st in strata
         if ct[(st, "Meccan")] > 0 and ct[(st, "Medinan")] > 0]
log("register x phase crosstab:")
for st in strata:
    log(f"  {st:16s} Meccan={ct[(st,'Meccan')]:3d} Medinan={ct[(st,'Medinan')]:3d}"
        f"  {'MIXED' if st in MIXED else 'DEGENERATE(zero permutable information)'}")

# ----------------------------------------------------------------------------
# 5. English translation, aligned (prereg §3.2)
# ----------------------------------------------------------------------------

tlines = [l for l in open(os.path.join(ROOT, "data", "translations", "en.sahih.txt"),
                          encoding="utf-8").read().split("\n")
          if l.strip() and not l.startswith("#")]
assert len(tlines) == 6236, f"translation has {len(tlines)} verse lines, expected 6236"

ordered_verses = [(s, v) for s in SURAHS for v in sorted(verses_in_surah[s])]
EN = {vk: tlines[i] for i, vk in enumerate(ordered_verses)}
# positive controls on the alignment (asserted, not assumed)
assert "no deity except Him" in EN[(2, 255)], "translation misaligned at 2:255"
assert "refuge in the Lord of mankind" in EN[(114, 1)], "translation misaligned at 114:1"
assert "name of Allah" in EN[(1, 1)], "translation misaligned at 1:1"
log("translation alignment: 3/3 positive controls PASS")

WORD_RE = re.compile(r"[a-z']+")

# ----------------------------------------------------------------------------
# 6. Token extraction and the two raters
# ----------------------------------------------------------------------------


def rater_a(tok):
    """prereg §3.1 — Arabic-morphology co-occurrence rule."""
    stems = verse_stems[(tok["s"], tok["v"])]
    i = tok["i"]                      # positional id, never a value-equality lookup
    for j, o in enumerate(stems):
        if abs(i - j) <= RATER_A_DIVINE_WINDOW and j != i:
            if o["root"] == "Alh" or o["lem"] == "r~aHoma`n":
                return "DIVINE"
    for j, o in enumerate(stems):
        if j == i:
            continue
        if o["root"] in RATER_A_KIN_ROOTS:
            return "BIO"
    return "AFF"


def rater_b(tok):
    """prereg §3.2 — the Sahih International translator's judgement."""
    words = WORD_RE.findall(EN[(tok["s"], tok["v"])].lower())
    allah_pos = [k for k, x in enumerate(words) if x == "allah"]
    aff_pos = [k for k, x in enumerate(words) if x in AFF_LEX]
    for a in allah_pos:
        for f in aff_pos:
            if abs(a - f) <= RATER_B_DIVINE_WINDOW:
                return "DIVINE"
    has_bio = any(x in BIO_LEX for x in words)
    has_aff = bool(aff_pos)
    if has_bio and not has_aff:
        return "BIO"
    if has_aff and not has_bio:
        return "AFF"
    return "AMBIGUOUS"


all_tokens = [t for vk in ordered_verses for t in verse_stems[vk]]

r1_tokens = []   # (tok, f20_class)
for t in all_tokens:
    if t["lem"] in BIO_R1:
        r1_tokens.append((t, "BIO"))
    elif t["lem"] in AFF_R1:
        r1_tokens.append((t, "AFF"))

r2_tokens = []
for t in all_tokens:
    if t["root"] in BIO_R2_ROOTS:
        r2_tokens.append((t, "BIO"))
    elif t["root"] in AFF_R2_ROOTS:
        r2_tokens.append((t, "AFF"))

log(f"R1 tokens: {sum(1 for _,c in r1_tokens if c=='BIO')} BIO / "
    f"{sum(1 for _,c in r1_tokens if c=='AFF')} AFF")
log(f"R2 tokens: {sum(1 for _,c in r2_tokens if c=='BIO')} BIO / "
    f"{sum(1 for _,c in r2_tokens if c=='AFF')} AFF")

# rater labels on every R1 token
labA = {id(t): rater_a(t) for t, _ in r1_tokens}
labB = {id(t): rater_b(t) for t, _ in r1_tokens}

r3_tokens = [(t, c) for t, c in r1_tokens
             if labA[id(t)] == labB[id(t)] == c]
log(f"R3 tokens (both raters agree AND agree with F-20 class): "
    f"{sum(1 for _,c in r3_tokens if c=='BIO')} BIO / "
    f"{sum(1 for _,c in r3_tokens if c=='AFF')} AFF")


def cohen_kappa(a, b, cats):
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = 0.0
    for c in cats:
        pe += (sum(1 for x in a if x == c) / n) * (sum(1 for x in b if x == c) / n)
    return (po - pe) / (1 - pe) if pe < 1 else float("nan")


A_all = [labA[id(t)] for t, _ in r1_tokens]
B_all = [labB[id(t)] for t, _ in r1_tokens]
op = [(x, y) for x, y in zip(A_all, B_all) if y != "AMBIGUOUS"]
KAPPA_FULL = cohen_kappa(A_all, B_all, ["DIVINE", "BIO", "AFF", "AMBIGUOUS"])
KAPPA_OP = cohen_kappa([x for x, _ in op], [y for _, y in op], ["DIVINE", "BIO", "AFF"])
AGREE_OP = (sum(1 for x, y in op if x == y) / len(op)) if op else float("nan")
log(f"kappa(A,B) operating-range = {KAPPA_OP:.4f} (n={len(op)}, raw agreement {AGREE_OP:.4f})")
log(f"kappa(A,B) full-set        = {KAPPA_FULL:.4f} (n={len(A_all)})")

# per-term proxy census
census = {}
for lemma in sorted(BIO_R1 | AFF_R1):
    toks = [t for t, c in r1_tokens if t["lem"] == lemma]
    if not toks:
        continue
    f20 = "BIO" if lemma in BIO_R1 else "AFF"
    ca, cb = Counter(labA[id(t)] for t in toks), Counter(labB[id(t)] for t in toks)
    agreed_in = sum(1 for t in toks if labA[id(t)] == labB[id(t)] == f20)
    both_agree = sum(1 for t in toks if labA[id(t)] == labB[id(t)])
    cross = sum(1 for t in toks
                if labA[id(t)] == labB[id(t)] and labA[id(t)] in ("BIO", "AFF")
                and labA[id(t)] != f20)
    divine = sum(1 for t in toks if labA[id(t)] == "DIVINE" or labB[id(t)] == "DIVINE")
    census[lemma] = {
        "f20_class": f20, "n_tokens": len(toks),
        "raterA": dict(ca), "raterB": dict(cb),
        "both_raters_agree": both_agree,
        "agreed_in_F20_class": agreed_in,
        "agreed_in_OTHER_class": cross,
        "divine_by_either_rater": divine,
        "clean_fraction": agreed_in / len(toks),
        "verses": sorted({f"{t['s']}:{t['v']}" for t in toks}),
    }
    log(f"  {lemma:12s} F20={f20}  n={len(toks):3d}  clean={agreed_in:3d} "
        f"({agreed_in/len(toks):.1%})  cross-class={cross:3d}  divine={divine:3d}")

# ----------------------------------------------------------------------------
# 7. Per-surah count matrices
# ----------------------------------------------------------------------------

S_INDEX = {s: i for i, s in enumerate(SURAHS)}


def counts(tokens):
    aff = np.zeros(114)
    bio = np.zeros(114)
    for t, c in tokens:
        (aff if c == "AFF" else bio)[S_INDEX[t["s"]]] += 1
    return aff, bio


TUPLES = {"R1": counts(r1_tokens), "R2": counts(r2_tokens), "R3": counts(r3_tokens)}

# ----------------------------------------------------------------------------
# 8. Channel statistics (prereg §5.2)
# ----------------------------------------------------------------------------


def resid_on_log_mvl(y, mask):
    """OLS residual of y on log(MVL), fit on the sub-corpus `mask`. Phase-free."""
    x = np.log(MVL[mask])
    yy = y[mask]
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, yy, rcond=None)
    out = np.full(114, np.nan)
    out[mask] = yy - X @ beta
    return out


def channel_vectors(aff, bio, mask):
    """Per-surah contrast in each non-pooled channel; RATIO handled separately."""
    per_word = (aff - bio) / W
    per_verse = (aff - bio) / V
    mvl_res = resid_on_log_mvl(per_word, mask)
    return {"PER_WORD": per_word, "PER_VERSE": per_verse, "MVL_RESID": mvl_res}


def ratio_delta(aff, bio, med_mask, mec_mask):
    a1, b1 = aff[med_mask].sum(), bio[med_mask].sum()
    a0, b0 = aff[mec_mask].sum(), bio[mec_mask].sum()
    if (a1 + b1) == 0 or (a0 + b0) == 0:
        return np.nan
    return a1 / (a1 + b1) - a0 / (a0 + b0)


def mean_delta(vec, med_mask, mec_mask):
    if med_mask.sum() == 0 or mec_mask.sum() == 0:
        return np.nan
    return vec[med_mask].mean() - vec[mec_mask].mean()


def ratio_delta_vec(a, b, perms):
    """Vectorised RATIO statistic over an (n_perm x n) boolean label matrix."""
    a_med = perms @ a
    b_med = perms @ b
    a_mec = a.sum() - a_med
    b_mec = b.sum() - b_med
    n1, n0 = a_med + b_med, a_mec + b_mec
    with np.errstate(divide="ignore", invalid="ignore"):
        out = np.where((n1 > 0) & (n0 > 0), a_med / n1 - a_mec / n0, np.nan)
    return out


def mean_delta_vec(vec, perms, n_med, n_tot):
    sums = perms @ vec
    return sums / n_med - (vec.sum() - sums) / (n_tot - n_med)


# ----------------------------------------------------------------------------
# 9. Permutation machinery
# ----------------------------------------------------------------------------


def perm_labels_free(rng, n, n_med, n_perm):
    """n_perm x n boolean matrix, exactly n_med True per row."""
    base = np.zeros((n_perm, n), dtype=bool)
    base[:, :n_med] = True
    idx = np.argsort(rng.random((n_perm, n)), axis=1)
    return np.take_along_axis(base, idx, axis=1)


def perm_labels_stratified(rng, strat_ids, is_med, n_perm):
    """Permute phase labels WITHIN each stratum independently."""
    n = len(strat_ids)
    out = np.zeros((n_perm, n), dtype=bool)
    for st in set(strat_ids):
        pos = np.where(np.array(strat_ids) == st)[0]
        k = int(is_med[pos].sum())
        sub = perm_labels_free(rng, len(pos), k, n_perm)
        out[:, pos] = sub
    return out


def one_sided_p(obs, null):
    null = np.asarray(null, dtype=float)
    ok = ~np.isnan(null)
    null = null[ok]
    if np.isnan(obs) or null.size == 0:
        return float("nan"), float("nan")
    ge = int((null >= obs - 1e-15).sum())
    ties = float((np.abs(null - obs) < 1e-12).sum()) / null.size
    return (1 + ge) / (1 + null.size), ties


def fisher_one_sided(a1, b1, a0, b0):
    """P(AFF_med >= a1) under the hypergeometric with fixed margins."""
    from math import comb
    n_med, n_mec = a1 + b1, a0 + b0
    total_aff, total = a1 + a0, a1 + b1 + a0 + b0
    num = 0.0
    den = comb(total, n_med)
    for k in range(int(a1), int(min(total_aff, n_med)) + 1):
        if total - total_aff < n_med - k or n_med - k < 0:
            continue
        num += comb(int(total_aff), k) * comb(int(total - total_aff), int(n_med - k))
    return num / den


RNG = np.random.default_rng(SEED)

# ----------------------------------------------------------------------------
# 10. Run the 3 x 4 x 2 cells (+ R2 diagnostic)
# ----------------------------------------------------------------------------

LEGAL_MASK = np.array([r == "LEGAL" for r in REGISTER])
MIXED_MASK = np.array([r in MIXED for r in REGISTER])

TEST_MASKS = {
    "T1_FULL": np.ones(114, dtype=bool),
    "T2_LEGAL_ABLATED": ~LEGAL_MASK,
    "T3_REGISTER_STRATIFIED": MIXED_MASK,
}
log(f"T1 N={int(TEST_MASKS['T1_FULL'].sum())}  "
    f"T2 N={int(TEST_MASKS['T2_LEGAL_ABLATED'].sum())} "
    f"(dropped {int(LEGAL_MASK.sum())} LEGAL surahs)  "
    f"T3 N={int(TEST_MASKS['T3_REGISTER_STRATIFIED'].sum())} over {len(MIXED)} mixed strata")

results = {}


def run_cell(test, channel, tup, aff, bio, rng):
    mask = TEST_MASKS[test]
    sub = np.where(mask)[0]
    is_med_sub = IS_MED[sub].astype(bool)
    n, n_med = len(sub), int(is_med_sub.sum())

    stratified = (test == "T3_REGISTER_STRATIFIED")
    if stratified:
        strat_ids = [REGISTER[i] for i in sub]
        perms = perm_labels_stratified(rng, strat_ids, is_med_sub, N_PERM)
    else:
        perms = perm_labels_free(rng, n, n_med, N_PERM)

    if channel == "RATIO":
        a, b = aff[sub], bio[sub]
        if stratified:
            def stat(medmask):
                num = den = 0.0
                for st in MIXED:
                    sel = np.array([x == st for x in strat_ids])
                    d = ratio_delta(a, b, sel & medmask, sel & ~medmask)
                    wgt = (a[sel].sum() + b[sel].sum())
                    if not np.isnan(d) and wgt > 0:
                        num += wgt * d
                        den += wgt
                return num / den if den > 0 else np.nan
            obs = stat(is_med_sub)
            null = np.array([stat(perms[i]) for i in range(N_PERM)])
        else:
            obs = ratio_delta(a, b, is_med_sub, ~is_med_sub)
            null = ratio_delta_vec(a.astype(float), b.astype(float),
                                   perms.astype(float))
    else:
        vec_all = channel_vectors(aff, bio, mask)[channel]
        vec = vec_all[sub]
        if stratified:
            def stat(medmask):
                num = den = 0.0
                for st in MIXED:
                    sel = np.array([x == st for x in strat_ids])
                    d = mean_delta(vec, sel & medmask, sel & ~medmask)
                    wgt = (aff[sub][sel].sum() + bio[sub][sel].sum())
                    if not np.isnan(d) and wgt > 0:
                        num += wgt * d
                        den += wgt
                return num / den if den > 0 else np.nan
            obs = stat(is_med_sub)
            null = np.array([stat(perms[i]) for i in range(N_PERM)])
        else:
            obs = mean_delta(vec, is_med_sub, ~is_med_sub)
            sums = perms @ vec
            total = vec.sum()
            null = sums / n_med - (total - sums) / (n - n_med)

    p, ties = one_sided_p(obs, null)
    flag = ""
    if not np.isnan(ties) and ties > TIE_THRESHOLD:
        a1 = aff[sub][is_med_sub].sum(); b1 = bio[sub][is_med_sub].sum()
        a0 = aff[sub][~is_med_sub].sum(); b0 = bio[sub][~is_med_sub].sum()
        p = fisher_one_sided(a1, b1, a0, b0)
        flag = "EXACT"
    return {
        "test": test, "channel": channel, "tuple": tup,
        "N": n, "n_medinan": n_med,
        "observed": None if np.isnan(obs) else float(obs),
        "null_mean": float(np.nanmean(null)), "null_sd": float(np.nanstd(null)),
        "null_q95": float(np.nanpercentile(null, 95)),
        "p": None if np.isnan(p) else float(p),
        "tie_fraction": None if np.isnan(ties) else float(ties),
        "flag": flag,
        "PASS": bool((not np.isnan(obs)) and obs > 0 and (not np.isnan(p)) and p < ALPHA_BON),
    }


log("")
log("=== PRIMARY CELLS ===")
for tup in ["R1", "R3", "R2"]:
    aff, bio = TUPLES[tup]
    for test in TESTS:
        for ch in CHANNELS:
            rng = np.random.default_rng(SEED)   # identical null draw per cell
            res = run_cell(test, ch, tup, aff, bio, rng)
            results[(tup, test, ch)] = res
            tag = "VERDICT" if tup in VERDICT_TUPLES else "diagnostic"
            obs = res["observed"]
            log(f"  [{tag:10s}] {tup} {test:24s} {ch:10s} "
                f"obs={obs if obs is None else f'{obs:+.6f}'} "
                f"null={res['null_mean']:+.6f} p={res['p']} "
                f"{'PASS' if res['PASS'] else 'fail'} {res['flag']}")

# ----------------------------------------------------------------------------
# 11. Verdict ladder (prereg §7) — diffed line by line against the prereg
# ----------------------------------------------------------------------------


def test_passes(tup, test):
    """A TEST PASSES under a rules-tuple iff ALL FOUR channels pass."""
    return all(results[(tup, test, ch)]["PASS"] for ch in CHANNELS)


T1_R1 = test_passes("R1", "T1_FULL")
T2_R1 = test_passes("R1", "T2_LEGAL_ABLATED")
T2_R3 = test_passes("R3", "T2_LEGAL_ABLATED")
T3_R1_RATIO = results[("R1", "T3_REGISTER_STRATIFIED", "RATIO")]["PASS"]

if not T1_R1:
    VERDICT = "NULL"
elif not T2_R1:
    VERDICT = "RESTATES THE HIJRA"
elif not T2_R3:
    VERDICT = "PROXY-DEPENDENT"
elif not T3_R1_RATIO:
    VERDICT = "PASS-DIRECTED (weak within-register)"
else:
    VERDICT = "PASS-WITHIN-REGISTER"

log("")
log(f"ladder inputs: T1_R1={T1_R1} T2_R1={T2_R1} T2_R3={T2_R3} T3_R1_RATIO={T3_R1_RATIO}")
log(f"*** VERDICT: {VERDICT} ***")

# dominant channel for the headline test (prereg §5.2)
hp = {ch: results[("R1", "T2_LEGAL_ABLATED", ch)]["p"] for ch in CHANNELS}
finite = {k: v for k, v in hp.items() if v is not None}
DOMINANT = (max(finite, key=lambda k: abs(np.log10(max(finite[k], 1e-12))
                                          - np.median([np.log10(max(x, 1e-12))
                                                       for x in finite.values()])))
            if finite else None)
log(f"dominant channel (T2/R1, furthest p in log10 from the median) = {DOMINANT}")
log(f"worst channel (T2/R1) = {max(finite, key=finite.get) if finite else None}")

# ----------------------------------------------------------------------------
# 12. Descriptive ablations (prereg §6) — consume no Bonferroni slots
# ----------------------------------------------------------------------------

log("")
log("=== DESCRIPTIVE ABLATIONS (no Bonferroni slots, cannot change the verdict) ===")
ablations = {}
MAWLA = {"mawolaY`", "mawa`liY", "mawa`liy"}
abl_defs = {
    "6.1_no_mawla": [(t, c) for t, c in r1_tokens if t["lem"] not in MAWLA],
    "6.2_no_surah12": [(t, c) for t, c in r1_tokens if t["s"] != 12],
    "6.3_walad_nondivine": [(t, c) for t, c in r1_tokens
                            if not (t["lem"] == "walad" and labA[id(t)] == "DIVINE")],
}
for name, toks in abl_defs.items():
    aff, bio = counts(toks)
    ablations[name] = {"n_bio": int(bio.sum()), "n_aff": int(aff.sum()), "cells": {}}
    for test in ["T1_FULL", "T2_LEGAL_ABLATED"]:
        for ch in CHANNELS:
            rng = np.random.default_rng(SEED)
            r = run_cell(test, ch, name, aff, bio, rng)
            ablations[name]["cells"][f"{test}|{ch}"] = r
            obs = r["observed"]
            log(f"  {name:22s} {test:20s} {ch:10s} "
                f"obs={obs if obs is None else f'{obs:+.6f}'} p={r['p']} "
                f"{'PASS' if r['PASS'] else 'fail'}")

# ----------------------------------------------------------------------------
# 13. Size loading (UNIT-DRIFT-DEFECT / PROXY-CLAIMS Screen A')
# ----------------------------------------------------------------------------


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    d = np.sqrt((rx ** 2).sum() * (ry ** 2).sum())
    return float((rx * ry).sum() / d) if d else float("nan")


aff1, bio1 = TUPLES["R1"]
SIZE_LOADING = {
    "rho_AFF_vs_log_wordcount": spearman(aff1, np.log(W)),
    "rho_BIO_vs_log_wordcount": spearman(bio1, np.log(W)),
    "rho_AFF_vs_log_versecount": spearman(aff1, np.log(V)),
    "rho_BIO_vs_log_versecount": spearman(bio1, np.log(V)),
    "rho_AFF_vs_log_MVL": spearman(aff1, np.log(MVL)),
    "rho_BIO_vs_log_MVL": spearman(bio1, np.log(MVL)),
}
log("")
log("=== SIZE LOADING (R1) ===")
for k, v in SIZE_LOADING.items():
    log(f"  {k:34s} {v:+.4f}")

# ----------------------------------------------------------------------------
# 14. MDE / power for the headline test (prereg §7.1) — mandatory if NULL
# ----------------------------------------------------------------------------

log("")
log("=== MDE / POWER for T2_LEGAL_ABLATED under R1 ===")
mask2 = TEST_MASKS["T2_LEGAL_ABLATED"]
sub2 = np.where(mask2)[0]
med2 = IS_MED[sub2].astype(bool)
n2, nm2 = len(sub2), int(med2.sum())
MDE = {}
mrng = np.random.default_rng(SEED)

# One permutation matrix, drawn once and reused across every simulation and grid
# point. It is a fixed random subsample of the permutation group and does not
# depend on the simulated data, so reusing it is valid and makes the sweep finish.
PERMS_MDE = perm_labels_free(mrng, n2, nm2, N_MDE_PERM).astype(float)

for ch in CHANNELS:
    if ch == "RATIO":
        a, b = aff1[sub2], bio1[sub2]
        tot = (a + b).astype(int)
        base = a[~med2].sum() / max(a[~med2].sum() + b[~med2].sum(), 1)
        grid = [round(float(x), 4) for x in np.arange(0.02, 0.86, 0.02)]
        found = None
        for d in grid:
            p_s = np.where(med2, min(base + d, 1.0), base)
            hits = 0
            for _ in range(N_MDE_SIM):
                a_sim = mrng.binomial(tot, p_s).astype(float)
                b_sim = tot.astype(float) - a_sim
                obs = ratio_delta(a_sim, b_sim, med2, ~med2)
                null = ratio_delta_vec(a_sim, b_sim, PERMS_MDE)
                pp, _ = one_sided_p(obs, null)
                if not np.isnan(pp) and pp < ALPHA_BON:
                    hits += 1
            if hits / N_MDE_SIM >= MDE_POWER_TARGET:
                found = d
                break
        MDE[ch] = {"mde": found, "units": "share difference",
                   "meccan_baseline_share": float(base),
                   "power_at_mde": (hits / N_MDE_SIM) if found is not None else None}
    else:
        vec = channel_vectors(aff1, bio1, mask2)[ch][sub2]
        sd = float(np.std(vec))
        grid = [float(sd * m) for m in np.arange(0.1, 4.05, 0.1)]
        found = None
        for d in grid:
            hits = 0
            for _ in range(N_MDE_SIM):
                boot = np.empty_like(vec)
                boot[~med2] = mrng.choice(vec[~med2], size=int((~med2).sum()), replace=True)
                boot[med2] = mrng.choice(vec[med2], size=nm2, replace=True) + d
                obs = mean_delta(boot, med2, ~med2)
                null = mean_delta_vec(boot, PERMS_MDE, nm2, n2)
                pp, _ = one_sided_p(obs, null)
                if not np.isnan(pp) and pp < ALPHA_BON:
                    hits += 1
            if hits / N_MDE_SIM >= MDE_POWER_TARGET:
                found = d
                break
        MDE[ch] = {"mde": found, "units": f"{ch} contrast units", "vec_sd": sd,
                   "power_at_mde": (hits / N_MDE_SIM) if found is not None else None}
    o = results[("R1", "T2_LEGAL_ABLATED", ch)]["observed"]
    mult = (MDE[ch]["mde"] / abs(o)) if (MDE[ch]["mde"] and o) else None
    MDE[ch]["multiple_of_observed"] = mult
    log(f"  {ch:10s} MDE@80% = {MDE[ch]['mde']}  "
        f"(observed {o if o is None else f'{o:+.6f}'}"
        f"{'' if mult is None else f'; MDE = {mult:.2f}x observed'})")

# ----------------------------------------------------------------------------
# 15. Artefacts
# ----------------------------------------------------------------------------

payload = {
    "finding_id": "H-NEW-3090",
    "run_utc": STAMP,
    "prereg_sha256": actual,
    "seed": SEED, "n_perm": N_PERM,
    "k_bonferroni": K_BONFERRONI, "alpha_bon": ALPHA_BON,
    "verdict": VERDICT,
    "ladder_inputs": {"T1_R1": T1_R1, "T2_R1": T2_R1, "T2_R3": T2_R3,
                      "T3_R1_RATIO": T3_R1_RATIO},
    "dominant_channel_T2_R1": DOMINANT,
    "worst_channel_T2_R1": (max(finite, key=finite.get) if finite else None),
    "register_crosstab": {f"{k[0]}|{k[1]}": v for k, v in ct.items()},
    "mixed_strata": MIXED,
    "degenerate_strata": [s for s in strata if s not in MIXED],
    "token_totals": {t: {"BIO": int(TUPLES[t][1].sum()), "AFF": int(TUPLES[t][0].sum())}
                     for t in TUPLES},
    "kappa_operating_range": KAPPA_OP,
    "kappa_full_set": KAPPA_FULL,
    "raw_agreement_operating_range": AGREE_OP,
    "n_operating_range": len(op),
    "proxy_census": census,
    "size_loading": SIZE_LOADING,
    "cells": {f"{t}|{te}|{c}": r for (t, te, c), r in results.items()},
    "ablations": ablations,
    "mde": MDE,
}
wx("results.json", json.dumps(payload, indent=2, ensure_ascii=False, default=str))
wx("run.log", "\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "manifest.txt"), "x", encoding="utf-8") as fh:
    fh.write(f"H-NEW-3090 run {STAMP}\nprereg_sha256={actual}\nseed={SEED}\n"
             f"n_perm={N_PERM}\nalpha_bon={ALPHA_BON}\nverdict={VERDICT}\n"
             f"python={sys.version.split()[0]}\nnumpy={np.__version__}\n"
             "inputs:\n"
             "  data/morphology/quranic-corpus-morphology-0.4.txt\n"
             "  data/revelation-order.csv\n"
             "  data/translations/en.sahih.txt\n"
             "  findings/classical-sources/neuwirth-sinai-genre-labels.tsv\n"
             "  quran-text/quran-min-tashkeel.json\n")
log(f"\nartefacts -> {RUNDIR}")
