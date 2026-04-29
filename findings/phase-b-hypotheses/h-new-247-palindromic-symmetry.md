# [[h-new-247-palindromic-symmetry|H-NEW-247]] — Palindromic surah-pair symmetry (k ↔ 115-k)

**Finding ID**: [[h-new-247-palindromic-symmetry|h-new-247]]
**Date**: 2026-04-17
**Specialist**: [[h-new-247-palindromic-symmetry|h-new-247]]-specialist
**Pre-reg**: `findings/phase-b-hypotheses/h-new-247-palindromic-symmetry-prereg.md`
**Pre-reg SHA-256**: `721e241bd0eb33480594f6732ae051af44b1c50a577a94b3f9e28864ab3c2b2a`
**Parent D-matrix SHA-256 ([[h-new-111-fisher-rao-mushaf|H-NEW-111]])**: `4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc`
**Seed**: 20260419
**Rules tuple**: (no-tashkeel, 114 surahs, 57 pairs {(k,115-k)}, QAC-STEM K=500 via [[h-new-111-fisher-rao-mushaf|H-NEW-111]], Hafs-Kūfan)
**Bonferroni**: k=4, α_bon=0.0125, N_perms=1000
**Verdict**: **NULL** (0/4 cells PASS; all four cells register SIGNIFICANT ANTI-PALINDROMIC effects — palindromic pairs are *less* structurally coherent than random pairings)

---

## Headline

**Palindromic pairing (k ↔ 115-k) is NOT a structural layer of the
mushaf.** Across 4 pre-registered cells (Fisher-Rao distance, shared
top-50 roots, muqaṭṭaʿāt concordance, log-length Spearman), 0/4 PASS
at α_bon = 0.0125. More strikingly, **all 4 cells are significantly
shifted in the OPPOSITE direction of the pre-registered palindromic
hypothesis** — palindromic pairs are z-score-distant from random
pairings *away from* structural similarity, not toward it. This
**confirms and sharpens** the sibling H-NEW-204 NULL on reverse-mushaf
boundary-Spearman: the mushaf ring topology is localized at the
terminus-to-origin wrap-around edge (Q 1 ↔ Q 108-114) and does NOT
generalize to a fold-symmetric palindromic architecture about the
mushaf midpoint Q 57/58.

---

## Numbers

### Four pre-registered cells (α_bon = 0.0125, N_perms = 1000)

| Cell | Statistic | Observed | Null mean | Null SD | z | p_perm | Direction | Verdict |
|:-:|:---|---:|---:|---:|---:|---:|:-:|:-:|
| (a) | Mean FR distance over 57 pairs | **1.0467** | 0.9231 | 0.0194 | **+6.39** | 1.000 (lower) | anti-pred | **NULL** |
| (b) | Mean shared top-50 roots | **8.72** | 11.00 | 0.452 | **−5.04** | 1.000 (upper) | anti-pred | **NULL** |
| (c) | Muq concordance count (/57) | **28** | 35.42 | 2.840 | **−2.61** | 1.000 (upper) | anti-pred | **NULL** |
| (d) | Spearman(log n_v(k), log n_v(115-k)) | **−0.466** | 0.0004 | 0.132 | **−3.52** | 1.000 (upper) | anti-pred | **NULL** |

**Anti-palindromic-structure signal**: the observed z-scores are NOT
distributed near zero; they sit 2.6–6.4 SD on the anti-palindromic side
of the null. The test answers its primary question clearly in the
**NEGATIVE**, and additionally provides a secondary observation (not
pre-registered as inferential): **random pairings are, on average, MORE
structurally coherent than palindromic pairings.** This is a
mechanical consequence of the mushaf's approximate length-descending
ordering, not a "surprise."

### Top-5 palindromic pairs by Fisher-Rao proximity

| Rank | Pair | d_FR | Notes |
|:-:|:-:|---:|:---|
| 1 | **Q 1 ↔ Q 114** | **0.3884** | The [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] wrap-around pair — an OUTLIER |
| 2 | Q 49 ↔ Q 66 | 0.8111 | al-Ḥujurāt ↔ al-Taḥrīm (both Medinan short; community/household themes) |
| 3 | Q 32 ↔ Q 83 | 0.8223 | al-Sajda ↔ al-Muṭaffifīn |
| 4 | Q 52 ↔ Q 63 | 0.8403 | al-Ṭūr ↔ al-Munāfiqūn |
| 5 | Q 53 ↔ Q 62 | 0.8447 | al-Najm ↔ al-Jumuʿa |

The (1, 114) pair is 0.42 SD below the corpus mean (0.81); the next-
closest palindromic pair (Q 49 ↔ Q 66) is AT the corpus mean
(0.81±ε). The ring-wrap-around at (1, 114) is not a representative
palindromic "closure" — it is the single short edge of a larger cycle
that is otherwise ANTI-mirrored.

