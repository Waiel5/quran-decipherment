---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: cross-references
date_last_updated: 2026-05-30
phase: B+
verdict: neighbors, juzʾ-30 cluster, kvr title-twin, thumma-refrain family, yaqīn-chain mapped
---

# Q 102 al-Takāthur — Cross-References

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## 1. Neighboring surahs in the mushaf (`h-new-720.json`)

| Seam | delta_raw | ascending-rank | relationship |
|:--|:--|:--|:--|
| Q 101 al-Qāriʿa → Q 102 al-Takāthur | +0.02873 | 30 / 113 | low-mid cost; juzʾ-30 short-surah run |
| Q 102 al-Takāthur → Q 103 al-ʿAṣr | +0.04795 | 44 / 113 | mid-spectrum; both terse eschatological-rebuke |

Both bracketing seams are below-median-cost — Q 102 sits in a smooth stretch of the juzʾ-30 short-Meccan
run (Q 99-114). The forward seam Q 102→Q 103 (0.04795) is the value the UAS picks up as `max_cost`
(`01-empirical-profile.md` §6).

## 2. Fisher-Rao neighbors (`h-new-111.json`)

- **Nearest:** Q 108 al-Kawthar (0.2937), Q 107 al-Māʿūn (0.3208), Q 106 Quraysh (0.3388), Q 111 al-Masad
  (0.3396), Q 103 al-ʿAṣr (0.3448), Q 100 al-ʿĀdiyāt (0.3465), Q 105 al-Fīl (0.3476), Q 112 al-Ikhlāṣ (0.3490).
- **Mean FR to all 113:** 0.8011 (well below corpus mean 0.9235; z −1.21).
- **Q 101 al-Qāriʿa (prev surah):** rank 13/113 (FR 0.3863).
- **Farthest:** Q 3 (1.298), Q 4 (1.289), Q 9 (1.280), Q 6 (1.239), Q 2 (1.234) — the long Medinan/Meccan
  narrative-legal surahs.

Q 102's nearest FR neighbor **Q 108 al-Kawthar** is the key coincidence: Q 108 is *also* rank-1 in Q 102's
own title-root *kvr* by per-word density (H-NEW-1820, §4 below). The title-root-#1 surah = the content-nearest surah.

## 3. Cluster memberships

- **Juzʾ-30 short-Meccan cluster {Q 99-114}:** Q 102 is a deep in-block cohesion member (H-NEW-590
  descriptive NULL, delta_pct 0.0; window {99-105}). Its FR neighborhood is entirely within this cluster.
- **Top-4 local-cohesion surahs (H-NEW-750 sig_B):** Q 102's sig_B = +2.1914 ranks **4/114** — among the
  most internally self-cohesive surahs in the corpus (local_cohesion 2.769, z +1.70).
- ***thumma*-doubled adjacent threat-refrain micro-family {Q 75, Q 78, Q 102}** (Q102-F-01 Arm B; new):
  the three surahs sharing a single-*thumma*-particle adjacent verbatim threat-doubling.

## 4. Title-root *kvr* twin (`h-new-1820.json`)

**Q 102 ↔ Q 108 al-Kawthar.** Both eponymous in the root *kvr* (k-th-r). Q 102 (al-Takāthur) is
`title_density_rank` **2**; Q 108 (al-Kawthar) is `title_density_rank` **1** — Q 108 is the densest *kvr*
carrier. H-NEW-1820 (title-density independence pillar law) is VINDICATED: the eponymous Q 102 is NOT
rank-1 in its own title-root. The same *kvr* root also makes Q 108 Q 102's nearest FR neighbor (§2) — the
lexical-density bridge and the content-geometry bridge coincide.

## 5. The *thumma*-doubled threat-refrain family (Q102-F-01 Arm B)

**{Q 75:34-35, Q 78:4-5, Q 102:3-4}** — the three corpus single-particle (*thumma*) adjacent verbatim
threat-doublings:

| Pair | Base verse | Doubled verse |
|:--|:--|:--|
| Q 75:34-35 | *awlā laka fa-awlā* | *thumma awlā laka fa-awlā* |
| Q 78:4-5 | *kallā sa-yaʿlamūn* | *thumma kallā sa-yaʿlamūn* |
| **Q 102:3-4** | *kallā sawfa taʿlamūn* | *thumma kallā sawfa taʿlamūn* |

