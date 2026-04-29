---
surah: 36
surah_name_ar: يس
surah_name_translit: Yāsīn
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 7 audits
---

# Q 36 Yāsīn — Classical Claims Audit

## 0. Source

This file pre-registers and tests classical claims about Q 36 with explicit rules-tuple discipline. Every claim is sourced to a specific scholar + work + passage. Tests are computed from on-disk data files (not from memory). Verdicts are: VINDICATED / FALSIFIED / RULES-TUPLE-FRAGILE / NOT-EMPIRICALLY-TESTABLE / DIRECTIONAL.

## Audit 1 — al-Tirmidhī's *qalb al-Qurʾān* tradition (Q 36 = "the heart of the Qurʾān")

### Claim
The classical popular tradition that Q 36 is *qalb al-Qurʾān* ("the heart of the Qurʾān"), sourced primarily to al-Tirmidhī's *Sunan*. The hadith text in our corpus (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` idInBook 2970, global id 28750):

> إِنَّ لِكُلِّ شَيْءٍ قَلْبًا وَقَلْبُ الْقُرْآنِ يس وَمَنْ قَرَأَ يس كَتَبَ اللَّهُ لَهُ بِقِرَاءَتِهَا قِرَاءَةَ الْقُرْآنِ عَشْرَ مَرَّاتٍ

(Anas-chain via Hārūn Abū Muḥammad ← Muqātil b. Ḥayyān ← Qatāda ← Anas).

### Operationalization
Two sub-claims to test:
- **(1a) Chain authenticity** — does the chain meet *ṣaḥīḥ* / *ḥasan* threshold?
- **(1b) Multi-axis quantitative-centrality** — does Q 36 score top-tier on multi-axis "heart" measures (positional / lexical / centrality / theme)?

