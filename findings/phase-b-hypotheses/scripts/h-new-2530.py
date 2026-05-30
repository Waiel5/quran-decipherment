#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2530 — Register-coded discourse grammar: do the function-word + person-grammar
signatures JOINTLY separate the three Quranic registers above a label-shuffle null?

The ONE unifying test of the §10.133 (Wave-Q) convergence. Reuses the existing finding
outputs VERBATIM (no detector recomputed):
  - csv/h-new-2520.json : per-surah wa-idh / fa-lammā / wa-qālū verse-onset counts
  - csv/h-new-2250.json : idhā eschatological conditional-cascade maximal runs
  - csv/h-new-2490.json : thumma-led adjacent doubling-for-emphasis roster (binary)
  - csv/h-new-2390.json : within-verse iltifāt locus catalogue (parent of H-NEW-2500)
  - csv/h-new-2500.json : surah-scale 3/4-register genre proxy (reused verbatim)

Pre-reg: prereg-h-new-2530-register-grammar.md (SHA-256 embedded + verified at runtime).
stdlib only. seed 20260509 (repl 20260511), 10000 perms, Bonferroni k=2, α_bon=0.025.
Direction LOCKED: observed separation EXCEEDS the upper tail of the label-shuffle null.

Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, math, random, hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                     # findings/phase-b-hypotheses
CSV  = os.path.join(ROOT, "csv")
PREREG = os.path.join(ROOT, "prereg-h-new-2530-register-grammar.md")

PREREG_SHA256 = "e840a8477c3ba7e524c4026725b5554e7157ddcaffaf810181d4998c98736cfe"

SEED       = 20260509
SEED_REPL  = 20260511
N_PERM     = 10000
BONF_K     = 2
ALPHA_BON  = 0.025

THREE = ["narrative", "legal_medinan", "eschatological_mufassal"]
FOUR  = ["narrative", "legal_medinan", "eschatological_mufassal", "liturgical_didactic"]
FEATS = ["f_idh", "f_lamma", "f_qalu", "f_idha_cascade", "f_doubling", "f_iltifat_type"]

# ---------------------------------------------------------------------------
# 0. Runtime SHA verification of the locked pre-registration (fail-fast)
# ---------------------------------------------------------------------------
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

actual = sha256_file(PREREG)
if actual != PREREG_SHA256:
    sys.exit(f"[FATAL] pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {actual}")
print(f"[SHA-OK] pre-reg locked SHA-256 verified: {actual}")

def load(name):
    return json.load(open(os.path.join(CSV, name), encoding="utf-8"))

# ---------------------------------------------------------------------------
# 1. Genre proxy — reused verbatim from H-NEW-2500
# ---------------------------------------------------------------------------
d2500 = load("h-new-2500.json")
SURAH_GENRE = {int(k): v for k, v in d2500["genre_proxy"]["surah_genre"].items()}
n_per = {}
for g in FOUR:
    n_per[g] = sum(1 for s in range(1, 115) if SURAH_GENRE[s] == g)
# MW-6 (a): reproduce 2500 n-per-genre
assert n_per == {"narrative": 31, "legal_medinan": 20,
                 "eschatological_mufassal": 40, "liturgical_didactic": 23}, \
    f"genre marginals {n_per} != 2500 (31/20/40/23)"
print(f"[MW-6a] genre marginals reproduced: {n_per}")

# ---------------------------------------------------------------------------
# 2. Verse counts V(s) — from 2520 per-surah 'verses' (cross-checked vs source)
# ---------------------------------------------------------------------------
d2520 = load("h-new-2520.json")
# 2520 per_surah holds counts only; get V(s) from the onset_density tables and the
# canonical source JSON for completeness.
QURAN = os.path.join(os.path.dirname(os.path.dirname(ROOT)), "quran-text", "quran-no-tashkeel.json")
quran = json.load(open(QURAN, encoding="utf-8"))
def verse_count(s):
    # quran-no-tashkeel.json: list of surah dicts with 'verses' list
    su = quran[s - 1] if isinstance(quran, list) else None
    if su is None:
        raise RuntimeError("unexpected quran json shape")
    vs = su.get("verses") or su.get("ayahs") or su.get("ayat")
    return len(vs)
