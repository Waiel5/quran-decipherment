---
id: H-NEW-90
title: Q 18 al-Kahf — quantitative test of 4-narrative structural parallelism vs other multi-narrative surahs (Q 7, 11, 26)
status: PRE-REGISTERED (not yet executed)
registered: 2026-04-15
spec_locked_at: 2026-04-15
agent: h-new-90-specialist
bonferroni_family: 2026-04-15-h-new-90-kahf-narrative
bonferroni_k: 5
alpha_bon: 0.010
rules_tuple:
  orthography: no-tashkeel for surface; QAC v0.4 morphology for roots
  word_definition: whitespace-split tokens (primary); QAC orthographic-word index (secondary, sensitivity)
  letter_definition: rasm graphemes, U+0621..U+064A plus U+0671
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  similarity: Jaccard of triliteral-root sets per narrative; Jaccard of opener-token sets
  null_model: random 4-block partition of length-matched non-Kahf surahs preserving block-count and verse-count distribution
primary_corpus: quran-text/quran-no-tashkeel.json
morphology: data/morphology/quranic-corpus-morphology-0.4.txt
prior_findings:
  - findings/phase-c-structures/al-kahf-deep-dive.md
  - findings/phase-c-structures/chiastic-audit.md
  - findings/phase-c-structures/moses-deep-dive.md
  - findings/phase-c-structures/ring-center-semantics.md
journal: journal/h-new-90-kahf-narrative-structure-run-1.md
---

# [[h-new-90-kahf-narrative-structure|H-NEW-90]] — Q 18 al-Kahf 4-narrative structural parallelism quantified

## Question

