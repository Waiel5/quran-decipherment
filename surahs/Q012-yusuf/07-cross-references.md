---
surah: 12
surah_name_ar: يوسف
surah_name_translit: Yūsuf
file_type: cross-references
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 12 Yūsuf — Cross-References


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Direct mushaf neighbours

### Q 11 Hūd → Q 12 Yūsuf (left seam)
- **TSP cost: 0.0354 length-units** ([[h-new-720-canonical-adjacency-cost|H-NEW-720]] pair [11,12]). One of the **cheapest** canonical adjacencies in the corpus.
- Same letter-family (ALR muqaṭṭaʿāt).
- Same prophet-narrative register (Q 11 has Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb sub-narratives).
- al-Biqāʿī's *munāsaba* between Q 11 and Q 12: empirical correlate is the **near-zero seam cost**. Strong local-*munāsaba*.
- Verse-twin signal: Q 11:120 *wa-kullan naquṣṣu ʿalayka min anbāʾi al-rusuli mā nuthabbitu bihi fuʾādaka* ("And we narrate to you the news of the messengers...") — directly anticipates Q 12:3 *naḥnu naquṣṣu ʿalayka aḥsana al-qaṣaṣ*. The narrative-frame phrase *naquṣṣu ʿalayka* is the **literal hand-off** from Q 11 to Q 12.

### Q 12 Yūsuf → Q 13 al-Raʿd (right seam)
- **TSP cost: 0.2158 length-units** (top-15 expensive in corpus). **Sharp register-shift.**
- Different letter-family (Q 13 opens with **ALMR**, not ALR).
- Different content register: Q 12 is single-protagonist narrative; Q 13 is doxological-cosmological + signs-of-creation.
- The mushaf accepts the high right-seam cost as the price of placing the continuous-narrative surah Q 12 in the prophet-narrative cluster (Q 10–11 ALR + Q 12 ALR). The canonical placement is content-driven, not seam-greedy.

## 2. Letter-family cluster (ALR)

ALR cluster: **Q 10, 11, 12, 14, 15** (Q 13 al-Raʿd is ALMR, not ALR — falls outside the cluster despite mushaf-adjacency).

| Surah | Name | Verses | Notes |
|:-:|:-:|:-:|:--|
| Q 10 | Yūnus | 109 | Multi-prophet narrative + theology; named after Jonah (ch 41 onward) |
| Q 11 | Hūd | 123 | Multi-prophet narrative (Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā cycles) |
| **Q 12** | **Yūsuf** | **111** | **Single-protagonist continuous narrative** |
| Q 14 | Ibrāhīm | 52 | Mixed: doxological + Ibrāhīm prayer + theology |
| Q 15 | al-Ḥijr | 99 | Multi-prophet vignette + Iblīs / human-creation theology |

**Per [[h-new-97]]**: 4/5 are named after a prophet (p=0.006 against random-5-from-114 null). Q 15 al-Ḥijr breaks the pattern (named after a place, not a prophet).

**Per [[h-new-610-letter-families]]**: ALR-5 NULL on whole-surah FR cohesion (56.25%ile). The cluster is united by **NAME-CLASS** but NOT by content-cohesion at FR-roots scale.

**Per [[cross-finding-008-muqattaat-book-intro-markers]]**: All 5 ALR surahs follow the **muqaṭṭaʿāt → book-reference** pattern (e.g. Q 12:1 *tilka āyātu al-kitābi al-mubīn*). Q 12 is the prototypical case.

## 3. Prophet-narrative cluster (FR-nearest neighbours)

Q 12's 5 FR-nearest surahs (computed from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D matrix):

1. Q 7 al-Aʿrāf (0.8995) — multi-prophet, polemic-rich.
2. Q 27 al-Naml (0.9070) — Sulaymān + multi-prophet.
3. Q 28 al-Qaṣaṣ (0.9133) — Mūsā continuous + theology.
4. Q 21 al-Anbiyāʾ (0.9336) — multi-prophet survey.
5. Q 11 Hūd (0.9638) — ALR cluster, multi-prophet.

**Q 12's content-distance signature places it in a clear "prophet-narrative" cluster**, even though the formal letter-family cluster (ALR) is content-NULL on cohesion. The empirical content cluster is broader than the formal cluster.

This is significant: **Q 12 is content-distinct from its formal ALR-cluster siblings (Q 10, 14, 15) but content-similar to Q 7, 27, 28, 21** — surahs without ALR letter-family. The signal is *narrative-form*, not *letter-family*.

## 4. Theological-iʿjāz orthogonality (Q 12 vs Q 55 al-Raḥmān)

