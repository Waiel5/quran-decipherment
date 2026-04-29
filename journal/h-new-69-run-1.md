---
journal_entry: h-new-69-run-1
date: 2026-04-15
agent: h-new-69-specialist
pre_reg: findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md
parent_runs: H-NEW-44.2 (POA NULL); H-NEW-44.2.1 (pharyngeal PASS); H-NEW-60 (dotless STRONG-PASS)
---

# Journal — H-NEW-69 run 1

## Task

Pre-register and execute H-NEW-69 — analyze the 14 muqaṭṭāʿat letters
{ا, ح, ر, س, ص, ط, ع, ق, ك, ل, م, ن, ه, ي} vs the OTHER 14
{ب, ت, ث, ج, خ, د, ذ, ز, ش, ض, ظ, غ, ف, و}. Test whether the 14-of-28
split corresponds to known classical Arabic groupings (shamsiyyah/
qamariyyah, majhūra/mahmūsa, etc.). Identify any best-matching grouping
and any novel structural complementarity.

## Method

Closed-form exact hypergeometric per grouping. 8 classical groupings
locked from authoritative sources (Sibawayh al-Kitāb, al-Khalīl Kitāb
al-ʿAyn, al-Zamakhsharī al-Mufaṣṣal, Watson 2002 *Phonology and
Morphology of Arabic*).

Bonferroni-8 family. α_per_grouping = 0.05/8 = 0.00625 (two-sided).

## Locked groupings

| # | Grouping | Source | |G| |
|---|---|---|---|
| G1 | shamsiyyah (sun) | Zamakhsharī Mufaṣṣal §82 | 14 |
| G2 | qamariyyah (moon) | complement of G1 | 14 |
| G3 | majhūra-Sibawayh | al-Kitāb IV ch. 565 | 18 |
| G4 | mahmūsa-Sibawayh | al-Kitāb IV ch. 565 | 10 |
| G5 | modern-voiced | Watson 2002 | 16 |
| G6 | modern-voiceless | Watson 2002 | 12 |
| G7 | ṣafīr (sibilants) | Sibawayh / al-Khalīl | 3 |
| G8 | iṭbāq (emphatics) | Sibawayh / al-Mubarrad | 4 |

## Garden-of-forking-paths log (BEFORE viewing data)

10 pre-locked decisions in pre-reg §9. Notable:
- 28-letter orthographic alphabet, hamza folded into alif (matches H-NEW-44.2 convention).
- Bonferroni-8 includes G1+G2 separately despite mathematical equivalence
  (k_2 = 14 - k_1 deterministic). Conservative inflation — does not change
  NULL outcome.
- Two-sided exact p via doubled-smaller-tail.
- ḥurūf al-zalāqa (6) and ḥurūf al-iṣmāt (22) EXCLUDED (not 14-of-28 splits).
- Sibawayh majhūra includes ṭ, ḍ, ʾ as voiced (classical convention);
  G3/G4 distinct from modern G5/G6.

## Engineering

- Pure-Python `math.comb`; no numpy required for closed-form.
- 8 hypergeometric calculations + 2 MW-5 controls + 1 phonotactic descriptor.
- Runtime: <1 second.

## Timeline

- 2026-04-15: Read pre-reg, parent findings (H-NEW-44.2, H-NEW-44.2.1, H-NEW-60).
- Wrote `findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md`.
- Wrote `scripts/h_new_69_half_alphabet_split.py` (~280 lines).
- Verified MW-5 positive control: planted U_planted = G1 → p = 4.99×10⁻⁸ ✓
- Verified MW-5b: planted G1 with 1 swap → p = 9.82×10⁻⁶ ✓
- Ran main test. All 8 groupings NULL (p > 0.7 across the board).
- Wrote findings + JSON + this journal.

## Results

```
G1 shamsiyyah        c=14 k= 6 E=7.0  jaccard=0.273  p_two=0.706  [DEPLETED]   n.s.
G2 qamariyyah        c=14 k= 8 E=7.0  jaccard=0.400  p_two=0.706  [ENRICHED]   n.s.
G3 majhura_Sib       c=18 k= 9 E=9.0  jaccard=0.391  p_two=1.000  [NEUTRAL]    n.s.
G4 mahmusa_Sib       c=10 k= 5 E=5.0  jaccard=0.263  p_two=1.000  [NEUTRAL]    n.s.
G5 modern_voiced     c=16 k= 7 E=8.0  jaccard=0.304  p_two=0.704  [DEPLETED]   n.s.
G6 modern_voiceless  c=12 k= 7 E=6.0  jaccard=0.368  p_two=0.704  [ENRICHED]   n.s.
G7 safir             c= 3 k= 2 E=1.5  jaccard=0.133  p_two=1.000  [ENRICHED]   n.s.
G8 itbaq             c= 4 k= 2 E=2.0  jaccard=0.125  p_two=1.000  [NEUTRAL]    n.s.

BEST-MATCHING: G2 qamariyyah (p = 0.706)

n_significant_Bonferroni-8: 0 / 8
n_significant_unprotected:  0 / 8

VERDICT: NULL
```