V = {s: verse_count(s) for s in range(1, 115)}
assert V[1] == 7 and V[2] == 286 and V[114] == 6, f"verse-count sanity failed: {V[1]},{V[2]},{V[114]}"
print(f"[verse-counts] V(1)={V[1]} V(2)={V[2]} V(114)={V[114]}  total={sum(V.values())}")

# cross-check the 2520 onset_density tables' 'verses' field agrees with V
for row in d2520["onset_density_top_by_count"] + d2520["onset_density_top_by_density"]:
    assert row["verses"] == V[row["surah"]], \
        f"2520 verses[{row['surah']}]={row['verses']} != V={V[row['surah']]}"
print("[verse-counts] cross-checked against 2520 onset_density tables: OK")

# ---------------------------------------------------------------------------
# 3. Build the 6-feature vector per surah (NO detector recomputed)
# ---------------------------------------------------------------------------
# 3a. onsets (2520)
ps = d2520["per_surah"]
idh = {int(k): v for k, v in ps["idh"].items()}
lam = {int(k): v for k, v in ps["lamma"].items()}
qal = {int(k): v for k, v in ps["qalu"].items()}

# 3b. idhā cascade density (2250)
d2250 = load("h-new-2250.json")
casc_len = {}
casc_surahs = set()
for r in d2250["runs"]["idha"]:
    casc_len[r["surah"]] = casc_len.get(r["surah"], 0) + r["length"]
    casc_surahs.add(r["surah"])

# 3c. thumma-doubling presence (2490, binary)
d2490 = load("h-new-2490.json")
doubling_surahs = set(r["surah"] for r in d2490["verse_grain_roster"])
# MW-6 (c): exactly 6 surah-members
assert len(doubling_surahs) == 6, f"2490 doubling roster surahs={sorted(doubling_surahs)} (expected 6)"
assert doubling_surahs == {74, 75, 78, 82, 94, 102}, f"2490 doubling surahs={sorted(doubling_surahs)}"
print(f"[MW-6c] 2490 doubling roster: {sorted(doubling_surahs)}")

# 3d. iltifāt 3↔1 vs 2↔3 per surah (2390 loci, 2500 type_tags rule verbatim)
d2390 = load("h-new-2390.json")
def type_tags(l):
    """EXACT copy of scripts/h-new-2500.py type_tags (person tags only used here)."""
    tags = []
    if l["person_shift"]:
        a, b = sorted([l["person_from"], l["person_to"]])
        if   (a, b) == (1, 3): tags.append("P_3<->1")
        elif (a, b) == (2, 3): tags.append("P_2<->3")
        elif (a, b) == (1, 2): tags.append("P_1<->2")
    return tags
n31 = {}; n23 = {}
tot31 = tot23 = 0
for l in d2390["all_loci"]:
    s = l["surah"]
    for t in type_tags(l):
        if t == "P_3<->1": n31[s] = n31.get(s, 0) + 1; tot31 += 1
        elif t == "P_2<->3": n23[s] = n23.get(s, 0) + 1; tot23 += 1
# MW-6 (b): reproduce 2500 person-tag marginals
assert tot31 == 3694, f"Σ P_3↔1 = {tot31} != 3694 (2500 col-total)"
assert tot23 == 6471, f"Σ P_2↔3 = {tot23} != 6471 (2500 col-total)"
print(f"[MW-6b] iltifāt person-tag marginals reproduced: P_3↔1={tot31}  P_2↔3={tot23}")

def feature_vector(s):
    v = V[s]
    f_idh   = idh.get(s, 0) / v
    f_lamma = lam.get(s, 0) / v
    f_qalu  = qal.get(s, 0) / v
    f_casc  = casc_len.get(s, 0) / v
    f_dbl   = 1.0 if s in doubling_surahs else 0.0
    a, b = n31.get(s, 0), n23.get(s, 0)
    f_ilt   = (a - b) / (a + b) if (a + b) > 0 else 0.0
    return [f_idh, f_lamma, f_qalu, f_casc, f_dbl, f_ilt]

RAW = {s: feature_vector(s) for s in range(1, 115)}

