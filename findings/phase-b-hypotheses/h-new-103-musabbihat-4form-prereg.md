---
id: H-NEW-103
title: Musabbiḥāt 4-Form Sub-Typology — Pre-Registration
phase: B
date: 2026-04-17
agent: h-new-103-specialist
status: PRE-REGISTERED
parent_family: H-NEW-58c (musabbiḥāt tense split extended from 5 → 7 surahs)
corpus_anchor: 6,236 verses / 77,797 tokens / Hafs-Kūfan
rules_tuple:
  orthography: min-tashkeel for verbal-form disambiguation; no-tashkeel for char-prefix/Jaccard similarity metrics
  tokenization: whitespace
  basmala_policy: basmala-counted-only-in-surah-1 (default JSON state)
bonferroni_k: 4
bonferroni_family: h-new-103-musabbihat-4form
alpha_bon: 0.0125
direction_A: descriptive (form assignment verification)
direction_B: within-form similarity > cross-form similarity; permutation p<alpha_bon (one-sided)
direction_C: exploratory 2-sided (length / period / Meccan-Medinan × form cross-tabulation)
direction_D: exploratory (Friday-cluster functional overlap with imperfect-form vs perfect-form)
acceptance_window: cell-B is PRIMARY directional; cells A/C/D descriptive or exploratory
seed: 20260417
---

# [[h-new-103-musabbihat-4form|H-NEW-103]] — Musabbiḥāt 4-form sub-typology (pre-registration)

## Hypothesis

The 7 classical musabbiḥāt surahs (Q 17, 57, 59, 61, 62, 64, 87) exhibit a **4-form verbal typology** at their opening: NOUN (Q 17), PERFECT (Q 57, 59, 61), IMPERFECT (Q 62, 64), IMPERATIVE (Q 87). Extending [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] (which established the perfect/imperfect binary for the Q 57-64 sub-cluster), this pre-reg asks whether the **full 4-form partition** has structural correlates — specifically, whether **within-form content similarity exceeds cross-form content similarity** by a margin detectable under permutation.

## The 7 musabbiḥāt (classical canon)

| Surah | Name | v1 verbal form | Form label | Period |
|------:|------|---|---|---|
| Q 17 | al-Isrāʾ | subḥāna alladhī asrā | NOUN | Meccan (Middle) |
| Q 57 | al-Ḥadīd | sabbaḥa li-llāhi | PERFECT | Medinan |
| Q 59 | al-Ḥashr | sabbaḥa li-llāhi | PERFECT | Medinan |
| Q 61 | al-Ṣaff | sabbaḥa li-llāhi | PERFECT | Medinan |
| Q 62 | al-Jumuʿah | yusabbiḥu li-llāhi | IMPERFECT | Medinan |
| Q 64 | al-Taghābun | yusabbiḥu li-llāhi | IMPERFECT | Medinan |
| Q 87 | al-Aʿlā | sabbiḥi sma rabbika | IMPERATIVE | Meccan (Early) |

Auxiliary cell (excluded from primary): Q 20 Ṭāhā contains "sabbiḥ" at v130 (imperative) but v1 is the muqaṭṭāʿa طه; reported as auxiliary only.

## Test cells

### Cell A — 4-form verbal-form ratification (descriptive)

Re-read v1 of each of the 7 musabbiḥāt under min-tashkeel and tabulate the verbal form. Assign each surah to ONE of {NOUN, PERFECT, IMPERFECT, IMPERATIVE}. Output: 4-form membership table. No p-value; descriptive.

### Cell B — Within-form vs cross-form content similarity (PRIMARY directional)

Compute three per-surah-pair similarity metrics on the no-tashkeel text:

1. **char-prefix**: number of characters from position 0 in v1 that match between a pair of surahs (same metric as [[h-new-58c-musabbihat-tense-split|H-NEW-58c]])
2. **root-Jaccard (whole-surah)**: QAC STEM root set intersection / union
3. **verse-length similarity**: 1 − |μ_a − μ_b| / max(μ_a, μ_b) on mean verse-length

For each metric M, compute:
- `mean_within_form(M)` = mean of M over all within-form pairs (pairs where both surahs share the same form label; excludes singleton forms which produce 0 pairs)
- `mean_cross_form(M)` = mean of M over all cross-form pairs

Test statistic: Δ(M) = mean_within_form(M) − mean_cross_form(M).

**Direction**: Δ(M) > 0 (within-form tighter than cross-form) for each metric.

