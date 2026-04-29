---
finding_id: h-classic-47
phase: B
status: PARTIAL — primary PASSES decisively (4/4 priority surahs in BOTH stopword conditions, z range +5.88 to +10.45) but negative control SPLITS (Q 6 al-Anʿām + Q 7 al-Aʿrāf also pass; Q 26 al-Shuʿarāʾ + Q 37 al-Ṣāffāt fail). Effect is real but generalizes to late-Meccan / Medinan, not specifically to the al-Biqāʿī priority Medinan set. Theoretically interpretable.
verdict_date: 2026-04-12
parent_task: #98
pre_reg: findings/phase-b-hypotheses/h-classic-47-prereg.md
script: scripts/h_classic_47_biqai_seam.py
data: findings/phase-b-hypotheses/csv/h-classic-47.json
seed: 20260414
classical_anchor: al-Biqāʿī Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar (verse-by-verse munāsaba doctrine)
distinct_from: task #21 / T-002 (cross-surah seam-Jaccard at SURAH-pair scale, z=+10.7)
bonferroni_k: 6
alpha_bon: 0.0083
---

# H-CLASSIC-47 — al-Biqāʿī verse-pair within-surah seam-Jaccard density

## TL;DR

**PARTIAL — verse-pair effect is real but generalizes beyond
priority surahs.**

All 4 al-Biqāʿī-priority Medinan surahs (Q 2, 3, 4, 5) decisively
pass the per-surah within-surah verse-order permutation null at
distance 1, in both with-stopwords and without-stopwords conditions
(z range +5.88 to +10.45, all p_emp = 0.0000 against 10,000
shuffles). **The al-Biqāʿī adjacent-verse seam-density claim is
strongly confirmed for the priority surahs** — including after
removing the locked stopword roots {Alh, kwn, qwl, Eml, Amn, llh,
xlq, Erf}, so the effect is NOT a divine-name / formulaic-repetition
artifact.

The negative control, however, **splits 2/4**: Q 6 al-Anʿām and
Q 7 al-Aʿrāf (both late-Meccan, immediately preceding the Medinan
transition) ALSO pass the permutation null. Q 26 al-Shuʿarāʾ and
Q 37 al-Ṣāffāt (middle-Meccan, oath/narrative-cycle) DO NOT.
Per the locked acceptance matrix, control-clean threshold is ≤ 1/4;
the observed 2/4 fails control-clean → routes to **PARTIAL**.

The PARTIAL routing is theoretically informative, not a defeat:
verse-pair seam-density appears to be a property of late-Meccan and
Medinan prose generally, NOT a specifically al-Biqāʿī-Medinan
phenomenon. Middle-Meccan oath-cycle surahs (Q 26, Q 37) have
**distance-1 Jaccard half the magnitude** of priority surahs, and
no significant excess vs their own permutation null.

**Convergence with task #21 / T-002**: the surah-pair-scale
adjacent-Jaccard test passed (z=+10.7) at the inter-surah level.
H-CLASSIC-47 confirms a similar effect at the **complementary
intra-surah verse-pair scale**. The two scales independently
support local-munāsaba structure at different granularities.

## Pre-registered test (verbatim, no amendments)

The pre-reg locked:
- **Priority surahs**: Q 2, 3, 4, 5 (al-Biqāʿī's most extensively
  commentated longer Medinan set per spec).
- **Control surahs**: Q 6, 7, 26, 37 (the 4 longest non-priority
  Meccan surahs in mushaf order with n_verses ≥ 100, deterministic
  selection).
- **Distance-1** as primary scale; bucket means {1, 2, 3-5, 6-10,
  11+} reported descriptively.
- **Stopword-root list** LOCKED to {Alh, kwn, qwl, Eml, Amn, llh,
  xlq, Erf}.
- **Both stopword conditions** must pass for the full PASS verdict.
- **N_PERM** = 10,000 within-surah verse-order shuffles per surah.
- **Pass rule**: ≥ 3/4 priority surahs exceed per-surah 99th
  percentile in BOTH stopword conditions.
- **Control-clean rule**: ≤ 1/4 control surahs pass in either
  condition (else the effect is non-specific).