### Leave-Q1-out sensitivity (descriptive)

Dropping the (1, 114) pair does not rescue any cell; all observed
statistics drift slightly further from the PASS direction (cell a:
1.047 → 1.058; cell b: 8.72 → 8.82; cell c: 28 → 27; cell d: −0.466 →
−0.515). The 0/4 result is not driven by the terminal pair — it is a
global mushaf-architecture property.

### Muqaṭṭaʿāt concordance breakdown

- Both-muq pairs: **0 / 57**
- Both-non-muq pairs: **28 / 57**
- Discordant pairs: **29 / 57**
- Null-expected concordance: 35.4 / 57

The 29 muq surahs sit almost entirely in the first half of the mushaf
(26 of 29 are in Q 1-50). Their palindromic partners 115-k are almost
all short back-half surahs, none of which are muq-opened (the muq
surahs in the back half — Q 68 — has partner Q 47 al-Muḥammad, also
non-muq). Zero both-muq pairs is the extremum.

### Length-reflection (cell d) — the strongest anti-signal

Observed Spearman(log n_v(k), log n_v(115-k)) = **−0.466**. This is a
strong *anti-correlation*: long surahs in the first half pair with
SHORT surahs in the back half (a known gross property of the mushaf,
since the ordering is approximately length-descending and the back half
is the short-mufaṣṣal). The palindromic pairing *maximally violates*
length-similarity. Null mean is essentially zero (0.0004), SD = 0.132,
z = −3.52. A POSITIVE-direction mean-reflected reformulation would be
a post-hoc rescue and is not pursued; we simply report the negative
observed as the honest descriptive answer.

---

## Interpretation

### Re ring-topology layers

[[cross-finding-013-mushaf-topological-ring|Cross-finding-013]] established the mushaf as a topological RING with
three layers:

- **Layer 1** (Hamiltonian-path geodesicity): CONFIRMED
- **Layer 2** (wrap-around closure Q 1 ↔ Q 108-114): CONFIRMED
- **Layer 3** (structured boundary-hinges): CONFIRMED

[[h-new-247-palindromic-symmetry|H-NEW-247]] asked whether a **Layer 4 "folded ring" structure** exists
— i.e., whether the Hamiltonian cycle is not just a ring but a
*palindromically folded* ring. The answer is **NO, with
high-confidence statistical backing**. The ring topology is:

- A nearly-optimal Hamiltonian CYCLE (short path + short wrap-edge)
- **NOT a palindrome-symmetric cycle** under the natural k↔115-k fold.

The wrap-around closure (Q 1 ↔ Q 114) is NOT representative of a
folded symmetry; it is the single short edge completing an
otherwise-non-symmetric cycle. Combined with the H-NEW-204 boundary-
mirror Spearman NULL, we can now say: **reflective/palindromic
symmetry about the mushaf midpoint is NOT a structural principle of
the Uthmanic order.** The ring is real; the fold is not.

### Re classical anchors

- al-Suyūṭī's *Itqān* discusses the 7-ṭiwāl opening and short-
  mufaṣṣal closing as structurally meaningful groupings but does NOT
  propose k↔115-k palindromic pairing. Our NULL is consistent with
  al-Suyūṭī's actual position (he treats groupings, not mirrors).
- Farāhī / Iṣlāḥī (*Niẓām al-Qurʾān*) propose **naẓm-groups** (surah
  clusters thematically linked) but NOT palindromic pairing between
  halves. Our NULL is consistent with Farāhī-Iṣlāḥī.
- al-Biqāʿī's *Naẓm al-Durar* proposes **adjacent munāsabāt** (local
  inter-surah coherence) but not folded symmetry. Consistent with the
  [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] Layer 1 geodesicity, not contradicted by the
  palindromic NULL.
- The [[h-new-158-mirror-pair-uniqueness|H-NEW-158]] Tier-1 ±58 mirror pair (Q 49→50 / Q 56→57) is a
  LOCAL structural hinge, not a palindromic fold; it sits WITHIN
  Layer 3 (structured hinges), not at Layer 4 (folded ring). [[h-new-247-palindromic-symmetry|H-NEW-247]]
  is consistent with [[h-new-158-mirror-pair-uniqueness|H-NEW-158]]'s single-mirror-pair claim by refuting
  the over-generalization.

### Anti-palindromic as a mechanistic signal

The observed z-scores' uniform anti-palindromic direction is
interpretable: the mushaf is approximately **length-descending** (Q 2
is the longest, Q 108-114 the shortest). Palindromic pairing therefore
deliberately MATCHES longest-with-shortest, which is the anti-geodesic
direction in FR space (short and long surahs have very different root
distributions). Any length-correlated feature (root-distributions,
shared vocabulary, muq-opening which correlates with length) will show
anti-palindromic z-scores as a mechanical consequence.

