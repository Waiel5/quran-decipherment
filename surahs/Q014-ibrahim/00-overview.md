---
surah: 14
surah_name_ar: ابراهيم
surah_name_translit: Ibrāhīm
surah_name_english: Abraham
file_type: overview
date_last_updated: 2026-05-08
phase: B+
verdict: SCAFFOLD — full template built; 3 novel tests pre-registered + executed under Bonferroni-k=3
---

# Q 14 Ibrāhīm — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 14 | canonical |
| Arabic name | إبراهيم | canonical |
| Transliteration | Ibrāhīm | canonical |
| English meaning | "Abraham" (named after the prophet whose Mecca-prayer occupies vv. 35-41) | classical |
| Verse count | 52 | Hafs-Kufan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 14 | canonical |
| Type | **Late Meccan** (uncontested across Sunnī tradition + Nöldeke) | `data/revelation-order.csv` Q14 row |
| Position in revelation order (Tanzil Egyptian Std, al-Suyūṭī-aligned) | **72 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **76 / 114 (Late Meccan)** | `data/revelation-order.csv` `noldeke_phase = Late Meccan` |
| Word count (no-tashkeel) | **885** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, all non-space chars) | **3,594** | same |
| Mean words/verse | **17.02** | computed |
| **Opening** | **الر ۚ كتاب أنزلناه إليك لتخرج الناس من الظلمات إلى النور** — "ALR. A Book that We have sent down to you, that you may bring forth mankind from darkness to light…" | muqaṭṭaʿāt (ALR) + book-self-reference + light-from-darkness |
| Top rāwī | **د (dāl)** at **23.9%** of 46 letter-final verses (after the 2 verses ending with sajda-marker / `ʿalāʾim al-waqf`) | computed from `h-new-750.json` |
| Sajda verse | none (Q 14 is NOT a *sūrat al-sajda*) | classical |

## 2. ⭐ Corpus-distinctive structural property — the Mecca-prayer of Abraham (Q 14:35-41)

**Q 14 contains the longest Abrahamic prophetic-prayer in the Qurʾān** (vv. 35-41, 7 verses, 107 words). Across these 7 verses, Abraham invokes God in a sustained second-person petition with vocatives *rabbi* (My Lord) / *rabbanā* (Our Lord) / *rabbi-jʿalnī* (My Lord — make me) / *fa-jʿal* / *wa-arzuq-hum* / *rabbanā ighfir lī wa-li-wālidayya wa-li-l-muʾminīn* (forgive me and my parents and the believers).

**Pre-test result (Q014-F-01, see `06-novel-findings.md`)**: the prayer-vocative density of Q 14:35-41 is **14.95 prayer-tokens per 100 words** — the **corpus-MAX** value across **5,569 7-verse windows** in the Qurʾān (rank **1 / 5,569**). The four highest-density 7-verse windows in the corpus are ALL inside Q 14 (Q 14:35-41, 36-42, 37-43, 34-40 — all > 12 prayer-tokens / 100w). The 5th-place window (Q 23:93-99) drops to 10.20 / 100w.

This is the empirical anchor for the surah's title-naming (named after the prophet whose petition-block dominates it). The Mecca-prayer (Q 14:35-41) is structurally and lexically the most-prayer-saturated 7-verse passage in the entire Qurʾānic corpus.

## 3. ⭐ Bilateral architectural twin with Q 13 al-Raʿd

The Q 13 specialist established `Q013-F-05` (CONFIRMED 3/3) that Q 13 is architecturally near-identical to Q 14 in 4-axis Euclidean signature space (d_arch = 0.486, while d_arch(Q13, Q76) = 4.293 — i.e. Q 14 is **8.83× closer** to Q 13 than a Medinan similar-length reference).

