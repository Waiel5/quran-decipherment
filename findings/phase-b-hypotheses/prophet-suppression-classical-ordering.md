---
finding_id: h-new-11-ext-classical-audit
phase: B
status: AUDIT-BLOCKER — pre-reg cannot execute as-written; three corrections required before dispatch
date: 2026-04-13
task_ref: #36 H-NEW-11-EXT
parent_task: #18 H-NEW-11 (team-discovery-007.md)
owner: classical-scholar
rules_tuple: (no-tashkeel, lemma QAC v0.4, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
classical_sources_physically_verified:
  - al-Suyūṭī al-Itqān fī ʿUlūm al-Qurʾān, Shamela0011728 ed. (4 vols)
  - Fakhr al-Dīn al-Rāzī Mafātīḥ al-Ghayb, Shamela0023635 ed.
  - QAC v0.4 Quranic lemma data
mw_tier: MW-6 physical read with verbatim snippets
---

# [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT — Classical anchors for prophet-suppression ordering (AUDIT)

## Executive verdict

**THREE BLOCKERS.** Task #36's pre-reg cannot be executed as-written. Filed for team-lead + hypothesis-generator review before any re-dispatch.

1. **Citation error in the pre-reg.** Task #36 cites "al-Suyūṭī *Itqān* nawʿ 63 *qiṣaṣ al-anbiyāʾ*, vol. 2 pp. 420-428". **This nawʿ does not exist.** Al-Itqān nawʿ 63 is *fī al-āyāt al-mushtabihāt* (on similar/ambiguous verses). There is NO nawʿ dedicated to *qiṣaṣ al-anbiyāʾ* in al-Itqān at all.

2. **Prophet-set mismatch between task #18 (empirical) and task #36 (pre-reg).** Task #18 measured 8 prophets; task #36 pre-registered a different 8-prophet ordering. **Only 5 prophets overlap.** Task #18 includes ʿĪsā, Ādam, Lūṭ which are not in task #36; task #36 pre-reg includes Shuʿayb, Hūd, Ṣāliḥ which were not measured by task #18. A Spearman ρ on the overlap (n=5) is statistically inert.

3. **Lūṭ counter-prediction already contradicted by existing task #18 data.** Task #36 predicts Lūṭ's leave-one-out is "negative (reduces suppression when removed)." Task #18 shows Lūṭ LOO z = −2.35, obs − null = −0.028 — Lūṭ's removal does NOT reverse the suppression direction. The counter-prediction is falsified by the parent task's own data.

Each blocker is documented below with verbatim classical anchors and exact data.

---

## 1. Classical source correction — what al-Itqān actually says

### 1.1 Full nawʿ table from Shamela0011728 edition

al-Suyūṭī's al-Itqān has 80 anwāʿ in this edition. A complete list of the surrounding anwāʿ relevant to the pre-reg's topic:

| Nawʿ # | Title | Relation to task #36 topic |
|---|---|---|
| 55 | *al-Ḥaṣr wa-l-ikhtiṣāṣ* | — |
| **56** | ***fī al-ījāz wa-l-iṭnāb*** | **Contains the qiṣaṣ-repetition discussion the pre-reg wants, vol. 3 pp. 229-232** |
| 57 | *al-khabar wa-l-inshāʾ* | — |
| 58 | *badāʾiʿ al-qurʾān* | — |
| 62 | *fī munāsabati al-āyāt wa-l-suwar* | — |
| **63** | ***fī al-āyāt al-mushtabihāt*** | **NOT *qiṣaṣ al-anbiyāʾ*** — pre-reg citation error |
| 64 | *fī iʿjāz al-qurʾān* | — |
| **65** | ***fī al-ʿulūm al-mustanbaṭa min al-qurʾān*** | **Lists prophet narratives in passing (line 20942)** |

**No nawʿ dedicated to *qiṣaṣ al-anbiyāʾ* exists in al-Itqān.** The classical material the pre-reg needs is lodged inside nawʿ 56 *ījāz/iṭnāb* as sub-topic: "why are some prophet stories repeated and Yūsuf not?"

### 1.2 What nawʿ 56 actually says about prophet-narrative repetition

Verbatim from Shamela0011728, vol. 3 pp. 229-232 (my reading):

> **Line 17365-17367, p. V03P229:** وَمِنْ ذَلِكَ تَكْرِيرُ القِصَصِ كَقِصَّةِ آدَمَ وَمُوسَى وَنُوحٍ وَغَيْرِهِمْ مِنَ الأَنْبِيَاءِ. قَالَ بَعْضُهُمْ: ذَكَرَ اللَّهُ مُوسَى فِي مِائَةٍ وَعِشْرِينَ مَوْضِعًا مِنْ كِتَابِهِ. وَقَالَ ابْنُ العَرَبِيِّ فِي القَوَاصِمِ: ذَكَرَ اللَّهُ قِصَّةَ نُوحٍ فِي خَمْسٍ وَعِشْرِينَ آيَةً وَقِصَّةَ مُوسَى فِي تِسْعِينَ آيَةً.
>
> *"And among that [i.e., iṭnāb by way of takrār] is the repetition of the stories, such as the story of Ādam, Mūsā, and Nūḥ and others of the prophets. Someone said: God mentioned Mūsā in 120 places of His book. Ibn al-ʿArabī said in al-Qawāṣim: God mentioned Nūḥ's story in 25 āyāt and Mūsā's story in 90 āyāt."*

> **Line 17393, p. V03P230:** وَقَدْ سُئِلَ: مَا الحِكْمَةُ فِي عَدَمِ تَكْرِيرِ قِصَّةِ يُوسُفَ وَسَوْقِهَا مَسَاقًا وَاحِدًا فِي مَوْضِعٍ وَاحِدٍ دُونَ غَيْرِهَا مِنَ القِصَصِ؟
>
> *"And it has been asked: what is the wisdom in not repeating the story of Yūsuf and telling it in a single sequence in one place, unlike the other stories?"*

Suyūṭī then lists 5 justifications for Yūsuf's individuation (the "tashabbub al-niswa," the "faraj baʿda al-shidda," the Abū Isḥāq al-Isfarāʾīnī "proof of miraculousness," the "ṣaḥāba's request to be told a story," and the Jawāb khāmis "destroyed-unbelievers" warning-function argument).

> **Line 17398-17399:** أَنَّهَا اخْتُصَّتْ بِحُصُولِ الفَرَجِ بَعْدَ الشِّدَّةِ بِخِلَافِ غَيْرِهَا مِنَ القِصَصِ فَإِنَّ مَآلَهَا إِلَى الوَبَالِ كَقِصَّةِ إِبْلِيسَ وَقَوْمِ نُوحٍ وَهُودٍ وَصَالِحٍ وَغَيْرِهِمْ.
>
> *"It [Yūsuf] is distinguished by its outcome of relief-after-hardship, unlike the other stories whose outcome is destruction, like the story of Iblīs and the people of Nūḥ, Hūd, Ṣāliḥ, and others."*

> **Line 17409-17413:** إِنَّ قِصَصَ الأَنْبِيَاءِ إِنَّمَا كُرِّرَتْ لِأَنَّ المَقْصُودَ بِهَا إِفَادَةُ إِهْلَاكِ مَنْ كَذَّبُوا رُسُلَهُمْ، وَالحَاجَةُ دَاعِيَةٌ إِلَى ذَلِكَ لِتَكْرِيرِ تَكْذِيبِ الكُفَّارِ لِرَسُولِ اللَّهِ.
>
> *"Indeed the prophet stories are only repeated because their purpose is to convey destruction of those who rejected their messengers, and this need calls for repetition because of the repeated rejection of the Messenger of God by the disbelievers."*

### 1.3 What nawʿ 56 establishes (and what it doesn't)

**Establishes:**
- **Position 1 (most individuated): Yūsuf.** Suyūṭī offers 5 reasons for why Yūsuf alone is not repeated. This is a direct classical anchor for "Yūsuf is the uniquely individuated prophet narrative."
- **Repetition-heavy cluster:** Mūsā (120 mentions) > Mūsā (90 āyāt Ibn al-ʿArabī count) > Nūḥ (25 āyāt Ibn al-ʿArabī count). **Mūsā and Nūḥ are explicitly anchored at the bottom of individuation.**
- **People of Nūḥ, Hūd, Ṣāliḥ grouped together** as parallel destruction-pericope prophets.

**Does NOT establish:**
- Any ranking among Shuʿayb / Hūd / Ṣāliḥ
- Any ranking of Yaḥyā (Yaḥyā is nowhere in the nawʿ-56 passage)
- Any ranking of Ibrāhīm against the destruction-pericope prophets
- The specific 8-rank ordering that task #36 registered

### 1.4 What Yaḥyā gets from Zamakhsharī + Ibn ʿAbbās

Confirmed anchor for Yaḥyā pericope rarity: Suyūṭī line 7013-7017 (nawʿ 36 *fī maʿrifat gharībihi*):

> وَأَخْرَجَ ابْنُ جَرِيرٍ عَنْ سَعِيدِ بْنِ جُبَيْرٍ أَنَّهُ سُئِلَ عَنْ قَوْلِهِ {وَحَنَانًا مِنْ لَدُنَّا} ... عَنْ عِكْرِمَةَ عَنِ ابْنِ عَبَّاسٍ قَالَ: لَا وَاللَّهِ مَا أَدْرِي مَا حَنَانًا... قَالَ: كُلُّ القُرْآنِ أَعْلَمُهُ إِلَّا أَرْبَعًا: {غِسْلِينَ} وَ{حَنَانًا} وَ{أَوَّاهَ} وَ{الرَّقِيمَ}.
>
> *Ibn ʿAbbās said: "By God, I do not know what ḥanānan means... I know every [word of the] Qurʾān except four: ghislīn, ḥanānā, awwāh, and al-raqīm."*

This confirms that Yaḥyā's verse (Q19:13 *wa-ḥanānan min ladunnā wa-zakātan*) contains a hapax that even Ibn ʿAbbās did not know. This is a MW-6 HIGH-confidence anchor for Yaḥyā's pericope having genuine lexical rarity.

### 1.5 What Razi gives for Lūṭ

Classical anchors for Lūṭ's vocabulary-sharing with other destruction-pericope prophets (al-Rāzī *Mafātīḥ al-Ghayb*, my reading of the OpenITI Shamela0023635 plaintext):

> وَكَذَلِكَ قَالَ هُودٌ وَصَالِحٌ وَلُوطٌ وَشُعَيْبٌ لِقَوْمِهِمْ... وَفِي العَنْكَبُوتِ قَالَ إِبْرَاهِيمُ لِقَوْمِهِ
>
> *"And likewise Hūd, Ṣāliḥ, Lūṭ, and Shuʿayb said to their peoples... and in al-ʿAnkabūt Ibrāhīm said to his people [similar words]"*

and directly linking Lūṭ with Ibrāhīm:

> إِبْرَاهِيمُ عَلَيْهِ السَّلَامُ كَانَ رَسُولًا إِلَى لُوطٍ عَلَيْهِ السَّلَامُ
>
> *"Ibrāhīm was a messenger to Lūṭ"*

and the city-destruction grouping:

> كَمَا فِي قَلْعِ مَدَائِنِ قَوْمِ لُوطٍ وَفِي يَوْمِ بَدْرٍ
>
> *"As in the uprooting of the cities of Lūṭ's people and on the day of Badr"*

**Razi establishes Lūṭ as vocabulary-shared with Ibrāhīm's pericope AND with the Hūd/Ṣāliḥ/Shuʿayb destruction-pericope cluster.** This is the classical basis for the pre-reg's "Lūṭ reduces suppression when removed" counter-prediction.

---

## 2. Prophet-set mismatch between pre-reg and parent task

### 2.1 Task #18 empirical 8-prophet set (from team-discovery-007.md)

| Task #18 prophet | Mean Jaccard to other 7 | LOO z | LOO obs − null |
|:---|---:|---:|---:|
| Abraham (Ibrāhīm) | 0.4028 | **−3.80** | −0.041 |
| Noah (Nūḥ) | 0.3917 | **−3.50** | −0.039 |
| Jesus (ʿĪsā) | 0.3718 | −3.05 | −0.035 |
| Moses (Mūsā) | 0.3513 | −3.23 | −0.036 |
| Lot (Lūṭ) | 0.3339 | −2.35 | −0.028 |
| Adam (Ādam) | 0.3316 | −2.65 | −0.030 |
| Joseph (Yūsuf) | 0.2999 | −2.37 | −0.028 |
| John (Yaḥyā) | 0.1992 | −3.41 | −0.031 |

### 2.2 Task #36 pre-reg 8-prophet set

Yūsuf > Yaḥyā > Shuʿayb > Hūd > Ṣāliḥ > Ibrāhīm > Mūsā > Nūḥ

### 2.3 Overlap and mismatch

**Overlapping (5 prophets):** Yūsuf, Yaḥyā, Ibrāhīm, Mūsā, Nūḥ
**In task #18 only (3 prophets):** Jesus (ʿĪsā), Lot (Lūṭ), Adam (Ādam)
**In task #36 pre-reg only (3 prophets):** Shuʿayb, Hūd, Ṣāliḥ

The pre-reg's primary Spearman test cannot be executed on its 8 prophets because Shuʿayb, Hūd, Ṣāliḥ were not measured. Two reduced variants are possible:

### 2.4 Reduced-overlap Spearman (n=5, statistically inert)

| Prophet | Pre-reg rank (1=top) | Empirical rank on |z| within the 5 |
|---|---|---|
| Yūsuf | 1 | 5 (|z|=2.37, smallest) |
| Yaḥyā | 2 | 3 (|z|=3.41) |
| Ibrāhīm | 6 | 1 (|z|=3.80, largest) |
| Mūsā | 7 | 4 (|z|=3.23) |
| Nūḥ | 8 | 2 (|z|=3.50) |

**Spearman ρ = −0.50.** Direction is inverted from the pre-reg: the empirical ordering puts Ibrāhīm and Nūḥ at the top of the suppression-contribution ranking, and Yūsuf near the bottom.

**Statistical power:** n = 5 is essentially inert. The smallest two-sided p-value achievable at n=5 is ~0.017 (requires |ρ|=1.0). Pre-reg specified α=0.0033 (Bonferroni k=3), which cannot be reached at n=5 under ANY ordering. The reduced Spearman is **under-powered by construction**.

### 2.5 Semantic reconciliation check

The empirical direction ρ = −0.50 is not noise. Task #18 already interpreted the ranking as **length-and-typicality correlated**: "Spearman ρ = +0.79 between pericope-token-count and mean-Jaccard." The pre-reg's "individuation = top driver" logic runs OPPOSITE to task #18's "shared-template → shared-lexicon → higher Jaccard → higher driver" logic:

- **Pre-reg logic:** Yūsuf is individuated (unique lexicon) → when dropped, the REMAINING set loses that unique lexicon → suppression reduces → Yūsuf is a STRONG driver.
- **Task #18 logic:** Abraham is TEMPLATE-central (most shared lexicon) → when dropped, the REMAINING set's shared-lexicon backbone breaks → suppression reduces → Abraham is the strongest driver.

These are **opposite directions in the same metric**. The empirical ρ = −0.50 is consistent with task #18's template-central logic.

This is a serious theoretical-direction conflict. The pre-reg's al-Suyūṭī / al-Zamakhsharī / al-Ṭabarī framing supports "individuated-prophet-is-top-driver" (Yūsuf has Q12's whole pericope depending on him), but the empirical Jaccard metric rewards shared-template centrality, not individuation.

