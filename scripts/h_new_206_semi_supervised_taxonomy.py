#!/usr/bin/env python3
"""H-NEW-206 — Semi-supervised surah taxonomy.

Build a per-surah feature matrix from multiple Phase-B findings, run
multiple clustering algorithms, pick best-k by silhouette, interpret
cluster centers, name each cluster per classical balāgha taxonomy
(descriptive), and report hub-surah cluster memberships.

Pre-reg:
/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-206-prereg.md

Seed: 20260419
Bonferroni k = 2 (two principal inferences).
"""
import csv
import json
import re
from pathlib import Path
import numpy as np

from sklearn.cluster import KMeans, HDBSCAN
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from scipy.stats import chi2_contingency, spearmanr

ROOT = Path("/Users/grey/Downloads/quran")
OUT = ROOT / "findings" / "phase-b-hypotheses" / "h-new-206-work"
CSV_DIR = ROOT / "findings" / "phase-b-hypotheses" / "csv"
OUT.mkdir(parents=True, exist_ok=True)

SEED = 20260419
BON_K = 2
ALPHA_BON = 0.05 / BON_K

rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------
# 1. Load surah text & basic stats
# ---------------------------------------------------------------
with open(ROOT / "quran-text" / "quran-no-tashkeel.json") as f:
    SURAHS_RAW = json.load(f)

SURAHS = {}
for s in SURAHS_RAW:
    sid = s["id"]
    verses = []
    for v in s["verses"]:
        toks = v["text"].split()
        verses.append({"text": v["text"], "tokens": toks, "wc": len(toks)})
    SURAHS[sid] = {
        "name": s["transliteration"],
        "type": s["type"],
        "n_verses": len(verses),
        "verses": verses,
    }
SIDS = sorted(SURAHS.keys())
assert len(SIDS) == 114

# muqaṭṭāʿat letter-sets (from H-NEW-125)
MUQ_LETTERS = {
    2: set("الم"), 3: set("الم"), 7: set("المص"), 10: set("الر"), 11: set("الر"),
    12: set("الر"), 13: set("المر"), 14: set("الر"), 15: set("الر"),
    19: set("كهيعص"), 20: set("طه"), 26: set("طسم"), 27: set("طس"), 28: set("طسم"),
    29: set("الم"), 30: set("الم"), 31: set("الم"), 32: set("الم"),
    36: set("يس"), 38: set("ص"), 40: set("حم"), 41: set("حم"), 42: set("حمعسق"),
    43: set("حم"), 44: set("حم"), 45: set("حم"), 46: set("حم"),
    50: set("ق"), 68: set("ن"),
}

