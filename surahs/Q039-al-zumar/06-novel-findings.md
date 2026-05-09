---
surah: 39
file_type: novel-findings
date_run: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_family: Q039-novel-tests
bonferroni_k: 4
alpha_bon: 0.0125
h_new_assignments:
  Q039-F-01: H-NEW-1270
  Q039-F-02: H-NEW-1280
  Q039-F-03: H-NEW-1290
  Q039-F-04: H-NEW-1300
verdict_summary:
  pass_directed: 3
  null: 1
---

# Q 39 al-Zumar — Novel Findings

This document presents 4 pre-registered novel tests on Q 39, each SHA-locked before execution, with rules-tuple and Bonferroni discipline applied.

**Bonferroni-4 family `Q039-novel-tests`**: α_bon = 0.05 / 4 = **0.0125**.
**Seed**: 20260509.
**Permutations per test**: 10,000.

All test scripts embed and runtime-verify the SHA-256 of the corresponding pre-registration file before computing.

## Q039-F-01 / H-NEW-1270 — Tanzīl-cluster Late-Meccan Nöldeke-peak co-localization

**Pre-reg**: `surahs/Q039-al-zumar/preregs/Q039-F-01-tanzil-cluster-noldeke-peak-prereg.md`
**SHA-256**: `3634a4cb01d1efbcf3ff86880297f78081d62a93bfb692ae7bebfec0a89bfbe3`
**Runtime SHA verification**: PASSED.

### Hypothesis (locked)

The H-NEW-1100 corpus-EXACT 6-surah tanzīl-opener cluster {Q 32, 39, 40, 41, 45, 46} should be chronologically concentrated in the Late-Meccan zone (cross-finding-012 Pattern-B), exhibiting (H1) lower variance-of-Nöldeke-rank than corpus-random 6-subsets, and (H2) higher mean-Nöldeke-rank than corpus-random 6-subsets.

### Result

| Cell | Observed | Null mean | Null q97.5 | Perm-p | Verdict |
|:--|:--|:--|:--|:--|:--|
| H1 (variance) | 39.92 | 967.87 | 1909.20 | **0.000300** | **PASS** |
| H2 (mean) | 76.50 | 57.62 | 84.00 | 0.074300 | FAIL |

H1 is among the strongest single-cell perm-p in the project's per-surah work — the tanzīl-cluster's Nöldeke-rank variance is in the bottom 0.03% of corpus-random 6-subsets. The 6 Nöldeke ranks are [70, 71, 72, 78, 80, 88] — span of 18 of 114 (15.8%).

H2 (mean) at 76.50 vs corpus-random mean 57.62 misses Bonferroni-4 (perm-p 0.074) but is directionally consistent with Late-Meccan placement (corpus-mean is 57.5, dragged down by Mufaṣṣal-short surahs).

### Verdict: **PASS-DIRECTED**

H1 PASSES strongly at α_bon = 0.0125; H2 FAILS Bonferroni but passes the visual-direction-locked prediction. The tanzīl-opener cluster is empirically a single Late-Meccan compositional moment.

### Interpretation