# ---------------------------------------------------------------------------
# 4. Z-score the feature matrix over a given surah population (labels never matter)
# ---------------------------------------------------------------------------
def zscore_matrix(surahs):
    X = [RAW[s][:] for s in surahs]
    nrow = len(X); ncol = len(FEATS)
    means = [0.0] * ncol; sds = [0.0] * ncol
    for j in range(ncol):
        col = [X[i][j] for i in range(nrow)]
        m = sum(col) / nrow
        var = sum((c - m) ** 2 for c in col) / nrow
        sd = math.sqrt(var)
        means[j] = m; sds[j] = sd
    Z = []
    for i in range(nrow):
        Z.append([(X[i][j] - means[j]) / sds[j] if sds[j] > 0 else 0.0 for j in range(ncol)])
    return Z, means, sds

# ---------------------------------------------------------------------------
# 5. STATISTICS
# ---------------------------------------------------------------------------
def loo_nearest_centroid(Z, labels, classes):
    """Leave-one-out nearest-centroid accuracy. Deterministic tie-break:
    larger class first, then by classes-order index."""
    n = len(Z); ncol = len(Z[0])
    csize = {c: labels.count(c) for c in classes}
    correct = 0
    confusion = {a: {b: 0 for b in classes} for a in classes}
    for i in range(n):
        cent = {}; cnt = {}
        for c in classes:
            cent[c] = [0.0] * ncol; cnt[c] = 0
        for k in range(n):
            if k == i: continue
            lc = labels[k]
            for j in range(ncol): cent[lc][j] += Z[k][j]
            cnt[lc] += 1
        # best class
        best_c = None; best_d = None
        for c in classes:
            if cnt[c] == 0: continue
            mu = [cent[c][j] / cnt[c] for j in range(ncol)]
            d = sum((Z[i][j] - mu[j]) ** 2 for j in range(ncol))
            # tie-break: smaller distance wins; on exact tie prefer larger class then order
            if best_d is None or d < best_d - 1e-12 or (
                abs(d - best_d) <= 1e-12 and (
                    csize[c] > csize[best_c] or
                    (csize[c] == csize[best_c] and classes.index(c) < classes.index(best_c)))):
                best_d = d; best_c = c
        confusion[labels[i]][best_c] += 1
        if best_c == labels[i]:
            correct += 1
    return correct / n, confusion

def anova_f_per_feature(surahs, labels, classes):
    """One-way ANOVA F-ratio per feature on the RAW (un-z) features; returns list of F_j."""
    # group raw features by label
    by = {c: [] for c in classes}
    for s, lab in zip(surahs, labels):
        by[lab].append(RAW[s])
    N = len(surahs); k = len(classes)
    Fs = []
    for j in range(len(FEATS)):
        grand = sum(RAW[s][j] for s in surahs) / N
        ssb = 0.0; ssw = 0.0
        for c in classes:
            grp = [row[j] for row in by[c]]
            ng = len(grp)
            if ng == 0: continue
            mg = sum(grp) / ng
            ssb += ng * (mg - grand) ** 2
            for x in grp: ssw += (x - mg) ** 2
        dfb = k - 1; dfw = N - k
        msb = ssb / dfb if dfb > 0 else 0.0
        msw = ssw / dfw if dfw > 0 else 0.0
        F = msb / msw if msw > 0 else (float("inf") if msb > 0 else 0.0)
        Fs.append(F)
    return Fs

def gaussian_nb_loo(Z, labels, classes):
    """LOO Gaussian naïve-Bayes accuracy (diagonal cov, variance floor)."""
    n = len(Z); ncol = len(Z[0]); VFLOOR = 1e-9
    correct = 0
    for i in range(n):
        # fit on all but i
        stats = {}; prior = {}
        for c in classes:
            rows = [Z[k] for k in range(n) if k != i and labels[k] == c]
            if not rows: continue
            ng = len(rows)
            mu = [sum(r[j] for r in rows) / ng for j in range(ncol)]
            var = [max(sum((r[j] - mu[j]) ** 2 for r in rows) / ng, VFLOOR) for j in range(ncol)]
            stats[c] = (mu, var); prior[c] = ng / (n - 1)
        best_c = None; best_lp = None
        for c in classes:
            if c not in stats: continue
            mu, var = stats[c]
            lp = math.log(prior[c])
            for j in range(ncol):
                lp += -0.5 * math.log(2 * math.pi * var[j]) - (Z[i][j] - mu[j]) ** 2 / (2 * var[j])
            if best_lp is None or lp > best_lp:
                best_lp = lp; best_c = c
        if best_c == labels[i]: correct += 1
    return correct / n

