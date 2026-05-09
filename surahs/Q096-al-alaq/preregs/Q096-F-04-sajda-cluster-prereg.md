---
id: Q096-F-04
title: Q 96 al-ʿAlaq sajda-surah membership and corpus-sajda Fisher-Rao cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q096-F-04-sajda-cluster
alpha_bon: 0.025
direction_of_effect: The 14 (Hanafī tradition) or 15 (Shāfiʿī tradition) classical sajda-tilāwa surahs (those containing a verse where the reciter prostrates) form a structurally cohesive Fisher-Rao cluster relative to length-matched random surah samples. Specifically (Cell A primary): mean intra-cluster FR distance ≤ 5th percentile of length-matched random N-surah samples (where N = sajda set size). (Cell B secondary): same on a normalized cluster excluding Q 1 al-Fātiḥa per H-NEW-89 sui-generis isolate convention.
origin: Q 96 v 19 contains the corpus's sajda-tilāwa marker (۩ at end-of-verse, *waqtarib* imperative). Q 96 is universally agreed to be a sajda-surah across Sunnī fiqh schools. The classical sajda-list is {Q 7:206, Q 13:15, Q 16:50, Q 17:109, Q 19:58, Q 22:18, Q 22:77, Q 25:60, Q 27:26, Q 32:15, Q 38:24, Q 41:38, Q 53:62, Q 84:21, Q 96:19}. Verified via Bukhārī Sujud al-Quran chapter (Bukhārī chapter 17, idInBook 1036-1048) which confirms several of these. Q 96 sajda specifically attested in Muslim Mosques chapterId=5 idInBook=1201, 1202.
verdict_ceiling: PASS-DIRECTED on success; corroboration of liturgical-class structural correlate
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: random-N-surah-samples-from-{1,...,114}-without-replacement (Cell A); same excluding Q 1 (Cell B)
  feature_space: H-NEW-111 Fisher-Rao matrix (csv/h-new-111.json)
  cluster_definition: 14-surah Sunnī shared list (Hanafī base — excludes Q 22:77 which is the disputed second Q 22 prostration debated between Mālikī and Shāfiʿī schools): {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}
---

# Q096-F-04 pre-registration

## Hypothesis

The 14-surah set of sajda-tilāwa surahs (those containing a verse where the reciter prostrates upon recitation) forms a structurally cohesive group in Fisher-Rao root-distribution space (h-new-111.json instrument). The 14 surahs span the corpus chronologically (Meccan + Medinan) but share a liturgical-event marker; if liturgical-event-class correlates with content-register, the 14 should be FR-tighter than 14 random surahs.

## Test design

### Cluster identity (locked)

The 14-surah Sunnī shared list (Hanafī base, all schools agree on these 14):
{Q 7 al-Aʿrāf, Q 13 al-Raʿd, Q 16 al-Naḥl, Q 17 al-Isrāʾ, Q 19 Maryam, Q 22 al-Ḥajj (single), Q 25 al-Furqān, Q 27 al-Naml, Q 32 al-Sajda, Q 38 Ṣād, Q 41 Fuṣṣilat, Q 53 al-Najm, Q 84 al-Inshiqāq, Q 96 al-ʿAlaq}.

Note: Shāfiʿī tradition adds Q 22:77 as a 15th sajda; the 14-set is the Sunnī-conservative base.

### Cell A — full 14-cluster FR cohesion (PRIMARY)

Compute mean pairwise FR distance among 14 sajda-surahs = 14*13/2 = 91 pairs from h-new-111.json D_matrix. Compare to permutation null: 10000 random 14-surah samples drawn uniformly without replacement from {1,…,114}. p_perm = fraction with mean intra-cluster ≤ observed.

PASS-DIRECTED at α_bon = 0.025: p_perm ≤ 0.025.

### Cell B — Q 1-excluded cluster (SECONDARY)

Same as Cell A but exclude Q 1 al-Fātiḥa from the random-surah pool (per H-NEW-89 / cross-finding-009 sui-generis isolate convention). The 14-cluster doesn't include Q 1 anyway, so Cell B tests whether the result is robust to excluding the structural isolate from the null.

PASS-DIRECTED at α_bon = 0.025: p_perm ≤ 0.025.

### Bonferroni

k = 2. α_bon = 0.025. Both must pass.

### Anti-flip

Reverse direction (sajda-surahs are FR-FARTHER than random) is NULL, not reportable PASS.

### Acceptance windows

- Both pass: full PASS-DIRECTED (sajda-surahs form a structural cohesion class)
- Only A passes: PARTIAL (cluster cohesion driven by Q 1-vs-rest gradient — likely length-confounded since Q 1 is shortest)
- Only B passes: WEIRD — flag for review
- Both fail: NULL (sajda-surahs are a liturgical-only class, not structural)

### Garden-of-forking-paths

- Origin disclosed: Q 96 v 19 sajda triggered scoping of the full sajda-class. The cluster identity {14 surahs, Hanafī base} was locked here BEFORE running h-new-111.json read.
- Cluster definition is the SUNNI-CONSERVATIVE 14, not the Shāfiʿī 15. Pre-committed.
- Cell A uses uniform random 14-surah samples (no length matching) as the simplest baseline. A length-matched cell would be a cleaner control but adds k; deferred to follow-up.

### MW-5 positive control

Use the **musabbiḥāt 5-cluster** (Q 57, 59, 61, 62, 64) — known FR-tight (H-NEW-58c). Test mean intra-cluster FR ≤ 5th percentile of random-5-surah samples. If positive control FAILS, NULL-BROKEN.

## Connection to existing findings

- **H-NEW-1300 / 1301** (IMPV-qrA cluster): sister test on a different liturgical-marker class (4-surah set). H-NEW-1301 returned NULL-BROKEN; the present test is on a DIFFERENT cluster (14 sajda-surahs, broader, span more chronology). Not co-dependent.
- **H-NEW-89 / cross-finding-009** META-cluster network: tests whether liturgical functional clusters correlate with structural clusters. H-NEW-68 already returned NULL on the Friday-recitation cluster as shape-cohesion test (it's functional, not shape-based). The present test asks the analogous question for sajda-tilāwa.
- **Bukhārī Sujud al-Quran** chapter (Kitab 17, idInBook 1036-1048) confirms Q 53 al-Najm sajda explicitly in 4 hadiths; Q 38 Ṣād (idInBook 1038); Q 84 al-Inshiqāq (idInBook 1043, 1047). Multiple ḥadīth-corroboration of cluster membership.
- **Muslim Mosques** chapterId=5 idInBook=1201, 1202: explicitly cite Q 96 sajda along with Q 84 al-Inshiqāq.

## Pre-commit attestation

SHA256-locked. Script verifies SHA before reading h-new-111.json.
