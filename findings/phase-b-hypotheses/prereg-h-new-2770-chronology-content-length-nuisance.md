---
id: H-NEW-2770
title: Pre-registration — Does the chronology–content map survive a null that matches verse length, or is it the denominator?
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any re-normalised axis, stratified null or baseline value was computed
family: NUISANCE-AUDIT-2026-08-07-B
target_claim: H-NEW-125 (comprehensive chronology-content map, 11/15 axes)
method_parent: [H-NEW-2680, H-NEW-2760]
defect_diagnosed: "null does not match the nuisance parameter — the H-NEW-740 shape"
seed: 20260509
seed_replication: 20260519
n_perm: 10000
tests_in_family: 5
alpha_bonferroni: 0.01
---

# Pre-registration — H-NEW-2770

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2770.py`.**
Directions locked in §5, decision rules in §6. **The runner's verdict logic must be diffed
against §6 before any verdict is declared** — `STATE-OF-THE-PROJECT-2026-08-07.md` §4.4.

---

## 0. Why this claim — the triage, stated because the reasoning is the deliverable

H-NEW-2760 took the first item (Pillar 1). This takes the second. The ranking was computed,
not asserted: every `H-NEW-NNN` reference across all 906 markdown files was counted, and each
finding was checked for an existing correction notice.

| rank | finding | cites | still standing? | defect | why it is or is not the target |
|--:|:--|--:|:--|:--|:--|
| 1 | H-NEW-111 | 2467 | ⛔ corrected | — | Fisher-Rao geodesic; already corrected |
| 2 | H-NEW-236.1 | 1431 | ⛔ corrected | — | already corrected |
| 3 | H-NEW-720 | 1235 | ⛔ corrected | — | decomposes a residual whose parent inference is withdrawn |
| 4 | H-NEW-750 | 1209 | ⛔ corrected | — | UAS input; UAS ruled NOT-A-DISCRIMINATION-CLAIM |
| 5 | H-NEW-590 | 1023 | uncorrected | **A** (no null) | **self-declared `REPLICATION-FAILED` at its own threshold** — it does not need an audit to know it failed |
| 6 | H-NEW-840 | 1005 | ⛔ corrected | — | UAS; already ruled not a discrimination claim |
| 7 | **H-NEW-125** | **353** | **uncorrected, PASS-DIRECTED** | **B** | **TAKEN — see below** |
| 8 | H-NEW-232 | 489 | uncorrected | B | 8/10 nearest-centroid matches at p = 0.02498 against α = 0.025 — a **single-draw margin**, and its nuisance (cluster density in a 15-dim space) is real but the claim is small and self-limiting |
| 9 | H-NEW-192 | 244 | uncorrected | B | mushaf position from compositional features, R² = 0.759 — a strong second candidate with the same length confound (mushaf position is length-descending at Spearman −0.846). **Queued as H-NEW-2780** |

**H-NEW-125 outranks the rest on all three criteria that matter.**

1. **It is the most load-bearing uncorrected claim that still carries an inference.** The
   three findings above it by citation count are corrected or self-failed. H-NEW-125
   underwrites the project's entire Meccan/Medinan register framework: every finding that
   conditions on revelation phase inherits its conclusion that "the Qurʾān *is* a
   chronologically-stratified corpus at the structural level."
2. **Its defect is defect (b) in its purest form, and it is arithmetical rather than
   arguable.** Eleven of its fifteen axes are densities of the form
   `100 × count / n_verses` — **per verse**. Its own axis 2, `mean_verse_length`, correlates
   with Nöldeke rank at **ρ = +0.904** and rises **4.4×** from Early Meccan to Medinan. A
   per-verse density must rise with verse length even when the per-word rate is flat. **The
   denominator is itself the strongest chronological signal in the study.**
3. **Its null cannot separate the two.** `scripts/h_new_125_chronology_content.py` permutes
   Nöldeke rank freely across all 114 surahs (`rng.shuffle(perm_indices)`). That destroys the
   length–chronology association along with everything else, so the null has no way to ask
   whether the correlation is chronology or length. **This is the H-NEW-740 shape exactly:
   a real, pre-registered null that does not hold the nuisance parameter fixed.**

**H-NEW-192 is the better-known confound but the smaller claim**, and it is queued rather
than taken. H-NEW-232's margin is a single permutation draw wide and would be resolved by
resolution, not by a better null.

---

## 1. The claim under audit

> **11 of 15 pre-registered content/structural axes show highly-significant Spearman
> correlations with Nöldeke revelation rank, surviving Bonferroni-15 (α_bon = 0.00333). The
> Qurʾān is a STRUCTURALLY-STRATIFIED CORPUS.**
> Strongest three: `mean_verse_length` ρ = +0.904, `divine_name_density` +0.897,
> `allah_density` +0.852.
> — `h-new-125-chronology-content.md`

Four axes are already NULL in the original (`muq_cardinality`, `oath_density`,
`rhyme_letter_diversity`, `refrain_density`) and are not the target. Of the eleven that pass,
**nine are per-verse densities**; the other two are `surah_length` and `mean_verse_length`,
which are length itself and are not in dispute.

---

## 2. The nuisance parameter — ranked on the data BEFORE the null was designed

H-NEW-2760's H2 failed its gate because it locked the weaker of two nuisance channels as
primary on an a-priori judgement. `STATE-OF-THE-PROJECT-2026-08-07.md` §4.10 records that as
a lesson. **It is applied here: all three candidate channels were measured first, and the
primary is chosen on the measurement.** These are corpus facts about the nuisance, not values
of any test statistic under test.

| candidate channel | ρ with Nöldeke rank |
|:--|--:|
| **N1 — mean verse length (tokens per verse)** | **+0.9038** |
| N2 — surah word count | +0.6892 |
| N3 — surah length (verse count) | +0.3903 |

And per axis, against each channel:

| per-verse density axis | ρ vs Nöldeke | **ρ vs N1 (MVL)** | ρ vs N3 | ρ vs N2 |
|:--|--:|--:|--:|--:|
| allah_density | +0.8520 | **+0.8490** | +0.2587 | +0.5824 |
| qul_density | +0.5421 | +0.5113 | +0.4458 | +0.5871 |
| prophet_narrative_density | +0.5304 | **+0.5854** | +0.4737 | +0.5925 |
| legal_term_density | +0.7039 | **+0.7935** | +0.4182 | +0.6614 |
| eschatological_density | +0.7096 | **+0.7637** | +0.4636 | +0.6795 |
| book_reference_density | +0.5744 | **+0.6929** | +0.5446 | +0.7060 |
| divine_name_density | +0.8973 | +0.8910 | +0.2907 | +0.6217 |
| personal_pronoun_density | +0.4956 | **+0.5541** | +0.2747 | +0.4529 |
| loanword_density | +0.8329 | **+0.8866** | +0.4340 | +0.7244 |
| oath_density *(already null)* | −0.0041 | +0.0340 | +0.2187 | +0.1577 |
| refrain_density *(already null)* | +0.0023 | −0.0447 | +0.3076 | +0.1692 |

**N1 is locked as primary.** It is the strongest channel against chronology (+0.9038), and
**six of the nine surviving density axes correlate more strongly with mean verse length than
with Nöldeke rank itself.** N2 and N3 are carried as registered secondary stratifications so
that the same mistake cannot be made twice.

---

## 3. Instruments — lifted verbatim, SHA-gated

- **The axes** are lifted from the frozen `scripts/h_new_125_chronology_content.py` as one
  contiguous source region (corpus load through axis 15, ending immediately before its
  Spearman section), SHA-checked at runtime, and executed. **Nothing is retyped.** The region
  also supplies `noldeke_rank`, `noldeke_phase` and the per-surah verse structures. A
  calibration of this lift before locking reproduced all six spot-checked published values —
  `mean_verse_length` +0.9038 (published +0.904), `allah_density` +0.8520 (+0.852),
  `divine_name_density` +0.8973 (+0.897), `loanword_density` +0.8329 (+0.833), `surah_length`
  +0.3903 (+0.390), `oath_density` −0.0041 (−0.004) — and every published token total
  (Allah 2704, qul 332, prophet 528, legal 851, eschatological 1394, book 1082, oath 206,
  divine-name 4539, pronoun 646, refrain 94, loanword 6156).
- **`spearman_rho` and `rank_array`** are lifted from the same file as a second SHA-checked
  region, so the correlation is computed by the original code.
- **The partition** is `build_pseudo_corpus` and the `AR_DIAC`/`NON_AR` block lifted verbatim
  from `findings/phase-b-hypotheses/scripts/h-new-2680.py` under the same three fragment
  digests H-NEW-2720 and H-NEW-2730 verified (`regex 2cd4d0ca289fd137`,
  `normalise_words 8e49ae080acc6335`, `build_pseudo_corpus 6931e0863f09a79c`).

**Locked instrument gate (fail-fast).** The lifted axes must reproduce all fifteen published
ρ to within ±0.005. Any axis outside that is a `SystemExit` and the run is abandoned.

---

## 4. The arms

### A1 — re-normalisation (the primary arm)
Recompute each of the eleven density axes as `100 × count / n_words` instead of
`100 × count / n_verses`, where `n_words` is the surah's token count under the same
tokenisation the lifted region already uses. Recompute Spearman ρ against Nöldeke rank and
the same 10,000-permutation p. **The count of density axes surviving Bonferroni-15 is the
headline statistic.**

### A2 — the length-stratified null
Permute Nöldeke rank **within mean-verse-length quintiles**, so the MVL profile of every
permuted chronology is identical to the real one by construction — the thing H-NEW-740 and
H-NEW-125 both failed to do. 10,000 draws, seed 20260509. Recompute p for all fifteen axes
under **both** normalisations. Secondary stratifications on N2 and N3 are also run and
reported.

### A3 — partial correlation
Spearman partial correlation of each axis with Nöldeke rank controlling `log(MVL)`, and
separately controlling `log(n_words)`. Reported as magnitude per axis; no gate.

### A4 — the genre control (matched partition, reusing H-NEW-2680 verbatim)
Each baseline word stream — al-Bukhārī (`bukhari-noquran.txt`), al-Jāḥiẓ
(`jahiz-hayawan.txt`), and the 14-file pre-Islamic poetry corpus — is cut into 6,236 units on
this corpus's verse word-length profile and grouped into 114 pseudo-surahs on the canonical
verse-count profile. **The pseudo-surahs therefore inherit this corpus's mean-verse-length
trajectory exactly.**

For each baseline and each of the nine surviving density axes, a **surrogate target set** is
drawn from that baseline's own vocabulary: word types sampled without replacement until the
pooled token count matches the Qurʾānic axis's pooled token count (Allah 2704, loanword 6156,
etc.) to within 2 %. **R = 20 seeded replicates per axis per corpus.** For each replicate,
compute the per-100-verse density per pseudo-surah and its Spearman ρ against (i) the
pseudo-surah's mean verse length and (ii) the pseudo-surah index.

**This is the mechanism test.** The surrogate vocabulary is *arbitrary* — it has no
chronology, no theology and no register. If arbitrary vocabulary in ḥadīth or adab prose
reproduces the Qurʾānic axes' ρ against mean verse length, then the axis is measuring its own
denominator.

### A5 — replication
Every arm re-run at seed 20260519.

---

## 5. LOCKED directions

Each is locked against the outcome that would be convenient.

**H1 — reproduction.** All 15 lifted ρ within ±0.005 of published. *(Gate, not a hypothesis.)*

**H2 — the nuisance is real and correctly ranked.** ρ(N1, Nöldeke) > ρ(N2, Nöldeke) >
ρ(N3, Nöldeke), all positive. **Locked because it was measured before the null was designed
(§2); it is registered so that the ranking is on the record and falsifiable, not so that it
can be discovered.**

**H3 — PRIMARY, re-normalisation.** **Locked prediction: the number of density axes surviving
Bonferroni-15 FALLS under per-word normalisation.** Justification: nine of eleven densities
divide by verse count while verse length rises 4.4× across the sequence, and six of nine
correlate more strongly with MVL than with chronology (§2). **Falsifiable in the other
direction:** if the count is unchanged or rises, the densities are not a denominator artefact
and H-NEW-125's inference is strengthened, and that will be published as such.

**H4 — the length-stratified null.** **Locked prediction: the number of axes surviving
Bonferroni-15 FALLS under MVL-stratified permutation, under both normalisations.**

**H5 — genre control.** **Locked prediction: arbitrary frequency-matched vocabulary in the
matched baseline partitions reproduces a positive ρ against pseudo-surah mean verse length,
at a median |ρ| of at least half the Qurʾānic axes' median ρ against MVL.** *This predicts
that the mechanism is generic.* If the baselines show no such correlation, the per-verse
density is not mechanically length-driven and H3's interpretation fails even if its count
falls.

---

## 6. LOCKED decision rules — diff the runner against this section

Let `S_pub` = 9 (density axes surviving Bonferroni-15 in the published per-verse form, of the
eleven densities; the two non-density survivors `surah_length` and `mean_verse_length` are
excluded throughout because they *are* the nuisance and cannot be re-normalised).

- **A1 label.** `RENORM-COLLAPSES` if the per-word surviving count ≤ ⌊S_pub/2⌋ = 4;
  `RENORM-ATTENUATES` if 5 ≤ count < S_pub; `RENORM-NEUTRAL` if count = S_pub;
  `RENORM-STRENGTHENS` if count > S_pub.
- **A2 label.** `STRATIFIED-COLLAPSES` / `STRATIFIED-ATTENUATES` / `STRATIFIED-NEUTRAL`, on
  the same thresholds applied to the MVL-stratified count under the **published per-verse**
  normalisation.
- **A4 label.** `MECHANISM-GENERIC` if the median surrogate |ρ| against pseudo-surah MVL,
  pooled over replicates, is ≥ 0.5 × the median Qurʾānic ρ(axis, MVL) in **at least two of the
  three** baseline corpora; `MECHANISM-CORPUS-SPECIFIC` if in none; `MECHANISM-MIXED` if in one.

**Overall verdict.**

```
DOES-NOT-DISCRIMINATE     A1 = RENORM-COLLAPSES  OR  A2 = STRATIFIED-COLLAPSES
GENRE-SHARED-BUT-LARGER   neither collapses, AND A4 = MECHANISM-GENERIC,
                          AND at least one of A1/A2 = ATTENUATES
