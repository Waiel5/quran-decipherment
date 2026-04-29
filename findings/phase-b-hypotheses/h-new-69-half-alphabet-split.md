---
id: H-NEW-69
title: Half-alphabet split — muqaṭṭaʿāt vs classical 14-of-28 groupings
phase: B
status: NULL — 0/8 groupings significant at Bonferroni-8 (α=0.00625), 0/8 at unprotected α=0.05
date: 2026-04-15
agent: h-new-69-specialist
pre_reg: findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md
script: scripts/h_new_69_half_alphabet_split.py
json: findings/phase-b-hypotheses/csv/h-new-69.json
test: closed-form exact hypergeometric per grouping
verdict: NULL
rules_tuple: (28-letter Arabic orthographic alphabet, hamza folded into alif, classical Sibawayh/al-Khalīl/al-Zamakhsharī classifications)
---

# [[h-new-69-half-alphabet-split|H-NEW-69]] — Half-Alphabet Split (RESULT)

## Headline

**NULL.** None of the 8 tested classical 14-of-28 (or near-14) groupings
predicts the muqaṭṭaʿāt-set significantly. The "exactly 14 of 28" property
of the muqaṭṭaʿāt is **NOT explained** by the shamsiyyah/qamariyyah split,
nor by either Sibawayh's or modern phonetic voicing classification, nor
by sibilant or emphatic groupings.

The 14-of-28 coincidence appears to be **independent** of the major
classical 14-cuts of the Arabic alphabet.

## Per-grouping overlap table

| Grouping | Source | |G| | k_obs | E[k] | Jaccard | direction | p (two-sided) | Bonferroni-8? |
|---|---|---|---|---|---|---|---|---|
| G1 shamsiyyah | Zamakhsharī Mufaṣṣal §82 | 14 | 6 | 7.0 | 0.273 | depleted | 0.706 | NO |
| G2 qamariyyah | complement of G1 | 14 | **8** | 7.0 | **0.400** | enriched | 0.706 | NO |
| G3 majhūra (Sibawayh) | al-Kitāb IV ch. 565 | 18 | 9 | 9.0 | 0.391 | neutral | 1.000 | NO |
| G4 mahmūsa (Sibawayh) | al-Kitāb IV ch. 565 | 10 | 5 | 5.0 | 0.263 | neutral | 1.000 | NO |
| G5 modern-voiced | Watson 2002 | 16 | 7 | 8.0 | 0.304 | depleted | 0.704 | NO |
| G6 modern-voiceless | Watson 2002 | 12 | 7 | 6.0 | 0.368 | enriched | 0.704 | NO |
| G7 ṣafīr (sibilants) | Sibawayh / al-Khalīl | 3 | 2 | 1.5 | 0.133 | enriched | 1.000 | NO |
| G8 iṭbāq (emphatics) | Sibawayh / al-Mubarrad | 4 | 2 | 2.0 | 0.125 | neutral | 1.000 | NO |

**Best-matching: G2 qamariyyah (moon letters)** — but at Jaccard 0.400 with
p = 0.706, this is NOT statistically distinguishable from random selection.

## What the data show

### The shamsiyyah/qamariyyah split — TIGHT NEAR-MISS

The most natural classical 14-of-28 partition is sun/moon letters, defined
by whether the lām of the definite article assimilates. The muqaṭṭaʿāt
overlap is k=8 with qamariyyah (moon, expected 7.0), and k=6 with
shamsiyyah (sun, expected 7.0). This is a TINY enrichment of qamariyyah
by 1 letter — far from statistical significance (p = 0.706).

Letter breakdown:
- **Muqaṭṭaʿāt that are qamariyyah (moon):** ا, ح, ع, ق, ك, م, ه, ي (8)
- **Muqaṭṭaʿāt that are shamsiyyah (sun):** ر, س, ص, ط, ل, ن (6)
- **Qamariyyah NOT in muqaṭṭaʿāt:** ب, ج, خ, غ, ف, و (6)
- **Shamsiyyah NOT in muqaṭṭaʿāt:** ت, ث, د, ذ, ز, ش, ض, ظ (8)

The overlap pattern is essentially what we'd expect from random selection of
14 from 28. The shamsiyyah/qamariyyah hypothesis as a "deep generator" of
the muqaṭṭaʿāt set is FALSIFIED.

### Sibawayh majhūra/mahmūsa — EXACT MATCH TO EXPECTATION

For Sibawayh's voicing classification (G3=18 voiced, G4=10 voiceless),
muqaṭṭaʿāt overlap is **exactly the hypergeometric expectation**:
k=9 vs E=9.0 for majhūra, k=5 vs E=5.0 for mahmūsa.

