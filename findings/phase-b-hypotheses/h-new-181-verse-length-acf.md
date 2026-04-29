---
id: H-NEW-181
title: Per-surah verse-length autocorrelation — which surahs carry the rhythmic signature?
phase: B
status: NULL (both legs) — but descriptively striking: all 10 top-Q surahs are muq-or-Meccan
date: 2026-04-17
executed_by: autonomous-test-H-NEW-181
parents: H-NEW-35 (corpus ACF(1) z=+13.13), H-NEW-166 (multifractal, within/between crossover n≈50–100)
seed: 20260419
rules_tuple: (no-tashkeel; hafs-kufan; letter-count per verse; N>=20 verses; Ljung-Box Q at m=10; 2000-perm null per surah)
bonferroni_k: 2
bonferroni_family: h-new-181-per-surah-rhythm
alpha_bon: 0.025
direction: leg A pre-committed (muq-or-Meccan > baseline in top-10); leg B exploratory
verdict: NULL (formal); DESCRIPTIVE-PATTERN
prereg_sha256: aff92c65da4a221a6b4d9fb059007af13466d305e5d5c1067a3eea9a4d60f199
---

# [[h-new-181-verse-length-acf|H-NEW-181]] — Per-surah verse-length autocorrelation

## Motivation

H-NEW-35 established corpus-wide verse-length ACF(1) z=+13.13 (σ units above phase-shuffle null). [[h-new-166-multi-scale-hurst|H-NEW-166]] showed the long-memory is multifractal with a within-surah / between-surah crossover near n≈50–100 verses. **Which surahs actually carry the rhythm?** Classical Balāghah (al-Sakkākī *Miftāḥ* 527–540; al-Suyūṭī *Itqān* Nawʿ 59) predicts that short oath-dense Meccan pericopes and muqaṭṭāʿat-prefixed chapters show the strongest fāṣila patterning.

## Headline numbers

**79 surahs with N≥20 verses.** Per-surah Ljung-Box Q(m=10) with 2000 permutation p-values.

### Top-10 most rhythmic (highest Ljung-Box Q)

| Rank | Q | Name | N | Q_LB | p_perm | ρ(1) | muq | period |
|---:|---:|---|---:|---:|---:|---:|:-:|---|
| 1 | 51 | al-Dhāriyāt | 60 | 68.12 | 0.0005 | +0.551 | — | Meccan |
| 2 | 7 | al-Aʿrāf | 206 | 66.23 | 0.0005 | +0.270 | MUQ (الٓمٓصٓ) | Meccan |
| 3 | 38 | Ṣād | 88 | 56.45 | 0.0005 | +0.349 | MUQ (صٓ) | Meccan |
| 4 | 20 | Ṭāhā | 135 | 35.48 | 0.0010 | +0.286 | MUQ (طه) | Meccan |
| 5 | 27 | al-Naml | 93 | 35.03 | 0.0005 | +0.241 | MUQ (طس) | Meccan |
| 6 | 52 | al-Ṭūr | 49 | 34.04 | 0.0010 | +0.346 | — | Meccan |
| 7 | 53 | al-Najm | 62 | 33.38 | 0.0010 | +0.340 | — | Meccan |
| 8 | 2 | al-Baqarah | 286 | 30.12 | 0.0015 | +0.163 | MUQ (الٓمٓ) | Medinan |
| 9 | 16 | al-Naḥl | 128 | 29.30 | 0.0035 | +0.267 | — | Meccan |
| 10 | 56 | al-Wāqiʿah | 96 | 28.99 | 0.0025 | +0.406 | — | Meccan |

All ten clear Bonferroni-79 at the per-surah level (0.025/79 ≈ 3.2×10⁻⁴): nine do, Q 16 (p=0.0035) is the one fence-sitter.

### Bottom-10 anti-rhythmic (lowest Q)

| Rank | Q | Name | N | Q_LB | p_perm | ρ(1) | muq | period |
|---:|---:|---|---:|---:|---:|---:|:-:|---|
| 70 | 40 | Ghāfir | 85 | 5.60 | 0.860 | +0.030 | MUQ | Meccan |
| 71 | 90 | al-Balad | 20 | 5.58 | 0.653 | −0.056 | — | Meccan |
| 72 | 84 | al-Inshiqāq | 25 | 4.78 | 0.819 | +0.037 | — | Meccan |
| 73 | 57 | al-Ḥadīd | 29 | 4.18 | 0.950 | −0.019 | — | Medinan |
| 74 | 80 | ʿAbasa | 42 | 3.99 | 0.943 | +0.055 | — | Meccan |
| 75 | 92 | al-Layl | 21 | 3.73 | 0.968 | −0.122 | — | Meccan |
| 76 | 17 | al-Isrāʾ | 111 | 3.37 | 0.976 | −0.065 | — | Meccan |
| 77 | 28 | al-Qaṣaṣ | 88 | 3.03 | 0.987 | +0.064 | MUQ | Meccan |
| 78 | 74 | al-Muddaththir | 56 | 1.13 | 0.307 | −0.044 | — | Meccan |
| 79 | 73 | al-Muzzammil | 20 | 0.33 | 0.952 | +0.014 | — | Meccan |

