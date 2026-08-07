---
finding_id: H-NEW-2770
title: The chronology–content map is the denominator — 9 of 11 density axes fall to a null that matches verse length, and two survive
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claim: H-NEW-125 (comprehensive chronology-content map, 11/15 axes)
prereg: findings/phase-b-hypotheses/prereg-h-new-2770-chronology-content-length-nuisance.md
prereg_sha256: da1c747d759a4da3ead662e263d38e8a4fe036057a10f041b524caf408894817
run: findings/phase-b-hypotheses/runs/h-new-2770/20260807T043327Z/
method_parent: [H-NEW-2680, H-NEW-2760]
defect_diagnosed: "null does not match the nuisance parameter — the H-NEW-740 shape"
seeds: 20260509 primary / 20260519 replication
n_perm: 10000
status: >-
  DOES-NOT-DISCRIMINATE under the locked rule. Of the 9 per-verse density axes that pass
  Bonferroni-15 as published, only 2 survive a null that permutes Nöldeke rank within
  mean-verse-length quintiles — and both are theonym counts. Identical in both seeds.
verdict: >-
  H-NEW-125's "PERVASIVE CHRONOLOGY" verdict does not survive. Its densities divide by
  VERSE COUNT while mean verse length rises 4.4× across the sequence and correlates with
  Nöldeke rank at ρ = +0.904 — a stronger correlation than most of the axes themselves.
  Under an MVL-matched null the surviving count falls 9 → 2. Arbitrary frequency-matched
  vocabulary in matched partitions of al-Bukhārī, al-Jāḥiẓ and pre-Islamic poetry
  reproduces the Qurʾānic axes' correlation with mean verse length at ratios of 0.994,
  0.997 and 0.994 — the mechanism is generic to any text cut on this verse-length profile.
  What genuinely survives is THEONYM DENSITY: allah_density and divine_name_density hold at
  partial ρ = +0.374 and +0.474 controlling log mean verse length.
---

# H-NEW-2770 — The chronology–content map, against a null that matches verse length

**Pre-reg SHA-256 `da1c747d…4817`, runtime-verified. Nine frozen inputs plus the 14-file
poetry corpus SHA-verified. The axes and the Spearman routine are lifted verbatim from the
frozen `scripts/h_new_125_chronology_content.py` as two SHA-checked source regions; the
partition is lifted verbatim from `scripts/h-new-2680.py` under the same three fragment
digests H-NEW-2720 and H-NEW-2730 verified. Nothing was re-implemented.**

---

## 0. Which claim I took, and why it outranked the rest

H-NEW-2760 took the first triage item. **The ranking for the second was computed, not
asserted:** every `H-NEW-NNN` reference across all markdown in the repository was counted, and
each finding checked for an existing correction notice.

| rank | finding | cites | standing? | why it is or is not the target |
|--:|:--|--:|:--|:--|
| 1–4 | H-NEW-111, 236.1, 720, 750 | 2467–1209 | ⛔ corrected | already corrected, or decompose a residual whose parent inference is withdrawn |
| 5 | H-NEW-590 | 1023 | uncorrected | **self-declared `REPLICATION-FAILED` at its own threshold** — it does not need an audit to know it failed |
| 6 | H-NEW-840 | 1005 | ⛔ corrected | UAS, already ruled NOT-A-DISCRIMINATION-CLAIM |
| — | H-NEW-232 | 489 | uncorrected | 8/10 nearest-centroid matches at p = 0.02498 against α = 0.025 — a **single permutation draw** wide; resolution would settle it, not a better null |
| **7** | **H-NEW-125** | **353** | **PASS-DIRECTED** | **TAKEN** |
| — | H-NEW-192 | 244 | uncorrected | same length confound (mushaf position is length-descending at Spearman −0.846) but a smaller claim. **Queued as H-NEW-2780** |

**H-NEW-125 outranked the rest on all three criteria.**

1. **It is the most load-bearing uncorrected claim that still carries an inference.**
   Everything above it by citation count is corrected or self-failed. H-NEW-125 underwrites
   the project's entire Meccan/Medinan register framework — every finding that conditions on
   revelation phase inherits its conclusion that *"the Qurʾān **is** a chronologically-
   stratified corpus at the structural level."*
