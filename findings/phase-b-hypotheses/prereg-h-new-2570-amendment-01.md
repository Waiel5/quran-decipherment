---
amendment_id: H-NEW-2570-AMENDMENT-01
parent_prereg: findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md
parent_prereg_sha256: 6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b
date: 2026-08-07
author: Waiel Al-Shujaa
type: PRIOR-ART DISCLOSURE + SCOPE NARROWING
effect_on_thresholds: NONE
effect_on_locked_directions: NONE
effect_on_verdicts: NONE
---

# AMENDMENT 01 to the H-NEW-2570 pre-registration

## Why this is a separate file and not an edit

The parent pre-registration is SHA-locked at
`6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b`, and that literal is embedded
in `findings/phase-b-hypotheses/scripts/h-new-2570.py`, which verified it at runtime before the
executed run. **Editing the parent file would change its hash and permanently break the
runtime verification of the run that has already been performed.** The parent is therefore left
byte-identical, and this amendment is recorded alongside it, in the manner of a corrigendum.

| Document | SHA-256 |
|:--|:--|
| Parent pre-reg (unchanged, runtime-verified by the executed run) | `6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b` |
| This amendment | recorded in the findings document on lock; see `h-new-2570-lexical-curriculum.md` §12 |

**This amendment changes no threshold, no null model, no locked direction, no Bonferroni k, and
no verdict.** Bonferroni k remains 12; α_corrected remains 0.0041667; the length-preserving null
N2 remains the primary test; every direction locked in parent §5 stands as locked. Its only
effects are to disclose prior art that the parent failed to cite and to **narrow** the scope of
what H-NEW-2570 claims. A narrowing that removes a novelty claim is permitted post-observation;
a loosening would not be, and none is made.

---

## 1. Prior art the parent pre-registration failed to cite

A reconnaissance survey of the project's 906 files surfaced prior work on the lexical-growth
axis that the parent pre-reg did not know about and should have cited in its
"what was known before lock". All of the following are verified on disk:

### 1.1 [[h-new-123-heap-law|H-NEW-123]] — the parent finding on this axis

`findings/phase-b-hypotheses/h-new-123-heap-law.md`, pre-reg `h-new-123-heap-law-prereg.md`,
script `scripts/h_new_123_heap_law.py`, JSON `csv/h-new-123.json`. Registered and executed
2026-04-17, Bonferroni k = 4, α_bon = 0.0125. Verdict MIXED, 2/4 PASS.

| Corpus | N | V | β | 95% boot-CI |
|:--|--:|--:|--:|:--|
| Qurʾān (no-tashkeel, surface-form) | 77,797 | 14,870 | **0.7468** | (0.729, 0.757) |
| al-Bukhārī (matched 77K window) | 77,797 | 12,154 | **0.7472** | (0.732, 0.759) |
| al-Jāḥiẓ *Kitāb al-Ḥayawān* (first 77K) | 77,797 | 22,984 | 0.8023 | (0.785, 0.811) |
| Muʿallaqāt (7 poems) | 7,285 | 3,843 | 0.8313 | (0.817, 0.849) |
| Qurʾān-shuffled (same multiset) | 77,797 | 14,870 | 0.7072 | (0.689, 0.717) |

- **Cell A1** β_Qurʾān < β_Bukhārī: **FAIL**, p = 0.3826 — essentially tied.
- **Cell B** β_Qurʾān ≠ β_shuffled-Qurʾān: **NULL**, p = 0.3340.

H-NEW-123's own reading of Cell B: *"β is shuffle-invariant, so 'compactness' is carried
entirely by the token-frequency distribution … not by any ordering or positional effect. Any
claim that the Quran's lexical structure depends on its CANONICAL ARRANGEMENT … is unsupported
at the Heap's-law level."*

`findings/HONEST-LIMITS-LEDGER.md` §27e records the corpus-level result as **NOT
Quran-distinctive**: *"Compactness is a genre feature of classical religious/historical prose,
shared with hadith literature, not a Quran-specific signature. The shuffle-within test is NULL
by construction (β is stream-order invariant)."*

### 1.2 Also on the axis, all per-CHAPTER rather than per-ORDERING

- **H-NEW-159** — Heaps β per chapter, Qurʾān vs Bukhārī bab-segments.
- **H-NEW-172** — Zipf α per chapter.
- **H-NEW-178** — the joint (α, β) manifold.
- **H-NEW-179** — (α, β)-residual as a muqaṭṭaʿāt predictor (INCONCLUSIVE).

None of the four tests the *sequence* of surahs; all four characterise surahs individually.

---

## 2. Scope narrowing

### 2.1 What H-NEW-2570 does NOT claim

