---
id: H-NEW-41
title: Root Combinatorial Saturation — does the Quran sample the 28³ triliteral root space in a structured, non-random way?
status: PRE-REGISTERED (not yet executed)
registered: 2026-04-15
spec_locked_at: 2026-04-15 (before any numerical result viewed)
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k: 3
alpha_bon: 0.0167 (= 0.05 / 3)
rules_tuple: (no-tashkeel, orthographic-token & lemma where noted, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
morphology_source: data/morphology/quranic-corpus-morphology-0.4.txt (QAC v0.4)
---

# [[h-new-41-root-combinatorial-saturation|H-NEW-41]] — Root Combinatorial Saturation

## Question

The 28-letter Arabic alphabet admits 28³ = **21,952** ordered triliteral root permutations (ignoring quadriliterals and degenerate repeats). Classical lexicography (Hans Wehr, Lane, Ibn Sīda's *Muḥkam*) attests ~6,000–7,500 as genuine roots. QAC v0.4 extracts **~1,636 distinct Quranic roots**.

Sub-question A (coverage): What fraction of classical-Arabic attested roots does the Quran sample?

Sub-question B (STRUCTURE-IN-AVOIDANCE): Is the set of **roots the Quran omits** distinguishable from a uniform random subsample of the classical root set? Specifically, does the Quran systematically avoid or prefer phonotactic patterns (sonority hierarchy, place-of-articulation homogeneity, emphatic-letter density, sun/moon-letter mix) at rates above Bonferroni-corrected thresholds?

Sub-question C (ZERO-ATTESTATION ANTI-SIGNATURE): Of the 28³ – |Classical| = ~14,500 phonotactically plausible root slots that classical Arabic itself does not attest, does the Quran's absence-set preserve the same structural anti-signature (i.e., Quran avoids them for the same phonotactic reasons as the classical language), or does the Quran exhibit a DIFFERENT anti-signature?

## Procedure

1. **Root extraction.** Parse QAC v0.4; collect all unique `ROOT:` values. Normalize to 3-letter form (drop quadriliterals to separate set Q4). Expected N_Q ≈ 1,636.
2. **Classical reference set.** Use Lane's *Arabic-English Lexicon* root index (public domain) + Hans Wehr's modern root list as the union "classical-attested" set. Expected N_C ≈ 6,500–7,500.
3. **Phonotactic feature extraction per root.** For each 3-letter root `(c₁, c₂, c₃)`:
   - Place of articulation (POA) per letter: {labial, dental, alveolar, post-alveolar, palatal, velar, uvular, pharyngeal, laryngeal}
   - Emphatic flag: {ص, ض, ط, ظ, ق}
   - Sonority class: {stop, fricative, nasal, liquid, glide, vowel}
   - OCP-Place violations (same-POA consecutive letters) per Frisch/Pierrehumbert 2004
4. **Observed feature distributions** for three sets: Q (Quran roots), C (classical but non-Quran) = C \ Q, U = 28³ \ C (never-attested).
5. **Null model (PRIMARY).** Draw 10,000 size-|Q| uniform random subsets S ⊂ C. Compute each phonotactic-feature statistic distribution under null. Compare observed Q vs null quantiles. **Two-sided test, one per feature.**
6. **Test family (inner).** 12 phonotactic statistics (4 POA-pair frequencies × 3 root-position pairs = 12 cells). Inner Bonferroni = 12 → α_inner = 0.0167 / 12 = 1.39 × 10⁻³. **Total family-wise α_per_cell = 1.39 × 10⁻³.**
7. **MW-5 POSITIVE CONTROL.** Apply the identical pipeline to a pre-registered Arabic positive-control corpus (*Diwān of al-Mutanabbī*, already on disk). The positive-control corpus must yield a phonotactic signature *similar to classical Arabic average* (z < +2 / z > –2 on all 12 cells). If the positive-control fails (shows anomalous phonotactic signature), the null model is broken and no Quran result is interpretable.
8. **MW-1 CONFOUND.** Frequency-weight correction: roots used more often in the Quran have more attestations → double-count risk. Primary test uses **type-level** (one vote per root). Secondary robustness: token-weighted (each root weighted by Quran frequency).

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| 0 of 12 cells significant at α = 1.39×10⁻³ | NULL — Quran's root sampling is phonotactically indistinguishable from random subsample of classical Arabic |
| 1 cell significant | EXPLORATORY-hit (not confirmed; report but do not promote) |
| 2–5 cells significant AND positive-control clean | PARTIAL-PASS — Quran's phonotactic selectivity beyond random, details specified |
| ≥6 cells significant AND positive-control clean | STRONG-PASS — structured avoidance confirmed |
| Positive-control anomalous | NULL-BROKEN — no Quran claim |

## Novelty / prior art

No published study operationalizes Quranic root-selection as a combinatorial-space-coverage problem with a rigorous null. Closest precedents:
- Frisch, Pierrehumbert, Broe (2004) "Similarity Avoidance and the OCP" — classical Arabic only, no Quran subset
- Bohas & Dat (2007) *Une théorie des matrices et étymons* — theoretical, no statistical null
- al-Khalil b. Aḥmad (*Kitāb al-ʿAyn*) — enumerates the root-space by letter-rank but pre-statistical

## Mechanism interpretation

- If STRONG-PASS with Quran MORE phonotactically structured than classical average → Quran exerts selection pressure beyond classical norm
- If STRONG-PASS with Quran LESS structured (more phonotactic outliers) → Quran draws from a phonotactically broader register (pre-classical? dialectal? mnemonic-constrained?)
- Either direction is publishable and theologically readable.

## Garden-of-forking-paths log

- Decision to use type-level primary with token-weighted secondary: locked here, pre-data.
- Decision to use al-Mutanabbī as positive-control: chosen because it's the densest attested-classical corpus in our baseline pool and is NOT Jāhiliyya (controls for pre-Islamic dialect bias).
- Choice of 12-cell inner family: 4 POA-pair types × 3 positions; locked here. Expansions to 24 or 36 cells are post-hoc and prohibited.
- ROOT normalization: quadriliterals split off into Q4 (separate test, not part of this pre-reg). Biliterals (rare) dropped.

## Integrity commitment

Publish PASS and NULL with equal prominence. Provide the classical root list, the feature table, the null quantiles, and the positive-control output JSON alongside the findings file.

---

## AMENDMENTS (post-audit-032, 2026-04-15, pre-execution, tightening-only)

**Amendment 41-A (MW-5 positive-control threshold precision).** §Procedure step 7 is replaced verbatim with: "Apply the identical pipeline to the Mutanabbī-Dīwān corpus. Compute the 12 phonotactic-cell z-scores using the classical reference set C with Mutanabbī's attested roots held out (leave-one-corpus-out). PASS criterion: for all 12 cells, |z_Mutanabbī| < 2.0. FAIL criterion (NULL-BROKEN): any cell with |z_Mutanabbī| ≥ 2.0. Any intermediate cell count (1–11) is reported as PARTIAL-POSITIVE-CONTROL and the Quran claim is downgraded to EXPLORATORY."

**Amendment 41-B (classical reference set SHA-256 lock).** Before execution, pin in the script header: (a) exact digital edition of Lane (file path + SHA-256), (b) exact Wehr edition (file path + SHA-256). Expansion/contraction of the classical reference set post-lock is prohibited. If neither Lane nor Wehr is available on disk, document the fallback set (QAC ∪ Mutanabbī-roots-only) and its SHA-256 before execution.

Both amendments tighten, not loosen — self-verifying per 2026-04-14 Bonferroni-asymmetry standard.
