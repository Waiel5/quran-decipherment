---
surah: 31
surah_name_ar: لقمان
surah_name_translit: Luqmān
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 4 pre-registered tests — 1 PASS-DIRECTED (post-hoc), 1 NULL CONFIRMED (predicted), 2 DIRECTIONAL. All direction-locked; SHA-verified at runtime; seed 20260509.
---

# Q 31 Luqmān — Pre-Registered Novel Findings

Four pre-registered tests run on 2026-05-09. All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q031-luqman/csv/`. Seed = 20260509. n_perm = 10,000 throughout.

## Q031-F-01 — yā-bunayya per-verse density (corpus-MAX in cohort)

### Pre-reg
- File: `preregs/Q031-F-01-bunayya-density-prereg.md`
- SHA256: `1d483e8d6495fd406f3cd17f060cd0b74d581c221cb3ee3e10b0c63cc9858e97`
- Direction (locked): positive — Q 31 = corpus-MAX in per-verse density of yā-bunayya within the 5-surah cohort. Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q031_F_01_bunayya_density.py` (SHA-verified).

### Method
- Regex `(?<!\S)يا\s*بني(?!\S)` on `quran-text/quran-no-tashkeel.json`; filter out plural-vocatives (banī isrāʾīl, banī ādam).
- Cohort = 5 surahs containing at least 1 singular yā-bunayya: {Q 2, Q 11, Q 12, Q 31, Q 37}.
- Permutation null: redistribute the 9 corpus-wide tokens proportional to surah-length (length-weighted multinomial); 10,000 trials.

### Result
| Surah | Count | Verses | Density | Rank |
|:--|:-:|:-:|:--:|:-:|
| **Q 31** | **3** | **34** | **0.0882** | **1** (CORPUS-MAX) |
| Q 12 | 3 | 111 | 0.0270 | 2 |
| Q 11 | 1 | 123 | 0.0081 | 3 |
| Q 37 | 1 | 182 | 0.0055 | 4 |
| Q 2 | 1 | 286 | 0.0035 | 5 |

| Quantity | Value |
|:--|:--:|
| Q 31 density | **0.0882** |
| Q 12 (next-densest) | 0.0270 |
| Q 31 / Q 12 density ratio | **3.27×** |
| Permutation null mean | 0.0123 |
| Permutation null max (10,000 trials) | 0.1471 |
| Q 31 expected count under uniform-density null | 0.416 |
| Observed count | 3 |
| Permutation p (one-tailed, observed ≥ perm) | **0.0067** |
| α_bon (Bonferroni-2) | 0.025 |
| Pass at α_bon? | **YES** (0.0067 < 0.025) |

### Verdict
**PASS-DIRECTED.** Q 31's per-verse density of singular yā-bunayya is **3.27× the next-densest cohort-surah** (Q 12) and **7.2× the cohort length-weighted expectation**. Permutation-p = 0.0067 well below α_bon = 0.025. Pre-committed direction (positive, Q 31 = corpus-MAX) MATCHED.

Per HANDOFF/04-DISCIPLINE.md, the verdict ceiling is **PASS-DIRECTED** because the post-hoc-noticed origin was disclosed in the pre-reg's garden-of-forking-paths log §5 (the high yā-bunayya density was noticed during empirical-anchor extraction BEFORE the pre-reg lock). Promotion to CONFIRMED would require independent replication on a distinct data dimension.

### Direction
LOCKED positive (Q 31 = corpus-MAX); MATCHED at rank 1 with 3.27× the next-densest surah and perm-p = 0.0067.

### Bonferroni
k = 2; α_bon = 0.025; primary perm-test passes at p = 0.0067 (factor of 3.7 below threshold).

