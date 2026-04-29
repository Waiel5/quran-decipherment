---
run: iblis-run-1
phase: B
date: 2026-04-12
agent: Phase-B hypothesis agent — Iblis/Satan theology
target: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/iblis-satan.md
---

# Iblīs / al-Shayṭān — Run Journal

## Approach

1. Read prior finding `findings/phase-b-hypotheses/quotation-analysis.md` §6 for
   the pre-existing four-retelling comparison (already identified as a
   *mutashābih-lafẓī* cluster).
2. Built a Python joiner over `quran-text/quran-no-tashkeel.json` +
   `data/translations/en.sahih.txt` (linear line-for-verse mapping, which the
   previous runs also use) to extract raw Arabic + English side-by-side for
   every target verse.
3. Extracted the 11 named Iblīs verses by raw Arabic-surface match on the string
   "إبليس". Confirmed count against the Leeds QAC morphology (LEM:<iboliys is a
   proper noun with no ROOT attribute — itself a diagnostic datum).
4. Counted *al-shayṭān* singular tokens by a whitelist of surface-form variants
   (الشيطان / شيطان / شيطانا / لشيطان / فالشيطان / والشيطان / بالشيطان /
   كالشيطان) → **69 tokens in 62 verses**. Plural (*shayāṭīn*) by the
   equivalent whitelist → **16 tokens in 15 verses**.
5. Ran collocation scan for *al-shayṭān* × *ʿaduww* within a verse: **11 verses**.
6. Ran root-scan for W-S-W-S (*waswasa*, *yuwaswisu*, *al-waswās*): **5 verses**.
7. Ran surface-scan for *al-ghurūr* (الغرور) as the deceiver-title: **5 verses**,
   of which Q 31:33, 35:5, 57:14 unambiguously personify (the others are
   adjectival, "*matāʿu l-ghurūr*").
8. Extracted full Arabic+English for the four retelling pericopes (7:11-18,
   15:28-44, 17:61-65, 38:71-85) and the two Adam-centred parallel pericopes
   (2:30-38, 20:115-123), plus Q 14:22, Q 35:6, Q 114:1-6, Q 37:6-10, Q 7:19-22.
9. Cross-referenced `findings/phase-b-hypotheses/mutashabih-lafzi.md` and
   `mutashabih-pairs.csv` (fifty-plus pair-alignments between the four
   retellings — a saturated cluster).
10. Synthesised the classical Iblīs-jinn/angel debate from memory of al-Ṭabarī,
    al-Zamakhsharī, al-Rāzī, Ibn Taymiyya, Ibn Kathīr. The *munqaṭiʿ* vs.
    *muttaṣil* grammatical split is the mechanism. Cited positions, not
    sub-arguments, because the finding file is analytic, not doxographical.

## Key statistics (verified against text)

- **Iblīs** (proper noun): 11 occurrences across 11 verses; 2 of the 11 are
  divine vocatives (Q 15:32, Q 38:75). No human Quranic speaker addresses him
  by name.
- **al-shayṭān** singular: 69 tokens across 62 verses.
- ***shayāṭīn*** plural: 16 tokens across 15 verses.
- **al-shayṭān + ʿaduww** co-occurrence: 11 verses (9 use the exact phrase
  *ʿaduww mubīn*).
- **Waswasa root (W-S-W-S)**: 5 verses (Q 7:20, Q 20:120, Q 50:16, Q 114:4-5).
- **al-ghurūr** (personified deceiver): 3 verses (Q 31:33, 35:5, 57:14).
- **Four retelling-pericopes**: Q 7:11-18 (8 verses), Q 15:28-44 (17 verses),
  Q 17:61-65 (5 verses), Q 38:71-85 (15 verses). Total: 45 verses.

## Core findings

- **Lexical split Iblīs / shayṭān is systematic.** Iblīs is the *named*
  refuser; al-shayṭān is the *functional* tempter. The two lexemes are not
  synonyms, and no human Quranic speaker addresses him by his proper name.
- **The four retellings of the prostration scene cluster into two pairs.** Q 7
  + Q 38 share the verbatim pride-argument; Q 15 + Q 38 share the
  sentence-formula *fa-khruj minhā fa-innaka rajīm* and the
  *mukhlaṣīn*-exception. Q 17 is the most compressed (5 verses). Q 38 is the
  most emotive (oath by God's *ʿizzat*). Q 15 is the most cosmological (ends
  with the seven gates of Hell).
- **Four dialogic modes of Iblīs's speech**: (a) self-justification to God,
  (b) petition to God, (c) threat-programme to God, (d) whisper-speech to
  humans, plus (e) post-mortem disavowal (Q 14:22, Q 59:16). The grammatical
  lexicons of modes (c) and (d) are mutually exclusive.
- **Q 14:22 is the anti-dualist confession.** *mā kāna lī ʿalaykum min sulṭān
  illā an daʿawtukum* — Satan admits he had no *authority*, only invitation.
  Evil is always consent.
- **Q 35:6 is the operative imperative.** *fa-ttakhidhūhu ʿaduwwan* — the rare
  Quranic command to actively hold an enemy-stance.
- **Jinn/angel crux.** Q 2:34's *illā Iblīs* following "the angels" reads most
  naturally as *muttaṣil* (Iblīs is of the angels); Q 18:50's *kāna min al-jinn*
  reads most naturally as ontological. The classical tradition split evenly;
  consensus from the 5th Hijri century forward went to the *munqaṭiʿ* reading.
- ***Shayāṭīn* is a functional category**, not a lineage. It includes jinn
  (Q 37:7), human adversaries of prophets (Q 6:112), Solomon's labour-force
  (Q 21:82), and the teachers of magic (Q 2:102).

## Scripts used

- /tmp/iblis_scan.py — Arabic-surface extraction of إبليس with EN match
- /tmp/shayTaan_count.py — token-count + plural-count + ʿaduww-cooccur
- /tmp/waswasa_scan.py — W-S-W-S root verses

## Open work

- A full phonosemantic scan of soft-speech vocabulary (*waswasa*, *hamas*,
  *najwa*, *sirr*) as a possible covert-speech register — flagged for a
  later agent.
- Statistical test of whether the 11-69-16 cascade of Iblīs / sing. shayṭān /
  plur. shayāṭīn maps to a gematric or structural invariant — preliminary
  judgement: no, the distribution tracks narrative frequency, not numerical
  design.
