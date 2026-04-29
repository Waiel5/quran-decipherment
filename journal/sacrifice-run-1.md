# Sacrifice & Vow Theology — Run 1 Journal

**Date:** 2026-04-12
**Agent:** Phase B — sacrifice-vow
**Target:** findings/phase-b-hypotheses/sacrifice-vow.md

## Methodology

Per-word inventory built from the Quranic Arabic Corpus morphology file
(`data/morphology/quranic-corpus-morphology-0.4.txt`). Root codes in Buckwalter
transliteration. Queried the following roots and lemmas:

| Concept | Root (Buckwalter) | Query result |
|---|---|---|
| slaughter (dhabḥ) | `*bH` | 9 occurrences (all verified as slaughter sense) |
| draw-near / qurbān | `qrb` (LEM:qurobaAn) | 3 occurrences of the noun qurbān |
| vow (nadhr) | `n*r` filtered by LEM:na*aro / n~a*or / nu*or | 7 occurrences (separated from the much larger warner/nadhīr family) |
| Hajj-sacrifice (hady) | `hdy` filtered by LEM:hadoy | 7 occurrences |
| rite (mansak/nusuk) | `nsk` | 7 occurrences |
| slaughter (naḥr) | `nHr` | 1 occurrence — hapax verb at 108:2 |
| hamstring she-camel (ʿaqara) | `Eqr` (the act against the naqa) | 3 occurrences (7:77, 54:29, 91:14) |
| ransom (fadā) | `fdy` — cross-root at 37:107 | fadaynāhu verified |

## Key observations during the run

1. The root for "slaughter" in dhabḥ (`*bH`) is confirmed at 37:107 (`*iboHK` —
   indefinite genitive, "a slaughtering"). Its 9 occurrences cluster into
   three distinct fields:
   - Pharaonic tyranny (yudhabbiḥu form II, intensive): 2:49, 14:6, 28:4
   - Legal/ritual: 2:67, 2:71 (Moses' cow); 5:3 (mā dhubiḥa ʿalā al-nuṣub —
     the prohibition of altar-slaughter to other-than-God)
   - Prophetic narrative: 27:21 (Solomon threatens to slaughter the hoopoe),
     37:102 (Abraham's dream), 37:107 (ransom noun)

2. The vow-nadhr (n*r sense "vow") is STRICTLY separated in the morphology
   from the nadhīr sense ("warner") which dominates the root with 316
   attestations. Only 7 tokens belong to the vow-sense. These 7 cluster
   around three narrative moments: charity-vows (2:270), Mary's mother's
   vow (3:35), Mary's vow of silence (19:26), and the abrār fulfilling
   a vow (76:7). Also 22:29 has nudhūrahum ("vows" — pilgrims) which shows
   hajj-context vows.

3. The noun qurbān appears exactly 3 times. All three are in contexts of
   REJECTION or FAILURE: Cain/Abel (5:27 — rejected from one), Israelite
   demand for a fire-eaten offering (3:183 — polemically invoked), and
   the pagans' "gods taken as qurbān" (46:28 — false mediators who
   abandon their devotees). Qurbān as a Quranic noun NEVER describes an
   accepted/normative Muslim rite.

4. The verb naḥara (108:2 "wa-nḥar") is a total hapax as a verb (only
   one occurrence in the entire Quran). The noun nuḥūr ("throats") from
   the same root is absent in the morphology (there's a separate root
   for it elsewhere, but the slaughter-verb is unique). This is
   extraordinary: the paired ritual `ṣallī + anḥar` is built on a verb
   that occurs exactly once.

5. The "dhibḥ ʿaẓīm" (37:107) is ALSO a hapax form of the root — the only
   noun *dhibḥ* in the Quran. Everywhere else we have verb forms. This
   mirrors the structural uniqueness of naḥara at 108:2. Both pivotal
   sacrifice-words are hapax.

6. Ṣāliḥ's she-camel is never called a qurbān, hady, dhibḥ, or nusuk.
   The word used for killing it is ʿaqara (to hamstring). This is
   lexically marked as anti-sacrifice: the verb is agrarian-violent, not
   cultic. The she-camel is God's sign (āya), not an offering. Its
   killers are not failed worshippers but rebels violating a sign.
   Contrast: Cain's qurbān at least names the cultic act even though
   it fails.

7. Mary at 19:26 vows a "fast to the Merciful" (ṣawman) consisting
   explicitly of speech-abstention ("fa-lan ukallima"). The nadhr here
   is a negative act — withholding speech — which is extraordinary
   against the universal ancient-Near-Eastern pattern of vow-as-offering
   (of objects or animals). Her mother's vow in 3:35 is also a human
   dedication (the child in her womb, muḥarraran — "liberated for
   service"), not an animal. Both Maryam-nadhr instances are DEDICATIONS
   OF PERSONS, not animal immolations.

8. The pairing ṣalāt + (nusuk/naḥr) appears twice in nearly-parallel
   form: 6:162 "ṣalātī wa-nusukī wa-maḥyāya wa-mamātī li-llāhi" and
   108:2 "fa-ṣalli li-rabbika wa-nḥar". In both cases sacrifice is
   positioned NEXT TO prayer and framed as totalizing ("my life and
   my death") or as a command to the Prophet himself. This suggests
   sacrifice-as-worship is the operative frame, not sacrifice-as-
   atonement or sacrifice-as-food-gift.

9. 22:37 contains the theological summary: "Their flesh and their
   blood will never reach Allah, but the taqwā from you reaches Him."
   This explicitly dematerializes hady: the material gift is not the
   point; the inner state is. This verse is the hermeneutic key to all
   the other sacrifice passages.

## Risks / caveats

- The morphology marks ROOT but not always semantic field; I had to
  manually filter n*r-vow from n*r-warner.
- The word ʿaqīqa is not Quranic (as briefed) — omitted from the
  inventory.
- "Ukhtibi" (covenant-slaughter) is not found in the morphology under
  any standard root transcription; likely a post-Quranic coinage or a
  transcription issue — treated as classical legal vocabulary, not
  Quranic.

## Time budget

- Inventory: 25% — mechanical grep queries
- Reading narrative passages from morphology: 45%
- Synthesis and writing: 30%
