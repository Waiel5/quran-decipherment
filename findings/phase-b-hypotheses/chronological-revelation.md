---
title: Chronological revelation order — diachronic metric analysis
phase: B
status: exploratory
pre_registered: false
agent: chrono-revelation
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi
  null_model: 1.5-permutation (10k surah-label permutations) for Meccan/Medinan separation; permutation-of-ordering for Jaccard overlap
ordering_sources:
  - "Egyptian Standard / King Fu'ad edition tartīb al-nuzūl, retrieved from https://tanzil.net/docs/revelation_order (default)"
  - "Theodor Nöldeke, Geschichte des Qorāns (1909-38); 4-phase periodisation (Early Meccan 1-48, Middle Meccan 49-69, Late Meccan 70-90, Medinan 91-114), via Wikipedia 'List of chapters in the Quran' and 'Geschichte des Qorāns'"
data_artifacts:
  - /Users/grey/Downloads/quran/data/revelation-order.csv
  - /Users/grey/Downloads/quran/scratch/chrono/per-surah-revelation-order.csv
  - /Users/grey/Downloads/quran/scratch/chrono/autocorrelation-table.csv
  - /Users/grey/Downloads/quran/scratch/chrono/meccan-vs-medinan.csv
  - /Users/grey/Downloads/quran/scratch/chrono/jaccard-overlap.csv
  - /Users/grey/Downloads/quran/scratch/chrono/new-roots-curve-revelation.csv
  - /Users/grey/Downloads/quran/scratch/chrono/root-temporal-trends.csv
---

# Chronological revelation order — diachronic metric analysis

## Summary

I analyse the Quran in the **traditional Egyptian-edition revelation order**
(`tartīb al-nuzūl`) and in **Nöldeke's four-period chronology**, comparing
metrics that should be sensitive to authorial-circumstance change over the
~22 years of Quranic delivery. The headline empirical result:

> **Across Nöldeke's four phases, average verse length in graphemes climbs
> monotonically: 18.5 → 38.7 → 66.0 → 79.9. One-way F = 209.96 (k=4, n=114).
> This is by far the cleanest diachronic signal in the corpus, and it shows
> up only when surahs are arranged in scholarly chronological order.**

The Hijra change-point appears in `avg_v_words` exactly one position past
the traditional Meccan→Medinan boundary; and the proper name "Muhammad"
(lemma `muHam~ad`) enters the corpus only at revelation position 89, after
the Hijra, and never appears in any of the 86 pre-Hijra surahs.

Negative results: lag-1 autocorrelation along the sequence is *higher* in
mushaf order than in revelation order for every length-correlated metric,
because the mushaf is sorted by length and length dominates these metrics.
Letter entropy and a crude rhyme-uniformity metric are diachronically flat.

This is **not a pre-registered finding**; it is a Phase B hypothesis run.
Effect sizes and permutation p-values are reported, but no claim is yet
"surviving" in the §3 sense of `statistical-rigor-protocol.md`.

---

## 1. Ordering sources and verification

| Position | Mushaf | Surah | Period | Nöldeke order | Nöldeke phase |
|----------|--------|-------|--------|---------------|---------------|
| 1 | 96 | Al-ʿAlaq | Meccan | 1 | Early Meccan |
| 2 | 68 | Al-Qalam | Meccan | 18 | Early Meccan |
| 3 | 73 | Al-Muzzammil | Meccan | 23 | Early Meccan |
| 4 | 74 | Al-Muddaththir | Meccan | 2 | Early Meccan |
| 5 | 1 | Al-Fātiḥa | Meccan | 48 | Early Meccan |
| ... | | | | | |
| 87 | 2 | Al-Baqara | Medinan | 91 | Medinan |
| ... | | | | | |
| 112 | 5 | Al-Māʾida | Medinan | 114 | Medinan |
| 113 | 9 | At-Tawba | Medinan | 113 | Medinan |
| 114 | 110 | An-Naṣr | Medinan | 111 | Medinan |

(Full table at `/Users/grey/Downloads/quran/data/revelation-order.csv`.)

Verification anchors:
- **Position 1 = Surah 96 (Al-ʿAlaq).** ✓ Universally agreed first
  revelation; matches both Egyptian and Nöldeke orderings.
- **First Medinan surah = Al-Baqara at position 87.** ✓ The Egyptian
  ordering puts the Hijra boundary between revelation positions 86 and 87.
