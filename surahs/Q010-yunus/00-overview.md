---
surah: 10
surah_name_ar: يونس
surah_name_translit: Yūnus
surah_name_english: Jonah
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all 8 template files + JOURNAL produced 2026-04-28; classical-claims audit produced 10 verdicts (6 VINDICATED / 2 FALSIFIED / 1 DIRECTIONAL / 1 RULES-TUPLE-FRAGILE / 0 DATA-GAP); novel findings landed 2 CONFIRMED (Q010-F-01, Q010-F-04) / 2 NULL (Q010-F-02 main + Q010-F-03 pre-commit-violation; Q010-F-02 PULLED-IN sub-finding); key Q 10 finding: Q 10 is empirically a *thesis-named* prophet-surah (yūnus-token concentration 50%, 1× in surah at v. 98) sitting at the 4th-most-expensive canonical adjacency in the mushaf (Q 9 → Q 10 = 3.73% of TSP residual), with Q 10:62 as the corpus's foundational *walāya* verse and semantic hub of a 12-verse fear-not-grief-not network — partial-vindicating al-Khaṭṭābī's *iʿjāz al-maʿnā* even where al-Bāqillānī's window-level *iʿjāz al-fawāṣil* is FALSIFIED for the surah (sig_A rank 102/114).
---

# Q 10 Yūnus — Overview


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
| Surah ID | 10 | canonical |
| Arabic name | يونس | canonical |
| Transliteration | Yūnus | canonical |
| English meaning | "Jonah" (the prophet's name) | classical |
| Verse count | 109 | Hafs-Kufan (`data/hafs-verse-counts.tsv`) |
| Position in mushaf | 10 | canonical |
| Type | Meccan; **Late Meccan** per Nöldeke (phase 84) | `data/revelation-order.csv` row 51 |
| Position in revelation order (al-Suyūṭī chronology) | **51 of 114** | `data/revelation-order.csv` |
| Word count (no-tashkeel) | 1,964 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel) | 7,714 | computed |
| Opening | الر ۚ تلك آيات الكتاب الحكيم — "ALR. These are the verses of the Wise Book." | muqaṭṭaʿāt + book-reference |
| Bismala | counted as part of v.1 only when conventionally prefixed; rules-tuple default = NOT counted (basmala-counted-only-in-Q1) | rules tuple |

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, on Q 10's verse-count: "yūnus: mi'a wa-ʿashra wa-qīla illā āya" — "[verses are] one hundred and ten, and it has been said all-but-one" (`data/literature/classical-tafsir/raw/suyuti-itqan-openiti-Q010.txt` line 17). The Hafs-Kufan reckoning is 109; Basran reckoning is 110.

## 2. Classical names and identifications

- **Yūnus** (يونس) — the canonical name; the prophet whose people are uniquely-mentioned at v. 98 as the only nation that successfully repented before punishment struck (per ibn Kathīr citing Qatāda; `data/literature/classical-tafsir/raw/ibn-kathir-openiti-Q010.txt` line 1434).
- **al-Sābiʿa fī al-sabʿ al-ṭiwāl** ("the seventh of the seven long [surahs]") — al-Suyūṭī classifies Q 10 as the seventh of the seven long surahs (Q 2-7 + Q 10 if barāʾa+anfāl are joined as one) (`suyuti-itqan-openiti-Q010.txt` line 16). al-Biqāʿī adds: "if [we count] al-Anfāl + Barāʾa as one of the long, then this is the first of the al-miʾīn (the surahs that exceed 100 verses)."

## 3. Opening formula — muqaṭṭaʿāt + book-reference

Q 10 opens with the **ALR muqaṭṭaʿāt** + book-reference *tilka āyātu al-kitābi al-ḥakīm* ("These are the verses of the Wise Book"). This is the canonical cross-finding-008 pattern: muqaṭṭaʿāt → book-reference. Variant on Q 12 (which uses *al-mubīn* "Clear") and Q 13 (which uses *Allāh-revealing* book reference).

Q 10 is a member of the **ALR letter-family cluster** = {Q 10, Q 11, Q 11b (Hūd), Q 12 Yūsuf, Q 14 Ibrāhīm, Q 15 al-Ḥijr}. H-NEW-600 found this cluster NULL on whole-surah FR-cohesion (56.25%ile). H-NEW-97 found 4/5 PROPHET_PERSON name-class membership (p=0.006).

## 4. Why is Q 10 named after Yūnus?

This is the central interpretive question. Q 10 contains:
- **109 verses**.
- Yūnus's people (*qawm yūnus*) explicitly mentioned in **a single verse: v. 98** (~ 1% of the surah).
- The token *yūnus* itself occurs **once** in the surah (Q 10:98). Its only other occurrence in the whole Quran is at Q 37:139 (al-Ṣāffāt).