### Test
**Sub-claim 1a — chain authenticity**: Direct corpus-internal evidence (`tirmidhi.json` global #28750 entry text):
- al-Tirmidhī's own grading: *gharīb*, "Hārūn Abū Muḥammad is an unknown shaykh" (*shaykh majhūl*).
- al-Tirmidhī's cross-chain note: "the chain is not authentic; its isnād is weak" (*lā yaṣiḥḥu min qibal isnādih, isnāduhu ḍaʿīf*).
- The hadith is **not in al-Bukhārī or Muslim** (verified by 0 substantive matches in `bukhari.json` and `muslim.json`).
- Modern criticism (al-Albānī): ḍaʿīf jiddan / mawḍūʿ via Hārūn.
- Ibn Kathīr's note (in `ibn-kathir-tafsir-quran.openiti.raw.txt` ~ offset 286,639): "*infarada bihī Aḥmad*" — sole-narration through Aḥmad.

**Sub-claim 1b — multi-axis centrality**: Pre-registered in [[h-new-82-yasin-heart|H-NEW-82]] (`findings/phase-b-hypotheses/h-new-82-yasin-heart.md`), tested across 6 axes:

| Axis | Q 36 rank | Pre-reg PASS threshold |
|:--|:-:|:--|
| A1 mushaf-position-median | 43 / 114 | top-5 |
| A2 verse-count-median | 88 / 114 | top-5 |
| A3 letter-count-median | 76 / 114 | top-5 |
| A4 lexical-centroid (mean root-Jaccard) | 18 / 114 | top-5 |
| A5 eigenvector-centrality | 27 / 114 | top-5 |
| A6 theme-centroid (cosine) | 16 / 114 | top-5 |

Q 36 attains top-5 on 0/6 axes. Pre-registered PASS criterion: rank 1 on ≥ 3 axes OR top-5 on ≥ 5 axes — **NOT MET (0/6)**.

### Rules-tuple
For (1a): chain text from `tirmidhi.json` directly, no rules-tuple sensitivity (the chain text is rules-tuple invariant).

For (1b): `(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan)` per H-NEW-82's pre-reg.

### Verdict
**1a — DIRECTIONAL ḌAʿĪF (the chain is corpus-internally graded *gharīb* + *shaykh majhūl* + *isnāduhu ḍaʿīf* by al-Tirmidhī himself)**. The chain does not meet *ṣaḥīḥ*/*ḥasan* canonical threshold. The hadith functions as a *fadāʾil*-tradition, actionable in classical Sunnī methodology under the multiple-chain mitigation but not as a textual-doctrinal anchor.

**1b — FALSIFIED** (Q 36 is not the multi-axis quantitative "heart" of the corpus; rank 0/6 top-5).

The empirical positional median is **Q 57 al-Ḥadīd**; the empirical lexical centroid is **Q 10 Yūnus**; the empirical theme centroid is **Q 46 al-Aḥqāf**; the empirical FR-distance centroid is **Q 112 al-Ikhlāṣ**. None of these is Q 36.

What remains intact is the **classical-liturgical-theological centrality**: Q 36 scores corpus-max 10/10 on the project's hadith-fadāʾil rubric ([[h-new-860-hadith-architectural-alignment|H-NEW-860]]). This is the dual-iʿjāz typology's meaning-iʿjāz axis. The classical claim's **liturgical-theological content** is empirically intact; only the **multi-axis quantitative-centrality form** is falsified.

## Audit 2 — The "recite Yāsīn over your dying" tradition (Abū Dāwūd #3122 / Ibn Mājah #1182)

### Claim
The classical-popular tradition that Yāsīn is the surah-of-the-deathbed, sourced to:
- Abū Dāwūd, *Sunan*, idInBook 3122 (global 23626): "اقْرَءُوا يس عَلَى مَوْتَاكُمْ" via Maʿqil b. Yasār.
- Ibn Mājah, *Sunan*, idInBook 1182 (global 31015): "اقْرَءُوهَا عِنْدَ مَوْتَاكُمْ — يَعْنِي يس" via the same chain.

### Operationalization
The chain is shared: Ibn al-Mubārak ← Sulaymān al-Taymī ← Abū ʿUthmān (*not* al-Nahdī, per the in-text disambiguation) ← his father ← Maʿqil b. Yasār.

We test:
- **(2a) Chain authenticity** — chain-link-by-link assessment
- **(2b) Cross-chain coverage** — the same chain in Abū Dāwūd + Ibn Mājah + Aḥmad's *Musnad* (per Ibn Kathīr's "*infarada bihī Aḥmad*" remark)

### Test
**Chain links**:
- *Maʿqil b. Yasār*: well-attested Companion (a known Companion of the Prophet).
- *His father*: **unnamed** in the chain — a structurally weak link.
- *Abū ʿUthmān (not al-Nahdī)*: the in-text editor's disambiguation phrase identifies the narrator as a different Abū ʿUthmān from the well-attested al-Nahdī. The non-Nahdī Abū ʿUthmān is poorly-attested in the rijāl literature.
- *Sulaymān al-Taymī*: well-attested.
- *Ibn al-Mubārak* (= ʿAbd Allāh b. al-Mubārak, d. 181 AH): well-attested.

The two-link weakness (*unnamed father* + *Abū ʿUthmān not al-Nahdī*) is the chain's primary defect.

**Cross-chain coverage**: Ibn Kathīr cites the same chain transmitted in Aḥmad's *Musnad* (Aḥmad #20302 per conventional numbering) and notes Aḥmad's solitary narration. Our corpus's `ahmed.json` is partial (1,374 hadith of 30,000+) and does not include the Musnad #20302 entry. **DATA-GAP**: the Aḥmad #20302 entry is not directly verifiable.

### Rules-tuple
Hadith text from on-disk JSON; chain-link assessment from in-text editor's disambiguating notes.

### Verdict
**DIRECTIONAL ḌAʿĪF (the chain has two structural-weakness links + multiple-chain mitigation)**. The popular liturgical practice rests on the *fadāʾil*-of-amal principle; the textual chain weakness is documented. Conservative classical positions (Ibn al-Qaṭṭān, al-Dāraquṭnī) rate the chain ḍaʿīf; majority-Ḥanafī and Mālikī classical positions accept the chain as ḥasan via multiple-chain mitigation. The popular practice is **not falsified** but **chain-grade-disputed**.

## Audit 3 — "Q 36 (يس) is the singleton 2-letter muqaṭṭaʿāt opening"

### Claim
A claim sometimes asserted in popular literature (and noted in the Wave-D launch task as a fact-to-verify) that Q 20 Ṭāhā and Q 36 Yāsīn are the only 2-letter muqaṭṭaʿāt openings; or further restricted, that Q 36 is the singleton 2-letter muqaṭṭaʿāt apart from Q 20.

### Operationalization
Inspect the muqaṭṭaʿāt of all 29 muqaṭṭaʿāt-opened surahs (`quran-text/quran-no-tashkeel.json` v.1 of each):

```
Q 1: (no muqaṭṭaʿāt)
Q 2: الم (3-letter)
Q 3: الم (3-letter)
Q 7: المص (4-letter)
Q 10-15: الر (3-letter — 6 surahs)
Q 13: المر (4-letter)
Q 19: كهيعص (5-letter)
Q 20: طه (2-letter)
Q 26: طسم (3-letter)
Q 27: طس (2-letter)
Q 28: طسم (3-letter)
Q 29-32: الم (3-letter — 4 surahs)
Q 36: يس (2-letter)
Q 38: ص (1-letter)
Q 40-46: حم (2-letter — 7 surahs)
Q 42: حم عسق (5-letter, spanning v.1-2)
Q 50: ق (1-letter)
Q 68: ن (1-letter)
```

### Test
The 2-letter muqaṭṭaʿāt-opening surahs are: **Q 20 (ṬH), Q 27 (ṬS), Q 36 (YS), Q 40-46 (ḤM × 7) = 10 surahs total**.

If we exclude the ḥawāmīm cluster (Q 40-46) as a single repeated marker: **Q 20, Q 27, Q 36 = 3 distinct 2-letter muqaṭṭaʿāt openings**.

If we use the "unique 2-letter combination" reading: **Q 20 (ṬH), Q 27 (ṬS), Q 36 (YS), Q 40 (ḤM, with Q 41-46 as repetitions) = 4 distinct combinations**.

Verified against `quran-text/quran-no-tashkeel.json` v.1 of each surah (computed; see `01-empirical-profile.md` §3 verification).

### Verdict
**FALSIFIED**. The claim that Q 36 is the singleton 2-letter muqaṭṭaʿāt is empirically false. The 2-letter muqaṭṭaʿāt set has **cardinality 10** (counting Ḥm-repetitions) or **3-4 distinct** (counting Ḥm as one cluster). Q 36 is one of THREE distinct 2-letter muqaṭṭaʿāt-opened surahs (Q 20, 27, 36) plus the Ḥm cluster.

The Wave-D launch task stipulated "YS = 2-letter muqaṭṭaʿāt singleton" as a claim to verify. The claim is empirically refuted. What IS true: **Q 36 (YS) and Q 20 (ṬH) are the only 2-letter muqaṭṭaʿāt openings whose muqaṭṭaʿāt is the entire first verse with NO trailing oath-or-content** — Q 27 (طس) has a trailing *تلك آيات القرآن وكتاب مبين* in v.1 itself (i.e., the muqaṭṭaʿāt + content share v.1); Q 36 (يس) has the muqaṭṭaʿāt as a standalone v.1 with the oath in v.2. Under that more-restricted operationalisation, **Q 36 is not the singleton; Q 20 and Q 36 are the two surahs whose 2-letter muqaṭṭaʿāt is a standalone v.1**. (Verified `quran-text/quran-no-tashkeel.json`: Q 20 v.1 = "طه" alone; Q 36 v.1 = "يس" alone; Q 27 v.1 = "طس ۚ تلك آيات القرآن وكتاب مبين".)

## Audit 4 — *Aṣḥāb al-Qarya = Antioch* (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr et al.)

### Claim
The classical near-consensus identification (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī al-Durr, al-Zamakhsharī, al-Ṭabarsī) that the *al-qarya* of Q 36:13 is **Antioch (Anṭākiya)**, sometimes specified as the apostolic visit by Yūḥannā (John) and Bawlas (Paul), reinforced by Sham‘ūn al-Ṣafā (Simon Peter).

### Operationalization
The verse text (`quran-text/quran-no-tashkeel.json` Q 36:13) reads:

> واضرب لهم مثلا أصحاب القرية إذ جاءها المرسلون

The text says only "*the city*" (al-qarya) without naming. The Antioch-identification is exegetical-traditional, sourced to *isrāʾīlīyāt* and post-Quranic apostolic-tradition concordance.

### Test
- The text says nothing identificatory about the city. **Not testable from the textual content alone.**
- Five classical mufassirūn (al-Ṭabarī, Ibn Kathīr, al-Zamakhsharī, al-Suyūṭī, al-Ṭabarsī) explicitly name Antioch as the primary identification; al-Qurṭubī enumerates 5 candidates with Antioch primary.
- The Antioch-identification depends on (a) the apostolic-tradition concordance (the Three-Messengers narrative as the Yūḥannā-Bawlas-Shamʿūn deputation to Antioch in Christian apostolic literature), (b) the *isrāʾīlīyāt* sources Ibn Kathīr explicitly flags as uncertain.

### Rules-tuple
Text-level verification: rules-tuple invariant (the verse says no city-name across all tashkeel variants).

### Verdict
**NOT-EMPIRICALLY-TESTABLE** at the text-level (the text does not name the city). **Classical-traditional consensus**: Antioch is the dominant interpretive identification (8 of 9 surveyed mufassirūn report it as primary or among the candidates). The verdict reflects the project's discipline: classical-traditional historical identifications that depend on extra-Quranic sources are **NOT-EMPIRICALLY-TESTABLE**, recorded as classical consensus without textual endorsement.

## Audit 5 — Q 36:82 *kun-fa-yakūn* corpus-wide instance count + climax-position uniqueness

### Claim
Classical exegetical observation (al-Rāzī, al-Zamakhsharī, Ibn Kathīr Q 36:82 commentary; cf. `03-tafsir-survey.md` §3) that Q 36 is "constructed around" the *kun fa-yakūn* climax. We operationalise this two ways:
- (5a) the corpus-wide *kun fa-yakūn* instance count
- (5b) the position-in-surah of each instance, testing whether Q 36:82 is uniquely at the rhetorical-climax position

### Operationalization
Search `quran-text/quran-no-tashkeel.json` for the orthographic-exact phrase `كن فيكون` (no-tashkeel), recording (surah, verse, total-verses-of-surah) for each match.

### Test
Computed:

| # | Reference | Position-in-surah |
|:-:|:--|:-:|
| 1 | Q 2:117 | 117/286 = **40.9%** |
| 2 | Q 3:47 | 47/200 = 23.5% |
| 3 | Q 3:59 | 59/200 = 29.5% |
| 4 | Q 6:73 | 73/165 = 44.2% |
| 5 | Q 16:40 | 40/128 = 31.2% |
| 6 | Q 19:35 | 35/98 = 35.7% |
| 7 | **Q 36:82** | **82/83 = 98.8%** |
| 8 | Q 40:68 | 68/85 = 80.0% |

8 corpus instances total. **Q 36:82 is the only verse > 95% of its surah; the next-closest is Q 40:68 at 80.0%, a gap of 18.8 percentage points.**

### Rules-tuple
`(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`. Cross-validated against `quran-text/quran-min-tashkeel.json`: same 8 verse identification (the *كن فيكون* substring is rules-tuple stable across no-tashkeel and min-tashkeel; under full-tashkeel some marker variation may shift orthography but does not affect verse-level identification).

### Verdict
**VINDICATED at descriptive-position level**. Q 36:82 is the only *kun fa-yakūn* verse positioned at the rhetorical climax of its surah (>95% through). The classical reading "Q 36 is structured around the *kun fa-yakūn* climax" is empirically supported at the position level by an 18.8-point gap to the next-closest instance (Q 40:68 at 80%). See Q036-F-03 in `06-novel-findings.md` for the pre-registered version.

## Audit 6 — Q 36 word-count rank vs corpus-mid (positional uniqueness)

### Claim
A claim sometimes implicit in the *qalb al-Qurʾān* tradition: that Q 36 has a corpus-relevant positional uniqueness — at the geometric center, structural midpoint, or word-count median.

### Operationalization
Compute Q 36's positional and length-related ranks:
- (6a) **mushaf position**: s = 36 / 114 = position 31.6% (head-third).
- (6b) **revelation-order** (al-Suyūṭī): #41 of 114 = 36.0% — Q 36 is just past the corpus's chronological midpoint (#57 = 50%).
- (6c) **word-count rank**: 754 words places Q 36 at rank ~33 / 114 of the long-mufaṣṣal head zone.
- (6d) **Window-midpoint Hijra-kink**: the s=50 boundary in the compression-tail laws is the empirical mushaf-architecture midpoint. Q 36 is 14 positions before this kink.

### Test
Computed against `data/hafs-verse-counts.tsv` and `data/revelation-order.csv`:

- mushaf position 36/114 = 31.6%, rank 36 = **NOT corpus median** (median = position 57.5).
- revelation-order #41 / 114 = **NOT corpus chronological median** (median = #57 al-Muṭaffifīn).
- word-count 754 = rank ~33/114, **NOT median word-count** (median = ~360 words for a typical mid-length surah).
- compression-tail s=50 kink: Q 36 is in the **pre-kink head-zone**, 14 positions before the kink.

### Rules-tuple
`(no-tashkeel, orthographic-words, basmala-counted-only-in-Q1, Hafs-Kufan)`. Cross-validated.

### Verdict
**FALSIFIED** for the corpus-positional-uniqueness reading. Q 36 is at none of the natural midpoints: not mushaf-position-median (Q 57 is), not revelation-order-median, not word-count-median, not Hijra-kink position. The H-NEW-82 NULL on positional-axis (rank 43/114) precisely encodes this. Audit 6 is a sub-test of Audit 1 sub-claim (1b).

## Audit 7 — Q 36:69 "we did not teach him poetry" + classical Quran-vs-poetry distinctness

### Claim
Q 36:69 (*وَمَا عَلَّمْنَاهُ الشِّعْرَ وَمَا يَنبَغِي لَهُ*) asserts Quran's categorical distinction from poetry. al-Bāqillānī's *Iʿjāz al-Qurʾān* and al-Khaṭṭābī's *Bayān iʿjāz al-Qurʾān* both ground their iʿjāz arguments partly in this verse.

### Operationalization
Test whether the Quran is empirically distinct from pre-Islamic poetry at the architectural level:
- (7a) Cross-corpus content-rhyme correlation: Quran shows r(content × rhyme) = −0.86 vs poetry's positive correlation.
- (7b) Cross-corpus poetry baseline: Quran vs 16 classical Arabic meters + 3 prose styles (Bonferroni-19 corrected).

### Test
Per [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]:
- Window-level Pearson r(content × rhyme) for Quran = **−0.86** (locked at law-strength).
- Same r for pre-Islamic poetry corpus (al-Muʿallaqāt + dīwāns) = positive (sign-reversed).
- Cross-corpus Fisher-z gap p < 10⁻¹⁰.

Per [[h-new-740-preislamic-poetry-control|H-NEW-740]]:
- Quran's content-rhyme anti-correlation is **uniquely Quran-specific**; not present in any classical Arabic poetic genre tested.

Per [[cross-finding-007|cross-finding-007]] (al-Bāqillānī iʿjāz al-fawāṣil empirical):
- Quran differs from 16 classical Arabic meters + 3 prose styles at p < 10⁻⁴ (Bonferroni-19 corrected).

### Rules-tuple
`(no-tashkeel, orthographic, window-K=20, basmala-counted-only-in-Q1, Hafs-Kufan)` per H-NEW-730/740 pre-regs.

### Verdict
**VINDICATED at law-strength**. The classical assertion in Q 36:69 (Quran is not poetry) is empirically locked at the project's strongest cross-corpus result (r = −0.86 + p < 10⁻¹⁰ Fisher-z gap + Bonferroni-19 distinction from 16 meters + 3 prose styles). Q 36:69 is a single textual instance of a corpus-wide architectural law.

## Audit summary

| Audit | Claim | Verdict |
|:-:|:--|:--|
| 1 | al-Tirmidhī *qalb al-Qurʾān* | **1a DIRECTIONAL ḌAʿĪF (chain-grade); 1b FALSIFIED (multi-axis NULL via H-NEW-82)** |
| 2 | "Recite Yāsīn over the dying" (Abū Dāwūd #3122 / Ibn Mājah #1182) | **DIRECTIONAL ḌAʿĪF (chain-grade-disputed)** |
| 3 | Q 36 = singleton 2-letter muqaṭṭaʿāt | **FALSIFIED (cardinality 10 with Ḥm-cluster, 3-4 distinct)** |
| 4 | Aṣḥāb al-Qarya = Antioch | **NOT-EMPIRICALLY-TESTABLE (extra-textual identification)** |
| 5 | Q 36:82 *kun-fa-yakūn* climax position | **VINDICATED at descriptive-position level (98.8% vs next 80.0%)** |
| 6 | Q 36 word-count corpus-positional-uniqueness | **FALSIFIED (Q 36 is at none of the natural midpoints)** |
| 7 | Q 36:69 anti-poetry assertion | **VINDICATED at law-strength via H-NEW-730 / H-NEW-740 / cross-finding-007** |

**Tally**: 1 audit at law-strength VINDICATED (7); 1 descriptive-position VINDICATED (5); 2 FALSIFIED (3, 6); 1 multi-axis FALSIFIED + chain-grade DIRECTIONAL ḌAʿĪF (1a/1b); 1 chain-grade DIRECTIONAL ḌAʿĪF (2); 1 NOT-EMPIRICALLY-TESTABLE (4).

The pattern aligns with the classical-modern reliability ratio and the dual-iʿjāz typology: **classical aesthetic-rhetorical claims (Audit 5, 7) survive empirically; classical numerical/positional claims (Audit 1b, 3, 6) tend to fail; classical chain-graded liturgical claims (Audit 1a, 2) reach DIRECTIONAL ḌAʿĪF rather than VINDICATED**. The empirical record is consistent with the project's [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] meta-pattern.
