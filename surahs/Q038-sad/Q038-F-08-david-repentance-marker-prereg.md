---
surah: 38
test_id: Q038-F-08
title: David sajda thematic discriminator — Q 38 David-narrative (vv 17-29) repentance-focus vs Q 21:78-80 David-praise
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q038-F-08-david-repentance-marker
alpha_bon: 0.05
---

# Q038-F-08 — Pre-registration: David-narrative repentance-focus discriminator

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The David narrative in Q 38 (vv 17-29) is **MORE repentance-focused** than the David-praise verses Q 21:78-80, measured by the density of tokens carrying the QAC roots associated with repentance / turning-back / forgiveness / prostration: {ʾwb (أوب), tāb (توب), gh-f-r (غفر), s-j-d (سجد), r-j-ʿ (رجع), n-d-m (ندم), ḥ-s-b (only when in penitential sense — excluded for safety), ʾ-w-b is the primary anchor since *innahu awwāb* refrains in Q 38}.

**Pre-committed direction (LOCKED):** density(repentance-roots in Q 38:17-29) > density(repentance-roots in Q 21:78-80), where density = (count of repentance-root token-occurrences) / (count of all tokens in the segment).

**H0:** Repentance-root density in Q 38 David-narrative ≤ that of Q 21 David-praise.

## 2. Operational definition

**Repentance-root set R** (LOCKED before observation):
- `Awb` (أوب)
- `twb` (توب)
- `gh-f-r` (غفر)
- `s-j-d` (سجد)
- `r-j-ʿ` (رجع)
- `n-d-m` (ندم)

These are extracted via QAC-v0.4 ROOT field. The root labels in QAC are stem-style strings like `Awob`, `tawob`, `gh~afar`, `sajad`, `rajaE`, `nadim` — the script must map to QAC's exact strings (see §6).

**Segment A** = Q 38:17-29 (13 verses, David-trial narrative including sajda at v.24).
**Segment B** = Q 21:78-80 (3 verses, David-praise narrative).

For each segment:
- `n_tokens(segment)` = count of all words.
- `n_repentance_tokens(segment)` = count of tokens whose QAC ROOT lies in R.
- `density(segment) = n_repentance / n_tokens`.

Test statistic: `Δ = density(A) − density(B)`.

**Null distribution**: For each of 10000 permutations, randomly assign the 16 combined verses (13 from Q 38:17-29 + 3 from Q 21:78-80) to two groups of size (13, 3) and recompute Δ. p = fraction of null Δs ≥ observed.

## 3. Test statistic

- Primary: `Δ = density(Q 38:17-29) − density(Q 21:78-80)` (in repentance-tokens / total-tokens).
- Significance: one-tailed permutation p (greater).
- Bonferroni: k = 1. α = 0.05.

## 4. Success / Failure

- **CONFIRMED**: `Δ > 0` AND `p_perm < 0.05`.
- **DIRECTIONAL**: `Δ > 0` but `p_perm ≥ 0.05`.
- **NULL**: `Δ ≤ 0` OR `p_perm ≥ 0.5`.
- **PRE-COMMIT VIOLATION**: `Δ < 0` (Q 21 strictly MORE repentance-focused than Q 38). Published with full prominence.

## 5. Honest limits known a priori

- The Q 21:78-80 segment is small (3 verses, ~30 tokens). Statistical power is low; small-N noise dominates.
- The classical reading (e.g. al-Ṭabarī ad Q 21:78-80; al-Rāzī ad Q 38:24-25) presents Q 21 as **praise** (wisdom granted, mountains and birds glorifying), Q 38 as **trial-and-repentance** (the two litigants, David's sajda, the *innahu awwāb* refrain). The pre-committed direction matches this classical reading.
- Root choice is locked in advance. Adding/removing roots post-observation is a pre-commit violation.
- The root *ʾwb* (أوب) appears at Q 38:17, 19, 30 (×2), 44 (×3). Three of these are inside segment A. The verb *sajada* at v.24 is in segment A. By construction these contribute to A's density.
- Q 21:79 contains *fa-fahhamnāhā Sulaymān* (granted understanding to Solomon) and the *sabbaha* / glorification roots — these are NOT in the locked R set. Q 21:80 mentions *li-tuḥṣinakum min baʾsikum* (armor for protection) — not in R. So Q 21:78-80's density of R-roots is expected to be low or zero.
- The expected result is therefore strongly directional. The honest framing is: this is a CONFIRMATION test of a classically-grounded reading, not a discovery test. The statistical interpretation must reflect that.

## 6. Rules-tuple and QAC root strings

`(no-tashkeel for token-id, root-tokens via QAC-v0.4 morphology, Hafs-Kufan, Mashriqi)`.

QAC ROOT-field mapping (locked in advance, verified against QAC v0.4 by direct grep):
- ʾwb → `Awb`
- twb → `twb`
- ghfr → `gfr`
- sjd → `sjd`
- rjʿ → `rjE`
- ndm → `ndm`

(These are the canonical QAC v0.4 ROOT abbreviations as observed in the corpus file; verified before SHA-lock. The script verifies each root has ≥ 1 attestation in the corpus before running.)

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q038_F_08_david_repentance_marker.py`. Fail-fast on mismatch.
