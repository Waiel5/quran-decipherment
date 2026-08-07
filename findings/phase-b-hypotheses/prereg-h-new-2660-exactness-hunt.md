---
id: H-NEW-2660
title: "PRE-REGISTRATION — The exactness hunt: an exhaustive generator over zero-tolerance structural coincidences, each with its own combinatorial denominator"
type: pre-registration
status: LOCKED-BEFORE-COMPUTATION
date: 2026-08-07
author: Waiel Al-Shujaa
phase: B
seed: 20260509
seed_replication: 20260519
rules_tuples: 3 (T-ROOT primary, T-LEMMA, T-NORM)
direction_lock: EXCESS (more exact coincidences than the null) — every cell, every type
---

# PRE-REGISTRATION — H-NEW-2660


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Nothing in this file may be amended after the SHA-256 below is computed.** The run
script embeds the SHA as a literal and raises `SystemExit` on mismatch. Seed 20260509;
replication seed 20260519. Immutable run directory
`findings/phase-b-hypotheses/runs/h-new-2660/<UTC timestamp>/`. Run directories are never
deleted, including superseded ones.

---

## 0. The most likely outcome, stated before the run

**I expect ZERO non-mechanical survivors.** Every prior exhaustive generator this project
has run over exact-coincidence space has landed there:

- H-NEW-2010: 118,584 exact root-count balances exist; the semantically meaningful ones
  are *under*-represented (1 observed vs ~4 expected, p = 0.979, direction REVERSED).
- H-NEW-2020: 3,734,882 exact surface-word balances exist; 1 of 13 famous antonym pairs
  balances, and that one (ṣayf/shitāʾ) is a single-verse co-occurrence.
- H-NEW-2090: 0 of 8 arithmetic position↔verse-count cells exceed chance; most fall
  *below* chance.
- H-NEW-2040: every systematic abjad↔structure correlation NULL; the one exact hit
  (al-Ḥadīd = 57) is exactly the chance expectation (perm-p = 0.172).
- H-NEW-2550: al-Zamakhsharī's muqaṭṭaʿāt claim is a *global minimum* and 1,024,500 of
  40,116,600 subsets tie it (p_exact = 0.0255).

**A finding of "0 survivors out of K exact coincidences scanned" is the deliverable, not a
failure.** It is pre-registered here as the expected result and will be reported as the
headline. I will not manufacture a positive result. If a survivor does appear, it must
carry its exact denominator and a stated mechanism, or it does not go in the finding file.

---

## 1. What this is, and what it is not

Most famous Qurʾān-miracle claims have the form "X is EXACTLY equal to Y." They have been
adjudicated one at a time, reactively, as apologists proposed them. **This is the
opposite: a generator.** Five coincidence TYPES are declared *here*, before any scan.
Each type is then swept EXHAUSTIVELY, and — the entire point — **for every exact
coincidence found, the number of alternative configurations that would also have been
exact is computed under an explicit null.** That denominator is what separates a fact from
a combinatorial inevitability, and it is precisely what the numerological literature never
computes.

**This is not a re-run of prior art.** The following are settled and are cited, not
re-tested: exact equality between root counts (H-NEW-2010), between surface-word counts
(H-NEW-2020), between abjad sums and structural integers (H-NEW-2040), between surah
position and verse count (H-NEW-2090), Code-19 divisibility (H-NEW-1530, H-NEW-1600),
number-word census (H-NEW-2410), QAC-lemma re-run of the balance claims (H-NEW-2230),
per-claim balance audit (H-NEW-2000). Where a declared cell of this test coincides with a
prior-art cell, it is marked **PRIOR-ART-REPLICATION**, used as an MW-6 instrument control,
counted in the Bonferroni denominator (which only tightens α), and **claimed as a
discovery under no circumstances**.

The space scanned here is the space those tests did **not** cover: rank-extremum
coincidences across axes, exact set coincidences between surah classes, exact integer
equalities among per-surah metrics in three geometries, and exact count↔location
coincidences over the whole root/lemma inventory.

---

## 2. Frozen inputs (SHA-256, verified at runtime; mismatch ⇒ SystemExit)

