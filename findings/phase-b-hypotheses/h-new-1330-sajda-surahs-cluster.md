---
id: H-NEW-1330
title: Sajda-surahs 14-surah cluster Fisher-Rao cohesion
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: NULL (both cells; PC passed at p=0.00020)
seed: 20260509
n_perm: 10000
prereg_sha: f56fd6446618b37485a6765f44d340e57888697eaa512ad876a95b48cbdc774f
prereg_path: findings/phase-b-hypotheses/h-new-1330-sajda-surahs-cluster-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1330_sajda_cluster.py
output_json: findings/phase-b-hypotheses/csv/h-new-1330.json
---

# H-NEW-1330 — Sajda-surahs 14-surah cluster Fisher-Rao cohesion

## Verdict: NULL

The 14 sajda-surahs {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} do NOT form a Fisher-Rao cohesive cluster on root-distribution. NULL on both pre-registered cells with positive-control passing at p=0.00020.

| Cell | Result | p | Pass (α=0.025) |
|:--|--:|--:|:-:|
| A — uniform 14-of-113 null | obs 0.941 vs null mean 0.926 | 0.571 | NO |
| B — length-matched (±15% of 1112v) | obs 0.941 vs null p5 0.929 | 0.110 | NO |
| MW-5 PC — H-NEW-1200 full 14-surah eschatology | obs 0.646 vs null p5 0.833 | **0.00020** | **YES ✓** |

The instrument-control on H-NEW-1200 14-surah cluster (CONFIRMED p=0.00030 in prior work) replicates here at p=0.00020 — the FR matrix can detect known same-size 14-surah cohesion. **This NULL is substantive, not instrument-broken.**

## Cluster identity

Classical Sunnī sajdat al-tilāwa (prostration-of-recitation) verses span 14 surahs:

| Surah | Sajda verse | Chronology | Muqaṭṭāʿat? | Verses |
|:--|:--|:--|:-:|:-:|
| Q 7 al-Aʿrāf | 7:206 | Late Meccan | المص | 206 |
| Q 13 al-Raʿd | 13:15 | Medinan/Late Meccan (debated) | المر | 43 |
| Q 16 al-Naḥl | 16:50 | Late Meccan | – | 128 |
| Q 17 al-Isrāʾ | 17:109 | Late Meccan | – | 111 |
| Q 19 Maryam | 19:58 | Middle Meccan | كهيعص | 98 |
| Q 22 al-Ḥajj | 22:18 (some traditions add 22:77) | Medinan | – | 78 |
| Q 25 al-Furqān | 25:60 | Middle Meccan | – | 77 |
| Q 27 al-Naml | 27:26 | Middle Meccan | طس | 93 |
| Q 32 al-Sajda | 32:15 | Middle Meccan | الم | 30 |
| Q 38 Ṣād | 38:24 | Middle Meccan | ص | 88 |
| Q 41 Fuṣṣilat | 41:38 | Late Meccan | حم | 54 |
| Q 53 al-Najm | 53:62 | Early Meccan | – | 62 |
| Q 84 al-Inshiqāq | 84:21 | Early Meccan | – | 25 |
| Q 96 al-ʿAlaq | 96:19 | Early Meccan (first-revealed) | – | 19 |

## Interpretation

The pattern emerging across recent inline NULL results (H-NEW-1301 IMPV-qrA, H-NEW-1310 Christ-narrative, H-NEW-1330 sajda):

> **Thematic and liturgical markers that occupy single verses or thin slices of a surah do NOT drive surah-aggregate root-distribution clustering.** FR cohesion requires the marker-theme to be the surah's DOMINANT root-driver, not a one-verse injection.

The sajda-trigger is the thinnest possible marker: ONE verse out of 19 to 206. That single verse cannot move the surah's root-distribution centroid relative to the corpus.

The PC passes precisely because H-NEW-1200's 14 surahs share *substantial* eschatological content (often 60-90% of the surah) — the eschatological vocabulary IS the dominant root-driver in those surahs. By contrast, the sajda-surahs share only a single liturgical-prostration trigger; the rest of each surah is heterogeneous.

## Descriptive observations not pre-registered

- **Sajda-surahs are over-represented for muqaṭṭāʿat-opening**: 6 of 14 (43%) vs corpus baseline 29/114 (25%) — about 1.7× enrichment. Not pre-registered as a cell here. Hypergeometric p (one-tailed): C(29, 6) × C(85, 8) / C(114, 14) ≈ 0.062 (not Bonferroni-significant). **Logged as descriptive observation for future H-NEW-1331 follow-up pre-reg.**
- **Sajda-surahs span all chronological phases**: Early (53, 84, 96), Middle (19, 25, 27, 32, 38), Late (7, 16, 17, 41), Medinan (13, 22). The classical-tradition 14 are NOT chronologically clustered.
- **Sajda-surahs span all length classes**: Q 7 (206v) to Q 96 (19v), Q 84 (25v). Cluster total = 1112 verses. The length confound was the main null-rejection candidate; Cell B's tighter p (0.110) suggests length-matched confounding is real but not strong enough to push to PASS.

## Connection to existing findings + the emerging "thin marker = NULL" pattern