**The corpus-level Heaps exponent is H-NEW-123's result and is not re-derived here.** Any
statement of the form "the Qurʾān's β is X" belongs to H-NEW-123. H-NEW-2570's cross-corpus
table (parent §7) is demoted from *deliverable* to **consistency check against H-NEW-123**, and
must be recomputed with **H-NEW-123's own estimator** (`fit_heap` / `vocab_curve` /
`normalize` / `tokenize` in `scripts/h_new_123_heap_law.py`; linear grid, step = 50, start = 100;
log-log OLS) so the two findings' numbers are directly comparable. Where H-NEW-2570's
independent implementation disagrees with H-NEW-123, H-NEW-123 is authoritative for the
corpus-level claim and the discrepancy is to be reported as a normalization or source-file
difference, not as a new estimate.

Parent §7 already forbade inference on this section ("no hypothesis is registered on it and no
p-value is computed for it"). That restriction is retained and reinforced: the section is
descriptive, MW-7 capped, and now additionally subordinate to H-NEW-123.

### 2.2 Cells 11 and 12 are reclassified as a replication, not a novel test

Parent §5 registered cells 11/12 (β_mushaf vs the N2 and N1 surah-permutation nulls) under the
label "H-DEFER", presented as novel. **Given H-NEW-123 Cell B, they are not novel**: β was
already shown to be near-invariant to shuffling the Qurʾān's token stream, and a permutation of
surahs is a weaker perturbation than a full token shuffle. Cells 11/12 are therefore reclassified
as an **independent replication of H-NEW-123 Cell B at the surah-permutation level**.

The locked direction (β_mushaf HIGHER), the null models, and α are unchanged; the cells remain in
the Bonferroni family at k = 12. Only the *novelty claim* is withdrawn. Note that this narrowing
is made against my own interest: it converts two cells from "novel test" to "replication", and
their observed outcome — NULL, direction violated — is thereby rendered *expected* rather than
surprising.

### 2.3 What H-NEW-2570 continues to claim, sharpened

H-NEW-2570's subject is **the ordering of the 114 surahs**, not the corpus's global exponent.
The distinction is exact and worth stating precisely:

> Every permutation of the 114 surahs uses the **identical token multiset**, and therefore has an
> identical V(N_tot), an identical type-frequency spectrum, and — to the precision at which
> H-NEW-123 works — an identical Heaps β. **β is the quantity that is invariant to ordering.**
> Statistics **J** (power-law-residual jerk) and **A** (mean absolute log-residual from the
> fitted Heaps curve) measure the *shape of the path* V(N) traces between fixed endpoints, which
> is exactly the information β discards.

Cells 1–10 are therefore orthogonal to H-NEW-123 by construction, and H-NEW-2570's registered
primary cell (cell 1: J for the mushaf against the length-preserving null N2) is untouched by
this amendment.

H-NEW-123 is recorded as the **parent finding**. Its Cell B NULL constitutes a prior that
H-NEW-2570's ordering statistics will also come back NULL; that prior is stated here for the
record, before this amendment is locked, so that a NULL outcome cannot later be presented as
having been unexpected.

### 2.4 One caveat of H-NEW-123 that H-NEW-2570 may resolve, descriptively

H-NEW-123's caveats flag a length-curvature artifact it could not remove: its poetry baseline was
the Muʿallaqāt alone at **7,285 tokens** against the Qurʾān's 77,797, and *"the β comparison
there is against the early-N region of the Heap curve, which systematically gives higher β for
all corpora."* It reported a post-hoc matched-length figure (β_Q7.3K = 0.801 vs Muʿallaqāt 0.831)
and flagged the gap as narrowed by the artifact.

`data/baseline-corpora/raw/` also holds seven **dīwāns** which H-NEW-123 did not use. Muʿallaqāt
plus dīwāns exceed 77,797 tokens, permitting the **fully length-matched** poetry comparison
H-NEW-123 could not perform. This is recorded as a **descriptive resolution of a caveat belonging
to H-NEW-123**, computed with H-NEW-123's estimator, MW-7 capped, **with no p-value and no
registered inference** — consistent with parent §7 and with §2.1 above.

---

## 3. Unchanged by this amendment

- Primary null: **N2, length-stratified, 19 strata of 6** — unchanged and still primary.
- Bonferroni k = 12; α_corrected = 0.0041667 — unchanged.
- Every locked direction in parent §5 and §5.2 — unchanged.
- The decision rule of parent §1 (a result surviving only the naive null is **not** a finding and
  is published as NULL — LENGTH ARTIFACT) — unchanged and still binding.
- All observed values, p-values, and verdicts from the executed run — unchanged; nothing is
  recomputed except the descriptive cross-corpus table, which is recomputed only to adopt
  H-NEW-123's estimator.

---

*Amendment 01 locked 2026-08-07 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
