---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: cross-references
date_last_updated: 2026-05-30
phase: B+
verdict: neighbors, short-Meccan cluster, consolation-pair, near-verbatim reprise ladder, H-NEW links mapped
---

# Q 94 al-Sharḥ — Cross-References


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
| **Q 93 al-Ḍuḥā → Q 94 al-Sharḥ** | **−0.0152** | **10/113** (seamless) | the consolation-pair seam: both direct second-person reassurances to the Prophet (*waddaʿaka* / *a-lam nashraḥ*); shared *rabbuka* address |
| **Q 94 al-Sharḥ → Q 95 al-Tīn** | +0.0470 | 43/113 (mid) | normal mid-cost transition: consolation-address → oath-opening (*wa-l-tīni wa-l-zaytūn*) |

The immediately-preceding Q 91 → Q 92 is the corpus's single cheapest seam (delta_raw −0.0868), so the
Early-Meccan run **Q 91 → Q 92 → Q 93 → Q 94** is an unusually smooth stretch of the mushaf. The Q 93 → Q 94
seam (rank 10/113) is the TSP-residual correlate of the classical consolation-pair reading (Claim 6,
`05-classical-claims-audit.md`). For contrast, the corpus's most expensive seams are Q 1→Q 2 (0.622),
Q 32→Q 33 (0.363), Q 33→Q 34 (0.331).

## 2. Fisher-Rao neighbors (`h-new-111.json`)

- **Mean FR to all 113:** **0.7936** (far below corpus mean 0.9235 — one of the lowest in the corpus; Q 94
  sits deep inside the dense short-surah neighborhood, not at a dispersion-extreme).
- **Nearest 8:** [[Q108-al-kawthar|Q 108 al-Kawthar]] (0.230), Q 106 (0.271), Q 111 (0.287), Q 113 (0.290),
  Q 103 (0.293), Q 100 (0.295), Q 112 (0.298), Q 105 (0.305) — almost the entire short-Meccan / muʿawwidhāt
  tail.
- **Neighbor surahs:** [[Q095-al-tin|Q 95 al-Tīn]] (next) at FR 0.3614, rank **15/113**;
  [[Q093-al-duha|Q 93 al-Ḍuḥā]] (prev, paired) at FR 0.3641, rank **16/113** — both are top-16 FR neighbors,
  so Q 94 sits content-near its mushaf neighbors.
- **Farthest 5:** Q 5 (1.255), Q 2 (1.261), Q 4 (1.299), Q 3 (1.303), Q 9 (1.304) — the long-Medinan
  legal/narrative surahs (maximal-vocabulary end of the corpus).

## 3. Cluster memberships