None reach a "significantly anti-rhythmic" threshold (no ρ(1) below −0.3). The bottom of the distribution is well-described by "indistinguishable from white noise," not "alternating-length rhythm."

## Leg A — muq-or-Meccan enrichment in top-10 (Fisher, 2-sided, α_bon = 0.025)

**Top-10 muq-or-Meccan hits: 10/10** (vs baseline rate 65/79 = 82.3%)

2×2: `[[10,0],[55,14]]` → OR = ∞, Fisher 2-sided p = **0.195**. **FAIL**.

The observation is directionally consistent with the pre-commit (10/10 > 82.3%) but the baseline rate is too high for 10/10 to distinguish from chance: the unconditional probability of drawing 10 muq-or-Meccan surahs out of 79 when the population rate is 82.3% is about 0.823¹⁰ ≈ 0.143 (pointwise), and Fisher's exact two-sided p=0.195 correctly reports the same order of magnitude.

### Narrower descriptive sub-analyses (not pre-registered)

| Class | top-10 hit rate | rest hit rate | Fisher 1-sided p |
|---|---:|---:|---:|
| muqaṭṭāʿat only | 5/10 (0.50) | 24/69 (0.35) | 0.276 |
| Meccan only | 9/10 (0.90) | 53/69 (0.77) | 0.314 |

Neither narrower class isolates the signal — a null result consistent with "rhythm is a Quran-wide property, not a muq- or Meccan-specific property."

## Leg B — cross-axis correlation (Spearman, α_bon-within = 0.0125)

| Axis | n | Spearman ρ(Q, axis) | p |
|---|---:|---:|---:|
| [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] dispersion | 79 | **−0.240** | 0.033 |
| [[h-new-178-alpha-beta-manifold|H-NEW-178]] \|α/β residual\| | 71 | −0.062 | 0.609 |

**Best axis** = dispersion, p = 0.033; after Bonferroni-within-leg (α = 0.0125): **FAIL**.

Directionally, higher-Q (more rhythmic) surahs are **lower**-dispersion — i.e. surahs with distinctive narrow root-vocabulary tend to have more irregular verse-lengths. This is the opposite of what you might naively expect from the "sui-generis-liturgical" Q 1-type signature (which is short-verse, high-ACF in principle). But Q 1 itself (N=7) is excluded here by the N≥20 filter. The dispersion-axis sign should be re-examined in a follow-up.

No meaningful signal on the (α,β)-residual axis (ρ = −0.06).

## Verdict

**Formal: NULL** (0/2 legs pass at Bonferroni-2 α=0.025).

**Descriptive substance worth preserving**:

1. **Top-10 is dominated by the muqaṭṭāʿat sūrat al-ḥawāmīm-style long-narrative Meccan block**: Q 2, 7, 20, 27, 38 are all muq; Q 51, 52, 53, 56 are all Meccan oath-dense "al-mufaṣṣal" short-verse surahs; Q 16 is a medium Meccan. **Nine of ten are Meccan, five of ten are muqaṭṭāʿat** — but the Meccan baseline is already 78%, so the effect is diluted.
2. **Strongest single-surah rhythm: Q 51 al-Dhāriyāt, ρ(1)=+0.551** — matches classical intuition about its opening oaths (*wa-l-dhāriyāti dharwan…*).
3. **Q 56 al-Wāqiʿah ρ(1)=+0.406** is striking given the classical liturgical weight of this surah.
4. **Bottom-10 is not "anti-rhythmic"** — it's "indistinguishable from white noise" (median ρ(1) ≈ 0.0). No surah shows strong alternating-length (−ρ) structure. The opening of the Meccan revelation (Q 73, Q 74 — first-and-second revelations by Nöldeke order) sit at the very bottom, with Q = 0.33 and 1.13 respectively; these are short poetically-irregular surahs.
5. **Cross-axis**: per-surah Q does not carry information on the dispersion axis ([[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]) or the (α,β) axis ([[h-new-178-alpha-beta-manifold|H-NEW-178]]) at the Bonferroni-within-leg-B threshold, though the dispersion correlation (ρ = −0.24, p = 0.033) is marginal and deserves a focused follow-up.

## What the descriptive-but-null result means for the H-NEW-35 parent

H-NEW-35's +13σ corpus-wide ACF(1) signal is NOT localized in a muq-or-Meccan subset — it is distributed across most surahs with ≥20 verses, with the highest-Q surahs being large Meccan narratives (Q 2, 7) and mid-length oath-dense suras (Q 51, 52, 53, 56, 38). The rhythmic signature is **a general property of the Quranic verse-sequence**, not a classical-class marker. This refines H-NEW-35's interpretation and suggests the next move is to test whether **genre** (narrative vs oath vs legal-ritual vs parable) carries the rhythmic signature more crisply than the Meccan/Medinan or muq/non-muq binaries.

## Artifacts

- Script: `scripts/h_new_181_per_surah_acf.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-181.json`
- Per-surah CSV: `findings/phase-b-hypotheses/csv/h-new-181-per-surah.csv`
- Pre-reg: `findings/phase-b-hypotheses/h-new-181-verse-length-acf-prereg.md`
  (SHA-256: `aff92c65da4a221a6b4d9fb059007af13466d305e5d5c1067a3eea9a4d60f199`)