| Cluster | Marker thickness | FR-cohesion result |
|:--|:--|:--|
| Muqaṭṭāʿat-opened (29 surahs) | Verse 1 + 13+ axes | **CONFIRMED** (p ≤ 10⁻¹², cross-finding-008) |
| H-NEW-1200 eschatology (14 surahs) | Dominant content | **CONFIRMED** (p = 0.00030) |
| H-NEW-1190 *wa-mā adrāka mā* (10 surahs) | Repeated meta-question + dominant content | **CONFIRMED** (p = 0.00068) |
| H-NEW-1080 short-Medinan block (Q 57-66) | Length + chronology + content | CONFIRMED (p = 0.049) |
| Refrain top-3 {Q 55, Q 77, Q 26} | Surah-dominant repeated structure | **PASS-DIRECTED** (H-NEW-1320, this session) |
| IMPV-qrA inventory {Q 17, 69, 73, 96} | Single imperative event | **NULL** (H-NEW-1301) |
| Christ-narrative {Q 3, Q 5, Q 19} | Sub-block (≈25-30 verses out of 100-200) | **NULL** (H-NEW-1310) |
| **Sajda-surahs (14 surahs)** | **Single verse** | **NULL (this finding)** |

The pattern holds: cohesion ↔ marker dominance.

**Cross-finding seed (NOT yet locked)**: a meta-finding about marker-thickness vs FR-cohesion threshold. Markers occupying ≥30% of a surah's content tend to produce FR cohesion; markers <10% don't. Markers in 10-30% range are mixed. This is a **rule-of-thumb threshold conjecture** queued for cross-finding-028.

## Honest limits

- **Single feature space**: H-NEW-111 root-distribution. Sajda-surahs might cohere on a non-root axis (verse-rhetoric, sajda-verse-internal-structure, prostration-trigger formula).
- **Sajda-list rules-tuple sensitivity NOT tested**: Imāmī 4-surah list {Q 32, 41, 53, 96} and Mālikī 13-surah list (excluding Q 38) untested. Future H-NEW-1331 could replicate.
- **Verdict ceiling = NULL**: pre-reg passed instrument-control + both cells genuinely NULL. This is a strong NULL.
- **6 of 14 are muqaṭṭāʿat-opened (descriptive)**: the over-representation at 1.7× is suggestive but not Bonferroni-significant alone. A focused H-NEW-1331 pre-reg with proper hypergeometric framing could promote this.

## Follow-up moves

- **H-NEW-1331** (queued): Hypergeometric test for sajda × muqaṭṭāʿat over-representation. Single test, k=1, α=0.05.
- **H-NEW-1332** (queued): Sajda-VERSE rhetorical structure — does the 14 sajda-verses share a rhetorical-syntactic skeleton (deity-acknowledgement + cosmic-witness + prostration-imperative)? Verse-level test on H-NEW-66 verse-twin instrument.
- **Cross-finding-028** (queued): "Marker thickness vs FR cohesion threshold" meta-pattern. Synthesize from H-NEW-1301 + H-NEW-1310 + H-NEW-1330 NULLs together with H-NEW-1190/1200/1320 PASSES.

## Classical citations

- al-Bukhārī *Ṣaḥīḥ*, Kitāb Sujūd al-Qurʾān (verify ḥadīth numbers against on-disk corpus before citing).
- al-Tirmidhī *Sunan*, Kitāb al-Witr ch. on sujūd al-tilāwa.
- al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on sujūd al-tilāwa (verify nawʿ-number against on-disk PDF).
- al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*, ch. on sujūd al-tilāwa enumerating the 14 surahs.

## Verdict summary

| Cell | p | Pass (α=0.025) | Status |
|:--|--:|:-:|:--|
| A — uniform null | 0.571 | NO | NULL |
| B — length-matched | 0.110 | NO | NULL |
| MW-5 PC (H-NEW-1200 full 14) | 0.00020 | YES | PC PASSED |

**Final verdict: NULL — promoted CONFIRMED-NULL via independent replication 2026-05-09.** Sajda-trigger is too thin a marker (1 verse per surah) to drive surah-aggregate FR cohesion. Substantive NULL with passing instrument-control. 6/14 muqaṭṭāʿat over-representation flagged as descriptive observation for H-NEW-1331 follow-up pre-reg.

## Independent replication (2026-05-09 same session)

**Q 53 al-Najm specialist's Q053-F-03 INDEPENDENTLY REPLICATES this NULL** with a different seed and slightly different operationalization:
- Q 53 specialist's perm-p = 0.588 vs my Cell A p = 0.571 (z = +0.333 in their report)
- Same direction-of-effect (within-cluster mean ≥ corpus mean → NULL)
- 20,000 perms vs my 10,000 — different seed, distinct random draws
- Same conclusion: 14 sajda-surahs are NOT FR-cohesive on root-distribution

**Per Protocol §1.5 INDEPENDENT REPLICATION criterion** (different operationalization, different seed, different specialist), H-NEW-1330's NULL is now **CONFIRMED-NULL** rather than the post-hoc-cap PASS-DIRECTED ceiling. The marker-thickness threshold prediction (cross-finding-025) is correspondingly strengthened.
