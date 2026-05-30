---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q092-F-01 — Arm A CONFIRMS H-NEW-2360 (frame-driven OVERLAP, z=+2.65) + Arm B PASS (frame-driven) + Arm C CONFIRMS H-NEW-1820 (Q92 lyl-rank 48/49)
seed: 20260509
n_perm: 10000
---

# Q 92 al-Layl — Pre-Registered Novel Findings

One pre-registered three-arm test, run with seed 20260509 / replication 20260601 and 10,000 permutations,
pre-reg SHA-256 locked before computation and verified at runtime (fail-fast).

- **Pre-reg:** `surahs/Q092-al-layl/Q092-F-01-giver-miser-antithesis-prereg.md`
- **Pre-reg SHA-256:** `6e41fd080525daf5d638f84416339584e3bd6143da457850afc75363d01981b8` (verified at runtime — printed `[ok] pre-reg SHA verified`)
- **Script:** `scripts/Q092_F_01_giver_miser_antithesis.py`
- **JSON:** `surahs/Q092-al-layl/csv/Q092-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The motivating object: Q 92:5–10 is the corpus's cleanest two-pole moral *muqābala* —
*fa-ammā man **aʿṭā wa-ttaqā** · wa-**ṣaddaqa** bi-l-ḥusnā · fa-sa-nuyassiruhu li-l-**yusrā*** (giver)
against *wa-ammā man **bakhila wa-staghnā** · wa-**kadhdhaba** bi-l-ḥusnā · fa-sa-nuyassiruhu li-l-**ʿusrā***
(miser). al-Suyūṭī catalogues exactly this figure (*Itqān* nawʿ 59). The test asks whether this textbook
muqābala behaves as the project's own corpus law **H-NEW-2360** (§10.103) predicts — content-**overlapping**
and **frame-driven** (the *jadal* signature) — or as the *rejected* "muqābala = minimal frame + disjoint
content" candidate law predicted. Direction LOCKED to the H-NEW-2360 prior (OVERLAP-positive) **before** any
null computation; a reversal would have been published as a pre-commit violation with full prominence.

---

## Q092-F-01 Arm A — content-overlap of the giver/miser muqābala (CONFIRMS H-NEW-2360 jadal/overlap direction)

**Hypothesis (pre-committed, direction-locked OVERLAP-positive):** the giver block G = roots(vv 5–7) and the
miser block M = roots(vv 8–10) share **more** content than a length-matched random same-surah 3-verse
block-pair — replicating H-NEW-2360's corpus reversal at the single-surah showcase-muqābala scale.

- **A-H1 (PRIMARY):** J(G, M) **>** null-mean AND upper-tail p_perm **< α = 0.05**.

**Result (`csv/Q092-F-01.json` → `arm_A_content_overlap`):**

| Quantity | Value |
|:--|:--|
| G = roots(vv 5–7) | {ETw (*aʿṭā*), Hsn (*ḥusnā*), Sdq (*ṣaddaqa*), wqy (*ittaqā*), ysr (*yusrā*)} — \|G\| = 5 |
| M = roots(vv 8–10) | {Esr (*ʿusrā*), Hsn (*ḥusnā*), bxl (*bakhila*), gny (*istaghnā*), k\*b (*kadhdhaba*), ysr} — \|M\| = 6 |
| shared roots | **{Hsn, ysr}** |
| **J(G, M)** | **0.2222** (= 2/9) |
| null-mean (seed 20260509, 10,000 perms) | 0.03416 |
| null-std | 0.07108 |
| n_ge (#{null J ≥ obs}) | 326 / 10,000 |
| **z** | **+2.646** |
| **p_upper_tail** | **0.0327** (< 0.05) |
| replication (seed 20260601) | null-mean 0.03353, **p_upper 0.0329** |
| direction observed | **OVERLAP-positive (TIGHTER than random)** — matches lock |
| pre-commit violation | **False** |

**Verdict: CONFIRMS H-NEW-2360's jadal/overlap direction at showcase scale.** The textbook giver/miser
muqābala shares **significantly more** root-content than a length-matched random same-surah block-pair
(z = +2.65, p = 0.033, replicated p = 0.033 on a second seed). The direction matches the pre-committed
H-NEW-2360 prior — antithetical blocks are content-**overlapping**, not depleted.

---

## Q092-F-01 Arm B — frame-vs-pole decomposition (PASS — overlap is frame-driven, divergence is in the poles)

**Hypothesis (deterministic):** the overlap is the antithesis **scaffold**, i.e. the shared roots are
exactly the frame held constant across the two poles ({Hsn = *al-ḥusnā*, ysr = *nuyassiruhu … yusrā/ʿusrā*}),
while the three giver-pole markers and three miser-pole markers are pairwise disjoint.

**Result (`csv/Q092-F-01.json` → `arm_B_frame_pole`):**

| Component | Value | Test |
|:--|:--|:--|
| frame | {Hsn, ysr} | — |
| shared roots ⊆ frame | {Hsn, ysr} ⊆ {Hsn, ysr} | **True** |
| giver poles | {ETw, Sdq, wqy} | — |
| miser poles | {bxl, gny, k\*b} | — |
| pole-marker intersection = ∅ | {ETw, Sdq, wqy} ∩ {bxl, gny, k\*b} = ∅ | **True** |
| frame in both blocks | {Hsn, ysr} ⊆ (G ∩ M) | **True** |
| **PASS** | — | **True** |

**Verdict: PASS — the overlap is frame-driven.** The shared content is *exactly* the antithesis frame
(*al-ḥusnā* + the *nuyassiru … li-l-{yusrā/ʿusrā}* easing-formula); the pole markers (*aʿṭā/ittaqā/ṣaddaqa*
vs *bakhila/istaghnā/kadhdhaba*) are perfectly disjoint. This is the **mechanism** behind Arm A's positive
overlap: the muqābala is *one argument-frame with two opposed values*, the within-surah analogue of
H-NEW-2360's Sub-test B (a robust shared frame coexists with opposed poles). Note that the "easing" root
**ysr** is part of the *shared* frame — the surah eases the soul toward *both* yusrā and ʿusrā (the
*iʿmalū fa-kullun muyassar* of the qadar ḥadīth, `04-hadith-corpus.md`), so the very word for "facilitation"
is the constant, and the divergence is carried by the poles.

---

## Q092-F-01 Arm C — title-density-independence: Q 92's own title-root *lyl* (CONFIRMS H-NEW-1820)

**Hypothesis (deterministic, direction-locked Q 92 rank > 1):** Q 92 al-Layl is NOT rank-1 in its title-root
*lyl* (*layl*, "night"), confirming the H-NEW-1820 title-density-independence majority law.

**Result (`csv/Q092-F-01.json` → `arm_C_title_density`; QAC `data/morphology/root-index.json`):**

| Quantity | Value |
|:--|:--|
| *lyl* total corpus attestations | **92** across **49** surahs |
| rank-1 surah in *lyl* | **Q 2 al-Baqara (5×)** |
| Q 92 *lyl* count | **1** (only v 1, *wa-l-layl*) |
| **Q 92 rank in *lyl* density** | **48 / 49** |
| confirms H-NEW-1820 | **True** |

**Verdict: CONFIRMS H-NEW-1820 — and quantifies an extreme.** Q 92 is named al-Layl yet uses *lyl* exactly
**once** and ranks **48th of the 49** surahs containing the root — one of the most extreme confirmations of
the title-density-independence law in the corpus (the eponym is rank-near-last in its own title-root). The
surah is named for its **rhetorical opening image** (*wa-l-layli idhā yaghshā*), not its lexical frequency,
exactly as al-Suyūṭī's naming-conventions framing (*Itqān* nawʿ 17, asmāʾ al-suwar) implies and H-NEW-1820
formalises (47/89 eponymous surahs not rank-1; the majority phenomenon).

---

## Bonferroni / family summary

Q092-F-01 has **one permutation cell** (Arm A, A-H1); α_corrected = 0.05/1 = 0.05 (per the pre-reg; Arms B
and C are deterministic and do not consume α). For the Q 92 session this is the single landed test.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1) | permutation (α = 0.05) | J = 0.2222, z = +2.65, p = 0.0327 (repl 0.0329) | **CONFIRMS H-NEW-2360 (overlap-positive)** |
| B | deterministic | shared = frame {Hsn, ysr}; poles disjoint | **PASS (frame-driven)** |
| C | deterministic | Q 92 *lyl*-rank 48/49 | **CONFIRMS H-NEW-1820** |
| **Q092-F-01 overall** | — | A ✓ + B ✓ + C ✓ | **CONFIRMED (3/3, no pre-commit violation)** |

## What the finding teaches (and the cross-finding it closes)

Q 92's giver/miser muqābala is the **mirror-image** of the Q 83 al-Muṭaffifīn sijjīn↔ʿilliyyīn showcase.
Both are textbook *muqābalāt* (al-Suyūṭī, Itqān nawʿ 59). But:

- **Q083-F-01** (§10.99) hand-selected a muqābala whose two destiny-blocks share only the bare
  *kitābun marqūm / mā adrāka* frame (3 roots vs null 12.7) with **perfectly disjoint** destiny-lexica —
  this looked like a "muqābala = minimal frame + disjoint content" law.
- **H-NEW-2360** (§10.103) then ran a corpus-wide GENERATOR over 3,853 antithetical W=5 block-pairs and
  **REJECTED** that candidate law: antithetical pairs share **MORE** content than random (z = +13.0), because
  block-antithesis is a *jadal*/disputation register where two poles of one argument share its vocabulary;
  the disjoint showcases (Q 83) were hand-picked closed-catalogue rarities.
- **Q098-F-01 Arm D** then replicated the jadal-overlap law at *verse-pair* scale (J = 0.083 > null; locked
  disjoint direction reversed).
- **Q092-F-01 Arm A** now confirms the **same direction at single-surah hand-block scale** (z = +2.65): the
  giver/miser muqābala is content-**overlapping** and **frame-driven**.

So Q 92 is the **third independent confirmation** of H-NEW-2360 over the rejected disjoint-content candidate,
and the clean *positive* counterpart to the Q 83 rarity: a hand-found showcase muqābala that, unlike Q 83's
closed destiny-catalogue, behaves exactly as the corpus law predicts. The lesson, consistent with the
scale-of-aggregation programme (cross-finding-025): Quranic antithesis is **frame-shared + pole-opposed**,
and at the content level it *overlaps* (jadal) rather than depletes — the disjoint cases are the exception,
not the rule. al-Suyūṭī's nawʿ 59 figure is real and marked; only its over-generalized "disjoint-content"
form fails, and Q 92 confirms it fails here too.

## MW protections applied

- **MW-1 (instrument-prior):** Jaccard on QAC stem-roots, the block definition (vv 5–7 / 8–10), the
  frame/pole partition, and the *lyl*-rank metric were all fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** Arm A used 10,000 same-surah length-matched permutations (≥ project minimum).
- **MW-3 (alternative-models):** Arm B reports the explicit frame-vs-pole mechanism separating "overlap"
  (Arm A) from "why" (Arm B), rather than a single J.
- **MW-5 (replication):** Arm A is seed-locked (20260509) with a second-seed replication (20260601,
  p = 0.0329, materially identical); Arms B and C are deterministic and fully replicable from the
  no-tashkeel JSON + QAC root-index.
- **MW-6 (instrument-control):** Arm A's random same-surah length-matched block-pairs are the non-target control.
- **MW-7 (post-hoc cap):** the giver/miser antithesis and the *lyl*-rank were noticed during close reading
  and promoted to direction-locked pre-registered tests BEFORE computation; the single-test α = 0.05 cap is
  respected. Arm A's direction was locked to the H-NEW-2360 prior (OVERLAP), not chosen post-hoc.

## Cross-finding integration

- **H-NEW-2360 (§10.103)** — Arm A is a third independent confirmation of the jadal/overlap direction
  (after the corpus generator itself and Q098-F-01 Arm D), and the positive showcase counterpart to the
  rejected disjoint candidate.
- **Q083-F-01 (§10.99)** — Q 92's giver/miser is the *overlap-positive* mirror of Q 83's disjoint
  sijjīn↔ʿilliyyīn showcase; together they bracket the muqābala-overlap spectrum (Q 83 = the rare exception,
  Q 92 = the law).
- **Q098-F-01** — verse-pair-scale jadal-overlap replication; Q 92 is the block-scale companion.
- **H-NEW-1820** — Arm C is one of the most extreme on-corpus confirmations (Q 92 rank 48/49 in *lyl*).
- **cross-finding-025 (scale-of-aggregation)** — Arm A + Arm B add the showcase-muqābala data point:
  frame-overlap dominates at the antithesis-block scale.

## Honest limits

- Arm A's null pools same-surah 3-consecutive-verse blocks with root-cardinality matched to (5, 6) within
  ±2; a tighter/wider tolerance or a different block-length would shift null-mean slightly but cannot erase a
  z of +2.65. p = 0.033 clears α = 0.05 but is not deep into the tail — Arm A is a *confirmation at the
  showcase scale*, not a law-strength corpus result (the corpus result is H-NEW-2360 itself, z = +13.0).
- The overlap J = 0.2222 is driven by **two** shared frame roots out of nine union-roots; the result is
  small-N at the single-surah scale (hence the explicit replication seed and the corpus-law anchor).
- Arm C's "rank 48/49" uses raw QAC `lyl` attestation counts (no length normalisation); a per-verse-density
  normalisation would re-order the long surahs but cannot lift a 1× count to rank-1, so the qualitative
  conclusion (Q 92 not rank-1, extreme low rank) is robust.

---

*Computed 2026-05-30, seed 20260509 / replication 20260601, 10,000 perms, SHA-locked pre-reg verified at
runtime. Script: `scripts/Q092_F_01_giver_miser_antithesis.py`; JSON: `csv/Q092-F-01.json`. By Waiel Al-Shujaa.*