**Null**: 10,000 permutations of the 7 form-labels across the 7 surahs (preserving form-label multiset {NOUN:1, PERFECT:3, IMPERFECT:2, IMPERATIVE:1}), seed 20260417. For each permutation, recompute Δ(M). One-sided p = (1 + #{perm Δ ≥ observed Δ}) / (1 + N_perm).

**Pass rule**: Combined test — PASS if the char-prefix metric has p < α_bon = 0.0125 (since this is the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] primary-derived metric, continuity with [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]'s 0.0001 signal expected). Secondary metrics (root-Jaccard, verse-length) reported but not counted toward primary PASS/NULL.

Note: only forms with ≥ 2 members contribute to within-form pairs (PERFECT contributes C(3,2)=3 pairs; IMPERFECT contributes C(2,2)=1 pair). Singleton forms (NOUN, IMPERATIVE) contribute 0 within-form pairs; all their pairs go to cross-form. Total pairs: C(7,2)=21; within-form = 3+1 = 4; cross-form = 17.

### Cell C — Form × structural class cross-tabulation (exploratory, 2-sided)

Cross-tabulate the 4 forms against:
- **Length class**: short (≤30 verses) / medium (31-100) / long (>100)
- **Period**: Meccan vs Medinan
- **Nöldeke phase**: Early / Middle / Late Meccan / Medinan
- **Muqaṭṭāʿat-opener status**: Y/N (only Q 20 has muqaṭṭāʿa; all 7 primaries do not)

Report contingency tables; no formal test (too few cells and exploratory).

### Cell D — Friday-cluster functional cross-reference (exploratory)

Q 62 al-Jumuʿah is the canonical Friday-recitation surah ([[h-new-68-friday-cluster|H-NEW-68]]) and, per [[h-new-89-meta-cluster-network|H-NEW-89]], the unique 4-cluster meta-hub. Q 64 al-Taghābun (also imperfect form) does not carry a Friday-recitation convention in the standard reports. Classical Friday-recitation also pairs Q 62 with Q 63 (al-Munāfiqūn, NON-musabbiḥa), not with Q 64. The functional question: **does the imperfect-form sub-group (Q 62 + Q 64) have a recognizable functional signature distinct from the perfect-form sub-group (Q 57, 59, 61)**, e.g., in classical recitation conventions, surah-topic emphasis, or length pattern?

Operationalization: descriptive cross-reference — report each surah's known recitation context, classical topical label, length, and whether any shared Friday/Jumuʿah association is documented.

## MW-5 positive control

**Expected**: Q 57, 59, 61 are ALL PERFECT; [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] showed perfect-perfect char-prefixes of 24, 24, 56 (mean 34.7). Under the new within-vs-cross permutation null, the PERFECT pairs must dominate the within-form mean; if the shuffle does NOT reproduce the 24-56 range as "unusually tight," the instrument is broken. Report the **within-form char-prefix mean** and the **char-prefix Δ** against the null. If within-form mean < 10 chars or if cross-tense prefix mean > 5 chars, declare INSTRUMENT-FAIL (cell B unreliable).

## Garden-of-forking-paths log

1. **Post-hoc origin**: The 4-form typology is a DIRECT extension of [[h-new-58c-musabbihat-tense-split|H-NEW-58c]], which found the perfect/imperfect binary post-hoc. I have not viewed Q 17's or Q 87's content-similarity to Q 57-64 before writing this pre-reg. The v1 verbal forms have been read (required to stratify the forms) but no cross-pair similarity computations have been run.

2. **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]] priors (explicit disclosure)**:
   - Q 57, 59, 61 form a tight perfect-form cluster (char-prefix 24-56)
   - Q 62, 64 form a tight imperfect-form cluster (char-prefix 37)
   - Cross-tense pairs among these 5: EXACTLY 0
   These priors guarantee cell-B passes IF Q 17 and Q 87 do not spoil the within-form tightness. Q 17 and Q 87 are SINGLETONS in their respective forms, so they contribute ZERO within-form pairs. They can only contribute to cross-form pairs (bringing down the cross-form mean relative to an all-zeros scenario — working AGAINST the within>cross direction). Therefore the [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] prior does not pre-ordain cell-B PASS by construction; the cross-form mean is genuinely free to vary.

3. **Bonferroni choice**: k=4 covers the four pre-committed cells (A, B, C, D). Cell-B is the primary directional test. The 3 similarity metrics within cell-B are NOT separately Bonferronified (the char-prefix metric is the primary declared metric; the other two are secondary diagnostics).

4. **Form-label multiset preservation in null**: critical — shuffling form labels while preserving multiset {1,3,2,1} means the null is over "which surahs get which labels," not over arbitrary re-stratifications. This respects the classical 4-form canon.

5. **Q 20 auxiliary**: Q 20 opens with muqaṭṭāʿa طه; excluded from primary. Reported separately as auxiliary data with "imperfect sabbiḥ at v130" note.

6. **Direction is LOCKED BEFORE viewing** any new cross-pair computations involving Q 17 or Q 87.

## Outputs

1. Script: `scripts/h_new_103_musabbihat_4form.py`
2. JSON: `findings/phase-b-hypotheses/csv/h-new-103.json`
3. Findings: `findings/phase-b-hypotheses/h-new-103-musabbihat-4form.md`
4. Journal: `journal/h-new-103-run-1.md`

## Acceptance window

- **Cell B char-prefix p < 0.0125** → PASS-DIRECTED (note: PASS-DIRECTED not CONFIRMED because descends from [[h-new-58c-musabbihat-tense-split|H-NEW-58c]] post-hoc observation)
- Cell B p ≥ 0.0125 → NULL
- MW-5 instrument-fail → INSTRUMENT-FAIL (no declaration)
- Cells A, C, D are descriptive/exploratory; no PASS/NULL declaration