# ---------------------------------------------------------------------------
# 6. Permutation engine
# ---------------------------------------------------------------------------
def run_block(classes, seed, label_tag):
    """Full primary+secondary computation for a given class set; returns dict."""
    surahs = [s for s in range(1, 115) if SURAH_GENRE[s] in classes]
    labels = [SURAH_GENRE[s] for s in surahs]
    Z, means, sds = zscore_matrix(surahs)

    acc_obs, conf = loo_nearest_centroid(Z, labels, classes)
    F_obs = anova_f_per_feature(surahs, labels, classes)
    Fsum_obs = sum(F_obs)
    nb_obs = gaussian_nb_loo(Z, labels, classes)

    rng = random.Random(seed)
    ge_acc = ge_F = ge_nb = 0
    perm_lab = labels[:]
    for _ in range(N_PERM):
        rng.shuffle(perm_lab)
        a, _ = loo_nearest_centroid(Z, perm_lab, classes)
        if a >= acc_obs: ge_acc += 1
        Fp = sum(anova_f_per_feature(surahs, perm_lab, classes))
        if Fp >= Fsum_obs: ge_F += 1
        nbp = gaussian_nb_loo(Z, perm_lab, classes)
        if nbp >= nb_obs: ge_nb += 1
    p_acc = (ge_acc + 1) / (N_PERM + 1)
    p_F   = (ge_F + 1) / (N_PERM + 1)
    p_nb  = (ge_nb + 1) / (N_PERM + 1)

    centroids = {}
    for c in classes:
        rows = [RAW[s] for s, lab in zip(surahs, labels) if lab == c]
        centroids[c] = [round(sum(r[j] for r in rows) / len(rows), 5) for j in range(len(FEATS))]

    return {
        "classes": classes, "n": len(surahs), "seed": seed,
        "loo_nearest_centroid_acc": round(acc_obs, 5), "p_loo": round(p_acc, 6),
        "anova_F_sum": round(Fsum_obs, 4), "p_anova": round(p_F, 6),
        "anova_F_per_feature": {FEATS[j]: round(F_obs[j], 4) for j in range(len(FEATS))},
        "gaussian_nb_loo_acc": round(nb_obs, 5), "p_nb": round(p_nb, 6),
        "confusion_matrix": conf,
        "centroids_raw": centroids,
        "baseline_majority_acc": round(max(labels.count(c) for c in classes) / len(surahs), 5),
    }

# ---------------------------------------------------------------------------
# 7. PRIMARY (3-register) + replication + 4-class robustness
# ---------------------------------------------------------------------------
print(f"\n[PRIMARY 3-register] seed={SEED}, n_perm={N_PERM} …")
primary = run_block(THREE, SEED, "3reg")
print(f"   LOO-NC acc = {primary['loo_nearest_centroid_acc']:.4f}  p={primary['p_loo']:.5f}  "
      f"(majority baseline {primary['baseline_majority_acc']:.4f})")
print(f"   ANOVA F_sum = {primary['anova_F_sum']:.3f}  p={primary['p_anova']:.5f}")
print(f"   NB-LOO acc = {primary['gaussian_nb_loo_acc']:.4f}  p={primary['p_nb']:.5f}")

print(f"[MW-5 replication] seed={SEED_REPL} …")
repl = run_block(THREE, SEED_REPL, "3reg")
print(f"   LOO-NC p={repl['p_loo']:.5f}  ANOVA p={repl['p_anova']:.5f}  NB p={repl['p_nb']:.5f}")

print(f"[MW-3 4-class robustness] seed={SEED} …")
fourclass = run_block(FOUR, SEED, "4reg")
print(f"   LOO-NC acc={fourclass['loo_nearest_centroid_acc']:.4f}  p={fourclass['p_loo']:.5f}  "
      f"ANOVA F_sum={fourclass['anova_F_sum']:.3f}  p={fourclass['p_anova']:.5f}")

# ---------------------------------------------------------------------------
# 8. Verdict (LOCKED criteria)
# ---------------------------------------------------------------------------
h1_pass = primary["p_loo"] < ALPHA_BON
h2_pass = primary["p_anova"] < ALPHA_BON
if h1_pass and h2_pass:
    verdict = "CONFIRMED"
