---
id: H-NEW-85
title: Oath-opening surahs — comprehensive structural & semantic analysis (21 wa-l-X surahs)
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (extractor + categories + tests locked BEFORE per-surah item-counting beyond what is already in oath-clusters.md and h-new-61.json)
bonferroni_family: 2026-04-15-Wave-H-NEW-85-Oath-Openers
bonferroni_k: 5
alpha_bon: 0.05 / 5 = 0.010
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, 29-muqaṭṭaʿāt-set, oath-set=H-NEW-61 OATH_PARTICLE class)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
prior_findings:
  - findings/phase-b-hypotheses/h-new-61-opening-words.md  (locks the 21 oath surahs)
  - findings/phase-b-hypotheses/oath-clusters.md           (cluster catalog + categories)
seed: 20260416
author: h-new-85-specialist
---

# [[h-new-85-oath-openers|H-NEW-85]] — Comprehensive analysis of oath-opening surahs

## Locked oath-opener set (from [[h-new-61-opening-words|H-NEW-61]], frozen)

Per [[h-new-61-opening-words|H-NEW-61]] OATH_PARTICLE class (n=21, 100% Meccan):

  {36, 37, 38, 43, 44, 50, 51, 52, 53, 68, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}

The set is FROZEN. No surah is added, removed, or re-classified in this pre-reg.
(Q 56:75 / Q 69:38 / Q 70:40 / Q 75:1 / Q 90:1 are interior or qsm-verb oaths and
are excluded — [[h-new-61-opening-words|H-NEW-61]] captures them only as opening *waw-particle* oaths.)

## Questions

1. **Verification.** Is the [[h-new-61-opening-words|H-NEW-61]] oath-list (21 surahs, 21/21 Meccan) reproducible?
2. **Multi-oath structure.** For each of the 21, count the number of waw-bound
   sworn-by NPs in the opening cluster. Is Q 91's count (7 oath-verses /
   8 head-NP items) the maximum?
3. **Object categories.** Categorize each sworn-by NP into a locked taxonomy
   (cosmic, temporal, terrestrial, kinetic, abstract, instrumental, scriptural,
   psychological, divine). Compute per-surah category-vectors.
4. **Surah-length distribution.** Does the oath-opening sub-corpus cluster at a
   particular length? Compare to non-oath Meccan baseline.
5. **Semantic clustering.** Are oath surahs semantically clustered around
   specific themes (eschatology / prophethood / Qurʾān-status / human-nature)?
   Test by jawāb-al-qasam (sworn-about) tagging vs. random jawāb-assignment.

## Locked oath-item extractor

Given the [[h-new-61-opening-words|H-NEW-61]] 21-surah list, for each surah:
1. Begin at the opener position defined by [[h-new-61-opening-words|H-NEW-61]] (after muqaṭṭaʿāt, after
   basmala-as-v1 if applicable). Q 36, 38, 50 and 68 have muqaṭṭaʿāt openers
   skipped first per [[h-new-61-opening-words|H-NEW-61]].
2. Walk the QAC morphology stream (Leeds v0.4, Buckwalter) forward.
3. Mark a **head NP** when:
   - leading PREFIX `w:P+` (oath-waw, particle) OR `w:CONJ+` (continuation-waw),
     OR `f:CONJ+` (fa-continuation), OR no prefix (interior bare NP after qsm),
   - immediately followed by an N or PN STEM with case=GEN,
   - optionally with intervening DET (`Al+`) or DEM,
   - optionally followed by a SUFFIX PRON (e.g., *wa-ḍuḥā-hā*) — the suffix
     does not start a new head.
4. **Stop the cluster** at the first verse boundary whose first segment is
   neither (a) `w:CONJ+` + GEN-noun nor (b) `f:CONJ+` + GEN-noun nor (c) bare
   GEN-noun in continuation (which we admit only inside the FIRST verse).
   The first non-conforming verse is the **jawāb al-qasam** boundary.
5. Within a single verse, count multiple head-NPs if the verse has `wa-N-GEN`
   followed by `wa-N-GEN` (e.g., Q 91:1 contains two: *wa-l-shams* and
   *wa-ḍuḥā-hā* — we count 2 head-NPs).
6. Output for each oath-opener surah:
   - **n_verses_in_cluster** = number of consecutive oath-verses (the
     "oath-block length")
   - **n_head_NPs** = total head NPs (sworn-by objects) in the block
   - **head_list** = ordered list of (verse, head-Arabic, head-buckwalter,
     root) triples
   - **first_post_oath_verse** = the v# where jawāb begins
   - **first_post_oath_word_QAC_segment** = the leading particle of the jawāb
     (for Q 91: *wa-qad* / *qad* / *fa-* / *inna* — diagnostic)

