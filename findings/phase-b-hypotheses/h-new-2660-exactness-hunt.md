---
id: H-NEW-2660
title: "The exactness hunt — 124,148 zero-tolerance structural coincidences scanned, every one priced against its own combinatorial denominator"
date: 2026-08-07
phase: B
status: HUNT-NULL
verdict: >-
  HUNT-NULL. An exhaustive generator over five pre-declared types of exact structural
  coincidence scanned 124,148 zero-tolerance candidates across three rules-tuples and found
  1,581 exact hits — and ZERO that survive their own denominator under the whole-space
  Bonferroni correction (α_hit = 4.027 × 10⁻⁷). Of 657 cell-level tests, 13 clear
  α_cell = 7.541 × 10⁻⁵ and all 13 are MECHANICAL by the pre-declared screen. In the
  decoupled strata the corpus produces exact coincidences at 0.69×–1.38× the exactly
  computed chance rate, and 432 of 657 cells fall BELOW their exact expectation. The
  exactness genre is retired over the whole scanned space.
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260519
prereg_sha256: aa0696c5d81a3170a6f5d190971e3201d8c2d8fa01ed262f439dae0a2dd39660
K_candidates: 124148
K_cells: 663
alpha_hit: 4.027e-07
alpha_cell: 7.541e-05
survivors: 0
rules_tuples: "T-ROOT (primary), T-LEMMA, T-NORM"
parents: [H-NEW-2000, H-NEW-2010, H-NEW-2020, H-NEW-2040, H-NEW-2090, H-NEW-2230, H-NEW-2410, H-NEW-2550, H-NEW-1530, H-NEW-1600]
---

# H-NEW-2660 — The exactness hunt

**Pre-reg SHA-256 `aa0696c5…9660`, runtime-verified. Ten frozen inputs SHA-verified.
Seed 20260509, replication 20260519. Every per-hit denominator is a closed form evaluated
in exact rational arithmetic; every E3 cell-level null is an exact enumeration, not a
sample.**

---

## TL;DR

Most famous Qurʾān-miracle claims have the form *"X is EXACTLY equal to Y."* This project
has retired them one at a time, reactively, as they were proposed. **This is the opposite:
a generator.** Five coincidence types were declared and SHA-locked *before* any scan, then
swept exhaustively; **for every exact coincidence found, the number of alternative
configurations that would also have been exact was computed.**

- **124,148 zero-tolerance coincidence opportunities scanned.**
- **1,581 exact coincidences found** — exact equality is cheap, as H-NEW-2010 and
  H-NEW-2020 already showed on two other axes.
- **0 survive** the whole-space Bonferroni threshold α_hit = 0.05 / 124,148 = 4.027 × 10⁻⁷.
- **671 are MECHANICAL** by the pre-declared screen; **910 are exact-but-ordinary (CBM)**.
- **13 of 657 cell-level tests clear α_cell — and all 13 are mechanical**: they are
  tautologies of the decimal numeral system (a surah's position equals its own
  digit-reversal for 20 surahs, because 1–9, 11, 22, …, 99, 101, 111 are palindromes) or
  deterministic-order pairs already established elsewhere (modal-rhyme-count = verse-count
  is rhyme-homogeneity, H-NEW-2240).
- **432 of 657 cells fall BELOW their exact expectation.** In the decoupled strata the
  observed-to-expected ratios are **0.69× (E3b), 0.91× (E3a), 1.34× (E3c), 1.04× (E4)**
  and **0.00 (E2)**. The corpus does not over-produce exact coincidences.

The single most useful output is not the null. It is the **price list** — for the first
time, a viral-shaped iʿjāz claim can be looked up and its denominator read off.

---

## 1. Prior art — what was NOT re-run

Cited, used as instrument controls, and **claimed as a discovery under no circumstances**:

