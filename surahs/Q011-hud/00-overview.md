---
surah: 11
surah_name_ar: هود
surah_name_translit: Hūd
surah_name_english: "Hud (the prophet)"
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 9-file Wave-E investigation produced 2026-04-28; classical-claims audit produced 5 verdicts (3 VINDICATED / 1 RULES-TUPLE-FRAGILE / 1 NULL); 4 novel pre-registered tests landed (verdicts in 06-novel-findings.md); key Q 11 finding: Q 11 is the corpus's MAXIMUM-prophet-density surah (7 prophets in 123 verses, density 0.057 prophets/verse) — the classical Tirmidhī "Hūd and its sisters" tradition's empirical anchor — but is empirically NULL on outlier-strength (delta_pct=-4.88pp, p=0.20, h-new-590) AND NULL on canonical-adjacency (Q10-Q11 cost rank 82/113, Q11-Q12 rank 77/113), placing Q 11 in the *iʿjāz-al-fawāṣil-pure*-leaning rather than *Structural-twin-pair* cell of cross-finding-026; Q 11's content axis is NULL on whole-surah FR-roots cohesion with ALR cluster (h-new-600 NULL at 56.25%ile) yet locally pulled-in (mean to ALR siblings 0.904 vs 1.046 to non-ALR — Δ=0.142, t-test post-hoc).
---

# Q 11 Hūd — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 11 | canonical |
| Arabic name | هود | canonical |
| Transliteration | Hūd | canonical |
| English meaning | "Hūd (the prophet of ʿĀd)" | classical |
| Verse count | 123 | Hafs-Kufan (`data/hafs-verse-counts.tsv`) |
| Position in mushaf | 11 | canonical |
| Type | Meccan (mostly); per `data/revelation-order.csv` row 52 | `data/revelation-order.csv` |
| Position in revelation order (al-Suyūṭī chronology) | **52 of 114** (immediately after Q 10 Yūnus rev #51, immediately before Q 12 Yūsuf rev #53) | `data/revelation-order.csv` |
| Word count (no-tashkeel) | **2,083** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel) | **7,954** | computed |
| Opening | الر ۚ كتاب أحكمت آياته ثم فصلت من لدن حكيم خبير — "ALR. A Book whose verses were rendered firm, then made distinct, from One Wise, All-Aware." | muqaṭṭaʿāt + book-reference (Q 11:1) |
| Bismala | counted as part of v.1 only when conventionally prefixed; rules-tuple default = NOT counted (basmala-counted-only-in-Q1) | rules tuple |

al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, on the **maqṣūd** (intent) of Q 11 (`data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt` — searchable by surah-marker سورة هود): the surah's intent is to demonstrate that the **Book** (al-kitāb) is from God, by means of a sequence of seven prophet-warning-narratives whose collective testimony establishes the Quranic warning's divine origin. Where Q 10 Yūnus argues the Book's divinity through the *exception* (the only people who repented in time), Q 11 Hūd argues it through *iteration* — seven historical confirmations in compressed form.

## 2. Classical names and identifications

- **Hūd** (هود) — the canonical name; the prophet of ʿĀd, mentioned at vv. 50-60 (his block) and named at v. 53 in direct address, v. 60 in narrator's report, and v. 89 in Shuʿayb's catalog of past warner-peoples. The token هود occurs **3× in Q 11** out of **4× total in the Quran** (75% concentration; the only other occurrence is in Q 26:124 within a separate ʿĀd-block). See `quran-text/quran-no-tashkeel.json`, computed.
- **Sūrat Hūd wa-akhawātihā** ("Hūd and its sisters") — al-Tirmidhī, *al-Jāmiʿ al-ṣaḥīḥ*, ḥadīth #3297, graded ḥasan-gharīb: the Prophet (peace be upon him) said *"Hūd and its sisters made me grey before [my] time"* (شيبتني هود وأخواتها). The "sisters" are conventionally identified by the commentators as Q 56 al-Wāqiʿa, Q 77 al-Mursalāt, Q 78 al-Nabaʾ, Q 81 al-Takwīr — surahs of catastrophic-eschatological imagery. Some commentators (e.g., Ibn Kathīr, see `data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt` Q 11 section) include Q 99 al-Zalzala. The hadith-citation is empirically tested in 04-hadith-corpus.md and 05-classical-claims-audit.md.

