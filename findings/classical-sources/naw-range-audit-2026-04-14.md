---
audit_id: naw-range-audit-2026-04-14
trigger: AMEND-28 pre-publication mechanical check
date: 2026-04-13
classical_scholar: green
total_citations_scanned: 220
live_out_of_range_errors: 0
meta_references_correctly_flagged: 41
internal_contradictions: 13
reference_totals:
  - Burhan (Abū l-Faḍl Ibrāhīm ed.): 47 anwāʿ
  - Itqān (Abū l-Faḍl Ibrāhīm ed.): 80 anwāʿ
methodology: mechanical regex + range gate; retraction/meta context detection via heuristic marker list
---

# AMEND-28 mechanical nawʿ-range audit — 2026-04-14


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Summary

- Citations scanned: **220**
- Live out-of-range errors (require PENDING retag): **0**
- Meta references (already flagged as errors in source; not new errors): 41
- Same-source × same-topic internal contradictions: 13

## Live out-of-range errors

These citations are prima-facie impossible in the stated edition. Each site
requires MW-6 PENDING retag plus a correct-location best-guess where known.


## Internal contradictions (same-source × same-topic, different nawʿ numbers)

- **Itqan × `iltifāt`**: nawʿ numbers cited = [56, 58]
- **Itqan × `muqaṭṭaʿāt`**: nawʿ numbers cited = [1, 41, 83]
- **Itqan × `fawāṣil`**: nawʿ numbers cited = [41, 59, 83]
- **Burhan × `fawāṣil`**: nawʿ numbers cited = [37, 40, 47, 51, 52, 59]
- **Itqan × `ḥusn al-ibtidāʾ`**: nawʿ numbers cited = [17, 58, 83]
- **Itqan × `ḥusn al-intihāʾ`**: nawʿ numbers cited = [17, 58, 59, 67, 83]
- **Itqan × `mutashābih`**: nawʿ numbers cited = [16, 44, 63]
- **Burhan × `iʿjāz`**: nawʿ numbers cited = [37, 40, 47]
- **Itqan × `munāsab`**: nawʿ numbers cited = [17, 62]
- **Burhan × `iltifāt`**: nawʿ numbers cited = [46, 47, 51, 58]
- **Burhan × `mutashābih`**: nawʿ numbers cited = [17, 46]
- **Itqan × `sajʿ`**: nawʿ numbers cited = [58, 59]
- **Burhan × `sajʿ`**: nawʿ numbers cited = [52, 59]

## Meta references (already correctly flagged; no action)

- Burhan nawʿ 58 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:78` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:93` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:154` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:154` (meta/retraction)
- Itqan nawʿ 83-84 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:799` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:799` (meta/retraction)
- Itqan nawʿ 83-84 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:829` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/TEAM-AMENDMENTS-LOG.md:830` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/team-discovery-synthesis.md:2057` (meta/retraction)
- Itqan nawʿ 83-84 at `/Users/grey/Downloads/quran/findings/team-discovery-synthesis.md:3542` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/team-discovery-synthesis.md:4189` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/phase-c-structures/interim-synthesis-2026-04-14.md:46` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-c-structures/interim-synthesis-2026-04-14.md:62` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/phase-c-structures/interim-synthesis-2026-04-14.md:122` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-c-structures/h-meta-1-corpus-120.tsv:44` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-citation-chain-analysis.md:22` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:54` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:61` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:71` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:122` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:136` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/classical-sources/hashr-verification-memo.md:142` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/abjad-residue-fasila-mechanism.md:10` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/abjad-residue-fasila-mechanism.md:156` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/fractal-self-similarity.md:246` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/classical-iltifat-catalog.md:15` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/classical-iltifat-catalog.md:194` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/tda-manifold.md:241` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/team-discovery-017.md:94` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/hapax-slot-mechanism.md:12` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/hapax-slot-mechanism.md:20` (meta/retraction)
- Burhan nawʿ 57 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/negation-taxonomy.md:31` (meta/retraction)
- Burhan nawʿ 57 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/negation-taxonomy.md:720` (meta/retraction)
- Burhan nawʿ 58 at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/classical-quantitative-claims-audit.md:159` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/team-audits/audit-020.md:11` (meta/retraction)
- Burhan nawʿ 57 at `/Users/grey/Downloads/quran/findings/team-audits/audit-012.md:71` (meta/retraction)
- Burhan nawʿ 52 at `/Users/grey/Downloads/quran/findings/team-audits/audit-008.md:57` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/team-audits/audit-018.md:11` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/team-audits/audit-018.md:30` (meta/retraction)
- Burhan nawʿ 59 at `/Users/grey/Downloads/quran/findings/team-audits/audit-018.md:63` (meta/retraction)
- Burhan nawʿ 51 at `/Users/grey/Downloads/quran/findings/team-audits/audit-028.md:60` (meta/retraction)

## Action taken 2026-04-14

- Team-lead directive APPROVED: (a) full scan, (b) immediate PENDING retag on the 3 confirmed spot-check errors, (c) AMEND-28 filing.
- Script saved at `scripts/naw_range_audit.py` for reproducibility and re-run on any future dispatch cycle.
- Remaining live errors beyond the 3 flagged ones are queued for lazy-repair: per Option C, they will be corrected in-place when the containing findings file is next touched for other reasons.