| Finding | Settled | Role here |
|:--|:--|:--|
| [[h-new-2010-root-frequency-balance-scan\|H-NEW-2010]] | 118,584 exact root-count balances exist; meaningful ones UNDER-represented (1 vs ~4, p = 0.979, direction REVERSED) | MW-6 control: my pipeline reproduces **1,642 roots, 185 distinct counts, histogram head {1:395, 2:197, 3:121, 4:96, 5:89}** |
| [[h-new-2020-word-balance-scan\|H-NEW-2020]] | 3,734,882 exact surface-word balances; 1 of 13 famous antonym pairs balances | cited; surface-word axis not re-scanned |
| [[h-new-2090-surah-arithmetic\|H-NEW-2090]] | 0 of 8 position↔verse-count cells exceed chance | MW-6 control: cells 1/2/6 reproduced **exactly** — 0 hits, 1 hit (Q 30), 0 hits — and my exact rook-polynomial nulls reproduce its 10,000-permutation null *means* to three decimals (0.886 / 0.518 / 0.982 vs its 0.88 / 0.51 / 0.98) |
| [[h-new-2040-abjad-sweep\|H-NEW-2040]] | every abjad↔structure correlation NULL; al-Ḥadīd = 57 is the chance expectation | cited; abjad axis not re-scanned |
| [[h-new-2000-numerical-symmetry-audit\|H-NEW-2000]] / [[h-new-2230-qac-lemma-numerical-rerun\|H-NEW-2230]] | 0 of 6–10 balance claims confirm cleanly at lemma-strict | cited |
| [[h-new-2410-number-word-census\|H-NEW-2410]] | number-word census; both locked tests NULL | supplied the attested-cardinal set |
| [[h-new-1530-khalifa-19-audit\|H-NEW-1530]] / [[h-new-1600-corpus-count-and-khalifa-19-audit\|H-NEW-1600]] | Code-19 divisibility NULL | cited |
| [[h-new-2550-muqattaat-phonetic-optimizer\|H-NEW-2550]] | descriptively EXACT (global minimum) and statistically ORDINARY (2.554 % of subsets tie) | the **methodological model** for this file |

The space scanned here is the space those tests did not cover: **rank-extremum
coincidences across axes, exact set coincidences between surah classes, exact integer
equalities among per-surah metrics in three geometries, and exact count↔location
coincidences over the whole morphological inventory.**

---

## 2. What was declared before the scan

Five types, 23 axes (one a seeded **decoy**), 156 surah classes, 14 integer metrics, 8
target functions, 5 location functions, two nulls, both Bonferroni thresholds, the
MECHANICAL screen, the EXCESS direction lock and four verdict vocabularies — all fixed in
`prereg-h-new-2660-exactness-hunt.md` and hashed before a single coincidence was counted.

**The pre-registration states, in §0, that ZERO non-mechanical survivors is the expected
outcome and the deliverable.** It also states, in §5 and *before the run*, the exact
arithmetic consequence of a whole-space correction: at α_hit ≈ 4 × 10⁻⁷ **only type E2 can
produce a per-hit survivor, and only for classes of size ≥ 4** (C(114,4) = 7,160,245 clears
it; C(114,3) = 241,024 does not). That was written down in advance precisely so this file
could not later present the threshold as chosen to fit the outcome.

| Type | What it sweeps | Candidates / tuple | Denominator |
|:--|:--|--:|:--|
| **E1** | rank-extremum coincidences over all axis pairs × 4 extremum modes | 1,012 | **exact closed form** `Σ_s P(ext_a=s)·P(ext_b=s)`, tie-structure respected (= 1/114 when tie-free) |
| **E2** | exact SET equality over all equal-size class pairs | 3,246 | **exact** `1/C(114,k)`; near-misses by exact hypergeometric tail |
| **E3a** | metric(s) == f(s) for 8 target functions | 12,426 | **exact** `mult(target)/114`; cell null by **exact rook-polynomial inclusion–exclusion** |
| **E3b** | metric(i) == metric(115−i) over the 57 mirror pairs | 798 | **exact** monochromatic-pair enumeration + 10⁷-draw pre-registered guard |
| **E3c** | metric(s) == metric′(s) over all metric pairs | 10,374 | **exact** rook-polynomial |
| **E4** | root/lemma count == a location integer, 5 functions | 8,210 / 24,160 | **exact** `h(target)/N`; two nulls |

