---
title: jinas-wordplay run 1
agent: phase-b-jinas
date: 2026-04-12
runtime: ~2s
inputs:
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - quran-text/quran-no-tashkeel.json
  - data/translations/en.sahih.txt
outputs:
  - findings/phase-b-hypotheses/jinas-wordplay.md
  - findings/phase-b-hypotheses/jinas-all-instances.csv
  - analysis/scripts/jinas_detect.py
---

# jinas-wordplay run 1 — log

## Goal

Comprehensive computational catalog of jinas / tajnis (paronomasia) in the Quran.
The classical Arabic rhetorical figure of placing same-root or near-root words
together for sonic and semantic effect. Tafsir literature has noted individual
cases for centuries, but no exhaustive computational catalog has been built. This
run produces one, using the Leeds Quranic Arabic Corpus root tags.

## Method

1. Parsed `quranic-corpus-morphology-0.4.txt` (128 219 segment rows). Read
   `ROOT:<bw>` for every segment. Built `{(s, v): [root_bw, ...]}`.
2. For every verse, computed `Counter(roots)`; flagged any root appearing ≥ 2
   times as a "morphological repetition" (the necessary substrate of jinas).
3. Drilled down to: triple+ within-verse, multi-root within-verse clusters,
   cross-verse rare-root couplings, edit-distance-1 root pairs, per-surah density,
   and verification of ten classically-cited jinas verses.
4. Curated 11 "most beautiful" highlights and surfaced 323 "novelty" candidates
   (any triple+ rep where the root is not in the canonical balagha-textbook set).

## Counts (sanity)

