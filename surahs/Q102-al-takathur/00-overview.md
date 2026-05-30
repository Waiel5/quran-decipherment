---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
surah_name_english: "Rivalry in Worldly Increase / The Piling-Up"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered 2-arm test landed — Arm A CONFIRMED (corpus-unique triple-kallā run) + Arm B DIRECTIONAL (bare-threat singleton ✓, thumma-refrain exclusivity REVERSED → 3-member family)
---

# Q 102 al-Takāthur — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 102 | canonical |
| Arabic name | التكاثر | canonical (verbal-noun *takāthur*, form-III "mutual multiplying/vying-in-increase"; from v 1) |
| Transliteration | al-Takāthur | canonical |
| English meaning | "Rivalry in worldly increase / Vying for more / The Piling-Up" | classical |
| Verse count | 8 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 102: "102	8") |
| Position in mushaf | 102 | canonical |
| Revelation order | #16 (Tanzil Egyptian Standard); "Early Meccan" | `data/revelation-order.csv` (row: `16,102,التكاثر,At-Takathur,Meccan,8,Early Meccan`) |
| Type | Meccan ("مكية" by the standard tradition; see §7) | `quran-text/quran-no-tashkeel.json` (type=meccan); al-Ṭabarī, al-Qurṭubī |
| Word count (no-tashkeel, marks stripped) | 28 | computed (`scripts/Q102_F_01_kalla_reduplication.py` pipeline) |
| Letter count (no-tashkeel, no spaces) | 123 | computed |
| Distinct QAC roots | 11 | `data/morphology/root-index.json` (lhw, kvr, zwr, qbr, Elm, yqn, rAy, jHm, Eyn, sAl, nEm) |
| Opening | أَلْهَاكُمُ التَّكَاثُرُ — "Rivalry in increase distracts you" | direct address (2nd-person plural rebuke) |
| Predominant rhyme (rāwī) | ن (nūn), 4/8 verses (50%) — the *-ūn / -īn / -īm* tail (taʿlamūn ×2, yaqīn ×2, jaḥīm, naʿīm) | `h-new-700.json` rhyme_letter_diagnostics; `h-new-750.json` |
| Length class | mufaṣṣal-qiṣār (short mufaṣṣal; juzʾ 30) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 102 matters for the project

1. **Corpus-UNIQUE rebuke-*kallā* triple-run (Q102-F-01 Arm A, CONFIRMED).** Q 102 is the ONLY surah
   in the corpus with a run of **three consecutive verses** (vv 3, 4, 5) each opening with a genuine
   rebuke-*kallā* (QAC POS:AVR, LEM `kal~aA`). Every other surah's longest consecutive-*kallā* run is
   ≤ 2 (Q 74:53-54, Q 78:4-5, Q 83:14-15). This is a deterministic structural singleton that anchors
   the corpus *kallā* census (33 rebuke-tokens, homograph-clean, none in Q 1–18) to a per-surah extreme.

2. **The *kallā* census vindication (H-NEW-2160 / H-NEW-2230 / §10.80).** Q 102 carries **3 of the 33**
   genuine rebuke-*kallā*, replicated here at QAC-lemma level. The classical claim (al-Suyūṭī *Itqān*
   nawʿ 40 ← al-Dānī: 33 *kallā*, mufaṣṣal-concentrated) is re-confirmed; the task-brief's working
   figure of "×2 *kallā*" is **corrected to 3** by the morphological ground-truth.

3. **A *thumma*-doubled threat-refrain family (Q102-F-01 Arm B, DIRECTIONAL).** The adjacent pair
   `kallā sawfa taʿlamūn` (v 3) → `thumma kallā sawfa taʿlamūn` (v 4) — verbatim plus a single prefixed
   *thumma* — is NOT corpus-exclusive (pre-commit violation on B-H1): it is one of exactly **three**
   such single-particle adjacent threat-doublings, alongside Q 75:34-35 (*awlā laka fa-awlā* → *thumma*
   …) and Q 78:4-5 (*kallā sa-yaʿlamūn* → *thumma* …). Q 102 and Q 78 are a 2nd/3rd-person minimal pair
   (*sawfa taʿlamūn* "you will know" vs *sa-yaʿlamūn* "they will know"). The **bare-threat sub-claim
   (B-H2) PASSES**: *kallā sawfa taʿlamūn* standing alone as a whole rebuke-verse is corpus-exclusive to
   Q 102:3-4.