**K_candidates = 124,148** (E1 3,036 · E2 9,738 · E3a 37,278 · E3b 2,394 · E3c 31,122 ·
E4 40,580) → **α_hit = 4.027 × 10⁻⁷**.
**K_cells = 663** → **α_cell = 7.541 × 10⁻⁵**.

---

## 3. Six coincidences that look like miracles — and their price tags

Every one below is **EXACTLY true** and verified token-by-token against
`data/morphology/quranic-corpus-morphology-0.4.txt` and `quran-text/quran-no-tashkeel.json`.
Every one is the precise shape of a claim that circulates. None survives.

| The coincidence | Exact? | Denominator | Verdict |
|:--|:-:|:--|:--|
| **ṣ-b-r** (*ṣabr*, patience) occurs **103** times; its **last** attestation is Q **103**:3 — *al-ʿAṣr*, in the very phrase *wa tawāṣaw bi-l-ṣabr* | ✔ | **1 in 1,642** (exactly one root has corpus count 103) | **CBM** |
| **q-r-b** (nearness) occurs **96** times; its **last** attestation is Q **96**:19 — the closing word of the first-revealed sūra, *wa-qtarib*, "and draw near" | ✔ | **1 in 547** (3 roots have count 96) | **CBM** |
| **z-w-j** (pairing) occurs **81** times; its **last** attestation is Q **81**:7 — *wa idhā al-nufūsu zuwwijat*, "and when the souls are paired" | ✔ | **1 in 1,642** | **CBM** |
| **s-b-l** (*sabīl*, path) occurs **176** times; its densest sūra is Q 4 *al-Nisāʾ*, which has exactly **176** verses | ✔ | **1 in 1,642** | **CBM** |
| **y-d-y** (*yad*, hand) occurs **120** times; its densest sūra is Q 5 *al-Māʾida*, which has exactly **120** verses | ✔ | **1 in 1,642** | **CBM** |
| **Q 55** *al-Raḥmān* and **Q 60** *al-Mumtaḥana* — a mirror pair, 55 + 60 = 115 — contain exactly **352** words each, despite having 78 and 13 verses | ✔ | **1 in 644** | **CBM** |

α_hit = 4.027 × 10⁻⁷. The best of these is 1-in-1,642 = 6.1 × 10⁻⁴ — **1,500× too common to
survive.** They are not rare; they are the expected yield of 124,148 draws.

**And here is the sentence that does the real work.** The ṣabr, qarraba and zawj
coincidences all belong to one cell — *"a root's corpus count equals the number of the last
sūra in which it appears"*. That cell was swept **exhaustively**, and it returns **exactly
nine hits, which are all of them**:

| root | count = last sūra | |
|:--|--:|:--|
| ṣ-b-r | **103** | ← *al-ʿAṣr*, "…and enjoined patience" |
| q-r-b | **96** | ← *al-ʿAlaq*, "…and draw near" |
| z-w-j | **81** | ← *al-Takwīr*, "…when the souls are paired" |
| q-n-ṭ-r | 4 | |
| ṣ-l-ḥ | 4 | |
| q-r-ḥ | 3 | |
| r-f-th | 2 | |
| s-f-k | 2 | |
| z-w-d | 2 | |

**Observed 9. Expected 11.05** under the unrestricted null, **7.35** under the
dependency-preserving null. Three of the nine are homiletically spectacular and six are
inert — and *the corpus produces fewer of them than a shuffled corpus would.* The three
that preach are not a signal; they are the three draws from a nine-draw urn that happened
to land on a theologically legible number. Selecting them and publishing them is exactly
the mechanism this project has documented for the whole genre — and it is now measured
rather than asserted.