**Q014-F-02 verifies the bilateral**: Q 13 is also Q 14's nearest FR-content neighbour at FR=**0.7838** (rank **1 / 113**). Per the FR-distance matrix `findings/phase-b-hypotheses/csv/h-new-111.json`:
- Q 13 → Q 14 is the FR-nearest neighbour from Q 13's row (computed by Q013 specialist: 0.7838).
- Q 14 → Q 13 is the FR-nearest neighbour from Q 14's row (computed Q014-F-02: 0.7838).
- The pair Q (13, 14) is therefore a **MUTUALLY-NEAREST FR-content pair** — the strongest possible bilateral cluster signal at this metric. Out of 6,441 corpus pairs, the 0.7838 distance is at percentile ≈ 7.5% (well into the FR-close tail).

This is the strongest bilateral architectural-twin signal between any Q s and Q s+1 mushaf-adjacent pair so far identified in the project. (See `07-cross-references.md` §3 for context vs other top FR-twin pairs.)

## 4. ALR-cluster membership

Q 14 is a member of the **ALR muqaṭṭaʿāt cluster** = {Q 10, 11, 12, 14, 15} (5 surahs). Q 14's mean FR-content distance to its 4 ALR siblings is **0.929** (computed from `h-new-111.json`):
- Q 14 → Q 10: 0.881
- Q 14 → Q 11: 0.896
- Q 14 → Q 12: **1.076** (the highest within ALR — Q 12's *aḥsan al-qaṣaṣ* continuous-narrative is FR-distinct)
- Q 14 → Q 13: **0.784** (the LOWEST — bilateral twin; note Q 13 is technically ALMR not ALR but is mushaf-adjacent)
- Q 14 → Q 15: 1.009

Q 14's ALR-sibling mean (0.929) is **slightly below the ALR-internal pairwise mean (0.955, computed in Q013-F-04)** and is **below the corpus pairwise FR median (0.957)**. The cluster-membership signature is consistent with FR-cluster-membership, but per H-NEW-610 (NULL on whole-surah letter-family cohesion), this is not statistically distinctive at the strict Bonferroni threshold (see Q014-F-03 below).

## 5. Length classification

52 verses, 885 words — **mufaṣṣal-ṭiwāl-class** (head-mushaf zone, pre-Hijra-kink at s=50). Per H-NEW-660 prediction: d̄_content(s=14) ≈ 0.96 (head-cohort plateau); observed mean_content_distance = **0.976** (`h-new-750.json` `mean_content_distance` for surah=14). Spot-on prediction.

Verse-length distribution: longest verse Q 14:9 (~30 words: the prophet-cycle-summary verse mentioning Nūḥ, ʿĀd, Thamūd); shortest verses Q 14:20 (5 words), Q 14:29 (4 words). Mean 17.0 w/v puts Q 14 in the head-mushaf medium-length register.

## 6. Rhyme structure

Final-letter distribution across the 46 letter-final-classifiable verses (per H-NEW-750):

| Final letter | % |
|:--:|:--:|
| **د (dāl)** | **23.9% — top rāwī** |
| ر (rāʾ) | (sub-rāwī) |
| ن (nūn) | (sub-rāwī) |
| م (mīm) | (sub-rāwī) |
| (other) | (mixed multi-rāwī tail) |

**Rhyme entropy (Shannon, nats): 1.9109** — corpus-z = **+2.066** — among the **TOP** rhyme-diverse surahs in the Qurʾān, second only to Q 13 al-Raʿd's z=+1.72 in the head-mushaf zone. Q 14 is markedly multi-rāwī (NOT monorhyme) — its top-rāwī د is at only 24% of verse-endings.

The dāl-final fawāṣil (in *al-ḥadīd / al-ḥamīd / la-shadīd / ṣadīd / ʿanīd / mubīn / al-ʿabīd* class endings) interlock with secondary mīm-final, nūn-final, and rāʾ-final verses. This rhyme-diversity is the empirical anchor for Q 14's high *iʿjāz al-fawāṣil* signature (Q 14 is in the top-15 of sig_A in the corpus).

## 7. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **20 / 114** (mid-pack, immediately ABOVE Q 13 at rank 21).
- **Outlier-strength** Δ_pct: **−4.28 pp**, classification **NULL** in window {Q 11–17} (`h-new-590.json` X=14). Q 14 is **NOT a content outlier** vs its mushaf cohort — like Q 13, it is a CLUSTER ANCHOR not an outlier.
- **iʿjāz sig_A**: +1.546 (rank **14 / 114** — top-15, structural-iʿjāz-positive). Q 14 is **structurally iʿjāz-positive** by the al-Bāqillānī axis.
- **iʿjāz sig_B**: +1.464 (rank **15 / 114** — top-15).
- **Mean FR-content distance to corpus**: 0.976 (z = +0.520).
- **Q 13→Q 14 canonical-adjacency cost**: **0.0497 length-units** (very cheap; bottom-quartile of 113 pairs) — the Raʿd→Ibrāhīm seam is structurally near-free.
- **Q 14→Q 15 canonical-adjacency cost**: **0.1988 length-units** (rank ≈ 13 / 113, top-15 EXPENSIVE) — the Ibrāhīm→Ḥijr seam is structurally costly, despite both being ALR-cluster members. The expensive seam is driven by the register shift from didactic-cosmological-prayer (Q 14, multi-rāwī, sig_A high) to iterative-prophet-narrative (Q 15, near-monorhyme on ن at 82%, sig_A negative).

## 8. Quick content structure

Q 14 is a 52-verse late-Meccan didactic-cosmological-prayer-eschatological surah, NOT a continuous narrative:

- **vv. 1-3**: Opening (الر + book-self-reference; *li-tukhrija al-nāsa min al-ẓulumāti ilā al-nūr* — bring mankind from darkness to light; eschatological warning to disbelievers).
- **vv. 4**: theology of revelation in mother-tongue (*wa-mā arsalnā min rasūl illā bi-lisān qawmihi*) — universal-prophet-language principle.
- **vv. 5-8**: Mūsā cycle compressed (Mūsā addresses his people; remembrance of God's grace at the Exodus).
- **vv. 9-15**: Generic prophet-cycle (Nūḥ, ʿĀd, Thamūd, "those after them whom only God knows"); messengers' confrontation with disbelievers; the disbelievers' threat of expulsion; God's promise to destroy the wrongdoers.
- **vv. 16-17**: hellfire details (drink of pus *māʾ ṣadīd*; Q 14:17 *yatajarra'uhu wa-lā yakādu yusīghuhu* — sips it but barely swallows it).
- **vv. 18**: parable of the disbelievers' deeds as ash in a windy day (*ka-ramādin ishtaddat bihi al-rīḥu fī yawmin ʿāṣif*).
- **vv. 19-22**: Resurrection scene; the weak vs the proud at the Judgment; **Q 14:22 — Iblīs's Day-of-Judgment speech** (*wa-qāla al-shayṭānu lammā quḍiya al-amr…*) — the corpus's UNIQUE Iblīs-as-eschatological-orator-self-disavowing speech (compare Q 15's Iblīs-as-rebelling-creature speech for cross-surah Iblīs typology).
- **vv. 23-27**: Believers' reward; **the parable of the GOOD WORD as a good tree** (*kalimatan ṭayyibatan ka-shajaratin ṭayyiba aṣluhā thābitun wa-farʿuhā fī al-samāʾ*) — Q 14:24-27, one of the most-celebrated parables in the Qurʾān.
- **vv. 28-30**: parable of the disbelievers — exchanged God's grace for disbelief.
- **vv. 31**: instruction to Muḥammad's believers (*qul li-ʿibādī alladhīna āmanū*…).
- **vv. 32-34**: cosmological-grace recital (heavens, earth, ships, sun & moon, day & night, *wa-ātākum min kulli mā saʾaltumūhu* — "He gives you of all you ask"; *wa-in taʿuddū niʿmata Allāhi lā tuḥṣūhā* — "if you count God's grace, you cannot enumerate it").
- **vv. 35-41**: ⭐ **THE MECCA-PRAYER** — Abraham's Mecca-prayer (corpus-MAX prayer-density 7-verse window). Petitions for Mecca's safety, for separation from idolatry, for sustenance for the descendants left at the Sacred House, the *al-ḥamdu li-llāhi alladhī wahaba lī ʿalā al-kibari Ismāʿīla wa-Isḥāq* (praise be to God who granted me Ishmael and Isaac in old age) — the corpus's UNIQUE *al-ḥamd-for-prophetic-progeny* declaration. Closing prayer: *rabbanā ighfir lī wa-li-wālidayya wa-li-l-muʾminīn yawma yaqūmu al-ḥisāb* — the corpus-distinctive *grandparent-child intercessory prayer*.
- **vv. 42-47**: eschatological closure (the wrongdoers' Judgment, *yawma tubaddalu al-arḍu ghayra al-arḍ* — Day when earth is changed).
- **vv. 48-51**: scene of the criminals on Judgment Day; the swift reckoning of God.
- **v. 52**: closing — *hādhā balāghun li-l-nāsi wa-li-yundharū bihi wa-li-yaʿlamū annamā huwa ilāhun wāḥid* (this is a message for mankind, that they may be warned, that they may know that He is one God).

The surah is a **didactic-cosmological-eschatological-prayer microcosm**: book-self-reference (v. 1) + universal-prophet-language (v. 4) + prophet-cycle-summary (vv. 5-15) + eschatology (vv. 16-22) + theology-of-the-good-word parable (vv. 24-27) + cosmological-grace recital (vv. 32-34) + Mecca-prayer of Abraham (vv. 35-41) + eschatological closure (vv. 42-52). The prayer-block is the structural and thematic centre.

## 9. Connection to ongoing project findings

- Q 14 is the FR-nearest neighbour of Q 13 (Q013-F-04 result, 0.784) and is the architectural twin of Q 13 in the 4-axis signature space (Q013-F-05 result, d=0.486). Q014-F-02 verifies the bilateral.
- Q 14 is in the ALR cluster {Q 10, 11, 12, 14, 15}; H-NEW-610 establishes muqaṭṭaʿāt-content-NULL at whole-surah scale; Q014-F-03 tests Q 14's specific position in the cluster.
- Q 14's structural-iʿjāz signature (sig_A rank 14/114, sig_B rank 15/114, rhyme entropy z=+2.07) places it firmly in the *iʿjāz al-fawāṣil-positive* zone of the dual-iʿjāz typology (cross-finding-026 §13).
- Q 14:35-41 is the corpus-MAX prayer-density 7-verse window (Q014-F-01 result) — corpus-distinctive in the lexical-syntactic prayer-vocative cluster.
- Q 14:24-27 (good-word parable) is referenced in `cross-finding-008-muqattaat-book-intro-markers` and is one of the most-frequently-cited parables in the classical balagha tradition (al-Zamakhsharī Kashshāf has an extensive entry).

## 10. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md (UAS rank 20; FR-nearest Q 13 at 0.784; outlier NULL; sig_A rank 14/114)
- [x] 02-content-analysis.md (10-section thematic structure; book-self-ref, prophet-cycle, parable-of-good-word, cosmological-grace, Mecca-prayer, eschatological closure)
- [x] 03-tafsir-survey.md (≥ 5 mufassirūn surveyed)
- [x] 04-hadith-corpus.md (Bukhārī/Muslim/Tirmidhī/Aḥmad — Mecca-prayer, good-word parable, Iblīs-on-Judgment-Day citations; verified hadith numbers)
- [x] 05-classical-claims-audit.md (al-Bāqillānī iʿjāz al-fawāṣil; al-Suyūṭī chronology; al-Biqāʿī Q 13→Q 14 munāsabah; rules-tuple verifications)
- [x] 06-novel-findings.md (Q014-F-01 prayer-density CONFIRMED corpus-MAX; Q014-F-02 bilateral-twin CONFIRMED; Q014-F-03 ALR-cluster-membership tested)
- [x] 07-cross-references.md (Q13↔Q14 bilateral twin; ALR-cluster context; Q14↔Q26 cross-Abrahamic-prayer; Iblīs-typology vs Q15)
- [x] JOURNAL.md (run log, SHA hashes, decision points)
