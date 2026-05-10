---
id: H-NEW-1780
title: ṣaḥīḥayn vs Sunan hadith-grade distribution across project surahs
date: 2026-05-10
verdict: DESCRIPTIVE-CONFIRMED
prereg: findings/phase-b-hypotheses/prereg-h-new-1780-hadith-grade-distribution.md
prereg_sha256: 2c93112e6bcf275f348566d0be65cc76b07369ef82ab46c17fe11832e69a78bf
script: findings/phase-b-hypotheses/scripts/h-new-1780.py
data: findings/phase-b-hypotheses/csv/h-new-1780.json
phase: B+
---

# H-NEW-1780 — ṣaḥīḥayn vs Sunan hadith-grade distribution across project surahs

## Origin

The Q 22 al-Ḥajj specialist (file `/Users/grey/Downloads/quran/surahs/Q022-al-hajj/04-hadith-corpus.md` section 1.4) discovered that al-Bukhārī's *Kitāb Sujūd al-Qurʾān* (chapter id 17, ḥadīths 1036–1048) is SILENT on Q 22. The Sunnī-majority double-sajda position rests entirely on:

- Abū Dāwūd *Sunan* #1402 (chain through ʿAbd Allāh b. Munayn, classed *majhūl* by some)
- al-Tirmidhī *Sunan* #578 (Tirmidhī's own grade: *laysa bi-dhāka al-qawī* — "not particularly strong")
- Ibn Mājah *Sunan* #1057
- Mawqūf statements via ʿUmar and Ibn ʿUmar

This is a Sunan-grade (not ṣaḥīḥayn-grade) attestation. The Mālikī school dissents and does NOT break with the ṣaḥīḥayn because the ṣaḥīḥayn are silent on the question.

This finding empirically tests whether the rhetorical short-hand "the classical tradition holds X" is, across the project's per-surah hadith corpus, frequently a transmission of a Sunan-grade claim rather than a ṣaḥīḥayn claim.

## Hypothesis (pre-registered, direction-locked)

H1: **≥ 30% of the surah-specific classical ḥadīth citations indexed in the project's per-surah `04-hadith-corpus.md` files rest on Sunan-grade evidence** (Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, al-Dārimī *Sunan*, al-Bayhaqī, Ibn Ḥibbān, al-Ḥākim, Ibn Abī Shayba) and **NOT on ṣaḥīḥayn** (al-Bukhārī + Muslim).

Direction LOCKED before tally: `%sunan-grade ≥ 30%`.

## Method

1. Audited all **63** per-surah `04-hadith-corpus.md` files present on disk at lock-time.
2. For each file, extracted every (collection, identifier) tuple where the collection-mention is followed within 80 chars by an explicit ḥadīth-number, idInBook reference, chapter-id, or roman-numeral.volume reference (the standard Musnad/Mustadrak/Muṣannaf citation form).
3. Required the number to be unambiguously attributable to the nearest preceding collection-mention (i.e. no other collection name intervening).
4. De-duplicated by (surah, collection, identifier) so that multiple topical citations of the same ḥadīth within one file count once.
5. Classified each citation: ṣaḥīḥayn / Sunan-4 / Other.
6. Computed corpus-wide ratios and per-surah breakdowns.

## Results

**Headline ratio (locked direction)**:

| Grade | N | % of classified |
|:--|--:|--:|
| ṣaḥīḥayn (Bukhārī + Muslim) | 374 | **55.00%** |
| Sunan-4 (Tirmidhī + Abū Dāwūd + Nasāʾī + Ibn Mājah) | 245 | **36.03%** |
| Other (Mālik + Aḥmad + Dārimī + Bayhaqī + Ibn Ḥibbān + Ḥākim + Ibn Abī Shayba) | 61 | **8.97%** |
| **Sunan-grade combined (Sunan-4 + Other)** | **306** | **45.00%** |
| **Total classified** | **680** | 100% |

**Pre-registered direction**: `%sunan-grade ≥ 30%` → **MET** (observed 45.00%).

