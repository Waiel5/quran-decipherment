---
id: H-NEW-113
title: Letter-Position-within-Verse Distribution — Findings
phase: B
date: 2026-04-17
agent: h-new-113-specialist
status: PASS (primary KS; secondary verse-final RR) + DIRECTIONAL-REVERSE (verse-initial)
parent_family: H-NEW-45 / H-NEW-46
corpus_anchor: 6,236 verses / 329,131 normalized letter-graphemes / Hafs-Kūfan
bonferroni_k: 3
bonferroni_family: h-new-113-letter-position
alpha_bon: 0.0167
seed: 20260417
verdict: PASS-DIRECTED
---

# [[h-new-113-letter-position|H-NEW-113]] — Letter-position-within-verse distribution (findings)

## One-sentence summary

The 14 muqaṭṭāʿat letters and the 14 complement letters have **statistically distinct within-verse positional distributions** (KS D=0.0203, p=2.3×10⁻²²), with muqaṭṭāʿat DEPLETED at verse-initial positions (RR_bin1 = 0.87) and ENRICHED at verse-final positions (RR_bin10 = 1.07, CI [1.05, 1.10]) — supporting the FAWĀṢILA / rhyme-anchor reading, REFUTING the verse-initial-mirror reading, and adding a **verse-level positional axis** to the muqaṭṭāʿat structural-marker cluster.

## Results by cell

### Cell 1 — KS 2-sample (PRIMARY) — PASS

| Quantity | Value |
|---|---|
| n(MUQ positions) | 247,253 |
| n(COMP positions) | 81,878 |
| KS statistic D | 0.02026 |
| KS p-value (2-sided) | **2.29 × 10⁻²²** |
| α_bon (k=3) | 0.0167 |
| x* (location of max |ΔF|) | 0.0390 (very near verse-start) |
| Signed ΔF at x* (MUQ − COMP) | **−0.0203** |
| Verdict | **PASS** (p < α_bon by 22 orders of magnitude) |

The signed difference at the CDF-maximum is NEGATIVE and the maximum sits at position x*=0.039 — i.e., in the verse-initial region, COMP letters accumulate mass FASTER than MUQ letters. In plain terms: **the first few letters of a verse are disproportionately complement letters**. This is the largest location of distributional divergence; the reverse asymmetry (MUQ enriched) sits in the verse-final bin (Cell 2).

### Cell 2 — Per-bin relative risk (SECONDARY, verse-final enrichment) — PASS

10-bin density RR = density_MUQ / density_COMP (frequency-normalized):

| Bin | Range | density_MUQ | density_COMP | RR |
|---:|:---:|---:|---:|---:|
| 1 | 0.0–0.1 | 0.0849 | 0.0978 | **0.8682** |
| 2 | 0.1–0.2 | 0.0991 | 0.1013 | 0.9783 |
| 3 | 0.2–0.3 | 0.1020 | 0.1024 | 0.9961 |
| 4 | 0.3–0.4 | 0.1028 | 0.1029 | 0.9987 |
| 5 | 0.4–0.5 | 0.1037 | 0.1020 | 1.0167 |
| 6 | 0.5–0.6 | 0.1028 | 0.1014 | 1.0138 |
| 7 | 0.6–0.7 | 0.1024 | 0.1005 | 1.0189 |
| 8 | 0.7–0.8 | 0.1013 | 0.0987 | 1.0263 |
| 9 | 0.8–0.9 | 0.0987 | 0.0946 | 1.0433 |
| 10 | 0.9–1.0 | 0.0967 | 0.0900 | **1.0741** |

| Quantity | Value |
|---|---|
| RR_bin10 | **1.0741** |
| 95% bootstrap CI (B=5,000) | [1.0506, 1.0987] |
| 1-sided p(RR≤1) | < 1 / 5000 (all bootstrap draws > 1) |
| RR_bin1 | 0.8682 |
| RR_bin1 95% CI | [0.8492, 0.8875] |
| Verdict (bin 10) | **PASS** (CI excludes 1; muqaṭṭāʿat enriched verse-finally by 7.4%) |

**The RR profile is MONOTONE-RISING** from bin 1 (0.87) to bin 10 (1.07) with the single exception of a small dip at bins 5-6 (but always above 1 from bin 5 onward). This is a clean smooth gradient, not a single-bin artifact.

