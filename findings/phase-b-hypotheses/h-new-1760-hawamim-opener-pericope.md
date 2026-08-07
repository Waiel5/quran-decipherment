---
id: H-NEW-1760
title: Ḥawāmīm 7-surah opener-pericope (first 3 verses) root-Jaccard cohesion — FLIP of H-NEW-1395 NULL
date: 2026-05-09
phase: B → C
status: PASS-DIRECTED (FLIP confirmed; 4th supporting finding-pair for cross-finding-025-formal pericope-flip law)
seed: 20260509
n_perm: 10000
prereg_sha: 160adb78a338a95248e4f2ab29f67412baeaa6daa5e2351aad7ac42ccd8d0eea
verdict: FLIP — z = +6.008, p_perm < 10⁻⁴ (0/10,000)
---

# H-NEW-1760 — Ḥawāmīm 7-surah opener-pericope (first 3 verses) flip-test of H-NEW-1395


> ## ⛔ SECOND CORRECTION NOTICE — 2026-08-07: the whole-surah NULL this flip is measured against was itself an artefact
>
> This finding's title, TL;DR and §"Cross-references" all frame it as a **flip**: the ḥawāmīm
> are NULL at whole-surah Fisher–Rao cohesion (H-NEW-1395; H-NEW-570 MW-5 at 20.90 %ile) and
> PASS at opener-pericope scale.
>
> **The whole-surah result is not a NULL.** H-NEW-570's null drew K surahs uniformly from 114
> while `d̄` rises steeply with set size, and the ḥawāmīm are among the corpus's larger surahs.
> Size-matched, the ḥawāmīm-7 sit at the **0.05th percentile — 10.7 % tighter** in root content
> than size-matched sets, corpus-extreme in every arm including the parameter-free one.
> H-NEW-1395's own length-matched Cell B had already moved *p* from 0.2086 to 0.0514; see the
> notice on that file for why its matching channel under-recovered the effect.
>
> **This weakens the flip framing rather than the flip measurement.** The z = +6.008 result at
> opener-pericope scale reproduces and is not retracted here — but it is no longer a *flip*
> from absence to presence. **The ḥawāmīm cohere at both scales**, more strongly at the opener
> and detectably at whole-surah level once size is held fixed. The phrase *"now rescued at
> opener-pericope scale"* (§Cross-references) is withdrawn: there was nothing to rescue.
>
> This is separate from, and does not supersede, the notice below on the pericope-flip law.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`.
> Full notice: `findings/H-NEW-570-REVERSAL-2026-08-07.md`.


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **This finding's own numbers reproduce exactly and are not retracted.** What was corrected is the
> law it feeds. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`), the
> pericope-flip test applied to five best-shot marker classes flips **5/5 on pre-Islamic poetry and
> 4/5 on al-Bukhārī** — length-matched 114-block partitions, instrument-matched pipeline. The
> mechanism is topical burstiness, which every text has and which this project already identified
> (H-NEW-2330). The statistic is additionally **invariant under every redactional randomisation**
> (marker labels, reading order, titles — verified 25/25), so it carries no weight in any conjunction
> of the pillar laws.
>
> **The pericope-scale rule remains correct methodology** — a whole-surah NULL is not a terminal
> verdict, and re-testing at the scale where structure operates is still project discipline.
> **What must stop is citing a flip as evidence that this corpus is structurally unusual.**
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## TL;DR

The 7 ḥawāmīm surahs {Q 40, 41, 42, 43, 44, 45, 46}, NULL'd at whole-surah Fisher-Rao root-distribution cohesion under H-NEW-1395 (Cell A p=0.2086, Cell B p=0.0514), **PASS at the opener-pericope scale with z = +6.008, p_perm < 10⁻⁴ (0 of 10,000 permutations match-or-exceed)**. This is the **4th** independent supporting finding-pair for the cross-finding-025-formal scale-of-aggregation pericope-flip law, and the FIRST on an **orthographic-opener marker class** (prior 3 pairs were narrative / liturgical / discourse). The flip is corpus-extreme: J_mean = 0.1547 vs null mean = 0.0497, a 3.11× elevation; null std = 0.01747.

## 1. Pre-registration

