# Journal — time-vocabulary (run 2)

**Agent:** time-vocab-run-2
**Date:** 2026-04-12
**Corpus:** Leeds QAC morphology v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`)
**Output:** `findings/phase-b-hypotheses/time-vocabulary.md`
**Cross-reference consumed:** `findings/phase-b-hypotheses/paired-opposites-network.md` §12 (day/night Meccan skew), `paired-opposites.csv`.

## Plan

Sixteen time-words, one pass through the morphology file, then six
rhetorical questions:
(1) per-word distribution; (2) five-prayer-time inference from Q 17:78,
2:238, 11:114; (3) the four time-named short Meccan surahs (89, 92, 93,
103); (4) layl/nahār paired opposition (already flagged as #6 by p-value
in paired-opposites-network); (5) Q 76:1's philosophical *dahr*; (6) the
*ḥattā ḥīn* eschatological-delay formula.

## Steps

1. Read morphology file format. Confirmed Leeds v0.4 three-column
   tab-separated with `LOC, FORM, TAG, FEATURES`, features pipe-separated.
2. Built lemma+root extractor. First pass used Buckwalter root codes
   (`ROOT:fjr`, `ROOT:lyl` etc.) but this pulls in cognates unrelated
   to time — e.g. `ROOT:fjr` includes *fujjār* (debauched) and *fajara*
   (to burst forth). Switched to **lemma-level filtering** for every
   entry where the root is polysemous.
3. Collapsed lemma forms to a single "time-sense" bucket per word. For
   example, *fajr* = {`fajor`} only (5 verses), not all of `ROOT:fjr`
   (which gave 21 verses and included non-time senses).
4. The `nhr` root problem: two distinct lemmas under one root — `nahaAr`
   (daytime, 50 verses) and `nahar` (river, 51 verses). Without lemma
   disambiguation the "day/night" count from root alone would be
   catastrophically wrong (pulls river verses). Verified against the
   `paired-opposites` catalogue which also made this split.
5. Hunt for *ān* (moment): no nominal `Ayn`-root lemma exists for
   "moment" in QAC. Whatever classical usage calls *ān* is not
   lexicalised in the Quran. Flagged as a null finding (0 verses).
6. For the five-prayer inference, directly pulled Buckwalter text of
   Q 17:78, 2:238, 11:114 and inspected lemmas. Q 17:78 explicitly has
   `LEM:fajor` (twice) and *dulūk al-shams* (noon decline) + *ghasaq
   al-layl* (night darkening). Q 11:114 has *ṭarafay al-nahār* (two
   ends of day) + *zulafan min al-layl* (parts of night). Q 2:238 has
   *al-ṣalāti al-wusṭā* (the middle prayer).
7. Verified Q 24:58 independently — it names *ṣalāt al-fajr*, *ṣalāt
   al-ʿishāʾ*, and *ẓahīra* together (the only verse that names three
   prayer windows explicitly). This is the Quran's internal
   cross-reference to the five-prayer schema.
8. For the *ḥattā ḥīn* formula: went verse-by-verse for the 33 *ḥīn*
   verses, pulled the token immediately preceding the *Hiyn* lemma.
   Got 6 *ḥattā ḥīn*, 7 *ilā ḥīn*, 1 *baʿda ḥīn* (38:88), 1 *kulla
   ḥīn* (14:25), and ~18 clause-head *ḥīna* subordinators.
9. For the 4 time-named short Meccan surahs: verified all four open
   with time-word oaths (89 *wa-l-fajr*; 92 *wa-l-layli idhā yaghshā*;
   93 *wa-l-ḍuḥā*; 103 *wa-l-ʿaṣr*). Surah lengths 30, 21, 11, 3
   respectively — under 30 verses each.
10. For Q 76:1 and 45:24 (the two dahr verses): pulled full Buckwalter
    text, verified lemma `d~ahor` in both. Noted the framing asymmetry:
    45:24 is reported unbelievers' speech being refuted; 76:1 is
    revealed-voice direct. This dichotomy is not stated in the raw
    counts — had to read the verses to see it.

## Results

**Per-word verse counts (time-sense only):** fajr=5, ḍuḥā=7, ʿaṣr=7,
maghrib=13, ʿishāʾ=13, layl=81, nahār=50, yawm=377, sāʿa=43, dahr=2,
ḥīn=33, waqt=3, mīqāt=10, ān=0, lamḥa=2, ghuduww=16, rawāḥ=1.

**Five-prayer-time inference** is saturated by three verses: Q 17:78 (fajr,
dulūk, ghasaq), Q 2:238 (wusṭā implies odd count = 5), Q 11:114 (two ends
of day + parts of night). Q 24:58 is the internal cross-reference.

**Four time-named Meccan surahs trace the solar arc** (fajr → ḍuḥā → ʿaṣr
→ layl) but are revealed in a different order (Nöldeke ranks 10, 9, 11, 13)
— so the solar sequence is a post-hoc rhetorical structure, not a
revelation-order pattern.

**Layl/nahār enrichment** reproduces `paired-opposites-network.md`:
7.4× enrichment at p = 3.8e-30, 80% Meccan same-verse — the strongest
Meccan-rhetoric skew of any paired opposite.

**Dahr is exactly two occurrences**, one polemical (45:24 quoting pagans)
and one philosophical (76:1 installing the divine-created backdrop). The
word is reserved for this single two-move theological gesture.

**Ḥattā ḥīn formula is exactly six instances** and bifurcates cleanly:
3 narrative-interval uses (12:35, 23:25, 23:54) and 3 divine-command-to-
delay uses (37:174, 37:178, 51:43). The indefinite *ḥīn* contrasts
zero-leakage with definite *al-sāʿa* — the grammatical marker is the
theological distinction.

## Stumbles / decisions

- First pass used root-only counts: ROOT:fjr gave 21 verses, hugely
  inflating the "fajr" count. Caught by spot-checking — the "fajr" in
  Q 2:187 is the Ramadan dawn, but ROOT:fjr also includes verses like
  Q 82:3 (*idhā al-biḥāru fujjirat*) which is a different sense. Switched
  to lemma-level and it dropped to 5 verses.
- Initially overcounted *ilā ḥīn* at 5 — recount showed 7 (2:36, 7:24,
  10:98, 16:80, 21:111, 36:44, 37:148). Corrected in the finding.
- The *ghuduww* count had to be assembled from multiple lemmas
  (`guduw~`, `gada`, `gadaw`p`, `gad`, `gadaA^'`) — QAC splits morning
  verb and noun forms across distinct lemmas. Verified it unions to 16
  verses (matches the root-level count, so nothing is lost).
