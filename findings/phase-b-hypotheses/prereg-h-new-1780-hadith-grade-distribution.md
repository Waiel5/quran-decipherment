---
id: H-NEW-1780
title: ṣaḥīḥayn vs Sunan hadith-grade distribution across project surahs
date_locked: 2026-05-10
seed: NA (descriptive ratio computation; no permutation null)
n_perm: NA
bonferroni_k: 1
bonferroni_family: H-NEW-1780 single-test descriptive ratio
alpha_bon: NA
direction_of_effect: ≥ 30% of project surah-specific classical ḥadīth citations rest on Sunan-grade evidence (Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī) NOT on ṣaḥīḥayn (al-Bukhārī + Muslim). Direction is LOCKED before tally.
origin: Q022-F-06 (Q 22 al-Ḥajj specialist, 2026-05-09) discovery that al-Bukhārī *Kitāb Sujūd al-Qurʾān* (chapter id 17, ḥadīths 1036–1048) is SILENT on Q 22 — the Sunnī double-sajda position rests on Abū Dāwūd #1402, Tirmidhī #578, Ibn Mājah #1057 (all Sunan-grade) plus mawqūf statements. This raises a broader methodological question: how often do classical surah-claims rest on ṣaḥīḥayn versus Sunan-grade evidence? The default rhetorical move of saying "the Sunnī classical tradition holds X" is sometimes shorthand for "Sunan-4 + Aḥmad transmit X" rather than "ṣaḥīḥayn confirm X". This audit makes that distinction empirical.
verdict_ceiling: DESCRIPTIVE-CONFIRMED if direction met; DESCRIPTIVE-NULL if % Sunan < 30%; PRE-COMMIT-VIOLATION published if reversed (which here means "% Sunan < 30% with majority ṣaḥīḥayn").
rules_tuple:
  hadith_classification: canonical Sunnī 9-book grouping (ṣaḥīḥayn = Bukhārī + Muslim; Sunan-4 = Tirmidhī + Abū Dāwūd + Nasāʾī + Ibn Mājah; Other = Mālik Muwaṭṭaʾ + Aḥmad Musnad + Dārimī)
  idInBook_indexing: per /Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset edition
  citation_unit: a (surah, claim-topic, collection) tuple drawn from per-surah 04-hadith-corpus.md files
  scope: 25+ surah-specific classical ḥadīth citations from project per-surah hadith corpus files
  sahihayn_definition: al-Bukhārī + Muslim only
  sunan_definition: Tirmidhī + Abū Dāwūd + Nasāʾī + Ibn Mājah
  other_definition: Mālik Muwaṭṭaʾ + Aḥmad Musnad + Dārimī
  attribution_rule: when a claim has BOTH ṣaḥīḥayn AND Sunan attestation, classify the PRIMARY claim by the project-noted strongest attestation; tally each ḥadīth-instance as its own citation
---

# H-NEW-1780 pre-registration — ṣaḥīḥayn vs Sunan-grade hadith citation distribution

## Origin

The Q 22 al-Ḥajj specialist (Q022-F-06, file `/Users/grey/Downloads/quran/surahs/Q022-al-hajj/04-hadith-corpus.md`, section 1.4) discovered that al-Bukhārī's *Kitāb Sujūd al-Qurʾān* (chapter id 17, ḥadīths 1036–1048) is SILENT on Q 22. The Sunnī-majority double-sajda position rests entirely on:

- Abū Dāwūd *Sunan* #1402 (chain through ʿAbd Allāh b. Munayn, classed *majhūl* by some)
- al-Tirmidhī *Sunan* #578 (Tirmidhī's own grade: *laysa bi-dhāka al-qawī* — "not particularly strong")
- Ibn Mājah *Sunan* #1057
- Mawqūf statements via ʿUmar and Ibn ʿUmar

This is a Sunan-grade (not ṣaḥīḥayn-grade) attestation. The Mālikī school dissents on this point and does NOT break with the ṣaḥīḥayn because the ṣaḥīḥayn are silent on the question.

This raises a broader empirical question: how often is the rhetorical short-hand "classical tradition holds X" actually a transmission of a Sunan-grade claim rather than a ṣaḥīḥayn claim?

## Hypothesis (single primary test)

