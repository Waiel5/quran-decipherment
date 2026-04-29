---
journal_entry: h-new-42-run-1
date: 2026-04-15
agent: h-new-42-specialist (integrator-completed)
pre_reg: findings/phase-b-hypotheses/h-new-42-reverse-direction-fragility-prereg.md
amendments_applied: 42-A, 42-B, 42-C
---

# Journal — H-NEW-42 run 1

## Task

Execute pre-registered reverse-direction structural fragility test. Compute 6-axis fingerprint per surah in forward vs reverse verse order, compare Δ̄ against three length-matched baselines (Bukhārī-noquran, Jāḥiẓ Ḥayawān, Muʿallaqāt pool of 7 canonical odes).

## Pipeline

1. Loaded quran-no-tashkeel.json (SHA-256 `253f72f3…5918a`).
2. Constructed Muʿallaqāt-pool from 7 individual files in canonical order (Imruʾ al-Qais, Ṭarafa, Zuhayr, Labīd, ʿAmr b. Kulthūm, ʿAntara, al-Ḥārith). Pool SHA-256 = `d97ce767…7e0300`.
3. Loaded Bukhārī-noquran (SHA-256 `0169b60d…c44a100`) and Jāḥiẓ-Ḥayawān (SHA-256 `4190954…bff0cd`).
4. Computed 6-axis fingerprint F(S) per surah: rhyme coherence (f₁), char-trigram Jaccard proxy (f₂, per amendment 42-C GoFP substitution), divine-name trajectory entropy (f₃), verse-length smoothness (f₄), root-repetition density (f₅), letter-trigram entropy (f₆).
5. Reversed verse order per surah; recomputed F(S').
6. Δ(S) = ||F(S) − F(S')||₁ / (|F(S)| × √n_verses(S)).
7. Repeated pipeline for each baseline with 1,000 null repartitions into 114 Quran-length-matched pseudo-surahs.
8. Computed positive-control: direct Muʿallaqāt fragility (7 poems, no partitioning) vs Jāḥiẓ partitioned; also Muʿallaqāt partitioned vs Jāḥiẓ partitioned.
9. Synthetic positive-control: Quran forward vs within-surah-verse-shuffled Quran.

## f₂ embedding-model amendment (GoFP)

Per amendment 42-C: no local Arabic transformer model available. f₂ substituted with char-trigram Jaccard Jaccard (letters-only, no-tashkeel normalized, alef-variants → plain alef, trigram set per verse, Jaccard between adjacent verses, mean over adjacent pairs). Logged BEFORE any numeric result viewed. Weakens f₂ but preserves 6-axis structure. Biases toward under-detection of semantic drift (conservative vs the pre-registered direction).

## Results (summary)

Verdict per strict MW-5 gate: **NULL-BROKEN** (direct-Muʿallaqāt positive-control FAIL).

Signed observation (under disqualified null): Quran fragility = 2.78e-4, LOWER than all three baselines (Bukhārī 3.50e-4, Jāḥiẓ 3.28e-4, Muʿallaqāt-partitioned 3.39e-4). Direction is OPPOSITE to pre-registered prediction. Per PRE-REG-STANDARD-01, filed as EXPLORATORY-REVERSE; cannot promote without independent H-NEW-42.1.

## Amendment-compliance

42-A: Muʿallaqāt fallback clause deleted. All three baselines required, hard-abort stance. Applied: pipeline ran with all three; no α loosening. ✓
42-B: Baseline paths corrected to `data/baseline-corpora/raw/*`. SHA-256 logged in JSON. ✓
42-C: Embedding-model commit hash pinning N/A (no model used); GoFP entry for char-trigram substitution logged pre-result. ✓

## MW-5 diagnostic

The direct-Muʿallaqāt positive-control failure was surprising: Muʿallaqāt verse-level fragility (1.33e-5) is far below Jāḥiẓ-partitioned (3.28e-4). Attributable to short-poem length normalisation effect (avg 70 verses per poem, √n dividing the score). Partitioned comparison passes at the edge (3.39e-4 > 3.28e-4). The strict reading (direct comparison must pass) dominates per audit-032 and is what drives the NULL-BROKEN verdict.

## Termination

Agent hit stream-idle timeout after ~6,400 s. JSON output already written; findings file and journal completed by integrator (main session) at 2026-04-15 using the JSON as authoritative data source.

Raw JSON: findings/phase-b-hypotheses/csv/h-new-42.json (complete, including positive-control values, SHA-256 hashes, extreme-surahs table).

## Cross-finding observation

Result is DIRECTION-CONSISTENT with H-NEW-34.1 (verse-final abjad under-dispersion) and H-NEW-43 (verse-length AR(1) closer to white than prose). Three orthogonal probes all show Quran-smoother-than-prose. Route to meta-analyst as the 2026-04-15-Fresh-Wave-3 triple meta-finding.
