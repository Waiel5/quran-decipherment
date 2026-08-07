#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2640 — Does the mood/modality system separate deontic command from epistemic
certainty across the three Quranic registers of cross-finding-028-formal?

The ṭalab / khabar division in balāgha, measured. Two indices built from QAC v0.4
feature ATOMS (never substrings):

  DEONTIC   D = imperative verbs + prohibitive-lā jussive + lām-al-amr jussive + IMPN
  EPISTEMIC E = qad/CERT + lām & nūn al-tawkīd + sa-/sawfa + inna

THE CONFOUND: MOOD:JUS is dominated by lam + past-negation, a purely syntactic trigger
with no modal content. Raw MOOD:JUS measures negation, not modality. The governor rule
of prereg §3.2 splits the 1,418 jussives; only 408 (28.8%) are deontic.

Pre-reg: prereg-h-new-2640-modality-register.md (SHA-256 embedded, verified at runtime).
stdlib only. seed 20260509, replication 20260519, 10000 perms, Bonferroni k=4,
α_bon = 0.0125. All four directions LOCKED in the pre-registration before computation.

Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, math, random, hashlib, os, sys, re, datetime, platform

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # findings/phase-b-hypotheses
REPO = os.path.dirname(os.path.dirname(ROOT))      # project root
CSV = os.path.join(ROOT, "csv")
PREREG = os.path.join(ROOT, "prereg-h-new-2640-modality-register.md")

PREREG_SHA256 = "0b300fdb19c351b1692dc06b7163480bdbed642702c02dbf1bf7e9272065de89"

SEED, SEED_REPL = 20260509, 20260519
N_PERM = 10000
BONF_K = 4
ALPHA_BON = 0.05 / BONF_K                          # 0.0125

THREE = ["narrative", "legal_medinan", "eschatological_mufassal"]

QAC_PATH = os.path.join(REPO, "data", "morphology", "quranic-corpus-morphology-0.4.txt")
D2530_PATH = os.path.join(CSV, "h-new-2530.json")
D2500_PATH = os.path.join(CSV, "h-new-2500.json")
QURAN_PATH = os.path.join(REPO, "quran-text", "quran-no-tashkeel.json")

FROZEN = {
    QAC_PATH:   "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    D2530_PATH: "5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c",
    D2500_PATH: "a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25",
    QURAN_PATH: "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
}


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def die(msg):
    raise SystemExit(f"[FATAL] {msg}")


# ---------------------------------------------------------------------------
# 0. Pre-registration + frozen-input verification (fail-fast, SystemExit)
# ---------------------------------------------------------------------------
_actual = sha256_file(PREREG)
if _actual != PREREG_SHA256:
    die(f"pre-reg SHA-256 mismatch\n  expected {PREREG_SHA256}\n  actual   {_actual}")
print(f"[SHA-OK] pre-reg locked: {_actual}")

for path, want in FROZEN.items():
    got = sha256_file(path)
    if got != want:
        die(f"frozen input SHA mismatch for {path}\n  expected {want}\n  actual   {got}")
print(f"[SHA-OK] {len(FROZEN)} frozen inputs verified")