The al-kahf-deep-dive (2026-04-12) DESCRIBED four parallel narratives in Q 18 (Cave 9-26, Gardens 32-44, Moses-Khidr 60-82, Dhū'l-Qarnayn 83-98). It DID NOT formally test whether their parallelism is unusual relative to other multi-narrative surahs.

[[h-new-90-kahf-narrative-structure|H-NEW-90]] asks **five pre-specified quantitative questions**:

**Q1.** Are the 4-narrative boundaries the modal scholarly consensus boundaries (al-Suyūṭī Itqān, Rāzī Mafātīḥ, Qurṭubī, Ibn Kathīr)?

**Q2.** Do the 4 narratives share **inter-narrative root Jaccard** higher than 4 narratives extracted by random partition from a length-matched control surah?

**Q3.** Is v50 a **narrative boundary** under the locked boundary set, or interior to a narrative?

**Q4.** Do the 4 narratives share more **thematic roots** (≥3 of 4 narratives contain root) than random length-matched partitions?

**Q5.** Is the 4-narrative parallelism (mean inter-narrative Jaccard) UNIQUE to Al-Kahf vs three pre-specified multi-narrative comparator surahs (Q 7 al-Aʿrāf, Q 11 Hūd, Q 26 al-Shuʿarāʾ)?

## Locked narrative boundaries

Per al-Rāzī *Mafātīḥ al-Ghayb* and Yaser Qadhi's modern systematization (al-Maghrib "Light upon Light"), confirmed by Sayyid Quṭb (*Fī Ẓilāl al-Qurʾān* ad 18) and Mawdūdī (*Tafhīm al-Qurʾān* ad 18):

- **N1 Cave** (People of the Cave): vv 9–26 (18 verses)
- **N2 Gardens** (Two Garden Owners): vv 32–44 (13 verses)
- **N3 Moses-Khidr**: vv 60–82 (23 verses)
- **N4 Dhū'l-Qarnayn**: vv 83–98 (16 verses)
- Interludes: 1-8 (opening), 27-31 (interlude A), 45-59 (interlude B, includes v50), 99-110 (closing)

**Pre-locked**: any narrative-boundary alternative (e.g., Cave extending to v31 or Moses-Khidr to v59) is rejected as a sensitivity check, NOT a primary spec.

## Comparator surahs (pre-locked)

- **Q 7 al-Aʿrāf** (206 verses): Adam (10-25), Nūḥ (59-64), Hūd (65-72), Ṣāliḥ (73-79), Lūṭ (80-84), Shuʿayb (85-93), Mūsā (103-156), narrative-rich
- **Q 11 Hūd** (123 verses): Nūḥ (25-49), Hūd (50-60), Ṣāliḥ (61-68), Ibrāhīm/Lūṭ (69-83), Shuʿayb (84-95), Mūsā (96-99) — explicit "narrative chain" surah
- **Q 26 al-Shuʿarāʾ** (227 verses): Mūsā (10-68), Ibrāhīm (69-104), Nūḥ (105-122), Hūd (123-140), Ṣāliḥ (141-159), Lūṭ (160-175), Shuʿayb (176-191) — most narrative-dense surah

For Q 7, Q 11, Q 26 we use the SAME boundary methodology (Rāzī or Mawdūdī modal consensus) but truncate to the FIRST 4 narratives only (to match Al-Kahf's k=4 narrative count).

## Primary tests

**T1 (Boundary verification, Q1):** Locked boundaries from above + verification that boundaries lie at sūra-internal section markers (interlude verses pre-narrative are non-narrative content). Pass = 4-of-4 boundaries match modal scholarly consensus.

**T2 (Inter-narrative Jaccard, Q2 + Q5):** For each surah ∈ {18, 7, 11, 26}, compute the 4×4 root-Jaccard matrix between its 4 narratives. Report `mean_offdiag(J)`. Compare against null distribution of: 1000 random 4-block partitions of the same surah preserving the empirical narrative verse-count distribution (18, 13, 23, 16 verses). Compute z-score: `z_J = (mean_offdiag_observed - mean_null) / std_null`.

  - **PASS condition for Al-Kahf:** `z_J > 2.0` (one-tailed, α = 0.025) AND `z_J(Al-Kahf) > z_J(any comparator)`.

**T3 (v50 boundary check, Q3):** Under locked boundaries, v50 sits in **interlude B (45-59)**, not at any narrative boundary. Report whether this matches the empirical word-midpoint convergence (al-kahf-deep-dive §1.1 reports word-midpoint at v50 under whitespace tokenization).

  - **PASS condition:** v50 ∈ interlude (not narrative boundary, not narrative interior). This means the prior word-midpoint claim is at a NON-narrative junction — a specific, falsifiable claim.

**T4 (Thematic root sharing, Q4):** For each surah, count roots appearing in ≥3 of 4 narratives. Compare to null distribution from 1000 random 4-block partitions. Report `n_3of4` and z-score.

  - **PASS condition:** `z_3of4(Al-Kahf) > 2.0` AND > comparator surahs.

**T5 (Opener parallelism, Q2 second axis):** Each narrative's first 3 normalized tokens form an "opener triple". Compute Jaccard of opener triples across the 4 narratives (mean off-diagonal). Compare to null. (Pre-locked: this is a separate signal axis from T2.)

  - **PASS condition:** `z_opener(Al-Kahf) > 2.0`.

## Bonferroni

**k_outer = 5** primary tests. α_outer = 0.05 / 5 = 0.010. Z-threshold for one-tailed: z > 2.326.

## MW-5 positive control

Verify on a **known structurally-parallel pair**: the Moses-Khidr ↔ Dhū'l-Qarnayn pair (al-kahf-deep-dive §6.1 documents 3-act structural isomorphism). Inter-narrative Jaccard between N3 and N4 of Al-Kahf should be ABOVE the surah's mean. If not, the metric is broken.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| All 5 cells PASS at α_bon | UNIQUE-4-NARRATIVE — Al-Kahf is structurally distinct |
| 3-4 cells PASS | PARTIAL-UNIQUE — some axes confirm, others not |
| 1-2 cells PASS | WEAK — most parallelism dissolves under matched controls |
| 0 cells PASS | NULL — claimed parallelism is artifact of qualitative reading |
| MW-5 positive control fails | NULL-BROKEN |

## Garden-of-forking-paths log (pre-execution, 2026-04-15)

- Boundary spec: locked to Rāzī's vv 9-26, 32-44, 60-82, 83-98. NOT permitted post-hoc to expand to 9-31 (Cave + interlude A as one unit).
- Comparator surahs: locked at {7, 11, 26}. NOT permitted to swap to {12, 28, 21} post-hoc.
- Tokenization: whitespace primary; QAC orthographic secondary. ONLY whitespace counted toward primary verdict.
- Null model: random 4-block partition preserving (18, 13, 23, 16) verse-count tuple. Locked.
- Narrative-truncation policy for comparators: take FIRST 4 narratives. Locked. NOT permitted to choose "best" 4 post-hoc.
- z-threshold: 2.326 (one-tailed α=0.01 Bonferroni). Locked.
- Iteration count: 1000 random partitions. Locked.

## Integrity commitment

Publish:
- 4×4 root-Jaccard matrix per surah
- Null distribution histograms (text-based)
- All five cell verdicts
- Sensitivity test: re-run T2 under QAC orthographic-token instead of whitespace
- Sensitivity test: re-run T2 under expanded Cave (9-31) and Moses-Khidr (45-82) boundaries

If primary spec FAILS but sensitivity-spec PASSES, that is reported as PARTIAL — not promoted to PASS without ratification.

## Mechanism interpretation

- UNIQUE-4-NARRATIVE → confirms classical Rāzī/Qadhi reading; al-Kahf has measurably distinct narrative-architectural fingerprint
- PARTIAL-UNIQUE → some axes (likely opener parallelism + thematic root sharing) confirm, others (likely raw Jaccard) dissolve under matched control
- WEAK / NULL → 4-narrative reading is interpretive but not statistically distinguishable from any narrative-rich surah

---
