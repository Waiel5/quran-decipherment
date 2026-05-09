---
surah: 72
surah_name_ar: الجن
surah_name_translit: al-Jinn
surah_name_en: "The Jinn"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: "Meccan #40 of revelation (al-Suyūṭī), Nöldeke #62 middle-Meccan; 28 verses; opens with the unique *qul ūḥiya ilayya annahu istamaʿa nafarun mina al-jinn* — one of 5 *qul*-opener surahs in the corpus {Q 72, 109, 112, 113, 114}; named for and corpus-rank-1 in jinn-being lemma density (per Q072-F-02)."
---

# Q 72 al-Jinn — Overview

## 1. Identification

| Field | Value |
|:--|:--|
| Surah number (mushaf order) | 72 |
| Name (Arabic) | الجن |
| Transliteration | al-Jinn |
| English meaning | "The Jinn" |
| Alternate name (al-Biqāʿī) | *qul ūḥiya* — the surah is also titled by its opening incipit (al-Biqāʿī *Naẓm al-Durar* §Q72: «وتسمى قل أوحى») |
| Verse count (Hafs-Kufan) | 28 |
| Type | Meccan |
| Position in revelation order (al-Suyūṭī) | 40 |
| Position in Nöldeke chronology | 62 (Middle Meccan) |
| Source for chronology | `data/revelation-order.csv` line for surah 72 |

## 2. Opening formula

The surah opens with the unique imperative-+-passive-revelation incipit:

> **قل أوحي إلي أنه استمع نفر من الجن فقالوا إنا سمعنا قرآنا عجبا**
> "Say: it has been revealed to me that a *nafar* of the jinn listened, and they said: 'We have heard a marvellous *qurʾān*'" (Q 72:1).

The opener pattern *qul ūḥiya ilayya* + reported-speech-of-the-jinn is a corpus-singleton. Q 72 is one of **five** surahs in the corpus whose entire first verse (verse-1, word-1) is the imperative *qul*: {Q 72, Q 109 al-Kāfirūn, Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās} — the **5-qul cluster** (per H-NEW-74; cross-finding-008). Of these, only Q 72 is the EXTENDED *qul* (full reported-speech phrase); the other four are the SHORT-CREEDAL *qul* + immediate predication (*qul huwa Allāhu aḥad*, *qul aʿūdhu bi-rabbi al-falaq*, etc.). See `06-novel-findings.md` Q072-F-01 for the FR-cohesion replication of the 5-qul cluster (PASS-STRONG at p=0.0026).

## 3. Basmala

