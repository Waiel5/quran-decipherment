---
prereg_id: H-NEW-2820
title: The two highest-citation flagged claims are GROUP comparisons — testing H-NEW-126 and H-NEW-570 against compositionally matched nulls
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-126 Cell A, H-NEW-570 PRIMARY]
rule_applied: findings/UNIT-DRIFT-DEFECT.md §3 Screen B (grouping form), §6.1, §6.3, §7
method_parent: [H-NEW-2790, H-NEW-2770, H-NEW-2760, H-NEW-2720, H-NEW-2680, H-NEW-2810]
seeds: 20260509 primary / 20260519 replication
status: LOCKED — written and SHA-256'd before any number in it was computed
---

# Pre-registration — H-NEW-2820

**Nothing in this document was computed. Every number quoted below is read from an existing
published file and is cited to it. The full list of what I knew before locking is §9.**

---

## 1. Why these two claims

`findings/UNIT-DRIFT-DEFECT.md` §8 records the most transferable result of the 2026-08-07
session: two independent audit lanes applied the same three screens to the same repository,
**agreed on every claim they both saw**, and were both structurally blind to an entire class.
Screen B as originally written asked only about **orderings**. The two highest-citation flagged
claims in the repository compare **groups**:

| claim | external citers | statistic | grouping |
|:--|--:|:--|:--|
| **H-NEW-126** Cell A | **32** | mean pairwise root-set Jaccard | a 5-surah "isolate core" vs the other 109 |
| **H-NEW-570** PRIMARY | **30** | mean pairwise Fisher–Rao distance | 29 muqaṭṭaʿāt surahs vs a draw from all 114 |

(Counts from `UNIT-DRIFT-DEFECT.md` §6.2's specified metric; H-NEW-2790 §12 reports 27 for
H-NEW-570 on a slightly different scope. Neither is asserted here as exact; both are ≥ 30 and
≥ 27 respectively and both head the queue.)

**Fifty-nine citations' worth of load-bearing claims sat outside the screen's coverage by
construction, and perfect agreement between two auditors said nothing about it.** Screen B has
since been widened. Neither claim has ever been tested against a null that holds unit size fixed.

**The nuisance parameter for a group comparison is not the nuisance parameter for an
ordering.** For a sequence the danger was unit-size drift *along* the ordering. For a group
comparison it is **compositional imbalance between the groups**: if one group's members are
systematically longer, more Meccan, or drawn from a different length regime, then any per-unit
statistic differs between the groups for reasons unrelated to the claimed mechanism. A grouping
needs no monotone trend to carry the defect. It only needs the groups to differ.

---

## 2. The two claims, exactly as published

### 2.1 H-NEW-126 Cell A

- **Finding**: `findings/phase-b-hypotheses/h-new-126-isolate-core.md`
- **Script**: `scripts/h_new_126_isolate_core.py`
- **Result JSON**: `findings/phase-b-hypotheses/csv/h-new-126.json`
- **Seed**: 20260417, `N_PERM` = 10,000, `α_bon` = 0.05/4 = 0.0125

**Statistic.** `J̄(S)` = mean over the C(|S|,2) pairs in a surah set `S` of
`|R_a ∩ R_b| / |R_a ∪ R_b|`, where `R_s` is the set of QAC roots attested in surah `s`, read
from `data/morphology/surah-root-graph.json`.

**Group.** `CORE_5 = {16, 21, 22, 23, 25}`, identified **post hoc** by cross-finding-010, not
by the finding itself. The finding discloses this.

**Published null.** 10,000 draws of 5 surahs uniformly from the 109 non-core surahs;
`p = (1 + #{null ≥ obs}) / (1 + 10000)`, one-sided upper.

**Published headline.** `obs = 0.3414`, `null mean = 0.1291`, `p = 0.0009`, ≈ 2.64× enrichment,
verdict **PASS-DIRECTED** at α_bon = 0.0125.

**Screen C is absent by the finding's own admission.** Its §"Honest caveat — length confound"
reads: *"Longer surahs have larger root-sets and higher baseline Jaccard with other long surahs.
… The null uses all 109 non-core surahs with NO length stratification. A stricter secondary null
matched by length (length-bucketed 5-sets) would be a natural follow-up; **NOT pre-registered
here**, so we flag but do not run … queue as H-NEW-126.1."* **H-NEW-126.1 was never run** — no
script, no JSON, and the only three files mentioning it are the finding, its pre-registration,
and `findings/ORPHAN-REFERENCES.md`. This pre-registration discharges that queued arm.

