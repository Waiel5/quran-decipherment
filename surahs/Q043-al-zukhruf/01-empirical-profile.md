---
surah: 43
surah_name: al-Zukhruf
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: HM-B opener; near-monorhyme; UAS=33; sig_A negative
---

# Q 43 al-Zukhruf — empirical profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline metrics

| Metric | Value | Provenance |
|:--|:--|:--|
| UAS score | +0.537 | h-new-840 |
| UAS rank | 33 / 114 | h-new-840 |
| |outlier| | 1.49 (mild) | h-new-840 |
| max neighbor TSP cost | **0.2357** (HM-7 max — at Q 42-Q 43 transition) | h-new-840 |
| |iʿjāz signature| | 1.102 | h-new-840 |
| sig_A (signed) | **−1.10** (anti-iʿjāz fawāṣil) | brief |
| Outlier Δ (signed) | +1.49 (mild outlier) | brief |
| Rhyme entropy | **0.594 bits — HM-7 minimum** | computed |
| Top rāwī | ن (78/89, **88%**) | computed |
| Distinct rhyme letters | 3 | computed |

## 2. Why "near-monorhyme"?

Q 43's rhyme structure is dominated by ن at 88% — only 11/89 verses have non-ن rāwī (10 with م, 1 with ل). The 2-char endings:

| Suffix | Count | Fraction |
|:--|:-:|:-:|
| -ūn | 52 | 58.4% |
| -īn | 26 | 29.2% |
| -īm | 9 | 10.1% |
| others | 2 | 2.3% |

Together -ūn + -īn = 87.6% of all verse-endings. The surah is functionally a -ūn/-īn drone with occasional -īm break. This is **the most prosodically uniform structure in HM-7**.

## 3. The Q 42 → Q 43 bifurcation transition (this session)

| | Q 42 al-Shūrā | Q 43 al-Zukhruf | Δ |
|:--|:-:|:-:|:-:|
| Rhyme entropy | 2.565 | 0.594 | −1.97 bits |
| Distinct finals | 9 | 3 | −6 |
| Top rāwī | ر (38%) | ن (88%) | category-switch |
| sig_A | +1.27 | −1.10 | −2.37 |
| max TSP cost | 0.2357 | 0.2357 | 0 (shared, this is *the* costly transition) |

The transition is the steepest one-step bifurcation in HM-7. The shared 0.2357 max-TSP-cost between Q 42 and Q 43 reflects the fact that the **same edge** (Q 42-Q 43) is the costly one — it's the cluster's internal-gap.

## 4. Within-HM-B cohesion

Per HMM-F-02 this session:
- HM-B {Q 43, 44, 45, 46}: d̄_FR = 0.8665 at 24.29%ile (moderate-cohesive)

Q 43's content is consistent with HM-B: post-bifurcation eschatological-discursive register, less narrative-dramatic than HM-A.

## 5. iʿjāz signature

- sig_A = **−1.10** (anti-iʿjāz fawāṣil — verse-end rhetorical density BELOW corpus mean)
- |iʿjāz| = 1.102

The negative sig_A is consistent with the near-monorhyme structure: the same rhyme repeated for 88% of verses produces a *less-rhetorically-varied fawāṣil* signal. Q 43 sits on the **anti-iʿjāz side** of the al-Bāqillānī axis.

This does NOT mean Q 43 is poor or unclassically appreciated — it means its rhetorical structure favors a different axis. Q 43's content density (the ʿĪsā passage, Q 43:31 socio-economic objection, Q 43:33-35 wealth-critique) is high; its **prosodic** density is low. They are anti-correlated per [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] (r = −0.86 at window-level).

## 6. Compression-tail position (s=43, intra-50)

Q 43 lies in the *intra-50* region. d̄_content baseline ≈ 0.96; d̄_rhyme baseline ≈ 0.36. Q 43's actual rhyme dispersion will be BELOW the s=43 baseline (near-monorhyme is opposite of dispersion). Q 43 is therefore a **rhyme-CONCENTRATION outlier** within intra-50 phase — the inverse of Q 42's pattern.

## 7. Adjacency

max neighbor TSP cost = 0.2357. Specifically the Q 42-Q 43 transition.

This is **the costliest single transition in HM-7**. Per [[h-new-720-canonical-adjacency-cost|H-NEW-720]] cost decomposition, Q 42-Q 43 ≈ 0.24 sits in the upper-third of canonical adjacency-cost transitions corpus-wide (top-3 in the corpus are Q 1-Q 2 ≈ 7.4%, Q 32-Q 33 ≈ 4.4%, Q 33-Q 34 ≈ 4.0%; Q 42-Q 43 ≈ 2.74% of total path-cost is also notable).

The empirical signal is consistent with the bifurcation: at the FR-content level, Q 42 and Q 43 are measurably distinct neighbors — content-wise distinct enough to register as adjacency-cost spikes.

## 8. Architectural classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | **negative** (sig_A=−1.10; anti-iʿjāz fawāṣil) |
| Theological-iʿjāz (al-Khaṭṭābī) | not specifically anchored in *thuluth* tradition |
| Compression-tail | NOT a tail surah (s=43 ≤ 50) |
| Outlier | mild outlier (Δ=+1.49) |
| Cluster role | **HM-B opener; bifurcation step partner** |

## 9. Honest limits

1. Q 43's UAS rank (33) is driven by max-TSP-cost not by iʿjāz signature; the architectural significance is "placement-difficulty", not "rhetorical-density".
2. The 88% ن-monorhyme pattern is structural; it's NOT necessarily the result of a *deliberate* monorhyme choice — it could reflect content-driven verse-ending requirements.
3. Negative sig_A (−1.10) co-varies with near-monorhyme; the two are likely the same effect from different angles.

## 10. Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[Q042-al-shura/01-empirical-profile|Q 42]] — preceding (bifurcation step partner)
- [[Q044-al-dukhan/01-empirical-profile|Q 44]] — following HM-B neighbor
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 42-Q 43 cost spike
- [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] — anti-twin lock context