Standard basmala precedes the surah (counted at mushaf-position only as a separator, per the project's rules-tuple: basmala counted only at Q 1).

## 4. Length and rhyme

| Metric | Value | Source |
|:--|:--|:--|
| Verse count | 28 | Hafs-Kufan via `data/hafs-verse-counts.tsv` |
| Word count (no-tashkeel) | 293 | computed from `quran-text/quran-no-tashkeel.json` |
| Character count | 1,529 | computed from `quran-text/quran-no-tashkeel.json` |
| Predominant rāwī (rhyme letter) | ا (alif) | per h-new-750: top_final_letter=ا at 100% of verses |
| Rhyme entropy (nats) | **0.0** | h-new-750 (every single verse-final rhymes to alif — corpus-extreme low entropy) |

The 100% alif-rhyme is a **corpus-extreme**: Q 72 ties the lowest-rhyme-entropy surahs in the corpus (alongside Q 55 *al-Raḥmān* whose famous refrain *fa-bi-ayyi ālāʾi rabbi-kumā tukadhdhibān* drives a similar single-rhyme dominance). See `01-empirical-profile.md` §3.

## 5. Length-classification

- **al-Suyūṭī taxonomy**: Q 72 sits in the **al-mufaṣṣal al-awsāṭ** tier — specifically the middle-mufaṣṣal block surahs that begin roughly at al-Buruj and run through al-Bayyina (al-Itqān, naw'a 1.4 on mufaṣṣal subdivision). 28 verses, ~293 words places Q 72 in the middle-length mufaṣṣal stratum, longer than the short-Meccan creedal tail (Q 100-114) but shorter than the long-Meccan narrative blocks (Q 19-39).
- **Project length-bin**: middle-mufaṣṣal awsāṭ (positions 67-77 plus 78-89 cluster).

## 6. Thematic blocks

Q 72 falls into TWO clean thematic blocks:

| Block | Verses | Content register | Diagnostic |
|:--|:--|:--|:--|
| **A — Jinn-confession** | 1-19 | reported-speech monotheistic creed from the jinn | 19 of 28 verses; opens with *qul ūḥiya*; verses 2-15 are jinn first-person plural quotation; verse 19 closes the reported-speech with the third-person observation about Muḥammad's standing-to-pray |
| **B — Prophet-cycle / eschatological** | 20-28 | prophet's first-person statement of his bounded prophetic role; eschatology of the unseen; closing statement on God's compass | 9 of 28 verses; verses 20, 21, 22, 25 each open with a fresh *qul*, marking the addressee-shift from "the jinn say" to "the prophet says" |

The block-boundary at v.19/v.20 is sharp and is reinforced by the *qul* repetition in v.20-25 (4 prophet-mode *qul* incipits within 6 verses). See `02-content-analysis.md` for verse-by-verse analysis.

## 7. Position in the mushaf

Q 72 sits at the canonical seam **Q 71 Nūḥ → Q 72 al-Jinn → Q 73 al-Muzzammil**. Both neighbours are Meccan; both are short-to-middle-length. The Q 71-72 transition is short-Meccan-narrative-of-prophet-rejection to short-Meccan-reported-speech-of-jinn-acceptance — a deliberate al-Biqāʿī-style contrast (the jinn accept what Nūḥ's people reject; al-Biqāʿī §Q72 op.). Per h-new-720, the Q 71→72 adjacency residual is Δ = 0.041 (modest — not in the top-10 expensive seams) and the Q 72→73 adjacency residual is Δ = 0.00 (zero excess TSP cost, a CHEAP canonical seam: the mushaf order matches the FR-locally-optimal order at this junction).

## 8. Headline findings (forward references)

Three pre-registered novel tests landed for Q 72:

| Test | Verdict | Headline |
|:--|:--|:--|
| **Q072-F-01** | **PASS-STRONG** (p=0.0026, predicted p<0.01) | 5-qul cluster {Q 72, 109, 112, 113, 114} FR-cohesion REPLICATED with MW-5 PC pass (independent seed 20260509) |
| **Q072-F-02** | **PASS** (rank 1/114) | Q 72 is corpus-rank-1 in strict LEM:jin~ density (10.24 per 1k tokens, 3.2× margin over Q 34 rank-2 at 3.19/1k) |
| **Q072-F-03** | **PASS** (p=0.0068, z=+2.81) | Q 72:1-19 ↔ Q 46:29-32 jinn-pericope-pair lexical Jaccard exceeds length-matched corpus null at α=0.05 |

Family-level Bonferroni-k = 3, α_bon = 0.0167. F-01 and F-03 both survive Bonferroni; F-02 is a corpus-rank-deterministic test (no permutation).

## 9. Cross-references

- `01-empirical-profile.md` — full H-NEW metric integration
- `02-content-analysis.md` — verse-by-verse block analysis
- `03-tafsir-survey.md` — al-Biqāʿī + al-Rāzī + al-Suyūṭī + Ibn Kathīr + al-Ṭabarī on Q 72
- `04-hadith-corpus.md` — Bukhārī 755 + 4713; Muslim 908; Tirmidhī 3342, 3407
- `05-classical-claims-audit.md` — al-Biqāʿī Q 71→Q 72 munāsabah audit; *qul*-opener cluster classical readings
- `06-novel-findings.md` — Q072-F-01/02/03 full write-ups
- `07-cross-references.md` — 5-qul cluster, H-NEW-1080 short-Medinan-block contrast, jinn-pericope cross-references to Q 46
- `JOURNAL.md` — investigation log
