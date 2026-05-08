---
surah: 7
test_id: Q007-F-01
title: Prophet-cycle parallelism — feature-vector pairwise similarity within Q 7's 7-prophet narrative
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q007-F-01..F-04 (Q 7 surah-local pre-registered family)
alpha_bon: 0.0125
direction_locked: positive — Q 7 has corpus-MAX intra-surah prophet-narrative parallelism
rules_tuple: (no-tashkeel, QAC-stem-roots + structural feature-set, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q007-F-01 — Pre-registration: Prophet-cycle parallelism characterization

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 7's 7 sequential prophet-narratives (Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā) exhibit **higher mean pairwise feature-vector similarity** than the 7 corresponding prophet-narratives reordered by NULL permutation, AND higher than the comparable prophet-narrative blocks in Q 11, Q 26, Q 21.

**H0:** Q 7's prophet-narratives are no more mutually-parallel than chance permutations of the same blocks; and Q 7 ranks not better than 2nd among {Q 7, Q 11, Q 26, Q 21}.

This formalizes the H-NEW-90 surprise z=+5.25 finding (parent-finding cited in the task brief). H-NEW-90 used a single composite metric; Q007-F-01 decomposes the signal into a structural feature-vector with 4 features per prophet-narrative.

## 2. Operational definition

### 2.1 Prophet-block boundaries (Q 7, locked from al-Biqāʿī *Naẓm al-Durar* + al-Rāzī *Mafātīḥ al-ghayb* + al-Ṭabarī *Jāmiʿ al-bayān* on Q 7)

| Prophet | Block | Verses |
|:---|:---|:---|
| Ādam | A | 7:11–25 |
| Nūḥ | N | 7:59–64 |
| Hūd | H | 7:65–72 |
| Ṣāliḥ | S | 7:73–79 |
| Lūṭ | L | 7:80–84 |
| Shuʿayb | Sh | 7:85–93 |
| Mūsā | M | 7:103–137 (Pharaonic phase, locked to the destruction-of-Pharaoh closure) |

Total = 7 blocks. (The Mūsā-Bani-Israel phase 7:138–171 and the parable phase 7:175–177 are EXCLUDED from H1 to keep block-typology homogeneous: H1 tests destruction-cycle parallelism specifically.)

### 2.2 Feature-vector per block (4 features, locked)

For each prophet-block, extract a binary 0/1 indicator for the presence of:

| F | Feature | Operational rule |
|:-:|:---|:---|
| F1 | Introductory formula | Block opens with `wa-ilā [tribe] akhāhum [prophet]` OR `laqad arsalnā [prophet]` OR equivalent Quranic prophetic-mission opener (regex on no-tashkeel text of first 2 verses) |
| F2 | Miracle / sign introduction | Presence of a verse containing `bayyina` (`byn`) AND/OR a named miracle (`nāqa`, `rusul`, `ʿaṣā`, `āyāt`) within the block |
| F3 | Opposition narrative | Presence of `qāla al-malaʾu` / `qālū` / opposition-tribe response containing root `kfr` or `kdb` or `Aly` (rebellion) within the block |
| F4 | Destruction narrative | Presence of destruction-event verb root: `gRq` (drowning), `Rjf` (earthquake), `mTr` (rain stones), `Ahl` (perish), `Anjy`+`gRq` complement, or `Ax*` with rebuke within block |

Feature-vector V_p ∈ {0,1}^4 per prophet p.

### 2.3 Pairwise similarity

For 7 blocks, compute 21 pairwise feature similarities S_ij = (4 − Hamming(V_i, V_j)) / 4 ∈ [0,1].

**Q 7 mean intra-surah parallelism** = mean(S_ij) over 21 pairs.

### 2.4 Comparison surahs (locked)

For Bonferroni-3 outer comparison:
- **Q 11**: 4 destruction-cycle blocks per al-Suyūṭī's chronological reading: Nūḥ (11:25–48), Hūd (11:50–60), Ṣāliḥ (11:61–68), Lūṭ (11:69–83), Shuʿayb (11:84–95). 5 blocks, 10 pairs.
- **Q 26**: 7 blocks per the refrain-cycle (already established Q026-F-01 CONFIRMED): Mūsā (26:10–68), Ibrāhīm (26:69–104), Nūḥ (26:105–122), Hūd (26:123–140), Ṣāliḥ (26:141–159), Lūṭ (26:160–175), Shuʿayb (26:176–191). 7 blocks, 21 pairs.
- **Q 21**: 7 prophet-blocks per al-Rāzī: Mūsā-Hārūn (21:48–50), Ibrāhīm (21:51–73), Lūṭ (21:74–75), Nūḥ (21:76–77), Dāwūd-Sulaymān (21:78–82), Ayyūb (21:83–84), Ismāʿīl-Idrīs-Dhū-l-Kifl (21:85–86). 7 blocks, 21 pairs.

(Block-boundaries are locked-in pre-reg; no post-hoc adjustment.)

## 3. Test statistics

**Primary**: Q 7 mean pairwise S compared to 10,000 within-surah block-permutation null:
- Per perm, randomly assign each of the 7 blocks' feature-vector among the 7 prophet positions; recompute mean S.
- This fixes the marginal feature-frequency and tests whether the OBSERVED arrangement of features is unusually clustered.
- p_perm_within = fraction of perms with mean S ≥ observed.

**Secondary (Bonferroni-3)**: Q 7 mean S vs Q 11, Q 26, Q 21 mean S separately.
- Pre-committed direction: Q 7 mean > each of {Q 11, Q 26, Q 21} mean.
- Test: rank Q 7 in the set of 4. Strict success: rank 1/4.
- α_outer per pairwise = 0.05/3 = 0.0167 (Bonferroni-3 within the comparison family).

## 4. Success / Failure

- **CONFIRMED**: Q 7 ranks 1/4 AND p_perm_within ≤ α_bon (= 0.0125 within the surah-local Q007-F-01..F-04 Bonferroni-4 family).
- **DIRECTIONAL**: Q 7 ranks 1/4 OR p_perm_within ≤ 0.05.
- **NULL**: Q 7 ranks 3rd or 4th (sub-median).
- **PRE-COMMIT VIOLATION**: Q 7 rank = 4/4 AND p_perm_within ≥ 0.95 (i.e., mean S strongly *below* random — a structural anti-parallelism).

## 5. Honest limits known a priori

1. **Block-boundary choices are interpretive**. We lock al-Biqāʿī/al-Rāzī/al-Ṭabarī standard boundaries; ±2-verse sensitivity not pre-tested.
2. **4 features is small**. Hamming has only 5 possible values; ties expected.
3. **The 4 features are theory-laden**. All four are present in EVERY classical prophet-narrative template (al-Sharīf al-Murtaḍā etc.); the question is whether the *combination* differs across prophets, not whether the template exists.
4. **Q 26's prophet-cycle is internally short** (16-19 verses each except Mūsā-59), which means features 2/3/4 are likely binary-saturated; this should *favor* Q 26 in any "mean S close to 1" metric. If Q 7 wins despite this, the result is robust.
5. **Q 11's `wa-ilā [tribe] akhāhum` lattice** (3 hits; Q 7 also 3 hits) means F1 is partially shared. The corpus-wide F1 lattice is also covered by H-NEW-90's parent finding.
6. **The H-NEW-90 surprise z=+5.25** (parent-finding queued for follow-up) used a different metric. Our test is INDEPENDENT replication (different operationalization, MW-5 protection).

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots + 4-feature structural vector, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time over this file; embedded in `scripts/Q007_F_01_prophet_cycle_parallelism.py`. Verified at runtime; fail-fast if mismatched.