---

## 4. Results by type

### E1 — rank-extremum coincidences (3,036 candidates)

| stratum | observed | exactly expected | ratio |
|:--|--:|--:|--:|
| all cells | 223 | 28.31 | 7.88× |
| **decoupled** (\|ρ\| < 0.70, no declared construction) | **23** | **16.61** | **1.38×** |
| MW-7 descriptive, \|ρ\| < 0.40 | 1 | 3.61 | 0.28× |

The 7.88× gross excess is entirely mechanical: fifteen of the twenty-three axes are
length-driven, and Q 2 al-Baqara is the argmax of nearly all of them. In the decoupled
stratum the excess falls to 1.38× (family p = 0.0396 for T-ROOT, against α_cell = 7.5 × 10⁻⁵
— **not significant**), and **every remaining decoupled hit lands on Q 2 or Q 1**: Q 2
because it is the longest sūra, Q 1 because it is the corpus's strongest structural
outlier (Δ_outlier = +27 pp, H-NEW-590). The residual is carried by one axis,
`n_exclusive_roots`, whose ρ against the size axes is 0.59–0.61 — transparently
length-driven, yet **below the locked 0.70 threshold**. The threshold was not moved. At
the post-hoc, MW-7-capped, no-p-value stratum ρ < 0.40 the count collapses to **1 observed
against 3.61 expected**, which locates the residual precisely.

### E2 — exact SET coincidences (9,738 candidates)

**147 exact set equalities found. All 147 are DEFINITIONAL** — same-source or ρ ≥ 0.70
derived classes, e.g. `BOT29_n_words == BOT29_n_letters`. **Non-definitional exact set
coincidences: 0, against an exact expectation of 6.83 × 10⁻⁸.**

This is the type that *could* have produced a survivor, and it did not. Nothing outside a
definitional pair coincides exactly with anything: not the 29 muqaṭṭaʿāt sūras, not the 7
ḥawāmīm, not the 6 musabbiḥāt, not the 14 sajdah-bearing sūras, not the 13
rhyme-homogeneous sūras — with any top-*k* or bottom-*k* class on any of 23 axes.

The strongest **non-definitional near-miss** in the whole sweep is
`TOP14_n_distinct_roots` vs `TOP14_n_exclusive_roots` at overlap **12 of 14**
(Jaccard 0.750, exact hypergeometric p = 1.45 × 10⁻¹²) — two morphological-richness axes at
ρ = 0.61, i.e. the long-sūra cluster again, and still **not exact**. Near-misses were
pre-registered as descriptive; no near-miss is promoted.

### E3 — exact integer equalities among per-surah metrics (70,794 candidates)

| geometry | observed | exactly expected | decoupled obs | decoupled exp | ratio |
|:--|--:|--:|--:|--:|--:|
| E3a self-referential | 385 | 247.41 | 187 | 163.91 | 1.14× |
| E3b mirror-pair | 30 | 43.70 | 30 | 43.70 | **0.69×** |
| E3c cross-metric | 239 | 158.55 | 113 | 84.28 | 1.34× |

**E3b is a deficit**: across 2,394 mirror-pair candidates the corpus produces 30 exact
mirror equalities where chance predicts 43.7. The Q 55 / Q 60 word-count identity above is
one of the 30 — real, exact, and one of *fewer than average*.

The exact mirror engine and the pre-registered 10⁷-draw permutation guard agree to three
decimals on every cell (e.g. 0.08522 exact vs 0.08450 sampled at only 2,000 draws in the
development run).

### E4 — exact count↔location coincidences (40,580 candidates)

