# Hapax catalog — run 1

Date: 2026-04-12
Agent: Phase B hapax-catalog

## Task
Comprehensive catalog of Quranic hapax legomena. Verify the 395-root figure
from `root-cartography.md`, extend to lemma level, test placement hypotheses,
identify hapax-pairs, cross-reference classical gharīb tradition.

## Data sources
- `data/morphology/quranic-corpus-morphology-0.4.txt` (128,219 segments)
- `data/morphology/root-stats.csv`
- Prior findings: phonaesthetics.md, root-cartography.md, jinas-wordplay.md,
  intra-quranic-cross-references.md, parables-catalog.md

## Methodology
1. Parsed morphology file into (surah, verse, word, segment, form, tag, root,
   lemma) tuples.
2. Counted root tokens → identified count==1 set.
3. Counted lemma tokens → identified count==1 set.
4. For each hapax, computed whether word_position == max(word_position) in
   its verse (verse-final flag).
5. Computed 2×2 χ² for verse-final vs non-final against baseline of all
   root-bearing tokens.
6. Cross-referenced placement with oath-cluster surahs, short surahs
   (93-114), and canonical ring-centers from prior phase work.
7. Identified roots/lemmas with count==2 where both tokens are in the same
   verse or within 3 verses of each other in the same surah → hapax-pairs.

## Findings highlights
- **395 root-hapaxes** (verified)
- **1,994 lemma-hapaxes**
- **28 root hapax-pairs** including srmd (28:71-72), bzg (6:77-78),
  sEd (11:105-108), zmr (39:71-73), wsq (84:17-18), A$r (54:25-26),
  gdr (18:47-49)
- **104 lemma hapax-pairs**
- **Verse-final placement p = 7.35e-29, OR = 3.19** — the headline signal
- Short-surah tail 2.11× over-representation
- Oath-cluster surahs 1.34× (p=0.011)
- 6 of 9 canonical ring-center points host a hapax within ±1 verse

## Surprises
- *fSm* at 2:256 is a hapax (in *lā infiṣāma lahā*) — paired with the
  Ayat-al-Kursi ring. This extends the ring-center hapax signal.
- *wsn* (drowsiness) and *Awd* (burden) both hapax inside Ayat al-Kursi
  (2:255). Two hapaxes in the same verse at the canonical ring center.
- The Light Verse (24:35) contains **six** lemma-hapaxes plus the
  same-verse *zjj* pair (*zujājah* ... *al-zujājah*). No other single
  verse has this density.
- *al-Ṣamad* and *kufuw* are both verse-final in Ikhlāṣ — the surah's
  two rare words are rhyme-break placed.
- Reduplicated hapaxes cluster: *damdama* (91:14), *kabkaba* (26:94),
  *ṣākhkhah* (80:33), *ṭāmmah* (79:34) — the doubling pattern itself
  is a hapax-forming device.

## Statistical methodology notes
- χ² computed with standard 2×2 Pearson formula, df=1, p via erfc
  approximation (matches scipy.stats.chi2.sf within 4 sig figs at
  chi2=124).
- Baseline for verse-final is all root-bearing tokens (49,572). Clitic
  prefixes are correctly excluded because they share word_position with
  their stem segment.
- Binomial z-test for oath-cluster uses normal approximation to binomial;
  n=395, p=0.125 is well inside the regime where this is valid.
- Ring-center test is descriptive (only 9 reference points); not suitable
  for a formal p-value. A proper test would bootstrap against random
  9-verse selections.

## Files produced
- `findings/phase-b-hypotheses/hapax-legomena-catalog.md`
- `findings/phase-b-hypotheses/hapaxes-full-list.csv` (2,446 rows incl.
  root-hapax, lemma-hapax, root-pair types)

## Loose ends / follow-ups
- Formal ring-center hapax bootstrap (dedicated test against N=1000
  random 9-verse selections from the corpus).
- Cross-check against Ibn ʿAbbās's transmitted answers to Nāfiʿ al-Azraq
  (200 q&a list) — would need a digitized version of that list to compute
  intersection rate precisely (manually sampled ~87/200 intersection).
- Classify lemma-hapaxes by derivational form (maṣdar, participial,
  ism-makān, etc.) to see which derivational classes are hapax-producing.
- Joint test: are hapaxes at verse-final position specifically in saj'
  rhymed passages or also in Medinan prose? Quick check suggests both,
  but Medinan has lower hapax density overall.

## Confidence
High on counts (directly from the corpus), high on the verse-final
statistical signal (p=7e-29 is hard to explain away), moderate on
classical cross-reference (manual sample not full intersection),
descriptive-only on ring-center signal.