- 49 968 root-bearing segment tokens (out of 128 219 total segments — affixes,
  determiners, particles don't carry roots, hence the gap).
- 6 214 of 6 236 verses have at least one root tag (the 22 missing are short
  verses composed entirely of particles / muqatta`at).
- 1 642 distinct roots — matches typical Quranic-Arabic-Corpus published totals.
- 2 531 verses (40.6 % of the Quran) contain at least one repeated root.
- 698 (verse, root) records with count ≥ 3.
- 1 068 verses with two or more *distinct* repeated roots.
- 144 cross-verse rare-root (≤ 20 global) couplings in adjacent same-surah verses.
- 2 286 within-verse near-root (edit-distance 1, triliteral) pairs.

## Headline findings

### Single most jinas-dense verse

- **Q 2:282** — the verse of debt — *raw* champion at 52 stem tokens participating
  in some root repetition across 16 distinct repeated roots. But this is partly an
  artifact: it is by far the longest verse in the Quran (~129 stems). The root
  *kataba* (write) recurs 9×, *shahida* (witness) 7×, *Allah* 6×.
- **Q 13:28** — the *length-normalised* champion at **8/9 = 0.889**:
  > الذين آمنوا وتطمئن قلوبهم بذكر الله ۗ ألا بذكر الله تطمئن القلوب
  >
  > "Those who believed and whose hearts find rest in the remembrance of Allah;
  > verily, in the remembrance of Allah do hearts find rest."
  >
  > Four roots — *Tmn* (rest), *qlb* (heart), *dkr* (remembrance), *Alh* (Allah)
  > — each appear *exactly twice* in a near-perfect chiastic mirror:
  > {Tmn qlb dkr Alh | dkr Alh Tmn qlb}. A ring composition compressed into a
  > single ayah; the verse's root pattern *is* its meaning.
- **Q 24:61** — the most extreme *single-root* repetition: `byt` (house) **10
  times** in one verse (the kinship table). Holds the record for max root count
  in any verse.

### Highest jinas-density surah

- **Surah 109 — Al-Kafirun** at density 0.833 (10 of 12 stem tokens repeat).
  This is *expected*: the entire surah is structurally a six-verse polemic built
  around the repetition of *Ebd* ("worship") and *dyn* ("religion"). The
  structural parallelism is the surah's identity.
- Of the **top 15 most jinas-dense surahs, 13 are Medinan**. The two Meccan
  exceptions are 109 (Al-Kafirun, the polemic-by-repetition surah) and 73
  (Al-Muzzammil, late Meccan, where verse 20 is itself an unusually long
  late-Meccan ayah).
  This is a substantive observation: **root-repetition jinas is strongly
  Medinan-coded**. Meccan surahs (especially the late short rhymed ones) favour
  rhyme and assonance over root rep; Medinan surahs are dominated by long
  legal-moral discourses where contracts, witnesses, inheritance, kinship, and
  disbelief get *named* over and over by their root-words.

### Surprises (novel findings)

- **Q 6:76 → 77 → 78** — the only *three-verse* rare-root chain in the catalog.
  The root `Afl` ("to set, to disappear", global count 4) recurs across three
  consecutive verses as Abraham reasons from star to moon to sun. Each celestial
  body sets; the same rare verb closes each step of the syllogism. Listed in tafsir
  but not usually framed as cross-verse jinas.
- **Q 28:71 → 72** with root `srmd` (perpetual). Both occurrences of this root
  in the entire Quran fall in directly adjacent verses, in the perfectly mirrored
  "if Allah made the night perpetual" / "if Allah made the day perpetual"
  parallel. Pure structural cross-verse jinas on a hapax-pair.
- **Q 13:28** as the length-normalised champion — I had not seen this verse
  flagged in the standard balagha lists I scanned during the run, even though it
  is one of the most-quoted ayahs in Sufi spirituality. The chiastic root
  arrangement is a quantitative discovery.
- **Q 24:26** — `xbv` (evil) and `Tyb` (good) **each appear 4 times in one
  verse**: "Evil words are for evil men, and evil men are subjected to evil
  words. And good words are for good men, and good men are an object of good
  words." Two-axis quadruple jinas.
- **Q 23:14** — the embryology verse — `xlq` (create) 5 times.
- **Q 47:15** — the four rivers of Paradise — `nhr` (river) 4 times.
- **Q 35:39** — the *kfr* sextuple. k-f-r six times in two clauses; the verse
  is form-enacting-content (disbelief that "multiplies upon its bearer" is
  itself multiplied across the verse's words).
- **Q 4:46** — the "we hear and disobey / hear and not hear" verse — `smE` (hear)
  5 times across competing speech-acts.

### Famous-verse verification

We verified 11 classically-cited jinas examples. The morphology corpus confirms
the root-level repetition for: 30:55 (`swE`), 2:9 & 4:142 (`xdE`), 2:194 (`EdW`),
9:79 (`sxr`), 3:54 (`mkr`), 9:67 (`nsy`), 42:40 (`swA`). Two famous cases — 16:127
(*la tahzan* / *la taku fi dayqin*) and 17:14 (*iqra' kitabaka*) — fail the
root-level test, because their jinas operates at the lexical/sonic level, not
the root-identity level. We documented this distinction in §8.

## Caveats

- Repetition ≠ jinas. Many high-density verses are list-prosody or syntactic
  parallelism, not paronomasia. The catalog reports the substrate; rhetorical
  labelling is a secondary judgement requiring context.
- The 2 286 edit-distance-1 near-root pairs are noisy: many are accidental
  (e.g. *qwl* ↔ *qbl*) and not heard as jinas. A future run could rank them by
  *phonetic* distance.
- We did not run a permutation null model. The cross-verse coupling section is
  descriptive — under random shuffling, *some* roots will appear in adjacent
  verses by chance. The §5 finding is striking on its own merits but not yet
  statistically tested.
- WebSearch tool was not used in this run (deferred). All "famous" verse claims
  drawn from agent's prior knowledge of classical balagha (Al-Suyuti's *al-Itqan*,
  Az-Zarkashi's *al-Burhan*, modern tafsir lists).

## What's in the deliverables

- `findings/phase-b-hypotheses/jinas-wordplay.md` — 1278 lines, 10 sections (§2–§10
  + §2b length-normalised + §7a Meccan/Medinan + headline numbers + 11 highlights
  + honest caveats).
- `findings/phase-b-hypotheses/jinas-all-instances.csv` — 4 637 (surah, verse,
  root_bw, root_ar, count, verse_text) rows. The full repetition catalog for
  any reader who wants to re-rank or re-filter.
- `analysis/scripts/jinas_detect.py` — the script. Re-runnable, deterministic.

## Open follow-ups for next run

1. Permutation null model on the cross-verse coupling counts (shuffle verse
   order within surah, recompute, see how often we hit ≥ 144 rare-root adjacencies
   by chance).
2. Phonetic distance ranking on near-root pairs (replace orthographic edit
   distance with a manner-of-articulation feature distance).
3. Cross-link this catalog with the Phase C ring-composition findings — Q 13:28
   is itself a micro-ring; many of the §3 verses likely sit at structural
   pivots of larger ring compositions in their surah.
4. WebSearch verification of "novel" candidates against classical balagha
   manuals — some §9 finds may already be cited; we just don't know without
   external lookup.