**Q 55 is Q 12's most-distant surah in the entire corpus** (FR distance 1.4185). Substantive content:
- Q 12: narrative, verb-driven, single-protagonist, sequential time, dialogue-rich.
- Q 55: refrain-saturated, nominal-doxological, *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* × 31, no protagonist.

This empirical near-orthogonality is the **dual-iʿjāz typology** ([[h-new-840-unified-architectural-score]], [[h-new-860-hadith-architectural-alignment]]) made concrete: Q 12 is **narrative-iʿjāz** (anti-iʿjāz al-fawāṣil, sig_A rank 109/114); Q 55 is **theological-iʿjāz** (refrain-cohesion, sig_A high). The two architectural axes are empirically orthogonal.

## 5. Yaʿqūb-narrative cross-references

Yaʿqūb (يعقوب) is named in Q 12 (3×) and elsewhere (13×):
- Q 2:132–133, 136, 140 — Yaʿqūb's deathbed *waṣiyya*; cited in *millat Ibrāhīm* discussions.
- Q 3:84 — included in the prophets' acceptance list.
- Q 4:163 — included in revelation-receiver list.
- Q 6:84 — included in prophet-list.
- Q 11:71 — Sara's annunciation: *bishshara nāhā bi-Isḥāqa wa-min warāʾi Isḥāqa Yaʿqūb*.
- Q 19:6, 49 — in the Maryam-context Zakariyyāʾ + Ibrāhīm-cycle.
- Q 21:72, Q 29:27, Q 38:45 — prophet-list contexts.

**The cross-reference signature**: Yaʿqūb is the *family-link* connecting Q 12 to broader Quranic Banū Isrāʾīl narrative. Q 12 stands as the single Yaʿqūb-and-his-sons surah; the rest of the Quran's Yaʿqūb references are *prophets-list / lineage* references, not narrative.

## 6. Yūsuf cross-references outside Q 12

- **Q 6:84**: prophets-list (*wa-Yūsufa wa-Mūsā wa-Hārūna*).
- **Q 40:34**: didactic — *wa-laqad jāʾakum Yūsufu min qabli bi-l-bayyināti...* (Yūsuf is cited as a prior bringer of clear signs whom they doubted, used as a polemical analogy in Q 40).

These are the **only 2 non-Q-12 attestations** of يوسف in the entire Quran. Q 12's 92.6% concentration of the name (Q012-F-03) is thus near-exclusive eponymity.

## 7. Wider H-NEW finding integration

| Finding | Q 12's role |
|:--|:--|
| [[h-new-590-outlier-spectrum\|H-NEW-590]] | Q 12 is MODERATE_OUTLIER +14.26 pp in window {Q 9–15} |
| [[h-new-660-compression-tail-gradient\|H-NEW-660]] | Q 12 (s=12) is in the pre-kink plateau zone (s<50); d̄ = 1.112 above the post-kink trajectory |
| [[h-new-700-phonological-compression-tail\|H-NEW-700]] | Q 12's rhyme entropy 0.534 nats — among the lowest in muqaṭṭaʿāt-29 |
| [[h-new-720-canonical-adjacency-cost\|H-NEW-720]] | Q 12 has a high right-seam cost (0.216) vs cheap left-seam (0.035) |
| [[h-new-730-content-rhyme-anticorrelation\|H-NEW-730]] | Q 12 is on the high-content-distance side; consistent with the iʿjāz anti-twin lock |
| [[h-new-740-preislamic-poetry-control\|H-NEW-740]] | Q 12's narrative form is empirically distinct from poetry — Q 12's nūn-rhyme is verb-suffix-driven, not pre-Islamic mono-rhyme stylization |
| [[h-new-750-ijaz-signature\|H-NEW-750]] | Q 12 sig_A rank 109/114 (anti-iʿjāz al-fawāṣil); sig_B rank 89/114 |
| [[h-new-840-unified-architectural-score\|H-NEW-840]] | Q 12 UAS rank 6/114; enters via outlier × adjacency-cost, NOT via iʿjāz signature |
| [[h-new-860-hadith-architectural-alignment\|H-NEW-860]] | Q 12 is structural-iʿjāz (high UAS) but moderate fadāʾil-rank — the orthogonality |
| [[h-new-97]] | ALR-cluster prophet-name 4/5, p=0.006; Q 12 is the cluster's most-eponymous member |
| [[h-new-610-letter-families\|H-NEW-610]] | ALR-5 NULL on whole-surah FR cohesion at 56.25%ile; cluster is name-united, not content-united |
| [[cross-finding-008-muqattaat-book-intro-markers\|cross-finding-008]] | Q 12:1 *tilka āyātu al-kitābi al-mubīn* — prototypical muqaṭṭaʿāt → book-reference |