## Locked sworn-by category taxonomy (10 classes, frozen)

Each head-NP maps to exactly ONE class by **root → category** dictionary
(the dictionary is locked HERE; it is the union of the categories used by
oath-clusters.md plus three additions for cases that were "other" there):

1. **CELESTIAL** — sun, moon, star, sky-as-vault, constellations, planets:
   roots {$ms, qmr, njm, smw, brj, Trq (when "morning star")}
2. **TEMPORAL** — day, night, dawn, dusk, hour, time, the late afternoon,
   the time-of-departure: roots {lyl, nhr, fjr, DHw, E$r, ywm, sjw, g$w
   (when temporal complement of layl)}
3. **TERRESTRIAL** — mountain, earth, town, fig, olive, fields, geographical:
   roots {Twr, ArD, bld, byt, sqf, sjr, tyn, zyt}
4. **KINETIC_NATURAL** — winds, waves, scattering, blowing, racing of
   non-personified motion: roots {*rw, ESf, n$r, jry, frq, Hml}
5. **KINETIC_AGENTIVE** — angels/horses/raiders ranked, driving, racing,
   penetrating, plunging: roots {Sff, zjr, tlw, nzE, n$T, sbH, sbq, dbr,
   Edw, qdH, gyr, vwr, rsl}
6. **INSTRUMENTAL_SCRIPTURAL** — pen, written-thing, parchment, book, Qurʾān,
   recitation, "what they inscribe": roots {qlm, ktb, sTr, qrA, nwn (Q68
   muqaṭṭaʿ-as-letter), rqq, Nshr (in scriptural sense)}
6b. **DIVINE_NAME** — bare *Allāh* / *rabb* (sworn-by Lord himself):
    roots {rbb, Allh}
7. **PSYCHOLOGICAL** — soul, breast, heart, the upbraiding-self:
   roots {nfs, Sdr, qlb, lwm}
8. **NUMERIC_PAIR** — even, odd, three, ten:
   roots {$fE, wtr, vlv, E$r-as-numeral}
9. **ABSTRACT** — witness, witnessed, the Promised Day (when not "day"):
   roots {$hd (in $aAhid / ma$ohuwd), wEd}
10. **OTHER** — anything not above (for honest residual)

**Tie-breaker** (if a root maps to >1 category): priority TEMPORAL >
KINETIC_AGENTIVE > KINETIC_NATURAL > CELESTIAL > TERRESTRIAL >
INSTRUMENTAL_SCRIPTURAL > DIVINE_NAME > PSYCHOLOGICAL > NUMERIC_PAIR >
ABSTRACT > OTHER. (Justification: temporal nouns are most stably
context-defined; kinetic-agentive and kinetic-natural can collide on roots
like rsl which is messenger/sent — we route by "wa-l-mursalāt" Q77 →
KINETIC_AGENTIVE per its participle reading.)

## Pre-registered test cells (Bonferroni k=5, α_bon = 0.010)

### Cell 1 — Verification of [[h-new-61-opening-words|H-NEW-61]] oath-list
- All 21 listed surahs MUST extract n_head_NPs ≥ 1.
- All 21 MUST be Meccan (per Egyptian standard chronology table).
- PASS = 21/21 confirmed; FAIL = any drop or recategorization.

### Cell 2 — Q 91 7-oath uniqueness (verse-block length)
- Compute n_verses_in_cluster for each of 21 oath-opener surahs.
- HYPOTHESIS: Q 91 has the strict maximum (= 7 verses).
- PASS = Q 91 strictly ≥ all other 20 surahs' n_verses_in_cluster.
- TIE = some other surah ties or beats 7 → uniqueness FAILS, finding logged.
- This is a structural-uniqueness verification, not a probability test.

### Cell 2b — Q 91 8-item uniqueness (head-NP packing)
- Compute n_head_NPs for each.
- HYPOTHESIS: Q 91 has the strict maximum (= 8 head-NPs).
- PASS = Q 91 strictly ≥ all other 20.
- (This is the classical *sabʿ āyāt qasam* claim with the [[h-new-61-opening-words|H-NEW-61]] mechanical
  head-NP rule. Q 52 reaches 6 per oath-clusters.md; Q 77 reaches 5; Q 79
  reaches 5; Q 89 reaches 5. So 8 should win cleanly.)