2. **Its defect is defect (b) in its purest form, and it is arithmetical rather than
   arguable.** Nine of its eleven surviving axes are densities of the form
   `100 × count / n_verses` — **per verse**. Its own axis 2, `mean_verse_length`, correlates
   with Nöldeke rank at **ρ = +0.904** and rises **4.4×** from Early Meccan to Medinan.
   **The denominator is itself the strongest chronological signal in the study.**
3. **Its null cannot separate the two.** The published runner permutes Nöldeke rank freely
   across all 114 surahs (`rng.shuffle(perm_indices)`), destroying the length–chronology
   association along with everything else. **This is the H-NEW-740 shape exactly.**

---

## 1. The instrument reproduces H-NEW-125 exactly

Fail-fast gate, run before any control value: **all fifteen published ρ reproduce to within
0.005**, and every published token total reproduces exactly (Allah 2704, qul 332, prophet 528,
legal 851, eschatological 1394, book 1082, oath 206, divine-name 4539, pronoun 646, refrain 94,
loanword 6156).

| axis | published ρ | reproduced |
|:--|--:|--:|
| mean_verse_length | +0.904 | **+0.9038** |
| divine_name_density | +0.897 | **+0.8973** |
| allah_density | +0.852 | **+0.8520** |
| loanword_density | +0.833 | **+0.8329** |
| surah_length | +0.390 | **+0.3903** |
| oath_density | −0.004 | **−0.0041** |

**Nothing here says any H-NEW-125 computation is wrong.** The arithmetic is exact. What is
challenged is what the correlations measure.

---

## 2. The nuisance parameter, ranked on the data *before* the null was designed

H-NEW-2760's H2 failed its gate because it locked the weaker of two nuisance channels as
primary on an a-priori judgement. That is now a standing lesson
(`STATE-OF-THE-PROJECT-2026-08-07.md` §4.10) and it is applied here: **all three candidate
channels were measured first, and the primary was chosen on the measurement.** H2 was then
registered so the ranking is on the record and falsifiable.

| channel | ρ with Nöldeke rank |
|:--|--:|
| **N1 — mean verse length (tokens/verse)** | **+0.9038** |
| N2 — surah word count | +0.6892 |
| N3 — surah length (verse count) | +0.3903 |

**H2 PASSES**: N1 > N2 > N3 > 0, p = 1 × 10⁻⁴.

**And six of the nine surviving density axes correlate more strongly with mean verse length
than with chronology itself** — `legal_term` +0.794 vs +0.704, `loanword` +0.887 vs +0.833,
`eschatological` +0.764 vs +0.710, `book_reference` +0.693 vs +0.574, `prophet_narrative`
+0.585 vs +0.530, `personal_pronoun` +0.554 vs +0.496.

---

## 3. The result — 9 → 2

Per-axis, all eleven densities. `*` marks the nine that pass Bonferroni-15 as published.
Per-axis bar throughout is H-NEW-125's own **α = 0.05/15 = 0.00333**.

| axis | ρ per-**verse** | ρ per-**word** | Δρ | p, MVL-stratified | partial ρ (ctrl log MVL) |
|:--|--:|--:|--:|--:|--:|
| `*`**allah_density** | +0.8520 | **+0.7535** | −0.0985 | **0.00020** ✓ | **+0.3744** |
| `*`**divine_name_density** | +0.8973 | **+0.7631** | −0.1342 | **0.00010** ✓ | **+0.4735** |
| `*`loanword_density | +0.8329 | **+0.0547** | **−0.7781** | 0.0159 ✗ | +0.1594 |
| `*`legal_term_density | +0.7039 | +0.4439 | −0.2600 | 0.6442 ✗ | **−0.0508** |
| `*`eschatological_density | +0.7096 | +0.1451 | −0.5645 | 0.1566 ✗ | +0.0700 |
| `*`book_reference_density | +0.5744 | +0.2772 | −0.2972 | 0.9332 ✗ | **−0.1680** |
| `*`qul_density | +0.5421 | +0.4867 | −0.0554 | 0.0232 ✗ | +0.2174 |
| `*`prophet_narrative_density | +0.5304 | +0.3506 | −0.1798 | 0.2329 ✗ | **+0.0037** |
| `*`personal_pronoun_density | +0.4956 | +0.1440 | −0.3516 | 0.6119 ✗ | **−0.0145** |
| oath_density *(already null)* | −0.0041 | −0.1362 | −0.1321 | 0.9265 ✗ | −0.0813 |
| refrain_density *(already null)* | +0.0023 | +0.0020 | −0.0003 | 0.9947 ✗ | +0.0999 |

