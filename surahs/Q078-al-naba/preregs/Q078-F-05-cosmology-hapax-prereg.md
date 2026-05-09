---
surah: 78
test_id: Q078-F-05
title: Q 78 corpus-hapax + intensive-pattern (faʿʿāl-an) block-confinement test (al-Bāqillānī iʿjāz al-balāgha audit)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q078-F-05-cosmology-hapax
alpha_bon: 0.025
---

# Q078-F-05 — Pre-registration: Q 78 corpus-hapax + block-confinement test

## 1. Hypothesis (locked before observation)

**H1 (single-test, locked direction):** Q 78 has ≥3 corpus-hapax roots (roots whose entire corpus attestation lies within Q 78).

DIRECTION: ≥ 3.

**H2 (single-test, locked direction):** All Q 78 corpus-hapax roots are confined to Block 2 (vv.6-16, cosmic-evidence) AND/OR Block 4 (vv.31-40, paradise-tableau). Zero hapax in Block 1 (vv.1-5, framing) or Block 3 (vv.17-30, eschatological-judgment).

DIRECTION: hapax confined to Blocks 2 + 4.

**H0 (joint):** H1 fails (< 3 hapax) OR H2 fails (any hapax in Block 1 or Block 3).

This pre-reg is a **classical-claim audit**: al-Bāqillānī's iʿjāz al-balāgha tradition cites Q 78:13-14 (sirājan wahhājan + māʾan thajjājan) as evidence of revelatory-distinctive lexical-choice. The block-confinement test extends this: if the rare-word lexical-choice is principled (NOT random), then it should concentrate in the Blocks where vivid imagery serves the argument (cosmic-evidence + paradise-reward), not in the framing or judgment blocks where standard vocabulary suffices.

## 2. Operational definition

- **Source data**: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC root tagging).
- **Hapax**: a root r such that surah_count(r in Q 78) == corpus_count(r) AND corpus_count(r) ≥ 1. Equivalently: r appears ONLY in Q 78.
- **Q 78 block partition** (LOCKED PRE-RUN per `02-content-analysis.md` §1):
  - Block 1 (framing): vv.1-5
  - Block 2 (cosmic-evidence): vv.6-16
  - Block 3 (judgment): vv.17-30
  - Block 4 (paradise-closure): vv.31-40

## 3. Test statistic

- H1: q78_hapax_count.
- H2: blocks-with-hapax (set of block-names containing any hapax token); pass = no overlap with {Block 1, Block 3}.

## 4. Null

- H1 is a count-claim; no permutation needed (the count is observable).
- H2 is a structural-confinement claim; the null is "hapax distributed RANDOMLY across blocks" — but the test as pre-registered is a POSITIONAL-CONFINEMENT TEST, not a randomization test. With only 3 hapax tokens (per pre-flight observation), randomization would be under-powered; we use the structural-confinement test as the primary inference.

## 5. Success / Failure

- **CONFIRMED**: both H1 (≥3 hapax) AND H2 (Blocks 2+4 only).
- **DIRECTIONAL**: H1 passes but hapax appears in unintended blocks (Block 1 or 3); only the count-claim survives.
- **PARTIAL**: H1 fails (< 3 hapax) but hapax that DO exist are in Blocks 2+4.
- **NULL**: neither passes.

## 6. Honest limits known a priori

- Pre-flight observation: Q 78 has 3 corpus-hapax roots (whj v.13, vjj v.14, dhq v.34) — block locations: Block 2 (whj, vjj) + Block 4 (dhq). Pre-flight matches the predicted direction.
- This pre-reg formalizes a corpus-EXACT count + structural-confinement claim. Per HANDOFF/04-DISCIPLINE.md, post-hoc-noticed protocol applies; verdict ceiling = PASS-DIRECTED.
- Independent-replication: a different rule-tuple (full-tashkeel + Uthmani-consonantal) might resolve some hapax differently. The QAC-root-based hapax is rule-tuple-specific.
- The block-partition is researcher-induced (per content-analysis §1). The block boundaries are content-marked by lexical-formula shifts (interrogative → confirmatory → eschatological-declaration → paradise-declaration), but the block-cuts could in principle differ. Sensitivity to block-partition variation is documented in §1.

## 7. Rules-tuple

`(no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H1 + H2). α_bon = 0.025.

## 9. Coordination

This is the FIRST surah-specialist test on Q 78 hapax + block-confinement. No prior specialist run. No duplication.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q078_F_05_cosmology_hapax.py`; verified at runtime.
