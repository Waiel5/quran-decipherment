---
finding_id: H-NEW-2810
title: Re-deriving the hard-coded literals — seven confirm exactly, and H-NEW-192's two are reachable but not identified
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-192, H-NEW-183, H-NEW-233, H-NEW-88, H-NEW-165, H-NEW-1710, H-NEW-1395]
prereg: findings/phase-b-hypotheses/prereg-h-new-2810-unverifiable-rederivation.md
prereg_sha256: 9e09aaa147b9a238b2514f42adbf28cbcd706bc6b43a855d45c24e6b966d16b4
run: findings/phase-b-hypotheses/runs/h-new-2810/20260807T072050Z/
rule_applied: findings/UNIT-DRIFT-DEFECT.md §6.3 (UNVERIFIABLE), §7 (write-once)
method_parent: [H-NEW-2790]
seeds: 20260509 primary / 20260519 replication
status: >-
  Nine literals found by scan, not by recall. Seven CONFIRM against their own artifacts, one of
  them (H-NEW-1710's Musa count) re-derived independently from the Leeds QAC and agreeing three
  ways. H-NEW-192's two are neither confirmed nor irrecoverable: an exhaustive search of all
  20,349 admissible 15-feature sets REACHES the Ridge literal 0.759 to six decimals, and 30 of
  100 candidates reach the RF literal 0.817 -- but NO candidate reproduces the published feature
  importance vector, which fails by 27x its locked bar and inverts the published top feature.
verdict: >-
  The literals are reachable and the computation is not identified. 0.759 is hit by 15 of 20,349
  candidate feature sets and 0.817 by 30 of 100, so hitting them is expected rather than
  evidential. What cannot be reproduced is the rest of the same published claim: H-NEW-192
  reports verse_count as the dominant RF feature at 0.416 with type_token_ratio minor at 0.095,
  and every candidate tested inverts this -- type_token_ratio dominates at 0.635 and verse_count
  falls to 0.133. The published R2 is recoverable by coincidence; the published model is not
  recoverable at all.
---

# H-NEW-2810 — Re-deriving the hard-coded literals

**Pre-reg SHA-256 `9e09aaa1…6d16b4`, runtime-verified. Seventeen frozen inputs SHA-verified.
Run 3,019 s. This is the first runner written under the corrected write-once rule: `results.json`
is written exactly once with mode `"x"`, and the 20,349-cell search checkpoints to
`runs/h-new-2810-progress/` — outside the run directory — in files that are never rewritten.**

---

## 0. What this audits

`findings/UNIT-DRIFT-DEFECT.md` §6.3 established a screen outcome that dominates the other three:

> **UNVERIFIABLE — the claim's headline numbers are not produced by any code in the repository.**

Such a number is worse than an unaudited one. It is consumed downstream as a fixed input —
sometimes as a **decision threshold** — so every result built on it inherits an unverified
constant while appearing corroborated by the citation. This audit re-derives them.

---

## 1. The generator — found by scan, not by recall

The inventory was produced by scanning every `.py` under `scripts/` and
`findings/phase-b-hypotheses/scripts/` for a numeric literal bound to a key naming *another*
finding. **Thirteen matches, nine distinct literals — and four of the nine (L6–L9) I had not
previously identified.** The two I already knew about were not the whole problem, which is the
argument for running a generator rather than auditing a remembered list. One match
(`h_new_900_cross_text.py:490`) records a window count in a comment, not a claimed value, and is
excluded.

---

## 2. The nine literals and what the two-command screen returned

| tag | literal | source claim | consumed at | script? | JSON? |
|:--|--:|:--|:--|:-:|:-:|
| **L1** | **0.759** | H-NEW-192 Ridge R² | `h_new_233_…:532,571`; `h_new_250_…:670` | **NO** | **NO** |
| **L2** | **0.817** | H-NEW-192 RF R² | `h_new_233_…:533,572`; `h_new_250_…:671` | **NO** | **NO** |
| L3 | 0.836 | H-NEW-183 Ridge R² | `h_new_233_…:573`; `h_new_250_…:674` | yes | yes |
| L4 | 0.7395 | H-NEW-233 Ridge R² | `h_new_250_…:672` | yes | yes |
| L5 | 0.8485 | H-NEW-233 RF R² | `h_new_250_…:673` | yes | yes |
| L6 | 0.4138 | H-NEW-88 RF top-1 | `h_new_179_alpha_beta_predictor.py:533` | yes | yes |
| L7 | 0.6552 | H-NEW-165 RF top-1 | `h_new_275_bukhari_opener_…py:385` | yes | yes |
| L8 | 136 | H-NEW-1710 Mūsā total | `Q028_F_06_musa_density_rank.py:126` | **NO** | yes |
| L9 | 0.9230 | H-NEW-1395 null mean | `Q030_F_08_alm_cluster_fr_cohesion.py:184` | yes | yes |

**Only L1 and L2 fail both checks.**

---

## 3. Seven CONFIRM, and they confirm exactly

| tag | literal | derived value | verdict |
|:--|--:|--:|:--|
| L3 | 0.836 | **0.8355931448** | `CONFIRMS` |
| L4 | 0.7395 | **0.7395490015** | `CONFIRMS` |
| L5 | 0.8485 | **0.8485169366** | `CONFIRMS` |
| L6 | 0.4138 | **0.4137931034** (= 12/29) | `CONFIRMS` |
| L7 | 0.6552 | **0.6551724138** (= 19/29) | `CONFIRMS` |
| L9 | 0.9230 | **0.9229933000** | `CONFIRMS` |
| **L8** | **136** | **136** | `CONFIRMS` — **three ways** |

**L8 is the strongest confirmation in the batch and the only one re-derived from the corpus
rather than from an artifact.** Counting Leeds QAC tokens with `LEM:muwsaY\`` — the extractor
`Q028_F_06_musa_density_rank.py:24` declares — returns **136**, matching (a) the literal, (b)
`h-new-1710.json`'s recorded total, and (c) the `corpus_total_musa_qac` that the consuming script
independently recomputes in the same run it hard-codes 136 into. Q 28's own count re-derives at
18, matching its published value.

**What a CONFIRM means here, stated precisely:** for L3–L7 and L9 it means **the constant matches
the artifact its producing script emitted** — a transcription check. It says nothing about
whether that computation was correct; H-NEW-2790 showed L4 and L5 reproduce perfectly and still
do not survive a size-matched null. **Only L8 is a re-derivation of the underlying quantity.**

---

## 4. L1 and L2 — the exhaustive search

H-NEW-192 has no script and names only **10** of its **15** features. H-NEW-2790 tried two
hand-built reconstructions and neither reproduced the Ridge literal. **Two reconstructions
failing is not evidence that no reconstruction succeeds**, so the question was asked
exhaustively over every admissible set:

- **Pool:** H-NEW-233's 29 columns + `divine_name_density` + `legal_term_density` = **31**
- **Fixed:** the ten features H-NEW-192 names, present in every candidate
- **Free:** choose 5 from the remaining 21 → **C(21,5) = 20,349**, all evaluated

| result | value |
|:--|--:|
| candidates evaluated | **20,349 of 20,349** |
| **matches within ±0.0005 of 0.759** | **15** |
| **closest achievable R²** | **0.759002** (\|dev\| = **0.000002**) |
| distribution min / median / max | 0.6601 / 0.7800 / 0.8273 |
| mean ± sd | 0.7653 ± 0.0405 |

**The literal is reachable, to six decimal places.** The closest set is
`{alpha, alpha_minus_beta, beta, hurst_verse_len, phon_emphatic}` added to the named ten.

**My pre-registered directions D3 and D4 both failed.** I predicted zero matches and predicted
the space minimum would exceed 0.759. Both were wrong: there are 15 matches and the space runs
down to 0.6601. **That is recorded here because a pre-registration that only gets confirmed is
not doing any work.**

---

## 5. The locked verdict, and why it is not the honest one

**The runner's implemented rule returned `L1 = CONFIRMS-BY-RECOVERY`, `L2 = RECOVERED`**, because
pre-registration §5 keys IRRECOVERABLE on the exhaustive search returning **zero** candidates,
and it returned fifteen. That is what was locked and that is what the runner computed.

**It is the wrong answer, and the defect is in my pre-registration rather than in the runner.**
Two things it failed to account for:

**(a) A search this large hits any target in its support.** With 20,349 candidates spread over
[0.6601, 0.8273], a normal approximation to the observed distribution predicts **≈ 198** hits
within ±0.0005 of 0.759 by chance alone. **Fifteen were observed — fewer than chance predicts.**
Hitting the literal is not evidence of anything; it is the expected outcome of asking 20,349
questions. The same holds for L2 more strongly: **30 of 100** Channel-B candidates land within
0.005 of 0.817.

**(b) I registered a second, independent recovery channel in §3.3 and set its tolerance in §4 —
and then did not wire it into the verdict function in §5.** The importance-vector criterion
(max abs deviation ≤ 0.02 **and** identical rank order) is in the locked text; the verdict rule
that consumed it is not. **This is the H-NEW-2600 error in its mirror image**: there, a runner
implemented a looser rule than the pre-registration; here, the runner faithfully implemented a
pre-registration clause that was itself too loose, while a stricter clause sat unused three
sections above it. **Diff the verdict function against the whole pre-registration, not against
its decision section.**

**Under the pre-registration read whole — §3.3 + §4 + §5 together — neither label fits**, because
the search returned matches (so not IRRECOVERABLE) and the importance channel failed (so not
recovered). The honest classification, named rather than forced into a locked label:

> ### L1, L2 — **REACHABLE-BUT-NOT-IDENTIFIED**
> The published numbers can be produced. The published computation cannot be recovered.

---

## 6. The decisive evidence — the importance vector does not merely miss, it inverts

H-NEW-192 publishes an RF importance vector alongside its R², and it is a far sharper constraint
than a single scalar: ten values that must match, in order, with the five unnamed features
carrying the residual **0.020**.

**Across all 100 Channel-B candidates:**

| statistic | observed | required |
|:--|--:|--:|
| best importance max-abs-deviation | **0.3204** | ≤ 0.02 |
| median importance max-abs-deviation | 0.3731 | ≤ 0.02 |
| **rank-order matches** | **0 of 100** | required |
| five-unnamed-feature mass, range | 0.0237 – 0.9038 | 0.020 |
| RF LOOCV R² within 0.005 of 0.817 | **30 of 100** | — |

**And the Ridge match carries almost no information about the importance match** — the
Ridge-matching candidates average 0.3745 deviation against the random controls' 0.4191, and the
single best extra-mass candidate is a *control*, not a Ridge match. The two channels are
independent, exactly as registered, and only one of them passes.

**The best simultaneous candidate**, measured post-hoc and descriptively — Ridge R² = **0.7590**,
matching the literal, with its five extras carrying **0.033** against the required 0.020:

| feature | published | derived | deviation |
|:--|--:|--:|--:|
| **verse_count** | **0.416** | **0.133** | **−0.283** |
| **mean_verse_len** | **0.173** | **0.028** | **−0.145** |
| eschat_density | 0.125 | 0.116 | −0.009 |
| **type_token_ratio** | **0.095** | **0.635** | **+0.540** |
| divine_name_density | 0.053 | 0.014 | −0.039 |
| loanword_density | 0.048 | 0.009 | −0.039 |
| qul_density | 0.039 | 0.015 | −0.024 |
| legal_term_density | 0.012 | 0.009 | −0.003 |
| muq_cardinality | 0.010 | 0.008 | −0.002 |
| refrain_score | 0.009 | 0.000 | −0.009 |
| *(five unnamed, total)* | *0.020* | *0.033* | *+0.013* |

**This is a structural contradiction, not a near miss.** H-NEW-192's headline reading of its own
model is *"Verse-count dominates (~42% of importance)"*. **On this data verse_count does not
dominate — `type_token_ratio` does, at 0.635, while verse_count falls to 0.133.** The published
first and fourth features swap places, and the gap is 0.540 against a bar of 0.02.

An RF importance vector that no feature set reproduces, attached to an R² that 15 feature sets
reproduce, is the signature of a number that survived and a model that did not.

**One correction to my own earlier work.** H-NEW-2790 §0 cited H-NEW-192's importance ranking as
context — *"its top two RF features are the two strongest drift channels"*. **That reading has no
reproducible basis and should not be repeated.** No H-NEW-2790 verdict depends on it: every one
rests on size-only baselines I computed directly, not on H-NEW-192's importances.

---

## 7. What should change in the project record

Flagged, not applied.

- **`h-new-192-mushaf-position-decomposition.md`** — its R² are **reachable**, which is more than
  H-NEW-2790 could say, and its importance vector is **not reproducible and inverts on the top
  feature**. Its `verdict: STRONG PASS` and its "Verse-count dominates" reading both need notices.
- **`h_new_233_ensemble_predictor.py:532-533`** — the pre-registered decision rule
  `H1 = bool(r2_A > 0.759 …)`, `H2 = bool(r2_B > 0.817)` gates a published verdict on constants
  no code produces. **The thresholds are reachable but arbitrary**: 30 % of arbitrary feature
  sets clear 0.817. That is not a ceiling, and H-NEW-233's "beats the baseline" claim should say
  so.
- **`findings/UNIT-DRIFT-DEFECT.md` §6.3** — UNVERIFIABLE resolves into two distinct states, and
  the difference matters. **NOT-PRODUCED-AND-NOT-REACHABLE** is a refutation.
  **REACHABLE-BUT-NOT-IDENTIFIED** is what H-NEW-192 actually is, and it needs the second
  independent constraint (here, the importance vector) to be detected at all. A single scalar
  cannot distinguish them, because any scalar inside a search space's support is reachable.
- **Seven literals are confirmed and should be cited as confirmed** — L3–L9. Naming the clean
  cases is part of the rule, and six of the nine constants circulating in this repository are
  exactly right.

---

## 8. Part 2 — the write-once sweep

`UNIT-DRIFT-DEFECT.md` §7 now carries the rule that H-NEW-2790's own defect produced:

> **A run script must never overwrite a file inside its own run directory.**

**594 scripts scanned by AST** — every `open(...)` call whose path expression references a
run-directory variable, with its mode and its enclosing loops and functions resolved.

### 8.1 True violations — exactly one

| script | path | sites | why |
|:--|:--|:--|:--|
| **`h-new-2790.py`** | `results.json` | **`:736` and `:806`** | `:736` is inside `snapshot()`, called 8× per run; `:806` is the completion write. **Nine writes to one path.** |

**Two apparent hits are false positives**, and the distinction is the rule's own: `h-new-2660.py:1387,1390` write inside a loop, but to `cells-%s.json % fam` and `hits-%s.json % fam` — the
filename is parameterised by a unique dict key, so **every path is written exactly once**. Writing
inside a loop is not the violation; writing *the same path* twice is.

### 8.2 The one true violation cannot be safely fixed, and that is a finding

`h-new-2790.py` is:
1. **hashed in its own completed run manifest** — `runs/h-new-2790/20260807T053241Z/manifest.json`
   records `script.sha256 = 0737155c1f30…`, which matches the file today. Editing it silently
   invalidates the chain that makes that run verifiable.
2. **cited by line number in the rule document** as the canonical example of the violation
   (§7 quotes `:733-737`).

**Editing it would break both records to fix a script that will never run again.** The correct
disposition is to leave the historical artifact intact — it is the exemplar — and demonstrate the
corrected pattern in new code. `h-new-2810.py` is that demonstration, and §8.4 verifies it.

### 8.3 What was fixed — the five scripts where an edit breaks nothing

Every candidate script was checked against every run manifest in the repository. **Ten have their
SHA pinned by a completed run and were not touched** (`h-new-2640`, `-2640-posthoc`, `-2680`,
`-2680b`, `-2680c`, `-2760`, `-2760-posthoc`, `-2790`, `-2800`, `-2800-diagnostics`). **Five
record no script hash anywhere and were safe to harden** — and none of the five had a *differing*
hash recorded, so no chain was already broken:

| script | write sites hardened `"w"` → `"x"` | run-dir creation |
|:--|--:|:--|
| `h-new-2650.py` | 4 | already `exist_ok=False` |
| `h-new-2650-discard-decomposition.py` | 2 | already `exist_ok=False` |
| `h-new-2660.py` | 6 | `exist_ok=True` → **`False`** |
| `h-new-2670.py` | 1 | `exist_ok=True` → **`False`** |
| `h-new-2720.py` | 2 | `exist_ok=True` → **`False`** |

**15 write sites hardened.** Mode `"x"` makes write-once *enforced* rather than merely intended:
`"w"` silently truncates an existing file, `"x"` raises. `exist_ok=False` closes the same hole one
level up — a second run can no longer land inside an existing run directory. All five re-parse,
and a re-scan confirms every run-directory write in all five is now mode `"x"`.

**No analysis was re-run and no run record was touched.** Fixing the code is not a licence to
regenerate outputs; that would commit the violation being repaired.

### 8.4 The corrected pattern, verified in practice

`h-new-2810.py` was written under the rule and observed obeying it during this run:

- `results.json` and `manifest.json` — **mode `"x"`, one write each, at completion**
- the 20,349-cell search checkpointed to `runs/h-new-2810-progress/20260807T072050Z/002000.json`
  and siblings — **outside the run directory**, one file per checkpoint, never rewritten
- **verified mid-run**: while the search was executing, the progress directory held its
  checkpoints and **the run directory was empty**. Under the old pattern it would have held a
  half-written `results.json` available for any passing `git add -A` to capture.

---

## 9. Honest limits

1. **The pool is what this repository can build, not what H-NEW-192 could have used.** If it used
   a feature existing in no frozen artifact, the search cannot find it. **The importance-vector
   failure is the stronger evidence precisely because it does not depend on the pool**: it says
   the *named ten* do not behave as published, whatever the other five are.
2. **The chance calculation is a normal approximation** to a distribution that is visibly
   left-skewed (median 0.7800 above mean 0.7653). The exact expected count is not 198; the point
   is that it is of order 10², not of order 1, and that conclusion is robust to the approximation.
3. **Channel B sampled 100 of 20,349 candidates.** Its conclusion is that no *tested* candidate
   reproduces the importance vector, with the best at 16× the bar and 0 of 100 matching rank
   order. An exhaustive RF sweep was not affordable; a candidate matching the vector could in
   principle exist among the untested 20,249.
4. **A CONFIRM for L3–L7 and L9 is a transcription check, not a validation** — §3.
5. **L8's rules-tuple is inherited** from `Q028-F-06`'s declaration, not independently adjudicated.
6. **The write-once sweep is static analysis.** It resolves `open()` calls whose path expression
   names a run-directory variable; a script writing via an aliased path or a helper function that
   obscures the variable would be missed.

---

## 10. Garden of forking paths

- **Locked at SHA `9e09aaa1…` before any derived value existed.** Known at lock time: the nine
  literals, their consumption sites, the script/JSON existence table, the published importance
  vector and its 0.980 sum, and H-NEW-2790's two failed reconstructions — all filesystem or
  already-published facts.
- **D3 and D4 both failed** and are reported as failures in §4. The pre-registration predicted
  zero matches and a space minimum above 0.759; there were fifteen matches and the minimum was
  0.6601.
- **The pre-registration's verdict rule was too weak, and the runner implemented it faithfully.**
  §5 states this rather than restating the verdict silently. The locked labels are published as
  computed; the honest classification is named separately and argued.
- **The importance-vector table in §6 is post-hoc and descriptive** — one RF fit on the single
  best candidate, run after the verdicts, to show *what* fails rather than only *that* it fails.
  It changes no classification.
- **Run directories are never deleted.** The calibration run is retained at
  `runs/h-new-2810-SMOKE/20260807T071648Z/`.

---

## 11. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2810-unverifiable-rederivation.md`
  (SHA-256 `9e09aaa147b9a238b2514f42adbf28cbcd706bc6b43a855d45c24e6b966d16b4`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2810.py` — pre-reg SHA-gated; lifts the
  H-NEW-183 and H-NEW-233 matrices and LOOCV as SHA-verified modules; **write-once by
  construction**
- JSON: `findings/phase-b-hypotheses/csv/h-new-2810.json`
- Run (immutable, never deleted): `findings/phase-b-hypotheses/runs/h-new-2810/20260807T072050Z/`
  with `manifest.json` recording every frozen input SHA in repository-relative form
- Progress checkpoints, **outside the run directory**:
  `findings/phase-b-hypotheses/runs/h-new-2810-progress/20260807T072050Z/`

---

*Run 2026-08-07 by Waiel Al-Shujaa. A constant that no code produces is not a result; and a
constant that twenty thousand searches can reach is not a recovery. Bismillāhi al-Raḥmāni
al-Raḥīm.*
