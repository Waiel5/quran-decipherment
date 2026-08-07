---
id: H-NEW-1360
title: yā-ayyuhā al-nabī (prophet-vocative) 6-surah cluster Fisher-Rao cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1360-prophet-vocative-cluster
alpha_bon: 0.025
direction_of_effect: The 6 surahs containing the vocative *yā-ayyuhā al-nabī* {Q 8, 9, 33, 60, 65, 66} have a mean intra-cluster Fisher-Rao distance LOWER than 95% of random 5th-percentile thresholds under uniform AND length-matched nulls (one-sided)
origin: Specialist test dispatched 2026-05-09 PM (Wave-H follow-up to H-NEW-1260 confirming Q 49 al-Ḥujurāt as corpus-rank-1 on *yā-ayyuhā alladhīna āmanū* density). Sister-construction *yā-ayyuhā al-nabī* identified by classical scholars (al-Suyūṭī *al-Itqān* nawʿ 51 *al-khiṭāb*) as a Medinan direct-address marker where Allāh speaks directly to Muḥammad.
verdict_ceiling: PASS-DIRECTED (single planned pre-registered test; independent replication required for CONFIRMED promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  cluster_definition: surahs-containing-the-vocative-ya-ayyuha-al-nabi
  search_pattern: regex 'يا\s*أيها\s*النبي' over no-tashkeel text
  null_model: random-6-surah-samples-from-114-uniform-and-length-matched
---

# H-NEW-1360 pre-registration


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Origin and classical grounding

The specialist dispatch follows the H-NEW-1260 confirmation that Q 49 al-Ḥujurāt is corpus-rank-1 on the *yā-ayyuhā alladhīna āmanū* believer-vocative density and that all 89 attestations of that vocative are strictly Medinan, vindicating al-Suyūṭī's classical Medinan-marker claim (*al-Itqān*, nawʿ 9 *al-makkī wa-l-madanī*; nawʿ 51 *fī khiṭābātihi*).

The sister-construction *yā-ayyuhā al-nabī* ("O Prophet!") is a smaller, more focused vocative. Classical scholars (al-Suyūṭī *al-Itqān*, al-Zarkashī *al-Burhān*) note this construction marks the surahs where Allāh directly addresses Muḥammad rather than the believing community. The vocatives *yā-ayyuhā al-muzzammil* (Q 73:1) and *yā-ayyuhā al-muddaththir* (Q 74:1) employ different epithets and are NOT in this cluster.

## Cluster verification (locked from direct corpus search)

Regex `يا\s*أيها\s*النبي` over `quran-text/quran-no-tashkeel.json` returns 13 attestations across 6 distinct surahs (all Medinan):

| Surah | Verses with *yā-ayyuhā al-nabī* | Count | Verses |
|:-:|:--|:-:|:-:|
| Q 8 al-Anfāl  | 64, 65, 70                  | 3 | 75 |
| Q 9 al-Tawba  | 73                          | 1 | 129 |
| Q 33 al-Aḥzāb | 1, 28, 45, 50, 59           | 5 | 73 |
| Q 60 al-Mumtaḥana | 12                      | 1 | 13 |
| Q 65 al-Ṭalāq | 1                           | 1 | 12 |
| Q 66 al-Taḥrīm | 1, 9                       | 2 | 12 |

Total: 13 attestations / 6 surahs / 314 cluster-verses (~5.0% of corpus 6,236 verses). Q 33 al-Aḥzāb carries the densest concentration (5 of 13 attestations = 38.5%). The cluster overlaps with prior findings: Q 60, 65, 66 are in the H-NEW-1261 Q 49 FR-cluster TARGET-SET; Q 8 and Q 9 are mid-corpus Medinan jurisprudence; Q 33 al-Aḥzāb is the top-UAS surah (H-NEW-840 rank 1).

## Hypothesis

The 6 surahs containing *yā-ayyuhā al-nabī* form a Fisher-Rao-cohesive cluster on the H-NEW-111 root-distribution instrument: the mean intra-cluster pairwise FR is LOWER than 95% of size-matched random samples (one-sided).

## Test design

### Cell A (uniform null)

Compute mean pairwise FR among {Q 8, 9, 33, 60, 65, 66} (15 pairs).
Permutation null: 10,000 random 6-surah samples from `range(1, 115)`.
PASS if `p_perm ≤ 0.025`; NULL otherwise.

### Cell B (length-matched null)

Same observed statistic. Null restricted to 6-surah samples whose total verse-count falls within ±20% of the observed cluster total (75 + 129 + 73 + 13 + 12 + 12 = 314 verses → window [251.2, 376.8]).
PASS if `p_perm ≤ 0.025`; NULL otherwise.

### Bonferroni

k = 2 cells. α_bon = 0.05 / 2 = 0.025 per cell.

### MW-5 positive control

Use H-NEW-1190 *wa-mā adrāka mā* sub-sample {Q 69, 97, 101} (deterministic, as specified in the dispatch prompt). H-NEW-1190 confirmed FR-cohesive at p = 0.00068. The PC permutation test on these 3 surahs (3 pairs) must pass at `p_pc ≤ 0.05`.

### Acceptance windows

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length confound) |
| ✗ | ✓ | ✓ | PARTIAL |
| ✗ | ✗ | ✓ | NULL |
| any | any | ✗ | NULL-BROKEN |

