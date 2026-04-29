# Journal: Fasting Theology (Phase B)

Run 1 — 2026-04-12
Agent: Phase B fasting-theology

## Method
1. Pulled all occurrences of ROOT:Swm from `data/morphology/quranic-corpus-morphology-0.4.txt` using grep on `ROOT:Swm`. Confirmed 14 tokens across 11 verses.
2. Loaded `quran-text/quran-min-tashkeel.json` to extract Arabic text for each root-bearing verse and surrounding context (2:183–187, 2:196, 4:92, 5:89, 5:95, 19:26, 33:35, 44:1–6, 58:1–4, 97:1–5).
3. Cross-tabulated morphological forms against semantic frames (liturgical Ramadan fast; expiatory fast; ascetic/votive fast).
4. Composed findings document with emphasis on (a) Ramadan legislation layering, (b) Laylat al-Qadr / Laylat Mubāraka identification, (c) kaffāra typology, (d) Maryam's speech-fast as the pivot.

## Raw morphological inventory (14 tokens)

| # | Location | Form (Buckwalter) | Lemma | POS | Gloss |
|---|----------|-------------------|-------|-----|-------|
| 1 | 2:183:6 | S~iyaAmu | SiyaAm | N (nom) | the fasting |
| 2 | 2:184:27 | taSuwmuw | yaSumo | V (impf 2MP subj) | that you fast |
| 3 | 2:185:17 | yaSumo-hu | yaSumo | V (impf 3MS juss) | let him fast it |
| 4 | 2:187:4 | S~iyaAmi | SiyaAm | N (gen) | of the fasting |
| 5 | 2:187:45 | S~iyaAma | SiyaAm | N (acc) | the fast |
| 6 | 2:196:29 | SiyaAmK | SiyaAm | N (indef gen) | (by) fasting |
| 7 | 2:196:48 | SiyaAmu | SiyaAm | N (nom) | fasting-of |
| 8 | 4:92:51 | SiyaAmu | SiyaAm | N (nom) | fasting-of |
| 9 | 5:89:29 | SiyaAmu | SiyaAm | N (nom) | fasting-of |
| 10 | 5:95:34 | SiyaAmFA | SiyaAm | N (indef acc) | as fasting |
| 11 | 19:26:14 | SawomFA | Sawom | N (indef acc) | a fast |
| 12 | 33:35:16 | S~aA}imiyna | S~aA}imiyn | PCPL MP | fasting (men) |
| 13 | 33:35:17 | S~aA}imaAti | S~aA}imaAt | PCPL FP | fasting (women) |
| 14 | 58:4:4 | SiyaAmu | SiyaAm | N (nom) | fasting-of |

Two distinct noun lemmas: **ṣiyām** (10 tokens — the regulative verbal-noun used for prescribed/expiatory fasting) and **ṣawm** (1 hapax at 19:26 — the archaic/older masdar used only for Mary's vow). Two active-participle forms at 33:35 and two finite verbs (2:184, 2:185).

## Observations worth flagging for the findings file
- Distributional: 7 of 14 tokens (50%) sit inside Q 2:183–196 — i.e. the Ramadan legislation plus the Hajj-fidya clause. The root is quasi-clustered.
- Lexical bifurcation: ṣiyām (institutional/legal) vs. ṣawm (personal/vowed). The Maryam hapax is not accidental — it preserves the older form for an older, pre-Islamic typology of fasting that is silence, not abstinence from food.
- 2:184 and 2:185 show **progressive legislation**: v.184 presents fasting as days countable with a ransom option for those-who-can-bear-it (yuṭīqūnah); v.185 tightens into an obligation keyed to witnessing the month. Classical tafsir reads v.185 as naskh (abrogation) of v.184's fidya option except for the infirm.
- 2:186 is a prayer-response verse inserted into the fasting block — a structural anomaly worth noting as a form of "iltifat" into divine first-person ("fa-innī qarībun… idhā daʿāni") in the middle of legal second-person.
- 2:187 contains the most concrete empirical time-marker in Quranic law: "until the white thread becomes distinguishable from the black thread of dawn" — an astronomical/phenomenological boundary (tabayyun al-khayṭ).
- Iʿtikāf is prescribed negatively: "do not approach them (wives) while you are engaged in iʿtikāf in the mosques" — iʿtikāf is presupposed, not commanded.
- Surah 97 is three ayahs + two; "khayrun min alfi shahr" = 83.3 years, i.e. more than an average human lifespan.
- 97:4 uses "tanazzalu" (iterative/present) not "nazala" (perfective) — the descent is durative, not a one-off. "min kulli amr" is ambiguous: either "for every matter" or "from every matter" (i.e. from every kind of command).
- Q 44:3 "laylatin mubārakah" with "fīhā yufraqu kullu amrin ḥakīm" (44:4) plausibly = Laylat al-Qadr, producing an intra-Quranic identification (anchored by the common "amr"-decision vocabulary). This is the classical exegetical reading (Ibn ʿAbbās, Qatāda).
- Kaffāra typology: in 4:92 the fast is 2 consecutive months (substitutes for both slave-manumission AND diyya when unable); in 5:89 the fast is 3 days (tertiary tier after feeding/clothing/manumission); in 58:4 the fast is 2 consecutive months (secondary tier after manumission, before feeding 60); in 5:95 the fast is an equivalent (ʿadl) count — the severity ordering maps to the moral gravity of the act.
- 2:183 "kamā kutiba ʿalā lladhīna min qablikum" — fasting is framed as trans-communal. No specification of which "those-before" — deliberately ecumenical.

## Word-count target tracking
Aimed for ~2800 words in findings file; actual will trend toward that.

## Open threads / follow-ups
- Cross-reference with root √k-t-b (the "kutiba ʿalaykum" formula appears also for qiṣāṣ 2:178 and qitāl 2:216 — a triad of prescriptions).
- Relationship of "tatta qūn" (purpose clause 2:183) and "yattaqūn" (purpose clause 2:187) as ring-composition markers bracketing the passage.
- Surah 97 vs. Surah 44 as twinned laylat-texts — a paired-surah phenomenon.
- Mary's "ṣawman li-l-raḥmān" as the only fast explicitly dedicated ("li-") to a divine name.
