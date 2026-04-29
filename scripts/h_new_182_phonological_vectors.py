#!/usr/bin/env python3
"""
H-NEW-182 — Phonological feature vector per surah; test clustering.

Pre-reg: findings/phase-b-hypotheses/h-new-182-phonological-vectors-prereg.md
Seed: 20260419
Bonferroni family: k=3, alpha_bon = 0.05 / 3 = 0.01667

Cells:
  A: k-means silhouette (k=4) vs shuffled null
  B: Meccan/Medinan ROC-AUC from emphatic-fraction
  C: Quran-Bukhari Euclidean distance in phonological-vector space
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import roc_auc_score, silhouette_score

SEED = 20260419
N_PERM_SIL = 1000
N_PERM_AUC = 10000
N_BOOT_BUKHARI = 1000
ALPHA_BON = 0.05 / 3

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
BUKHARI_TXT = ROOT / "data" / "baseline-corpora" / "raw" / "bukhari-noquran.txt"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-182.json"
OUT_CSV = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-182-surah-vectors.csv"
OUT_MD = ROOT / "findings" / "phase-b-hypotheses" / "h-new-182-phonological-vectors.md"

# ---------- phonological feature codebook (LOCKED) ----------

PLACE_LABIAL = set("بفمو")
PLACE_ALVEOLAR = set("تدطزسصضلنر")
PLACE_PALATAL = set("جشي")
PLACE_VELAR = set("كق")
PLACE_PHARYNGEAL = set("عحخغ")
PLACE_GLOTTAL = set("ءه")
EMPHATIC = set("صضطظ")
# Classical majhūra (voiced) letters per al-Khalīl / Sībawayh tradition
VOICED = set("بجددذزضظعغلمنروياى")
# Stops (non-continuant)
STOPS = set("بتدطءكقج")

FEATURE_NAMES = [
    "labial", "alveolar", "palatal", "velar",
    "pharyngeal", "glottal", "emphatic", "voiced", "continuant",
]

# Accept main Arabic letter range and alif-with-hamza variants
ARABIC_LETTER_RE = re.compile(r"[\u0621-\u064A\u0671-\u06D3]")


def letter_feature_vector(letter: str) -> np.ndarray:
    """One-hot 9-d feature vector for a single Arabic letter."""
    # normalize some variants: ى → ي (in feature space); أإآ → ا (but these
    # graphemes map to own place-of-articulation rows via hamza / alif rules).
    # We use the letter AS-IS per mashriqi rule — but map alif variants to core
    # membership. The variants ا أ إ آ are all "alif" semantically.
    fv = np.zeros(9, dtype=float)
    # unify alif variants
    alif_variants = {"أ", "إ", "آ", "ٱ"}
    if letter in alif_variants:
        letter = "ا"
    if letter == "ى":
        letter = "ي"
    if letter == "ة":
        letter = "ه"  # ta-marbuta treated as ha for phonology

    fv[0] = 1.0 if letter in PLACE_LABIAL else 0.0
    fv[1] = 1.0 if letter in PLACE_ALVEOLAR else 0.0
    fv[2] = 1.0 if letter in PLACE_PALATAL else 0.0
    fv[3] = 1.0 if letter in PLACE_VELAR else 0.0
    fv[4] = 1.0 if letter in PLACE_PHARYNGEAL else 0.0
    fv[5] = 1.0 if letter in PLACE_GLOTTAL else 0.0
    fv[6] = 1.0 if letter in EMPHATIC else 0.0
    fv[7] = 1.0 if letter in VOICED else 0.0
    fv[8] = 0.0 if letter in STOPS else 1.0
    return fv


def vector_from_text(text: str) -> tuple[np.ndarray, int]:
    """Return mean phonological feature vector + letter count."""
    letters = ARABIC_LETTER_RE.findall(text)
    if not letters:
        return np.zeros(9), 0
    M = np.zeros((len(letters), 9), dtype=float)
    for i, L in enumerate(letters):
        M[i] = letter_feature_vector(L)
    return M.mean(axis=0), len(letters)


def letters_from_text(text: str) -> list[str]:
    return ARABIC_LETTER_RE.findall(text)


# ---------- Quran loading ----------

def load_quran() -> tuple[list[dict], list[str], list[str]]:
    data = json.loads(QURAN_JSON.read_text())
    surahs = []
    types = []
    names = []
    for s in data:
        body = " ".join(v["text"] for v in s["verses"])
        surahs.append({"id": s["id"], "body": body, "type": s["type"]})
        types.append(s["type"])
        names.append(s["name"])
    assert len(surahs) == 114
    return surahs, types, names


# ---------- main ----------

def main() -> None:
    print("=== H-NEW-182 Phonological Feature Vectors per Surah ===", flush=True)
    print(f"Seed: {SEED}   Bonferroni k=3, α_per = {ALPHA_BON:.5f}", flush=True)

    rng = np.random.default_rng(SEED)

    # --- Step 1: load Quran and build per-surah vectors ---
    surahs, types, names = load_quran()
    n_surahs = len(surahs)
    vectors = np.zeros((n_surahs, 9), dtype=float)
    letter_counts = np.zeros(n_surahs, dtype=int)
    all_surah_letters: list[list[str]] = []

    for i, s in enumerate(surahs):
        letters = letters_from_text(s["body"])
        all_surah_letters.append(letters)
        if letters:
            M = np.array([letter_feature_vector(L) for L in letters])
            vectors[i] = M.mean(axis=0)
            letter_counts[i] = len(letters)

    print(f"Built {n_surahs} surah vectors; total letters = {letter_counts.sum()}", flush=True)
    print(f"Shortest surah: Q{surahs[int(np.argmin(letter_counts))]['id']} ({letter_counts.min()} letters)", flush=True)
    print(f"Longest  surah: Q{surahs[int(np.argmax(letter_counts))]['id']} ({letter_counts.max()} letters)", flush=True)

    # MUQ surahs (29)
    MUQ_SURAHS = {2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}

    # --- Step 2: standardize design matrix ---
    mu = vectors.mean(axis=0)
    sd = vectors.std(axis=0)
    sd[sd == 0] = 1.0
    X = (vectors - mu) / sd

    # --- Cell A: k-means silhouette ---
    print("\n=== CELL A: k-means (k=4) silhouette ===", flush=True)
    km = KMeans(n_clusters=4, random_state=SEED, n_init=10)
    labels = km.fit_predict(X)
    observed_sil = float(silhouette_score(X, labels, metric="euclidean"))
    print(f"  observed silhouette = {observed_sil:.4f}", flush=True)

    # cluster composition
    print("  cluster composition (k=4):", flush=True)
    cluster_summary = {}
    for c in range(4):
        idxs = np.where(labels == c)[0]
        if len(idxs) == 0:
            continue
        n_meccan = sum(1 for i in idxs if types[i] == "meccan")
        n_medinan = sum(1 for i in idxs if types[i] == "medinan")
        n_muq = sum(1 for i in idxs if surahs[i]["id"] in MUQ_SURAHS)
        cluster_mean_vec = vectors[idxs].mean(axis=0).round(4).tolist()
        cluster_summary[f"cluster_{c}"] = {
            "size": int(len(idxs)),
            "meccan": int(n_meccan),
            "medinan": int(n_medinan),
            "muq": int(n_muq),
            "mean_vector": {nm: cluster_mean_vec[j] for j, nm in enumerate(FEATURE_NAMES)},
            "surahs": [int(surahs[i]["id"]) for i in idxs],
        }
        print(f"    c={c}: n={len(idxs)} meccan={n_meccan} medinan={n_medinan} muq={n_muq}", flush=True)
        print(f"         means: {dict(zip(FEATURE_NAMES, [round(v,3) for v in cluster_mean_vec]))}", flush=True)

    # Permutation null for silhouette: shuffle rows of X (shuffles column values
    # independently across columns — the right null for "is the clustering
    # structure a function of the joint feature vectors, or of the marginals?").
    # LOCKED: per-feature independent shuffle (standard clustering null).
    print(f"  computing silhouette null (n={N_PERM_SIL})...", flush=True)
    null_sils = np.zeros(N_PERM_SIL)
    rng_local = np.random.default_rng(SEED)
    for i in range(N_PERM_SIL):
        X_sh = X.copy()
        for j in range(X_sh.shape[1]):
            rng_local.shuffle(X_sh[:, j])
        km_n = KMeans(n_clusters=4, random_state=SEED + i + 1, n_init=3)
        lbls_n = km_n.fit_predict(X_sh)
        try:
            null_sils[i] = silhouette_score(X_sh, lbls_n, metric="euclidean")
        except Exception:
            null_sils[i] = 0.0
        if (i + 1) % 200 == 0:
            print(f"    perm {i+1}/{N_PERM_SIL} null_mean={null_sils[:i+1].mean():.4f}", flush=True)

    null_q95 = float(np.quantile(null_sils, 0.95))
    p_sil = float((1 + np.sum(null_sils >= observed_sil)) / (N_PERM_SIL + 1))
    cell_a_pass = (observed_sil > null_q95) and (p_sil < ALPHA_BON)
    print(f"  null mean={null_sils.mean():.4f} q95={null_q95:.4f} max={null_sils.max():.4f}", flush=True)
    print(f"  p_sil = {p_sil:.4f}   PASS_A = {cell_a_pass}", flush=True)

    # --- Cell B: Meccan/Medinan ROC-AUC from emphatic fraction ---
    print("\n=== CELL B: Meccan/Medinan ROC-AUC from emphatic-fraction ===", flush=True)
    emphatic = vectors[:, FEATURE_NAMES.index("emphatic")]
    y_true = np.array([1 if t == "medinan" else 0 for t in types])
    print(f"  n_meccan={int((y_true==0).sum())}   n_medinan={int((y_true==1).sum())}", flush=True)

    observed_auc = float(roc_auc_score(y_true, emphatic))
    if observed_auc < 0.5:
        reported_auc = 1.0 - observed_auc
        flip = True
    else:
        reported_auc = observed_auc
        flip = False
    print(f"  observed AUC = {observed_auc:.4f} (flip={flip}, reported |AUC| = {reported_auc:.4f})", flush=True)

    # two-sided permutation
    print(f"  permutation (n={N_PERM_AUC})...", flush=True)
    rng_b = np.random.default_rng(SEED + 1)
    null_aucs = np.zeros(N_PERM_AUC)
    for i in range(N_PERM_AUC):
        y_sh = rng_b.permutation(y_true)
        null_aucs[i] = roc_auc_score(y_sh, emphatic)

    # two-sided p: fraction at-or-further from 0.5 than observed
    dev_obs = abs(observed_auc - 0.5)
    dev_null = np.abs(null_aucs - 0.5)
    p_auc = float((1 + np.sum(dev_null >= dev_obs)) / (N_PERM_AUC + 1))

    cell_b_pass = (dev_obs >= 0.10) and (p_auc < ALPHA_BON)
    print(f"  null |AUC-0.5| q95 = {np.quantile(dev_null, 0.95):.4f}", flush=True)
    print(f"  p_auc (two-sided) = {p_auc:.4f}   PASS_B = {cell_b_pass}", flush=True)

    # Auxiliary: same test with pharyngeal and voiced (exploratory)
    aux_auc = {}
    for feat in ("pharyngeal", "voiced", "alveolar", "labial"):
        sc = vectors[:, FEATURE_NAMES.index(feat)]
        a = float(roc_auc_score(y_true, sc))
        aux_auc[feat] = {"auc": a, "dev": abs(a - 0.5)}
    print(f"  exploratory (not in bonferroni): {aux_auc}", flush=True)

    # --- Cell C: Quran vs Bukhari phonological distance ---
    print("\n=== CELL C: Quran-vs-Bukhārī phonological-vector distance ===", flush=True)
    bukhari_text = BUKHARI_TXT.read_text()
    bukhari_letters = ARABIC_LETTER_RE.findall(bukhari_text)
    print(f"  Bukhari letter count = {len(bukhari_letters)}", flush=True)

    # Precompute per-letter feature matrix for Bukhari (N×9) — vastly faster
    B_mat = np.array([letter_feature_vector(L) for L in bukhari_letters], dtype=np.float32)
    # Quran per-letter matrix (flatten all surahs)
    all_quran_letters = [L for L_list in all_surah_letters for L in L_list]
    Q_mat = np.array([letter_feature_vector(L) for L in all_quran_letters], dtype=np.float32)

    quran_vec = Q_mat.mean(axis=0)
    bukhari_vec = B_mat.mean(axis=0)
    obs_dist = float(np.linalg.norm(quran_vec - bukhari_vec))

    print(f"  Quran vec:   {dict(zip(FEATURE_NAMES, [round(float(v),4) for v in quran_vec]))}", flush=True)
    print(f"  Bukhari vec: {dict(zip(FEATURE_NAMES, [round(float(v),4) for v in bukhari_vec]))}", flush=True)
    print(f"  observed Quran-Bukhari Euclidean distance = {obs_dist:.6f}", flush=True)

    # Block-bootstrap via cumulative-sum trick: build block-level summary matrix
    # of shape (n_blocks, 9) where each row is the SUM of feature vectors in that block.
    # Mean over sampled blocks = sum(rows) / (n_blocks * block).
    rng_c = np.random.default_rng(SEED + 2)
    block = 100
    n_blocks_total = len(bukhari_letters) // block
    B_trunc = B_mat[:n_blocks_total * block]
    # Reshape: (n_blocks, block, 9) → sum over axis 1 → (n_blocks, 9)
    B_blocks_sum = B_trunc.reshape(n_blocks_total, block, 9).sum(axis=1)

    self_dists = np.zeros(N_BOOT_BUKHARI)
    bukhari_boot_dists_to_quran = np.zeros(N_BOOT_BUKHARI)
    print(f"  computing {N_BOOT_BUKHARI} bootstrap self-distances (block={block}, n_blocks={n_blocks_total})...", flush=True)
    half = n_blocks_total // 2

    for i in range(N_BOOT_BUKHARI):
        # Self-split: permute blocks, take first and second halves
        perm = rng_c.permutation(n_blocks_total)
        a_ids = perm[:half]
        b_ids = perm[half:2 * half]
        va = B_blocks_sum[a_ids].sum(axis=0) / (half * block)
        vb = B_blocks_sum[b_ids].sum(axis=0) / (half * block)
        self_dists[i] = np.linalg.norm(va - vb)
        # Bootstrap Bukhari with replacement at block level
        boot_ids = rng_c.integers(0, n_blocks_total, size=n_blocks_total)
        v_boot = B_blocks_sum[boot_ids].sum(axis=0) / (n_blocks_total * block)
        bukhari_boot_dists_to_quran[i] = np.linalg.norm(v_boot - quran_vec)
        if (i + 1) % 250 == 0:
            print(f"    boot {i+1}/{N_BOOT_BUKHARI} self_mean={self_dists[:i+1].mean():.6f}", flush=True)

    self_q95 = float(np.quantile(self_dists, 0.95))
    p_dist = float((1 + np.sum(self_dists >= obs_dist)) / (N_BOOT_BUKHARI + 1))
    cell_c_pass = (obs_dist > self_q95) and (p_dist < ALPHA_BON)
    print(f"  self-split distance: mean={self_dists.mean():.6f} q95={self_q95:.6f} max={self_dists.max():.6f}", flush=True)
    print(f"  Quran vs Bukhari boot distances: mean={bukhari_boot_dists_to_quran.mean():.6f} q05={np.quantile(bukhari_boot_dists_to_quran, 0.05):.6f}", flush=True)
    print(f"  p_dist = {p_dist:.4f}   PASS_C = {cell_c_pass}", flush=True)

    # --- Positive control (MW-5) ---
    print("\n=== MW-5 POSITIVE CONTROL ===", flush=True)
    # generate 114 fake surahs with IID uniform letters over 28-letter alphabet
    alphabet = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
    rng_mw = np.random.default_rng(SEED + 99)
    # precompute alphabet features
    alpha_feats = np.array([letter_feature_vector(L) for L in alphabet])
    fake_vectors = np.zeros((114, 9))
    for i in range(114):
        n_letters = int(max(letter_counts[i], 10))
        idxs = rng_mw.integers(0, len(alphabet), size=n_letters)
        fake_vectors[i] = alpha_feats[idxs].mean(axis=0)
    mu_f = fake_vectors.mean(0); sd_f = fake_vectors.std(0); sd_f[sd_f == 0] = 1.0
    Xf = (fake_vectors - mu_f) / sd_f
    km_f = KMeans(n_clusters=4, random_state=SEED, n_init=10)
    lbls_f = km_f.fit_predict(Xf)
    try:
        sil_f = silhouette_score(Xf, lbls_f)
    except Exception:
        sil_f = 0.0
    print(f"  MW-5 fake-IID silhouette = {sil_f:.4f} (expected ~0)", flush=True)
    print(f"  MW-5 observed Quran silhouette = {observed_sil:.4f}", flush=True)

    # --- Verdicts ---
    print("\n=== VERDICTS ===", flush=True)
    verdict_a = "PASS" if cell_a_pass else "NULL"
    verdict_b = "PASS" if cell_b_pass else "NULL"
    verdict_c = "PASS" if cell_c_pass else "NULL"
    n_pass = cell_a_pass + cell_b_pass + cell_c_pass
    if n_pass == 3:
        overall = "JOINT-PASS"
    elif n_pass >= 1:
        overall = f"PARTIAL-PASS-{n_pass}of3"
    else:
        overall = "NULL"
    print(f"  Cell A (silhouette):       {verdict_a}", flush=True)
    print(f"  Cell B (AUC Meccan/Med):   {verdict_b}", flush=True)
    print(f"  Cell C (Bukhari distinct): {verdict_c}", flush=True)
    print(f"  OVERALL: {overall}", flush=True)

    # --- Write outputs ---
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    out = {
        "id": "H-NEW-182",
        "seed": SEED,
        "bonferroni_k": 3,
        "alpha_bon": ALPHA_BON,
        "feature_names": FEATURE_NAMES,
        "n_surahs": n_surahs,
        "letter_counts": letter_counts.tolist(),
        "cell_a": {
            "k": 4,
            "observed_silhouette": observed_sil,
            "null_mean": float(null_sils.mean()),
            "null_std": float(null_sils.std()),
            "null_q95": null_q95,
            "null_max": float(null_sils.max()),
            "p_sil": p_sil,
            "pass": bool(cell_a_pass),
            "cluster_summary": cluster_summary,
        },
        "cell_b": {
            "feature": "emphatic_fraction",
            "observed_auc": observed_auc,
            "reported_abs_auc": reported_auc,
            "flipped": flip,
            "p_auc_two_sided": p_auc,
            "effect_size_dev": float(dev_obs),
            "aux_auc_exploratory": aux_auc,
            "pass": bool(cell_b_pass),
        },
        "cell_c": {
            "observed_quran_bukhari_distance": obs_dist,
            "self_split_mean": float(self_dists.mean()),
            "self_split_q95": self_q95,
            "self_split_max": float(self_dists.max()),
            "p_dist": p_dist,
            "bukhari_boot_to_quran_mean": float(bukhari_boot_dists_to_quran.mean()),
            "bukhari_boot_to_quran_q05": float(np.quantile(bukhari_boot_dists_to_quran, 0.05)),
            "bukhari_boot_to_quran_q95": float(np.quantile(bukhari_boot_dists_to_quran, 0.95)),
            "quran_vec": {nm: float(v) for nm, v in zip(FEATURE_NAMES, quran_vec)},
            "bukhari_vec": {nm: float(v) for nm, v in zip(FEATURE_NAMES, bukhari_vec)},
            "pass": bool(cell_c_pass),
        },
        "mw5": {"fake_iid_silhouette": float(sil_f), "quran_silhouette": observed_sil},
        "verdict_cells": {"A": verdict_a, "B": verdict_b, "C": verdict_c},
        "verdict_overall": overall,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUT_JSON}", flush=True)

    # per-surah CSV
    csv_lines = ["surah_id,type,letter_count,cluster," + ",".join(FEATURE_NAMES)]
    for i in range(n_surahs):
        csv_lines.append(
            f"{surahs[i]['id']},{types[i]},{letter_counts[i]},{labels[i]},"
            + ",".join(f"{v:.6f}" for v in vectors[i])
        )
    OUT_CSV.write_text("\n".join(csv_lines))
    print(f"Wrote {OUT_CSV}", flush=True)


if __name__ == "__main__":
    main()