### 2.2 H-NEW-570 PRIMARY

- **Finding**: `findings/phase-b-hypotheses/h-new-570-muqattaat-content-cluster.md`
- **Script**: `scripts/h_new_570_muqattaat_content_cluster.py`
- **Result JSON**: `findings/phase-b-hypotheses/csv/h-new-570.json`
- **Seed**: 20260520, `N_PERMS` = 10,000

**Statistic.** `d̄(S)` = mean over the C(|S|,2) pairs in `S` of `D[a][b]`, where `D` is the
114 × 114 Fisher–Rao distance matrix over per-surah QAC-root probability vectors, read from
`findings/phase-b-hypotheses/csv/h-new-111.json` → `D_matrix_upper_triangular`.

**Group.** The 29 muqaṭṭaʿāt-opened surahs
`{2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}`.

**Published null.** 10,000 draws of 29 surahs uniformly **from all 114** (the group's own members
are in the donor pool); `percentile = 100 × #{null ≤ obs} / 10000`.

**Published headline.** `d̄ = 0.9388131231527093`, `percentile = 65.62`. The script's own locked
threshold is `primary = (pM <= 10.0)` → **fails** → verdict **NULL / "median-level" /
"muqaṭṭaʿāt-axis is ORTHOGONAL to content-axis"**, with the downstream claims that al-Suyūṭī's
epistemic humility is *empirically vindicated* and al-Biqāʿī's *munāsaba* is *empirically
falsified* at whole-surah scale.

**Note a correction to the queue's own description of this claim.** H-NEW-2790 §12 lists
H-NEW-570's statistic as *"eight density measures, muq vs non-muq"* with denominator *"verse
count"*. **That is not what the script computes.** It computes one statistic — a mean pairwise
Fisher–Rao distance over root distributions — and its denominator-shaped exposure is unit size
entering the smoothed distribution, not a verse-count division. The queue entry is corrected
here from the source, and the test below is built on the actual statistic.

**Why a NULL claim is worth this much work.** A null is not exempt from the defect; it is
exposed to it in the *opposite* direction. If muqaṭṭaʿāt surahs are systematically larger and
`d̄` rises with size, then a size-blind null under-states the expected `d̄`, the observed value
is pushed **up** the percentile scale, and a real cluster can be reported as median-level. Thirty
citing files rest on the resulting "orthogonal" architecture claim.

---

## 3. The imbalance channels to be characterised (locked)

For **each** grouping, and reported before any null is run, quantified — not asserted:

| # | channel | form |
|--:|:--|:--|
| 1 | mean verse length | tokens ÷ verses |
| 2 | verse count | count |
| 3 | surah word count | token count |
| 4 | unique root-set size `\|R_s\|` | count |
| 5 | Meccan / Medinan composition | proportion Medinan |
| 6 | Nöldeke rank | mean rank |
| 7 | mushaf position | mean index |

Reported per group: **n, mean, median, SD, the between-group ratio of medians, and Cohen's d**
(on `log` for channels 1–4, raw for 6–7, and a proportion difference for 5). H-NEW-2790 §12
publishes the muqaṭṭaʿāt median ratios already (mean verse length 2.98×, verse count 3.27×, word
count 4.34×); those are a prediction this run must reproduce, not an input to it.

### 3.1 Dominant-channel selection rule — LOCKED, ranked on the data before use

`UNIT-DRIFT-DEFECT.md` §5 requires ranking candidate channels on the data before locking one,
and §6.1 requires that the ranking metric be the one the statistic actually has to clear.

> **Rule.** Over the 10,000 draws of each claim's **own published null**, compute the Spearman
> ρ between each draw's set statistic (`J̄` or `d̄`) and that draw's **mean log channel value**.
> The candidate with the largest |ρ| is the **dominant channel** and is the stratifier for the
> primary matched null. Candidates are channels 1–4. Ties (|Δρ| < 0.02) break to the channel
> with the larger between-group Cohen's d.

Channel 5 (Meccan/Medinan) is binary and cannot be quantile-binned; it is characterised and
enters only as the cross-stratified secondary arm A2c.

**This rule has no free parameter and is fixed now, before the correlations exist.**

