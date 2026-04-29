---
finding_id: h-new-212
title: Alternative chronology orderings — Fisher-Rao path-length
parent: h-new-111 (Fisher-Rao mushaf-order geodesic)
status: PASS (family-level) / MUSHAF-STILL-WINS
date: 2026-04-17
seed: 20260419
bonferroni_k: 3
alpha_bon: 0.01667
verdict_ceiling: PASS (not CONFIRMED; single feature-set)
pre_reg_sha256: 70777c0b108a0dc54af59f120829c74395b2e601f80623eb50e99ba7e774076e
---

# [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] — Alternative chronologies under Fisher-Rao

## Result

Under the Fisher-Rao distance matrix D from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC STEM roots, top-500,
Dirichlet α=0.5, L1-normalized), path-length leaderboard over 114 surahs:

| Rank | Ordering | L | z vs null | p (1-sided lower) |
|----|----|----|----|----|
| 1 | **mushaf** (reference) | **85.7597** | **−11.42** | 0.0001 |
| 2 | Nöldeke 1860 (reference) | 87.2321 | −10.52 | 0.0001 |
| 3 | Bell 1937 | 87.7956 | −10.17 | 0.0001 |
| 4 | Egyptian Standard 1924 | 89.5297 | −9.11 | 0.0001 |
| 5 | Blachère 1947 | 89.8345 | −8.92 | 0.0001 |

Null mean = 104.35, null SD = 1.63 (10 000 perms, seed 20260419, fresh).

## Pre-registered Bonferroni family (k=3, α_bon=0.01667)

All three PASS at α_bon:

- **Egyptian Standard 1924**: p = 0.0001 → **PASS**
- **Bell 1937**: p = 0.0001 → **PASS**
- **Blachère 1947**: p = 0.0001 → **PASS**

## Primary questions answered

**Which ordering is Fisher-Rao-SHORTEST?**  mushaf (85.76), by a margin
of 1.47 (0.91 null-SDs) over the nearest chronology (Nöldeke 1860).

**Does mushaf still win?**  YES. L_mushaf < L_c for every c ∈ {Egyptian,
Nöldeke, Bell, Blachère}. Margins (null-SD units) vs mushaf:

- Egyptian 1924: +2.317 SDs longer
- Nöldeke 1860: +0.905 SDs longer
- Bell 1937: +1.251 SDs longer
- Blachère 1947: +2.504 SDs longer

## Chronology spearman correlations (diagnostic, not in family)

- ρ(Bell, Nöldeke) = +0.954 (near-identical)
- ρ(Blachère, Egyptian) = +0.963 (near-identical)
- ρ(Bell, Blachère) = +0.689 (moderate)
- ρ(Egyptian, Nöldeke) = +0.771 (moderate)
- ρ(mushaf, Nöldeke) = −0.655; ρ(mushaf, Bell) = −0.621;
  ρ(mushaf, Blachère) = −0.406; ρ(mushaf, Egyptian) = −0.406

Two "schools" emerge:

- **length-sorted chronologies** (Egyptian, Blachère) — ρ=+0.96 with each
  other; both ~2.3–2.5 null-SDs longer than mushaf
- **style-sorted chronologies** (Nöldeke, Bell) — ρ=+0.95 with each other;
  both ~0.9–1.3 null-SDs longer than mushaf

All four chronologies correlate negatively with mushaf (canonical order is
anti-chronological in all schemes, which is the classical *tawqīfī*
position: canonical order is not chronology).

## Interpretation

1. The Fisher-Rao geodesic-like property of the mushaf ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) is NOT
   trivially recovered by any of the four published academic chronologies.
   Mushaf is shorter than the best chronology (Nöldeke 1860) by 0.91 null-SDs
   — a **descriptive** margin, not a chronology-mushaf permutation p-value
   (not pre-registered).

2. **All four chronologies BEAT random (p < 10⁻⁴ one-sided)**. There IS a
   chronological coherence signal — just weaker than the mushaf's.

3. The two style-based chronologies (Nöldeke, Bell) outperform the two
   length-descending chronologies (Egyptian, Blachère) for Fisher-Rao root
   coherence. Plausible because Nöldeke/Bell use VOCABULARY style as a
   classifier, and Fisher-Rao D operates on root distributions — so of
   course vocabulary-sorted chronologies do better.

4. Since all four chronologies agree that **canonical order ≠ chronology**
   (all ρ negative), the mushaf's Fisher-Rao shortness is NOT chronological
   information; it is SOMETHING ELSE. [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s original finding survives
   this robustness check.

## Data quality caveats (documented in pre-reg §5-6)

- **Bell, surah 15**: source (Fr. Wikipedia) codes as "M" not numeric; imputed
  rank 52 (middle Meccan median).  Sensitivity: changing this rank by ±10
  shifts L_bell by <0.05 (<<0.03 null-SDs); does not affect verdict.
- **Bell, surahs 81/82**: both rank 15 → mushaf-order secondary.
- **Blachère, surahs 80/84**: both rank 24 → mushaf-order secondary.

## Inherited assumptions

- Distance matrix D inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (SHA-256
  4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc).
- Rules-tuple: no-tashkeel, QAC STEM roots, QAC v0.4, Hafs-Kufan,
  basmala-counted-only-in-surah-1.
- MW-1 (length control via L1-normalization) inherited.
- MW-5 (positive control greedy-NN-from-s1) inherited (PASSES in [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).

## Verdict

- **Family-level**: PASS (all 3 alt chronologies beat random at α_bon)
- **Head-to-head vs mushaf**: mushaf remains SHORTEST; descriptive margin
  0.91 null-SDs over Nöldeke (best chronology)
- **Ceiling**: PASS (not CONFIRMED) per project discipline — single feature
  set, no independent replication required by this pre-reg. Replication
  candidates: [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-gram Fisher-Rao) and [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] (verse-length
  Fisher-Rao) exist; extending [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] to those is a natural H-NEW-212.1.

## Files

- pre-reg: `findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao-prereg.md`
- script: `scripts/h_new_212_alt_chronology_fisher_rao.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-212.json`