### Anti-flip (direction-lock)

Reverse direction (cluster mean ≥ 95th percentile) is NOT a reportable PASS. If observed, publish as NULL with explicit reverse-direction pre-commit-violation note per Protocol §1.8.

## Garden-of-forking-paths log (BEFORE run)

1. **Cluster membership**: locked at 6 surahs via direct regex over no-tashkeel corpus. Q 73 (*al-muzzammil*) and Q 74 (*al-muddaththir*) explicitly EXCLUDED because their first verses use different epithets (verified: Q 73:1 = *yā-ayyuhā al-muzzammil*; Q 74:1 = *yā-ayyuhā al-muddaththir*). The construction is *yā-ayyuhā al-nabī* (O Prophet) — strict literal match.
2. **Direction**: locked one-sided "cluster mean is LOWER than null."
3. **FR matrix**: H-NEW-111 root-distribution (the same instrument used by H-NEW-1190, 1261, 1320, 1340).
4. **Length-match window**: ±20% (same convention as H-NEW-1340).
5. **PC sub-sample**: {Q 69, 97, 101} fixed in dispatch prompt; not selected post-hoc.
6. **Seed**: 20260509 (session-day convention).
7. **n_perm**: 10,000 (Protocol MW-2 floor).
8. **α**: 0.025 per cell after k=2 Bonferroni.

## A-priori expectation

The cluster spans long Medinan jurisprudence (Q 8, 9 — battle + treaty; Q 33 — Confederates + Prophet's household) and short Medinan domestic-marriage law (Q 60, 65, 66). Q 33 is a UAS rank-1 anchor. The construction *yā-ayyuhā al-nabī* is THEMATICALLY narrow: direct second-person command to the Prophet, often regarding his household, his wives, or his stance toward unbelievers/hypocrites.

Per cross-finding-025 (marker-thickness): the prophet-vocative is a **3-token phrase** (slightly THICKER than the 5-token *yā-ayyuhā alladhīna āmanū* but applied as a discourse-anchor, NOT every verse). Three of the six members (Q 60, 65, 66) are short Medinan household-jurisprudence and previously shown to cluster tightly via H-NEW-1261 (Q 49 al-Ḥujurāt FR-cluster TARGET-SET). Q 8 + Q 9 are long Medinan jurisprudence (mushaf-adjacent). Q 33 is the top-UAS Medinan anchor.

**Prediction**: a PASS is plausible because the cluster overlaps significantly with the H-NEW-1261 jurisprudential-Medinan cluster. However, the cluster mixes long-Q9 + short-Q66, so length-matched null (Cell B) could weaken the signal. A DESCRIPTIVE-ONLY or PARTIAL outcome is possible.

## Connection to existing findings

- **H-NEW-1260/1261/1262/1263**: Q 49 al-Ḥujurāt specialist findings. Q 49 contains *yā-ayyuhā alladhīna āmanū* (5 instances) but NOT *yā-ayyuhā al-nabī*. This is a sister-construction test.
- **H-NEW-1190**: 10-surah *wa-mā adrāka mā* cluster (PASS at p=0.00068). Serves as MW-5 PC.
- **H-NEW-1340**: *al-ḥamdu li-llāh* 5-surah opener cluster — analogous classical-form-pattern test on opener-formula cluster.
- **H-NEW-840**: UAS rank-1 = Q 33. The cluster contains the top-UAS surah.
- **Cross-finding-025**: marker-thickness rule applied to a new cluster.
- **Cross-finding-012**: Late-Meccan apparatus excludes this cluster (all Medinan).
- **al-Suyūṭī, *al-Itqān*, nawʿ 51 *fī khiṭābātihi*** — classifies Quranic addresses (vocatives) by addressee; *yā-ayyuhā al-nabī* is treated as a distinct category.

## Pre-commit attestation

This pre-reg is locked. The companion script `scripts/h-new-1360.py` computes SHA256 of this file at runtime and aborts if mismatched. Direction and acceptance windows are fixed before any FR-matrix lookup of the cluster.
