---
agent: numbers-spelled-1
phase: B
run: 1
date: 2026-04-12
inputs:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
outputs:
  - findings/phase-b-hypotheses/numbers-spelled.md
  - scratch/count_numbers.py, scratch/count_numbers2.py
  - scratch/numbers_output.txt, scratch/numbers_v2.txt
---

# Journal — Numbers Spelled, Run 1

## Goal
Catalog every spelled-out Arabic number (cardinals, ordinals, fractions) in
the Quran, producing surah:verse references and counts, with attention to
the ten task-specified scenes.

## What I did

1. **Read the existing `numerical-coincidences.md` dossier** (partially —
   the file is very long; read the header and the N=1, N=3 sections). Its
   structure is a per-N famous-number dossier (thematic neighborhoods,
   abjad matches, lemma counts at that frequency). It is NOT a catalog of
   spelled-out numbers per se, so this run fills the gap.

2. **Looked at data sources.**
   - `quran-text/quran-no-tashkeel.json` is a structured 114-surah JSON
     with verse-level text (Hafs numbering, basmalas counted only in
     Al-Fātiḥa).
   - `data/morphology/quranic-corpus-morphology-0.4.txt` is QAC v0.4:
     LOCATION \t FORM (Buckwalter) \t TAG \t FEATURES, with LEM/ROOT
     fields usable for lemma-level counts.
   - Given the task is to catalog *surface* occurrences (which recitation
     the reader actually sees), I worked from the no-tashkeel JSON and
     cross-checked the QAC lemmas.

3. **Wrote `scratch/count_numbers.py` (v1)** — simple token-in-set match.
   Immediately found false negatives for phrases like "بثلاثة آلاف"
   (prefix ب attached) and false positives for stems like "الف" that
   also occur as substring in الفتح.

4. **Wrote `scratch/count_numbers2.py` (v2)** — prefix-tolerant whole-word
   match. Allowed an initial proclitic in {و, ف, ب, ل, ك, س, ال, وال,
   فال, بال, كال, لل, ولل, فلل, وب, فب, ول, فل, وس, فس, ولب, فلب, بالل}.
   This caught Q 3:124 (بثلاثة), Q 22:47 (كألف), Q 8:41 (خمسه), etc.

5. **Handled phrase-level numbers** (11, 12, 13, 19, 300, 3000, 5000,
   50000, 1000 years, 40 years, 40 nights, 2000) as token-sequence matches
   with the same prefix tolerance per token. Each phrase was its own unit
   of observation.

6. **Sanity-checked polysemy**:
   - Q 12:20 "ثمن" is *thaman* "price" not *thumn* "one-eighth" — flagged
     as false positive in the thumn category; only Q 4:12 is a real
     fraction.
   - Q 47:20 "أولى" is *awlā* "more fitting / woe" not *awwal* "first" —
     flagged in prose; the 83-token *awwal* count includes ~40 *awwalīn*
     "ancients" and ~10 *awlā* "more worthy" tokens.
   - Q 2:102 *aḥad* means "anyone", not "one"; aḥad is polysemous.

7. **Checked the ten task-specified scenes** individually by pulling the
   verse texts:
   - Q 18:25 — thalāth miʾa + izdādū tisʿan = 309 ✓
   - Q 74:30 — tisʿata ʿashar = 19, 3-word verse ✓
   - Q 3:124 (3000) and Q 3:125 (5000), back-to-back ✓
   - Q 12:4 — aḥada ʿashar kawkaban = 11 stars ✓
   - Q 70:4 — khamsīn alf sana = 50,000 years ✓
   - Q 46:15 — arbaʿīn sana = 40 years (with thalāthūn shahran = 30 months) ✓
   - Q 8:41 — khums = 1/5 of spoils ✓
   - Q 4:11-12 — the complete fraction set ✓

## Findings of note (beyond what the task already named)

- **Teens are nearly absent.** The Quran spells 1-12 and 19 but never
  13, 14, 15, 16, 17, or 18. Q 74:30's "19" is literally the only
  teen-number-after-twelve in the entire text.
- **Fractions are legal-only.** The eight fraction-bearing verses (2:237,
  4:11, 4:12, 4:25, 4:176, 8:41, 34:45, 73:20) are all either inheritance /
  dowry / spoils legislation, or the night-vigil liturgical instruction of
  Q 73:20. Never cosmological.
- **Fraction set = divisors of 24.** The fractions actually used (1/2,
  1/3, 1/4, 1/6, 1/8) are the set with denominators dividing 24 — exactly
  the arithmetic closure needed for Islamic *mīrāth* math. The Quran's
  fraction vocabulary is thus *mathematically* as well as legally curated.
- **Noah's 1000-50 = 950** (Q 29:14) is the only place the Quran spells
  a number by subtraction rather than a single word.
- **Q 46:15 doubles up** 30 + 40, the only verse with two distinct
  cardinals in the same clause.
- **Q 37:147 — "a hundred thousand"** (Nineveh) is one I would not have
  listed had I gone only by famous-number lore. It's unique and large.

## What I did not do

- Did not produce a formal null model: this is a descriptive catalog, not
  a hypothesis test. Claims about 19 / 309 etc. are reported as the text's
  own self-description, not as anomalies against chance.
- Did not run full QAC-lemma cross-tabulation to char level; I used the
  text layer as primary and quoted the QAC lemma IDs as sanity checks.
- Did not inspect fractional tokens in ḥadīth or qirāʾāt (out of scope).

## Files produced
- `findings/phase-b-hypotheses/numbers-spelled.md` — the report (~3000 words)
- `scratch/count_numbers2.py` — the extraction script
- `scratch/numbers_v2.txt` — raw counts + per-verse listings