**H1**: At least 30% of the surah-specific classical ḥadīth citations indexed in this project's per-surah `04-hadith-corpus.md` files rest on Sunan-grade evidence (Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, or al-Dārimī *Sunan*) and NOT on ṣaḥīḥayn (al-Bukhārī + Muslim).

This makes empirical the methodological observation that "Sunnī classical hadith" is heterogeneous in grade.

## Methodology

1. Read each `surahs/Q{NNN}-{slug}/04-hadith-corpus.md` file present on disk (63 files at the time of lock).
2. For each file, extract every distinct ḥadīth-citation that names a specific collection plus either a ḥadīth-number, idInBook reference, or chapter/bāb reference. Each (surah, claim-topic, collection, identifier) tuple is one citation-instance.
3. Categorize each citation:
   - **ṣaḥīḥayn**: al-Bukhārī, Muslim
   - **Sunan-4**: Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah
   - **Other (Sunan-grade)**: Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, al-Dārimī *Sunan*, al-Bayhaqī *Sunan al-Kubrā* (treated as Sunan-grade), Ibn Ḥibbān *Ṣaḥīḥ* (treated as Sunan-grade since it is outside the canonical 9-book ṣaḥīḥayn pair), al-Ḥākim *Mustadrak*, Ibn Abī Shayba *Muṣannaf*.
   - **Tafsīr-only**: claim is attested only via tafsir literature (al-Suyūṭī *al-Itqān*, Ibn Kathīr *Tafsīr*, al-Ṭabarī *Tārīkh*) without a primary 9-book collection — these are noted but EXCLUDED from the ratio numerator/denominator since they are not "ḥadīth-corpus citations" in the technical sense.
4. Compute:
   - N_total = total ḥadīth-corpus citation-instances counted
   - N_sahihayn = count of ṣaḥīḥayn citations
   - N_sunan4 = count of Sunan-4 citations
   - N_other = count of Mālik + Aḥmad + Dārimī + Bayhaqī + Ibn Ḥibbān + Mustadrak + Muṣannaf
   - %sahihayn = N_sahihayn / N_total
   - %sunan4 = N_sunan4 / N_total
   - %other = N_other / N_total
   - %sunan-grade = (N_sunan4 + N_other) / N_total
5. Direction check: %sunan-grade ≥ 30% → H1 supported (DESCRIPTIVE-CONFIRMED). %sunan-grade < 30% → DESCRIPTIVE-NULL.

## Pre-registered direction lock

Direction LOCKED before tallying: **%sunan-grade ≥ 30%**. The Q 22 al-Ḥajj specialist case (where ṣaḥīḥayn is silent and the entire Sunnī position rests on Sunan-grade) was the prompting case. The 30% threshold is a substantively-meaningful minority threshold (one in three) — large enough that the rhetorical short-hand "classical = ṣaḥīḥayn" is empirically wrong, small enough that a true majority of citations could still be ṣaḥīḥayn.

Failure modes:
- %sunan-grade < 30% with ṣaḥīḥayn-dominant: PRE-COMMIT VIOLATION → published as DESCRIPTIVE-NULL with full prominence; would mean the project's existing corpus is ṣaḥīḥayn-dominant and the Q 22 case is an outlier rather than typical.
- %sunan-grade ≥ 30%: H1 supported; the methodological-vigilance prediction is empirically substantiated.

## Sample-size requirement

Project requirement: audit ≥ 25 surah-specific classical ḥadīth citations. In practice we will tally all extractable citations from all 63 per-surah files; the sample size should comfortably exceed 100. The 25-citation threshold is the minimum for ratio-meaningfulness.

## Operational definition of "surah-specific" classical ḥadīth citation

A ḥadīth-citation qualifies as "surah-specific" when:
- The ḥadīth-corpus file explicitly cites it as supporting a Q{NNN}-specific claim (e.g., a fadāʾil-of-the-surah, an asbāb al-nuzūl, a recitation-prescription, a doctrinal point, or a textual-link).
- The collection name AND either a ḥadīth-number, idInBook, or chapter-section reference is present.

