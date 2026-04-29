# Journal: Plants of the Qur'an — Run 2

**Agent:** Phase B hypothesis-generator
**Date:** 2026-04-12
**Deliverable:** `findings/phase-b-hypotheses/plants-quran.md`
**Primary data:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Dukes v0.4)
**Secondary data:** `quran-text/quran-min-tashkeel.json` (Tanzil Uthmani)

## Procedure

1. Enumerated the target plant lexicon from the brief:
   - Named plants: nakhl (palm), zaytūn (olive), tīn (fig), ʿinab (grape), rummān (pomegranate), ṭalḥ, sidr, mann, salwā, qiththāʾ, baṣal, fūm, ʿadas, burr (tested — absent), khamṭ, zaqqūm, ʿuṣf, abb.
   - Collective: shajar (tree).
2. For each lexeme, constructed a Buckwalter root query and ran a full-corpus grep against the Dukes morphology file. Captured (location, form, lemma, features) for every `STEM` token.
3. Filtered homographs — critical for `mnn` (plant "manna" vs. verb "to bestow"), `ESf` (plant "chaff" vs. "storming wind"), `brr` (claimed "burr = wheat" vs. "birr = piety"). Conclusion: `burr` (wheat) has no lexical presence in the corpus. Wrote this into the findings as a negative finding.
4. Extracted Uthmani text for every verse containing a plant-token, plus surrounding ayāt for context (paradise/hell scenes, Maryam 19, Sabaʾ 34, ʿAbasa 80, An-Naḥl 16, Wāqiʿa 56, Ṣāffāt 37).
5. Organised findings into six-section structure following the brief's numbered tasks.

## Key data points discovered

- **tīn is hapax.** Only one Qur'anic token of the fig, at 95:1:1. The entire oath-pair "wa-l-tīn wa-l-zaytūn" rests on one appearance of the fig against the olive's seven.
- **Palm-grape dyad frequency.** Nine of eleven grape tokens co-occur with palm, making nakhl-aʿnāb the most consistent agricultural pair.
- **The Q 2:61 "seven."** The morphology shows only five named plants in the verse (baql, qiththāʾ, fūm, ʿadas, baṣal). The "seven" of the brief counts those five plus mann+salwā from 2:57. All five plant-words are hapaxes — they enter the Qur'an only to be renounced.
- **Sidr-zaqqūm structural antipode.** The lote-tree at the cosmic summit (53:14 `sidrat al-muntahā`) has as its inverse the Qur'anic-coined proper noun `zaqqūm` at the root of Jahīm (37:64). Both are feminine-singular `$ajarap`/`sidorap` individuations. The Qur'an's cosmic axis is a tree at each pole.
- **Shajar grammatical toggle.** Masculine collective `$ajar` for ecological backdrop; feminine singular `$ajarap` for named, iconic, morally-weighted trees (Eden, Zaqqūm, Sinai olive, Mūsā's bush, Ridwān tree, the cursed tree). This is a consistent pattern across 26 stem tokens.
- **Three plant registers.** (a) creation-sign lists (6:99, 6:141, 16:11 — same quartet olive/palm/grape/pomegranate thrice); (b) paradise provision (55:68, 56:28–29, 24:35); (c) punishment / inversion (34:16 Sabaʾ's stunted gardens; 37:62 etc. zaqqūm).
- **ʿAbasa 80:24–32 microcosm.** A seven-element food-list running from water → earth-splitting → grain (`Hab`) → grape + `qaDob` (fodder) → olive + palm → gardens → fruit + `>ab~` (fodder) → "enjoyment for you and your livestock." The fact that *abb* is a hapax refused by Abū Bakr matches the structural role: it names what grazing animals eat, without needing a taxonomy.

## Methodological notes

- The Dukes morphology treats `zaq~uwm` as `PN` (proper noun), signalling the corpus editors' judgment that this is a Qur'anic coinage not reducible to a known species. I preserved that tag in the findings.
- Where tradition disagrees (fūm = garlic vs. wheat; ṭalḥ = banana vs. acacia; ʿuṣf = chaff vs. tender leaf), I cited both readings and let the structural context arbitrate rather than ruling.
- I did not extend the search to near-synonyms (`thamar`, `jannah`, `zarʿ`, `ḥabb`, `ḥadāʾiq`, `fākihah`, `rayḥān`) except to note their supporting presence; the brief specified *named plants*, and those words are either generic categories or compound food-terms. They are recorded in §1.16 as "adjacent lexemes."

## Decisions and their justifications

- **Excluded *burr*.** No `brr`-stem token in the corpus means "wheat." The root `brr` is the piety root. I flagged this as a negative finding rather than silently omitting it.
- **Included *salwā*** despite being an animal — the brief pairs it with mann, and the Q 2:61 complaint structurally contrasts 2 heavenly provisions against 5 earthly plants.
- **Included *ʿuṣf*** despite its homograph with "storm wind" — 55:12 and 105:5 are unambiguously the plant-material sense, and the two-token distribution (paradise vs. annihilation) is thematically telling.
- **Treated the "seven" framing of Q 2:61 as 2+5.** Five named plants + two heavenly provisions (mann, salwā named in 2:57, two verses earlier, in the same narrative unit). The rhetorical contrast in the verse is "one food (ṭaʿām wāḥid) → demand for five earthly plants" — the Qur'an itself rhetorically collapses manna+salwā into *one* food. So 1 (heavenly) vs. 5 (earthly) is the verse's own framing; 2 vs. 5 is the unit framing; 7 total is the user's framing. I accepted and explained all three.

## Loose threads / questions for later runs

1. The three creation-sign quartets (6:99, 6:141, 16:11) share olive+palm+grape+pomegranate. A future pass should measure the *order* of enumeration (do the trees appear in the same order?) and any phonetic/prosodic signal.
2. The blessed olive "neither east nor west" (24:35) against the zaqqūm "growing from the root of Jahīm" (37:64) is a spatial inversion worth a dedicated paper.
3. Maryam's *n~axolap* at 19:23/19:25 is the only feminine-singular individuated palm in the Qur'an. Whether other named Qur'anic women are associated with individuated plants is a worthwhile sub-study.
4. The ʿuṣf pairing 55:12 (paradise: "grain with its chaff") and 105:5 (Elephant: "like eaten chaff") — the same botanical lexeme at heaven and at punishment. An interesting parallel to sidr/zaqqūm.
5. The `sakar` (intoxicant) of 16:67 as a pre-prohibition register of wine. Chronology against 5:90 (khamr prohibition) is documented; the semantic shift within the Qur'an's own text would merit a chronology-of-terms study.
6. `athl` (tamarisk, hapax at 34:16) was noted in passing — a full sub-inventory of the *Sabaʾ* degraded trio (khamṭ + athl + sidr qalīl) would make a small paper of its own.

## Word count check

Main findings file: approximately 3,000 words (body prose, excluding appendix). Verified by rough count of paragraph word-density.