Compare Q 12 Yūsuf (entire surah is one continuous narrative; *yūsuf* appears 20× in Q 12, 95.24% concentration of all corpus occurrences). The two namesake-surahs are STRUCTURALLY OPPOSITE.

al-Biqāʿī's *Naẓm al-Durar* (`biqai-openiti-Q010.txt` lines 1-13) gives the answer at the surah-opening: the *maqṣūd* (intent) of Q 10 is **to demonstrate that the Book is from God**. The *proof* (argument, dalīl) for this is the story of *qawm Yūnus* — the only people in history whose mass repentance averted divinely promised punishment. al-Biqāʿī writes: *"and this is decisively-clear evidence that the One who brought it [the Book/punishment-warning] is God whom they believed in — for had it been other than Him, their belief would have been a cause for affliction"*.

Thus the surah is named **for the climactic theological-evidentiary moment**, not for narrative density. The eponymity is thematic-teleological, not narrative-quantitative. This is structurally distinct from Q 12 (where the entire surah IS the narrative) and resembles instead Q 19 Maryam (named for a single key episode).

## 5. Length classification

109 verses, 1,964 words, 7,714 letters — **mid-length Meccan; longest of the late-Meccan ALR cluster**. Q 10 is NOT in al-mufaṣṣal; al-Suyūṭī places it as the seventh of *al-sabʿ al-ṭiwāl* (or as the first of *al-miʾīn* under the Anfāl+Barāʾa-joined reckoning).

Position s=10 places Q 10 in the head-mushaf zone, well before the s=50 Hijra-kink.

## 6. Rhyme structure

Final-letter distribution across 109 verses (computed from `quran-text/quran-min-tashkeel.json`):
- **ن (nūn): 98 verses (89.9%)** — extreme dominance; near-monorhyme on -ūn / -īn / -ān endings.
- م (mīm): 10 verses (9.2%)
- ل (lām): 1 verse (0.9%)

Rhyme entropy (Shannon, nats): **0.358** (per H-NEW-700) — second-lowest in the corpus. The -ūn/-īn cadence is sustained throughout.

al-Suyūṭī notes the surah's *rāʾ*-letter saturation: *"Q 10 has more than two hundred occurrences of the letter rāʾ"* (`suyuti-itqan-openiti-Q010.txt` line 23). This is consonantal (not rhyme-final) but contributes to a cluster-wide ALR-family phonological signature.

## 7. Empirical architectural profile (preview — see 01-empirical-profile.md)

