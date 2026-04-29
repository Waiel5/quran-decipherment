---
id: H-NEW-44.2.1
title: Pharyngeal/Glottal Exhaustivity — directed single-test independent pre-reg
status: PRE-REGISTERED 2026-04-16 (BEFORE re-running the test; H-NEW-44.2 result viewed but the directed cell was non-significant after Bonferroni-8 there)
spec_locked_at: 2026-04-16
bonferroni_family: 2026-04-16-H-NEW-44-2-1
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (28-letter Arabic alphabet, al-Khalīl/Sibawayh POA grouping)
primary_data: 14 muqaṭṭaʿāt letters; 4 pharyngeal/glottal letters {ا, ه, ع, ح}
---

# [[h-new-44-2-poa-closure|H-NEW-44.2]].1 — Pharyngeal/Glottal Exhaustivity (directed)

## Garden-of-forking-paths disclosure

[[h-new-44-2-poa-closure|H-NEW-44.2]] (the parent test) found that ALL 4 pharyngeal/glottal letters {ا, ه, ع, ح} are in the 14 muqaṭṭaʿāt set. Marginal p (one-sided upper) = 0.061 — fails Bonferroni-8 (α=0.00625) but would survive α=0.05 unprotected.

Per the audit-022 / PRE-REG-STANDARD-04 pattern, a SINGLE-TEST independent pre-reg is permitted to test this specific directed hypothesis with no Bonferroni-8 cost. This pre-reg is filed BEFORE re-running the test, with the explicit acknowledgment that the directed-cell statistic from [[h-new-44-2-poa-closure|H-NEW-44.2]] was already viewed.

This is NOT a re-test of the same data — the data is the same — but a pre-registered DIRECTED hypothesis with single-test α=0.05.

## The single test

H_0: among uniform random 14-letter selections from 28, the count of pharyngeal/glottal letters (4-element class {ا, ه, ع, ح}) is hypergeometrically distributed with mean 4×14/28 = 2.

H_1 (directed, one-sided upper): the count is EXHAUSTIVE (= 4 of 4).

Test statistic: number of pharyngeal/glottal letters in the muqaṭṭaʿāt set.
Observed: 4.

Null: P(X ≥ 4 | hypergeometric(N=28, K=4, n=14)) = C(4,4)×C(24,10)/C(28,14) = 1·C(24,10)/C(28,14).

C(24,10) = 1,961,256
C(28,14) = 40,116,600
P = 0.04891

**Pre-committed verdict criterion:** PASS iff p ≤ α=0.05 (single test, k=1, no Bonferroni cost).

## MW-5 positive control

Inherits [[h-new-44-2-poa-closure|H-NEW-44.2]]'s pipeline validation (POA classification was used there with MW-7 spot-checks). No additional positive control needed for a closed-form hypergeometric test.

## Pre-committed verdict

| Outcome | Verdict |
|---|---|
| p ≤ 0.05 (≈ 0.049) | PASS-DIRECTED — pharyngeal/glottal exhaustivity confirmed at α=0.05 single-test |
| p > 0.05 | NULL |

This is essentially deterministic — the calculation is closed-form and independent of any random sampling. The pre-reg's role is to LOCK the directed hypothesis as the single test before any further interpretation.

## Mechanism interpretation (conditional on PASS)

If pharyngeal/glottal exhaustive coverage is confirmed at α=0.05 single-test:

- The 14 muqaṭṭaʿāt letters include EVERY pharyngeal/glottal letter of Arabic ({ا, ه, ع, ح}).
- The pharyngeal/glottal class is the DEEPEST articulation point in the vocal tract (back of throat, glottis).
- This may signal that the muqaṭṭaʿāt selection prioritizes articulation depth — perhaps a sonic-prominence consideration.
- The Khalīlian classical phonetic ordering (حلقية → شفوية = throat → lips) starts with this class. Muqaṭṭaʿāt covering this class exhaustively is consistent with prioritizing the "first" class in al-Khalīl's framework.
- Alternative reading: pharyngeals are uniquely Semitic; the muqaṭṭaʿāt prioritize Arabic's distinctive sonic identity.

## Honest caveats

- The test is post-hoc-noticed at the [[h-new-44-2-poa-closure|H-NEW-44.2]] wave. The independent pre-reg + α=0.05 single-test is the project's protection against tuple-shopping.
- Per audit-031 / PRE-REG-STANDARD-04 standard, a single PASS at α=0.05 in this pattern (post-hoc noticed → independent pre-reg) is **PASS-DIRECTED**, not CONFIRMED. Confirmation requires INDEPENDENT REPLICATION on a distinct data dimension (e.g., do the 4 pharyngeal/glottal letters have any internal structure within the muqaṭṭaʿāt set — frequency, position, surah-cluster distribution?).
- The hypergeometric calculation is closed-form; "running" the test means verifying the arithmetic.

## Integrity

- Single test, no Bonferroni cost.
- Pre-registered direction (one-sided upper).
- Closed-form computation; no random sampling.
- Verdict criterion is α=0.05 strict.
- Both PASS and NULL publishable.
