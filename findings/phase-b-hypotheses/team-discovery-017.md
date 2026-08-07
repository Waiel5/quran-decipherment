---
finding_id: team-discovery-017
phase: B
hypothesis: H-NEW-22 — Quranic acrostic (per-surah + cross-surah)
status: NULL-with-anti-signal
verdict: Pre-registered positive direction FAILS on all three sub-tests. Anti-signal detected: Quran verse-boundary letters yield FEWER dictionary substrings than chance.
rules_tuple: (rasm, no-tashkeel, basmala-only-Q1, Kufan-ayah, mashriqi-ordering)
seed: 20260413
date: 2026-04-13
bonferroni_k: 3
alpha_bon: 0.0033
dictionary_size: 4927 QAC-derived roots+lemmas ≥3 chars (Buckwalter→Arabic normalized)
classical_anchor: Ibn ʿAshūr dismissal of intra-surah acrostics; al-Zarkashī on muqaṭṭaʿāt
---

# H-NEW-22 — Quranic acrostic scan (per-surah + cross-surah)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Hypothesis

Per Ibn ʿAshūr's own dismissal of acrostic readings beyond the muqaṭṭaʿāt,
the pre-registered one-sided prediction was: **rate(dictionary substrings
inside verse-first-letter / verse-last-letter strings) > null**.

Ibn ʿAshūr (*Taḥrīr* 1:96-102) rejects speculative acrostic readings but
leaves open the possibility of intentional letter-level structure at the
muqaṭṭaʿāt. If the Quran has a measurable acrostic signature beyond the
muqaṭṭaʿāt, verse-first-letter strings should embed more QAC roots/lemmas
than expected under shuffle, letter-frequency, or baseline-corpus nulls.

## Design

Three sub-tests, Bonferroni k=3, per-test α = 0.01/3 = 0.00333.

### Sub-test A — per-surah verse-first-letter scan

- For each of 114 surahs, extract first Arabic letter of each verse after
  normalizing (أ إ آ ٱ → ا, ى → ي, ة → ه).
- Scan the resulting string for dictionary substrings of length 3-7.
- Dictionary = QAC v0.4 roots + lemmas, Buckwalter-converted to Arabic,
  normalized, ≥3 chars → **4,927 entries**.
- Total scanned: 6,236 first-letters (= verse count).

### Sub-test B — cross-surah 114-letter string

- Take first letter of each surah's verse 1, in canonical and Nöldeke
  chronological order. Scan the two 114-letter strings.

### Sub-test C — per-surah verse-LAST-letter scan

- Same procedure on last letters. Rhyme-conditional null samples from
  each surah's own last-letter distribution.

### Nulls

- **N1 (Sub-A)**: within-surah random shuffle preserving unigram marginal.
  500 perms.
- **N2 (Sub-A)**: length-matched strings drawn from global first-letter
  frequency. 500 perms.
- **N3 (Sub-A)**: Muʿallaqāt baseline rate (7 odes, 792 line-opening letters).
- **B-null**: 10,000 random permutations of the 114-letter strings.
- **C-null**: per-surah rhyme-conditional sampling, 300 perms.

## Results

| Sub-test | Observed | Null mean | Null SD | z | p (one-sided ≥) | Verdict |
|---|---|---|---|---|---|---|
| A·N1 within-shuffle | 636 | 681.9 | 23.4 | **−1.96** | 0.980 | FAIL (opposite direction) |
| A·N2 global-freq | 636 | 720.1 | 26.3 | **−3.19** | 1.000 | FAIL (opposite direction) |
| A·N3 Muʿallaqāt rate | 0.1020 | 0.1149 | — | 88.8% of baseline | — | Quran BELOW baseline |
| B canonical | 12 | — | — | **−1.03** | 0.883 | FAIL |
| B Nöldeke | 12 | — | — | **−1.02** | 0.881 | FAIL |
| C last-letter rhyme-cond. | 594 | 637.5 | 21.8 | **−2.00** | 0.973 | FAIL (opposite direction) |

**Every sub-test yields negative z. Pre-registered positive direction: NULL across the board.**

