---
prereg_id: H-NEW-2790
title: One harness, five flagged claims — the size-matched null applied in batch
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
status: PRE-REGISTERED — locked before any effect under test was computed
method_parent: [H-NEW-2770, H-NEW-2760, H-NEW-2680]
rule_applied: findings/UNIT-DRIFT-DEFECT.md
seeds: 20260509 primary / 20260519 replication
script: findings/phase-b-hypotheses/scripts/h-new-2790.py
run_dir: findings/phase-b-hypotheses/runs/h-new-2790/
---

# Pre-registration — H-NEW-2790

**Five claims, one harness, one locked decision rule. Nothing in §§3–8 had been computed
when this file was written; the only numbers already on the record at lock time are the
nuisance-channel correlations in §2, which the standing rule *requires* be measured before a
primary channel is locked, and the published headlines in §1, which are quotations.**

---

## 0. Why these five, and in this order

`findings/UNIT-DRIFT-DEFECT.md` states the rule and its three screens. A claim is FLAGGED if
it hits all three: **(A)** the headline statistic is a ratio with a unit count in the
denominator or a model whose features are such ratios; **(B)** the comparison runs across an
ordering with monotone unit-size drift; **(C)** no null holds unit size fixed.

The worklist was ranked by **citation count**, computed rather than asserted: every
`H-NEW-NNN` reference across all 2,859 markdown files in the repository outside `.git`,
`node_modules`, run directories and stale worktree copies. Findings already carrying a
correction notice were dropped, since correcting a corrected claim buys nothing.

| order | claim | cites | A | B | C | why here |
|--:|:--|--:|:-:|:-:|:-:|:--|
| **C1** | **H-NEW-192** — mushaf-position decomposition | **138** | ✓ | ✓ | ✗ | highest-cited uncorrected screen-hit; its top two RF features *are* the two strongest drift channels |
| **C2** | **H-NEW-183** — Nöldeke predictor | 50 | ✓ | ✓ | partial | the family's parent; supplies the 0.836 "ceiling" that C1 and C3 are both measured against |
| **C3** | **H-NEW-233** — 29-feature ensemble | 53 | ✓ | ✓ | ✗ | extends C1; its own top feature is `log_length` at 0.563 importance |
| **C4** | **H-NEW-74 Cell 6** — qul density × phase | 75 | ✓ | ✓ | ✗ | an independent density claim, different statistic (Kruskal–Wallis), so it tests the harness on a second shape |
| **C5** | **H-NEW-231** — per-surah KL divergence | 83 | ✓ | ✓ | n/a | **calibration arm, not a claim under test** — it *self-declares* length as its dominant axis, so the harness must recover that or the harness is wrong |

C2 outranks C3 and C4 despite fewer citations because it is structurally load-bearing in a
way citation counts do not capture: **C1's headline is not an R², it is a *difference*
against C2's R²** ("mushaf is ~8 % LESS predictable than Nöldeke"), and C3's pre-registered
PASS condition is "beats the Nöldeke ceiling of 0.836", which is C2's number. If C2 moves,
C1 and C3 both move with it.

**Claims deliberately NOT taken**, so the next session knows they were considered:
H-NEW-111 / 130 / 720 / 840 / 660 / 236.1 / 212 / 239 / 940 (all already carry correction
notices); H-NEW-125 (done by H-NEW-2770); H-NEW-142 (self-downgraded to
SPECULATIVE-DESCRIPTIVE by its own author); H-NEW-126 (Cell C already NULL-BROKEN, and the
headline is a cluster-membership claim, not a ratio); H-NEW-88, 136, 19, 570, 234, 49, 273,
123, 96, 90, 46, 44, 2210, 340, 290, 56.

---

## 1. The claims under audit, quoted exactly

**C1 — H-NEW-192**, `status: STRONG PASS + residual-extraction`:

> **15 compositional features predict mushaf position at R²≈0.76-0.82 (LOOCV).**
> **Mushaf is ~8% LESS PREDICTABLE than Nöldeke from the same features.** This gap
> quantifies the organizing principle that differentiates mushaf from chronology.

Published: Ridge LOOCV **R² = 0.759**, MAE 10.81; RF LOOCV **R² = 0.817**, MAE 7.96;
permutation null R² = −0.18, p < 0.0001. Top RF importances: `verse_count` **0.416**,
`mean_verse_length` **0.173**.

**C2 — H-NEW-183**, `status: PASS-DIRECTED (CHRONOLOGY-QUANTITATIVE)`:

> A 12-feature per-surah compositional signature predicts the Nöldeke revelation rank
> (1-114) with LOOCV R² = 0.836 … **The length-only baseline achieves R² = 0.446** …
> The full-feature model nearly **doubles** R² and **more than halves** MAE.

**C3 — H-NEW-233**, `status: PASS (RF cell; H2) — Ridge cell NULL (H1)`:

> RF (29 features) R² LOOCV **0.8485** … **+0.013 (beats ceiling!)** [vs Nöldeke 0.836]

**C4 — H-NEW-74 Cell 6**, `PASS`: qul density per 100 verses across the Nöldeke 4-phase
partition, **Kruskal–Wallis H = 35.36, df = 3, p = 1.02 × 10⁻⁷**, against its own
Bonferroni bar α = 0.00833. Phase means 1.74 / 4.89 / **8.95** / 4.93.

> **The qul-corpus is overwhelmingly a LATE-MECCAN phenomenon.**

**C5 — H-NEW-231** (calibration): per-surah KL divergence from the corpus average,
`title: … length is the dominant explanatory axis`.

---

## 2. The nuisance channels, ranked on the data BEFORE the primary was locked

The standing rule (`UNIT-DRIFT-DEFECT.md` §5) requires the candidate channels be measured
and ranked before one is locked as primary, because H-NEW-2760 locked the weaker of two on
an a-priori judgement and its rate ratio fell from 2.580 to 1.694 against the stronger.
**Measured here, on this corpus, before any arm of §4 was written:**

| ordering | channel | ρ (Spearman) | rank |
|:--|:--|--:|:-:|
| **mushaf position** | **log word count** | **−0.9342** | **1 — LOCKED PRIMARY for C1, C3, C5** |
| mushaf position | verse count | −0.8446 | 2 — locked secondary |
| mushaf position | mean verse length | −0.7131 | 3 |
| **Nöldeke rank** | **mean verse length** | **+0.9038** | **1 — LOCKED PRIMARY for C2, C4** |
| Nöldeke rank | log word count | +0.6892 | 2 — locked secondary |
| Nöldeke rank | verse count | +0.3903 | 3 |

All six reproduce `UNIT-DRIFT-DEFECT.md` §3 to four decimals. Cross-check:
ρ(mushaf, Nöldeke) = −0.6551.

**The sign asymmetry is load-bearing for this batch.** The two orderings drift in *opposite*
directions on verse length, so C1's "mushaf is 8 % less predictable than Nöldeke" is a
comparison between two models whose dominant nuisance channels are *different variables*.
That is registered here as a stated interpretive hazard, not as a hypothesis.

---

## 3. Instruments — lifted, SHA-gated, never re-implemented

| instrument | source | how used |
|:--|:--|:--|
| 12-feature matrix, LOOCV Ridge/RF, permutation null | `scripts/h_new_183_chronology_predictor.py` | imported as a SHA-verified module region for C2 |
| 29-feature matrix (BASE + EXPANSION) | `scripts/h_new_233_ensemble_predictor.py` | imported as a SHA-verified module region for C1 and C3 |
| Spearman, stratified permutation, quintile binning, partial ρ | `findings/phase-b-hypotheses/scripts/h-new-2770.py` | re-implemented identically and asserted equal on a fixed vector pair |

