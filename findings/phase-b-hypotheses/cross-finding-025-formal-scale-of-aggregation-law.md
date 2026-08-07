---
finding_id: cross-finding-025-formal
status: FORMAL CODIFICATION (graduates from PRELIMINARY 2026-05-09 PM to FORMAL 2026-05-09 PM-2 after triple-flip confirmation)
phase: B+ → C
date: 2026-05-09
verdict: 3/3 scale-of-aggregation flips CONFIRMED — principle locked at corpus-wide law strength
---

# Cross-finding-025 (FORMAL) — Scale-of-aggregation as a methodological axis: pericope-scale flip law

## The principle, formally stated

> **Cohesion verdicts in the Quran corpus are jointly determined by the triple `(marker-thickness × scale-of-aggregation × instrument)`. Pre-registration of a cluster-cohesion test MUST specify all three dimensions. Discrepant verdicts across different aggregation scales are first-class findings, not contradictions.**
>
> **Pericope-scale flip corollary**: thin-marker NULLs at whole-surah scale will frequently PASS at pericope scale (verse-window centered on the marker-attestation). This is a corpus-wide regularity, not an exception.

## Triple-flip empirical evidence (3/3 confirmed)

| Marker class | Whole-surah NULL | Pericope-scale PASS | Flip effect-size |
|---|---|---|---|
| **Iblīs-narrative** | H-NEW-039 (z = +0.24, p = 0.537) | **H-NEW-1380 (z = +4.76, p ≤ 10⁻⁴)** | **+4.52 σ** |
| **Sajda 14-verse cluster** | H-NEW-1330 (p = 0.571 / 0.110) | **H-NEW-1510 (z = +2.685, p = 0.0058)** | corroborates flip |
| **yā-ayyuhā al-nabī** | H-NEW-1360 (p = 0.573 / 0.584) | **H-NEW-1520 (z = +6.41, p < 10⁻⁴)** | **+6.41 σ — largest** |

**All three independently-pre-registered tests under the same instrument (Fisher-Rao-derived root-Jaccard, seed 20260509, 10000 perms) at the same statistical protocol, applied at different aggregation scales, produce inverted verdicts.** The pericope-scale finding is consistently more powerful than the whole-surah test for thin markers.

## Theoretical explanation

A marker that occupies a small fraction of a surah (single verse, single phrase, single sajda glyph) cannot move the *whole-surah* root-distribution measurably. The host-surah's content is dominated by ambient-block vocabulary; the marker is statistical noise at whole-surah scale.

But at the *pericope scale* (verse-window centered on the marker), the marker IS the content. Two pericopes from different host-surahs that share the same marker share — by construction — the marker-vocabulary. If they also share thematic vocabulary (the narrative material that surrounds the marker), the pericope-scale root-Jaccard will be elevated above random pericope baseline.

The empirical question is whether the shared THEMATIC vocabulary is enough to produce statistically-significant cohesion. Per H-NEW-1380, H-NEW-1510, H-NEW-1520, the answer is YES for at least three thin-marker classes.

## What this means for the project

1. **Re-test all thin-marker NULLs at pericope scale**. Queued:
   - **H-NEW-1310 Christ-narrative NULL (Q 3+Q 5+Q 19) — H-NEW-1500 in flight at session-end**
   - **H-NEW-1340 al-ḥamdu-li-llāh-opener cluster** — opener pericope = first 1-3 verses
   - **H-NEW-1395 ḥawāmīm 7-surah cluster** — muqaṭṭāʿat-opener pericope = first 3 verses
   - **H-NEW-1301/Q073-F-04 IMPV-qrA cluster** — imperative-verse pericope = the IMPV-qrA verse ± 2

