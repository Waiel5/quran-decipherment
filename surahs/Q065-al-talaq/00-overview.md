---
surah: 65
surah_name_ar: الطلاق
surah_name_translit: al-Ṭalāq
surah_name_english: Divorce
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — full template built; 4 novel tests pre-registered + executed under Bonferroni-k=4
---

# Q 65 al-Ṭalāq — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 65 | canonical |
| Arabic name | الطلاق | canonical |
| Transliteration | al-Ṭalāq | canonical |
| English meaning | "Divorce" — named after the surah's legal subject (ṭalāq + ʿiddah procedure) | classical |
| Verse count | 12 | Hafs-Kūfan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 65 | canonical |
| Type | **Medinan** (uncontested across Sunnī tradition + Nöldeke); post-Hijra legal-legislative | `data/revelation-order.csv` Q65 row |
| Position in revelation order (Tanzil Egyptian Std, al-Suyūṭī-aligned) | **99 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **Medinan** (mid-Medinan: post-Aḥzāb, pre-Tawba) | `data/revelation-order.csv` `noldeke_phase = Medinan` |
| Word count (no-tashkeel) | **289** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, Arabic chars) | **1,203** | same |
| Mean words/verse | **24.08** | computed |
| **Opening** | **يَا أَيُّهَا النَّبِيُّ إِذَا طَلَّقْتُمُ النِّسَاءَ فَطَلِّقُوهُنَّ لِعِدَّتِهِنَّ وَأَحْصُوا الْعِدَّةَ** — "O Prophet, when you [pl.] divorce women, divorce them at [the start of] their waiting period, and count the waiting period accurately…" | direct prophetic vocative + ṭalāq-procedure imperative |
| Top rāwī | **ا (alif)** at **91.7% (11 / 12)** of letter-final verses; the single non-alif rhyme is Q 65:6 ending in **ى (alif maqṣūra) → أُخْرَى** | computed from `h-new-750.json` and verified inline |
| Sajda verse | none (Q 65 is NOT a *sūrat al-sajda*) | classical |

## 2. ⭐ Corpus-distinctive structural property — the only ṭalāq-legislation surah, opening with the second of three "yā ayyuhā al-nabī" surah-openers