| function | obs (roots) | exp N1 | exp N2 | obs (lemmas) | exp N1 | exp N2 |
|:--|--:|--:|--:|--:|--:|--:|
| count == first sūra | 39 | 96.51 | 41.31 | 174 | 246.63 | 166.25 |
| count == last sūra | 9 | 11.05 | 7.35 | 28 | 50.25 | 28.61 |
| count == modal sūra | 40 | 61.35 | 38.25 | 166 | 167.73 | 154.72 |
| count == verses of modal sūra | 3 | 2.80 | 1.80 | 3 | 4.68 | 1.78 |
| count == 115 − first sūra | 1 | 2.03 | 1.35 | 2 | 3.70 | 2.29 |

**The two nulls are the whole story.** N1 (unrestricted permutation) badly over-predicts —
96.5 expected against 39 observed — because it destroys the real dependency between how
often a root occurs and where it occurs. N2, the pre-registered dependency-preserving null
that permutes counts only within deciles of `n_distinct_surahs`, lands almost exactly on
the observation: **41.31 vs 39, 7.35 vs 9, 38.25 vs 40, 1.80 vs 3, 1.35 vs 1.** Once the
mundane fact that frequent roots appear early and everywhere is held fixed, **every single
count↔location coincidence in the Qurʾān is accounted for.** No residue.

---

## 5. Cell-level: 13 excesses, all thirteen mechanical

Of 657 cell-level tests, 13 clear α_cell = 7.541 × 10⁻⁵. Every one trips the
pre-declared §6 screen:

| cell | obs | exp | why it is mechanical |
|:--|--:|--:|:--|
| `mushaf_position == digit-reverse(position)` | 20 | 0.90 | **constructional.** The palindromes below 115 are 1–9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111. This is a property of base-10 numerals; the Qurʾān is not involved. |
| `mushaf_position == digit-sum(position)` | 9 | 1.00 | **constructional** (the single digits 1–9). |
| `modal_rhyme_count == n_verses` | 13–15 | 1.48 | **deterministic order** (modal ≤ total) with ρ = 0.951. This *is* rhyme-homogeneity, already established by H-NEW-2240. |
| `n_words == n_root_tokens` (T-LEMMA) | 12 | 0.28 | **deterministic order**, ρ = 0.9996. |

The strongest **non-mechanical** cell in the entire sweep is
`n_verses == Nöldeke revelation order` — 5 hits (Q 85 = 22 v., Q 87 = 19 v., Q 102 = 8 v.,
Q 106 = 4 v., Q 107 = 7 v.) against 0.886 expected, **p = 0.00201**. Against
α_cell = 7.5 × 10⁻⁵ that is **not significant**, and it reproduces across all three
rules-tuples because it is the same data. Reported here because a generator that hides its
best non-survivor is not a generator.

For completeness: **exactly 3 sūras have mushaf position equal to Tanzil revelation order**
— Q 38, Q 71, Q 82 — against an exact expectation of 0.886 and 114 opportunities. Chance.

---

## 6. The direction — the corpus under-produces exact coincidences

The locked direction was **EXCESS**. The aggregate result runs the other way:

- **432 of 657 cells fall below their exact expectation**; 193 above; 32 exactly on it.
- Decoupled observed-to-expected ratios: **E2 0.00, E3b 0.69×, E3a 1.14×, E3c 1.34×,
  E4 1.04× (N2), E1 1.38×** — and none of the above-1 ratios is significant at α_cell.

