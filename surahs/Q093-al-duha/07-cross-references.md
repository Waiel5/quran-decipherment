---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: cross-references
date_last_updated: 2026-05-30
phase: B+
verdict: neighbors, short-Meccan cluster, paired-surah bond, oath-frame family, H-NEW links mapped
---

# Q 93 al-Ḍuḥā — Cross-References


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

All FR / seam / UAS values are read from the on-disk JSON artifacts (cited in `01-empirical-profile.md`).
In the 1-indexed Fisher-Rao matrix Q 93 is index/id 93; in the 0-indexed `h-new-700.json` phoneme-vector
list it is index 92.

## 1. Neighboring surahs in the mushaf (`h-new-720.json`)

| Seam | delta_raw | rank | relationship |
|:--|:--|:--|:--|
| **Q 92 al-Layl → Q 93 al-Ḍuḥā** | +0.06063 | 55/113 (mid) | shared *wa-l-layl idhā [verb]* oath-frame (Q 93:2 ↔ Q 92:1) but a mid-spectrum entry-seam |
| **Q 93 al-Ḍuḥā → Q 94 al-Sharḥ** | **−0.01520** | **10/113 (seamless)** | the classically-PAIRED "one surah" (Ṭāwūs, ʿUmar b. ʿAbd al-ʿAzīz; al-Rāzī) — a clamped/negative joint, one of 13 seamless seams |

The seam-asymmetry around Q 93 is itself patterned (`csv/Q093F03-seam-asymmetry.json`): across
Q 91→92→93→94→95 the seamless/non alternation is **SEAMLESS | NON | SEAMLESS | NON**
(Q 91→92 rank 1, Q 92→93 rank 55, Q 93→94 rank 10, Q 94→95 rank 43) — Q 93 is *entered* by a mid-seam and
*exited* by a seamless joint into its paired successor al-Sharḥ.

## 2. Fisher-Rao neighbors (`h-new-111.json`)

- **Top-15 nearest:** Q 108 al-Kawthar (0.309), Q 106 Quraysh (0.353), Q 100 al-ʿĀdiyāt (0.364),
  **Q 94 al-Sharḥ (0.364)**, Q 113 al-Falaq (0.367), Q 111 al-Masad (0.368), Q 105 al-Fīl (0.370),
  Q 107 al-Māʿūn (0.375), Q 103 al-ʿAṣr (0.383), Q 112 al-Ikhlāṣ (0.387), Q 110 al-Naṣr (0.391),
  Q 114 al-Nās (0.402), Q 104 al-Humaza (0.404), Q 97 al-Qadr (0.408), Q 102 al-Takāthur (0.410).
- **Mean FR to all 113:** **0.8152** (well below corpus mean 0.9235 — Q 93 is deeply embedded in the
  short-Meccan tail).
- **5 farthest:** Q 2 (1.249), Q 5 (1.253), Q 4 (1.285), Q 9 (1.292), Q 3 (1.293) — the long Medinan
  legal surahs.

**Key cross-reference (Q093-F-01 Arm A):** Q 94 al-Sharḥ is Q 93's **4th-nearest** FR neighbor — the
whole-surah realization of the classical pairing. By contrast Q 92 al-Layl, which shares the *surface*
oath-frame (*wa-l-layl idhā [verb]*) and is chronologically adjacent (#9 → #11), is only Q 93's **18th**
FR neighbor. **The surface-anaphora bond (Q 92) and the root-distribution bond (Q 94) point to DIFFERENT
neighbors** — and the boundary-lexical bond to Q 94 is itself null (seam J = 0.0). See
`06-novel-findings.md`.

## 3. Cluster memberships

- **Short-Meccan mufaṣṣal-qiṣār tail:** Q 93's 14 nearest FR neighbors are ALL short late-mushaf surahs
  (the Q 94-114 region) plus Q 100 al-ʿĀdiyāt — the tightest part of the corpus.
- **{Q 90-96} ultra-cohesive window (H-NEW-590):** Q 93's outlier-window is {Q 90,91,92,93,94,95,96}; its
  d̄_W ≈ **0.4725** (vs corpus FR mean 0.92) — one of the tightest content-windows in the corpus. Removing
  Q 93 shifts the window dispersion by delta_pct **−0.06** (p = 0.9997) — Q 93 is a **deep cohesion
  member**, classification **NULL**, not an outlier.
- **al-Ḍuḥā + al-Sharḥ pair (Q093F01):** the {93, 94} pair's FR distance (0.364) ranks **128 / 6441**
  (1.99th percentile) corpus-wide (`csv/Q093F01-pair-cohesion.json`); the {92, 93, 94} trio mean FR
  (0.403) is z = −3.58 vs a corpus-triple null (`csv/Q093F02-trio-cohesion.json`) — but both pair- and
  trio-cohesion attenuate to NULL inside the short-mufaṣṣal pool (the whole tail is this tight), so the
  bond is a *short-Meccan-tail* effect, not a pair-exclusive one.

## 4. The paired-surah bond (Q093-F-01 Arm A)

**Q 93 al-Ḍuḥā ↔ Q 94 al-Sharḥ** — the classically-debated single unit (Ṭāwūs, ʿUmar b. ʿAbd al-ʿAzīz;
al-Rāzī reports and rejects). The bond is **whole-surah-distribution-cohesive** (FR rank 4; TSP exit-seam
rank 10/113 seamless) but **boundary-lexically null** (seam root-Jaccard 0.0 at k=3 and k=5; the only
shared root anywhere is `rbb`, outside the seam). The junction the classical reading names — Q 93:6
(*alam yajidka yatīman*) → Q 94:1 (*alam nashraḥ laka*) — shares no QAC root. And the pairing is **NOT
ḥadīth-attested**: no 9-book narration cites both surahs (`04-hadith-corpus.md` §4). The pairing is a
juristic/exegetical position with whole-surah empirical support and no isnād.

## 5. The oath-frame family (surface anaphora, NOT FR-bond)

**Q 93:2 ↔ Q 92:1** — the *wa-l-layl idhā [verb]* oath-frame (*sajā* "settles" / *yaghshā* "covers").
Ibn Kathīr cross-references Q 93:1-2 with Q 92:1-2 directly on disk (`en-tafisr-ibn-kathir/93/1.json`).
This is a **surface-anaphora** bond: Q 92 is only Q 93's 18th FR neighbor — the shared oath-frame does
NOT pull the two surahs together at the root-distribution scale. (A clean control for Arm A: surface
echo ≠ whole-surah cohesion.)

## 6. Content cross-references

- **Q 93:5 (*fa-tarḍā*) ↔ Ṣaḥīḥ Muslim intercession ḥadīth** — al-Qurṭubī cites the ʿAbdallāh b. ʿAmr
  *ummatī ummatī* → *innā sa-nurḍīka* narration as the *riḍā* reading of v 5 (`04-hadith-corpus.md` §3).
- **Q 93:6-8 (the biography of favors)** — the orphan/guidance/wealth triad is the Qurʾān's most compact
  autobiographical statement of the Prophet's early life (expanded in the sīra; Ibn Kathīr unpacks the
  orphan-biography on disk).
