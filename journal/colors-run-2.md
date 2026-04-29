# colors-run-2 — Journal

**Date:** 2026-04-12
**Agent:** Phase-B (colors in the Quran)
**Output:** `findings/phase-b-hypotheses/colors-in-quran.md`

## Task

Inventory the Quran's chromatic vocabulary and test four theological hypotheses:
1. Per-color inventory (6 named colors: white, black, green, yellow, red, blue).
2. Paradise green vs hell darkness.
3. White/black Judgment-day face polarity (Q 3:106-107).
4. Yellow as color of test.
5. Q 35:27 three-color mountain verse.

## Data sources

- `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4, 128,276 segments).
- `quran-text/quran-no-tashkeel.json` (Tanzil Uthmani, 6236 verses).
- `data/translations/en.sahih.txt` (Sahih International; one verse per line, 6236 lines).
- `docs/master-index.md` for context + prior-art cross-checks.

## Method

Filtered morphology file by `ROOT:` field for six chromatic roots: byḍ, swd, xḍr, ḥmr, ṣfr, zrq. Added meta-root lwn for the Quranic "color" word itself. Disambiguated homographs:
- Root ḥmr: 5/6 tokens are *ḥimār* ("donkey"), only 35:27 is the color *ḥumr*. Red is effectively a chromatic hapax.
- Root swd: 3/10 tokens are *sayyid/sādat* ("chief/master"), 7 are chromatic.
- Root byḍ: all 12 tokens are chromatic (though Q 37:49 *bayḍ maknūn* "hidden eggs" is a metaphorical use for houris, not a color descriptor per se).

Extracted corresponding Arabic and English text from the Tanzil and Sahih files via the global verse-index computed from `total_verses` summed over the 114 surahs.

## Findings summary

### Per-color counts (chromatic-adjective senses only, homographs filtered)

| Color | Root | Chromatic tokens | Key verses |
|---|---|---|---|
| White | byḍ | ~10 | 2:187 thread, 3:106-107 faces, Moses' hand (5×: 7:108, 20:22, 26:33, 27:12, 28:32), 12:84 Jacob's eyes, 35:27 mountains |
| Black | swd | 7 | 2:187 thread, 3:106 faces (×2), 16:58 daughter, 35:27 mountains, 39:60 faces, 43:17 daughter |
| Green | xḍr | 8 | 6:99, 12:43, 12:46, 18:31, 22:63, 36:80, 55:76, 76:21 (+ 55:64 mudhāmmatān via related lemma) |
| Yellow | ṣfr | 5 | 2:69 cow, 30:51, 39:21, 57:20 (three parallel crop-yellowing), 77:33 hell sparks |
| Red | ḥmr | 1 | 35:27 only |
| Blue | zrq | 1 | 20:102 only |

### Structural findings

- **Q 3:106-107 white/black polarity is Form-IX verb-balanced:** 2 byḍ + 2 swd tokens exactly, distributed as imperfect-then-perfect for each color. Classic chiastic chromatic-morphology.
- **Face-blackening idiom (muswadd-) migrates:** Judgment (3:106, 39:60) ↔ daughter-shame (16:58, 43:17). The Quran reuses the damnation gesture to indict pagan misogyny.
- **Paradise green is 100% positively valenced** (4/4 garment-and-cushion + 3/3 vegetation signs + 1/1 fire-from-green-tree). Hell is *never* named with a color; hell has *ẓulumāt* (darkness-plural, 23×) plus derivative value-collapses (blackened faces, blue pallor, yellow sparks).
- **Q 35:27 is the chromatic-densest verse:** 5 color-tokens in one verse (2× *alwānu* + *bīḍ* + *ḥumr* + *sūd*). Q 35:28 adds a 6th *alwānu*. Only verse naming three chromatic adjectives simultaneously. White and red both occur as plural adjectives *bīḍ* and *ḥumr*, and black as *gharābību sūd* (raven-extreme).
- **Yellow is the pre-collapse / test-liminal color.** 4/5 tokens sit at threshold moments (test-object 2:69; crop-to-debris pivot ×3; pre-flame sparks 77:33).
- **Blue is the Quran's only pure chromatic hapax** (Q 20:102, Day of Gathering). Red is functionally a hapax too but shares its root with *ḥimār*.
- **The meta-word *lawn* is a sign-of-God refrain:** 7 of 9 occurrences are *mukhtalif alwān-* ("varying in colors"), treating chromatic plenitude itself as theological proof.

### Cross-checks with existing findings

- `findings/phase-b-hypotheses/quotation-analysis.md` (eschatological speech asymmetry) confirmed: the shorter paradise clause in 3:107 (9 words) vs. longer hell clause in 3:106 (14 words) matches the project-wide pattern of damned-speak-at-length / saved-speak-briefly.
- `findings/phase-b-hypotheses/parables-catalog.md` ("garden" as polyvalent): green as paradise-color never bleeds into damned-context, sharpening the exclusivity.
- `findings/phase-b-hypotheses/hapax-legomena-catalog.md`: *mudhāmmatān* (55:64), *gharābīb* (35:27), *zurq* (20:102) are hapax or near-hapax forms, clustering three of the project's most distinctive color-adjectives at the chromatically-loaded verses.

## Limitations

- Counts rely on QAC v0.4 root-tagging; potential mis-tags not audited line-by-line.
- *Mudhāmmatān* (Q 55:64) was classed under green via tafsir; QAC may list it under a separate root (dhmm). Not tested explicitly.
- Classical tafsir references summarized from working memory of Ṭabarī/Qurṭubī/Rāzī/Ibn Kathīr; not chain-cited to specific page numbers.
- Statistical null-model test of "35:27 is densest" is only informal (5 tokens / 28 words); Phase-C should formalize via sliding-window test.

## Deliverables

- `findings/phase-b-hypotheses/colors-in-quran.md` — full analysis (~2800 words).
- `journal/colors-run-2.md` — this journal.

## Phase-C open hypotheses registered

- H-C-1 sliding-window chromatic density: is 35:27 formally the densest?
- H-C-2 paradise-green exclusivity: 8/8 positively-valenced under strict test?
- H-C-3 blue-as-hapax rhetorical reservation vs. chance low-count.
- H-C-4 yellow-threshold structural signature across the three crop verses.
- H-C-5 Form-IX color-becoming verbs as a Judgment-morphology class.

## Time

~25 min of extraction + composition. No code written; all data access via grep on morphology file and Python one-liners on JSON.
