---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: cross-references
date_last_updated: 2026-05-30
phase: B+
verdict: neighbors, clusters, Muʿādh liturgical cluster, muqābala-overlap network mapped
---

# Q 92 al-Layl — Cross-References

All FR values reconstructed from `findings/phase-b-hypotheses/csv/h-new-111.json`
(`D_matrix_upper_triangular`, 1-indexed surah IDs; Q 92 is row 92 in the matrix, index 91 in the 0-indexed
phoneme-vector list). Seam values from `h-new-720.json` (`per_adjacency`); see `01-empirical-profile.md`.

## 1. Neighboring surahs in the mushaf

| Seam | delta_raw | ascending-rank | relationship |
|:--|:--|:--|:--|
| **Q 91 al-Shams → Q 92 al-Layl** | **−0.08683** | **1 / 113** (THE cheapest seam in the mushaf) | shared oath-of-opposed-cosmic-pairs → soul-bifurcation template |
| **Q 92 al-Layl → Q 93 al-Ḍuḥā** | +0.06063 | 55 / 113 (mid) | catch-word *al-layl*: Q 93 reuses the day/night oath (*wa-l-ḍuḥā wa-l-layli idhā sajā*) |

The **Q 91 → Q 92** transition is the **single most seamless canonical adjacency in the entire corpus**
(rank 1/113, delta_raw −0.08683, fraction_residual clamped to 0.0). Both surahs are early-Meccan oath-opening
short surahs on **cosmic-pairs → moral-duality**: al-Shams (sun/moon/day/night/heaven/earth/soul →
*qad aflaḥa man zakkāhā · wa-qad khāba man dassāhā*) and al-Layl (night/day/male-female → *fa-ammā man aʿṭā* /
*wa-ammā man bakhila*). For contrast the corpus's most expensive seams are Q 1 → Q 2 (0.622), Q 32 → Q 33
(0.363), Q 33 → Q 34 (0.331). The exit Q 92 → Q 93 is a normal mid-cost seam.

## 2. Fisher-Rao neighbors (`h-new-111.json`)

- **Mean FR to all 113 surahs:** **0.8438** (below corpus mean 0.9235 — a content-typical, near-central surah).
- **Nearest 15:** Q 111 (0.4060), Q 108 (0.4106), Q 94 (0.4115), **Q 93 (0.4338)**, Q 104 (0.4446),
  Q 106 (0.4452), Q 112 (0.4466), Q 113 (0.4479), Q 107 (0.4527), Q 103 (0.4588), Q 105 (0.4690),
  Q 100 (0.4722), **Q 91 (0.4734)**, Q 95 (0.4752), Q 101 (0.4767).
- **Farthest 5:** Q 5 (1.251), Q 6 (1.252), Q 9 (1.281), Q 3 (1.282), Q 4 (1.299) — the long Medinan legal surahs.

Q 92's FR neighborhood is the **short early-Meccan mufaṣṣal-qiṣār cluster**. Both of Q 92's literal mushaf
neighbors are top-13 FR neighbors — **Q 93 al-Ḍuḥā rank 4** and **Q 91 al-Shams rank 13** — a rare
convergence of canonical-adjacency and content-geometry (most surahs' mushaf neighbors are NOT among their
nearest FR neighbors). The 5 farthest are the opposite register (long Medinan legal surahs).

## 3. Cluster memberships

- **Short early-Meccan mufaṣṣal-qiṣār FR cluster** (H-NEW-111): Q 92's nearest neighbors are Q 111, 108, 94,
  93, 91, 95, 100, 101, 103, 104, 106, 107 — short oath/admonition surahs with dense believer/disbeliever/
  judgment vocabulary.
- **{Q 89–95} outlier-window deep-cohesion member** (H-NEW-590): Q 92 is a deep cohesion member of its
  symmetric ±3 window; removing it barely moves the window's dispersion (delta_pct **−0.06**, p = 0.9993,
  classification **NULL**). The window's percentile (0.07) is among the lowest in the corpus — one of the
  most internally-cohesive 7-surah neighborhoods in the mushaf.
- **The Muʿādh recitation cluster** {Q 87 al-Aʿlā, Q 91 al-Shams, Q 92 al-Layl, Q 93 al-Ḍuḥā} — the surahs
  the Prophet named fit for leading congregational prayer (Muslim #942/#943, al-Bukhārī #688; see
  `04-hadith-corpus.md`). This liturgical pairing has a **content-geometry correlate**: Q 93 is Q 92's
  rank-4 FR neighbor, Q 91 is rank-13, and the Q 91 → Q 92 seam is the cheapest in the corpus. The ḥadīth's
  prayer-cluster tracks the empirical short-Meccan cohesion block.
- **al-mufaṣṣal al-qiṣār** (al-Zarkashī *al-Burhān* mufaṣṣal-tier): Q 92 is a short-mufaṣṣal surah (21 verses).

## 4. The muqābala content-overlap network (Q092-F-01 Arm A)

