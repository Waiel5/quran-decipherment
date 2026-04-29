#!/usr/bin/env python3
"""H-NEW-252: Combined classical-tajwīd phonological + (Zipf α, Heap β) predictor
for muqaṭṭaʿāt singletons — extends H-NEW-232.

Pre-reg: findings/phase-b-hypotheses/h-new-252-combined-phon-alphabeta-singleton-prereg.md
Seed: 20260421
"""

import csv
import hashlib
import json
import math
import random
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_232_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-232.json"
H_NEW_172_CSV = ROOT / "findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv"
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-252-combined-phon-alphabeta-singleton-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-252.json"

SEED = 20260421
N_PERM = 1000

# Classical a-priori accepted clusters (copied verbatim from H-NEW-232)
APRIORI = {
    "ALMS": ["ALM"],
    "ALMR": ["ALM", "ALR"],
    "KHYAS": ["HM", "TSM"],
    "TH": ["TSM"],
    "TS": ["TSM"],
    "YS": ["ALM", "ALR"],
    "S": ["TSM"],
    "HMASQ": ["HM"],
    "Q": ["HM", "TSM"],
    "N": ["ALM", "ALR"],
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_h_new_232():
    with open(H_NEW_232_JSON) as f:
        d = json.load(f)
    return d


def load_alpha_beta():
    """Returns dict surah_id -> (alpha, beta) or None if missing."""
    data = {}
    with open(H_NEW_172_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah_id"])
            try:
                alpha = float(row["alpha"])
                beta = float(row["beta_h159"])
                data[sid] = (alpha, beta)
            except (ValueError, KeyError):
                data[sid] = None
    return data


def reconstruct_muq_features():
    """Recompute H-NEW-165 15-dim feature vectors from scratch.

    We need the raw per-surah features (not just centroids).
    Since h-new-232.json has centroids_z but not raw per-surah features,
    we extract from the per_singleton_results and infer multi-member vectors
    from cluster assignments.

    Approach: use the nearest_multi_surah + nearest_multi_distance to
    back out the singleton positions relative to centroids, but we lack
    the per-surah raw features for multi-member surahs.

    Alternative: recompute from H-NEW-165 definitions inline.
    """
    return None  # Handled inline below


def compute_phon_features_inline():
    """Recompute 15-dim classical-tajwīd features per H-NEW-165 codebook.

    Letter-level features per classical tajwīd:
      makhraj: al-Khalīl 8-tier ordinal (pharynx=1 ... lips=8)
      voice: 1 if majhūra (voiced), 0 if mahmūsa (voiceless)
      manner: stop=1 fricative=2 glide=3 lateral=4 nasal=5 trill=6
      emphatic: 1 if in {ص, ض, ط, ظ} (ḥurūf al-tafkhīm)
      pharyngeal: 1 if in {ح, ع, ء} OR in mustaʿliya {خ, ص, ض, غ, ط, ق, ظ}
      sonorant: 1 if in {م, ن, ل, ر, ي, و}
      continuant: 1 if NOT a stop
      idhlaq: 1 if in {ف, ر, م, ن, ل, ب} (idhlāq letters)
      vowel_carrier: 1 if in {ا, و, ي}
      has_qalqala: 1 if any letter in {ق, ط, ب, ج, د}

    Muqaṭṭaʿāt letter-sets per canonical (29 surahs, 14 distinct sets):
      Q 2, 3, 29, 30, 31, 32: ALM
      Q 10, 11, 12, 14, 15: ALR
      Q 13: ALMR (singleton)
      Q 19: KHYAS (singleton)
      Q 20: TH (singleton)
      Q 26, 28: TSM
      Q 27: TS (singleton)
      Q 36: YS (singleton)
      Q 38: S (singleton)
      Q 40, 41, 42, 43, 44, 45, 46: HM
      Q 42: HMASQ (singleton) - SHARES Q 42 with HM? No: Q 42 is HMASQ, Q 40-46 except 42 are HM
      Q 50: Q (singleton)
      Q 68: N (singleton)
      Q 7: ALMS (singleton)

    Correction: ḥawāmīm cluster is Q 40, 41, 42, 43, 44, 45, 46 but Q 42 opens with HMASQ not HM. So HM = {Q 40, 41, 43, 44, 45, 46} = 6 surahs; HMASQ is a singleton.
    TSM = {Q 26, 28} = 2 surahs (Q 27 is TS singleton).
    ALM = {Q 2, 3, 29, 30, 31, 32} = 6 surahs.
    ALR = {Q 10, 11, 12, 14, 15} = 5 surahs.
    """
    # Arabic letter definitions
    LETTERS = {
        "ا": {"makhraj": 1, "voice": 0, "manner": 3, "emph": 0, "phar": 0,
              "son": 0, "cont": 1, "idhl": 0, "vc": 1, "qalq": 0},
        "ل": {"makhraj": 5, "voice": 1, "manner": 4, "emph": 0, "phar": 0,
              "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
        "م": {"makhraj": 8, "voice": 1, "manner": 5, "emph": 0, "phar": 0,
              "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
        "ر": {"makhraj": 5, "voice": 1, "manner": 6, "emph": 0, "phar": 0,
              "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
        "ك": {"makhraj": 4, "voice": 0, "manner": 1, "emph": 0, "phar": 0,
              "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 0},
        "ه": {"makhraj": 1, "voice": 0, "manner": 2, "emph": 0, "phar": 1,
              "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
        "ي": {"makhraj": 4, "voice": 1, "manner": 3, "emph": 0, "phar": 0,
              "son": 1, "cont": 1, "idhl": 0, "vc": 1, "qalq": 0},
        "ع": {"makhraj": 2, "voice": 1, "manner": 2, "emph": 0, "phar": 1,
              "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
        "ص": {"makhraj": 6, "voice": 0, "manner": 2, "emph": 1, "phar": 1,
              "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
        "ط": {"makhraj": 6, "voice": 1, "manner": 1, "emph": 1, "phar": 1,
              "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 1},
        "س": {"makhraj": 6, "voice": 0, "manner": 2, "emph": 0, "phar": 0,
              "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
        "ق": {"makhraj": 3, "voice": 1, "manner": 1, "emph": 0, "phar": 1,
              "son": 0, "cont": 0, "idhl": 0, "vc": 0, "qalq": 1},
        "ن": {"makhraj": 5, "voice": 1, "manner": 5, "emph": 0, "phar": 0,
              "son": 1, "cont": 1, "idhl": 1, "vc": 0, "qalq": 0},
        "ح": {"makhraj": 2, "voice": 0, "manner": 2, "emph": 0, "phar": 1,
              "son": 0, "cont": 1, "idhl": 0, "vc": 0, "qalq": 0},
    }

    # Muqaṭṭaʿāt letter sets for 29 surahs
    MUQ_LETTERS = {
        2: "الم", 3: "الم", 7: "المص", 10: "الر", 11: "الر", 12: "الر",
        13: "المر", 14: "الر", 15: "الر", 19: "كهيعص", 20: "طه",
        26: "طسم", 27: "طس", 28: "طسم", 29: "الم", 30: "الم",
        31: "الم", 32: "الم", 36: "يس", 38: "ص", 40: "حم", 41: "حم",
        42: "حمعسق", 43: "حم", 44: "حم", 45: "حم", 46: "حم",
        50: "ق", 68: "ن",
    }

    # Cluster labels (consistent with H-NEW-232 apriori)
    MULTI_MEMBER_CLUSTERS = {
        "ALM": [2, 3, 29, 30, 31, 32],
        "ALR": [10, 11, 12, 14, 15],
        "HM": [40, 41, 43, 44, 45, 46],
        "TSM": [26, 28],
    }
    SINGLETONS = {
        "ALMS": 7, "ALMR": 13, "KHYAS": 19, "TH": 20, "TS": 27,
        "YS": 36, "S": 38, "HMASQ": 42, "Q": 50, "N": 68,
    }

    def compute_features(letters_str):
        letters = list(letters_str)
        n = len(letters)
        makhraj_mean = sum(LETTERS[L]["makhraj"] for L in letters) / n
        voice_mean = sum(LETTERS[L]["voice"] for L in letters) / n
        manner_mean = sum(LETTERS[L]["manner"] for L in letters) / n
        emph_mean = sum(LETTERS[L]["emph"] for L in letters) / n
        phar_mean = sum(LETTERS[L]["phar"] for L in letters) / n
        son_mean = sum(LETTERS[L]["son"] for L in letters) / n
        cont_mean = sum(LETTERS[L]["cont"] for L in letters) / n
        idhl_mean = sum(LETTERS[L]["idhl"] for L in letters) / n
        vc_mean = sum(LETTERS[L]["vc"] for L in letters) / n
        letter_count = n
        frac_emph = emph_mean
        frac_phar = phar_mean
        frac_son = son_mean
        frac_idhl = idhl_mean
        has_qalq = 1 if any(LETTERS[L]["qalq"] for L in letters) else 0
        return [makhraj_mean, voice_mean, manner_mean, emph_mean, phar_mean,
                son_mean, cont_mean, idhl_mean, vc_mean, letter_count,
                frac_emph, frac_phar, frac_son, frac_idhl, has_qalq]

    # Compute 15-dim features per surah
    features = {}
    for surah, letters in MUQ_LETTERS.items():
        features[surah] = compute_features(letters)

    return features, MULTI_MEMBER_CLUSTERS, SINGLETONS


def z_score_matrix(X, mean, sd):
    return [[(x - mean[j]) / (sd[j] if sd[j] > 0 else 1.0) for j, x in enumerate(row)]
            for row in X]


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def cluster_centroids(cluster_members, features_z):
    """Given {cluster_name: [surah_ids]} and {surah: z_features}, compute mean
    z-feature per cluster."""
    centroids = {}
    for cname, members in cluster_members.items():
        if not members:
            continue
        n = len(members)
        d = len(features_z[members[0]])
        mean_vec = [0.0] * d
        for m in members:
            for j in range(d):
                mean_vec[j] += features_z[m][j]
        mean_vec = [v / n for v in mean_vec]
        centroids[cname] = mean_vec
    return centroids


def nearest_cluster(singleton_vec, centroids):
    best_c, best_d = None, float("inf")
    all_dists = {}
    for c, cen in centroids.items():
        d = euclidean(singleton_vec, cen)
        all_dists[c] = d
        if d < best_d:
            best_d = d
            best_c = c
    return best_c, best_d, all_dists


def count_matches(nearest_per_singleton, apriori):
    return sum(1 for s, info in nearest_per_singleton.items()
               if info["nearest"] in apriori[s])


def main():
    random.seed(SEED)

    print("=" * 75)
    print("H-NEW-252: Combined phonological + (α,β) predictor for muq singletons")
    print("=" * 75)
    prereg_sha = sha256_file(PREREG_MD)
    print(f"Pre-reg SHA-256: {prereg_sha}")
    print(f"Seed: {SEED}")
    print(f"N_perm: {N_PERM}")
    print()

    # 1. Compute 15-dim phonological features
    print("Step 1: Reconstructing 15-dim classical-tajwīd features per H-NEW-165...")
    phon_features, multi_clusters, singletons = compute_phon_features_inline()
    print(f"  Multi-member clusters: {list(multi_clusters.keys())}")
    print(f"  N multi-member surahs: {sum(len(v) for v in multi_clusters.values())}")
    print(f"  N singletons: {len(singletons)}")
    print()

    # 2. Load (α, β)
    print("Step 2: Loading (α, β) per-surah from h-new-172-per-surah.csv...")
    alpha_beta = load_alpha_beta()
    missing_ab = []
    for surah in list(phon_features.keys()):
        if surah not in alpha_beta or alpha_beta[surah] is None:
            missing_ab.append(surah)
    print(f"  Missing (α,β) for surahs: {missing_ab}")
    print()

    if missing_ab:
        print(f"  WARNING: {len(missing_ab)} muq surahs missing (α,β); will exclude.")
    print()

    # 3. Concatenate features
    print("Step 3: Concatenating 15-dim phonology + 2-dim (α,β) = 17-dim...")
    joint_features = {}
    for surah, phon in phon_features.items():
        if surah in alpha_beta and alpha_beta[surah] is not None:
            alpha, beta = alpha_beta[surah]
            joint_features[surah] = phon + [alpha, beta]

    # Also compute phon-only (15-dim) features for the same surahs, for direct comparison
    phon_only = {s: phon_features[s] for s in joint_features}

    print(f"  Joint features computed for {len(joint_features)} surahs")
    print()

    # 4. Z-score against multi-member reference
    print("Step 4: Z-scoring against 19 multi-member surahs...")

    def zscore_against_multi(features_dict, multi_members):
        n_feats = len(next(iter(features_dict.values())))
        ref = [features_dict[s] for cname, mms in multi_members.items() for s in mms
               if s in features_dict]
        means = [sum(row[j] for row in ref) / len(ref) for j in range(n_feats)]
        sds = []
        for j in range(n_feats):
            var = sum((row[j] - means[j]) ** 2 for row in ref) / max(1, len(ref) - 1)
            sds.append(math.sqrt(var))
        z = {s: [(row[j] - means[j]) / (sds[j] if sds[j] > 0 else 1.0)
                 for j in range(n_feats)] for s, row in features_dict.items()}
        return z, means, sds

    joint_z, joint_means, joint_sds = zscore_against_multi(joint_features, multi_clusters)
    phon_z, phon_means, phon_sds = zscore_against_multi(phon_only, multi_clusters)

    # 5. Compute centroids
    joint_centroids = cluster_centroids(multi_clusters, joint_z)
    phon_centroids = cluster_centroids(multi_clusters, phon_z)

    # 6. Nearest-cluster per singleton
    print("Step 5-6: Computing nearest-cluster per singleton on both feature spaces")
    joint_results = {}
    phon_results = {}
    for sing_name, sid in singletons.items():
        if sid not in joint_z:
            continue
        jnc, jnd, jall = nearest_cluster(joint_z[sid], joint_centroids)
        pnc, pnd, pall = nearest_cluster(phon_z[sid], phon_centroids)
        joint_results[sing_name] = {
            "surah": sid, "nearest": jnc, "distance": jnd, "all_distances": jall,
            "apriori_accepted": APRIORI[sing_name],
            "match": jnc in APRIORI[sing_name],
        }
        phon_results[sing_name] = {
            "surah": sid, "nearest": pnc, "distance": pnd, "all_distances": pall,
            "apriori_accepted": APRIORI[sing_name],
            "match": pnc in APRIORI[sing_name],
        }

    joint_matches = sum(1 for r in joint_results.values() if r["match"])
    phon_matches = sum(1 for r in phon_results.values() if r["match"])
    n_singletons_eval = len(joint_results)

    print(f"\n  Phonology-only (H-NEW-232 replication):  {phon_matches}/{n_singletons_eval}")
    print(f"  Joint phon+(α,β) (H-NEW-252):              {joint_matches}/{n_singletons_eval}")

    # 7. MW-5 positive control — shuffle cluster labels on the 19 multi-member surahs
    print(f"\nStep 7: MW-5 null — {N_PERM} shuffles...")
    all_multi_members = [s for cname, mms in multi_clusters.items() for s in mms
                          if s in joint_z]
    cluster_sizes = {c: len(mms) for c, mms in multi_clusters.items()}

    null_joint_matches = []
    null_phon_matches = []
    for perm_i in range(N_PERM):
        # Shuffle cluster labels
        shuffled = list(all_multi_members)
        random.shuffle(shuffled)
        new_clusters = {}
        idx = 0
        for cname, sz in cluster_sizes.items():
            new_clusters[cname] = shuffled[idx:idx + sz]
            idx += sz

        # Recompute centroids
        new_joint_cent = cluster_centroids(new_clusters, joint_z)
        new_phon_cent = cluster_centroids(new_clusters, phon_z)

        # Recompute matches
        jm = 0
        pm = 0
        for sing_name, sid in singletons.items():
            if sid not in joint_z:
                continue
            jnc, _, _ = nearest_cluster(joint_z[sid], new_joint_cent)
            pnc, _, _ = nearest_cluster(phon_z[sid], new_phon_cent)
            if jnc in APRIORI[sing_name]:
                jm += 1
            if pnc in APRIORI[sing_name]:
                pm += 1
        null_joint_matches.append(jm)
        null_phon_matches.append(pm)

    null_joint_mean = sum(null_joint_matches) / len(null_joint_matches)
    null_phon_mean = sum(null_phon_matches) / len(null_phon_matches)
    joint_p = sum(1 for v in null_joint_matches if v >= joint_matches) / N_PERM
    phon_p = sum(1 for v in null_phon_matches if v >= phon_matches) / N_PERM

    print(f"\n  Null joint mean: {null_joint_mean:.3f}, p = {joint_p:.4f}")
    print(f"  Null phon  mean: {null_phon_mean:.3f}, p = {phon_p:.4f}")

    alpha_bon = 0.025
    if joint_matches >= 9 and joint_p < alpha_bon:
        verdict = "PASS-IMPROVEMENT"
    elif joint_matches == 8 and joint_p < alpha_bon:
        verdict = "PASS-RATIFIED (no improvement but significance preserved)"
    elif joint_matches < 8:
        verdict = "NULL-DEGRADED (α,β harms phonological signal)"
    else:
        verdict = "MIXED"

    print(f"\nVerdict: {verdict}")

    # 8. Output JSON
    out = {
        "id": "H-NEW-252",
        "title": "Combined phonological + (α,β) predictor for muq singletons",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": 2,
        "alpha_bon": alpha_bon,
        "n_singletons_evaluated": n_singletons_eval,
        "apriori_accepted_clusters": APRIORI,
        "phon_only_matches": phon_matches,
        "joint_phon_alphabeta_matches": joint_matches,
        "null_phon_mean": null_phon_mean,
        "null_joint_mean": null_joint_mean,
        "perm_p_phon": phon_p,
        "perm_p_joint": joint_p,
        "phon_results": phon_results,
        "joint_results": joint_results,
        "verdict": verdict,
        "missing_alpha_beta": missing_ab,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
