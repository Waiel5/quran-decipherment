---
id: H-NEW-2910
title: "Pre-registration — extending the vocalised-prose control from two books to all nine, to settle H-NEW-2890's 0.00010 margin"
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any Δ, agreement or null draw was computed for the seven new books
family: RHYME-2026-08-07
frontier_item: F-16
parent: H-NEW-2890 (CONTROL PASSES, on a margin of 0.00010 under one reading of its locked threshold)
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 108
alpha_bonferroni: 0.00046296
---

# Pre-registration — H-NEW-2910

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2910.py`.**
The inclusion rule is locked in §3, the statistics in §4, **the re-verdict criterion for
H-NEW-2890 in §5**, and the decision rules in §6. The runner's verdict logic will be diffed
against §6 and printed before any verdict is declared.

---

## 1. Why this test exists

H-NEW-2890 returned **CONTROL PASSES** on a worst case of Δ = +0.03249. Under an alternative
reading of its own locked threshold — worst case over **both** pausal tuples rather than the
registered P1 — the worst case is **+0.04682** against a threshold of **+0.04672**. It
**exceeds by 0.00010**, and its `result.json` records
`verdict_under_that_reading: "PARTIAL"`.

**0.00010 of adjacent-pair agreement is about six ḥadīth pairs out of 6,579. A conclusion
resting on one ten-thousandth of one book-tuple-setting cell is not settled; it is lucky.**

The estimate rests on **two** books. H-NEW-2890's own census found **50,884 fully vocalised
ḥadīth across nine**, spanning ḥarakāt densities 0.7702–0.8829 around this corpus's 0.7801.
**Seven are unused.** Going from n = 2 to n = 9 replaces a knife-edge point estimate with a
distribution, which is what the margin question actually needs.

**A result that re-verdicts H-NEW-2890 to PARTIAL is a success of this test, not a failure.**

---

## 2. What is already known, and therefore not pre-registrable

H-NEW-2890 is published. Its al-Bukhārī and Muslim numbers are on the record and are
**re-computed** here, not predicted:

| quantity (Arm B, readable, R2) | published |
|:--|--:|
| Δ(P1): Bukhārī S5 / S3 / S0 | +0.0297 / +0.0318 / +0.0316 |
| Δ(P1): Muslim S5 / S3 / S0 | +0.0325 / +0.0324 / +0.0325 |
| Δ(P2): Bukhārī S5 / S3 / S0 | +0.0441 / +0.0460 / **+0.04682** |
| Δ(P2): Muslim S5 / S3 / S0 | +0.0454 / +0.0451 / +0.0452 |
| D-P3 arms clearing α_2890 | 3 of 12, all Muslim under P1 |
| this corpus | Δ(P1) = +0.1869, Δ(P2) = +0.1880, z = +15.03 |

**No Δ, agreement value or null draw has been computed for any of the seven new books.**
§8 lists everything that was inspected before locking.

---

## 3. Inclusion — the gate is inherited, and it excludes nobody

A book enters the primary distribution iff **all three** hold:

1. **Unit-final vocalisation ≥ 0.90** — inherited verbatim from H-NEW-2870 §6.4 via
   H-NEW-2890 §3.1. Not set here.
2. **≥ 500 readable adjacent within-chapter pairs.** Fixed against the project's own
   precedent: H-NEW-2870's poetry arm was reported on **234** pairs, so 500 is more than twice
   the smallest arm this project has published on.
3. **The pausal partition is a coarsening of the citation partition**, without which the
   exact null of H-NEW-2880 §5 is undefined (its §4.1 condition).

**Measured before locking (§8), and declared here so the gate can be seen to do no work:**

| book | unit-final voc. | readable pairs | coarsening | admitted |
|:--|--:|--:|:--|:--|
| al-Bukhārī | 0.9426 | 6,579 | yes | ✔ |
| Muslim | 0.9405 | 7,054 | yes | ✔ |
| Abū Dāwūd | 0.9505 | 4,950 | yes | ✔ |
| al-Tirmidhī | 0.9887 | 3,746 | yes | ✔ |
| al-Nasāʾī | 0.9511 | 5,482 | yes | ✔ |
| Ibn Mājah | 0.9484 | 4,172 | yes | ✔ |
| Mālik | 0.9457 | 1,764 | yes | ✔ |
| Aḥmad (partial) | 0.9512 | 1,364 | yes | ✔ |
| al-Dārimī | 0.9445 | 3,351 | yes | ✔ |

**All nine qualify. Every book is run and every book is reported**, so no book can be dropped
after seeing its Δ. Aḥmad is flagged in reporting as a partial work (its source is missing
chapters 8–30, and it has only 8 chapters on disk) but it is **not** excluded.

---

## 4. Method — H-NEW-2890's pipeline, unmodified

The runner loads `scripts/h-new-2890.py`
(SHA-256 `ac6f83465aa32b7a761f622f0010ed414329eb654bc60cb0bbed516e90edea73`), which itself
pins `scripts/h-new-2880.py`
(`c9577870b2a4bc3451344031f46f192795534af0ef56f4f46be57f07db7c7074`). Both are SHA-256
verified at runtime. **No parameter of the instrument, the null, or the statistic is changed.**

- **Arm B (composed boundaries), the primary**: unit = one ḥadīth, block = one chapter,
  adjacent within-chapter pairs, readable-pairs restriction; rime **R2**.
- **Statistic**: Δ = A(P) − A(C), and E = A − Σpᵢ² against the exact zero-variance-floor null.
- **Every cell**: 9 books × 3 stripping settings {S5, S3, S0} × 2 tuples {P1, P2} × 2 seeds.
- **Arm A (length-matched cuts)** is run per book and setting and reported, against the locked
  comparison target — this corpus's own re-cut Δ = **+0.0284**.

**Execution note, declared because it must not be mistaken for a method change:** the 108
exact-null arms are run **in parallel across processes**. Each arm constructs its own
`random.Random(seed)` and is fully self-contained, so results are **bit-identical** to serial
execution and independent of scheduling order. This is a speed change only.

**Checkpoints are written PER ARM, not per stage** — a defect identified in H-NEW-2890's own
runner, where the entire 22-minute exact-null stage wrote nothing and was externally
indistinguishable from a hang. Checkpoints go **outside** the run directory, write-once.

---

## 5. The re-verdict criterion for H-NEW-2890 — LOCKED BEFORE ANY Δ

Let the **cell set** be the 9 books × 3 settings × 2 tuples = **54** values of Δ(Arm B,
readable, R2) at the primary seed. Let **T = +0.04672**, H-NEW-2890's quarter threshold, and
let **f** be the fraction of the 54 cells with Δ ≥ T.

| outcome | verdict on H-NEW-2890 |
|:--|:--|
| **f < 0.10** | **2890 ROBUST.** Its +0.04682 cell is an extreme of the prose distribution and the margin was an unlucky draw. Its CONTROL PASSES stands as published |
| **0.10 ≤ f < 0.25** | **BORDERLINE.** 2890's verdict stands but its §7.1 disclosure must be strengthened to say the margin is not settled |
| **f ≥ 0.25** | **2890 RE-VERDICTED TO PARTIAL.** An amendment notice is written into H-NEW-2890 and the re-verdict is reported at full prominence |

**And a second, independent trigger, because f alone can hide the answer to the actual
question:**

> **Where does al-Bukhārī S0 P2 (+0.04682) sit in the 54-cell distribution?**
> **≥ 90th percentile → it is an outlier**, consistent with ROBUST.
> **≤ 75th percentile → it is a typical prose value**, and the finding is **at least
> BORDERLINE regardless of f**, because a threshold that a typical book-cell crosses is not a
> threshold the parent's verdict can rest on.

Both triggers are evaluated and the **stricter** outcome is taken.

---

## 6. Decision rules and reporting

**Registered inference family — 108 tests:** {D-P1, D-P3} × 9 books × 3 settings × 2 tuples.
**Bonferroni k = 108, α = 0.05/108 = 0.00046296**, one-sided in the locked direction.
Resolution 1/10,001 = 0.0001 < α ✔.

- **D-P1** — Δ_thisCorpus > Δ_prose, by 10,000-permutation label exchange. Locked direction.
- **D-P3** — prose E against **its own** exact null. **Reported at this finding's α AND at
  H-NEW-2890's α = 0.00138889**, so the arm counts are comparable across the two findings.

**Locked question on D-P3, whose answer changes how 2890's failure is read:** 2890 found 3 of
12 arms clearing α, all Ṣaḥīḥ Muslim under P1. **Is that a Muslim-specific property of its
isnād style, or a general feature of vocalised ḥadīth?** If failures appear in a minority of
books it is book-specific; **if the majority of books show clearing arms, it is a general
property of the genre and H-NEW-2890 §6.1's reading must be amended to say so.** Threshold
locked at **> 50 % of books showing at least one clearing arm = general**.

**Reporting order (locked):** the nine-book census → the Δ distribution with its mean, spread
and full per-book table → this corpus's position relative to it → the direct answer on
al-Bukhārī S0 P2 → D-P3 across books → the verdict against §5.

---

## 7. Failure conditions

- **A book fails §3** → excluded, and its failing number stated; it is not quietly dropped.
- **Any exact-null arm loses floor exactness** (deviation ≠ 0) or exceeds a 1 % redraw rate →
  that arm is defective and reports no p-value, per H-NEW-2880 §6 G1.
- **f ≥ 0.25, or Bukhārī S0 P2 at or below the 75th percentile** → H-NEW-2890 is amended, and
  that leads the write-up.
- **Residual limits inherited and not removable here:** ḥadīth is one register, not Arabic
  prose in general; a ḥadīth is not a verse and Arm B compares composed boundaries across two
  genres of different unit length; the upstream licence position is unstated; Musnad Aḥmad is
  partial.
- **A limit specific to this test:** nine books of one genre by nine compilers are **not** nine
  independent samples of Classical Arabic prose. They share a register, a transmission
  vocabulary and a large stock of shared matn. **The spread reported here is a spread across
  ḥadīth collections, and it must not be described as a spread across Arabic prose.**

---

## 8. Garden of forking paths

1. Read H-NEW-2890, its pre-registration, its runner and `result.json`; H-NEW-2880;
   `findings/ABSENCE-CLAIMS.md`.
2. **All of H-NEW-2890's published values for al-Bukhārī and Muslim are known to me** (§2),
   including the +0.04682 cell that motivates this test. **No value for any of the seven new
   books is known.**
3. **Pre-lock census of all nine books** (§3): units, chapters, ḥarakāt density, unit-final
   vocalisation, within-chapter adjacent pairs, readable pairs, units surviving each stripping
   setting, and the coarsening check. Readability is measured on the **input**, per H-NEW-2870
   REPAIR-2. **No agreement, Δ or null draw was computed for any new book.**
4. The §3 gate and the §5 thresholds were fixed **after** that census and **before** any Δ. The
   vocalisation gate is inherited; the 500-pair floor is set against the project's own
   published 234-pair precedent; T = +0.04672 is H-NEW-2890's own published threshold; the
   0.10 / 0.25 and 90th / 75th percentile lines are round values chosen for interpretability,
   not tuned to anything measured.

---

## 9. Run discipline

Immutable run directory `runs/h-new-2910/<UTC>/`, `os.makedirs(..., exist_ok=False)`, outputs
opened with mode `'x'`, manifest paths repo-relative, **per-arm checkpoints written OUTSIDE the
run directory**, write-once. **No run directory is ever deleted.** This pre-registration's
SHA-256 is embedded as a literal in the runner and verified at runtime. Every permutation test
is replicated at seed 20260519. **The finding is drafted outside `findings/` and moved to its
final path only once the run directory exists and the file is complete** — the rule H-NEW-2890
broke.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