Q 92's giver/miser muqābala (vv 5–10) is part of the project's **antithesis-overlap** network — the set of
hand-found and generated antithetical block/verse pairs tested against the jadal-overlap law:

| Object | Scale | Content behaviour | Verdict |
|:--|:--|:--|:--|
| **Q 92:5–10 giver↔miser** | single-surah hand-block | **OVERLAP-positive (J=0.222, z=+2.65)** | CONFIRMS H-NEW-2360 (Q092-F-01) |
| Q 83:7–28 sijjīn↔ʿilliyyīn | hand-block (closed catalogue) | disjoint (3 shared roots vs null 12.7) | the rare exception (Q083-F-01) |
| Q 98:6-7 sharr↔khayr al-bariyya | verse-pair | OVERLAP-positive (J=0.083 > null) | CONFIRMS jadal-overlap (Q098-F-01 Arm D) |
| 3,853 W=5 antithetical block-pairs | corpus generator | OVERLAP (z=+13.0) | the corpus law (H-NEW-2360) |

Q 92 is the **overlap-positive mirror** of the Q 83 disjoint showcase: both are textbook *muqābalāt*
(al-Suyūṭī Itqān nawʿ 59), but Q 92 behaves as the corpus law predicts while Q 83 is the hand-picked rarity.

## 5. Content cross-references

- **Q 91 al-Shams** (preceding): same oath-of-opposed-cosmic-pairs → soul-bifurcation template; the
  corpus-cheapest seam (`01-empirical-profile.md` §5).
- **Q 93 al-Ḍuḥā** (following): *wa-l-ḍuḥā · wa-l-layli idhā sajā* reuses Q 92's day/night oath-pair as its
  own opening — an inter-surah catch-word carrying Q 92's title-word *layl* into the next surah's oath.
- **Q 87:8 al-Aʿlā** (Muʿādh-cluster): *wa-nuyassiruka li-l-yusrā* — the "We shall ease you to ease"
  facilitation-formula (root *ysr*) is shared between Q 87 and Q 92 (vv 7, 10).
- **Q 92:5/8 ↔ qadar ḥadīth-family**: the giver/miser apodoses *fa-sa-nuyassiruhu li-l-{yusrā/ʿusrā}* are the
  *locus classicus* for the predestination-vs-deeds debate (*iʿmalū fa-kullun muyassar*, al-Bukhārī #1315/
  #4740, Muslim #6566; `04-hadith-corpus.md`).

## 6. H-NEW links

| Finding | Link to Q 92 |
|:--|:--|
| [[h-new-111\|H-NEW-111]] | FR matrix row; mean 0.8438; nearest Q 111 (0.406); Q 93 r4, Q 91 r13 |
| [[h-new-590\|H-NEW-590]] | outlier NULL; deep cohesion member of {Q 89–95} (delta_pct −0.06, p 0.9993) |
| [[h-new-700\|H-NEW-700]] | **perfect ي (`-ā`) monorhyme** (frac 1.000, 21/21 verses); phoneme dispersing regime (s>75) |
| [[h-new-720\|H-NEW-720]] | **Q 91 → Q 92 cheapest seam in the mushaf (rank 1/113)**; Q 92 → Q 93 rank 55/113 |
| [[h-new-750\|H-NEW-750]] | rhyme-entropy floor (0.0 nats, z −1.39) + above-average local cohesion (2.134, z +0.84); sig_A −0.61 |
| [[h-new-840\|H-NEW-840]] | UAS −2.029, rank 100/114 — not a structural hub; interest is positional + micro-rhetorical |
| [[h-new-1820-title-density-independence-formal\|H-NEW-1820]] | Q 92 rank **48/49** in *lyl* (Arm C) — an extreme on-corpus confirmation |
| [[h-new-2360-antithesis-law\|H-NEW-2360]] | giver/miser muqābala = frame-driven OVERLAP (Q092-F-01 Arm A, z +2.65) |

## 7. Role in cross-finding syntheses

- **H-NEW-2360 (§10.103) — jadal/overlap law:** Q092-F-01 Arm A is the **third independent confirmation**
  (after the corpus generator and Q098-F-01 Arm D) that antithetical pairs are content-overlapping, and the
  positive showcase counterpart to the rejected disjoint-content candidate (the Q 83 sijjīn/ʿilliyyīn case).
- **cross-finding-025 (scale-of-aggregation):** the giver/miser showcase adds a frame-overlap-dominant data
  point at the antithesis-block scale — frame cohesion beats pole-divergence in content terms.
- **H-NEW-1820 — title-density independence:** Q 92 (rank 48/49 in *lyl*) is among the most extreme
  confirmations: the eponym is rank-near-last in its own title-root.
- **TSP-residual / canonical-order (cross-finding-011 family):** the Q 91 → Q 92 seam (rank 1/113) is the
  smoothest single joint in the mushaf — a positional anchor for the early-Meccan cohesion block.

---

*2026-05-30 by Waiel Al-Shujaa. All FR/seam/UAS values cited to JSON artifacts in `01-empirical-profile.md`.*
