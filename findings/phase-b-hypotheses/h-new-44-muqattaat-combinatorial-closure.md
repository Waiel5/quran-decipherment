---
id: H-NEW-44
title: Muqaṭṭaʿāt Combinatorial Closure — full 10K null result (NULL verdict)
phase: B
status: NULL
date: 2026-04-15
agent: h-new-44-1-specialist (numpy-vectorized rerun of compute-blocked H-NEW-44)
pre_reg: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md
script_observed: scripts/h_new_44_observed_only.py
script_null: scripts/h_new_44_1_muqattaat_null.py
json: findings/phase-b-hypotheses/csv/h-new-44.json
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
bonferroni_family: 2026-04-15-Fresh-Wave-3b
bonferroni_k: 6
alpha_cell: 0.00833
seed: 20260415
verdict: NULL
n_significant_after_bonferroni: 0/6
---

# [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] — Muqaṭṭaʿāt Combinatorial Closure (full 10K null)

## Status

**NULL.** All six pre-registered combinatorial-closure properties of the 14 canonical muqaṭṭaʿāt subsets are statistically generic when compared against 10,000 cardinality-matched uniform random subset families. After Bonferroni-6 correction (α-cell = 0.00833), **0 of 6 properties are significant**.

The deterministic algebraic facts (rank-12, two Boolean decompositions, one multiset partition relation) survive — they are real combinatorial features of F. But under the cardinality-matched uniform null, these features are ubiquitous, not surprising.

## Garden-of-forking-paths amendments (filed BEFORE null run)

Two pre-run amendments to the pre-registered method, both TIGHTENING under the project's Bonferroni-asymmetry standard (self-verifying):

1. **`boolean_rank` approximated by `gf2_rank`.** GF(2)-rank ≤ boolean-rank-within-F for 0/1 matrices, so `gf2_rank == 14 ⇒ boolean_rank == 14`. Reverse can fail. Since observed `boolean_rank == 12 ≠ 14`, the cell test is `P(null is FALSE)`, and the proxy `P(null gf2_rank ≠ 14) ≥ P(null boolean_rank ≠ 14)` — i.e. the observed-FALSE p-value under proxy ≥ true p-value, more conservative.

2. **`poset_width_14` derived from `is_antichain`.** Width=14 in a 14-element poset means the maximum antichain spans the whole family — equivalent to the family itself being an antichain (when all 14 rows are distinct, which holds for the observed and any cardinality-matched null with 14 distinct draws). EXACT, not an approximation. Saves the O(2^14) brute-force inner loop.

Both amendments are self-verifying per the Bonferroni-tightening-vs-loosening standard (memory: `feedback_bonferroni_tightening_vs_loosening.md`). MW-5 positive control passes.

## The 14 canonical muqaṭṭaʿāt subsets

| # | Letters | Cardinality | Surahs that open with it |
|---|---|---|---|
| 1 | ص | 1 | Q 38 Ṣād |
| 2 | ق | 1 | Q 50 Qāf |
| 3 | ن | 1 | Q 68 al-Qalam |
| 4 | ط, ه | 2 | Q 20 Ṭā-Hā |
| 5 | ي, س | 2 | Q 36 Yā-Sīn |
| 6 | ط, س | 2 | Q 27 al-Naml |
| 7 | ح, م | 2 | Q 40–46 (7 Ḥā-Mīm cluster) |
| 8 | ا, ل, م | 3 | Q 2, 3, 29, 30, 31, 32 |
| 9 | ا, ل, ر | 3 | Q 10, 11, 12, 14, 15 |
| 10 | ط, س, م | 3 | Q 26 al-Shuʿarāʾ, Q 28 al-Qaṣaṣ |
| 11 | ا, ل, م, ص | 4 | Q 7 al-Aʿrāf |
| 12 | ا, ل, م, ر | 4 | Q 13 al-Raʿd |
| 13 | ك, ه, ي, ع, ص | 5 | Q 19 Maryam |
| 14 | ح, م, ع, س, ق | 5 | Q 42 al-Shūrā |

Universe = ⋃ Sᵢ = {ا, ح, ر, س, ص, ط, ع, ق, ك, ل, م, ن, ه, ي} = exactly 14 letters (half the 28-letter alphabet).

## 6-property table with null

| Property | Observed | Null TRUE count / 10K | p-value (P(null = obs)) | Sig at α=0.00833? |
|---|---|---|---|---|
| Antichain | FALSE | 0 / 10000 | 1.0000 | NO |
| Intersection-closed | FALSE | 0 / 10000 | 1.0000 | NO |
| Real-rank = 14 | FALSE (rank=12) | 1370 / 10000 | 0.8630 | NO |
| Union = 14-letter universe | TRUE | 5022 / 10000 | 0.5022 | NO |
| Poset-width = 14 | FALSE (width=9) | 0 / 10000 | 1.0000 | NO |
| Boolean-rank = 14 | FALSE (rank=12; gf2=12) | 913 / 10000 (gf2=14) | 0.9087 | NO |

