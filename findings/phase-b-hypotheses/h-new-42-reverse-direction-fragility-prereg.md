---
id: H-NEW-42
title: Reverse-Direction Structural Fragility — does surah structure degrade MORE under verse-order reversal than matched-Arabic prose?
status: PRE-REGISTERED (not yet executed)
registered: 2026-04-15
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k: 3
alpha_bon: 0.0167
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
baselines:
  - data/baseline-corpora/raw/bukhari-noquran.txt
  - data/baseline-corpora/raw/jahiz-hayawan.txt
  - muallaqat_pool: constructed at execution by concatenating data/baseline-corpora/raw/muallaqa-{imru-al-qais,tarafa,zuhayr,labid,amr-bin-kulthum,antara,harith}.txt in that canonical order; SHA-256 of the resulting pool logged in the findings JSON
---

# [[h-new-42-reverse-direction-fragility|H-NEW-42]] — Reverse-Direction Structural Fragility

## Question

Asymmetric-time sacred text hypothesis. If a text was composed under real multi-constraint optimization (rhyme, chiasm, progressive argument, eschatological narrative arc), its **forward-ordered** structural fingerprint should be far more coherent than its **reverse-ordered** fingerprint — AND this Δ (forward-minus-reverse coherence) should exceed the Δ of matched Arabic prose (which is ordered but not multi-constraint-optimized).

This test distinguishes "ordered text" (prose) from "densely-optimized text" (hypothesized Quran property): both will lose coherence when reversed, but the dense-optimization text should lose MORE.

## Procedure

1. **Fingerprint vector per surah.** For each surah S, compute fingerprint F(S) = (f₁, …, f₆):
   - f₁ = rhyme-class coherence (fraction of verse-final rhyme-class transitions that are repeats or within-class)
   - f₂ = semantic embedding drift (cosine-similarity sum of adjacent verse-embeddings using a fixed Arabic encoder; fixed model: `aubmindlab/bert-base-arabertv02` or equivalent — embedding model LOCKED before execution)
   - f₃ = divine-name trajectory entropy (H of the divine-name-occurrence time series)
   - f₄ = verse-length first-difference smoothness (1 – normalized total variation)
   - f₅ = root-repetition density (fraction of roots reused in ≤ k=3 verse window)
   - f₆ = n-gram (letter trigram) transition entropy under within-surah Markov