- **Q 93:6 (*yatīman*) → Q 93:9 (*al-yatīma*)** — the surah's UNIQUE internal lexical hinge (`ytm`); the
  only root bridging the favor block (vv 6-8) to the command block (vv 9-11). Among the 12 `ytm`-bearing
  surahs, only Q 2, Q 4, Q 93 carry it in ≥2 verses, and only Q 93 realizes a favor→command recall
  (Q093-F-01 Arm B).
- **Q 93:11 (*bi-niʿmati rabbika*) — the *rbb* inclusio** — vv 3, 5, 11 frame the surah on *rabb*; this is
  also the lone root Q 93 shares with Q 94 (Q 94:8 *wa-ilā rabbika*) — but it does not fall in the boundary
  seam.

## 7. H-NEW links

| Finding | Link to Q 93 |
|:--|:--|
| [[h-new-111\|H-NEW-111]] | FR matrix row; Q 94 = 4th-nearest neighbor; mean FR 0.8152 (short-Meccan tail) |
| [[h-new-590\|H-NEW-590]] | outlier NULL; Q 93 is a deep cohesion member of the {Q 90-96} window (d̄_W 0.47, delta_pct −0.06, p 0.9997) |
| [[h-new-700\|H-NEW-700]] | yāʾ (maqṣūra) monorhyme 72.7%; rhyme entropy 0.760 nats; phoneme dispersing regime (s>75) |
| [[h-new-720\|H-NEW-720]] | Q 93→Q 94 seamless exit-seam (rank 10/113); Q 92→Q 93 mid entry-seam (rank 55/113) |
| [[h-new-750\|H-NEW-750]] | iʿjāz sig_A +1.0503 (rank 32/114), sig_B +1.1581 (rank 23/114); local_cohesion 2.38 (z +1.18, upper band) |
| [[h-new-840\|H-NEW-840]] | UAS −1.4521 (rank 87/114); NOT a dispersion hub — micro-structural + phonological interest |
| [[h-new-2280\|H-NEW-2280]] | al-Biqāʿī munāsabah-seam; Q 93→Q 94 is a zero-Jaccard seam despite a smooth whole-surah joint |
| [[cross-finding-025\|CF-025]] | scale-of-aggregation — Q093-F-01 Arm A is a new supporting instance (paired-surah variant) |

## 8. Role in cross-finding syntheses

- **cross-finding-025 (formal scale-of-aggregation law):** Q093-F-01 Arm A adds the **paired-surah**
  variant — a classically-PAIRED unit cohesive at the whole-surah-distribution scale but lexically NULL at
  the boundary-pericope scale. (Q066-F-01 Arm B supplied the *intra-surah parable-pair* variant.) The Q 93
  case is especially sharp because the classical reading explicitly locates the bond at a *specific
  junction* (Q 93:6 → Q 94:1) where the root-Jaccard is exactly 0.
- **Favor→command lexical-recall census (candidate H-NEW):** Arm B's "same root names a divine favor AND
  heads a same-surah command" construction (`ytm`, v 6 → v 9) is a candidate corpus-wide structure not yet
  given an H-NEW ID — flagged for promotion (a corpus census of favor→command lexical recalls).
- **Surface-echo vs FR-bond control:** the Q 92 oath-frame echo (18th FR neighbor) vs the Q 94
  root-distribution bond (4th FR neighbor) is a clean per-surah demonstration that *surface anaphora is
  not whole-surah cohesion* — useful for any future munāsabah instrument-validation.

---

*2026-05-30. All links to on-disk findings; FR / seam / UAS / iʿjāz values cited to JSON artifacts in
`01-empirical-profile.md` and `csv/Q093-F-01.json`.*
