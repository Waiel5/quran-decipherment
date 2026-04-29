---
id: H-NEW-49
title: Surah-name semantic classification — distribution, muqaṭṭaʿāt-status enrichment, and lexical-content prediction
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (taxonomy locked from memory BEFORE consulting any name-list source or quran-no-tashkeel.json content; only structural format of JSON inspected, not surah-name strings beyond Q1 al-Fatiḥa and Q2 al-Baqara visible during environment setup)
bonferroni_family: 2026-04-15-Wave-Surah-Name-Class
bonferroni_k: 5
alpha_bon: 0.01
rules_tuple: (hafs-kufan; canonical 114; standard transliteration; 29-muqaṭṭaʿāt set as in H-NEW-44/45/46)
primary_data: 114 surah names with locked class-labels + muqaṭṭaʿāt indicator + per-surah text for lexical-centrality test
seed: 20260416
---

# [[h-new-49-surah-name-class|H-NEW-49]] — Surah-name Semantic Classification

## Question

(1) What is the distribution of pre-registered semantic classes across the 114 surah names?
(2) Are muqaṭṭaʿāt-opened surahs enriched in any specific semantic class?
(3) Are the Khawātim al-Ḥashr surahs (Q 59 area, the divine-names cluster) enriched in divine-attribute names?
(4) Does the surah-name appear as a lexically-central root inside the surah text (i.e., is the name a content-key)?

## Garden-of-forking-paths disclosure

Prior knowledge before locking the taxonomy:
- I know al-Baqara (Q 2, "the cow") opens with muqaṭṭaʿāt (الم). So at least one ANIMAL-class surah is muqaṭṭaʿāt-opened.
- I know Q 12 Yūsuf opens with الر (muqaṭṭaʿāt). Q 19 Maryam opens with كهيعص. Q 36 Yāsīn opens with يس. Q 38 Ṣād opens with ص. So at least 4 PROPHET/PERSON-class surahs open with muqaṭṭaʿāt.
- I know Q 29 al-ʿAnkabūt (spider) opens with الم and Q 27 al-Naml (ant) opens with طس — so ANIMAL-class is plausibly enriched in muqaṭṭaʿāt openers.
- I know Q 55 al-Raḥmān is divine-attribute and is NOT a muqaṭṭaʿāt opener.
- I know Q 59 al-Ḥashr ends with the famous "huwa Allāh alladhī …" divine-names passage, but the SURAH NAME itself (al-Ḥashr = "the Gathering") is an EVENT/COSMOLOGICAL class, not a divine-attribute. This is a key honest disclosure: my Q4 will probably be NULL because al-Ḥashr's name doesn't fall in the divine-attribute class even though the surah CONTAINS the divine-names cluster.
- Lexical-centrality (Q4 lexical): I expect al-Baqara to feature root b-q-r (cow incident, Q 2:67-71) but it's not the most-frequent root globally. So the Q4 test must use rate vs corpus baseline, not global rank.

These disclosures are made BEFORE running tests.

## Locked taxonomy (frozen 2026-04-15, before reading the surah-name list from JSON)

I assign each of 114 surahs to ONE primary class. Multi-class names (e.g., al-Anbiyāʾ = both prophets and revelation) get the most-specific class. Categories:

1. **PROPHET_PERSON** — surahs named after a prophet, messenger, or named human figure (e.g., Yūsuf, Hūd, Ibrāhīm, Muḥammad, Maryam, Nūḥ, Yūnus, Luqmān, Āl ʿImrān).
2. **ANIMAL_OBJECT** — surahs named after an animal, plant, or physical object (e.g., al-Baqara=cow, al-Naḥl=bee, al-Naml=ant, al-ʿAnkabūt=spider, al-Fīl=elephant, al-Anʿām=cattle, al-Qalam=pen).
3. **DIVINE_ATTRIBUTE** — surahs named after a name/attribute of God (al-Raḥmān, al-Nūr, al-Mulk, al-Aʿlā, al-Ṣamad if framed as al-Tawḥīd / al-Ikhlāṣ).
4. **COSMOLOGICAL_NATURAL** — surahs named after a celestial body or natural phenomenon (al-Najm=star, al-Shams=sun, al-Qamar=moon, al-Layl=night, al-Fajr=dawn, al-Ḍuḥā=morning, al-ʿAṣr=time, al-Burūj=constellations, al-Ṭāriq, al-Raʿd=thunder).
5. **EVENT_ESCHATOLOGICAL** — surahs named after a Day-of-Judgment event or eschatological scene (al-Qiyāma, al-Qāriʿa, al-Wāqiʿa, al-Ḥāqqa, al-Inshiqāq, al-Infiṭār, al-Takwīr, al-Zalzala, al-Ghāshiya, al-Nabaʾ, al-Ḥashr=Gathering, al-Mursalāt).
6. **SOCIAL_LEGAL** — surahs named after a social group, legal theme, or human-relations content (al-Nisāʾ=women, al-Mujādilah=disputer, al-Mumtaḥina, al-Ṭalāq=divorce, al-Ḥujurāt, al-Munāfiqūn, al-Kāfirūn, al-Muʾminūn, al-Mulk if read as kingship, al-Nās).
7. **REVELATION_RITUAL** — surahs named after a revelation event, scripture, prayer, or ritual act (al-Fātiḥa=opening, al-ʿAlaq, al-Qadr, al-Bayyina, al-Jumʿah, al-Māʿūn, al-Furqān, al-Kahf, al-Isrāʾ, al-Sajdah, al-Aḥzāb if read as confederates of revelation event).
8. **MUQATTAAT_LETTER** — surahs whose name IS a muqaṭṭaʿāt letter-string (Ṭāhā=Q20, Yāsīn=Q36, Ṣād=Q38, Qāf=Q50, possibly al-Raʿd, but al-Raʿd belongs to COSMOLOGICAL not MUQATTAAT). The MUQATTAAT_LETTER class has at most 4 members (Ṭāhā, Yāsīn, Ṣād, Qāf).
9. **OTHER_ABSTRACT** — abstract concepts that don't fit elsewhere (al-Ikhlāṣ=sincerity if not divine-attribute; al-ʿĀdiyāt; al-Inshirāḥ; al-Tīn=fig — wait, al-Tīn goes to ANIMAL_OBJECT; al-Aʿrāf — Heights, ambiguous → cosmological/spatial → put in COSMOLOGICAL_NATURAL).

Each surah is assigned to exactly ONE class. In ambiguous cases the "most-specific lexical referent" wins. Class definitions are frozen here.

## Pre-committed assignment principles (binding)

- A name that IS a muqaṭṭaʿāt-letter string → MUQATTAAT_LETTER (Ṭāhā, Yāsīn, Ṣād, Qāf).
- A proper-noun person → PROPHET_PERSON. (Includes Maryam, Luqmān; includes tribal/family-of-X like Āl ʿImrān).
- A common-noun animal/plant/object → ANIMAL_OBJECT.
- An asmāʾ-Allāh-ḥusnā direct lexeme → DIVINE_ATTRIBUTE (al-Raḥmān, al-Mulk if read as kingdom-of-God).
- An astronomical body or weather/time phenomenon → COSMOLOGICAL_NATURAL.
- A scene/event description from yawm al-qiyāma → EVENT_ESCHATOLOGICAL.
- A relational/social/legal noun → SOCIAL_LEGAL.
- A scripture/recitation/prayer/ritual term → REVELATION_RITUAL.
- Otherwise → OTHER_ABSTRACT.

Tie-breaker: if two classes apply, prefer the one with the smaller global count (post-counting), to break ties via rarity. If still tied, prefer the order as listed (PROPHET_PERSON > ANIMAL_OBJECT > DIVINE_ATTRIBUTE > COSMOLOGICAL_NATURAL > EVENT_ESCHATOLOGICAL > SOCIAL_LEGAL > REVELATION_RITUAL > MUQATTAAT_LETTER > OTHER_ABSTRACT).

The class for each surah will be assigned in code immediately after loading the name-list and BEFORE any statistical test is run. The mapping will be printed and frozen in the JSON output BEFORE the χ² is computed. The mapping is auditable.

## The 5 pre-registered test cells (Bonferroni k=5, α=0.01)

