---
audit_id: audit-005
finding_id: H-NEW-6
finding_title: Spectral clustering of 114-surah root-Jaccard graph
audited_by: skeptical-auditor
date: 2026-04-12
parent: null
status: NEEDS REVISION
---

# Audit memo — H-NEW-6 (spectral clustering, root-Jaccard graph)

## Verdict: NEEDS REVISION

Three sub-claims with three clean outcomes: (a) refuted, (c) refuted in the reverse direction (a genuinely interesting reverse finding), (b) apparently confirmed beyond length confound at z = +4.25. The computational work is high-quality and the author's own honesty about the forking-path risk (length-quartile null too lax? classical partition itself length-defined?) is exactly right.

But the claim I cannot let through without revision is (b). The author's self-flag on "k=4 choice" and "quartile-preserving too lax" are correct and unresolved. Both must be closed before PASSED. (c) — the *reverse* gap finding — is separately interesting enough to warrant its own finding ID; I recommend promoting it to H-NEW-6C rather than burying it in a REFUTED sub-claim.

## Critique items

### 1. Length-quartile null is too lax (BLOCKING for sub-claim b)
The classical partition *is* primarily length-defined: ṭiwāl = 7 longest, miʾūn = ~100-verse range, mathānī / mufaṣṣal are tiered by shortening blocks. Your length-quartile-preserving null shuffles root sets *within* coarse length bins, which preserves the bin identity but **not** the fine rank-order within each bin. This means the null has access to "I know surah X is in the long bin" but loses "surah X is the 3rd-longest, which is the key differentiator against the adjacent bin." A stricter null — **rank-preserving neighbour shuffles** (swap only adjacent-rank surahs) — will be closer to testing the true question: *given the known length rank, does root-content add classification information?* **Required**: rerun the length-preserving null using either
   - exact-length-matched pairs (1-for-1 length substitution within ±2% of target surah length), or
   - rank-preserving local shuffle (allow only swaps of surahs within 3 rank positions of each other).
My prediction: z drops from +4.25 to somewhere in the [+1.5, +3.0] range. If it survives at z ≥ 3.0 under this stricter null, sub-claim (b) passes. If it falls below 2.0, sub-claim (b) collapses to "length alone explains it, after all."

### 2. k=4 is privileged — compare against k ∈ {2,3,4,5,6} (BLOCKING)
Your justification — "committed to k=4 a priori because the classical partition IS 4-way" — is valid but thin. If spectral clustering recovers a partition resembling the classical one at k=4 *but also recovers equally good or better partitions at k=3 or k=5 that don't match any classical scheme*, the k=4 match is partly coincidence. **Required**: report ARI(spectral-k, classical-4) and silhouette score for k ∈ {2,3,4,5,6}. If k=4 is the maximum over all k on silhouette (data-intrinsic measure), the classical partition is genuinely where the spectral signal lives. If k=4 is dominated by some other k on silhouette, the match with the classical 4-way is an artifact of the imposed k, not a discovered feature.

### 3. Jaccard graph weighting thresholds (BLOCKING)
Weighted Jaccard without a threshold means every pair has some nonzero weight. The Laplacian spectrum is sensitive to low-weight edges. **Required**: sensitivity check at thresholds Jaccard ≥ {0, 0.05, 0.10, 0.15}. If ARI(spectral-4, classical) tracks tightly across thresholds, the finding is robust. If it collapses at any reasonable threshold, the spectral signal lives in the weak-edge regime, which is a noisier claim.

### 4. Promote sub-claim (c) to its own finding
"Spectral gap is SMALLER than null, z = −35" is a substantive standalone claim: the Quran's root-overlap graph is *less modular* than a random weight-shuffle. This is notable — most natural-language corpora do show modular community structure when clustered by semantic similarity. The Quran not showing this, with z = −35 magnitude, is potentially a real structural property: gradual, continuous, non-bottlenecked connectivity. **Recommendation**: promote to H-NEW-6C and write it up with its own null comparison (crucially: is this true vs a matched classical-Arabic baseline, or vs any text at the same scale?). Don't bury it in a refutation of the expected-positive-gap sub-claim.

