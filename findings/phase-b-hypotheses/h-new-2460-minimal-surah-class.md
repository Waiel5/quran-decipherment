---
finding_id: H-NEW-2460
title: The minimal-surah structural class + the {Q103,Q108} rā'-twin
file_type: novel-findings
date: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
prereg_sha256: 5eef084af1009fccb3142c8100ebc23d429b36f38981ed8efd5883a7a4b0b833
verdict: "Arm A CONFIRMED (power-limited, 1/3 floor) · Arm B CONFIRMED · Arm C CONFIRMED (p=0.0001)"
rules_tuple: "(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2460 — The minimal-surah structural class + the {Q103,Q108} rā'-twin

**Pre-reg** `findings/phase-b-hypotheses/prereg-h-new-2460-minimal-surah-class.md`
(SHA-256 `5eef084af1009fccb3142c8100ebc23d429b36f38981ed8efd5883a7a4b0b833`, runtime-verified, fail-fast).
**Script** `scripts/h-new-2460.py`. **JSON** `findings/phase-b-hypotheses/csv/h-new-2460.json`.
Seed 20260509, 10000 perms (Arm C-H2 only). All values read from disk.

## The minimal-surah class (generator output)

Sorted by Hafs-Kūfan `total_verses`, the corpus tail (≤6 verses, **N=11**; Q1 al-Fātiḥa = 7
verses, excluded) is:

| Surah | Name | v | Type | Verse-finals | Perfect mono? | Shape | mean-FR-to-all-113 | FR-central rank |
|:--|:--|:-:|:--|:--|:--|:--|:--:|:--:|
| Q112 | al-Ikhlāṣ | 4 | Meccan | ددد د | **د (dāl)** | command (qul) | 0.7592 | **1/114** |
| Q110 | al-Naṣr | 3 | Medinan | ح ا ا | — | conditional-temporal | 0.7644 | 2/114 |
| Q108 | al-Kawthar | 3 | Meccan | ر ر ر | **ر (rā')** | declaration (innā) | 0.7718 | 3/114 |
| Q106 | Quraysh | 4 | Meccan | ش ف ت ف | — | causal-decl. (li-) | 0.7803 | 5/114 |
| Q114 | al-Nās | 6 | Meccan | س ×6 | **س (sīn)** | command (qul) | 0.7838 | 6/114 |
| Q113 | al-Falaq | 5 | Meccan | ق ق ب د د | — | command (qul) | 0.7843 | 7/114 |
| Q103 | al-ʿAṣr | 3 | Meccan | ر ر ر | **ر (rā')** | oath (wāw-qasam) | 0.7870 | 9/114 |
| Q105 | al-Fīl | 5 | Meccan | ل ×5 | **ل (lām)** | interrogative-rebuke | 0.7877 | 10/114 |
| Q111 | al-Masad | 5 | Meccan | ب ب ب ب د | — | imprecation | 0.7954 | 15/114 |
| Q109 | al-Kāfirūn | 6 | Meccan | ن ن د م د ن | — | command (qul) | 0.8135 | 19/114 |
| Q97 | al-Qadr | 5 | Meccan | ر ×5 | **ر (rā')** | declaration (innā) | 0.8197 | 24/114 |

Verse-tier counts in the ≤6 frame: 3-verse ×3, 4-verse ×2, 5-verse ×4, 6-verse ×2.
**Primary class (≤4)** = {Q103, Q106, Q108, Q110, Q112}.
**3-verse sub-class** = {Q103, Q108, Q110}.

Structural-shape census: the qul-imperative is the modal opening (4/11: Q109, Q112, Q113, Q114 —
all in the muʿawwidhāt / creedal-tail group), with one each of oath, two declarations (innā),
conditional-temporal, causal, interrogative-rebuke, and imprecation. Only **Q103** is a qasam
(oath) surah (per `h-new-2210.json`). 6 of 11 are perfect strict-final monorhymes.

---

## Arm A — the {Q103,Q108} rā'-twin within the 3-verse sub-class — **CONFIRMED (power-limited)**

- **A-H1 (deterministic) PASS:** of the three 3-verse surahs {Q103, Q108, Q110}, exactly
  {Q103, Q108} are perfect rā'-monorhymes (every verse-final = ر); Q110 al-Naṣr is non-mono
  (finals ح-ا-ا). Holds identically under both no-tashkeel and min-tashkeel.
- **A-H2 (direction-locked) PASS:** in the 3-node FR triangle,
  **d(Q103,Q108) = 0.2399 < d(Q108,Q110) = 0.2684 < d(Q103,Q110) = 0.3238** — the rhyme-matched
  pair is the MINIMUM edge. The locked direction held: the rhyme-twin and the closest edge are
  the SAME pair.

**Honest power note (pre-registered):** with a 3-member class the locked direction A-H2 carries
at most a **1/3 exact-combinatorial floor** (P that a named edge is the triangle minimum under
random labeling = 0.333). This is **underpowered by construction**; A-H2 is reported as an EXACT
corpus fact (the edge IS the minimum), NOT as a significant permutation result. We explicitly
decline to inflate it to a small p-value.

**Honest non-result (reported, not pre-registered as pass/fail):** Q103 and Q108 are **NOT
mutually-nearest neighbors**. Q108 IS Q103's rank-1 FR neighbor (0.2399), but Q108's own rank-1
neighbor is **Q106 al-Quraysh (0.2127)**, not Q103. The {103,108} bond is asymmetric: one-way
nearest, rhyme-matched, and the 3-verse-triangle minimum — a real "twin" within the 3-verse
sub-class, but not a globally reciprocal nearest-neighbor pair.

## Arm B — rhyme-class ⊥ FR-proximity (the honest control) — **CONFIRMED**

- **B-H1 (deterministic) PASS:** the corpus has exactly **four** strict-final rā'-monorhymes:
  **{Q54 al-Qamar, Q97 al-Qadr, Q103 al-ʿAṣr, Q108 al-Kawthar}**.
- **B-H2 (direction-locked) PASS:** among the six pairwise FR distances of these four,
  **{103,108} is the minimum (0.2399)**; the next are {97,108}=0.3321, {97,103}=0.3785; while the
  long 55-verse narrative member **Q54 al-Qamar is FR-DISTANT** from all three short rā'-members
  (mean 0.8626 — i.e. {54,97}=0.8624, {54,103}=0.8739, {54,108}=0.8515).

**Interpretation:** rā'-monorhyme membership does NOT by itself make surahs FR-close — Q54 shares
the rā' rawiyy yet sits ~0.86 from the short rā'-members (about the corpus pairwise mean 0.9235).
So the {103,108} closeness is **not a rhyme artifact**; it is rhyme-match AND root-content
proximity co-occurring. This is the project's recurrent **letter/sound-axis ⊥ content-axis**
result, here at the rhyme-class level (cf. the muqaṭṭaʿāt letter ⊥ content pillar).

## Arm C — minimal-class profile + the FR-central extreme — **CONFIRMED**

- **C-H1 (descriptive) produced:** the full 11-member profile table above + the 11×11 within-class
  FR matrix (in JSON).
- **C-H2a PASS:** within-class mean pairwise FR = **0.3185** vs corpus-wide pairwise mean
  **0.9235** — the minimal class is internally ~3× tighter than the corpus at large.
- **C-H2b PASS:** **all 11/11** minimal-class members rank in the corpus FR-central LOWER HALF
  (rank ≤57/114); 10/11 rank ≤24, and **Q112 al-Ikhlāṣ is the corpus FR-rank-1 most-central
  surah** (smallest mean root-distribution distance to all 113 others).
- **C-H2 permutation (MW-2 / MW-6) PASS:** against 10,000 random size-11 surah subsets
  (seed 20260509), the minimal-class within-class mean FR 0.3185 vs null mean 0.9234 (std 0.0612),
  **z = −9.882, p_perm = 0.0001** (0 of 10,000 random subsets were as cohesive). Direction
  (obs < null) held.

**Interpretation:** the shortest surahs are NOT root-distribution outliers — they are the corpus's
FR-CENTRE. Short surahs lean on the high-frequency common root vocabulary (Allāh, rabb, qul,
nās, the creedal/eschatological core), so they sit close to the corpus centroid and to each
other. This corroborates the established **Q112 / Q113 / Q114 meta-hub** result
(cross-finding-010's 4-way centrality tie {Q62, Q112, Q113, Q114}) from an independent
verse-count-defined direction: Q112, Q113, Q114 are all in this minimal class and all FR-central.

---

## Significance

1. **A new structural class is cataloged and characterized**: the ≤6-verse minimal-surah class is
   (a) overwhelmingly Meccan (10/11; only Q110 al-Naṣr Medinan), (b) FR-central as a body
   (z = −9.88, p = 0.0001 vs random subsets), and (c) qul-imperative-dominated in opening shape.
2. **The {Q103,Q108} rā'-twin is empirically real but precisely bounded**: rhyme-matched +
   3-verse-triangle FR-minimum, **but not mutually-nearest** and **power-limited to a 1/3 floor**.
   The honest framing is: *within the 3-verse sub-class*, the rhyme-twin and the closest edge
   coincide on {103,108} — a clean exact fact, not a high-powered inference.
3. **Rhyme ⊥ content, re-confirmed at the rhyme-class level**: Q54 al-Qamar shares the rā' rawiyy
   yet is FR-distant — the rā'-monorhyme set is NOT an FR cluster; {103,108} happen to be both.

## Honest limits

- **Small-N is the dominant limit.** The 3-verse sub-class has 3 members; the locked Arm A
  direction can carry at most a 1/3 exact null. Arm A is an exact corpus fact, deliberately not
  dressed as a permutation p-value. Arm C's inferential strength comes ONLY from the corpus-wide
  random-subset null (a legitimately powered N=11 vs 114 comparison), not from within the tiny
  class.
- **{103,108} is one-way nearest, not reciprocal.** Reported in full (Q108's true NN is Q106).
- **FR matrix is the QAC-stem-root instrument** (`h-new-111.json`); a different content
  representation (char-n-gram, lemma) could shift the within-class ordering. The class membership
  (verse-counts) and the rhyme facts (verse-finals) are instrument-independent.
- **Rhyme = strict last-grapheme.** A rawiyy-with-vowel definition (min/full-tashkeel) would
  re-segment some non-mono members (e.g. Q110's ا-finals), but does NOT change {103,108}=rā' or
  the corpus rā'-set {54,97,103,108} (re-verified under both no- and min-tashkeel for the 3-verse
  class).

## Cross-references

- [[Q103-al-asr/Q103-F-01-asr-minimal|Q103-F-01]] — promotes Arm A of Q103-F-01 (queued Q103-F-03)
  to corpus-wide; this finding closes that queue item.
- [[cross-finding-010-extended-network|cross-finding-010]] — Q112/Q113/Q114 meta-hub; Arm C
  corroborates from the verse-count axis.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — FR matrix source.
- [[h-new-2210|H-NEW-2210]] — qasam catalog (only Q103 in the minimal class is an oath surah).
- Letter/sound ⊥ content pillar (muqaṭṭaʿāt FALSIFIED 4×) — Arm B is the rhyme-class instance.

*Run 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