**Surviving density axes, by arm:**

| arm | surviving of 11 | locked label |
|:--|--:|:--|
| published per-verse form (reproduction) | **9** | — |
| **per-WORD re-normalisation** | **6** | `RENORM-ATTENUATES` |
| **per-verse, MVL-quintile-stratified null** | **2** | `STRATIFIED-COLLAPSES` |
| per-word **and** MVL-stratified | **2** | — |
| per-verse, word-count-stratified *(secondary)* | 6 | — |
| per-verse, **verse-count**-stratified *(secondary)* | **9** | — |

That last row is the control on the control. Stratifying on **verse count** — the channel at
ρ = +0.390, the one an a-priori guess would have picked — changes nothing: 9 of 9 survive.
**Only the correct channel moves the result**, which is what a nuisance parameter is supposed
to do and precisely what H-NEW-125's free shuffle could never show.

**Every axis's Δρ is negative.** Re-normalising per word reduces the correlation for all
eleven, with no exceptions and no compensating rises.

**`loanword_density` is the extreme case: ρ = +0.833 per verse, +0.055 per word.** Ninety-three
per cent of the "Arabicised loanword density rises across the revelation sequence" signal is
the denominator. **Seven of the nine published survivors have a partial correlation of
essentially zero or negative once log mean verse length is controlled** — and two of those
seven (`legal_term`, `book_reference`) change sign.

---

## 4. The mechanism is generic — arbitrary vocabulary in any corpus reproduces it

Each baseline stream cut into 6,236 units on this corpus's verse word-length profile and
grouped into 114 pseudo-surahs on the canonical verse-count profile, using H-NEW-2680's code
verbatim. The pseudo-surahs therefore inherit this corpus's mean-verse-length trajectory
exactly — ρ(pseudo-surah MVL, index) = **−0.7131**, identical in all three corpora **by
construction**, which is the point.

For each of the nine published-passing axes, a **surrogate target set** was drawn from the
baseline's *own* vocabulary, frequency-matched to the Qurʾānic axis's pooled token count
within 2 % (Allah 2704, loanword 6156, qul 332, …), 20 seeded replicates each. The surrogate
vocabulary is arbitrary: no chronology, no theology, no register.

| corpus | median surrogate ρ vs pseudo-surah MVL | Qurʾān's median ρ(axis, MVL) | ratio |
|:--|--:|--:|--:|
| al-Bukhārī | **+0.7591** | +0.7637 | **0.994** |
| al-Jāḥiẓ *Kitāb al-Ḥayawān* | **+0.7613** | +0.7637 | **0.997** |
| pre-Islamic poetry | **+0.7591** | +0.7637 | **0.994** |

Per axis it is just as tight. For the `allah_density` token budget (2,704 tokens), arbitrary
al-Bukhārī vocabulary gives **+0.8445** [+0.719, +0.886], al-Jāḥiẓ **+0.8512**, poetry
**+0.8527** — against the Qurʾān's own **+0.8490**.

**`MECHANISM-GENERIC` in all three corpora.** A per-verse density of *any* frequency-matched
vocabulary, in *any* Arabic text cut on this verse-length profile, tracks mean verse length at
the same magnitude the Qurʾānic axes do. The axes are measuring their denominator.

---

## 5. Verdict

Locked rule, prereg §6, diffed clause-by-clause against the runner before execution:

```
DOES-NOT-DISCRIMINATE     A1 = RENORM-COLLAPSES  OR  A2 = STRATIFIED-COLLAPSES
GENRE-SHARED-BUT-LARGER   neither collapses, AND A4 = MECHANISM-GENERIC,
                          AND at least one of A1/A2 = ATTENUATES
DISCRIMINATES             A1, A2 ∈ {NEUTRAL, STRENGTHENS} AND A4 ≠ MECHANISM-GENERIC
ATTENUATED                every other combination
```

A1 = `RENORM-ATTENUATES` · **A2 = `STRATIFIED-COLLAPSES`** · A4 = `MECHANISM-GENERIC` →

### **DOES-NOT-DISCRIMINATE**

Identical at seed 20260519 on every arm. **Not seed-fragile.**

---

## 6. What survives, and it is worth more than what fell

**Two axes survive everything, and they are the same phenomenon.**

| | ρ per-verse | ρ per-word | p MVL-stratified | p per-word + stratified | partial ρ (ctrl log MVL) |
|:--|--:|--:|--:|--:|--:|
| `divine_name_density` | +0.8973 | **+0.7631** | **0.00010** | **0.00020** | **+0.4735** |
| `allah_density` | +0.8520 | **+0.7535** | **0.00020** | **0.00040** | **+0.3744** |

**The Medinan register genuinely says the divine name more often per WORD, not merely per
verse.** That holds under re-normalisation, under an MVL-matched null, under both
simultaneously, and at a substantial partial correlation. It is the one axis of the fifteen
that is chronology rather than length.

**The two are nested** — *Allāh* is one of the ninety-nine names — so this is **one surviving
result, not two**, and it should be cited as one.

**The honest replacement for H-NEW-125's headline** is therefore not "the Qurʾān is a
chronologically-stratified corpus at the structural level on nearly every axis," but:

> **Verse length rises steeply across the revelation sequence, and almost every content
> "axis" that appeared to rise with it is that rise seen through a per-verse denominator.
> What independently rises is theonym density.**

That is a smaller claim and a much better one, because it is the one that survives a null
matching its nuisance parameter.

---

## 7. Honest limits

1. **Re-normalising per word is not obviously the "right" denominator either.** A per-word
   rate answers "how often among words"; a per-verse rate answers "how often per verse." Both
   are meaningful quantities. **What is established is that the correlation is not robust to
   the choice, and that the choice is itself a chronological variable — which makes the claim
   not established, a weaker statement than false.** This distinction was pre-registered
   (§10.3) and is carried into the verdict language deliberately.
2. **Length may be a mediator, not only a confounder.** If the revelation sequence genuinely
   produced longer verses, conditioning on verse length removes part of the mechanism under
   test — the same caution H-NEW-2760 §3 raised about revelation phase. **The stratified
   counts are floors on the effect, not estimates of it.** The two surviving axes are
   therefore a lower bound on what survives, and the seven that fall are not thereby shown to
   be zero — they are shown to be unestablished.
3. **A4 is a mechanism demonstration, not an independent genre comparison.** The matched
   partition is *designed* to inherit the verse-length trajectory, so reproducing it there is
   expected if the mechanism is what I claim. It is decisive about the *mechanism* and says
   nothing about whether the Qurʾān differs from ḥadīth in any other way. This was
   pre-registered as a limit (§10.1) and the verdict language reflects it.
4. **Nöldeke chronology is a scholarly reconstruction, not data.** Everything here inherits
   its uncertainty; nothing here tests it.
5. **The surrogate vocabulary sets are frequency-matched only**, not dispersion-matched.
   H-NEW-2710 showed dispersion matters. A dispersion-matched surrogate would be a stronger
   control and is not run — though since the surrogates already reach ratio 0.994–0.997, a
   stronger control could only tighten the conclusion.
6. **Four axes were already NULL** in the original (`muq_cardinality`, `oath_density`,
   `rhyme_letter_diversity`, `refrain_density`) and are evidence for nothing here.
7. **The two survivors are one phenomenon**, on a single vocabulary class, and this test says
   nothing about *why* theonym density rises.

