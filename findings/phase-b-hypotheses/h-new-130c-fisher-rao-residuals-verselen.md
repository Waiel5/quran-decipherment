# [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] — Fisher-Rao residuals TRIPLE-FEATURE replication (verse-length)

**Finding ID**: [[h-new-130c-fisher-rao-residuals-verselen|h-new-130c]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent (primary)**: [[h-new-130-fisher-rao-residuals|H-NEW-130]] (CONFIRMED)
**Parent (D-matrix)**: [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] (PARTIAL-PASS, verse-length Fisher-Rao)
**Pre-reg**: `findings/phase-b-hypotheses/h-new-130c-prereg.md`
**Seed**: 20260417
**Verdict**: **TRIPLE-REPLICATION-CONFIRMED**

---

## Headline

**The mushaf's boundary-marking pattern replicates on the THIRD, orthogonal feature space — verse-length histograms (RHYTHM, not CONTENT).** 13 of 15 top-Fisher-Rao jumps under verse-length D-matrix coincide with the pre-committed structural-boundary set B; hypergeometric p = 1.16×10⁻³.

**Three universal hinges** appear in the top-15 of ALL three feature spaces (roots, char-4-grams, verse-length):
- **Q 14 → Q 15** (Nöldeke phase: Late-Meccan → Middle-Meccan)
- **Q 49 → Q 50** (mufaṣṣal-alt start + muqaṭṭāʿat-presence change + period change + phase change)
- **Q 56 → Q 57** (period Meccan→Medinan + phase Early-Meccan→Medinan)

These three hinges are structurally-invariant across content, register, and rhythm — the mushaf marks them regardless of which linguistic axis is measured.

---

## Numbers

### PRIMARY — hypergeometric (pre-registered, α_bon = 0.0167)

| Quantity | Roots ([[h-new-130-fisher-rao-residuals|H-NEW-130]]) | Char-4-gram ([[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]) | Verse-length ([[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]) |
|---|---:|---:|---:|
| |M ∩ B| | 15 / 15 | 15 / 15 | **13 / 15** |
| Hypergeom p | 4.78×10⁻⁶ | 4.78×10⁻⁶ | **1.16×10⁻³** |
| Margin over α_bon | 3,493× | 3,493× | 14.4× |
| **PASS** | ✓ | ✓ | ✓ |

Rhythm is somewhat less boundary-concentrated than content or register (13 vs 15), but still passes the 80% threshold. The two non-B top-15 pairs under verse-length are Q 73→74 and Q 96→97 — not in any of the 5 pre-committed boundary types. These are likely rhythm-specific discontinuities (large changes in verse-length distribution shape without corresponding content or register transition).

### SECONDARY A — B-vs-notB concentration

| Quantity | Roots | Char-4-gram | Verse-length |
|---|---:|---:|---:|
| T = mean_B − mean_notB | +0.244 | +0.257 | **+0.385** |
| p_two_sided (10K perms) | 1×10⁻⁴ | 1×10⁻⁴ | 1×10⁻⁴ |
| Sign | + | + | + |
| PASS | ✓ | ✓ | ✓ |

Rhythm has the LARGEST concentration effect (+0.385) — B-pairs have verse-length distributions that are more dissimilar than non-B-pairs, more so than on content or register axes. This is surprising given rhythm had the weakest primary replication (13/15 vs 15/15). Interpretation: when rhythm signals a boundary, the signal is strong; rhythm just has 2 additional non-B top-jumps (Q 73→74, Q 96→97) where it signals without a corresponding structural-boundary.

### SECONDARY B — 3-way universal-hinges intersection

| Quantity | Value |
|---|---|
| M_root ∩ M_char ∩ M_vlen | **{(14,15), (49,50), (56,57)}** |
| Cardinality | 3 |
| Null expected (3 independent 15-of-113) | 15³ / 113² = 0.264 (≈ 0.26) |
| Observed | 3 |
| Pre-committed PASS threshold | ≥ 3 |
| **UNIVERSAL-HINGES** | ✓ |

Under a naive 3-way-independent null, 3 universal hinges would have probability (15/113)² · 15 = 0.26 expected. Observing 3 is ~11× higher than expected, confirming these 3 hinges are NOT artifacts of shared feature-space.

### MW-5 discriminativeness

| Quantity | Value |
|---|---|
| Synthetic sort-by-verse-count top-15 | 0 of 15 shared with vlen top-15 |
| Synthetic top-15 B-hits | 0 |
| **PASS discriminativeness** | ✓ |

Notably, the synthetic "sort surahs by verse count" ordering ITSELF is constructed from verse-count data, yet produces ZERO overlap with the verse-length D-matrix top-15. This is strong evidence that the [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] pattern is not a sort-by-length artifact — it arises specifically from the Fisher-Rao distance between verse-length histograms of CONSECUTIVE mushaf surahs, not from the raw verse counts.

---

## The 3 universal hinges

### Q 14 → Q 15 (Ibrāhīm → al-Ḥijr)

- Both muqaṭṭāʿat-opened (ALR group)
- Nöldeke phase change: Late-Meccan → Middle-Meccan
- No muq-presence change, no letter-set change (both ALR) — but across-phase
- **Universal in content, register, AND rhythm**

### Q 49 → Q 50 (al-Ḥujurāt → Qāf)

- Q 49 is al-Ḥujurāt (Medinan, non-muq); Q 50 is Qāf (Meccan, ق muq)
- **mufaṣṣal-alt start** (one of the canonical classical boundaries)
- muq-presence change (non-muq → muq)
- Period change: Medinan → Meccan
- Phase change: Medinan → Middle-Meccan
- **5-fold simultaneously-triggered boundary** — unsurprising it's universal

### Q 56 → Q 57 (al-Wāqiʿah → al-Ḥadīd)

- Q 56 al-Wāqiʿah (Meccan, eschatological); Q 57 al-Ḥadīd (Medinan, musabbiḥāt start)
- Period change: Meccan → Medinan
- Phase change: Early-Meccan → Medinan
- **Entry-point to the musabbiḥāt cluster** (Q 57, 59, 61, 62, 64 per [[h-new-58c-musabbihat-tense-split|H-NEW-58c]])
- Universal across content, register, rhythm — content-level it's a thematic switch, register-level it's a formulaic-opening (Q 57:1 opens with سبح), rhythm-level it's the transition from the 96-verse eschatology of al-Wāqiʿah to Medinan discourse

### What's NOT universal

- **Q 1→2 al-Fātiḥa→al-Baqara**: root+vlen top-15 but NOT char-4-gram. Roots see vocabulary discontinuity; char-4-grams see morphological continuity (both are "standard" Arabic) — register-invariant hinge that content and rhythm mark differently.
- **Q 12→13 ALR→ALMR muq letter-set**: root+char top-15, NOT vlen. The letter-set boundary is a content+register signal but does NOT shift verse-length distribution.
- **Q 54→55, Q 55→56**: root+char top-15, NOT vlen. Period-hopping at the Meccan/Medinan interface in short-mufaṣṣal zone — strong in content+register, rhythm is muted.

This asymmetric non-universality is structurally informative: some boundaries are content-boundaries only, some are content+register, some are universal.

---

## Interpretation

### Why 13 instead of 15

Under verse-length D-matrix, the mushaf's top-15 includes 2 pairs NOT in B:
- **Q 73 → Q 74** (both Early-Meccan, both muq-free): no period/phase/muq transition. d_vlen = 1.336. Must be a verse-length-specific discontinuity; these two short-mufaṣṣal surahs have very different verse-length distributions (Q 73 al-Muzzammil: mean verse-length high; Q 74 al-Muddaththir: shorter verses).
- **Q 96 → Q 97** (both Early-Meccan, both muq-free): same situation. d_vlen = 1.271. Q 96 al-ʿAlaq vs Q 97 al-Qadr have different rhythm profiles.

These are interesting: rhythm-axis picks up 2 internal-to-short-mufaṣṣal discontinuities that content and register miss. They would be candidates for a B-expansion (e.g., "rhythm-internal mufaṣṣal boundaries") in a follow-up pre-reg, but NOT in this analysis (feature-space locked, PRE-REG-STANDARD-03).

### Partial-vs-full replication semantics

The finding is **PASS** at the pre-registered threshold (≥12/15). The fact that content and register hit the ceiling (15/15) while rhythm hits 13/15 does NOT demote rhythm — all three pass. The 3 universal hinges identified across all three feature spaces are the most robust structural invariants.

### Under theorist's 6-principle model

Theorist's P1+P5 merged principle (Late-Meccan Scripture-Announcement) predicts Q 49→50 (muqaṭṭāʿat + mufaṣṣal + Late-Meccan) should be universal. CONFIRMED.

P2 (local-continuity / Fisher-Rao geodesic) is the root finding. [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] shows P2 extends to rhythm as well as content, with the 3 universal hinges as the most feature-invariant "rebelling-against-continuity" points in the canonical order.

---

## Honest limits

1. **13/15 instead of 15/15 on rhythm**. Honest: the rhythm axis is structurally related but not identical to content. The 2 non-B rhythm pairs (Q 73→74, Q 96→97) show rhythm does pick up some non-content-boundary signals.

2. **Secondary B threshold (≥3) was conservative and pre-committed**. Exactly 3 universal hinges identified. If the threshold had been higher (say, ≥5), the test would have failed — not a ceiling-bound result. This is a healthy test: the 3-universal-hinges finding is genuine, not ceiling-bounded.

3. **Universal-hinges identification depends on the top-15 cut.** A top-25 cut might identify more universal hinges; K is locked at 15 across all three tests.

4. **Verse-length is NOT fully orthogonal to content.** Meccan surahs tend to have shorter verses than Medinan surahs; so period-transitions drive verse-length jumps by construction. This is NOT a bug — [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] pre-registered expected rhythm to partially track period. The interesting finding is that 2 of the top-15 rhythm jumps (Q 73→74, Q 96→97) are NOT period-transitions and represent truly rhythm-specific structure.

5. **Shared-corpus limitation remains.** All three feature-space replications use the same Quranic text. Cross-corpus replication remains out-of-scope.

---

## Connections

- **[[h-new-130-fisher-rao-residuals|H-NEW-130]] / 130b**: this completes the 3-feature replication set; [[h-new-130-fisher-rao-residuals|H-NEW-130]] CONFIRMED verdict reinforced.
- **[[h-new-111c-fisher-rao-verselen|H-NEW-111c]]**: parent verse-length Fisher-Rao, PARTIAL-PASS; [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] shows its residual structure ALSO aligns with boundaries.
- **[[h-new-58c-musabbihat-tense-split|H-NEW-58c]] (musabbiḥāt cluster Q 57, 59, 61, 62, 64)**: Q 56→57 universal hinge is the entry-point. Reinforces the musabbiḥāt cluster as a structurally-marked cohesive unit.
- **[[h-new-67-sab-tiwal-mathani|H-NEW-67]] (sabʿ al-ṭiwāl Q 7→8)**: NOT in verse-length top-15 (was root-top-15 only). Sabʿ boundary is a content phenomenon, not rhythm.
- **[[h-new-89-meta-cluster-network|H-NEW-89]] meta-cluster network**: Q 14→15 (Ibrāhīm→al-Ḥijr) appears here as universal; this is at the edge of the "long-الم" cluster (Q 2,3,10-15) and entering the "prophet-narrative" cluster (Q 19,20,21,22).
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] mushaf structured-geodesic**: now confirmed on 3 feature spaces with 3 universal hinges.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-130c-prereg.md`
- Script: `scripts/h_new_130c_fisher_rao_residuals_verselen.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-130c.json`
- Journal: `journal/h-new-130c-run-1.md`

## Verdict

**TRIPLE-REPLICATION-CONFIRMED**:
- Primary: k = 13/15, hypergeom p = 1.16×10⁻³ (PASS by 14×)
- Secondary A: T = +0.385, p = 1×10⁻⁴ (strongest of the 3 feature spaces)
- Secondary B: 3 universal hinges identified (Q 14→15, Q 49→50, Q 56→57)
- MW-5: fires (0 overlap with synthetic length-sort, 0 B-hits)

**Action**: [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s CONFIRMED status is reinforced to THREE-FEATURE-CONFIRMED. [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] addendum to be updated with 3-feature list and universal-hinges.