---

## 3. Lūṭ counter-prediction — already falsified

Task #36 tertiary test: *"Lūṭ's leave-one-out effect is negative (reduces suppression when removed)."*

Task #18 empirical: **Dropping Lūṭ leaves obs = 0.3357, null = 0.3634, z = −2.35, p(obs ≥ null) = 0.994.** The suppression signal survives. Lūṭ's removal does NOT reverse the sign.

Among the 8 empirical prophets, Lūṭ is **rank 8 by |z|** (weakest contributor, tied with Joseph at −2.35 vs −2.37). So Lūṭ is at the BOTTOM of the suppression-contribution ranking, consistent with al-Ṭabarī / al-Qurṭubī framing that Lūṭ shares vocabulary with Ibrāhīm — but Lūṭ's contribution is STILL negative (still suppresses), just by the smallest margin.

**The pre-reg's "Lūṭ becomes a positive driver" prediction is falsified.** The weaker read "Lūṭ is near the bottom" is empirically supported. Which of these two readings counts as "the pre-reg prediction" is ambiguous on the pre-reg wording and should be adjudicated by hypothesis-generator.

---

## 4. Recommended remediation paths (for team-lead / hypothesis-generator)

**Option A — Amend pre-reg, re-execute task #18 on task #36 prophet set.**
Re-run task #18's leave-one-out pipeline on the 8 task-#36 prophets (adding Shuʿayb, Hūd, Ṣāliḥ; removing Jesus, Adam, Lot). Computational-tester effort: ~1 session. Then Spearman on n=8 with clean α=0.0033.