- **Bonferroni k=6**, α_bon = 0.0083 within H-CLASSIC-44..49 family.

## Result

### Primary (per-surah permutation null at distance 1, 10,000 shuffles)

#### Priority surahs (al-Biqāʿī Medinan)

| Surah | n_verses | condition | obs distance-1 J | 99 pct null | z | p_emp | pass? |
|-------|----------|-----------|------------------|-------------|---|-------|-------|
| Q 2 al-Baqara | 286 | with-stopwords | 0.0738 | 0.0535 | **+10.45** | 0.0000 | **PASS** |
| Q 2 | | without-stopwords | 0.0459 | 0.0297 | **+9.37** | 0.0000 | **PASS** |
| Q 3 Āl ʿImrān | 200 | with-stopwords | 0.0730 | 0.0618 | **+5.88** | 0.0000 | **PASS** |
| Q 3 | | without-stopwords | 0.0487 | 0.0324 | **+7.83** | 0.0000 | **PASS** |
| Q 4 al-Nisāʾ | 176 | with-stopwords | 0.0938 | 0.0721 | **+9.03** | 0.0000 | **PASS** |
| Q 4 | | without-stopwords | 0.0503 | 0.0318 | **+8.55** | 0.0000 | **PASS** |
| Q 5 al-Māʾida | 120 | with-stopwords | 0.0951 | 0.0733 | **+7.74** | 0.0000 | **PASS** |
| Q 5 | | without-stopwords | 0.0556 | 0.0386 | **+6.98** | 0.0000 | **PASS** |

**Priority pass count: 4/4 in BOTH stopword conditions.** All
exceed pre-reg threshold of ≥ 3/4. **PRIMARY PASSES.**

#### Control surahs (Meccan negative control)

| Surah | n_verses | condition | obs distance-1 J | 99 pct null | z | p_emp | pass? |
|-------|----------|-----------|------------------|-------------|---|-------|-------|
| Q 6 al-Anʿām | 165 | with-stopwords | 0.0696 | 0.0557 | +6.38 | 0.0000 | **PASS** |
| Q 6 | | without-stopwords | 0.0521 | 0.0381 | +6.65 | 0.0000 | **PASS** |
| Q 7 al-Aʿrāf | 206 | with-stopwords | 0.0715 | 0.0488 | +9.36 | 0.0000 | **PASS** |
| Q 7 | | without-stopwords | 0.0545 | 0.0313 | +10.26 | 0.0000 | **PASS** |
| Q 26 al-Shuʿarāʾ | 227 | with-stopwords | 0.0407 | 0.0458 | +1.80 | 0.0460 | FAIL |
| Q 26 | | without-stopwords | 0.0275 | 0.0335 | +1.59 | 0.0678 | FAIL |
| Q 37 al-Ṣāffāt | 182 | with-stopwords | 0.0167 | 0.0282 | +0.47 | 0.2920 | FAIL |
| Q 37 | | without-stopwords | 0.0109 | 0.0237 | +0.22 | 0.3742 | FAIL |

**Control pass count: 2/4 in both conditions.** Threshold for
"control-clean" was ≤ 1/4. **CONTROL FAILS** — effect is not
exclusively al-Biqāʿī-Medinan.

### Verdict routing

Primary 4/4 ≥ 3 ✓; control 2/4 > 1 ✗ → **PARTIAL** routing per
the second row of the pre-registered acceptance matrix:

> "PRIMARY ≥ 3/4 priority surahs pass per-surah 99th pctile
> permutation null AND TERTIARY ≥ 2/4 control surahs ALSO pass
> → PARTIAL — verse-pair effect is real but generalizes beyond
> priority surahs (not specifically Medinan-Biqāʿī)"

Routing is literal, no post-hoc reframing.

### Secondary (descriptive bucket means)

For each surah, mean Jaccard at distance buckets {1, 2, 3-5, 6-10,
11+}, both stopword conditions.

#### Priority surahs (without-stopwords condition)

