---
finding_id: team-discovery-013
phase: B
status: CONFIRMED (strong)
date: 2026-04-12
rules_tuple: (no-tashkeel, QAC-roots, counted-only-in-surah-1, hafs-kufan, mashriqi)
null_model: 10,000-permutation surah-order-shuffle + non-adjacent pair baseline + per-pair Stouffer-Z
pre_registration_reference: pre-declared in script docstring prior to data read (seed 20260413)
bonferroni_k: 3
alpha_bon: 0.0167
hypothesis_origin: al-Biqāʿī (Burhān al-Dīn, d. 1480), *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*
related_findings:
  - team-discovery-010 (al-Biqāʿī RING: REFUTED)
  - team-discovery-010 (al-Rāzī LINEAR: CONFIRMED Z=+30.76)
---

# H-BIQAI-LOCAL — al-Biqāʿī's adjacent-surah seam munāsaba CONFIRMED

## Executive verdict

**CONFIRMED at Z = +10.06, p_one_sided < 0.0001.**

For 113 consecutive surah pairs (k, k+1), the Jaccard overlap between the
*last 20% of surah k*'s root tokens and the *first 20% of surah k+1*'s root
tokens exceeds a random-order baseline by more than ten permutation-null
standard deviations.

- mean adjacent-seam Jaccard: **0.1030**
- mean non-adjacent pair Jaccard: 0.0664 ± 0.0622
- permutation null (10,000 surah-order shuffles): 0.0667 ± 0.0036
- **z = +10.058**, p = 0.0000 (none of 10,000 shuffles matched the observed mean)
- Stouffer Z across 113 pairs: **+6.249**

All three tests pass Bonferroni-corrected α_bon = 0.0167 by large margins.

## Classical claim

al-Biqāʿī's *Naẓm al-Durar* (1480) argues that the final verses of surah k
"prefigure" or thematically "connect to" the opening of surah k+1 — this is
his local (seam) munāsaba claim. It is **logically distinct** from his
surah-internal ring-composition claim (which team-discovery-010 falsified
at Z = -2.51).

The distinction matters classically: al-Biqāʿī is often treated as a single
edifice, but the seam-claim and the ring-claim rest on different evidence
and different mechanisms. Here we adjudicate them separately.

## Observed vs pre-registered criteria

| Criterion | Threshold | Observed | Verdict |
|---|---|---|---|
| adj > non-adj (Stouffer, α_bon=0.0167) | Z > 2.39 | +6.25 | **PASS** |
| adj > random-order (permutation, α_bon) | Z > 2.39, p<0.0167 | +10.06, p<0.0001 | **PASS** |
| per-pair mean deviation | Stouffer Z > +2.33 | +6.25 | **PASS** |

## Effect size

Adjacent seam Jaccard is **55% larger** than the non-adjacent pair mean
(0.103 vs 0.066). This is not a subtle marginal signal — it is
comparable in magnitude to the al-Rāzī linear-autocorrelation finding.

## Head-to-head with al-Biqāʿī's ring thesis

From team-discovery-010:
- al-Biqāʿī ring (mean Jacc[v_i, v_{N-i-1}] vs random pairs): **Z = -2.51 (REFUTED)**
- al-Biqāʿī seam (mean Jacc[end_k, start_{k+1}] vs random-order): **Z = +10.06 (CONFIRMED)**

The same scholar, two different claims, two opposite empirical verdicts.
This is the kind of differential result that falsification-based
computational theology is designed to produce: not "al-Biqāʿī was right"
nor "al-Biqāʿī was wrong" but *this specific sub-claim replicates under
this operationalization while this other specific sub-claim does not*.

Seam-munāsaba (local adjacency) is real in root-Jaccard measure;
ring-composition (surah-internal chiasmus) is not detectable in the same
measure at surah scale.

## Interpretation

Consecutive surahs really do share more root vocabulary at their
boundaries than expected under random surah ordering. Three non-exclusive
explanations:

1. **Redactional seam-crafting**: whoever fixed the canonical order
   chose adjacent surahs whose boundary vocabulary resonates. This is
   the classical claim al-Biqāʿī makes.
2. **Topic continuity**: adjacent surahs tend to share topic clusters
   (e.g., al-Baqara → Āl ʿImrān both treat Jewish/Christian polemic;
   al-Tawba → Yūnus both treat Meccan/Medinan revelation dynamics).
3. **Length correlation confound**: adjacent surahs have correlated
   lengths (team-discovery-004 H-NEW-3), so root-vocabulary overlap
   may track length. However, the 10k-permutation null preserves
   length marginals (shuffles assignment but keeps set sizes), and
   the signal survives at Z=+10, so this confound is partially
   controlled.

## Garden of forking paths (disclosed)

- Edge window size: 20% (cut = max(10, n//5)). Not varied. Chosen pre-data.
- Jaccard as similarity metric (not cosine, not overlap coefficient).
- QAC roots (not lemmas, not raw tokens).
- Adjacency defined by canonical surah numbering 1→114 (uthmānic order).
  A reverse-chronological (Nöldekean) re-ordering is a natural follow-up.
- Non-adjacent baseline excludes the pair (i, i+1) but includes (i+1, i)
  (reverse-adjacent), which may slightly inflate the baseline.

## Limits

1. **Canonical order bias**: the test rewards *whatever* consistent
   ordering principle produced the mushaf. It does not distinguish
   "al-Biqāʿī-style thematic prefiguration" from "length-sorted"
   from "chronological-then-length" orderings. To do so requires
   a test that compares canonical ordering to Nöldeke-chronological.
2. **Root-level only**: we do not test phrase-level or syntactic
   seam. A richer semantic seam test (e.g., embedding similarity)
   is future work.
3. **Jaccard is symmetric**: al-Biqāʿī's classical claim is
   directional ("k prefigures k+1"). The symmetric Jaccard
   measures co-occurrence, not direction. A directed test (e.g.,
   fraction of end_k tokens that reappear in start_{k+1} but not
   vice versa) is a natural follow-up.
4. **No matched-corpus baseline**: we did not compute the same
   seam-Jaccard for, e.g., a shuffled-verse Qurʾan or a matched
   Arabic prose corpus. The within-corpus permutation null is
   strong but does not compare against a non-Quranic baseline.

## Reproducibility

Script: `scratch/team-discovery/h_biqai_local_seam.py`
Result JSON: `scratch/team-discovery/result-biqai-local-seam.json`
Seed: 20260413
Runtime: 4.07s user on 2026-04-12

## Classical significance

al-Biqāʿī's *Naẓm al-Durar* is the most ambitious medieval Muslim defense
of surah-order as deliberately crafted. Its reception has been mixed —
al-Suyūṭī accepted munāsaba in principle; Abū Ḥayyān and Ibn ʿAshūr were
skeptical. This finding provides the first **quantitative confirmation**
of al-Biqāʿī's seam-claim at canon-wide scale, alongside the decisive
refutation of his ring-claim. Both results together sharpen rather than
vindicate or dismiss the medieval tradition.
