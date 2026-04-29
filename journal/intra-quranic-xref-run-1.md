# Intra-Quranic Cross-Referencer — Run 1

**Date:** 2026-04-12  
**Agent:** intra-quranic-xref  
**Output:** `findings/intra-quranic-cross-references.md`

## Purpose

Build per-finding cross-reference blocks for the 10 priority findings in master-index.md, weaving each finding into the broader Quranic textual fabric at root, lemma, thematic, structural, muhkam/mutashabih, and self-commentary levels.

## Methodology

### Data sources loaded

- `quran-text/quran-no-tashkeel.json` — 114 surahs / 6,236 verses, primary corpus
- `data/morphology/root-index.json` — 1,642 roots, token-level (s,v,w) index
- `data/morphology/quranic-corpus-morphology-0.4.txt` — Leeds v0.4, parsed for lemma and root fields (4,832 lemmas)
- `data/translations/en.sahih.txt` — 6,236 verse lines + trailing metadata block; aligned to mushaf order after stripping `#`-prefixed header/trailer lines

### Tools written

`/tmp/xref/helper.py` — a small Python module exposing:
- `root_occurrences(root)` / `root_verses(root)` / `surah_counts(root)`
- `lemma_occurrences(lemma)` / `lemma_verses(lemma)`
- `search_sahih(pattern)` — regex probe on Sahih English
- `get_sahih(s,v)` / `get_arabic(s,v)`
- `LOC_TO_LEMMA`, `LOC_TO_ROOT` per-token lookups

All root keys use Buckwalter transliteration (Leeds convention): e.g., `*kr` for dh-k-r, `Afl` for hamza-fa-lam, `<ila`h` for ilāh with prefixed hamza and grave-accent long-alif.

### Analyses performed

1. **Root-level distribution:** Counter per surah for each priority root.
2. **Lemma-level verification:** exact-count confirmation for raHomap (114), <ila`h (147), jan~ap (147), gayor (147), srmd (2), Afl (4), muHam~ad (4), sjn (12).
3. **Semantic probes:** regex searches on Sahih for thematic clusters — "prison", "reassured", "deity other than", "O Prophet", "O Messenger", "remember(ance)", "night.*day.*sign", etc.
4. **Letter-frequency over-representation scan:** binomial z-score per letter per surah, 20 letters × 114 surahs, looking for over-represented single consonants. Found the Surah 55 refrain effect (ب z=+8.98), Surah 113 ق effect (0.082 rate), ن over-representation in Surahs 26 and 37 (rhyme-driven), and confirmed the Q 50 ق=57 anchor (z=+4.45, tied with Surah 20).
5. **Strict 1-verse root-palindrome detector:** for each verse with ≥5 stem-token roots, test if the root sequence equals its reverse. Found only Q 33:3 and Q 73:15 under strict test. Q 13:28 is chiastic at the phrase level (ABCD|CDAB) but not strict-palindromic at the token level (because of the opening relative pronoun + verb "alladhīna āmanū").
6. **Oath-cluster palindrome test:** recomputed letter counts for Surahs 91, 92, 93, 100, 103. Confirmed Q 91:1-7 is the unique full palindrome. Q 100:1-5 has a looser 3+2 near-symmetry.
7. **Co-occurrence matrix:** pairwise intersection of the 147-triple verse sets. Found ilāh ∩ ghayr = 18 verses; jannah ∩ ghayr = 7 verses; ilāh ∩ jannah = 0; triple = 0. The three lemmas at count 147 never phrasally co-occur.
8. **Abraham narrative comparison:** pulled all 25 surahs with Ibrahim (69 tokens), compared opening formulas of each retelling, identified the 26-37 twin "mādhā taʿbudūn?" opening.

## Key findings (above and beyond the 10 assignments)

### MAJOR CORRECTION needed for master-index

**Finding 2 (Yusuf sjn=12) is partially incorrect as stated.** The claim "ALL 12 occurrences are in Surah 12 (Yusuf)" is wrong per Leeds morphology v0.4:

- 9 of 12 sjn-root tokens are in Surah 12 (from lemmas `s~ijon` 6× and `yusojana` 3×)
- 1 is in Surah 26:29 (lemma `masojūniyn`, Pharaoh's threat to Moses)
- 2 are in Surah 83:7-8 (lemma `sij~iyn`, the eschatological register)

The corrected version of the finding is still remarkable — the root's **lemmas** are lexically stratified: two "literal prison" lemmas are exclusively Surah-12, and two other lemmas carry the root out to different surahs once each. The 12-surah-12-tokens coincidence still holds in a refined form but the simple "all 12 in Surah 12" claim is false. **This should be flagged in `root-cartography.md` §1 and in master-index.md.**

### New candidate rings discovered

1. **Surah 21:51-73 Abraham ring** — mirroring Al-Baqarah 131-144 at a smaller scale: rushd → idol-confrontation → fire miracle → inversion → imāma. Not in the chiastic-audit.md catalog yet.
2. **Surahs 7 and 11 are ring-twins** — the prophetic cycle (Noah → Hud → Salih → Shu'ayb) runs in both surahs with the **exact same refrain verbatim** *mā lakum min ilāhin ghayruhū*. The formulaic parallelism is explicit and algorithmically detectable.

### The 6:12 / 6:54 intra-surah refrain

Both verses contain the identical phrase **"kataba ʿalā nafsihī al-raḥma"** ("He has decreed mercy upon Himself"). This exact phrase occurs nowhere else. It is a **twin-verse self-refrain** internal to Surah 6, a micro-pattern that should be added to the refrain catalog.

### The 39:23 meta-verse

Q 39:23 (skins shiver at recitation → hearts relax at dhikr) is the single most self-commentating verse in the Quran on the 13:28 finding. It uses:
- The same *qulūb* + *dhikr* pair as 13:28
- Declares the Book to be *mutashābihan mathāniya* — self-similar reiteration  
- Describes bodily reception — physiological

Any future analysis of Q 13:28 should treat 39:23 as the **explicit Quranic commentary on the 13:28 form**.

### Sensory chiasm in Q 28:71-72

The srmd pair ends with *a-fa-lā tasmaʿūn* (do you not hear?) for the night-counterfactual and *a-fa-lā tubṣirūn* (do you not see?) for the day-counterfactual. **Hearing pairs with night, sight with day.** This sensory-content pairing is a second-layer chiasm on top of the content-mirroring. Not previously noted in the jinas-wordplay.md entry.

### The 4/5 Muhammad-name count

Adding lemma `Aḥmad` (Q 61:6, unique occurrence — Jesus predicting a messenger named Aḥmad) gives a 5-total proper-name count for the Prophet. The finding "the Quran names Muhammad 4 times" is more accurately "uses the name **Muḥammad** 4 times and the variant **Aḥmad** once, for 5 total proper-name references."

### The 113 ق anomaly

Surah 113 Al-Falaq has the **highest ق-rate of any surah at 0.082** — 4× the global rate. Not muqatta'at. Driven by: *al-falaq* (daybreak), *khalq* (create), *ghāsiq* (dark), *ʿuqad* (knots), *ḥāsid* (envier) — qaf-clustered content words. Worth flagging as a non-muqatta'at single-consonant thematic density signal, parallel to (and stronger-by-rate than) Q 50's ق density.

## Network depth per finding

| Finding | Roots probed | Lemmas verified | Cross-refs built | Muhkam anchors |
|---|---|---|---|---|
| 1. Rahma 114 | rHm, gfr | raHomap (114), r~aHoma`n (57) | ~30 verses | 6:12/54, 7:156, 17:82, 21:107, 40:7 |
| 2. Yusuf sjn | sjn (4 lemmas) | 12 total tokens, NOT all in S12 | 12+26+83 | 83:18 (ʿilliyyīn counterpart) |
| 3. Shams palindrome | sms, qmr, ywm, lyl, smw, arD, nfs | all 7 cosmic roots | 5 oath-cluster surahs tested | 17:12, 41:37, 16:12 |
| 4. Q 13:28 dhikr | *kr (292), Tmn (13), qlb (168) | 84+76+51 lemmas | 15+ dhikr-heart verses | 29:45, 39:23, 15:9, 89:27 |
| 5. Abraham ring | — | <iboraAhiym (69 in 25 surahs) | 12 retellings compared | 60:4, 4:125, 2:124 |
| 6. Qaf density | — | — | 20 letters × 114 surahs scan | 3:7, 50:1 |
| 7. Muhammad name | Hmd | muHam~ad (4), 'aHomad (1) | 13 "O Prophet" + 2 "O Messenger" | 33:40, 48:29, 21:107 |
| 8. Afl chain | Afl | 4 tokens in 3 verses | 6 anti-astrolatry verses | 41:37 |
| 9. 147 triple | — | <ila`h + jan~ap + gayor | 18 ilāh+ghayr verses | 2:255, 2:163 |
| 10. srmd pair | srmd | 2 tokens in 2 verses | 6 day/night-sign verses | 36:40, 17:12, 13:3 |

## Time spent

~2 hours of analysis. Most time was spent building the helper module and tracing lemma ↔ root ↔ verse mappings. The output document is ~50KB of dense cross-referencing.

## What I did NOT do

- I did NOT run a full chi-square or null-model test on any new cross-reference claim. Cross-referencing surfaces connections; it doesn't statistically validate them. Claims like "Surahs 7 and 11 are ring-twins" would need their own null-model test to claim structural significance.
- I did NOT exhaustively process ALL findings in master-index — only the 10 priority findings. The other findings (Jahannam-77, Bismillah-19 family, word-pair family, Kahf Dhul-Qarnayn ring, etc.) remain uncovered and could be processed in a Run 2.
- I did NOT re-verify the Leeds v0.4 morphology file's tokenization against an independent lemma source. The 339 rHm count vs the raHomap 114 count rests on Leeds conventions.

## Next steps

1. Propagate the **sjn correction** into root-cartography.md §1 and master-index.md.
2. Add the **Abraham Surah 21:51-73 candidate ring** to the chiastic audit catalog for formal testing.
3. Add the **6:12 / 6:54 "kataba ʿalā nafsihī al-raḥma"** twin-verse refrain to the refrain catalog.
4. Investigate whether **Q 39:23 as meta-commentary** for the whole mathānī concept deserves its own finding entry.
5. Formal null-model test: is the "18 verses of *ilāh + ghayr* exactly split into one prophet-cycle formula across Surahs 7 and 11" a structural coincidence or intentional?