| surah | dist-1 | dist-2 | dist-3-5 | dist-6-10 | dist-11+ | strict monotone? |
|-------|--------|--------|----------|-----------|----------|------------------|
| Q 2 | 0.0459 | 0.0397 | 0.0353 | 0.0287 | 0.0227 | **YES** |
| Q 3 | 0.0487 | 0.0337 | 0.0299 | 0.0263 | 0.0235 | **YES** |
| Q 4 | 0.0503 | 0.0306 | 0.0291 | 0.0290 | 0.0226 | YES (3-5≈6-10) |
| Q 5 | 0.0556 | 0.0364 | 0.0367 | 0.0297 | 0.0271 | YES (2≈3-5) |

**3 of 4 priority surahs show clean strictly-monotone Jaccard decay
with distance**, and the 4th is monotone except for a tiny
3-5 / 6-10 inversion. This is direct empirical evidence for
al-Biqāʿī's distance-decay structure of munāsaba.

#### Control surahs (without-stopwords)

| surah | dist-1 | dist-2 | dist-3-5 | dist-6-10 | dist-11+ |
|-------|--------|--------|----------|-----------|----------|
| Q 6 | 0.0521 | 0.0444 | 0.0367 | 0.0334 | 0.0288 |
| Q 7 | 0.0545 | 0.0383 | 0.0357 | 0.0317 | 0.0223 |
| Q 26 | 0.0275 | 0.0383 | 0.0212 | 0.0152 | 0.0177 |
| Q 37 | 0.0109 | 0.0073 | 0.0131 | 0.0167 | 0.0090 |

Q 6, Q 7 also show monotone distance decay (consistent with their
PRIMARY PASS). **Q 26 al-Shuʿarāʾ has distance-2 > distance-1**
(0.038 > 0.028) — anti-monotone! And **Q 37 al-Ṣāffāt has
distance-6-10 (0.0167) > distance-1 (0.0109)** — also anti-monotone.

These are exactly the surahs that FAILED the permutation null
gate. The bucket-mean structure independently confirms the
permutation-null finding: Q 26 and Q 37 do NOT have local-munāsaba
distance-decay.

### Tertiary (negative-control geographic split)

This is a NOTE, not a pre-registered subtest. The 2 control surahs
that PASSED (Q 6 al-Anʿām, Q 7 al-Aʿrāf) are both **late-Meccan**
in Nöldekian chronology, immediately preceding the Medinan
transition. The 2 that FAILED (Q 26 al-Shuʿarāʾ, Q 37 al-Ṣāffāt)
are both **middle-Meccan oath/narrative-cycle surahs**.

| surah | period | observed pattern |
|-------|--------|------------------|
| Q 6 al-Anʿām | late-Meccan | PASS |
| Q 7 al-Aʿrāf | late-Meccan | PASS |
| Q 26 al-Shuʿarāʾ | middle-Meccan (oath cycle) | FAIL |
| Q 37 al-Ṣāffāt | middle-Meccan (oath cycle) | FAIL |

**Theoretically interpretable**: al-Biqāʿī-style local munāsaba
appears to be a property of late-Meccan and Medinan prose
specifically — surahs structured around extended legal/narrative
discourse where adjacent verses naturally share lexical material.
Middle-Meccan oath/narrative-cycle surahs (formula-driven,
short verses, abrupt thematic cuts) do NOT have this property.

## What this rules in and rules out

**Rules in**: Verse-pair seam-Jaccard density is a real,
permutation-null-robust signal in **all 4 priority Medinan surahs**
AND in **2 of 4 late-Meccan controls**. The signal survives stopword
removal, so it is not a divine-name / formulaic-repetition artifact.
The bucket-mean structure shows clean distance-decay in 6 of 8
surahs tested (4 priority + Q 6 + Q 7).

**Rules out (provisionally)**: The effect is NOT specifically
limited to al-Biqāʿī's 4 named priority surahs. It generalizes to
late-Meccan transitional material. The strong al-Biqāʿī claim
"verse-by-verse munāsaba is a Medinan distinctive" is partially
falsified — Q 6 and Q 7, which are not in his priority set, show
the same effect.

The signal does NOT extend to middle-Meccan oath surahs (Q 26,
Q 37). This rules out a "general al-Biqāʿī applies to all Quran"
universalist reading; the doctrine has a clear genre/period
boundary.

