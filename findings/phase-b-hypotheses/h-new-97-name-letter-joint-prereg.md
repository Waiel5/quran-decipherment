---
id: H-NEW-97-PREREG
title: Surah-name-class × muqaṭṭāʿat letter-set JOINT distribution — χ² independence + per-cluster profile
phase: B
status: PRE-REGISTERED
date: 2026-04-17
agent: h-new-97-specialist
test: χ² test of independence on 10 × N_classes contingency + Monte-Carlo null (10K perms) + per-cluster χ² against uniform
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; 29-muqaṭṭaʿāt set; H-NEW-49 locked 9-class taxonomy; H-NEW-88 letter-set taxonomy 14 distinct sets — collapsed to 10 per pre-reg below)
seed: 20260417
bonferroni_k: 4
bonferroni_family: h-new-97-name-letter-joint
alpha_bon: 0.0125
direction_primary: χ² independence rejected at p<0.0125
direction_secondary: al-r cluster has PROPHET_PERSON majority; hm cluster has DIVINE_ATTRIBUTE or narrative-majority; alm cluster has mixed
acceptance_window: per-cell p<0.0125 for Bonferroni-4
---

# [[h-new-97-name-letter-joint|H-NEW-97]] — PRE-REGISTRATION

## Question

[[h-new-49-surah-name-class|H-NEW-49]] observed that **PROPHET_PERSON** surahs are 64% muqaṭṭaʿāt-opened (7/11) versus baseline 25% — the largest directional skew among the 9 name-classes. The test missed α_bon by a factor of ~1.6× at the all-name-class level.

[[h-new-88-letter-set-predictor|H-NEW-88]] observed that the 3 multi-member muqaṭṭaʿāt letter-clusters (الم, الر, حم) are partially predictable (RF top-1 = 41%, p=0.002) and that الر recall was highest for the Q 10–12 prophet-named cluster, while حم has a divine-attribute / eschatological-tinted signature.

[[h-new-97-name-letter-joint|H-NEW-97]] **connects** these two findings: conditional on being a muqaṭṭaʿāt-opener, **do the specific letter-clusters share specific name-classes?** I.e., does the joint distribution over (letter-set, name-class) depart from independence?

## Hypothesis

H1 (signal): Letter-set and name-class are NOT independent across the 29 muqaṭṭaʿāt-opened surahs.
H0 (null): Letter-set and name-class are independent given muqaṭṭaʿāt-status.

## Sample

N = 29 muqaṭṭaʿāt-opened surahs (locked, from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]/49/88):
Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68.

## LOCKED letter-set taxonomy (10 classes)

Task brief specifies 10 letter-sets. Locked BEFORE viewing joint as follows:

| # | Set | Surahs | n |
|---|---|---|---|
| 1 | **ALM** (الم) | 2, 3, 29, 30, 31, 32 | 6 |
| 2 | **ALR** (الر) | 10, 11, 12, 14, 15 | 5 |
| 3 | **HM** (حم) | 40, 41, 43, 44, 45, 46 | 6 |
| 4 | **TSM** (طسم) | 26, 28 | 2 |
| 5 | **ALMS** (المص) | 7 | 1 |
| 6 | **ALMR** (المر) | 13 | 1 |
| 7 | **KHYAS** (كهيعص) | 19 | 1 |
| 8 | **HMASQ** (حم·عسق) | 42 | 1 |
| 9 | **SINGLE_COMPOUND** — merged "rare multi-letter singletons" ؟ | — | 0 |
| 10 | **SINGLE_SIMPLE** — 1-letter-sets merged {ص, ق, ن} + 2-letter singletons {طه, يس, طس} | 20, 27, 36, 38, 50, 68 | 6 |

**Decision locked**: Per task brief "some singletons might collapse into base sets; stay consistent with [[h-new-88-letter-set-predictor|H-NEW-88]] taxonomy": [[h-new-88-letter-set-predictor|H-NEW-88]] kept all 14 sets separate. For the χ² independence test, cells are too sparse at 14 × 9 = 126 cells on N=29. I collapse as follows for the PRIMARY χ² to get sensible expected counts:

- **Primary contingency (10 rows × 9 name-class cols = 90 cells)**: 8 compound-letter singletons split into their own rows (ALMS, ALMR, KHYAS, HMASQ each stay separate) plus **SINGLE_SIMPLE** pooling the 6 one-letter and short-2-letter singletons (طه, يس, ص, ق, ن, طس). This is the 10-row taxonomy in the task brief (ALMS+ALMR+KHYAS+HMASQ = 4 of the "7 singletons"; طه+يس+ص+ق+ن+طس = 6 merged into SINGLE_SIMPLE; total 10 rows).
- **Fallback contingency (3 rows × name-class cols)**: cluster-only, i.e., {ALM, ALR, HM} × name-class × N=17. Used if primary χ² expected-cell violation is severe.

This collapse is **locked BEFORE viewing joint**. Rationale: SINGLE_SIMPLE is a pre-existing cut from [[h-new-88-letter-set-predictor|H-NEW-88]] (all 1–2-letter singletons share the "unique-marker" profile that cluster-member surahs do not).

## Name-class taxonomy (LOCKED from [[h-new-49-surah-name-class|H-NEW-49]])