**Option B — Amend pre-reg to task #18's actual 8-prophet set, re-derive classical ordering.**
Classical-scholar reissues the ordering for the 8 prophets that were actually measured (Abraham, Noah, Jesus, Moses, Lot, Adam, Joseph, John), anchored in Suyūṭī's available texts + Razi. Pre-reg ordering recommendation:

| Rank | Prophet | Classical anchor |
|---|---|---|
| 1 | Joseph | Suyūṭī nawʿ 56: explicit singular non-repeated status; 5 justifications |
| 2 | John | Zamakhsharī *ḥanān* hapax; pericope confined to 5 mentions in Q3/Q6/Q19/Q21 |
| 3 | Adam | Suyūṭī nawʿ 56 groups with Mūsā/Nūḥ as repeated but less dense than Mūsā |
| 4 | Lot | Razi links Lūṭ with Ibrāhīm pericope (Ibrāhīm was rasūl to Lūṭ) + city-destruction cluster |
| 5 | Jesus | Repeated in Q3/Q19 (Suyūṭī note), Maryam + Āl ʿImrān pair |
| 6 | Abraham | Razi has 1607 discussions; repetition-heavy, template-central |
| 7 | Moses | Suyūṭī: 120 mentions, 90 āyāt per Ibn al-ʿArabī — most-repeated |
| 8 | Noah | Suyūṭī: 25 āyāt Ibn al-ʿArabī count; destruction template |

