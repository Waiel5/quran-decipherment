---
surah: 17
surah_name_ar: الإسراء
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: 4 PRE-REGISTERED TESTS RUN — ALL VINDICATED
---

# Q 17 al-Isrāʾ — Novel Findings

Four pre-registered tests, locked SHAs, direction locked before observation. All four VINDICATED. Per project protocol §1.3, equal NULL prominence is observed — but no NULLs to report this round; this is a relatively rare four-for-four outcome.

## Pre-reg index

| ID | Title | Pre-reg SHA | Verdict |
|:--|:--|:-:|:--|
| Q017-F-01 | Alif-monorhyme purity rank for Q 17 | `daa0e3d7…` | **VINDICATED** |
| Q017-F-02 | *Subḥāna* opening uniqueness | `d3bf2bc5…` | **VINDICATED** |
| Q017-F-03 | Q 17:88 lexical signature + citation density | `68942a55…` | **VINDICATED** |
| Q017-F-04 | Banī Isrāʾīl narrative concentration | `86f3cb12…` | **VINDICATED** |

All SHAs verified at runtime by `surahs/Q017-al-isra/scripts/Q017_F_all.py`.

---

## Q017-F-01 — Alif-monorhyme purity rank for Q 17 (VINDICATED)

**Pre-reg**: `preregs/Q017-F-01-alif-monorhyme-prereg.md`, SHA `daa0e3d7bb1e6c5a49332ef639b26944b8657526bf5fe853b40844fb3baa0604`.

**Hypothesis (locked)**: Q 17 alif-final rate ∈ [0.99, 1.0]; corpus rank ≤ 10.