- **Last three positions = Al-Māʾida, At-Tawba, An-Naṣr** (positions 112,
  113, 114). ✓ All three are commonly cited as among the very last
  revelations in classical biographical/exegetical literature.

The Egyptian and Nöldeke orderings agree on the start but disagree on the
internal placement of many short surahs and on a few transitional cases
(e.g. Surah 99 Az-Zalzala is Medinan in Egyptian but Early Meccan in
Nöldeke). Disagreement on individual surah labels is well-known and is
*itself* a fact about the limits of traditional chronological knowledge.

---

## 2. Per-surah metrics in revelation order

Computed seven metrics per surah from the no-tashkeel JSON corpus and the
Quranic Arabic Corpus morphology (`quranic-corpus-morphology-0.4.txt`):

| Metric | Definition |
|---|---|
| `avg_v_words` | mean orthographic-token count per verse |
| `avg_v_letters` | mean Arabic-grapheme count per verse |
| `letter_entropy` | Shannon entropy of letter distribution (bits) |
| `n_distinct_roots` | number of distinct triliteral (etc.) roots in surah, from QAC |
| `ttr_lemma` | type-token ratio over QAC lemma tokens |
| `abjad_total` | mashriqi gematric sum over all letters |
| `fasila_uniformity` | proportion of verses sharing the most-common verse-final 2-letter ending |

Full per-surah table at `scratch/chrono/per-surah-revelation-order.csv`.
Selected positions:

| Pos | Surah | n_verses | avg_v_words | avg_v_letters | n_distinct_roots | ttr_lemma |
|----:|-------|---------:|------------:|--------------:|-----------------:|----------:|
| 1 | 96 Al-ʿAlaq | 19 | 3.79 | 15.16 | 32 | 0.681 |
| 5 | 1 Al-Fātiḥa | 7 | 4.00 | 17.43 | 21 | 0.875 |
| 23 | 53 An-Najm | 62 | 4.85 | 19.71 | 144 | 0.479 |
| 39 | 7 Al-Aʿrāf | 206 | 14.97 | 62.94 | 477 | 0.323 |
| 53 | 12 Yusuf | 111 | 15.61 | 65.78 | 351 | 0.336 |
| 86 | 83 Al-Muṭaffifīn | 36 | 4.42 | 19.50 | 90 | 0.604 |
| 87 | 2 Al-Baqara | 286 | 21.62 | 92.29 | 712 | 0.299 |
| 95 | 47 Muhammad | 38 | 14.87 | 65.16 | 257 | 0.503 |
| 113 | 9 At-Tawba | 129 | 19.91 | 87.65 | 524 | 0.348 |
| 114 | 110 An-Naṣr | 3 | 6.33 | 26.67 | 14 | 0.875 |

(The last row is a striking exception: An-Naṣr is at position 114 but is
3 verses long; the local revelation-order trend is dominated by it being
short.)

---

## 3. The Nöldeke 4-phase ramp — the cleanest diachronic signal

Per-phase mean metrics, ordered by Nöldeke phase:

| Phase | n surahs | avg_v_words | avg_v_letters | ttr_lemma | n_distinct_roots |
|---|---:|---:|---:|---:|---:|
| Early Meccan | 48 | 4.36 | **18.49** | 0.722 | 51.9 |
| Middle Meccan | 21 | 9.20 | **38.66** | 0.456 | 217.0 |
| Late Meccan | 21 | 15.85 | **66.02** | 0.370 | 257.1 |
| Medinan | 24 | 18.36 | **79.86** | 0.453 | 210.3 |

**One-way ANOVA F (avg_v_letters across the 4 phases) = 209.96**, k=4,
n=114. The four means form a perfect monotone ramp (each phase is longer
than the previous), and the gap between Early and Late Meccan is *larger*
than the gap between Late Meccan and Medinan. This is consistent with the
historiographical claim that the rhetorical shift from short oracular
verses to long discursive verses happened *gradually* through the Meccan
period and was already well underway before the Hijra.

The ttr_lemma column has a more interesting shape: it drops by half from
Early Meccan to Middle Meccan (0.72 → 0.46) and then *bottoms out at Late
Meccan* (0.37) and partially *recovers* in Medinan (0.45). The recovery
in Medinan is consistent with the Medinan surahs introducing a new legal
vocabulary that increases lemma diversity.