---

## 4. The arms

### A0 — Reproduction, including the distinguishing outputs

Per H-NEW-2810: **reproducing a headline scalar is not reproducing a computation.** Each
claim's own frozen script is executed unmodified at its own published seed, and the following
are checked, all of them:

**H-NEW-126** — Cell A `obs` 0.3414 / `null_mean` 0.1291 / `p` 0.0009; **Cell A MW-5** ḥawāmīm
{40–44} `obs` 0.3062 / `null_mean` 0.1298 / `p` 0.0046; **Cell C** `obs` 5.32 / `null_mean`
14.83 / `p` 0.0157; **Cell C MW-5** musabbiḥāt {57,59,61,62,64} `obs` 16.08 / `null_mean` 14.53
/ `p` 0.6732; **Cell D** the five top-extremity axes and percentiles
(16→`unique_root_count` 92.5; 21→`surah_length` 88.2; 22→`noldeke_rank` 93.4;
23→`surah_length` 89.0; 25→`unique_root_count` 78.5); and the **profile table** verse counts
(128/112/78/118/77), mean verse lengths (14.4/10.5/16.4/8.9/11.6) and unique-root counts
(358/284/328/271/250).

**H-NEW-570** — PRIMARY `d̄` 0.9388131231527093 / pct 65.62; **MW-5** ḥawāmīm-7 {40–46} `d̄`
0.8672422857142857 / pct 20.90; **MW-6** non-muq-29 `d̄` 1.0228183201970442 / pct 100.00; and
`aggregate_h1_confirmed = false`.

**Tolerances.** Statistics: |Δ| ≤ 0.002 absolute. Percentiles: ≤ 1.0 percentile point.
Monte-Carlo p-values: ≤ 0.002 absolute. Deterministic values (`d̄`, `obs`, Cell D percentiles,
profile-table entries) must match to **12 significant figures** — they contain no randomness,
so any deviation is a defect, not noise.

**A0 failure ⇒ `UNVERIFIABLE` for that claim, reported prominently, and no null run against it
is reported as meaningful.** A distinguishing-output failure with a reproducing headline is
recorded as flag `REPRODUCTION-PARTIAL` and carried beside the verdict, not instead of it.

### A1 — Conditional exceedance: the parameter-free size diagnostic

Restrict each claim's **own published null draws** to the sub-population whose mean log
dominant-channel value is **≥ the observed group's**, and recompute the claim's own statistic
within that restricted set:

- H-NEW-126: `p_A1 = (1 + #{restricted null ≥ obs}) / (1 + n_restricted)`.
- H-NEW-570: `pct_A1 = 100 × #{restricted null ≤ obs} / n_restricted`.

**No bin width, no free parameter.** If the effect is size, `p_A1` inflates (126) or `pct_A1`
collapses (570). Reported with `n_restricted`; if `n_restricted < 200` the arm is reported as
underpowered and is not decisive.

### A2 — Stratified matched null (primary inferential arm)

Bin all 114 surahs into `k` quantile bins of the dominant channel. Let `(n_1 … n_k)` be the
observed group's occupancy. Each null draw takes exactly `n_i` surahs uniformly at random from
bin `i`, from the **same donor pool the published null used** (126: the 109 non-core; 570: all
114). 10,000 draws.

- **A2-k5** — `k = 5` (quintiles). **PRIMARY.**
- **A2-k10** — `k = 10` (deciles). **SECONDARY, registered now**, per `UNIT-DRIFT-DEFECT` §6.1:
  a stratified null must declare its bin width as part of the null and report at least two.
  **If the two disagree, both are reported and the finer bin is the honest one.**
- **A2b — caliper arm (H-NEW-126 only).** With a 5-member group, quintiles leave ~23 donors per
  bin. Each null member is instead drawn from the `w = 11` nearest donors to the corresponding
  core surah by rank on the dominant channel (the core surah itself excluded). Registered as a
  *stricter* arm.
- **A2c — cross-stratified arm.** Bins = (dominant channel at `k = 5`) × (Meccan/Medinan), 10
  cells, matching the group's occupancy exactly. **Reported as `NOT-ESTIMABLE` if any cell has
  fewer donors than the group requires** — that determination is made by counting, not by
  judgement.
