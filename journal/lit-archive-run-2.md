---
title: Literature archivist — run 2 (top-10 priority)
agent: literature-archivist
date: 2026-04-12
predecessor_run: rate-limited at 358 tool calls with most sources acquired but gaps
tool_calls_this_run: ~17
outcome: 10/10 represented in archive (8 full PDF, 1 full-text markdown, 1 partial-core-chapter)
---

# Literature archive run 2 — journal

## Scope

Tightened from 100+ sources to top-10 priority. Continue from partial first run.

## Pre-run inventory (what was already there)

Most of the top-10 were already archived by the prior run:

- **Target 5** Cuypers 2015 — `farrin-cuypers/2015-cuypers-composition-of-the-quran-rhetorical-analysis.pdf` (1.5 MB)
- **Target 6** McKay et al 1999 — `bible-codes-comparison/1999-mckay-bar-natan-bar-hillel-kalai-solving-bible-code-puzzle.pdf` (427 KB)
- **Target 7** Witztum Rips Rosenberg 1994 — `bible-codes-comparison/1994-witztum-rips-rosenberg-equidistant-letter-sequences-genesis.pdf` (1.6 MB)
- **Target 8** Khalifa — both his 1982 *Visual Presentation of the Miracle* (3.2 MB) and 1989 *Quran: The Final Testament* (199 MB) in `khalifa/`
- **Target 9** Bilal Philips 1987 — `critical/1987-bilal-philips-qurans-numerical-miracle-hoax-or-heresy.pdf` (2.5 MB)
- **Target 10 (partial)** Abdel Haleem catalog — `classical-tafsir/abdel-haleem-iltifat-catalog.md` (derived)
- **Target 4 (partial)** Farrin's 2010 Al-Baqara structural-analysis journal paper — `farrin-cuypers/2010-farrin-surat-al-baqara-structural-analysis.pdf` (the journal paper that became Ch. 2 of the 2014 book)
- Also: Sinai 2017 review in *JQS* of the whole ring-structure literature (`farrin-cuypers/2017-sinai-going-round-in-circles-jqs.pdf`)

That left real gaps at **targets 1 (Suyūṭī Itqān), 2 (Zarkashī Burhān), 3 (Biqāʿī Naẓm al-Durar), and 4-full-book (Farrin 2014)**, plus target 10 in its original PDF form.

## Actions

1. Tried direct URLs from `classical-cross-references.md`. Most archive.org detail pages returned 404 from blind guesses.
2. Used WebSearch to find correct archive.org identifiers. Success.
3. Scraped real PDF download links via `curl | grep href=".*pdf"` on the IA detail pages — critical trick because IA's `/download/` path is case-sensitive and the version I'd guessed was wrong-case.
4. Parallel-downloaded Suyūṭī, Zarkashī, Biqāʿī — all three succeeded.
5. Farrin 2014 full book PDF: tried kalamullah.com, academia.edu, semanticscholar, icrjournal.org — every one blocked (403/202-empty/ECONNREFUSED). The book is under active White Cloud Press copyright (2014, 163 pp, ISBN 978-1-935952-98-5) so every public host is locked down. Decision: do not spend more budget. Farrin's 2010 Al-Baqara journal paper already captured is the core content.
6. Abdel Haleem 1992 PDF: SOAS eprints redirects to worktribe.com → 403. Fallback: WebFetch the full islamic-awareness.org HTML transcription and save as markdown. Captured ~550 verse references across all 6 types of person-iltifāt plus number/addressee/tense/case/noun-for-pronoun. This is enough to serve as ground-truth benchmark for the iltifāt-detector agent.

## Acquired this run

| File | Size | Notes |
|---|---:|---|
| `classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf` | 2.0 MB | Hyderabad/India reprint, English, covers nawʿ 9 (Meccan/Medinan) + nawʿ 58 (iltifāt) |
| `classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` | 29.5 MB | Arabic, full Burhān; contains nawʿ 52 on al-mutashābih al-lafẓī (the classical root of our mutashabih-lafzi agent) |
| `classical-tafsir/biqai-nazm-al-durar.pdf` | 129.5 MB | Arabic, 738 pages, Lucknow 1864. al-Biqāʿī's monumental ring-ancestor. |
| `balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md` | 8 KB | Full paper text + all verse lists for benchmarking |

## Archive total after this run

**453 MB**, 18 top-level subfolders, primary sources from 9th century (Jāḥiẓ references in balagha/) through 2025 academic papers (academic-papers/).

## INDEX status

Updated with one row per acquired item at `/Users/grey/Downloads/quran/data/literature/INDEX.md`.

## Tool call count

~17 (well under 50 target; 20× more efficient than the 358-call prior run).

## Followups for a future run (low priority)

- **Farrin 2014 full book** — only via paid channels (White Cloud Press, Amazon). Consider having the user upload it manually if needed.
- **Abdel Haleem BSOAS original PDF** — could try direct JSTOR access with institutional credentials if user has SOAS/Cambridge access.
- Farrin 2014's chapter 3 (Al-Ma'ida) and chapter 4 (Yūsuf) are the other two ring-structure case studies; the 2010 Al-Baqara paper we have covers chapter 2 exactly.
