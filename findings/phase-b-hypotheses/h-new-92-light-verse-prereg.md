---
id: H-NEW-92
title: Q 24:35 (Āyat al-Nūr / the Light Verse) — multi-axis structural uniqueness audit vs full Quranic corpus
phase: B
status: PRE-REGISTERED 2026-04-15 (locked BEFORE running script)
agent: h-new-92-specialist
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Wave-H-NEW-92-Light-Verse
bonferroni_k: 8
alpha_bon: 0.00625  # 0.05 / 8 axes
rules_tuple: (no-tashkeel; orthographic-token via real_words; graphemes; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
companion_data:
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt (Leeds QAC v0.4, lemma+root)
  - /Users/grey/Downloads/quran/findings/verse-signature-atlas.csv (per-verse atlas)
  - /Users/grey/Downloads/quran/findings/per-verse-annotations.csv (per-verse multi-tag corpus)
seed: 20260415
---

# [[h-new-92-light-verse|H-NEW-92]] — Āyat al-Nūr (Q 24:35): structural uniqueness audit

## Question

Q 24:35 ("Allāh is the Light of the heavens and the earth; the parable of His Light is as a niche...") is among the most theologically and rhetorically celebrated verses of the Quran. Classical scholars who wrote dedicated treatises or extended chapters on it include al-Ghazālī (*Mishkāt al-Anwār*), al-Rāzī (*Mafātīḥ al-Ghayb* ad loc., ~30 pages), Ibn Kathīr, al-Qurṭubī, Mullā Ṣadrā, Ibn ʿArabī, and many Sufis. Despite this exegetical mass, **the verse has never been subjected to multi-axis quantitative structural testing against the full corpus distribution**.

[[h-new-92-light-verse|H-NEW-92]] asks: **on which structural axes is Q 24:35 actually distinctive — and on which is its celebrated status carried by exegetical tradition rather than measurable form?** The aim is honest demarcation between (a) axes where it is empirically extreme, (b) axes where it is unremarkable, and (c) the comparative profile vs three other classically-celebrated verses (Q 1:1, Q 2:255, the unit Q 112:1-4 as a single short surah).

## Garden-of-forking-paths disclosure (BEFORE running script)

Pre-existing knowledge entering this run:

- From `findings/verse-signature-atlas.csv` row `24,35`: Q 24:35 = 203 letters / 48 words / medinan / rhyme letter م / position-class `middle`. 27 atlas tags including `balagha`, `cosmology-audit`, `earth-sciences-audit`, `fire-light`, `hapax`, `iltifat`, `intra-xref`, `jinas`, `loan-word`, `parable`, `plant`, `animal`. Already flagged `famous:ayat-al-nur`.
- From `findings/phase-b-hypotheses/csv/fire-light-nwr.csv`: Q 24:35 contains the lemma `nuwr` 5 times (segments 2, 6, 33, 35, 38) plus `naAr` (fire) once at segment 32. This is the single most lexically-light-saturated verse in the corpus.
- From `findings/per-verse-annotations.csv` row `24,35`: 17 confirmed cross-finding tags.
- The verse is mid-surah in Sūrat al-Nūr (24, 64 verses), so position 35 is past the midpoint (32) — slightly post-axis.
- Verse 35: numerologically, 35 = 5 × 7. Surah 24 = 8 × 3 = 2³ × 3. The number 35 itself has no abjad-Quranic prior I know of.
- Q 2:282 is the longest verse (~129 words / ~542 letters); Q 24:35 at 48/203 sits in the upper tail but well below the maximum.
- The verse contains the famous `mathal-` (parable) construction; "parable of His Light" is one of ~40 explicit parable-formulas in the Quran.
- Surah 24 al-Nūr is named after this very verse — the only surah whose name comes from the same root as a verse-internal noun in this density.

Honest constraint: the lexical-light density is already public knowledge (atlas + nwr csv). I commit BEFORE running the script that Axis 6 (light-density per word) is **not** counted as a "novel" finding even if extreme — it is **expected** to be the verse's strongest distinguishing axis. Axes 1, 2, 3, 4, 5, 7, 8 are the ones whose ranks I do not yet know.

## Locked methodology

### Pre-registered axes (k = 8, Bonferroni α = 0.05/8 = 0.00625)

For each axis, Q 24:35 is scored, then a percentile rank against the full 6236-verse corpus distribution is computed. **Two-sided p-value** is reported as `min(rank, 6236-rank+1) / 6236 × 2` (treating ties pessimistically — Q 24:35 not breaking its own rank). A verse is "outlier" on an axis if `p_two_sided < α_bon` AND it is in the top or bottom 1% (≤ 62 verses).

| # | Axis | Metric | Direction tested |
|---|---|---|---|
| 1 | length-letters | grapheme count of verse (no-tashkeel) | both tails |
| 2 | length-words | real_words count of verse | both tails |
| 3 | distinct-lemmas | number of distinct Leeds lemmas in verse | both tails |
| 4 | hapax-density | fraction of verse lemmas that occur ≤1 time across the entire Quran | both tails |
| 5 | divine-name-density | count of `lex:Allah` or other definite divine-name lemma occurrences per word | both tails |
| 6 | light-vocabulary density | (light + fire root tokens: nwr, Dwʔ, srj, qbs, Swr-light) per word | both tails (one-sided expected) |
| 7 | type-token diversity (TTR) | distinct-form / total-token (proxy for "concept density") | both tails |
| 8 | abjad-mashriqi total | sum of letter abjad values | both tails |

### Comparators (exempted from Bonferroni — descriptive only)

For each axis above, also compute and report:
- Q 1:1 (Bismillah)
- Q 2:255 (Āyat al-Kursī)
- Q 112:1-4 treated as the entire 4-verse Sūrat al-Ikhlāṣ summed
- For light-vocabulary density specifically: Q 24:36-40 (the surrounding light-verses) as immediate context

### Numerological position observation (Axis 9, exploratory only — NOT in Bonferroni family)

Compute and report:
- Surah 24 prime/composite: 24 = 2³ × 3 (composite)
- Verse position 35 = 5 × 7 (composite, semiprime)
- Position 35 within surah of 64 verses = 35/64 = 0.547 (post-midpoint by 3 verses)
- Reverse-position: 64 - 35 + 1 = 30 (= 2 × 3 × 5; verse 35 from the end is verse 30)
- Distance from surah midpoint (verse 32): +3
- Surah 24 contains 64 verses; 24 × 64 = 1536; surah 24 verse 35 = 24*64+35 = wrong calc, but cumulative position via verse-counts table is reported

**No null model is applied** to position because there is no honest direction-of-positive-result; the numerological observation is descriptive only.

### Pass criteria

For each of 8 axes:
- **STRONG-PASS**: p_two_sided < 0.00625 AND extreme-tail (≤62 verses or ≥6175 verses)
- **PASS-DIRECTED**: p_two_sided < 0.05 (unprotected) AND in top/bottom 5% (≤311 or ≥5926)
- **NULL**: otherwise

### Verdict logic

- **UNIQUE**: ≥3 axes STRONG-PASS, AND light-density (Axis 6) STRONG-PASS, AND distinct-lemma (Axis 3) STRONG-PASS or PASS-DIRECTED
- **NOTABLE**: 1-2 axes STRONG-PASS, OR ≥4 axes PASS-DIRECTED
- **EXEGETICALLY-CARRIED**: 0 axes STRONG-PASS — celebrated by tradition not measurable form

### Data and tools

- Primary corpus: `quran-text/quran-no-tashkeel.json` (locked rules tuple).
- Lemma + root: Leeds QAC v0.4 — already a project-acquired companion.
- Tokenization: `analysis/tools/tokenize.real_words` and `analysis/tools/tokenize.graphemes`.
- Abjad: `analysis/tools/gematria.text_value` with `mashriqi`.
- All computations stdlib-only Python; no randomness — full corpus enumeration for null distributions.

### Light vocabulary roots

Pre-committed root list (matches `findings/phase-b-hypotheses/csv/fire-light-*.csv` files): `nwr` (light), `Dwʔ` (illuminate), `srj` (lamp), `qbs` (firebrand), `Swr` (form-light edge case), `wqd` (kindle), `nfx` (blow), `shhb` (flame), `rmd` (ash), `SbH` (lamp/morning), `Dwq` (taste). Light-density Axis 6 will be COUNTED as the union of these lemmas.

### Hapax definition

A lemma is "hapax" if it appears exactly **1** time in the QAC v0.4 lemma index across the full Quran. Counted on lemma key, not form.

### Output files (locked targets)

- `journal/h-new-92-run-1.md` — run log
- `findings/phase-b-hypotheses/h-new-92-light-verse.md` — RESULTS document
- `findings/phase-b-hypotheses/csv/h-new-92.json` — machine-readable scores + percentiles
- `scripts/h_new_92_light_verse.py` — analysis script

## Honest expectations

I expect:
- **Axis 6 (light-density)** to be #1 in the corpus (extreme right tail, p < 0.0001)
- **Axis 1 (letters)** and **Axis 2 (words)** to be in upper tail but probably not extreme (verse 2:282 is far longer)
- **Axis 3 (distinct lemmas)** to be elevated, plausibly STRONG-PASS
- **Axis 4 (hapax-density)** plausibly elevated due to mishkāt, mishkāh, kawkab, durrī, zaytūnah, etc.
- **Axis 5 (divine-name density)** to be ordinary (only 1 explicit Allāh per atlas count)
- **Axis 7 (TTR)** to be moderate
- **Axis 8 (abjad)** to be unremarkable except as scaled function of length

If I am wrong on any of these the report MUST flag the surprise.

## Cross-finding context

- [[h-new-67-sab-tiwal-mathani|H-NEW-67]] just established al-sabʿ al-ṭiwāl by length; [[h-new-92-light-verse|H-NEW-92]] is the verse-level analog for one celebrated verse.
- [[h-new-43-verse-length-fft|H-NEW-43]] (verse-length FFT) frames length-as-axis.
- The ayat-al-kursi.md deep-dive establishes the comparator template for celebrated verses.
- `findings/khawatim-al-hashr-analysis.md` is the third celebrated comparator already analyzed.

## Locked SHA / timestamp

This pre-registration was written and saved BEFORE any tool was run on Q 24:35 percentile or hapax-density. The script `scripts/h_new_92_light_verse.py` has not yet been written or executed at the moment this prereg is committed.