- **A2d — pool sensitivity (H-NEW-570 only).** The published null draws from all 114, including
  the 29 muqaṭṭaʿāt themselves. A2-k5 repeated with the donor pool restricted to the 85
  non-muqaṭṭaʿāt. Reported alongside; **it does not enter the verdict**, which is scored on the
  published pool.

### A3 — Genre control on a compositionally identical pseudo-group

Partitioning code is **lifted verbatim** from `findings/phase-b-hypotheses/scripts/h-new-2680.py`
by the H-NEW-2720 mechanism: `AR_DIAC`/`NON_AR`, `normalise_words`, `build_pseudo_corpus`
extracted from the frozen source, each fragment SHA-256-checked before `exec`, nothing retyped.
Grouping into 114 pseudo-surahs is H-NEW-2720's `group_matched`.

Because `build_pseudo_corpus` cuts the baseline stream to **the Qurʾān's exact verse
word-length profile** and `group_matched` applies **the Qurʾān's exact surah verse counts**, the
pseudo-group taken at the *same surah indices* has **identical verse counts, identical verse
lengths and identical word counts to the real group — the compositional imbalance is identical
by construction, to the token.** This is the tightest available form of "same imbalance,
different text".

- **Baselines**: `data/baseline-corpora/raw/bukhari-noquran.txt` (ḥadīth),
  `data/baseline-corpora/raw/jahiz-hayawan.txt` (adab prose).
