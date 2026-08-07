---
finding_id: H-NEW-2370
status: NULL-REVERSED — within-verse emphatic iconicity runs OPPOSITE to the locked direction; punishment verses are slightly LIGHTER than their own surah's baseline. Combined with the surah-scale NULL (H-NEW-2340), this conclusively retires the emphatic-punishment-iconicity claim at ALL scales.
phase: B+ → C
date: 2026-05-29
rules_tuple: (no-tashkeel orthographic letters, Hafs-Kūfan; QAC v0.4 ROOT/LEM for punishment-lexicon disambiguation; verse = QAC āya; counting unit = QAC token letters in Buckwalter space)
verdict: NULL-REVERSED (direction locked positive; observed Δ̄ = −0.0066, p = 0.976; 45/68 surahs negative)
prereg_sha256: d7476efd8d24aee38c9773c231ec07be5334dedda52b17721bfa8435f289c7ec
seed: 20260509
nperm: 10000
---

# H-NEW-2370 — Within-verse emphatic iconicity: NULL-REVERSED. The fine scale kills the iconicity claim too


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## What was tested

H-NEW-2340 found that the classical balāgha/tajwīd intuition — that punishment passages "sound heavier" in the 7 ḥurūf al-isti'lāʾ (ص ض ط ظ ق غ خ) — is **NULL at the surah scale** (ρ = +0.023, p = 0.41; the heaviest surah, Q113 al-Falaq, is a refuge prayer). That NULL explicitly flagged a finer-scale follow-up (H-NEW-2340.1): the surah aggregate cannot separate theme from each surah's own rhyme/phonotactics, so the iconicity — if real — should live at the **verse / pericope** scale (cross-finding-025: structure is finer-scoped than the surah).

This test puts the claim where it should live. **Paired, within-surah design**: for each surah with both punishment and non-punishment verses, compute

```
Δ_s = mean(heavy-density of punishment verses) − mean(heavy-density of non-punishment verses)
```

Because both means come from the same surah, Δ_s is controlled for that surah's phonological baseline — the exact confound that flattened 2340. The aggregate Δ̄ = mean_s(Δ_s).

- **Heavy letters (locked):** isti'lāʾ {ص ض ط ظ ق غ خ} = Buckwalter {S,D,T,Z,q,g,x}.
- **Punishment lexicon (primary):** ROOT `E*b` (ʿadhāb) — contains no heavy letter, so any signal is pure co-text iconicity. 336 verses across 68 qualifying surahs.
- **Self-coupling broken:** letters of every punishment-lexicon *token* removed from BOTH numerator and denominator (load-bearing for the secondary set: saqar→q, laẓā→ẓ, ḥuṭama→ṭ; immaterial for ʿadhāb/jaḥīm/saʿīr/nār, which have none).
- **nār (fire) lemma-pinned; nūr (light) excluded** (the kallā lesson, §10.80).

Pre-registered, direction LOCKED positive (Δ̄ > 0). Pre-reg SHA-256 `d7476efd…c7ec`, runtime-verified. Seed 20260509; 10000 within-surah label-permutations + 10000 sign-flips.

## Result — NULL-REVERSED (unanimous)

| Arm | Δ̄ (mean paired diff) | p (one-sided, locked +) | n surahs |
|---|---|---|---|
| **PRIMARY ʿadhāb (within-surah label perm)** | **−0.00657** | **0.976** | 68 |
| Primary — sign-flip null | −0.00657 | 0.988 | 68 |
| R1 secondary hellfire set | −0.00338 | 0.868 | 86 |
| R2 Meccan-only | −0.00687 | — | 50 |
| R2 Medinan-only | −0.00573 | — | 18 |
| R3 verse-weighted | −0.00403 | — | 68 |
| R4 token-pool (unpaired, context) | −0.00413 | — | corpus |

**Every single arm is negative.** The locked positive direction is not merely unsupported — the effect runs *backwards*: within a surah, punishment verses carry **lower** heavy-consonant density than the surah's non-punishment verses. The sign-count is **45 of 68 surahs negative** (66%), only 23 positive, 0 zero. Under the within-surah permutation null, Δ̄_obs sits at the 2.4th percentile of the *wrong* tail. **Verdict: NULL-REVERSED** — pre-committed direction violated, published with full prominence per §1.8.

