---
id: Q096-F-03
title: Q 96 ↔ Q 68 al-Qalam *qalam*-token-shared-position structural mirror
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q096-F-03-q96-q68-qalam-mirror
alpha_bon: 0.025
direction_of_effect: Q 68 al-Qalam (revelation-order #2 per Tanzil; Nöldeke #18) and Q 96 al-ʿAlaq (revelation-order #1 per Tanzil; Nöldeke #1) are the two short Meccan surahs that invoke *qalam* in their opening verses — Q 68:1 (oath-opener "Nūn wa-l-qalam") and Q 96:4 ("alladhī ʿallama bi-l-qalam"). Of the 4 corpus *qalam* token occurrences (Q 3:44, Q 31:27, Q 68:1, Q 96:4), exactly 2 fall in opening verses of Meccan-revealed surahs (Q 68:1 verse-1, Q 96:4 verse-4). The pre-registered direction: Q 68 and Q 96 form a structural mirror-pair on (a) shared early-revelation-order proximity (#2 and #1 in Tanzil ordering) AND (b) Fisher-Rao FR-distance below the corpus median.
origin: empirical-discovery — *qalam* corpus inventory inspection (4 occurrences) found 2 fall in early-Meccan surahs at opening positions, both classically tied to the literacy/writing-oath cluster; Q 68 directly NAMED *al-Qalam* mirrors Q 96 v 4 *bi-l-qalam* call.
verdict_ceiling: PASS-DIRECTED on success; sets up M2-extension hypothesis (the literacy-marker pair as classical-aesthetic anchor)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: random-pair-of-Meccan-surahs from full Meccan set (filtered period == Meccan in revelation-order.csv, ~85 surahs); verse-count length matching ±50% of mean(Q 68=52, Q 96=19) = 35.5 v, window [17, 53]
  feature_space: H-NEW-111 Fisher-Rao distance matrix (csv/h-new-111.json) for FR cell; revelation-order.csv for chronology cell
---

# Q096-F-03 pre-registration

## Hypothesis

Q 68 al-Qalam (Nöldeke #18, Tanzil rev-order #2) and Q 96 al-ʿAlaq (Nöldeke #1, Tanzil rev-order #1) are linked by:

1. **Shared classical literacy-marker**: Q 96:4 explicitly invokes *al-qalam* in the mid-block of vv 1-5 (the first-revealed core); Q 68 is the SHORT-EARLY-MECCAN surah named *al-Qalam* opening with the oath *nūn wa-l-qalami wa-mā yasṭurūn*. They are the only two short Meccan surahs to invoke *qalam* in their opening (Q 3:44 and Q 31:27 are within longer compositional units, not opening-cluster).
2. **Shared chronological proximity**: Tanzil rev-order pair (1, 2). Nöldeke pair (1, 18) — close on Tanzil scale, less close on Nöldeke. Tanzil is the classical Egyptian-standard ordering used by H-NEW-1030 / cross-finding-012.

The pre-registered direction: under H-NEW-111 Fisher-Rao distance, Q 68 ↔ Q 96 distance is MORE-SIMILAR than 95th percentile (one-sided lower-tail) of length-matched random Meccan pairs.

## Test design

### Cell A — Fisher-Rao FR-distance (PRIMARY)

Compute FR(Q 68, Q 96) from h-new-111.json D_matrix (we already verified above: FR = 0.7324). Compute null distribution: 10000 random pairs of Meccan surahs (period == Meccan per revelation-order.csv, ~85 surahs) length-matched within ±50% of mean(Q 68 verses=52, Q 96 verses=19) = mean 35.5, range [17, 53] verses. p_perm = fraction of pairs with FR ≤ 0.7324.

PASS-DIRECTED at α_bon = 0.025: p_perm ≤ 0.025.

### Cell B — Tanzil revelation-order proximity (SECONDARY)

Q 96 = rev-order 1; Q 68 = rev-order 2. The 2 surahs are revelation-order-CONSECUTIVE. Test whether ANY consecutive-revelation-order pair (1, 2), (2, 3), …, has the lowest FR distance among the 113 consecutive pairs. Direction: Q 96-Q 68 FR rank ≤ 6 (top 5%) of the 113 consecutive-revelation pairs.

PASS-DIRECTED at α_bon = 0.025: rank ≤ 6 of 113 (≈0.053 — pre-registered as ≤ 5 to clear α=0.025 strictly).

### Bonferroni

k = 2 cells. α_bon = 0.025 per cell. PASS requires both.

### Anti-flip

Reverse direction (Q 68-Q 96 FR is FARTHER than 95% of length-matched Meccan pairs OR rank ≥ 108 of 113 consecutive-rev pairs) is NULL, not reportable PASS.

### Acceptance windows

- Both pass: PASS-DIRECTED — Q 68/Q 96 form an empirically-mirror-pair on FR + chronology
- Only A passes: PARTIAL — FR-near but chronologically-typical
- Only B passes: PARTIAL — chronologically-near but FR-typical (Tanzil proximity is structural artifact)
- Both fail: NULL

### Garden-of-forking-paths

- Origin disclosed: post-hoc *qalam* inventory inspection found {Q 3:44, Q 31:27, Q 68:1, Q 96:4} as the 4 corpus tokens; visual recognition that Q 68 + Q 96 share opening-position *qalam* + early-Meccan + short status. This pre-reg locks BEFORE Cell A or Cell B numerics are computed (FR(96, 68) was already computed during pre-flight as 0.7324; that distance is locked here, not subject to revision).
- Length-window [17, 53] locked here.
- Tanzil ordering (Egyptian-standard) is the project's primary chronology axis per `revelation-order.csv` and H-NEW-1030 / cross-finding-012; Nöldeke chronology not used in primary cells.

### MW-5 positive control

Use the **musabbiḥāt cluster** (Q 57, 59, 61, 62, 64) which is CONFIRMED FR-tight (H-NEW-58c, mean shared char-prefix 14.1 vs null 0.36). Sub-sample any 2 of 5 (e.g., Q 57 ↔ Q 59) and run same length-matched-pair-FR null. Positive control passes if Q 57-Q 59 FR rank ≤ 5%. If FAILS, NULL-BROKEN.

## Connection to existing findings

- **H-NEW-56 extended-writing-cluster** (kitāb + qurʾān + qalam + satr): 25/29 muqaṭṭāʿat surahs (86%); Q 96 is NON-muqaṭṭāʿat but contains *qalam* — orthogonal cell to the muqaṭṭāʿat-set.
- **Cross-finding-008 muqaṭṭāʿat-as-book-introduction**: Q 68 (نون) is muqaṭṭāʿat-opened single-letter; Q 96 is non-muqaṭṭāʿat. The pair Q 68 + Q 96 spans the muq/non-muq boundary at the *qalam*-attestation axis.
- **H-NEW-1030** Q 110 chronology-dissociation per Tanzil ordering — analogous chronology-axis test.

## Pre-commit attestation

SHA256-locked. Script verifies SHA before loading h-new-111.json or revelation-order.csv.