**Verdict**: **DESCRIPTIVE-CONFIRMED.** Across 63 per-surah hadith-corpus files in the project, 45.00% of identified surah-specific ḥadīth-citation instances rest on Sunan-grade evidence rather than ṣaḥīḥayn. This is well above the pre-registered 30% threshold and substantively important: it means that **nearly half** of the project's surah-claim-supporting ḥadīth citations are NOT in al-Bukhārī or Muslim. The Q 22 al-Ḥajj observation that prompted this test (al-Bukhārī silent on Q 22 sujūd; entire Sunnī-majority double-sajda position resting on Sunan-grade) is **representative of a corpus-wide pattern**, not an outlier.

## Per-collection ranking

| Collection | Grade | N | % of classified |
|:--|:--|--:|--:|
| al-Bukhārī | ṣaḥīḥayn | 274 | 40.29% |
| al-Tirmidhī | Sunan-4 | 136 | 20.00% |
| Muslim | ṣaḥīḥayn | 100 | 14.71% |
| Abū Dāwūd | Sunan-4 | 41 | 6.03% |
| Ibn Mājah | Sunan-4 | 40 | 5.88% |
| al-Nasāʾī | Sunan-4 | 28 | 4.12% |
| al-Dārimī | Other | 23 | 3.38% |
| Aḥmad | Other | 21 | 3.09% |
| Mālik | Other | 13 | 1.91% |
| al-Ḥākim | Other | 2 | 0.29% |
| Ibn Abī Shayba | Other | 1 | 0.15% |
| al-Bayhaqī | Other | 1 | 0.15% |

**Most-cited collection**: al-Bukhārī (274 = 40.29%) — confirming his canonical primacy in the project's specialist work.

**Second-most-cited collection**: al-Tirmidhī (136 = 20.00%) — a Sunan-grade collection. Tirmidhī alone exceeds Muslim (14.71%) in project citations. This is the strongest single-book empirical signal that the project's classical-claim corpus is substantively Sunan-leaning.

**Combined Sunan-4 (Tirmidhī + Abū Dāwūd + Nasāʾī + Ibn Mājah) = 245 (36.03%)** — by itself exceeding the 30% pre-registered threshold and exceeding Muslim's individual contribution.

## Per-surah distribution (selected)

**Sunan-grade-majority surahs** (>50% Sunan-grade): 21 of 63 = **33%**
**ṣaḥīḥayn-majority surahs** (<50% Sunan-grade): 27 of 63 = **43%**
**Balanced surahs** (=50%): 8 of 63 = **13%**
(Remaining: surahs with <3 citations, excluded from majority-analysis as below-statistical-resolution.)

### Heavy-Sunan surahs (highest %sunan-grade):

| Surah | sahihayn | sunan4 | other | total | %sunan-grade |
|:--|--:|--:|--:|--:|--:|
| Q 11 Hūd | 4 | 11 | 3 | 18 | **77.8%** |
| Q 46 al-Aḥqāf | 5 | 8 | 6 | 19 | **73.7%** |
| Q 22 al-Ḥajj | 5 | 6 | 7 | 18 | **72.2%** |
| Q 67 al-Mulk | 5 | 7 | 3 | 15 | **66.7%** |
| Q 17 al-Isrāʾ | 8 | 10 | 2 | 20 | **60.0%** |
| Q 18 al-Kahf | 11 | 8 | 4 | 23 | **52.2%** |

The Q 22 al-Ḥajj specialist's observation (72.2% Sunan-grade) is corroborated by Q 11 Hūd (77.8%), Q 46 al-Aḥqāf (73.7%), Q 67 al-Mulk (66.7%), Q 17 al-Isrāʾ (60%), and Q 18 al-Kahf (52.2%). **Five other surahs in the project sit in the same Sunan-heavy territory as Q 22**.

### Pure-Sunan-grade surahs (ZERO ṣaḥīḥayn citations in 04-hadith-corpus.md):