**C1 has no script.** Its frontmatter reads `executed_by: team-lead (inline, autonomous
loop)` and its Files section reads `Script: inline (seed 20260419)`. Its finding names only
**10** of its **15** features, and two of the ten — `divine_name_density`, `legal_density` —
are **not** in H-NEW-233's `BASE_FEATURES`, while the other eight are. **The exact
15-feature set is therefore not recoverable from the repository record.** This is registered
in advance as a reproducibility defect of C1 independent of any result. Two reconstructions
are locked, and both are reported:

- **RECON-A** = H-NEW-233's `BASE_FEATURES` verbatim (15 features: H-NEW-183's 12 +
  `verse_count`, `type_token_ratio`, `refrain_score`).
- **RECON-B** = RECON-A with `allah_density` → `divine_name_density` and
  `book_ref_density` → `legal_term_density`, so that all ten named features are present.

C1's reproduction gate is met if **either** reconstruction lands inside tolerance; the
verdict is then carried by that reconstruction, and both R² are published.

---

## 4. The arms

### A0 — reproduction gate (runs first, on every claim)
Recompute the published headline with the published seed 20260419 and published
hyper-parameters. **Tolerances, locked:**

| statistic | tolerance | reason |
|:--|:--|:--|
| Ridge LOOCV R² (deterministic) | \|Δ\| ≤ 0.03 | no stochasticity; only library drift |
| RF LOOCV R² (stochastic) | \|Δ\| ≤ 0.05 | seeded but sklearn-version-sensitive |
| Kruskal–Wallis H | \|Δ\| ≤ 1.0 **and** p within one order of magnitude | integer-count statistic |

**A0 failure does not stop the run.** The claim is labelled `DID-NOT-REPRODUCE`, reported
prominently, and its remaining arms are still executed and reported as descriptive.

### A1 — the size-only baseline (the decisive diagnostic)
Same model class, same LOOCV, same seed, **no vocabulary, no morphology, no phonology** —
size columns only:

- **S1** = the primary channel alone (one column).
- **S3** = `{log word count, verse count, mean verse length}` (three columns).

Report `R²_full`, `R²_S1`, `R²_S3`, and `ΔR² = R²_full − R²_S3`. For C4, the analogue is the
**per-word re-normalisation**, which is exact: a per-100-verse density divided by mean verse
length is the per-100-word density, requiring no new data.

### A2 — the size-matched permutation null
Permute the **target** within quintiles (k = 5) of the primary drift channel and recompute
the full model's LOOCV R² on each draw. Secondary arm at k = 10. For C4, permute the phase
label within MVL quintiles and recompute Kruskal–Wallis H.

**Permutation budgets and bars, locked** (chosen so each bar is resolvable at its budget):

