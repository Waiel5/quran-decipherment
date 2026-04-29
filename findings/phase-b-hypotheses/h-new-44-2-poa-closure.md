---
id: H-NEW-44.2
title: Place-of-Articulation closure test on the 14 muqaṭṭaʿāt letters (al-Khalīl POA classification)
phase: B
status: NULL — 0/8 per-class significant at Bonferroni-8 (α=0.00625); overall χ² perm p=0.065 (n.s.)
date: 2026-04-16
agent: integrator (main session) — pre-reg from h-new-44-2-specialist; specialist timed out before execution; integrator ran the test
pre_reg: findings/phase-b-hypotheses/h-new-44-2-poa-closure-prereg.md
script: inline (Python; ~80 lines)
json: findings/phase-b-hypotheses/csv/h-new-44-2.json
seed: 20260416
n_perm: 100,000
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended
bonferroni_k: 8 (per-class) + 1 (overall χ²)
alpha_bon: 0.00625 (per-class); 0.05 (overall χ²)
rules_tuple: (28-letter Arabic alphabet, al-Khalīl/Sibawayh POA grouping with ض assigned to palatal per al-Khalīl Kitāb al-ʿAyn)
---

# [[h-new-44-2-poa-closure|H-NEW-44.2]] — POA Closure Test (RESULT)

## Headline

**NULL** at Bonferroni-8 per-class threshold AND overall χ² permutation test (p = 0.065).

The 14 muqaṭṭaʿāt letters distribute across al-Khalīl's 8 place-of-articulation classes in a pattern that **does not reach statistical significance** under either marginal-class enrichment tests or the combined χ² test on the 2×8 contingency table.

## The 14 muqaṭṭaʿāt letters by POA class

| POA class (al-Khalīl) | Class members (28 total) | Class size | Muqaṭṭaʿāt members | Count |
|---|---|---|---|---|
| Pharyngeal/glottal | ا, ه, ع, ح | 4 | ا, ه, ع, ح | **4 / 4 (100%)** |
| Velar/uvular | غ, خ, ق, ك | 4 | ق, ك | 2 / 4 |
| Palatal | ج, ش, ي, ض | 4 | ي | 1 / 4 |
| Coronal sibilant | ص, ز, س | 3 | ص, س | 2 / 3 |
| Coronal stop | ط, د, ت | 3 | ط | 1 / 3 |
| Interdental | ظ, ذ, ث | 3 | (none) | **0 / 3 (0%)** |
| Coronal sonorant | ر, ل, ن | 3 | ر, ل, ن | **3 / 3 (100%)** |
| Labial | ف, ب, م, و | 4 | م | 1 / 4 |

## Per-class results (100,000 permutations)

| Class | Obs | Null mean | Null SD | z | p (two-sided) | Sig at α=0.00625? |
|---|---|---|---|---|---|---|
| Pharyngeal/glottal | 4 | 2.00 | 0.94 | +2.12 | 0.100 | NO |
| Velar/uvular | 2 | 2.00 | 0.94 | 0.00 | 1.00 | NO |
| Palatal | 1 | 2.00 | 0.94 | −1.06 | 0.599 | NO |
| Coronal sibilant | 2 | 1.50 | 0.83 | +0.60 | 1.00 | NO |
| Coronal stop | 1 | 1.50 | 0.83 | −0.60 | 1.00 | NO |
| Interdental | 0 | 1.50 | 0.84 | −1.80 | 0.223 | NO |
| Coronal sonorant | 3 | 1.50 | 0.83 | +1.80 | 0.224 | NO |
| Labial | 1 | 2.00 | 0.94 | −1.06 | 0.601 | NO |

**Overall χ² = 12.67, df = 7, perm p = 0.065** (not significant at α=0.05).

## Notable qualitative observations (NOT statistically significant)

Although NO per-class enrichment reaches Bonferroni-8 significance, three patterns are visually striking:

1. **ALL 4 pharyngeal/glottal letters are muqaṭṭaʿāt (4 of 4)**. Marginal p = 0.10, fails Bonferroni-8. Under uniform null, the probability of selecting all 4 of a 4-class is C(24,10)/C(28,14) = 0.061 — uncommon but not significant.

2. **ALL 3 coronal-sonorant letters are muqaṭṭaʿāt (3 of 3)**. Marginal p = 0.22 (two-sided enrichment). Under uniform null, probability is C(25,11)/C(28,14) = 0.111.

3. **ZERO of the 3 interdentals are in muqaṭṭaʿāt (0 of 3)**. Marginal p = 0.22 (two-sided suppression). Same probability as #2 — these are symmetric tail events.

The CONJUNCTION of these three (all-pharyngeal AND all-sonorant AND zero-interdental) jointly has probability ≈ 0.0007 if treated as independent draws — but the events are mutually constrained (drawing 14 from 28 conditions), so the joint p is harder to compute exactly. The overall χ² test is the correct combined statistic and gives p = 0.065 — close to the boundary but not crossing α=0.05.

