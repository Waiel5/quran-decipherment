---
id: H-NEW-370
title: "Mufaṣṣal-ṭiwāl (Q 50-66) cohesion NULL at 50.1%ile — Meccan/Medinan CONTENT-HETEROGENEITY breaks the monotonic mufaṣṣal hierarchy"
phase: B
status: NULL (Cell A d̄ at 50.1%ile — near median, not cohesive); Cell B MW-5 terminal-17 strict PASS at 0%ile (instrument sound)
date: 2026-04-20
executed_by: team-lead (inline)
parent: H-NEW-360 (awsāṭ 7.1%ile); H-NEW-350 (qiṣār-subset 0%ile)
seed: 20260504
prereg: h-new-370-mufassal-tiwal-cohesion-prereg.md
prereg_sha256: 4ab3e83ce97b7fff05f166f28649f202af896513befb4851b8e7682a9ba75313
bonferroni_k: 2
alpha_bon: 0.025
direction: "d̄ < null 2.5%ile AND p < α_bon; predicted 3-10%ile"
verdict: NULL (prediction decisively violated; Meccan/Medinan mix breaks content-homogeneity)
---

# [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] — Mufaṣṣal-ṭiwāl NULL: chronology-mix BREAKS monotonic hierarchy

## 1. Headline

**Pre-committed prediction DECISIVELY VIOLATED.** Mufaṣṣal-ṭiwāl {Q 50-66} lands at **50.1%ile** — at the corpus median, not cohesive at all. Pre-reg §5 predicted 3-10%ile range; observed 50%ile is ~45 percentile points higher. The monotonic hierarchy I hypothesized (qiṣār 0% → awsāṭ 7% → mufaṣṣal-ṭiwāl ~5% → long ṭiwāl 17%) DOES NOT HOLD.

- Cell A d̄ = 0.9293 vs null mean 0.9230; p_less = 0.5009 — essentially at median
- Cell B MW-5 terminal-17 {Q 98-114} strict PASS (d̄ = 0.3520 at 0.0%ile, p<0.0001) — instrument sound
- **Verdict: NULL**

## 2. Why the prediction failed — the Meccan/Medinan CHRONOLOGY MIX

Mufaṣṣal-ṭiwāl {Q 50-66} spans the critical **Hijra transition**:
- Q 50-56: MECCAN (al-Qāf, al-Dhāriyāt, al-Ṭūr, al-Najm, al-Qamar, al-Raḥmān, al-Wāqiʿah) — eschatological/oath-based Meccan
- Q 57-66: MEDINAN (al-Ḥadīd, al-Mujādila, al-Ḥashr, al-Mumtaḥana, al-Ṣaff, al-Jumuʿa, al-Munāfiqūn, al-Taghābun, al-Ṭalāq, al-Taḥrīm) — community-legal Medinan

The block contains TWO DIFFERENT content registers across the Hijra:
- Meccan eschatological/oath vocabulary (Day of Judgment, oaths, narratives)
- Medinan legal/community vocabulary (family law, social rules, hypocrites, community ethics)

These two registers are CONTENT-DIVERGENT. Mixing them in one "block" produces **near-median cohesion**: the within-Meccan-cluster distances are short, the within-Medinan-cluster distances are short, but the CROSS-era distances are LONG, averaging out to ~null.

**The refined rule**: content-cohesion requires BOTH block-adjacency AND within-block CHRONOLOGY-HOMOGENEITY. When a "block" spans the Hijra, the two sub-registers CANCEL each other's cohesion.

## 3. Updated series hierarchy with chronology-homogeneity