| model | n_perm | bar |
|:--|--:|:--|
| Ridge (fast, deterministic) | 500 | p = (#{null ≥ obs} + 1)/501 < α_bon |
| RF (expensive) | 100 | observed **strictly above the maximum** of 100 draws ⇒ p ≤ 1/101 = 0.0099 < α_bon |
| Kruskal–Wallis (cheap) | 10000 | p = (#{null ≥ obs} + 1)/10001 < α_bon |

RF null draws use `n_estimators = 200` for **both** the observed and the null values inside
the A2 cell, so the comparison is internally consistent; the A0 gate separately uses the
published `n_estimators = 500`. Both RF R² are published.

### A3 — per-word re-normalisation of the density features
Every per-verse density feature is replaced by its exact per-word form
(`100 × count / n_words`, with `count = density × n_verses / 100`). Re-run A0's model.
Reports whether the predictor's power is carried by the densities or by their denominator.

### A4 — replication
Every arm re-run at seed 20260519. A claim whose classification differs between seeds is
labelled `SEED-FRAGILE` in front of its verdict.

---

## 5. LOCKED directions

| # | prediction | locked before the run |
|:-:|:--|:--|
| D1 | For C1 and C3 (mushaf), `R²_S3` ≥ 0.70 — size alone predicts mushaf position well | ρ = −0.9342 makes this near-arithmetic; if it fails, my channel measurement is wrong |
| D2 | For C2 (Nöldeke), `R²_S3` > the published length-only baseline of 0.446 | the published baseline used **one** column |
| D3 | For C4, the per-word effect is **smaller** than the per-verse effect (ε² falls) | every one of H-NEW-2770's eleven axes fell under re-normalisation, with no exceptions |
| D4 | For C5 (calibration), size alone explains the KL divergence | the finding says so itself; a miss here invalidates the harness, not the finding |

**If D1 or D4 fails, the harness is suspect and every verdict in this batch is void.** That
is the point of registering them.

---

## 6. LOCKED decision rules — diff the runner against this section before declaring anything

Bonferroni family = the five claims, k = 5, **α_bon = 0.05 / 5 = 0.01**, applied to A2.

**For the predictor claims (C1, C2, C3, C5):**

```
DID-NOT-REPRODUCE        A0 outside its tolerance in §4

DOES-NOT-SURVIVE         A2 p >= alpha_bon                                   [null not beaten]
                     OR  R2_S3 >= R2_full - 0.02                        [size alone suffices]

GENRE-SHARED-BUT-LARGER  A2 p < alpha_bon
                     AND 0.02 <= (R2_full - R2_S3) < 0.10

SURVIVES                 A2 p < alpha_bon
                     AND (R2_full - R2_S3) >= 0.10
```

**For the density claim (C4):**

```
DID-NOT-REPRODUCE        A0 outside its tolerance in §4

DOES-NOT-SURVIVE         p_MVL_stratified >= alpha_pub    [alpha_pub = 0.00833, its own bar]
                     OR  p_per_word >= alpha_pub

GENRE-SHARED-BUT-LARGER  both p < alpha_pub  AND  epsilon^2 falls by >= 50% per word

SURVIVES                 both p < alpha_pub  AND  epsilon^2 falls by <  50% per word
```

`GENRE-SHARED-BUT-LARGER` is the team's label; in this batch there is no genre arm, so it
carries its within-corpus sense exactly and only: **the effect is largely the denominator,
with a real but small residual above it.** The finding will say so in those words rather
than let the label imply a cross-genre comparison that was not run.

**Magnitude is reported unconditionally, for every claim, whatever the label** — `R²_full`,
`R²_S1`, `R²_S3`, `ΔR²`, the null mean, the null 95th percentile and maximum, and the
observed percentile. A binary verdict alone is forbidden: H-NEW-2680's most damaging result
was that baselines were *more* extreme than this corpus, which pass/fail would have hidden.

---

## 7. Nulls, seeds, corrections

- Seeds 20260509 primary, 20260519 replication. The published seed 20260419 is used **only**
  inside the A0 reproduction gate, because reproducing a published number requires its seed.
- α_bon = 0.01 across the five-claim family for A2. C4 additionally faces its own published
  bar of 0.00833, which is stricter; **the stricter of the two applies**, which is a
  tightening and therefore self-verifying.
- Permutation p is always `(#{null ≥ obs} + 1)/(n_perm + 1)`.
- Run directories are immutable and **never deleted**, including calibration and failed runs.
  The manifest records every input path **repository-relative**.

---

## 8. Frozen inputs (SHA-256, runtime-verified; mismatch ⇒ `SystemExit`)

| path (repo-relative) | SHA-256 |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `findings/phase-b-hypotheses/csv/h-new-123.json` | `33bbeec06c1187b1a96448ecf87720a4915a49a827cf110685d4d277aa449f46` |
| `findings/phase-b-hypotheses/csv/h-new-125.json` | `8b2f7f1cf217562dd34be75519c80d29ceaebcc40b2b0c6fbe95bebb5d0442e1` |
| `findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv` | `7778d07f620d68b3a3fefbf5903c0e9e30665e25b58fe1f766d7f08cf6a07594` |
| `findings/phase-b-hypotheses/csv/h-new-182-surah-vectors.csv` | `30571ef0ee37f32881033ca22fcb368cffbaaf986d040491ed4396b2cb2b8acc` |
| `findings/phase-b-hypotheses/csv/h-new-187-per-surah.csv` | `7eee6ba49222e3fcd989ca2521114503fd5dcb3f907de6f1d343950970ed32ec` |
| `findings/phase-b-hypotheses/csv/h-new-183.json` | `246af4b198c2c7d5d4e2edf86d5d1924c37a35f5d4e6a5292b0e12291787a16f` |
| `findings/phase-b-hypotheses/csv/h-new-233.json` | `28715441baab9bef58735acb8fa7b63bd58686844fed25ee0f162ccfe67236a0` |
| `scripts/h_new_183_chronology_predictor.py` | `a30666c03c8bbdc0fa618099497ebe6962306cf7c712d5abf1b7adbbd025db2b` |
| `scripts/h_new_233_ensemble_predictor.py` | `ad69720a10159c43094336fab9890671743b545fbcfef5c53db1bbcb3478edd7` |

---

## 9. Garden of forking paths — what was known at lock time

- **Known and recorded here:** the citation ranking of every candidate; the correction status
  of each; the six nuisance-channel correlations of §2; the published headlines of §1; the
  fact that C1 has no script and that its 15 features are not fully recoverable; and the fact
  that C2's "length-only baseline" is the **single column `log_length`**, read from
  `scripts/h_new_183_chronology_predictor.py:295`, which is `log(N)` with `N` the surah's
  **token count** from H-NEW-123's Heaps fit (Q1 → N = 29 for a 7-verse surah).
- **This last item contradicts the repository's own rule document.** `UNIT-DRIFT-DEFECT.md`
  §5 states that H-NEW-183 "ran a length baseline using **verse count only** (ρ = +0.390)".
  The source says word count (ρ = +0.6892). **This is recorded before the run**, will be
  verified by executing the published script rather than by reading it, and will be reported
  whichever way it comes out. If the source reading is right, the rule document's example is
  wrong on the channel while remaining right on the mechanism, and the correction belongs to
  the rule document's author, not to me.
- **Not computed at lock time:** every R², every ΔR², every null distribution, every
  stratified p, every ε², and every per-word value in this batch.
- **Verdict logic was written into §6 before the runner existed**, and the runner is diffed
  clause-by-clause against §6 before execution — the H-NEW-2600 lesson.

---

## 10. Honest limits, stated in advance

1. **Conditioning on size may remove mechanism, not only confound.** If the mushaf was
   *ordered by length*, then length is the organizing principle rather than a nuisance, and a
   size-matched null removes the very thing under study. **The classical tradition says
   exactly this** — the mushaf's ṭiwāl → mathānī → mufaṣṣal arrangement is a length
   arrangement, attested long before any of this. So for C1, C3 and C5 the stratified result
   is a **floor on what is left after length**, and a claim that falls is shown *unestablished
   as a compositional claim*, not shown false. This distinction is carried into the verdict
   language deliberately.
2. **LOOCV R² on n = 114 is optimistically biased**, equally in every arm, so ΔR² is safer
   than any single R². The published findings' own honest-limits sections say this too.
3. **A reconstruction is not the original.** C1's verdict rests on a rebuilt feature matrix
   and is reported as such, with both reconstructions' numbers.
4. **Nöldeke chronology is a scholarly reconstruction, not data.** Everything touching C2 and
   C4 inherits its uncertainty; nothing here tests it.
5. **No genre arm.** Nothing in this batch compares against al-Bukhārī, al-Jāḥiẓ or poetry.
   No verdict here may be read as a statement about what distinguishes this corpus from
   other Arabic.
6. **Five claims is not the inventory.** Whatever is not reached is named explicitly in the
   finding so the next session starts exactly there.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any effect under test was computed.
A rate is a ratio, and the divisor is part of the claim. Bismillāhi al-Raḥmāni al-Raḥīm.*