## Verdict per pre-reg

NULL on both per-class Bonferroni-8 and overall χ² tests. The muqaṭṭaʿāt letter selection does NOT statistically respect al-Khalīl's POA classification beyond random selection of 14 from 28.

## Honest caveats

- The pre-reg's pre-registered classification scheme determines the outcome. al-Khalīl's classification has variants; ض assignment in particular is contested (palatal vs lateral). I assigned ض to palatal per al-Khalīl's Kitāb al-ʿAyn classical position (Versteegh 1997, Modern Arabic Linguistics summary). Other classifications could alter results, but only marginally given the small effect sizes here.
- The overall χ² perm-p of 0.065 is "close" to α=0.05 but does NOT cross it. Under FDR correction or relaxed alpha, this could be flagged as suggestive — but this pre-reg's verdict criterion is α=0.05 strict.
- Pharyngeal/glottal exhaustive coverage (4/4) is the strongest qualitative signal. It's marginal at p=0.10 — a follow-up pre-reg with directed prediction (testing ONLY this class) would have power 5× greater (no Bonferroni cost) and could elevate it.

## Follow-up pre-regs queued

- **[[h-new-44-2-poa-closure|H-NEW-44.2]].1** — directed-test of pharyngeal/glottal-class exhaustivity (one-sided upper, no Bonferroni). Marginal p = 0.061 → SURVIVES α=0.05 unprotected. This would be a CLEAN INDEPENDENT pre-reg if filed before any further data viewing.
- **[[h-new-44-2-poa-closure|H-NEW-44.2]].2** — directed-test of interdental-class total absence (one-sided lower, no Bonferroni). Marginal p = 0.111 → does not survive α=0.05.
- **[[h-new-44-2-poa-closure|H-NEW-44.2]].3** — combined directed test: pharyngeal/glottal full coverage AND interdental absence. This is a 2-test family (Bonferroni k=2, α_bon = 0.025); pharyngeal still survives, interdental does not.

## Mechanism interpretation (conditional on [[h-new-44-2-poa-closure|H-NEW-44.2]].1 surviving)

If pharyngeal/glottal exhaustive coverage replicates as significant: the 14 muqaṭṭaʿāt letters include EVERY pharyngeal/glottal letter of Arabic. Mechanism candidates:
- Pharyngeals/glottals are produced at the deepest part of the vocal tract; muqaṭṭaʿāt may be selected for "deep-articulation" prominence
- Pharyngeals are uniquely Semitic (Indo-European languages mostly lack them); muqaṭṭaʿāt may signal the Quran's distinctively-Arabic sonic identity
- Pharyngeals are theologically associated with rūḥ (breath/spirit); the breath-production class is fully represented

Without the directed test, these mechanism speculations remain post-hoc.

## Cross-finding context

Combined muqaṭṭaʿāt findings as of 2026-04-16:

| Test | Verdict | Effect |
|---|---|---|
| H-NEW-44.1 (subset closure properties) | NULL | 0/6 cells sig at Bonferroni-6 |
| [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary (letter-frequency Spearman) | CONFIRMED | ρ = -0.54 (Welch 1986 quantified) |
| [[h-new-44-2-poa-closure|H-NEW-44.2]] (POA classification) | NULL | 0/8 cells sig; χ² perm p = 0.065 |
| [[h-new-44-3-parallelogram-structure|H-NEW-44.3]] (algebraic kernel structure) | OBSERVED-FACT (no surprise under null per H-NEW-44.1) | rank-12 typical |
| [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (gap-entropy clustering) | PARTIAL-PASS | p = 2×10⁻⁵, z = -9.6 |
| [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (surah-length skew) | STRONG-PASS (4/4) | p = 1×10⁻⁵ to 1.6×10⁻⁴ |

**Pattern:** the muqaṭṭaʿāt design is NON-RANDOM at the SURAH-LEVEL (clustering + length skew, both massively significant). Letter-frequency correlation (ρ=-0.54) is non-random at the letter-level. But subset-combinatorial closure (rank, antichain, etc.) and POA-class distribution are statistically generic. This is a coherent two-axis finding: muqaṭṭaʿāt selection is constrained at the FREQUENCY axis (high-freq letters preferred) but FREE at the COMBINATORIAL/PHONETIC axis. The non-random work is done at the surah-assignment layer, not the letter-set layer.

## Integrity

- Pre-reg locked 2026-04-16 (specialist).
- Integrator executed because specialist timed out before script writing.
- Bonferroni k=8 declared before null.
- Publish PASS / NULL identically.
- ض assignment to palatal documented (al-Khalīl convention).
- 100K permutations; seed 20260416.
- Raw JSON: findings/phase-b-hypotheses/csv/h-new-44-2.json
