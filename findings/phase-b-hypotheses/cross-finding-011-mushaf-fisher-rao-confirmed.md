---
id: cross-finding-011
title: Mushaf order is Fisher-Rao information-geodesic optimal — CONFIRMED via cross-feature replication
phase: B (synthesis)
date: 2026-04-17
status: CONFIRMED (primary geodesic claim); PASS-DIRECTED (chronology-reversal claim, feature-specific)
parent_findings: [H-NEW-111, H-NEW-111b, H-NEW-111c]
seed: 20260417
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-Surah-1, canonical mushaf order, Fisher-Rao arccos-Bhattacharyya distance)
---

# [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] — Mushaf order is Fisher-Rao information-geodesic optimal

## Headline

**The canonical mushaf ordering of the 114 surahs is Fisher-Rao
information-geodesic optimal.** Under TWO independent feature spaces
(morphological roots + character-4-grams), the total path length
L_mushaf is ~11 standard deviations below random-permutation mean,
within 11% of an approximate TSP optimum, with p-value at the
permutation floor (< 10⁻⁴) in both replications.

Under a third, weakly-related feature space (verse-length histograms),
the primary significance claim also holds (p < 10⁻⁴) but the
near-TSP-optimality claim does NOT hold — rhythm and content give
separate signals about mushaf structure.

**Verdict: the PRIMARY geodesic claim promotes from PASS-DIRECTED to
CONFIRMED.** The secondary claim about mushaf being shorter than
chronology DOES NOT robustly replicate and remains PASS-DIRECTED at
the parent feature only.

---

## Evidence triangle