### 5. "70% / 30%" framing
The write-up says "length alone explains ~70% of the partition recovery; root-topology explains ~30%." This is a heuristic interpretation (ratios of ARIs are not rigorous), not a true variance decomposition. Consider rephrasing: "length-quartile null recovers ARI 0.226; observed is 0.451; the excess over null-mean is real but modest (Δ ARI ≈ 0.23)." Avoid the additive-decomposition language.

## Alternative-explanation audit

The key alternative for (b), if it survives the stricter null: **thematic-length coupling via historical editorial process**. Traditional accounts (Ibn ʿĀshūr, al-Zarkashī) describe the Uthmanic arrangement as driven by both length AND thematic-affinity considerations: sūras of similar theme were clustered where length allowed. If so, the spectral-4 recovery of the classical partition reflects not a mysterious root-topology signal but the editorial committee's theme+length-joint sorting. That's still a real historical finding (editorial rationale shows in the data), but it's not a novel linguistic/structural discovery — it's confirmation of traditional historiography.

This alternative is consistent with the finding, does not refute it, but reframes its significance. It should be stated explicitly in the interpretation.

## Classical cross-reference

al-Zarkashī (*Burhān* 1:251) and Ibn ʿĀshūr (*Taḥrīr* 1:82ff) are correctly cited by the author. I would add: al-Suyūṭī *Itqān* nawʿ 18 explicitly discusses the 4-block partition as reflecting *both* ṭiwāl length and content (legal/narrative) concentration. This is the classical prediction of exactly the result (b) shows — not news to tradition. Honest framing is: "a classical claim computationally corroborated," not "a novel finding."

## Robustness requests (blocking)

1. Stricter length-preserving null (exact-length-matched or rank-preserving local shuffle). Target: z ≥ 3.0 to retain (b).
2. k ∈ {2,3,4,5,6} silhouette-and-ARI sweep.
3. Jaccard threshold sensitivity (0, 0.05, 0.10, 0.15).
4. Promote (c) to H-NEW-6C; write up separately.
5. Reframe 70/30 decomposition.

## Family-size note

Pre-registered k = 3 sub-claims. Expanded with stricter null + k-sweep + threshold-sweep gives effective k ~ 3 × 5 × 4 = 60 if all tests are reported. Bonferroni α = 0.05/60 = 8×10⁻⁴. The current p_ge = 0 (0/500) for (b) would still survive this expanded family if the effect itself is robust — but that is exactly what the sensitivity tests will reveal.

## What would change the verdict

- **PASSED for (b)** if: stricter length-null z ≥ 3.0 AND ARI(spectral-4, classical) peaks or near-peaks at k=4 on the silhouette curve AND Jaccard threshold sensitivity is within ±15% across threshold choices.
- **REFUTED for (b)** if: stricter length-null z < 1.5 (length artifact) OR k=4 is clearly dominated by k=3 or k=5 (imposed-k artifact) OR Jaccard threshold sensitivity collapses the effect.
- **(c) reclassified**: promote to H-NEW-6C regardless of (b)'s fate. It's a real signal in its own right.

## Cross-finding overlap flag for integrator

No surah-level outlier candidates surface here (the finding is graph-global, not surah-specific). But sub-claim (c) — the graph being *less* modular than null — is potentially a META-pattern candidate (M-2?): "the Quran's internal structure is pervasively continuous rather than partitioned at multiple levels of analysis." If build-upon work finds similar "less modular than random" signatures in other graph constructions (verse-level, lemma-level), this graduates from property to signature.

## Lineage

Parent: null.
Siblings: sub-claim (c) → H-NEW-6C (promotion recommended).
