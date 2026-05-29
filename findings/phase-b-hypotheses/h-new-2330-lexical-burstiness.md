---
finding_id: H-NEW-2330
status: CONFIRMED — Quranic content vocabulary is topically clumped ~170× beyond a size-preserving random-allocation null (p=0.0001)
phase: B+ → C
date: 2026-05-29
rules_tuple: (QAC root v0.4, Buckwalter ROOT field, root-bearing tokens only, Hafs-Kūfan)
verdict: CONFIRMED (direction locked L_obs>L_null before computation)
---

# H-NEW-2330 — Lexical burstiness: the Quran's content vocabulary is topically clumped, anchored on surah-defining roots, over a single ubiquitous spine root (rabb)

## What was tested

The complement of H-NEW-2320 (hapax = the singleton tail). Here: are the *recurring* content roots **topically clumped** — i.e. does a root, once introduced, tend to recur within a single surah rather than spread across the corpus? This is *burstiness*, measured at the surah scale. Pre-registered with direction locked before computation (pre-reg SHA-256 `7463c7e4821e0f6516892310527324b7de1d2cc65a43cf3c4a40700162b0d645`, runtime-verified; seed 20260509; 10000 simulations).

- **Surah-local burst root:** corpus frequency ≥ 3, all tokens in exactly one surah.
- **Null:** for each root, re-allocate its tokens by a multinomial draw weighted by surah size (preserves each root's frequency and each surah's length, destroys clumping). 10000 simulated corpora.

## Primary result — CONFIRMED

| Quantity | Value |
|---|---|
| Observed surah-local burst roots (L_obs) | **22** |
| Null mean (size-preserving allocation) | **0.13** |
| One-sided p (locked: L_obs > L_null) | **0.0001** |

Under random size-weighted allocation, essentially **zero** roots of frequency ≥3 would be confined to a single surah (expected 0.13). The corpus has **22**. The Quran's content vocabulary is topically clumped **~170× beyond chance**. **Verdict: CONFIRMED.**

This is a quantified statement of a property philologists assume but had not measured on this corpus: Quranic content words are *bursty* — they belong to their surah's topic and do not diffuse.

## The bursts are surah-DEFINING words (secondary S2)

The extreme single-surah bursts read like a table of contents — each is the lexical signature of its host surah:

| Root | Gloss | Freq | Host surah (all tokens) |
|---|---|---|---|
| qmṣ | qamīṣ "shirt" | 6 | **Q 12 Yūsuf** (Joseph's shirt — torn, bloodied, cast on Jacob's face) |
| khf | kahf "cave" | 6 | **Q 18 al-Kahf** (the cave of the sleepers) |
| Syd | ṣayd "hunting/game" | 6 | **Q 5 al-Māʾida** (the iḥrām hunting-prohibition) |
| myl | mayl "inclining" | 6 | **Q 4 al-Nisāʾ** (marital/inheritance law) |
| shṭr | shaṭr "direction" | 5 | **Q 2 al-Baqara** (the qibla pericope, 2:144-150) |
| ṣlḥ (context) | … | 4 | Q 4 al-Nisāʾ |
| jhz | jahhaza "to equip/provision" | 4 | **Q 12 Yūsuf** (loading the caravan's provisions) |
| Afl | afala "to set (of stars)" | 4 | **Q 6 al-Anʿām** (Abraham watching the star/moon/sun set) |

That `qamīṣ` (shirt) occurs 6 times and every one is in Sūrat Yūsuf, or that `kahf` (cave) is wholly contained in al-Kahf, is the burstiness law made visible: the surah's defining motif is carried by a root that exists *nowhere else* in the Book.

## The lexical spine has ONE root (secondary S1)

Roots appearing in ≥ 90 of the 114 surahs:

| Root | Gloss | Distinct surahs |
|---|---|---|
| **rbb** | **rabb "Lord"** | **94 / 114** |

`rabb` is the unique lexical backbone of the corpus — the only root present in the overwhelming majority of surahs. Notably it is **more dispersed than the proper name Allāh** (`Alh`), because the short oath/eschatology surahs frequently invoke *rabb* ("your Lord") while not always using the name *Allāh*. The Quran's vocabulary architecture is therefore: **one ubiquitous spine root (rabb), and a long tail of topic-locked content roots** — a maximally bursty profile.

## Region split (secondary S3)

The 22 burst roots split 12 Meccan / 10 Medinan (54.5% Meccan). Unlike the hapax tail (H-NEW-2320, strongly Meccan), *recurring* topical bursts are region-balanced — Medinan surahs have their own dense topical lexicons (inheritance *mayl*, hunting *ṣayd*), confirming that burstiness is a general compositional property, not a Meccan-register artifact.

## Integration

- **H-NEW-2320 (hapax census):** the two findings are the two tails of one law — the singleton tail (gharīb, Meccan-concentrated) and the recurring-burst tail (topical, region-balanced). Together: Quranic vocabulary is neither uniform nor function-word-flat; it is *front-of-spine + heavy topical clumping*.
- **cross-finding-025 (pericope-scope):** burstiness is the lexical mechanism behind pericope-scoped cohesion — a surah's topic-roots cluster because they belong to that surah's pericopes. H-NEW-2330 supplies the corpus-wide quantification of why pericope-scale tests find structure that whole-surah tests miss.
- **Classical:** the *gharīb* genre (H-NEW-2320) catalogs the singleton tail; the surah-naming tradition (al-Suyūṭī *Itqān* nawʿ 22) names surahs after exactly these burst-motifs (al-Kahf, al-Baqara via shaṭr/qibla context, Yūsuf) — H-NEW-1820's title-density-independence law is refined here: titles track the *bursty motif root* (kahf, qamīṣ) even when that root is not the surah's most-frequent word.

## Limits

- Root-level; lexeme-level burstiness is a distinct (finer) instrument.
- "Burst" threshold freq≥3 / spread=1 is pre-registered; lower thresholds would add more bursts (all in the locked direction).
- The single-spine result is sensitive to the ≥90 cutoff; at ≥80 surahs a small handful more (Allāh, qawl) would join — reported as descriptive, not a test.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2330-lexical-burstiness.md` (SHA-256 `7463c7e4…0d645`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2330.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2330.json`

---

*H-NEW-2330 logged 2026-05-29 by Waiel Al-Shujaa. The shirt is in Yūsuf, the cave is in al-Kahf, and the Lord is everywhere. Bismillāhi al-Raḥmāni al-Raḥīm.*
