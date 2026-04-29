---
id: H-NEW-260
title: "Q 54 + Q 55 dyad deep-dive — empirical Mode-B mirror-pair coherence"
phase: B
status: NULL
date: 2026-04-18
executed_by: autonomous
parent: H-NEW-253 (Mode-B siblings; Q 54 emerged descriptively as Q 55's closest structural sibling)
prereg: h-new-260-q54-q55-dyad-prereg.md
seed: 20260419
rules_tuple: (no-tashkeel, hafs-kufan, 2-surah dyad + adjacent-pair baselines, seed 20260419)
bonferroni_k: 3
alpha_bon: 0.01667
verdict: "**NULL (0/3 PASS)** — the Q 54+Q 55 dyad does NOT survive preregistered testing; Q 55 remains individually unique, but the dyad claim collapses under joint ACF, root-Jaccard, and Fisher-Rao mirror-asymmetry cells."
classical_anchors:
  - al-Biqāʿī Naẓm al-Durar (Q 54→55 eschatology-mercy bridge)
  - al-Rāzī Mafātīḥ al-ghayb on the Q 54→55 transition
  - al-Suyūṭī al-Itqān fann 62 munāsabāt
---

# [[h-new-260-q54-q55-dyad|H-NEW-260]] — Q 54 + Q 55 dyad deep-dive

## Headline

**The preregistered Q 54+Q 55 dyad claim fails cleanly.**

All three inferential cells miss their Bonferroni-adjusted targets:

- **Cell A joint verse-length ACF**: **NULL**
- **Cell B content-root Jaccard**: **NULL**
- **Cell C Fisher-Rao mirror asymmetry**: **NULL**

**Verdict: 0/3 PASS.** Q 54 al-Qamar may still be the closest *descriptive*
Mode-B sibling to Q 55 al-Raḥmān under [[h-new-253-mode-b-siblings|H-NEW-253]]'s restricted-cell
criterion, but the stronger dyad claim does **not** survive formal testing.

This is an honest narrowing:

- **Q 55 remains uniquely distinctive**
- **Q 54 remains descriptively interesting**
- **Q 54+Q 55 as a special two-surah architectural dyad is not supported**

---

## Results

### Cell A — Joint verse-length ACF coherence

Pre-registered test: concatenate Q 54 and Q 55 into one 133-verse
sequence and compare `max|ACF|` at lags 1..3 against the adjacent-pair
baseline.

- Observed:
  - lag-1 = **0.0509**
  - lag-2 = **0.2558**
  - lag-3 = **0.1408**
  - `max|ACF| = 0.2558`
- Baseline:
  - `n = 103` adjacent pairs with both surahs >= 5 verses
  - median `max|ACF| = 0.2380`
  - observed percentile = **54.85**

**Result: NULL.**

The Q 54+Q 55 concatenated sequence is not an upper-tail prosodic outlier.
Its joint ACF signature is only slightly above the baseline median, not near
the p95 cutoff required by the preregistration.

### Cell B — Content-root Jaccard coherence

Pre-registered test: compare the distinct-root Jaccard overlap of Q 54
and Q 55 against the adjacent-pair baseline.

- `|R_54| = 140`
- `|R_55| = 105`
- `|R_54 ∩ R_55| = 31`
- Jaccard = **0.1449**
- overlap/min = **0.2952**
- Baseline:
  - `n = 113` adjacent pairs
  - median Jaccard = **0.2000**
  - observed percentile = **37.61**

**Result: NULL.**

Q 54 and Q 55 share some salient roots, but by the adjacent-pair
standard they are actually **below-median** in content-root overlap.
The dyad does not cohere as a strong adjacent lexical pair.

### Cell C — Fisher-Rao mirror asymmetry

Pre-registered test: compare `|d(54,55) - d(55,56)|` against the
adjacent-triple baseline distribution.

- `d(Q54,Q55) = 1.1516`
- `d(Q55,Q56) = 1.1493`
- `d(Q54,Q56) = 1.0228`
- `|Δ| = 0.0022`
- Baseline:
  - `n = 112` adjacent triples
  - median `|Δ| = 0.0486`
  - observed percentile = **2.23**
  - upper-tail empirical `p = 0.9823`

**Result: NULL, with direction opposite the preregistered expectation.**

The triple Q 54-55-56 is **more symmetric** in Fisher-Rao spacing than
expected, not more asymmetric. The pre-registered "mirror-vs-closure
distinction" does not appear. If anything, the result suggests Q 55 sits at
an unusually even semantic spacing between Q 54 and Q 56.

---

## MW-5 sanity

Five random adjacent pairs were sampled (excluding Q 54-55). None
simultaneously matched the p95 signature on Cell A + Cell B:

- Q 100-101
- Q 37-38
- Q 78-79
- Q 91-92
- Q 31-32

**MW-5 outcome: 0/5 replicate the dyad signature.**

This is the expected sanity result. The null verdict is therefore not an
instrument-collapse problem; it is a genuine failure of the Q 54+Q 55
dyad hypothesis under the chosen operationalization.

---

## Shared-root profile

Q 54 and Q 55 share **31 roots**. The most jointly salient are:

| Root | Q 54 count | Q 55 count |
|---|---:|---:|
| `k*b` | 9 | 32 |
| `rbb` | 1 | 36 |
| `jnn` | 2 | 8 |
| `kll` | 6 | 3 |
| `kwn` | 6 | 1 |
| `byn` | 2 | 4 |
| `smw` | 1 | 5 |
| `Eyn` | 3 | 2 |
| `qrA` | 4 | 1 |
| `rsl` | 4 | 1 |

This is enough to sustain a **thematic bridge** reading, but not enough to
make the pair a lexical-overlap outlier by adjacent-pair standards.

That distinction matters:

- **thematic bridge** can still be real
- **empirical dyad fingerprint** is not supported here

---

## Interpretation

### What survives

1. **Q 55 remains individually unique.**
   [[h-new-234-q55-unified-profile|H-NEW-234]] and [[h-new-253-mode-b-siblings|H-NEW-253]] still stand: Q 55 is a uniquely saturated
   Mode-B / refrain-stylistic exemplar.

2. **Q 54 remains the nearest descriptive sibling under the restricted
   M1+M3+M5-no-M2 criterion.**
   That descriptive claim is weaker than the preregistered dyad claim and
   is not invalidated by this result.

3. **The Q 54→55 thematic bridge in classical munāsabāt remains possible.**
   Classical exegetes can be right about adjacency in a rhetorical /
   theological sense without the pair forming a quantitative dyad under
   these three instruments.

### What collapses

1. **No joint prosodic dyad signature.**
   The concatenated verse-length sequence is ordinary by adjacent-pair
   standards.

2. **No lexical-overlap dyad signature.**
   Root Jaccard is below the adjacent-pair median.

3. **No mirror-vs-closure asymmetry.**
   Q 54-55 and Q 55-56 are almost equally spaced in Fisher-Rao distance.

The cleanest reading is:

> **Q 54 is a descriptive near-neighbour to Q 55, but not a formally
> supported dyad.**

That keeps [[h-new-253-mode-b-siblings|H-NEW-253]]'s descriptive observation in bounds and prevents
upgrading it into a stronger claim the data do not support.

---

## Classical-scholarship integration

This finding does **not** refute al-Biqāʿī or al-Rāzī on the Q 54→55
transition. It refines what kind of claim they can support empirically.

- **Classical munāsabāt claim that survives**:
  - Q 54 and Q 55 are adjacent in a meaningful rhetorical sequence
  - apocalypse / warning in Q 54 transitions into mercy / address in Q 55

- **Modernized dyad claim that fails**:
  - Q 54+Q 55 form a quantitatively distinct adjacent pair across joint
    ACF, lexical overlap, and FR asymmetry

So the correct empirical statement is narrower:

> **The classical bridge may be real as adjacency commentary, but it is not
> a three-cell dyad fingerprint.**

That is a valuable boundary on how far munāsabāt can be operationalized.

---

## Honest limits

1. **The dyad test uses only three operationalizations.** A different
   feature family could still capture a Q 54→55 relation.
2. **Cell A uses verse-length letters as the prosodic proxy.** A richer
   syllabic or tajwīd-based sequence could behave differently.
3. **Cell B is bag-of-roots Jaccard.** It ignores syntax, ordering, and
   higher-level thematic argument.
4. **Cell C tests asymmetry, not simple closeness.** The observed near-zero
   `|Δ|` may itself be interesting, but it is the opposite of the
   preregistered direction and cannot be upgraded here.
5. **Q 55's uniqueness is not at risk.** This is a dyad null, not a Q 55
   null.

---

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-260-q54-q55-dyad-prereg.md`
- Script: `scripts/h_new_260_q54_q55_dyad.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-260.json`
- Baseline CSV: `findings/phase-b-hypotheses/csv/h-new-260-adjacent-pair-baselines.csv`
- Journal: `journal/h-new-260-run-1.md`

## Final statement

**[[h-new-260-q54-q55-dyad|H-NEW-260]] lands as a clean NULL.** The Q 54+Q 55 pair does not show
special joint verse-length periodicity, does not show exceptional
content-root overlap, and does not show the preregistered Fisher-Rao
mirror asymmetry. The strongest positive claim that remains is the weaker
one already visible in [[h-new-253-mode-b-siblings|H-NEW-253]]:

> **Q 54 is Q 55's closest descriptive Mode-B sibling, but not a formally
> supported empirical dyad.**
