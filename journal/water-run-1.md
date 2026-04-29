---
run: water-run-1
phase: B
date: 2026-04-12
output: findings/phase-b-hypotheses/water-vocabulary.md
---

# Journal — water vocabulary run 1

## Prompt
Phase-B task: map water vocabulary in the Quran across a seed list of
~14 roots (baḥr, nahr, māʾ, ghayth, maṭar, rīḥ, ʿayn, biʾr, kawthar,
yamm, jānib, sāḥil, bariyya, plus theological loci 21:30, 25:53, 35:12,
55:19–20, 47:15, 26:63, 20:77, 108, rain-as-revival, and the four
purifying modes).

## Method

1. Read the companion paired-opposites file to inherit conventions
   (N = 6236, Fisher-exact protocol, root-index format).
2. Loaded the Leeds QAC root-index JSON. Found a mismatch between the
   seed-list transliterations and the Buckwalter keys used in the index:
   - *baḥr* = bHr (42 positions)
   - *nahr* = nhr (113 positions; three distinct lemmas within one root:
     nahr river, nahār daytime, tanhar to repel)
   - *māʾ* = mwh (63 — confirms seed)
   - *ghayth* = gyv (4; one is *yughāthu*, Q 12:49)
   - *maṭar* = mTr (15)
   - *rīḥ/rūḥ* = rwH (57; rīḥ 29, rūḥ 21, rawḥ 3, rayḥān 2, verbal 2)
   - *ʿayn* = Eyn (65; 57 ʿayn, 4 maʿīn, 4 ʿīn)
   - *biʾr* = bAr (1 — hapax)
   - *kawṯar* = kvr root, kawṯar the single occurrence; root total 167
   - *yamm* = ymm (11; yamm 8, tayammam 3 — discovered polysemy)
   - *jānib* = jnb (33; ijtanaba 9, jānib 9, janb 8, junub 4, other 3)
   - *sāḥil* = sHl (1 — hapax)
   - *bariyya* — the root br' is for "creatures" (from the task note);
     but the task brief says *bariyya* = "shallow" which actually reads
     closer to *barr* "dry land" (brr). I catalogued *brr* (22 barr,
     8 birr, 2 tabarrū), not br', since "shallow/dry land" is the
     relevant Phase-B opposition. Flagged this as a possible seed-list
     transliteration ambiguity.
3. Added four non-seed but highly-relevant lexemes after pattern-hunting:
   mawj (wave), mlḥ (salt, Ajj briny), frt (sweet), ḥmm (scalding),
   gsq (dark hell-liquid), snm (*tasnīm* paradise fountain, hapax),
   fjr (gush), sqy (give-drink), mzj (blend), syl (flood), qṭr (drop).
4. Pulled every cited verse into the working bundle via the Arabic JSON
   + Sahīh English translation, cross-checked against morphology for
   lemmatic resolution of the key words.
5. Checked the paradise-rivers formula *tajrī min taḥtihā al-anhār*:
   35 × taḥtihā + 4 × taḥtihim = 39 occurrences. This contextualises
   the Q 47:15 four-river enumeration.
6. Wrote the ~3000-word findings file with 11 sections.

## Surprises / findings that survived

- **yamm / tayammum share a root**: the Egyptian sea (Moses) and the
  dry-substitute ablution. The Quran's purity law lexically encodes the
  sea's absence as the name of its earthen replacement. Not new to
  classical grammarians (al-Rāghib notes both under y-m-m) but this is
  the first time I see the connection drawn with counts.
- **yamm vs baḥr split in the Moses cycle**: yamm is the drowning-word
  (4 attestations of Pharaoh's troops); baḥr is the parting-word (Moses'
  staff strikes *baḥr* at 26:63 and 20:77, but Pharaoh drowns in *yamm*
  at 20:78 etc.). Looks like an agency-register split — worth formalising
  as a phase-C test.
- **nhr root polysemy** — river / daytime / repel. Q 93:10 *fa-lā tanhar*
  (do not repel the beggar) and Q 17:23 *wa-lā tanharhumā* (do not repel
  your parents) share a root with *nahar* (river). If the phonosemantic
  claim is that nhr = "flow / push aside", then "repelling" is "damming
  the flow". Unverified lexicographic claim — flagged as a hypothesis.
- **jnb → janāba → jānib → ijtanib** family: the ritually impure state
  shares a root with "side" (the bank of a valley) and with "avoid".
  Lexical family resolves to: set aside, side-stepped, ritually sidelined.
  Water restores the centre.
- **ghayth vs maṭar valence**: ghayth is always positive (4/4),
  maṭar is usually punitive (14/15). Dedicated rain-words for mercy vs
  judgment. Paralleling Q 42:28's *ghayth* ↔ *raḥma* co-location.
- **kawṯar / abtar muqābala inside Q 108**: superlative abundance vs
  superlative cut-off. The surah is itself a three-verse balāgha exercise.
- **naḥr / nahr phonic near-pun** in Q 108:2 — same consonants except
  ḥ/h. Given §2's abundance-river framing, "and sacrifice" (wa-nḥar)
  almost overlays a river-gesture on the ritual act.

## Things I did NOT do (for later runs)

- No Fisher-exact p-values computed for the water pairs. The main
  paired-opposites file already handles baḥr/barr. The other water
  pairs (ʿaḏb/milḥ, ghayth/maṭar, māʾ/ḥamīm) are low-N and would need
  exact tests with continuity correction — a phase-C follow-up.
- No abjad for *al-kawṯar* yet; flagged in §10 of the output file.
- No phonetic-profile read on water vocabulary; scratch/ already has
  phonaesthetics output. Could cross-reference later.

## Files touched

- Read: data/morphology/root-index.json,
  data/morphology/quranic-corpus-morphology-0.4.txt,
  quran-text/quran-no-tashkeel.json,
  data/translations/en.sahih.txt,
  findings/phase-b-hypotheses/paired-opposites-network.md
- Wrote: findings/phase-b-hypotheses/water-vocabulary.md (this run's output)
- Wrote: journal/water-run-1.md (this file)

## Confidence notes

- Counts: confidence high (QAC is well-validated, random spot-checks
  passed).
- Semantic claims about yamm/baḥr register split: medium — 11 total
  attestations of yamm, so n is small; reads like a pattern but could
  be narrative accident.
- Root-polysemy claims (nhr tri-senses, ymm bi-sense, jnb tetra-sense):
  high — these are lexicographic facts, and the count split is clear
  in the lemma breakdown.
- Kawṯar / abtar structural claim: high (well-attested in classical
  tafsīr).
- Ghayth-as-revival-theology: high — five parallel verses (Q 16:65,
  22:5, 30:50, 43:11, 50:9) all instantiate the schema.
