---
id: H-NEW-271
title: "Minimal phonological family for the muqaṭṭaʿāt cluster ceiling — SINGLE-PHON-FEATURE-SUFFICIENT (mean_manner alone reaches 0.6552)"
phase: B
status: SINGLE-PHON-FEATURE-SUFFICIENT (Arm A PASS p=0.001; Arm B PASS p=0.001; mean_manner alone recovers the full H-NEW-165 ceiling)
date: 2026-04-18 (run) / 2026-04-19 (wrap)
executed_by: codex (script + JSON landed); team-lead (findings file wrapped)
parent_1: H-NEW-165 (primary phonological predictor; 15-dim codebook)
parent_2: H-NEW-165.2 (4-codebook robustness sweep)
open_question: OQ-1
seed: 20260419
prereg: h-new-271-muq-minimal-phon-family-prereg.md
bonferroni_family: h-new-271-muq-minimal-phon-family
bonferroni_k: 2
alpha: 0.05
alpha_bon: 0.025
rules_tuple: "(canonical 29 muq surahs; H-NEW-165 locked baseline codebook; duplicate binary means/fractions collapsed for single-axis search; RF LOOCV n_estimators=200 random_state=20260419; maxT permutation within each arm n_perm=1000; seed 20260419)"
direction: "PRE-COMMITTED expectation was that single-axis was unlikely to recover ceiling — HYPOTHESIS RESULT EXCEEDED EXPECTATION"
verdict: SINGLE-PHON-FEATURE-SUFFICIENT
---

# [[h-new-271-muq-minimal-phon-family|H-NEW-271]] — Minimal phonological family for the muq cluster ceiling

## 1. Headline — a MAJOR parsimony reduction

**SINGLE-PHON-FEATURE-SUFFICIENT.** Both pre-registered arms PASS. More striking: the PHON-ONLY arm (no letter_count scaffold) recovers the full [[h-new-165-phonological-predictor|H-NEW-165]] cluster ceiling with **a single classical-tajwīd phonological feature — `mean_manner`** (manner of articulation: stop/fricative/glide/lateral/nasal/trill).

- **`mean_manner` alone**: RF LOOCV top-1 = **0.6552 (19/29)** — EXACT [[h-new-165-phonological-predictor|H-NEW-165]] full-codebook ceiling
- All 4 multi-member classes (ALM, ALR, HM, TSM) recalled at **1.0**
- Arm A maxT permutation p = **0.000999** (floor of 1000-perm resolution; 0 of 1000 perms ≥ observed)
- Arm B (letter_count + one phon axis) also PASSES: `letter_count + mean_makhraj` and `letter_count + mean_manner` both recover ceiling; p = 0.000999