This is not a "surprise anti-finding" — it is the **predicted
consequence of the existing length-ordering principle** operating in a
direction orthogonal to the palindromic hypothesis. [[h-new-247-palindromic-symmetry|H-NEW-247]] thus
also serves as a **negative control** for length-based structural
principles: if any FUTURE test of reflective symmetry fails to condition
on length, it will replicate this anti-palindromic artifact.

### Re [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] synthesis

No update to [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s ring claim. The synthesis statement
**"the mushaf is a structured Hamiltonian cycle"** stands; [[h-new-247-palindromic-symmetry|H-NEW-247]]
adds a DISCONFIRMED refinement ("the cycle is NOT palindromically
folded"). The 3-layer architecture is the correct level of
description.

---

## Honest limits

- N = 57 pairs is small; 1000 permutations is adequate for α_bon =
  0.0125 resolution but not for finer (e.g. α = 0.001) detection.
  Weak palindromic sub-effects at N < 57 subsets are not ruled out.
- Palindromic pairing under k↔115-k is ONE symmetry among many.
  Possible alternative folds (block-wise 7-14-… pairings; Farāhī
  group-by-group mirrors; junction-centered folds at Q 50 vs Q 57.5)
  are NOT tested here.
- Cells (a), (b), (d) share length-covariance; cell (c) is the
  only cell fully independent of length. The anti-palindromic
  direction is strongest on length-sensitive cells (cells a, d) and
  weakest on the length-independent cell c (z = −2.61). This is
  consistent with the length-descending-ordering mechanistic story.
- The muq concordance 0/57 both-muq is an extreme point statistic; with
  only 29 muq surahs and a back-half deficit, a null draw expects ~1.5
  both-muq pairs. The observed 0 is ~1.5 SD low but not by itself
  diagnostic of anti-palindromic intent.

---

## Verdict

| Cell | Verdict |
|:-:|:-:|
| (a) FR distance | **NULL** (anti-predicted direction z=+6.39) |
| (b) shared roots | **NULL** (anti-predicted direction z=−5.04) |
| (c) muq concordance | **NULL** (anti-predicted direction z=−2.61) |
| (d) length-reflection Spearman | **NULL** (anti-predicted direction z=−3.52) |
| **OVERALL** | **0/4 PASS → NULL; palindromic pairing is NOT structural** |

**Recommended framing**: [[h-new-247-palindromic-symmetry|H-NEW-247]] is a HIGH-CONFIDENCE NULL that
**localizes [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s ring topology** — the ring is
geodesic (Layer 1), has a short wrap-around closure edge (Layer 2),
has structured boundary hinges (Layer 3), and **is NOT palindromically
folded (no Layer 4)**. This is a useful scope-limit on the ring claim:
it rules out an intuitive but unsupported over-generalization.

Consistency with H-NEW-204 (reverse-mushaf boundary-mirror Spearman
NULL) is exact: both findings say "no mirror symmetry about the
midpoint." [[h-new-247-palindromic-symmetry|H-NEW-247]] strengthens this by testing the surah-pair
level rather than the boundary-pair level and by covering 4
orthogonal feature spaces rather than 1.

---

## Connections

- **Parent**: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] (ring topology CONFIRMED). [[h-new-247-palindromic-symmetry|H-NEW-247]]
  tests Layer 4 "folded ring" hypothesis and returns NULL. No
  update to [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s three-layer synthesis.
- **Sibling**: H-NEW-204 (reverse-mushaf boundary Spearman NULL).
  [[h-new-247-palindromic-symmetry|H-NEW-247]] replicates and generalizes the no-mirror-symmetry
  finding to the surah-level across 4 feature spaces.
- **[[h-new-158-mirror-pair-uniqueness|H-NEW-158]]** (±58 Tier-1 mirror uniqueness): [[h-new-247-palindromic-symmetry|H-NEW-247]] does NOT
  contradict; the ±58 mirror is a LOCAL hinge within Layer 3, not a
  global palindromic fold.
- **OQ-6** (complete meta-architecture): partial answer — the mushaf
  is a ring but NOT a palindrome. Rules out one class of candidate
  organizing principles.
- **[[cross-finding-014-five-principle-unified-equation|cross-finding-014]] / 018 / 020** (unified equation): no change;
  no principle predicted palindromic pairing.

---

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-247-palindromic-symmetry-prereg.md`
- Script: `scripts/h_new_247_palindromic.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-247.json`
- Journal: `journal/h-new-247-run-1.md`
- Parent D-matrix: `findings/phase-b-hypotheses/csv/h-new-111.json` (sha256 above)
- Related: `findings/phase-b-hypotheses/cross-finding-013-mushaf-topological-ring.md`,
  `findings/phase-b-hypotheses/csv/h-new-204.json` (H-NEW-204 reverse-mushaf JSON)
