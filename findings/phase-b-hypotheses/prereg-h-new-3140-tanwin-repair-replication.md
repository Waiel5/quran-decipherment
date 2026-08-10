---
id: H-NEW-3140
title: Pre-registration — the tanwīn-repair replication of H-NEW-2690 / H-NEW-2730's scanner
date: 2026-08-09
author: Waiel Al-Shujaa
type: INSTRUMENT-REPAIR REPLICATION — not a new hypothesis
status: LOCKED — written and SHA-256'd BEFORE any repaired value was computed
repairs: H-NEW-2690 (scanner), H-NEW-2730 (inherits the same scanner verbatim)
defect_source: h-new-2870-pausal-rhyme.md §1.1, raised 2026-08-07, undischarged
repair_source: scripts/h-new-2990.py line 146 (TANWIN_REMAP), from prereg-h-new-2870 §4.1
seed: 20260509
seed_replication: 20260519
n_perm: 10000
frontier_item: F-2 (retired as answered; this is the residual instrument repair)
---

# Pre-registration — H-NEW-3140

**This registers a DECISION RULE, not a hypothesis.** The hypotheses were registered in
`prereg-h-new-2690-quantitative-scansion.md` and are not restated, reopened or amended here.
What is locked below is the rule for classifying what the repair does to the published
conclusions — fixed before any repaired number exists, so the comparison cannot be
rationalised after the fact.

**The pre-registration of H-NEW-2690 is NOT edited by this document.**

---

## 0. THE HEADLINE CAVEAT, STATED BEFORE THE METHOD

**This replication CANNOT rescue H-NEW-2730's central claim, and it is not an attempt to.**

H-NEW-2730 withdrew H1b (*prose is less metrical than the Qurʾān*) on two arms that are
**invariant to any uniform change of the phonemiser**:

- **D8, the self-recut** — the Qurʾān's own word stream, re-cut to ḥadīth sentence lengths,
  moves 99.4 % of the way to ḥadīth's `d_min`. Both sides of that comparison are the *same
  corpus under the same phonemiser*. Lengthen every Qurʾānic syllable string and both sides
  move together.
- **D5, the matched-length bin** — Qurʾān and prose have identical medians (0.21739) at
  matched syllable length.

A length-driven artefact does not stop being length-driven because the syllable weights
underneath it changed. **If this run returns "conclusion unchanged" on D8, that is the
expected result and must not be reported as a vindication of H1b.** H1b stays withdrawn
regardless of what follows.

**What the repair CAN legitimately change is H1a — the one surviving result of the family.**
See §2.

---

## 1. The defect, measured before this document was written

`scripts/h-new-2690.py` line 89 places three codepoints in its `DROP` set. In the Uthmānī
orthography these are **not** what their Unicode names say; they are tanwīn. The mapping is
inherited from `prereg-h-new-2870-pausal-rhyme.md` §4.1, where it was verified against Tanzil
Uthmani v1.1 on 2,534 tanwīn-bearing words with **zero mismatches**.

| codepoint | Unicode name | actual function | count in corpus |
|:--|:--|:--|--:|
| U+0656 | ARABIC SUBSCRIPT ALEF | **tanwīn kasr** | 1,935 |
| U+0657 | ARABIC INVERTED DAMMA | **tanwīn fatḥ** | 2,901 |
| U+065E | ARABIC FATHA WITH TWO DOTS | **tanwīn ḍamm** | 1,807 |
| | | **total deleted** | **6,643** |
| U+064B/C/D | classic tanwīn | tanwīn | **1,911 retained** |

**Deleted share = 6,643 / 8,554 = 0.7766.** All figures counted directly from
`quran-text/quran-full-tashkeel.json` before this file was written.

### 1.1 The defect is Qurʾān-SPECIFIC — every comparison arm is unaffected

Counted directly, before locking:

| arm | affected codepoints | classic tanwīn |
|:--|--:|--:|
| **Qurʾān** (`quran-full-tashkeel.json`) | **6,643** | 1,911 |
| muʿallaqa Imruʾ al-Qays | **0** | 109 |
| muʿallaqa Zuhayr | **0** | 86 |
| muʿallaqa ʿAmr b. Kulthūm | **0** | 114 |
| Sunan al-Dārimī | **0** | 15,798 |
| Ṣaḥīḥ al-Bukhārī | **0** | 46,606 |

**This is the fact that makes the repair worth running.** The Qurʾān lost 77.66 % of its
nunation; every corpus it was compared against lost none. **Every comparison in the family
was therefore asymmetric**, and the asymmetry ran in one direction only.

### 1.2 Why the positive control could not detect it

The muʿallaqāt contain **zero** occurrences of the affected codepoints. The pre-registered
hard gate — 3/3 poems, 0.7708 per-bayt accuracy — was **structurally incapable** of failing
on this axis. The general form, which this run does not test but records:

