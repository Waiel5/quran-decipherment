---
agent: verse-annotator-run-1
date: 2026-04-12
phase: aggregation
status: complete
---

# Per-verse annotator — run 1

## Goal
Build compressed annotation for every one of the 6,236 Hafs Kufan verses, drawing
from all 85+ findings files, so any downstream tool can answer "which findings
touched verse S:V?"

## Method

1. **Verse universe** derived from `data/hafs-verse-counts.tsv` (114 surahs,
   6,236 verses verified).
2. **Structured CSVs**: parsed directly into per-verse tags:
   - `divine-names-by-verse.csv` → `divine-names`, `divine-name-cluster` (≥3),
     `divine-name-pair-ending`.
   - `hapaxes-full-list.csv` → `hapax` (root/lemma/form hapaxes).
   - `iltifat-per-verse.csv` → `iltifat` (only strict-intra or strict-inter shifts).
   - `mutashabih-pairs.csv` → `mutashabih-lafzi` (both members tagged).
   - `parables-full-list.csv` → `parable`.
   - `quotations-catalog.csv` → `quotation`.
   - `rhetorical-questions-per-verse.csv` → `rhetorical-question` and
     `rhyme-break` (when `is_rhyme_break=1`).
   - `vocatives-per-verse.csv` → `vocative`.
   - `csv/innama-verses.csv` → `innama`.
   - `csv/oath-clusters.csv` → `oath-cluster` (expanded to every verse in each
     start–end span).
   - `csv/imperatives-qul-catalog.csv` → `qul-say-opener`.
   - `csv/imperatives-all-tokens.csv` → `imperative`.
   - `csv/imperatives-prohibitive.csv` → `prohibitive`.
   - `csv/dual-tokens.csv` → `dual-form`.
   - `saj-fasila-per-verse.csv` → `rhyme-break` in uniform-rhyme surahs
     (modal rhyme ≥70% share; deviating verses flagged).
3. **Markdown S:V extraction**: regex `(\d{1,3})[:.](\d{1,3})` scanned across
   every `.md` in `findings/`, `findings/phase-a-replications/`,
   `findings/phase-b-hypotheses/`, `findings/phase-c-structures/`. Each file
   mapped to a coarse topic tag via `FILE_TAG_MAP`. Header-line heuristic:
   verses mentioned under a section whose header contains "highlight", "key
   verse", or "witness" get an additional `highlight` tag.
4. **Hand-coded structural sets**: Fatiha (1:1–7), Ayat al-Kursi (2:255),
   longest-verse (2:282), Baqarah 131–144 (Ibrahim/Qibla pivot),
   Kahf pivots (18:1,9,10,17,22,25,28,32,45,50,60,65,74,82,83,98,103,104,109,110),
   Maryam 1–40 nativity & 16–35 Jesus pericope, Hashr 18–24 khawatim,
   Ar-Rahman (all 78 verses, with the 31 refrain-verses tagged),
   Al-Ikhlas (all 4), Al-Falaq + An-Nas (muawwidhat), Hadid 1–6 & 25,
   Muqattaʿat openers (29 surahs), basmala (1:1 + 27:30 embedded),
   Muhammad-naming verses (3:144, 33:40, 47:2, 48:29, 61:6 Ahmad),
   prophecy verses (30:2–4 Rum, 110:1–2, 54:45, 48:27, 5:67, 15:9),
   scientific-foreknowledge claims (21:30,33; 36:38,40; 51:47; 55:19–20,33;
   23:12–14; 75:37–39; 25:53; 24:40; 16:68–69; 30:48; 39:6; 50:6; 79:30;
   86:6–7), oath-opener surahs (37,51,52,53,56,68,69,75,77,79,81,85,86,
   89–93,95,100,103) first 5 verses.
5. **Translations** loaded from `data/translations/en.sahih.txt-2.txt`
   (pipe-delimited) for the unannotated verses listing.

