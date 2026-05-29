# Pre-registration — H-NEW-2370: Within-verse / pericope-scale emphatic iconicity (the finer-scale follow-up to H-NEW-2340)

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE the verdict computation)
**Seed:** 20260509 · **Permutations:** 10000
**Rules-tuple:** (no-tashkeel orthographic letters, Hafs-Kūfan; QAC v0.4 ROOT/LEM for punishment-lexicon disambiguation; counting unit = QAC token letters in Buckwalter space; verse = QAC āya; basmala counted-only-in-Q1 per project default — basmala carries no punishment lexicon so this is immaterial)

## Background — why the scale matters

H-NEW-2340 tested the classical balāgha/tajwīd intuition that punishment/terror passages "sound heavier" (richer in the 7 ḥurūf al-isti'lāʾ ص ض ط ظ ق غ خ) at the **surah scale** and found it **NULL** (Spearman ρ = +0.023, p = 0.41; the heaviest surah, Q113 al-Falaq, is a refuge prayer, not a threat). The NULL finding explicitly flagged a finer-scale follow-up (H-NEW-2340.1): heavy-consonant density is driven by surah-level rhyme/phonotactics, which a surah-aggregate test cannot separate from theme. Per **cross-finding-025** (structural effects in the Quran live at finer scales than the surah), the iconicity claim — if it exists at all — should live at the **verse / pericope** scale, where a *paired, within-surah* design controls for each surah's own phonological baseline.

This test resolves the iconicity question at the scale where it should live: **within a single surah, do the punishment verses carry higher heavy-consonant density than that same surah's non-punishment verses?**

## Definitions (LOCKED)

- **Heavy letters (locked set):** the 7 ḥurūf al-isti'lāʾ — `ص ض ط ظ ق غ خ` = Buckwalter `{S, D, T, Z, q, g, x}`. (Fixed classical tajwīd category; not data-selected. Context-dependent ر/ل/ا tafkhīm excluded to avoid judgment calls. Identical set to H-NEW-2340.)
- **A "letter":** any non-diacritic, non-space alphabetic Buckwalter symbol in a QAC token form (diacritics `a i o u ~ F N K` and tatweel `ـ` excluded). Identical letter-counting rule to H-NEW-2340.
- **Heavy-consonant density of a verse:** (heavy letters in the verse) / (all letters in the verse), computed over the verse's QAC token forms **AFTER removing the letters of any punishment-lexicon token in that verse** (numerator AND denominator) — to break the mechanical self-coupling whereby some punishment-words themselves contain heavy letters (saqar→q, laẓā→ẓ, ḥuṭama→ṭ). ʿadhāb / jaḥīm / saʿīr / nār carry NO heavy letter, so for the primary set the exclusion only touches the denominator; for the secondary set it is load-bearing.
- **Punishment verse:** a verse containing ≥1 punishment-lexicon token (below).
- **Non-punishment verse:** a verse in the same surah containing ZERO punishment-lexicon tokens.

### Punishment lexicon (LOCKED, QAC-disambiguated)

- **Primary set = ʿadhāb only:** ROOT `E*b` (ʿ-dh-b, عذاب "torment/punishment" — unambiguous; contains no isti'lāʾ letter → any signal is pure co-text iconicity, not self-coupling).
- **Secondary robustness set = primary + hellfire terms** (QAC ROOT/LEM, the nār/nūr homograph explicitly disambiguated — the kallā lesson, §10.80):
  - ROOT `jHm` (jaḥīm), ROOT `sEr` (saʿīr), ROOT `HTm` (ḥuṭama), ROOT `lZy` (verb form talaẓẓā), LEM `saqar` (PN), LEM `` laZaY` `` (laẓā, PN), LEM `naAr` (fire — root nwr, lemma-pinned to "fire" so لْنُور "light" lemma `nuwr` is EXCLUDED).
  - (The 2340 secondary set used the wrong Buckwalter encodings `sER`/`sqr`/`lZy`-as-root for some of these; this pre-reg uses the QAC-verified encodings confirmed on disk. The 2340 secondary result was robustness-only and already NULL, so this correction does not alter 2340; it makes the present secondary set faithful.)

## Design — paired, within-surah

For each surah `s` that has **≥1 punishment verse AND ≥1 non-punishment verse** (so the paired difference is defined):

```
Δ_s = mean(heavy_density of punishment verses in s) − mean(heavy_density of non-punishment verses in s)
```

Each qualifying surah contributes ONE paired difference Δ_s. Because both means come from the SAME surah, Δ_s is controlled for that surah's rhyme/phonotactic baseline — the exact confound that flattened the surah-scale test. The primary set yields 68 qualifying surahs (verified on disk: 68 surahs have ≥1 ʿadhāb verse, none is all-ʿadhāb); the secondary set yields 86.

**Aggregate statistic (primary):** the mean paired difference `Δ̄ = mean_s(Δ_s)` across qualifying surahs.

## Primary hypothesis (direction LOCKED)

> **H1:** Within-surah, punishment verses carry HIGHER heavy-consonant density than non-punishment verses: `Δ̄ > 0`.
>
> **Null (primary, within-surah label permutation):** within each surah independently, randomly relabel which verses are "punishment," keeping that surah's punishment-verse count fixed; recompute every Δ_s and the aggregate Δ̄. Repeat 10000×, seed 20260509. This destroys the verse↔punishment-label association while preserving each surah's verse-density distribution AND its punishment-verse count (the correct paired/within-surah null). One-sided p = (1 + #{Δ̄_null ≥ Δ̄_obs}) / (1 + 10000), in the locked positive direction.
>
> **Null (secondary, sign-flip):** randomly flip the sign of each Δ_s independently (Rademacher), 10000×, same seed; one-sided p for Δ̄ > 0. Reported alongside as a paired-difference robustness null.

If `Δ̄ ≤ 0` (reversed or absent), publish as NULL with full prominence.

## Robustness (pre-specified)

- **R1 — secondary lexicon set:** repeat the entire primary test with the secondary (hellfire-inclusive) punishment lexicon. Same direction lock.
- **R2 — Meccan-only / Medinan-only:** repeat the primary within-surah test restricted to each region, to check the effect is not a register artifact.
- **R3 — verse-weighted aggregate:** repeat with Δ_s weighted by the number of punishment verses in s (so surahs with more punishment material count more), as an alternative aggregation (MW-3 alternative-model).
- **R4 — token-level fallback (descriptive):** pool all punishment verses vs all non-punishment verses corpus-wide (NOT paired) as a sanity descriptive; reported but NOT the primary verdict (it reintroduces the surah confound and is for context only).

## Bonferroni

Test family = {primary H1, R1 secondary set} = 2 direction-locked confirmatory cells. α_corrected = 0.05 / 2 = 0.025. Region splits (R2), weighting (R3), and token-pool (R4) are descriptive robustness, not confirmatory cells.

## Verdict logic

- **VINDICATED (fine-scale):** primary H1 passes (Δ̄ > 0, p < 0.025) AND R1 same-sign AND R2 both regions same-sign. The iconicity claim is real but lives at the verse scale, invisible to the surah aggregate.
- **DIRECTIONAL:** primary H1 passes at p < 0.025 but R1 or a region flips sign.
- **NULL / NULL-REVERSED:** Δ̄ ≤ 0 or p ≥ 0.025. Combined with the 2340 surah-scale NULL, this would conclusively retire the emphatic-punishment-iconicity claim at ALL scales — the impression is a cherry-pick from a handful of famous verses (al-Qāriʿa, al-Ḥuṭama), not a distributional regularity.

## Quality gates

- Direction locked BEFORE verdict; reversal → NULL with prominence.
- All counts from `quran-text/quran-no-tashkeel.json` (corpus/region) + `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC token forms + ROOT/LEM); NO values from memory.
- Self-coupling broken by removing punishment-lexicon-token letters from BOTH numerator and denominator.
- Homograph nār/nūr lemma-disambiguated.
- Equal NULL prominence: a flat result is reported as the decisive retirement, not buried.

## Files

- This pre-reg (SHA-256 self-locked; embedded in scripts/h-new-2370.py, runtime-verified)
- `scripts/h-new-2370.py` · `csv/h-new-2370.json` · `h-new-2370-within-verse-iconicity.md`