DISCRIMINATES             A1 ∈ {NEUTRAL, STRENGTHENS} AND A2 ∈ {NEUTRAL, STRENGTHENS}
                          AND A4 ≠ MECHANISM-GENERIC
ATTENUATED                every other combination — reported per arm, no headline binary
```

A verdict is prefixed **SEED-FRAGILE** if the primary and replication seeds disagree on any
arm label.

**Per-axis reporting is mandatory and is the deliverable.** Direction and magnitude
(ρ_published, ρ_perword, Δρ, partial ρ, stratified p) are reported for every one of the
fifteen axes regardless of verdict, per the standing instruction that magnitude beats
pass/fail.

---

## 7. Nulls, seeds, corrections

- 10,000 permutations, seed 20260509, replication 20260519, `p = (n_ge + 1)/(n_perm + 1)`.
- **Bonferroni k = 5** over the registered family {H2, H3, H4, H5, and the A2 secondary
  stratification}, α_bon = **0.01**. The **per-axis** significance bar remains H-NEW-125's own
  **Bonferroni-15, α = 0.00333**, so that surviving counts are directly comparable to the
  published 11/15.
- **MW-7:** anything outside the registered family is descriptive, single-test α = 0.05, and
  labelled.

## 8. Frozen inputs (SHA-256, runtime-verified; mismatch = `SystemExit`)

`quran-text/quran-no-tashkeel.json`, `data/revelation-order.csv`,
`data/morphology/quranic-corpus-morphology-0.4.txt`, `data/asma-al-husna.txt`,
`data/loanwords/jeffery-1938-loanwords.tsv`,
`scripts/h_new_125_chronology_content.py`,
`findings/phase-b-hypotheses/scripts/h-new-2680.py`,
`data/baseline-corpora/raw/bukhari-noquran.txt`,
`data/baseline-corpora/raw/jahiz-hayawan.txt`, and the 14-file poetry corpus digest.
Literal digests are embedded in `scripts/h-new-2770.py`.

**Run immutability.** Output to `findings/phase-b-hypotheses/runs/h-new-2770/<UTC>/` with
`result.json` + `manifest.json`, **manifest paths repository-relative**. **No run directory
may ever be deleted or overwritten, including smoke and superseded runs.**

## 9. Garden of forking paths — what was known at lock time

**Measured before locking, and used to write §0 and §2:** the citation counts and correction
status of every finding; the three nuisance channels' ρ against Nöldeke rank; each axis's ρ
against each channel; and the six-value instrument reproduction of §3. **These are the
published axes and corpus facts about the nuisance — no re-normalised axis, no stratified
null, no partial correlation and no baseline value of any kind existed before this file was
locked.**

**Fixed before any new value existed:** the target claim, the primary channel, all five
direction locks, every threshold in §6, and the overall verdict rule.

## 10. Honest limits, stated in advance

1. **A partition is not a composed book.** The baseline pseudo-surahs are arbitrary cuts. For
   the A4 mechanism test this cuts *toward* the null being easy to satisfy — the partition is
   *designed* to inherit the verse-length trajectory — so **A4 is a mechanism demonstration,
   not an independent corpus comparison**, and it is labelled as such rather than counted as a
   genre discrimination.
2. **Nöldeke chronology is a scholarly reconstruction**, not data. Everything here inherits
   its uncertainty; nothing here tests it.
3. **Re-normalising per word is not obviously the "right" denominator either.** A per-word
   rate answers "how often does this vocabulary occur among words"; a per-verse rate answers
   "how often per verse". Both are meaningful. **The claim under audit is that the correlation
   measures chronology; if it reverses under a change of denominator that is itself a
   chronological variable, the claim is not established — which is weaker than saying it is
   false.** This distinction is carried into the verdict language.
4. **Length may be a mediator, not only a confounder.** If the revelation sequence genuinely
   produced longer verses, then conditioning on verse length removes part of the mechanism
   under test — the same caution H-NEW-2760 §3 raised about revelation phase. Stratified
   results are therefore **floors on the effect, not estimates of it**, and are reported that
   way.
5. **Four axes were already NULL** in the original and are not evidence for anything here.
6. **The surrogate vocabulary sets are frequency-matched only**, not matched on dispersion or
   burstiness. H-NEW-2710 showed dispersion matters; a dispersion-matched surrogate would be
   a stronger control and is not run.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any re-normalised, stratified or baseline value
was computed. A p-value is a property of a null, not of a claim. Bismillāhi al-Raḥmāni
al-Raḥīm.*