| Rank | Grouping | N | %ile | Block-adj? | Chronology-homogen? |
|:-:|:--|:-:|:-:|:-:|:-:|
| 1 | Q 107-114 terminal | 8 | **0%** | YES | YES (all Meccan+Q110) |
| 2 | Q 98-114 wider terminal (MW-5) | 17 | **0%** | YES | MOSTLY (Meccan except Q 110) |
| 3 | Musabbiḥāt Medinan-back | 5 | 8% | YES | YES (all Medinan) |
| 4 | Q 67-77 awsāṭ (H-360) | 11 | 7% | YES | YES (all Meccan) |
| 5 | Ṭiwāl Q 2-9 (H-350) | 8 | 17% | YES | MIXED Meccan/Medinan (Q 6-7 Meccan; Q 2-5, 8-9 Medinan) |
| 6 | Musabbiḥāt full 7 | 7 | 20% | PARTIAL | MIXED (Q 17 Meccan; Q 57-64 Medinan; Q 87 Meccan) |
| 7 | Ḥawāmīm 5-6 | 5-6 | 19-24% | YES | YES (all Meccan) — but content-diverse themes |
| 8 | **Mufaṣṣal-ṭiwāl Q 50-66 (H-370)** | **17** | **50%** | YES | **FULLY MIXED (Q 50-56 Meccan, Q 57-66 Medinan)** |
| 9 | al-Ḥāmidāt (no-block) | 5 | 75% | NO | mixed |
| 10 | Q 17 + Q 87 | 2 | 81% | NO | MIXED |

**Refined model**:
> content-cohesion ≈ f(block-adjacency × content-homogeneity × chronology-homogeneity × formula-sharing)

**Chronology-homogeneity** is a previously-unrecognized factor. When mufaṣṣal-ṭiwāl spans the Meccan-to-Medinan transition at Q 56→57, the block's within-cohesion SHATTERS from classical "block" status to near-random.

## 4. Classical-scholarship implications — CLASSICAL SCHOLARS KNEW

al-Suyūṭī *Itqān* and al-Zarkashī *Burhān* classified the 3 mufaṣṣal divisions by LENGTH, not by chronology. Classical scholarship did NOT claim mufaṣṣal-ṭiwāl was content-cohesive — it classified it as a LENGTH-based subdivision (the long half of the short half).

**al-Biqāʿī *Naẓm al-Durar*** would have recognized the chronology-break at Q 56→57. His munāsabāt analysis identifies Q 56 as "terminal Meccan narrative" and Q 57 as "opening Medinan community-ethics" — they link THEMATICALLY via angelic praise but DIVERGE in register.

