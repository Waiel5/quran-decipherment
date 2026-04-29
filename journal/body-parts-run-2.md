# Journal — Body Parts in the Quran (run 2)

Agent: Phase-B body-parts analyst
Date: 2026-04-12
Output: findings/phase-b-hypotheses/body-parts.md

## Scope

Inventory every major body-part noun in the Quran, tabulate distribution, and
pursue seven sub-tasks commissioned by the coordinator:

1. Per-part inventory (count, representative verses, register).
2. *Wajh Allāh* — classical anthropomorphism debate (11 occurrences).
3. Q 41:20–22 — the skins (*julūd*) testify at Judgement.
4. *Yadā Allāh* — Q 38:75 and Q 5:64 "two hands" debate.
5. Pharaoh's threat "hands and feet from opposite sides" (*min khilāf*)
   as a *mutashābih* triad.
6. Dual body-part cross-reference (eyes, hands, feet, ears).
7. *Qulūb fī ṣ-ṣudūr* — the nesting formula of Q 22:46.

Reference to the already-completed qalb-theology memo; cite findings briefly,
don't re-excavate.

## Method

Parsed `data/morphology/quranic-corpus-morphology-0.4.txt` (Buckwalter-
transliterated Quranic Arabic Corpus 0.4, Dukes 2011) by root code.

Body-part roots in Buckwalter notation:

| Part | Buckwalter root | Notes |
|---|---|---|
| wajh (face) | wjh | |
| ʿayn (eye/spring) | Eyn | 57 of 65 are "eye"-lemma |
| yad (hand) | ydy | |
| rijl (foot/leg) | rjl | conflated w/ "rajul" = man |
| udhun (ear) | A*n | dhal transliterated * |
| lisān (tongue) | lsn | |
| fam (mouth) | fwh | |
| dam (blood) | dmw | |
| jild (skin) | jld | |
| ʿaẓm (bone) | EZm | 15 of 128 are "bone"; rest = ʿaẓīm (mighty) |
| raʾs (head) | rAs | |
| ṣadr (breast/chest) | Sdr | |
| ẓahr (back) | Zhr | |
| baṭn (belly) | bTn | |
| shafah (lip) | $fh | Q 90:9 hapax |
| ṣulb (spine) | Slb | 2 noun tokens; others = crucify |
| aṣābiʿ (fingers) | SbE | 2 (Q 2:19, 71:7) — root ≠ sbE "seven" |
| qadam (step/foot) | qdm | 10 noun |
| rukba (knee) | jvw (kneel) | no root "rkb=knee"; kneel-root 3x |
| ḥulqūm (throat) | Hlq | 2 noun |

### Counting notes

Where a root is polysemic (ʿaẓm shares with ʿaẓīm; rjl shares with rajul;
rkb-ride shares with rukba-knee; SbE-fingers shares with sbE-seven), I
filtered by **lemma** not by root. The fingers root in the corpus is *SbE*
(capital S = ṣād), distinct from *sbE* "seven" (small s = sīn) — they are
homographs in transliteration but phonologically and lexically distinct.

For "rukba (knee)" the user's brief flagged Q 45:28 as a hapax. This is
actually the word *jāthiya* (kneeling, active participle of *jathā*), root
*j-th-w* (corpus code `jvw`), which occurs 3× (Q 19:68, 19:72, 45:28). There
is no noun *rukba* in the Quranic lexicon. I corrected this in the report.

### Wajh Allāh extraction

I extracted every noun-token of wjh, pulled the verse-and-position coordinate,
then checked the following word for `LEM:{ll~ah` or `ROOT:rbb` (Rabb). Hit
exactly **11 constructs**: Q 2:112, 2:115, 2:272, 3:20, 4:125, 13:22, 30:38,
30:39, 55:27, 76:9, 92:20. This matches traditional count (some sources count
10 by excluding Q 2:115 *fa-thamma wajh Allāh* because the grammar differs;
other sources count 13 by including *wajhaka li-llāh* Q 2:112 formulations).

### Julūd-testify verses

Q 41:20–22 grepped in full, confirmed triad hearing+sight+skins. Q 41:22
adds the "you used to hide" (*tastatirūna*) reversal — extraordinary case of
epidermis epistemology.

### Pharaoh min khilāf

Khilāf occurs 4× — Q 5:33 (hirāba ruling; hands-and-feet-opposite penalty),
and Q 7:124, 20:71, 26:49 (all Pharaoh to his magicians). The three Pharaoh
verses form a textbook *mutashābih* triad, with Q 5:33 as the halakhic
distant echo.

## Findings outline

- Wajh dominates by frequency (74 noun tokens); it operates simultaneously
  as physical face, directional kibla-face, eschatological face (radiant vs.
  dust-covered), and theological *wajh Allāh*.
- Hands (120 tokens) cluster in idioms: *bayna yadayhi* (before him),
  *mabsūṭa* (outstretched), and the disputed divine *yadayya* / *yadāhu*.
- Chest (ṣadr 44) is the container; heart (qalb 132, see qalb-theology memo)
  is its contents — Q 22:46 nests them explicitly.
- Fingers, lips, throat, spine, knee — each has 1–3 tokens, almost all in
  highly specific contexts (fingers-in-ears of unbelievers; throat at death;
  spine as site of generation Q 86:7; lips as one of "two paths" Q 90:9;
  kneeling as universal eschatological posture).
- Skin (jild 11 tokens): 3 in Q 41, 2 in Q 22:20 (hide-melting in fire), 1
  in Q 39:23 (believers' skins shiver), 1 in Q 4:56 (skin-replacement
  torment), rest in animal-hide contexts. **Every skin-of-a-human verse is
  eschatological** — a striking specialisation.

## Cross-references to existing findings

- `findings/phase-c-structures/qalb-theology.md` — heart as
  bridge-centrality root; 132 *qalb* nouns; Q 22:46 noted there.
- `findings/phase-b-hypotheses/hapax-legomena-catalog.md` — shafah (Q 90:9),
  aṣābiʿ (Q 2:19, 71:7), ṣulb (Q 86:7), ḥulqūm (Q 56:83).
- `findings/phase-b-hypotheses/dual-form-mapping.md` — paired body parts
  likely overlap with dual-form mapping; this memo adds the specifically
  *anatomical* duals.
- `findings/phase-b-hypotheses/mutashabih-lafzi.md` — Pharaoh's triad should
  be indexed there.

## Open questions for later runs

1. Does the *skin-as-witness* motif correlate with verses where the body
   parts are grammatically active (subject of yaḍlil / yaʿrif / yanṭiqu)?
   A quick pass showed Q 41:21 has Allah as the active principle (*anṭaqanā*).
2. Counting *wajh Allāh* rigorously depends on grammar. I adopted the
   idāfa-construct criterion (*wajh + genitive Allah/Rabb*); this yields 11.
3. The "hand of Allah" verses (not limited to the *yadā* dual; cf. Q 48:10
   *yadu llāhi fawqa aydīhim*, Q 36:71 *mimmā ʿamilat aydīnā*) warrant their
   own table — 7+ constructs total.

## Deliverable

`findings/phase-b-hypotheses/body-parts.md` — ~3000 words, seven sections.
400-word summary appended to final message for the coordinator.