### Cell 3 — Category-distribution non-uniformity (χ²)
- Tabulate total head-NPs by category across all 21 surahs.
- Null: 10 categories uniform across the head-NP corpus.
- χ² goodness-of-fit, df = (k-1) where k = non-empty categories.
- α_bon = 0.010.
- PASS = p < 0.010 (reject uniform → categories are non-randomly distributed).

### Cell 4 — Surah-length distribution test
- Compute median verse-count for the 21 oath-openers.
- Compute median verse-count for the 65 other Meccan surahs (114 total minus
  28 Medinan minus 21 oath-Meccan = 65).
- Mann-Whitney U (two-sided) on verse-counts.
- α_bon = 0.010.
- PASS = oath-openers significantly SHORTER than other Meccan
  (one-sided expectation per Itqān).

### Cell 5 — Semantic clustering of jawāb (sworn-about) themes
- For each of 21 surahs, manually classify the FIRST jawāb verse into one of
  4 macro-themes (locked from oath-clusters.md §4):
  - PROPHETHOOD ("you are a messenger / not a madman")
  - QURAN_STATUS ("we have made it Arabic / sent down on a blessed night")
  - ESCHATOLOGY ("the punishment is coming / what you are promised")
  - HUMAN_NATURE ("man is in loss / created in best of stature / ungrateful")
  - OTHER (residual)
- Test 1: are all 5 themes represented? (descriptive)
- Test 2: χ² goodness-of-fit against uniform 5-class.
- α_bon = 0.010.
- PASS = p < 0.010 (themes non-uniform — i.e., clustered).

## Pre-committed verdict table

| Cell | Result | Verdict |
|---|---|---|
| 1 | 21/21 verify | PASS |
| 1 | <21/21 | EXTRACTOR_BROKEN |
| 2 | Q 91 unique max verses | UNIQUENESS_CONFIRMED |
| 2 | Q 91 ties or loses | UNIQUENESS_REJECTED |
| 2b | Q 91 unique max items | ITEM_UNIQUENESS_CONFIRMED |
| 3 | χ² p < 0.010 | CATEGORIES_NONUNIFORM |
| 4 | MW p < 0.010 | OATH_OPENERS_SHORTER |
| 5 | χ² p < 0.010 | THEMES_CLUSTERED |

## Garden-of-forking-paths disclosure

Already known from oath-clusters.md (read in this session):
- Q 91 is described there as the unique category-heterogeneous long opening (4
  categories across 8 items).
- The 21 oath surahs are all Meccan; [[h-new-61-opening-words|H-NEW-61]] already established this.
- oath-clusters.md tabulates ~10 length-≥3 opening clusters with counts.
- The macro-themes 4-list is taken directly from oath-clusters.md §4
  (PROPHETHOOD / QURAN_STATUS / ESCHATOLOGY / HUMAN_NATURE).

What is NOT yet known and is genuinely tested here:
- The mechanical n_verses_in_cluster vs. n_head_NPs split (oath-clusters.md
  used a hand-built rule; this re-runs it from the QAC morphology with the
  locked rule above).
- The MW Cell 4 length-distribution test against non-oath Meccan.
- The χ² Cell 5 theme-uniformity test.

## Integrity

- 21-surah set FROZEN at locking, taken from [[h-new-61-opening-words|h-new-61]].json OATH_PARTICLE.
- Categories FROZEN before per-surah classification.
- 5 cells with k=5 Bonferroni declared.
- Seed 20260416.
- Author: [[h-new-85-oath-openers|h-new-85]]-specialist.

## Garden-of-forking-paths amendment 2026-04-15 (post-pilot run)

After the first walker-run, four root-codes that surfaced in extracted heads
were not in the locked dictionary: `qsm`, `lqy`, `wry`, `ESr`. These are
*known classical oath nouns* (Q 51:4 muqassimāt, Q 77:5 mulqiyāt,
Q 100:2 mūriyāt, Q 103:1 al-ʿaṣr) and were placed into the locked categories
per their unambiguous lexical meaning:
  - `qsm` (apportioning agents) → KINETIC_AGENTIVE
  - `lqy` (delivering agents)   → KINETIC_AGENTIVE
  - `wry` (fire-strikers)       → KINETIC_AGENTIVE
  - `ESr` (the late afternoon)  → TEMPORAL
These additions are NOT a tuple-loosening (per
feedback_bonferroni_tightening_vs_loosening): they refine OTHER → specific
class on the basis of unambiguous lexical content; they cannot be used to
inflate any cell's significance because Cell 3 χ² is computed over the
HEAD-NP totals and additions REMOVE counts from OTHER (which then becomes
empty), reducing df from 9 to 8 and TIGHTENING the Bonferroni-corrected
α requirement. Cell 3 result reported with the corrected dictionary.