4. **al-Ṭabarī's own balāgha rationale for the doubling.** al-Ṭabarī (*Jāmiʿ al-bayān*, on v 4):
   *"karrara qawlahu marratayn, li-anna al-ʿArab idhā arādat al-taghlīẓ fī al-takhwīf wa-l-tahdīd
   karrarū al-kalimata marratayn"* — the Arabs double a word to intensify a threat. The empirical
   *thumma*-refrain family is the cross-corpus correlate of this stated device.

5. **FR-content twin of its own title-root rank-1 surah.** Q 102's nearest Fisher-Rao neighbor is
   **Q 108 al-Kawthar (FR 0.2937)** — which is *also* the corpus rank-1 surah in Q 102's title-root
   (kvr, per-word density; H-NEW-1820). The title-root-density-#1 surah and the content-nearest surah
   coincide. Q 102 itself is rank-2 in its own title-root by per-word density (H-NEW-1820 VINDICATED;
   §05 audit).

6. **Deep compression-tail / short-mufaṣṣal anchor.** Q 102's FR mean to the other 113 surahs is
   **0.8011** (well below corpus mean 0.9235; H-NEW-750 z = −1.21) and its iʿjāz **sig_B rank is 4/114**
   (top-4 corpus-wide) — a high-local-cohesion, low-content-dispersion short surah, exactly the profile
   of the dense juzʾ-30 rebuke-cluster.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.8011 | `h-new-111.json` (Q102 row) |
| Nearest FR neighbor | **Q 108 al-Kawthar** (FR 0.2937) | `h-new-111.json` |
| Top-5 FR neighbors | Q 108, 107, 106, 111, 103 | `h-new-111.json` |
| Q 101 (prev surah) rank in Q 102's FR list | 13/113 (FR 0.3863) | `h-new-111.json` |
| Q 101 → Q 102 seam | delta_raw = +0.02873, ascending-rank 30/113 | `h-new-720.json` |
| Q 102 → Q 103 seam | delta_raw = +0.04795, ascending-rank 44/113 | `h-new-720.json` |
| H-NEW-590 outlier | NOT a tested candidate (candidates = {1,9,18,55,62,112}) → DATA-GAP, treated as 0 in UAS | `h-new-590.json` |
| H-NEW-700 monorhyme | ن (nūn), 50.0% (4/8) | `h-new-700.json` |
| H-NEW-750 rhyme entropy | 1.0397 nats (z +0.49) | `h-new-750.json` |
| H-NEW-750 sig_A | +1.6963 (rank 12/114) | `h-new-750.json` |
| H-NEW-750 sig_B | +2.1914 (rank **4/114**, top-4) | `h-new-750.json` |
| H-NEW-750 local_cohesion | 2.769 (z +1.70) | `h-new-750.json` |
| H-NEW-840 UAS | −0.7412 (understated; abs_outlier=0 data-gap) | `h-new-840.json` |
| rebuke-*kallā* (POS:AVR) | 3 (vv 3,4,5) of corpus-33 | QAC v0.4 + `h-new-2230` |

## 4. Surface structure (8 verses, 2 thematic movements)

| Block | Verses | Function |
|---|---|---|
| The diagnosis: rivalry-in-increase distracts | 1-2 | *alhākum al-takāthur ḥattā zurtum al-maqābir* — the vying for "more" preoccupies you until you reach the graves (death / grave-counting) |
| The triple rebuke + escalating threat | 3-5 | *kallā sawfa taʿlamūn* / *thumma kallā sawfa taʿlamūn* / *kallā law taʿlamūna ʿilma al-yaqīn* — three *kallā*-rebukes, the first two a near-verbatim doubling, the third introducing *ʿilm al-yaqīn* |
| The vision of the Fire (certainty) | 6-7 | *latarawunna al-jaḥīm thumma latarawunnahā ʿayn al-yaqīn* — you will surely see Hell, then see it with the eye of certainty |
| The questioning about blessing | 8 | *thumma latusʾalunna yawmaʾidhin ʿan al-naʿīm* — then you will be questioned about *al-naʿīm* (the favours/delight) |

