---
surah: 59
test_id: Q059-F-01
title: Khawātim al-Ḥashr per-token-density replication of H-NEW-95 Cell E
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q059-F-01-khawatim-density-replication
alpha_bon: 0.025
post_hoc_origin: NO — this is a planned replication of H-NEW-95 Cell E within the Q 59 specialist context with a specific extension (per-token-density).
---

# Q059-F-01 — Pre-registration: Khawātim al-Ḥashr per-token-density replication

## 1. Hypothesis (locked before observation, by the Q 59 specialist brief)

**H1a (one-tailed, locked direction):** Q 59:22-24 is the corpus RANK-1 3-verse window by absolute 99-divine-name token count (F99) — replicating [[h-new-95-khawatim-extension|H-NEW-95]] Cell E.

**H1b (one-tailed, locked direction):** Q 59:22-24 is in the corpus top-5 3-verse windows by per-token-density (F99 / W) under the rule **window word-count W ≥ 10** (the rule excludes trivially-tiny denominator windows).

**Direction:** Q 59:22-24 = corpus-MAX (LOCKED for H1a). Top-5 by density (LOCKED for H1b).

## 2. Why the per-token-density extension

[[h-new-95-khawatim-extension|H-NEW-95]] Cell E used the absolute count F99 as the test statistic. The Q 59 specialist context asks the inverse: when the surah-specific argument is "Q 59:22-24 carries the densest divine-name PER-TOKEN ratio in the corpus," is that statement load-bearing? A 3-verse window of the form "huwa allāh huwa allāh huwa allāh" with 3 words and 3 names would score density = 1.00 but F99 = 3 — which is rhetorically banal. The density-with-floor variant {W ≥ 10} excludes such trivialities and tests the substantive iʿjāz claim.

## 3. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Name list**: `data/asma-al-husna.txt` (canonical al-Walīd ibn Muslim 99-name list per al-Tirmidhī #3507).
- **Substring rule** (replicating H-NEW-95): word matches name N if `word == proclitic + N` for proclitic ∈ {ε, و, ف, ل, ب, ك, فل, ول, وب, فب, فال, وال, ولل, فلل, بال, كال}. The full list is locked in `scripts/Q059_F_01_khawatim_density_replication.py`.
- **3-verse sliding-window**: 6,234 windows across the 6,236-verse corpus, including windows that span surah boundaries (matching H-NEW-95 Cell E methodology).
- **Density floor**: W ≥ 10 (yields ~5,963 windows; rejected windows are trivially-small denominator cases).

## 4. Test statistics

- **F99(window)** = total 99-name token count in the 3-verse window.
- **density(window)** = F99(window) / words(window), restricted to W ≥ 10.

## 5. Permutation null

Word-count-weighted verse re-draw of 99-name tokens (the same null design as H-NEW-95):
1. Total tokens fixed at the corpus-observed total.
2. Each token assigned to a verse with probability proportional to verse word-count.
3. After re-distribution, compute max-F and max-density across all 6,234 windows.
4. p-value = fraction of permutations where null max ≥ observed value.

n_perm = 10,000, seed = 20260509.

## 6. Success / Failure

- **CONFIRMED**: H1a passes (rank 1) AND H1b passes (top 5) AND BOTH p < α_bon = 0.025.
- **PARTIAL**: only H1a passes OR only H1b passes.
- **NULL**: both H1a and H1b fail.

## 7. Honest limits known a priori

- **Inventory choice is load-bearing**: the test uses the full 99-name list (not the 9-Khawātim-exclusive). Alternative inventory tests are deferred to robustness arms.
- **Density-floor W ≥ 10 is a pre-committed parameter**: alternative thresholds (5, 15, 20) are NOT tested under this pre-reg.
- **Surah-spanning 3-verse windows**: Q 59:23 → Q 60:1 and similar boundary-crossing windows are included (consistent with H-NEW-95).
- **Q 1 al-Fātiḥa basmala dominates short-window density**: Q 1:1-3 has F99=5 in 10 words for density=0.5 (basmala = "al-Raḥmān al-Raḥīm"). This is a known feature of the corpus that may displace Q 59:22-24 from rank 1 by density even though Q 59 dominates by absolute F99.

## 8. Rules-tuple

`(no-tashkeel, ornament-stripped, whitespace-tokenized, proclitic-prefix-tolerant, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi)`.

## 9. Bonferroni

k = 2 (H1a + H1b). α_bon = 0.025.

## 10. Coordination

This test extends [[h-new-95-khawatim-extension|H-NEW-95]] Cell E. The original H-NEW-95 finding is unaffected; this is a **rule-tuple extension** under the Q 59 specialist context. No double-counting against H-NEW-95.

## 11. SHA256 lock

Computed at write-time, embedded into `scripts/Q059_F_01_khawatim_density_replication.py`, verified at runtime.

## 12. Authored by

Waiel Al-Shujaa, 2026-05-09.