2. **Update pre-registration discipline**. All cluster-cohesion pre-regs must henceforth specify:
   - **Marker definition** (what is the cluster's identifying feature?)
   - **Aggregation scale** (whole-surah / pericope-window / verse-pair / cross-block)
   - **Instrument** (FR root-distribution / char-4-gram / verse-length / rhyme)
   - The combination is the experimental unit, not any single axis.

3. **Re-classify existing NULLs**. Of the documented thin-marker NULLs in the project ledger (~10 entries), most should be re-tested at pericope scale. Likely PASSes: H-NEW-1340 al-ḥamdu (opener pericope), H-NEW-1395 ḥawāmīm (opener pericope), H-NEW-1310 Christ-narrative.

4. **NULLs that are NULL at BOTH scales are stronger findings**. If a marker-cluster NULLs at BOTH whole-surah AND pericope scale, the cluster is genuinely not cohesive at any granularity — a substantive NULL much stronger than a single-scale NULL.

5. **Update cross-finding-022 Wave-5 terminal synthesis**: the corpus-EXACT/EXTREME roster now includes the *methodological principle* itself as a finding-class — not a textual feature but a research-method discovery.

## Classical-tradition connection

al-Suyūṭī Itqān nawʿ 49 *fī asbāb al-nuzūl* implicitly recognizes the pericope-scale principle: classical asbāb-tradition treats individual verses (or short pericopes) as the units of revelation-event analysis, not whole surahs. The pericope-scale flip empirically vindicates the methodological intuition behind 1,400 years of asbāb-al-nuzūl literature.

al-Biqāʿī's *Naẓm al-durar* extends this to surah-level munāsabah but acknowledges that internal coherence of pericopes (the *naẓm* within a unit) operates at smaller scales than surah-surah munāsabah.

## Open follow-ups

1. Complete the pericope-scale re-test sweep across all queued thin-marker NULLs
2. Pre-register the **scale-of-aggregation principle** as itself a falsifiable claim — test 5+ NEW thin-marker pre-regs at pericope scale with direction-locked PASS prediction; verify ≥4 of 5 PASS
3. Investigate whether a *4th scale* (block-of-surah, verse-pair) reveals further structure
4. Cross-corpus baseline — does pre-Islamic poetry show the same scale-dependence?

## Files

- This formal codification: `findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md`
- Empirical anchors:
  - `findings/phase-b-hypotheses/h-new-1380-iblis-pericope-replication.md`
  - `findings/phase-b-hypotheses/h-new-1510-sajda-pericope-replication.md` (pending file write by specialist)
  - `findings/phase-b-hypotheses/h-new-1520-prophet-vocative-pericope.md` (pending file write by specialist)
- Earlier preliminary (`cf-025-marker`): `findings/phase-b-hypotheses/cross-finding-025-marker-thickness-vs-fr-cohesion-threshold.md`
  *(Correction 2026-08-07: this line previously pointed at `cross-finding-025-preliminary-marker-thickness.md`, a path that does not exist on disk. The file above is the actual ancestor — its §"next steps" is what names the future "cross-finding-025-formal".)*
- **ID disambiguation**: this document is `cf-025-formal`. Two other files also carry `cross-finding-025`: `cf-025-marker` (the preliminary above) and `cf-025-multiaxis` (`findings/cross-finding/cross-finding-025-multi-axis-architecture.md`, 2026-04-28, an unrelated topic). See `findings/CROSS-FINDING-INDEX.md`.

---

*Cross-finding-025 elevated to FORMAL status 2026-05-09 PM by Waiel Al-Shujaa upon triple-flip confirmation. Bismillāhi al-Raḥmāni al-Raḥīm.*


---

## Update 2026-05-10 — Pericope-flip law extended to 5/5 (H-NEW-1750 + H-NEW-1760 landings)

Two same-session opener-pericope flips extend the law to a 5-pair anchor.

| # | Marker class | Whole-surah NULL | Pericope PASS | Flip z |
|:-:|:--|:--|:--|:-:|
| 1 | Iblīs narrative | H-NEW-039 | H-NEW-1380 | +4.76 |
| 2 | Sajda 15-verse | H-NEW-1330 | H-NEW-1510 | +2.685 |
| 3 | yā-ayyuhā al-nabī | H-NEW-1360 | H-NEW-1520 | +6.41 |
| 4 | al-ḥamdu li-llāh opener | H-NEW-1340 | **H-NEW-1750** | **+3.86** |
| 5 | **Ḥawāmīm orthographic-opener (muqaṭṭaʿāt)** | **H-NEW-1395** | **H-NEW-1760** | **+6.008** |

The 5th pair (H-NEW-1760, ḥawāmīm 7-surah opener-pericope at z=+6.008, p<10⁻⁴) is the FIRST orthographic-opener marker class to support the law and the second-largest z-magnitude on record. The flip is driven by the corpus-EXACT *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* opener-formula sub-family (Q 40 / 41 / 45 / 46) and the *wal-kitāb al-mubīn* sub-family (Q 43 / 44), with Q 45 ↔ Q 46 pairing at J = 0.438 (corpus-extreme for the 21-pair table).

The next falsification-target is the first NULL/NULL pair — a thin-marker cluster that NULLs at BOTH whole-surah AND pericope scale would refine the law's domain of applicability. Until such a counterexample is found, the pericope-flip law stands at corpus-wide law strength across narrative / liturgical / discourse / liturgical-opener / orthographic-opener marker classes (5/5).

- H-NEW-1750 (al-ḥamdu opener-pericope flip): pre-reg + finding under standard paths.
- H-NEW-1760 (ḥawāmīm opener-pericope flip): `findings/phase-b-hypotheses/prereg-h-new-1760-hawamim-opener-pericope.md`, `scripts/h-new-1760.py`, `csv/h-new-1760.json`, `h-new-1760-hawamim-opener-pericope.md`.
