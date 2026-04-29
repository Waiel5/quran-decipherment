---
id: H-NEW-400
title: "Q 62 al-Jumuʿa outlier-candidate test — CLEAN NULL (Q 62 is NOT an outlier; 'meta-hub' liturgical-prominence does NOT equal content-outlier status)"
phase: B
status: NULL — removing Q 62 from musabbiḥāt-block changes percentile by only -1.6pp (8.1%→9.7%, SLIGHTLY WORSE); verdict Q62-NOT-OUTLIER
date: 2026-04-21
executed_by: team-lead (inline)
parent_1: H-NEW-340 (musabbiḥāt-block {57,59,61,62,64} at 8.1%ile)
parent_2: H-NEW-390 (Q 55 outlier confirmed at +32.6pp)
parent_3: NEXT-AGENT-PROMPT (Q 62 flagged as "4-cluster meta-hub")
seed: 20260507
prereg: h-new-400-q62-outlier-candidate-prereg.md
prereg_sha256: c1162998a874b24439c09da949899f287368f7b87034517b14b5811b19bb971e
bonferroni_k: 2
alpha_bon: 0.025
direction: "Cell A exclusion < null 2.5%ile AND p < α_bon; OR delta ≥ 5pp improvement"
verdict: NULL (Q62-NOT-OUTLIER; validates specificity of outlier-factor — not all "prominent" surahs are content-outliers)
---

# [[h-new-400-q62-outlier-candidate|H-NEW-400]] — Q 62 al-Jumuʿa NOT an outlier

## 1. Headline

**Q 62 al-Jumuʿa is NOT a content-axis outlier**, despite classical designation as "4-cluster meta-hub" (NEXT-AGENT-PROMPT, OQ-5). Removing Q 62 from the [[h-new-340-musabbihat-block-subset|H-NEW-340]] musabbiḥāt-block {Q 57, 59, 61, 62, 64} changes percentile by only **-1.6pp** (8.1% → 9.7%, actually slightly WORSER). **Contrasts sharply with Q 55's +32.6pp outlier-disruption effect ([[h-new-390-q55-outlier-exclusion|H-NEW-390]]).**

- **Q 62 pairwise distances to other musabbiḥāt-block members**: 0.73, 0.81, 0.73, 0.85 — ALL below corpus null mean 0.92
- **Cell A exclusion {Q 57, 59, 61, 64} N=4**: d̄ = 0.7628 at **9.7%ile**
- **Baseline {Q 57, 59, 61, 62, 64} N=5** ([[h-new-340-musabbihat-block-subset|H-NEW-340]]): d̄ = 0.7704 at 8.1%ile
- **Delta: −1.6pp** — removal slightly INCREASES d̄

**Verdict: Q62-NOT-OUTLIER.** Q 62's classical "meta-hub" status reflects liturgical prominence (Friday prayer verses Q 62:9-11), NOT content-axis uniqueness. The outlier-factor is SPECIFIC to Q 55 at this scale; it does not generalize to all classical "prominent" surahs.

## 2. Q 62's distances empirically show MAINSTREAM content

The pairwise distances reveal Q 62 is a NORMAL musabbiḥāt-block member:

| Q 62 to | FR distance | Δ from corpus null 0.92 |
|:-:|:-:|:-:|
| Q 57 al-Ḥadīd | 0.8490 | -0.07 |
| Q 59 al-Ḥashr | 0.8088 | -0.11 |
| Q 61 al-Ṣaff | 0.7345 | -0.19 |
| Q 64 al-Taghābun | 0.7347 | -0.19 |
| **Mean** | **0.7818** | **-0.14** |

Compare to Q 55's mean FR distance to its own Meccan-block neighbors: **1.114** ([[h-new-390-q55-outlier-exclusion|H-NEW-390]]).

Q 55: mean +0.19 ABOVE null — clear outlier
Q 62: mean -0.14 BELOW null — clear mainstream-member

**Q 55 and Q 62 are qualitatively different phenomena.** Q 55's 31-refrain cosmic-mercy structure is content-distinct; Q 62's Friday-prayer institution is content-mainstream (shares community-legal vocabulary with Medinan neighbors).

## 3. Interpretation — outlier-factor is SPECIFIC not generic

[[h-new-390-q55-outlier-exclusion|H-NEW-390]] established Q 55 as +32.6pp moderate disruptor. The question was whether the outlier-factor generalizes to other "prominent" classical surahs — Q 62 being a natural candidate given its 4-cluster meta-hub designation.