# ---------------------------------------------------------------------------
# 1. QAC v0.4 — atom-level parse. NEVER substring matching.
# ---------------------------------------------------------------------------
ROWS = []
with open(QAC_PATH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts[:4]
        s, v, w, g = (int(x) for x in loc.strip("()").split(":"))
        ROWS.append({"s": s, "v": v, "w": w, "g": g, "form": form,
                     "feats": feats, "atoms": set(feats.split("|")),
                     "seq": feats.split("|")})
ROWS.sort(key=lambda r: (r["s"], r["v"], r["w"], r["g"]))
print(f"[QAC] {len(ROWS)} annotation rows")

_POS = re.compile(r"(?:^|\|)POS:([A-Z]+)(?:\||$)")
_LEM = re.compile(r"(?:^|\|)LEM:([^|]+)")


def pos(r):
    m = _POS.search(r["feats"])
    return m.group(1) if m else None


def lem(r):
    m = _LEM.search(r["feats"])
    return m.group(1) if m else None


def has(r, atom):
    return atom in r["atoms"]


# --- MW-6.6: the substring-vs-atom exhibit -------------------------------
n_sub = sum(1 for r in ROWS if "POS:PRO" in r["feats"])
n_atom = sum(1 for r in ROWS if has(r, "POS:PRO"))
if (n_sub, n_atom) != (3633, 332):
    die(f"MW-6.6 substring exhibit: got {n_sub}/{n_atom}, expected 3633/332")
print(f"[MW-6.6] substring 'POS:PRO' = {n_sub}  vs  atom POS:PRO = {n_atom}  "
      f"({n_sub / n_atom:.1f}x inflation — substring matching LIES)")

# --- corpus geometry -----------------------------------------------------
WORDS = {}
VERSES = {}
for r in ROWS:
    WORDS.setdefault(r["s"], set()).add((r["v"], r["w"]))
    VERSES.setdefault(r["s"], set()).add(r["v"])
NW = {s: len(WORDS[s]) for s in WORDS}
NV = {s: len(VERSES[s]) for s in VERSES}
if not (sum(NW.values()) == 77429 and sum(NV.values()) == 6236 and len(NW) == 114):
    die(f"MW-6.5 geometry: words={sum(NW.values())} verses={sum(NV.values())} surahs={len(NW)}")
print(f"[MW-6.5] word-tokens={sum(NW.values())} verses={sum(NV.values())} surahs={len(NW)}")


# ---------------------------------------------------------------------------
# 2. The jussive governor rule — prereg §3.2, verbatim
# ---------------------------------------------------------------------------
def classify_jussives():
    out = {}
    n = len(ROWS)
    for i, r in enumerate(ROWS):
        if not has(r, "MOOD:JUS"):
            continue
        c = None
        # (1) same orthographic word, preceding segments
        k = i - 1
        while k >= 0 and (ROWS[k]["s"], ROWS[k]["v"], ROWS[k]["w"]) == (r["s"], r["v"], r["w"]):
            if has(ROWS[k], "l:IMPV+"):
                c = "D_lam_amr"
                break
            k -= 1
        # (2) nearest preceding STEM in the same verse
        if c is None:
            j = i - 1
            while j >= 0 and (ROWS[j]["s"], ROWS[j]["v"]) == (r["s"], r["v"]):
                f = ROWS[j]["feats"]
                if f.startswith("PREFIX|"):
                    if has(ROWS[j], "l:IMPV+"):
                        c = "D_lam_amr"
                        break
                    j -= 1
                    continue
                if f.startswith("SUFFIX|"):
                    j -= 1
                    continue
                p, l = pos(ROWS[j]), lem(ROWS[j])
                if p == "PRO" and l == "laA":
                    c = "D_pro_la"
                elif p == "NEG" and l in ("lam", "l~am~aA"):
                    c = "N_lam"
                elif p == "NEG" and l == "laA":
                    c = "X_neg_la"
                elif p == "COND":
                    c = "C_cond"
                elif p == "REL" and l in ("man", "maA"):
                    c = "C_cond_rel"
                break
        # (3) unresolved -> rescan the whole verse before i
        if c is None:
            has_cond = has_impv = False
            j = i - 1
            while j >= 0 and (ROWS[j]["s"], ROWS[j]["v"]) == (r["s"], r["v"]):
                pj, lj = pos(ROWS[j]), lem(ROWS[j])
                if pj == "COND" or (pj == "REL" and lj in ("man", "maA")):
                    has_cond = True
                if has(ROWS[j], "IMPV") or has(ROWS[j], "l:IMPV+"):
                    has_impv = True
                j -= 1
            c = "C_apodosis" if has_cond else ("C_jawab_talab" if has_impv else "R_other")
        out[i] = c
    return out


JUS = classify_jussives()
SPLIT = {}
for c in JUS.values():
    SPLIT[c] = SPLIT.get(c, 0) + 1

LOCKED_SPLIT = {"N_lam": 351, "D_pro_la": 330, "C_cond": 220, "C_apodosis": 189,
                "X_neg_la": 110, "D_lam_amr": 78, "C_jawab_talab": 67,
                "C_cond_rel": 45, "R_other": 28}
if SPLIT != LOCKED_SPLIT:
    die(f"MW-6.4 jussive split mismatch\n  got    {dict(sorted(SPLIT.items()))}\n"
        f"  locked {dict(sorted(LOCKED_SPLIT.items()))}")
print(f"[MW-6.4] jussive split reproduced, Σ={sum(SPLIT.values())}: "
      f"{dict(sorted(SPLIT.items(), key=lambda kv: -kv[1]))}")

_deon_jus = SPLIT["D_pro_la"] + SPLIT["D_lam_amr"]
print(f"[CONFOUND] only {_deon_jus}/1418 jussives ({100 * _deon_jus / 1418:.1f}%) are deontic; "
      f"{SPLIT['N_lam']} are lam-negation")


# ---------------------------------------------------------------------------
# 3. Marker inventories (MW-6.3) and per-surah counts
# ---------------------------------------------------------------------------
def acc_ACC_inna(r):
    return has(r, "POS:ACC") and has(r, "LEM:<in~")


def acc_ACC_anna(r):
    return has(r, "POS:ACC") and has(r, "LEM:>an~")


TOTALS = {
    "MOOD:JUS": sum(1 for r in ROWS if has(r, "MOOD:JUS")),
    "MOOD:SUBJ": sum(1 for r in ROWS if has(r, "MOOD:SUBJ")),
    "POS:CERT": sum(1 for r in ROWS if has(r, "POS:CERT")),
    "POS:PRO": sum(1 for r in ROWS if has(r, "POS:PRO")),
    "IMPV_verb": sum(1 for r in ROWS if has(r, "POS:V") and has(r, "IMPV")),
    "POS:IMPN": sum(1 for r in ROWS if has(r, "POS:IMPN")),
    "l:EMPH+": sum(1 for r in ROWS if has(r, "l:EMPH+")),
    "+n:EMPH": sum(1 for r in ROWS if has(r, "+n:EMPH")),
    "POS:FUT": sum(1 for r in ROWS if has(r, "POS:FUT")),
    "sa+": sum(1 for r in ROWS if has(r, "sa+")),
    "ACC_inna": sum(1 for r in ROWS if acc_ACC_inna(r)),
    "ACC_anna": sum(1 for r in ROWS if acc_ACC_anna(r)),
}
LOCKED_TOTALS = {"MOOD:JUS": 1418, "MOOD:SUBJ": 1330, "POS:CERT": 414, "POS:PRO": 332,
                 "IMPV_verb": 1876, "POS:IMPN": 2, "l:EMPH+": 1001, "+n:EMPH": 243,
                 "POS:FUT": 42, "sa+": 119, "ACC_inna": 1682, "ACC_anna": 362}
if TOTALS != LOCKED_TOTALS:
    die(f"MW-6.3 marker totals mismatch\n  got    {TOTALS}\n  locked {LOCKED_TOTALS}")
print(f"[MW-6.3] marker totals reproduced: {TOTALS}")

SURAHS_ALL = list(range(1, 115))


def zeros():
    return {s: 0 for s in SURAHS_ALL}


cnt_D_T1, cnt_D_T2, cnt_E_T1, cnt_E_T2, cnt_J = zeros(), zeros(), zeros(), zeros(), zeros()
cnt_Nlam, cnt_Ccond = zeros(), zeros()

for i, r in enumerate(ROWS):
    s = r["s"]
    # --- deontic
    d = 0
    if has(r, "POS:V") and has(r, "IMPV"):
        d = 1
    elif has(r, "POS:IMPN"):
        d = 1
    elif i in JUS and JUS[i] in ("D_pro_la", "D_lam_amr"):
        d = 1
    cnt_D_T1[s] += d
    cnt_D_T2[s] += d + (1 if (i in JUS and JUS[i] == "X_neg_la") else 0)
    # --- epistemic
    e = 0
    if has(r, "POS:CERT"):
        e += 1
    if has(r, "l:EMPH+"):
        e += 1
    if has(r, "+n:EMPH"):
        e += 1
    if has(r, "POS:FUT"):
        e += 1
    if has(r, "sa+"):
        e += 1
    if acc_ACC_inna(r):
        e += 1
    cnt_E_T1[s] += e
    cnt_E_T2[s] += e + (1 if acc_ACC_anna(r) else 0)
    # --- the naive instrument + confound buckets
    if has(r, "MOOD:JUS"):
        cnt_J[s] += 1
    if i in JUS and JUS[i] == "N_lam":
        cnt_Nlam[s] += 1
    if i in JUS and JUS[i] in ("C_cond", "C_cond_rel", "C_apodosis", "C_jawab_talab"):
        cnt_Ccond[s] += 1

if sum(cnt_D_T1.values()) != 2286 or sum(cnt_E_T1.values()) != 3501:
    die(f"index totals: D={sum(cnt_D_T1.values())} (want 2286), "
        f"E={sum(cnt_E_T1.values())} (want 3501)")
print(f"[indices] D_T1={sum(cnt_D_T1.values())} E_T1={sum(cnt_E_T1.values())} "
      f"D_T2={sum(cnt_D_T2.values())} E_T2={sum(cnt_E_T2.values())} J={sum(cnt_J.values())}")


# ---------------------------------------------------------------------------
# 4. Register labels — reused through the pointer H-NEW-2530 itself records
# ---------------------------------------------------------------------------
d2500 = json.load(open(D2500_PATH, encoding="utf-8"))
d2530 = json.load(open(D2530_PATH, encoding="utf-8"))
if d2530["genre_proxy_source"] != "h-new-2500.json genre_proxy.surah_genre (reused verbatim)":
    die(f"2530 genre_proxy_source changed: {d2530['genre_proxy_source']!r}")
GENRE = {int(k): v for k, v in d2500["genre_proxy"]["surah_genre"].items()}

marg = {}
for s in SURAHS_ALL:
    marg[GENRE[s]] = marg.get(GENRE[s], 0) + 1
if marg != d2530["n_per_genre"] or marg != {"narrative": 31, "legal_medinan": 20,
                                            "eschatological_mufassal": 40,
                                            "liturgical_didactic": 23}:
    die(f"MW-6.1 genre marginals {marg} != 2530 {d2530['n_per_genre']}")
print(f"[MW-6.1] register marginals reused verbatim: {marg}")

S91 = [s for s in SURAHS_ALL if GENRE[s] in THREE]
LAB91 = [GENRE[s] for s in S91]
if len(S91) != 91:
    die(f"N={len(S91)} != 91")


# ---------------------------------------------------------------------------
# 5. Densities, OLS length-residualisation (prereg §3.5)
# ---------------------------------------------------------------------------
def density(cnt, per="word"):
    if per == "word":
        return {s: 1000.0 * cnt[s] / NW[s] for s in S91}
    return {s: 1000.0 * cnt[s] / NV[s] for s in S91}


def solve(A, b):
    """Gaussian elimination with partial pivoting."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) < 1e-14:
            die("OLS: singular design matrix")
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r == c:
                continue
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def residualise(dens):
    """OLS on [1, log(n_verses), mean words/verse]; returns residuals dict."""
    X = [[1.0, math.log(NV[s]), NW[s] / NV[s]] for s in S91]
    y = [dens[s] for s in S91]
    p = len(X[0])
    XtX = [[sum(X[i][a] * X[i][b] for i in range(len(X))) for b in range(p)] for a in range(p)]
    Xty = [sum(X[i][a] * y[i] for i in range(len(X))) for a in range(p)]
    beta = solve(XtX, Xty)
    return {s: y[i] - sum(beta[j] * X[i][j] for j in range(p)) for i, s in enumerate(S91)}, beta


# ---------------------------------------------------------------------------
# 6. Statistics
# ---------------------------------------------------------------------------
def anova_F(vals, labels):
    """One-way ANOVA F on a single variable. vals aligned with labels."""
    N = len(vals)
    k = len(THREE)
    grand = sum(vals) / N
    ssb = ssw = 0.0
    for c in THREE:
        grp = [vals[i] for i in range(N) if labels[i] == c]
        if not grp:
            continue
        mg = sum(grp) / len(grp)
        ssb += len(grp) * (mg - grand) ** 2
        for x in grp:
            ssw += (x - mg) ** 2
    msb = ssb / (k - 1)
    msw = ssw / (N - k)
    return msb / msw if msw > 0 else (float("inf") if msb > 0 else 0.0)


def centroids(vals, labels):
    out = {}
    for c in THREE:
        grp = [vals[i] for i in range(len(vals)) if labels[i] == c]
        out[c] = sum(grp) / len(grp) if grp else 0.0
    return out


def zcol(vals):
    n = len(vals)
    m = sum(vals) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in vals) / n)
    return [(x - m) / sd if sd > 0 else 0.0 for x in vals]


def loo_exact(Z, labels):
    """Byte-faithful port of scripts/h-new-2530.py loo_nearest_centroid."""
    n = len(Z)
    ncol = len(Z[0])
    csize = {c: labels.count(c) for c in THREE}
    correct = 0
    conf = {a: {b: 0 for b in THREE} for a in THREE}
    for i in range(n):
        cent = {c: [0.0] * ncol for c in THREE}
        cnt = {c: 0 for c in THREE}
        for k in range(n):
            if k == i:
                continue
            lc = labels[k]
            for j in range(ncol):
                cent[lc][j] += Z[k][j]
            cnt[lc] += 1
        best_c = best_d = None
        for c in THREE:
            if cnt[c] == 0:
                continue
            mu = [cent[c][j] / cnt[c] for j in range(ncol)]
            d = sum((Z[i][j] - mu[j]) ** 2 for j in range(ncol))
            if best_d is None or d < best_d - 1e-12 or (
                abs(d - best_d) <= 1e-12 and (
                    csize[c] > csize[best_c] or
                    (csize[c] == csize[best_c] and THREE.index(c) < THREE.index(best_c)))):
                best_d, best_c = d, c
        conf[labels[i]][best_c] += 1
        if best_c == labels[i]:
            correct += 1
    return correct / n, conf


def loo_fast(Z, labels):
    """Same classifier, O(n·k·d): class sums computed once, held-out point subtracted.
    Gated against loo_exact on the observed data before any null uses it."""
    n = len(Z)
    ncol = len(Z[0])
    csize = {c: labels.count(c) for c in THREE}
    tot = {c: [0.0] * ncol for c in THREE}
    for k in range(n):
        lc = labels[k]
        for j in range(ncol):
            tot[lc][j] += Z[k][j]
    correct = 0
    conf = {a: {b: 0 for b in THREE} for a in THREE}
    for i in range(n):
        li = labels[i]
        best_c = best_d = None
        for c in THREE:
            m = csize[c] - (1 if c == li else 0)
            if m == 0:
                continue
            if c == li:
                mu = [(tot[c][j] - Z[i][j]) / m for j in range(ncol)]
            else:
                mu = [tot[c][j] / m for j in range(ncol)]
            d = sum((Z[i][j] - mu[j]) ** 2 for j in range(ncol))
            if best_d is None or d < best_d - 1e-12 or (
                abs(d - best_d) <= 1e-12 and (
                    csize[c] > csize[best_c] or
                    (csize[c] == csize[best_c] and THREE.index(c) < THREE.index(best_c)))):
                best_d, best_c = d, c
        conf[li][best_c] += 1
        if best_c == li:
            correct += 1
    return correct / n, conf


# ---------------------------------------------------------------------------
# 7. MW-6.2 — reproduce the published H-NEW-2530 six-feature classifier exactly
# ---------------------------------------------------------------------------
FEATS6 = d2530["features"]
RAW6 = {int(k): [v[f] for f in FEATS6] for k, v in d2530["raw_feature_vectors"].items()}
Z6 = [list(col) for col in zip(*[zcol([RAW6[s][j] for s in S91]) for j in range(6)])]
acc6, conf6 = loo_exact(Z6, LAB91)
pub = d2530["primary_3register"]
if round(acc6, 5) != pub["loo_nearest_centroid_acc"]:
    die(f"MW-6.2 LOO6 {acc6:.5f} != published {pub['loo_nearest_centroid_acc']}")
if conf6 != pub["confusion_matrix"]:
    die(f"MW-6.2 confusion mismatch\n  got {conf6}\n  pub {pub['confusion_matrix']}")
LEGAL_RECALL_6 = conf6["legal_medinan"]["legal_medinan"]
if LEGAL_RECALL_6 != 8:
    die(f"MW-6.2 legal recall {LEGAL_RECALL_6} != 8")
print(f"[MW-6.2] H-NEW-2530 six-feature classifier reproduced EXACTLY: "
      f"LOO={acc6:.5f}, legal recall {LEGAL_RECALL_6}/20")

acc6f, conf6f = loo_fast(Z6, LAB91)
if (round(acc6f, 12), conf6f) != (round(acc6, 12), conf6):
    die("loo_fast disagrees with loo_exact on observed data — fast path refused")
print("[gate] loo_fast == loo_exact on observed data; fast path enabled for nulls")


# ---------------------------------------------------------------------------
# 8. Permutation machinery
# ---------------------------------------------------------------------------
NVS = sorted(NV[s] for s in S91)
T33 = NVS[int(round(0.333 * (len(NVS) - 1)))]
T67 = NVS[int(round(0.667 * (len(NVS) - 1)))]


def stratum(s):
    return 0 if NV[s] <= T33 else (1 if NV[s] <= T67 else 2)


STRATA = {}
for idx, s in enumerate(S91):
    STRATA.setdefault(stratum(s), []).append(idx)
print(f"[Null B] length tertile cuts at n_verses <= {T33} / <= {T67}; "
      f"strata sizes {[len(v) for k, v in sorted(STRATA.items())]}")


def shuffled_labels(rng, mode):
    if mode == "A":
        p = LAB91[:]
        rng.shuffle(p)
        return p
    p = LAB91[:]
    for _, idxs in sorted(STRATA.items()):
        sub = [p[i] for i in idxs]
        rng.shuffle(sub)
        for i, lab in zip(idxs, sub):
            p[i] = lab
    return p


def pval(ge):
    return (ge + 1) / (N_PERM + 1)


# ---------------------------------------------------------------------------
# 9. The four registered inferences, per rules-tuple
# ---------------------------------------------------------------------------
def run_tuple(name, cntD, cntE, per):
    dens = {"D": density(cntD, per), "E": density(cntE, per), "J": density(cnt_J, per),
            "N_lam": density(cnt_Nlam, per), "C_cond": density(cnt_Ccond, per)}
    resid, betas = {}, {}
    for k in dens:
        resid[k], betas[k] = residualise(dens[k])

    vD = [resid["D"][s] for s in S91]
    vE = [resid["E"][s] for s in S91]
    vJ = [resid["J"][s] for s in S91]

    F_D, F_E, F_J = anova_F(vD, LAB91), anova_F(vE, LAB91), anova_F(vJ, LAB91)
    dF = F_D - F_J
    cD, cE, cJ = centroids(vD, LAB91), centroids(vE, LAB91), centroids(vJ, LAB91)
    argD = max(cD, key=cD.get)
    argE = max(cE, key=cE.get)
    argJ = max(cJ, key=cJ.get)

    # --- I3: eight-feature classifier
    zD, zE = zcol(vD), zcol(vE)
    Z8 = [Z6[i] + [zD[i], zE[i]] for i in range(len(S91))]
    acc8, conf8 = loo_exact(Z8, LAB91)
    a8f, c8f = loo_fast(Z8, LAB91)
    if (round(a8f, 12), c8f) != (round(acc8, 12), conf8):
        die("loo_fast/exact disagree on the 8-feature observed vector")
    delta = acc8 - acc6

    out = {
        "tuple": name, "denominator": per,
        "beta_D": [round(b, 6) for b in betas["D"]],
        "beta_E": [round(b, 6) for b in betas["E"]],
        "raw_density_by_register": {
            k: {c: round(v, 4) for c, v in
                centroids([dens[k][s] for s in S91], LAB91).items()} for k in dens},
        "resid_density_by_register": {
            "D": {c: round(v, 4) for c, v in cD.items()},
            "E": {c: round(v, 4) for c, v in cE.items()},
            "J_rawJUS": {c: round(v, 4) for c, v in cJ.items()},
            "N_lam": {c: round(v, 4) for c, v in
                      centroids([resid["N_lam"][s] for s in S91], LAB91).items()},
            "C_cond": {c: round(v, 4) for c, v in
                       centroids([resid["C_cond"][s] for s in S91], LAB91).items()},
        },
        "F_D": round(F_D, 4), "F_E": round(F_E, 4), "F_J_rawJUS": round(F_J, 4),
        "delta_F": round(dF, 4),
        "argmax_D": argD, "argmax_E": argE, "argmax_J_rawJUS": argJ,
        "loo6": round(acc6, 5), "loo8": round(acc8, 5), "delta_loo": round(delta, 5),
        "confusion8": conf8,
        "legal_recall_6": LEGAL_RECALL_6,
        "legal_recall_8": conf8["legal_medinan"]["legal_medinan"],
        "nulls": {},
    }

    for mode in ("A", "B"):
        for sd, tag in ((SEED, "primary"), (SEED_REPL, "replication")):
            rng = random.Random(sd)
            ge_D = ge_E = ge_dF = 0
            for _ in range(N_PERM):
                pl = shuffled_labels(rng, mode)
                if anova_F(vD, pl) >= F_D:
                    ge_D += 1
                if anova_F(vE, pl) >= F_E:
                    ge_E += 1
                if anova_F(vD, pl) - anova_F(vJ, pl) >= dF:
                    ge_dF += 1
            # I3 null: permute (zD, zE) as a bound pair across surahs
            rng3 = random.Random(sd)
            order = list(range(len(S91)))
            ge_delta = 0
            for _ in range(N_PERM):
                rng3.shuffle(order)
                Zp = [Z6[i] + [zD[order[i]], zE[order[i]]] for i in range(len(S91))]
                ap, _c = loo_fast(Zp, LAB91)
                if (ap - acc6) >= delta:
                    ge_delta += 1
            out["nulls"][f"{mode}_{tag}"] = {
                "p_I1_F_D": round(pval(ge_D), 6),
                "p_I2_F_E": round(pval(ge_E), 6),
                "p_I3_delta_loo": round(pval(ge_delta), 6),
                "p_I4_delta_F": round(pval(ge_dF), 6),
            }

    pa = out["nulls"]["A_primary"]
    out["verdicts"] = {
        "I1_deontic": {
            "p": pa["p_I1_F_D"], "direction_locked": "legal_medinan", "direction_observed": argD,
            "p_pass": pa["p_I1_F_D"] < ALPHA_BON, "direction_pass": argD == "legal_medinan",
            "PASS": pa["p_I1_F_D"] < ALPHA_BON and argD == "legal_medinan"},
        "I2_epistemic": {
            "p": pa["p_I2_F_E"], "direction_locked": "eschatological_mufassal",
            "direction_observed": argE,
            "p_pass": pa["p_I2_F_E"] < ALPHA_BON,
            "direction_pass": argE == "eschatological_mufassal",
            "PASS": pa["p_I2_F_E"] < ALPHA_BON and argE == "eschatological_mufassal"},
        "I3_orthogonality": {
            "p": pa["p_I3_delta_loo"], "direction_locked": "delta >= 0",
            "delta_observed": round(delta, 5),
            "p_pass": pa["p_I3_delta_loo"] < ALPHA_BON, "direction_pass": delta >= 0,
            "PASS": pa["p_I3_delta_loo"] < ALPHA_BON and delta >= 0},
        "I4_confound": {
            "p": pa["p_I4_delta_F"], "direction_locked": "delta_F > 0",
            "delta_F_observed": round(dF, 4),
            "p_pass": pa["p_I4_delta_F"] < ALPHA_BON, "direction_pass": dF > 0,
            "PASS": pa["p_I4_delta_F"] < ALPHA_BON and dF > 0,
            "locked_descriptive_rawJUS_argmax_not_legal": argJ != "legal_medinan"},
    }
    return out


print(f"\n[RUN] Bonferroni k={BONF_K}, α_bon={ALPHA_BON}, n_perm={N_PERM}, "
      f"seeds {SEED}/{SEED_REPL}")
RESULTS = {}
for nm, cD, cE, per in (("T1_primary", cnt_D_T1, cnt_E_T1, "word"),
                        ("T2_sensitivity_A", cnt_D_T2, cnt_E_T2, "word"),
                        ("T3_sensitivity_B", cnt_D_T1, cnt_E_T1, "verse")):
    print(f"  … {nm}")
    RESULTS[nm] = run_tuple(nm, cD, cE, per)
    r = RESULTS[nm]
    print(f"     F_D={r['F_D']} (argmax {r['argmax_D']})  F_E={r['F_E']} (argmax {r['argmax_E']})  "
          f"F_rawJUS={r['F_J_rawJUS']} (argmax {r['argmax_J_rawJUS']})")
    print(f"     LOO6={r['loo6']} -> LOO8={r['loo8']}  Δ={r['delta_loo']}  "
          f"legal recall {r['legal_recall_6']}/20 -> {r['legal_recall_8']}/20")
    print(f"     p: {r['nulls']['A_primary']}")

# ---------------------------------------------------------------------------
# 10. Verdict, incl. the §7 tuple-fragility rule
# ---------------------------------------------------------------------------
T1 = RESULTS["T1_primary"]["verdicts"]
FINAL = {}
for inf in ("I1_deontic", "I2_epistemic", "I3_orthogonality", "I4_confound"):
    if not T1[inf]["PASS"]:
        reversed_dir = not T1[inf]["direction_pass"]
        FINAL[inf] = "REVERSED-PRECOMMIT-VIOLATION" if reversed_dir else "NULL"
    else:
        t2 = RESULTS["T2_sensitivity_A"]["verdicts"][inf]["PASS"]
        t3 = RESULTS["T3_sensitivity_B"]["verdicts"][inf]["PASS"]
        FINAL[inf] = "PASS" if (t2 or t3) else "RULES-TUPLE-FRAGILE"

if all(v == "PASS" for v in FINAL.values()):
    VERDICT = "CONFIRMED"
elif any(v == "REVERSED-PRECOMMIT-VIOLATION" for v in FINAL.values()):
    VERDICT = "PARTIAL-WITH-PRECOMMIT-VIOLATION"
elif any(v in ("PASS", "RULES-TUPLE-FRAGILE") for v in FINAL.values()):
    VERDICT = "PARTIAL"
else:
    VERDICT = "NULL"

print(f"\n[VERDICT] {FINAL}\n[OVERALL] {VERDICT}")

# ---------------------------------------------------------------------------
# 11. Immutable run directory
# ---------------------------------------------------------------------------
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join(ROOT, "runs", "h-new-2640", stamp)
if os.path.exists(RUNDIR):
    die(f"run directory already exists (immutability): {RUNDIR}")
os.makedirs(RUNDIR)

result = {
    "id": "H-NEW-2640",
    "title": "Modality and register — deontic command vs epistemic certainty across the "
             "three Quranic registers",
    "prereg_sha256": PREREG_SHA256,
    "seed": SEED, "seed_replication": SEED_REPL, "n_perm": N_PERM,
    "bonferroni_k": BONF_K, "alpha_bonferroni": ALPHA_BON,
    "rules_tuple_primary": "(QAC-v0.4 pipe-atom exact matching, orthographic-word-token "
                           "denominator, basmala-counted-only-in-Q1 as QAC encodes it, "
                           "D = IMPV + D_pro_la + D_lam_amr + IMPN, E = CERT + EMPH{l:EMPH+,+n:EMPH} "
                           "+ FUT{POS:FUT,sa+} + ACC^LEM:<in~, OLS residualisation on "
                           "[log n_verses, mean words/verse], Hafs-Kufan, Mashriqi)",
    "register_label_source": "csv/h-new-2500.json genre_proxy.surah_genre, via the pointer "
                             "recorded in csv/h-new-2530.json (reused verbatim, never re-derived)",
    "n_per_register": marg,
    "n_primary": len(S91),
    "corpus_geometry": {"word_tokens": sum(NW.values()), "verses": sum(NV.values()),
                        "surahs": len(NW)},
    "substring_vs_atom_exhibit": {"substring_POS:PRO": n_sub, "atom_POS:PRO": n_atom,
                                  "inflation": round(n_sub / n_atom, 2)},
    "frontier_map_label_corrections": {
        "POS:EMPH": "no such POS tag in QAC; EMPH is a clitic tag: l:EMPH+ 1001 + "
                    "+n:EMPH 243 = 1244",
        "POS:FUT": "POS:FUT alone = 42 (sawfa); sa+ prefix = 119; 42+119 = 161"},
    "marker_totals": TOTALS,
    "jussive_split": SPLIT,
    "jussive_deontic_fraction": round(_deon_jus / 1418, 4),
    "index_totals": {"D_T1": sum(cnt_D_T1.values()), "E_T1": sum(cnt_E_T1.values()),
                     "D_T2": sum(cnt_D_T2.values()), "E_T2": sum(cnt_E_T2.values()),
                     "rawJUS": sum(cnt_J.values())},
    "mw6_controls": {
        "prereg_sha_verified": True, "frozen_inputs_verified": True,
        "genre_marginals_reproduced": True,
        "h_new_2530_six_feature_loo_reproduced": round(acc6, 5),
        "h_new_2530_confusion_reproduced": conf6,
        "loo_fast_equals_loo_exact": True,
        "length_tertile_cuts": [T33, T67]},
    "per_surah_indices": {str(s): {"n_words": NW[s], "n_verses": NV[s],
                                   "register": GENRE[s],
                                   "D_count": cnt_D_T1[s], "E_count": cnt_E_T1[s],
                                   "rawJUS_count": cnt_J[s], "N_lam_count": cnt_Nlam[s]}
                          for s in S91},
    "tuples": RESULTS,
    "inference_verdicts": FINAL,
    "verdict": VERDICT,
}
with open(os.path.join(RUNDIR, "result.json"), "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

manifest = {
    "id": "H-NEW-2640",
    "utc": stamp,
    "script_sha256": sha256_file(os.path.abspath(__file__)),
    "prereg_sha256": PREREG_SHA256,
    "inputs_sha256": {os.path.relpath(p, REPO): FROZEN[p] for p in FROZEN},
    "python": platform.python_version(),
    "seeds": {"primary": SEED, "replication": SEED_REPL},
    "n_perm": N_PERM,
    "bonferroni_k": BONF_K,
    "alpha_bonferroni": ALPHA_BON,
    "verdict": VERDICT,
    "immutability": "This run directory is immutable. Per prereg §8 it must never be "
                    "deleted or overwritten, including if superseded or uncommitted.",
}
with open(os.path.join(RUNDIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

with open(os.path.join(CSV, "h-new-2640.json"), "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\n[run] {RUNDIR}")
print(f"[csv] {os.path.join(CSV, 'h-new-2640.json')}")
