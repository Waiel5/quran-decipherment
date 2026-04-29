---
agent: parables-run-1
phase: B
date: 2026-04-12
---

# Parables run 1 — journal

## Inputs
- Leeds morphology (`data/morphology/quranic-corpus-morphology-0.4.txt`), root
  filter `ROOT:mvl` — 169 segment hits across **148 unique verses**.
- Sahih International translation aligned to hafs verse counts (6,236 verses,
  file has 6,249 lines due to trailing comments; alignment verified by
  endpoints 2:1, 2:286, 3:1, 114:1, 114:6 all correct).
- Hand-curated supplementary list of 32 ka-prefix similes that lack the
  m-th-l root (e.g., Q 54:7 locusts, Q 63:4 propped logs, Q 101:4 moths,
  Q 2:19-20 rainstorm/lightning, Q 24:39 mirage, Q 24:40 darkness-on-sea).

## Method
1. Extract all m-th-l occurrences → 148 verses.
2. Pull translations; classify each manually per 4-type scheme
   (A extended / B condensed / C meta / D apophatic / E non-parable mithl).
3. Augment with ka-only similes (the 32).
4. Filter non-parable uses of mithl (legal-equivalence *mithl ḥaẓẓ al-unthayayn*,
   lex-talionis *mithla mā iʿtadā*, ransom *mithlahu maʿahu*, prophetic refrain
   *basharun mithlukum* ×18, etc.). 84 out of 148 m-th-l verses fail as
   parables. The 96 surviving parables break down A:39 B:32 C:20 D:5.
5. Build tenor→vehicle map; find exclusivities; find adjacent-pair
   patterns; probe Q 24:35 density quantitatively.

## Counts (final)
- m-th-l root verses: 148
- + ka-only famous similes: 180 total
- Genuine parables (A/B/C/D): **96**
  - A (extended): 39
  - B (condensed simile): 32
  - C (meta-frame): 20
  - D (apophatic): 5

## Key findings
1. Q 24:35 has 5 comparison markers in 40 Arabic words, ~3× the average
   extended-parable density. Three hapax vehicles in one verse.
2. Q 24:35 and Q 24:40 form a deliberate light/darkness parable pair
   5 verses apart, sharing the lexeme *nūr* at both ends of the sequence.
3. Five adjacent-parable pairs identified (listed in catalog §9). Adjacency-
   as-antithesis is a systematic Quranic device.
4. Rain and garden are the only polyvalent vehicles (used for both
   believers and disbelievers across different verses). The reverse-parable
   mechanism exploits this.
5. *bal … aḍall* ("nay, more astray") is a small novel rhetorical
   subcategory — explicit hyperbolic exceeding of the simile's vehicle.
6. 13 vehicles used exclusively for disbelievers/hypocrites; 5 exclusively
   for believers. Cattle/dog/donkey/spider/fly/ashes/mirage/propped-
   logs/fire-extinguished/Satan-abandoning/scattered-moths/frost-wind/
   smooth-stone-in-rain form the "negative" pole.

## Honest ledger
- Classification into A/B/C/D is hand-labeled; a second pass could
  shift a dozen borderline cases (especially B vs C). The counts
  should be read as ±5.
- Arabic density measurement in §5 is rough; an exact morpheme count
  from Leeds would give a precise denominator.
- Classical al-Māwardī's *Amthāl al-Qurʾān* and Ibn al-Qayyim's
  monograph are referenced but not consulted verbatim — WebSearch /
  WebFetch declined to avoid broken tool schema (schemas are deferred
  under this harness). Classical claims rely on cross-references
  already in the project's `classical-cross-references.md`.

## Outputs
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/parables-catalog.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/parables-full-list.csv`
- This journal.