> **A positive control validates an instrument only on the encoding features the control
> corpus exercises.**

---

## 2. The repair, and the locked directional prediction

**The repair.** One function is changed. `normalize()` gains a single line applied **before**
the `DROP` filter:

```python
t = "".join(TANWIN_REMAP.get(c, c) for c in t)
TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}   # U+0657, U+065E, U+0656
```

Lifted verbatim from `scripts/h-new-2990.py` line 146. **Nothing else in the scanner, the
meter table, the corpora, the seeds or the statistics is altered.** Both the defective and
the repaired phonemiser are run **in the same process on the same inputs**, so the comparison
is internally controlled and carries no cross-run drift.

**Locked directional prediction P1.** Restoring a tanwīn adds a `V` and a `C(n)` to the
phoneme string, so Qurʾānic syllable strings get **longer**. H-NEW-2730 §6.1 measured
`d_min` rising with length at r = +0.551 within the Qurʾān (R² = 0.304). Therefore:

> **P1: repaired median `d_min`(Qurʾān) > 0.22222 (the defective value) under P_forceheavy.**

**Locked directional prediction P2.** Poetry and prose are unaffected (§1.1), so their values
must not move at all. If the Qurʾān rises and poetry does not, the Qurʾān−poetry gap
**widens** and **H1a strengthens**:

> **P2: the repaired H1a difference exceeds the defective +0.07937.**

**The competing mechanism is stated, not hidden.** A restored word-final `-Vn` supplies a
regular `CVC` coda, which could make strings *more* template-conformant and push `d_min`
**down**, narrowing the gap and threatening H1a. P1/P2 back the length mechanism because it
is the one with a measured coefficient in this corpus. **P1 and P2 are falsifiable and may
both be wrong; the outcome is reported either way.**

---

## 3. Falsifiable self-checks on my own defect analysis

These test §1, not the finding. **A failure here means my analysis is wrong**, and the run
reports that with equal prominence.

- **S1 — poetry must be BIT-IDENTICAL** to the 2026-08-07 run: median `d_min` 0.14286,
  positive control 3/3 poems, per-bayt accuracy 0.7708. Any movement falsifies "the
  muʿallaqāt carry zero affected codepoints".
- **S2 — prose must be BIT-IDENTICAL**: Dārimī median `d_min` 0.23963.
- **S3 — the Qurʾān MUST move.** If repaired = defective for the Qurʾān, the `DROP`-set
  reading is wrong and §1 is retracted.
- **S4 — the defective arm must reproduce the 2026-08-07 published values exactly**
  (Qurʾān 0.22222, poetry 0.14286, Dārimī 0.23963, noise floors 0.23913/0.22222). This is
  the gate that proves the lift is faithful; **if S4 fails the run is void** and no repaired
  number is reported.

---

## 4. TARGETS — locked before running

| id | quantity | source of the published value |
|:--|:--|:--|
| **T1** | **H1a** — Qurʾān vs poetry: direction + permutation p | 2690 `H1a_quran_gt_poetry` |
| T2 | positive control — per-poem correct, per-bayt accuracy | 2690 `positive_control` |
| T3 | H1b — prose vs Qurʾān (already withdrawn; completeness only) | 2690 `H1b_prose_gt_quran` |
| T4 | H3a — `diff_B_minus_A`, direction + p | 2690 `H3.direction_ok` |
| T5 | H3b — `modal_meter_A` | 2690 `H3.modal_meter_A` |
| T6 | paired excess over matched noise — median excess, win-rate | 2730 D6 |
| T7 | D8 self-recut — % distance moved toward ḥadīth lengths | 2730 D8 |
| T8 | metre-specificity excess ratio (Qurʾān vs own noise) | 2690-POSTHOC D2 |

**T1 is PRIMARY.** It is the only surviving result in the family and the only one the repair
can legitimately overturn.

---

## 5. THE DECISION RULE — locked, and this is the object of this pre-registration

Every target is classified into **exactly one** of three labels.

### 5.1 CONCLUSION-CHANGED — fires if ANY of:

- **(a)** a locked direction reverses sign — H1a, H1b, or H3a; or
- **(b)** a permutation p crosses its α — 0.016667 for H1/H3 (2690 §6, k = 3); or
- **(c)** the positive-control gate fails — per-poem correct < 3, or per-bayt accuracy
  < 0.50; or
- **(d)** T7's self-recut distance-moved falls **below 80 %** (from 99.4 %); or
- **(e)** T6's win-rate crosses 50 % such that D6's reported sign flips; or
- **(f)** T5's `modal_meter_A` becomes **rajaz or sarīʿ** — which would retrospectively
  satisfy H-NEW-2690's H3(b) clause.