## Outputs

- `findings/per-verse-annotations.md` — surah-by-surah readable index with
  top-10 table, distribution-by-surah table, and compact tag+note lines
  per annotated verse.
- `findings/per-verse-annotations.csv` — 5,778 rows, columns:
  `surah, verse, n_tags, tags (semicolon-joined), brief_note`.
- `findings/verses-with-no-annotations.csv` — 458 rows with translation preview.

## Numbers

- Annotated verses: **5,778 / 6,236 (92.6%)**.
- Un-annotated: **458**.
- Top surahs by un-annotated count: 37 (29), 26 (26), 56 (21), 51 (14), 83 (12),
  80 (12), 23 (12), 84 (11), 74 (11), 52 (11). These are overwhelmingly
  narrative-heavy late-Meccan surahs where the CSV corpora (divine names,
  hapaxes, vocatives, parables etc.) are less dense and where findings files
  cite surah ranges rather than individual verses.

## Top-10 most-annotated verses (after run)

| rank | S:V | tags |
|---:|---|---:|
| 1 | 1:1 | 29 |
| 2 | 1:5 | 29 |
| 3 | 1:4 | 29 |
| 4 | 1:2 | 26 |
| 5 | 1:3 | 23 |
| 6 | 2:255 | 22 |
| 7 | 5:3 | 21 |
| 8 | 2:282 | 20 |
| 9 | 3:2 | 19 |
| 10 | 5:1 | 19 |

Al-Fatiha dominates because Fatiha is used as illustration/control across
nearly every finding. 2:255 (Ayat al-Kursi), 5:3 (the "today I have perfected"
verse), 2:282 (longest / debt verse), 3:2 (Al-Hayy al-Qayyum divine-name
climax), 5:1 (Ma'idah opener — covenant/vocative/hapax dense) are the next
legitimate density peaks.

## Honest coverage gaps

1. **Late-Meccan oath / eschatology surahs** (37, 26, 56, 51, 83, 80) are
   under-annotated mid-surah. Our oath-opener rule only tags verses 1–5 of
   each oath-surah; the long narrative middles drop out unless they carry
   a hapax, vocative, or were cited in a finding. A follow-up agent
   should per-verse scan surahs 37 and 26 specifically.
2. **`highlight` tag is regex-based**, not an authoritative pull from a
   "Highlights:" frontmatter field. Some findings use "Witness verses",
   "Key examples", "Case study" headers that were not included.
3. **Verse-range citations** like "Q 37:83–113" inside findings currently
   only tag the two endpoints (37:83 and 37:113), not every verse in the
   span. A span-expander pass would raise coverage by perhaps 100–200 verses.
4. **Classical scientific-foreknowledge** claims are hand-coded from my
   reading of `scientific-foreknowledge-run-1` — I may have missed a few
   flagship verses the underlying finding cites.
5. **Muhkam vs mutashābih**: only verses cited in the `muhkam-mutashabih.md`
   finding get the tag; the broader classical classification across the whole
   corpus was not applied.
6. **Prophet-micro-ring centers**: currently inherited from generic S:V regex,
   not from a dedicated "center" field. Identification of which verse is the
   **center** (vs just a member) of each ring is not distinguished in the
   tag set.

## Possible next runs

- Span-expander to fully populate verse ranges cited in findings.
- Ring-center–only pass that tags just center verses from
  `phase-c-structures/ring-center-semantics.md` and `prophet-micro-rings.md`.
- "Highlight" strict pass reading YAML frontmatter `highlights:` fields if
  any findings use them.
- Coverage sweep for the 458 un-annotated verses — each one should be
  either explicitly labeled "no-marker" or acquire at least one tag.

## Artifacts

- Script: `/Users/grey/Downloads/quran/scratch/verse-annotator/annotate.py`
- Run: single invocation, deterministic.
- Runtime: ~4 s.