EXCLUDED:
- Vague "the ḥadīth literature attests" with no specific number.
- Tafsīr-only attestations.
- Claims that are not surah-specific (e.g., a general fadāʾil al-Qurʾān ḥadīth that names many surahs).
- Sub-references to the same ḥadīth-number under different topical groupings (de-duplicate by collection + ḥadīth-number).

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Classification | Canonical Sunnī 9-book grouping |
| ṣaḥīḥayn | al-Bukhārī + Muslim only |
| Sunan-4 | al-Tirmidhī + Abū Dāwūd + al-Nasāʾī + Ibn Mājah |
| Other-Sunan | Mālik + Aḥmad + Dārimī + Bayhaqī + Ibn Ḥibbān + Mustadrak + Muṣannaf (all post-ṣaḥīḥayn, all categorized as Sunan-grade for purposes of this binary) |
| Tafsīr-only | EXCLUDED from ratio (noted separately) |
| Attribution | One citation-instance per (surah, ḥadīth-number, collection) tuple |
| De-duplication | Multiple citations of the same ḥadīth across topical sections of one surah file count as one instance per file |
| Sample-size minimum | 25 citations |

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Classification scheme locked above before counting.
- **MW-2 (corpus-prior)**: No permutation null (descriptive ratio test).
- **MW-3 (alternative-models)**: We will report both the binary (ṣaḥīḥayn vs not-ṣaḥīḥayn) and the trinary (ṣaḥīḥayn / Sunan-4 / Other) distributions.
- **MW-4 (over-fitting)**: No fitted parameter.
- **MW-5 (replication)**: A separate re-tally by an independent reader is queued as H-NEW-1780b if PASS.
- **MW-6 (instrument-control)**: A per-surah breakdown is the natural control; if one or two surahs dominate, the corpus-level ratio may be Simpson-biased and we report this.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc.

## Garden-of-forking-paths disclosure

- The 30% threshold is chosen before tallying; if we observed first and then chose 30%, this would be post-hoc.
- The classification of Ibn Ḥibbān as "Other-Sunan" (not as ṣaḥīḥayn-grade) is locked here; Ibn Ḥibbān is sometimes called *Ṣaḥīḥ Ibn Ḥibbān* in classical literature, but it is NOT part of the canonical ṣaḥīḥayn pair. We use the strict ṣaḥīḥayn definition.
- al-Bayhaqī, al-Ḥākim, Ibn Abī Shayba are all classified as Other-Sunan because they post-date the ṣaḥīḥayn and are widely treated as Sunan-grade in classical hadith-criticism.
- Q 2's al-Dārimī count of 45 hits (auto-indexed) is large and could dominate the Other column; we will report per-surah breakdowns to expose this Simpson-risk.
- We tally citation-INSTANCES per file (one per topical claim), not unique ḥadīth-numbers; this gives more weight to ḥadīths cited under multiple claims, which is the desired weighting for the methodological-vigilance question (which asks: when a project surah's classical-claim references hadith, how often is that hadith ṣaḥīḥayn-grade?).

## Connection to existing findings

- Q022-F-06 (parent finding): al-Bukhārī silent on Q 22 sujūd; Sunan-grade only.
- cross-finding-015-classical-scholarship-validation-pattern: a related question of when classical scholarship aligns with empirical findings.
- This pre-reg generalizes the Q 22 observation across the project's full surah-specialist corpus.

## Honest limits

- The project's per-surah `04-hadith-corpus.md` files are NOT a complete index of all hadith literature for each surah; they are the project specialist's chosen-representative citations. The ratio measures the GRADE-MIX OF CITATIONS THE PROJECT HAS MADE, not the GRADE-MIX OF ALL CLASSICAL HADITH ON THESE SURAHS.
- For some surahs (notably Q 2 al-Baqara), the auto-generated `Q002-citations.md` index records 126 hits across 9 books; the 04-hadith-corpus.md file then selectively cites prominent ones. Our tally is on the 04-hadith-corpus.md cites, not on the raw auto-index.
- The Q 2 specialist file is unusually well-developed; smaller-surah files are thinner. We will report the per-surah citation count alongside the ratio.

## Pre-commit attestation

Locked by SHA256. The run script will verify before computation.

EXPECTED_SHA256 will be computed after this file is finalized and embedded as the EXPECTED_SHA constant in `findings/phase-b-hypotheses/scripts/h-new-1780.py`. Any mismatch = fail-fast.