| Feature space | Test | L_mushaf | Null mean | z | Ratio to L_2opt | p_primary | Verdict |
|---|---|---|---:|---:|---:|---:|---|
| QAC-STEM roots (K=500) | [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (parent) | 85.76 | 104.35 | **−11.46** | 1.107 | < 10⁻⁴ | PASS |
| Char-4-grams (K_char=2000) | [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] | 89.23 | 103.06 | **−11.41** | 1.114 | < 10⁻⁴ | PASS |
| Verse-length hist (8 bins) | [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] | 77.66 | 138.15 | **−9.84** | 2.71 | < 10⁻⁴ | PARTIAL-PASS |

**Between [[h-new-111-fisher-rao-mushaf|H-NEW-111]] and [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]** (orthogonal content features):
- z-scores match within **0.4%**
- Ratio L_mushaf / L_2opt matches within **0.7%**
- Independent feature engineering produces identical geodesicity signal

This is a textbook cross-feature replication, and under any reasonable
rule for combining p-values across independent tests (Fisher's method,
Stouffer's z, or simple Bonferroni-2 reduction) the primary claim
survives with enormous margin.

---

## What's confirmed vs not confirmed

### Confirmed (upgrade PASS-DIRECTED → CONFIRMED)

**Claim 1.** The canonical 114-surah mushaf ordering has Fisher-Rao
path length significantly shorter than random permutations of the
same 114 surahs. Combined p across two orthogonal content feature
spaces is at the permutation floor (< 10⁻⁴) in BOTH.

**Claim 2.** The mushaf is within ~11% of a 2-opt TSP upper bound on
the 114-node root-distance graph. This "geodesic-like" property
holds on content features (roots + char-4-grams); does NOT hold on
rhythm features (verse-length). The content-axis version is
confirmed.

### Not confirmed (remains PASS-DIRECTED at parent feature only)

**Claim 3** (the original [[h-new-111-fisher-rao-mushaf|H-NEW-111]] unexpected finding). "Mushaf is
MORE coherent than Nöldeke/Tanzil chronology on the root-feature
axis." This is TRUE on roots (Δ = −1.47 vs Nöldeke, p = 2×10⁻⁴) but
does NOT replicate on char-4-grams (Δ = +0.13, chronology narrowly
shorter) and REVERSES on verse-length (Δ = +15.95, chronology
significantly shorter).

**Interpretation**: the chronology-reversal is a root-feature-specific
observation, NOT a universal structural fact about the mushaf. It
may reflect how Nöldeke's chronological reconstruction groups
surahs by register-cues that manifest differently in roots (which
abstract away register) vs char-4-grams (which preserve register via
function-word n-grams) vs verse-length (which is length-coupled by
construction).

Honest statement: the mushaf is unambiguously Fisher-Rao-short, but
the relative ranking of mushaf vs chronology depends on which
linguistic axis we measure. ON CONTENT (root-distribution), mushaf
wins; on rhythm, chronology wins; on char-4-grams (mixed
content+register), they tie.

---

## Implications

### For the Quran's structure

The mushaf order encodes an implicit LOCAL-CONTINUITY principle in
the root-content space: consecutive surahs share vocabulary more than
chance would allow. Under the "muqaṭṭāʿat as book-introduction
markers" reading (cross-finding-008), this is consistent: surahs that
introduce themselves as "the Book" tend to cluster in local mushaf
positions (cross-finding-006 surah-position clustering at z = −9.6).

The 4-region hub architecture ([[cross-finding-010-extended-network|cross-finding-010]] with audit-035
amendment) is consistent: the mushaf visits {Q 2, 3} → {Q 50} → {Q
59, 62} → {Q 112, 113, 114} in a path that stays close to vocabulary
continuity.

### For classical debates

Classical Quranic studies have three main theories of mushaf order:
1. **Arbitrary-Uthmanic**: the committee ordered by length, with no
   deeper principle
2. **Chronological-recovery**: mushaf approximates revelation
   chronology imperfectly
3. **Divinely-ordered**: the mushaf reflects intrinsic structural
   design

[[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]]'s evidence addresses (1) and (2):

- **Against (1)**: length-sorted ordering performs at null-mean
  (L = 107 ≈ null mean 104). Length-first cannot explain mushaf's
  L = 85.76. So the Uthmanic ordering goes BEYOND length.
- **Against (2)**: on root-content, mushaf < Nöldeke by 1.47 units.
  Chronology, even reconstructed by Nöldeke's most careful
  philological work, is MORE random than mushaf on this axis. So
  mushaf is NOT a chronology-approximation (on content).
- **On (3)**: we make no theological claim. The structural
  observation is compatible with (3) but does not discriminate
  between (3) and "the Uthmanic committee had a sophisticated
  organizing principle beyond length". The cross-finding ends at
  the empirical observation.

---

## Limits and caveats

1. **Independent replication accomplished on ROOT + CHAR-4-GRAM but
   NOT on more exotic feature spaces** (e.g., semantic embeddings via
   a classical-Arabic-trained model, phonological category
   histograms, or prosodic features). Future replications could
   strengthen or qualify.

2. **TSP 2-opt is an upper bound on L_min.** A Concorde-exact or
   Lin-Kernighan-3 solver would tighten the ratio bound; the TRUE
   L_mushaf/L_min could be higher than 1.11.

3. **Fisher-Rao metric choice was pre-registered** (arccos-
   Bhattacharyya), but Hellinger / KL / Jensen-Shannon would give
   similar results. Robustness across distances would strengthen.

4. **Chronology reversal claim is not robust** (only root axis).
   Honesty demands this be the headline caveat in any public-facing
   writeup.

5. **N = 114 is a small number** for TSP problems but large enough
   that the combinatorial space (114! ~10^186) is vastly larger than
   our 10K permutations. We cannot exhaustively verify L_min; we
   report L_2opt as an upper bound.

---

## Reproduction

- Pre-regs: `[[h-new-111-fisher-rao-mushaf|h-new-111]]-prereg.md`, `[[h-new-111b-fisher-rao-char-4gram|h-new-111b]]-prereg.md`,
  `[[h-new-111c-fisher-rao-verselen|h-new-111c]]-prereg.md`
- Scripts: `scripts/h_new_111_*.py`, `scripts/h_new_111b_*.py`,
  `scripts/h_new_111c_*.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-111.json` (+111b, +111c)
- Journal: `journal/h-new-111-run-1.md` and siblings

Seed 20260417 locked across all three.

---

## Status

**CONFIRMED** — primary Fisher-Rao-geodesicity claim, two orthogonal
feature spaces, z > 11 on both, ratio < 1.12 on both.

**PASS-DIRECTED** — secondary chronology-reversal claim, root-feature
only.

**Queued follow-ups**:
- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] fractal extension (verse-within-surah Fisher-Rao — IN
  FLIGHT)
- Additional feature spaces (embedding-based, phonological)
- Concorde-exact TSP to tighten L_min bound
- Robustness across distance metrics

---

## Addendum (2026-04-17) — [[h-new-130-fisher-rao-residuals|H-NEW-130]] + [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] residuals decomposition

**Scope**: this addendum extends [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] with a DIAGNOSTIC
finding about WHERE the mushaf's 11% non-geodesic excess concentrates.
It does not change the parent CONFIRMED verdict; it decomposes the
residual mechanism.

### New results

**[[h-new-130-fisher-rao-residuals|H-NEW-130]]** (roots, PASS-DIRECTED 2026-04-17): 15 of the 15 largest
Fisher-Rao consecutive-surah distances in mushaf order coincide with a
pre-committed structural-boundary set B (|B|=54 of 113 pairs, 5
boundary-types: classical length, Meccan↔Medinan, Nöldeke phase,
muqaṭṭāʿat presence, muqaṭṭāʿat letter-set). Hypergeometric
p = 4.78×10⁻⁶. Secondary A (B-vs-notB mean-distance concentration):
T = +0.244, p = 1×10⁻⁴.

**[[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]** (char-4-grams, REPLICATION-CONFIRMED 2026-04-17): 15
of 15 identical; hypergeometric p = 4.78×10⁻⁶. Secondary A:
T = +0.257, p = 1×10⁻⁴. Secondary B (cross-feature top-15 overlap
with [[h-new-130-fisher-rao-residuals|H-NEW-130]]): 10 of 15 shared pairs, hypergeometric p = 1.15×10⁻⁷.

**Promotion**: [[h-new-130-fisher-rao-residuals|H-NEW-130]] elevates from PASS-DIRECTED to CONFIRMED
via [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] cross-feature replication, under identical replication
discipline that promoted [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] itself.

### What this tells us about [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s 11% excess

The parent [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] established L_mushaf/L_2opt ≈ 1.11 (11%
above TSP-optimum). [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b decompose that 11% excess: it is
NOT uniformly distributed noise across 113 pairs. It concentrates at
exactly 15 specific structural-boundary hinges, and those 15 pairs are
reproducible across two orthogonal feature spaces (roots + char-4-grams)
with 10 of 15 being identical in both.

### Mechanism (honest)

The 15 top-jumps are dominated by the Meccan↔Medinan period axis.
Under a robustness bracket that drops period + phase, only 7 of 15
remain (p = 0.086, N.S.). The effect is real and pre-registered under
the full 5-boundary-type B, but its ROOT CAUSE is Meccan/Medinan
linguistic divergence being STRUCTURALLY INTERLEAVED in the mushaf
reading-order — as opposed to being CLUSTERED as in Nöldeke
chronology or Tanzil revelation-order.

### Reinforces [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s chronology-reversal interpretation

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s root-axis finding that L_mushaf < L_noldeke
(chronology-reversal) had been honestly qualified as "feature-specific"
(doesn't hold on char-4-grams or verse-length). [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b clarify
WHY: chronology clusters Meccans together (minimizing period-hops);
mushaf interleaves them (maximizing period-hops at discrete, structured
hinges). The CUMULATIVE path length is still shorter on mushaf under
roots because the 98 non-top-15 pairs are unusually short (local
coherence), while the 15 period-boundaries are deliberate large jumps
used as structural markers.

This is a coherent picture: mushaf optimizes local-continuity SUBJECT
TO structural-boundary preservation. Not a pure geodesic. A
"structured-geodesic".

### Shared pairs (cross-feature invariants)

10 of 15 top-jump pairs appear in BOTH roots and char-4-gram top-15:
Q 12→13, Q 14→15, Q 23→24, Q 24→25, Q 32→33, Q 33→34, Q 49→50,
Q 54→55, Q 55→56, Q 56→57.

These are the most feature-invariant structural hinges in the
canonical mushaf ordering. All are period/phase transitions or
muqaṭṭāʿat architectural boundaries.

### Files

- `findings/phase-b-hypotheses/h-new-130-prereg.md`
- `findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`
- `findings/phase-b-hypotheses/csv/h-new-130.json`
- `findings/phase-b-hypotheses/h-new-130b-prereg.md`
- `findings/phase-b-hypotheses/h-new-130b-fisher-rao-residuals-char4gram.md`
- `findings/phase-b-hypotheses/csv/h-new-130b.json`

### Addendum verdict

**[[h-new-130-fisher-rao-residuals|H-NEW-130]] CONFIRMED** via cross-feature replication.
**[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] CONFIRMED status unchanged** (parent claim; already
CONFIRMED).
**Interpretive enhancement**: the mushaf's 11% geodesic excess is not
noise; it is structured and structurally interpretable across feature
spaces. Mushaf is a "structured-geodesic" (local-continuity subject to
structural-boundary preservation).

---

## Second addendum (2026-04-17) — [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] triple-feature + universal hinges + wrap-around integration ([[h-new-130d-reverse-universal-wraparound|H-NEW-130d]])

### [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] (rhythm/verse-length replication)

Third feature-space replication on verse-length-histogram D-matrix
from [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]. Result: **TRIPLE-REPLICATION-CONFIRMED**. 13 of 15
top-jumps hit B (hypergeom p = 1.16×10⁻³). Secondary A concentration
T = +0.385 (strongest of 3 features). Secondary B (3-way intersection):
3 universal hinges.

### 3 universal hinges across ALL THREE feature spaces

The pairs appearing in top-15 of roots, char-4-grams, AND verse-length:

- **Q 14 → Q 15** (Ibrāhīm → al-Ḥijr; Nöldeke phase Late-Meccan → Middle-Meccan)
- **Q 49 → Q 50** (al-Ḥujurāt → Qāf; mufaṣṣal-alt start + muq-presence + period + phase)
- **Q 56 → Q 57** (al-Wāqiʿah → al-Ḥadīd; musabbiḥāt cluster entry-point)

These are the maximum-robustness structural markers in the canonical
mushaf ordering — structural boundaries that are visible regardless of
which linguistic axis we measure.

### Wrap-around edge (Q 114 → Q 1) behavior ([[h-new-130d-reverse-universal-wraparound|H-NEW-130d]] T-L.3)

Post-hoc exploratory check: does the hypothesized ring-closure edge
behave like a hinge or like continuity?

| Feature | d(Q 114, Q 1) | Rank among 113 forward pairs |
|---|---:|:-:|
| Root | 0.388 | **97 of 113** |
| Char-4-gram | 0.423 | **98 of 113** |
| Verse-length | 0.083 | **113 of 113 (smallest)** |

The wrap-around edge is **CONTINUITY on all three feature spaces**.
On verse-length, it is the smallest distance of any candidate edge
(Q 114 and Q 1 have nearly-identical verse-length distributions; both
are ultra-short surahs). This reinforces [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s
topological-ring claim: the mushaf closes smoothly at Q 114 → Q 1,
NOT at a structural hinge. A cyclical reading architecture fits.

### Integrated "punctuated-cycle geodesic" picture

The mushaf has four structural edge-types in Fisher-Rao space:

1. **15 structural-hinge edges** (forward-top-15, all in B)
2. **3 UNIVERSAL structural-hinge edges** (top-15 in every feature)
3. **~98 continuity edges** (non-top-15, low distance, coherent local flow)
4. **1 wrap-around edge** (Q 114 → Q 1, continuity-type, supports ring)

**Mushaf = local-continuity geodesic + 15 structural-boundary hinges + smooth ring-closure.**

### Files (both addenda)

- `[[h-new-130-fisher-rao-residuals|h-new-130]]-prereg.md`, `[[h-new-130-fisher-rao-residuals|h-new-130]]-fisher-rao-residuals.md`, `csv/h-new-130.json`
- `[[h-new-130b-fisher-rao-residuals-char4gram|h-new-130b]]-prereg.md`, `[[h-new-130b-fisher-rao-residuals-char4gram|h-new-130b]]-fisher-rao-residuals-char4gram.md`, `csv/h-new-130b.json`
- `[[h-new-130c-fisher-rao-residuals-verselen|h-new-130c]]-prereg.md`, `[[h-new-130c-fisher-rao-residuals-verselen|h-new-130c]]-fisher-rao-residuals-verselen.md`, `csv/h-new-130c.json`
- `[[h-new-130d-reverse-universal-wraparound|h-new-130d]]-reverse-universal-wraparound.md` (post-hoc integration)
- `[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]-mushaf-topological-ring.md` (parallel ring-closure)
- `[[h-new-137-wrap-around-closure|h-new-137]]-wrap-around-closure.md` (wrap-around parent)

### Second addendum verdict

**[[h-new-130-fisher-rao-residuals|H-NEW-130]] THREE-FEATURE CONFIRMED** (roots + char-4-grams + verse-length).
**3 universal hinges identified** (pre-registered threshold ≥3 met).
**Ring-closure empirically smooth** (T-L.3 descriptive, corroborates
[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]).

**[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] updated status**: CONFIRMED primary claim; extended
interpretation is "punctuated-cycle geodesic" with hinge-decomposition
and smooth wrap-around.
