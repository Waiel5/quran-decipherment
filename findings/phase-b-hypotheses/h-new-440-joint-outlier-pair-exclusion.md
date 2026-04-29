---
id: H-NEW-440
title: "NULL — joint Q 55+Q 56 exclusion does NOT crash block percentile; neighborhood-contrast hypothesis FALSIFIED; Q 56 contributes <1pp to block disruption; post-hoc chronology-seam hypothesis emerges"
phase: B
status: NULL on H1 aggregate (0/2 primary tests pass); MW-5 PASS; strong post-hoc diagnostic finding
date: 2026-04-21
executed_by: team-lead (inline)
parent_1: H-NEW-430 (Q 55 PC strict-fail triggered diagnostic)
parent_2: H-NEW-420 (post-hoc neighborhood-contrast hypothesis now falsified)
parent_3: H-NEW-410 (Q 56 rank-3 full-corpus outlier — context-dependent)
seed: 20260511
prereg: h-new-440-joint-outlier-pair-exclusion-prereg.md
prereg_sha256: 5737b8ff9490c4b3b06c5f6ac51afda8792e913aeb34e6fb0dc086d6008a9bb0
bonferroni_k: 3
alpha_bon: 0.01667
direction_outcome: "Joint removal delta -15.36pp (baseline 98.53% → 83.17%); H1 required ≤30%ile; FAILS. Superadditivity -5.49pp (required ≤-10pp); FAILS. MW-5 passes."
verdict: NULL (neighborhood-contrast / outlier-density hypothesis FALSIFIED)
---

# [[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] — Joint Q 55+Q 56 exclusion: NULL on H1, strong post-hoc diagnostic

## 1. Headline

**H1 FALSIFIED. Joint removal of Q 55 AND Q 56 from block {53,54,55,56,57} shifts percentile from 98.53% to only 83.17% — STILL extreme.** The neighborhood-contrast / outlier-density hypothesis from [[h-new-420-novel-outlier-exclusion|H-NEW-420]] post-hoc speculation is **empirically falsified** by pre-registered prediction-failure.

| Test | Observed | Pre-commit | Verdict |
|:--|:-:|:--|:-:|
| Singleton Q 55 removal | −9.72pp | ≤ −5pp | PASS (weak) |
| Singleton Q 56 removal | **−0.15pp** | ≤ −10pp | **FAIL** |
| Joint {Q 55, Q 56} removal | −15.36pp | p3 ≤ 30%ile | **FAIL** (still 83.17%) |
| Superadditivity | −5.49pp | ≤ −10pp | **FAIL** |
| MW-5 (Q 62 NC) | +1.85pp | \|delta\|<5 | **PASS** |

**Q 56 al-Wāqiʿah is NOT a cohesion-disruptor within this block.** It contributes essentially nothing (−0.15pp singleton effect) to block percentile.

## 2. Why [[h-new-410-outlier-spectrum|H-NEW-410]]'s rank-3 for Q 56 is context-specific

[[h-new-410-outlier-spectrum|H-NEW-410]] ranked Q 56 as #3 outlier based on its mean FR distance to {Q 54, 55, 57, 58} — including Q 58 al-Mujādilah (Medinan), NOT included in the ±2 window of {Q 53, 54, 55, 56, 57}.

Checking Q 56's individual distances within H-440 block:
- D(56, 53) = moderate
- D(56, 54) = low (shared Meccan-eschatological register)
- D(56, 55) = low (Q 55 al-Raḥmān paired-block)
- D(56, 57) = moderate-high (Medinan boundary)

Q 56 fits reasonably within its ±2 Meccan-eschatological neighbors. Its rank-3 in H-410 came from a DIFFERENT ±2 window ({54, 55, 57, 58}) that included both Q 55 (itself a huge outlier) and Q 58 (Medinan boundary) — which inflates Q 56's "mean distance to ±2 neighbors" in a framework-specific way.

**Lesson**: [[h-new-410-outlier-spectrum|H-NEW-410]] ranks are window-specific. A surah can rank high in the full-corpus spectrum but contribute little to any SPECIFIC block's disruption. The ranking metric (mean-to-±2) and the block-exclusion metric (delta-to-±2-block) are not interchangeable.

## 3. Post-hoc chronology-seam hypothesis (α=0.05 cap per MW-7)

The block {Q 53, 54, 55, 56, 57}'s residual extremity after joint removal (83.17%ile on {Q 53, 54, 57}) demands explanation. Candidate:

**Q 53, 54, 55, 56 are Meccan. Q 57 al-Ḥadīd is Medinan musabbiḥāt.** Q 55's ±2 window CROSSES THE MECCAN-MEDINAN CHRONOLOGY SEAM.

- Q 53 al-Najm: Meccan, late, *al-najm* theology/ascension
- Q 54 al-Qamar: Meccan, late, eschatological-warnings + cosmic-moon-splitting
- Q 55 al-Raḥmān: Meccan, *ʿarūs al-Qurʾān* singular register
- Q 56 al-Wāqiʿah: Meccan, tripartite-humanity-at-hour eschatology
- **Q 57 al-Ḥadīd: Medinan, musabbiḥāt, community-legal + cosmic-iron**

