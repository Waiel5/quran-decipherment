---
id: H-NEW-1390
title: Corpus-wide search for OPENING-LINKED CONTENT-DIVERGENT mushaf-adjacent pairs
date_locked: 2026-05-09
seed: 20260509
n_perm: 0
bonferroni_k: 1
bonferroni_family: H-NEW-1390-opening-linked-content-divergent
alpha_bon: 0.05
direction_of_effect: At least 3 of the 113 mushaf-adjacent pairs (Q_n, Q_{n+1}) simultaneously satisfy (A ∨ B ∨ C) = TRUE and D = FALSE, where A = clamped-zero TSP seam (in the H-NEW-1240 13-seamless set per h-new-720.json bottom10_cheap + extension to all delta_raw ≤ 0), B = morphologically-isomorphic first 3 words of v1 (identical word-1 + word-2 + same morphological template for word-3), C = identical surface opener pattern (shared opener class from the locked taxonomy), and D = FR-mutual top-15 (each surah in the other's top-15 nearest neighbors per the h-new-111.json Fisher-Rao distance matrix). The signature (A ∨ B ∨ C) ∧ ¬D is the OPENING-LINKED CONTENT-DIVERGENT class formalized from Q073-F-02 (DIRECTIONAL, 2026-05-09, see MASTER-FINDINGS-LEDGER §10.48.2).
origin: Q073-F-02 (Q 73 ↔ Q 74 muzzammil/muddaththir pair) returned axis-A FR-mutual-top-15 FAIL (Q 74 ranks 37 in Q 73's neighbors and Q 73 ranks 37 in Q 74's neighbors) BUT axis-B clamped-zero seam PASS (delta_raw = -0.02888) AND axis-C morph-iso opening PASS (both 3-word yā-ayyuhā al-XaXXiX Form-V passive participle). This raised the candidate architectural class "OPENING-LINKED CONTENT-DIVERGENT" — pairs held together by opening-formula + mushaf-architecture but content-divergent on root-distribution. This pre-reg formalizes the class definition and runs the corpus-wide scan to see how rare or common the signature is.
verdict_ceiling: PASS-DIRECTED-CORPUS-SCAN (descriptive enumeration with a single direction-locked count threshold; INDEPENDENT REPLICATION required for promotion to architectural law).
rules_tuple:
  orthography: no-tashkeel
  word_definition: split-on-whitespace (orthographic-token)
  letter_definition: non-space-character (graphemes)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  reading_tradition: Hafs-Kufan
  script: Mashriqi
  fisher_rao_source: findings/phase-b-hypotheses/csv/h-new-111.json `D_matrix_upper_triangular`
  tsp_seam_source: findings/phase-b-hypotheses/csv/h-new-720.json `per_adjacency.delta_raw`
---

# H-NEW-1390 pre-registration

## Origin and motivation

Q073-F-02 (Q 73 ↔ Q 74 vocative pair test, see MASTER-FINDINGS-LEDGER §10.48.2 and `surahs/Q073-al-muzzammil/csv/Q073-F-02.json`) found a pair signature that did not fit either the FR-cohesive cluster class (cross-finding-010, H-NEW-1080 etc.) or the FR-isolated pair class. The Q 73 ↔ Q 74 pair is mushaf-adjacent, opens with morphologically isomorphic 3-word vocative formulas (yā-ayyuhā al-muzzammil, yā-ayyuhā al-muddaththir), sits at a clamped-zero TSP seam (delta_raw ≈ -0.029 per h-new-720.json bottom10_cheap row), and yet is FR-distant: Q 74 ranks 37th nearest among Q 73's 113 neighbors and Q 73 ranks 37th nearest among Q 74's neighbors. This combination — opening-formula coupling plus mushaf-position coupling plus content divergence — has no prior architectural label in the project's catalog.

H-NEW-1390 formalizes the signature as a 4-axis flag tuple per mushaf-adjacent pair and runs an enumerative scan over all 113 such pairs to test whether the Q 73 ↔ Q 74 pair is a corpus singleton (which would make Q073-F-02 a sui-generis observation) or an instance of a broader architectural class.

## Definitions

For each mushaf-adjacent pair (Q_n, Q_{n+1}) with n ∈ {1, …, 113}:

**Axis A — clamped-zero TSP seam**:
- A = TRUE iff the pair's delta_raw value in h-new-720.json `per_adjacency` is ≤ 0 (i.e., the TSP simulator clamps the constrained-path cost increment to zero for this adjacency).
- Per h-new-720.json there are exactly 13 such pairs: (3,4), (4,5), (6,7), (37,38), (64,65), (65,66), (72,73), (73,74), (86,87), (91,92), (93,94), (105,106), (109,110). All other 100 pairs have A = FALSE.

**Axis B — morph-iso first 3 words**:
- B = TRUE iff word-1 of v1(Q_n) == word-1 of v1(Q_{n+1}) AND word-2 of v1(Q_n) == word-2 of v1(Q_{n+1}) AND word-3 of v1(Q_n) is morphologically templated identically to word-3 of v1(Q_{n+1}) (same length, same Arabic-letter-class prefix pattern at position 1–3).
- The morphological-template test for word-3 is operationalized as: same first-letter and same word length within ±1 character. If either surah's v1 has fewer than 3 words, B = TRUE only if all the present words match identically and lengths match.
- Strict reading of word-1 + word-2 exact match; word-3 same template.

**Axis C — identical surface opener pattern**:
- C = TRUE iff both surahs share the same opener class from the locked taxonomy:
  - `basmala` (starts with بسم الله الرحمن الرحيم — only Q1)
  - `qul` (starts with قل)
  - `al-hamd` (starts with الحمد)
  - `tabaraka` (starts with تبارك)
  - `sabbaha` (starts with سبح)
  - `yusabbihu` (starts with يسبح)
  - `ya-ayyuha:<addressee>` (starts with يا أيها followed by addressee word: ya-ayyuha-al-nas, ya-ayyuha-alladhina, ya-ayyuha-al-nabi, ya-ayyuha-al-muzzammil, etc.)
  - `muqatta:<letters>` (single-token muqaṭṭaʿāt opener: الم, الر, حم, يس, طس, ق, ص, ن, كهيعص, طه, طسم, المص, المر, حمعسق)
  - `tanzil` (starts with تنزيل)
  - `idha` (starts with إذا)
  - `wa-<noun>` (oath particle wa- followed by a noun; subclass by noun: wa-al-sama, wa-al-fajr, etc.)
  - `qad` (starts with قد)
  - `inna` (starts with إنا)
  - `lam` (starts with لم)
  - `lā` (starts with لا)
  - `hal` (starts with هل)
  - `arā'a` (starts with أرأيت)
  - `araj` (starts with ألم)
  - `alhakum` (starts with ألهاكم)
  - `viewer` other (starts with anything else; subclass labeled by first word)
- Note: the ya-ayyuha class has SUBCLASSES tagged by addressee word (al-nas vs alladhīna vs al-nabī vs al-muzzammil etc.). For Axis C, the SUBCLASS must match (i.e., Q4 → Q5 = ya-ayyuha:al-nas vs ya-ayyuha:alladhīna → C = FALSE under subclass-matching; C = TRUE only under broader ya-ayyuha-any matching).
- We test BOTH the strict subclass-matching variant (C_strict) and the loose broader-class variant (C_loose); the primary axis C is C_strict (subclass must match). C_loose is reported for sensitivity but does not enter the primary verdict.

**Axis D — FR-mutual top-15**:
- D = TRUE iff Q_{n+1} is in Q_n's 15 nearest FR-neighbors AND Q_n is in Q_{n+1}'s 15 nearest FR-neighbors per the h-new-111.json `D_matrix_upper_triangular` Fisher-Rao distance matrix.
- This is the IDENTICAL operationalization as Q073-F-02 axis A.

## Primary direction-locked hypothesis

H1: **At least 3 of the 113 mushaf-adjacent pairs satisfy (A ∨ B ∨ C_strict) = TRUE AND D = FALSE**.

This is a count-based threshold over the 113-pair enumeration. The Q 73 ↔ Q 74 seed contributes 1 of the required ≥3 pairs (it satisfies A AND B AND C_strict, and D = FALSE per Q073-F-02's measured ranks 37 + 37).

The threshold of ≥3 is chosen as **at-least-doubling** the Q 73 ↔ Q 74 seed: H1 = TRUE means OPENING-LINKED CONTENT-DIVERGENT is a class with at least 3 instances (the seed plus ≥2 independent siblings), not a singleton. A threshold of ≥3 is the minimum for "class" status in the project's prior convention (≥3 corpus instances = formal class; ≤2 = candidate / observation-only).

## Baseline rate computation (corpus-prior MW-2)

The corpus-wide baseline rate for D = FALSE on mushaf-adjacent pairs is computed at runtime from h-new-111.json. From the matrix, for each of the 113 mushaf-adjacent pairs, compute mutual top-15 status; the empirical baseline is reported as P(D = FALSE | mushaf-adjacent). This baseline is NOT used as a single-test p-value but as the multinomial denominator for the joint signature.

Joint baseline expected under independence:
- P(A=TRUE) = 13/113 ≈ 0.115 (clamped-zero seams from h-new-720.json)
- P(B=TRUE) = empirical from scan (locked at runtime)
- P(C_strict=TRUE) = empirical from scan (locked at runtime)
- P(D=FALSE) = empirical from scan (locked at runtime)
- P((A∨B∨C_strict) ∧ ¬D | independence) = (1 - (1-P(A))(1-P(B))(1-P(C))) × P(D=FALSE)

The expected number of pairs satisfying the joint signature under independence = 113 × P((A∨B∨C_strict) ∧ ¬D | independence). H1 is supported if the OBSERVED count exceeds the EXPECTED count by at least 1.5× AND ≥3 absolute.

## Acceptance windows

| Outcome | Verdict |
|:--|:--|
| Observed ≥ 3 pairs AND observed ≥ 1.5× expected | PASS-DIRECTED (class established) |
| Observed ≥ 3 pairs AND observed < 1.5× expected | DIRECTIONAL (signature exists but at chance level) |
| Observed = 2 pairs | PARTIAL (signature exists but below class threshold) |
| Observed = 1 pair (just the seed) | NULL (Q 73 ↔ Q 74 is a corpus singleton; Q073-F-02 reframed as observation-only) |
| Observed = 0 pairs (seed fails replication) | PRE-COMMIT VIOLATION (would mean my axis flags are inconsistent with Q073-F-02; halt and audit) |

## Garden-of-forking-paths disclosure

Pre-locked:
- 113-pair enumeration is exhaustive (no cherry-picking of pairs).
- Axis A definition uses h-new-720.json `delta_raw ≤ 0` (operationalization stated above, verifiable from the JSON).
- Axis B definition uses morphological template = same first letter + length ±1; the project's prior morph-iso protocol uses identical word length + identical first 3 character classes. The first-letter-plus-length-±1 rule is a slight relaxation chosen to capture the broader class of templated openers (e.g., al-muzzammil 6 letters vs al-muddaththir 7 letters both start with al-mu- and end with consonant; the seed pair Q 73 ↔ Q 74 has lengths 6 and 7 respectively).
- Axis C taxonomy is locked above (20 opener classes plus other-subclass). Subclass-matching for ya-ayyuha is the strict variant.
- Axis D uses Q073-F-02's exact operationalization (mutual top-15 per h-new-111.json).
- The ≥3 threshold for H1 is direction-locked BEFORE scan; the seed Q 73 ↔ Q 74 contributes 1 of the required 3.
- Direction is locked as ≥3 instances → class. Reversed direction (the Q 73 ↔ Q 74 seed is the ONLY instance, observed = 1) is NULL with full prominence.

## Connection to existing findings

- **Q073-F-02**: Seed; this pre-reg formalizes the candidate class introduced there.
- **H-NEW-1240 / cross-finding-013**: The 13-seamless TSP set provides Axis A.
- **H-NEW-111 / cross-finding-011**: The Fisher-Rao matrix provides Axes B/C labels (Q073-F-02 measured FR-rank for Q 73 ↔ Q 74).
- **Cross-finding-025 marker-thickness**: This test extends cross-finding-025 by introducing a CONTRARIAN signature — the opening-formula marker IS thin (<5% of surah content) AND yet the architectural coupling exists at the seam-and-formula level. If H1 holds, OPENING-LINKED CONTENT-DIVERGENT becomes a NEW class type that operates orthogonally to FR-cohesion, not in opposition to cross-finding-025 but extending it: thin markers do NOT drive FR-cohesion but they DO operate as architectural couplers at the mushaf-seam + opening-formula level.
- **OQ-3 (other introduction-marker classes besides muqaṭṭāʿat)**: H-NEW-1390 may contribute new introduction-marker class candidates beyond al-ḥamdu li-llāh (H-NEW-1340 NULL).

## Pre-commit attestation

This pre-reg is SHA-locked. The run script verifies the SHA before computing. Direction is ≥3 instances → PASS; ≤2 instances → NULL/PARTIAL with full prominence per PRE-REG-STANDARD-04.

## Computation plan

1. Load `quran-text/quran-no-tashkeel.json`.
2. Load `findings/phase-b-hypotheses/csv/h-new-720.json` for Axis A flags.
3. Load `findings/phase-b-hypotheses/csv/h-new-111.json` for Axis D Fisher-Rao matrix.
4. Build per-surah v1 word list (first 3 words).
5. For each of 113 mushaf-adjacent pairs (n=1..113), compute (A, B, C_strict, C_loose, D) flags.
6. Emit 113-row table.
7. Filter to OPENING-LINKED CONTENT-DIVERGENT subset: (A ∨ B ∨ C_strict) ∧ ¬D = TRUE.
8. Compute observed count, expected count under independence, ratio.
9. Apply acceptance window for verdict.
10. Emit JSON + finding markdown.

## Honest limits

- Axis B morph-iso template-match is operationalized loosely (length ±1, same first letter); a stricter root/template match would require QAC v0.4 morphological lookup at the verse level which is feasible but not necessary for the broader class definition.
- Axis C subclass-matching for ya-ayyuha may be too strict if the architectural class is really "ya-ayyuha-any addressee"; the loose variant is reported.
- D = mutual top-15 is the operationalization carried from Q073-F-02. A stricter threshold (top-5) or looser (top-30) is not tested here; the top-15 axis is the project default and is what Q073-F-02 pre-committed.
- The test is descriptive enumerative; no permutation null is computed because the 113-pair universe is exhaustively enumerated and the expected-under-independence baseline is computed directly. This is appropriate for a class-formation test, not a single-pair significance test.
