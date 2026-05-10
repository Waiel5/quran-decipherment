---
id: H-NEW-1560
title: 99 asmāʾ al-ḥusnā corpus-wide distribution + top-10-by-density Fisher-Rao cluster cohesion
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1560-divine-names-distribution (Cell A uniform + Cell B length-matched)
alpha_bon: 0.025
direction_of_effect: The 10 surahs with the highest per-word divine-name density (computed under the locked substring rule on the 99 al-Tirmidhī names) have a mean intra-cluster Fisher-Rao distance LOWER than 95% of length-matched random 10-surah samples drawn from the 113 non-Q1 surahs
origin: handoff §2c-class inline corpus-wide test — classical Sunnī tradition counts 99 "most beautiful names" of God (al-Bukhārī #2736, Muslim #2677 attesting the existence-claim; the actual 99-list comes from al-Tirmidhī #3507 al-Walīd b. Muslim chain, gharīb). Question: which surahs concentrate divine names, and do high-name-density surahs cluster on root-distribution?
verdict_ceiling: PASS-DIRECTED (single planned cluster test under Bonferroni-2; independent replication required for CONFIRMED promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (whitespace split)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  name_list_source: data/asma-al-husna.txt (al-Tirmidhī #3507 / al-Walīd b. Muslim chain — gharīb)
  name_detection_rule: per-name SUBSTRING match in no-tashkeel verse text. Each name (e.g. الرحمن, الملك, القدوس, مالك الملك, ذو الجلال والإكرام) is checked literally as a substring against each verse. A name is "attested" if at least one verse contains the substring. A multi-token entry (e.g. مالك الملك) is checked as a whitespace-flexible substring (single internal spaces collapsed before matching).
  density_metric: name_attestations_per_word = (sum over 99 names of total substring count in the surah) / surah_word_count
  cluster_definition: top-10 surahs by density_metric (descending; tie-break by sid ascending)
  null_model_A: random-10-surah-samples-no-Q1-uniform (10,000 perms; seed 20260509)
  null_model_B: random-10-surah-samples-no-Q1-length-matched ±15% on total word-count (10,000 perms; seed 20260509+2)
  fr_instrument: findings/phase-b-hypotheses/csv/h-new-111.json (114×114 FR distance matrix on QAC stem-roots, no-tashkeel)
---

# H-NEW-1560 pre-registration

## Origin

The classical Sunnī tradition records that God has 99 "most beautiful names" (*asmāʾ al-ḥusnā*) — al-Bukhārī ḥadīth #2736 (Kitāb al-Daʿwāt) and Muslim #2677 attest the existence of the 99-count, with the canonical enumeration appearing in al-Tirmidhī *Jāmiʿ* #3507 via the al-Walīd b. Muslim chain. al-Tirmidhī himself grades this chain as *gharīb* — the enumeration is a strong candidate for a later expansion of an earlier general claim. al-Suyūṭī (*al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 56) acknowledges that some traditionally-counted names do not appear in the Quranic text in the canonical *al-X* divine-masculine-singular form.

This pre-reg locks two questions:

1. **Descriptive corpus coverage**: of the 99 al-Tirmidhī names, how many appear (as a substring in any verse) in the Quran corpus? Which do NOT appear at all? This is descriptive cataloguing (no hypothesis, no α).
2. **Primary hypothesis**: do the 10 surahs with the highest per-word divine-name density form a Fisher-Rao cohesive cluster on the H-NEW-111 root-distribution instrument?

## Hypothesis (primary, pre-registered)

**H1**: The mean intra-cluster Fisher-Rao distance for the top-10-by-density cluster is lower than the 95th-percentile-lower-tail of length-matched random 10-surah samples (Cell B), AND lower than the 95th-percentile-lower-tail of uniform random 10-surah samples (Cell A).

**Test statistic**: mean intra-cluster pairwise FR distance over the 45 pairs of the 10-surah cluster.

**Null distribution**:
- Cell A (uniform): 10,000 random 10-of-113 samples (excluding Q 1, since Q 1 is a known anchor outlier — same convention as H-NEW-1330).
- Cell B (length-matched): 10,000 random 10-of-113 samples constrained to total word-count within ±15% of the observed cluster's total word-count.

**Decision rule**: PASS-DIRECTED if BOTH cells reject the null at p_perm ≤ 0.025 (Bonferroni-corrected α; k = 2). Other outcomes per the acceptance-window table below.

## Direction lock

Direction LOCKED before computation: **intra-cluster mean ≤ 5th percentile of null** (i.e. the cluster is FR-tighter than chance). The reverse direction (cluster mean ≥ 95th percentile = anti-cohesion) is NOT a reportable PASS and must be published as NULL with explicit reverse-direction annotation.

## A-priori expectation: WEAK signal

Per cross-finding-025 (marker-thickness vs FR-cohesion threshold), single-marker thematic classes tend to NULL on FR-cohesion unless the marker dominates ≥30% of surah content (Late-Meccan apparatus, eschatology-cluster) OR shows multi-axis correlation. Divine-name density is a single-axis lexical marker that varies smoothly across the corpus (the Allāh substring saturates 5.2× higher in Medinan than Meccan per H-NEW-1350, but other-than-Allāh names show a different distribution). Marker-thickness for the top-10 candidate cluster is unknown a priori.

**Honest prediction**: 60/40 toward NULL given the marker-thickness rule. A PASS would suggest divine-name lexical density correlates with root-distribution similarity (which would extend H-NEW-1350's Allāh-density finding to a multi-name signature).

## Cell A (uniform null)

Mean intra-cluster pairwise FR over 45 pairs of the 10-surah top-density cluster. Compare to 10,000 uniform random 10-of-113 samples.

PASS if p_perm ≤ 0.025; NULL otherwise.

## Cell B (length-matched control)

Same test, but null restricted to 10-surah samples with total word-count within ±15% of observed cluster's total. Word-count is computed from the same no-tashkeel JSON used for density (whitespace-split tokens).

PASS if p_perm ≤ 0.025; NULL otherwise.

## MW-5 positive control

H-NEW-1200 14-surah eschatology cluster {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} was CONFIRMED FR-cohesive at p = 0.00030. The 10-surah sub-sample drawn from H-NEW-1200 (first 10 by sid: {56, 69, 74, 77, 81, 82, 83, 84, 86, 90}) is used as MW-5 PC. PC must pass uniform 10-of-113 null at p ≤ 0.05.

If PC fails, the FR instrument is presumed compromised for this size/distance regime and the primary verdict is NULL-BROKEN regardless of Cell A/B outcomes.

## Acceptance windows

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length-confound suspected) |
| ✗ | ✓ | ✓ | PARTIAL (length-matched only) |
| ✗ | ✗ | ✓ | NULL |
| any | any | ✗ | NULL-BROKEN |

## Descriptive outputs (NOT part of pre-registered hypothesis)

In addition to H1, the script computes (descriptively, no α):

1. **Per-name corpus attestation table** (99 rows): name (Arabic), substring count across the full corpus, n_surahs_with_at_least_one_attestation, n_verses_with_attestation, first attestation (surah:verse).
2. **Names that do NOT appear at all** under the substring rule: list and count.
3. **Per-surah divine-name density** (114 rows): surah id, n_words, total_name_attestations, density, corpus_rank.
4. **Top-10 by density** (the cluster) + **Bottom-10 by density** (descriptive).
5. **Cross-reference to morphological catalog** `divine-names-distribution.md` (which counted ~58 of 99 names as canonical DET-MS divine-referring tokens). The two rules differ by design: substring matches all morphological variants and orthographic neighbors; the morphological catalog isolates the strict *al-X* divine-masculine-singular form. Both numbers are reported.

These descriptive outputs do NOT carry their own α — they are summary statistics on the same instrument as H1's cluster definition.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel (`quran-text/quran-no-tashkeel.json`) |
| Token level | substring match on grapheme sequence of each of the 99 names |
| Counting unit | (a) substring attestation count for descriptive; (b) attestation/word density for cluster definition; (c) pairwise FR distance for cohesion test |
| Basmala | counted only in Q 1 — consistent with default rules-tuple; Q 1's *bi-smi llāhi al-raḥmāni al-raḥīm* contains الله, الرحمن, الرحيم |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Name list source | `data/asma-al-husna.txt` (al-Tirmidhī #3507 list, 99 names; UTF-8) |

**Note on substring detection ambiguity**: The substring rule does NOT disambiguate divine vs non-divine referents. For example, الملك "the king" can refer to God OR to the King of Egypt (Q 12:43, 50, 54), and العزيز "the mighty" can refer to God OR to the dignified Egyptian governor (Q 12:30, 51, 78, 88). The morphological catalog `divine-names-distribution.md` does this disambiguation; the substring rule does NOT. This means the substring-density metric over-counts divine-name attestations in Q 12 specifically. This is acknowledged as a known limitation. The substring rule is locked for simplicity and reproducibility; the disambiguation question is left to the secondary descriptive cross-reference.

**Note on multi-token names**: Two of the 99 names are multi-token: مالك الملك (#89) and ذو الجلال والإكرام (#90). These are matched as whitespace-flexible substrings (verse text is normalized to single-space-separated tokens before matching). This is consistent with the prior `divine-names-distribution.md` convention.

## Permutation null protocol

1. Compute observed mean intra-cluster FR on the 10-surah top-density cluster.
2. Set RNG seed = 20260509 (Cell A) and 20260511 (Cell B).
3. Cell A: draw 10,000 uniform 10-of-113 samples (excluding Q 1); compute mean intra-FR.
4. Cell B: draw 10,000 length-matched 10-of-113 samples (within ±15% of cluster total word-count); compute mean intra-FR. Reject any sample outside the window; continue until 10,000 valid samples or 200× cap.
5. p_perm_A = (count of perm-mean ≤ observed) / 10,000.
6. p_perm_B = (count of perm-mean ≤ observed) / N_valid_perms.

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_A ≤ 0.025 AND p_B ≤ 0.025 AND PC ≤ 0.05 | PASS-DIRECTED |
| p_A ≤ 0.025 AND p_B > 0.025 AND PC ≤ 0.05 | DESCRIPTIVE-ONLY (length-confound) |
| p_A > 0.025 AND p_B ≤ 0.025 AND PC ≤ 0.05 | PARTIAL (length-matched only) |
| both p > 0.025 AND PC ≤ 0.05 | NULL |
| PC > 0.05 | NULL-BROKEN (instrument failure) |
| Reverse direction (cluster mean ≥ 95th %ile null) | NULL (reverse-direction; published with observed p) |

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: substring detection rule + density metric + cluster-definition (top-10 descending) + FR instrument (h-new-111) all locked above. Mean intra-cluster FR statistic locked.
- **MW-2 (corpus-prior)**: 10,000 permutations per cell; minimum standard met.
- **MW-3 (alternative-models)**: Two cells (uniform + length-matched) test two model classes. A Bonferroni-corrected joint test is locked.
- **MW-4 (over-fitting)**: cluster size = 10 (fixed); FR instrument is pre-existing (no fitted parameter on this run).
- **MW-5 (replication)**: PASS-DIRECTED is the verdict ceiling for this single pre-registered test. Independent replication required for CONFIRMED. MW-5 PC = 10-surah sub-sample of H-NEW-1200.
- **MW-6 (instrument-control)**: The uniform null (Cell A) controls for instrument distribution shape at the same cluster size. The PC controls for instrument validity in the same size regime.
- **MW-7 (post-hoc cap)**: Two planned cells; no post-hoc dimensions.

**Post-hoc-noticing acknowledgment**: The cluster identity (which 10 surahs) is data-derived (top-10 by density), not theory-derived. However, the FR instrument (h-new-111) is orthogonal to the cluster-selection statistic (density is a substring count; FR is a root-distribution distance). The two metrics share rules-tuple but compute different quantities on the same corpus. This is analogous to the test for "which surahs are the longest, and do they cluster on FR?" — the post-hoc cap applies because the cluster is selected post-observation of one metric to test on another metric. Per MW-7 we cap the verdict at PASS-DIRECTED and require independent replication for CONFIRMED.

## Garden-of-forking-paths disclosure

- The 99-name list is the al-Tirmidhī #3507 al-Walīd b. Muslim list (`data/asma-al-husna.txt`). Other lists exist (al-Ḥākim's list of ~80, Ibn al-ʿArabī's expanded list of >300); only the al-Tirmidhī standard list is in scope.
- The substring detection rule is the same rule-class as H-NEW-1350 (the *Allāh* density test). No alternative detection rule (root-match, lemma-match, full morphological-disambiguation) was considered for this pre-reg lock. The cross-reference to the prior `divine-names-distribution.md` morphological catalog is reported descriptively only.
- The density metric is per-WORD (not per-VERSE). Per-verse coverage was considered and rejected because divine-name attestations are concentrated in shorter rhetorical-cluster verses, which would make per-verse coverage dominated by short-surah outliers. Per-word density is the locked metric.
- Cluster size = 10. Sizes 5, 15, 20 were NOT considered for this lock.
- The cluster is selected as TOP-10. A BOTTOM-10 cluster cohesion test was NOT pre-registered (would be a separate hypothesis with its own α-budget).
- The null sample pool excludes Q 1 (consistent with H-NEW-1330 and prior FR-cluster tests).
- Length-matched ±15% is the same window as H-NEW-1330; no alternative window (±10%, ±20%) was considered.

## Connection to existing findings

- **H-NEW-1350 (Allāh-density Medinan > Meccan, p=0.0001)**: same instrument family (no-tashkeel substring). H-NEW-1560 extends to all 99 names, not just الله.
- **cross-finding-025 (marker-thickness vs FR-cohesion)**: divine-name density is a single lexical axis; a-priori NULL expected unless top-10 surahs share other architectural features.
- **divine-names-distribution.md (prior morphology-strict catalog)**: identified ~58 of 99 names as canonically attested in DET-MS divine-referring form. H-NEW-1560 reports the substring-rule attestation count for cross-reference.
- **H-NEW-170 (99-name network) and H-NEW-140 (divine-name pair cohesion)**: prior findings on divine-name *pairings*, not surah-level density. H-NEW-1560 is orthogonal to these.
- **al-Suyūṭī, al-Itqān, nawʿ 56 (asmāʾ Allāh)**: discusses which traditional names are Quranically attested. H-NEW-1560 provides a corpus-internal substring tally as one empirical answer.

## Anti-flip

The reverse direction (cluster mean ≥ 95th percentile of null = anti-cohesion) is NOT a reportable PASS. The verdict for any direction not matching the lock is NULL, published with the observed p_perm regardless of sign.

## Honest expectation summary

The single most likely outcome (per cross-finding-025) is NULL on root-FR-cohesion of the top-10-by-density cluster, with the descriptive sub-tally (which names appear, which don't) being the more useful product. A NULL on H1 + a robust descriptive catalog is still a worthwhile inline test: it lands the corpus-side fact (which names attest, which don't), corroborates the morphology-strict catalog, and confirms that divine-name density (like sajda-trigger, like Christ-narrative) is a marker-thin axis that does not drive FR-clustering.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in the run script as EXPECTED_SHA. Any mismatch = fail-fast.