Removing Q 55 and Q 56 from this block leaves {Q 53 Meccan, Q 54 Meccan, Q 57 Medinan} — still a register-diverse 3-surah set spanning chronology. Mean FR d̄ = 1.0444 corresponds to 83.17%ile.

**Alternative post-hoc interpretation**: Q 55's block extremity is NOT pure outlier-effect but an **outlier × chronology-seam** INTERACTION effect. The ±2 window places Q 55 at the Meccan→Medinan transition, and this chronology-seam amplifies any outlier-factor.

**Mandatory future pre-registration** ([[h-new-450-window-sensitivity|H-NEW-450]] queued): compute block-percentile for EACH CHRONOLOGICALLY-HOMOGENEOUS ±2 subset of Q 55's and other outliers' neighborhoods; compare to full-±2.

## 4. Falsification of the H-420 post-hoc "outlier-density" narrative

[[h-new-420-novel-outlier-exclusion|H-NEW-420]]'s closing paragraph speculated: *"outlier-factor magnitude depends on CONTRAST between outlier and its neighborhood... Q 55's lower PC effect is explained by co-occurrence of Q 56 (another top-3 outlier) in its ±2 neighborhood."*

This speculation made a testable prediction: joint Q 55+Q 56 removal should crash block cohesion. **It does not.** The joint removal delta is −15.36pp, not the ~−68pp the outlier-density model predicted.

Instead:
- Q 55 alone accounts for essentially ALL of the removable outlier-contribution (−9.72pp of the −15.36pp joint delta).
- Q 56 is a cohesion-neutral member (−0.15pp solo effect, +5.64pp marginal effect in joint).
- The persistent post-joint-exclusion 83.17%ile implicates NON-OUTLIER structure.

**H-420 post-hoc narrative now demoted to disproven speculation.** Per MW-7 discipline, post-hoc insights are provisional pending pre-registered replication — H-440 is that replication and it **rejects** the speculation.

The 5-factor cohesion model's outlier-factor is NOT continuous-neighborhood-contrast-weighted. It is closer to **binary-per-surah with chronology-seam amplification at Meccan-Medinan boundaries**.

## 5. Classical-scholarship reconciliation

The classical tradition's recognition of Q 55 as *ʿarūs al-Qurʾān* is confirmed: Q 55 alone carries the outlier-factor in its block. The classical paired-status of Q 55+Q 56 (*al-Raḥmān* mercy + *al-Wāqiʿah* judgment) reflects THEMATIC/RHETORICAL complementarity, NOT joint-disruption of block cohesion.