- **UAS rank**: **8/114** (UAS = 3.479).
- **Outlier-strength Δ**: **−7.83pp** — WEAK_ANCHOR (Q 10 is mildly cohesion-positive — i.e., its presence STRENGTHENS the corpus's mean cohesion structure).
- **iʿjāz sig_A**: −1.978 (rank 102/114) — VERY LOW. Q 10 wins UAS via canonical-adjacency (Q9-Q10 = 4th most-expensive transition in the corpus) NOT iʿjāz al-fawāṣil. The near-monorhyme + very-uniform content makes Q 10 anti-iʿjāz at the window-level.
- **Q9-Q10 canonical-adjacency cost**: **0.309** = **3.73% of the total mushaf TSP residual** = **rank 4/113 most-expensive adjacency**. Only Q1-Q2, Q32-Q33, Q33-Q34 cost more.
- **Q10-Q11 cost**: 0.030 (rank ~80; cheap — natural ALR-cluster transition).
- **Mean content distance to corpus**: 1.048 (z=+1.23 above corpus mean — content-distinct).

**Q 10 is content-distinctively-anchored, in the prophet-narrative ALR cluster, with EXTREME asymmetric canonical cost — expensive on the Q 9 boundary, cheap on the Q 11 boundary.** This asymmetry is itself a finding: the Q 9 → Q 10 transition is a chronology-block boundary (Q 9 is the LAST-revealed surah; Q 10 is mid-Meccan) and is structurally costly, while the Q 10 → Q 11 transition is within the ALR cluster and is structurally seamless.

## 8. Quick content structure

Q 10 is **not** a continuous narrative; it is a **theological-polemical late-Meccan discourse with embedded narrative anchors**. Major thematic blocks:

- vv. 1-2: ALR opening; book-reference *al-ḥakīm*; *qadam ṣidq* and the disbelievers' *sāḥir mubīn* charge.
- vv. 3-10: cosmological signs (six-day creation, ʿarsh, sun-as-ḍiyāʾ moon-as-nūr); the Reckoning; reward/punishment paired contrast.
- vv. 11-23: God's mercy vs human ingratitude; the false-gods who "intercede"; *al-fulk* (ship) parable.
- vv. 24-30: the dunyā as a deceptive crop (*ka-māʾin anzalnāhu min al-samāʾ*); the *dār al-salām* call; the Day of Reckoning with witnesses.
- vv. 31-36: rhetorical *qul* questions on God's lordship; idolatry's incoherence.
- vv. 37-44: the *iftirāʾ* charge against the Quran; *fa'tū bi-sūratin mithlihī* challenge (one of the iʿjāz-tahaddī verses).
- vv. 45-56: Day-of-Resurrection scenarios; *kullā* refrains.
- vv. 57-67: the awaited mercy; **Q 10:62 awliyāʾ Allāh — the foundational walī-passage**; sea-storm-prayer narrative.
- vv. 68-70: refutation of "God has a son" claim.
- vv. 71-74: **Nūḥ narrative** (compressed); his people's destruction.
- vv. 75-93: **Mūsā + Pharaoh narrative** (mid-length); the *sāḥir* duel; Pharaoh's drowning + deathbed-faith rejection; Banū Isrāʾīl's settlement.
- vv. 94-97: *fa-in kunta fī shakkin* — comfort/admonition to the Prophet himself (rare iltifāt to Muḥammad).
- v. 98: **the Yūnus moment** — *qawm Yūnus* as the unique exception.
- vv. 99-103: *wa-law shāʾa rabbuka* (predestination); *fa-hal yantaẓirūna illā mithla ayyāmi alladhīna khalaw min qablihim*.
- v. 101: *qul unẓurū mādhā fī al-samāwāti wa-l-arḍ* — cosmic-call closer.
- vv. 104-109: closing — *qul yā ayyuhā al-nās in kuntum fī shakkin min dīnī*; *wa-ittabiʿ mā yūḥā ilayka wa-ṣbir ḥattā yaḥkuma allāh*.

## 9. Connection to ALR-cluster & cross-findings

H-NEW-97 found ALR cluster (Q 10, 11, 12, 14, 15) has 4/5 PROPHET_PERSON name-class (p=0.006). Q 10's role in the cluster: **the cluster's theological-polemical anchor**. While Q 12 is pure-narrative (Yūsuf), Q 11 is a sequence of warner-narratives (Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb), and Q 14 is a single-prophet pair (Ibrāhīm + Mūsā), Q 10 is the cluster's **discursive frame** — the surah that argues *why* the Book is true and treats the prophet-narratives as ratifying evidence.

Q010-F-02 (this investigation) NULL-replicated H-NEW-600 on full-cluster cohesion (perm-p=0.61), but found Q 10's mean FR distance to ALR siblings (0.914) IS LOWER than to non-ALR (1.053) — a weak local pull-in (PULLED-IN). Q 10 is empirically a cluster-internal node despite the cluster-wide NULL on FR-cohesion.

## 10. Cross-references (high-level)

- [[h-new-590-outlier-spectrum]] — Q 10 −7.83pp WEAK_ANCHOR.
- [[h-new-840-unified-architectural-score]] — UAS rank 8/114.
- [[h-new-720-canonical-adjacency-cost]] — Q9-Q10 = rank 4/113 most-expensive (0.309 = 3.73% of residual).
- [[h-new-750-per-surah-iʿjāz-signature]] — sig_A = −1.978, rank 102/114 (anti-iʿjāz at window level).
- [[h-new-700-phonological-compression-tail]] — rhyme entropy 0.358 (very low).
- [[h-new-600-letter-families]] — ALR-5 NULL at 56.25%ile (replicated by Q010-F-02).
- [[h-new-97]] — ALR-PROPHET_PERSON 4/5 partial.
- [[Q012-yusuf/00-overview|Q 12 Yūsuf]] — eponymity-asymmetry contrast.
- [[Q009-al-tawba/00-overview|Q 9 al-Tawba]] — Q9-Q10 boundary specialist.
- [[cross-finding-008]] — Q 10 ALR + book-reference (prototypical with Q 12, Q 13, Q 26).

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md (109 verses)
- [x] 03-tafsir-survey.md (≥5 mufassirūn)
- [x] 04-hadith-corpus.md (139 raw hits scanned across 9 books; filtered to ~10 prophet-Yūnus hadith)
- [x] 05-classical-claims-audit.md (≥5 claims)
- [x] 06-novel-findings.md (4 pre-registered tests; 2 CONFIRMED, 1 NULL, 1 NULL-with-PULLED-IN-secondary)
- [x] 07-cross-references.md
- [x] JOURNAL.md