This is a striking NULL — the muqaṭṭaʿāt selection is voicing-NEUTRAL
under Sibawayh's classification.

Per memory note [[h-new-44-2-poa-closure|H-NEW-44.2]]'s "~7-7 split" claim: under MODERN voicing
(G5=16 voiced, G6=12 voiceless), muqaṭṭaʿāt split is 7 voiced + 7 voiceless.
This matches the prior observation but the test reveals the 7-7 IS the
expected ratio under random selection given the asymmetric class sizes —
not a meaningful pattern.

### ṣafīr (sibilants) and iṭbāq (emphatics)

- **Sibilants {ز, س, ص}:** muqaṭṭaʿāt include 2 of 3 (س, ص, missing ز). Under
  hypergeometric this gives p = 1.0 (the "expected" overlap of 1.5
  rounded down to 1 or up to 2).
- **Emphatics {ص, ض, ط, ظ}:** muqaṭṭaʿāt include exactly 2 of 4 (ص, ط,
  missing ض, ظ). Perfectly balanced — exactly the expected 2.0.

Both are NEUTRAL with respect to their natural complements.

## MW-5 positive controls — both PASS

- **MW5 planted-full** (`U_planted = G1` exactly): k=14/14 vs c=14, p=4.99×10⁻⁸ ✓
- **MW5b planted-one-swap** (`U_planted = G1 with ت→ك`): k=13/14, p=9.82×10⁻⁶ ✓

Pipeline correctly detects both planted signals far below their thresholds
(1×10⁻⁷ and 1×10⁻³). The NULL on real data is genuine, not a pipeline
failure.

## Phonotactic side-test (descriptive, NOT in Bonferroni family)

| Class | Total in alphabet | In muqaṭṭaʿāt | In non-muqaṭṭaʿāt |
|---|---|---|---|
| Sonorants | 6 (ر ل م ن و ي) | **5/6** (ر ل م ن ي; missing و) | 1/6 (و) |
| Stops | 7 (ا ب ت د ط ك ق) | 4/7 (ا ط ق ك) | 3/7 (ب ت د) |
| Fricatives | 14 (ث ح خ ذ ز س ش ص ض ظ ع غ ف ه) | 5/14 (ح س ص ع ه) | 9/14 (ث خ ذ ز ش ض ظ غ ف) |

### Striking observation (post-hoc, NOT in Bonferroni family)

**5 of 6 Arabic sonorants are in the muqaṭṭaʿāt** — only و excluded.
Hypergeometric p = C(6,5) × C(22,9) / C(28,14) = 6 × 497,420 / 40,116,600
= 0.0744 single-test (one-sided enrichment) — does not reach α=0.05 even
unprotected. But qualitatively, this aligns with [[h-new-44-2-poa-closure|H-NEW-44.2]]'s observation
that "all 3 coronal sonorants {ر, ل, ن}" are in the muqaṭṭaʿāt; the
sonorant pattern extends to nasals (م, ن) and the palatal glide (ي).

The single sonorant excluded — و (waw) — was also one of the two dotless
exceptions in [[h-new-60-muqattaat-dotless-preference|H-NEW-60]]. Convergence: **و appears to be systematically
excluded** across multiple muqaṭṭaʿāt-design axes despite being dotless,
sonorant, and high-frequency. This deserves its own follow-up pre-reg.

### Fricative depletion (post-hoc, NOT in Bonferroni family)

The muqaṭṭaʿāt include only 5 of 14 fricatives (35.7%, vs expected 50%).
Hypergeometric: P(K ≤ 5 | N=28, K=14, n=14) = ~0.135 — not significant
unprotected. But combined with the sonorant enrichment, the qualitative
pattern is **muqaṭṭaʿāt prefer sonorants over fricatives** — also
post-hoc and not in this pre-reg's family.

## What this DOES claim

- The shamsiyyah/qamariyyah "exactly 14 vs 14" split is **NOT** the
  generator of the muqaṭṭaʿāt's 14-of-28 property. The two 14-cuts of the
  alphabet are independent.
- Neither Sibawayh's nor the modern voicing classification predicts
  muqaṭṭaʿāt membership.
- The "14 of 28" property of the muqaṭṭaʿāt is robust across these
  classical groupings — it does not coincide with any well-known classical
  binary partition.

## What this does NOT claim

- That the muqaṭṭaʿāt's 14-of-28 has NO phonological generator — only
  that the 8 tested classical groupings do not provide one.
- That post-hoc-noticed patterns (sonorant 5/6, fricative depletion,
  و-exclusion) are statistically significant — they require their own
  pre-registered tests on independent data dimensions.