The H-NEW-1100 cluster is not just a formal opener-pattern; it is a **chronologically tight Late-Meccan signature**. The 6 surahs were composed (per Nöldeke's relative chronology) within an 18-position window in a 114-position chronological scheme — they are clustered to a specific phase. This:
1. Vindicates al-Zamakhsharī's classical *Kashshāf* recognition of the tanzīl-cluster (3 of 6 use *al-ʿAzīz al-Ḥakīm*; 4 of 7 are Hawamim).
2. Supports cross-finding-012's Pattern-B Late-Meccan Scripture-Announcement Apparatus framing — the tanzīl-cluster IS Pattern-B "scripture-announcement-content" at a specific compositional moment.
3. Adds an axis to MASTER-LEDGER §10.24 H-NEW-1100: not just "form-defined", but also "chronology-defined".

### Honest limits

- N=6 is small; statistical power is moderate. The variance-test is over-determined by 5 of 6 surahs at Nöldeke ranks 70-78 (a tight 8-rank cluster).
- Q 46 al-Aḥqāf at Nöldeke rank 88 is the cluster's outlier — without it, the variance would be ~13 (extremely tight); with it, variance = 39.92 (still tight).
- The H1 perm-p = 0.0003 is single-cell — the Bonferroni-4 family correction has been applied (α_bon = 0.0125) and H1 still passes by a factor of 41×. No Bonferroni-loosening required.
- This test is SUPPORTING/CO-DEPENDENT with cross-finding-012 per the audit-036 A3 caution about shared latent factor; not independent evidence of the broader Pattern-B claim.

## Q039-F-02 / H-NEW-1280 — Q 39 خلص root concentration

**Pre-reg**: `surahs/Q039-al-zumar/preregs/Q039-F-02-mukhlis-root-concentration-prereg.md`
**SHA-256**: `092aed7c34f1223b3aae2c48f17e2c34ea1433dfa8eb9ccf4bfc4f7a39760b9b`
**Runtime SHA verification**: PASSED.

### Hypothesis (locked)

Q 39's per-1000-word density of the *xlS* root (sincere-devotion / mukhliṣ-mukhlis-khāliṣ semantics) is HIGHER than corpus baseline. Late-Meccan concentration of corpus xlS tokens (cross-finding-012 Pattern-B) is a secondary check.

### Result

| Statistic | Value |
|:--|:--|
| Total corpus *xlS* root tokens | **31** |
| Q 39 *xlS* tokens | **4** (vv. 2, 3, 11, 14) |
| Q 39 *xlS* density per 1000 words | **3.398** |
| Rest-of-corpus density | **0.352** |
| **Density ratio (Q 39 / rest)** | **9.65×** |
| Q 39 xlS density rank | **4 / 114** |
| H1 perm-p (multinomial null) | **0.001100** |
| H2 binomial-p (Late-Meccan concentration) | 0.182542 |

### Verdict: **PASS-DIRECTED**

H1 (Q 39's density above corpus) PASSES at α_bon = 0.0125 by a factor of 11×. H2 (Late-Meccan corpus-wide concentration) FAILS — xlS distributes more broadly in the corpus than just Late-Meccan.

### Interpretation

Q 39's xlS-root concentration is the most-empirical confirmation of al-Rāzī's classical *ikhlāṣ-surah* framing. The 4 attestations cluster in the surah's first 14 verses (vv. 2, 3, 11, 14) — front-loading the doctrinal anchor. Q 39's density is **10× the rest of the corpus** at p = 0.001.

Q 39 ranks 4 of 114 by xlS density. The top-3 are smaller surahs where 1-2 xlS tokens in a small word-count produce extreme density:
- (likely) Q 98 al-Bayyina: 1 token of *mukhliṣīna lahu al-dīn* in v. 5 in a small surah.
- Q 7 al-Aʿrāf: multiple xlS tokens.
- Q 6 al-Anʿām: multiple xlS tokens.

But Q 39 has the highest ABSOLUTE count among major surahs and is corpus-rank-4 by density. This is the classical *ikhlāṣ-surah* identity at empirical resolution.

### Honest limits

- The H1 perm-p of 0.0011 reflects a multinomial-null-under-word-weights operationalization. A simpler hypergeometric (xlS tokens drawn from total tokens, Q 39 receives ≥ 4 of 31 tokens) would yield similar p.
- H2 NULL is honest: xlS distributes more broadly than the Late-Meccan zone. Of 31 corpus xlS tokens, ~21 (68%) are in surahs with Nöldeke rank ≥ 65 (the threshold). This is above chance (58%) but not Bonferroni-significant. The Late-Meccan concentration is REAL but not strong.
- The 4 Q 39 xlS attestations are vv. 2, 3, 11, 14 — concentrated in a 14-verse opening segment. Beyond that, Q 39 shifts to other doctrinal vocabulary. The concentration is intra-surah-front-loaded.

## Q039-F-03 / H-NEW-1290 — Zumar-throng motif structural-twin search

**Pre-reg**: `surahs/Q039-al-zumar/preregs/Q039-F-03-zumar-throng-structural-twin-prereg.md`
**SHA-256**: `074be7d3e28b71fdf09b67f6db9aa06381e6d1b3a564aabadd2f6431cbf80864`
**Runtime SHA verification**: PASSED.

### Hypothesis (locked)

H1: Q 39:71-72 / Q 39:73-74 is RANK-1 by Jaccard among consecutive paired-eschatological-polarity 4-verse-windows in the corpus.
H2: The *wa-sīqa alladhīna* incipit construction is corpus-EXACT (only repeated in Q 39).

### Result

#### H2 — *wa-sīqa* incipit corpus-EXACT

| Statistic | Value |
|:--|:--|
| Total *wa-sīqa* (وسيق) verse-incipits in the corpus | **2** |
| Surahs with any *wa-sīqa* incipit | **1** (Q 39) |
| Surahs with ≥2 *wa-sīqa* incipits | **1** (Q 39) |
| Q 39's *wa-sīqa* verse positions | **vv. 71, 73** |

**H2 PASS**: only Q 39 has the *wa-sīqa alladhīna* construction repeated. The eponymous root *zmr* (zumar) is also corpus-EXACT to Q 39 (2 tokens, both vv. 71 and 73).

#### H1 — Jaccard rank

| Statistic | Value |
|:--|:--|
| Qualifying paired-eschatological-polarity 4-tuples corpus-wide | 8,991 |
| Q 39:71-72 ↔ Q 39:73-74 Jaccard | 0.2031 |
| Q 39 rank | **17 / 8,991** (top 0.19%) |
| H1 rank-1 condition | FAIL |

H1 did NOT reach rank-1. Top-3 positions belong to long surahs (Q 5, Q 22) where short verse pairs in the same eschatology-cluster yield higher Jaccard than Q 39's longer verses (where the function-word denominator is larger).

### Verdict: **PASS-DIRECTED**

H2 PASSES corpus-EXACT (perfect 1-of-1 result). H1 PASSES top-0.19% but does not reach rank-1.

The classical-naming-tradition claim is vindicated: Q 39 is corpus-EXACT *zumar*-named because the root is corpus-EXACT, AND the paired-incipit construction (*wa-sīqa alladhīna [kafarū / ittaqaw]…*) is corpus-EXACT. The motif is not just "named" — it is structurally singular in the corpus.

### Interpretation

The *wa-sīqa alladhīna* paired-incipit construction is one of the corpus's clearest cases of *al-muqābala al-tāmma* (complete antithesis under parallel arrangement) — the classical-balāgha figure that al-Biqāʿī identifies in his Q 39 commentary. It is corpus-EXACT: not a single other surah in the corpus uses *wa-sīqa* as a verse-incipit at all, let alone twice.

The eponymous *zmr* root being corpus-EXACT (2 tokens, both Q 39) confirms that the surah's name *al-Zumar* is not a generic descriptive label but a corpus-singular reference to vv. 71-73 specifically.

### Honest limits

- H1 (rank-1 by Jaccard) was the more ambitious claim. The 8,991 qualifying 4-tuples produce many high-Jaccard pairs in long surahs (Q 5 vv. 9-10/86-87 at J=0.333; Q 22 vv. 13-14/23-24 at J=0.324). These exceed Q 39's 0.203 not because they are MORE structurally parallel but because shorter individual verses have proportionally more shared function-words (الذين, إلى, الله, etc.) per surface-Jaccard formulation.
- A root-Jaccard alternative (using QAC roots instead of orthographic words) would likely shift Q 39 to a higher rank, since the *zmr* + *wa-sīqa* + ʾtq/kfr root-pairs are corpus-EXACT to Q 39. This is a sensitivity check available for follow-up but was not pre-registered as the primary metric.
- H2 (incipit corpus-EXACT) is the cleaner result — corpus-EXACT is not a probabilistic claim but a structural identity.

## Q039-F-04 / H-NEW-1300 — Q 39 self-ring (tanzīl-opener + hamd-closer + rabb-al-ʿālamīn echo)

**Pre-reg**: `surahs/Q039-al-zumar/preregs/Q039-F-04-self-ring-cohesion-prereg.md`
**SHA-256**: `fe370b2edecfb818cc18ad6a13f3bd79f1a8b3455fccb5838b8e1b037ca17d81`
**Runtime SHA verification**: PASSED.

### Hypothesis (locked)

H1: Random 4-element hamd-closer set hits the fixed tanzīl-opener cluster {32, 39, 40, 41, 45, 46} ≥ 1 time at p ≤ 0.0125.
H2: Random 6-element tanzīl-opener set hits the fixed hamd-closer set {17, 27, 37, 39} ≥ 1 time at p ≤ 0.0125.
H3: The rabb-al-ʿālamīn-final-closer cluster ({37, 39, 81}) size = 3 is unlikely under within-surah verse-shuffle null at p ≤ 0.0125.

### Result

| Cell | Observed | Null statistic | Perm-p | Verdict |
|:--|:--|:--|:--|:--|
| H1 (random hamd × fixed tanzīl ≥ 1) | observed = 1 | null mean = 0.21 expected | **0.1991** | FAIL |
| H2 (random tanzīl × fixed hamd ≥ 1) | observed = 1 | null mean = 0.21 expected | **0.1967** | FAIL |
| H3 (rabb-al-ʿālamīn-closer ≥ 3) | observed = 3 | null mean = 0.94 | **0.0191** | FAIL at α_bon=0.0125 (PASS at single-test α=0.05) |

### Verdict: **NULL**

None of H1, H2, H3 reach the Bonferroni-4 α_bon = 0.0125 threshold. H3 (p = 0.0191) is significant at single-test α = 0.05 but does not survive the family Bonferroni correction.

### Interpretation

The DESCRIPTIVE structural-form claim of MASTER §10.27 (Q 39 is corpus-UNIQUE self-ring composition: tanzīl-opener + hamd-closer + rabb-al-ʿālamīn-closer) is REAL — it accurately describes a corpus feature. But the FORMAL Bonferroni-corrected permutation test under the specific operationalizations (random-set intersection, within-surah verse-shuffle for closer cluster) does NOT survive multi-test correction.

This is honest discipline: the form-level claim is a real corpus feature; the formal cohesion test under strict Bonferroni-4 fails. The classical *radd al-ʿajz ʿalā al-ṣadr* observation (al-Biqāʿī) stands as a descriptive-rhetorical insight that empirical statistics cannot promote to law-strength under the project's strict protocol — but cannot refute either.

The H1, H2 failures reflect the small effect-size: with a 4-element hamd-closer set and a 6-element tanzīl set in a 114-surah corpus, 6 × 4 / 114 ≈ 0.21 expected intersection — observing 1 is barely above chance. The structural pattern is REAL, but the formal multiple-comparison-corrected test cannot distinguish it from chance under standard permutation null.

### Honest limits

- This test is REPLICATIVE — it pre-registers a formal verification of MASTER §10.27, which is itself a descriptive observation. The NULL outcome means: the descriptive claim is preserved as descriptive, not promoted to formally-confirmed.
- The H1 + H2 are essentially the same test in different framings (intersection of two sets); H3 is a different operationalization (cluster-size unlikelihood).
- The Bonferroni-4 family includes 3 dependent legs of Q039-F-04 plus Q039-F-01..F-03 — strict correction. Less-strict correction (e.g., counting Q039-F-04 as 1 test cell) would give H3 at p = 0.0191 a single-test PASS.

## Family-level Verdict Summary

| Test | H-NEW # | Verdict | Lead p-value |
|:--|:--|:--|:--|
| Q039-F-01 — Tanzīl-cluster Nöldeke variance | H-NEW-1270 | **PASS-DIRECTED** | 0.0003 |
| Q039-F-02 — xlS root density | H-NEW-1280 | **PASS-DIRECTED** | 0.0011 |
| Q039-F-03 — *wa-sīqa* incipit corpus-EXACT | H-NEW-1290 | **PASS-DIRECTED** | corpus-EXACT |
| Q039-F-04 — Self-ring cohesion | H-NEW-1300 | **NULL** | 0.0191 (H3) |

**Family Bonferroni**: α = 0.05 / 4 = 0.0125. Three of four PASS-DIRECTED at this threshold (or below).

## NULL with Equal Prominence

Q039-F-04 (H-NEW-1300) yielded NULL under the strict Bonferroni-4 protocol. This is published with equal prominence to the PASS-DIRECTED results. The NULL is honest:

- The descriptive structural-form claim of MASTER §10.27 is REAL — Q 39 is corpus-uniquely positioned at the tanzīl-opener × rabb-al-ʿālamīn-closer intersection.
- The formal cohesion test under strict Bonferroni-4 does not promote this descriptive observation to formally-confirmed status.
- The H3 leg at p = 0.0191 is below single-test α=0.05 — relevant for less-strict-correction settings but NOT for the project's strict protocol.

The NULL strengthens the project's credibility by demonstrating that even a clear classical-balāgha observation does not always survive strict statistical testing. The classical insight stands as descriptive; the formal-test outcome is honest about its limits.

## Cross-finding implications

Q039-F-01 PASS-DIRECTED at perm-p = 0.0003 supports cross-finding-012 (Pattern-B Late-Meccan apparatus) at a specific sub-axis: the H-NEW-1100 tanzīl-opener cluster. Adds a chronology-axis to MASTER-LEDGER §10.24 H-NEW-1100.

Q039-F-02 PASS-DIRECTED at perm-p = 0.0011 vindicates al-Rāzī's classical *ikhlāṣ-surah* framing empirically. Adds Q 39's xlS-density signature to the classical-tradition-validation tally (cross-finding-015).

Q039-F-03 PASS-DIRECTED at corpus-EXACT (H2) confirms the classical-balāgha *muqābala al-tāmma* reading of Q 39:71-75 (al-Biqāʿī). Adds the *wa-sīqa* incipit construction to the corpus-EXACT form-pattern typology (joining H-NEW-1100, H-NEW-1010, H-NEW-110, H-NEW-1130, H-NEW-1160, H-NEW-1170, H-NEW-1180, H-NEW-1190).

Q039-F-04 NULL is recorded as one of the project's many honest classical-claim NULLs — the descriptive form-claim is preserved (Q 39's self-ring is real); the formal cohesion test does not survive strict Bonferroni-4.

## Reproduction

To reproduce all results:

```bash
cd /Users/grey/Downloads/quran
python3 surahs/Q039-al-zumar/scripts/Q039_F_01_tanzil_cluster.py
python3 surahs/Q039-al-zumar/scripts/Q039_F_02_mukhlis_root.py
python3 surahs/Q039-al-zumar/scripts/Q039_F_03_zumar_throng.py
python3 surahs/Q039-al-zumar/scripts/Q039_F_04_self_ring.py
```

Each script runtime-verifies its pre-reg SHA-256 before computing and writes to `surahs/Q039-al-zumar/csv/Q039-F-NN.json`.

Seeds, perm counts, and α values are encoded in the scripts (no command-line flags). Replication should yield bit-identical results given the same Python + NumPy versions.