- **Q 102 ↔ Q 78** = 2nd/3rd-person minimal pair (*sawfa taʿlamūn* "you will know" vs *sa-yaʿlamūn* "they
  will know"), both *thumma*-doubled rebuke-*kallā* threats.
- Q 102's genuine singleton is the **bare-threat reduplication** (Q102-F-01 B-H2): only Q 102 strips the
  threat to *sawfa taʿlamūn* alone as a whole rebuke-verse, doubled.

## 6. The *yaqīn*-grade chain

| Grade | Locus |
|:--|:--|
| *ʿilm al-yaqīn* (knowledge-certainty) | **Q 102:5** |
| *ʿayn al-yaqīn* (eyesight-certainty) | **Q 102:7** |
| *ḥaqq al-yaqīn* (truth-certainty) | Q 56:95, Q 69:51 (NOT in Q 102) |

Q 102 holds the first two grades as a deliberate intra-surah pair; the third is cross-surah (queued as
Q102-F-03). al-Jalālayn reads *ʿayn al-yaqīn* as the direct-sight intensification of *ʿilm al-yaqīn*.

## 7. Content / occasion cross-references (ḥadīth — `04-hadith-corpus.md`)

- **Q 102 ↔ valley-of-gold (Bukhārī #6197/#6200/#6201, Kitāb al-Riqāq):** Ubayy b. Kaʿb — "we used to
  regard *[the valley-of-gold saying]* as Qurʾān until al-Takāthur was revealed." The surah is the
  prophetic replacement of that greed-admonition; the two sit adjacent in Bukhārī's Riqāq.
- **Q 102:1 ↔ "māl mālī" servant-ḥadīth** (Muslim #7236; Tirmidhī #2411, #3438; Nasāʾī #3621): the Prophet
  comments on v 1's reciting with "the son of Adam says my wealth, my wealth…".
- **Q 102:2 ↔ ʿadhāb al-qabr** (Tirmidhī #3439, *gharīb*; al-Ṭabarī on v 2): ʿAlī — "we doubted the
  punishment of the grave until al-Takāthur was revealed."

## 8. H-NEW links

| Finding | Link to Q 102 |
|:--|:--|
| [[h-new-111\|H-NEW-111]] | FR matrix row; nearest Q 108 (0.2937); juzʾ-30 cluster; mean 0.8011 |
| [[h-new-590\|H-NEW-590]] | outlier descriptive NULL (delta_pct 0.0); deep in-block cohesion member |
| [[h-new-700\|H-NEW-700]] | rhyme ن 50% (4/8); phoneme vector idx 101 [0,0.073,0.033,0.041] |
| [[h-new-720\|H-NEW-720]] | Q 101→Q 102 (rank 30) + Q 102→Q 103 (rank 44) seams |
| [[h-new-750\|H-NEW-750]] | sig_A +1.696 (rank 12); sig_B +2.191 (rank **4/114**, top-4); local_cohesion z +1.70 |
| [[h-new-840\|H-NEW-840]] | UAS −0.741 (rank 67/114); understated (abs_outlier=0) |
| [[h-new-1820\|H-NEW-1820]] | title-root *kvr* rank-2 (rank-1 = Q 108); title-density independence VINDICATED |
| [[h-new-2160\|H-NEW-2160]] / [[h-new-2230\|H-NEW-2230]] | rebuke-*kallā* census 33; Q 102 carries 3 (Q102-F-01 Arm A) |
| [[h-new-2310\|H-NEW-2310]] | refrain/reduplication axis; Q 102's *thumma*-doubling = new supporting instance + 3-member family |

## 9. Role in cross-finding syntheses

- **title-density independence pillar law:** Q 102 (rank-2 in own *kvr*) is a clean confirming case; the
  rank-1/nearest-FR coincidence with Q 108 is a candidate for a "title-root binds eponym to its density-#1"
  micro-pattern (queued Q102-F-04).
- **refrain / reduplication (H-NEW-2310):** the *thumma*-doubled adjacent threat-refrain family
  {Q 75, Q 78, Q 102} is a corpus-wide structure surfaced by Q102-F-01 Arm B — candidate for formal
  promotion (Q102-F-02).
- **rebuke-*kallā* census (H-NEW-2230 §10.80):** Q 102's corpus-unique 3-consecutive-*kallā* run is the
  per-surah deterministic extreme of the 33-token census.

---

*2026-05-30. All links to on-disk findings; FR/seam/UAS/title-density values cited to JSON artifacts in
`01-empirical-profile.md`.*