### 5.2 NUMBERS-CHANGED-CONCLUSION-UNCHANGED

None of (a)–(f) fires, **and** any headline median moves by **|Δ| > 0.005**.

*Justification of the tolerance:* `d_min` medians are ratios of small integers with an
irregular grain of roughly 0.01 (e.g. 0.22222 = 2/9, 0.21739 = 5/23). 0.005 sits below one
grain step, so this label fires on any genuine shift and not on floating-point noise.

### 5.3 UNCHANGED

None of (a)–(f), and every headline median moves by **|Δ| ≤ 0.005**.

### 5.4 Overall label

**The worst label across all eight targets**, in the order
`CONCLUSION-CHANGED > NUMBERS-CHANGED-CONCLUSION-UNCHANGED > UNCHANGED`.

**Reported per-target as the primary object**, so a reader can apply any aggregation.

### 5.5 What each overall label licenses — stated now, so it cannot be chosen later

- **UNCHANGED** → the defect is real but inert on these statistics. H-NEW-2690/2730's
  published numbers stand as computed. **This does NOT un-withdraw H1b** (§0).
- **NUMBERS-CHANGED-CONCLUSION-UNCHANGED** → every published *conclusion* stands, but the
  published *values* are superseded by the repaired ones and should be re-quoted. **This
  does NOT un-withdraw H1b** (§0).
- **CONCLUSION-CHANGED** → the affected result is withdrawn or restated. If T1 fires,
  **H1a — the family's one surviving result — is withdrawn**, and the correct summary of the
  entire scansion family becomes *nothing survives*.

---

## 6. Scope — declared before running, with reasons

**IN:** the full H-NEW-2690 registered statistic set (H1a, H1b, H2, H3, positive control,
matched-noise floors), plus 2730's **D6** and **D8**, plus the post-hoc **D1/D2**, each
computed under **both** phonemisers in one process.

**OUT, and why:**

1. **H-NEW-2730's D1 matched-partition arm** (200 offsets × 2 prose corpora × 500 units).
   It is the expensive arm — 2730's full run took 1,074 s — it is **not** the arm 2730 leads
   with, and 2730 §10.2 states the partition caveat cuts *against* its own conclusion. D8 and
   D6, the two arms that score **no baseline partition**, are in scope and are what the parent
   leads with.
2. **D5's decile bins.** Same reason; D5 rests on a single usable bin by 2730's own §10.9.
3. **T7 runs 60 re-cut draws, not 2730's 200.** Declared as a deliberate coarsening. The
   question here is whether the repair moves D8 across the 80 % bar, not to re-estimate D8
   precisely. **This is a deciding parameter and is named as one.**

**Deciding parameters declared:** the 0.005 tolerance (§5.2), the 80 % D8 bar (§5.1d), the
60-draw D8 coarsening (§6.3), `P_forceheavy` as the primary tuple (inherited from 2690).

---

## 7. Nulls, seeds, immutability

- Permutation null: arm-label shuffle, **10,000 perms, seed 20260509**, replication
  **20260519** — inherited verbatim from 2690 §7.
- Run directory `findings/phase-b-hypotheses/runs/h-new-3140/<UTC>/`, created with
  `os.makedirs(..., exist_ok=False)`; every file opened with mode `'x'`.
- **The H-NEW-2690 and H-NEW-2730 run directories are never touched, and no run directory is
  ever deleted.**
- This pre-registration's SHA-256 is embedded in `scripts/h-new-3140.py` as
  `EXPECTED_PREREG_SHA` and verified at runtime; mismatch = `SystemExit`.
- Every frozen input SHA from 2690's `FROZEN` map is re-verified at runtime.

---

## 8. Garden of forking paths

- **Known at lock time:** the three codepoints and their counts (§1); the zero-counts for all
  five comparison corpora (§1.1); the repair's source line in `h-new-2990.py`; every published
  value in T1–T8, all of which are already in the record and are the comparison baseline.
- **Not known at lock time:** any repaired value whatsoever. No repaired phonemiser had been
  run against any corpus before this file was written and hashed.
- **The directional predictions P1/P2 are locked and justified from a measured coefficient**
  (2730 §6.1, r = +0.551 within the Qurʾān), not from the frontier map's prior line, which
  §CALIBRATION of that map scores at 1-for-7 and which this lane is barred from citing.
- **The expected outcome is stated:** I expect NUMBERS-CHANGED-CONCLUSION-UNCHANGED, with
  H1a strengthening. **The result that would most change the record is T1 firing
  CONCLUSION-CHANGED**, and if it does, the finding is that the scansion family has no
  survivors.
- **The verdict function will be diffed against §5 clause by clause before the run**, and the
  diff recorded in the finding.

---

*Locked 2026-08-09 by Waiel Al-Shujaa, before any repaired value existed.*