**The three certainties.** The surah builds a graded epistemology of the Hereafter through the *yaqīn*
chain: *ʿilm al-yaqīn* (knowledge of certainty, v 5) → *ʿayn al-yaqīn* (eye/sight of certainty, v 7) →
[*ḥaqq al-yaqīn*, the third grade, appears elsewhere at Q 56:95 and Q 69:51, NOT in Q 102]. al-Jalālayn,
al-Ṭabarī, al-Qurṭubī all treat the *ʿilm → ʿayn* progression as a deliberate intensification.

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q102-F-01 Arm A | **CONFIRMED** | Q 102 is the corpus-UNIQUE 3-consecutive-verse rebuke-*kallā* run (vv 3-4-5); others ≤ 2; census 33, homograph-clean |
| Q102-F-01 Arm B | **DIRECTIONAL (pre-commit violation on B-H1)** | bare *kallā sawfa taʿlamūn* threat is corpus-exclusive to Q 102:3-4 (B-H2 ✓), BUT the *thumma*-doubled adjacent refrain is a **3-member family** {Q 75:34-35, Q 78:4-5, Q 102:3-4}, not a Q 102 singleton |

## 6. Cross-references

- **H-NEW-2160 / H-NEW-2230 (§10.80)** — Q 102 carries 3 of the 33 rebuke-*kallā*; QAC-lemma replication.
- **H-NEW-2310** — refrain/reduplication axis; Q 102's *thumma*-doubling is a new supporting instance and
  surfaces a 3-member *thumma*-threat-refrain micro-family.
- **H-NEW-1820** — Q 102 rank-2 in title-root kvr (per-word density), rank-1 = Q 108 al-Kawthar (VINDICATED).
- **H-NEW-111** — Q 108 is Q 102's nearest FR neighbor (0.2937); the title-density-#1 surah = content-nearest.
- **H-NEW-750** — sig_B rank 4/114 (top-4); high local cohesion.
- **Q 78 al-Nabaʾ** — *kallā sa-yaʿlamūn* doubling (Q078-F-03); the 2nd/3rd-person minimal-pair twin of Q 102:3-4.
- **Q 101 al-Qāriʿa / Q 103 al-ʿAṣr** — mushaf neighbors; both mid-spectrum seams.

## 7. Classical-tradition status

- **al-Ṭabarī** (*Jāmiʿ al-bayān*): rivalry = boasting of wealth and numbers (Qatāda: tribes vying
  "we are more than Banū Fulān" until they all end in the graves); "visiting the graves" (v 2) = being
  buried, cited as **proof of grave-torment (ʿadhāb al-qabr)** via ʿAlī ("we used to doubt grave-torment
  until al-Takāthur was revealed"); the v3/v4 doubling is *takrīr li-l-taghlīẓ*; *qirāʾa* dispute on
  *latarawunna* (al-Kisāʾī).
- **al-Qurṭubī** (*al-Jāmiʿ li-aḥkām*): Meccan; two readings of "until you visit the graves" (death vs.
  literal grave-counting boast); the *al-naʿīm* dispute (security/health vs. cool water + shade + food).
- **Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿaẓīm*): the Ubayy b. Kaʿb "valley of gold" linkage (Bukhārī
  Riqāq); the "māl mālī" servant-hadith (Muslim, Tirmidhī, Nasāʾī); *al-naʿīm* = every favour to be
  accounted.
- **al-Jalālayn**: terse verse-by-verse — v 4 doubling = the moment of soul-extraction then the grave;
  *ʿayn al-yaqīn* = sight-certainty, *ʿayna* a verbal noun (ra'ā = ʿāyana).
- **al-Suyūṭī** (*al-Itqān*, nawʿ 40 ← al-Dānī): *kallā* count = 33, mufaṣṣal-concentrated (the
  census anchoring Q 102's 3 tokens).

## 8. Open questions / queued tests

- Q102-F-02 (queued): formalize the *thumma*-doubled threat-refrain family {Q 75, 78, 102} as a corpus
  cross-finding (is the *thumma*-particle the unique doubler, or do {و, ف} also produce adjacent twins?).
- Q102-F-03 (queued): the *yaqīn* chain — does the *ʿilm al-yaqīn → ʿayn al-yaqīn* intra-surah pair, with
  *ḥaqq al-yaqīn* withheld to Q 56/69, form a deliberate cross-surah 3-grade distribution?
- Q102-F-04 (queued): Q 102 ↔ Q 108 FR-twin + title-root-density coincidence — is the kvr root the
  binding lexical bridge, or is the proximity carried by the shared short-rebuke register?

---

*Investigation: Wave-N (2026-05-30) Q 102 al-Takāthur full deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified fadāʾil + asbāb chain.*