# ---------------------------------------------------------------
# 2. Load external feature CSV/JSON sources
# ---------------------------------------------------------------
# 2a. h-new-187-per-surah.csv → alpha, beta, dispersion, lz_norm_log, gzip_ratio
feat187 = {}
with open(CSV_DIR / "h-new-187-per-surah.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row["surah"])
        def _f(x):
            try:
                return float(x)
            except Exception:
                return np.nan
        feat187[sid] = {
            "alpha": _f(row["zipf_alpha"]),
            "beta": _f(row["heap_beta"]),
            "dispersion": _f(row["dispersion"]),
            "lz_norm_log": _f(row["lz_norm_log"]),
            "gzip_ratio": _f(row["gzip_ratio"]),
        }

# 2b. Nöldeke rank from zipf-per-surah.csv
noldeke = {}
with open(CSV_DIR / "zipf-per-surah.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row["mushaf_order"])
        try:
            noldeke[sid] = int(row["noldeke_order"])
        except Exception:
            noldeke[sid] = np.nan

# 2c. First-root inclusio flag from h-new-156.json
with open(CSV_DIR / "h-new-156.json") as f:
    h156 = json.load(f)
inclusio = {int(k): int(v["inclusio"]) for k, v in h156["per_surah_results"].items()}

# ---------------------------------------------------------------
# 3. Compute H-NEW-125 per-surah axis values
# ---------------------------------------------------------------
# Allah-token rule (H-NEW-71 locked)
ALLOWED_PREFIXES_ALLAH = {"و", "ف", "ب", "ت", "أب", "أف", "أو", "وت", "فت", "فب"}

def is_allah_token(w):
    if not w:
        return False
    if w in ("الله", "اللهم", "آلله", "لله"):
        return True
    if w.endswith("الله") and len(w) > 4:
        return w[: -len("الله")] in ALLOWED_PREFIXES_ALLAH
    return False

QUL_FORMS = {"قل", "قلنا", "فقل", "وقل"}

PROPHET_NAMES = {
    "موسى", "عيسى", "ابراهيم", "إبراهيم", "نوح", "يوسف", "محمد", "هارون", "اسحاق",
    "إسحاق", "يعقوب", "داود", "داوود", "سليمان", "ايوب", "أيوب", "زكريا", "يحيى",
    "اسماعيل", "إسماعيل", "لوط", "هود", "شعيب", "صالح", "يونس", "إلياس", "الياس",
}

LEGAL_ROOT_STEMS = [
    "حرم", "حلل", "احل", "أحل", "حل ", "حكم", "امر", "نهى", "زكاة", "صلاة", "صيام",
    "حج", "طلاق", "نكاح", "ميراث", "وصية", "قصاص", "قتل", "سرقة", "ربا", "دين",
    "شهاد",
]

ESCHAT_STEMS = [
    "قيامة", "جهنم", "جنة", "نار", "حشر", "صور", "يوم الدين", "الساعة", "البعث",
    "الاخرة", "الآخرة", "النار", "بعث", "قبر", "اهوال", "الميزان", "عذاب",
]

BOOK_REF_STEMS = [
    "كتاب", "الكتاب", "قرآن", "القرآن", "تنزيل", "التنزيل", "كتب", "الذكر", "الذكرى",
    "الفرقان", "الزبور",
]

# 99 divine names (approximate short list of distinctive name-tokens)
DIVINE_NAMES = {
    "الرحمن", "الرحيم", "الملك", "القدوس", "السلام", "المؤمن", "المهيمن", "العزيز",
    "الجبار", "المتكبر", "الخالق", "البارئ", "المصور", "الغفار", "القهار", "الوهاب",
    "الرزاق", "الفتاح", "العليم", "القابض", "الباسط", "الخافض", "الرافع", "المعز",
    "المذل", "السميع", "البصير", "الحكم", "العدل", "اللطيف", "الخبير", "الحليم",
    "العظيم", "الغفور", "الشكور", "العلي", "الكبير", "الحفيظ", "المقيت", "الحسيب",
    "الجليل", "الكريم", "الرقيب", "المجيب", "الواسع", "الحكيم", "الودود", "المجيد",
    "الباعث", "الشهيد", "الحق", "الوكيل", "القوي", "المتين", "الولي", "الحميد",
    "المحصي", "المبدئ", "المعيد", "المحيي", "المميت", "الحي", "القيوم", "الواجد",
    "الماجد", "الواحد", "الاحد", "الأحد", "الصمد", "القادر", "المقتدر", "المقدم",
    "المؤخر", "الاول", "الأول", "الاخر", "الآخر", "الظاهر", "الباطن", "الوالي",
    "المتعال", "البر", "التواب", "المنتقم", "العفو", "الرؤوف", "الغني", "المغني",
    "المانع", "الضار", "النافع", "النور", "الهادي", "البديع", "الباقي", "الوارث",
    "الرشيد", "الصبور",
}

PRONOUNS = {
    "هو", "هي", "هم", "هن", "هما", "انا", "أنا", "انت", "أنت", "انتم", "أنتم",
    "انتن", "أنتن", "نحن", "انتما", "أنتما",
}

LOANWORD_PROXY = {
    # compact subset of Jeffery-218 high-frequency non-Arabic loan proxies
    "سجيل", "صراط", "فردوس", "تابوت", "جبريل", "ميكال", "قسط", "قسطاس", "قنطار",
    "يس", "طه", "هاروت", "ماروت", "اسرائيل", "إسرائيل", "ابليس", "إبليس",
    "قسورة", "ابلق", "سرادق", "زبور", "رقيم",
}


def token_in_set(tok, s):
    return tok in s


def allah_density(tokens, n_v):
    if n_v == 0:
        return 0.0
    c = sum(1 for t in tokens if is_allah_token(t))
    return c / n_v * 100


def simple_density(tokens, n_v, target_set):
    if n_v == 0:
        return 0.0
    c = sum(1 for t in tokens if t in target_set)
    return c / n_v * 100


def stem_density(tokens, n_v, stems):
    if n_v == 0:
        return 0.0
    c = 0
    for t in tokens:
        for st in stems:
            if st in t:
                c += 1
                break
    return c / n_v * 100


# Build H-NEW-125 per-surah axes
h125 = {}
for sid, d in SURAHS.items():
    all_tokens = [t for v in d["verses"] for t in v["tokens"]]
    n_v = d["n_verses"]
    mean_verse_len = (sum(v["wc"] for v in d["verses"]) / n_v) if n_v > 0 else 0.0
    h125[sid] = {
        "surah_length": n_v,
        "mean_verse_length": mean_verse_len,
        "allah_density": allah_density(all_tokens, n_v),
        "qul_density": simple_density(all_tokens, n_v, QUL_FORMS),
        "prophet_density": simple_density(all_tokens, n_v, PROPHET_NAMES),
        "legal_density": stem_density(all_tokens, n_v, LEGAL_ROOT_STEMS),
        "eschat_density": stem_density(all_tokens, n_v, ESCHAT_STEMS),
        "book_ref_density": stem_density(all_tokens, n_v, BOOK_REF_STEMS),
        "divine_name_density": simple_density(all_tokens, n_v, DIVINE_NAMES),
        "loanword_density": simple_density(all_tokens, n_v, LOANWORD_PROXY),
        "muq_cardinality": len(MUQ_LETTERS[sid]) if sid in MUQ_LETTERS else 0,
    }

# ---------------------------------------------------------------
# 4. Compute per-surah MF-DFA width Δα (H-NEW-166 methodology)
# ---------------------------------------------------------------
def mfdfa_width(x, qs=(-3, -2, -1, 0, 1, 2, 3), order=1, min_scale=4):
    """Compute multifractal width Δα = α_max − α_min from small MF-DFA.

    x: 1-D sequence of verse-word-counts within a surah.
    Returns width (float) or np.nan if not enough scales.
    """
    x = np.asarray(x, dtype=float)
    N = len(x)
    if N < 30:
        return np.nan
    y = np.cumsum(x - np.mean(x))
    # pick log-spaced scales
    max_scale = max(min_scale + 2, N // 4)
    if max_scale <= min_scale:
        return np.nan
    n_steps = min(6, max(3, int(np.log2(max_scale / min_scale)) + 1))
    scales = np.unique(np.round(np.logspace(
        np.log10(min_scale), np.log10(max_scale), n_steps)).astype(int))
    scales = scales[scales >= min_scale]
    if len(scales) < 3:
        return np.nan
    qs_arr = np.array(qs, dtype=float)
    Fq = np.full((len(scales), len(qs_arr)), np.nan)
    for si, scale in enumerate(scales):
        n_seg = N // scale
        if n_seg < 2:
            continue
        t = np.arange(scale)
        F2 = []
        for start in range(0, n_seg * scale, scale):
            seg = y[start: start + scale]
            coef = np.polyfit(t, seg, order)
            trend = np.polyval(coef, t)
            F2.append(np.mean((seg - trend) ** 2))
        for start in range(N - n_seg * scale, N - scale + 1, scale):
            seg = y[start: start + scale]
            coef = np.polyfit(t, seg, order)
            trend = np.polyval(coef, t)
            F2.append(np.mean((seg - trend) ** 2))
        F2 = np.array(F2)
        F2_pos = F2[F2 > 1e-12]
        if len(F2_pos) < 2:
            continue
        for qi, q in enumerate(qs_arr):
            if abs(q) < 1e-8:
                Fq[si, qi] = np.exp(0.5 * np.mean(np.log(F2_pos)))
            else:
                Fq[si, qi] = (np.mean(F2_pos ** (q / 2.0))) ** (1.0 / q)
    # Compute h(q) by log-log fit
    logs = np.log(scales)
    hq = np.full(len(qs_arr), np.nan)
    for qi in range(len(qs_arr)):
        y_ = Fq[:, qi]
        mask = np.isfinite(y_) & (y_ > 0)
        if mask.sum() < 3:
            continue
        slope, _ = np.polyfit(logs[mask], np.log(y_[mask]), 1)
        hq[qi] = slope
    # τ(q) = q*h(q) − 1; α = dτ/dq; width = α_max − α_min
    if np.isnan(hq).any():
        return np.nan
    tau = qs_arr * hq - 1.0
    # central differences for α
    alpha = np.gradient(tau, qs_arr)
    width = float(np.nanmax(alpha) - np.nanmin(alpha))
    return width


mfdfa_by_sid = {}
for sid in SIDS:
    wc_seq = [v["wc"] for v in SURAHS[sid]["verses"]]
    mfdfa_by_sid[sid] = mfdfa_width(wc_seq)

# ---------------------------------------------------------------
# 5. Compute PC1-3 of Hellinger-sqrt word matrix (H-NEW-176 method)
# ---------------------------------------------------------------
from collections import Counter
# Tokenize all surahs; pick top-K by corpus frequency
K_TOP_WORDS = 500
corpus_counter = Counter()
surah_counters = {}
for sid in SIDS:
    c = Counter()
    for v in SURAHS[sid]["verses"]:
        c.update(v["tokens"])
    surah_counters[sid] = c
    corpus_counter.update(c)
top_words = [w for w, _ in corpus_counter.most_common(K_TOP_WORDS)]
word_to_idx = {w: i for i, w in enumerate(top_words)}

# Build 114 × K matrix of probabilities, then sqrt (Hellinger)
M = np.zeros((len(SIDS), K_TOP_WORDS), dtype=float)
for r, sid in enumerate(SIDS):
    c = surah_counters[sid]
    for w, n in c.items():
        if w in word_to_idx:
            M[r, word_to_idx[w]] = n
# Row-normalize to probabilities
row_sums = M.sum(axis=1, keepdims=True)
row_sums[row_sums == 0] = 1.0
M_prob = M / row_sums
M_hell = np.sqrt(M_prob)
# Center columns
M_centered = M_hell - M_hell.mean(axis=0, keepdims=True)
# SVD → top-3 PCs
svd = TruncatedSVD(n_components=3, random_state=SEED)
PC = svd.fit_transform(M_centered)  # 114×3
pc_by_sid = {SIDS[i]: PC[i].tolist() for i in range(len(SIDS))}
explained_ratio_pc123 = svd.explained_variance_ratio_.tolist()

# ---------------------------------------------------------------
# 6. Assemble the master feature matrix
# ---------------------------------------------------------------
FEATURE_NAMES = [
    "alpha", "beta", "dispersion",
    "PC1", "PC2", "PC3",
    "mean_verse_length", "allah_density", "qul_density", "prophet_density",
    "legal_density", "eschat_density", "book_ref_density", "divine_name_density",
    "loanword_density",
    "mfdfa_width",
    "lz_norm_log",
    "inclusio",
    "surah_length",
    "muq_cardinality",
    "noldeke_order",
]

rows = []
for sid in SIDS:
    row = {
        "sid": sid,
        "name": SURAHS[sid]["name"],
        "type": SURAHS[sid]["type"],
        "alpha": feat187.get(sid, {}).get("alpha", np.nan),
        "beta": feat187.get(sid, {}).get("beta", np.nan),
        "dispersion": feat187.get(sid, {}).get("dispersion", np.nan),
        "PC1": pc_by_sid[sid][0],
        "PC2": pc_by_sid[sid][1],
        "PC3": pc_by_sid[sid][2],
        "mean_verse_length": h125[sid]["mean_verse_length"],
        "allah_density": h125[sid]["allah_density"],
        "qul_density": h125[sid]["qul_density"],
        "prophet_density": h125[sid]["prophet_density"],
        "legal_density": h125[sid]["legal_density"],
        "eschat_density": h125[sid]["eschat_density"],
        "book_ref_density": h125[sid]["book_ref_density"],
        "divine_name_density": h125[sid]["divine_name_density"],
        "loanword_density": h125[sid]["loanword_density"],
        "mfdfa_width": mfdfa_by_sid[sid],
        "lz_norm_log": feat187.get(sid, {}).get("lz_norm_log", np.nan),
        "inclusio": inclusio.get(sid, 0),
        "surah_length": h125[sid]["surah_length"],
        "muq_cardinality": h125[sid]["muq_cardinality"],
        "noldeke_order": noldeke.get(sid, np.nan),
    }
    rows.append(row)

# Impute NaNs with column median
X = np.array([[r[k] for k in FEATURE_NAMES] for r in rows], dtype=float)
for j in range(X.shape[1]):
    col = X[:, j]
    mask = np.isnan(col)
    if mask.any():
        med = np.nanmedian(col)
        if np.isnan(med):
            med = 0.0
        X[mask, j] = med

# Save feature matrix
with open(OUT / "feature_matrix.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sid", "name", "type"] + FEATURE_NAMES)
    for i, r in enumerate(rows):
        w.writerow([r["sid"], r["name"], r["type"]] +
                   [f"{X[i, j]:.6g}" for j in range(X.shape[1])])

# Standardize
Xz = StandardScaler().fit_transform(X)

# ---------------------------------------------------------------
# 7. Clustering — k-means k∈{3,4,5,6,7,8,10} + HDBSCAN
# ---------------------------------------------------------------
km_results = {}
for k in [3, 4, 5, 6, 7, 8, 10]:
    km = KMeans(n_clusters=k, n_init=50, random_state=SEED)
    labels = km.fit_predict(Xz)
    sil = float(silhouette_score(Xz, labels))
    ch = float(calinski_harabasz_score(Xz, labels))
    km_results[k] = {
        "labels": labels.tolist(),
        "silhouette": sil,
        "calinski_harabasz": ch,
        "inertia": float(km.inertia_),
        "centers_z": km.cluster_centers_.tolist(),
    }

hdb_results = {}
for mcs in [3, 5, 7]:
    hdb = HDBSCAN(min_cluster_size=mcs)
    labels = hdb.fit_predict(Xz)
    uniq = sorted(set(labels.tolist()))
    n_noise = int(np.sum(labels == -1))
    n_clusters_found = int(sum(1 for u in uniq if u != -1))
    sil = np.nan
    if n_clusters_found >= 2:
        mask = labels != -1
        if mask.sum() >= n_clusters_found + 1:
            try:
                sil = float(silhouette_score(Xz[mask], labels[mask]))
            except Exception:
                sil = np.nan
    hdb_results[mcs] = {
        "labels": labels.tolist(),
        "n_clusters_found": n_clusters_found,
        "n_noise": n_noise,
        "silhouette": sil,
    }

# Pick best-k by silhouette among k-means
best_k = max(km_results.keys(), key=lambda kk: km_results[kk]["silhouette"])
best_silhouette = km_results[best_k]["silhouette"]

# ---------------------------------------------------------------
# 8. Interpret cluster centers (un-standardize for humans)
# ---------------------------------------------------------------
scaler = StandardScaler().fit(X)
labels_best = np.array(km_results[best_k]["labels"])
centers_orig = np.array(km_results[best_k]["centers_z"]) * scaler.scale_ + scaler.mean_

# Per-cluster: compute within-cluster mean (in original units) and size
cluster_summary = {}
for c in range(best_k):
    mask = labels_best == c
    size = int(mask.sum())
    means = {FEATURE_NAMES[j]: float(X[mask, j].mean()) for j in range(X.shape[1])}
    members = [int(SIDS[i]) for i in range(len(SIDS)) if labels_best[i] == c]
    cluster_summary[int(c)] = {
        "size": size,
        "members": members,
        "means": means,
    }

# Save cluster centers CSV
with open(OUT / "cluster_centers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["cluster", "size"] + FEATURE_NAMES)
    for c in range(best_k):
        w.writerow([c, cluster_summary[c]["size"]] +
                   [f"{cluster_summary[c]['means'][fn]:.4g}" for fn in FEATURE_NAMES])

# Save cluster assignments CSV
with open(OUT / "cluster_assignments.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["sid", "name", "type", "cluster_best_k", "best_k",
                *[f"k{kk}_label" for kk in [3, 4, 5, 6, 7, 8, 10]]])
    for i, sid in enumerate(SIDS):
        row = [sid, SURAHS[sid]["name"], SURAHS[sid]["type"],
               int(labels_best[i]), best_k]
        for kk in [3, 4, 5, 6, 7, 8, 10]:
            row.append(int(km_results[kk]["labels"][i]))
        w.writerow(row)

# ---------------------------------------------------------------
# 9. Classical balāgha taxonomy naming heuristic
# ---------------------------------------------------------------
# Ground-truth classical labels:
TIWAL = set([2, 3, 4, 5, 6, 7, 9])  # "seven long" (Yūnus 10 by some)
MIUN = set(range(10, 18))           # al-Mi'ūn
MATHANI = set(range(18, 50))
MUFASSAL = set(range(49, 115))
HAWAMIM = set([40, 41, 42, 43, 44, 45, 46])
MUSABBIHAT = set([17, 57, 59, 61, 62, 64, 87])
ALR_CLUSTER = set([10, 11, 12, 14, 15])

def overlap_score(cluster_members, name_set):
    inter = len(set(cluster_members) & name_set)
    return inter, len(name_set), inter / max(1, len(name_set)), inter / max(1, len(cluster_members))

cluster_names = {}
for c in range(best_k):
    m = set(cluster_summary[c]["members"])
    # Features-based labelling priority
    cm = cluster_summary[c]["means"]
    # Compute qualitative tags
    tags = []
    if cm["mean_verse_length"] >= np.quantile([cluster_summary[cc]["means"]["mean_verse_length"] for cc in range(best_k)], 0.75):
        tags.append("long-verse")
    if cm["mean_verse_length"] <= np.quantile([cluster_summary[cc]["means"]["mean_verse_length"] for cc in range(best_k)], 0.25):
        tags.append("short-verse")
    if cm["legal_density"] >= np.quantile([cluster_summary[cc]["means"]["legal_density"] for cc in range(best_k)], 0.75):
        tags.append("legal-heavy")
    if cm["eschat_density"] >= np.quantile([cluster_summary[cc]["means"]["eschat_density"] for cc in range(best_k)], 0.75):
        tags.append("eschatology-heavy")
    if cm["prophet_density"] >= np.quantile([cluster_summary[cc]["means"]["prophet_density"] for cc in range(best_k)], 0.75):
        tags.append("prophet-narrative-heavy")
    if cm["muq_cardinality"] >= 1.0:
        tags.append("muq-rich")
    # Overlap with classical names
    overlaps = {}
    for label, name_set in [("ṭiwāl", TIWAL), ("mi'ūn", MIUN), ("mathānī", MATHANI),
                            ("mufaṣṣal", MUFASSAL), ("ḥawāmīm", HAWAMIM),
                            ("musabbiḥāt", MUSABBIHAT), ("al-R-cluster", ALR_CLUSTER)]:
        inter, Ntarget, recall, precision = overlap_score(list(m), name_set)
        overlaps[label] = {
            "n_in_cluster_from_target": inter,
            "n_in_target": Ntarget,
            "recall": recall,  # fraction of target captured by this cluster
            "precision": precision,  # fraction of cluster that is target-members
        }
    # Pick best-match label by F1
    def f1(o):
        p, r = o["precision"], o["recall"]
        return (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    best_label = max(overlaps.keys(), key=lambda lb: f1(overlaps[lb]))
    best_f1 = f1(overlaps[best_label])
    cluster_names[c] = {
        "feature_tags": tags,
        "classical_overlaps": overlaps,
        "best_classical_label": best_label if best_f1 >= 0.3 else None,
        "best_classical_label_f1": best_f1,
    }

# ---------------------------------------------------------------
# 10. Hub-surah cluster membership
# ---------------------------------------------------------------
HUBS_PRIMARY = [2, 3, 59, 62]
HUBS_SECONDARY = [18, 36, 50, 68]
ALL_HUBS = HUBS_PRIMARY + HUBS_SECONDARY

hub_report = {}
for sid in ALL_HUBS:
    idx = SIDS.index(sid)
    hub_report[sid] = {
        "name": SURAHS[sid]["name"],
        "cluster_best_k": int(labels_best[idx]),
        "is_primary_hub": sid in HUBS_PRIMARY,
        "labels_by_k": {str(kk): int(km_results[kk]["labels"][idx]) for kk in [3,4,5,6,7,8,10]},
    }

# ---------------------------------------------------------------
# 11. Inference: χ² cluster × muq membership
# ---------------------------------------------------------------
is_muq = np.array([1 if sid in MUQ_LETTERS else 0 for sid in SIDS])
cont = np.zeros((best_k, 2), dtype=int)
for i in range(len(SIDS)):
    cont[int(labels_best[i]), int(is_muq[i])] += 1
chi2, p_chi2, dof, exp = chi2_contingency(cont)
inference_b_pass = bool(p_chi2 < ALPHA_BON)

# Inference (a): silhouette > 0.2
inference_a_pass = bool(best_silhouette > 0.2)

# ---------------------------------------------------------------
# 12. Save artifacts
# ---------------------------------------------------------------
silhouette_scores = {
    "k_means": {str(k): {"silhouette": km_results[k]["silhouette"],
                          "calinski_harabasz": km_results[k]["calinski_harabasz"],
                          "inertia": km_results[k]["inertia"]} for k in km_results},
    "hdbscan": {str(mcs): {k: v for k, v in hdb_results[mcs].items() if k != "labels"}
                 for mcs in hdb_results},
    "best_k": int(best_k),
    "best_silhouette": best_silhouette,
}
with open(OUT / "silhouette_scores.json", "w") as f:
    json.dump(silhouette_scores, f, indent=2, ensure_ascii=False)

with open(OUT / "hub_cluster_report.json", "w") as f:
    json.dump(hub_report, f, indent=2, ensure_ascii=False)

summary_json = {
    "finding_id": "H-NEW-206",
    "title": "Semi-supervised surah taxonomy",
    "seed": SEED,
    "bonferroni_k": BON_K,
    "alpha_bon": ALPHA_BON,
    "n_features": len(FEATURE_NAMES),
    "feature_names": FEATURE_NAMES,
    "n_surahs": len(SIDS),
    "pca_explained_ratio_pc123": explained_ratio_pc123,
    "km_silhouette_by_k": {str(k): km_results[k]["silhouette"] for k in km_results},
    "km_calinski_harabasz_by_k": {str(k): km_results[k]["calinski_harabasz"] for k in km_results},
    "hdb_summary": {str(mcs): {kk: vv for kk, vv in hdb_results[mcs].items() if kk != "labels"}
                     for mcs in hdb_results},
    "best_k": int(best_k),
    "best_silhouette": best_silhouette,
    "inference_a_silhouette_gt_0p2": inference_a_pass,
    "inference_b_cluster_muq_chi2": {
        "chi2": float(chi2),
        "p": float(p_chi2),
        "dof": int(dof),
        "alpha_bon": ALPHA_BON,
        "pass": inference_b_pass,
        "contingency": cont.tolist(),
    },
    "cluster_summary": cluster_summary,
    "cluster_names": cluster_names,
    "hub_cluster_report": hub_report,
}

with open(CSV_DIR / "h-new-206.json", "w") as f:
    json.dump(summary_json, f, indent=2, ensure_ascii=False, default=float)

# Markdown report generator
lines = []
lines.append("# H-NEW-206 — Semi-supervised surah taxonomy (results)\n")
lines.append(f"**seed**: {SEED} | **Bonferroni k** = {BON_K} | α_bon = {ALPHA_BON:.4f}\n")
lines.append("## Silhouette scores (k-means)\n")
lines.append("| k | silhouette | Calinski-Harabasz | inertia |\n|---:|---:|---:|---:|")
for k in sorted(km_results.keys()):
    r = km_results[k]
    lines.append(f"| {k} | {r['silhouette']:.4f} | {r['calinski_harabasz']:.2f} | {r['inertia']:.2f} |")
lines.append("")
lines.append("## HDBSCAN\n")
lines.append("| min_cluster_size | n_clusters_found | n_noise | silhouette |")
lines.append("|---:|---:|---:|---:|")
for mcs in sorted(hdb_results.keys()):
    r = hdb_results[mcs]
    sil_s = f"{r['silhouette']:.4f}" if np.isfinite(r["silhouette"]) else "nan"
    lines.append(f"| {mcs} | {r['n_clusters_found']} | {r['n_noise']} | {sil_s} |")
lines.append("")
lines.append(f"**Best k (silhouette)** = {best_k}, silhouette = {best_silhouette:.4f}\n")
lines.append(f"- Inference (a) silhouette > 0.2 at α_bon = {ALPHA_BON:.4f}: **{'PASS' if inference_a_pass else 'FAIL'}**")
lines.append(f"- Inference (b) χ²(cluster × is-muq): p = {p_chi2:.2e} at α_bon = {ALPHA_BON:.4f}: **{'PASS' if inference_b_pass else 'FAIL'}**\n")
lines.append("## Cluster centers (interpretation)\n")
for c in range(best_k):
    s = cluster_summary[c]
    cn = cluster_names[c]
    lines.append(f"### Cluster {c} — size {s['size']}\n")
    if cn["best_classical_label"] is not None:
        lines.append(f"**Best classical match**: {cn['best_classical_label']} (F1 = {cn['best_classical_label_f1']:.2f})")
    else:
        lines.append(f"**Best classical match**: none (top F1 = {cn['best_classical_label_f1']:.2f})")
    lines.append(f"**Feature tags**: {', '.join(cn['feature_tags']) if cn['feature_tags'] else '—'}\n")
    # Top distinctive features (vs grand mean)
    grand = {fn: float(X[:, j].mean()) for j, fn in enumerate(FEATURE_NAMES)}
    deltas = [(fn, s["means"][fn] - grand[fn]) for fn in FEATURE_NAMES]
    deltas.sort(key=lambda t: abs(t[1]), reverse=True)
    lines.append("Top distinctive features (|Δ from grand mean|):\n")
    lines.append("| feature | cluster mean | grand mean | Δ |\n|---|---:|---:|---:|")
    for fn, d in deltas[:6]:
        lines.append(f"| {fn} | {s['means'][fn]:.3g} | {grand[fn]:.3g} | {d:+.3g} |")
    lines.append("")
    # List members (first 10)
    mem_list = ", ".join(str(m) for m in s["members"][:15])
    more = "" if len(s["members"]) <= 15 else f" … (+{len(s['members']) - 15} more)"
    lines.append(f"**Members** (first 15): {mem_list}{more}\n")
    # Classical overlaps
    lines.append("Classical-label overlaps:\n")
    lines.append("| label | inter | target-size | recall | precision |")
    lines.append("|---|---:|---:|---:|---:|")
    for lab, o in cn["classical_overlaps"].items():
        lines.append(f"| {lab} | {o['n_in_cluster_from_target']} | {o['n_in_target']} | {o['recall']:.2f} | {o['precision']:.2f} |")
    lines.append("")

lines.append("## Hub surah cluster membership\n")
lines.append("| surah | name | primary? | cluster | k=3 | k=4 | k=5 | k=6 | k=7 | k=8 | k=10 |")
lines.append("|---:|---|:-:|---:|---:|---:|---:|---:|---:|---:|---:|")
for sid in ALL_HUBS:
    hr = hub_report[sid]
    row_labels = [str(hr["labels_by_k"][str(kk)]) for kk in [3,4,5,6,7,8,10]]
    lines.append(f"| {sid} | {hr['name']} | {'yes' if hr['is_primary_hub'] else 'no'} | {hr['cluster_best_k']} | " + " | ".join(row_labels) + " |")

with open(ROOT / "findings" / "phase-b-hypotheses" / "h-new-206-semi-supervised-taxonomy.md", "w") as f:
    f.write("\n".join(lines))

# Journal entry
journal_lines = []
journal_lines.append(f"# H-NEW-206 run 1 — {2026}-04-17")
journal_lines.append(f"seed={SEED}, bonferroni_k={BON_K}, n_features={len(FEATURE_NAMES)}")
journal_lines.append(f"best k-means k: {best_k}, silhouette={best_silhouette:.4f}")
journal_lines.append(f"inference (a): {'PASS' if inference_a_pass else 'FAIL'}")
journal_lines.append(f"inference (b): {'PASS' if inference_b_pass else 'FAIL'}, p={p_chi2:.3e}")
journal_lines.append("hub clusters (best_k):")
for sid in ALL_HUBS:
    journal_lines.append(f"  Q{sid} ({hub_report[sid]['name']}): cluster {hub_report[sid]['cluster_best_k']}")
with open(ROOT / "journal" / "h-new-206-run-1.md", "w") as f:
    f.write("\n".join(journal_lines))

print(json.dumps({
    "best_k": best_k,
    "best_silhouette": best_silhouette,
    "silhouette_by_k": {str(k): km_results[k]["silhouette"] for k in km_results},
    "hdb_summary": {str(mcs): {kk: vv for kk, vv in hdb_results[mcs].items() if kk != "labels"}
                     for mcs in hdb_results},
    "inference_a": inference_a_pass,
    "inference_b": {"p": p_chi2, "pass": inference_b_pass},
    "pca_explained": explained_ratio_pc123,
}, indent=2, default=float))