---

## 8. Garden of forking paths

- **Every direction, threshold and verdict rule was locked at SHA `da1c747d…` before any
  re-normalised axis, stratified null, partial correlation or baseline value existed.** The
  pre-registration states the expected outcome explicitly and the result went the way it
  predicted on H3, H4 and H5.
- **Known at lock time** and recorded in prereg §9: the citation counts and correction status
  of every finding; the three nuisance channels' ρ against Nöldeke rank; each axis's ρ against
  each channel; and the six-value instrument reproduction. **These are published axes and
  corpus facts about the nuisance.** No re-normalised axis, no stratified null and no baseline
  value existed before the lock.
- **The nuisance channel was ranked on measurement, not judgement** — the direct correction of
  H-NEW-2760's H2 failure, and the reason the secondary verse-count stratification was also
  run (§3) rather than assumed irrelevant.
- **One implementation defect, found and fixed between the calibration run and the primary
  run, disclosed because it is exactly the H-NEW-2600 class of error.** `perm_p` was written
  with `n_perm=N_PERM` as a *default argument*, which binds at definition time; the `--smoke`
  flag's override of the module global was therefore silently ignored and the calibration run
  executed the full 10,000 permutations. It produced correct numbers — the calibration run is
  retained and its axis values are identical to the primary run's — but the flag did not do
  what the code said it did. `n_perm` now resolves at call time. **The bug ran in the
  conservative direction (more permutations, not fewer) and changed no value.**
- **Run directories are never deleted.** The calibration run is retained beside the primary.

---

## 9. What should change in the project record

Flagged, not applied — a correction to another finding's file is not mine to make.

- **`h-new-125-chronology-content.md` needs a correction notice.** Its `status` reads
  `PASS-DIRECTED (11/15 axes survive Bonferroni-15)` and its headline declares the
  **PERVASIVE CHRONOLOGY** regime. **Under a null matching mean verse length, 2 of the 9
  density axes survive.** Its own axis 2 is the confounder. Its Pattern-A/B/C trajectory
  taxonomy (§"3 phase-transition architectures") is built on per-verse densities throughout
  and should carry the same notice — in particular the **LATE MECCAN high-water mark** reading,
  whose five constituent axes (`qul`, `eschatological`, `book_reference`, `muq_cardinality`,
  `loanword`) include the two weakest survivors and the single most denominator-driven axis in
  the study.
- **Any finding conditioning on the Meccan/Medinan register as an established
  *content*-stratification** should note that what is established is a **verse-length**
  stratification plus a theonym-density stratification.
- **`STATE-OF-THE-PROJECT-2026-08-07.md`** should gain a row in §2 and, in §1, the surviving
  theonym result at its measured strength.
- **A methodological lesson for §4.** *Check the denominator before trusting the correlation.*
  A rate is a ratio, and when the divisor is itself the strongest correlate of the predictor,
  the ratio measures the divisor. This is the third distinct form the same error has taken
  today, after unit size (H-NEW-2720, H-NEW-2730) and exchangeability (H-NEW-2760).

---

## 10. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2770-chronology-content-length-nuisance.md`
  (SHA-256 `da1c747d759a4da3ead662e263d38e8a4fe036057a10f041b524caf408894817`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2770.py` — pre-reg SHA-gated; lifts the
  H-NEW-125 axes and Spearman as two SHA-checked regions and the H-NEW-2680 partition as three
  SHA-checked fragments; fail-fast instrument gate on all fifteen published ρ
- JSON: `findings/phase-b-hypotheses/csv/h-new-2770.json`
- Runs (immutable, never deleted): `findings/phase-b-hypotheses/runs/h-new-2770/20260807T043327Z/`
  (primary, 125 s) and `runs/h-new-2770-SMOKE/20260807T043039Z/` (calibration), each with a
  `manifest.json` recording every frozen input SHA in repository-relative form

---

*Run 2026-08-07 by Waiel Al-Shujaa. A rate is a ratio, and the divisor is part of the claim.
Bismillāhi al-Raḥmāni al-Raḥīm.*