## 8. Verse-twin / phrase-twin highlights

- **Q 11:120** *naquṣṣu ʿalayka min anbāʾi al-rusul* ↔ **Q 12:3** *naquṣṣu ʿalayka aḥsana al-qaṣaṣ*: the narrative-frame verb *naquṣṣu* is the literal hand-off from Q 11 to Q 12.
- **Q 11:49** *tilka min anbāʾi al-ghaybi nūḥīhā ilayka* ↔ **Q 12:102** *dhālika min anbāʾi al-ghaybi nūḥīhi ilayka*: the *anbāʾ al-ghayb* epilogue formula at narrative-section closures.
- **Q 12:18** ↔ **Q 12:83** *fa-ṣabrun jamīl*: long-range internal refrain (Yaʿqūb's spiritual axis, repeated in homologous tests).
- **Q 12:6 / Q 12:38** *Ibrāhīma wa-Isḥāqa wa-Yaʿqūba* ↔ **Bukhārī #3243** *al-karīm ibn al-karīm ibn al-karīm ibn al-karīm Yūsuf b. Yaʿqūb b. Isḥāq b. Ibrāhīm*: the four-generation pedigree explicit in Q 12, glossed by the Prophet ﷺ.
- **Q 12:31** (women cutting their hands at Yūsuf's beauty) ↔ classical *shaṭr al-ḥusn* tradition (audited in `04-hadith-corpus.md` §2 and `05-classical-claims-audit.md` §5).
- **Q 12:92** *al-yawma lā tathrība ʿalaykum* (Yūsuf's forgiveness of his brothers) ↔ the Sīra report of the Prophet ﷺ at *fatḥ Makka* using the same words.

## 9. Surah-rank-position bookkeeping

- UAS rank: **6/114** ([[h-new-840-unified-architectural-score|H-NEW-840]]).
- FR-mean-distance rank (high = unique vocabulary): rank ~9/114 (z = +1.86).
- frac_narrative_verses rank: **1/114** (Q012-F-01).
- يوسف-name concentration rank: **1/114** (Q012-F-03).
- Outlier-strength rank: ~30/114 (MODERATE_OUTLIER).
- iʿjāz sig_A rank: 109/114 (low; structural anti-iʿjāz).
- iʿjāz sig_B rank: 89/114 (low; not pure-rhyme).
- Rhyme entropy rank (muqaṭṭaʿāt-29 internal): among lowest (0.534 nats).
- Position in revelation order (al-Suyūṭī chronology): 53/114 (mid-Meccan).

## 10. Summary of Q 12's role in the corpus

Q 12 occupies a **uniquely-positioned** intersection in the corpus's architectural signature space:

1. **Maximum narrative-form** (rank 1/114 on `frac_narrative_verses`).
2. **Maximum name-eponymity** (rank 1/114 on Yūsuf-token concentration).
3. **Anti-iʿjāz al-fawāṣil** (rank 109/114 on sig_A) — the structural opposite of refrain-rich Q 55 al-Raḥmān (FR distance 1.42 — Q 12's most-distant corpus surah).
4. **High UAS rank (6/114)** — driven by content-outlier × canonical-adjacency cost, NOT by structural-cohesion.
5. **Cluster pivot** — the most-eponymous member of the ALR cluster, which is name-united but content-NULL.

This conjunction makes Q 12 the **canonical reference point for narrative-iʿjāz** in the corpus. It is the surah-form that the *aḥsan al-qaṣaṣ* epithet describes literally, statistically, and architecturally.

## 11. Files in this surah's folder

```
surahs/Q012-yusuf/
├── 00-overview.md          (pre-existing scaffold)
├── 01-empirical-profile.md
├── 02-content-analysis.md
├── 03-tafsir-survey.md
├── 04-hadith-corpus.md
├── 05-classical-claims-audit.md
├── 06-novel-findings.md
├── 07-cross-references.md   (this file)
├── JOURNAL.md
├── Q012-F-01-narrative-purity-prereg.md
├── Q012-F-02-phase-cohesion-prereg.md
├── Q012-F-03-yusuf-token-density-prereg.md
├── Q012-F-04-self-reference-position-prereg.md
└── csv/
    ├── Q012-F-01.json
    ├── Q012-F-02.json
    ├── Q012-F-03.json
    ├── Q012-F-04.json
    └── Q012-classical-3-break-markers.json
```

Scripts: `scripts/Q012_F_01_narrative_purity.py`, `Q012_F_02_phase_cohesion.py`, `Q012_F_03_yusuf_density.py`, `Q012_F_04_self_reference.py`.