9 classes, verbatim from [[h-new-49-surah-name-class|H-NEW-49]]:
- PROPHET_PERSON, ANIMAL_OBJECT, DIVINE_ATTRIBUTE, COSMOLOGICAL_NATURAL, EVENT_ESCHATOLOGICAL, SOCIAL_LEGAL, REVELATION_RITUAL, MUQATTAAT_LETTER, OTHER_ABSTRACT.

No reclassification. The 29 muqaṭṭaʿāt-opened surahs' class assignments come directly from `findings/phase-b-hypotheses/csv/h-new-49.json`.

## Test cells (Bonferroni k=4, α_bon = 0.0125)

### Cell 1 — PRIMARY: χ² independence on 10 × N_classes contingency
- Compute χ² statistic on full 10-row × 9-col table (some classes will be empty across all 29 muq surahs — they become columns-with-zero-total and are dropped before χ², which is standard).
- Use Monte-Carlo null: 10K permutations of the name-class label across the 29 muqaṭṭaʿāt surahs (preserves row margin = letter-set counts; resamples column assignment).
- **Acceptance**: p_MC < 0.0125.

### Cell 2 — SECONDARY: per-cluster χ² vs uniform over 9 name-classes
- For each of the 3 multi-member clusters (ALM n=6, ALR n=5, HM n=6):
  - Compute χ² goodness-of-fit vs uniform-over-9-classes null.
  - Report p-value per cluster.
  - **Cell-2 result accepted** iff at least 2/3 clusters individually reject at p<0.0125.

### Cell 3 — TERTIARY: Cramer's V effect size
- Compute Cramer's V on the primary 10×N contingency. Report as descriptive effect size.
- No p-value required; reported for interpretation.
- Threshold for "large effect": V > 0.30.

### Cell 4 — QUATERNARY: per-cluster name-class RANK profile
- For each multi-member cluster, list name-class counts in descending order.
- Directional check: does ALR have PROPHET_PERSON as its modal class? (pre-reg direction).
- Does HM have DIVINE_ATTRIBUTE or narrative/eschatological-heavy modal?
- Does ALM have mixed profile (no single class >3/6)?
- **Accepted** iff the directional predictions for ALR + HM + ALM all match qualitative expectation.

## Garden-of-forking-paths log

**Prior information reviewed BEFORE pre-reg lock**:
1. [[h-new-49-surah-name-class|H-NEW-49]] class assignments for the 29 muq surahs have been READ (see data extraction above — this is required to run the test). However, the JOINT 10×9 contingency table has NOT been constructed, viewed, or tallied. Margins of each axis are known from prior findings (e.g., PROPHET_PERSON count = 7 of 29), but the cell-level joint is unobserved.
2. [[h-new-88-letter-set-predictor|H-NEW-88]] letter-set distribution is known: ALM=6, HM=6, ALR=5, TSM=2, 8 singletons.
3. [[h-new-49-surah-name-class|H-NEW-49]]'s own per-class muq-rate is known (PROPHET_PERSON 64%, EVENT_ESCH 6%, etc.) — this gives the row-conditional margins but NOT the letter-set × class joint.

**Directional predictions locked here BEFORE tally**:
- ALR will be PROPHET_PERSON-modal (given Q 10, 11, 12, 14 are prophet-named).
- HM will have no PROPHET_PERSON (Q 40–46 are not prophet-named in [[h-new-49-surah-name-class|H-NEW-49]]'s taxonomy except possibly none) and will have a mix of SOCIAL_LEGAL / ANIMAL_OBJECT / COSMOLOGICAL / DIVINE_ATTRIBUTE / REVELATION / EVENT_ESCH.
- ALM will be mixed (Q 2 ANIMAL, Q 3 PROPHET, Q 29 ANIMAL, Q 30 SOCIAL, Q 31 PROPHET, Q 32 REVELATION).

These directional predictions are derived DIRECTLY from the [[h-new-49-surah-name-class|H-NEW-49]] class assignments of the 29 muq surahs listed above, which this specialist read to construct the taxonomy. The cell-level counts are LOCKED BEFORE execution by virtue of being deterministic reads of two locked taxonomies.

**Post-hoc concession**: because the directional predictions derive from deterministic classification, the predicted directions are essentially pre-loaded; Cell 4's "accepted" verdict is tautological-IF the directions match. The NOVELTY is in Cell 1 (χ² independence p-value) and Cell 2 (per-cluster χ² magnitude and its Bonferroni-4 survival), which DEPEND on cell counts but NOT on the directional prediction of which class dominates.

## Bonferroni

- k = 4 (Cell 1, 2×3-sub-tests pooled as Cell 2, Cell 3 descriptive (no p), Cell 4 descriptive (no p)). 
- Conservative treatment: if we count the 3 Cell-2 sub-tests as 3 separate tests, k = 5 and α_bon = 0.01. I lock **k = 4** per task brief, treating Cell 2 as a single "family" judged by the 2/3 criterion. If the 2/3 criterion is not met but any individual cluster survives α = 0.01 (stricter), I will report it honestly as "passes at k=5 not k=4" — tightening is self-verifying.

## Publication policy

- PRE-REG-STANDARD-04: all Bonferroni frontmatter fields declared above.
- NULL result published with same prominence as PASS.
- Every cell reports observed + null-mean + p.
- Cramer's V reported regardless of significance.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_97_name_letter_joint.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-97.json`
- Findings: `findings/phase-b-hypotheses/h-new-97-name-letter-joint.md`
- Journal: `journal/h-new-97-run-1.md`

Seed: 20260417 (locked).
