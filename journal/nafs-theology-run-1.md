# Journal — nafs-theology run 1

Date: 2026-04-12
Agent: Phase C theological-structural
Scope: Full computational audit of root n-f-s in the Quran and classical 3-soul-state typology (ammāra / lawwāma / muṭma'inna).

## Inputs
- `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4, 128,276 segments)
- `quran-text/quran-no-tashkeel.json`
- `data/translations/en.sahih.txt`
- `findings/intra-quranic-cross-references.md` (Q 13:28 dhikr/reassurance network)
- `findings/phase-b-hypotheses/root-cartography.md` (root `nfs` = 298)

## Method
1. Grep morphology for `ROOT:nfs` → 298 segment tokens → classified by lemma + grammatical features (FS / FP, NOM / ACC / GEN, POS N vs V).
2. For each singular nafs, scan adjacent tokens (w±2) for adjectives or participles; separately hunt roots {Amr, lwm, rDy, Tmn, hwy} near every nafs.
3. Cross-verse: intersect `nfs` verse-set with `qlb` (heart) and `rwH` (spirit), and with `hwy` (base desire), `mwt` (death).
4. Structural: position of Q 12:53 inside Sūrat Yūsuf (word-cumulative → 48.4% of the surah), context windows around Q 12:50–56, Q 75:1–15, Q 89:15–30, Q 91:1–10.
5. Meccan/Medinan split using canonical `surah.type` field in the JSON.
6. Verified the classical 4th-state candidates: found `rāḍiya` + `marḍiyya` as twin participles of root r-D-w modifying the *muṭma'inna nafs* of Q 89:27 → 89:28. No other Quranic nafs takes a *virtue* adjective; every other adjective-modified nafs is neutral (wāḥida "one/single," dhā'iqa "tasting [death]") or negative (ammāra, lawwāma are in the classical trio).

## Counts verified
- Root nfs segment count: **298** (root-cartography said ~295; tight match, 1% off — counting noun + 2 verbs + 1 participle of same root).
- Distinct *verses* containing nfs: **270** (one verse can have multiple tokens; max is Q 16:111 with 3).
- Singular nafs: **140** tokens. Plural anfus/nufuws: **155** (broken plural nufuws appears only 2×, Q 17:25 and Q 81:7). Verbal Form V (tanaffasa) 1× Q 81:18. Form VI imperfect (yatanāfasu) 1× Q 83:26. Active participle Form VI (mutanāfisūn "competitors") 1× Q 83:26.
- Meccan 163 / Medinan 135; plural anfus is MEDINAN-leaning (66 Meccan vs 89 Medinan); singular nafs is MECCAN-leaning (97 vs 46). This aligns with Meccan focus on individual soul-accountability vs Medinan collective/legal ("yourselves").

## Key structural findings (surprises)
1. **Q 12:53 sits at exactly 48.4% of Sūrat Yūsuf's word count** (926/1912). It is the *near-center* of Joseph's surah. Classical Sufi hermeneutic reads 12:53 as the psychological pivot of the whole Joseph narrative; the corpus appears to back this structurally. Noteworthy but not ring-confirmed.
2. **The noun *ammāra* is NOT root nfs** — it's root A-M-R (to command) in hyperbolic feminine intensive (*fa''āla*). So the phrase *nafs ammāra* is morphologically a noun + noun (or noun + adjective derived from A-M-R). The "evil-commanding" modifier is a verbal-noun applied to nafs, not built from nfs itself.
3. **Q 75:2 *lawwāma* IS root l-w-m**, morphologically `STEM|POS:ADJ|LEM:l~aw~aAmap|ROOT:lwm|F|GEN`. Root l-w-m occurs 14× in the Quran; at 75:2 it's the only intensive feminine form — a hapax of grammar.
4. **Q 89:27 *muṭma'inna* IS root T-m-n**, `ACT|PCPL|(XII)` — one of only **13** tokens of this root across the whole Quran. *Critically*, that same root drives Q 13:28 (heart-rest), Q 2:260 (Abraham's heart), Q 3:126, Q 5:113, Q 8:10, Q 16:106 (*muṭma'inn bi-l-īmān*), Q 16:112 (*muṭma'inna* as a town at peace), Q 22:11, Q 17:95 (angels muṭma'inna on earth). **The T-m-n root unifies "heart reassured" + "soul reassured" + "faith reassured" + "city at peace"** — the muṭma'inna nafs of 89:27 is the culmination of the whole T-m-n theological vocabulary.
5. **Q 89:28 rāḍiya + marḍiyya** — active and passive participles of root r-D-w stacked — modifies the same *muṭma'inna nafs*. This is the "4th and 5th" nafs-state Sufi tradition separates (nafs rāḍiya, nafs marḍiyya), but the Quran gives them as continuation of 89:27, not as independent states. **They belong to the same nafs.**
6. **nafs + qalb co-occur in only 4 verses**: Q 3:154, Q 4:63, Q 5:52, Q 18:28. They are **not a paired vocabulary** in the Quran. Classical Sufi psychology that treats nafs / qalb / rūḥ as three distinct centers is a SCHOLASTIC SYNTHESIS, not a Quranic lexical pattern.
7. **nafs + rūḥ co-occur in only 2 verses**: Q 2:87, Q 3:117 (rūḥ here is "Holy Spirit" / wind — not interchangeable with nafs as "soul").
8. **Voice/agency**: 83/140 singular nafs are in GENITIVE case (possessive "his/her soul" or after prepositions). 33 ACC (nafs as object: "to send ahead a soul / to kill a soul"). 24 NOM (nafs as subject: "every nafs will taste death," "the nafs is ammāra"). **The nafs is more often TALKED ABOUT than ACTING** — it is twice as often patient as agent in singular form.
9. **No explicit Quranic sequence of ammāra → lawwāma → muṭma'inna**. The three terms occur in different surahs (12, 75, 89) and are never juxtaposed. The classical progression is an *interpretive overlay* on a thematic inventory. HOWEVER — the three appearances correspond structurally: 12:53 the self-confessing mid-narrative soul; 75:2 the resurrection-oath soul; 89:27 the paradise-welcoming soul. In revelation-chronology (Nöldeke): 89 (late Meccan), 75 (early Meccan), 12 (middle Meccan). There is NO chronological progression. The "3-stage ladder" is purely synchronic theology.
10. **Q 91:7-10 is the most condensed Quranic psychology**: "by the nafs and the One who proportioned it / and inspired it with its fujūr and its taqwā / successful is he who purifies it, failed is he who defiles it." This 4-verse oath-block contains the raw materials of the entire classical doctrine: a nafs with dual potential + a refinement ethic — but uses NONE of the ammāra/lawwāma/muṭma'inna vocabulary.

## Decisions
- Report the 3-stage typology honestly as **inventory**, not **sequence**. Sufi scholarship imposed the ladder; the Quran inventories states.
- Include the *rāḍiya* + *marḍiyya* pair from 89:28 as an organic 4th/5th state that Sufi tradition correctly identifies.
- Cross-link root Tmn network to the 13:28 finding already documented — the *muṭma'inna* nafs completes that arc.
- Target: 3000+ words, YAML frontmatter, network diagram, honest verdict.

## Open questions
- Would a chronological-by-revelation re-read of all 298 nfs tokens show a semantic shift Meccan → Medinan? Quick count (163 Meccan / 135 Medinan) plus plural-skew suggests yes, but full semantic diachronic work out of scope for this run.
- Is there a *structural* ring in Sūrat Yūsuf with 12:53 as center? 48.4% word-midpoint is suggestive; not tested.