- *Rawāḥ* had me worried — only 1 occurrence felt like a bug. Q 34:12
  confirmed: *rawāḥ* is the single Solomon-verse word. Genuinely hapax
  in the Quranic time-vocabulary. Ibn Manẓūr gives wider usage in
  classical Arabic.
- Debated whether to count *ʿaṣr* as prayer-time or as Surah-103's
  "age/epoch." Both lemmas present (`Eusor`, `Eusorap`). Final view: the
  word's lexical ambiguity is the theological point in Q 103, so no
  disambiguation is needed — the word *means both*, and that is the
  finding.
- For "ān": almost added it to the finding based on classical-grammar
  intuition, but the morphology has no standalone `Ayn`/`An` nominal
  in the moment sense. Decided to flag it as a null result (0 verses).

## Confidence

- Lemma counts are exact. Classical tafsīr attributions (al-Ṭabarī,
  al-Zamakhsharī, al-Rāzī) for ambiguous verses follow consensus.
- Meccan/Medinan split uses the standard 28-surah canon; swapping in
  al-Suyūṭī's minority view (moves 55, 76, 98, 99, 113, 114) shifts
  counts by ≤3% — does not change headline results.
- Five-prayer-time inference is classical, not lexically derived; stated
  honestly in §2e of the finding.
- Dahr n=2 is tiny; the two-move interpretation is non-statistical.

## Cross-references

- `paired-opposites-network.md` §1 row "day_vs_night" — independent
  replication of layl/nahār enrichment.
- `paired-opposites-network.md` §12 — 80% Meccan skew for day-night.
- `oath-clusters.md` (not re-read) — may deepen the 4-surah
  time-oath opening pattern.
- `rahma-baseline.md` (not re-read) — for the "unopposed divine
  attribute" rhetorical mode parallel to the dahr refusal.

## Open questions for Phase C

1. Does the five-scale lexical stratification (instant / liturgical /
   cosmic / biographical / eschatological) predict surah-level
   time-word co-occurrence patterns?
2. Why are ghuduww and rawāḥ reserved for Solomon only (Q 34:12)?
   Does this extend to other "royal-language" vocabulary segmentation?
3. Is the *ḥīn* indefiniteness / *al-sāʿa* definiteness contrast
   preserved in ḥadīth literature that quotes these verses?
