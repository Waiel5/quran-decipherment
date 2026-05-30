---
surah: 54
test_id: Q054-F-06
title: Q 54 al-Qamar al-Muqtadir closure-concentration — corpus-share + closure-position test
file_type: pre-registration
date_locked: 2026-05-30
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q054-F-06-muqtadir-closure
alpha_bon: 0.025
---

# Q054-F-06 — Pre-registration: al-Muqtadir closure-concentration in Q 54

## 0. Provenance / forking-paths disclosure (BEFORE lock)

During the 2026-05-09 Q 54 deep-dive (overview §12) it was *noticed* that the divine name
*muqtadir* (مقتدر) appears twice in Q 54 (vv 42, 55), both in surah-closure-frame position, and the
overview carried an UNVERIFIED self-flagged "[check]" on the corpus-wide count (it speculatively
listed Q 55:78 as a possible 5th instance). This pre-reg LOCKS a direction and a permutation null to
turn that noticed-but-unverified observation into a tested claim. Because the *existence* of the two
Q 54 instances was noticed pre-lock, the verdict CEILING on the corpus-share cell (H6a) is
**PASS-DIRECTED**, not CONFIRMED, per the project post-hoc-noticed protocol (HANDOFF/04-DISCIPLINE).
The closure-position cell (H6b) and the permutation null (H6c) are genuinely novel and carry no
post-hoc discount. The corpus-wide *muqtadir* count is RE-VERIFIED from disk as part of this test
(not assumed from the overview).

## 1. Hypotheses (locked before computation)

**H6a (corpus-share, locked direction positive):** Q 54 holds the corpus-MAXIMUM share of all
orthographic *muqtadir* (مقتدر) tokens. Locked threshold: Q 54 share ≥ 0.40 of all corpus *muqtadir*
verses. (Direction: Q 54 is the single most *muqtadir*-dense surah by raw count.)

**H6b (closure-position, locked direction positive):** BOTH Q 54 *muqtadir* instances fall in
surah-closure-frame position, operationalised as: (i) the surah-final verse, OR (ii) the final verse
of a major narrative block whose right-boundary is the last destruction-pericope. Locked threshold:
2/2 Q 54 *muqtadir* verses are closure-frame (v 55 = surah-final; v 42 = final verse of the
5-pericope destruction-block, vv 9-42).

**H6c (permutation null, locked direction positive):** Q 54's count of *muqtadir* tokens (=2) is
elevated above a length-weighted multinomial redistribution of all corpus *muqtadir* tokens across
the 114 surahs. Locked: one-tailed permutation p (observed Q 54 count ≥ permuted) < α_bon = 0.025.

**H0:** H6a fails (Q 54 share < 0.40) OR H6c perm-p ≥ α_bon.

## 2. Operational definitions

- **Source text:** `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Token:** orthographic substring `مقتدر` (matches both *muqtadir* sing. and the broader
  *muqtadirūn* plural form Q 43:42; the regex is the bare stem `مقتدر`). One hit per verse counts as
  one *muqtadir*-verse.
- **Corpus-share:** n_Q54_muqtadir_verses / n_total_corpus_muqtadir_verses.
- **Closure-frame:** pre-committed verse-set (see H6b).

## 3. Permutation null (H6c)

Redistribute the N total corpus *muqtadir* tokens across the 114 surahs under a length-weighted
multinomial (weights ∝ verse-count per surah, from `data/hafs-verse-counts.tsv`). For each of 10,000
trials, record the count assigned to Q 54. p = P(perm_count ≥ observed_count). seed = 20260509.

Rationale for length-weighting: longer surahs have more opportunity to host a token; the null asks
whether Q 54's count exceeds what its *length* alone would predict. (A uniform null is also reported
as a secondary diagnostic.)

## 4. Test statistics

- H6a: share_Q54 ≥ 0.40 (binary).
- H6b: |closure-frame Q 54 muqtadir verses| == 2 (binary).
- H6c: perm_p < 0.025.

## 5. Success / Failure

- **CONFIRMED (joint):** H6b + H6c both pass at α_bon = 0.025 (H6a ceiling PASS-DIRECTED).
- **PARTIAL:** exactly one of {H6b, H6c} passes.
- **NULL:** neither H6b nor H6c passes.
- **PRE-COMMIT VIOLATION:** observed Q 54 share < observed share of some OTHER single surah (i.e.
  Q 54 is NOT the corpus-max), which would reverse H6a's locked direction.

## 6. Honest limits known a priori

- *muqtadir* is a RARE token (pre-flight unverified count ~4 corpus-wide); with small N the
  length-weighted null is coarse and the perm-p is granular. A count of 2 in a small-N regime can
  reach significance easily; the closure-position cell (H6b) is the substantive discriminator.
- H6a is arithmetically near-trivial once the count is verified (it is a raw-count ranking, not a
  modelled effect); its value is the closure-position structure (H6b), not the bare count.
- The finding, if confirmed, is a single-surah descriptive-architectural fact (a doubled
  power-name closure frame), NOT a corpus-law. It complements but does not depend on Q054-F-01..05.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, verse-as-unit, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (H6b + H6c; H6a is a disclosed PASS-DIRECTED-ceiling pre-flight observation, not counted in
the inferential family). α_bon = 0.025.

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q054_F_06_muqtadir_closure.py` as EXPECTED_SHA,
verified at runtime (fail-fast on mismatch).