| Surah | sunan4 | other | Total |
|:--|--:|--:|--:|
| Q 40 Ghāfir | 1 | 0 | 1 |
| Q 51 al-Dhāriyāt | 9 | 0 | 9 |
| Q 99 al-Zalzala | 4 | 1 | 5 |

These three surahs have specialist hadith-corpus files that cite NO ṣaḥīḥayn ḥadīth for Q-specific claims. Q 51 al-Dhāriyāt is the most striking: 9 separate Sunan-grade citations and zero ṣaḥīḥayn. (Q 40 has only 1 total citation so is below statistical resolution.)

### Pure-ṣaḥīḥayn surahs (ZERO Sunan-grade citations):

| Surah | sahihayn |
|:--|--:|
| Q 48 al-Fatḥ | 22 |
| Q 1 al-Fātiḥa | 7 |
| Q 53 al-Najm | 3 |
| Q 96 al-ʿAlaq | 3 |
| Q 114 al-Nās | 3 |
| Q 49 al-Ḥujurāt | 2 |
| Q 35 Fāṭir | 1 |
| Q 112 al-Ikhlāṣ | 1 |

The most-cited "pure-ṣaḥīḥayn" surah is Q 48 al-Fatḥ (22 citations, all ṣaḥīḥayn) — the Ḥudaybiya-treaty surah, attested heavily in both Bukhārī and Muslim through abundant Madinan-period historical narration. Q 1 al-Fātiḥa is the second (7 all-ṣaḥīḥayn citations), reflecting the central liturgical role established in the ṣaḥīḥ-grade *Umm al-Kitāb* tradition.

## What this means for the project

1. **The methodological-vigilance concern is empirically substantiated.** When a project specialist file references "classical hadith for Q N," the citation has about a **45% chance of being Sunan-grade rather than ṣaḥīḥayn**. This is large enough to require active distinction in any future specialist write-up.

2. **Three pure-Sunan surahs identified.** Q 40 Ghāfir, Q 51 al-Dhāriyāt, Q 99 al-Zalzala have NO ṣaḥīḥayn citations in their current specialist files. For Q 51 in particular (9 Sunan citations, 0 ṣaḥīḥayn), the absence is striking and may itself be a finding — does the ṣaḥīḥayn corpus actually contain Q 51 citations that the project's specialist missed, or is the ṣaḥīḥayn corpus genuinely thin on Q 51?

3. **al-Tirmidhī's outsized role.** Tirmidhī alone supplies 20% of project citations — exceeding Muslim. This reflects Tirmidhī's *Sunan* being the canonical source for the fadāʾil-of-each-surah genre, which is the per-surah ḥadīth-corpus's natural backbone. But Tirmidhī himself frequently grades his own narrations as *ḥasan*, *ḥasan gharīb*, or weaker — the project's specialist files must carry this grading forward (as Q022-F-06 did) rather than asserting "classical hadith confirms X" without grade-specification.

4. **The "classical = ṣaḥīḥayn" rhetorical short-hand is empirically wrong** in 45% of project citations. Recommended project practice: when summarising a classical-claim's hadith basis, distinguish:
   - "ṣaḥīḥayn-attested" (al-Bukhārī or Muslim) — 55% of project citations
   - "Sunan-attested" (Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah) — 36%
   - "Post-canonical-Sunan-attested" (Mālik, Aḥmad, Dārimī, Bayhaqī, Ibn Ḥibbān, Ḥākim, Ibn Abī Shayba) — 9%

5. **Six surahs flagged for grade-specific re-audit**: Q 11, Q 17, Q 22, Q 46, Q 67, Q 18. These are the >50% Sunan-grade-cited surahs with substantial citation count (≥15). For each, the specialist's claim-strength on hadith-grounded findings should explicitly carry the Sunan-grade qualifier forward.

## NULL prominence (per Protocol §1.3)

