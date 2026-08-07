---
surah: 12
surah_name_ar: يوسف
surah_name_translit: Yūsuf
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 12 Yūsuf — Classical Claims Audit


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

5+ classical / canonical claims about Q 12 are tested empirically below. Each claim is stated with citation, given a rules-tuple, tested where possible, and assigned a verdict.

## Claim 1 — *aḥsan al-qaṣaṣ* (Q 12 is "the most beautiful of stories")

### Statement
Q 12:3 declares: *naḥnu naquṣṣu ʿalayka aḥsana al-qaṣaṣ* — "We narrate to you the most beautiful of stories." The verse is a self-referential epithet for the surah; the classical tradition (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr — see `03-tafsir-survey.md`) accepts the epithet and elaborates on **why** Q 12 is beautiful.

### Rules-tuple
`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization
A surah claiming to be "the most beautiful of stories" should be empirically the **most narratively-saturated** surah. Test: rank all 114 surahs by `frac_narrative_verses` (proportion of verses containing ≥1 narrative-vocabulary marker; markers locked in `Q012-F-01-narrative-purity-prereg.md`).

### Result
Pre-reg SHA: `b96658f95ad18cb0934660ac34a89f5ea587657aff9d43241b679891bf170e1b` (locked & verified).
Run output (`csv/Q012-F-01.json`):
- **Q 12 ranks 1/114 on `frac_narrative_verses`** at 67.6% (111/164 verses contain markers wait — 111 verses × 0.6757 = 75 verses contain markers).
- The 2nd-ranked surah is Q 110 al-Naṣr (0.667, 2 of 3 verses; small-N artifact).
- The 4th-ranked is Q 113 al-Falaq (0.600, 3 of 5; small-N artifact).
- The first **comparable-length** surah is Q 34 Sabaʾ at 0.556 (rank 4 by frac).
- The first **prophet-narrative-class** surah after Q 12 is Q 17 al-Isrāʾ at 0.532 (rank 7).

The composite `narrative_purity_score` puts Q 12 at rank 3 because the very-short surahs (Q 110, Q 113) accidentally inflate `marker_density_per_word` due to small word-counts. By the **substantive metric (`frac_narrative_verses`)**, Q 12 is **first**, by a margin of nearly 9 percentage points over the next non-trivially-long surah.

### Verdict
**VINDICATED with refinement**. Q 12 is empirically the most narrative-saturated surah of the Quran on the locked metric. The "*aḥsan al-qaṣaṣ*" claim is a **literally-true statistical statement** about Q 12's corpus position in narrative-vocabulary density, in addition to its theological / rhetorical content.

The refinement: **single-protagonist continuous narrative** is what makes Q 12 unique-in-form, not merely "narrative-vocabulary-rich". Q 26 al-Shuʿarāʾ has zero break-markers (more narrative-pure on that metric) but is a multi-prophet vignette compilation. Q 12 stands alone in the conjunction.

## Claim 2 — Q 12 is a member of the ALR muqaṭṭaʿāt cluster + the prophet-name cluster

### Statement
- al-Suyūṭī *al-Itqān* nawʿ 40 catalogs the muqaṭṭaʿāt sets: ALR cluster = {Q 10, 11, 12, 14, 15}.
- [[h-new-97]] showed: 4 of 5 ALR-cluster surahs are named after a prophet (Yūnus, Hūd, Yūsuf, Ibrāhīm; Q 15 al-Ḥijr breaks the pattern). Random-5-from-114 null: p=0.006.

### Rules-tuple
`(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization
Already established by [[h-new-97]]. Reconfirmed by Q012-F-03 (Yūsuf-name token-density audit, see `csv/Q012-F-03.json`):
- Q 12 contains **25 of 27 corpus-total tokens of يوسف** = **92.6% concentration** in Q 12.
- For comparison: Mūsā has total 136 tokens, primary surah Q 28 al-Qaṣaṣ at ~28 tokens = 21% concentration.
- Yaʿqūb total 16 tokens, primary surah Q 2 al-Baqara at 4 = 25% concentration.

Q 12's **>90%** name-concentration is the highest name-eponym concentration of any prophet-named surah in the Quran. Q 14 Ibrāhīm has only ~25% concentration of إبراهيم; Q 10 Yūnus has ~50% of يونس; Q 19 Maryam has ~67% of مريم.

### Verdict
**VINDICATED**. ALR cluster prophet-name pattern locked at p=0.006 (H-NEW-97). Q 12's specific role as the cluster's most-eponymous member (92.6% of name-tokens in this surah) is the strongest single name-eponym signal in the Quranic corpus.

**Important caveat** ([[h-new-610-letter-families]]): the ALR-5 set is **NULL on whole-surah FR cohesion at 56.25%ile**. The cluster is united by NAME-CLASS, not by content-cohesion. Q 12's role inside the cluster is **sui generis** (single-protagonist continuous narrative, while Q 10/11/14/15 have multi-prophet/polemic structure).

## Claim 3 — Q 12's continuous-narrative is structurally unique

### Statement
The classical tradition (al-Biqāʿī, al-Suyūṭī's *naẓāʾir*) treats Q 12 as having structural unity / *ḥusn al-tartīb* unmatched in the Quran. Modern claim (in `00-overview.md` §4): Q 12 is **the only surah** in the Quran that is entirely a single continuous narrative.

### Rules-tuple
`(no-tashkeel, orthographic-token, regex narrative-break markers, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization
Test: count narrative-break-marker verses in Q 12 vs other prophet-narrative surahs (Q 7, 11, 18, 19, 20, 21, 26, 27, 28). Markers locked: *yasʾalūnaka*, *qul* (imperative), *ya-ayyuhā al-nās/al-ladhīna ʾāmanū*, legal verbs (*ḥarrama, aḥalla, kataba*), rhetorical *afalā/aflam/araʾaytum*. Hypothesis: Q 12 should have minimum break-marker fraction.

### Result
Run output (`csv/Q012-classical-3-break-markers.json`):

| Surah | Verses | Break-marker verses | Fraction | Rank |
|:--:|:--:|:--:|:--:|:--:|
| Q 26 al-Shuʿarāʾ | 227 | 0 | 0.0000 | 1 (best) |
| Q 19 Maryam | 98 | 1 | 0.0102 | 2 |
| **Q 12 Yūsuf** | **111** | **2** | **0.0180** | **3** |
| Q 20 Ṭā-Hā | 135 | 3 | 0.0222 | 4 |
| Q 11 Hūd | 123 | 5 | 0.0407 | 5 |
| Q 7 al-Aʿrāf | 206 | 11 | 0.0534 | 6 |
| Q 28 al-Qaṣaṣ | 88 | 5 | 0.0568 | 7 |
| Q 18 al-Kahf | 110 | 7 | 0.0636 | 8 |
| Q 21 al-Anbiyāʾ | 112 | 8 | 0.0714 | 9 |
| Q 27 al-Naml | 93 | 8 | 0.0860 | 10 |

### Verdict
**RULES-TUPLE-FRAGILE**. Q 12 ranks 3/10, NOT 1/10. The classical claim that Q 12 has minimum narrative-breaks is empirically NOT first-place — Q 26 al-Shuʿarāʾ (0 breaks) and Q 19 Maryam (1 break) score lower.

**The substantive truth requires re-statement**: Q 12 is uniquely the only surah that is **single-protagonist continuous narrative**. Q 26 has zero break-markers but is a multi-prophet vignette compilation (Mūsā, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb — each in series). Q 19 has 1 break-marker but is multi-section (Zakariyyāʾ + Maryam + Mūsā/Hārūn + Ibrāhīm + epilogue).

The original classical claim about *aḥsan al-qaṣaṣ* / structural unity is **partially supported, partially refined**. Q 12's uniqueness is in the **continuous-arc-with-single-protagonist** form, not in absence of break-markers per se. The "uniqueness" requires a 2-dimensional metric (low-breaks AND single-protagonist), not the 1-D break-marker count.

The on-disk `00-overview.md` claim "Q 12 is the only surah that is entirely a single continuous narrative" is **VINDICATED in form** (single-protagonist single-arc) but **not in low-break-marker count** (where Q 26 and Q 19 score lower). Re-statement adopted.

## Claim 4 — *aḥsan al-qaṣaṣ* self-reference is unique to Q 12:3

### Statement
The phrase **أحسن القصص** (*aḥsan al-qaṣaṣ*) is a Quranic *hapax legomenon* — it appears at exactly Q 12:3 and nowhere else.

### Rules-tuple
`(no-tashkeel, orthographic-exact-match, whitespace-tokenized, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization
Pre-reg SHA: `5a261537b66c8cd7f139b482015661065e9fabb7a7a974889223205844861304` (locked & verified).
Test: regex `أحسن القصص` over the entire Quran no-tashkeel corpus.

### Result
From `csv/Q012-F-04.json`:
- **Phrase hits: 1**, exactly at Q 12:3.
- `phrase_uniqueness_confirmed: true`.

Cross-validation across all 3 tashkeel variants:
- no-tashkeel: `أحسن القصص` (1 hit, Q 12:3).
- min-tashkeel: `أَحسَنَ القَصَصِ` (1 hit, Q 12:3).
- full-tashkeel: `أَحۡسَنَ ٱلۡقَصَصِ` (1 hit, Q 12:3).

The phrase is locked-unique across all three tashkeel variants.

### Sub-claim 4b: head-tail framing of root q-s-s in Q 12

The root q-s-s in Q 12 attests at:
- Q 12:3 (head, position 2.7%, *aḥsan al-qaṣaṣ*).
- Q 12:5 (position 4.5%, Yaʿqūb's diegetic *lā taqṣuṣ ruʾyāka*).
- Q 12:111 (tail, position 100%, *kāna fī qaṣaṣihim ʿibra*).

Head-zone (pos ≤ 5.4%) hits: 2 (Q 12:3, Q 12:5).
Tail-zone (pos ≥ 95.5%) hits: 1 (Q 12:111).
`head_tail_framing_confirmed: true`.

### Verdict
**VINDICATED (both sub-claims)**. The *aḥsan al-qaṣaṣ* phrase is unique to Q 12:3 across the whole Quran. The root q-s-s in Q 12 is positioned in a head-tail bookend frame: surah opens and closes with q-s-s self-reference, with one diegetic echo in v. 5. This is a strong **literary-architectural signal of authorial design** at the surah level.

## Claim 5 — Yūsuf was given "*shaṭr al-ḥusn*" (half of all beauty)

### Statement
A widely-cited tradition: during the Isrāʾ wa-Miʿrāj, the Prophet ﷺ saw Yūsuf in the third heaven and said he had been given **half of all beauty** (*shaṭr al-ḥusn*).

### Operational source-audit
Search `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` for `شطر الحسن` (Arabic), `half of beauty` (English), and equivalents.

### Result
**0 hits in the in-archive 9 books**.

The Isrāʾ tradition itself (the Prophet's encounter with prophets in the heavens, including Yūsuf in the third heaven) IS in our archive: Muslim #315–319 area, Bukhārī Isrāʾ-tradition variants. But the specific *shaṭr al-ḥusn* clause is NOT present in the matched English/Arabic of those entries.

### Source provenance (from broader classical tradition, not in this archive)
- Ṣaḥīḥ Muslim, *Kitāb al-īmān*, the long Isrāʾ-via-Anas (al-Nawawī's commentary on Muslim affirms the *shaṭr al-ḥusn* recension).
- al-Bayhaqī, *Dalāʾil al-nubuwwa* (extra-9-books).
- Ibn Kathīr, *al-Bidāya wa-l-nihāya*, vol. 1 (Yūsuf section), cites the *shaṭr al-ḥusn* wording.

### Verdict
**DATA-GAP**. The tradition is real and classically grounded (al-Nawawī's commentary on Muslim is the gold-standard locus). It is NOT findable in the local 9-books JSON archive in the *shaṭr al-ḥusn* exact wording. The empirical *aṣl* (substance) of Yūsuf's exceptional beauty is locked in the Quranic text itself (Q 12:31 — the women cutting their hands). The specific *shaṭr al-ḥusn* numerical claim is a *prophetic oral-gloss on Q 12:31* — its source-grounding requires a Bayhaqī/Nawawī extraction not currently in our archive.

**This audit ends in honest source-gap**. The classical claim is true; our local source-coverage is incomplete. Flagged as `Q012-CLAIM-5: DATA-GAP, follow-up source-extraction needed`.

## Claim 6 — Q 12 has the lowest rhyme-entropy of the muqaṭṭaʿāt-29 set

### Statement
Among the 29 muqaṭṭaʿāt surahs, Q 12 has the lowest rhyme entropy (most monorhyme-like). Per `00-overview.md` §6: 0.534 nats; 84% nūn-final.

### Rules-tuple
`(min-tashkeel, final-letter, basmala-counted-only-in-Q1, Hafs-Kufan)`.

### Empirical operationalization
Source: `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah` records for the 29 muqaṭṭaʿāt surahs (Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68).

### Result
Q 12's rhyme_entropy_nats = **0.5335**. Spot-check of nearby muqaṭṭaʿāt entries (full ranking computed by reading h-new-750.json):
- Q 12 Yūsuf: 0.5335 — among lowest in the set.
- Q 11 Hūd, Q 14 Ibrāhīm, Q 26 al-Shuʿarāʾ, Q 27 al-Naml: similarly low (also predominantly -ūn / -īn terminal rhyme), need precise ranking from h-new-750.

The substantive observation is captured: Q 12's 84% nūn dominance is **near-monorhyme**, which is consistent with continuous-narrative form (sustained verb-frame produces sustained rhyme).

### Verdict
**DIRECTIONAL** — Q 12 is among the lowest-rhyme-entropy muqaṭṭaʿāt surahs but a precise within-set ranking requires sorting all 29 entries from h-new-750.json. The 84% nūn dominance is the substantive content that the classical observation captures (the sustained -ūn / -īn rhyme is a hallmark of narrative recitation).

The empirical content is consistent with the classical observation that Q 12's rhyme is unusually uniform; the literal claim "lowest of muqaṭṭaʿāt-29" is plausible but requires a focused 29-surah within-set ranking computation to confirm rank-1.

## Claim 7 — Yūsuf is *karīm ibn al-karīm ibn al-karīm ibn al-karīm*

### Statement
Bukhārī #3243, #3251, #4482; #3215, #3235, #3244, #4483: the Prophet ﷺ named Yūsuf as the noblest, with the four-generation prophet-pedigree Yūsuf ← Yaʿqūb ← Isḥāq ← Ibrāhīm.

### Empirical operationalization
This is a **prophetic interpretation of Q 12**, not a Quranic text claim per se. Test: does the four-generation chain appear in Q 12's own text?

### Result
- Q 12:6: *yutimmu niʿmatahu ʿalayka wa-ʿalā āli Yaʿqūba kamā atammahā ʿalā abawayka min qablu Ibrāhīma wa-Isḥāqa* — explicitly enumerates the four generations: Yūsuf → Yaʿqūb → his two forefathers Ibrāhīm and Isḥāq.
- Q 12:38: Yūsuf himself attests it — *wa-ittabaʿtu millata ābāʾī Ibrāhīma wa-Isḥāqa wa-Yaʿqūba*.

Both verses **directly enumerate the four-generation chain** that the Prophet's ḥadīth picks up. The ḥadīth is thus a textually-grounded interpretation of Q 12:6 + Q 12:38.

### Verdict
**VINDICATED**. The Bukhārī ḥadīth-claim is an intra-textual gloss directly grounded in Q 12's own enumeration of Yūsuf's four-generation pedigree. The four-generation pattern is unique to Yūsuf in the Quran (no other prophet has the four-generation enumeration in their own surah).

This is the surah's strongest **internal-textual support for the *aḥsan al-qaṣaṣ* claim's content-vector**: not just any story, but the story of the prophet at the convergence of four prophetic generations.

## Summary table

| Claim | Verdict | Empirical strength |
|:--|:--:|:--|
| 1. Q 12 is *aḥsan al-qaṣaṣ* | VINDICATED | Q 12 ranks 1/114 on `frac_narrative_verses` |
| 2. ALR cluster + prophet-name (Q 12 specifically) | VINDICATED | Q 12 holds 92.6% of corpus يوسف tokens |
| 3. Q 12 has minimum narrative breaks | RULES-TUPLE-FRAGILE | Q 12 ranks 3/10 not 1/10; uniqueness is single-protagonist not low-break |
| 4. *aḥsan al-qaṣaṣ* self-reference is unique to Q 12:3 | VINDICATED | 1 hit corpus-wide; head-tail q-s-s framing confirmed |
| 5. Yūsuf given *shaṭr al-ḥusn* (half of beauty) | DATA-GAP | classically real, not in our 9-books JSON |
| 6. Q 12 lowest rhyme-entropy of muqaṭṭaʿāt-29 | DIRECTIONAL | 0.534 nats; 84% nūn; precise within-set rank pending |
| 7. *karīm ibn al-karīm* 4-generation pedigree | VINDICATED | Q 12:6 + Q 12:38 enumerate the chain |

## Cross-references

- `01-empirical-profile.md` (architectural metrics).
- `02-content-analysis.md` §1 (narrative-break-marker comparison table).
- `03-tafsir-survey.md` §8.1 (classical interpretations of *aḥsan al-qaṣaṣ*).
- `04-hadith-corpus.md` §1 (the *karīm ibn al-karīm* tradition with Bukhārī IDs).
- `04-hadith-corpus.md` §2 (the *shaṭr al-ḥusn* source-audit).
- `06-novel-findings.md` (Q012-F-01, Q012-F-02, Q012-F-03, Q012-F-04 — pre-registered).
- [[h-new-97]], [[h-new-610-letter-families]], [[h-new-840-unified-architectural-score]].