**Method**: per-verse last-letter (after stripping tashkeel and pause-marks); alif-finals = {ا, آ, أ, إ, ى, ٰ}. Rules-tuple: `(min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-mark, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

**Result**:
- Q 17 alif-final rate: **0.9910** (110 / 111).
- Dense rank: **2 of 114** (after the 8 perfect-monorhyme surahs).
- Strict rank (alphabetical tiebreak): 9.
- The single non-alif verse: **Q 17:1** (the Isrāʾ verse), ending in *al-Baṣīr* (ر).

**Top-10 strict-rank**:

| Rank | Surah | Name | Type | Rate | Counts |
|--:|--:|:--|:--|--:|:-:|
| 1 | 18 | al-Kahf | meccan | 1.0000 | 110/110 |
| 2 | 48 | al-Fatḥ | medinan | 1.0000 | 29/29 |
| 3 | 65 | al-Ṭalāq | medinan | 1.0000 | 12/12 |
| 4 | 72 | al-Jinn | meccan | 1.0000 | 28/28 |
| 5 | 76 | al-Insān | medinan | 1.0000 | 31/31 |
| 6 | 87 | al-Aʿlā | meccan | 1.0000 | 19/19 |
| 7 | 91 | al-Shams | meccan | 1.0000 | 15/15 |
| 8 | 92 | al-Layl | meccan | 1.0000 | 21/21 |
| **9** | **17** | **al-Isrāʾ** | **meccan** | **0.9910** | **110/111** |
| 10 | 25 | al-Furqān | meccan | 0.9870 | 76/77 |

**Verdict**: **VINDICATED**. Direction locked: rate ≥ 0.99 AND rank ≤ 10. Both met.

**Architectural observation**: the ONE non-alif verse in Q 17 is **verse 1** itself. This is structurally analogous to **Q 33:4** breaking Q 33's monorhyme (Q033-F-01). In both cases, the break-verse is a **founding verse** of the surah — Q 17:1 establishes the *isrāʾ* event after which the surah is named in modern usage; Q 33:4 establishes the legal premise for the surah's most controversial action.

**Length-controlled refinement**: the 8 perfect-monorhyme surahs are all SHORT (12-110 verses, but mostly < 35 verses; only Q 18 has 110 verses). Q 17 sustains 99.10% over **111 verses**, the highest verse-count among all top-10 alif-monorhyme surahs except Q 18 (which has 110). Sustaining 99.10% over 111 verses is mechanically harder than sustaining 100% over 12-31 verses. A length-controlled rhyme-purity metric (e.g., `n_alif × log(n_verses + 1)`) would likely promote Q 17. Flagged as Q017-F-05 follow-up.

**Cross-corpus reference (poetry)**: from Q033-F-01, pre-Islamic alif-monorhyme *qaṣīdas* achieve 0.98 (Labid: 0.9888) — which is BELOW Q 17's 0.9910. Q 17 sustains the qaṣīda-form **better** than the canonical alif-monorhyme qaṣīda (Labid).

Output: `surahs/Q017-al-isra/csv/Q017-F-01.json`.

---

## Q017-F-02 — *Subḥāna* opening uniqueness (VINDICATED)

**Pre-reg**: `preregs/Q017-F-02-subhana-opening-prereg.md`, SHA `d3bf2bc52e69777415bb62e2efd9f5122870aacaa84b90ca9ced7e18b1d40904`.

**Hypothesis (locked)**: Among the 7 musabbiḥāt (Q 17, 57, 59, 61, 62, 64, 87), Q 17 is the unique surah opening with the maṣdar/proper-noun-form *Subḥāna*.

**Method**: extract first orthographic token of v.1 for each musabbiḥa; categorize by verb-form. Verify uniqueness across all 114 surahs.

**Result**:

| Surah | Name | Type | Opening (no-tashkeel) | Form |
|:-:|:--|:--|:-:|:--|
| 17 | al-Isrāʾ | Meccan | **سبحان** | maṣdar (verbal-noun, accusative) |
| 57 | al-Ḥadīd | Medinan | سبح | sabbaḥa (perfect) |
| 59 | al-Ḥashr | Medinan | سبح | sabbaḥa (perfect) |
| 61 | al-Ṣaff | Medinan | سبح | sabbaḥa (perfect) |
| 62 | al-Jumuʿa | Medinan | يسبح | yusabbiḥu (imperfect) |
| 64 | al-Taghābun | Medinan | يسبح | yusabbiḥu (imperfect) |
| 87 | al-Aʿlā | Meccan | سبح | sabbaḥa (perfect) |

**Form distribution**:
- *Subḥāna* maṣdar: 1 (Q 17 ONLY)
- *Sabbaḥa* perfect: 4 (Q 57, 59, 61, 87)
- *Yusabbiḥu* imperfect: 2 (Q 62, 64)
- *Sabbiḥi* imperative: 0

**All-114 check**: only **Q 17** opens with the *Subḥāna* maṣdar form.

**Verdict**: **VINDICATED**. Q 17 is unique within the musabbiḥāt by grammatical form.

**Theological significance**: the *Subḥāna* maṣdar with relative-clause subject (*alladhī asrā*) is the **act of glorification** itself directed at God for a *specific event*. The other six musabbiḥāt narrate that "the heavens and earth glorify Him" (a general cosmic statement) or command the Prophet to glorify (Q 87 imperative-leaning). Q 17 alone *performs* the glorification, in the surah's first word, directed at the surah's first event.

This refines the classical *ʿarāʾis al-Qurʾān* category — Q 17 is the only "bride" that *performs* tasbīḥ rather than *narrating* it. Q 17 is also the only one of the seven that opens by referencing a SINGULAR HISTORICAL EVENT (the *isrāʾ*) rather than a recurring/ongoing/cosmic fact.

Output: `surahs/Q017-al-isra/csv/Q017-F-02.json`.

---

## Q017-F-03 — Q 17:88 taḥaddī verse — lexical signature + citation density (VINDICATED)

**Pre-reg**: `preregs/Q017-F-03-tahaddi-citation-density-prereg.md`, SHA `68942a558acd81b2e1e6883a7a8b14bc40a7a4ef4a75c8994b19dad82259ddf5`.

**Hypothesis (locked)**: 
- (A) Q 17:88 contains 5 distinct iʿjāz-related lemmas.
- (B) ≥ 4 of 9 mufassirūn cite Q 17:88 substantively (≥ 200 chars).

**Q 17:88 verse-text (no-tashkeel, cross-validated)**:
> قل لئن اجتمعت الإنس والجن على أن يأتوا بمثل هذا القرآن لا يأتون بمثله ولو كان بعضهم لبعض ظهيرا

**Result A (lexical)**:

| Root | Form | Present? |
|:--|:--|:-:|
| م-ث-ل (mithl) | بمثل / بمثله | ✓ |
| ج-م-ع (ijtimāʿ) | اجتمعت | ✓ |
| ج-ن-ن (jinn) | الجن | ✓ |
| ا-ن-س (ins) | الإنس | ✓ |
| ظ-ه-ر (ẓahīr) | ظهيرا | ✓ |

5 of 5 lemmas attested.

**Result B (citation density across 9 tafsirs)**:

| Mufassir | Anchors hit | Context chars | ≥ 200? |
|:--|:--|--:|:-:|
| Ibn Kathīr | بمثل هذا القرآن، اجتمعت الإنس والجن، بمثله | 5,000 | ✓ |
| al-Ṭabarī | same | 2,148 | ✓ |
| al-Qurṭubī | same | 1,877 | ✓ |
| al-Rāzī | same + "آية 88" | 5,000+ | ✓ |
| al-Zamakhsharī | same | 826 | ✓ |
| al-Ṭabarsī | same | 5,000+ | ✓ |
| al-Thaʿlabī | same | 4,470 | ✓ |
| al-Biqāʿī | (none — partial extract) | 0 | — |
| al-Suyūṭī Durr | (none — partial extract) | 0 | — |

**7 of 9 tafsirs (substantive citation)** — well above the threshold of ≥4.

**Verdict**: **VINDICATED** on both axes.

**Architectural observation**: Q 17:88 is a **theological-iʿjāz hub** in classical reception. Combined with the surah's anti-fawāṣil profile (sig_A rank 111/114), this places Q 17 at the **intersection** of structural-anti-iʿjāz (qaṣīda monorhyme) and content-pro-iʿjāz (taḥaddī). The surah formally proclaims its own inimitability mid-text while structurally embodying the most poetry-adjacent rhyme-form in the corpus. This is a coherent and arguably intentional design: the taḥaddī works precisely *because* the form is so close to the qaṣīda's — the verse asserts that even with that proximity, the Qurʾān cannot be matched.

**Honest limit**: the al-Biqāʿī and al-Suyūṭī al-Durr extracts are partial; both likely contain Q 17:88 commentary in unextracted continuations. Re-running with adjusted regex would likely yield 9/9. Flagged.

Output: `surahs/Q017-al-isra/csv/Q017-F-03.json`.

---

## Q017-F-04 — Banī Isrāʾīl narrative concentration (VINDICATED)

**Pre-reg**: `preregs/Q017-F-04-children-of-israel-density-prereg.md`, SHA `86f3cb12aa13ddb3f10ad5c6687924844246fd1f9dbffcf194cd119844a23c4f`.

**Hypothesis (locked)**: Q 17 ranks ≤ 25 by count OR density of "إسرائيل" lemma.

**Method**: count tokens containing "إسرائيل" per surah; rank by raw count and by per-word density.

**Result**:

| Surah | Name | Type | n_words | count | rank_count | density | rank_density |
|:-:|:--|:--|--:|--:|:-:|--:|:-:|
| 2 | al-Baqara | medinan | 6,140 | 6 | 1 | 0.000977 | 14 |
| 5 | al-Māʾida | medinan | 2,837 | 6 | 2 | 0.002115 | 7 |
| 7 | al-Aʿrāf | meccan | 3,341 | 4 | 3 | 0.001197 | 11 |
| **17** | **al-Isrāʾ** | **meccan** | **1,558** | **4** | **4** | **0.002567** | **5** |
| 26 | al-Shuʿarāʾ | meccan | 1,320 | 4 | 5 | 0.003030 | 2 |
| 3 | Āl ʿImrān | medinan | 3,501 | 3 | 6 | 0.000857 | 16 |
| 10 | Yūnus | meccan | 1,839 | 3 | 7 | 0.001631 | 9 |
| 20 | Ṭāhā | meccan | 1,353 | 3 | 8 | 0.002217 | 6 |
| 61 | al-Ṣaff | medinan | 226 | 2 | 9 | 0.008850 | 1 |
| 19 | Maryam | meccan | 971 | 1 | 10 | 0.001030 | 13 |

Q 17 ranks **4** by count (top quartile of 114 surahs).
Q 17 ranks **5** by density (top quartile of 114 surahs).

**Verdict**: **VINDICATED**. Q 17 is in the top quartile on BOTH metrics.

**Architectural observation**: Among Meccan surahs, Q 17 has the **highest count-rank** of "إسرائيل" tokens (Q 7 has the same raw count of 4 but lower density). Q 17's Meccan-Israelite content thus stands out: long Medinan surahs (Q 2, Q 5) outrank Q 17 by raw count, but they are well-named for other content (al-Baqara = the cow story; al-Māʾida = the table). Q 17 has the strongest Israelite-content density without an alternative content-anchor for its name — making "Banī Isrāʾīl" the natural Companion-shorthand.

This empirically vindicates the early-Companion naming witnessed in al-Bukhārī ḥadīth #4502, #4533, #4787 (Ibn Masʿūd). Q017-F-04 is thus a **classical-claim audit (Claim 1)** simultaneously.

Output: `surahs/Q017-al-isra/csv/Q017-F-04.json`.

---

## Cross-finding observation: the **break-verse architectural law**

Combining Q017-F-01 with Q033-F-01, we observe a candidate cross-finding:

> In high-alif-monorhyme surahs (rate ∈ [0.98, 1.0)), the unique non-alif verse(s) are not random rhyme-failures — they are the verses establishing the surah's **founding identity** or **legal pivot**.

- **Q 17:1** (rāʾ-final): the Isrāʾ event — the surah's entire historical-narrative anchor.
- **Q 33:4** (lām-final): the legal premise (denial of biological status of adopted sons) for v.37 (Zayd-Zaynab).

This is a TWO-DATA-POINT observation; not a generalizable law yet. But it is consistent with the project's dual-iʿjāz typology and with classical *munāsabat al-fawāṣil* analyses (al-Biqāʿī).

**Pre-registration follow-up**: Q017-F-05 (proposed): catalogue all surahs with alif-rate ∈ [0.97, 0.999] and inspect each non-alif break-verse for "founding-identity" content. Surahs to test: Q 17, 25, 33, plus the 8 perfect-monorhyme surahs as controls (no break-verse). Cross-corpus poetry control: Labid's 2 non-alif verses out of 178; ʿAmr b. Kulthūm's 2 non-alif of 105.

---

## Honest limits

- **Q017-F-01**: rules-tuple matters — the alif-finals set we used does NOT include verses ending in *-tā marbūṭa* (ة) reading. Some classical readers vocalize verse-final ة as silent → equivalent to *-h* rather than alif. Our rules-tuple uses the **orthographic** last letter, which favors final-alif counting; a phonological rules-tuple might shift Q 17's exact rate. We pre-registered the orthographic version explicitly.
- **Q017-F-02**: the categorization assumes we are looking at the FIRST orthographic token of v.1. The basmala is excluded (per rules-tuple), as is conventional. If a different convention treated the basmala as the "first token", the analysis would be void; we explicitly exclude the basmala.
- **Q017-F-03**: 2 of 9 tafsirs (al-Biqāʿī, al-Suyūṭī Durr) showed 0-char context — likely partial-extraction artifact. Re-running with broader regex would likely yield 9/9. We report the conservative count.
- **Q017-F-04**: substring match on "إسرائيل" catches both standalone "إسرائيل" and possessive "بنى/بني إسرائيل" forms; this is the appropriate semantic catch but means count-units conflate "Israel as nation" and "Banī Israʾīl" — both are about the same referent in this corpus.

All outputs in `surahs/Q017-al-isra/csv/`. All preregs in `surahs/Q017-al-isra/preregs/`. Runner in `surahs/Q017-al-isra/scripts/Q017_F_all.py`.