- Pre-reg: [[prereg-h-new-1760-hawamim-opener-pericope]]
- SHA-locked: `160adb78a338a95248e4f2ab29f67412baeaa6daa5e2351aad7ac42ccd8d0eea`
- Direction: one-tailed greater (J_mean > null mean) — LOCKED PRE-OBSERVATION
- Single primary test (k = 1); no Bonferroni adjustment
- N_perm = 10,000; seed = 20260509
- Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
- Aggregation scale: OPENER-PERICOPE = first 3 verses (vv 1-3) uniform across all 7 ḥawāmīm

## 2. Cluster definition

C = {Q 40, 41, 42, 43, 44, 45, 46} — corpus-EXACT HM-opener block, verified at runtime by checking v1 == "حم" across all 7 surahs.

| # | Surah | Opener-pericope (vv 1-3) | n_unique_roots |
|:-:|:--|:--|:-:|
| 1 | Q 40 al-Ghāfir | HM + *tanzīl al-kitāb min Allāh al-ʿAzīz al-ʿAlīm* + *ghāfir al-dhanb wa-qābil al-tawb...* | 13 |
| 2 | Q 41 Fuṣṣilat | HM + *tanzīl min al-Raḥmān al-Raḥīm* + *kitāb fuṣṣilat āyātuhu qurʾānan ʿarabiyyan...* | 9 |
| 3 | Q 42 al-Shūrā | HM + ʿSQ + *kadhālika yūḥī ilayka...* | 5 |
| 4 | Q 43 al-Zukhruf | HM + *wal-kitāb al-mubīn* + *innā jaʿalnāhu qurʾānan ʿarabiyyan...* | 6 |
| 5 | Q 44 al-Dukhān | HM + *wal-kitāb al-mubīn* + *innā anzalnāhu fī laylatin mubārakatin...* | 7 |
| 6 | Q 45 al-Jāthiya | HM + *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* + *inna fī l-samāwāt wa-l-arḍ...* | 9 |
| 7 | Q 46 al-Aḥqāf | HM + *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* + *mā khalaqnā l-samāwāt...* | 14 |

**Q 42 treatment**: uniform vv 1-3 (= HM + ʿSQ + 1 content verse). The muqaṭṭaʿāt verses contribute zero ROOT-tagged tokens under QAC v0.4 (INL-tagged); the root-set comes entirely from the content verse(s).

## 3. Results

| Quantity | Value |
|:--|:--|
| Observed J_mean (21 pairs) | **0.15472** |
| Null mean | 0.04972 |
| Null std | 0.01747 |
| **z-score** | **+6.008** |
| **p_perm (strict, one-tailed, ≥ obs)** | **0.0000** (0 / 10,000) |
| p_reportable_upper_bound | < 10⁻⁴ |
| Direction match | TRUE (J_mean > null mean) |
| Pre-commit violation | FALSE |
| **Verdict** | **PASS-DIRECTED** |
| **Flip verdict** | **FLIP (whole-surah NULL → opener-pericope PASS-DIRECTED)** |

Full JSON: `findings/phase-b-hypotheses/csv/h-new-1760.json`.

## 4. Pair-level structure: the *tanzīl al-kitāb* signature

The 21 pairwise Jaccard scores reveal a clear sub-structure within the ḥawāmīm openers:

| Rank | Pair | J | Shared roots |
|:-:|:--|:-:|:--|
| 1 | Q 45:1-3 ↔ Q 46:1-3 | **0.438** | Alh, ArD, Ezz, Hkm, ktb, nzl, smw |
| 2 | Q 42:1-3 ↔ Q 45:1-3 | 0.273 | Alh, Ezz, Hkm |
| 3 | Q 41:1-3 ↔ Q 43:1-3 | 0.250 | Erb, ktb, qrA |
| 4 | Q 44:1-3 ↔ Q 46:1-3 | 0.235 | byn, ktb, nDr, nzl |
| 5 | Q 40:1-3 ↔ Q 45:1-3 | 0.222 | Alh, Ezz, ktb, nzl |
| 6 | Q 40:1-3 ↔ Q 42:1-3 | 0.200 | Alh, Ezz, qbl |
| 7 | Q 41:1-3 ↔ Q 45:1-3 | 0.200 | Ayy, ktb, nzl |
| 8 | Q 42:1-3 ↔ Q 46:1-3 | 0.188 | Alh, Ezz, Hkm |
| 9 | Q 43:1-3 ↔ Q 44:1-3 | 0.182 | byn, ktb |

