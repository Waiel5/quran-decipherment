---
surah: 29
surah_name_translit: al-ʿAnkabūt
file_type: cross-references
date_last_updated: 2026-05-10
phase: B+
verdict: "Q 29 sits at the head of the contiguous Late-Meccan ALM-4 quartet {Q 29, 30, 31, 32} and is the 3rd of the larger ALM-6 cluster {Q 2, 3, 29, 30, 31, 32}. Q 29's FR-content-nearest neighbor is Q 3 (d=0.842), not Q 30 (d=0.915). Pericope-scale ALM-4 cohesion NULLs (Q029-F-02); whole-surah ALM-6 cohesion is PARTIAL (Q030-F-08). Q 29 ↔ Q 30 munāsabah is thematic-narrative (promise→fulfillment) but lexically NULL."
---

# Q 29 al-ʿAnkabūt — Cross-references


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

## 1. Immediate neighbors

### Q 28 → Q 29 (mushaf preceding)

- **Q 28 al-Qaṣaṣ** — Late Meccan; ṬSM (Ṭā-Sīn-Mīm) muqaṭṭāʿat; Q 28:2-3 *tilka āyātu al-kitābi al-mubīn* — opens with book-reference. Cross-finding-008 BOOK-REFERENCE pattern present.
- **FR-distance** Q 28 ↔ Q 29: not in H-NEW-111 quick-reference; H-NEW-720 canonical-adjacency δ = 0.0746 (fraction_residual = 0.009).
- The Q 28 → Q 29 mushaf transition is one of the more expensive among Late-Meccan adjacencies (per H-NEW-720). The muqaṭṭāʿat shift (ṬSM → ALM) may be part of the cost.

### Q 29 → Q 30 (mushaf following)

- **Q 30 al-Rūm** — Late Meccan; ALM muqaṭṭāʿat; ALSO a cross-finding-008 exception (no book-reference at vv 1-3; the book-reference appears at v 6).
- **FR-distance** Q 29 ↔ Q 30 = 0.9153 (rank 7/15 within ALM-6).
- **H-NEW-720** canonical-adjacency δ = 0.0293 (fraction_residual = 0.0035). This is content-cheap — Q 29 → Q 30 is a low-cost mushaf transition.
- The Q 29 → Q 30 pair constitutes the **only ALM-cluster consecutive-mushaf-position exception-pair** to cross-finding-008. They are also the only consecutive-mushaf-position muqaṭṭāʿat-pair without book-reference at vv 1-3.

### Cohesion: Q 29 ↔ Q 30 micro-pair

| Test | Verdict | p_perm |
|:--|:--|:-:|
| Whole-surah FR (within ALM-6) | rank 7/15 — NOT a tight pair | n/a (descriptive) |
| Pericope (first 3 verses) Jaccard | J=0.000 (no root intersection) | n/a |
| Q030-F-04 architectural-twin | NOT a content-FR-twin pair | (per Q 30 specialist) |
| al-Biqāʿī Q 29 → Q 30 munāsabah | thematic-narrative (promise→fulfillment) | qualitative |