## 3. Opening formula — muqaṭṭaʿāt + book-affirmation

Q 11 opens with the **ALR muqaṭṭaʿāt** + a distinctive book-affirmation: *"A Book whose verses were rendered firm (uḥkimat), then made distinct (fuṣṣilat), from One Wise, All-Aware."* This is the cross-finding-008 pattern (muqaṭṭaʿāt → book-reference) but with a unique pair of verbs — *iḥkām* (locking-in) followed by *tafṣīl* (distinguishing/articulating) — that classical commentators (al-Rāzī, al-Qurṭubī, al-Zamakhsharī) read as a meta-statement on Quranic structure: the Book is BOTH a sealed unity AND an articulated multiplicity. Within the ALR family, this opening is closest in form to Q 10:1 (*tilka āyātu al-kitābi al-ḥakīm*) and Q 15:1 (*tilka āyātu al-kitābi wa-qurʾānin mubīn*) but uses the verbal pair distinctively.

Q 11 is a member of the **ALR letter-family cluster** = {Q 10, Q 11, Q 12 Yūsuf, Q 14 Ibrāhīm, Q 15 al-Ḥijr}. [[h-new-600-letter-families|H-NEW-600/610]] found ALR-5 NULL on whole-surah FR-cohesion (56.25%ile, above corpus-median dispersion). [[h-new-97-name-letter-joint|H-NEW-97]] found 4/5 PROPHET_PERSON name-class membership (p_mc=0.0059). Q 11 is one of the four PROPHET_PERSON members.

## 4. Why is Q 11 named after Hūd?