### Cell 1 — Class-distribution baseline
Tabulate counts per class across 114 surahs. No p-value; descriptive (counts as one of the 5 cells for transparency).
**Verdict rule**: cell 1 is descriptive. PASS = published table.

### Cell 2 — Muqaṭṭaʿāt vs name-class χ²
Build 2×9 contingency table: muqaṭṭaʿāt-opener (Y/N) × 9 classes. χ² test. df = 8 (or fewer if classes pooled for low expected counts).
- One-sided null: classes are independent of muqaṭṭaʿāt status.
- α_bon = 0.01.
- If any expected cell < 5, pool small classes (OTHER_ABSTRACT + MUQATTAAT_LETTER + REVELATION_RITUAL pooled FIRST in this fixed order).

### Cell 3 — Permutation test, MUQATTAAT_LETTER class enrichment in muqaṭṭaʿāt-openers
The 4 MUQATTAAT_LETTER surahs (Ṭāhā, Yāsīn, Ṣād, Qāf) are by definition muqaṭṭaʿāt-openers (their NAME is the opener). One-sided p via 10⁵ permutations of class-labels across 114 surahs; observed = 4/4 of MUQATTAAT_LETTER are muqaṭṭaʿāt-openers.
**Note**: this is a TAUTOLOGICAL POSITIVE CONTROL (MW-5). Locked here as a sanity check. Expected p ≪ 0.001.

### Cell 4 — Khawātim al-Ḥashr divine-attribute enrichment
Test: Q 59 al-Ḥashr's NAME is in DIVINE_ATTRIBUTE class? **Pre-registered prediction: NO** (al-Ḥashr = "the Gathering" → EVENT_ESCHATOLOGICAL).
Then: among the surrounding "Mufaṣṣal short" surahs Q 50–114, what fraction are DIVINE_ATTRIBUTE-named vs the long-surah region Q 1–49? Fisher exact, two-sided.
α_bon = 0.01.

### Cell 5 — Lexical centrality of name-root in surah
For each surah whose name is a content-noun (not just a muqaṭṭaʿāt-letter), test whether the rough Arabic root of the name appears in the surah text at a per-token rate higher than the rate in the rest of the corpus.
- Statistic: per-surah fraction of tokens containing the name-root letters (consonant-skeleton match) vs the global-corpus rate excluding that surah.
- One-sided test per surah → Bonferroni-corrected within Cell 5 by number of testable surahs (~80–100).
- Bonferroni-adjusted threshold for Cell 5: α_per_surah = 0.01 / N_testable.
- Cell 5 PASSES if ≥ 1/3 of testable surahs are individually significant after within-cell Bonferroni; STRONG-PASS if ≥ 2/3.

## MW-5 positive control

Cell 3 itself is the tautological MW-5 (MUQATTAAT_LETTER class is a perfect predictor). For Cell 5, additional MW-5: surah Q 71 Nūḥ — root n-w-ḥ should appear at extreme density (Nūḥ is named ~28 times in 28 verses). Pre-registered: Q 71 Nūḥ should be the most extreme outlier in Cell 5.

## Null model

- Cell 2: standard χ² (analytical).
- Cell 3: 10⁵ permutations, seed 20260416.
- Cell 4: Fisher exact (analytical).
- Cell 5: per-surah hypergeometric or binomial vs corpus rate.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Cell 1 only (descriptive) | DESCRIPTIVE-only |
| Cell 2 significant | name-class IS associated with muqaṭṭaʿāt status |
| Cell 3 significant | MW-5 control PASS |
| Cell 4 significant | divine-attribute clusters in mufaṣṣal |
| Cell 5 ≥ 1/3 surahs sig | name predicts content (PASS) |
| Cell 5 ≥ 2/3 surahs sig | name strongly predicts content (STRONG-PASS) |
| All cells null except 3 | only the tautology fires; no real signal |

## Integrity

- Taxonomy is locked HERE before reading any name-list.
- Bonferroni k=5 declared.
- Cell 3 is explicitly a tautological control.
- Cell 4's pre-registered prediction is NULL for the al-Ḥashr name itself.
- All cells published regardless of direction.
- Seed 20260416.
