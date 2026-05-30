---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 7 claims audited — 4 VINDICATED (incl. 1 corpus-rarity), 1 DIRECTIONAL (al-Shāfiʿī sufficiency → Q103-F-01), 2 NOT-TESTABLE
---

# Q 103 al-ʿAṣr — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan,
Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json` (id 103); H-NEW values from
`findings/phase-b-hypotheses/csv/`.

## Claim 1 — "Q 103 is Meccan" (al-Qurṭubī, al-Baghawī; Qatāda dissenting)

**Claim:** al-Qurṭubī (*al-Jāmiʿ*, on Q 103:1): *"wa-hiya makkiyya. wa-qāla Qatāda madaniyya, wa-ruwiya ʿan
Ibn ʿAbbās"*; al-Baghawī (*Maʿālim*): *"makkiyya."*

**Test:** Cross-check `data/revelation-order.csv`.

**Result:** Row `"13,103,العصر,Al-Asr,Meccan,21,Early Meccan"` — Q 103 = revelation-order #13 (Tanzil Egyptian
Standard), period **Meccan**, Nöldeke #21 "Early Meccan." No Medinan-classification variant on disk.

**Verdict: VINDICATED.** Q 103 is Meccan in both the Egyptian-standard and Nöldeke chronologies on disk. The
Qatāda/Ibn-ʿAbbās minority "Medinan" view (preserved by al-Qurṭubī) is not reflected in the on-disk chronology
data, which is documented as a tradition, not adjudicated.

## Claim 2 — "It is three verses" (al-Qurṭubī, al-Rāzī)

**Claim:** al-Qurṭubī: *"wa-hiya thalāth āyāt"*; al-Rāzī (*Mafātīḥ*, surah header L263740): *"thalāth āyāt makkiyya."*

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 103); cross-check `data/hafs-verse-counts.tsv`.

**Result:** 3 verses in the JSON; `hafs-verse-counts.tsv` line 103 = 3.

**Verdict: VINDICATED.** 3 verses, Hafs-Kūfan. (No variant verse-count tradition for Q 103 is on disk; the
surah is below the threshold where the counting schools diverge.)

## Claim 3 — "*al-insān* is generic (al-jins), proven by the v 3 exception" (al-Ṭabarī, al-Rāzī, al-Jalālayn)

**Claim:** al-Ṭabarī (on Q 103:3): *"wa-stathnā alladhīna āmanū min al-insān, li-anna al-insān bi-maʿnā
al-jamʿ, lā bi-maʿnā al-wāḥid"* — the believers are excepted *from* al-insān, which therefore must be collective.
al-Rāzī (v 2, masʾala 1) and al-Jalālayn (*"al-insān, the generic"*) concur.

**Test:** Is the v 3 subject grammatically plural (so the exception is from a plural set)? Check QAC morphology
(`data/morphology/quranic-corpus-morphology-0.4.txt`, surah-103): *alladhīna* (REL, plural) + *āmanū / ʿamilū /
tawāṣaw* (all perfect plural verbs).

**Result:** v 3 opens *illā* (EXP) + *alladhīna* (relative plural) + three masculine-plural perfect verbs
(*āmanū, ʿamilū, tawāṣaw*). The excepted set is grammatically plural, which is coherent only if *al-insān* (v 2)
is read collectively. al-Ṭabarī's argument is a sound grammatical inference from the text.

**Verdict: VINDICATED (grammatical).** The plural exception in v 3 entails the generic reading of *al-insān* in
v 2. (This is a grammatical-logical claim verifiable from the morphology, not a numerical one.)

## Claim 4 — al-Shāfiʿī: "if people pondered this surah it would suffice them" — the maximal-content-minimal-form claim (Ibn Kathīr)

**Claim:** Ibn Kathīr (*Tafsīr*, on Q 103; `en-tafisr-ibn-kathir/103/1.json`): *"Ash-Shafiʿi said: 'If the
people were to ponder on this Surah, it would be sufficient for them.'"* Operationally: Q 103 packs a complete
soteriological programme (faith + works + mutual truth + mutual patience) into minimal form.

**Test (PRE-REGISTERED as Q103-F-01, Arms A + C):** Does Q 103 realise a complete rhetorical arc
(oath→jawāb→exception) at minimal scale, with high local self-cohesion, and is it a structurally matched
minimal-surah? See `06-novel-findings.md` for the full pre-reg + run.

**Result:**
- **Arm C CONFIRMED:** full qasam→jawāb→istithnāʾ arc in 3 verses; qasam→jawāb distance = 1 (minimal, H-NEW-2210);
  local_cohesion **rank 10/114** (top decile); rhyme_entropy **0.0** (corpus floor).
- **Arm A CONFIRMED:** Q 103 is the minimal-surah rā'-twin of Q 108 (its rank-1 FR neighbour, 0.2399); only 2 of
  the 3 three-verse surahs are perfect rā'-monorhymes, and {103,108} is that pair.

**Verdict: DIRECTIONAL → CONFIRMED-at-structure.** al-Shāfiʿī's qualitative "sufficiency / maximal-content"
intuition has a direct structural correlate: Q 103 carries a complete oath→verdict→remedy programme at minimal
length with top-decile internal cohesion and the corpus's floor rhyme entropy. The *theological* sufficiency
claim is NOT-TESTABLE empirically; the *structural* "maximal completeness in minimal form" reading is VINDICATED
by Q103-F-01 Arms A + C. (Honest split between the empirical correlate and the theological assertion.)

## Claim 5 — al-Rāzī: Q 103 is a valid *taḥaddī* (inimitability-challenge) test-case (Mafātīḥ on Q 2:23)

**Claim:** al-Rāzī (*Mafātīḥ al-ghayb*, on Q 2:23 *faʾtū bi-sūratin min mithlihi*, L14000): the challenge "a surah
like it" *"yatanāwalu sūrat al-Kawthar wa-sūrat al-ʿAṣr wa-sūrat qul yā ayyuhā al-kāfirūn"* — Q 103 is one of his
three named test-cases for the surah-level challenge.

**Test:** This is a theological/literary inimitability claim — not an empirical-architectural one. The closest
project-internal correlate is the surah's #2 emphatic-density (Q103-F-01 Arm B) and its perfect-monorhyme
phonological seal, but iʿjāz/taḥaddī status itself is out of scope (protocol §10).

**Verdict: NOT-TESTABLE (empirically).** The claim that Q 103 is humanly inimitable is theological-literary, not
falsifiable by the project's instruments. Documented because al-Rāzī's choice of Q 103 as a taḥaddī case directly
motivates the minimal-architecture framing of Q103-F-01 (`06-novel-findings.md`). The Musaylima parody anecdote
(Ibn Kathīr) is the traditional illustration; it is an *iʿjāz*-anecdote, not a testable structural claim.

## Claim 6 — al-Rāzī: the ʿaṣr-oath (loss) is the antithesis-pair of the ḍuḥā-oath (profit) (Mafātīḥ on Q 103:1)

**Claim:** al-Rāzī (*Mafātīḥ*, surah-ʿAṣr, L263779, L263793-263795): *"He swore by* al-ʿaṣr *as He swore by*
al-ḍuḥā *… as He swore by* al-ḍuḥā *in the matter of profit (al-ribḥ) and gave the Messenger glad tidings of
advance, so here in the matter of the loser (al-khāsir) He warns of decline."* The two oaths form a
profit/loss mercantile diptych.

**Test:** Is there an empirical content-relationship between Q 103 (al-ʿAṣr) and Q 93 (al-Ḍuḥā)? Read the FR
distance from `h-new-111.json` and the seam structure; and is the *khusr* (mercantile-loss) vocabulary
distinctive? (The diptych is a thematic-rhetorical pairing; the empirical test is whether the two are
content-adjacent and share the loss/profit lexical axis.)

**Result:** Q 93 (al-Ḍuḥā) and Q 103 (al-ʿAṣr) are both in the short-Meccan mufaṣṣal-qiṣār FR-dense block; the
*khusr* root (x-s-r) is the surah's distinctive lexeme (al-Jalālayn, al-Rāzī, al-Qurṭubī all read it
mercantile: *"in all his bargaining"*). The diptych is a rhetorical-thematic pairing (oath-on-time-as-loss ↔
oath-on-morning-as-profit) rather than a measurable structural adjacency: Q 93 and Q 103 are 10 surahs apart,
not mushaf-adjacent, so the pairing lives at the thematic level, not the seam/FR-rank level.

**Verdict: NOT-TESTABLE (rhetorical) / partially documented.** al-Rāzī's loss/profit oath-diptych is a
balāgha-level reading (the rhetorical antithesis of two oath-surahs); it is not an architectural-adjacency claim
and the project's seam/FR instruments are not the right tool. Documented as a thematic cross-reference
(`02-content-analysis.md` §6, `07-cross-references.md`), not adjudicated empirically.

## Claim 7 — al-Baghawī (← Ibrāhīm al-Nakhaʿī): Q 103's loss/exception mirrors Q 95:4-6

**Claim:** al-Baghawī (*Maʿālim*, on Q 103:3; `ar-tafsir-al-baghawi/103/3.json`): the *insān-in-decline* +
*illā alladhīna āmanū* frame *"is like His saying:* laqad khalaqnā al-insāna fī aḥsani taqwīm, thumma radadnāhu
asfala sāfilīn, illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāt *[Q 95:4-6]."*

**Test:** Do Q 103 and Q 95 share the *al-insān + illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāt* construction? Scan
both verses' text in `quran-text/quran-no-tashkeel.json`.

**Result:** Q 95:6 reads *illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāti* — **character-identical** (mark-stripped)
to the opening of Q 103:3 (*illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāti*). Both surahs frame *al-insān* in a
negative default state (Q 103 *khusr* / Q 95 *asfal sāfilīn*) and rescue the same excepted set with the same
formula. This is a genuine shared-construction parallel.

**Verdict: VINDICATED — shared-construction parallel.** Q 103:3 and Q 95:6 share the verbatim
*illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāti* clause and the identical insān-default-state-then-exception logic.
al-Baghawī's cross-reference is textually exact. (The *āmanū wa-ʿamilū al-ṣāliḥāt* formula is the corpus's most
frequent creed-action collocation, so the parallel is real but not unique to this pair; the *insān-default →
same-exception* logic is the distinctive shared frame.)

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan (Qatāda: Medinan) | al-Qurṭubī, al-Baghawī | **VINDICATED** |
| 2 | 3 verses | al-Qurṭubī, al-Rāzī | **VINDICATED** |
| 3 | *al-insān* generic (exception proves it) | al-Ṭabarī, al-Rāzī, al-Jalālayn | **VINDICATED** (grammatical) |
| 4 | al-Shāfiʿī "would suffice them" / maximal-in-minimal | Ibn Kathīr | **DIRECTIONAL → CONFIRMED-at-structure** (Q103-F-01 A+C) |
| 5 | Q 103 a taḥaddī test-case | al-Rāzī | NOT-TESTABLE (theological) |
| 6 | ʿaṣr-loss / ḍuḥā-profit oath-diptych | al-Rāzī | NOT-TESTABLE (rhetorical) |
| 7 | Q 103:3 mirrors Q 95:4-6 | al-Baghawī ← Ibrāhīm | **VINDICATED** (verbatim shared clause) |

## Honest limits

- Claim 4's split is the key honesty point: the *structural* maximal-completeness reading is vindicated by
  Q103-F-01 Arms A+C, but the *theological* "sufficiency" assertion is explicitly out of empirical scope.
- Claim 7's parallel rests on the *āmanū wa-ʿamilū al-ṣāliḥāt* formula, which is corpus-frequent; the distinctive
  shared element is the *insān-negative-default → same-exception* logic shared by Q 103 and Q 95, not the formula alone.
- The Qatāda/Ibn-ʿAbbās "Medinan" minority view (Claim 1) is not on disk in the chronology data; treated as a
  documented tradition.
- No verse-count or major orthographic variant for Q 103 is on disk; Hafs-Kūfan is treated as canonical.

---

*All testable claims pre-registered before computation (Q103-F-01) or deterministic/grammatical. 2026-05-30.*