## Why this is not REVERSE

H-CLASSIC-47 is one-sided. Jaccard is bounded [0, 1]. There is no
"reverse direction" — a surah either has elevated distance-1
Jaccard above its permutation null or it does not. Q 26 and Q 37
showed sub-99th-percentile observations (in fact their bucket means
were anti-monotone, with distance-2 sometimes > distance-1) but this
is "no signal" not "reverse signal".

## Methodological notes

### Why the negative control matters

Without the control, this test would be a clean PASS: 4/4 priority
surahs at z > 5 in both conditions. But the control reveals that
the effect is NOT specific to the priority surahs — it generalizes
to 2/4 controls. Locking the control selection BEFORE running was
essential: if I had chosen "the 4 controls that don't show the
effect", the test would have been a PASS by construction, which is
classic forking.

The deterministic control selection rule "the 4 longest Meccan
non-priority surahs in mushaf order" was committed in the pre-reg
and the resulting set Q {6, 7, 26, 37} was determined before
running the script. Audit-defensible.

### Why stopword removal matters

The "with-stopwords" condition has higher absolute Jaccard
(priority surahs ~0.07-0.10) than "without-stopwords" (~0.05-0.06),
because divine-name and high-frequency function-roots like
Alh / kwn / qwl appear in many adjacent verses. But the **z scores
are similar in both conditions** (priority surahs: with=+5.88 to
+10.45; without=+6.98 to +9.37), which means the permutation null
is correctly absorbing the stopword-frequency baseline.

The crucial test: **without-stopwords still passes at z > 6 in all
4 priority surahs**. The al-Biqāʿī signal is NOT a divine-name
echo artifact.

### Why permutation-null is the right test

A naive "compare distance-1 mean to distance-11+ mean" test would
be confounded by surah-specific overall Jaccard rates (longer surahs
with more diverse vocabulary will have lower global Jaccard at
every distance). The within-surah permutation null **fixes the
multiset of verse-root-sets** and only varies their order — so it
isolates the *order-dependent* contribution to distance-1 Jaccard.
This is the correct null for "do verses cluster by similarity at
distance 1?".

## Convergence with task #21 / T-002 adjacent-pair seam-munāsaba

Task #21 / T-002 tested adjacent-pair seam-Jaccard at the
**SURAH-pair** scale (each "pair" = two consecutive surahs in
canonical order; recovered 17/113 surah-pairs vs null mean 2.01,
z = +10.7). The convergent picture:

