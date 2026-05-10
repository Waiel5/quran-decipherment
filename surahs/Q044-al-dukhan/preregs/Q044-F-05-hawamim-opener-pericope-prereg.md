---
prereg_id: Q044-F-05
title: ḥawāmīm sibling-opener pericope test — Q 44:1-8 ↔ Q 41:1-8 / Q 46:1-8
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q044-F-05 — HM opener-pericope similarity

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The opener-pericopes Q 44:1-8, Q 41:1-8, and Q 46:1-8 (HM + 7 introduction verses) share *higher pairwise Jaccard root-overlap* than randomly-selected size-8 verse-blocks from non-HM surahs.

This tests whether the HM opener is a *templated unit* (shared lexicon, shared formal structure) or *independent* (only the muqaṭṭaʿāt is shared).

## 2. Null / negation

**H0**: The mean pairwise Jaccard of the 3 HM opener-pericopes is ≤ the null distribution median.

## 3. Operationalization

- Pericope = verses 1-8 inclusive for each of Q 41, Q 44, Q 46.
- Source: `data/morphology/quranic-corpus-morphology-0.4.txt` for QAC v0.4 root extraction; `quran-text/quran-no-tashkeel.json` for verse text.
- Verse-block root-set = unique stem-roots in the 8-verse window.
- Pairwise Jaccard = |A ∩ B| / |A ∪ B|.
- Observed metric: mean of 3 pairwise Jaccards (Q41-Q44, Q41-Q46, Q44-Q46).
- Null: 10000 permutations sampling 3 random size-8 verse-blocks from non-HM surahs; compute mean Jaccard each draw.
- Sampling constraint: blocks chosen from surahs with ≥8 verses; block-start uniform within surah.
- One-sided upper-tail p = (# null means ≥ observed) / 10000.

## 4. Direction lock

Pre-committed: **observed mean Jaccard > null median** (HM openers share template).

## 5. Bonferroni

Member of Q 44 novel-findings family (k=3 in this batch). α_corrected = 0.0167.

## 6. Success / failure criteria

- **PASS-DIRECTED**: p < 0.0167 AND observed > null median.
- **DIRECTIONAL**: observed > null median but p ≥ 0.0167.
- **NULL**: observed ≤ null median.

## 7. Seed

`20260509`. `n_perm = 10000`.

## 8. Output

JSON to `csv/Q044-F-05.json`: pericope_roots (Q41, Q44, Q46), observed_jaccards (3 pairwise), observed_mean, null_stats (median, p25, p75), p_one_sided, verdict.

## 9. Rationale

The HM cluster's defining feature is the shared opener حم. Cross-finding-025 (marker-thickness rule) warns that single-marker clusters often NULL on root-FR. This test isolates the *opener-pericope window* (8 verses each), where the template effect should be strongest, to determine whether the muqaṭṭaʿāt opener templates the *immediate context* even when the full surahs diverge.

## 10. Honest limits

- 8-verse window is a hyperparameter; not tested at other widths in this batch.
- Jaccard is symmetric and ignores frequency; weighted variants not tested here.
- Sampling pool of non-HM surahs ≥8 verses is large (~100); null is well-resolved.
- Q 42:1-8 spans the special **ʿsq** secondary opener — deliberately EXCLUDED from the HM-3 because Q 42's opener-pattern is heterogeneous (HM at v1 then ʿsq at v2); a follow-up could test Q 42:1-8 separately.