- **Short-Meccan / muʿawwidhāt-adjacent tail:** Q 94's nearest 15 FR neighbors are all short late-mushaf
  surahs (Q 100-114 + Q 95). Its nearest neighbor Q 108 al-Kawthar is a short-Meccan gift/consolation surah
  (both reassure the Prophet against the mushrikūn's slights). Q 94 is a textbook member of this dense,
  lexically-narrow cluster.
- **Outlier-window cohesion member (H-NEW-590):** Q 94's symmetric ±3 window is {Q 91-97}, with an
  extraordinarily low content-dispersion percentile (pct_W 0.01). Removing Q 94 lowers the dispersion
  percentile by only 0.07pp (delta_pct **−0.07, NULL**) — Q 94 is a cohesion member, not an outlier.
- **Consolation-pair {Q 93, Q 94}:** the al-Ḍuḥā ↔ al-Sharḥ diptych — consecutive in the mushaf (93→94),
  consecutive in revelation order (#11 → #12), top-16 FR neighbors, seamless seam (rank 10/113). One of the
  most tightly-bound surah pairs in the corpus across mushaf-adjacency, chronology, content, and seam-cost
  simultaneously (see Claim 6).
- **No muqaṭṭaʿāt; no musabbiḥāt.** Q 94 opens on a rhetorical-interrogative *a-lam* (affirmation), not a
  letter-prefix or *sabbaḥa*/*qul* formula.

## 4. Near-verbatim adjacent reprise network (Q094-F-01)

**Q 94:5-6** — *fa-inna maʿa al-ʿusri yusrā* / *inna maʿa al-ʿusri yusrā* — is the **corpus-singleton**
near-verbatim adjacent couplet: the unique adjacent same-surah pair differing by only a single leading
fāʾ/wāw (Arm A), and the **global minimum** character edit distance (1) over all 5,821 substantive adjacent
pairs (Arm B). The corpus has **zero** exact-verbatim adjacencies.

**The edit-2 runner-up family** (the in-corpus control, `csv/Q094-F-01.json` top12): **Q 74:19-20,
Q 75:34-35, Q 82:17-18, Q 102:3-4** — four near-verbatim adjacent reprises with a two-character delta. These
form a candidate corpus-wide class of "near-verbatim adjacent reprises" (queued Q094-F-02), of which
Q 94:5-6 is the *tightest* member and the only *consolation* member (the runner-ups are graded-threat /
oath / eschatological reprises). Notably [[Q102-al-takathur|Q 102 al-Takāthur]] (5:3-4, *kallā sawfa
taʿlamūn / thumma kallā sawfa taʿlamūn*) is both an edit-2 reprise here AND the subject of Q102-F-01's
thumma-threat-doubling family — the two surahs sit at adjacent rungs of the reprise ladder.

## 5. Content cross-references

- **Q 93 al-Ḍuḥā:** the paired consolation surah — shared second-person register, *rabbuka* address (Q 93:3,5,11;
  Q 94:8 *rabbika*), dhikr/elevation theme; both early-Meccan reassurances during the *fatra* tradition.
- **Q 48 al-Fatḥ (48:2):** Ibn Kathīr reads Q 94:2 (*waḍaʿnā ʿanka wizrak*) in light of Q 48:2 (*li-yaghfira
  laka Allāhu mā taqaddama min dhanbika wa-mā taʾakhkhar*) — the burden as the forgiven matter.
- **The *sharḥ al-ṣadr* motif (root š-r-ḥ + ṣadr):** Q 94:1 is the only first-person-plural divine
  *expansion* of the Prophet's breast; the collocation recurs at Q 6:125 (*yashraḥ ṣadrahu li-l-islām*),
  Q 39:22 (*sharaḥa Allāhu ṣadrahu*), Q 16:106 (*sharaḥa bi-l-kufri ṣadran*), and Q 20:25 (Mūsā's prayer
  *rabbi-shraḥ lī ṣadrī*) — Q 94:1 answers, for Muḥammad, the prayer Mūsā had to make.
- **Q 9:52 (*iḥdā al-ḥusnayayn*):** al-Zamakhsharī cross-cites this for the "two eases" (dunyā + ākhira)
  reading of vv 5-6.
- **Q 108 al-Kawthar (FR-nearest, 0.230):** short-Meccan gift/consolation register; both reassure the
  Prophet against the mushrikūn.

## 6. H-NEW links

| Finding | Link to Q 94 |
|:--|:--|
| [[h-new-111\|H-NEW-111]] | FR matrix row; mean 0.7936 (corpus-low), nearest Q 108 (0.230) |
| [[h-new-590\|H-NEW-590]] | outlier NULL; Q 94 is a {Q 91-97} cohesion member (pct_W 0.01) |
| [[h-new-700\|H-NEW-700]] | three-zone rhyme (top letter ك 0.5, vv 1-4); phoneme dispersion-tail (s>75) |
| [[h-new-720\|H-NEW-720]] | Q 93 → Q 94 seamless seam (asc-rank 10/113); smooth Q 91→92→93→94 run |
| [[h-new-750\|H-NEW-750]] | iʿjāz signature: sig_A +1.7705 (rank 11/114), sig_B +1.7603 (rank 13/114), local_cohesion 2.45 |
| [[h-new-840\|H-NEW-840]] | UAS −0.6415 (rank 65/114); iʿjāz-high but outlier-flat → not a whole-surah hub |
| [[h-new-2100\|H-NEW-2100]] | within-verse reduplication — Q 94:5-6 is the *inter*-verse near-verbatim analogue |
| [[h-new-2140\|H-NEW-2140]] | verse-initial anaphora — the -ka-suffix run (vv 1-4) is a sustained 2nd-person anaphora |
| [[h-new-2280\|H-NEW-2280]] | munāsabah-seam — Q 93/94 consolation-pair smooth adjacency correlate |
| [[h-new-2310\|H-NEW-2310]] | refrain census — Q 94:5-6 is the near-verbatim complement the *verbatim* census omits |
| [[h-new-2350\|H-NEW-2350]] | exact-verse-twins same-period — Q 94:5-6 is the intra-surah limiting case |
| [[h-new-2380\|H-NEW-2380]] | near-twin census (≤2 edits) — Q 94:5-6 is the corpus minimum (edit-1) |

## 7. Role in cross-finding syntheses

- **Repetition-architecture ladder:** Q094-F-01 contributes the **near-verbatim adjacent reprise** rung — a
  repetition type invisible to byte-exact refrain counting (H-NEW-2310) and distinct from within-verse
  reduplication (H-NEW-2100) and verse-initial anaphora (H-NEW-2140). Q 94:5-6 is the global tightest case;
  the edit-2 family {Q 74, 75, 82, 102} is the candidate corpus-wide class (Q094-F-02, queued).
- **Pillar-law correlate (scale-of-aggregation):** Q 94 is whole-surah *middling* (UAS rank 65/114) but
  micro-structurally *singular* (the corpus-tightest reprise) — a clean instance of architectural
  distinctiveness living at the **finest scale** (cf. H-NEW-2420 within-surah naẓm; cross-finding-025/026),
  not the whole-surah scale.
- **Consolation-pair as a tightly-bound dyad:** {Q 93, Q 94} co-locate across four instruments (mushaf
  adjacency, revelation chronology, FR distance, seam-cost) — a candidate exemplar for a future
  "paired-unit" corpus census.

---

*2026-05-30. All links to on-disk findings; FR/seam/UAS/iʿjāz values cited to JSON artifacts in
`01-empirical-profile.md`.*