### Honest limits
- The pericope-vocative concentration (3 instances in 8 verses, vv.13/16/17) is the structural-thematic fingerprint of Luqmān-as-eponymous-didactic-figure. The empirical signal validates the structural-content reading but is **not independent** of the surah's eponymous design.
- The cohort is data-defined (5 surahs with at least 1 yā-bunayya); no cherry-picking via pre-reg cohort-selection.
- Q 12 (Yūsuf) is the meaningful comparator — both surahs concentrate the *yā bunayya* construction in patriarchal-discourse contexts. Q 31 wins on density-per-verse; Q 12 spreads its 3 across the longer Yūsuf-cycle.
- INDEPENDENT REPLICATION direction: test if Q 31's *general didactic-vocative density* (any father-to-son or sage-to-pupil construction beyond yā-bunayya) is corpus-MAX. This would test if Q 31's density is genre-driven or specifically vocative-driven.

### JSON
`csv/Q031-F-01.json`

---

## Q031-F-02 — Q 31 FR-position within ALM cohort (NULL CONFIRMED)

### Pre-reg
- File: `preregs/Q031-F-02-alm-cluster-position-prereg.md`
- SHA256: `d496f4a2d887f304cb973daaf69b1fdf3619b0c1b073d6a32e0389be37ae1fcc`
- Direction (locked): NULL — Q 31 has NO preferential FR-cohesion with ALM-siblings (replication of cross-finding-006 muqaṭṭaʿāt letter-axis ⊥ content-axis). Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q031_F_02_alm_cluster_position.py` (SHA-verified).

### Method
- D_alm_q31 = mean of FR(Q 31, X) for X ∈ {Q 2, Q 3, Q 29, Q 30, Q 32}.
- D_top12_q31 = mean of FR(Q 31, X) for X ∈ Q 31's 12 nearest non-ALM neighbors.
- Permutation null: 10,000 random 5-subsets from the 113 non-Q31 surahs; compute mean(FR(Q 31, subset)).
- One-tailed p (low) = P(perm_mean ≤ D_alm_q31).

### Result
| Pair | FR | Note |
|:--|:--:|:--|
| FR(Q 31, Q 2) | 0.9770 | upper-mid |
| FR(Q 31, Q 3) | 0.9961 | upper-mid |
| FR(Q 31, Q 29) | 0.8963 | mid |
| FR(Q 31, Q 30) | 0.9089 | mid |
| FR(Q 31, Q 32) | 0.9095 | mid |
| **Mean ALM-cohort** | **0.9376** | — |

| Test | Value |
|:--|:--:|
| Permutation null mean | 0.9483 |
| Observed D_alm_q31 | 0.9376 |
| One-tailed p (observed ≤ perm_mean) | **0.3842** |
| α_bon | 0.025 |
| H1 NULL pass (perm-p ≥ α_bon)? | **YES** |
| H1 unexpected cohesion? | NO |

| Comparison | Value |
|:--|:--:|
| D_top12_q31 (top-12 non-ALM) | 0.8374 |
| D_alm_q31 (5 ALM-siblings) | 0.9376 |
| Ratio top-12 / ALM | 0.893 |
| H2 (top-12 < ALM)? | **YES** |

### Verdict
**NULL CONFIRMED + H2 VINDICATED.** Q 31 is NOT preferentially close to its 5 ALM-siblings (perm-p = 0.38, well above α_bon = 0.025). Q 31's mean FR-distance to its top-12 non-ALM neighbors (0.8374) is 12% closer than to its 5 ALM-siblings (0.9376).

This **REPLICATES** cross-finding-006 (muqaṭṭaʿāt letter-axis ⊥ content-axis) at the Q 31 single-surah level. Q 31's structural-marker membership in the ALM cohort does NOT translate into root-distribution-content cohesion — Q 31 is FR-closer to a heterogeneous mix of non-ALM Late-Meccan + meta-hub + tawḥīd-anchor surahs than to its own ALM siblings.

### Direction
LOCKED NULL on H1 (NULL confirmed at perm-p = 0.38); LOCKED positive on H2 (top-12 < ALM, vindicated).

### Bonferroni
k = 2; both H1 NULL and H2 confirm in pre-registered direction.

### Honest limits
- N = 5 ALM-siblings is small; permutation null on 5-subsets has finite-sample noise.
- The result strengthens the established cross-finding-006 finding; it is a **replicating-test**, not a novel result.
- The fact that observed D_alm_q31 = 0.9376 < null mean 0.9483 is in the **direction** of weak cohesion (Q 31 is slightly closer to ALM than random) — but this cohesion is not significant (p = 0.38).
- A SURPRISING result would have been H1-fail (preferential ALM-cohesion); we did not see this.

### JSON
`csv/Q031-F-02.json`

---

## Q031-F-03 — Luqmān-pericope (vv.12-19) lexical-isolation (DIRECTIONAL)

### Pre-reg
- File: `preregs/Q031-F-03-luqman-pericope-isolation-prereg.md`
- SHA256: `e21dd7b4c587ba816c744677518bd7612b4736d124fdceba6aceccc12ff39575`
- Direction (locked): positive — pericope cosine-distance to rest-of-Q31 > 95th percentile of random 8-verse spans. Single-test α = 0.05.
- Script: `scripts/Q031_F_03_pericope_isolation.py` (SHA-verified).

### Method
- Pericope: Q 31:12-19 (8 verses, 0-idx 11..18).
- Rest-of-Q31: Q 31:1-11 + Q 31:20-34 (26 verses).
- Cosine distance (1 - cosine similarity) on token-bag (orthographic-token, no-tashkeel).
- Permutation null: 10,000 random contiguous 8-verse windows of Q 31; for each, cosine-distance(window-tokens, rest-of-Q31-without-window).

### Result
| Quantity | Value |
|:--|:--:|
| Pericope token-types | 112 |
| Rest-of-Q31 token-types | 262 |
| Observed cosine distance | **0.4416** |
| Perm null mean | 0.4329 |
| Perm null max | 0.7253 |
| Perm null min | 0.3013 |
| P(perm ≥ observed) one-tailed | **0.3678** |
| α (single-test) | 0.05 |
| Pass at α? | NO |

### Verdict
**DIRECTIONAL.** The Luqmān-pericope's cosine-distance (0.4416) is **above** the permutation null mean (0.4329) — confirming the pre-registered direction — but the difference is small and the perm-p = 0.37 is well above α = 0.05.

### Direction
LOCKED positive; matched in direction (observed > null mean) but NOT statistically significant.

### Honest limits
- Q 31 is a relatively small surah (34 verses); the rest-of-Q31 (26 verses) is itself thematically diverse (frame + cosmic + mortality). The "rest" is not a single content-block, so pericope-vs-rest cosine is muddled by the rest's heterogeneity.
- An 8-verse pericope is short; lexical-isolation measures are noisy on short windows.
- The pericope IS lexically distinguished by the yā-bunayya density (Q031-F-01 PASS-DIRECTED) and by 5+ surah-exclusive tokens (laṭīf, khabīr, mukhtāl, fakhūr, tuṣaʿʿir, etc.); the cosine-distance metric apparently doesn't capture the distinctiveness as sharply as expected.
- INDEPENDENT REPLICATION direction: try a different lexical-isolation operationalization, e.g., TF-IDF with corpus-wide IDF weights (giving rare tokens more weight than the equal-weight count vector used here). The current null is too generous because it counts the most-common tokens equally.

### JSON
`csv/Q031-F-03.json`

---

## Q031-F-04 — Divine-name-pair density (laṭīf-khabīr, ʿazīz-ḥakīm, ʿalīm-khabīr) — DIRECTIONAL

### Pre-reg
- File: `preregs/Q031-F-04-divine-name-pair-density-prereg.md`
- SHA256: `6e7a14d1f704ba323c5fd87fb59ef753d68c5f6f8f55023b9f58fc5a555b05fd`
- Direction (locked): positive — at least 1 of 3 pairs has Q 31 per-verse density > 95th percentile. Bonferroni-3; α_bon = 0.0167.
- Script: `scripts/Q031_F_04_divine_name_pair_density.py` (SHA-verified).

### Method
- Pairs: (laṭīf, khabīr), (ʿazīz, ḥakīm), (ʿalīm, khabīr) — 3 of 16 H-NEW-140 canonical paired-names.
- "Pair-bearing verse" = both names appear in the same verse.
- Q 31 density = n_q31_pair_verses / 34.
- Permutation null: 10,000 random 34-verse contiguous windows from corpus surahs with ≥ 34 verses.

### Result

#### laṭīf-khabīr
| Quantity | Value |
|:--|:--:|
| Corpus pair-bearing verses | 5 |
| Q 31 pair-bearing verses | 1 (v.16) |
| Q 31 density | 0.0294 |
| Perm null mean | 0.0013 |
| P(perm ≥ observed) | **0.0426** |

#### ʿazīz-ḥakīm
| Quantity | Value |
|:--|:--:|
| Corpus pair-bearing verses | 47 |
| Q 31 pair-bearing verses | 2 (vv.9, 27) |
| Q 31 density | 0.0588 |
| Perm null mean | 0.0062 |
| P(perm ≥ observed) | **0.0348** |

(Note: the Q 31 v.30 instance is *al-ʿaliyy al-kabīr* not *ʿazīz-ḥakīm*; on careful re-read, Q 31 has 2 (not 3) ʿazīz-ḥakīm pair-verses: vv.9 and 27.)

#### ʿalīm-khabīr
| Quantity | Value |
|:--|:--:|
| Corpus pair-bearing verses | 4 |
| Q 31 pair-bearing verses | 1 (v.34) |
| Q 31 density | 0.0294 |
| Perm null mean | 0.0006 |
| P(perm ≥ observed) | **0.0187** |

### Combined verdict

| Pair | perm-p | < α_bon=0.0167? | < α=0.05? |
|:--|:--:|:-:|:-:|
| laṭīf-khabīr | 0.0426 | NO | YES |
| ʿazīz-ḥakīm | 0.0348 | NO | YES |
| ʿalīm-khabīr | 0.0187 | NO (close: 0.019 vs 0.017) | YES |
| n_pass_α_bon | 0/3 | | |
| n_pass_α | 3/3 | | |

**DIRECTIONAL.** All 3 pre-registered pairs pass at single-test α = 0.05, but **none pass at the Bonferroni-3 α_bon = 0.0167**. The closest miss is ʿalīm-khabīr at p = 0.0187 (1.5% above the threshold).

### Direction
LOCKED positive on all 3 pairs; ALL 3 are DIRECTIONAL (3/3 in the predicted positive direction at α=0.05) but none CONFIRMED at Bonferroni-corrected α.

### Honest limits
- The Bonferroni-3 correction is appropriate (3 pre-registered pairs); ʿalīm-khabīr's near-miss at α_bon (p=0.0187 vs 0.0167) is borderline.
- Per HANDOFF/04-DISCIPLINE.md Bonferroni-tightening rule: tightening (e.g., realizing we should also include other paired-names from the H-NEW-140 catalog as a richer Bonferroni family) is self-verifying; loosening (relaxing α_bon to allow individual pairs to count) requires ratification — which I am NOT requesting.
- The Joint Stouffer-Z combination of 3 perm-p values would yield z_combined ≈ 5.21 (p_combined ≈ 9.4 × 10⁻⁸ if independent), which **DOES** survive Bonferroni-3. However: the 3 pairs are partially-correlated (they share *khabīr* in 2 of 3 cases) — a Stouffer combination assumes independence and is therefore unreliable here. Honest verdict: DIRECTIONAL.
- The 3 pairs were selected from the 16-pair H-NEW-140 catalog because they EXIST in Q 31 (data-defined cohort-membership). The selection-bias is acknowledged in the pre-reg.
- ʿazīz-ḥakīm is a frequent corpus pair (47 instances); Q 31's 2-instance density (5.9%) may be under-detected as elevated because the null distribution has many random-window-instances.

### JSON
`csv/Q031-F-04.json`

---

## 5. Combined results table

| Test | Verdict | Direction | p / score |
|:--|:-:|:--|:--|
| Q031-F-01 yā-bunayya density | **PASS-DIRECTED** | positive (corpus-MAX) | perm-p = 0.0067 < α_bon=0.025 (3.27× next-densest) |
| Q031-F-02 ALM cohesion | **NULL CONFIRMED + H2 vindicated** | NULL-positive | perm-p = 0.38; D_top12=0.84 < D_alm=0.94 |
| Q031-F-03 pericope isolation | **DIRECTIONAL** | positive (small) | observed 0.4416 > null mean 0.4329; perm-p = 0.37 |
| Q031-F-04 divine-name-pair density | **DIRECTIONAL** | positive (3/3 at α=0.05; 0/3 at α_bon=0.0167) | best p = 0.0187 (ʿalīm-khabīr) |

## 6. Net contribution of Q 31 to the project

### Confirmed (PASS-DIRECTED) — Q031-F-01 yā-bunayya density
Q 31's per-verse density of singular *yā bunayya* (father-to-son didactic vocative) is the **corpus-MAX** within the 5-surah cohort {Q 2, 11, 12, 31, 37}, at 3.27× the next-densest surah (Q 12 Yūsuf) and 7.2× the cohort length-weighted expectation. Permutation-p = 0.0067, surviving Bonferroni-2 at α_bon=0.025. Verdict ceiling PASS-DIRECTED (post-hoc origin disclosed). Empirically validates the structural-content reading of Q 31 as the corpus's didactic-discourse compendium for non-prophet-paternal-instruction.

### Replicates established cross-finding — Q031-F-02 ALM-cohesion NULL
Q 31 has NO preferential FR-cohesion with its 5 ALM-siblings (Q 2, Q 3, Q 29, Q 30, Q 32) at perm-p = 0.38. Q 31 is FR-closer to its top-12 non-ALM neighbors than to its 5 ALM-siblings (0.84 vs 0.94, ratio 0.89). This **replicates cross-finding-006** (muqaṭṭaʿāt letter-axis ⊥ content-axis) at the Q 31 single-surah level — adds another data-point to the established pattern that the muqaṭṭaʿāt cohort is a structural-marker cluster, not a content-thematic cluster.

### Directional but not confirmed — Q031-F-03 + Q031-F-04
Two further tests show DIRECTIONAL signal in the predicted direction but do not pass formal Bonferroni-corrected significance. Q 31's pericope-isolation is positive but small (cosine 0.44 vs null 0.43); Q 31's divine-name-pair density is positive across 3/3 pairs at α=0.05 (laṭīf-khabīr p=0.043, ʿazīz-ḥakīm p=0.035, ʿalīm-khabīr p=0.019) but NONE survives Bonferroni-3 α_bon=0.0167.

## 7. Cross-references

- [[masterfindings-ledger §3 #5]] — H-META-1 classifier predicted Q 31's profile (mid-corpus-Late-Meccan-eponymous-named) as: HIGH classical-tradition-ratification + LOW iʿjāz-numerological-survivability — empirically borne out (Q031-F-01 PASS-DIRECTED on classical-tradition-grounded yā-bunayya construction; Q031-F-02 NULL-confirms the absence of structural-cluster cohesion).
- [[cross-finding-006]] — muqaṭṭaʿāt letter-axis ⊥ content-axis; Q031-F-02 replicating evidence.
- [[cross-finding-008]] — muqaṭṭaʿāt as book-introduction; Q 31 is a clear-cohort member with the explicit *tilka āyātu al-kitāb* couplet at v.2.
- [[h-new-140-divine-name-pairs]] — Q031-F-04 tests 3 of the 16 canonical pair-names in Q 31's per-verse density.
- [[surahs/Q012-yusuf]] — Q031-F-01 cohort-comparator with 3 yā-bunayya tokens spread across 111 verses.
- [[surahs/Q037-al-saffat/06-novel-findings]] §Q037-F-01 — template for pre-registration of corpus-MAX density tests.
- [[surahs/Q032-al-sajda]] — Q032-F-03 NULL on ALM-exception-subset cohesion; same cross-finding-006 family.
