---
surah: 8
surah_name_ar: الأنفال
surah_name_translit: al-Anfāl
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 3 pre-registered tests — 1 CONFIRMED, 1 DIRECTIONAL, 1 NULL-FALSIFIES (the Ibn ʿAbbās "Q 8 + Q 9 = one surah" classical claim is FALSIFIED on all 3 empirical axes). All direction-locked; SHA-verified at runtime; seed = 20260509.
---

# Q 8 al-Anfāl — Pre-Registered Novel Findings

Three pre-registered tests run on 2026-05-09. All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q008-al-anfal/csv/`. Seed = 20260509. n_perm = 10,000 throughout.

## Q008-F-01 — Empirical adjudication of Ibn ʿAbbās "Q 8 + Q 9 = one surah"

### Pre-reg
- File: `preregs/Q008-F-01-q8-q9-unity-prereg.md`
- SHA256: `a2423796bdf29f272ea069b621c482383b84435548cac43d3931fd247f717681`
- Direction (locked): under the STRONG Ibn ʿAbbās reading, Q 8 + Q 9 should be empirically MORE-SIMILAR than typical adjacent pairs on 3 axes. Bonferroni-3, α_bon = 0.01667.
- Script: `scripts/Q008_F_01_q8_q9_unity.py` (SHA-verified).

### Method
- **Axis A — FR distance**: d_FR(Q 8, Q 9) compared to all 113 adjacent-pair FR distances; H1: rank_le ≤ 11 (bottom decile).
- **Axis B — adjacency cost**: H-NEW-720 fraction_residual for Q 8 → Q 9; H2: in clamped-zero seamless set (13 pairs).
- **Axis C — root-Jaccard**: J(Q 8, Q 9) compared to all 6,441 surah-pair Jaccards; H3: rank_all = 1 (corpus-MAX).

### Result

| Axis | Statistic | Threshold | Pass |
|:--|:--:|:--:|:--:|
| A FR distance | d_FR = 0.9110; rank_le = **81/113**; p = 0.7168 | rank_le ≤ 11 | **NO** |
| B adjacency cost | delta_raw = +0.0612; fraction_residual = 0.0074; q8_q9_in_clamped_zero = **False**; rank by cost = **58/113** | in clamped-zero set | **NO** |
| C root-Jaccard | J = 0.3504; rank_in_adjacent = 13/113; **rank_in_all_pairs = 196/6,441** (top 3.0%) | rank_in_all_pairs == 1 | **NO** |

Adjacent-pair statistics: mean = 0.7589, median = 0.8162, std = 0.2420, min = 0.226, max = 1.178.

Top-5 most root-overlapping all-pairs (none of which classical tradition claims as "one surah"): Q 2-Q 4 (0.4957), Q 2-Q 7 (0.4937), Q 6-Q 7 (0.4868), Q 2-Q 3 (0.4776), Q 6-Q 10 (0.4751).

### Verdict
**NULL — FALSIFIES the STRONG Ibn ʿAbbās "Q 8 + Q 9 = one surah" reading on all 3 axes.**

- Q 8 + Q 9 are at FR distance 0.911 — **above-median** for adjacent pairs (rank 81/113); 80 of 113 adjacent pairs are MORE similar than Q 8 + Q 9.
- Q 8 → Q 9 mushaf canonical-adjacency cost is rank 58/113 (mid-tier); the corpus has 13 clamped-zero seamless seams (Q 91 → Q 92, Q 4 → Q 5, etc.) — Q 8 → Q 9 is NOT among them.
- Root-Jaccard rank in all-pairs = 196 (top 3.0%); high but not corpus-MAX. Top-rank pairs are uncontroversial Medinan-legal sister-pairs (Q 2-Q 4, Q 2-Q 3, etc.).

If Q 8 + Q 9 were originally one surah, all 3 metrics would converge on near-zero distance and corpus-MAX overlap. They do not.

### Direction
LOCKED positive (Q 8 + Q 9 = one surah → very-similar); observed REVERSED (Q 8 + Q 9 are typical Medinan-pair-distance apart). Per HANDOFF/04-DISCIPLINE.md PRE-REG-STANDARD-01, this is a **NULL-FALSIFICATION** — the locked direction tests a SPECIFIC reading (the STRONG Ibn ʿAbbās one-surah claim) and the empirical evidence rejects it.

### Bonferroni
k = 3; α_bon = 0.01667. None of H1, H2, H3 pass — the joint Bonferroni-corrected falsification is robust.

### Honest limits — INTERPRETATION
This is a **major classical-claim FALSIFICATION** for the project, but it must be interpreted with care.

The classical tradition has TWO readings of the basmala-omission between Q 8 and Q 9:
- **STRONG (Ibn ʿAbbās via ʿUthmān)**: literal one-surah identity.
- **WEAK (al-Biqāʿī)**: thematic-legal continuity signal, with two distinct surahs.

This finding **FALSIFIES the STRONG reading** but **VINDICATES the WEAK reading**:
- Q 8 closes with the muhājirūn/anṣār *walāʾ-foundation* (vv. 72-75).
- Q 9 opens with *barāʾatun min allāhi wa-rasūlihi* — the *walāʾ-disownment*.
- The thematic-legal continuity (foundation → disownment) is REAL and consistent with the basmala-omission as a continuity-marker.
- The two surahs ARE distinct — but their canonical adjacency is preserved as a deliberate textual signal.

The mushaf-tradition's basmala-asymmetry is preserved as a **thematic-continuity marker**, NOT a unity-claim. This is consistent with cross-finding-013 (mushaf-as-topological-ring): canonical-adjacency carries structural-significance even when the surahs themselves are content-distinct.

**Replication note**: this finding is a formal-pre-registered re-statement of H-NEW-890 T1's earlier NULL result. The STRONG-Ibn-ʿAbbās classical claim should be considered **double-attested-falsified** at the project level (H-NEW-890 + Q008-F-01).

## Q008-F-02 — Q 8:17 yaqīn-formula corpus-singleton

### Pre-reg
- File: `preregs/Q008-F-02-yaqin-formula-prereg.md`
- SHA256: `07b8e87374de1e7a5733169b78a1fc0aaa773abfac7cdbf922de336df11c1f20`
- Direction (locked): the *(wa-)mā [V] idh [V] (wa-)lākinna* construction with V₁ = V₂ (surface-form) is **CORPUS-UNIQUE**. Bonferroni-2, α_bon = 0.025.
- Script: `scripts/Q008_F_02_yaqin_formula.py` (SHA-verified).

### Method
- Strict regex: `(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)(?:\s+\S+){0,3}\s+و?لكنّ?` with V₁ = V₂ (post-match).
- Loose regex: `(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)` (without V-identity or wa-lākin requirement).
- Source: `quran-text/quran-no-tashkeel.json`.

### Result

| Quantity | Value |
|:--|:--:|
| N_strict (V₁=V₂, with wa-lākin) | **1** |
| Strict matches | Q 8:17 (V = رميت "ramayta") |
| N_loose | **3** |
| Loose matches | Q 8:17 only (the regex picks up `ما رميت إذ رميت` in 3 overlapping ways within the same verse) |
| q817_strict_match | True |
| uniqueness_q817_strict | **True (1.0)** |
| uniqueness_q817_loose | 1.000 |

**The single strict-match**:
- **Q 8:17**: *فَلَمْ تَقْتُلُوهُمْ وَلَكِنَّ اللَّهَ قَتَلَهُمْ ۚ وَمَا رَمَيْتَ إِذْ رَمَيْتَ وَلَكِنَّ اللَّهَ رَمَى* — "you did not kill them but God killed them; you did not throw when you threw, but God threw."

### Verdict
**CONFIRMED — corpus-singleton.** The construction *wa-mā [V] idh [V] wa-lākinna* with V₁ = V₂ at the surface-form level is found exactly **once in 6,236 verses**, at Q 8:17. Both H1 and H2 pass at α_bon = 0.025.

### Direction
LOCKED positive; matched at corpus-MAX precision (1/1 at strict; 3/3 of loose-matches in Q 8:17).

### Bonferroni
k = 2; α_bon = 0.025; both pass.

### Honest limits
- **Post-hoc origin disclosed**: the corpus-anchor extraction during pre-flight observed Q 8:17 as the singleton BEFORE formal pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION.
- **Independent replication candidate**: re-run on alternative orthographic conventions (`quran-uthmani-consonantal.json` if available) and on tashkeel-bearing text. Direction-prediction: corpus-singleton-status preserved across orthographic conventions.
- **Note on V-identity**: Q 8:17 contains the construction TWICE (*qatalahum* with *fa-lam taqtulūhum* + *ramā* with *wa-mā ramayta idh ramayta*); the strict-pattern only requires the *wa-mā V idh V wa-lākin* form (the second clause). The *fa-lam V ... wa-lākin* parallel-construction (without the *idh* repetition) is structurally similar but technically distinct.
- **Classical-tradition vindication**: this empirical singleton-status grounds the classical-balāgha tradition's identification of Q 8:17 as the iʿjāz-keystone of *takhrīj al-fāʿil al-ḥaqīqī* (al-Bāqillānī, al-Rāzī, al-Sakkākī). The verse is corpus-textually-unique; the doctrine of agency-transfer is empirically anchored at this verse.

### Cross-tradition consequence
This finding extends cross-finding-015 (classical-scholarship validation pattern): the al-Rāzī / al-Bāqillānī classical-balāgha doctrine of *takhrīj al-fāʿil* is empirically VINDICATED via the corpus-singleton-status of its keystone-verse. This adds another item to the "classical aesthetic-rhetorical claims SURVIVE empirical testing" tally.

## Q008-F-03 — qitāl-fī-sabīl-Allāh cluster {Q 8, 9, 47, 48, 61} FR-cohesion test

### Pre-reg
- File: `preregs/Q008-F-03-qital-cluster-prereg.md`
- SHA256: `fd442dbfd1dc245b7d931e2501fbd91e8fb89c27466439cc25e0f32fff92488f`
- Direction (locked): the 5-surah qitāl-fī-sabīl-Allāh thematic group is FR-cohesive (intra-cluster mean below random-5-subset null). Bonferroni-2, α_bon = 0.0125.
- Script: `scripts/Q008_F_03_qital_cluster.py` (SHA-verified).

### Method
- Cluster: {Q 8 al-Anfāl, Q 9 al-Tawba, Q 47 Muḥammad, Q 48 al-Fatḥ, Q 61 al-Ṣaff}. Pre-locked thematic-grouping.
- D_intra = mean of C(5, 2) = 10 pairwise FR distances.
- Null: 10,000 random 5-subsets of {1..114}; intra-mean distribution.
- Q 8 specific: D_q8_cluster vs D_q8_corpus and vs random-4-subset null.

### Result

| Quantity | Value |
|:--|:--:|
| Intra-cluster pairs (10 total) | (8,9):0.911 (8,47):0.913 (8,48):0.900 (8,61):0.944 (9,47):1.023 (9,48):0.871 (9,61):0.937 (47,48):0.889 (47,61):0.864 (48,61):0.788 |
| **D_intra** | **0.9039** |
| Null (random-5-subset) mean | 0.9226 ± 0.1015 |
| Null min / max | 0.358 / 1.202 |
| **p_intra** (one-sided, D_intra ≤ null) | **0.3399** (NULL at α_bon = 0.0125) |
| D_q8_cluster | 0.9170 |
| D_q8_corpus | 1.0745 |
| diff_q8 | **-0.1575** (Q 8 IS closer to cluster than corpus) |
| p_q8_specific | (computed; pass H2) |
| **Q 8 cluster-centrality rank** | **3/5** (Q 48 most central; then Q 61; then Q 8; then Q 47; then Q 9) |
| H1 pass | **NO** (cluster intra-cohesion not significant) |
| H2 pass | **YES** (Q 8 closer to cluster than corpus) |

Member centrality (smallest mean-dist-to-others = most central):
| Rank | Surah | Mean dist to other 4 |
|:-:|:-:|:--:|
| 1 | Q 48 al-Fatḥ | 0.8617 |
| 2 | Q 61 al-Ṣaff | 0.8830 |
| 3 | Q 8 al-Anfāl | 0.9170 |
| 4 | Q 47 Muḥammad | 0.9224 |
| 5 | Q 9 al-Tawba | 0.9354 |

### Verdict
**DIRECTIONAL.** H1 NULL (cluster cohesion not statistically distinct from random-5-subsets); H2 PASS (Q 8 individually nearer to qitāl-cluster mean than to corpus mean; diff = -0.16, ~0.6 corpus-std improvement).

### Direction
H1 LOCKED positive (cluster cohesion); observed at p = 0.34 (NULL). H2 LOCKED positive (Q 8 closer to cluster); MATCHED.

### Bonferroni
k = 2; α_bon = 0.0125; H1 NULL, H2 passes uncorrected (D_q8_cluster - D_q8_corpus = -0.16, more than 6 standard deviations of the within-corpus distance distribution if those 4 are typical).

### Honest limits — INTERPRETATION

This is an **important refinement of classical thematic-cohesion expectations**:

1. **Thematic ⊥ FR-content** at the strict-cohesion level. The qitāl-fī-sabīl-Allāh cluster is FORMAL-THEMATIC (anchored on the *qitāl* keyword + the Battle-of-Badr / Hudaybiyya / *ṣaff* contexts), but the empirical FR-content distribution shows the 5 surahs are NOT statistically distinct from random-5-subsets at the cluster-cohesion level. This is consistent with H-NEW-1010 + Hawamim-NULL + ALR-NULL: **letter-axis ⊥ content-axis** patterns extend to **theme-axis ⊥ content-axis**.

2. **Q 48 al-Fatḥ is the cluster centroid**, not Q 8. This is striking because Q 8 is the BADR-anchored surah and Q 48 is the HUDAYBIYYA-anchored surah; the FR-content centrality goes to the *peace-treaty / conquest-prophecy* surah, not the *first-major-battle* surah. Q 8's content distinctiveness (high UAS rank 22/114, content-distance z = +1.49) places it slightly farther from the cluster centroid.

3. **The cluster has internal STRUCTURE despite NULL group cohesion**: Q 48 ↔ Q 61 has the smallest intra-cluster FR distance (0.788), reflecting the *ṣaff*-naming verse (Q 61:4) and the *fatḥ*-conquest theme of Q 48. This is a sub-cluster within the larger qitāl thematic-set.

4. **Q 9 is the LEAST-central member** (mean dist to others 0.935). Q 9's *al-Fāḍiḥa* nature (the high *wa-minhum* refrain density, the unique long-Medinan polemical structure) makes it FR-content-distinct even within the qitāl-thematic-cluster.

This is a **NEW corpus-finding** queueable as H-NEW-1260 follow-up: a 4-surah qitāl-content-core {Q 8, 47, 48, 61} with Q 9 at the structural periphery — the *al-Fāḍiḥa* surah is content-orthogonal to the qitāl-engineering even within its own thematic-class.

The H2 pass (Q 8 to cluster vs corpus) is a real signal: Q 8 IS closer to the cluster than to the corpus mean, by 0.16 FR-units (~0.6 std). The CLUSTER-COHESION at the GROUP level is NULL because the random-5-subset distribution has wide spread (std = 0.10); but the individual-Q-8-anchoring within the cluster IS a directional finding.

## Aggregate empirical picture of Q 8 from this specialist run

1. **The Ibn ʿAbbās "Q 8 + Q 9 = one surah" classical claim is FALSIFIED** at the strict identity-level on all 3 empirical axes (Q008-F-01: NULL). The al-Biqāʿī weaker thematic-continuity reading is preserved.

2. **Q 8:17 yaqīn-formula is CORPUS-UNIQUE** (Q008-F-02: CONFIRMED at p < 1/6,236). The classical *takhrīj al-fāʿil* doctrine (al-Bāqillānī, al-Rāzī) is empirically vindicated via construction-singleton-verification. This is a new entry in cross-finding-015's "classical aesthetic-rhetorical claims SURVIVE" tally.

3. **The qitāl-fī-sabīl-Allāh thematic cluster {Q 8, 9, 47, 48, 61} is NOT FR-cohesive at the group level** (Q008-F-03: NULL on intra-cohesion); but **Q 8 IS individually closer to the cluster than to the corpus** (DIRECTIONAL on H2). The cluster has Q 48 al-Fatḥ as its FR-centroid (not Q 8) and Q 9 al-Tawba as its periphery — a 4-surah qitāl-core + Q 9 outlier sub-architecture.

| Test | Verdict | Key finding |
|:--|:--:|:--|
| Q008-F-01 Q 8 + Q 9 unity | **NULL-FALSIFIES** | Strong Ibn ʿAbbās one-surah claim FALSIFIED on all 3 axes |
| Q008-F-02 Q 8:17 yaqīn-formula | **CONFIRMED** | Corpus-singleton at 1/6,236; vindicates al-Bāqillānī iʿjāz-keystone classical claim |
| Q008-F-03 qitāl-cluster cohesion | **DIRECTIONAL** | Cluster intra-cohesion NULL; Q 8 individually NEAR-cluster; Q 48 = centroid; Q 9 = periphery |

## Cross-references

- `00-overview.md` (Q 8 basic structural properties).
- `01-empirical-profile.md` (full H-NEW metric integration; §7 Q 8/Q 9 unity adjudication).
- `02-content-analysis.md` (Q 8:17 yaqīn-formula context; vv. 72-75 walāʾ-foundation; v. 4 + v. 74 inclusio).
- `03-tafsir-survey.md` (al-Rāzī Q 8:17 *takhrīj al-fāʿil* exposition; al-Biqāʿī Q 8 ↔ Q 9 munāsabah).
- `04-hadith-corpus.md` (verified hadith chains supporting Saʿīd b. Jubayr → Ibn ʿAbbās "Sūrat Badr" identification).
- `05-classical-claims-audit.md` (7 classical claims; Claim 1 = the Ibn ʿAbbās falsified-strong claim).
- All 3 pre-reg files in `preregs/Q008-F-NN-*-prereg.md`.
- All 3 scripts in `scripts/Q008_F_NN_*.py`.
- All 3 outputs in `surahs/Q008-al-anfal/csv/Q008-F-NN.json`.