## Striking observations (NOT in pre-reg family — POST-HOC)

1. **5 of 6 sonorants in muqaṭṭaʿāt** ({ر, ل, م, ن, ي}; missing only و).
   p_unprotected = 0.074 single-test; not significant.
2. **Fricative depletion**: 5/14 fricatives in muqaṭṭaʿāt (35.7% vs expected 50%).
   p_unprotected ≈ 0.135.
3. **Convergence on و-exclusion**: و is the single sonorant excluded AND
   one of two dotless exceptions in H-NEW-60. The waw seems to be
   systematically excluded across multiple muqaṭṭaʿāt-design axes despite
   meeting most "muqaṭṭaʿāt-favored" criteria. **Worthy of independent
   pre-reg.**
4. **Sibawayh majhūra/mahmūsa lands EXACTLY at expectation** (k=9 vs E=9.0
   and k=5 vs E=5.0). The muqaṭṭaʿāt is voicing-NEUTRAL under classical
   classification — even more "perfectly random" than under random selection.
5. **Iṭbāq (emphatics) split exactly 2-2** of {ص, ض, ط, ظ}: muqaṭṭaʿāt
   include ص and ط (the velarized stops/sibilants); exclude ض and ظ
   (the velarized fricatives/laterals). This is descriptively striking
   but per the test NEUTRAL.

## Falsifications established

- **Shamsiyyah/qamariyyah hypothesis** for the muqaṭṭaʿāt 14-of-28 property:
  REJECTED (p = 0.706).
- **Voicing hypothesis** (Sibawayh OR modern): REJECTED (p ≥ 0.704).
- **Sibilant clustering**: REJECTED.
- **Emphatic clustering**: REJECTED.

The "exactly 14 of 28" property of the muqaṭṭaʿāt is **independent** of
the major classical Arabic binary alphabet partitions.

## MW-7 internal error gate

PASS. All 8 p-values in [0, 1]; alphabet partitions verify; both MW-5
positive controls detect their planted signals at p < threshold.

## Deliverables

- findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md
- findings/phase-b-hypotheses/h-new-69-half-alphabet-split.md
- findings/phase-b-hypotheses/csv/h-new-69.json
- scripts/h_new_69_half_alphabet_split.py
- journal/h-new-69-run-1.md (this file)

## Honest caveats

- The G1/G2 pair is mathematically dependent (k_2 = 14 - k_1); we
  Bonferroni-counted both as a transparency measure (we DID inspect both).
  The "honest" Bonferroni count is 7. Even with α_per = 0.05/7 = 0.00714,
  the conclusion is identical.
- The Sibawayh G3/G4 and modern G5/G6 pairs are also dependent, so the
  effective independent test count is more like 4 (G1-vs-G2 pair, G3-vs-G4
  pair, G5-vs-G6 pair, G7, G8) plus dependence between G3/G4 and G5/G6
  via shared phonological logic. The conservative Bonferroni-8 dominates.
- The post-hoc sonorant 5/6 observation crosses the unprotected α=0.05
  bar at p=0.074 — close but doesn't make it. Cannot be elevated without
  independent pre-reg replication.
- Result is a CLEAN NULL on a tightly pre-registered family. This is
  legitimate scientific evidence AGAINST the shamsiyyah/qamariyyah
  hypothesis as the muqaṭṭaʿāt-generator.

## What I'd do next (queued for follow-up)

1. **H-NEW-70 (proposed)** — pre-register a directed test of the و-exclusion
   pattern: across H-NEW-60 (dotless) + H-NEW-44.2 (sonorant) + H-NEW-69
   (qamariyyah), و is repeatedly the "missing piece". Joint rejection
   probability could be computed under independence-null.
2. **H-NEW-71 (proposed)** — sonorant-enrichment directed test as
   independent replication of the post-hoc observation.
3. **H-NEW-72 (proposed)** — fricative-depletion directed test.

These are queued but NOT executed in this run — they would be tuple-shopping
violations if executed by the same agent in the same wave.

## No promotion to MASTER-FINDINGS-LEDGER §1

Per pre-reg, NULL verdict means no §1 promotion. The result IS valuable as
a clean falsification of the shamsiyyah/qamariyyah-as-generator hypothesis
and warrants §3 inclusion (FALSIFIED HYPOTHESES) and cross-finding-006/008
addition as the 13th independent muqaṭṭaʿāt-design axis tested.