2. **Reverse operation.** Reverse verse order of surah S to get S'. Recompute F(S').
3. **Fragility score** Δ(S) = ||F(S) – F(S')||₁ / (|F(S)| × n_verses(S)^0.5), length-normalized.
4. **Pooled statistic** Δ̄_Quran = mean Δ(S) over all 114 surahs. Also median.
5. **Baseline.** Partition each baseline corpus into 114 pseudo-surahs matched to Quran surah-length distribution (quantile-matched by letter count). Compute Δ̄_baseline same way.
6. **Null model.** 1,000 baseline repartitions. Empirical p = fraction of null Δ̄_baseline ≥ Δ̄_Quran. **One-sided (pre-reg prediction: Quran more fragile).**
7. **MW-5 POSITIVE CONTROL.** Use Muʿallaqāt (rhymed poetry, known to be ordered by rhyme constraint) as a second positive-control. Muʿallaqāt should show fragility > Jāḥiẓ prose. If Muʿallaqāt ≤ prose, null is broken.
8. **MW-1 LENGTH CONFOUND.** Baselines are length-matched by construction (step 5).

## Three-baseline joint-threshold

Quran must beat ALL THREE baselines (Bukhārī, Jāḥiẓ, Muʿallaqāt) at one-sided α_cell = 0.0167 / 3 = 5.56 × 10⁻³. If Muʿallaqāt is the closest competitor (most-constrained baseline), it is the decisive discriminant; passing vs Muʿallaqāt means "beyond the best-known rhymed-text constraint." **All three baselines REQUIRED. Hard abort (not fallback) on any preprocessing failure; re-file with corrected preprocessing. No two-baseline fallback at any α. No α adjustment.** (Per amendment 42-A, audit-032.)

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| Quran Δ̄ > all three baselines at α_cell | STRONG-PASS — dense-optimization signature confirmed vs prose AND poetry |
| Quran > Bukhārī and Jāḥiẓ but ≤ Muʿallaqāt | PASS-VS-PROSE — constrained like poetry, not beyond |
| Quran ≤ Bukhārī or Jāḥiẓ | NULL — Quran fragility indistinguishable from or less than prose |
| Positive-control Muʿallaqāt ≤ Jāḥiẓ | NULL-BROKEN |

## Direction pre-registration (PRE-REG-STANDARD-01 compliance)

Predicted direction: **Δ̄_Quran > Δ̄_baseline** (Quran MORE fragile to reversal). Opposite-direction result (Quran less fragile) would be recorded as EXPLORATORY-REVERSE but not elevated without an independent follow-up pre-reg.

## Mechanism interpretation

- STRONG-PASS → evidence for directional-optimization (forward-specific structure, including chiasmus with one-way narrative arc, argument progression, eschat-culmination pattern)
- PASS-VS-PROSE → evidence for poetic-constraint equivalence but no super-poetic structure
- NULL → the forward-specific-optimization hypothesis fails; Quran behaves like "ordered prose" under this probe

## Garden-of-forking-paths log

- 6 fingerprint axes chosen because each measures a DIFFERENT order-sensitive property (rhyme, semantic, divine, length, lexical, statistical)
- Addition of f₇ is prohibited post-hoc
- Embedding model locked before run; alternative embeddings are separate follow-up pre-regs
- "Pseudo-surah" construction by quantile-matched letter count; other matching schemes (by word count, by verse count) are separate follow-up tests
- Verse-reversal ONLY (not word-reversal within verse); word-reversal test is a future H-NEW-42.1

## Integrity commitment

Publish PASS, PASS-VS-PROSE, NULL, NULL-BROKEN with equal prominence.

---

## AMENDMENTS (post-audit-032, 2026-04-15, pre-execution, tightening-only)

**Amendment 42-A (delete Muʿallaqāt fallback; hard abort required).** The previous clause "If Muʿallaqāt unavailable, we fall back to two baselines at α_cell = 0.0083" is DELETED as a BLOCK-class defect per audit-032. Applied inline above. All three baselines required; hard abort on any baseline processing failure; no α loosening permitted. This reincarnates the audit-023 fallback-clause abuse pattern and is prohibited.

**Amendment 42-B (baseline paths corrected).** Header `baselines:` paths updated to actual filesystem paths: `data/baseline-corpora/raw/bukhari-noquran.txt`, `data/baseline-corpora/raw/jahiz-hayawan.txt`, and Muʿallaqāt-pool constructed from 7 individual `muallaqa-*.txt` files. Script must log SHA-256 of the constructed Muʿallaqāt-pool in the findings JSON for integrity.

**Amendment 42-C (embedding model commit hash).** If `aubmindlab/bert-base-arabertv02` is used for f₂, pin the exact HuggingFace model commit-hash in the script header. Any "or equivalent" substitute must be disclosed as garden-of-forking-paths entry BEFORE any result is viewed.

All amendments tighten or clarify; none loosen.

---

## GARDEN-OF-FORKING-PATHS ENTRY — f₂ substitute (2026-04-15, pre-result-viewing, specialist [[h-new-42-reverse-direction-fragility|h-new-42]])

Declared BEFORE any numeric result was viewed (background script killed at amendment-032 landing before completion; output file contents not read). No local Arabic embedding model is available on this machine (no `aubmindlab/bert-base-arabertv02` weights, no HuggingFace cache, no cached equivalent). Network downloads not attempted from this specialist. Per amendment 42-C, this requires a GoFP entry before results are viewed.

**Substitution.** f₂ replaced with a rule-based proxy: mean char-trigram Jaccard similarity of adjacent verses (letters-only after no-tashkeel normalization, alef-variants → plain alef). Specifically: for each adjacent verse pair (v_i, v_{i+1}), concatenate tokens to letter stream, form trigram set, Jaccard = |T_i ∩ T_{i+1}| / |T_i ∪ T_{i+1}|; f₂(S) = mean over adjacent pairs.

**Why this weakens but does not invalidate.** Char-trigram Jaccard captures surface-lexical continuity, not deep semantics. It is still order-sensitive (adjacency shifts when verses are reversed), so reversal perturbs it. It under-captures semantic drift where adjacent verses share meaning via different roots — biasing f₂ toward LOW fragility deltas, which is conservative vs the pre-reg's prediction (Quran MORE fragile). Under-powered but unbiased toward the null.

**Other 5 axes (f₁, f₃, f₄, f₅, f₆) are as pre-registered.** No other axis is modified.

**Follow-up pre-reg required.** A separate pre-reg H-NEW-42.2 will re-run with true Arabic transformer embeddings once a model is available on-disk.

Logged: 2026-04-15 by [[h-new-42-reverse-direction-fragility|h-new-42]]-specialist, before first view of any numeric fragility output.