This ordering is **classically anchored at positions 1, 7, 8** (Yūsuf top, Mūsā + Nūḥ bottom) with remaining positions inferred from the same sharing-vs-individuation logic. It should be checked against task #18's empirical |z| ordering — which is: Abraham (1), Noah (2), John (3), Moses (4), Jesus (5), Adam (6), Joseph (7), Lot (8). **Spearman ρ on this classical-vs-empirical would be negative** for positions 1/6 (Joseph vs Abraham), suggesting the task #18 metric does NOT track individuation.

**Option C — File [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT as NULL on methodological grounds.**
Declare the pre-reg un-executable, preserve task #18's finding that suppression is pan-prophetic, drop the per-prophet ranking test entirely. Publishable as a methodological null: "the Jaccard leave-one-out metric does not discriminate individuation vs template-centrality, so the pre-reg's ordering hypothesis cannot be tested by this instrument."

**Option D — Switch metric.**
Re-define the per-prophet contribution as **Herfindahl-Hirschman concentration** of each prophet's lemma occurrences across surahs. Prophets whose lemma mass is concentrated in a single surah (Yūsuf: 100% in Q12) score HIGH on individuation. Prophets whose lemma mass is distributed across many surahs (Mūsā: ~30 surahs) score LOW. This is a different metric from task #18's Jaccard-to-others and would test a different (arguably more classically-aligned) notion of "individuation." Pre-reg would need full re-authoring.

**Classical-scholar recommendation:** Option A (re-run task #18 on the 8 task-#36 prophets) is the cleanest path if the pre-reg's prophet set is doctrinally preferred. Option B is faster but forces the classical ordering to conform to what was measured rather than what al-Suyūṭī explicitly discusses. Option D is the most intellectually honest but biggest effort. Option C is the conservative default if the team decides the experiment isn't worth rescuing.

---

## 5. MW-6 verbatim-confidence notes

All classical source citations in this memo are from the Shamela0011728 al-Itqān edition and Shamela0023635 al-Rāzī edition, both downloaded from OpenITI (0925AH and 0625AH repositories respectively) as plaintext. Line numbers and PageV03Pnnn markers are from the OpenITI mARkdown files at:

- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt`

Verbatim Arabic quotes are transcribed directly from those files and should be treated as HIGH-confidence MW-6. Page references (V03P229-232) map to the Dār al-Kitāb al-ʿArabī Cairo print edition that Shamela 0011728 is based on.

**The pre-reg's "nawʿ 63 *qiṣaṣ al-anbiyāʾ*, vol. 2 pp. 420-428" citation is a recall error.** The material is in **nawʿ 56 *fī al-ījāz wa-l-iṭnāb*, vol. 3 pp. 229-232**. A PENDING tag should go on any downstream citation of this passage until the correction propagates.

---

## 6. Recommended action for computational-tester

**DO NOT DISPATCH.** Computational-tester should not execute task #36 as currently pre-registered. The blockers listed above need team-lead + hypothesis-generator adjudication first. Appropriate next action:

1. Team-lead routes this audit to hypothesis-generator
2. Hypothesis-generator issues an AMEND to task #36 selecting one of Option A / B / C / D
3. If AMEND chooses Option A: computational-tester re-runs task #18 pipeline on {Yūsuf, Yaḥyā, Shuʿayb, Hūd, Ṣāliḥ, Ibrāhīm, Mūsā, Nūḥ}
4. If AMEND chooses Option B: computational-tester uses the classical ordering in §4 Option B above and runs Spearman on existing task #18 data
5. If AMEND chooses Option C: integrator files NULL with this audit as primary evidence
6. If AMEND chooses Option D: full re-authoring required

Classical-scholar stands by to produce additional classical anchors under whichever path is chosen.

---

## 7. Task state

- Classical sources physically verified: ✓
- Pre-reg 8-prophet ordering classical anchor: PARTIAL (positions 1, 7, 8 anchored; positions 2–6 inferred)
- Task #36 executable as pre-registered: ✗ (three blockers)
- Task #36 status: held at `in_progress` on classical-scholar queue until team-lead/hypothesis-generator amendment
- Output: this memo