## Interpretation

### Primary verdict
The pre-registered H-NEW-22 positive-direction prediction **fails completely**.
There is no evidence that the Quran embeds acrostic signatures in its
verse-first-letter or verse-last-letter sequences at the lexical level.
This CONFIRMS Ibn ʿAshūr's classical dismissal of intra-surah acrostic
readings beyond the muqaṭṭaʿāt.

### Anti-signal (not pre-registered, disclosed honestly)
All three orthogonal nulls (within-shuffle, global-freq, rhyme-conditional)
and the Muʿallaqāt baseline point in the **same negative direction**:
the Quran's verse-boundary letters produce FEWER embedded roots/lemmas than
chance. Under N2 (global letter-frequency null) this reaches **z = −3.19**,
which under a two-sided test would be p ≈ 0.0014 — below the Bonferroni
threshold, but as an UNDIRECTED, POST-HOC result.

Classical reading of the anti-signal: the Quran's verse-boundary letters are
heavily **rhyme-constrained** (sajʿ, fawāṣil). Al-Zarkashī's *Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive fawāṣil doctrine (phonetic-acoustic selection of verse-final letters) unchanged; H-NEW-22 rhyme-constraint anti-signal finding unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil* pending Phase-2 secondary-triangulation]**
notes that fawāṣil are selected for phonetic-acoustic compatibility, not
for lexical encoding. A rhyme-selected letter distribution is, by
construction, restricted to a small number of terminal consonants (mostly
ن م ر), and this SUPPRESSES the diversity needed to form dictionary
substrings. The anti-signal is therefore a SECONDARY confirmation of the
rhyme-selection hypothesis rather than a new finding.

### What the Muʿallaqāt baseline shows
The Muʿallaqāt (7 classical odes, rhymed monolithic qāfiya) produce a
first-letter hit rate of 0.1149. The Quran: 0.1020. **Classical monorhyme
poetry is more acrostic-dense than the Quran at the verse-opening level.**
This is the opposite of what Ibn ʿAshūr's opponents (the acrostic-readers)
would have predicted, and it is consistent with the Muʿallaqāt being
line-opening-free (poets vary bayt openings) while Quranic verses are
discourse-constrained.

## Garden of forking paths (disclosed)

1. **Buckwalter conversion bug fixed mid-run**: first execution had empty
   dictionary (QAC roots were Buckwalter-encoded, not Arabic-script). Fixed
   by adding Buckwalter→Arabic map and re-running. Pre-registered design
   unchanged; only the dictionary-loading implementation changed.
2. **Dictionary length constraint**: chose ≥3 chars to match classical
   trilateral-root minimum. Not chosen to maximize signal.
3. **Substring scan window**: 3-7 characters; longer matches wouldn't affect
   z because dictionary has very few roots ≥8 chars.
4. **Anti-signal is post-hoc** and NOT counted toward the pre-registration
   verdict. It's reported only as a disclosure of actual observed direction.

## Limits

1. **Dictionary is QAC-dependent**: a dictionary built from an external
   source (e.g., Lisān al-ʿArab) would likely be larger and possibly
   change the per-test ratio, though not the direction.
2. **Substring scan is greedy non-overlapping**: overlapping matches are
   counted separately, which inflates both observed and null equally so
   the z is preserved, but the absolute count isn't comparable across
   corpora with different letter entropies.
3. **Ibn ʿAshūr's own position is already dismissive**: the test is
   therefore functionally a confirmation of classical rejection rather
   than an adjudication of a live classical debate.

## Verdict

**NULL on the pre-registered positive direction.** All three sub-tests and
both orderings fail. Side-finding of a consistent anti-signal disclosed
honestly but not counted as the finding. The Quran does NOT encode
lexical acrostics beyond the muqaṭṭaʿāt.

## Files

- Script: `/Users/grey/Downloads/quran/scratch/team-discovery/h_acrostic.py`
- Results: `/Users/grey/Downloads/quran/scratch/team-discovery/result-acrostic.json`
- Seed: 20260413
