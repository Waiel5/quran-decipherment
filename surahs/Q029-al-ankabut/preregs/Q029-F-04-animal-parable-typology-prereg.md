---
surah: 29
test_id: Q029-F-04
title: Q 29:41 spider-web parable typological uniqueness — corpus comparison to other animal-vehicle parables
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (single test under structural-uniqueness verification; deterministic textual classification)
hypothesis_anchor: al-Rāzī (*Mafātīḥ al-ghayb* on Q 29:41) — the spider parable distinguishes itself from other Quranic *amthāl* by the *frailty-disguised-as-shelter* logic; al-Bāqillānī *iʿjāz al-tashbīh*; al-Zarkashī (*al-Burhān*) on the typology of Quranic *mathal*.
direction_of_effect: Q 29:41 is the UNIQUE corpus-instance of the *mathal X ka-mathal animal-vehicle SHELTER-with-the-frailty-property* parable schema (LOCKED). Other animal-vehicle parables (bee Q 16:68, ant Q 27:18, fly Q 22:73) use animals as VEHICLES but with different rhetorical schemas.
origin: SESSION-HANDOFF-2026-05-09-PM specialist brief — Q 29 deep-dive T3.
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (whitespace-split, default)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: textual classification of the parable schema; deterministic + classical-source-supported
---

# Q029-F-04 — Pre-registration: Q 29:41 spider-web parable typological uniqueness

## 1. Background

T2 (Q029-F-03) confirmed *Eankabuwt* (spider) is a corpus-singleton lemma at Q 29:41. T3 extends the question from LEXICAL singleton to RHETORICAL SCHEMA singleton: is the Q 29:41 spider-web parable the unique corpus-instance of its parable type (vehicle = animal-built shelter; tenor = idol-worship; common property = fragility-of-apparent-protection), OR is the schema instantiated elsewhere with a different animal?

The 4 animal-vehicle parables in the Quran:
- **Q 16:68** (bee, *naḥl*): COMMAND vehicle — Allah reveals to the bee to take houses from mountains and trees. NOT a *mathal* — it is an instructive narrative.
- **Q 22:73** (fly, *dhubāb*): IMPOTENCE-of-IDOLS vehicle — *Duriba mathalun fa-stamiʿū lahu, inna alladhīna tadʿūna min dūni llāhi lan yakhluqū dhubāban wa-law ijtamaʿū lahu* — the idols cannot create a fly even if united. Vehicle = fly's basic existence; tenor = idol's impotence.
- **Q 27:18** (ant, *namlah*): NARRATIVE-DIALOGUE — an ant warns its fellows about Solomon's army. NOT a *mathal* — it is a narrative anecdote.
- **Q 29:41** (spider, *ʿankabūt*): SHELTER-FRAGILITY vehicle — *mathalu al-ladhīna ittakhadhū min dūni llāhi awliyāʾa ka-mathali al-ʿankabūti ittakhadhat baytan; wa-inna awhana al-buyūti la-baytu al-ʿankabūt* — the idol-worshippers are like the spider that builds a house — the frailest of houses. Vehicle = spider's web (a shelter); tenor = idol-worshippers' protectors; common property = fragility-of-apparent-shelter.

## 2. Hypothesis (LOCKED)

**H1 (T3)**: Q 29:41 is the UNIQUE corpus-instance of the *mathal X ka-mathal animal-vehicle [SHELTER-with-property-of-frailty]* schema. No other Quranic verse instantiates this exact schema (vehicle = animal-built shelter; tenor = idol-worship / false-protection; common property = frailty-of-apparent-shelter).

**Pre-committed claim**: Q 29:41 is corpus-unique in:
1. Its parable-formula opener (*mathalu al-ladhīna ... ka-mathali al-ʿankabūt*).
2. Its animal-built-shelter vehicle.
3. Its frailty-of-shelter common property (*awhana al-buyūt*).

**H0**: ≥ 1 other Quranic verse instantiates the same schema with a different animal.

## 3. Decision rule (deterministic + classical-source-supported)

Verdict criteria (joint AND):

| Sub-claim | Evidence | Verdict component |
|:--|:--|:--|
| (a) *ʿankabūt* lemma is corpus-singleton | Q029-F-03 (already PASSED) | Verified — lemma corpus-singleton |
| (b) `awohan` (frailty-superlative) is corpus-singleton | scan QAC for LEM:>awohan | Verified or NULL |
| (c) The 3-part schema {*mathalu* opener + animal-vehicle + frailty-property} is corpus-unique | textual scan of all Quran verses for the combined schema | Verified or NULL |

**Composite verdict:**
- All 3 PASS → **PASS-DIRECTED — corpus-unique parable schema**.
- 2 of 3 PASS → **DIRECTIONAL — partially-unique schema**.
- 0-1 PASS → **NULL**.

## 4. Comparator anchor (locked at T2)

The 4 animal-vehicle Quranic parables (all 4 are corpus-singletons in their respective animal lemmas, per Q029-F-03 comparator data):
- Q 16:68 (bee): vehicle = bee; tenor = divine-revelation-network. NOT a *mathal*.
- Q 22:73 (fly): vehicle = fly; tenor = idol-impotence. IS a *mathal* (opens with *Duriba mathalun*).
- Q 27:18 (ant): vehicle = ant; tenor = recognition-of-prophet. NOT a *mathal*.
- Q 29:41 (spider): vehicle = spider's web; tenor = idol-worshipper-protection. IS a *mathal*.

Only Q 22:73 and Q 29:41 are formally *amthāl*. Of these two:
- Q 22:73: vehicle = fly's basic existence; common property = inability-to-create-or-recover. NOT shelter-related.
- Q 29:41: vehicle = spider's web (shelter); common property = frailty-of-shelter. SHELTER-related.

This pre-reg's central empirical claim: only Q 29:41 has the shelter-frailty schema. The classical iʿjāz al-tashbīh tradition (al-Bāqillānī, al-Rāzī) is the source of this typology.

## 5. Operational definition

1. **Scan QAC for `LEM:>awohan`**: deterministic count of attestations.
2. **Scan QAC for `LEM:Eankabuwt`**: confirmed corpus-singleton at Q029-F-03.
3. **Textual scan for the 3-part schema** across all 6,236 verses, using regex on `quran-text/quran-no-tashkeel.json`:
   - Schema = (a) opens with `مثل` or contains `مثل` + (b) has an animal-name token + (c) has `بيوت` or `بيت` + (d) has a fragility/weakness root (`وهن`, `ضعف`).
   - Only Q 29:41 is expected to satisfy ALL FOUR.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, QAC v0.4 LEM, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)`.

## 7. SHA256 lock

Computed at run-time. Embedded in `scripts/Q029_F_04_animal_parable_typology.py` as `EXPECTED_SHA`. Verified before computation.

## 8. Honest a-priori limits

- The 4-part schema is a stipulated classification; alternative classifications (e.g., dropping the *mathal* formula requirement) yield different verdicts. The pre-reg locks ONE classification scheme.
- The frailty-vehicle common property is captured by the root *whn* (weakness) and *Def* (frailty); other near-synonyms (*hayy* = alive but weak, etc.) are not in the search. The pre-reg is a focused operationalization, not exhaustive.
- The verdict at sub-claim (c) is sensitive to the regex; the regex is locked in the script.

## 9. Pre-commit attestation

Direction is LOCKED before observation. If sub-claim (c) returns ≥ 2 matching verses, the pre-committed claim is FALSIFIED and the test is published as NULL with prominence.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
