---
id: H-NEW-2760
title: Pre-registration — the muqaṭṭaʿāt book-reference law under a null matched to opening-window size and revelation phase, with a matched-partition genre control
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
status: PRE-REGISTERED — locked before any null was computed
target_claim: H-NEW-53 / cross-finding-008 / Pillar 1 (H-NEW-2680 L1)
seed: 20260509
seed_replication: 20260519
n_perm: 10000
tests_in_family: 6
alpha_bonferroni: 0.00833333
raw_p_gate: 0.00083333
rules_tuple: "(no-tashkeel, orthographic-token, whitespace words, opening window = verses 1-3, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# Pre-registration — H-NEW-2760

**Nothing in this file may be changed after the SHA-256 below is computed. The SHA is
embedded as a literal in `scripts/h-new-2760.py` and verified at runtime with a
`SystemExit` on mismatch.**

---

## 1. Why this claim and not another

Three claims in this repository carry more raw citations than the one tested here
(H-NEW-720 at 314, H-NEW-750 at 271, H-NEW-590 at 264, against H-NEW-53's 48 and
cross-finding-008's 192). **All three of those feed structures that were corrected on
2026-08-07 and no longer carry an inference.** H-NEW-720 decomposes the residual of the
Fisher-Rao geodesic, whose optimality reading was withdrawn
(`findings/PILLAR-LAW-CORRECTION-2026-08-07.md`). H-NEW-750 and H-NEW-590 are two of the
three inputs to UAS, which H-NEW-2720 G8 ruled `NOT-A-DISCRIMINATION-CLAIM`. Putting a null
under a statistic whose parent inference is already retracted is lower-value work.

**The muqaṭṭaʿāt book-reference law is the only standing claim that neither baseline
satisfies** (H-NEW-2680 §7: al-Bukhārī 2/4, pre-Islamic poetry 3/4, and L1 is the sole law
failing for both). It is Pillar 1. `STATE-OF-THE-PROJECT-2026-08-07.md` §1.1 lists it first
among the four survivors. If it falls, the project has no discriminating law left; if it
survives a properly matched null, it is the first claim here to have done so. Either
outcome is worth more than a null under a retracted statistic.

## 2. The claim under test, stated exactly as published

> **24 of 29 muqaṭṭaʿāt-opened surahs (82.8 %) reference *kitāb* (Book) or *qurʾān* within
> their first 3 verses. Only 10 of 85 non-muqaṭṭaʿāt-opened surahs (11.8 %) do.**
> **Hypergeometric P(X ≥ 24 | n = 29, K = 34, N = 114) = 3.17 × 10⁻¹².**

`findings/phase-b-hypotheses/h-new-53-muqattaat-book-reference.md:17,19,110`.
Transported to the pillar conjunction as L1 at
`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` §7, where the repaired
marker-class search returns p_bonf = 4.7 × 10⁻¹³ on this corpus and nothing on either
baseline.

## 3. The defect

**Defect (b) — the null does not match the nuisance parameter driving the statistic.**
This is H-NEW-740's defect, not Pillar 4's: the claim *has* a null, and the null is wrong.

The hypergeometric draws 29 surahs **uniformly at random from 114** and asks how many are
book-referencing. That null is correct only if muqaṭṭaʿāt surahs are exchangeable with the
other 85 on every dimension that affects the outcome. **They are not, and this project
established that itself:**

- `h-new-46-muqattaat-vs-surah-length.md:3` — **STRONG-PASS on all 4 length-axes**:
  muqaṭṭaʿāt-opened surahs concentrate in LONG surahs.
- `h-new-46-1-chronology-disentangle.md` — STRONG-PASS 6/7 separating length from
  chronology; muqaṭṭaʿāt surahs are chronologically clustered.
- `cross-finding-012-late-meccan-scripture-announcement.md` — scripture-announcement
  vocabulary is a Late-Meccan apparatus.

H-NEW-53 has **no honest-limits section at all**, is self-declared post-hoc-noticed
(`:22-37`), and nowhere mentions surah length. The repaired 2680 transport is
Bonferroni-corrected over 721 hypergeometric evaluations — still exchangeable-surah at
its core.

## 4. The nuisance parameters, named before anything is designed

Written down before the null was built, per the lesson of H-NEW-740 and H-NEW-2720 §2.3
(unit size alone explains 91.5 % of the compression tail and half the anti-twin).

**What could produce a high opening book-reference rate among muqaṭṭaʿāt surahs other
than an engineered marker system:**

| # | nuisance | mechanism | how it is held fixed |
|---|---|---|---|
| **N1** | **opening-window token budget** — the number of words in verses 1-3 | A substring search over a longer window has more chances to hit. This is the literal denominator of the instrument. | stratified permutation on binned opening-window word count |
| **N2** | **revelation phase** | Scripture-announcement vocabulary is a Late-Meccan register (cross-finding-012). Muqaṭṭaʿāt surahs are chronologically clustered. | stratified permutation on Nöldeke phase, crossed with N1 |
| **N3** | **the surah's own base rate of the target vocabulary** | A surah whose body is about *kitāb* throughout will mention it early by chance alone. Presence ≠ front-loading. | a within-surah positional null that conditions on the surah's own token set |
| **N4** | **whole-surah length** | Correlated with N1 but not identical; enters through register rather than through window size. | reported as a covariate; N1 is the sharper control and is the one locked |

N1 is the primary nuisance. N3 generates the sharpest test in the family (H5), because it
is completely length-free by construction.

## 5. Instrument — frozen, and NOT re-designed

The detector is taken **verbatim** from `scripts/h-new-2680b.py` (the script whose L1
transport carries the surviving pillar), not reimplemented:

- `AR_DIAC`, `NON_AR`, `normalise_words`, `cut_to_profile`, and the `NARROW` regex pair.
- Opening window = verses 1-3 (`min(3, NV[sid])`), matching both H-NEW-53 and 2680b.
- Muqaṭṭaʿāt set = the canonical 29 surahs
  {2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}.

**Disclosed instrument divergence, found during reproduction and recorded here before
locking:** under the 2680b `NARROW` patterns the non-muqaṭṭaʿāt count is **11 of 85**, not
H-NEW-53's 10 of 85, so K = 35 rather than 34. The muqaṭṭaʿāt count reproduces **exactly
at 24 of 29**. This test locks on the **2680b instrument**, because that is the instrument
the pillar-conjunction control actually ran. Both K values are reported.

## 6. What was computed before this file was locked

Garden-of-forking-paths log. Exactly three things:

1. The observed counts under the 2680b instrument (24/29, 11/85) — already-published
   quantities, recomputed to confirm the rebuild.
2. The median opening-window word count by group: **muqaṭṭaʿāt 19, non-muqaṭṭaʿāt 13**.
   This confirms N1 is live; it was already implied by H-NEW-46 and is not a null result.
3. File availability for the strata and the three baseline corpora.

**No null distribution, no permutation, no p-value, and no baseline statistic of any kind
was computed before this SHA was taken.**

## 7. The six registered inferences, with directions locked

Bonferroni k = 6, α_bon = 0.05/6 = 0.00833333. The project novelty rule is stricter
(corrected p < 0.005), so the **raw decision gate is p < 0.00083333**. 10,000 permutations
per null gives a p floor of 9.999 × 10⁻⁵, below the gate. Seed 20260509, replication
20260519.

| # | inference | statistic | **locked direction** | gate |
|---|---|---|---|---|
| **H1** | reproduction | observed muqaṭṭaʿāt hit count | **exactly 24 of 29** | exact match, no p |
| **H2** | the nuisance is real | Spearman ρ(opening-window words, hit) over all 114 | **ρ > 0** | raw p < 0.00083333 |
| **H3** | **primary** — survives N1 | hit count under opening-window-size-stratified label permutation (Null B) | **observed > null mean** | raw p < 0.00083333 |
| **H4** | survives N1 × N2 | hit count under size × phase stratified permutation (Null C) | **observed > null mean** | raw p < 0.00083333 |
| **H5** | front-loading, length-free | among surahs with ≥ 1 target token, mean normalised position of the FIRST target token | **muqaṭṭaʿāt earlier than non-muqaṭṭaʿāt** | raw p < 0.00083333 |
| **G1** | genre control | Spearman ρ(opening-window words, hit) in each of 3 matched partitions | **ρ > 0 in the baselines** — i.e. size-dependence is a general property of Arabic prose/verse, not special to this corpus | raw p < 0.00083333 |

**H3 is the primary.** If H3 fails, the law does not survive its nuisance parameter and
that is the headline, whatever H4 and H5 do.

### 7.1 Null definitions, fixed

- **Null A (published).** Uniform hypergeometric, N = 114, n = 29. Reproduced for
  comparison only; it is the null under audit and cannot license anything.
- **Null B (N1-matched).** Bin the 114 surahs by opening-window word count into **quintiles
  of the 114-surah distribution**. Permute the muqaṭṭaʿāt label **within** each bin, so
  every draw takes exactly as many surahs from each opening-window-size stratum as the real
  muqaṭṭaʿāt set does. The opening-window size profile is therefore **identical by
  construction**, which is precisely what H-NEW-740 failed to do.
- **Null C (N1 × N2-matched).** Same, with strata = opening-window tertile × Nöldeke phase
  (Early Meccan / Middle Meccan / Late Meccan / Medinan) from `data/revelation-order.csv`.
  Tertiles rather than quintiles because crossing with 4 phases would otherwise leave
  strata too thin to permute. **Any stratum containing 0 or all muqaṭṭaʿāt surahs
  contributes no variance and is reported as such** — this is a power limit, not a pass.
- **Null D (N3-matched, for H5).** For each surah holding ≥ 1 target token, permute the
  positions of that surah's own verses and recompute the first-target-token position. This
  conditions on the surah's own vocabulary and length simultaneously.

### 7.2 The genre control — transport, and its declared limit

The matched partition is built with `cut_to_profile` **imported in substance from
`scripts/h-new-2680b.py`**: cut each baseline word stream into 6,236 units matching this
corpus's verse word-length profile in order, then group into 114 pseudo-surahs on the
canonical verse-count profile. Corpora: al-Bukhārī, al-Jāḥiẓ *Kitāb al-Ḥayawān*, and the
14-file pre-Islamic poetry corpus (the same file list and SHA as `h-new-2720.py`).

**What the control can and cannot resolve, stated in advance.** H-NEW-2680 §7 already
established that only **6** Bukhārī and **1** poetry pseudo-surah mention the target
vocabulary in their opening units. A floor that low makes the baseline **uninformative
about marker engineering** — there is nothing there to mark. **The control is therefore
transported to the NUISANCE, not to the marker**: G1 asks whether opening-window size
predicts opening self-reference *in the baselines*, which is answerable at any base rate
and which tells us whether N1 is a general property of Arabic text. A "the baselines have
no markers" result is **not** counted as evidence for the law; it is already known and
already caveated.

**Honest limit for this claim specifically.** A partition is not a composed book. The
statistic here is **boundary-sensitive** — it depends on where unit 1 begins — and per
`STATE-OF-THE-PROJECT-2026-08-07.md` §4.7 arbitrary cuts *destroy* real boundaries, so a
baseline *pass* would be strong evidence against the law while a baseline *failure* is
weak evidence for it. This asymmetry is why the weight of this test sits on H3 and H5,
which use **no baseline at all**.

## 8. Decision rule — the literal text the runner must implement

Diff this section against the script's verdict logic before declaring anything
(the H-NEW-2600 lesson).

```
DISCRIMINATES
    H1 exact AND H3 passes its gate AND H5 passes its gate
    AND the observed hit count lies outside the Null B 95% band.

GENRE-SHARED-BUT-LARGER
    H3 passes its gate but the Null B effect size is a rate ratio < 2.0,
    OR H3 passes while H5 fails — i.e. a real but reduced residual, with the
    front-loading component unsupported.

DOES-NOT-DISCRIMINATE
    H3 fails its gate.

Any arm whose observed direction is opposite to the locked direction is published as a
PRE-COMMIT VIOLATION with full prominence and is NOT rescued by any other arm.
H2 or G1 failing does not rescue H3; it reclassifies the nuisance, and that is reported
separately.
```

**No arm may be rescued by another. H3 is primary and its failure is the verdict.**

## 9. Failure conditions

- H1 not exact → the rebuild is wrong; report the discrepancy and stop.
- H3 raw p ≥ 0.00083333 → `DOES-NOT-DISCRIMINATE`. Not massaged, not re-binned, not
  re-nulled.
- Observed < null mean on H3, H4 or H5 → pre-commit violation, published as such.
- Any stratum degeneracy in Null C is reported as a power limit and Null C is **not**
  used to rescue a failing Null B.

## 10. Outputs

- `scripts/h-new-2760.py` with this file's SHA-256 embedded as a literal.
- Immutable run directory `runs/h-new-2760/<UTC>/` with `result.json` and `manifest.json`.
  **Manifest paths are repository-relative.** **The run directory is never deleted.**
- `csv/h-new-2760.json`, `h-new-2760-muqattaat-book-reference-nuisance.md`.

*Locked by Waiel Al-Shujaa, 2026-08-07, before any null was computed.
Bismillāhi al-Raḥmāni al-Raḥīm.*