This is a **direction reversal in aggregate** and is published as such per Protocol §1.8,
with no massaging. It converges with H-NEW-2090 (which found sub-chance coincidence counts
on the position↔verse-count channel and attributed it to the mushaf's length-ordering) and
with H-NEW-2010 (whose meaningful root-balances were *under*-represented at p = 0.979).
**Three independent exhaustive generators, three sub-chance results.**

The honest reading is *not* that the Qurʾān avoids exact coincidences. With most cells
having expectations below 1, "observed 0 < expected 0.4" is the modal outcome of a discrete
right-skewed null, so the 432/657 tally overstates the effect. The defensible claim is the
weaker and sufficient one: **exact structural coincidence is not over-produced anywhere in
the scanned space, and in one geometry (E3b) it is measurably under-produced.**

---

## 7. Instrument controls (MW-6) — all fail-fast, all passed

- **Decoy axis A23** (seeded uniform random, participating in every E1 and E2 cell):
  **0 hits in 264 cells against 2.32 expected.** The instrument does not inflate.
- Σ verse counts = **6236** across 114 sūras (al-Suyūṭī, *al-Itqān*, nawʿ 17).
- QAC: **1,642 roots**, **4,832 lemmas**, **185 distinct root counts**, histogram head
  **{1:395, 2:197, 3:121, 4:96, 5:89}** — reproducing H-NEW-2010 exactly.
- Muqaṭṭaʿāt detector (which never names the letters it seeks): **30 loci in exactly 29
  sūras, 14 distinct graphemes**, from 228 scanned tokens — reproducing H-NEW-1740 §1 and
  H-NEW-2550 §2.
- **H-NEW-2090 replication**: cells 1, 2 and 6 reproduced exactly — 0 hits, 1 hit (Q 30),
  0 hits — *and* the exact rook-polynomial expectations reproduce its 10,000-permutation
  null means to three decimals.
- **Exact-engine validation**: both the hit-distribution engine and the mirror-pair engine
  were validated against **full brute-force enumeration of every permutation** on 10
  randomised small cases before the real run; every probability matched as an exact
  rational.

---

## 8. What this licenses, and what it forbids

**Licensed.** (i) The 1,581 exact coincidences are real and are published in full, with
denominators, in the run directory — they are facts about the text. (ii) The count↔location
coincidences are *completely* explained by the dependency between a root's frequency and
its distribution (§4, null N2). (iii) The 20 position/digit-reversal coincidences are facts
about base-10 numerals. (iv) The rhyme-homogeneity excess is real and is
[[h-new-2240-fasila-assonance-taxonomy|H-NEW-2240]]'s result, not a new one.

**Forbidden.** Any claim that an exact structural coincidence in the Qurʾān constitutes
evidence of numerical design *within the scanned space*. The space was swept exhaustively,
each hit was priced, and the highest-priced non-mechanical hit is 1,500× too common to
survive its own correction. **A property shared by 1 in 1,642 alternatives, drawn 124,148
times, is not a signature.**

This is the **fourth** exhaustive generator this project has run over exact-coincidence
space (H-NEW-2010 roots, H-NEW-2020 surface words, H-NEW-2090 surah arithmetic, and now
H-NEW-2660 across four new geometries) and the fourth to land NULL or sub-chance. Combined
with the per-claim audits (H-NEW-2000, H-NEW-2230, H-NEW-2040, H-NEW-1530, H-NEW-1600,
H-NEW-2410) and H-NEW-2550's exact 40,116,600-subset enumeration, **the numerical-iʿjāz
programme is now retired generatively, not just claim-by-claim.** The project's standing
positive results remain where they always were: in architecture (compression-tail laws,
R² = 0.986), in the iʿjāz anti-twin lock (r = −0.86), and in the classical scholars'
qualitative observations — al-Bāqillānī on *fawāṣil*, al-Khaṭṭābī on *maʿnā* — none of
which is arithmetic.

---

## 9. Honest limits

1. **Five types do not exhaust "structural coincidence."** A determined numerologist can
   always define a sixth. The defence is procedural, not exhaustive: the types were
   declared *before* the scan and swept *completely within themselves*, which is more than
   the literature under audit does. This is stated in the pre-registration, not discovered
   afterwards.
2. **The whole-space correction forecloses per-hit survival for E1, E3 and E4 by
   construction** — their denominators are bounded below by 1/114 and 1/N respectively,
   both ≫ α_hit. This was computed and written into pre-reg §5 *before the run*, and it is
   why those types are carried by cell-level tests and by their published denominators
   rather than by a survivor list. A reader who wants a per-hit-survivable design must use
   a smaller declared space, and must declare it in advance.
3. **The MECHANICAL screen is aggressive**: 90 of 109 E3a cells and 88 of 91 E3c cells are
   flagged. That is honest — most per-sūra metrics really are mechanically related — but it
   leaves the decoupled strata small (19 and 3 cells respectively), so those tests are
   underpowered.
4. **The single locked ρ = 0.70 threshold is a blunt instrument.** It lets through the
   `n_exclusive_roots` cluster at ρ = 0.59–0.61, which is transparently length-driven. The
   threshold was **not** moved after seeing this; the residual is instead located by an
   explicitly MW-7-capped, no-p-value diagnostic (§4 E1).
5. **E1 and E2's derived classes inherit the axis list**, and the axis list is a judgement
   call. It contains a decoy control and is drawn from quantities the project computed for
   other purposes, but a different defensible list would move counts by a few units.
6. **QAC v0.4 root/lemma boundaries are Dukes's analytic choices** (H-NEW-2230 §5). A ±1–2
   shift in a count could add or remove an individual E4 hit; it cannot change a
   combinatorial denominator.
7. **The 432/657 deficit tally overstates the direction reversal** because most cells have
   sub-1 expectations under a discrete right-skewed null (§6). The ratio statistics are the
   defensible form.
8. **`numpy` is used**, a disclosed deviation from Protocol §7.1. Every exact computation
   is stdlib integer / `fractions.Fraction` arithmetic and is reproducible without numpy;
   numpy is used only for the sampled guards.

---

## 10. Garden of forking paths

- **Choices made after seeing data: two, both disclosed, both in the conservative
  direction.**
  1. **The constructional screen was corrected mid-development.** The first implementation
     *inferred* functional dependence, which fires trivially on any injective vector —
     mushaf position, revelation order and Nöldeke order are permutations of 1–114 and so
     "determine" every other metric. That flagged 39 E3c cells and every M12/M13/M14 E3a
     cell as mechanical, suppressing genuinely open comparisons (mushaf position vs
     revelation order among them). It was replaced by the **declared** source map that
     pre-reg §6.2 actually specifies. The correction makes the screen *less* aggressive,
     i.e. it makes MORE hits eligible to be survivors, which is the conservative direction
     for a null-seeking test. Survivors before and after: 0 and 0.
  2. **The cell-level EXCESS label was tightened** to require `observed > expected`, not
     merely a small tail p. No cell changed status.
- **Pre-registered method strengthened in one place, weakened in one place.**
  - *Strengthened:* E3b's cell-level null was pre-registered for 10⁷ draws; an exact
    closed-form enumeration was found and is used as primary, with the pre-registered 10⁷
    sampler retained as a guard. Both are reported and they agree.
  - *Weakened, and disclosed:* E4's cell-level tail was pre-registered as an exact
    rook-polynomial computation. That formula is correct but **numerically infeasible at
    N = 1,642 / 4,832** — board degree ~10³, coefficients of ~10³ digits, and catastrophic
    cancellation whenever the observation sits far *below* the expectation, which is the
    regime every E4 cell is in. The exact **per-hit denominators** and the exact
    **expectations under both nulls** are retained; only the tail is sampled, at **10⁶
    draws** rather than 10⁷. This resolves to 10⁻⁶, which is 75× finer than
    α_cell = 7.5 × 10⁻⁵, and no E4 cell is anywhere near it — every E4 result is a deficit
    or at-chance under N2. The reduced budget cannot change any verdict, and pre-reg §5
    had already established that no E4 hit can survive at the per-hit level.
- **Run directory retained, not deleted:** `2026-08-07T013054Z` (superseded — halted
  mid-flight when the constructional-screen defect was found) is kept alongside the four
  development runs and the final primary and replication runs, per the project's standing
  no-deletion rule.
- **Alternatives considered and discarded before the lock:** location functions with a
  deterministic order relation to the count (`n_distinct_surahs ≤ count`) were rejected
  *before* the run precisely because a coincidence there would be mechanical; lām-alif as
  a 29th letter (not applicable here); an inferred rather than declared constructional
  screen (see above).
- **Why this test:** the numerological genre had been retired reactively, one claim at a
  time. It had never been swept generatively, with a denominator attached to every hit.

---

## 11. Cross-references

- **Model:** [[h-new-2550-muqattaat-phonetic-optimizer|H-NEW-2550]] — descriptively exact,
  statistically ordinary, both halves reported. This file applies that discipline at scale.
- **Siblings:** [[h-new-2010-root-frequency-balance-scan|H-NEW-2010]] and
  [[h-new-2020-word-balance-scan|H-NEW-2020]] — the two earlier exhaustive generators.
  H-NEW-2660 adds four geometries neither covered, and lands in the same place.
- **Converging null:** [[h-new-2090-surah-arithmetic|H-NEW-2090]] — sub-chance coincidence
  counts on the position↔verse-count channel; reproduced here exactly as an MW-6 control.
- **Challenging prior:** [[h-new-2240-fasila-assonance-taxonomy|H-NEW-2240]] — the
  rhyme-homogeneity result is the one genuine cell-level excess in this sweep, and it is
  *already known* and mechanically explained (modal ≤ total, ρ = 0.951). Reported rather
  than absorbed.
- **Instrument sources:** [[h-new-840-unified-architectural-score|H-NEW-840]] (UAS),
  [[h-new-750-per-surah-ijaz-signature|H-NEW-750]], [[h-new-111-fisher-rao-matrix|H-NEW-111]],
  [[h-new-720-canonical-adjacency-cost|H-NEW-720]], [[h-new-590-outlier-spectrum|H-NEW-590]]
  (Q 1 Δ_outlier = +27 pp, which explains the Q 1 cluster in E1).
- **Classical:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (*ʿadad al-suwar
  wa-l-āyāt*) — the 6,236 total is vindicated at exact integer precision and used as an
  MW-6 assertion. al-Khaṭṭābī's *iʿjāz al-maʿnā* and al-Bāqillānī's *iʿjāz al-fawāṣil*
  locate inimitability in language and meaning, **not** arithmetic — a position this file
  supports by exhaustion rather than by argument.
- **Method memory:** `feedback_rules_tuple_bidirectional` — three tuples were run; none
  rehabilitated any coincidence, and none demoted one either. Exactness turns out to be
  remarkably tuple-stable, because combinatorial denominators do not care about
  orthography.

---

## 12. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2660-exactness-hunt.md`
  (SHA-256 `aa0696c5d81a3170a6f5d190971e3201d8c2d8fa01ed262f439dae0a2dd39660`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2660.py` (runtime SHA-gated)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2660.json`
- run dirs: `findings/phase-b-hypotheses/runs/h-new-2660/` — primary, replication
  (seed 20260519), one halted superseded run and four development runs, **all retained**
- per-family dumps in every run dir: `cells-E{1,2,3a,3b,3c,4}.json`,
  `hits-E{…}.json`, `mechanical.json`, `cbm.json`, `e2-nearmiss-full.json`

---

*H-NEW-2660 completed 2026-08-07 by Waiel Al-Shujaa. 124,148 exact coincidences scanned,
1,581 found, 0 survived their own denominators. The root for patience occurs one hundred
and three times and stops in sūra one hundred and three, at the word patience. It is true,
it is beautiful, and it is worth one in one thousand six hundred and forty-two. Reporting
the second fact alongside the first is the whole of the discipline.
Bismillāhi al-Raḥmāni al-Raḥīm.*