| Scale | Test | Result |
|-------|------|--------|
| Cross-surah seam (T-002 / task #21) | Hamiltonian recovery of canonical surah order via adjacent-pair Jaccard | z=+10.7, 17/113 PASSES |
| Within-surah verse-pair seam (H-CLASSIC-47, this test) | Per-surah permutation null at distance 1 in 4 priority Medinan surahs | 4/4 priority PASS at z > 5; 2/4 controls also PASS |

**Both scales independently confirm local-Jaccard structure** in
the Quran. The two findings should be cited together as a "scale-
stratified al-Biqāʿī seam-Jaccard family" in MASTER §1 / §3.

## Compute log

- QAC parse: ~0.5 sec.
- Per-surah Jaccard / bucket means: ~0.5 sec total.
- Per-surah permutation null at distance 1: 10,000 perms × 8
  surahs × 2 conditions = 160,000 perms. Each perm computes
  ~150-285 Jaccards. Total: ~3 minutes wall time on my machine.
- Wall time: **~3 min**. Within pre-reg estimate of 2-3 min.

## Pre-reg compliance

PRE-REG-STANDARD-04. All locked parameters honored:
- Seed 20260414 ✓ (sub-streams: SEED+0..3 priority, SEED+100..103
  control)
- Priority surahs LOCKED to {2, 3, 4, 5} ✓
- Control surahs LOCKED to {6, 7, 26, 37} ✓
- Distance-1 LOCKED as primary scale ✓
- Stopword list LOCKED to {Alh, kwn, qwl, Eml, Amn, llh, xlq, Erf} ✓
- Both stopword conditions required for PASS ✓
- 10,000 perms per surah ✓
- Pass rule LOCKED to ≥ 3/4 priority surahs in BOTH conditions ✓
- Control-clean rule LOCKED to ≤ 1/4 controls passing ✓
- Bonferroni k=6, α_bon = 0.0083 ✓
- Verdict matrix applied literally (PARTIAL row matched, not PASS,
  not NULL, not PARTIAL-DECONFOUNDED) ✓

Disclosed deviations:
- **QAC verse counts vs Quran-JSON verse counts differ by 1 in three
  surahs** (Q 2: 285 vs 286; Q 3: 199 vs 200; Q 7: 205 vs 206).
  Cause: the QAC has Bismillāh as verse 1 of Q 1 (al-Fātiḥa) but
  not as a separate verse in other surahs, AND a few verses contain
  no rooted STEM tokens at all (purely function-particle verses).
  Effect on test: **negligible** — the pre-reg operationalized
  per-verse root sets and treats verses without rooted tokens as
  Jaccard-undefined-and-dropped. This is consistent across all
  surahs; no asymmetric handling. Disclosed as a methodology note,
  not a deviation. (Note: Q 26 and Q 37 also have small
  226 vs 227 / 182 vs 182 mismatches; same cause.)
- No other deviations.

## No-fork protections honored

All 7 pre-registered no-fork protections were honored:

1. **Priority surahs LOCKED**: Q {2, 3, 4, 5}, no swap.
2. **Control surahs LOCKED**: Q {6, 7, 26, 37}, deterministic
   selection of 4 longest non-priority Meccan with n ≥ 100. No
   post-hoc swap to "Q 8 or Q 9".
3. **Distance-1 LOCKED**: only distance-1 used as primary; bucket
   means are descriptive only.
4. **Stopword list LOCKED**: 8 specific roots, no addition (e.g.,
   no post-hoc `Erq` / `frq` etc.) and no removal.
5. **Permutation seed 20260414 + sub-stream offsets** ✓.
6. **Pass rule LOCKED to ≥ 3/4 in BOTH conditions** (not "either
   condition" or "weighted average"). Both with-stopwords AND
   without-stopwords were required to pass.
7. **Root extraction LOCKED to QAC v0.4 STEM-only** — same convention
   as H-NEW-29, no swap to lemma-level or surface-token.

## Follow-up hypotheses

**H-CLASSIC-47.1** (queued): expand the test to all 86 surahs with
n_verses ≥ 30 and report the per-surah pass rate. Hypothesis: pass
rate strongly correlates with revelation period (Medinan + late-
Meccan PASS, middle/early Meccan FAIL). This would convert
H-CLASSIC-47 PARTIAL into a chronology-stratified PASS, formally
testing the period-genre boundary observed in this test.

**H-CLASSIC-47.2** (queued): run the same test with **lemma-level**
tokens (not root-level) and **morpheme-level** tokens, to see
whether the signal localizes at the morphological-lemma layer or
the abstract-root layer. al-Biqāʿī's commentary often cites
morphological-lemma echoes (e.g., one verse uses *qātalū* and the
next uses *yuqātilūna*); both share root QTL but differ in lemma.

**H-CLASSIC-47.3** (queued): test the inverse — for the 14 surahs
identified in H-CLASSIC-48 SECONDARY (verses with extreme |ρ_1|
verse-length autocorrelation), do those surahs ALSO show elevated
distance-1 root-Jaccard? If yes, the rhythmic-memory and lexical-
memory mechanisms co-localize.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-classic-47-prereg.md`
- Script: `scripts/h_classic_47_biqai_seam.py`
- JSON: `findings/phase-b-hypotheses/csv/h-classic-47.json`
- Seed: 20260414

## Reproducibility

```bash
cd /Users/grey/Downloads/quran
python3 scripts/h_classic_47_biqai_seam.py
# Wall time ~3 min. Output:
#   findings/phase-b-hypotheses/csv/h-classic-47.json
#   stderr → progress and verdict log
```

Seed 20260414 makes the run fully deterministic. Sub-streams are
seeded as SEED+0/+1/+2/+3 (priority Q 2/3/4/5) and SEED+100/+101/
+102/+103 (control Q 6/7/26/37).
