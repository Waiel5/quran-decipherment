---
id: H-NEW-1395
title: Ḥawāmīm 7-surah cluster {Q 40-46} Fisher-Rao root-distribution cohesion
date: 2026-05-09
phase: B
status: NULL (CONFIRMED-NULL via valid PC)
seed: 20260509
n_perm: 10000
prereg_sha: 06bc435a00d5622d29c8e3d459ffe8083e020aafa0ef9fa0eac83583ea9f296f
verdict: NULL — HM-7 NOT FR-cohesive on root distribution
---

# H-NEW-1395 — Ḥawāmīm 7-cluster Fisher-Rao cohesion test

## TL;DR

The 7 consecutive ḥawāmīm surahs (Q 40-46), the corpus-EXACT HM-opener block, are **NOT FR-cohesive on QAC root-distribution**. Observed intra-cluster mean Fisher-Rao distance d̄(HM-7) = **0.8672**; lower than the uniform-7 null mean (0.9230) and length-matched null mean — direction-consistent — but neither cell crosses Bonferroni α=0.025. PC valid (p_pc=0.0414). The HM cluster is a **muqaṭṭaʿāt-axis cluster, not a root-distribution-axis cluster**, replicating the pattern observed in H-NEW-1301 (IMPV-qrA) and consistent with cross-finding-025's marker-thickness rule.

## 1. Pre-registration

- Pre-reg: [[prereg-h-new-1395-hawamim-cluster]]
- SHA-locked: `06bc435a00d5622d29c8e3d459ffe8083e020aafa0ef9fa0eac83583ea9f296f`
- Direction: one-tailed lower (cluster d̄ ≤ null d̄)
- Bonferroni α_corr = 0.025 (k=2 cells: A uniform-7, B length-matched-7)
- N_perm = 10,000; seed = 20260509

## 2. Cluster definition

C = {Q 40, 41, 42, 43, 44, 45, 46} — verified corpus-EXACT under Q040-F-02:
- Q 40 *Ghāfir* (85 v), Q 41 *Fuṣṣilat* (54 v), Q 42 *al-Shūrā* (53 v), Q 43 *al-Zukhruf* (89 v), Q 44 *al-Dukhān* (59 v), Q 45 *al-Jāthiya* (37 v), Q 46 *al-Aḥqāf* (35 v).
- Total verses = 412. All 7 first verses == "حم" exactly (no-tashkeel).

## 3. Results

| Quantity | Value |
|:--|:--|
| Observed d̄(HM-7) | **0.8672** |
| Cell A null mean (uniform-7) | 0.9230 |
| Cell A null p5 | 0.8617 |
| Cell A p (one-tailed lower) | **0.2086** |
| Cell A pass at α=0.025 | ✗ |
| Cell B null mean (length-matched ±20%) | 0.91 |
| Cell B p (one-tailed lower) | **0.0514** |
| Cell B pass at α=0.025 | ✗ |
| Cell B n | 10,000 |
| MW-5 PC subsample (4-of-10 adraka-mā H-NEW-1190) | {Q 69, 74, 97, 101} |
| MW-5 PC d̄ | (computed; in lower tail of uniform-4 null) |
| MW-5 PC p_pc | **0.0414** |
| MW-5 PC pass at 0.05 | ✓ |

Full JSON: `findings/phase-b-hypotheses/csv/h-new-1395.json`.

## 4. Verdict: NULL

**HM-7 is NOT FR-cohesive on root-distribution** at pre-committed Bonferroni-corrected α=0.025.

The direction is correct (cluster d̄ < null mean in both cells), but the effect size is sub-threshold:
- Cell A p=0.2086 — only 21% of uniform-7 samples have lower d̄ than HM-7. The cluster sits in the upper-left third of the null distribution, not the extreme lower tail.
- Cell B p=0.0514 — once length is controlled (HM-7 contains both Q 43 at 89 v and Q 46 at 35 v), the effect tightens but still misses α=0.025 by ~2pp.

