---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: prereg
test_id: Q092-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q092-F-01 — Pre-Registration: the giver/miser antithetical pair as a shared-frame *jadal* instance (H-NEW-2360 confirmatory replication)

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q092_F_01_giver_miser_antithesis.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 92 al-Layl closes its opening movement (vv 1–4: the *wa-l-layl / wa-l-nahār / wa-mā khalaqa
al-dhakara wa-l-unthā* oath-triad → *inna saʿyakum la-shattā*, "your strivings are divergent")
with the corpus's cleanest two-pole moral antithesis (vv 5–10):

- **giver pole (vv 5–7):** *fa-ammā man aʿṭā wa-ttaqā · wa-ṣaddaqa bi-l-ḥusnā · fa-sa-nuyassiruhu
  li-l-yusrā* ("as for him who gives and fears God, and affirms the best — We shall ease him toward ease")
- **miser pole (vv 8–10):** *wa-ammā man bakhila wa-staghnā · wa-kadhdhaba bi-l-ḥusnā · fa-sa-nuyassiruhu
  li-l-ʿusrā* ("and as for him who is miserly and deems himself self-sufficient, and denies the best —
  We shall ease him toward hardship")

The two blocks are syntactically parallel down to a shared template: `[ammā] man V₁ wa-V₂ · wa-{ṣaddaqa/
kadhdhaba} bi-l-ḥusnā · fa-sa-nuyassiruhu li-l-{yusrā/ʿusrā}`. al-Suyūṭī (*al-Itqān*, nawʿ 59, *al-ṭibāq
wa-l-muqābala*) and the balāgha tradition identify exactly this figure (ṭibāq/muqābala). The project's
own H-NEW-2360 (§10.103, 2026-05-29) tested at corpus block scale whether antithetical block-pairs have
**disjoint content** (the "muqābala = minimal frame + disjoint catalogue" candidate law) and found the
opposite: antithetical W=5 block-pairs share **significantly MORE** content than random same-surah block-pairs
(content-Jaccard z = +13.0), because block-scale antithesis is a *jadal*/disputation register where two poles
of one argument share its argument vocabulary; only a robust shared **frame** survives (frame-overlap z = +37.9).

This test asks: **does Q 92's hand-found giver/miser antithetical pair — the textbook muqābala — behave
as H-NEW-2360 predicts (OVERLAP-positive, frame-driven), or as the rejected disjoint-content candidate law
predicted (depleted content)?** This is a direction-locked replication of H-NEW-2360 at the single-surah
hand-block scale, and a probe of whether the corpus law transfers to the showcase muqābala that motivated it.

## Rules-tuple

`(no-tashkeel, orthographic-token, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. Roots from QAC v0.4
(`/Users/grey/Downloads/quran/data/morphology/root-index.json`, `[surah,verse,word]` attestations).
Block = set-union of the QAC stem-roots of its member verses. Jaccard J(A,B) = |A∩B| / |A∪B|.

## Blocks (deterministic, from disk)

- **giver block G = roots(v5 ∪ v6 ∪ v7)** = {ETw (aʿṭā), wqy (ittaqā), Hsn (ḥusnā), Sdq (ṣaddaqa), ysr (yusrā)} — 5 roots.
- **miser block M = roots(v8 ∪ v9 ∪ v10)** = {bxl (bakhila), gny (istaghnā), Hsn (ḥusnā), kdb (kadhdhaba), Esr (ʿusrā), ysr (yusrā)} — 6 roots.
- shared = {Hsn, ysr}; J(G,M) = 2/9 = 0.2222.

(These deterministic values are stated here for the record; the SHA lock predates any null computation.)

## Arm A — content-overlap direction (H-NEW-2360 confirmatory, DIRECTION-LOCKED)

**Hypothesis A:** the giver/miser pair shares MORE content than a random same-surah-eligible 3-verse
block-pair of matched root-cardinality, replicating H-NEW-2360's corpus reversal at the showcase-muqābala scale.

- **A-H1 (direction-locked, PRIMARY):** J(G,M) **>** null-mean, and the permutation upper-tail
  p_perm = (#{null J ≥ obs} + 1)/(N+1) **< α** = 0.05. **Direction lock: OVERLAP-positive (TIGHTER than random).**
- **Permutation null A (seed = 20260509, 10000 perms):** draw two disjoint 3-consecutive-verse blocks
  from the same randomly-chosen surah (surah must have ≥6 verses), each block's root-cardinality matched
  to (|G|=5, |M|=6) within ±2 roots; compute J; record the null distribution. p = upper-tail fraction.
  This is the same family of null used in H-NEW-2360 (same-surah block-pairs), adapted to 3-verse hand-blocks.

**A success:** A-H1 holds (J(G,M) > null-mean AND p_perm < 0.05) → **CONFIRMS** the H-NEW-2360 jadal/overlap
direction at the showcase scale.
**A pre-commit violation / NULL:** J(G,M) < null-mean (direction reversed — the muqābala IS content-disjoint,
contradicting the corpus law) → published as NULL with explicit pre-commit-violation flag and full prominence.

## Arm B — frame-vs-pole decomposition (DETERMINISTIC, descriptive)

**Hypothesis B (corpus-mechanism check):** the giver/miser overlap is **frame-driven**, i.e. the shared
roots are the antithesis SCAFFOLD ({Hsn = al-ḥusnā, ysr = nuyassiruhu...yusrā/ʿusrā}) — the part of the
template held constant across the two poles — while the **pole markers** (ETw/wqy/Sdq vs bxl/gny/kdb) are
fully disjoint. **Direction lock (deterministic): shared = exactly the frame {Hsn, ysr}; the 3 giver-pole
markers and 3 miser-pole markers are pairwise disjoint (intersection of pole-markers = ∅).** This is the
within-surah analogue of H-NEW-2360's Sub-test B (a robust shared frame coexists with opposed poles).

**B success:** shared roots ⊆ frame AND pole-marker intersection = ∅ → PASS (frame-driven overlap, as the corpus law predicts).
**B fail:** any pole-marker shared, or a frame root NOT shared → re-describe.

## Arm C — title-density-independence check (H-NEW-1820 confirmatory, DETERMINISTIC)

**Hypothesis C:** Q 92 al-Layl is NOT rank-1 in its own title-root `lyl` (layl, "night"), confirming the
H-NEW-1820 title-density-independence law (47/89 eponymous surahs not rank-1; majority phenomenon).

- **C-H1 (direction-locked, deterministic):** ranking all surahs by QAC `lyl`-root attestation count,
  Q 92's rank is **> 1** (NOT the density peak). **Direction lock: Q 92 rank in lyl > 1.**

**C success:** Q 92 rank > 1 → CONFIRMS H-NEW-1820 (and quantifies how extreme: Q 92 is the eponym of a
root it uses how many times, and at what rank?).
**C reversal:** Q 92 rank == 1 → the hint's "Q92 is rank-1 in its own title-root" would be vindicated and
H-NEW-1820's law would gain a counter-example; published honestly either way.

## Bonferroni

Test family Q092-F-01 has **k = 1 permutation cell** (Arm A, A-H1). Arms B and C are deterministic and do
not consume α. α_corrected = 0.05 / 1 = 0.05.

## Null distributions

- **Null A (Arm A):** same-surah disjoint-3-verse-block pairs, root-cardinality matched to (5,6) within
  ±2, seed = 20260509, 10000 perms. p_perm = (#{null J ≥ obs} + 1)/(N + 1), upper-tail.

## MW protections

- **MW-1 (instrument-prior):** Jaccard on QAC stem-roots, block definition, frame/pole partition, and the
  lyl-rank metric are all fixed here before any run.
- **MW-2 (corpus-prior):** Null A uses 10,000 same-surah length-matched permutations.
- **MW-3 (alternative-models):** Arm B reports the frame-vs-pole decomposition as the explicit overlap
  mechanism; the test thus separates "overlap" (Arm A) from "why" (Arm B) rather than reporting a single J.
- **MW-5 (replication):** Arms B and C are deterministic and fully replicable from the no-tashkeel JSON +
  QAC root-index; Arm A is seed-locked at 20260509. A second seed (20260601) is reported as a replication arm.
- **MW-6 (instrument-control):** Null A's random same-surah block-pairs are the non-target control.
- **MW-7 (post-hoc cap):** the giver/miser antithesis and the lyl-rank were noticed during close reading
  and are promoted to PRE-REGISTERED direction-locked tests here before computation; the single-test
  α = 0.05 cap is respected. Arm A's direction is locked to the H-NEW-2360 prior (OVERLAP), not chosen post-hoc.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | J(G,M) > null-mean ∧ p_perm < 0.05 | CONFIRMS H-NEW-2360 jadal/overlap direction |
| A | J(G,M) < null-mean | NULL (pre-commit violation, full prominence) — muqābala IS disjoint |
| B | shared ⊆ frame ∧ pole-marker ∩ = ∅ | PASS (frame-driven) |
| C | Q 92 lyl-rank > 1 | CONFIRMS H-NEW-1820 |
| C | Q 92 lyl-rank == 1 | H-NEW-1820 counter-example |

Final Q092-F-01 verdict = honest combination of Arms A, B, C, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