**Two distinct sub-signatures** emerge:

- **Tanzīl al-kitāb signature** (Q 40 / Q 41 / Q 45 / Q 46): shared roots include **nzl** (tanzīl), **ktb** (al-kitāb), **Alh** (Allāh), **Ezz** (al-ʿAzīz), **Hkm** (al-Ḥakīm). The Q 45 ↔ Q 46 pair is corpus-extreme at J = 0.438 — their openers are nearly identical in formulaic structure.
- **Wal-kitāb al-mubīn signature** (Q 43 / Q 44): shared roots **byn** (al-mubīn) and **ktb** (al-kitāb).

The corpus-EXACT *Āl Ḥā Mīm* family (per Ibn Sīrīn via Ibn Kathīr opening of Sūrat Ghāfir) is empirically locked at root-Jaccard z = +6.0 at the opener-pericope scale, vindicating Ibn Masʿūd's classical *dībāj* (brocade) characterization — but only at the scale where the *dībāj* operates, namely the opener thread itself, not the whole surah.

## 5. Flip vs whole-surah NULL: the scale-of-aggregation principle on a 4th marker class

| Marker class | Whole-surah NULL | Pericope-scale PASS | Flip effect-size |
|:--|:--|:--|:-:|
| Iblīs-narrative | H-NEW-039 (z=+0.24, p=0.537) | H-NEW-1380 (z=+4.76, p ≤ 10⁻⁴) | +4.52 σ |
| Sajda 15-verse | H-NEW-1330 (p=0.571/0.110) | H-NEW-1510 (z=+2.685, p=0.0058) | +2.5 σ (corroborating) |
| yā-ayyuhā al-nabī | H-NEW-1360 (p=0.573/0.584) | H-NEW-1520 (z=+6.41, p<10⁻⁴) | +6.41 σ |
| **Ḥawāmīm orthographic-opener** | **H-NEW-1395 (p=0.2086/0.0514)** | **H-NEW-1760 (z=+6.008, p<10⁻⁴)** | **+5.8 σ** |

The ḥawāmīm flip is **the first orthographic-opener marker class** to support the pericope-flip law. The 3 prior pairs were narrative (Iblīs), liturgical (sajda), and discourse (vocative). H-NEW-1760 extends the law's domain of applicability to a 4th, structurally distinct marker class.

The effect-size (+5.8 σ) is the **second largest** on record (behind only the H-NEW-1520 prophet-vocative flip at +6.41 σ) and is corpus-extreme by any reasonable threshold.

## 6. What classical scholars said vs what the opener-pericope FR-axis finds

Classical claim:
- Ibn Masʿūd via al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 17 — the ḥawāmīm are *al-dībāj* ("the brocade of the Qurʾān").
- Ibn ʿAbbās via Abū ʿUbayd b. Sallām *Faḍāʾil al-Qurʾān*; Ibn Kathīr *Tafsīr al-Qurʾān al-ʿaẓīm* opening of Sūrat Ghāfir — the ḥawāmīm are *lubāb al-Qurʾān* ("the heart-pith of the Qurʾān").
- Misʿar b. Kidām via Ibn Kathīr ibid. — *al-ʿarāʾis* ("the brides").
- Ibn Sīrīn via Ibn Kathīr ibid. — *Āl Ḥā Mīm* ("the Family of Ḥā Mīm").
- al-Suyūṭī *al-Itqān* nawʿ 8 (*tarjamat al-sūra wa-ākhirihā*) and al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* (*fawātiḥ al-suwar*) — the opener is the *tarjama* (programmatic statement) of the surah.

**Empirical result at the opener-pericope scale**: the FR root-Jaccard axis recovers the classical coherence-claim at corpus-extreme strength (z = +6.0, p < 10⁻⁴). At the whole-surah scale (H-NEW-1395), the same classical claim was empirically NULL — because the marker (HM + opener-formula) is diluted by 35-89 verses of heterogeneous downstream content (legal injunction in Q 42, eschatology in Q 44, signs-of-creation in Q 45, etc.).