## Close reading — the impression is a cherry-pick

The famous "harsh" punishment surahs that fuel the intuition — al-Qāriʿa (Q101), al-Ḥuṭama (Q104), al-Ḥāqqa (Q69), Saqar (Q74) — **do not even qualify** for the paired test on the ʿadhāb root: they are too short or too thematically saturated to contain both ʿadhāb verses and a non-ʿadhāb contrast set. The "heaviness" people hear in them comes from their *rhyme letters* (qāf in al-Qāriʿa, the ṭāʾ/mīm of al-Ḥuṭama, saqar's own qāf), which is a whole-surah phonotactic property — exactly H-NEW-2340's finding — not a property of the verses' punishment content.

Where ʿadhāb verses *do* sit beside non-ʿadhāb verses, they trend **lighter**:

- Most-negative Δ_s: Q84 al-Inshiqāq (−0.067), Q15 al-Ḥijr (−0.061), Q88 al-Ghāshiya (−0.056), Q61 al-Ṣaff (−0.048), Q28 al-Qaṣaṣ (−0.039) — in these, the ʿadhāb verses are *less* isti'lāʾ-dense than the surrounding narrative/creedal material.
- The largest positive, Q73 al-Muzzammil (+0.124), is a small-n sampling artifact (a single ʿadhāb-bearing verse against a long non-punishment body) — the kind of noise that the within-surah permutation null correctly absorbs.

The classical "sounds of terror" reading survives only as a perception of a handful of hand-selected verses, not as a distributional regularity. It is the cherry-picking signature the project's generators exist to detect.

## Significance — the iconicity question is RESOLVED (retired) at both scales

H-NEW-2340 showed no surah-scale theme↔phonology correlation; H-NEW-2370 shows that even at the verse scale, controlling for surah baseline, the effect is **absent and slightly reversed**. There is no remaining scale at which "punishment sounds heavy" lives as a corpus regularity. **The emphatic-punishment-iconicity claim is now conclusively retired.** It joins the project's retirement ledger of impressionistic claims that dissolve under a proper null (balanced-word miracle H-NEW-2010, abjad, Code-19) — the balāgha-side counterpart to numerology retirement: *iconicity asserted, distribution flat (or backwards)*.

This does NOT deny that an individual orator-poet can deploy emphatic clusters for local effect in a chosen verse — only that the Quran's punishment vocabulary as a class is **not** phonologically heavier than its other material at any aggregation scale. What heaviness exists is governed by **rhyme/phonotactics, orthogonal to theme** — consistent with the iʿjāz anti-twin lock (content ⊥ phonology, r = −0.86) and the scale-of-aggregation law.

## Honest limits

- The test measures *grapheme-level* isti'lāʾ density in QAC token forms (no-tashkeel). It does not model rule-governed tafkhīm of ر/ل/ا (deliberately excluded to avoid judgment calls) nor sub-phonemic duration/qalqala. A future test could use full-tashkeel phonemic features (MW-3 alternative instrument), but the surah-scale 2340 already covered the phonemic-density axis via H-NEW-700 with the same null direction, so a rescue is unlikely.
- ʿadhāb-verse identification is lemma/root-exact (QAC); a verse can be eschatologically "about" punishment without carrying the ʿadhāb root (e.g. veiled threats). The secondary hellfire set (jaḥīm/saʿīr/saqar/laẓā/ḥuṭama/nār, +86 surahs) broadens coverage and is equally negative, so this is not driving the NULL.
- The famous short punishment surahs are excluded by the paired design (no within-surah contrast). This is a feature, not a bug: they are the very cases where surah-level rhyme cannot be separated from theme, and 2340 already showed their heaviness is rhyme-driven.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2370-within-verse-iconicity.md` (SHA-256 `d7476efd…c7ec`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2370.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2370.json`
- parent: `findings/phase-b-hypotheses/h-new-2340-emphatic-iconicity.md` (surah-scale NULL)

---

*H-NEW-2370 logged 2026-05-29 by Waiel Al-Shujaa. The surah-scale was flat; the verse-scale is backwards. Across 68 surahs the punishment verses are, if anything, the lighter ones. Iconicity asserted, distribution reversed — the claim is retired at every scale. Bismillāhi al-Raḥmāni al-Raḥīm.*
