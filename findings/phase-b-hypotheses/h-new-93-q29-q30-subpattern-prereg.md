---
hypothesis_id: H-NEW-93
title: "Q 29 al-ʿAnkabūt + Q 30 al-Rūm as a TEST-AND-PROPHECY muqaṭṭāʿat sub-pattern"
date_prereg: 2026-04-17
author: h-new-93-specialist
status: PRE-REG-LOCKED
data_variant: no-tashkeel
rules_tuple: (hafs-kūfan; no-tashkeel; QAC-morphology-root-STEM-tokens v0.4)
seed: 20260417
perms: 10000
bonferroni_k: 4
bonferroni_family: h-new-93-sub-pattern
alpha_bon: 0.0125
alpha_single_test_cap: 0.05
direction: "Q29+30 higher on (a) test-of-believers + (b) historical-prophecy; NOT different from Meccan baseline on (c) Allah-density; similar to other Meccan on (d) eschatological"
acceptance_window: "single-test α=0.05 PASS-DIRECTED cap (post-hoc-noticed sub-cluster); extreme-p (e.g., < 10^-6) may justify citing Bonferroni-4-pass but ceiling remains PASS-DIRECTED until independent replication"
verdict_ceiling: PASS-DIRECTED
replication_requirement: independent operationalization or independent data slice before promotion
---

# [[h-new-93-q29-q30-subpattern|H-NEW-93]] — Q 29 + Q 30 TEST-AND-PROPHECY sub-pattern (PRE-REG)

## Context

Cross-finding-008 established that **27 of 29 muqaṭṭāʿat-opened surahs** reference "kitāb/qurʾān" (or extended writing-family) in verses 1-3 — hypergeometric p = 3 × 10⁻¹² ([[h-new-53-muqattaat-book-reference|H-NEW-53]]; extended to 10⁻¹³ via [[h-new-56-five-exceptions|H-NEW-56]]).

**The 2 genuine exceptions**: Q 29 al-ʿAnkabūt and Q 30 al-Rūm. Both:

- Late Meccan (Nöldeke period III)
- الم opener (same letter-set as Q 2, 3, 31, 32)
- Adjacent in mushaf order (29-30)
- Q 29 opens with a **TEST theme**: "Do the people think that they will be left to say: we believe — and they will not be tested (لا يفتنون)?" (Q 29:2)
- Q 30 opens with a **HISTORICAL PROPHECY**: "The Romans have been defeated (غلبت الروم) in the nearest land; but they, after their defeat, will be victorious (سيغلبون)" (Q 30:2-3)

**Hypothesis** ([[h-new-93-q29-q30-subpattern|H-NEW-93]]): Q 29 and Q 30 constitute a SECOND functional sub-class of muqaṭṭāʿat surahs — a **TEST-AND-HISTORICAL-PROPHECY** type — distinct from the dominant "book-introduction" function, with measurable differential density in test-related and historical-prophecy-related roots.

## Garden-of-forking-paths disclosure (post-hoc origin)

**CRITICAL**: The Q 29 + Q 30 sub-cluster was identified by **EYEBALL post-hoc** as the residual after cross-finding-008. Specifically:

- [[h-new-53-muqattaat-book-reference|H-NEW-53]] ran all 29 muqaṭṭāʿat surahs through a v1-3 kitāb/qurʾān substring scan; 24/29 hit
- [[h-new-56-five-exceptions|H-NEW-56]] extended the scan to writing-family (kitāb, qurʾān, qalam, satr); 25/29 hit
- Manual inspection of the 4 residuals identified Q 29 and Q 30 as the two NON-marginal exceptions (the other 2 — Q 50 Qāf and Q 68 Nūn — have surrounding context that pulls them into other sub-patterns)
- Q 29 and Q 30 were eyeballed to share a salient theme: testing + historical prophecy

This is a POST-HOC-NOTICED pattern, NOT a PRE-REGISTERED prediction. We therefore apply:

1. Single-test α = 0.05 cap (no full-Bonferroni-family credit)
2. Verdict ceiling = PASS-DIRECTED (not CONFIRMED)
3. Bonferroni-4 across the 4 pre-committed cells applies WITHIN this study; between-study elevation requires independent replication
4. Full disclosure in the final write-up

## Pre-committed test design

### Corpora and comparison groups

- **Target group**: Q 29 al-ʿAnkabūt, Q 30 al-Rūm (n = 2)
- **Other-الم group**: Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 31 Luqmān, Q 32 al-Sajda (n = 4)
- **Meccan-stratified non-muqaṭṭāʿat baseline**: 50 Meccan surahs that are NOT muqaṭṭāʿat-opened. Drawn from the 86 Meccan surahs minus the 26 muqaṭṭāʿat-opened Meccan ones (leaving 60); we take ALL 60 (re-specified; see stratification below).

### Stratification: Meccan-only baseline

Because Q 29 and Q 30 are Meccan, we restrict the non-muqaṭṭāʿat baseline to the 60 Meccan non-muqaṭṭāʿat surahs (type == "meccan" per loader; this matches the 86-Meccan classification — minus the 26 Meccan muqaṭṭāʿat). This is TIGHTER than the original spec of "50 Meccan-stratified"; we take the full set of 60 (which is MORE baseline, i.e., a strengthening of the comparison). This spec tightening is bidirectional-rule-legitimate per our methodology.

**Specialist-judgment override**: The pre-reg seed specified "50 Meccan-stratified"; we use all 60 Meccan non-muqaṭṭāʿat surahs because (1) it's strictly a tighter test (more null observations), (2) random sub-sampling to 50 would introduce a seed-dependent analyst degree of freedom that we prefer to avoid, (3) it preserves the Meccan-stratification logic exactly. Locked in pre-reg before run.

### Four pre-committed test cells

