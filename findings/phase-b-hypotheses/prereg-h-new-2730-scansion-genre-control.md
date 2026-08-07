---
id: H-NEW-2730
title: Pre-registration — Does H-NEW-2690's scansion ordering survive a matched-partition control, and is d_min length-invariant in practice?
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any partitioned or length-stratified value was computed
family: SCANSION-2026-08-07-B
parent: H-NEW-2690
method_parent: H-NEW-2680 / H-NEW-2720
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 4
alpha_bonferroni: 0.0125
---

# Pre-registration — H-NEW-2730

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2730.py`.**
Directions are locked in §6, decision rules in §7, failure conditions in §11. The runner's
verdict logic must be diffed against §7 before any verdict is declared — this is
`STATE-OF-THE-PROJECT-2026-08-07.md` §4.4, and it is the rule that retracted H-NEW-2600's
published verdict.

---

## 1. Why this test exists

H-NEW-2690 reported the one passing discriminating result of the 2026-08-07 session. On
`d_min` — the length-invariant distance to the nearest classical metrical template — it found
**poetry < Qurʾān < prose**, both directions locked in advance, both passing at p = 1×10⁻⁴ in
both pausal rules-tuples, on a scanner that recovered 3/3 muʿallaqāt meters at 0.771 per-bayt
accuracy.

**It has not been genre-controlled, and it says so itself.** Its honest-limits §4.1 reads:

> `d_min` is designed to be length-invariant … but **designed-to-be-invariant is not the same
> as verified-invariant.** A matched-partition control on this statistic is REQUIRED before
> this is cited as a discriminating result.

Today's base rate makes that limit urgent rather than formal. H-NEW-2720 found **0 of 9**
standing laws discriminate the Qurʾān from length-matched partitions of al-Bukhārī and
al-Jāḥiẓ, and that **unit size alone explained 91.5 % of the compression tail and about half
the iʿjāz anti-twin**. H-NEW-740 *had* a genuine, pre-registered cross-corpus control and
still got its answer backwards, because the control was not matched on the variable driving
the statistic, and because its honest-limits section reasoned about the *direction* of a bias
instead of measuring it.

### 1.1 The specific reason for concern, stated before any test statistic was computed

The three arms of H-NEW-2690 are ordered in unit length exactly as they are ordered in
`d_min`. Measured before locking, from the frozen inputs, as a corpus fact and not a test
statistic:

| arm | unit | median words/unit | mean words/unit |
|:--|:--|--:|--:|
| poetry | muʿallaqa bayt | ≈ 9.6 (mean; 2,299 words / 240 abyāt) | 9.6 |
| **Qurʾān** | verse | **10** | 12.4 |
| prose | Sunan al-Dārimī sentence, split on `[.؟!]`, ≥ 10 Arabic letters | **36** | 38.0 |

**The reported ordering poetry < Qurʾān < prose is monotone in median unit length: 9.6 < 10 <
36.** A three-way ordering is ordinarily harder to fake than a two-way extremity claim — that
is H-NEW-2690's stated defence — but that argument fails precisely when the nuisance parameter
is itself monotone across the three arms, which is the case here. The prose arm's units are
**3.6× the Qurʾān's in the median**, a mismatch of the same kind and larger magnitude than the
30-bayt-block mismatch that reversed H-NEW-740.

### 1.2 The mechanism by which `d_min` could fail to be length-invariant

`d_min` normalises by unit length L and tiles each template to exactly L at every phase, so it
is length-invariant *in its units*. That is not the same as being distributed identically
across L. `d_min` is a **minimum over ~200 template candidates** (16 meters × up to 14 phases;
77 of them distinct at L = 28). For a string of length L the normalised distance to any single
fixed template concentrates around a constant with fluctuation of order L^(−1/2); the minimum
over N candidates sits roughly `sqrt(2 log N / L)` below that constant. **The minimum-of-many
therefore falls as L falls, mechanically, even for random strings.** Short units look more
metrical than long ones for reasons that have nothing to do with metre.

H-NEW-2690's own length-invariance check (its §4, "median at len ≈ 20 / 24 / 28 → 0.136 /
0.163 / 0.107 — flat") tests three bins inside a span of 8 syllables, on 240 poetry abyāt, and
its three values are non-monotone. **It does not cover the range that separates the arms** —
the Qurʾān's own verse syllable-lengths run from below 10 to above 65 (p10 = 10, median = 28,
p90 = 65, measured before locking). Nothing in the record verifies invariance over that range.
This is exactly the pattern `STATE-OF-THE-PROJECT-2026-08-07.md` §4.5 names: *never assert a
robustness property — compute it.*

### 1.3 The expected outcome, stated before running

**I expect H-NEW-2690's ordering to fall, and I am running this test in order to kill it.**
Killing it is a success: it is the last discriminating result standing, and it should not
stand on an unverified invariance assumption. If it survives a properly matched control that
is a genuinely important positive — the only one this project has — and it will be reported at
exactly its true strength and no more.

---

## 2. The severe data limitation that shapes this design, stated first

**Scansion requires vocalisation. The genre-control corpora used by H-NEW-2680 and H-NEW-2720
are unvocalised and cannot be scanned at all.** Measured before locking:

| file used by 2680/2720 | diacritics per Arabic letter | scannable |
|:--|--:|:--|
| `data/baseline-corpora/raw/bukhari-noquran.txt` | **0.0000** | **no** |
| `data/baseline-corpora/raw/jahiz-hayawan.txt` | **0.0000** | **no** |
| `data/baseline-corpora/raw/diwan-*.txt` (all 8) | **0.0000** | **no** |

An exhaustive sweep of `data/` for files with ≥ 2,000 Arabic letters and a diacritic ratio
≥ 0.40 returns **only** the Qurʾān, the ḥadīth collections, Ibn Kathīr's tafsīr, and the three
vocalised muʿallaqāt. There is **no vocalised adab prose on disk**, so **al-Jāḥiẓ cannot be
tested on this statistic by any means**. Ibn Kathīr is disqualified as a genre control: its
Arabic content is ḥadīth quotation embedded in English commentary, and it quotes the Qurʾān
throughout.

**al-Bukhārī, however, is recoverable.** `data/literature/hadith/ahmedbaset-json/db/by_book/
the_9_books/bukhari.json` is the same Ṣaḥīḥ, **vocalised at ratio 0.770**, 522,354 words under
2680's `normalise_words`. It was not available to 2720's instrument because 2720 needed no
vocalisation and used the plain-text edition. This test uses the vocalised edition, so the
task's request for a matched al-Bukhārī partition **is** satisfied.

### 2.1 Locked corpus inventory

| role | source | voc. ratio | words after `normalise_words` | partition slack |
|:--|:--|--:|--:|--:|
| **Qurʾān** | `quran-text/quran-full-tashkeel.json`, 6,236 canonical verses | 0.918 | — | native |
| **prose A** | Sunan al-Dārimī (`…/the_9_books/darimi.json`, `hadiths[].arabic`) | 0.866 | 167,564 | +85,189 |
| **prose B** | Ṣaḥīḥ al-Bukhārī (`…/the_9_books/bukhari.json`, `hadiths[].arabic`) | 0.770 | 522,354 | +439,979 |
| **poetry** | 3 vocalised muʿallaqāt (Imruʾ al-Qays, Zuhayr, ʿAmr b. Kulthūm) | 0.72–0.84 | 2,299 | **−80,076** |
| al-Jāḥiẓ | `jahiz-hayawan.txt` | **0.000** | — | **UNTESTABLE** |

**Prose A is the corpus H-NEW-2690's own prose arm used**, so the matched partition re-cuts
the very stream that produced "prose > Qurʾān". That is the primary control. Prose B is a
second, independently compiled ḥadīth collection.

**Poetry cannot support the 6,236-unit partition.** 2,299 words is **2.8 %** of the 82,375 the
partition consumes. This is a harder version of 2720's problem (poetry had 145 words of slack
there); the scaled substitute is specified in §4.3 and its weakness is stated in §10.

### 2.2 Qurʾānic-quotation strip — applied identically to both prose corpora

Ḥadīth quotes the Qurʾān. Undetected quotation drags a prose baseline's `d_min` toward the
Qurʾān's, which **biases toward finding no discrimination** — the direction that favours my
own expected conclusion, so it must be removed rather than argued about. 2720 used
`bukhari-noquran.txt` for the same reason.

Locked procedure: build the multiset of all **7-word n-grams** of the Qurʾān's own
diacritics-stripped word stream; walk each prose corpus's diacritics-stripped word list;
mark every word covered by any position-7 window matching a Qurʾānic 7-gram; delete marked
words from the vocalised stream. The number and fraction of words dropped is reported. The
primary run uses the stripped streams. If stripping leaves a corpus below 82,375 words, that
corpus is dropped and the fact is reported.

---

## 3. The instrument

### 3.1 The scanner is H-NEW-2690's, lifted verbatim and SHA-gated

`scan()`, `phonemes()`, `syllables()`, `normalize()`, `strip_pausal()`, `METERS`, `tiled()`,
`lev_band()`, `metricality()` and `matched_noise()` are **extracted from the frozen
`scripts/h-new-2690.py` source at runtime**, their source text SHA-checked against values
recorded when this pre-registration was written, and executed. Nothing is retyped. A fragment
whose SHA has changed is a `SystemExit`.

### 3.2 One declared performance rewrite, with a mandatory identity gate

`metricality()` costs ≈ 0.026 s per unit, which makes the offset design infeasible. A
functionally identical routine `dmin_fast()` is used for the bulk arms. It differs only in
(i) de-duplicating the tiled template set (182 candidates → 77 distinct at L = 28), (ii)
computing the Hamming bound by integer bit-mask popcount, (iii) carrying a **global** rather
than per-meter Levenshtein cap, and (iv) pruning candidates by the valid lower bound
|heavy(obs) − heavy(canon)| ≤ edit distance. It returns `d_min` and the argmin meter only; it
does not return the per-meter vector, which this test does not use.

**Locked gate (MW-6, fail-fast):** before any arm is computed, `dmin_fast()` and the lifted
`metricality()` are run on **1,500 units drawn from all four corpora** and must agree on
`d_min` to 1×10⁻¹² **and** on the argmin meter on **every** unit. Any disagreement is a
`SystemExit` and the run is abandoned. *(A calibration of this gate on 1,000 Qurʾānic units
before locking returned 0 mismatches at a 4.8× speedup; the run re-asserts it on all four
corpora.)*

### 3.3 The partition is H-NEW-2680's, lifted verbatim — with one unavoidable, verified change

`build_pseudo_corpus()` and the `AR_DIAC` / `NON_AR` regex block are extracted from the frozen
`scripts/h-new-2680.py` and SHA-checked against the same three fragment digests H-NEW-2720
verified (`regex 2cd4d0ca289fd137`, `normalise_words 8e49ae080acc6335`,
`build_pseudo_corpus 6931e0863f09a79c`).

**`normalise_words()` cannot be used verbatim on its own output, because it strips every
diacritic** — it is the tokeniser of a test that needed no vocalisation, and applying it here
would delete the entire signal under measurement. A vocalisation-preserving tokeniser
`normalise_words_voc()` is used instead. It is not free to differ:

> **Locked equivalence gate (MW-6, fail-fast).** For every baseline corpus,
> `[AR_DIAC.sub('', w) for w in normalise_words_voc(raw)]` must equal
> `normalise_words(raw)` **exactly, token for token**. Any mismatch is a `SystemExit`.

If that holds, the word stream this test cuts is **provably the identical stream 2680 and 2720
cut**, with the diacritics retained. The partition cannot drift.

### 3.4 Two word-length profiles — a declared rules-tuple axis

2680 and 2720 take `QVERSE_WLEN` from `quran-text/quran-no-tashkeel.json` (**82,375** words).
H-NEW-2690 scanned `quran-text/quran-full-tashkeel.json` (**77,429** words). The 4,946-word
difference is real and was measured before locking: the no-tashkeel file writes Qurʾānic waqf
marks as space-separated tokens, so it counts them as words (e.g. Q2:2 is 9 tokens there and 7
here). Using it would give every baseline unit ≈ 6 % more real words than the Qurʾānic verse
it is matched to — a systematic mismatch of exactly the kind this test exists to detect.

Both are run, as a locked axis:

- **W_2680 (PRIMARY)** — `quran-no-tashkeel.json`, verbatim as 2680/2720 used it. Primary
  because the instruction is to reuse the parent method verbatim and because it keeps this
  test commensurable with 2680 and 2720.
- **W_lex (SENSITIVITY)** — `quran-full-tashkeel.json`, the file actually scanned, whose
  tokens are words.

A verdict that differs between them is **PROFILE-FRAGILE** and may not be reported as
either outcome.

### 3.5 Pausal tuples

H-NEW-2690's headline is reported in **both** `P_forceheavy` (the tuple its §4 control was
calibrated on) and `P_pausal` (its prereg §5 T1 read literally). Both are run here at full
design. `P_none` is not run: 2690's verdict rule already treats it as a third tuple, and it is
not part of the headline this test is auditing. A verdict holding in one pausal tuple only is
**RULES-TUPLE-FRAGILE**.

---

## 4. The arms

Every arm's units pass through the **identical** `scan()` → `dmin_fast()` instrument. The
Qurʾān is never compared to a baseline through a different code path.

### 4.1 Native arms (reproduction of H-NEW-2690's comparison)
Qurʾān 6,236 verses; poetry 240 muʿallaqāt abyāt (2690's filters: diacritic ratio ≥ 0.55,
≥ 8 syllables); prose A and prose B sentences (2690's splitter, ≥ 10 Arabic letters, ≥ 8
syllables, seed-locked cap of 2,500 per corpus). Units of fewer than 4 syllables are masked
out of the statistics, as in 2690.

### 4.2 Matched-partition arms — prose (the headline control)
For each prose corpus and each of **N_OFF = 200** seeded offsets drawn uniformly from
`[0, slack)`: apply the lifted `build_pseudo_corpus()` to the vocalised stream from that
offset, producing 6,236 units on the locked word-length profile. Compute `d_min` on a
seed-locked random sub-sample of **n_sub = 500** of those units and record the median.
(The 114-pseudo-surah grouping of 2680/2720 is computed and asserted for provenance but is
**irrelevant to this statistic**: `d_min` is a per-unit quantity with no surah-level
aggregation. This is stated so that no reader infers a surah-level control that was not run.)

### 4.3 Matched-cut arm — poetry (scaled, and declared weaker)
The poetry stream is 2.8 % of the length the partition requires, so `build_pseudo_corpus()`
returns its insufficiency error. The substitute walks the **same locked profile cyclically**:
`build_pseudo_corpus_cyclic(words, profile, profile_start, offset)` cuts the stream into units
of lengths `profile[(profile_start + i) mod 6236]` until the stream is exhausted, discarding
the final partial unit.

**Locked equivalence gate (fail-fast):** with `profile_start = 0` and `offset = 0`, on any
stream of at least 82,375 words, `build_pseudo_corpus_cyclic` must return **exactly** what
`build_pseudo_corpus` returns. Asserted at runtime on both prose corpora; mismatch is a
`SystemExit`. The cyclic function is therefore the verbatim 2680 cut, extended to streams too
short to complete one pass.

**N_DRAW = 200** seeded draws of `(profile_start, offset)`, yielding ≈ 174 units each. A
deterministic draw at `(0, 0)` is also reported, as 2720 reported poetry as a single
deterministic point.

### 4.4 Qurʾān self-recut — the baseline-free arm
The Qurʾān's own verse word stream, **order preserved**, re-cut into units drawn cyclically
from (a) the prose-A sentence word-length profile and (b) the muʿallaqāt bayt word-length
profile, with 200 seeded draws each. This is the analogue of H-NEW-2720 §2.1c, which
re-cut the Qurʾān's own verses to equal size and collapsed the compression tail from R² =
0.9887 to 0.3388. **It uses no baseline corpus at all and is therefore immune to the
"a partition is not a composed book" caveat of §10.1.**

### 4.5 Length-invariance arms (no partition, no baseline)
(a) Regression of `d_min` on `log L` (L = syllable-string length), pooled over all native
arms and within each arm separately; R² reported for each.
(b) **Length-stratified ordering.** Bin all native units by L into deciles of the pooled
length distribution. A bin is *usable* if it contains ≥ 30 units from each of the three
native arm types (poetry, Qurʾān, prose). Within each usable bin, test whether
median `d_min`(poetry) < median `d_min`(Qurʾān) < median `d_min`(prose).

### 4.6 Excess metricality over matched noise
2690's `matched_noise()` is lifted verbatim: for each unit, one random syllable string of
**identical length and identical heavy-fraction**, seed-locked. Excess = `d_min`(observed) −
`d_min`(matched noise), computed per unit and compared across arms. This controls length **and**
syllable-weight composition *within* each unit, by construction, and needs no partition.
2690 computed this control for the Qurʾān and poetry arms but never used it as an ordering
test; the prose arm's noise floor was never computed at all.

### 4.7 Positive control re-run on partitioned data
2690's `best_meter()` is lifted verbatim and its 16-way meter identification is re-run on
the **partitioned** poetry stream (§4.3), against the same ground truth (Imruʾ al-Qays ṭawīl,
Zuhayr ṭawīl, ʿAmr b. Kulthūm wāfir — a partitioned unit is attributed to the poet whose
stream contributed its first word). Per-unit top-1 accuracy is reported beside the native
0.771 benchmark.

---

## 5. Nulls, seeds, resampling

- **Permutation null:** arm-label shuffle between the two arms under comparison, preserving
  arm sizes; 10,000 permutations; `p = (n_ge + 1) / (n_perm + 1)`; seed 20260509. This is
  2690's `perm_median_diff`, lifted verbatim.
- **Offset band:** each partition arm is a distribution of 200 medians; the Qurʾān is given a
  percentile within it, exactly as 2720 did.
- **Qurʾān band:** the Qurʾān's own median is bootstrapped 200× at n = 500 from its 6,236
  precomputed values, so a median-of-500 is compared to a median-of-500.
- **MW-5 replication:** seed 20260519, partition arms re-drawn with 60 fresh offsets per
  corpus in both pausal tuples.
- **MW-7:** anything outside the k = 4 family is descriptive, single-test α = 0.05 ceiling,
  and labelled as such.
- **Bonferroni k = 4**, α_bon = 0.05/4 = **0.0125**, over the four registered permutation
  tests: D1-p, D2-p, D6a-p, D6b-p.

---

## 6. LOCKED directions

Each direction is locked **against** the outcome that would be convenient, and each is
justified before any value exists.

**D1 — matched-partition prose.** H-NEW-2690's H1b claims median `d_min`(prose) > median
`d_min`(Qurʾān). **Locked prediction: under the matched partition the prose median FALLS to at
or below the Qurʾān's.** Justification: prose native units are 3.6× the Qurʾān's in median
words (§1.1) and `d_min` is a minimum over ~200 templates whose fluctuation term scales as
L^(−1/2) (§1.2), so shortening the units should lower `d_min` mechanically. **This predicts
against the parent finding.** If the prose partition instead stays above the Qurʾān, H1b is
confirmed under a matched control and that is a genuine positive.

**D2 — matched-cut poetry.** H1a claims median `d_min`(Qurʾān) > median `d_min`(poetry).
**Locked prediction: partitioned poetry stays BELOW the Qurʾān, i.e. H1a survives.**
Justification: `d_min` tiles every template at every phase, so it is phase-invariant by
construction; a genuinely metrical stream cut at arbitrary offsets still matches its own
tiled canon across the cut. **This predicts in favour of the parent finding**, and it is the
arm that can most cleanly separate "d_min measures metre" from "d_min measures length": if
partitioned poetry rises to meet the Qurʾān, either d_min is length-driven or the cut destroys
metre, and D7 distinguishes those two.

**D3 — the ordering.** The claim under audit is a **three-way ordering**, not two extremity
claims. It survives only if D1 and D2 both survive, simultaneously, in the same cell.

**D4 — length-variance-explained.** **Locked prediction: length explains a large share.**
Reported as R² of `d_min` on `log L`.

**D5 — length-stratified ordering.** **Locked prediction: the ordering weakens or reverses
within matched length bins.**

**D6 — excess over matched noise.** **Locked prediction: the ordering weakens on excess.**
Locked directions for the two tests: (a) excess(Qurʾān) > excess(poetry); (b) excess(prose) >
excess(Qurʾān) — the same directions H-NEW-2690 locked, transported to the controlled
statistic.

**D7 — positive control on partitioned data.** No direction is locked; this is a gate, not a
hypothesis. Reported before D2 is interpreted.

**D8 — Qurʾān self-recut.** **Locked prediction: the Qurʾān's `d_min` moves toward the target
arm's native value when cut to that arm's unit-length profile** — up toward prose under the
sentence profile, down toward poetry under the bayt profile.

---

## 7. LOCKED decision rules — the runner's verdict logic must be diffed against this section

Let `Q` = the Qurʾān's median `d_min` in the cell; `B_j` = the median of offset partition *j*.

**D1 (prose).** For each prose corpus:
- **SURVIVES** iff `Q` < min over all 200 offsets of `B_j` (the Qurʾān is more metrical than
  *every* matched prose cut) **and** the permutation test of Qurʾān vs the pooled partitioned
  prose units gives p < 0.0125 in the locked direction.
- **ARTEFACT** iff `B_j ≤ Q` for ≥ 100 of 200 offsets.
- **ATTENUATED** otherwise; the percentile is quoted and no binary claim is made.
- D1 overall is **SURVIVES** only if it is SURVIVES for **both** prose corpora.

**D2 (poetry).**
- **SURVIVES** iff `Q` > max over all 200 draws of the poetry median **and** p < 0.0125 in the
  locked direction.
- **ARTEFACT** iff the poetry median ≥ `Q` for ≥ 100 of 200 draws.
- **ATTENUATED** otherwise.
- **UNINTERPRETABLE** if D7 fails (below), overriding all three.

**D3 (ordering).** **ORDERING-SURVIVES** iff D1 = SURVIVES **and** D2 = SURVIVES, in the
primary cell **and** the tuple-sensitivity cell. Otherwise **ORDERING-DOES-NOT-SURVIVE**,
with each arm's label reported separately. Explicitly locked: if D2 survives and D1 does not,
the surviving claim is **not** the three-way ordering but the single statement "the Qurʾān is
less metrical than the muʿallaqāt", which is a two-way extremity claim on the side where the
comparison unit is a different kind of object, and it must be reported as such.

**D4 (invariance).** Pooled R² of `d_min` on `log L` across native arms:
- **NOT-LENGTH-INVARIANT** iff R² ≥ 0.50.
- **PARTIALLY-LENGTH-DRIVEN** iff 0.20 ≤ R² < 0.50.
- **LENGTH-INVARIANT-IN-PRACTICE** iff R² < 0.20.
Reported alongside: the between-arm `d_min` gap predicted by the fitted length model from the
arms' median lengths alone, as a fraction of the observed gap.

**D5 (stratified).** Over usable bins (§4.5b):
- **NON-OVERLAPPING-SUPPORT** iff fewer than 3 bins are usable — in which case the arms are
  declared not length-comparable and the raw three-way median comparison is declared
  uninterpretable without a partition.
- **STRATIFIED-SURVIVES** iff the full ordering holds in ≥ 2/3 of usable bins.
- **STRATIFIED-FAILS** iff it holds in < 1/2.
- **MIXED** otherwise.

**D6 (excess).** **EXCESS-SURVIVES** iff both locked directions hold with p < 0.0125 in both
pausal tuples. Otherwise **EXCESS-FAILS**, with the failing arm named.

**D7 (partitioned positive control).** Per-unit top-1 meter accuracy on partitioned poetry.
- **CONTROL-HOLDS** iff accuracy ≥ 0.40 (the gate H-NEW-2690 locked for its own scanner).
- **CONTROL-FAILS** otherwise → D2 is reported **UNINTERPRETABLE**, neither passed nor failed,
  and the incomparability of the partitioned poetry arm is itself reported as a finding.

**D8 (self-recut).** **SELF-RECUT-CONFIRMS-LENGTH** iff, under either re-cut, the Qurʾān's
median `d_min` moves ≥ 50 % of the distance from its native value to the target arm's native
value. **SELF-RECUT-REFUTES-LENGTH** iff it moves ≤ 10 % under both. **PARTIAL** otherwise.

### 7.1 Overall verdict (locked)

- **DISCRIMINATES** — D3 ORDERING-SURVIVES **and** D6 EXCESS-SURVIVES **and** D4 is not
  NOT-LENGTH-INVARIANT.
- **ARTEFACT-OF-UNIT-LENGTH** — D1 = ARTEFACT, **or** (D4 = NOT-LENGTH-INVARIANT **and**
  D8 = SELF-RECUT-CONFIRMS-LENGTH).
- **ATTENUATED** — every other combination. Each arm's label is reported; no headline binary
  is issued.
- Any of these is prefixed **PROFILE-FRAGILE** if W_2680 and W_lex disagree, and
  **RULES-TUPLE-FRAGILE** if the two pausal tuples disagree.

---

## 8. Frozen inputs (SHA-256, verified at runtime; mismatch = `SystemExit`)

| file | role |
|:--|:--|
| `quran-text/quran-full-tashkeel.json` | Qurʾān, scanned arm + W_lex profile |
| `quran-text/quran-no-tashkeel.json` | W_2680 profile (2680/2720's) |
| `data/literature/hadith/…/the_9_books/darimi.json` | prose A |
| `data/literature/hadith/…/the_9_books/bukhari.json` | prose B |
| `data/baseline-corpora/raw/muallaqa-imru-al-qais.txt` | poetry |
| `data/baseline-corpora/raw/muallaqa-zuhayr.txt` | poetry |
| `data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt` | poetry |
| `findings/phase-b-hypotheses/scripts/h-new-2690.py` | scanner source, fragment-lifted |
| `findings/phase-b-hypotheses/scripts/h-new-2680.py` | partition source, fragment-lifted |

Literal digests are embedded in `scripts/h-new-2730.py` and asserted before any computation.

**Run immutability.** Output to `findings/phase-b-hypotheses/runs/h-new-2730/<UTC>/` with
`result.json` + `manifest.json`, **manifest paths repo-relative** so the run is committable.
**No run directory may ever be deleted or overwritten, including smoke, superseded or failed
runs.** No exception.

---

## 9. Garden of forking paths — what was known at lock time

Recorded now so it cannot be reconstructed favourably later.

**Computed before locking, and used to write this document:**
- Diacritic ratios and word counts of every candidate corpus (feasibility only).
- Unit word-length profiles: Qurʾān verse median 10 / mean 12.4; Dārimī sentence median 36 /
  mean 38.0; muʿallaqāt bayt mean 9.6. **These are corpus facts, not test statistics**, and
  §1.1's direction lock is justified by them.
- The Qurʾān's verse syllable-length distribution (p10 = 10, median = 28, p90 = 65).
- The three 2680 fragment SHAs, confirmed identical to the ones 2720 verified.
- A speed calibration of `dmin_fast()` against `metricality()` on 1,000 Qurʾānic units:
  0 mismatches, 4.8×. This necessarily computed Qurʾānic `d_min` values, whose median is
  already published by H-NEW-2690 (0.2222). **No arm median was inspected, no baseline value
  of any kind was computed, and no partition was constructed, before this file was locked.**

**Choices made before any baseline value existed:** the corpus list, both word-length
profiles, both pausal tuples, N_OFF, N_DRAW, n_sub, all eight direction locks, every decision
threshold in §7, and the overall verdict rule in §7.1.

**Choices that will be disclosed if made after data is seen:** any at all, labelled MW-7 and
excluded from the verdict.

---

## 10. Honest limits, stated in advance

1. **A partition is not a composed book.** The pseudo-units are arbitrary cuts of a
   continuous stream, never authored as units. Per `STATE-OF-THE-PROJECT-2026-08-07.md` §4.7
   the direction of that weakness depends on the statistic's regime, and **`d_min` is
   contiguity-sensitive**: arbitrary cuts of a continuous stream preserve local continuity and
   do not destroy any real boundary that `d_min` reads. **A baseline pass here is therefore
   weaker evidence against the law than the percentile alone suggests.** This is stated as a
   limit, not used as an escape hatch — and it is the reason arms §4.4, §4.5 and §4.6 exist,
   since none of them uses a baseline partition at all.
2. **al-Jāḥiẓ is untestable** on this statistic. The genre control is ḥadīth-only on the prose
   side. Two ḥadīth collections are not "Arabic prose in general".
3. **The poetry arm is scaled, not matched.** 2,299 words against 82,375 required. Its
   units come from cycling the profile, so a single draw re-uses the same stream under many
   different cuts, and the 200 draws are far from independent.
4. **Only 2 of 16 meters have vocalised ground truth** (ṭawīl, wāfir) — H-NEW-2690's limit,
   inherited whole.
5. **The prose corpora are differently vocalised** (0.866 and 0.770 against the Qurʾān's
   0.918). Incomplete vocalisation inflates `d_min`, so this biases the prose arms *upward*
   relative to the Qurʾān — **toward** H1b passing, i.e. toward the parent finding surviving.
   The bias runs against this test's expected conclusion, which is the conservative direction.
6. **`dmin_fast` is a rewrite.** Its identity gate (§3.2) is exact on 1,500 units across four
   corpora but is not a proof.
7. **Failure to discriminate is not disproof of al-Bāqillānī.** "Neither *nathr* nor *shiʿr*"
   was never a claim about medians of normalised edit distances. What can fall here is the
   stated empirical vindication, not the classical thesis.

---

## 11. Failure conditions (locked)

- Any frozen-input or fragment SHA mismatch → `SystemExit`, no result.
- `dmin_fast` identity gate fails on any of the 1,500 units → `SystemExit`.
- `normalise_words_voc` equivalence gate fails on any corpus → `SystemExit`.
- `build_pseudo_corpus_cyclic` equivalence gate fails → `SystemExit`.
- A prose corpus falls below 82,375 words after the Qurʾān-quotation strip → that corpus is
  dropped and the fact reported; if both drop, D1 is reported untested.
- D7 fails → D2 is **UNINTERPRETABLE**, not a pass and not a fail.
- The two pausal tuples disagree → **RULES-TUPLE-FRAGILE**; the two word profiles disagree →
  **PROFILE-FRAGILE**. Neither may be reported as the outcome that suits the expectation.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any partitioned, stratified or noise-controlled
value was computed. A law that has never met a control is a description. Bismillāhi
al-Raḥmāni al-Raḥīm.*