`p` here is the empirical frequency in the null of families having the SAME value of the property as observed (observed=TRUE → p = null_TRUE/10K; observed=FALSE → p = null_FALSE/10K).

**0 of 6 properties are significant after Bonferroni-6** (α-cell = 0.00833).

**Verdict: NULL** — the 14 muqaṭṭaʿāt subsets are combinatorially generic conditional on their cardinality distribution.

## Null distribution shape

| Real rank | Count / 10000 | Cumulative |
|---|---|---|
| 9 | 1 | 1 |
| 10 | 43 | 44 |
| 11 | 552 | 596 |
| 12 | 2991 | 3587 |
| 13 | 5043 | 8630 |
| 14 | 1370 | 10000 |

| GF(2) rank | Count / 10000 |
|---|---|
| 9 | 2 |
| 10 | 77 |
| 11 | 822 |
| 12 | 3566 |
| 13 | 4620 |
| 14 | 913 |

| Union size | Count / 10000 |
|---|---|
| 10 | 12 |
| 11 | 108 |
| 12 | 1017 |
| 13 | 3841 |
| 14 | 5022 |

**Striking:** The observed real-rank of 12 is the SECOND-most-common rank under uniform null (29.91% of draws), and the OBSERVED gf2_rank of 12 is the MOST-common gf2-rank (35.66%). The mode of the null real-rank distribution is 13 (50.43%), with rank-14 appearing only 13.7% of the time.

Equivalently: in random samples of 14 subsets of the 14-letter universe with cardinalities [1,1,1,2,2,2,2,3,3,3,4,4,5,5], the expected real rank is ~12.6, with rank-deficiency by 1-2 being typical. Observed rank-deficiency by 2 is on the more-common side of typical.

## Algebraic facts (DETERMINISTIC, preserved from observed-only pass)

These facts survive the NULL verdict because they are properties of the OBSERVED family; the verdict only says "this isn't statistically distinguishable from random under the chosen null."

### The two exact Boolean decompositions

```
1.  المص = ص ∪ الم          (i.e. {ا, ل, م, ص} = {ص} ∪ {ا, ل, م})
2.  المر = الم ∪ الر          (i.e. {ا, ل, م, ر} = {ا, ل, م} ∪ {ا, ل, ر})
```

**Decomposition 1:** Q 7 al-Aʿrāf's opener (المص) is the union of Q 38 Ṣād's opener ({ص}) and Q 2/3/29/30/31/32's opener ({ا, ل, م}).

**Decomposition 2:** Q 13 al-Raʿd's opener (المر) is the union of Q 2/3/29/30/31/32's opener ({ا, ل, م}) and Q 10/11/12/14/15's opener ({ا, ل, ر}).

### The one non-trivial ℝ-linear multiset relation

```
3.  طس + المر − الر − طسم = 0
```

Unpacked as multiset equality:

```
{ط, س} ⊎ {ا, ل, م, ر}  =  {ا, ل, ر} ⊎ {ط, س, م}
```

Both sides sum to the 6-letter multiset {ا, ل, ر, ط, س, م}. The muqaṭṭaʿāt of Q 27 al-Naml ({ط, س}) combined with those of Q 13 al-Raʿd ({ا, ل, م, ر}) form the same 6-letter multiset as the muqaṭṭaʿāt of Q 10–15 cluster ({ا, ل, ر}) combined with those of Q 26/28 ({ط, س, م}).

### Interpretation in light of NULL

Rank-12 (out of 14) is the second-most-common rank in random samples with this cardinality distribution. The two Boolean decompositions, while real, can be viewed as artifacts of the rank-deficiency that uniform sampling produces ~29% of the time. The observed Boolean decompositions remain noteworthy as concrete inclusion relations between specific surah openers — but they do not constitute statistical evidence of "engineering" beyond what cardinality-matched uniform sampling generates.

## Secondary: letter-frequency Spearman correlation

**Spearman ρ(is-muqaṭṭaʿa-letter, Quran-wide-letter-frequency-rank) = −0.5409** (n = 33 Arabic letters in the corpus including hamza variants and ة/ى).

Negative ρ means muqaṭṭaʿāt letters rank LOWER (= are MORE frequent). Quantifies Welch (1986)'s qualitative claim:

| Subset | Mean freq-rank |
|---|---|
| 14 muqaṭṭaʿāt letters | 11.0 |
| 19 non-muqaṭṭaʿāt letters | 21.4 |