| Path | SHA-256 |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `quran-text/quran-min-tashkeel.json` | `87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36` |
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| `data/hafs-verse-counts.tsv` | `e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba` |
| `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| `findings/phase-b-hypotheses/csv/h-new-840.json` | `e16a0f70aa842fbe650f2b14874a3f27b176193b86d7964fa9c6b76620ff2aa0` |
| `findings/phase-b-hypotheses/csv/h-new-750.json` | `6f2fd5922e0c59506e20e68318c858b73a317cd9944b1d5d2df6565f6df9fe59` |
| `findings/phase-b-hypotheses/csv/h-new-111.json` | `4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc` |
| `findings/phase-b-hypotheses/csv/h-new-720.json` | `0b342b20639aaf6100cf07d17aca9c9c28f89bf4c127aef3ffd059edb51d4c97` |

---

## 3. Rules-tuples (three, all run, all reported)

- **T-ROOT (primary)** — `(no-tashkeel, orthographic-token, graphemes U+0621–U+064A
  unnormalised, QAC-ROOT as the morphological unit, basmala-counted-only-in-Q1,
  Hafs-Kūfan, Mashriqī)`.
- **T-LEMMA (morphological-unit fork)** — identical, except **QAC-LEM replaces QAC-ROOT**
  everywhere a morphological unit is required (axes A06/A07, metrics M06/M07, and the E4
  unit inventory).
- **T-NORM (orthographic/tashkeel fork)** — identical to T-ROOT, except every grapheme is
  first normalised: `أ إ آ ٱ → ا`, `ى → ي`, `ة → ه`, `ؤ → و`, `ئ → ي`, taṭwīl `ـ` deleted.
  This changes letter counts, type counts, and the verse-final rhyme letter. Rhyme is
  extracted from `quran-min-tashkeel.json` in T-ROOT/T-LEMMA and from
  `quran-full-tashkeel.json` in T-NORM (diacritics stripped, then normalised).

Rules-tuple sensitivity is bidirectional: a fork may rehabilitate a coincidence as easily
as demote it. All three tuples are reported with equal prominence; no tuple is dropped.

---

## 4. The five declared coincidence TYPES

### TYPE E1 — Exact rank-extremum coincidences across independent per-surah axes

**Locked axis list (22).** All are per-surah numeric vectors over Q1–Q114.

| id | axis | source |
|:--|:--|:--|
| A01 | `n_verses` | `data/hafs-verse-counts.tsv` |
| A02 | `n_words` (whitespace tokens) | no-tashkeel corpus |
| A03 | `n_letters` (graphemes) | no-tashkeel corpus |
| A04 | `n_word_types` (distinct surface tokens) | no-tashkeel corpus |
| A05 | `n_root_tokens` (QAC segments carrying ROOT) | QAC v0.4 |
| A06 | `n_distinct_roots` | QAC v0.4 |
| A07 | `n_distinct_lemmas` | QAC v0.4 |
| A08 | `n_surah_hapax_roots` (root occurs once *within* the surah) | QAC v0.4 |
| A09 | `n_exclusive_roots` (root occurs in this surah and no other) | QAC v0.4 |
| A10 | `mean_verse_letters` = A03/A01 | derived |
| A11 | `mean_verse_words` = A02/A01 | derived |
| A12 | `n_rhyme_classes` (distinct verse-final letters) | min/full-tashkeel |
| A13 | `modal_rhyme_count` (verses ending in the modal final letter) | min/full-tashkeel |
| A14 | `type_token_ratio` = A04/A02 | derived |
| A15 | `revelation_order` (Tanzil Egyptian Standard) | `data/revelation-order.csv` |
| A16 | `noldeke_order` | `data/revelation-order.csv` |
| A17 | `UAS` | `csv/h-new-840.json` |
| A18 | `rhyme_entropy_nats` | `csv/h-new-750.json` |
| A19 | `mean_content_distance` | `csv/h-new-750.json` |
| A20 | `local_cohesion` | `csv/h-new-750.json` |
| A21 | `fr_centroid_dist` (mean Fisher-Rao distance to the other 113) | `csv/h-new-111.json` |
| A22 | `max_neighbour_tsp_cost` | `csv/h-new-840.json` (`max_cost`) |
| **A23** | **DECOY** — seeded uniform random vector (MW-6 instrument control) | seed 20260509 |

A23 is a **decoy axis**: it must land at chance. It participates in every E1 and E2 cell
and is counted in the Bonferroni denominator. If the decoy produces an above-chance
coincidence rate the instrument is broken and the whole finding is void.

**Sweep.** For every unordered pair of distinct axes `{a,b}` (C(23,2) = 253) and every one
of 4 extremum modes — `argmax(a)==argmax(b)`, `argmin(a)==argmin(b)`,
`argmax(a)==argmin(b)`, `argmin(a)==argmax(b)` — record whether the two extremum surahs
are EXACTLY the same surah. Ties are broken by **lowest surah number** (locked).

**Candidates:** 253 × 4 = **1,012 per rules-tuple**.

**Exact denominator (closed form, no sampling).** Null N1 = each axis's value vector is an
independent uniform random permutation of its own observed values across the 114 surahs.
Under N1 the extremum position of a tie-free axis is uniform on {1..114}, so
`p_exact = Σ_{s=1}^{114} P(ext_a = s) · P(ext_b = s)`, computed exactly from each axis's
tie structure. For tie-free axes this is exactly **1/114 = 0.0087719**.

**Cell-level family test.** Under N1 the 46 extremum positions (23 axes × 2 modes) are
independent uniform draws, so the total coincidence count over all 1,012 cells is
simulated exactly by drawing 46 uniform positions per replicate: **10,000,000 replicates**,
seed 20260509, replication 20260519.

---

### TYPE E2 — Exact SET coincidences among pre-declared surah classes

**Base classes (18), every one derivable from a frozen input — no invented gazetteer.**

| id | class |
|:--|:--|
| C01 | muqaṭṭaʿāt surahs (detector: first token of v.1/v.2 carrying no ordinary vocalisation) |
| C02 | ḥawāmīm (muqaṭṭaʿāt string == حم) |
| C03 | ALM family (muqaṭṭaʿāt string == الم) |
| C04 | ALR family (muqaṭṭaʿāt string == الر) |
| C05 | Meccan (`revelation-order.csv` period) |
| C06 | Medinan |
| C07 | Nöldeke Early Meccan |
| C08 | Nöldeke Middle Meccan |
| C09 | Nöldeke Late Meccan |
| C10 | Nöldeke Medinan |
| C11 | musabbiḥāt (v.1 contains a QAC `sbH`-root verb) |
| C12 | surahs whose v.1 first token is قل |
| C13 | surahs containing ≥1 sajdah glyph U+06E9 (full-tashkeel) |
| C14 | surahs whose v.1 *is* the basmala |
| C15 | surahs with no basmala header |
| C16 | surahs whose v.1 first token begins with و |
| C17 | surahs whose v.1 first token is يا |
| C18 | rhyme-homogeneous surahs (`n_rhyme_classes == 1`) |

**Derived classes.** For each of the 23 axes, `top-k` and `bottom-k` for k ∈ {7, 14, 29},
ties broken by lowest surah number: 23 × 2 × 3 = **138 derived classes**.

**Sweep.** All unordered pairs of distinct classes with **equal cardinality** (exact set
equality is impossible otherwise). Report exact equalities AND, for every scanned pair,
the Jaccard index, so the near-miss distribution is published in full.

**Exact denominator (closed form).** Null N1 = one class is fixed, the other is a uniform
random k-subset of the 114 surahs. Then

`p_exact(exact equality) = 1 / C(114, k)` — exactly enumerated, never sampled.

`p_exact(near-miss with overlap j) = Σ_{i≥j} C(k,i)·C(114−k, k−i) / C(114,k)` — the exact
hypergeometric upper tail. Every scanned pair carries this number.

Monte Carlo is **not** used here: at k = 7 the exact probability is 1/1.9×10¹⁰ and 10⁷
draws could not resolve it. Exact enumeration is strictly stronger.

---

### TYPE E3 — Exact integer equalities among per-surah structural metrics

**Locked integer-metric list (14).** Only integers, since exact equality is the observable.

`M01 n_verses · M02 n_words · M03 n_letters · M04 n_word_types · M05 n_root_tokens ·
M06 n_distinct_roots · M07 n_distinct_lemmas · M08 n_surah_hapax_roots ·
M09 n_exclusive_roots · M10 n_rhyme_classes · M11 modal_rhyme_count ·
M12 mushaf_position · M13 revelation_order · M14 noldeke_order`

**Three geometries, all swept exhaustively.**

- **E3a — self-referential.** For each metric `m`, each of 8 locked target functions `f`,
  and each surah `s`: is `m(s) == f(s)` exactly?
  `F1 f(s)=s · F2 f(s)=115−s · F3 f(s)=2s · F4 f(s)=digit-reverse(s) ·
   F5 f(s)=revelation_order(s) · F6 f(s)=115−revelation_order(s) · F7 f(s)=n_verses(s) ·
   F8 f(s)=digit-sum(s)`
  The three tautological cells `(M01,F7)`, `(M12,F1)`, `(M13,F5)` are excluded.
  **Candidates: (14×8 − 3) × 114 = 109 × 114 = 12,426 per tuple.**
  Cells `(M01,F1)`, `(M01,F3)`, `(M01,F4)` are **PRIOR-ART-REPLICATION** of H-NEW-2090
  cells 1, 2 and 6 and serve as MW-6 controls (must return 0, 1 [Q30], 0 hits).

- **E3b — mirror-pair.** For each metric `m` and each of the 57 mirror pairs
  `(i, 115−i)`, i = 1..57: is `m(i) == m(115−i)` exactly?
  **Candidates: 14 × 57 = 798 per tuple.**

- **E3c — cross-metric within surah.** For each unordered pair of distinct metrics
  `{m,m'}` (C(14,2) = 91) and each surah: is `m(s) == m'(s)` exactly?
  **Candidates: 91 × 114 = 10,374 per tuple.**

**E3 total: 23,598 per tuple.**

**Exact denominator (closed form, no sampling) for E3a and E3c.** Null N1 = the metric
vector `m` is a uniform random permutation of its own values across the 114 surahs, the
target vector held fixed. Then for a single candidate at surah `s`,

`p_exact = mult_m(target(s)) / 114`

where `mult_m(v)` is the number of surahs whose metric `m` equals `v`. This is exact and
requires no draws. **The full null distribution of the cell's hit-count is also exact**,
via the classical rook-polynomial / inclusion–exclusion "hits" formula:
with `r_k` the coefficient of `x^k` in `∏_v Σ_j C(n_v,j)·C(t_v,j)·j!·x^j` (`n_v` = the
multiplicity of value `v` in the metric vector, `t_v` = its multiplicity in the target
vector), `P(M = h) = Σ_{k≥h} (−1)^{k−h} C(k,h) · r_k · (114−k)! / 114!`, computed in exact
rational arithmetic. Monte Carlo is not needed and is not used.

**E3b** has no closed form available here and is computed by **10,000,000 seeded
permutation draws** per cell (seed 20260509, replication 20260519).

---

### TYPE E4 — Exact count ↔ location coincidences over the full morphological inventory

The mechanised form of the popular claim "the word X occurs exactly N times, and N is the
number of the surah where it lives."

**Locked location functions (5).** For each morphological unit `u` (QAC root under
T-ROOT/T-NORM; QAC lemma under T-LEMMA), with total corpus count `c(u)`:
`L1 first-attestation surah number · L2 last-attestation surah number ·
 L3 modal surah number (most attestations; ties → lowest surah) ·
 L4 n_verses of the modal surah · L5 115 − first-attestation surah number`

None of the five has a deterministic order relation to `c(u)` — functions with one (e.g.
`n_distinct_surahs ≤ c`) were considered and **discarded before the lock** precisely
because the coincidence would be mechanical.

**Sweep.** Every unit × every function: `c(u) == L_j(u)` exactly.
**Candidates: 5 × 1,642 = 8,210 (T-ROOT, T-NORM); 5 × 4,832 = 24,160 (T-LEMMA).**

**Exact denominator (closed form).** Null N1 = the count vector is a uniform random
permutation across units, location vectors fixed. Then

`p_exact = h(L_j(u)) / N_units`

where `h(N)` is the number of units whose corpus count is exactly `N`. Exact. The cell's
full hit-count distribution uses the same exact rook-polynomial formula as E3a.

**Secondary null N2 (MW-3 alternative model).** `c(u)` and `L_j(u)` are genuinely
dependent — a frequent root attests early and everywhere. N2 therefore permutes the count
vector **only within deciles of `n_distinct_surahs`**, preserving that dependency.
10,000,000 seeded draws. Both nulls reported for every E4 cell; N1 is primary.

---

### TYPE E5 — Exact corpus-level integer coincidences (declared, capped, no p-value promotion)

A small closed set of whole-corpus exact identities is computed and published as
**descriptive facts with exact denominators**, never promoted: Σ verse counts, Σ surah
numbers, their difference and factorisations, the number of surahs whose verse count is a
prime, and the exact multiplicity of every corpus constant in the metric histograms.
**E5 contributes 0 candidates to the Bonferroni denominator, carries no p-value, and can
produce no survivor.** It exists so that any "corpus constant" a reader might notice has
its denominator already on the page. (H-NEW-2090 §D1 already computed several of these;
they are reproduced as MW-6 controls.)

---

## 5. Bonferroni over the ENTIRE scanned space — both thresholds stated up front

Two corrections, both computed from the scan itself, both reported:

- **α_hit = 0.05 / K_candidates** — the primary threshold, applied to the `p_exact` of
  **every individual exact coincidence**. `K_candidates` is the total number of individual
  zero-tolerance coincidence opportunities scanned across E1–E4 and all three rules-tuples,
  including PRIOR-ART-REPLICATION and DECOY cells. **Pre-run estimate:
  K_candidates ≈ 1,012×3 + |E2 pairs|×3 + 23,598×3 + (8,210 + 24,160 + 8,210)
  ≈ 1.2 × 10⁵, giving α_hit ≈ 4 × 10⁻⁷.** The exact value is computed by the script and
  reported; only the *rule* is locked here.
- **α_cell = 0.05 / K_cells** — the secondary threshold, applied to cell-level
  excess tests, where `K_cells` is the number of cell-level p-values computed.

Where the two disagree, **α_hit governs the survivor list** and α_cell governs the
cell-level commentary. Both are reported for every claim. A correction that *tightens* α
is self-verifying and may be applied; a correction that *loosens* it may not.

At α_hit ≈ 4 × 10⁻⁷ the arithmetic is transparent and is stated now, before the run: an
E2 exact set coincidence survives iff `C(114,k) > 1/α_hit`, i.e. **k ≥ 4**
(C(114,4) = 7,160,245; C(114,3) = 241,024 does not clear it). No E1 hit can survive at the
per-hit level (1/114 ≫ α_hit). No E3 or E4 hit can survive at the per-hit level
(`p_exact ≥ 1/114` and `≥ 1/N_units` respectively). **Therefore the only type that can
produce a per-hit survivor is E2, and only for classes of size ≥ 4.** This is stated in
advance so that the finding cannot later be presented as if the threshold had been chosen
to fit the outcome. E1/E3/E4 remain fully informative through their cell-level excess
tests and through the published denominators themselves.

---

## 6. The MECHANICAL screen (locked before observation)

An exact coincidence is labelled **MECHANICAL** — reported in full, never counted as a
survivor — if any of the following holds:

1. **Correlation coupling.** The two axes / metrics have |Spearman ρ| ≥ 0.70 over the 114
   surahs. (For E2, the two classes derive from the same axis, or from two axes with
   |ρ| ≥ 0.70.)
2. **Constructional dependence.** One quantity is an input to the other's construction.
   Declared list: A17 UAS ← {A22, sig_A of h-new-750}; A10 ← A03,A01; A11 ← A02,A01;
   A14 ← A04,A02; A21 ← the same Fisher-Rao matrix as A19/A20.
3. **Deterministic order relation.** One quantity is provably ≤ or ≥ the other for all 114
   surahs (e.g. M06 ≤ M05, M04 ≤ M02, M11 ≤ M01).
4. **Definitional set relation.** For E2, one class is a subset of the other by
   construction (e.g. C02 ⊂ C01, C07 ⊂ C05).

The ρ threshold 0.70 is locked here; which pairs exceed it is unobserved at lock time.
Every family test is reported **twice** — over all cells, and over the DECOUPLED stratum
only.

---

## 7. Direction lock

**EXCESS**, for every cell-level test in every type: the pre-registered alternative is
that the corpus produces MORE exact coincidences than the null. A **DEFICIT** (observed
below the null median) is a pre-commit-direction reversal and is published as
**NULL-REVERSED with full prominence** per Protocol §1.8 — not massaged, not re-pointed,
not silently re-registered. H-NEW-2010 and H-NEW-2090 both landed there and this test may
too.

---

## 8. Decision language — every outcome, including zero survivors

**Per individual coincidence:**

| label | condition |
|:--|:--|
| **SURVIVOR** | exact hit, `p_exact < α_hit`, and NOT flagged MECHANICAL |
| **MECHANICAL-EXACT** | exact hit that trips any §6 screen — reported with its denominator, never a survivor |
| **CBM** (confirmed-but-meaningless) | exact hit with `p_exact ≥ α_hit` — descriptively exact, statistically ordinary |
| **PRIOR-ART-REPLICATION** | exact hit in a cell already settled by a cited finding — MW-6 control only |

**Per cell:**

| label | condition |
|:--|:--|
| **CELL-EXCESS** | observed hit-count exceeds the null at `p < α_cell`, direction EXCESS |
| **CELL-NULL** | not significant in the locked direction |
| **CELL-DEFICIT** | observed strictly below the null median — reported as a direction reversal |

**Per family (the headline):**

| label | condition |
|:--|:--|
| **HUNT-NULL** | **0 SURVIVORs.** The pre-registered most-likely outcome. Reported as the headline result: the exactness genre is retired over the whole scanned space, with `K_candidates` and `α_hit` stated. |
| **HUNT-POSITIVE** | ≥1 SURVIVOR. Each survivor is published with its exact denominator, its rules-tuple stability across all three tuples, and a stated mechanism. A survivor that appears under one tuple only is labelled **RULES-TUPLE-FRAGILE**. |
| **INSTRUMENT-VOID** | the DECOY axis A23 produces an above-chance coincidence rate, or any MW-6 assertion fails. The entire finding is void and is published as such. |

**Zero survivors is a success condition of this pre-registration, not a failure.**

---

## 9. MW-1 … MW-7 compliance

- **MW-1 (instrument-prior)** — axes, classes, metrics, target functions, location
  functions, both nulls, both thresholds, the MECHANICAL screen, the direction lock and
  all four verdict vocabularies are fixed in this file before any coincidence is scanned.
- **MW-2 (corpus-prior)** — E1's per-hit and E2's per-hit and near-miss denominators are
  **exact closed forms**; E3a/E3c/E4's per-hit denominators and full cell-level null
  distributions are **exact** (rook-polynomial inclusion–exclusion in rational
  arithmetic). Only E1's family test, E3b and E4's N2 use sampling, each at
  **10,000,000 draws** — 1,000× the Protocol §7.1 minimum.
- **MW-3 (alternative models)** — three rules-tuples; two nulls for E4; every family test
  reported over both the full cell set and the DECOUPLED stratum.
- **MW-4 (over-fitting)** — no fitted parameters anywhere; no statistic has a free
  constant.
- **MW-5 (replication)** — every sampled quantity re-run at seed 20260519. Exact
  quantities need none.
- **MW-6 (instrument-control)** — all fail-fast at runtime:
  (a) DECOY axis A23 must land at chance;
  (b) 1,642 QAC roots, 185 distinct root-counts, count-histogram head
      `{1:395, 2:197, 3:121, 4:96, 5:89}` — reproducing H-NEW-2010;
  (c) Σ verse counts == 6236, 114 surahs — reproducing al-Suyūṭī *al-Itqān* nawʿ 17;
  (d) the muqaṭṭaʿāt detector returns exactly 29 surahs and 14 distinct letters —
      reproducing H-NEW-1740 §1 and H-NEW-2550 §2;
  (e) E3a cells `(M01,F1)`, `(M01,F3)`, `(M01,F4)` return 0, 1 (Q30) and 0 hits —
      reproducing H-NEW-2090 cells 1, 2, 6;
  (f) the exact rook-polynomial engine is validated against brute-force enumeration on
      randomised small cases (n ≤ 8, all permutations) before the real run;
  (g) `Σ_{k} C(114,k)`-style enumeration constants asserted where used.
  Any failure ⇒ `SystemExit`.
- **MW-7 (post-hoc cap)** — any coincidence noticed during the run that does not belong to
  a declared type is reported descriptively, carries **no p-value**, adds **no cell**, and
  can never be a survivor. Type E5 is pre-emptively placed in this category.

---

## 10. Disclosure of pre-lock knowledge (honest, and it matters)

Before this file was locked I had:

1. Read H-NEW-2000, 2010, 2020, 2040, 2090, 2230, 2410, 2550 and the FRONTIER-MAP. These
   publish many exact facts that therefore cannot be discoveries here: 118,584 exact root
   balances; 3,734,882 exact word balances; 0 surahs with `verse_count == position`;
   Q 30 al-Rūm = 2×30; 6 surahs where position divides verse count; al-Ḥadīd name-abjad
   = 57; `dunyā` = 115; `shahr`-singular = 12; `Iblīs` = 11; rebuke-*kallā* = 33. All are
   cited as prior art or used as MW-6 controls; none is claimed.
2. Parsed QAC and observed 1,642 roots / 4,832 lemmas / 185 distinct root counts and the
   histogram head. **These are H-NEW-2010's published numbers**, re-derived as an
   instrument check, and they are used as MW-6 assertions (b) above.
3. Verified the shape — not the content — of every frozen input.

I had **not** computed any E1, E2, E3 or E4 coincidence, any denominator, or any p-value.
The entire empirical content of this test — which coincidences exist, how many, and what
each is worth against its own combinatorial denominator — is unobserved at lock time.

---

## 11. Honest limits, acknowledged in advance

1. **Type declaration is itself a choice.** Five types do not exhaust "structural
   coincidence". A determined numerologist can always define a sixth. The defence is that
   the types are declared *before* the scan and swept *exhaustively within themselves* —
   which is strictly more than the literature under audit ever does — not that the space
   is complete.
2. **The axis and class lists are judgement calls.** They are locked here, they include a
   decoy control, and they are drawn from quantities the project already computed for
   other reasons. A different defensible list would move counts by a few units. It cannot
   convert an exact 1/C(114,7) into an ordinary event.
3. **α_hit's arithmetic forecloses per-hit survival for E1/E3/E4** (§5). This is a real
   limitation of a whole-space correction, stated in advance rather than discovered
   afterwards; those types are carried by their cell-level tests and by their published
   denominators.
4. **The N1 nulls destroy inter-axis dependency by construction.** Where that dependency
   is real, the coincidence is *explained*, not *designed* — which is what the MECHANICAL
   screen and the reported Spearman ρ exist to expose. E4's N2 is the one place a
   dependency-preserving null is available and it is run.
5. **QAC v0.4 lemma/root boundaries are Dukes's analytic choices** (per H-NEW-2230 §5). A
   ±1–2 shift in a count is possible; it cannot rescue or destroy a result whose
   denominator is combinatorial.
6. **`numpy` is used** — a disclosed deviation from Protocol §7.1 (stdlib-only). The
   justification is the 10⁷-draw sampled cells; every exact computation is stdlib integer
   / `fractions.Fraction` arithmetic and is independently reproducible without numpy.

---

## 12. Deliverables

- pre-reg: this file (SHA-256 embedded in the script, verified at runtime)
- script: `findings/phase-b-hypotheses/scripts/h-new-2660.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2660.json`
- run dir: `findings/phase-b-hypotheses/runs/h-new-2660/<UTC timestamp>/` (never deleted)
- finding: `findings/phase-b-hypotheses/h-new-2660-exactness-hunt.md`

The finding file must report, at minimum: **total candidates scanned**, **both corrected
thresholds**, **survivor count**, **the full survivor table with denominators**, **the
near-miss table**, and **every cell-level verdict including the deficits**.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any coincidence was scanned. The denominator
is the finding. Bismillāhi al-Raḥmāni al-Raḥīm.*