`n_distinct_roots` has the same shape: rises through Meccan period, peaks
in Late Meccan (257), then *drops* in Medinan (210). This is despite
Medinan surahs being on average longer; per-surah root variety actually
peaks in the Late Meccan phase, not Medinan. **This is a counter-intuitive
result and worth flagging as a possible novel observation.**

---

## 4. Hijra change-point detection

Smoothed (window-5 moving average) consecutive deltas for each metric in
revelation order. Reported is the position of the largest |Δ| and the Δ
at the Meccan→Medinan boundary (position 86→87).

| Metric | Largest |Δ| at position | Δ at Hijra (86→87) |
|---|---:|---:|
| avg_v_words | **88** (+4.48) | +0.78 |
| avg_v_letters | **88** (+19.83) | +3.41 |
| n_distinct_roots | 84 (+109.6) | +48.8 |
| abjad_total | 84 (+359 824) | +157 686 |
| ttr_lemma | 15 (-0.11) | -0.03 |
| letter_entropy | 24 (+0.18) | -0.01 |
| fasila_uniformity | 28 (-0.17) | -0.09 |

**For verse length (the dominant signal), the largest discontinuity is at
position 88, exactly two positions past the traditional Hijra boundary.**
For root variety and abjad totals (both length-driven), the largest
discontinuity is at position 84, three positions before the boundary.
The signal is therefore "near the boundary, slightly diffuse" — not a
sharp cliff, more a regime change that takes a couple of surahs to settle.
This pattern is what we should expect if the traditional ordering is
approximately right but contains some local errors of placement.

---

## 5. Mushaf vs revelation autocorrelation — *negative result*

Lag-1 autocorrelation of each metric along the two orderings:

| Metric | Mushaf order ρ₁ | Revelation order ρ₁ | Diff (rev−mushaf) |
|---|---:|---:|---:|
| avg_v_words | +0.728 | +0.572 | -0.156 |
| avg_v_letters | +0.731 | +0.597 | -0.134 |
| letter_entropy | +0.455 | +0.395 | -0.060 |
| n_distinct_roots | +0.834 | +0.465 | -0.369 |
| ttr_lemma | +0.780 | +0.566 | -0.215 |
| abjad_total | +0.702 | +0.228 | -0.474 |
| fasila_uniformity | -0.114 | +0.060 | +0.174 |

**On six of seven metrics, mushaf order is smoother than revelation
order.** This *looks* like a refutation of the traditional ordering, but
the honest reading is the opposite: the mushaf's surah arrangement is
roughly length-sorted by construction, so any length-correlated metric
will be artificially smooth in mushaf order. This test is biased.

To check, I regressed each metric on `log(n_words)` and re-computed the
autocorrelation on the residuals. Mushaf order *still* wins, by similar
margins. This means the mushaf has additional structure (likely thematic
clustering: the long Medinan surahs are at the front, the very short
ones at the end, so the *period labels* themselves are autocorrelated in
mushaf order). Length-detrended autocorrelations:

| Metric | Mushaf resid ρ₁ | Revelation resid ρ₁ |
|---|---:|---:|
| avg_v_words | +0.579 | +0.428 |
| avg_v_letters | +0.584 | +0.481 |
| n_distinct_roots | +0.710 | +0.198 |
| abjad_total | +0.671 | +0.103 |
| ttr_lemma | +0.228 | +0.098 |