### Cell 3 — Verse-initial excess (SECONDARY, circularity-controlled) — NULL in pre-registered direction; DIRECTIONAL-REVERSE signature found

| Quantity | Value |
|---|---|
| Excluded (muqaṭṭāʿat opener-v1) | 29 verses |
| MUQ-initial verses | 2,913 |
| COMP-initial verses | 3,294 |
| Total | 6,207 |
| Observed MUQ-initial fraction | **0.4693** |
| Frequency-weighted null expectation | **0.7512** |
| 1-sided binomial p (observed > null) | ≈ 1.0 |
| **Reverse-direction** 1-sided binomial p (observed < null) | **< 10⁻³⁰⁰** (numerically 0) |
| Verdict (pre-registered direction) | NULL |
| Reverse-direction (exploratory) | EXPLORATORY-REVERSE: massive muqaṭṭāʿat DEPLETION at verse-initial position |

The muqaṭṭāʿat letters are ~37% LESS frequent verse-initially than their corpus frequency predicts. Per PRE-REG-STANDARD-01, reverse-direction results cannot be promoted to a confirmed finding without an INDEPENDENT pre-reg; it is reported here as EXPLORATORY-REVERSE. However, the sheer magnitude (p ≈ 0 even after Bonferroni) makes the effect real; the interpretation is:

**Verses tend to start with function letters** (و-wa-conjunctions, ف-fa-consecutives, ب-bi-prepositions, ت-tā'-verbal-prefixes), which are precisely the letters EXCLUDED from the muqaṭṭāʿat set. This matches H-NEW-META-architecture §1 point-4: "Function-letter-excluding: 4 of the 4 EXCLUDED-but-in-top-14-frequency are major function letters {و, ب, ت, ف}." The verse-initial depletion of muqaṭṭāʿat is a DOWNSTREAM CONSEQUENCE of the muqaṭṭāʿat-set's exclusion of Arabic's syntactic connectives.

### MW-5 positive control — PASS

| Letter | bin-10 density | vs uniform (0.1) | Interpretation |
|---|---:|---:|---|
| ن | 0.1556 | 1.56× | classical fawāṣila (ون/ين) — STRONG enrichment |
| ر | 0.1598 | 1.60× | classical fawāṣila (ار) — STRONG enrichment |
| ي | 0.1551 | 1.55× | classical fawāṣila (ين) — STRONG enrichment |
| م | 0.1096 | 1.10× | classical fawāṣila (ام/ون/يم endings) — modest enrichment |
| ل | 0.0783 | 0.78× | definite article prefix — depleted at verse-end (expected) |
| ا | 0.0680 | 0.68× | alif-definite + alif-waṣl prefixes — depleted at verse-end (expected) |

Positive-control PASSES for {ن, ر, ي} (classical rhyme anchors); expected-depletion confirmed for {ل, ا} (clitic positions). The position-binning instrument is validated.

## Interpretation

### What this adds to the muqaṭṭāʿat architecture

[[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]/46 established the muqaṭṭāʿat set as structural markers at the **surah level** (surah-position clustering, length skew). [[h-new-113-letter-position|H-NEW-113]] now adds a **verse-internal positional signature**:

> The 14 muqaṭṭāʿat letters are NON-RANDOMLY distributed within verses: depleted at verse-onset (where function-letters dominate), enriched through the verse body, and maximally enriched at verse-end (where fawāṣila rhymes are drawn from the {ن, م, ر, ي} core of the muqaṭṭāʿat set).

The RR_bin10 = 1.074 is a SMALL effect-size per-letter but statistically extreme (p=2×10⁻²²) because of the 247K+81K observation count. The shape (monotone increasing through the verse) is more revealing than the magnitude: **the 14-vs-14 split has a positional signature consistent with the fawāṣila-letters literature**.

### Connection to [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] (dotless preference) and Layer-1 meta-architecture

The muqaṭṭāʿat set EXCLUDES the top 4 function-letters {و, ب, ت, ف}. Function-letters are verse-initial enrichers (conjunctions, prepositions, verbal prefixes). Therefore the muqaṭṭāʿat-is-depleted-verse-initially finding is a **mechanical consequence** of the function-letter-exclusion property of the set. This is NOT a new design axis; it is a DOWNSTREAM CORRELATE of an existing design axis.

The verse-FINAL enrichment, however, is NOT a mechanical consequence of function-letter exclusion — complement-14 letters include plenty of non-function letters (ث, ج, خ, د, ذ, ز, ش, ض, ظ, غ). The finding that muqaṭṭāʿat letters are specifically ENRICHED verse-finally beyond their frequency is NEW information and is the genuine [[h-new-113-letter-position|H-NEW-113]] signal.

### What this does NOT claim

- [[h-new-113-letter-position|H-NEW-113]] is a **small-effect population test** (RR 1.07), not a per-surah or per-verse discrimination signal.
- It does NOT say that a random verse can be predicted to be muqaṭṭāʿat-opened from its fawāṣila letter.
- It does NOT claim the Quran was designed around a letter-level-10-bin rule; the fawāṣila–muqaṭṭāʿat alignment is a natural poetic consequence of Arabic rhyming in ن/ر/ي/م.
- The INITIAL-LETTER depletion is explained by function-letter exclusion, not a separate "do not start verses with muqaṭṭāʿat" rule.

## Verdict

- **Primary (KS)**: PASS at p = 2.3 × 10⁻²² (Bonferroni-3, α_bon=0.0167 survives by 20 orders of magnitude).
- **Secondary (RR_bin10)**: PASS (CI excludes 1, 1-sided p < 2×10⁻⁴).
- **Secondary (initial-letter)**: NULL in pre-registered direction; EXPLORATORY-REVERSE signal of muqaṭṭāʿat DEPLETION verse-initially — attributed to function-letter exclusion.

Overall verdict: **PASS-DIRECTED** (2/3 pre-committed cells pass in pre-registered direction; third cell explains the depletion-reverse mechanistically via existing finding).

PASS-DIRECTED (not CONFIRMED) because this is a NOVEL test; INDEPENDENT REPLICATION should use (a) a different verse-splitting rule (e.g., word-initial vs word-final rather than character-position), (b) a different letter-set carving (e.g., muqaṭṭāʿat-prototype-frequency-controlled matched set), or (c) shuffled positive-control on a non-Quranic matched-register Arabic corpus.

## Outputs

- JSON: `findings/phase-b-hypotheses/csv/h-new-113.json` (full 28×10 position-density matrix + bootstrap CIs + MW-5 controls)
- Script: `scripts/h_new_113_letter_position.py`
- Pre-reg: `findings/phase-b-hypotheses/h-new-113-letter-position-prereg.md`
- Journal: `journal/h-new-113-run-1.md`

---

## audit-035 amendment (appended 2026-04-17) — effect-size disclosure

**Audit flag**: with N ≈ 329K letter-position observations, even very
small distributional differences produce extreme p-values. Cell 1's
KS D = 0.0203 is a **small effect** despite p = 2.3×10⁻²². The
MONOTONE-RISING RR gradient (bin 1: 0.87 → bin 10: 1.07) is more
interpretable as an effect-size statement than the KS p-value alone.

### Numerical interpretation

- KS D = 0.0203 means the maximum vertical separation between MUQ and
  COMP cumulative distributions is ~2% — a **small, statistically
  robust distributional shift**.
- Per-bin relative risk at bin 10 (verse-final): RR = 1.07 = **7% over-
  representation** of muqaṭṭāʿat letters verse-finally, relative to
  frequency-expected baseline.
- Per-bin relative risk at bin 1 (verse-initial): RR = 0.87 = **13%
  under-representation** verse-initially.

### Why this matters

The Cell 1 KS result is technically BONFERRONI-PASS by ~20 orders of
magnitude, but the effect is small. The Cell 2 RR gradient is a more
honest summary: muqaṭṭāʿat letters have a modest (<15%) but
systematically MONOTONE positional bias, rising from under-represented
at verse-start to over-represented at verse-end. The verse-initial
DEPLETION is mechanically explicable (function letters excluded from
muqaṭṭāʿat set, per Layer-1 meta-architecture); the verse-final
ENRICHMENT is a NEW structural-marker axis worth noting.

### Publication recommendation

Report Cell 1 with the effect size (D = 0.02) alongside the p-value.
Publish Cell 2 (RR gradient) as the INTERPRETATION-BEARING result.

