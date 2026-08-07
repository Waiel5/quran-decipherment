---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: cross-references
date_last_updated: 2026-05-30
phase: B+
verdict: neighbors, minimal-surah cohort, FR cluster, qasam family, content parallels mapped
---

# Q 103 al-ʿAṣr — Cross-References


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

## 1. Neighboring surahs in the mushaf (`h-new-720.json`)

| Seam | delta_raw | ascending-rank | relationship |
|:--|:--|:--|:--|
| **Q 102 al-Takāthur → Q 103 al-ʿAṣr** | +0.04795 | **44/113** (cheap) | both admonitions on misspent life: worldly-accumulation-as-ruin (al-Takāthur) → humankind-in-loss (al-ʿAṣr) |
| **Q 103 al-ʿAṣr → Q 104 al-Humaza** | +0.11570 | 88/113 (mid) | sharper tonal shift: universal loss → the backbiting wealth-hoarder |

The backward seam (Q 102 → Q 103) is cheaper than the forward seam (Q 103 → Q 104), matching the topical flow:
al-Takāthur → al-ʿAṣr is a smooth admonition-to-admonition transition, whereas al-Humaza introduces a specific
vituperative portrait. For scale, the corpus's most expensive seam is Q 1 → Q 2 (0.622); Q 103's seams are ≈ 1/13
and ≈ 1/5 of that. **Recitation echo:** Aḥmad *Musnad* #639 (verified, `04-hadith-corpus.md`) places al-Takāthur
(Q 102) and al-ʿAṣr (Q 103) in the same witr cycle — an independent practice-level echo of the cheap Q102→Q103 seam.

## 2. Fisher-Rao neighbors (`h-new-111.json`)

- **Nearest (top-15, all FR < 0.345):** Q 108 al-Kawthar (0.240), Q 106 al-Quraysh (0.263), Q 111 al-Masad (0.280),
  Q 112 al-Ikhlāṣ (0.291), Q 94 al-Sharḥ (0.293), Q 95 al-Tīn (0.297), Q 113 al-Falaq (0.298), Q 107 al-Māʿūn
  (0.299), Q 100 al-ʿĀdiyāt (0.311), Q 104 al-Humaza (0.312), Q 105 al-Fīl (0.312), Q 110 al-Naṣr (0.324),
  Q 101 al-Qāriʿa (0.334), Q 114 al-Nās (0.338), Q 102 al-Takāthur (0.345).
- **Mean FR to all 113:** 0.787 (far below corpus mean 0.9235) — Q 103 sits in the densest, most self-similar
  corner of the corpus.
- **Farthest:** Q 2 (1.239), Q 6 (1.245), Q 4 (1.270), Q 9 (1.281), Q 3 (1.288) — the long Medinan surahs.

Q 103's entire FR neighbourhood is the **short-Meccan mufaṣṣal-qiṣār tail** (Q 94-114). Its rank-1 neighbour
Q 108 al-Kawthar is the basis of Q103-F-01 Arm A.

## 3. Cluster memberships

- **Minimal-surah cohort {Q 103, Q 108, Q 110}** — the corpus's exactly three 3-verse surahs. Q 103 and Q 108
  are the **perfect rā'-monorhyme pair** (Q103-F-01 Arm A); Q 110 al-Naṣr (finals ح/ا/ا) is not. Q 103 → Q 108
  is FR rank 1 (0.240); Q 103 → Q 110 is FR rank 12 (0.324).
- **Perfect-monorhyme set (rhyme_entropy 0.0, H-NEW-750)** — only 15 of 114 surahs; Q 103 is one, sharing its
  **rā' final** with Q 54 (al-Qamar), Q 97 (al-Qadr), and Q 108 (al-Kawthar).
- **Short-Meccan mufaṣṣal-qiṣār FR-dense block {≈ Q 100-114}** — Q 103 is a perfect cohesion member (H-NEW-590
  outlier NULL, delta_pct 0.0, window {100-106}); it is maximally "in-block," the structural opposite of an outlier.