This is non-trivial. Q 11 is the canonical **multi-prophet anthology**: 7 prophets are explicitly named (Nūḥ, Hūd, Ṣāliḥ, Ibrāhīm, Lūṭ, Shuʿayb, Mūsā — see verse-locations under §8 below). Of these, Hūd is NOT the most narratively expansive (Nūḥ's block at vv. 25-49 is the longest single narrative; Mūsā is mentioned as bookend at v. 17 and v. 96-110). Yet the surah is named after Hūd.

al-Biqāʿī's reading (`biqai-nazm-al-durar.openiti.raw.txt`, surah-marker سورة هود): the surah is named after Hūd because his is the **central** narrative — the surah is structured as a chiastic ring with Hūd's block at vv. 50-60 mid-corpus (123 verses, midpoint at v. 61-62; Hūd's narrative ends at v. 60). al-Biqāʿī treats Hūd's confrontation with ʿĀd as the *paradigmatic* warner-confrontation that the surrounding narratives variantly replay.

**Classical "sisters" tradition**: al-Tirmidhī #3297 (graded ḥasan-gharīb) — the surah's name has a status independent of pure narrative-density: the Prophet himself made it the head-name of a 4-5 surah cluster of severity-of-warning. This is a corpus-singular **prophet-named-cluster-head** function — similar to how Q 1 al-Fātiḥa is *umm al-Kitāb* but not because it dominates content. Q 11 is the head of a **warning-cluster** as Q 1 is the head of the corpus.

**Empirical**: Hūd-token concentration 75% (3 of 4 corpus occurrences in Q 11). Compare Yūnus-token 50% in Q 10, Yūsuf-token 92.6% in Q 12, Ibrāhīm-token 1.61% in Q 14. Q 11 is INTERMEDIATE between Q 10 (thesis-named) and Q 12 (narrative-named) on this axis — Q 11 is **anthology-named-by-block-eponym**, a third type.

## 5. Length classification

123 verses, 2,083 words, 7,954 letters — **mid-length Meccan; longer than Q 10 Yūnus (109v) and Q 14 Ibrāhīm (52v); shorter than Q 12 Yūsuf (111v but more verses)**. Q 11 is in *al-miʾīn* (the surahs that exceed 100 verses) per al-Biqāʿī's reckoning. al-Suyūṭī's *al-Itqān* nawʿ on Quran division places Q 11 at the boundary between *al-sabʿ al-ṭiwāl* and *al-miʾīn* (this designation depends on whether al-Anfāl + Barāʾa are joined).

Position s=11 places Q 11 deep in the head-mushaf zone, before the s=50 Hijra-kink. Per the [[cross-finding-026-iʿjāz-architecture|iʿjāz architecture]] laws, Q 11 sits in the d̄_content ≈ 0.96 (uncompressed-tail) region. Computed mean FR-content distance = **1.041** (slightly elevated; see 01-empirical-profile.md), confirming the head-mushaf prediction.

## 6. Rhyme structure

Final-letter distribution across 123 verses (computed from `quran-text/quran-min-tashkeel.json`):

| Final letter | Count | % |
|:--|:-:|:-:|
| ن (nūn) | 56 | **45.5%** |
| د (dāl) | 23 | 18.7% |
| ب (bāʾ) | 13 | 10.6% |
| ر (rāʾ) | 11 | 8.9% |
| م (mīm) | 5 | 4.1% |
| Other 8 letters | 15 | 12.2% |

**Rhyme entropy (Shannon, nats): 1.737** — per [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] (`csv/h-new-750.json` per_surah[Q=11]: rhyme_entropy_nats=1.7365). z-rhyme-entropy = +1.75 (high — well above corpus mean). This is **MULTI-RHYME** territory — Q 11 is the most rhyme-diverse of the ALR-cluster surahs (compare Q 10 at 0.358, Q 15 at 0.538). The dominance is on nūn (typical fāṣila) + dāl (the *-ūd* / *-īd* / *-ād* endings of the prophet-warning-passages where the warnings end in *-ʿūd*, *-ḥamīd*, etc.) — a phonologically meaningful diversity tied to the sequence of warner-blocks each ending in a Day-of-Reckoning warning.

## 7. Empirical architectural profile (preview — see 01-empirical-profile.md)

- **UAS rank**: **88/114** (UAS = −1.457). Q 11 is in the BOTTOM third of architectural significance per [[h-new-840-unified-architectural-score|H-NEW-840]].
- **Outlier-strength Δ**: **−4.88pp** (rank low; classified NULL, p=0.20). Q 11 does NOT register as a corpus-significant outlier under the H-NEW-590 protocol. (Compare Q 12 Yūsuf at +9.05pp WEAK_OUTLIER, Q 14 Ibrāhīm at -4.28pp NULL, Q 15 al-Ḥijr at +5.51pp WEAK_OUTLIER.)
- **iʿjāz sig_A**: **+0.594, rank 46/114** — moderately positive, near corpus median. Q 11's high rhyme-entropy (z=+1.75) drives a positive sig_A even though its content-distance is also elevated (z=+1.16); these net out.
- **Q10-Q11 canonical-adjacency cost**: **0.030 (rank 82/113)** — CHEAP transition (within ALR-cluster, expected). [[h-new-720-canonical-adjacency-cost|H-NEW-720]] `csv/h-new-720.json` per_adjacency[s=10].
- **Q11-Q12 canonical-adjacency cost**: **0.035 (rank 77/113)** — also cheap; intra-ALR.
- **Mean content distance to corpus**: 1.041 (z=+1.16 above corpus mean — content-distinct in the elevated direction).
- **Architectural type classification (iʿjāz architecture)**: Q 11 fits NEITHER the *Structural-twin-pair* cell (it has no high-cost adjacency on either side) NOR the *iʿjāz-al-fawāṣil-pure* cell (its outlier-strength is unremarkable). Q 11 is best classified as **iʿjāz-al-fawāṣil-leaning, narrative-anthology sub-type**: high rhyme entropy (sig_A positive), unremarkable outlier-strength, low canonical-adjacency cost — the surah's architecture lives in its *internal* rhyme-block structure (each prophet-block has its own rāwī-pattern) more than in its *whole-surah* outlier signature.

**Q 11 is rhyme-diverse, content-elevated-but-not-outlier, low-canonical-cost — the anthology surah's signature is internal block-variety rather than whole-surah distinctness.**

## 8. Quick content structure

Q 11 is **not** a continuous narrative; it is a **multi-prophet warning-anthology with a 7-prophet narrative compression** between two homiletic frames. Major thematic blocks (verse spans confirmed by verse-by-verse reading; see 02-content-analysis.md):

- **vv. 1-5** — ALR opening; *iḥkām + tafṣīl* book-affirmation; tawḥīd-warning thesis.
- **vv. 6-24** — Cosmological signs; ʿarsh; six-day creation; the Resurrection challenge; the "*who is more wronging than one who fabricates lies on God*" motif (vv. 18-19); contrast: those-who-believe-and-do-righteous-deeds vs the deaf-and-blind.
- **vv. 25-49** — **Nūḥ narrative (longest single block)** — call to Nūḥ; Nūḥ's son refuses; Flood; Ark; *yā arḍu blaʿī māʾaki* (v.44); Nūḥ's intercession for his son rejected (v.45-47).
- **vv. 50-60** — **Hūd narrative** — the warning to ʿĀd; Hūd's confrontation with the disbelieving chiefs; ʿĀd's destruction by *rīḥ ṣarṣar*.
- **vv. 61-68** — **Ṣāliḥ narrative** — call to Thamūd; the she-camel; Thamūd's hamstringing; the destruction; Ṣāliḥ saved.
- **vv. 69-83** — **Ibrāhīm + Lūṭ narrative** — angel-guests; Sarah's laughter; the announcement of Isḥāq; Lūṭ's people; the destruction of Sodom; Lūṭ's wife.
- **vv. 84-95** — **Shuʿayb narrative** — call to Madyan; *innī arā* dialogue; the *aṣ-ṣayḥa* destruction.
- **vv. 96-99** — **Mūsā + Pharaoh** (compressed, framing): a brief reprise of the Mūsā/Firʿawn confrontation as another warner-paradigm.
- **vv. 100-108** — Pedagogical commentary: *that's how it is when your Lord seizes the towns*; the *dhālika min anbāʾi al-qurā* refrain; the Day of Reckoning warning; the *fāṣila* of *fa-minhum shaqiyyun wa-saʿīd*.
- **vv. 109-115** — Doctrinal admonitions: *fa-staqim kamā umirta* (v. 112 — the famous "stand firm as you have been commanded" verse, classically associated with the Prophet's grey-hair tradition); *aqim al-ṣalāta ṭarafayi al-nahār* (v. 114 — "establish prayer at the two ends of the day").
- **vv. 116-119** — Why prior nations were destroyed despite *uli baqiyya* (people of moral remnant).
- **vv. 120-123** — Closing recapitulation: *wa-kullā naquṣṣu ʿalayka min anbāʾi al-rusul mā nuthabbitu bihi fuʾādaka* (v. 120 — "We narrate the news of the messengers to make your heart firm" — meta-narrative on the surah's own design); the closing *wa-Allāhi ghaybu al-samāwāti wa-l-arḍ* (v. 123 — book-conclusion echoing book-opening's *iḥkām*).

**Verse-by-verse first-mention of each prophet** (computed from `quran-text/quran-no-tashkeel.json`):
- Mūsā (موسى): first at v. 17 (in the disbelief-sign list); main block at vv. 96-110.
- Nūḥ (نوح): vv. 32, 36, 42, 45, 46, 48 — block 25-49.
- Hūd (هود): vv. 53, 60, 89 — block 50-60.
- Ṣāliḥ (صالح): vv. 46 (in Nūḥ-block historical reference), 62, 89 — block 61-68.
- Ibrāhīm (إبراهيم): vv. 69, 74, 75, 76 — block 69-83.
- Lūṭ (لوط): vv. 70, 74, 81, 89 — block 69-83 (joint with Ibrāhīm).
- Shuʿayb (شعيب): vv. 87, 91 — block 84-95.

**Prophet density**: 7 prophets in 123 verses = **0.057 prophets/verse**. Pre-registered test in 06-novel-findings.md: is this corpus-MAX? See [[Q011-F-01-prophet-density-prereg|Q011-F-01]].

## 9. Connection to ALR-cluster & cross-findings

[[h-new-97-name-letter-joint|H-NEW-97]] established ALR-PROPHET_PERSON 4/5 at p_mc=0.0059. Q 11 is one of the four (alongside Q 10, Q 12, Q 14). Q 11's role within the ALR cluster: **the prophet-anthology centerpiece** — the surah whose multi-prophet form most fully expresses the ALR cluster's prophet-naming convention. While Q 12 Yūsuf is single-prophet narrative, and Q 10 / Q 14 are thesis-named with sparse prophet-mentions, Q 11 is the *encyclopedic* form. This is what makes Q 11 the "head of the warning-cluster" in al-Tirmidhī's tradition: it is the anthology-form to which other surahs are "sisters."

Q011-F-02 (this investigation) NULL-replicated [[h-new-600-letter-families|H-NEW-600]]'s ALR-5 cohesion null AT WHOLE-SURAH FR scale, but found Q 11's mean FR distance to ALR siblings (0.904) IS LOWER than to non-ALR (1.046, Δ = 0.142) — the **strongest ALR pull-in among the 5 cluster members** (Q 10's was 0.914 vs 1.053 = Δ 0.139; Q 14's = 0.011; Q 15's REVERSED at -0.023). This is post-hoc t-test signal, not pre-registered, and is reported as DIRECTIONAL with full disclosure.

## 10. Cross-references (high-level)

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 11 −4.88pp NULL (`csv/h-new-590.json` X=11).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 88/114.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q10-Q11 rank 82/113 (cheap, 0.36% residual); Q11-Q12 rank 77/113 (cheap, 0.43%).
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A = +0.594, rank 46/114; high rhyme-entropy (1.737 nats).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — multi-rhyme; head-mushaf (s=11) so non-compression-tail.
- [[h-new-600-letter-families|H-NEW-600]] — ALR-5 NULL at 56.25%ile (replicated by Q011-F-02 with Q 11-pull-in noted).
- [[h-new-97-name-letter-joint|H-NEW-97]] — ALR-PROPHET_PERSON 4/5 at p_mc=0.0059 (Q 11 is one of the 4).
- [[Q010-yunus/00-overview|Q 10 Yūnus]] — ALR cluster sibling; thesis-named-prophet contrast.
- [[Q012-yusuf/00-overview|Q 12 Yūsuf]] — ALR cluster sibling; narrative-named-prophet contrast.
- [[Q014-ibrahim/00-overview|Q 14 Ibrāhīm]] — ALR cluster sibling; thesis-named with extreme low concentration (1.61%).
- [[Q015-al-hijr/00-overview|Q 15 al-Ḥijr]] — ALR cluster sibling; place-named (only non-PROPHET_PERSON in ALR-5).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 — Q 11 falls in the iʿjāz-al-fawāṣil-pure-leaning sub-cell (high rhyme-entropy, low outlier).
- al-Tirmidhī #3297 *Hūd and its sisters* — chain audit in 04-hadith-corpus.md.

## 11. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md (123 verses)
- [x] 03-tafsir-survey.md (≥6 mufassirūn)
- [x] 04-hadith-corpus.md (al-Tirmidhī #3297 chain audit + 9-book scan)
- [x] 05-classical-claims-audit.md (≥5 claims)
- [x] 06-novel-findings.md (4 pre-registered tests with SHA-locked pre-regs)
- [x] 07-cross-references.md
- [x] JOURNAL.md