**The right test of "true ordering" is therefore not lag-1 autocorr but
the Nöldeke 4-phase F, which only revelation order (and only Nöldeke's,
not the Egyptian's bare 2-period split) can produce.**

The one metric where revelation beats mushaf is `fasila_uniformity` —
mushaf order is anti-correlated lag-1 (-0.114) while revelation is
mildly positive (+0.060). This is consistent with rhyme uniformity
being a *temporal* style choice rather than a length artifact.

---

## 6. Vocabulary overlap between consecutive surahs

Mean Jaccard overlap of root-sets between adjacent surahs:

| Order | Mean Jaccard | Notes |
|---|---:|---|
| Mushaf | 0.2071 | length-sorted, so adjacent surahs have similar size → similar root counts → high baseline |
| Revelation | 0.1864 | |
| Random ordering (5000 perms) | mean ~0.16 | revelation > random p ≈ 0.0002 |

Revelation order has *lower* mean Jaccard than mushaf order, but is still
significantly higher than a uniform random ordering of the same 114
surahs (perm-p ≈ 0.0002, n_iter=5000). So revelation order *does* carry
genuine adjacency-coherence signal — it just doesn't beat the trivial
length-sort coherence of the mushaf.

---

## 7. Meccan/Medinan separation by metric (Egyptian ordering)

| Metric | Meccan mean | Medinan mean | Cohen's d | perm p (10k) |
|---|---:|---:|---:|---:|
| avg_v_words | 8.13 | 17.05 | **+1.74** | **<0.0001** |
| avg_v_letters | 34.04 | 74.11 | **+1.87** | **<0.0001** |
| n_distinct_roots | 139.2 | 197.4 | +0.47 | 0.030 |
| ttr_lemma | 0.578 | 0.469 | -0.58 | 0.008 |
| abjad_total | 166 969 | 322 398 | +0.57 | 0.009 |
| letter_entropy | 4.303 | 4.326 | +0.13 | 0.55 |
| fasila_uniformity | 0.412 | 0.429 | +0.09 | 0.67 |

The two verse-length metrics dominate. Letter entropy and fasila
uniformity are diachronically flat. ttr_lemma is the only metric where
the Medinan mean is *lower* than the Meccan mean (i.e., Medinan surahs
are lexically *less* type-rich, as expected for longer didactic prose).

These p-values are not corrected for the family of 7 tests; with
Holm-Bonferroni at α=0.05 the cutoff for the strongest test is 0.05/7 =
0.0071, and 4 of the 7 metrics survive that bar.

---

## 8. New-roots-introduced ("Heaps' law") curve in revelation order

Cumulative distinct root count after each surah (revelation order). Top 10
surahs by *new* roots introduced at the moment of their revelation:

| Rev pos | Mushaf | Surah | New roots | Cumulative |
|---:|---:|---|---:|---:|
| 39 | 7 | Al-Aʿrāf | **133** | 845 |
| 2 | 68 | Al-Qalam | 109 | 141 |
| 3 | 73 | Al-Muzzammil | 59 | 200 |
| 38 | 38 | Sad | 59 | 712 |
| 4 | 74 | Al-Muddaththir | 57 | 257 |
| 53 | 12 | Yusuf | 45 | 1206 |
| 45 | 20 | Ta-Ha | 43 | 1000 |
| 87 | 2 | Al-Baqara | 43 | 1487 |
| 23 | 53 | An-Najm | 40 | 456 |
| 34 | 50 | Qaf | 39 | 604 |

Total distinct roots after all 114 surahs (either order) = 1642.

The biggest single bump is **Al-Aʿrāf at revelation position 39**: +133
new roots, taking the cumulative from 712 to 845. This is the moment in
the chronological sequence where the rich narrative and prophet-history
vocabulary really enters. The Heaps'-law curve is approximately the right
shape — concave, decelerating — consistent with natural-language vocabulary
accumulation. **There is no obvious vocabulary "second wind" at the
Hijra**; Al-Baqara at position 87 introduces only 43 new roots, less than
several Meccan surahs.

---

## 9. Frequent-root temporal drift

Spearman ρ between per-surah root frequency (root count / n_lemma_tokens)
and revelation position, computed for all 203 roots with global occurrence
≥ 50.

**Top 12 ramp-UP roots (highest +ρ):** these are roots whose frequency
*rises* over time:

| Root | N | ρ | Mecc freq | Med freq | Gloss |
|---|---:|---:|---:|---:|---|
| `nsw` | 59 | +0.917 | 7e-5 | 12.5e-4 | women |
| `nfq` | 111 | +0.883 | 1.7e-4 | 41.6e-4 | hypocrisy / spending |
| `fsq` | 54 | +0.875 | 2.4e-4 | 13.7e-4 | rebellion / iniquity |
| `Hll` | 51 | +0.865 | 2.5e-4 | 10.5e-4 | lawful / permitted |
| `Erf` | 70 | +0.861 | 3.1e-4 | 15.7e-4 | recognise / right conduct |
| `Swb` | 77 | +0.856 | 3.0e-4 | 12.8e-4 | recompense / reward |
| `bAs` | 73 | +0.852 | 3.0e-4 | 14.1e-4 | tribulation / valour |
| `tHt` | 51 | +0.848 | 3.0e-4 | 18.3e-4 | beneath / underneath |
| `Tyb` | 50 | +0.844 | 2.0e-4 | 6.6e-4 | good / wholesome |
| `xbr` | 52 | +0.820 | 6.0e-4 | 24.4e-4 | informed / experience |
| `DEf` | 52 | +0.812 | 2.9e-4 | 6.2e-4 | weak / multiplied |
| `dwr` | 55 | +0.808 | 2.7e-4 | 9.9e-4 | turn / circulate |

These are exactly the *legal-and-community* vocabulary that historians
attribute to the Medinan period: women's rights, hypocrites, the
permitted/forbidden, recompense, tribulation. The ranking is not
cherry-picked — it's the top 12 by Spearman ρ across all 203 frequent
roots.

**Bottom 12 (most ramp-down or weakest growth):**

| Root | N | ρ | Mecc freq | Med freq | Gloss |
|---|---:|---:|---:|---:|---|
| `rbb` | 980 | **-0.179** | 191.9e-4 | 128.4e-4 | lord (rabb) |
| `*kr` | 292 | +0.090 | 55.9e-4 | 26.7e-4 | remember / mention |
| `xlq` | 261 | +0.116 | 59.8e-4 | 19.3e-4 | create |
| `qwl` | 1722 | +0.172 | 187.8e-4 | 136.7e-4 | say |
| `k*b` | 282 | +0.203 | 60.4e-4 | 48.2e-4 | lie / deny |
| `nEm` | 140 | +0.263 | 32.2e-4 | 11.3e-4 | favour / blessing |
| `ywm` | 405 | +0.264 | 74.4e-4 | 38.6e-4 | day |
| `jEl` | 346 | +0.281 | 54.6e-4 | 25.4e-4 | make / appoint |
| `smw` | 381 | +0.291 | 63.9e-4 | 48.4e-4 | heaven / sky |
| `Dll` | 191 | +0.293 | 31.4e-4 | 11.9e-4 | go astray |
| `lyl` | 92 | +0.297 | 35.2e-4 | 6.8e-4 | night |
| `Awl` | 170 | +0.298 | 24.2e-4 | 14.0e-4 | first / former |

`rbb` (Lord) is the **only** frequent root with negative Spearman ρ vs
revelation position — i.e. the only one whose density actually *declines*
through revelation. The next-most-static is `*kr` (mention/remember). The
strongly *Meccan* vocabulary is the cosmological/eschatological set:
night, day, sky, creation — exactly the terms historians use to
characterise early Meccan apocalyptic.

**No root with ≥ 50 occurrences is exclusively Meccan or exclusively
Medinan.** Even the strongest Medinan-skewed roots have a few Meccan
occurrences, and vice versa. This is itself a finding: the
vocabulary differences between phases are *quantitative*, not categorical.

---

## 10. Theological-term first-appearance

First revelation-order position at which each root enters the corpus:

| Term | Root | First rev pos | Mushaf surah | Period | Total N |
|---|---|---:|---:|---|---:|
| ilāh / Allah | `Alh` | 1 | 96 Al-ʿAlaq | Meccan | 2851 |
| rabb (Lord) | `rbb` | 1 | 96 Al-ʿAlaq | Meccan | 980 |
| ṣalāh (prayer) | `Slw` | 1 | 96 Al-ʿAlaq | Meccan | 99 |
| qurʾān (recite) | `qrA` | 1 | 96 Al-ʿAlaq | Meccan | 88 |
| jinn | `jnn` | 2 | 68 Al-Qalam | Meccan | 201 |
| kitāb (book) | `ktb` | 2 | 68 Al-Qalam | Meccan | 319 |
| kufr (disbelief) | `kfr` | 2 | 68 Al-Qalam | Meccan | 525 |
| zakāh (alms) | `zkw` | 3 | 73 Al-Muzzammil | Meccan | 59 |
| rasūl (messenger) | `rsl` | 3 | 73 Al-Muzzammil | Meccan | 513 |
| dīn (religion) | `dyn` | 4 | 74 Al-Muddaththir | Meccan | 101 |
| ḥamd (praise) | `Hmd` | 5 | 1 Al-Fātiḥa | Meccan | 63 |
| nabī (prophet) | `nbA` | 23 | 53 An-Najm | Meccan | 160 |
| ḥijāb (barrier; veil sense in 33:53) | `Hjb` | 38 | 38 Sad | Meccan | 8 |
| fiqh (understand) | `fqh` | 39 | 7 Al-Aʿrāf | Meccan | 20 |
| nifāq (hypocrisy) | `nfq` | 41 | 36 Yā-Sīn | Meccan | 111 |
| jihād | `jhd` | 42 | 25 Al-Furqān | Meccan | 41 |
| ṣawm (fasting) | `Swm` | 44 | 19 Maryam | Meccan | 14 |
| ḥajj | `Hjj` | 49 | 28 Al-Qaṣaṣ | Meccan | 33 |
| **proper name "Muhammad"** (lemma `muHam~ad`) | — | **89** | **3 Āl ʿImrān** | **Medinan** | **4** |

The most striking row is the last. **The proper name "Muḥammad" enters
the corpus only at revelation position 89 (Al-Imrān), and all four of its
occurrences are in Medinan surahs.** The pre-Hijra revelations never name
the Prophet by his proper name. Locations: 3:144, 33:40, 47:2, 48:29.

The ritual-and-belief vocabulary (Allah, rabb, ṣalāh, qurʾān, kitāb,
kufr, zakāh, rasūl, dīn) is *all* present from the very first 5
positions. The legal-community vocabulary (nifāq, jihad, ṣawm, ḥajj) is
present from the late Early Meccan period onwards — much earlier than
the Hijra. This is consistent with traditional Islamic historiography:
the foundational theology was in place by the early Meccan years, and
the legal vocabulary was *introduced gradually* over the Meccan period
before being elaborated in Medinan legislation.

---

## 11. Garden of forking paths disclosure

### Choices made after seeing the data
- I added a length-detrended re-test of the autocorrelation comparison
  *after* observing that mushaf was smoother than revelation; I report
  both versions and the bias direction.
- I added the proper-name `muHam~ad` lemma trace *after* seeing that the
  Hmd root (from `LEM:Hamid`/etc.) was diachronically uninformative. I
  flag this addition.
- The Nöldeke 4-phase F was not in the original task but became the
  obvious clean test once I saw the per-phase means.

### Alternative rule tuples considered and discarded
- Used the no-tashkeel JSON corpus throughout. Did not re-run on
  full-tashkeel; would shift letter counts modestly.
- Used basmala-counted-only-in-surah-1 (the JSON default). This affects
  surah 1 (Al-Fātiḥa) only; would not change the overall ramp.
- Used surface-token whitespace word definition; lemma-token TTR uses
  QAC lemmas which is a different definition.
- Did not run Nöldeke as default; chose Egyptian per task instructions.

### Sibling hypotheses considered
- Distinct *lemma* count per surah (not just root count) — not run.
- Per-period *new* lemma vs new root curves — not run.
- Variance in verse length within surah (a "regularity" measure) — not run.
- Average word length in letters per surah — not run.
- Per-surah huroof muqattaʿat presence in revelation order — not run.

### Why this one and not those
- The seven metrics in the task were specified; I added the one-way F
  across Nöldeke phases because it was the obvious aggregate test of "is
  the chronological ordering meaningful." Nothing was kept *because* it
  was significant; the autocorrelation negative result is reported with
  the same prominence as the F-test positive result.

---

## 12. What is statistically clean

Of the metrics computed:

- **Statistically clean (large effect, low p):** average verse length in
  words and letters. Cohen's d = 1.7-1.9 for Meccan/Medinan. Permutation
  p < 0.0001 (10 000 draws). Survives Holm-Bonferroni at the 7-test
  family. Survives the Nöldeke 4-phase F = 209.96. **This is the
  flagship signal of revelation-order analysis: the corpus gets
  monotonically more verbose over time.**
- **Moderately clean:** ttr_lemma (Cohen's d = -0.58, perm-p = 0.008,
  survives Holm), n_distinct_roots (d = +0.47, p = 0.030, marginal),
  abjad_total (d = +0.57, p = 0.009, but driven by length).
- **Not clean / null result:** letter_entropy (perm-p = 0.55),
  fasila_uniformity (perm-p = 0.67). These are diachronically flat
  within measurement error.
- **Negative result:** mushaf order has higher lag-1 autocorrelation than
  revelation order on every length-correlated metric, even after log-length
  detrending. The "true ordering should be smoother" prediction fails for
  this corpus and these metrics. The mushaf's length-sort makes it an
  unfair smoothness benchmark.

## 13. Novel observations worth flagging for follow-up

1. **The Nöldeke 4-phase verse-length ramp is monotone** with F = 209.96.
   This is not novel as a fact (every Quran scholar knows Medinan surahs
   are longer) but it is novel as a *quantified* metric: the gap between
   Early and Middle Meccan is *larger* than the gap between Late Meccan
   and Medinan, contradicting the popular "everything got long after the
   Hijra" framing.
2. **Lemma TTR follows a U-shape across the 4 Nöldeke phases**: Early
   Meccan 0.72 → Middle 0.46 → Late 0.37 → Medinan 0.45. The Medinan
   recovery is a measurable rebound in lexical diversity, attributable to
   new legal vocabulary entering the corpus.
3. **Per-surah root variety peaks in Late Meccan, not Medinan** (257.1
   vs 210.3 mean distinct roots), despite Medinan surahs being longer on
   average. Worth investigating: is this because Medinan surahs reuse a
   smaller specialised legal vocabulary?
4. **The proper name "Muḥammad" is post-Hijra only**, with all four
   occurrences in Medinan surahs (positions 89, 90, 95, 111). 86 pre-Hijra
   surahs do not name the Prophet by his proper name.
5. **The cosmological-eschatological vocabulary (`lyl` night, `ywm` day,
   `xlq` create, `nEm` favour) is the most strongly Meccan-skewed**,
   consistent with traditional periodisation.
6. **No frequent root is exclusively Meccan or exclusively Medinan.**
   The vocabulary differences are quantitative not categorical, even at
   the most extreme Spearman ρ values.

---

## 14. Prior art

A web search for prior computational/stylometric work on Quranic chronology
turns up one closely-related paper:

- **Behnam Sadeghi (2011), "The Chronology of the Qurʾān: A Stylometric
  Research Program," _Arabica_ 58(3-4), 210-299.** Sadeghi tests a 7-phase
  "Modified Bazargan" chronology against four independent style markers,
  including (1) **average verse length** and (2) percentages of the 28
  most common morphemes. He reports smooth monotone trajectories across
  the seven phases, taking this as evidence that the chronology is
  approximately correct. Sadeghi works on Bazargan's ordering, not
  Egyptian or Nöldeke; the 4-phase Nöldeke F = 209.96 reported here is a
  comparable result on a different (cruder) periodisation.
- **Sadeghi (2013), "The Chronology of the Qur'ān: Stylometry and the
  Refinement of a Qur'anic Timeline,"** in *The Early Qur'an in Mecca*
  (Cambridge UP). Continues the program with finer phase resolution.
- **Sadeghi (2013), "One Muḥammad or Many Muḥammads? What Stylometry Can
  and Can't Tell Us About Quranic Authorship,"** uses the same machinery
  to argue for stylistic continuity across the corpus (single underlying
  voice). Methodologically relevant as the explicit acknowledgment that
  stylometry can confirm chronological coherence without proving
  authorship questions.
- Older religious-studies literature: Ibn Abbas-attributed orderings;
  Bazargan (1965, Persian); Theodor Nöldeke (1860, German, revised by
  Schwally, Bergsträßer, Pretzl 1909-1938).

**The closest direct comparison** to my analysis is Sadeghi 2011: he
already showed that average verse length is a smooth function of
chronological position. My contribution duplicates this and adds the
specific Nöldeke 4-phase F-statistic, the Hijra change-point detection,
the per-root Spearman trend table, the Heaps'-law new-roots curve, and
the proper-name "Muḥammad" first-appearance observation. None of these
are directly in Sadeghi.

## 15. Pre-registration status

**This is not a pre-registered finding.** It is a Phase B exploratory
hypothesis run. To upgrade observations 1-4 to findings under the §3
protocol, I would need:

- pre-registration of the rules tuple, exact metric, and null model;
- a second null beyond the within-surah permutation (e.g. Markov
  surrogate over revelation positions, or comparable-corpus check
  against a Bukhari-style chronologically-arranged early hadith corpus
  if that exists);
- replication on Nöldeke ordering as a robustness check (not just
  Egyptian).

The seventh task item (autocorrelation) returned a clean *negative*
result and I report it as such.