Although the verdict is DESCRIPTIVE-CONFIRMED with respect to the pre-registered direction, the **majority of citations (55%) ARE ṣaḥīḥayn** — meaning the project's classical-claim corpus is NOT majority Sunan-grade. The headline reading "55% ṣaḥīḥayn" deserves equal prominence: the project's per-surah hadith corpora are anchored in the most-authentic Sunnī collections more often than not.

The pre-registered question was about whether the Sunan-grade share is **substantively large** (≥30%), not whether it is the majority. The 30% threshold was pre-locked precisely because the question is "does the rhetorical short-hand 'classical = ṣaḥīḥayn' work?" — and a 30% Sunan-share would already break that short-hand. The observed 45% breaks it decisively while leaving the ṣaḥīḥayn majority intact.

## Honest limits

- **The audit measures the GRADE-MIX OF CITATIONS THE PROJECT HAS MADE, not the GRADE-MIX OF ALL CLASSICAL HADITH ON THESE SURAHS.** The 63 per-surah hadith-corpus files are specialist-curated; a more-complete index of every ḥadīth touching every surah might yield a different ratio. The Q 2 auto-generated index records 126 hits across 9 books, but the 04-hadith-corpus.md file selectively cites prominent ones — our tally is on the curated, not the raw.
- The regex extraction may miss some citations (e.g., those phrased ambiguously) and may include some loose chapter-id references (e.g., "chapter id 17"). The chapter-id references are real anchors to project ḥadīth-claims but are coarser than ḥadīth-numbers.
- "Other" includes Bayhaqī, Ibn Ḥibbān, Ḥākim — three sources that some classical hadith-critics treat as approaching ṣaḥīḥayn-level reliability (Ibn Ḥibbān's collection is called *Ṣaḥīḥ Ibn Ḥibbān*). The pre-reg explicitly locked these as "Other-Sunan" using the strict canonical ṣaḥīḥayn definition (Bukhārī + Muslim only). Under a more inclusive ṣaḥīḥayn definition (adding Ibn Ḥibbān, Ḥākim), the ṣaḥīḥayn share would rise by a fraction of a percent — irrelevant to the headline.
- Q 002 al-Baqara, the most-developed file, contributes 23 deduped citations (19 ṣaḥīḥayn, 4 Sunan-4, 0 Other = 17.4% Sunan-grade). Q 2 is a high-citation surah and may pull the corpus-wide average toward ṣaḥīḥayn. The per-surah-breakdown above shows the underlying heterogeneity.
- The audit is a snapshot: as more surah-specialist files are written, the ratio will update. The pre-reg-locked direction-check is a one-shot test on the 2026-05-10 state of the project.

## Pre-commit attestation

- Pre-reg SHA256: `2c93112e6bcf275f348566d0be65cc76b07369ef82ab46c17fe11832e69a78bf` (verified at runtime).
- Direction-locked at `≥30% Sunan-grade` BEFORE tally; observed 45.00%. Direction MET.
- Sample size: 680 citation-instances across 63 surah files, exceeding the pre-registered 25-citation minimum by 27×.

## Cross-references

- **Q022-F-06** (parent finding, the prompting case): Sunan-grade attestation for Q 22 double-sajda; al-Bukhārī silent.
- **cross-finding-015-classical-scholarship-validation-pattern**: when classical scholarship aligns with empirical findings — this audit refines the cross-finding by distinguishing ṣaḥīḥayn-classical from Sunan-classical.
- **MASTER-FINDINGS-LEDGER**: H-NEW-1780 entry to be added under classical-claims-audit section.

## Replication queue

- **H-NEW-1780b**: independent re-tally by a different reader on the same 63 files (manual classification rather than regex extraction) — would test the regex's recall and precision against human gold-standard.
- **H-NEW-1780c**: re-tally restricted to surahs with ≥10 citation-instances (drops small-file noise; tests robustness of the 45% ratio).
- **H-NEW-1780d**: future re-run when project expands to all 114 surah-specialist files (the current 63 is a partial sample; some unfilled surahs may shift the ratio).