elif h1_pass or h2_pass:
    verdict = "PARTIAL"
else:
    verdict = "NULL"
# reversal check (separation BELOW null lower tail)
reversed_flag = (primary["p_loo"] > (1 - ALPHA_BON)) and (primary["p_anova"] > (1 - ALPHA_BON))
if reversed_flag:
    verdict = "REVERSED"

print(f"\n[VERDICT] H1(LOO) p={primary['p_loo']:.5f} {'PASS' if h1_pass else 'FAIL'} | "
      f"H2(ANOVA) p={primary['p_anova']:.5f} {'PASS' if h2_pass else 'FAIL'} | "
      f"α_bon={ALPHA_BON} → {verdict}")
print(f"[cross-finding-028] mint = {verdict == 'CONFIRMED'}")

# ---------------------------------------------------------------------------
# 9. Per-feature permutation-p (descriptive, MW-7-capped) on PRIMARY
# ---------------------------------------------------------------------------
surahs3 = [s for s in range(1, 115) if SURAH_GENRE[s] in THREE]
labels3 = [SURAH_GENRE[s] for s in surahs3]
F_obs3 = anova_f_per_feature(surahs3, labels3, THREE)
rngf = random.Random(SEED)
ge_each = [0] * len(FEATS)
pl = labels3[:]
for _ in range(N_PERM):
    rngf.shuffle(pl)
    Fp = anova_f_per_feature(surahs3, pl, THREE)
    for j in range(len(FEATS)):
        if Fp[j] >= F_obs3[j]: ge_each[j] += 1
per_feature_p = {FEATS[j]: round((ge_each[j] + 1) / (N_PERM + 1), 6) for j in range(len(FEATS))}
print(f"[per-feature ANOVA p (MW-7-capped)]: {per_feature_p}")

# ---------------------------------------------------------------------------
# 10. Emit JSON
# ---------------------------------------------------------------------------
out = {
    "id": "H-NEW-2530",
    "title": "Register-coded discourse grammar — joint function-word + person-grammar "
             "separability of the three Quranic registers",
    "prereg_sha256": PREREG_SHA256,
    "seed_primary": SEED, "seed_replication": SEED_REPL, "n_perm": N_PERM,
    "bonferroni_k": BONF_K, "alpha_bonferroni": ALPHA_BON,
    "rules_tuple": "(no-tashkeel, QAC-v0.4 features via parents 2250/2390/2490/2500/2520, "
                   "per-surah feature vector, surah-scale 3-register genre proxy [reused H-NEW-2500], "
                   "Hafs-Kufan, Mashriqi)",
    "parents": ["H-NEW-2250", "H-NEW-2490", "H-NEW-2500", "H-NEW-2520"],
    "features": FEATS,
    "feature_sources": {
        "f_idh": "h-new-2520.json per_surah.idh / V", "f_lamma": "h-new-2520.json per_surah.lamma / V",
        "f_qalu": "h-new-2520.json per_surah.qalu / V",
        "f_idha_cascade": "h-new-2250.json runs.idha Σlength / V",
        "f_doubling": "h-new-2490.json verse_grain_roster membership (binary)",
        "f_iltifat_type": "h-new-2390.json all_loci, 2500 type_tags: (n31-n23)/(n31+n23)"},
    "genre_proxy_source": "h-new-2500.json genre_proxy.surah_genre (reused verbatim)",
    "n_per_genre": n_per,
    "iltifat_person_tag_marginals": {"P_3<->1": tot31, "P_2<->3": tot23},
    "doubling_surahs": sorted(doubling_surahs),
    "cascade_surahs": sorted(casc_surahs),
    "raw_feature_vectors": {str(s): {FEATS[j]: round(RAW[s][j], 6) for j in range(len(FEATS))}
                            for s in range(1, 115)},
    "primary_3register": primary,
    "replication_3register": repl,
    "robustness_4class": fourclass,
    "per_feature_anova_p_primary": per_feature_p,
    "h1_loo_pass": h1_pass, "h2_anova_pass": h2_pass,
    "verdict": verdict,
    "mint_cross_finding_028": (verdict == "CONFIRMED"),
}
OUTJ = os.path.join(CSV, "h-new-2530.json")
with open(OUTJ, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"\n[written] {OUTJ}")
print(f"[DONE] verdict={verdict}")
