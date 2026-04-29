# [[h-new-197-prophet-cycle|H-NEW-197]]: Prophet-narrative parallelism across surahs — NULL

**Date:** 2026-04-17
**Pre-reg:** `[[h-new-197-prophet-cycle|h-new-197]]-prophet-cycle-prereg.md` (same date, pre-run)
**Seed:** 20260419 | **N_null:** 2000 | **Bonferroni k:** 2

## Question

Does the Quran's repetition of prophet-stories (Moses, Abraham) across surahs follow a *common sequential template*? If so, inter-surah atom-sequence alignment should beat a within-surah shuffle null.

## Method (locked before run)

- Event-atoms (Moses: 11 codes; Abraham: 10 codes) detected by surface-form regex on min-tashkeel Arabic text with unicode normalisation (alef variants, ya/alef-maqsura, ta marbuta).
- For each target surah, collect verses containing the prophet-anchor (MU / IB) and ±1-verse neighbours; flatten atom firings into an ordered string; collapse adjacent duplicates.
- Score = mean normalised-Levenshtein pairwise similarity across all surah pairs.
- Null A (primary): shuffle verse-order within each surah, rebuild window around post-shuffle anchors, recompute score. 2000 reps.
- Null B: shuffle the atom-code string directly (loses all structure). 2000 reps.

## Results

### Moses cycle (Q 7, 10, 11, 20, 26, 28, 79)

| metric | value |
|---|---|
| observed mean pairwise sim | **0.235** |
| Null A mean ± sd | 0.238 ± 0.013 |
| Null A 97.5 % quantile | 0.265 |
| Null B mean ± sd | 0.214 ± 0.006 |
| **p (vs Null A, primary)** | **0.579** |
| p (vs Null B) | 0.0005 |
| Bonferroni α (k=2) | 0.025 |

**Verdict: NULL.** Observed is *below* the Null A mean. The surah-specific orderings are no more aligned with one another than a permuted baseline that preserves each surah's atom-bag.

Pairwise sims show a tight band ~0.10 – 0.44 (7↔20 = 0.39, 20↔28 = 0.44 are the "best-aligned" pairs; Q 79 is an outlier because it contains only `MU RB`).

Null B p is tiny (0.0005) — which just confirms the obvious fact that a completely scrambled atom string is *worse-aligned* than the real one. That is not evidence of a template; it is evidence that atoms are not uniformly random. Primary test is Null A.

### Abraham cycle (Q 14, 19, 21, 26, 37)

| metric | value |
|---|---|
| observed mean pairwise sim | **0.364** |
| Null A mean ± sd | 0.372 ± 0.067 |
| Null A 97.5 % quantile | 0.533 |
| Null B mean ± sd | 0.315 ± 0.030 |
| **p (vs Null A, primary)** | **0.494** |
| p (vs Null B) | 0.107 |

**Verdict: NULL.** Again, observed sits essentially on top of the Null A mean. The Abraham atom strings are short (len 1–7) because the anchor is sparse and the ±1 window is tight, making this test underpowered — but even so, there is no template signal.

## Verdict

Under the pre-registered rules-tuple (anchor-±1 window, Levenshtein similarity, per-verse-atom-bag shuffle null), **neither Moses nor Abraham cycles show a common sequential narrative template**. Both cycles: NULL, pass neither Bonferroni α = 0.025 nor the substantive-effect floor of 0.50.

## Interpretation

The claim "the Quran retells prophet stories with parallel syntactic ordering" is *not* supported by this operationalisation. The multi-telling appears to rearrange sub-events rather than follow a fixed template — consistent with classical observations (Ṭabarī, Rāzī) that Quranic prophet-narratives vary which episode is foregrounded per surah (e.g. Q 20 foregrounds call-at-Ṭuwā, Q 26 foregrounds the sorcerers' duel, Q 28 foregrounds Midian exile, Q 79 is a brief theological allusion).

## Fragility / limitations

- **Pre-reg window ±1 is tight.** Widening the window to ±3 or the full rukūʿ block would likely change sequence length but is a post-hoc tweak; not performed.
- **Atom inventory is coarse.** Only surface lexical cues, no syntactic parsing. A parsed-discourse-relation alignment (beyond this study's scope) might detect subtler template-like structure.
- **Null A is strong** — it preserves atom *bags* per verse, so only ordering is tested. If the hypothesis were "the Quran retells with a common *set* of atoms per surah", the answer would flip. That is a different hypothesis and would need a separate pre-reg.
- **Q 79 is an outlier** for Moses (length 2) and drags the mean pairwise sim down; removing it would be post-hoc, not done.

## Rules-tuple sensitivity

A follow-up not in this pre-reg (kept here only as a noted forking path, not executed): window ±3 with full-block inclusion, and an atom-bag-jaccard variant (ignores order) would address different hypotheses. They are not evidence for or against [[h-new-197-prophet-cycle|H-NEW-197]] as pre-registered.

## Files

- `scripts/h_new_197_prophet_cycle.py`
- `findings/phase-b-hypotheses/h-new-197-work/summary.json`
- `findings/phase-b-hypotheses/h-new-197-work/moses_sequences.tsv`
- `findings/phase-b-hypotheses/h-new-197-work/abraham_sequences.tsv`
- `findings/phase-b-hypotheses/h-new-197-work/moses_pairwise_sim.tsv`
- `findings/phase-b-hypotheses/h-new-197-work/abraham_pairwise_sim.tsv`
