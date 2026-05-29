---
surah: 2
surah_name: al-Baqara
file_type: pre-registration
test_id: Q002-F-06
date_registered: 2026-05-29
phase: B+
status: LOCKED-BEFORE-RUN
seed: 20260509
n_perms: 10000
rules_tuple: (no-tashkeel, QAC-triliteral-root, root-sets, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q002-F-06 — Āyat al-Kursī (Q 2:255) ROOT-LEVEL local distinctiveness

## Motivation

Q002-F-01 (divine-name density) returned NULL on the pre-committed per-word density,
VINDICATED only on absolute counts (rules-tuple-fragile). Q002-F-03 (whole-corpus
centrality) found Q 2 is a cohesion-anchor not a centroid. **Neither test asked
whether Āyat al-Kursī (Q 2:255) is a LOCAL peak inside Q 2 at the ROOT level.** The
prior tests were surface-token (F-01) or whole-surah-vector (F-03); both flagged
"root-level test pending" in their Honest Limits.

This test asks a close-reading question: within al-Baqara, is verse 255 lexically
DISTINCTIVE from its local neighbourhood (does it introduce roots that set it apart),
and is it a local maximum of root-Jaccard *distance* to its surrounding verses? The
classical hadith claim (al-Bukhārī #4008, Muslim #810 — Āyat al-Kursī is *aʿẓam āya*,
the greatest verse) is theological; the falsifiable PROXY here is: a "greatest verse"
should at minimum be lexically NON-redundant with its immediate context (a self-
contained theological summit, not a continuation of an adjacent passage).

## Hypothesis (DIRECTION LOCKED)

**H1 (local distinctiveness):** Q 2:255 has HIGHER mean root-Jaccard *distance*
(= 1 − Jaccard) to its ±k local window neighbours than ≥ 95% of all 286 verses of
Q 2 (i.e. it is in the TOP-5% most locally-distinctive verses of al-Baqara), for the
pre-committed window radius k = 3 (the 6 nearest verses, 2:252–254 and 2:256–258).

**H2 (corpus-wide replication):** Among the 6,236 verses of the whole corpus, Q 2:255
ranks in the TOP-10% by the same local-distinctiveness metric (±3 in-surah window).

Direction is LOCKED: HIGH local-distinctiveness (Q 2:255 is lexically distinct from
its neighbours). A LOW result (Q 2:255 is lexically redundant with neighbours) = NULL
published with full prominence.

## Metric (MW-1 instrument locked)

- Per-verse root set R(v) = set of QAC-triliteral roots in verse v, from
  `data/morphology/root-index.json` (the `ROOT:` field of QAC v0.4).
- Jaccard(a,b) = |R(a)∩R(b)| / |R(a)∪R(b)|; distance = 1 − Jaccard.
- local_distinctiveness(v, k) = mean over the up-to-2k in-surah neighbours
  {v−k..v−1, v+1..v+k} of distance(v, neighbour). Window radius k = 3 LOCKED.
  Verses near surah edges use the available (fewer) neighbours.
- Rank computed two ways: (a) within Q 2's 286 verses (H1), (b) across all 6,236
  verses, each scored against its own in-surah ±3 neighbours (H2).

## Null / significance

- H1 success: in-surah rank ≤ 15 / 286 (top-5%).
- H2 success: corpus rank ≤ 624 / 6236 (top-10%).
- Permutation control (MW-2): 10,000 random in-surah verse-order shuffles of Q 2
  (seed 20260509); report the permutation p that Q 2:255's neighbour-distance
  exceeds the shuffled-neighbour distance. This controls for "any verse looks
  distinctive against random neighbours."
- Bonferroni: k = 2 (H1, H2) → α_corrected = 0.025.

## Failure / NULL conditions

- If Q 2:255 in-surah rank > 15 → H1 NULL.
- If corpus rank > 624 → H2 NULL.
- If the permutation p > 0.025 → no signal beyond chance; NULL.
- A LOW-distinctiveness result (rank in BOTTOM half) is a pre-commit-relevant
  reversal: published as NULL with the reversal flagged.

## MW protections

- MW-1: metric (root-Jaccard local distance, k=3) locked here, pre-run.
- MW-2: 10,000-perm in-surah shuffle null.
- MW-3: report k = 2 and k = 5 as alternative-radius robustness (NOT the primary;
  primary is k = 3). Direction must hold for the primary k = 3.
- MW-5: corpus-wide (H2) replication of the in-surah (H1) claim.
- MW-7: any post-hoc metric carries single-test α = 0.05 ceiling.

## Honesty note

This is a PROXY for the theological "greatest verse" claim, not a measure of it.
Lexical distinctiveness ≠ theological greatness. A NULL here does NOT impugn the
hadith; it only says the *aʿẓam āya* is not lexically isolated from its context.
