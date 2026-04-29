# Fire/Light Vocabulary — Run 2 (Phase B)

**Date:** 2026-04-12
**Data source:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4)
**Script:** `scripts/fire_light_extract.py` (new)
**Outputs:**
  - `findings/phase-b-hypotheses/fire-light-vocabulary.md`
  - `findings/phase-b-hypotheses/csv/fire-light-{nwr,DwA,srj,SbH,qbs,shhb,nfx,wqd,rmd,Swr}.csv`

## Method

Extracted all morphology segments whose `ROOT:` feature matched one of ten target codes. For each segment, captured location, form, POS, lemma, and tag; grouped by root and lemma; cross-referenced against the no-tashkeel JSON text for verse-level context.

First-pass root codes guessed from transliteration — one correction: *ḍiyāʾ* lives under `ROOT:DwA` (not `Dw'`). Confirmed by grepping unique ROOT values against the pattern `^ROOT:(nwr|DwA|srj|SbH|qbs|\$hb|nfx|wqd|rmd|Swr)$`; all ten resolved.

## Findings registered in the main file

1. Root-level counts: nwr 194 (naAr 145 / nuwr 43 / muniyr 6); wqd 11; nfx 20 (10 of which are horn-blasts); SbH 45 (only 4 are miṣbāḥ; the rest are ṣubḥ/aṣbaḥa). Shihāb = 5, qabas = 3, sirāj = 4, ḍiyāʾ = 6, ramād = 1 (hapax).

2. Surah 24 density: 13 of 14 fire/light tokens in this surah are inside verse 35 (Light Verse). The only nār in 24:35 appears in an **explicitly negated** clause (*wa-law lam tamsashu nār*) — the only place in the Qurʾān where the oil's luminosity is asserted *independent of* fire.

3. Q 2:17 uses four distinct fire/light roots (wqd, nwr, DwA, and the implied contrast with ẓulumāt) in one verse. The verb *istawqada* is a hapax form and is middle/reflexive — the hypocrite kindles his own fire.

4. Q 57:13 quotes the Mosaic qbs root back at the hypocrites: *naqtabis min nūrikum*. Moses's word for his domestic firebrand (*qabas*, 20:10) becomes the verb the hypocrites use to beg for a share of believers' light. It is refused. This is a deliberate lexical linkage late in the Medinan corpus back to the Mosaic theophany in the Meccan corpus.

5. The horn (Swr = 19 segments total, but 10 specifically the *ṣūr* noun in the horn-phrase *fī l-ṣūr*) always pairs with passive *nufikha/yunfakhu*. Q 39:68 is the only double-blast verse.

6. The root نفخ (nafakha) carries three theological acts: creation (Adam — 15:29, 32:9, 38:72; Mary — 21:91, 66:12), miracle (Jesus breathing life into clay bird — 3:49, 5:110), and judgment (horn — 10 instances). Genesis and apocalypse share a lexical root.

7. *Sirāj* (4 tokens) attaches to sun (71:16), Prophet (33:46), and stars in general (25:61, 78:13). Q 71:16 pairs sirāj-sun with nūr-moon; Q 10:5 pairs ḍiyāʾ-sun with nūr-moon. Emitter-vs-reflector vocabulary is stable.

## Open follow-ups

- Root صلي (to roast in the fire) — not queried; adds to the fire field.
- Root جذو (jadhwah, 28:29) — probable hapax, deserves separate audit.
- The *nūr 49* vs *nuwr 43 + muniyr 6* convention: classical count adds munīr as nūr-variant; Leeds separates them.
- Could cross-reference the chronological sequence: shihāb cluster is Meccan (15, 37, 72), *nūr ʿalā nūr* is Medinan (24), hypocrite-iqtabisa is late Medinan (57). The qbs-light arc runs chronologically Meccan→Medinan.

## Process notes

- Running a syntax-check on python f-string escapes: `\\'` inside an f-string was the first error; pulled the sanitisation out into a variable.
- The DwA / Dw' root-code ambiguity cost one extra run; worth grepping unique ROOT codes before committing to a Buckwalter guess.