The MW-5 PC is valid (p_pc=0.0414 ≤ 0.05) — the H-NEW-111 FR matrix correctly detects cohesion on the known-cohesive H-NEW-1190 adraka-mā sub-cluster, so the NULL is NOT due to instrument unreliability.

## 5. Connection to prior findings

This NULL **replicates the pattern** established by:
- **H-NEW-1301 NULL-BROKEN** (IMPV-qrA cluster {Q 73, 74, 96}): the HM-axis is muqaṭṭāʿat-tight, NOT FR-root-tight.
- **H-NEW-570** (HM-7 at 20.90 percentile FR-cohesion): identified the moderate-only signal pre-Bonferroni; H-NEW-1395 now provides the direction-locked Bonferroni-corrected test that demotes that signal to formal NULL.
- **cross-finding-025** (marker-thickness rule): the ḥawāmīm share a SINGLE marker (حم — 2 letters in each surah's v.1). Per the rule, single thematic/liturgical/orthographic markers are necessary-not-sufficient for FR-cohesion. HM-7 marker thickness ≈ 2 graphemes per surah vs ~1,000-9,000 graphemes per surah — far below the 10% threshold cross-finding-025 identifies as the boundary.

## 6. What classical scholars said vs what the FR-axis finds

Classical claim: the ḥawāmīm are *al-dībāj* (Ibn Masʿūd via al-Suyūṭī *al-Itqān* nawʿ 17), *lubāb al-Qurʾān* (Ibn ʿAbbās via Abū ʿUbayd b. Sallām *Faḍāʾil al-Qurʾān*; Ibn Kathīr tafsīr opening of Sūrat Ghāfir), *al-ʿarāʾis* (Misʿar b. Kidām via Ibn Kathīr ibid.), or *Āl Ḥā Mīm* (Ibn Sīrīn via Ibn Kathīr ibid.) — all positioning HM as a coherent thematic family.

Empirical result: the FR-roots distance axis does NOT recover this coherence at Bonferroni-corrected strength. The classical coherence-claim either:
- (a) holds on axes other than QAC-root-distribution (e.g., theme, opening formula, rhyme, eschatological intensity, position) — testable;
- (b) was a literary-rhetorical observation that does not survive translation to root-frequency metrics;
- (c) is true but at a magnitude under the Bonferroni-corrected detection threshold for n=7 with n_perm=10,000.

cell B's p=0.0514 (one cell of two) is **suggestive but not significant**. A future test on a different metric (theme-keyword density; eschatological-vocabulary cohesion; iʿjāz signature similarity) could rescue the classical claim on a different axis. This is the proper way to follow up.

## 7. Honest limits

1. The pre-reg pre-committed Bonferroni-corrected α=0.025 across 2 cells. With α=0.05 single-cell, cell B passes (p=0.0514 borderline). The Bonferroni discipline is what makes this a NULL.
2. PC uses a 4-of-10 sub-sample of H-NEW-1190's 10-cluster — a smaller sample than the cluster under test. Validity is acknowledged but the PC's statistical power is lower than the 7-of-114 test.
3. The HM-axis defines a corpus-EXACT 7-tuple — there is no "next 7" to test, so direct replication is impossible. Replication options: alt-text (Uthmani-consonantal); different distance metric (cosine on TF-IDF); HM-A vs HM-B split (per Q040-overview claim).

## 8. Cross-references

- [[Q040-ghafir/00-overview|Q 40 Ghāfir overview]] — sub-cluster role and HM-A/HM-B split
- [[h-new-1301-impv-qra-cluster|H-NEW-1301]] — IMPV-qrA muqaṭṭāʿat NULL precedent
- [[cross-finding-025-marker-thickness-vs-fr-cohesion-threshold|cross-finding-025]] — marker-thickness rule
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] — pre-Bonferroni precursor
- [[h-new-1340-hamdu-lillah-cluster|H-NEW-1340]] — analogous NULL pattern on a different opener-class

*Bismillāhi al-Raḥmāni al-Raḥīm.*