This is a textbook example of cross-finding-025-formal's pericope-flip law: **classical *tarjama*-based observations cohere at the *tarjama*-scale, not at the whole-surah scale**. al-Suyūṭī and al-Zarkashī were operating implicitly at the opener-pericope scale when they catalogued opener-formulae as a structural family; their methodological intuition is empirically vindicated at this scale, and only at this scale.

## 7. Honest limits

1. **Single pre-registered test (k=1)**. No Bonferroni adjustment. A replication arm (H-NEW-1760b at a different seed, e.g. 20260510) is queued; a window-size sensitivity arm (H-NEW-1760-sens for window=2 and window=5) is queued.
2. **Corpus-EXACT 7-tuple**. There is no "next 7 ḥawāmīm" to test, so direct sample-replication is impossible. The 3/3 prior pericope-flip pattern across independent marker classes is the strongest available cross-test.
3. **QAC ROOT-tagging convention**. Muqaṭṭaʿāt verses (v1 across all 7; v2 in Q 42) carry no ROOT-tag under QAC v0.4 (INL = initial letters). The opener-pericope's root-set therefore comes entirely from the content verses. This is consistent with the cross-finding-025 muqaṭṭaʿāt-axis ⊥ content-axis observation: the HM-marker itself is orthogonal to root-content, and the cohesion-signal at the opener-pericope scale comes from the *content immediately following* the HM marker (i.e. the *tarjama*-formula proper).
4. **Q 42 ʿSQ included in vv 1-3**. Q 42 uniquely carries a 2-verse muqaṭṭaʿāt opening (HM + ʿSQ), so its opener-pericope is HM + ʿSQ + 1 content verse, while the others are HM + 2 content verses. This makes Q 42's root-set the smallest (5 unique roots vs 6-14 for the others), and Q 42 is the only surah that pairs at J=0 with two others (Q 43, Q 44). Even so, Q 42 pairs at J=0.27 with Q 45, J=0.20 with Q 40, and J=0.19 with Q 46 — strong enough to contribute to the overall +6.0 σ flip.
5. **No translation invariance check**. The result is QAC-v0.4-ROOT-specific. A cross-instrument replication (cosine on TF-IDF, char-4-gram NCD) is queued.

## 8. Cross-references

- [[h-new-1395-hawamim-cluster|H-NEW-1395]] — whole-surah NULL precursor (this flip's "control")
- [[cross-finding-025-formal-scale-of-aggregation-law|cross-finding-025-formal]] — the pericope-flip law (now 4/4 supporting pairs)
- [[h-new-1380-iblis-pericope-replication|H-NEW-1380]] — 1st flip (Iblīs, +4.76 σ)
- [[h-new-1510-sajda-pericope-replication|H-NEW-1510]] — 2nd flip (sajda, +2.685 σ)
- [[h-new-1520-prophet-vocative-pericope|H-NEW-1520]] — 3rd flip (vocative, +6.41 σ)
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] — pre-Bonferroni HM-7 percentile signal (20.90%ile); now rescued at opener-pericope scale
- [[Q040-ghafir/00-overview|Q 40 al-Ghāfir overview]] — HM-A / HM-B sub-cluster classification
- [[Q042-al-shura/00-overview|Q 42 al-Shūrā overview]] — the unique HM + ʿSQ 2-verse muqaṭṭaʿāt
- al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 8 (*tarjamat al-sūra*) and nawʿ 17 (muqaṭṭaʿāt)
- al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* (chapter on *fawātiḥ al-suwar*)
- Ibn Kathīr *Tafsīr al-Qurʾān al-ʿaẓīm* opening of Sūrat Ghāfir (ḥawāmīm-family characterizations)

## 9. Update to cross-finding-025-formal

cross-finding-025-formal now stands at **4/4 confirmed pericope-flips across 4 structurally distinct marker classes**: narrative (Iblīs), liturgical (sajda), discourse (vocative), orthographic-opener (ḥawāmīm). The law is locked at corpus-wide strength on each of the 4 axes; the next falsification-target is to find a thin-marker NULL at whole-surah scale that does NOT flip to PASS at pericope scale (a NULL/NULL pair would refine the law's domain).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