- **Qasam (oath) family (H-NEW-2210)** — Q 103 is a single wāw-oath on a *temporal* sworn object (ʿaṣr), with
  qasam→jawāb distance 1 (1 of 11 distance-1 clusters of the corpus's 44). Sister temporal-oath surahs include
  Q 89 al-Fajr, Q 92 al-Layl, Q 93 al-Ḍuḥā, Q 100 al-ʿĀdiyāt.

## 4. Content / thematic cross-references

- **Q 103:3 ≈ Q 95:6** — the verbatim *illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāti* clause, with the same
  *al-insān-negative-default → same-exception* logic (al-Baghawī ← Ibrāhīm al-Nakhaʿī; Claim 7,
  `05-classical-claims-audit.md`). Q 95 *aḥsan taqwīm → asfal sāfilīn* mirrors Q 103 *al-insān → khusr*.
- **Q 103 (loss-oath) ↔ Q 93 al-Ḍuḥā (profit-oath)** — al-Rāzī's mercantile profit/loss oath-diptych (*khusr*
  vs *al-ribḥ*; Claim 6). A thematic-rhetorical pairing, not a mushaf-adjacency (the two are 10 surahs apart).
- **The *khusr* / capital-loss image** recurs across the corpus: e.g. Q 35:29 (*tijāra lan tabūr* — "trade that
  will never perish"), Q 22:11 (*khasira al-dunyā wa-l-ākhira*). Q 103 is the most compressed deployment of the
  life-as-melting-capital metaphor (al-Rāzī's ice-seller anecdote, `03-tafsir-survey.md`).
- **The *āmanū wa-ʿamilū al-ṣāliḥāt* formula** — the corpus's most frequent creed-action collocation; Q 103:3
  is its most compressed deployment (the formula carrying an entire surah's salvific load).
- **No explicit citation of another surah** — Q 103 is self-contained (a single oath-form sentence).

## 5. H-NEW links

| Finding | Link to Q 103 |
|:--|:--|
| [[h-new-111\|H-NEW-111]] | FR matrix row; mean 0.787; rank-1 neighbour Q 108 (0.2399) |
| [[h-new-590\|H-NEW-590]] | outlier NULL (delta_pct 0.0); cohesion member of {100-106} |
| [[h-new-700\|H-NEW-700]] | perfect rā'-monorhyme (frac 1.0); phoneme emphatic-channel high (0.0959) |
| [[h-new-720\|H-NEW-720]] | Q 102→Q 103 (rank 44) cheaper than Q 103→Q 104 (rank 88) |
| [[h-new-750\|H-NEW-750]] | rhyme_entropy 0.0 (floor); local_cohesion rank 10/114; sig_A −0.0473 (rank 61), sig_B +0.7180 (rank 38) |
| [[h-new-840\|H-NEW-840]] | UAS −2.244 (rank **106/114**, bottom band — protocol §3.3 bottom-10) |
| [[h-new-2210\|H-NEW-2210]] | minimal wāw-qasam, temporal object, jawāb distance 1 |
| [[h-new-2340\|H-NEW-2340]] | **#2/114** emphatic-istiʿlāʾ density (0.0959, ṣād-driven); adhab_density 0.0 |

## 6. Role in cross-finding syntheses

- **Structural-vs-theological iʿjāz orthogonality (protocol §3.4; al-Bāqillānī vs al-Khaṭṭābī).** Q 103 is a clean
  instance: a surah classical scholars revered for its *meaning* (al-Shāfiʿī "would suffice them"; al-Rāzī taḥaddī
  test-case) sits at the **bottom band of the structural-dispersion UAS** (rank 106/114). Its empirical interest is
  micro-structural/phonological (the minimal-surah rā'-twin, #2 ṣād-density, minimal qasam skeleton), not
  whole-surah dispersion — a supporting data-point for the orthogonality of the two iʿjāz axes.
- **Minimal-surah twin (candidate corpus-wide H-NEW).** The {Q 103, Q 108} rā'-monorhyme + FR-rank-1 pairing
  (Q103-F-01 Arm A) is a candidate corpus-wide "minimal-surah twin" finding, parallel to the verbatim-twin roster
  promoted from Q066-F-01; queued as Q103-F-03.
- **Emphatic-iconicity (H-NEW-2340).** Q 103 is the #2 data-point; its DIRECTIONAL (p=0.070) per-surah result +
  zero adhab_density supports the corpus-level NULL of the heavy↔punishment hypothesis (emphasis is lexical-spine
  driven, not theme-driven).

---

*2026-05-30. All links to on-disk findings; FR/seam/UAS/density values cited to JSON artifacts in
`01-empirical-profile.md`.*