The Q 29 ↔ Q 30 relationship is **classical-qualitative** (al-Biqāʿī's promise-fulfillment *munāsabah*) but **NOT lexical**. This is a clean instance of cross-finding-025 marker-thickness rule: a single thematic-marker is insufficient to drive lexical cohesion.

## 2. Cluster memberships

### 2a. ALM-6 muqaṭṭaʿāt cluster

C_ALM_6 = {Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}.

- Whole-surah FR-cohesion (Q030-F-08): **PARTIAL** — Cell A NULL (uniform p=0.418), Cell B length-matched PASS (p=0.0225). Length-confound is the reason for PARTIAL.
- Within-cluster ranks of Q 29's pairs:
  - Q 29 ↔ Q 3 = 0.842 (rank 2/15 within ALM-6) — Q 29's CLOSEST FR-neighbor in the cluster.
  - Q 29 ↔ Q 2 = 0.849 (rank 3/15).
  - Q 29 ↔ Q 31 = 0.896 (rank 4/15).
  - Q 29 ↔ Q 30 = 0.915 (rank 7/15).
  - Q 29 ↔ Q 32 = 0.938 (rank 9/15).
- This means Q 29 is FR-closer to the MEDINAN ALM-surahs (Q 2, Q 3) than to its Late-Meccan ALM-quartet companions (Q 30, Q 31, Q 32). This is an interesting **chronology-architecture dissociation**.

### 2b. ALM-4 Late-Meccan sub-cluster (the contiguous mushaf-quartet)

C_ALM_4 = {Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}.

- Pericope-window FR-cohesion (Q029-F-02): **NULL** (J=0.043 vs null 0.050; direction reversed).
- Whole-surah within-quartet mean FR (Q030-F-08 data):
  - 6 pairs: (29,30), (29,31), (29,32), (30,31), (30,32), (31,32)
  - Distances: 0.915, 0.896, 0.938, 0.909, 0.927, 0.909
  - Mean = **0.916** (comparable to the broader ALM-6 mean 0.926).
- The contiguous mushaf-position is a real fact but does NOT confer lexical cohesion.

### 2c. Late-Meccan prophet-narrative cluster (Q 7, Q 11, Q 26, Q 29, Q 37, Q 54, Q 71)

Q 29:14-40 contains the 7-prophet narrative sequence (Nūḥ → Ibrāhīm → Lūṭ → Shuʿayb → ʿĀd → Thamūd → Mūsā-Firʿawn-Hāmān-Qārūn). This narrative pattern is shared with:
- Q 7 al-Aʿrāf (Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā)
- Q 11 Hūd (Nūḥ, Hūd, Ṣāliḥ, Ibrāhīm-Lūṭ, Shuʿayb, Mūsā)
- Q 26 al-Shuʿarāʾ (Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb)
- Q 37 al-Ṣāffāt (Nūḥ, Ibrāhīm, Mūsā-Hārūn, Ilyās, Lūṭ, Yūnus)
- Q 54 al-Qamar (Nūḥ, ʿĀd, Thamūd, Lūṭ, Firʿawn — punishment-cycle)
- Q 71 Nūḥ (Nūḥ alone — dedicated surah)

Q 29's prophet-block is structurally distinct: 7 prophets in 27 verses (vv 14-40), an unusually compressed narrative density. The "1000 minus 50 years" tradition (Q 29:14) for Nūḥ's mission is corpus-unique numerical phrasing.

### 2d. Imtihān-doctrine cluster (Q 2:155, Q 3:152, Q 7:168, Q 21:35, Q 29:2-3, Q 47:31)

Q 29:1-3 is the canonical imtihān-opener in the Quran. The doctrine appears across:
- Q 2:155 — *wa-la-nablwannakum bi-shayʾin* (testing through hardship).
- Q 3:152 — *wa-la-qad ṣadaqakumu llāhu waʿdahu idh taḥussūnahum*.
- Q 7:168 — *wa-balawnāhum bi-l-ḥasanāti wa-l-sayyiʾāt*.
- Q 21:35 — *wa-naluwwakum bi-l-sharri wa-l-khayri fitnatan*.
- Q 29:2-3 — *a-ḥasiba al-nāsu an yutrakū ... lā yuftanūn*.
- Q 47:31 — *wa-la-nablwannakum ḥattā naʿlama al-mujāhidīna minkum*.

Q 29:2 is the only one that uses the FORMULA *a-ḥasiba al-nāsu* (rhetorical-question opener). This is corpus-unique phrasing in the imtihān cluster.

## 3. Cross-mushaf content references

| Q 29 content | Cross-surah references | Notes |
|:--|:--|:--|
| Q 29:8 (parents-vs-shirk) | Q 31:14-15 (Luqmān's analogous teaching) | Q 31:14 explicitly couples *waṣṣaynā al-insāna bi-wālidayhi* + *wa-in jāhadāka ʿalā an tushrika bī*. Q 29:8 and Q 31:14-15 are NEAREST-VERSE-TWINS at the doctrinal level. |
| Q 29:14 (Nūḥ's 950 years) | none — corpus-unique phrasing | The 1000-minus-50 form is corpus-singleton. |
| Q 29:41 (spider parable) | none — corpus-unique vehicle | (Q029-F-03 + Q029-F-04 confirm). |
| Q 29:48 (prophet's pre-Quranic illiteracy) | Q 7:157-158 (al-nabī al-ummī) | Q 29:48 is the "before-the-Quran" form. |
| Q 29:56 (migration verse, *arḍī wāsiʿah*) | Q 4:97 (*alam takun arḍu llāhi wāsiʿatan*) | Both are migration-incentive verses; Q 4:97 is Medinan, Q 29:56 Meccan. Direction of dependence: Q 29 → Q 4 chronologically. |
| Q 29:69 (*jāhadū fīnā la-nahdiyannahum*) | Q 5:35, Q 8:74, Q 9:20 (jihād + guidance pattern) | Q 29:69 is the OLDEST attestation of this striving-guidance bracket; the Medinan parallels post-date. |

## 4. H-NEW findings touching Q 29

| H-NEW ID | Claim | Q 29 role |
|:--|:--|:--|
| H-NEW-53 | muqaṭṭāʿat + book-reference correlation | Q 29 = 1 of 2 ALM-cluster exceptions to the pattern (Q 29 + Q 30) |
| H-NEW-93 (parent NULL) | Q 29/30 sub-pattern | Imtihān-density at Q 29 is 8.20/k (above Meccan baseline 5.05) but does not pass Bonferroni-4 alone |
| H-NEW-111 | 114×114 FR matrix | Q 29's row contains its closest FR-neighbors (Q 3, Q 2, Q 31) |
| H-NEW-590 | per-surah outlier-strength | Q 29 = WEAK_ANCHOR (Δ%ile = −7.34) — content-cohesive |
| H-NEW-660 | content compression-tail law | Q 29 (s=29, head-pole) predicted d̄ = 0.96; observed 0.998 (slightly above law) |
| H-NEW-700 | per-surah rhyme + phoneme | Q 29 rhyme-entropy z = −0.484 (moderately consolidated); 86% nūn |
| H-NEW-720 | canonical-adjacency TSP-cost | δ(Q28→Q29) = 0.075; δ(Q29→Q30) = 0.029 |
| H-NEW-750 | per-surah iʿjāz signature | sig_A = −1.218 (rank 90/114); sig_B = −1.017 (rank 80/114) |
| H-NEW-840 | UAS ranking | Q 29 UAS = +0.158 (rank 44/114) — moderate-high |
| H-NEW-1340 | al-ḥamdu li-llāh opener NULL | Q 29 NOT in this cluster (Q 29 opens with ALM, not *al-ḥamdu*) |

## 5. Q 29 in cross-finding syntheses

- **[[../findings/cross-finding/cross-finding-008-muqattaat-book-introduction-marker-synthesis|cross-finding-008]]**: Q 29 is one of 2 ALM-cluster exception-surahs to the muqaṭṭāʿat → book-reference correlation. (Q 29:1-3 does NOT contain a book-reference; Q 30:1-3 likewise.)
- **[[../findings/cross-finding/cross-finding-025-multi-axis-architecture|cross-finding-025]]**: Q029-F-02 NULL provides a counter-data-point for the marker-thickness rule at narrow-pericope scale. Q 30 ↔ Q 29 ↔ Q 31 ↔ Q 32 share the ALM marker (corpus-EXACT) + chronology + mushaf-adjacency + 3-of-4 book-reference morphology — and STILL the first-3-verses pericope window does NOT cohere on root-Jaccard. This refines the rule: multi-axis correlation is necessary but not sufficient at narrow aggregation scales.
- **[[../findings/cross-finding/cross-finding-026-iʿjāz-architecture|cross-finding-026]]**: Q029-F-04 PASS supports the iʿjāz al-tashbīh axis empirically. Q 29:41 is the corpus-unique parable schema instance.
- **scale-of-aggregation corollary (H-NEW-1380)**: Q029-F-02 NULL at pericope contrasts with Q030-F-08 PARTIAL at whole-surah — same theological set, different verdicts at different scales. This is the "second NULL pericope-scale boundary-case" relative to the Iblīs-pericope PASS at the same instrument.

## 6. Q 29 → Q 31 doctrinal twin (Q 29:8 ↔ Q 31:14-15)

The strongest cross-mushaf doctrinal twin involving Q 29 is **Q 29:8 ↔ Q 31:14-15**:
- Q 29:8: *wa-waṣṣaynā al-insāna bi-wālidayhi ḥusnā; wa-in jāhadāka li-tushrika bī mā laysa laka bihi ʿilmun fa-lā tuṭiʿhumā*.
- Q 31:14-15: *wa-waṣṣaynā al-insāna bi-wālidayhi ḥamalathu ummuhu wahnan ʿalā wahnin ... wa-in jāhadāka ʿalā an tushrika bī mā laysa laka bihi ʿilmun fa-lā tuṭiʿhumā*.

Both verses share the same core formula. Q 31:14 even uses the root `whn` (twice: *wahnan ʿalā wahnin*) — the same root as Q 29:41's *awhana al-buyūt*. This is an intra-ALM-4 lexical bridge that survives the Jaccard threshold at the FULL-surah scale (the `whn` root is shared between Q 29 and Q 31), but is NOT in the first-3-verses pericope (the root appears at v 41 and v 14 respectively).

## 7. Q 29's UAS placement and architectural type

- UAS rank 44/114 — moderate-high.
- WEAK_ANCHOR (Δ%ile = −7.34) — content-cohesive within 7-window neighborhood.
- iʿjāz signature sig_A = −1.218 (structural-iʿjāz quadrant, moderate strength).
- 86% nūn rhyme (Late-Meccan default).

Q 29 is a **mid-strength architectural anchor with corpus-unique semantic eponym**. Its strength is concentrated at the parable-verse Q 29:41 (corpus-unique lemma + frailty-superlative + joint-schema-singleton), not at the whole-surah architectural axes.

## 8. Honest limits

- The FR-distance matrix H-NEW-111 is computed on QAC stem-roots; alternative instruments (TF-IDF tokens, character n-grams) may show different neighbor rankings.
- The Q 29 ↔ Q 31 doctrinal twin claim (Q 29:8 ↔ Q 31:14-15) is qualitative-textual; quantitative verse-twin ranking is queued.
- The 8-prophet-narrative cluster is a thematic-content cluster, not a quantitative cohesion cluster (no FR-cohesion test has been run on this subset specifically).