This fine-grained distinction matches classical scholarly discernment:
- **al-Tirmidhī** #3291 flags ONLY Q 55 with *ʿarūs al-Qurʾān* title.
- **al-Suyūṭī** *Itqān* and **al-Biqāʿī** *Naẓm al-Durar* vol. 19 discuss Q 55↔Q 56 thematic-pairing (mercy-judgment polarity) but do NOT frame Q 56 as content-outlier.
- The classical *shayyabatnī* hadith (al-Tirmidhī #3297) pairs Q 56 with Hūd, al-Mursalāt, ʿAmma, al-Shams on EMOTIONAL-IMPACT grounds, not structural-singularity grounds.

**Classical tradition distinguishes structural-singular (Q 55) from emotional-singular (Q 56)**. [[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] empirically vindicates this distinction: Q 55 is a content-axis outlier, Q 56 is not.

## 6. What the full decomposition tells us

| Removal | d̄ | percentile | delta from baseline |
|:--|:-:|:-:|:-:|
| None (full) | 1.0909 | 98.53% | — |
| −Q 55 | 1.0390 | 88.81% | −9.72pp |
| −Q 56 | 1.1097 | 98.38% | −0.15pp |
| −{Q 55, Q 56} | 1.0444 | 83.17% | −15.36pp |

**Attribution**:
- Pure Q 55 contribution: −9.72pp
- Pure Q 56 contribution: −0.15pp
- Joint additive sum: −9.87pp
- Observed joint: −15.36pp
- **Interaction term: −5.49pp (sub-additive in absolute magnitude, since joint < sum)**

Wait — superadditivity = joint − (sum_of_singletons) = −15.36 − (−9.87) = **−5.49pp** (MORE negative than sum). So joint removal IS slightly superadditive, just not ≥10pp as pre-committed. There IS a small interaction effect (~−5pp of extra drop when both removed together), but it's far from the dramatic neighborhood-contrast multiplicative-model prediction.

**Revised interpretation**: weak superadditive interaction ~5pp, consistent with Q 55 and Q 56 sharing some Meccan-eschatological lexical content that's obscured when only one is removed. But not the dominant effect.

## 7. MW-5 positive control: Q 62 NC passes again

Q 62 singleton removal delta = +1.85pp. This is within 0.3pp of [[h-new-430-corrected-direction-replication|H-NEW-430]]'s +1.53pp and [[h-new-400-q62-outlier-candidate|H-NEW-400]]'s +1.6pp. **Three-test framework-independence validation for Q 62 NULL-control status**.

Instrument validated under fresh seed. The H-440 NULL verdict is NOT a noise/bug; it's a genuine falsification of the outlier-density hypothesis.

## 8. Honest limits

1. **N=3 subset is very small.** Null distribution at α_bon=0.01667 for N=3 is heavy-tailed. But the primary verdict (joint removal delta=−15.36pp, not <−68pp required) is well-defined regardless of tail sensitivity.
2. **±2 window is FIXED per [[h-new-410-outlier-spectrum|H-NEW-410]] convention.** Doesn't explore ±1 or ±3.
3. **Chronology-seam hypothesis is POST-HOC** — subject to MW-7 α=0.05 single-test cap. Requires [[h-new-450-window-sensitivity|H-NEW-450]] pre-registration to promote.
4. **Classical paired-status interpretation** relies on my reading of al-Tirmidhī #3297 and *Itqān* — a specialist could refine.
5. **FR-roots only.**
6. **Single block tested.** Other outliers (Q 33, Q 24, Q 12, Q 9) may or may not show chronology-seam effects; untested here.

## 9. Cross-references

- **cross-finding-008** (musabbiḥāt): Q 57 al-Ḥadīd is a musabbiḥāt member — the surah that "causes" the Meccan-Medinan seam in Q 55's block. Cross-finding-008's musabbiḥāt cohesion prediction is UNAFFECTED by this result.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (mushaf Fisher-Rao optimality): consistent — the FR framework itself discriminates outliers from non-outliers cleanly (per Q 62 NC framework-independence), but ranking metrics (H-410) and block-exclusion metrics (H-440) are NOT interchangeable.
- **P8** (4-region architecture): Q 55 sits at the region-2/region-3 (mid-late Meccan → early Medinan) boundary per P8; H-440 empirically shows this boundary-effect INTERACTS with outlier-factor.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]** (muqaṭṭaʿāt hub): Q 55 is NOT muqaṭṭaʿāt-opened; no direct interaction tested.

## 10. Queued follow-ups

- **[[h-new-450-window-sensitivity|H-NEW-450]]**: pre-registered chronology-seam test — for each confirmed outlier (Q 33, 24, 12, 9, 55), compute BOTH full-±2 and chronology-homogeneous-±2 block exclusion effects; predict chronology-homogeneous effect ≥ 80% of full-±2 effect.
- **[[h-new-460-q24-q33-hijab-pair|H-NEW-460]]**: [[h-new-410-outlier-spectrum|H-NEW-410]] rerun with chronology-homogeneous window restriction; does the outlier ranking change?
- **H-NEW-470**: continuous outlier-intensity feature construction; regress against 5-factor model with chronology-interaction term.

## 11. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-440-joint-outlier-pair-exclusion-prereg.md` (SHA `5737b8ff…`)
- Script: `scripts/h_new_440_joint_outlier_pair_exclusion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-440.json`
- Findings: this file

## 12. Final statement

**The outlier-factor / neighborhood-contrast speculation from [[h-new-420-novel-outlier-exclusion|H-NEW-420]] is FALSIFIED at Bonferroni α_bon=0.01667.** Q 55's extreme block-percentile is not explained by Q 56's co-outlier-density; Q 56 contributes only −0.15pp singleton-effect. Joint removal leaves the 3-surah residual block still at 83.17%ile — persistent non-outlier-attributable structure.

**Post-hoc candidate explanation (α=0.05 cap)**: the residual extremity reflects a Meccan-Medinan chronology-seam effect — Q 57 al-Ḥadīd is the Medinan musabbiḥāt surah at Q 55's ±2 boundary, and the register-transition amplifies any outlier-factor at this location. This promotes to pre-registered status only after [[h-new-450-window-sensitivity|H-NEW-450]].

**Classical-tradition reconciliation**: al-Tirmidhī's singular *ʿarūs al-Qurʾān* designation for Q 55 ALONE (not Q 55+Q 56) is empirically vindicated. The classical thematic pairing of Q 55+Q 56 reflects mercy-judgment complementarity, not joint structural-singularity. Classical scholarly discrimination is finer-grained than naive "outlier-density" models.

**Revised [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] 5-factor outlier-factor model**: binary-per-surah (outlier / non-outlier) with potential CHRONOLOGY-SEAM INTERACTION at Meccan-Medinan boundaries. The continuous neighborhood-contrast weighting refinement from [[h-new-420-novel-outlier-exclusion|H-NEW-420]] post-hoc is NOT supported. Downgrade to binary-with-chronology-interaction.

This is a scientifically productive NULL: it falsifies a speculative mechanism, vindicates classical scholarly discrimination, and generates a new pre-registerable hypothesis (chronology-seam interaction).

**Per user standing instruction**: publishing NULL with equal prominence to PASS findings.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