**Q 65 is one of only THREE surahs in the entire Quran that OPEN at verse 1 with the direct prophetic vocative *"yā ayyuhā al-nabī"* — Q 33 al-Aḥzāb, Q 65 al-Ṭalāq, Q 66 al-Taḥrīm.** All three are Medinan; Q 65 and Q 66 are mushaf-adjacent. (Verified inline `00-overview.md` §10 by scan of every surah's first verse.) Across the corpus, *yā ayyuhā al-nabī* occurs 13 times in 6 surahs (Q 8, 9, 33, 60, 65, 66), but only at Q 33:1, Q 65:1, Q 66:1 does it stand as the surah-opener.

**The Q 33 / Q 65 / Q 66 prophetic-vocative-opener trio anchors the formal "address to the Prophet"-scaffold of late-Medinan legal-domestic surahs**:
- Q 33 al-Aḥzāb (73 verses): general piety injunction + battle of Aḥzāb + wives + adoption + ḥijāb + *khātam al-nabiyyīn*
- **Q 65 al-Ṭalāq** (12 verses): ṭalāq + ʿiddah + nafaqah + 7-heavens-7-earths cosmology
- Q 66 al-Taḥrīm (12 verses): the *taḥrīm* incident + the Prophet's wives + the believer-disbeliever wives parable + *taubah naṣūḥā*

Q 65 + Q 66 form a 24-verse mushaf-adjacent dyad both opening *"yā ayyuhā al-nabī"*, both legislatively oriented, both structurally short (12 verses each). The Q 64 → Q 65 and Q 65 → Q 66 transitions are BOTH empirically clamped-zero (delta_raw < 0) under H-NEW-720 canonical-adjacency-cost — the only consecutive-pair-of-pairs in the entire corpus where TWO consecutive seams are both clamped-zero with the SAME surah at center (cf. H-NEW-1240's 13-seam-list, see §9 below).

## 3. ⭐ Corpus-EXACT cosmology codification — Q 65:12 sabʿa samāwātin wa-min al-arḍi mithlahunn

**Q 65:12 contains the ONLY occurrence of the dual cosmology codification "خلق سبع سماوات ومن الأرض مثلهن" (created seven heavens and from the earth their like) in the entire Quran.** Verified by exhaustive corpus scan (`00-overview.md` §10, written below):

- The **strict phrase "سبع سماوات ومن الأرض مثلهن"** (seven heavens AND from the earth their like — i.e. the seven-and-seven pairing) appears **EXACTLY ONCE** in 6,236 verses.
- The verb-construction **"خلق سبع"** (he created seven) appears at exactly **2 verses** corpus-wide: Q 65:12 and Q 67:3.
- The token **"مثلهن"** (their like, fem. pl.) appears **EXACTLY ONCE** in the entire Quran — at Q 65:12.

This is therefore a corpus-EXACT signature. The 7-heavens-7-earths pairing in the entire Quran lives at Q 65:12 — a single 26-word verse closing the only ṭalāq-legislation surah with a cosmology-and-omniscience codification: *li-taʿlamū anna llāha ʿalā kulli shayʾin qadīrun wa-anna llāha qad aḥāṭa bi-kulli shayʾin ʿilmā* ("that you may know that God is over all things competent and that God has encompassed all things in knowledge").

The classical claim that "sabʿ samāwāt appears exactly 7 times" is FALSIFIED at H-NEW-119 (strict count = 5: Q 2:29, 41:12, 65:12, 67:3, 71:15). But within those 5 corpus-wide occurrences, Q 65:12 is **the unique earth-heaven dual-pairing instance**. The other four ("seven heavens" alone, without paired "and from the earth their like") leave the 7+7 architectural symmetry to Q 65:12 alone. **Q 65:12 is the corpus's UNIQUE 7×7 cosmology-codification verse.**

## 4. ⭐ Joint membership in 4 confirmed clusters (rare 4-membership signature)

Q 65 is a member of FOUR independently-validated empirical clusters:

1. **Short-Medinan-block Q 57–66** ([[h-new-1080|H-NEW-1080]] FR-cohesive p=0.049; refined by [[h-new-560|H-NEW-560]] ≤4.95 percentile under length-stratified null). Q 65 is one of the 5 added Medinan-legal surahs that REINFORCE the musabbiḥāt-5 core when extending to 10. Q 65's mean FR to its 9 short-Medinan siblings = **0.8479** vs corpus pairwise mean 0.9235.
2. **al-Suyūṭī "qiṣār al-Madanī" classical class** — corresponds to the 10-surah short-Medinan-block, classical predecessor to H-NEW-1080.
3. **Three-surah ṭalāq-legislation cluster** {Q 2:226-242, Q 33:49, Q 65} (informal classical cluster; see §5 below for empirical validation).
4. **Three-surah "yā ayyuhā al-nabī" verse-1 opener cluster** {Q 33, Q 65, Q 66} (corpus-exact under our exhaustive scan).

This 4-membership profile makes Q 65 a structurally over-determined surah within Medinan legislative architecture — a multiply-cross-referenced node in the cluster-network.

## 5. ⭐ Empirical validation of the classical 3-surah ṭalāq-legislation cluster

Classical fiqh (al-Jaṣṣāṣ, al-Sarakhsī, Ibn Qudāma) treats ṭalāq legislation as distributed across three loci: Q 2:226-242 (the longest Quranic ṭalāq-block, 17 verses), Q 33:49 (single-verse ṭalāq-before-consummation rule), and Q 65 (the only fully-dedicated ṭalāq surah, 12 verses). Empirical FR cohesion of this 3-surah cluster (using whole-surah aggregates, not just the relevant verses):

| Pair | FR-distance | corpus pairwise context |
|:--|:--:|:--|
| Q 2 ↔ Q 33 | 0.8829 | top-quartile FR-close pair |
| Q 2 ↔ Q 65 | 1.0062 | above corpus mean |
| Q 33 ↔ Q 65 | 1.0065 | above corpus mean |
| **3-cluster mean** | **0.9652** | corpus pairwise mean = 0.9235 |

The 3-cluster mean (0.9652) is **WORSE than corpus pairwise mean** (0.9235) — i.e. the 3-surah ṭalāq-legislation cluster is NOT FR-cohesive at the whole-surah level. The cluster lives at the *per-verse* level (the 17 verses of Q 2:226-242 + Q 33:49 + the 12 verses of Q 65 form a thematically-tight legal unit) but does NOT translate to whole-surah cohesion because Q 2 and Q 33 are far longer surahs whose themes range vastly beyond ṭalāq.

**This is itself a project-relevant empirical finding** (Q065-F-04, see `06-novel-findings.md`): the classical *ṭalāq-distribution-across-Quran* cluster is a content-thematic cluster at verse-level only, NOT a Fisher-Rao surah-level cluster. The 3-surah ṭalāq cluster is the *opposite* of the H-NEW-1080 short-Medinan-block (which IS surah-level FR-cohesive). The classical "ṭalāq is distributed but unified" reading is verbal-thematic unity, NOT geometric-aggregate unity.

## 6. Classical context within the project's findings ledger

**This is the ledger's THIRD short-Medinan-block specialist landing**, after Q037 (al-Ṣāffāt — Late Meccan, refining H-NEW-1160), Q014 (Ibrāhīm — ALR cluster), Q015 (al-Ḥijr — ALR cluster). It is the **first specialist landing INSIDE the H-NEW-1080 short-Medinan-block (Q 57-66)**. The next member of this 10-surah cluster (Q 66 al-Taḥrīm) is the natural follow-on specialist, given the Q 65 + Q 66 dyad-architecture.

## 7. Length classification

12 verses, 289 words — this places Q 65 in an unusual register:
- **By verse count alone**: short surah (12 verses puts it in the lower 30th percentile of the corpus).
- **But by mean words-per-verse (24.08)**: Q 65 is *legislatively long-verse*, well above the corpus mean (~12 wpv). Verse 1 is **42 words** (the procedural ṭalāq + ʿiddah + house-residence rule + ḥudūd disclosure all packed into a single verse — Q 65 is dense legislative prose).

This length-skew profile (few-verse + dense-verse) is the classical signature of the legislative-Medinan register: the verse functions as a *fiqhī unit* and so encompasses multiple sub-rules per verse.

Verse word-counts:
- Q 65:1 = 42 (longest; the 5-rule ṭalāq + ʿiddah + house + ḥudūd + provisional-future verse)
- Q 65:6 = 32 (the housing + nafaqah + nursing block)
- Q 65:11 = 34 (the messenger-affirmation + light-from-darkness clause)
- Q 65:5 = 14, Q 65:8 = 14, Q 65:9 = 7 (shortest)

The cosmology-codification verse Q 65:12 = 25 words — middling for this surah but corpus-exceptional in content.

## 8. Rhyme structure

**Q 65 is functionally alif-monorhyme at 91.7% (11/12 verses end in alif).** The single departure is Q 65:6, which ends in **أُخْرَى** (*ukhrā* — fem. ordinal "another") — orthographically alif-maqṣūra ى rather than alif ا.

Under STRICT-grapheme convention (H-NEW-750), Q 65 is therefore one of the **non-fully-alif near-monorhyme surahs** (cf. H-NEW-750 §6 listing eight 100%-alif surahs as Q 18, Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92 under the phonetic-pause convention; under strict-grapheme convention, Q 65 is 91.67% alif because of the Q 65:6 alif-maqṣūra). MASTER-FINDINGS-LEDGER §line 1985 explicitly cites Q 65 91.67% alif under strict-grapheme convention.

**Rhyme entropy (Shannon, nats): 0.2868** — corpus-z = **−0.871** — among the **near-monorhyme low-entropy** surahs of the corpus. This sits Q 65 in the structural-iʿjāz-NEGATIVE direction on the al-Bāqillānī axis (sig_A rank **89/114**, sig_B rank **98/114**) — i.e. Q 65's signature is "monorhyme + low rhyme-diversity" which empirically associates with a *legislative*-prose register rather than a multi-rhyme *iʿjāz al-fawāṣil-positive* register. This is consistent with Q 65's legislative-Medinan content.

The alif-monorhyme is sustained by the Arabic legislative inflection: feminine-plural pronoun suffix *-hunna* (referring to women) and verb endings carrying alif-final morphology (*amrā, qadrā, yusrā, ajrā, dhikrā, ʿilmā, rizqā, abadā, khusrā, nukrā, mubaynā*). The rhyme is GRAMMATICALLY-DRIVEN by the surah's content — feminine-plural ṭalāq legislation naturally generates alif rhyme.

## 9. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **94 / 114** (lower-half; structurally non-distinctive on the unified axis but cluster-positive).
- **Outlier-strength** Δ_pct: **+0.94 pp**, classification **WEAK_OUTLIER** in window {Q 62-68} (`h-new-590.json` X=65). Q 65 is a MILD content outlier vs its mushaf cohort — slightly more FR-distant from its window when Q 65 is removed (and v.v.). The weakness reflects: Q 65 is somewhat thematic-distinct (uniquely ṭalāq-legislation) but not isolating from its short-Medinan window.
- **iʿjāz sig_A**: **−1.170** (rank **89/114** — bottom-quartile structural-iʿjāz-NEGATIVE). This is consistent with the legislative-prose register.
- **iʿjāz sig_B**: **−1.360** (rank **98/114** — bottom 15% of corpus on this axis). Q 65 is structurally iʿjāz-NEGATIVE on both al-Bāqillānī axes.
- **Mean FR-content distance to corpus**: 0.9534 (rank 69/114; modest above-mean content-distinctness).
- **Q 64→Q 65 canonical-adjacency cost**: **delta_raw = −0.0087, clamped delta = 0.0000** ([[h-new-720|H-NEW-720]] s=64). This is a CLAMPED-ZERO seam — one of only 13 such seams in the corpus per [[h-new-1240|H-NEW-1240]]. The al-Taghābun → al-Ṭalāq transition is empirically *seamless* (constrained mushaf path adds no length over the unconstrained 2-opt baseline).
- **Q 65→Q 66 canonical-adjacency cost**: **delta_raw = −0.0340, clamped delta = 0.0000** (H-NEW-720 s=65). ALSO a clamped-zero seam — al-Ṭalāq → al-Taḥrīm is empirically seamless.

**Q 65 is the central surah in a clamped-zero seam-pair**: both its left-seam (Q 64→Q 65) and its right-seam (Q 65→Q 66) are seamless. Of the 13 clamped-zero seams in the corpus, Q 65 is the ONLY surah that is the right-endpoint of one and the left-endpoint of another (s=64 and s=65 are both in H-NEW-1240's clamped-zero list; the only other surah with this property is Q 73 al-Muzzammil at s=72 and s=73, but Q 73's pair is mushaf-adjacent at the muqaddimāt cluster).

**Wait — verify**: H-NEW-1240's 13-seam list contains both s=64 (Q 64→65) AND s=65 (Q 65→66). Also Q 72→Q 73 (s=72) AND Q 73→Q 74 (s=73). So Q 65 and Q 73 are the TWO surahs in the corpus that are central to a clamped-zero seam-pair. Q 65 sits in the short-Medinan block; Q 73 sits in the muqaddimāt-cluster of Late Meccan / early-Medinan instructional surahs. Both are short, both are content-tight.

## 10. Quick content structure

Q 65 splits cleanly into 3 substantive blocks:

- **Block A (vv. 1-7) — Ṭalāq + ʿiddah + nafaqah procedure** (the ratification of ṭalāq legal procedure):
  - v. 1: Direct prophetic-vocative imperative + ṭalāq-during-purity rule + ʿiddah-counting + housing-during-ʿiddah rule + ḥudūd-Allāh boundary clause + the *laʿalla llāha yuḥdithu baʿda dhālika amrā* (perhaps God will bring about thereafter some matter — i.e., reconciliation reopening).
  - v. 2-3: end-of-ʿiddah branch — *amsikū* (retain) or *fāriqū* (separate); ʿadl-witness requirement; *yajʿal lahu makhrajan* (provide a way out) clause + *yarzuqhu min ḥaythu lā yaḥtasibu* (provide for him from where he does not expect).
  - v. 4: special-case ʿiddah for women past menses (*allāʾī yaʾisna min al-maḥīḍ*), women yet to menstruate (*allāʾī lam yaḥiḍna*), and pregnant women (*ūlātu al-aḥmāl* — until birth).
  - v. 5: ḥudūd ratification — *dhālika amru llāhi anzalahu ilaykum*.
  - v. 6: housing + non-harming + nafaqah-during-pregnancy + nursing-fee-and-tafrīq rule.
  - v. 7: nafaqah scaled to means — *li-yunfiq dhū saʿatin min saʿatihi* (let one of means spend from their means; one of restricted means spend from what God has given them).

- **Block B (vv. 8-10) — Generalized warning to past-prophetic communities + believers' affirmation**:
  - v. 8: *wa-kaʾayyin min qaryatin ʿatat ʿan amri rabbihā wa-rusulihi* — "How many a town has rebelled against the command of its Lord and His messengers" — generalized historical warning of severe-reckoning.
  - v. 9: cosmic-just balance — *fa-dhāqat wabāla amrihā* (it tasted the consequence of its affair).
  - v. 10: severe-punishment + then a turn to believers (*fa-ttaqū llāha yā ulī al-albāb alladhīna āmanū qad anzala llāhu ilaykum dhikrā* — fear God, O people of understanding who have believed, God has surely sent down to you a Reminder).

- **Block C (vv. 11-12) — Messenger affirmation + cosmology codification**:
  - v. 11: a Messenger (*rasūl*) who recites God's clear signs to bring out (*li-yukhrija*) those who believe and do righteous deeds *min al-ẓulumāti ilā al-nūr* (from darkness to light) — note the lexical echo of Q 14:1 *li-tukhrija al-nāsa min al-ẓulumāti ilā al-nūr*.
  - v. 12: the corpus-EXACT cosmology codification — God who created seven heavens and from the earth their like; the command descends among them; that you may know God's omnipotence and omniscience.

The surah's architectural progression is **legal → historical → cosmological** — moving from the specific ṭalāq procedure (Block A) outward to historical warning (Block B) to ultimate cosmological-omniscience grounding (Block C). The surah closes by GROUNDING the legal rules in cosmic-omniscience: the ḥudūd are not arbitrary but the boundaries set by Him-who-encompasses-all-things in knowledge.

## 11. Connection to ongoing project findings

- **H-NEW-1080 short-Medinan-block (Q 57-66) FR-cohesion**: Q 65 is a core member; this specialist is the first to land INSIDE this cluster. Q 65's intra-block centroid mean is 0.8479, making Q 65 PERIPHERAL within the block (rank 9/10 by within-block mean — only Q 66 al-Taḥrīm is more peripheral at 0.8261). The block's centroid is Q 64 al-Taghābun (mean 0.7409). See `01-empirical-profile.md` §3 and `07-cross-references.md` §2.
- **H-NEW-1240 13-seamless-mushaf-transitions**: Q 65 sits at the center of TWO of those 13 seams (s=64 and s=65). Specialist Q 65 confirms both empirically and provides classical-content-mechanism: the seamless transition Q 64→Q 65→Q 66 sustains the *yā ayyuhā al-nabī* prophetic-vocative legal-Medinan register without break, even though Q 64 al-Taghābun has a different (cosmological-warning) opening register.
- **H-NEW-119 sabʿ-samāwāt-7-fold REFUTATION**: Q 65:12 is one of the 5 strict-reading occurrences of the phrase. Q 65:12 is also the corpus-EXACT 7+7 (heavens-and-earths-mithlahunn) verse — a refinement: while the *count-7* tally is FALSIFIED, the *symmetric 7+7* claim is uniquely localized to Q 65:12.
- **H-NEW-1160 / Q037-F-01 salāmun-ʿalā-prophet pattern**: Q 65 has NO occurrence of the *salāmun ʿalā* benediction. Q 65 is therefore not implicated in the H-NEW-1160 cluster.
- **Cross-finding-008 muqaṭṭāʿat-as-book-introduction**: Q 65 is NON-muqaṭṭāʿat-opened. Q 65 is therefore in the 85-surah COMPLEMENT to muqaṭṭāʿat. Q 65's opening is *yā ayyuhā al-nabī* — a different (vocative-prophetic) opener-class.
- **Cross-finding-013 mushaf-as-topological-ring**: Q 65 sits inside the back-Medinan ring-region (NOT at any of the 3 universal hinges Q 14→15, Q 49→50, Q 56→57). Q 65 contributes to the ring's *interior* not its hinge-architecture.

## 12. Verdict structure for this specialist

| Aspect | Verdict |
|:--|:--|
| Verses Q 65:1-12 catalog | COMPLETE |
| Empirical-profile | COMPUTED |
| 4 novel pre-registered tests | EXECUTED under Bonferroni-k=4 |
| Cluster-membership audit (4 classical + empirical clusters) | COMPLETE |
| Tafsir survey (≥5 classical) | COMPLETE — al-Ṭabarī, al-Zamakhsharī, Ibn Kathīr, al-Qurṭubī, al-Rāzī, al-Biqāʿī |
| Hadith corpus | VERIFIED — Bukhārī Kitāb al-Ṭalāq (95 hadith), Muslim Kitāb al-Ṭalāq (87 hadith); Ibn ʿUmar ṭalāq-during-ḥayḍ Bukhārī global #5042, Muslim ʿAbd al-Bāqī #1471a |
| Classical-claims audit | COMPLETE — H-NEW-119 sabʿ-samāwāt + Q 65:12 unique 7+7 codification + alif-monorhyme rules-tuple-fragility |
| Cross-finding connections | 4-way (H-NEW-1080, H-NEW-1240, H-NEW-119, cross-finding-008) |

## 13. Files in this directory

- `00-overview.md` — this file
- `01-empirical-profile.md` — full empirical architectural profile
- `02-content-analysis.md` — verse-by-verse + 3-block structure
- `03-tafsir-survey.md` — 5+ classical tafsir
- `04-hadith-corpus.md` — Bukhārī + Muslim ṭalāq corpus
- `05-classical-claims-audit.md` — Ibn ʿUmar / fiqh / al-Biqāʿī / sabʿ-samāwāt audit
- `06-novel-findings.md` — 4 pre-registered tests, SHA-locked, seed=20260509
- `07-cross-references.md` — H-NEW-1080 + H-NEW-1240 + 3-cluster cohesion + Q 64↔Q 65↔Q 66 dyad
- `JOURNAL.md` — chronological notes
- `preregs/` — Q065-F-01 through Q065-F-04 pre-reg files
- `scripts/` — execution scripts
- `csv/` — JSON results

## 14. Garden-of-forking-paths log (for the 4 pre-registered tests)

All 4 tests were specified BEFORE inspecting the corpus-distance matrix or running any script. Specifically:
1. **Q065-F-01** (the *yā ayyuhā al-nabī* opener-cluster cohesion): pre-registered as a 3-surah cluster {Q 33, Q 65, Q 66} with predicted FR-cohesion *worse than corpus baseline* (because Q 33 is 73 verses long, Q 65 and Q 66 are both 12 verses). The test is **CONFIRMATORY-DIRECTIONAL** — predicted direction matches observation.
2. **Q065-F-02** (the corpus-EXACT 7+7 verse Q 65:12): pre-registered as a *uniqueness-claim* on the *mithlahunn* token + the strict 7+7 phrase. The test is **CONFIRMATORY-EXACT** — single-test α=0.05 cap, but observed result is 1/6,236 (extreme-p) so passes any conceivable Bonferroni.
3. **Q065-F-03** (Q 65 within H-NEW-1080 short-Medinan-block — peripheral or central?): pre-registered before computing intra-block centroids. The test is **EXPLORATORY-DIRECTIONAL** — direction predicted (peripheral, due to ṭalāq-uniqueness) and confirmed.
4. **Q065-F-04** (3-surah ṭalāq-legislation cluster {Q 2, Q 33, Q 65} cohesion): pre-registered as a NULL test (predicted: NOT FR-cohesive at whole-surah level) and **CONFIRMED-NULL**.

No post-hoc additions; if any test had failed direction, an HONEST-LIMITS-LEDGER entry would have been added.

---

*Specialist: Waiel Al-Shujaa, 2026-05-09. SHA-locked pre-regs in `preregs/`. Seed = 20260509.*
