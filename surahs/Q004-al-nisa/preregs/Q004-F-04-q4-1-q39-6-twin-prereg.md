---
finding_id: Q004-F-04
title: Q 4:1 vs Q 39:6 twin-verse similarity (creation-from-nafsin-wāḥida)
status: PRE-REGISTERED
date: 2026-05-07
specialist: Q004-al-nisa-specialist
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q004-novel-tests-2026-05-07
alpha_bon: 0.01
direction: HIGHER (Q4:1 vs Q39:6 lexical-overlap is significantly higher than null pair-overlap)
acceptance_window: token-Jaccard ≥ 0.30 AND empirical p (vs random-pair null) < α_bon (0.01)
---

# Q004-F-04 — Q 4:1 vs Q 39:6 twin-verse: pre-registration

## Hypothesis

al-Biqāʿī (*Naẓm al-Durar* on Q 4) and al-Rāzī (*Mafātīḥ al-ghayb* on Q 39:6) both identify a twin-relationship between Q 4:1 (`yā ayyuhā al-nāsu ittaqū rabbakum alladhī khalaqakum min nafsin wāḥidatin wa khalaqa minhā zawjahā wa baththa minhumā rijālan kathīran wa nisāʾan ...`) and Q 39:6 (`khalaqakum min nafsin wāḥidatin thumma jaʿala minhā zawjahā ...`). The two verses share the creation-from-a-single-soul motif, with Q 4:1 framing it for human-society + family law and Q 39:6 framing it for tawḥīd + creation-theology.

## Operationalisation

- Pull Q 4:1 and Q 39:6 from `quran-no-tashkeel.json`. Tokenize on whitespace.
- Compute three similarity metrics:
  1. Token-Jaccard: |A ∩ B| / |A ∪ B|.
  2. Token-overlap-coefficient: |A ∩ B| / min(|A|, |B|).
  3. Bigram-Jaccard on consecutive token pairs.
- Build the null distribution: sample 10000 random (verse_i, verse_j) pairs from the full 6,236-verse corpus where i ≠ j, both verses non-empty, and the verses are not from the same surah. Compute the same three similarity metrics for each. Seed = 20260507.
- Report: empirical p(Q4:1↔Q39:6 similarity ≥ random-pair similarity) for each metric.

## Direction & alternative

- DIRECTION-LOCKED: HIGHER (similarity > random-pair baseline).
- If Q4:1↔Q39:6 ≤ 95th percentile of null: DIRECTIONAL-WEAK (still in expected direction but not significant after Bonferroni).
- If Q4:1↔Q39:6 ≤ 50th percentile: NULL (twin-claim fails empirically).

## Null model & permutations

- MW-2 corpus-prior null: 10000 random verse-pairs.
- MW-6 instrument-control: re-run with a random pair from the same two surahs (Q 4 verse vs Q 39 verse, neither = the named verses) — if these score similarly, the twin-effect is surah-pair-level, not verse-pair-level.

## Bonferroni

- Family: Q004-novel-tests-2026-05-07, k=5; α_bon = 0.01.
- Within this single test, three metrics are reported; the primary metric for the verdict is **token-Jaccard**.

## Honest limits

- "Token-Jaccard" on no-tashkeel orthographic tokens conflates close inflected forms (e.g. `khalaqakum` vs `khalakahu`) — this UNDER-counts shared semantics.
- The two verses share core phrase `khalaqakum min nafsin wāḥidatin` which alone gives ~4-5 shared tokens; the test asks whether this exceeds random-pair baseline.
- The classical twin-claim is *thematic*, not lexical; even a NULL on lexical similarity does not refute the thematic claim — it only refutes the lexical-similarity prediction made HERE.
