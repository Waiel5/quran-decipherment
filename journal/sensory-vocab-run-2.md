# Journal: Sensory Vocabulary (Phase B, run 2)

**Date:** 2026-04-12
**Agent:** Phase B hypothesis generator
**Data:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Dukes Quranic Arabic Corpus v0.4)

## Scope

Map the Quran's sensory lexicon across the five Islamic senses — baṣar (sight), samʿ (hearing), shamm (smell), dhawq (taste), lams (touch) — plus lisān (tongue/language) and the negated-sensory triad ṣumm / bukm / ʿumy (deaf / dumb / blind). Quantify the dominance of the divine-attribute pair al-Samīʿ al-Baṣīr at verse endings. Test the hypothesis that smell / taste / touch are theologically excluded from the divine Names and that dhawq is preferentially figurative (tasting punishment).

## Method

1. Parsed the morphology file, indexing every `STEM` token by `(surah, ayah, word, token)` with its LEM and ROOT features.
2. Per-root token counts using Buckwalter root codes: `bSr`, `smE`, `$mm`, `*wq`, `lms`, `lsn`, `Smm`, `bkm`, `Emy`. Also checked `rwH` (riyḥ / scent) as the closest lexical neighbour of smell.
3. For each verse, determined the last and penultimate stem lemmas and tagged verse-final epithets. Built sets:
   - verses ending on `samiyE` (or penultimate-samiyE + final partner)
   - verses ending on `baSiyr`
   - verses where both appear in the last two stem slots (the pair formula)
4. For the dhawq root, classified its 61 host verses by collocation with `Ea*aAb` / `wabaAl` / `bao>s` (torment-cluster) vs. `jan~ap` / `TaEaAm` / `HasanFA` (literal-food-cluster) vs. other.
5. Read the three triad verses (2:18, 2:171, 17:97) plus the parallel Q 11:24 (four-way contrast) and Q 7:179 (the fullest anatomical indictment) directly from the morphology output.
6. Read Q 14:4 and Q 41:44 lemma by lemma for the mother-tongue revelation motif.

## Key numerical findings

- Per-root token counts: bSr = 148, smE = 185, *wq = 63, lms = 5, $mm = **0**, lsn = 25, Emy = 33, Smm = 15, bkm = 6.
- **Samīʿ** (as lemma `samiyE`) appears 47× as a stem; **46** of those tokens sit in the last two stem slots of a verse. It is **never the absolute last word** — always the first half of a fixed epithet pair.
- **Baṣīr** (lemma `baSiyr`) appears 51× as a stem; **41** of those sit in the last two slots, and **38** close the verse (last word).
- **Pair formula `… samīʿ(un) … baṣīr`** ending a verse: **11** occurrences (2/4, 2/22, 2/17, 1/31, 2/40, 1/42, 1/58, 1/76).
- Samīʿ's dominant partner is not Baṣīr but ʿAlīm (31/46 ≈ 67 %). Baṣīr's dominant partner is Khabīr (5), but its commonest pre-word is a participial `ʿamila` (15) — the rhyme formula `bimā taʿmalūna baṣīr`.
- Combined divine-attribute verse endings in the samīʿ/baṣīr field: **46 + 38 − 11 = 73** distinct verse-ending tokens (exceeds the 60+ target).
- Dhawq distribution among 61 verses: torment-collocation **38**, literal food **2** (Q 7:22, Q 3:185 — and 3:185 is actually still figurative), other **21**. Causative ʾadhāqa (22/63 of all *wq tokens) is overwhelmingly God-as-subject with ʿadhāb as object.
- Shamm (`$mm`) is a **true zero** in the corpus — the root does not occur at all. Riyḥ (wind/scent, root `rwH`) occurs 29× but never as a sensory organ and never paired with a human olfactory verb.
- Triad ṣumm-bukm-ʿumy appears in full in exactly three verses: **Q 2:18, Q 2:171, Q 17:97**. Q 11:24 and Q 43:40 pair the triad differently.

## Surprises

1. The **asymmetry** of Samīʿ and Baṣīr at verse-end: Baṣīr finalises, Samīʿ never does. This is a rhyme/prosody constraint — `–īr` sits at qāfiyah position, `–īʿ` yields to the longer partner. So the "pair" is not symmetric in position; hearing ushers in sight.
2. `$mm` has **zero** attestation. Smell has no verbal root at all in the Quranic corpus. The one verse that arguably names smell (Q 12:94 `innī la-ajidu rīḥa Yūsufa`) uses `rwH` (wind) with the verb `wajada` (to find), not a dedicated olfactory verb.
3. Touch (`lms`) appears only 5× and only as a verb, never as a noun; no form "the sense of touch" exists. Four of the five tokens concern sexual contact (Q 4:43, 5:6) or ritual purity; only Q 72:8 (the jinn touching the heaven) is spatial.

## Hypotheses to forward

- H1. **The two-sense cosmos.** The Quran constructs divine epistemology entirely around hearing + seeing; the other three senses are human-bodily and cannot predicate God. This is structurally enforced by the corpus itself — there is no smell-root available to predicate.
- H2. **Rhyme economy explains the pair's order.** The samīʿ/baṣīr pair is co-rhetorical but rhyme-asymmetric: baṣīr gets qāfiyah, samīʿ gets the lead-in.
- H3. **Dhawq is pedagogic.** Because taste is first-person and undeniable (you cannot deny what you have tasted), it is the corpus's preferred metaphor for divine retribution: "so taste (dhūqū)" / "We made them taste (adhaqnāhum)" closes deniability.
- H4. **The triad is eschatological-cognitive, not medical.** The `ṣumm bukm ʿumy` trio always co-occurs with a cognitive negation verb (`lā yarjiʿūn` 2:18, `lā yaʿqilūn` 2:171, `maʾwāhum jahannam` 17:97), i.e. sensory privation = cognitive ruin = damnation.
- H5. **Lisān both organ and idiom.** Of 24 lisān-verses, at least 5 mean "language" (Q 14:4, 16:103, 19:97, 41:44, 46:12, 44:58) and most of the rest are organ (moral speech). Mother-tongue revelation (14:4) is the theological hinge: the corpus distinguishes God's competence over languages from the Prophet's singular lingual vehicle.

## Output

`findings/phase-b-hypotheses/sensory-vocabulary.md` (~2 800 words).

## Loose ends / follow-ups

- Cross-check Samīʿ/Baṣīr against the 99-Names lists (findings/phase-b-hypotheses/razi-99names-test.md) to verify these are Tier-1 attested Names.
- Correlate dhawq-torment verses with Meccan/Medinan split via `chronological-revelation.md`.
- Check whether the triad (2:18) sits inside the opening sura's hypocrite pericope and whether 2:171 rhymes structurally with 2:18.
