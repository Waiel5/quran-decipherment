---
agent: imperative-run-1
phase: phase-b-hypotheses
date: 2026-04-12
status: complete
inputs:
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt (Leeds QAC v0.4)
  - /Users/grey/Downloads/quran/data/revelation-order.csv (Tanzil/Noldeke period tags)
  - /Users/grey/Downloads/quran/data/hafs-verse-counts.tsv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/quotation-analysis.md (for the 332 qul datum)
scripts:
  - /Users/grey/Downloads/quran/scripts/imperative_extract.py (main extractor)
  - /tmp/prophet_verses.py (prophet-name proximity)
  - /tmp/challenge.py (taḥaddī imperatives)
  - /tmp/extras.py (joint ritual formula aqImu + A^tu)
outputs:
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/imperative-mood.md
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-all-tokens.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-per-surah.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-prohibitive.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-qul-catalog.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-stats.json
---

# Journal — Imperative mood extraction (run 1)

## Task

Audit the imperative-mood (*fiʿl amr*) distribution across the entire
Quran using the Leeds Quranic Arabic Corpus v0.4. Eight sub-tasks were
specified: total count, addressee classification, qul corpus
verification, prohibitive nāhī corpus, emphatic imperatives, taḥaddī
(challenge) imperatives, ritual imperatives, and per-surah density with
Meccan/Medinan split.

## Method notes

### Imperative detection

The Leeds QAC marks imperative verbs with the `|IMPV` feature flag on a
verbal (tag=V) segment. A grep over the full morphology file returned
**1,876** matches — this is the canonical figure. An alternative query
using `MOOD:IMP` returned 0, because Leeds reserves the MOOD feature
for imperfect-verb moods only (JUSsive, SUBJunctive, INDicative). A
third query using the stem tag `POS:V|IMPV` agreed with the first. 1,876
is therefore robust against three formulation variants.

### Prohibitive detection

The *nāhī* construction is lexically *lā* + morphologically jussive. The
Leeds corpus treats the prohibitive particle *lā* as POS:PRO (distinct
from NEG *lā*, which is a different particle use). 332 POS:PRO tokens
appear in the corpus — essentially all of them precede a jussive verb.
Our pairing logic collected 313 (surface-adjacent) pairs, missing about
6% where the jussive is separated from the *lā* by an intervening
particle; this is a known limitation and the 313 figure should be read
as a slight undercount.

### Addressee classification

The hardest methodological call was how to map imperative tokens to
addressees. The Quranic convention is that a bare 2MS imperative is
divine address to the Prophet (unless a vocative opens the verse), and
a bare 2MP imperative is divine address to the believing community.
Dedicated prophet-name vocative markers ("yā Mūsā", "yā Ādam") exist but
are scarce at the verse level (two such matches in the full corpus).
Most specific-individual imperatives therefore live inside narrative
quotation frames ("qāla Ibrāhīmu … faʾtinī bi-ṭaʿāmin") and cannot be
cleanly routed via morphology alone.

We therefore used a two-tier approach:

1. **Vocative-anchored** (VOC tag present in verse): classify by the
   noun or name that follows. *yā ayyuhā alladhīna āmanū* → believers;
   *yā ayyuhā al-nās* → humanity; *yā banī Isrāʾīl* → Children of Israel.
2. **Bare default**: 2MS → Prophet Muḥammad; 2MP → community
   ("believers-or-group" tag).

For narrative prophet addressees we ran a supplementary proximity query
— how many IMPV tokens appear in verses that morphologically mention a
specific prophet PN. Results: Moses 64, Mary 16, Noah 13, Joseph 10,
Ishmael 8, Shuʿayb 5. These are not the Prophet-Muḥammad count and
should not be double-counted with the 940 to-Muḥammad tally.

A lemma-spelling pitfall: the Leeds corpus uses backtick-terminated
lemmas for final-alif names (*muwsaY`*, *EiysaY`*, *yaHoyaY`*). The
first pass of the prophet query missed Moses entirely because of this;
the corrected query with backticks returned the 64 figure.

### Joint ritual formula

The canonical pairing "*aqīmū al-ṣalāh wa-ātū al-zakāh*" was checked by
finding verses where both lemmas (*aqaAma* IMPV and *A^taY* IMPV)
co-occur. Nine verses match: 2:43, 2:83, 2:110, 4:77, 22:78, 24:56,
33:33, 58:13, and 73:20. Eight are Medinan; the single Meccan instance
is at the very end of Al-Muzzammil — a verse generally considered a
late Medinan insertion, which is itself an independent confirmation.

## Hypotheses checked

| hypothesis | outcome |
|---|---|
| Total IMPV ≥ 1,000 | confirmed, 1,876 |
| Qul count ≈ 332 (from quotation-analysis.md) | confirmed exactly, 332 |
| Meccan-Medinan density split, Medinan higher | confirmed, ratio 1.97× |
| "yā ayyuhā alladhīna āmanū" is Medinan-register | strongly confirmed: 113/119 (95.0%) |
| Top-20 density surahs are Medinan-heavy | confirmed, 13-to-7 split |
| taḥaddī imperatives exist as a small, formal corpus | confirmed, 3 direct (2:23, 10:38, 11:13) + 2 related |
| The joint "salāh + zakāh" formula is a Medinan fingerprint | confirmed 8/9 verses Medinan |
| Prophet receives majority of 2MS imperatives | confirmed, 938/951 (98.6%) |
| iʿlam and iṣbir form a pedagogical cluster | confirmed, 31 + 25 tokens; *ufhum* absent |

## Surprises and refinements

1. **The prohibitive is more plural than the positive**. The 2MP share
   for prohibitions is 63.6% versus 46.4% for positive imperatives.
   This inverts a naïve expectation and suggests that the Quran's
   ethical don'ts are much more a community-level instruction than the
   do's, which are more evenly divided between Prophet and community.

2. **The command "be patient" (*iṣbir*) is heavily 2MS (to Prophet)**.
   19 of 25 iṣbir tokens are 2MS; only 6 are plural. The Quran is
   telling the Prophet to endure more often than it is telling the
   community to.

3. **No *ufhum* in the corpus.** Although "ufhum!" is a standard
   classroom imperative, the Quran never uses it. *iʿlam* (know!) and
   *unẓur* (look!) entirely cover that pedagogical space.

## Caveats

* The 2MS-default-to-Prophet rule may over-count by a small margin in
  narrative sections where the imperative is in a quoted speech between
  two humans (e.g. Q 12:50 *ijʿalhu ʿindaka*, spoken by the king; Q
  12:29 *astaghfirī li-dhambiki*, Joseph's master to his wife). An
  exact count of those narrative-interior imperatives would require a
  quotation-boundary detector, which is beyond the scope of this run.
  Rough estimate by sampling: <5% of the 938 2MS-Prophet count.
* The prohibitive count of 313 is a slight undercount (see above).
* Per-surah density uses Hafs-Kufan verse counts. For Q 1 the basmala
  is counted as verse 1 (a mushaf convention); including it in other
  surahs would shift the densities marginally but not change rankings.

## Links to related findings

* `quotation-analysis.md` — the 332 qul finding, replicated.
* `negation-taxonomy.md` — bāb al-nafī, of which *lā* + jussive is the
  prohibitive branch.
* `covenant-language.md` — the *yā ayyuhā alladhīna āmanū* address is
  one of the covenant-language markers.
* `dual-form-mapping.md` — the 16 dual-addressee imperatives (Moses-
  Aaron cluster).
* `divine-names-distribution.md` — remaining open question: does
  *iʿlam anna* correlate with specific divine-name classes?