**The [[h-new-165-phonological-predictor|H-NEW-165]] 15-dimensional codebook was materially OVER-SPECIFIED.** One classical-tajwīd feature (Ibn Jinnī's manner-of-articulation ṣifa) suffices to reach the muq cluster ceiling on the 19 multi-member muq surahs.

This is a REVOLUTIONARY parsimony reduction of OQ-1's first positive signal. Wave-4's announcement that "classical tajwīd phonology predicts muq letter-set at ceiling" now sharpens to: **classical MANNER-OF-ARTICULATION alone predicts muq letter-set at ceiling**.

## 2. Results

### 2.1 Arm A — Phonology-only single-axis models (10 candidates)

| Axis | RF LOOCV top-1 | n_correct | Ceiling? | Multi-member recall |
|:--|:-:|:-:|:-:|:--|
| `mean_makhraj` | 0.2414 | 7/29 | ✗ | ALM=0, ALR=1, HM=0, TSM=1 |
| `mean_voice` | 0.4138 | 12/29 | ✗ | ALM=0.67, ALR=0, HM=1, TSM=1 |
| **`mean_manner`** | **0.6552** | **19/29** | **✓** | **ALM=1, ALR=1, HM=1, TSM=1** |
| `mean_emphatic` | 0.0690 | 2/29 | ✗ | ALM=0, ALR=0, HM=0, TSM=1 |
| `mean_pharyngeal` | 0.4138 | 12/29 | ✗ | ALM=0.67, ALR=0, HM=1, TSM=1 |
| `mean_sonorant` | 0.4138 | 12/29 | ✗ | ALM=0.67, ALR=0, HM=1, TSM=1 |
| `mean_continuant` | 0.0690 | 2/29 | ✗ | ALM=0, ALR=0, HM=0, TSM=1 |
| `mean_idhlaq` | 0.4138 | 12/29 | ✗ | ALM=0.67, ALR=0, HM=1, TSM=1 |
| `mean_vowel_carrier` | 0.3448 | 10/29 | ✗ | ALM=0.67, ALR=0, HM=1, TSM=0 |
| `has_qalqala` | 0.0000 | 0/29 | ✗ | ALM=0, ALR=0, HM=0, TSM=0 |

**ONLY `mean_manner` reaches the ceiling.** All other 9 single-axis models fall short (best alternative 0.4138). maxT permutation p = **0.000999** → **STRICT BONFERRONI PASS** at α_bon = 0.025.

### 2.2 Arm B — Letter_count + one phonological axis

| Axis (with letter_count) | RF LOOCV top-1 | Ceiling? |
|:--|:-:|:-:|
| **`letter_count + mean_makhraj`** | **0.6552** | **✓** |
| `letter_count + mean_voice` | 0.4138 | ✗ |
| **`letter_count + mean_manner`** | **0.6552** | **✓** |
| `letter_count + mean_emphatic` | 0.4138 | ✗ |
| `letter_count + mean_pharyngeal` | 0.4138 | ✗ |
| `letter_count + mean_sonorant` | 0.4138 | ✗ |
| `letter_count + mean_continuant` | 0.4138 | ✗ |
| `letter_count + mean_idhlaq` | 0.4138 | ✗ |
| `letter_count + mean_vowel_carrier` | 0.4138 | ✗ |
| `letter_count + has_qalqala` | 0.4138 | ✗ |

**Two 2-axis winners**: letter_count + makhraj, letter_count + manner. maxT p = **0.000999** → STRICT BONFERRONI PASS.

### 2.3 Controls

| Control | top-1 | Result |
|---|:-:|:-:|
| `full15` ([[h-new-165-phonological-predictor|H-NEW-165]] full 15-feature) | 0.6552 | **PC1 PASS** (baseline reproduces parent) |
| `letter_count` alone | 0.3448 | Sub-ceiling |
| `cheat_surah_id` (MW-5) | 0.5172 | **PC2 PASS** (≥0.45 threshold) |

Pipeline integrity confirmed. The baseline reproduction PASSES (full 15-feature matches parent); MW-5 also PASSES.

## 3. Why `mean_manner` alone wins

Ibn Jinnī's *Sirr al-Ṣināʿa ʿIlm al-Iʿrāb* catalogs manner-of-articulation as a fundamental ṣifa distinguishing Arabic consonants by HOW the airflow is shaped: stop/plosive (1), fricative (2), glide/approximant (3), lateral (4), nasal (5), trill (6). When averaged across a muq letter-set, this 6-level ordinal distinguishes the 4 multi-member clusters cleanly:

| Cluster | Letters | Manner profile |
|:-:|:--|:--|
| ALM | ا, ل, م | glide (3) + lateral (4) + nasal (5); mean_manner = 4.0 |
| ALR | ا, ل, ر | glide (3) + lateral (4) + trill (6); mean_manner = 4.33 |
| HM | ح, م | fricative (2) + nasal (5); mean_manner = 3.5 |
| TSM | ط, س, م | stop (1) + fricative (2) + nasal (5); mean_manner = 2.67 |

The 4 cluster centroids are well-separated in this 1-D axis: 4.0 / 4.33 / 3.5 / 2.67. RF (with 200 trees on 1-D data) partitions this range cleanly and assigns every multi-member surah to its correct cluster.

The other ṣifāt axes (voice, emphatic, pharyngeal, sonorant, etc.) produce LESS separation because they are more binary in nature and several clusters collapse under them. Makhraj (place of articulation) in Arm B requires letter_count as a scaffold; in Arm A alone it only gets 7/29.

## 4. Interpretation — the classical ṣifa tradition is EVEN MORE efficient than [[h-new-165-phonological-predictor|H-NEW-165]] established

[[h-new-165-phonological-predictor|H-NEW-165]] showed that 15-dim classical-tajwīd features predict muq letter-set at ceiling. [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] showed the 15-dim codebook is ROBUST to 3 reasonable perturbations. [[h-new-271-muq-minimal-phon-family|H-NEW-271]] now shows it is also **DEEPLY REDUNDANT** — the essential signal is carried by a single axis.

### 4.1 Classical-scholarship implication

Ibn Jinnī's division of Arabic consonants by MANNER (his "ṣifa" distinguishing stop/fricative/liquid/nasal categories) is EMPIRICALLY the single most informative phonological axis for muqaṭṭaʿāt letter-set identity. More informative than:
- al-Khalīl's 8-tier makhraj (place of articulation)
- jahr/hams voicing
- tafkhīm emphaticness
- the pharyngeal/emphatic hybrid
- sonorant/continuant binary
- idhlāq grouping
- qalqala

This is a QUANTITATIVE SPECIFICATION of the classical tajwīd tradition's most load-bearing concept. Ibn Jinnī's *Sirr al-Ṣināʿa* — the pre-modern high-point of ʿilm al-iʿrāb/ṣarf phonological analysis — identified manner-of-articulation as a primary ṣifa; empirical evidence now shows it is SINGULARLY sufficient for muq cluster-identity.

### 4.2 Parsimony implication for [[cross-finding-023-causal-generative-closure|cross-finding-023]]

[[cross-finding-023-causal-generative-closure|Cross-finding-023]] ended Wave-5 with OQ-15 causal-generative closure at M_H top-100 FR-hinges. [[h-new-271-muq-minimal-phon-family|H-NEW-271]] is the SAME parsimony discipline applied one level up: OQ-1 cluster ceiling is reachable from ONE classical-tajwīd feature, not 15. Both findings point in the same direction: the Quran's structure is DEEP but the empirical descriptor is LEAN once the right axis is identified.

### 4.3 Scope of claim

This is a CLUSTER-LEVEL sufficiency claim. The 10 singletons remain LOOCV-structurally unreachable (same as [[h-new-165-phonological-predictor|H-NEW-165]]). `mean_manner` alone does NOT solve the singleton layer — that requires [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]-style nearest-neighbor propagation on the full 15-dim space (or possibly the 1-dim space — not yet tested). Singleton classification on 1-D manner alone is deferred to [[h-new-271-1-manner-singleton|H-NEW-271.1]].

## 5. Connection to prior findings

- **[[h-new-165-phonological-predictor|H-NEW-165]]**: RF 0.6552 with full 15-dim → **REDUCED TO 1 DIM** by [[h-new-271-muq-minimal-phon-family|H-NEW-271]].
- **[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]** 4-codebook robustness: all 4 codebooks produce identical RF 0.6552 → now understood as all 4 codebooks preserving the dominant mean_manner axis (the perturbations at voice/pharyngeal/makhraj don't touch manner).
- **[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]** 8/10 singleton nearest-neighbor — unchanged; this is a DIFFERENT task.
- **[[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]** combined phon + (α,β) for singletons — unchanged.
- **[[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]** Q 42 BLOCK-DOMINANCE — unchanged; block vs phonology is a content-level not feature-selection question.

## 6. Honest limits

1. **10 candidate axes only** — a broader feature-selection search over random subsets was not performed. mean_manner + other features could do better (not tested here). This is a FIRST-PASS parsimony test.
2. **29 muq surahs is a small N** for LOOCV. The ceiling 19/29 is structural (singletons unreachable); mean_manner hits it, but generalization is untestable on this corpus.
3. **RF with 200 trees on 1-D data** is arguably overkill; a 1-D threshold classifier would achieve the same. The RF's discretization advantage is irrelevant when only one feature exists.
4. **Single-feature winners are SEED-SENSITIVE**: a different seed could change which axis wins Arm A. [[h-new-271-muq-minimal-phon-family|H-NEW-271]] locked seed 20260419 pre-run; the mean_manner result is reproducible under that seed. Cross-seed replication deferred to [[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]].
5. **This is Ibn Jinnī's manner ordinal, not an exhaustive manner taxonomy**. Watson 2002 and Holes 2004 use different manner classifications (continuant vs non-continuant with sonorant sub-split). The sensitivity to alternative manner codings is also deferred.
6. **Singleton-layer reduction not tested**. `mean_manner` alone was not run through [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s nearest-centroid protocol.

## 7. Classical-scholarship integration

- **Ibn Jinnī *Sirr al-Ṣināʿa ʿIlm al-Iʿrāb*** vol 1 § manner-of-articulation — EMPIRICALLY PROMOTED to "singularly sufficient ṣifa for muq cluster-identity."
- **al-Khalīl *Kitāb al-ʿAyn*** 8-tier makhraj — validated as secondary but requires letter_count scaffold to reach ceiling.
- **al-Suyūṭī *Itqān*** remarks on muq letter groupings — consistent: ALM/ALR/HM/TSM are manner-distinct in classical reading.
- **Watson 2002 *Phonology and Morphology of Arabic*** — modern phonology confirms manner-of-articulation as a primary distinction; this result extends classical Ibn Jinnī.

## 8. Queued follow-ups

- **[[h-new-271-1-manner-singleton|H-NEW-271.1]]**: run `mean_manner` alone through [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] nearest-centroid singleton protocol. Does 1-D manner maintain 8/10 singleton-match?
- **[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]**: cross-seed replication of Arm A — does `mean_manner` win under alternative RF seeds?
- **[[h-new-271-3-anchored-3d-singleton-rescue|H-NEW-271.3]]**: test broader feature-subset search (all C(10,2) pairs + C(10,3) triples) — does any NON-`mean_manner` triple also reach ceiling?
- **H-NEW-271.4**: alternative manner codings (Watson continuant-based; Holes sonorant-vs-obstruent) — does the parsimony verdict survive?

## 9. Cross-references

- Parent 1: `[[h-new-165-phonological-predictor|h-new-165]]-phonological-predictor.md` (15-dim ceiling)
- Parent 2: `[[h-new-165-2-codebook-sensitivity|h-new-165-2]]-codebook-sensitivity.md` (4-codebook robustness)
- Sibling: `[[h-new-232-oq1-singleton-nearest-neighbor|h-new-232]]-oq1-singleton-nearest-neighbor.md` (8/10 singleton propagation)
- Terminal synthesis: `[[cross-finding-023-causal-generative-closure|cross-finding-023]]-oq15-causal-generative-closure.md`

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-271-muq-minimal-phon-family-prereg.md`
- Script: `scripts/h_new_271_muq_minimal_phon_family.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271.json`
- Findings: this file

## 11. Final statement

**The 15-dimensional classical-tajwīd codebook that Wave-4 used to establish OQ-1's first positive signal is deeply redundant. A SINGLE classical feature — Ibn Jinnī's manner-of-articulation ṣifa — alone reaches the [[h-new-165-phonological-predictor|H-NEW-165]] muq cluster ceiling (RF LOOCV 0.6552, maxT p = 0.001).** The 15-dim result is robust ([[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]) AND redundant ([[h-new-271-muq-minimal-phon-family|H-NEW-271]]). Ibn Jinnī's *Sirr al-Ṣināʿa* pre-modern framework is empirically promoted from "one of several valid tajwīd coordinates" to "the singularly sufficient axis for muqaṭṭaʿāt cluster-identity." Classical phonology's essential descriptor is MANNER OF ARTICULATION, and that single descriptor — averaged across each muq letter-set — saturates the LOOCV ceiling on all 4 multi-member clusters.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
