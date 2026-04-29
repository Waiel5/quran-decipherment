# H-NEW-111b — run 1 journal

**Date**: 2026-04-17
**Specialist**: h-new-111b-specialist
**Task**: Independent replication of H-NEW-111 on char-4-gram feature space.

## Chronology

1. **Oriented** via HANDOFF/04-DISCIPLINE.md and the parent finding
   (`h-new-111-fisher-rao-mushaf.md` + prereg). Read the parent script
   (`scripts/h_new_111_fisher_rao_mushaf.py`) to understand the exact
   convention for TSP and Fisher-Rao computation so my replication
   method is architecturally comparable.

2. **Data check**: confirmed `quran-text/quran-no-tashkeel.json` has
   114 surahs; basmala appears only at 1:1 (matches rules-tuple
   "basmala-counted-only-in-surah-1"); surah 2 starts with `الم` not
   basmala. Added an assertion in the script to guard this.

3. **Wrote pre-reg** locking K_char = 2000 before any computation, with
   Bonferroni k=3 and α_bon = 0.0167 in YAML front-matter
   (PRE-REG-STANDARD-04). Direction pre-committed as one-sided
   lower-tail for PRIMARY and for SECONDARY B (replication posture,
   not two-sided). Documented garden-of-forking-paths including
   K_char rationale, feature-orthogonality claim, and the specific
   replication-intent posture.

4. **Wrote script** using numpy for matrix Fisher-Rao computation
   (sqrt-prob inner product via `sqrt_prob @ sqrt_prob.T` → arccos)
   and the same seed (20260417) and PERMS (10,000) as the parent, for
   maximum comparability. Used the same greedy-NN + 2-opt structure
   as the parent for secondary A. Loaded the same `data/revelation-
   order.csv` for Nöldeke and Tanzil orderings.

5. **Ran the script** once (deterministic; no re-runs with parameter
   tweaks). Total runtime ~25 seconds (numpy matmul on 114x2000 is
   cheap; null loop over 10,000 perms dominates).

## Results

```
L_mushaf = 89.2261
null mean = 103.0621, sd = 1.2125, min = 98.8391
z = -11.41
p_primary = 10^-4 (0 / 10,000 perms beat mushaf)

L_greedy_best = 81.4851
L_2opt_best = 80.0820
ratio L_mushaf / L_2opt = 1.1142

L_nold = 89.0996  (narrowly shorter than mushaf!)
L_tanzil = 91.4432 (longer than mushaf by 2.22)
p_nold = 10^-4, p_tanzil = 10^-4

MW-5 pos-ctrl: L = 81.7545, p = 10^-4 (PASS)

Δ = L_mushaf - L_nold = +0.1265  (sign FLIPPED vs parent)
reversal replicated: NO
```

## Feature-space diagnostics

Top-5 char-4-grams (by global freq):
- ` من ` (2763) — function word "from" + whitespace
- `لله ` (2699) — tail of "Allah" + space (copular)
- `الله` (2555) — the divine name
- ` الل` (2244) — leading "Al-l" of "Allah"
- `ن ال` (2078) — "-n al-" boundary common in Medinan prose

Top-K=2000 cutoff frequency: 37. Cumulative coverage: 59.2%.

The top-5 dominated by function words + the divine name is expected for
a no-tashkeel Quranic corpus and explains why this feature is
register-sensitive (Medinan legalistic prose has more repetition of
these than Meccan eschatological prose).

## Interpretation (my take, not in pre-reg)

Primary + secondary-A replicate at *nearly identical effect size*
(z within 0.4%, ratio within 0.7%). This is striking: the two feature
spaces use entirely different engineering (morphological vs graphemic)
and land on indistinguishable verdicts for the primary geodesicity
claim.

Secondary-B (Nöldeke reversal) does NOT replicate, and the sign flips.
The magnitude is tiny (0.13 units vs parent's 1.47 units on a feature
where SD is ~1.2), so this isn't "overwhelming evidence against
reversal"; it's "reversal is not robust to the feature axis". I believe
the correct interpretation is that the chronology-reversal in H-NEW-111
is a root-feature-specific finding, not a general property of the
mushaf. I've written this up in the findings doc with the
length/register-clustering hypothesis for why char-4-grams would let
Nöldeke catch up.

## Cross-finding combination

For the PRIMARY claim:
- Parent (roots): p ≤ 10⁻⁴, z = −11.46
- Child (4-grams): p ≤ 10⁻⁴, z = −11.41

Conservative Bonferroni across families: min(p) × 2 = 2×10⁻⁴ — still
well past any CONFIRMED threshold. Fisher combination under (contested)
independence: ~2×10⁻⁷. I did NOT write a separate cross-finding file
(that's team-lead territory); flagged in the findings doc.

## Discipline compliance

- ✅ PRE-REG-STANDARD-04: Bonferroni/family/alpha in YAML frontmatter
- ✅ PRE-REG-STANDARD-01: direction pre-committed before viewing results
- ✅ MW-1: L1-normalization of p_i (in method)
- ✅ MW-5: positive control specified and fires at p < 10⁻⁴
- ✅ Locked K_char = 2000 before running
- ✅ Seed 20260417 (same as parent for comparability)
- ✅ Honest disclosure of Secondary-B failure with same prominence
- ✅ Writing NULL with equal prominence (Secondary B reversal fails)

## Issues / notes for next agent

- The reversal-fails-on-4-grams result is interesting enough to warrant
  a formal H-NEW-111c on a THIRD feature axis (candidate: verse-length
  distribution per surah, which is neither morphological nor graphemic
  but statistical over verse counts). If the third axis SIDES WITH the
  parent (roots), then the 4-gram result is the outlier. If it sides
  with 4-grams, the reversal is the outlier.
- Decision about whether to promote H-NEW-111 PRIMARY to CONFIRMED via
  cross-finding entry is a team-lead call. The evidence is there on the
  PRIMARY geodesicity + near-optimal ratio. The chronology-reversal is
  NOT to be promoted.
- H-NEW-111b JSON saved to `csv/h-new-111b.json` (includes full
  upper-triangular D matrix, 6441 pairs).