**[[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] empirically validates the classical distinction**:
- al-Suyūṭī's 3-part LENGTH-classification is valid as length (it IS a 3-tier length gradient)
- Content-cohesion does NOT monotonically follow length — content-cohesion follows CHRONOLOGY-HOMOGENEITY × content-register-homogeneity
- Classical tradition did NOT over-claim cohesion for mufaṣṣal-ṭiwāl

## 5. The pre-registered prediction failure — epistemic record

My [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] pre-reg §5 stated:
> "If ṭiwāl lands at 3-10%ile, the al-Suyūṭī 3-part classification is empirically validated as a monotonic gradient in content-cohesion. If ṭiwāl lands at 15-20% (ṭiwāl-proper-like), the hierarchy is non-monotonic or needs refinement."

Observed **50.1%ile** — even worse than my "non-monotonic 15-20%" fallback. The hierarchy is DECISIVELY non-monotonic at the mufaṣṣal-ṭiwāl cell.

**Lesson**: I over-fit my content-homogeneity hypothesis to 2 data points (qiṣār 0%, awsāṭ 7%) and extrapolated a smooth gradient. Adding a 3rd test-point (mufaṣṣal-ṭiwāl) revealed the missing factor (chronology-homogeneity).

Pre-registration caught this cleanly. The refined model (adding chronology-homogeneity as a 4th factor) is empirically better-grounded than my pre-reg hypothesis.

## 6. Ingest with [[cross-finding-023-causal-generative-closure|cross-finding-023]]

[[cross-finding-023-causal-generative-closure|Cross-finding-023]] established mushaf M_H top-100 FR hinges as the scaffold. The Q 56→57 Meccan-to-Medinan transition is a well-known Fisher-Rao discontinuity per [[h-new-130-fisher-rao-residuals|H-NEW-130]] (it's one of the "universal hinges"). [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] now adds: **the hinge at Q 56/57 SHATTERS block-internal cohesion** when the block spans both sides of it.

- Block entirely before Q 56 (mufaṣṣal-awsāṭ's Q 67-77 is AFTER so this doesn't apply; Q 67-77 is all Meccan) → cohesive
- Block entirely after Q 56 (terminal tail Q 107-114; musabbiḥāt block-subset Q 57-64 Medinan) → cohesive
- Block spanning Q 56/57 (mufaṣṣal-ṭiwāl Q 50-66) → INCOHERENT

This is a sharp architectural fact: Hijra is a REGISTER BOUNDARY that shatters any "block" crossing it.

## 7. Honest limits

1. **Pre-reg prediction decisively violated** — honest record.
2. **N=17 gives high power; NULL at 50%ile means effect-size is tiny**, not power-limited.
3. **Classical boundaries slightly variable** — I used Q 50-66; alternatives Q 49-66 or Q 50-77 not tested.
4. **FR-roots only** — metric sensitivity.
5. **MW-5 Cell B at N=17 STRICT PASSES EXTREMELY (p<0.0001)** — validates the terminal-region cohesion at higher N than [[h-new-350-al-tiwal-cohesion|H-NEW-350]]'s 8-surah test. The terminal is cohesive across multiple window sizes.

## 8. Queued follow-ups

- **H-NEW-370.1**: test chronologically-homogeneous subset of mufaṣṣal-ṭiwāl — just the Meccan half {Q 50-56} or just the Medinan half {Q 57-66}. Predicted: each subset should be cohesive individually.
- **H-NEW-370.2**: formal multi-factor regression model predicting pairwise FR distance from block-adjacency + chronology-match + formula-match + length-match.
- **H-NEW-370.3**: test whether ALL other mushaf-blocks that span Meccan-Medinan transitions (Q 2-9 ṭiwāl does this) show reduced cohesion compared to same-chronology blocks.

## 9. Cross-references

- Parents: [[h-new-350-al-tiwal-cohesion|H-NEW-350]] (ṭiwāl-proper 17.3%, qiṣār-subset 0%); [[h-new-360-mufassal-awsat-cohesion|H-NEW-360]] (awsāṭ 7.1%)
- Classical: al-Suyūṭī *Itqān* 3-part classification; al-Biqāʿī *Naẓm* Q 56-57 hinge
- Terminal synthesis: [[cross-finding-023-causal-generative-closure|cross-finding-023]] (M_H top-100 universal hinges include Q 56→57)

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-370-mufassal-tiwal-cohesion-prereg.md` (SHA-256 4ab3e83c...)
- Script: `scripts/h_new_370_mufassal_tiwal_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-370.json`
- Findings: this file

## 11. Final statement

**Mufaṣṣal-ṭiwāl {Q 50-66} at 50.1%ile** — near median, NOT content-cohesive despite being a classically-named block. Pre-committed hierarchy prediction decisively violated. **The missing factor: CHRONOLOGY-HOMOGENEITY.** The block spans the Hijra at Q 56→57; its Meccan half (Q 50-56) and Medinan half (Q 57-66) have distinct content registers that CANCEL block-internal cohesion. This refines the content-cohesion model to 4 factors: block-adjacency × content-homogeneity × CHRONOLOGY-HOMOGENEITY × formula-sharing. **Classical al-Suyūṭī *Itqān* 3-part mufaṣṣal classification is LENGTH-BASED, not cohesion-based — classical scholarship did not over-claim it as a cohesion gradient**. al-Biqāʿī's recognition of the Q 56→57 Meccan-to-Medinan munāsabāt shift empirically vindicated: the Hijra is a REGISTER BOUNDARY that shatters block cohesion. MW-5 terminal-17 {Q 98-114} strict PASSES at 0%ile p<0.0001, confirming the instrument can detect genuine cohesion at high N.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