- That the muqaṭṭaʿāt are phonologically random — [[h-new-44-2-poa-closure|H-NEW-44.2]].1 (PASS)
  shows the pharyngeal/glottal class is exhaustively covered, and
  [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] (STRONG-PASS) shows dotless preference. The muqaṭṭaʿāt ARE
  non-random; just not explained by these particular 14-of-28 splits.

## Cross-finding context

| Test | Verdict | Effect on muqaṭṭaʿāt phonology |
|---|---|---|
| H-NEW-44.1 (combinatorial closure) | NULL | algebraic structure generic |
| [[h-new-44-2-poa-closure|H-NEW-44.2]] (al-Khalīl 8 POA classes) | NULL | distributes across all classes |
| [[h-new-44-2-poa-closure|H-NEW-44.2]].1 (pharyngeal/glottal exhaustivity) | PASS-DIRECTED | all 4 covered (p=0.049) |
| [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] (dotless preference) | STRONG-PASS | 11/13 dotless in muqaṭṭaʿāt (p=0.0009) |
| **[[h-new-69-half-alphabet-split|H-NEW-69]] (8 classical 14-cuts)** | **NULL** | no classical binary partition predicts membership |

**Pattern.** The muqaṭṭaʿāt are non-random along **orthographic** (dotless
preference) and **deepest-articulation** (pharyngeal exhaustivity) axes, but
**generic** along combinatorial-algebraic, full-POA-distribution, and
classical-binary-partition axes. The selection signal is concentrated on
1-2 specific properties, not on broad classical phonological groupings.

The "14-of-28" property is NOT a side-effect of being shamsiyyah, qamariyyah,
voiced, voiceless, sibilant, or emphatic. It appears to be a **standalone**
constraint of the muqaṭṭaʿāt design, possibly emergent from combinations
of the dotless + pharyngeal + sonorant biases acting jointly.

## Honest caveats

1. **NULL outcome on PRE-REGISTERED test.** Per project discipline (publish
   PASS / NULL identically): the qamariyyah enrichment of k=8 vs E=7 is a
   1-letter excess and does not approach significance.
2. **Post-hoc observations** (sonorant 5/6; fricative depletion; و-exclusion
   convergence) are flagged as POST-HOC and NOT counted toward the verdict.
   They earn replication-pre-reg status but no statistical claim here.
3. **Bonferroni-8 includes G1+G2 separately** even though they are
   mathematically equivalent (k_qamariyyah = 14 - k_shamsiyyah). This is
   intentionally CONSERVATIVE — the Bonferroni cost on the actual
   information is k=7 (8 - 1 dependence), so even with k=7 the conclusion
   would be NULL (max two-sided p = 0.704; α_per_grouping at k=7 = 0.0071
   — still NS).
4. **Sibawayh's "majhūra" includes ṭ, ḍ, ʾ which modern phonetics calls
   voiceless**: the discrepancy between G3/G4 vs G5/G6 reflects a real
   classical-vs-modern divergence. We tested both — both NULL.
5. **The هurūf al-zalāqa (6) and هurūf al-iṣmāt (22) groupings were
   excluded** as not 14-of-28 — but per pre-reg §9 this exclusion was
   documented and not post-hoc.

## Verdict

**NULL.** None of the 8 pre-registered classical 14-of-28 (or near-14)
groupings predicts the muqaṭṭaʿāt-set membership. The muqaṭṭaʿāt's
"exactly half" property is independent of shamsiyyah/qamariyyah, voicing
(both Sibawayh's and modern), sibilants, and emphatics.

The best-matching grouping is **qamariyyah (moon letters)** at Jaccard 0.400
with p = 0.706 — far from significance.

**Recommendation:** add to cross-finding-006 / cross-finding-008 as the
13th muqaṭṭaʿāt-design axis tested, with NULL verdict. The "14-of-28"
property of the muqaṭṭaʿāt is now established as INDEPENDENT of the major
classical Arabic 14-cuts.

## Integrity

- Pre-reg locked 2026-04-15 BEFORE script execution.
- Closed-form exact hypergeometric (no Monte Carlo); reproducible by inspection.
- All 8 grouping memberships locked from classical sources before run.
- MW-5 + MW-5b positive controls both PASS.
- MW-7 internal-error gate: PASS (all p-values in [0,1], partition arithmetic verified).
- Publish PASS/NULL identically per project standard.
- Post-hoc observations clearly flagged.
- Raw JSON: findings/phase-b-hypotheses/csv/h-new-69.json
- Script self-hash: see JSON.