The 14 letters DO skew toward high-frequency Arabic letters (effect size |ρ| > 0.5). This is a SEPARATE finding from the combinatorial null and stands on its own. It does not move the verdict on [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] PRIMARY (which is closure-properties), but it confirms a long-standing qualitative observation in the secondary axis.

## MW-5 Positive control (chain sizes 1..14)

Built {{1}}, {{1,2}}, ..., {{1..14}} — a chain of 14 nested prefixes through the 14-letter universe.

| Property | Expected | Actual | Pass? |
|---|---|---|---|
| Antichain | False | False | YES |
| Intersection-closed | True | True | YES |
| Real-rank = 14 | True | True | YES |
| Union = 14 | True | True | YES |
| Poset-width = 14 | False (width=1) | False (width=1) | YES |
| Boolean-rank = 14 | True | True | YES |

**Positive control PASSES.** Pipeline correctly recovers the chain's distinctive properties.

## MW-7 Internal-error gate

PASS. No out-of-bounds p-values; observed values consistent across observed-only-pass and current run; SHA-256 of corpus matches.

## Prior art and novelty

- **Welch 1986** (*Encyclopedia of Islam* muqaṭṭaʿāt entry): qualitative letter-frequency argument — confirmed quantitatively here (ρ = −0.54). Not surprising; it's a stable feature.
- **Nöldeke 1919** (*Geschichte des Qorans*): catalogs the 14 letters, no combinatorial analysis. Our test now formally rules in NULL on combinatorial closure under uniform-null.
- **Rashad Khalifa 1982**: 19-base counting scheme (debunked in Phase A; orthogonal to the present test).
- **Massey 1996**: each muqaṭṭaʿa as a mnemonic for the next surah's opening phrase — not a combinatorial test.
- **Al-Rāzī, *Mafātīḥ al-Ghayb*** — 12 mutually inconsistent theories of muqaṭṭaʿāt; none of them anchored the Boolean decomposition algebra.
- **The two Boolean decompositions and the multiset partition relation** are reported as observed combinatorial facts; they do NOT achieve significance under the cardinality-matched uniform null.

## Verdict

**[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] PRIMARY: NULL** (0 of 6 properties significant after Bonferroni-6 at α-cell = 0.00833).

**[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] SECONDARY (letter-frequency): PASS** (Spearman ρ = −0.54 confirms Welch 1986 quantitatively; one-sided test against the binomial null of "high-frequency-skew direction" is p ≈ 0.005 — see csv for letter-rank table).

**Algebraic facts:**
1. Real-rank of incidence matrix = 12; common (29.91% of cardinality-matched nulls).
2. Two Boolean decompositions: المص = ص ∪ الم and المر = الم ∪ الر — concrete cross-surah letter-set relations, not statistically surprising.
3. One ℝ-linear multiset relation: {ط,س} ⊎ {ا,ل,م,ر} = {ا,ل,ر} ⊎ {ط,س,م}.

These are real but combinatorially generic. The muqaṭṭaʿāt mystery is **NOT combinatorial** at the level of subset-algebra closure; the secondary letter-frequency skew remains a real signal in the data.

## Follow-up implications

- **[[h-new-44-2-poa-closure|H-NEW-44.2]]** queued: al-Khalīl place-of-articulation closure test (whether the 14 muqaṭṭaʿāt letters form any specific POA-class structure).
- **[[h-new-44-3-parallelogram-structure|H-NEW-44.3]]** queued: muqaṭṭaʿāt × surah-topic mutual information.
- The NULL verdict here means future muqaṭṭaʿāt hypotheses should focus on PHONETIC, SEMANTIC, or NARRATIVE structure rather than pure subset-algebra. The combinatorial axis is exhausted.

## Integrity

- Pre-reg filed 2026-04-15. Two amendments filed 2026-04-15 BEFORE the null run; both self-verify under Bonferroni-tightening (gf2_rank proxy is conservative; poset_width_14 ⇔ antichain is exact).
- MW-5 positive control PASS. MW-7 internal-error gate PASS.
- Seed 20260415. SHA-256 of `quran-no-tashkeel.json` archived in csv/h-new-44.json.
- 14 canonical muqaṭṭaʿāt subsets identical to pre-reg listing; no post-hoc subset substitution.
- Null sampling = 10K cardinality-matched uniform draws; same cardinality distribution as observed.
- Verdict published identically (PASS / EXPLORATORY / NULL / NULL-BROKEN regardless of direction); this is NULL.
- The Quran is one text; rules-tuple-independent algebraic facts (rank, Boolean decompositions) hold under any orthography variant.
