---
run: oath-clusters-run-1
date: 2026-04-12
agent: oath-clusters (Phase B, novelty)
status: complete
output: findings/phase-b-hypotheses/oath-clusters.md
---

# Oath-clusters run — journal

## What I set out to do

Task was to build the first comprehensive computational catalog of Quranic
oath clusters (qasam). The hypothesis was that these most-marked rhetorical
passages would expose patterns classical scholarship had only qualitatively
noted.

## Method I chose

Two oath-opening patterns from Leeds morphology:
1. `waw-oath` = verse opens with waw-prefix (P or CONJ, form 'w') + optional
   DET/DEM + noun/PN/ADJ in **genitive** case. Genitive is the diagnostic
   al-Farrāʾ rule for `wāw al-qasam` (oath waw governs genitive, conjunctive
   waw does not).
2. `qsm-oath` = verse has root=qsm verb (`uqsimu`, "I swear"), possibly with
   leading NEG/REM/CONJ (for "lā uqsimu" / "fa-lā uqsimu" / "wa-lā uqsimu"),
   followed by `bi` + genitive noun.

Plus `fa-CONJ + GEN noun` is permitted as continuation of an already-started
cluster (Q 51:2–4 "fa-l-ḥāmilāti… fa-l-jāriyāti…"). Within-verse item-packing
is also scanned, so Q 86:1 correctly registers as 2 sworn-by items (heaven,
night-star) and Q 91:1 as 2 items (sun, brightness).

## Iterations

1. First-pass detector used CONJ-tag only for waw; missed all opening verses
   of oath surahs, because the FIRST waw of a cluster is tagged `P`
   (preposition = oath particle), not `CONJ`. Fixed by allowing both.
2. Added GEN-case requirement to filter out non-oath waw+noun constructions
   (got me from ~40 false-positive interior clusters down to ~7 incidental
   cases).
3. Added fa-prefix continuation to recover Q 51:1-4, Q 77:1-5, Q 79:1-5,
   Q 37:1-3, Q 100:1-3, Q 52:1-6 as multi-verse clusters.
4. Added DEM step-through to catch Q 95:3 (`wa-hādhā l-balad`) and Q 90:1
   (`bi-hādhā l-balad`).
5. Per-verse within-verse item scan to catch packed oaths (Q 86:1, Q 91:1).

## Main results

- 20 opening oath clusters in 20 Meccan surahs, with length distribution
  (item count) peaking at 2-3.
- Q 91 is the longest (8 items over 7 verses) and the ONLY heterogeneous
  (4-category) opening of length ≥ 3. Every other length-3+ opening is
  monothematic or spans just 2 categories.
- Q 52 is the second-longest (6 items over 6 verses), a terrestrial +
  instrumental blend.
- Ibn al-Qayyim's classical 42-oath count broadly matches; my strict
  opening-cluster count is narrower because I exclude singleton oaths and
  qsm-oaths with parenthetical breaks (Q 90) and verb-coordinate
  continuations (Q 100:4-5, Q 69:38-39).

## Honest negative results

- Saj' rhyme uniformity within clusters is not significantly higher than
  length-matched random runs in the same surah (p = 0.130 over 1 000
  permutations). The "tight rhyme" classical scholars attribute to oath
  clusters is largely a short-run artifact.
- No robust category-chiasm in any opening cluster. Q 100 looks chiastic
  (warrior/other/warrior) but the "other" is coarse-tagging noise; finer
  semantic tagging would classify all three as warrior-kinetic, making it
  monothematic rather than chiastic.
- Size-order (cosmic → personal) descent is not strictly monotonic in
  Q 91. It holds at coarse grain (first 6 items: cosmic oscillation;
  last item: soul) but oscillates celestial ↔ temporal at fine grain.

## Connection to prior findings

- [palindromes.md](../findings/phase-b-hypotheses/palindromes.md)
  reports three length-7 letter palindromes, all "oath clusters". My
  strict definition shows only Q 91:1-7 is a qasam cluster; Q 81:2-8 is
  an *idhā*-cluster (structurally oath-like but grammatically not
  waw-qasam) and Q 37:127-133 is a *salām*-on-prophet coda. So the
  palindrome-oath connection is tight for Q 91 and looser for the others.
- [saj-rhyme-analysis.md](../findings/phase-b-hypotheses/saj-rhyme-analysis.md)
  highlights Q 91 as the 15/15 perfect-uniform surah. The oath cluster is
  verses 1-7, the first half of the 15-verse mono-rhyme.
- [chronological-revelation.md](../findings/phase-b-hypotheses/chronological-revelation.md):
  all 20 opening oath clusters are in Nöldeke Phase 1 (Early Meccan).

## Classical prior art consulted

- al-Farrāʾ, *Maʿānī l-Qurʾān* (via Kinberg lexicon).
- Ibn al-Qayyim, *al-Tibyān fī Aqsām al-Qurʾān* (English study by
  Hamid Lakhnawi).
- Neuwirth, *The Qur'an and Late Antiquity*.
- Sinai, *The Qur'an: A Historical-Critical Introduction*.
- Farāhī, *Imʿān fī Aqsām al-Qurʾān*; Islāhī, *Tadabbur-i Qurʾān*.
- Mir's summary "The Qur'an Oaths: Farahi's Interpretation"
  (islamic-awareness.org).

## Artifacts

- `/Users/grey/Downloads/quran/analysis/notebooks/oath_clusters.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/oath-clusters.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/oath-clusters.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/oath-clusters.csv`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/oath-clusters-stats.json`

## Follow-up questions worth registering

1. Pre-register: does the **monothematic-opening** pattern survive a formal
   test against a Meccan-register control? i.e. randomly generated length-
   matched waw-GEN chains over the Meccan-surah vocabulary should give the
   null for "1 category out of 11 possible". The claim is that Q 51/77/79/95
   are concentrated in ways far beyond chance.
2. Test: is Q 91's 8-item oath really *the* summa of Quranic oaths? Compute
   a similarity score between Q 91's sworn-by multiset and the union of all
   other opening-cluster multisets. If Q 91 is maximally inclusive, its
   Jaccard overlap with the union should be maximal.
3. The *idhā*-cluster family (Q 81:1-13, Q 82:1-5, Q 84:1-5, Q 99:1-3) was
   explicitly excluded. Worth a sister study: *idhā*-clusters as the
   apocalyptic analog of qasam-clusters.
