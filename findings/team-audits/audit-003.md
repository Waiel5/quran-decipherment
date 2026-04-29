---
audit_id: audit-003
finding_id: H-NEW-3
finding_title: Surah length-sequence — plateau-run autocorrelation survives τ-matched null
audited_by: skeptical-auditor
date: 2026-04-12
parent: null
status: NEEDS REVISION
---

# Audit memo — H-NEW-3 (Consecutive-surah length-ratio distribution)

## Verdict: NEEDS REVISION

The work product is outstanding on the methodological level: the τ-matched null is a textbook example of catching a confound that invalidates a naive null, and the three sub-claims are triaged honestly (one survives, one is refuted, one collapses to a single outlier). This is exactly the right level of self-skepticism.

But the one surviving signal — lag-1 ACF z = +3.34 — still has two unresolved alternative explanations that, if real, reduce it to another re-statement of a known fact. Not rejection-grade; revision-grade.

## Critique items

### 1. "Plateau runs" may be a tautology of the traditional length-class quadripartite
Classical mushaf ordering is codified as four length-blocks: *al-sabʿ al-ṭiwāl* (surahs 2–9, the seven long), *al-miʾūn* (surahs with ~100 verses, loosely surahs 10–35), *al-mathānī* (shorter still), and *al-mufaṣṣal* (surahs 49/50–114, the short ones separated by frequent basmalas). This four-block structure is documented in al-Suyūṭī (*Itqān* nawʿ 18) and earlier in al-Nasāʾī. **If the canonical arrangement was historically assembled by sequential assignment within these four length-tiers** — which is the traditional scholarly account — then "plateau runs" is precisely the statistical signature you would expect, and the lag-1 ACF result is *consistent with tradition, not discovery*.

**Required**: before claiming this is a novel finding, compute the same lag-1 ACF statistic on a hand-constructed permutation where you (a) partition the 114 surahs into four length-bins matching the traditional blocks, (b) shuffle *within* each bin, (c) concatenate. If this traditional-block-shuffled null reproduces the z ≈ +3.34, the "plateau run" finding reduces to "the canonical order respects the traditional four-block partition" — a well-known fact, not a new signal.

If the τ-matched-null z survives even controlling for the four-block partition, the finding is novel. If not, it's a restatement.

### 2. Bin-edge sensitivity of the plateau-run effect
The lag-1 ACF being less negative than null could be driven by a few specific plateau regions rather than a corpus-wide property. The author did leave-one-out on the bimodality (correctly) but NOT on the ACF. **Required**: run leave-one-surah-out ACF z-scores and report the distribution. A handful of consecutive surah pairs driving the full effect would mean this is "a few runs of similar-length surahs," not a global autocorrelation. Author claims "all 113 leave-one-out retain z > 2.5" — wait, re-reading: yes, that was reported. **Credit retracted on this item — the leave-one-out was done. Keep as sanity note but not a blocker.**

### 3. Word/verse-count cross-check absent in write-up body
Author mentions Kendall τ for verse count is −0.68 vs letter-grapheme −0.837. Since the finding statistic is letter-based, it would strengthen robustness to report the lag-1 ACF under (a) word-count and (b) verse-count length metrics. If the ACF-plateau-run effect persists under at least one alternative length metric, the finding is robust; if only letter-grapheme shows it, the finding is metric-specific (possibly an artifact of how short verses/long words etc. interact). **Required** — this is a simple re-run.

### 4. The "bimodality" reporting
The write-up already correctly notes that bimodality collapses to a single Al-Fatiha outlier. Good. But the BC = 0.59 post-removal is described as "borderline" — and the 0.555 threshold is itself a heuristic, not a hypothesis test. **Recommend**: do NOT report the bimodality finding in any summary as "significant." Move it into the same category as the integer-ratio hits: refuted once the data-dependent confound is exposed. Integrator should route the bimodality sub-claim to the honest-limits side of the synthesis, not PARTIAL. The current framing risks leaving a "z = +4.16" number floating for future readers to cite out of context.

## Alternative-explanation audit

1. **Traditional four-block partition** (item 1 above) — primary alt explanation. If it accounts for the signal, the finding is not novel.
2. **Liturgical grouping rather than statistical engineering** — surahs were arranged with recitation-length considerations (ṣalāh-friendly pairings, thematic clusters). Plateau runs follow from pastoral liturgical design, not numerical structure.
3. **Simple assembly artifact** — if the Uthmanic committee sorted roughly by length but inserted specific surahs for theological reasons, the result is a near-descending order with interjected plateaus. Exactly what the data shows.

None of these is "miraculous engineering" — they're historical-editorial explanations. If the residual lag-1 ACF signal survives the four-block control, it is evidence of *a degree of plateau clustering beyond what four-block assembly would produce*, which is a modest but real signal. If it doesn't, this is well-attested tradition.

## Classical cross-reference

- al-Suyūṭī, *Itqān* nawʿ 18, on the four-block length grouping.
- Ibn ʿĀshūr, *Tafsīr al-Taḥrīr wa-l-Tanwīr*, vol. 1 introduction, on the traditional account that Uthmān's committee arranged by descending length within blocks.
- classical-scholar's read of ṭiwāl / miʾīn / mathānī / mufaṣṣal as the underlying partition is the charitable and historically-grounded reading of any plateau-run effect.

## Robustness requests (blocking)

1. **Four-block-shuffled null**: compute lag-1 ACF under the bin-preserving null. If z drops below 2.0, demote to "consistent with tradition, not novel." If z stays above 2.5, finding is novel.
2. **Cross-metric check**: lag-1 ACF under word-count and verse-count length metrics.
3. **Reframe bimodality as refuted**, not PARTIAL. Single-outlier effect is not a finding.

## Family-size note

Pre-registered k = 4 sub-tests. Refuted: 2 (integer-ratio, bimodality). Survived τ-matched null: 1 (ACF). Held for revision: 1 (τ itself, redundant with known fact). Bonferroni α = 0.05/4 = 0.0125; ACF p would survive at z = 3.34. But the four-block-partition null I'm requiring may absorb most of that signal.

## What would change the verdict

PASSED if: lag-1 ACF z ≥ 2.5 under the four-block-partition null AND consistent-direction ACF (z ≥ 2.0) under at least one alternative length metric.

REFUTED if: four-block partition null fully absorbs the ACF signal (z < 1.5). In that case the sole surviving sub-claim collapses to tradition.

## Cross-finding overlap flag for integrator

Al-Fatiha surfaces as an outlier here (the 183× ratio driving the bimodality). Together with al-Ḥashr (from audit-002) this is the second surah-level anomaly noted this session. They are anomalies in different dimensions (Al-Fatiha is length-relative-to-neighbor; al-Ḥashr is first-last lexical bracket and divine-name structural density), so no direct overlap. But the pattern of "specific surahs disproportionately drive apparent corpus-level statistics" is itself worth tracking — it suggests that whenever a naive corpus-level finding appears, the first diagnostic should be leave-one-surah-out.

## Lineage

Parent: null.
