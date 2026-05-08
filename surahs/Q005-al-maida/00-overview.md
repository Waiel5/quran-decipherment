---
surah: 5
surah_name_ar: المائدة
surah_name_translit: al-Māʾida
surah_name_english: "The Table-Spread"
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — al-Suyūṭī LATE-CHRONOLOGY claim VINDICATED (rev #112 / Nöldeke #114); 5 pre-registered novel tests (1 VINDICATED, 1 DIRECTIONAL, 3 NULL); the late-Medinan signature triangulation is a striking dissociation NULL — Q 5 is architecturally near-identical to Q 2 (early-Medinan-ṭiwāl head) on all 4 axes despite being canonically the last-or-near-last surah revealed.
---

# Q 5 al-Māʾida — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 5 | canonical |
| Arabic name | المائدة | `quran-text/quran-no-tashkeel.json` |
| Transliteration | al-Māʾida | canonical |
| English meaning | "The Table-Spread" / "The Banquet" | from Q 5:112-115 episode |
| Verse count | **120** | Hafs-Kufan; `data/hafs-verse-counts.tsv` |
| Position in mushaf | 5 (al-sabʿ al-ṭiwāl, 5th of 7) | canonical |
| Type | Medinan (whole) | classical consensus |
| Position in revelation order — Egyptian Standard | **112 / 114** (third-to-LAST surah revealed) | `data/revelation-order.csv` |
| Position in revelation order — Nöldeke | **114 / 114** (LAST surah revealed) | `data/revelation-order.csv` ; al-Suyūṭī *al-Itqān* nawʿ 1 |
| Word count (no-tashkeel) | **3,047** | computed |
| Letter count (no-tashkeel, alpha-only) | 12,206 | computed |
| Unique-root count (QAC v0.4) | 422 | computed |
| Unique-lemma count (QAC v0.4) | 684 | computed |
| **Bismala status** | present | canonical |
| Opening | يا أيها الذين آمنوا أوفوا بالعقود — "O you who believe, fulfill the covenants" | direct legal vocative |

## 2. Classical names

- **al-Māʾida** (المائدة) — "The Table-Spread"; the standard name. Refers to the table-from-heaven episode at Q 5:112-115.
- **al-ʿUqūd** (العقود) — "The Covenants"; from the opening word *awfū bi-l-ʿuqūd* (Q 5:1). Used by al-Ṭabarī (*Jāmiʿ al-bayān* on Q 5:1) and al-Qurṭubī (*al-Jāmiʿ li-aḥkām al-Qurʾān* on Q 5:1).
- **al-Munqidha** (المنقذة) — "The Rescuer"; from a tradition that whoever recites it well is rescued from punishment (mentioned by al-Suyūṭī, *al-Durr al-manthūr* on Q 5).

## 3. Chronological position — the LAST-revealed-surah debate

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (in chronology of revelation) records the famous tradition of ʿĀʾisha (via Asmāʾ bint Yazīd, in al-Ḥākim and al-Tirmidhī) that *sūrat al-māʾida* was the LAST surah revealed. Ibn ʿAbbās is recorded by al-Suyūṭī as supporting the same position. The Egyptian Standard chronology (Nasr's mushaf preface, used in `data/revelation-order.csv`) places Q 5 at rev #112 — third-from-last — with Q 9 at #113 and Q 110 at #114. Nöldeke's reconstruction places Q 5 at #114 — the absolute LAST.

The competing traditions:
- ʿĀʾisha (al-Tirmidhī #3063 ≈ "Sūrat al-Māʾida is the last surah revealed; what you find in it of the lawful, take as lawful, and what of the unlawful, deem unlawful").
- Ibn ʿAbbās (multiple isnāds).
- al-Bayhaqī's harmonization: Q 9 al-Tawba was the last to be revealed in BLOCKS (because it includes Q 9:128-129, "the very last verses" per Ubayy b. Kaʿb); Q 5 was the last surah revealed as a structural unit before any later additions to other surahs.

al-Suyūṭī's harmonization (*al-Itqān*, nawʿ 1): each Companion reported what reached them; no contradiction. **In no version is Q 5 EARLY**; it is uniformly LATE-Medinan.

## 4. Q 5:3 — the "completion of religion" verse

Q 5:3 contains the famous *al-yawma akmaltu lakum dīnakum wa-atmamtu ʿalaykum niʿmatī wa-raḍītu lakumu l-islāma dīnan* ("This day I have perfected your religion for you, completed My favor upon you, and chosen Islam for you as religion"). al-Bukhārī ḥadīth #45 (kitāb al-īmān) records ʿUmar ibn al-Khaṭṭāb identifying this as revealed at ʿArafāt on the Day of Hajj, which coincided with a Friday — specifically the Farewell Pilgrimage (ḥajjat al-wadāʿ) of 10 AH. al-Tirmidhī #3043 records the same context.

This makes Q 5:3 a candidate for "the last verse revealed" (one of four classical candidates per al-Suyūṭī *Itqān* nawʿ 8: Q 9:128-129, Q 4:176, Q 2:281, Q 5:3). al-Suyūṭī's harmonization holds that the four candidates report different "lasts" — Q 5:3 is the last verse of legal-establishment, while Q 2:281 is the last of inheritance-rules, etc.

Empirical novel-finding **Q005-F-03** locks Q 5:3 as the **corpus-RANK-1 verse-level density** of the 5-cluster {dīn, niʿmah, k-m-l, t-m-m, r-ḍ-w} (5 of 5 distinct cluster-members, p_perm = 0.0001 < α_bon = 0.01). This is the strongest empirical "completion-of-religion" signature in the corpus.

## 5. Opening formula

Q 5 opens with the legal-vocative *yā ayyuhā l-ladhīna āmanū awfū bi-l-ʿuqūd* — "O you who believe, fulfill the covenants." This is the **legal-imperative** opening pattern, distinct from the al-ḥamd type (Q 1, 6, 18, 34, 35), the muqaṭṭaʿāt type (Q 2, 3, 7, ...), or the tasbīḥ type (Q 17, 57, 59, 61, 62, 64, 87). Q 4 also opens with *yā ayyuhā* (al-nās); Q 5's *yā ayyuhā l-ladhīna āmanū* is the proximate-believer-vocative, which is the most common vocative form in Q 5 (it occurs 16 times in 120 verses).

## 6. Length classification

al-sabʿ al-ṭiwāl (the seven long surahs): Q 2, 3, 4, 5, 6, 7, with Q 8 + Q 9 sometimes counted as the seventh. Q 5 (120 verses, 3,047 words) is the SHORTEST of the al-sabʿ al-ṭiwāl in word-count, BUT is uniformly classified as a member by all classical lists (al-Suyūṭī *Itqān* nawʿ 9, al-Zarkashī *al-Burhān* on the seven longs).

## 7. Rhyme structure

Final-letter distribution across 120 verses (computed from `quran-no-tashkeel.json`):
- ن (nūn): 80 verses (66.7%) — dominant rāwī
- م (mīm): 24 (20.0%)
- ر (rāʾ): 7 (5.8%)
- ب (bāʾ): 4 (3.3%)
- ل (lām): 3 (2.5%)
- د (dāl): 2 (1.7%)

Rhyme entropy (Shannon, nats): **1.0318** — among the highest in the al-sabʿ al-ṭiwāl. Compare: Q 2 = 0.972, Q 3 = 0.872, Q 4 = 0.690, Q 9 = 0.812. Q 5 is the **rhyme-MOST-DIVERSE** of the al-sabʿ al-ṭiwāl on Shannon entropy. (Source: H-NEW-750 `mean_content_distance` and rhyme stats per `findings/phase-b-hypotheses/csv/h-new-750.json`.)

## 8. Empirical architectural profile

See `01-empirical-profile.md` for full integration. Headline:
- **UAS rank**: **66 / 114** (mid-pack). H-NEW-840 `csv/h-new-840.json`.
- **Outlier-strength Δ%ile**: **−5.68 pp** (WEAK_ANCHOR — Q 5 is a content-COHESION-CONTRIBUTOR within the al-sabʿ al-ṭiwāl, not a content-disruptor). H-NEW-590 `csv/h-new-590.json`.
- **iʿjāz signature sig_A**: −1.060 (rank 86/114) — moderate anti-iʿjāz; sig_B = +0.106 (rank 55/114) — neutral. H-NEW-750.
- **Mean FR-content distance**: 1.079 (rank ~73/114, slightly above mean — but inside the al-sabʿ al-ṭiwāl cluster). H-NEW-750.
- **5 nearest FR-roots neighbors of Q 5**: **Q 2 (0.696), Q 3 (0.698), Q 4 (0.778), Q 9 (0.836), Q 6 (0.860)** — every one of the 5 nearest neighbors is a member of the al-sabʿ al-ṭiwāl (or its Medinan satellite Q 9). This is a tightly clustered Medinan-legal architectural signature. (H-NEW-111 distance matrix.)
- **Q 4 → Q 5 canonical-adjacency cost**: 0.0000 — rank 102/113 (essentially **FREE**; the Q 4-to-Q 5 transition is one of the cheapest in the entire mushaf). H-NEW-720.
- **Q 5 → Q 6 canonical-adjacency cost**: 0.0051 (0.51%) — rank 72/113 (cheap). H-NEW-720.

**Architectural interpretation**: Q 5 is the **architectural twin of Q 2-Q 4** in FR-roots and signature-axes. It is NOT an outlier; it is a cluster-anchor. This is despite Q 5's late-revelation chronology — a striking dissociation between **chronology** (LATE) and **mushaf-architecture** (EARLY-Medinan-ṭiwāl-cluster). See novel-finding Q005-F-05 for the formal triangulation.

## 9. Quick content structure

- **vv. 1-11**: Opening covenants — fulfillment of contracts, food laws, Q 5:3 completion-of-religion declaration, Q 5:6 ablution-establishing verse.
- **vv. 12-32**: Israelite covenant; Christian covenant; addressing the People-of-the-Book; Cain-and-Abel narrative (vv. 27-32) — the FIRST appearance of *banī Adam* murder narrative in mushaf order.
- **vv. 33-50**: Punishments and laws; theft punishment (Q 5:38); Tawrāh + Injīl as guidance; *judgment-by-what-Allāh-revealed* refrain (Q 5:44, 45, 47); the *manhāj* + *sharʿa* verse (Q 5:48).
- **vv. 51-86**: Walāyah polemic (Q 5:51 *lā tattakhidhū l-yahūda wa-l-naṣārā awliyāʾ*; Q 5:55 *innamā waliyyukumu llāhu wa-rasūluhu*); tablīgh verse Q 5:67; Trinity refutation (Q 5:72-77); ḥawāriyyūn praise (Q 5:82-85).
- **vv. 87-93**: Food permissions; oath-expiation (Q 5:89); intoxicants and gambling prohibition (Q 5:90-91); maysir + anṣāb + azlām.
- **vv. 94-104**: Hunting in iḥrām; Kaʿba; pre-Islamic dietary superstitions (baḥīrah, sāʾiba, waṣīla, ḥām).
- **vv. 105-108**: Will-witness verse (long-verse legal block).
- **vv. 109-120**: Closing — Day-of-Resurrection scene with prophets; **māʾida-from-heaven episode (Q 5:112-115)**; ʿĪsā's Day-of-Resurrection denial of self-deification (Q 5:116-118); final closing on God's dominion.

## 10. Cross-references

- [[h-new-111-fisher-rao-information-geodesic|H-NEW-111]] — Q 5's 5 nearest neighbors are Q 2, Q 3, Q 4, Q 9, Q 6.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 5 is a WEAK_ANCHOR (Δ%ile −5.68); contributes COHESION to the al-sabʿ al-ṭiwāl.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 4→Q 5 is rank 102/113 (essentially free); Q 5→Q 6 rank 72/113 (cheap). The mushaf pays NEGLIGIBLE TSP cost to seat Q 5 in its canonical position.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 5 sig_A rank 86, neutral sig_B; rhyme-entropy = 1.032 (rank ≈ top-quartile).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 5 UAS rank 66/114 (mid-pack).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 5 occupies the *al-sabʿ al-ṭiwāl* head-pole architecture (low rhyme-entropy variance, high content-cohesion).
- [[Q002-al-baqara/00-overview|Q 2 al-Baqara]] — architectural twin (FR-distance 0.696, near-identical signature vectors).
- [[Q009-al-tawba/00-overview|Q 9 al-Tawba]] — chronological twin (rev #112 vs #113), architectural OPPOSITES (Q 9 UAS rank 4, outlier; Q 5 UAS rank 66, anchor).
- [[Q004-al-nisa/00-overview|Q 4 al-Nisāʾ]] — predecessor in mushaf, near-zero adjacency cost (rank 102/113); legal-Medinan architectural cohort.

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 5 pre-registered novel findings (Q005-F-01..F-05) — see `06-novel-findings.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