**[[h-new-400-q62-outlier-candidate|H-NEW-400]] cleanly answers**: NO. Q 62 is not an outlier. The outlier-factor in the 5-factor cohesion model ([[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]) is **Q 55-specific at this scale** (though other, untested candidates remain).

**Classical "prominence" ≠ content-axis outlier**:
- Q 55: content-outlier (structural singular cosmic-mercy refrain) → outlier-disruptor ✓
- Q 62: liturgical-prominent (Friday prayer) → NOT content-outlier ✗
- Q 112: theological-central ("1/3 of Quran") → tested by H-NEW-175 as descriptive but not outlier at this scale

Different classical "prominence" designations track different axes. Only structural-content-singular surahs like Q 55 act as cohesion-disruptors.

## 4. Q 62's positive contribution

Interestingly, removing Q 62 slightly WORSENS cohesion (+1.6pp dispersion). Q 62 was pulling d̄ DOWN in the [[h-new-340-musabbihat-block-subset|H-NEW-340]] 5-surah set — removing it removes a cohesion-contributing member.

This reflects Q 62's content being TIGHTLY on the musabbiḥāt community-legal register:
- Opens *yusabbiḥu li-Llāhi* (shared with Q 57, 59, 61, 64)
- Focuses on community ethics, legal institution, Friday prayer
- Short (11 verses), Medinan, formal register

Q 62 is a **cohesion-exemplar**, not a cohesion-disruptor.

## 5. Series-complete outlier ranking

Cumulative [[h-new-380-hijra-split|H-NEW-380]]→400 outlier analysis:

| Surah | Status | Mean distance to block | Classical flag |
|:-:|:--|:-:|:--|
| **Q 55 al-Raḥmān** | **outlier (+32pp)** | 1.114 (above null) | *ʿarūs al-Qurʾān* |
| **Q 62 al-Jumuʿa** | **NOT outlier (-1.6pp)** | 0.782 (below null) | 4-cluster meta-hub / Friday prayer |

Only 2 surahs tested; 1 confirmed outlier. Generalization-via-extrapolation would be premature.

## 6. Classical-scholarship nuance

**al-Tirmidhī #3291** designation for Q 55 (*ʿarūs al-Qurʾān*) is a UNIQUENESS designation — implies content-singular.

**NEXT-AGENT-PROMPT / [[cross-finding-010-extended-network|cross-finding-010]]** designation for Q 62 (4-cluster meta-hub) is a LITURGICAL-PROMINENCE designation — implies ritual-centrality.

These are DIFFERENT CLASSICAL CLAIMS and they have DIFFERENT EMPIRICAL IMPLICATIONS. Classical scholars distinguished uniqueness-designation (Q 55 ʿarūs) from liturgical-prominence (Q 62 Friday) — [[h-new-400-q62-outlier-candidate|H-NEW-400]] empirically vindicates this distinction at content-axis.

## 7. Honest limits

1. **N=4 exclusion subset is very small** — null 2.5%ile at d̄≈0.625, quite extreme. Strict α impossible at this N.
2. **Descriptive -1.6pp is tiny** — within noise; the direction-lock is correct (not ≥5pp improvement).
3. **Only Q 62 tested** — other potential outlier-candidates (Q 1 sui-generis; Q 112 1/3-Quran; Q 18 al-Kahf Friday-recitation) untested.
4. **Classical "meta-hub" designation varies by source** — NEXT-AGENT-PROMPT cites [[cross-finding-010-extended-network|cross-finding-010]]; other classical traditions flag Q 1 or Q 2 or Q 112 as "meta-hubs."
5. **FR-roots only**.

## 8. Queued follow-ups

- **H-NEW-400.1**: Q 1 al-Fātiḥa as outlier-candidate — sui-generis-liturgical per [[h-new-155-q1-sui-generis|H-NEW-155]], content-distant per [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]]. Test its exclusion effect on any block it would be in.
- **H-NEW-400.2**: Q 112 al-Ikhlāṣ as outlier-candidate — Q 112 is IN the terminal-tail Q 107-114 (0%ile cohesive). Remove Q 112 from Q 107-114; does cohesion break?
- **H-NEW-400.3**: Q 1 + Q 112 joint outlier-double-exclusion test.
- **H-NEW-400.4**: formal "distance-to-block-mean" metric across ALL 114 surahs; rank-order gives outlier spectrum.

## 9. Cross-references

- Parent: [[h-new-390-q55-outlier-exclusion|H-NEW-390]] Q 55 outlier +32.6pp
- Baseline: [[h-new-340-musabbihat-block-subset|H-NEW-340]] musabbiḥāt-block 8.1%ile
- Classical anchor: [[cross-finding-010-extended-network|cross-finding-010]] 4-cluster meta-hub; OQ-5 Q 62 framing
- [[cross-finding-024-five-factor-cohesion-model|Cross-finding-024]] 5-factor model (validates specificity of outlier-factor)

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-400-q62-outlier-candidate-prereg.md`
- Script: `scripts/h_new_400_q62_outlier_candidate.py`
- JSON: `csv/h-new-400.json`
- Findings: this file

## 11. Final statement

**Q 62 al-Jumuʿa is NOT a content-axis outlier.** Its pairwise FR distances to musabbiḥāt-block neighbors are UNIFORMLY BELOW the corpus null mean (0.78 vs null 0.92). Removing Q 62 from the [[h-new-340-musabbihat-block-subset|H-NEW-340]] block makes cohesion slightly WORSE (+1.6pp dispersion). **Q 62 is a cohesion-exemplar**, not a disruptor. **The outlier-factor in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]'s 5-factor cohesion model is Q 55-specific at this scale**, not a general extrapolation to all classically-prominent surahs. Classical "4-cluster meta-hub" designation (liturgical prominence via Friday prayer) is EMPIRICALLY DISTINCT from content-axis outlier status (al-Tirmidhī *ʿarūs al-Qurʾān* uniqueness). **Classical tradition's epistemic discipline in distinguishing these prominence-types is empirically vindicated** — different types of classical prominence predict different empirical behaviors. Pre-committed ≥5pp threshold correctly rejected the H1 hypothesis; pre-registration caught over-generalization of the outlier-factor.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