- **`N_OFFSET` = 200** offset partitions each (H-NEW-2720's constant), offsets drawn from the
  slack with the run seed; offset 0 always included.
- **`N_PERM` = 2,000** null draws per offset per arm (the baseline arm needs a percentile to
  ~1 pp, not to 0.01 pp); the Qurʾān arms keep 10,000.
- **Instrument matching is mandatory and is a limitation, stated now.** No morphological
  analyser exists for the baselines, so the genre comparison is run on **surface word types**
  for all three corpora — H-NEW-2680's instrument-matched surface-word arm:
  - claim 1 analogue: `J̄` over per-pseudo-surah **surface word-type sets**;
  - claim 2 analogue: `d̄` over Fisher–Rao distances between per-pseudo-surah **top-500
    surface-word-type** probability vectors, Dirichlet α = 0.5 (H-NEW-2720 `content_matrix` +
    `fisher_rao`, the same construction H-NEW-111 used at root level).
  - **The Qurʾān's own surface-word value is computed and reported in the same instrument.**
    Root-instrument values are never compared across corpora.
- Reported per baseline: across the 200 offsets, the **min / median / max** of the group's
  unmatched percentile and of its A2-k5 matched percentile (570) or matched `p` (126), plus the
  **fraction of offsets at least as extreme as the Qurʾān's surface-word value**.

### A4 — Replication

Every arm re-run at seed 20260519. A classification that changes between seeds is reported
`SEED-FRAGILE` and both values are published.

### Magnitude reporting — mandatory in every arm

For every arm: `observed`, `null mean`, null `q05 / q50 / q95`, `z = (obs − mean)/SD`, and the
ratio `obs / null mean`. **No arm may be reported as pass/fail alone.** H-NEW-2680's most
damaging result was that baselines were *more* extreme than the Qurʾān, which a binary verdict
would have hidden.

---

## 5. Directional predictions, recorded before the run

Registering these costs nothing and makes the result falsifiable as a prediction rather than as
a story told afterwards.

1. **H-NEW-126 Cell A is predicted to be largely size.** Jaccard is mechanically bounded above
   by `min(|R_a|,|R_b|) / max(|R_a|,|R_b|)`, and for two small sets sampled from a Zipfian
   vocabulary the expected overlap fraction is small. The core-5 carry 358/284/328/271/250 roots
   against a corpus in which most surahs are short mufaṣṣal units. **Predicted:
   `p_A2-k5 ≥ 0.0125` — `DOES-NOT-SURVIVE`.**
2. **H-NEW-570's published NULL is predicted to move toward the lower tail, possibly across its
   own threshold.** H-NEW-2720 measured `r(d̄_content, log unit size) = +0.956`
   (`STATE-OF-THE-PROJECT-2026-08-07.md` §2), so larger units carry larger Fisher–Rao content
   distance. The muqaṭṭaʿāt are larger by 2.98–4.34× on the published medians. A size-blind null
   therefore **under**-states the `d̄` expected of a set that size, inflating the observed
   percentile. **Predicted: `pct_A2-k5 < 65.62`, and a reversal to `pct ≤ 10.0` is a live
   outcome.**
3. **The genre arm is predicted to reproduce whatever survives**, because the pseudo-groups
   carry the identical size imbalance by construction and no content mechanism at all.

**Being wrong on any of these is a result and will be reported as one.**

---

## 6. Decision rule — LOCKED

Scored per claim. Every threshold below is the claim's **own published threshold**, not one
chosen here.

```
Step 0.  A0 fails                       -> UNVERIFIABLE   (stop; no null result is reported as meaningful)
         A0 headline OK, distinguishing output fails
                                        -> flag REPRODUCTION-PARTIAL and continue
```

### 6.1 H-NEW-126 Cell A — published classification: PASS (the core clusters)

Own bar: `p < α_bon = 0.0125`. The finding also claims the post-hoc single-test cap
`p < 0.05`; both are reported, the verdict is scored on **0.0125**.

```
SURVIVES                  p_A2-k5 < 0.0125  AND  p_A2-k10 < 0.0125  AND  p_A2b < 0.0125
                          AND  p_A1 < 0.0125
                          AND  neither baseline's median p_A2-k5 < 0.0125
GENRE-SHARED-BUT-LARGER   the matched arms clear as above, AND >=1 baseline median clears too,
                          AND the Quran's z exceeds that baseline's median z
GENRE-SHARED-AND-SMALLER  as above, but a baseline's median z exceeds the Quran's
DOES-NOT-SURVIVE          p_A2-k5 >= 0.0125
```

### 6.2 H-NEW-570 PRIMARY — published classification: NULL (no content cluster; "median-level")

Own bar, taken from the published script: `primary = (pct <= 10.0)`.

```
SURVIVES                  pct_A2-k5 > 10.0  AND  pct_A2-k10 > 10.0
                          (the published NULL stands under matching)
REVERSES-CLUSTERED        pct_A2-k5 <= 10.0
                          (the published NULL is overturned: muqattaat DO cluster in content
                           once size is held fixed, and the al-Biqai / al-Suyuti readings
                           attached to the null must be withdrawn)
REVERSES-OVERDISPERSED    pct_A2-k5 >= 90.0
                          (also contradicts "median-level", in the opposite direction)
```

**Two-sided reading of "median-level", registered now.** The finding's own language is
*"65.62%ile = median corpus dispersion"* and *"orthogonal"*. Both tails contradict it. A matched
result with `|pct − 50| ≥ 40` overturns the published description whichever tail it lands in.

**Genre modifier for 570.** If a verdict of `REVERSES-CLUSTERED` or `REVERSES-OVERDISPERSED` is
reached AND ≥ 1 baseline's median matched percentile lands in the same tail, the verdict is
suffixed `-GEOMETRIC`: the shift is a property of the size profile and the smoothing, not of
Qurʾānic content. **This is the arm that decides whether a reversal means anything**, and it is
registered before the reversal is known to occur.

### 6.3 Arms in conflict

`UNIT-DRIFT-DEFECT` §6.6: **if two nulls disagree, report both and take the stricter.** The
finer bin (k = 10) and the caliper arm are stricter than k = 5. A verdict resting on the
lenient arm alone must say so in the same sentence.

**The runner's verdict logic will be diffed clause-by-clause against this section before
anything is declared** — the H-NEW-2600 failure mode.

---

## 7. Run discipline

- Pre-registration SHA-256 computed at lock time, **embedded as a literal in the runner**, and
  verified at runtime with `SystemExit` on mismatch.
- Frozen inputs, each SHA-256-verified at runtime: `quran-text/quran-no-tashkeel.json`,
  `data/morphology/surah-root-graph.json`, `data/revelation-order.csv`,
  `findings/phase-b-hypotheses/csv/h-new-111.json`, `findings/phase-b-hypotheses/csv/h-new-126.json`,
  `findings/phase-b-hypotheses/csv/h-new-570.json`, `scripts/h_new_126_isolate_core.py`,
  `scripts/h_new_570_muqattaat_content_cluster.py`,
  `findings/phase-b-hypotheses/scripts/h-new-2680.py`,
  `data/baseline-corpora/raw/bukhari-noquran.txt`,
  `data/baseline-corpora/raw/jahiz-hayawan.txt`.
- Seeds **20260509** primary, **20260519** replication.
- **Write-once, enforced in code** (`UNIT-DRIFT-DEFECT` §7): the run directory is created with
  `os.makedirs(..., exist_ok=False)` and every file inside it is opened with mode `'x'`.
  `results.json` is written **exactly once, at completion**.
- **Progress checkpoints go to a directory OUTSIDE the run directory** and are never rewritten.
- **A run directory is never deleted.**
- `manifest.json` records every frozen input SHA with **repository-relative paths**.
- No `git commit` is made by this lane.

---

## 8. Honest limits, declared in advance

1. **The genre arm cannot use roots.** Both claims' native instrument is the QAC root layer,
   which exists for no baseline. The cross-corpus comparison is therefore surface-word-type only,
   and the Qurʾān's surface-word values are reported so the comparison is like-for-like. A
   surface-word result does not automatically transfer to the root layer.
2. **A partition is not a composed book** (`STATE-OF-THE-PROJECT` §4.7). Both statistics here are
   *contiguity-insensitive* set/distribution comparisons at surah scale, so arbitrary cuts
   neither create nor destroy the relevant structure in an obvious direction. That is an argument
   for the control's fairness, not a proof of it, and it is not used to strengthen any verdict.
3. **Conditioning on size may remove mechanism, not only confound.** If the muqaṭṭaʿāt genuinely
   mark long surahs (`h-new-46` STRONG-PASS), then stratifying on length removes part of what the
   muqaṭṭaʿāt *are*. The correct reading of a matched result is therefore "given two sets of
   surahs of the same size profile, does the muqaṭṭaʿāt set differ in content dispersion" — a
   narrower question than the published one, and it is the question being answered.
4. **H-NEW-126's target is post-hoc.** The 5-surah core was selected by cross-finding-010 on
   data that includes the content axis being tested. No null run here repairs that; the matched
   null tests the size confound only.
5. **Fisher–Rao `d̄` on Dirichlet-smoothed vectors is size-dependent by construction.** Short
   surahs are pulled toward the prior and toward each other. This is the mechanism under test,
   and it means a "matched" result for 570 is a statement about a size-conditional contrast, not
   about the muqaṭṭaʿāt in the abstract.
6. **Monte-Carlo resolution.** At 10,000 draws a percentile has SE ≈ 0.5 pp near the middle and
   ≈ 0.3 pp near the tails; at the baselines' 2,000 draws, ≈ 1.1 pp. A verdict landing within
   1 SE of its threshold is reported as a boundary case.

---

## 9. Garden of forking paths — what I knew before locking

Recorded so that nothing below can later be presented as a prediction it was not.

- **Both claims' published headline numbers**, read from their finding files and result JSONs and
  quoted in §2 and §4 above.
- **Both scripts, read in full**, including H-NEW-570's donor pool being all 114 rather than the
  85 non-muqaṭṭaʿāt, and H-NEW-126's `HAWAMIM_MW5` being `{40..44}` (five) while its finding's
  prose says "ḥawāmīm" (classically seven).
- **H-NEW-126's own "Honest caveat — length confound" section**, which names the exact confound
  this pre-registration tests and states that the matched arm was queued as H-NEW-126.1 and not
  run. **I verified before locking that H-NEW-126.1 has no script and no JSON.**
- **The muqaṭṭaʿāt size ratios** (mean verse length 2.98×, verse count 3.27×, word count 4.34×)
  from H-NEW-2790 §12, and `h-new-46`'s STRONG-PASS that muqaṭṭaʿāt concentrate in long surahs.
- **`r(d̄_content, log unit size) = +0.956`** from H-NEW-2720 via `STATE-OF-THE-PROJECT` §2 —
  which is the basis of prediction §5.2 and is why a reversal is registered as a live outcome
  *before* it is known whether one occurs.
- **H-NEW-2790's §12 mis-description of H-NEW-570's statistic**, found while reading the script
  and corrected in §2.2 above **before** any test was designed against it.
- **That the two claims were invisible to the ordering-only Screen B**, from
  `UNIT-DRIFT-DEFECT` §8.
- **No number in §§3–6 exists yet.** The dominant channel is unknown, all matched percentiles
  and p-values are unknown, and the baseline arms have not been run.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before computing. A rate is a ratio; and for a group
comparison the divisor is the composition of the groups. Bismillāhi al-Raḥmāni al-Raḥīm.*