All roots are matched at the **STEM-ROOT level from the Quranic Arabic Corpus morphology v0.4** (Kais Dukes). The per-surah metric is **ROOT-TOKEN DENSITY** = (count of STEM tokens whose ROOT is in the cell's root-list) / (total STEM tokens in surah). All roots verified present in root-stats.csv.

**Cell (a) — TEST-OF-BELIEVERS density**

Roots: `{ftn (fitna/fatana), blw (balā/ibtilāʾ), mHn (imtiḥān), Sbr (ṣabr)}`

All-lemma, all STEM tokens matching these roots.

**Cell (b) — HISTORICAL-PROPHECY density**

Roots:
- `glb (ghalaba — conquer/defeat; the Q 30:2-3 verb)`
- `nSr (naṣara — help, victory)`
- `kwn (kāna — past perfect "was/were"; historical-narrative marker)` — filtered to PAST-PERFECT verbal forms only (lemma `kaAna`) to avoid generic copula inflation
- `ywm (yawm — day, with historical-marker specificity)` — filtered to prepositional-phrase "yawma ʾidh" and specific historical-day constructions is non-trivial; for pre-reg robustness we use the FULL ywm root but interpret as historical-marker proxy

**Note**: kwn is the Arabic copula and is VERY high-frequency everywhere (1,390 occurrences / 86 surahs in QAC). To prevent the kwn signal from drowning the narrow historical markers, we report cell (b) with and WITHOUT kwn; the pre-committed primary statistic uses the full 4-root list. We ALSO report the ghalaba-only and ghalaba+naṣara-only statistics as pre-committed secondary.

**Cell (c) — ALLAH-DENSITY CONTROL**

Root: `{Alh}` (includes "Allāh", "ilāh", etc.)

Prediction: NO significant difference between target group and Meccan baseline. This is a negative control; if it differs significantly, it suggests a generic-divine-density confound.

**Cell (d) — ESCHATOLOGICAL density**

Roots: `{Axr (ākhir/ākhira), bEv (baʿth — resurrection), Hsb (ḥisāb — reckoning), jzy (jazāʾ — recompense)}`

All STEM tokens matching these roots.

Prediction: Q 29+30 should NOT differ significantly from Meccan baseline on this cell (i.e., eschatological density is generic-Meccan, not a sub-pattern marker).

### Test statistic

For each cell, two comparisons:
1. **Target (Q29+30) vs other-الم (Q2, Q3, Q31, Q32)**: mean density difference
2. **Target (Q29+30) vs Meccan non-muqaṭṭāʿat (n=60)**: mean density difference

### Null via permutation

For each cell and each comparison, permutation test:
- 10,000 permutations (seed 20260417)
- Shuffle the group labels within the pooled set of surahs
- Recompute the mean density difference under the null
- Two-sided p = fraction of |perm_diff| ≥ |observed_diff|

Also report one-sided p in the pre-registered direction (target > other for cells (a)+(b); |target - baseline| minimized for cells (c)+(d)).

### MW-5 positive control

Cells (a) and (b) for the **OTHER-الم group (Q 2, 3, 31, 32)** compared to the Meccan non-muqaṭṭāʿat baseline. Per the book-introducer sub-pattern hypothesis, these 4 surahs should NOT show elevated test/prophecy density (they are book-introducers, not test-and-prophecy-type).

- Positive-control PASSES if Q 2, 3, 31, 32 show NO cell-(a) or cell-(b) elevation vs Meccan baseline (p > 0.05 two-sided)
- Positive-control FAILS if Q 2, 3, 31, 32 show elevation similar to Q 29+30

### Pre-committed verdicts

| Pattern | Cell (a) | Cell (b) | Cell (c) | Cell (d) | MW-5 | Verdict |
|---------|----------|----------|----------|----------|------|---------|
| Full target-pattern | Q29+30 > baseline, p<0.0125 | Q29+30 > baseline, p<0.0125 | Q29+30 ≈ baseline (p>0.05) | Q29+30 ≈ baseline (p>0.05) | PASS | **PASS-DIRECTED** |
| Partial target-pattern | 1 of (a)/(b) passes | other of (a)/(b) passes | OK | OK | PASS | **WEAK-PASS-DIRECTED** |
| Control violation | pass/fail | pass/fail | c fails (p<0.05) | OK | n/a | **INCONCLUSIVE-CONFOUND** |
| MW-5 fail | | | | | other-الم also elevated | **NULL-BROKEN-on-specificity** |
| Full target reject | (a)+(b) both p > 0.05 | | | | | **NULL** |

## Bonferroni family

- k = 4 pre-committed cells
- α_bon = 0.05 / 4 = **0.0125** per cell
- Separately, single-test α = 0.05 cap applies because this is post-hoc-noticed
- Interpretation: a cell that passes α_bon = 0.0125 is "strong within-family"; a cell that passes only α = 0.05 is "single-test-only"

## Data sources & rules-tuple

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4, Dukes 2011)
- `/Users/grey/Downloads/quran/data/morphology/root-stats.csv`
- `/Users/grey/Downloads/quran/data/revelation-order.csv` (Nöldeke via Tanzil) — for chronology sanity check (NOT primary test)
- Loader: `/Users/grey/Downloads/quran/analysis/tools/loader.py`

## Independent-replication plan

Post-PASS-DIRECTED, independent replication requires:

1. Different operationalization: e.g., SURFACE-STRING grep on Arabic text (not QAC-root) for test/prophecy phrases
2. Different data slice: e.g., test/prophecy density in v1-5 vs v1-10 vs whole-surah
3. Different feature set: e.g., classifier including stance-marker words, not just roots

Queued as H-NEW-93.1 (not in current pre-reg scope).

## Commitments

- All four cells computed before any p-values viewed
- Direction locked as stated above BEFORE null permutation runs
- Sign-flip prohibited (a cell passing in the REVERSE direction is EXPLORATORY-REVERSE)
- Full output (including null cell-level stats) reported with equal prominence

**END PRE-REG — lock at commit time.**
