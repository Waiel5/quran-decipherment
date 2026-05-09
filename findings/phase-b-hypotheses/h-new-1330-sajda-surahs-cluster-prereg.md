---
id: H-NEW-1330
title: Sajda-surahs 14-surah cluster Fisher-Rao cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1330-sajda-cluster
alpha_bon: 0.025
direction_of_effect: The 14 surahs containing sajdat al-tilāwa verses {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} have a mean intra-cluster Fisher-Rao distance lower than 95% of length-matched random 14-surah samples
origin: handoff §7b — sajda-surahs structural cluster test (one of the suggested high-EV inline tests)
verdict_ceiling: PASS-DIRECTED (single planned pre-registered test)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  sajda_surah_definition: classical-14-list (Q 7:206, 13:15, 16:50, 17:109, 19:58, 22:18, 25:60, 27:26, 32:15, 38:24, 41:38, 53:62, 84:21, 96:19)
  null_model: random-14-surah-samples-no-Q1-uniform-and-length-matched
---

# H-NEW-1330 pre-registration

## Origin

Handoff §7b lists "sajda-surahs cluster cohesion" as a suggested high-EV test. The 14 sajda-surahs (sujūd al-tilāwa, prostration-of-recitation) form a classical liturgical-marker class: each contains a verse before which the reciter prostrates during recitation. The tradition is recorded in al-Bukhārī Kitāb Sujūd al-Qurʾān, al-Tirmidhī Kitāb al-Witr, al-Suyūṭī *al-Itqān* nawʿ on sujūd al-tilāwa.

## Hypothesis

The 14 sajda-surahs form a Fisher-Rao cohesive cluster on the H-NEW-111 root-distribution instrument.

## Cluster locked from classical tradition

{Q 7 al-Aʿrāf, Q 13 al-Raʿd, Q 16 al-Naḥl, Q 17 al-Isrāʾ, Q 19 Maryam, Q 22 al-Ḥajj, Q 25 al-Furqān, Q 27 al-Naml, Q 32 al-Sajda, Q 38 Ṣād, Q 41 Fuṣṣilat, Q 53 al-Najm, Q 84 al-Inshiqāq, Q 96 al-ʿAlaq}

Note: the Mālikī school excludes Q 38 (treats v 24 as sujūd shukr); some traditions add Q 22:77 making 15 sajda-events but still 14 surahs; the Imāmī (Shīʿī) tradition has only 4 mandatory sajdas {Q 32, 41, 53, 96}. This pre-reg uses the **broadest classical-Sunnī list of 14 surahs** as default. A rules-tuple-sensitivity test under the Imāmī 4-surah list is **not** in scope.

## Test design

### Cell A (uniform null)

Mean intra-cluster pairwise FR (14 surahs = 91 pairs). Permutation null: 10000 random 14-of-113 samples (excluding Q 1). Direction-locked: intra-cluster mean ≤ permutation null 5th percentile.

PASS if p_perm ≤ 0.025; NULL otherwise.

### Cell B (length-matched control)

Same test restricting null to 14-surah samples with total verse-count within ±15% of observed (sajda cluster total ≈ Q 7=206, Q 13=43, Q 16=128, Q 17=111, Q 19=98, Q 22=78, Q 25=77, Q 27=93, Q 32=30, Q 38=88, Q 41=54, Q 53=62, Q 84=25, Q 96=19 → ≈ 1112 verses).

PASS if p_perm ≤ 0.025; NULL otherwise.

### Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025 per cell.

### MW-5 positive control

H-NEW-1200 14-surah eschatology cluster {56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104} — CONFIRMED FR-cohesive at p = 0.00030. Run on this cluster directly (not sub-sample); test under uniform 14-of-113 null. PC must pass at p ≤ 0.05.

This is a **same-size** PC (14 surahs), so the null distribution is identical between PC and primary test — strongest possible PC matching.

### Acceptance windows

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length-confound) |
| ✗ | ✓ | ✓ | PARTIAL |
| ✗ | ✗ | ✓ | NULL |
| any | any | ✗ | NULL-BROKEN |

### Garden-of-forking-paths

Origin disclosed: handoff §7b. No FR-matrix value loaded for the sajda set yet. Direction locked (cluster ≤ 5th percentile null). Cluster identity locked from classical Sunnī tradition. No alternative cells. No Imāmī-list rerun within this pre-reg.

### Anti-flip

Reverse direction (cluster mean ≥ 95th percentile = anti-cohesion) is NOT a reportable PASS. Publish as NULL with reverse-direction note.

### Honest a-priori expectation

Sajda-surahs share a liturgical-marker function but span Meccan-Medinan, long-short, muqaṭṭāʿat-non-muqaṭṭāʿat. **A-priori expectation is mixed**: the function-based unity (sajda-trigger) might NOT correspond to root-distribution similarity, just as Christ-narrative thematic-unity didn't (H-NEW-1310 NULL). On the other hand, the 14 sajda verses themselves share rhetorical-positioning (typically address-of-God + cosmic-witness + prostration-trigger themes), which might cohere in root-distribution.

## Connection to existing findings

- **H-NEW-1310** Christ-narrative cluster NULL: thematic clusters do NOT cohere on root-distribution unless the theme dominates the surah's content. Sajda-trigger is a single verse per surah — even THINNER than Christ-narrative blocks. A-priori weak signal expected.
- **Q 32 al-Sajda is eponymous**: named for sajdat al-tilāwa. Yet its sajda is just one verse out of 30. The eponymy suggests the sajda was structurally anchoring at composition-time.
- **Q 53 al-Najm** is heavily-overrepresented in this cluster's mid-mushaf segment (only sajda in the Q 51-56 zone — connects to oath-cluster H-NEW-1070).
- **Cross-finding-008** muqaṭṭāʿat: 4 of 14 sajda-surahs are muqaṭṭāʿat-opened {Q 13 الر, Q 19 كهيعص, Q 27 طس, Q 32 الم, Q 38 ص, Q 41 حم}. Wait that's 6/14 ≈ 43%. Compare to corpus baseline 29/114 = 25%. Sajda-surahs are over-represented muqaṭṭāʿat at ~1.7× — flagged as descriptive observation, NOT pre-registered as a cell here.
- **Cross-finding-013** ring-topology: sajda-surahs span the corpus broadly (Q 7 to Q 96) — not clustered in mushaf position.

## Pre-commit attestation

Locked by SHA256 hash. Run script verifies before loading FR matrix.
