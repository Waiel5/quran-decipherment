# [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] - Direct isolated-tranche test: no direct repair; the decisive five-edge tranche closes the local block on top-50 but not the globals

**Finding ID**: [[h-new-236-1g-direct-tranche-test|h-new-236-1g]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1g-direct-tranche-test-prereg.md`  
**Pre-reg SHA-256**: `3798d28a3f410faeda79631a75fd7a9c4b480b594496ca22046a2cc7ed75cf48`  
**Seed**: 20260424  
**Parents**: [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] / [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]]  
**Grandparent**: [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] / [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Bonferroni**: k=4, alpha_bon = 0.0125  
**Verdict**: **NO DIRECT ISOLATED-TRANCHE REPAIR.** None of the four locked direct-tranche cells returns empirical `L_path` and empirical `L_tail_91_114` to the simulator 95% CI while keeping empirical `L_mufassal_short` and `Block-chi2` inside. The answer to the main question is still no.

---

## Headline

[[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] asked the cleanest remaining hard-adjacency question left
by [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] and [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]]:

> if the decisive `K=95 -> 100` tranche really carries the missing
> repair information, does it work when tested directly, rather than as
> part of the failed cumulative late-tail prefix?

It does not.

- the positive control passed cleanly
- no main cell achieved the primary direct-repair target
- no main cell achieved family strict 4/4 closure
- all four main cells remained `LOCAL-CLOSED-GLOBAL-FAIL`

But the run still identified something real and new:

> the exact five-edge tranche is strong enough to close the local
> `mufassal-short` block on the plain [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 scaffold,
> even without the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Juz30 top-5 additions

That is not a global repair, but it is a genuine mechanistic clue.

---

## 1. Positive control

`mw5_positive_control_cell_a_base` re-ran the unmodified [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]
Cell A base and passed exactly as required:

- same qualitative signature: PASS
- drift thresholds: PASS

Drift versus [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A sim means:

- `|Delta L_path sim_mean| = 0.000190`
- `|Delta L_tail_91_114 sim_mean| = 0.005235`
- `|Delta L_mufassal_short sim_mean| = 0.000074`

So the negative result is not an instrument failure.

---

## 2. Locked cell results

| Cell | Design | `L_path` sim mean / pct | `L_tail_91_114` sim mean / pct | `L_mufassal_short` sim mean / pct | `Block-chi2` pct | Verdict |
|---|---|---|---|---|---|---|
| `cell_a_base_plus_exact_tranche` | [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A + exact 5-edge tranche | `86.8654`, pct `0.0` | `10.7110`, pct `0.0` | `16.7727`, pct `5.6` | `94.3` | `LOCAL-CLOSED-GLOBAL-FAIL` |
| `cell_b_base_plus_core_only` | [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A + core `(99,100)/(100,101)/(101,102)` | `86.6765`, pct `0.2` | `10.6108`, pct `0.4` | `16.6038`, pct `28.0` | `64.7` | `LOCAL-CLOSED-GLOBAL-FAIL` |
| `cell_c_base_plus_overlap_pair_only` | [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A + overlap pair `(92,93)/(109,110)` | `86.7414`, pct `0.1` | `10.6546`, pct `0.1` | `16.6375`, pct `23.6` | `75.4` | `LOCAL-CLOSED-GLOBAL-FAIL` |
| `cell_d_top50_plus_exact_tranche` | [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 + exact 5-edge tranche | `86.4333`, pct `2.2` | `10.4597`, pct `0.4` | `16.3359`, pct `86.4` | `82.8` | `LOCAL-CLOSED-GLOBAL-FAIL` |

Top-level JSON summary:

- `primary_repair_cells = []`
- `strict_4of4_cells = []`
- `best_local_closed_cell = cell_d_top50_plus_exact_tranche`
- `overall_verdict = NO-DIRECT-ISOLATED-TRANCHE-REPAIR`

---

## 3. What the direct test actually shows

### 3.1 The answer to the main question is still no

None of the four locked designs repaired both globals:

- every main cell kept empirical `L_mufassal_short` inside
- every main cell kept empirical `Block-chi2` inside
- every main cell left empirical `L_path` outside low
- every main cell left empirical `L_tail_91_114` outside low

So the isolated-tranche hard-adjacency story does not rescue the
[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] overcorrection.

### 3.2 On the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A base, every direct tranche variant makes the globals worse

Relative to the positive-control base:

- control `L_path sim_mean = 86.5089`
- control `L_tail_91_114 sim_mean = 10.5085`

The three direct additions on top of that base all worsen both globals:

- exact tranche: `86.8654` / `10.7110`
- core only: `86.6765` / `10.6108`
- overlap pair only: `86.7414` / `10.6546`

Among these three, the core-only cell is the least damaging. But even
the least damaging cell remains cleanly outside on both global
observables.

### 3.3 The strongest new partial finding is Cell D

The exact five-edge tranche on the plain [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 scaffold
is the best local-closed cell in the run:

- `best_local_closed_score_abs_path_plus_tail_gap = 2.4936`
- `L_mufassal_short sim_mean = 16.3359`, percentile `86.4`, inside
- `Block-chi2` percentile `82.8`, inside

That matters because the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 base did **not** have
local terminal closure. So this five-edge tranche alone carries enough
local terminal information to collapse the old local miss.

But it still fails globally:

- `L_path` percentile `2.2`, outside low
- `L_tail_91_114` percentile `0.4`, outside low

So the precise read is:

> the decisive tranche is locally powerful, but globally insufficient.

---

## 4. Interpretation

[[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] changes the terminal picture in a useful way.

### What it confirms

1. **Direct isolated hard-tranche repair is not the answer.**
   The exact [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] tranche does not repair the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]
   overcorrection when tested directly.

2. **The decisive tranche has genuine local causal bite.**
   It is not a meaningless top-100 artifact. On the top-50 base, those
   five edges alone are enough to close the local `mufassal-short`
   block.

3. **Local terminal closure is not uniquely front-loaded.**
   [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] showed one front-loaded Juz30 route to local closure.
   [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] now shows a second route: the late-tail decisive
   tranche can also close the local block on the top-50 scaffold.

### What it does not show

1. It does **not** show that the decisive tranche is a global repair
   law.
2. It does **not** show that the overlap pair is the hidden rescue.
3. It does **not** show that the core three-edge set is enough by
   itself, even though it is the mildest of the three [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]-base
   direct injections.

The honest conclusion is therefore:

> the `95 -> 100` tranche is real signal, but not a sufficient isolated
> hard mechanism.

---

## 5. Consequence for the frontier

[[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] eliminates one more clean candidate:

- not cumulative hard-prefix repair ([[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]])
- not direct isolated hard-tranche repair ([[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]])

The highest-value next step is now more specific:

- test a **small interacting complement** to the decisive tranche rather
  than the tranche alone
- or test the same information as a **soft or mixed constraint** rather
  than a pure hard-adjacency law

The main thing [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] adds is clarity: the five decisive edges
matter, but they are not the whole equation.

---

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1g-direct-tranche-test-prereg.md`
- Script: `scripts/h_new_236_1g_direct_tranche_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1g.json`
