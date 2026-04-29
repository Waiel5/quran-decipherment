# [[h-new-236-2b-extra-scaffold-predictability|H-NEW-236.2b]] - Held-out predictability of the extra scaffold edges

**Finding ID**: `[[h-new-236-2b-extra-scaffold-predictability|h-new-236-2b]]`  
**Date**: `2026-04-19`  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability-prereg.md`  
**Pre-reg SHA-256**: `b6bfd54250cfb42d37f53c14f00a6b9b7d59e8f89e0b1dcce3d53c3d5516a7cf`  
**Seed**: `20260419`  
**Rules tuple**: `(113 canonical consecutive edges; H100 and H50 imported directly from [[h-new-236-1d-minimal-k-bracket|h-new-236-1d]].json; positive=P=H100\H50; negative=N=E\H100; 9 locked binary features from [[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]; LOOCV logistic C=1.0 class_weight=balanced solver=newton-cholesky; 10000 label permutations; descriptive [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 positive control)`  
**Verdict**: **PASS-DIRECTED (weak)**. The locked 9-feature family predicts the extra-scaffold tranche above the permutation null, but only modestly: `AUC_LOOCV = 0.647692`, `p_perm = 0.030197`. The same feature family is much stronger on the earlier [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 jump problem (`AUC = 0.900680`, descriptive only).

## Headline

This run asked a narrow held-out question:

> once the already-landed top-50 scaffold is removed from the target, can the
> *additional* edges that enter by top-100 (`H100 \ H50`) still be recovered
> from a compact locked family of classical-boundary features?

Answer:

- **yes, but weakly**
- the signal is formally above the 10,000-permutation null
- the effect size is modest and far below the earlier [[h-new-130-fisher-rao-residuals|H-NEW-130]] jump problem

So the extra scaffold is **not pure unstructured residue**, but it is also not
cleanly compressible by this 9-feature family.

## 1. Locked pool and primary result

Universe:

- all `113` canonical consecutive edges

Locked analysis pool:

- positives `P = H100 \ H50` -> `50` edges
- negatives `N = E \ H100` -> `13` edges
- total pool -> `63` edges

Primary LOOCV result:

| Metric | Value |
|---|---:|
| `AUC_LOOCV` | **0.647692** |
| Accuracy at 0.5 | 0.619048 |
| Balanced accuracy at 0.5 | 0.731538 |
| Permutation `p` | **0.030197** |
| Null mean AUC | 0.430961 |
| Null q95 | 0.623077 |
| Null q99 | 0.692308 |
| Null max | 0.793846 |

`301 / 10000` label shuffles met or exceeded the observed AUC, giving the
exact one-sided permutation p-value above.

Under the locked prereg rule, that is enough for **PASS-DIRECTED**. Under the
locked descriptive bands, the effect remains **weak** rather than moderate or
strong.

## 2. Why the signal is weak rather than strong

The pool geometry is lopsided in a very specific way:

- all `13` negatives lie **inside mufaṣṣal-short**
- only `23 / 50` positives lie there

That makes `within_mufassal_short` the dominant separating pressure in the
wrong direction for many true positives. The full-data logistic fit reflects
exactly that:

| Feature | Coefficient |
|---|---:|
| `within_mufassal_short` | **-2.222671** |
| `classical_length_boundary` | +0.418034 |
| `muq_presence_change` | +0.377077 |
| `phase_transition` | +0.257314 |
| `muq_letterset_change` | +0.141846 |
| `period_transition` | +0.107676 |
| `within_hawamim` | +0.087124 |
| `same_rhyme_class` | -0.179432 |
| `liturgical_pair` | -0.432041 |

Interpretation:

- the model does recover a **real boundary-coded signal** from classical
  length slots, chronology transitions, and muq-boundary changes
- but the late extra-scaffold tranche inside mufaṣṣal-short is only weakly
  captured by the rest of the feature family
- rhyme-class and liturgical-pair indicators do **not** rescue that late
  tranche once the negative set is defined as `E \ H100`

That is the central result of the run.

## 3. Where the model succeeds

The highest-probability held-out positives are mostly the earlier structural
add-on edges rather than the late terminal chain:

| Edge | True label | LOOCV `p_positive` |
|---|---:|---:|
| `Q50 -> Q51` | 1 | 0.909600 |
| `Q67 -> Q68` | 1 | 0.909600 |
| `Q77 -> Q78` | 1 | 0.889670 |
| `Q3 -> Q4` | 1 | 0.886887 |
| `Q6 -> Q7` | 1 | 0.886887 |
| `Q39 -> Q40` | 1 | 0.886887 |
| `Q68 -> Q69` | 1 | 0.886887 |

These are exactly the kinds of edges the locked feature family was built to
recognize:

- classical boundary slots
- phase / period transitions
- muq-entry or muq-regime changes

So the classifier is not drifting randomly. It is recovering the
boundary-shaped part of the extra scaffold.

## 4. Where it fails

At threshold `0.5` there is only **1 false positive**:

- `Q110 -> Q111` with `p = 0.746484`

But there are **23 false negatives**, and they are overwhelmingly the late
terminal additions:

- `Q78 -> Q79`
- `Q79 -> Q80`
- `Q80 -> Q81`
- `Q81 -> Q82`
- `Q82 -> Q83`
- `Q83 -> Q84`
- `Q84 -> Q85`
- `Q85 -> Q86`
- `Q86 -> Q87`
- `Q87 -> Q88`
- `Q88 -> Q89`
- `Q89 -> Q90`
- `Q90 -> Q91`
- `Q91 -> Q92`
- `Q92 -> Q93`
- `Q95 -> Q96`
- `Q96 -> Q97`
- `Q97 -> Q98`
- `Q98 -> Q99`
- `Q99 -> Q100`
- `Q100 -> Q101`
- `Q101 -> Q102`
- `Q109 -> Q110`

This is the cleanest qualitative read of the finding:

> the simple feature family can recover the extra scaffold when that scaffold
> still looks like [[h-new-130-fisher-rao-residuals|H-NEW-130]]-style boundary structure, but it does **not**
> adequately recover the dense late mufaṣṣal-short tranche.

That is why the AUC is above null but only modestly so.

## 5. Feature prevalence in the locked pool

| Feature | Positives | Negatives |
|---|---:|---:|
| `classical_length_boundary` | 2 | 0 |
| `period_transition` | 5 | 1 |
| `phase_transition` | 8 | 1 |
| `muq_presence_change` | 6 | 0 |
| `muq_letterset_change` | 2 | 0 |
| `within_hawamim` | 1 | 0 |
| `within_mufassal_short` | 23 | 13 |
| `same_rhyme_class` | 9 | 5 |
| `liturgical_pair` | 2 | 2 |

Two consequences follow immediately:

1. Several features occur only in positives and therefore contribute some real
   separative signal.
2. The late-block features are **not** exclusive to positives under this pool
   definition, because every negative edge also lives in the same terminal
   region. That is exactly what suppresses effect size.

## 6. Descriptive positive control

Using the same 9 features, same logistic model, and same LOOCV pipeline on the
full [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 jump problem gives:

| Metric | Value |
|---|---:|
| `AUC_LOOCV` | **0.900680** |
| Accuracy at 0.5 | 0.734513 |
| Balanced accuracy at 0.5 | 0.736395 |

This branch is **descriptive only** in [[h-new-236-2b-extra-scaffold-predictability|H-NEW-236.2b]], but it matters
interpretively:

> the feature family is clearly strong enough to recover the earlier [[h-new-130-fisher-rao-residuals|H-NEW-130]]
> jump regime, and only partially generalizes to the later extra-scaffold
> regime.

So the weak main AUC is not because the feature family is empty. It is because
the specific `H100 \ H50` tranche is structurally harder and less cleanly
boundary-coded than the [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 set.

The positive-control full-model coefficients also show a different regime:

- `period_transition = +2.000148`
- `phase_transition = +1.738635`
- `within_mufassal_short = -1.662738`

That is exactly the [[h-new-130-fisher-rao-residuals|H-NEW-130]] picture: large jumps are heavily concentrated at
chronological transition seams, whereas the extra scaffold extends further into
terminal internal structure.

## 7. Interpretation

The honest combined read is:

- **OQ-16 is still already answered by the hinge family itself**: [[h-new-236-generative-simulator|H-NEW-236]]
  and descendants showed that the residual is the structural-hinge component.
- [[h-new-236-2b-extra-scaffold-predictability|H-NEW-236.2b]] adds a narrower second-layer statement:
  the *extra* scaffold beyond top-50 is **weakly predictable** from the locked
  classical-boundary feature family, but much of its late terminal structure is
  **not** compressed by those nine indicators alone.

In practical terms:

> the extra scaffold has some classical-boundary regularity, but a large share
> of the top-50 -> top-100 increment behaves like a late-region internal
> adjacency family rather than a simple seam/boundary family.

That is consistent with the [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] story:

- broad hinge extension closes the terminal residual
- but the terminal additions are not reducible to a tiny list of rhyme or
  liturgical indicators
- and they are only partially recoverable from this compact boundary-feature
  codebook

## 8. Honest limits

1. The pool intentionally excludes `H50`, so this is **not** a classifier over
   all canonical edges.
2. The main pool is heavily imbalanced (`50 / 13`) and the negatives all sit in
   the same terminal region. That makes `within_mufassal_short` a confound as
   much as a feature.
3. Several features are very rare, so their coefficients are interpretable in
   sign more than in precise magnitude.
4. The positive control is descriptive only here. Its strong AUC supports
   interpretation but does not add inferential weight to [[h-new-236-2b-extra-scaffold-predictability|H-NEW-236.2b]] itself.
5. A richer late-terminal feature family might lift the AUC further, but that
   would be a different preregistered task, not an amendment to this one.

## Bottom line

**PASS-DIRECTED (weak).** The nine locked binary features recover the extra
scaffold tranche above the 10,000-permutation null (`AUC = 0.647692`,
`p = 0.030197`), but the effect is modest and concentrated in the earlier
boundary-shaped additions. The dense late mufaṣṣal-short additions remain only
partially predictable. By contrast, the same pipeline is very strong on the
earlier [[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 jump problem (`AUC = 0.900680`, descriptive only).
