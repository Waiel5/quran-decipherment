---
surah: 56
surah_name_ar: الواقعة
surah_name_translit: al-Wāqiʿa
surah_name_english: The Inevitable Event / The Imminent
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: SCAFFOLD-COMPLETE — 5 novel tests pre-registered & executed (1 STRONGLY VINDICATED, 1 VINDICATED, 3 NULL with prominence)
---

# Q 56 al-Wāqiʿa — Overview


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
| Surah ID | 56 | canonical |
| Arabic name | الواقعة | canonical |
| Transliteration | al-Wāqiʿa | canonical |
| English meaning | "The Inevitable Event" / "The Imminent" / "The Befalling" | derived from v1 *idhā waqaʿat al-wāqiʿa* |
| Verse count | 96 | Hafs-Kufan (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, q[55]['total_verses']) |
| Position in mushaf | 56 | canonical |
| Type | Meccan (predominant view: Ḥasan, ʿIkrimah, Jābir, ʿAṭāʾ); 1-4 Medinan exceptions per minority views (Ibn Qutayba: Q 56:82; al-Kalbī: 56:81-82, 13-14, 39-40) | al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, intro to sūra (`spa5k-tafsir-api/ar-tafseer-al-qurtubi/56/1.json`) |
| Position in revelation order | **46 of 114** (Tanzīl Egyptian Standard); **41** (Nöldeke) — Early Meccan | `data/revelation-order.csv` row 46 |
| Word count (no-tashkeel) | **380** (own count), **379** (after stripping ۞ ornament markers) | computed |
| Letter count (no-tashkeel, includes whitespace-stripped graphemes) | 1,757 | computed |
| Opening | إذا وقعت الواقعة — "When the Inevitable befalls" | direct conditional-temporal |
| Bismala | counted as separator only (not v1 in this surah) | rules-tuple default |
| Length classification | mufaṣṣal-ṭiwāl (the "long mufaṣṣal" — al-Zarkashī's first sub-tier of mufaṣṣal) | al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on al-mufaṣṣal |

## 2. Classical names and structural identity

- **al-Wāqiʿa** (الواقعة) — canonical, from v1.
- **One of the "5 surahs that aged the Prophet"** — per al-Tirmidhī #3381 (ḥasan gharīb): the Prophet identified Hūd, al-Wāqiʿa, al-Mursalāt, ʿAmma yatasāʾalūn (Q 78), and Idhā ʾl-shamsu kuwwirat (Q 81) as the surahs whose intensity made him gray.
- **The "Sūrat al-Faqr" surah** — by association with the contested Ibn Masʿūd hadith *man qaraʾa sūrat al-Wāqiʿa kulla layla lam tuṣibhu fāqatun abadan*. The classical chain is recorded by Ibn Kathīr citing **Ibn ʿAsākir → al-Sarī b. Yaḥyā → Shujāʿ → Abū Ẓabya → Ibn Masʿūd**. The chain is **graded ḍaʿīf** by al-Bayhaqī (in *Shuʿab al-Īmān*) and **MUNKAR** by al-Albānī (*Silsilat al-Aḥādīth al-Ḍaʿīfa* #290) on grounds that Shujāʿ and Abū Ẓabya are *majhūl* (unidentified). The honorific "every-night-recitation" tradition is empirically PRESENT in classical literature but the chain-strength claim is FALSIFIED at canonical-strength. See `05-classical-claims-audit.md` Claim 2.

## 3. ⭐ Unique structural feature — the 3-CLASS RING ARCHITECTURE

Q 56 is the **only surah in the corpus with an explicit 3-class human-classification architecture** that is *named, partitioned, described separately, and recapitulated*:

**Block A — Day of Judgment (vv 7-56) — full descriptions:**
- *azwāj thalātha* (v 7) — "you (humanity) are three classes"
- A.1 *al-Sābiqūn al-Sābiqūn* / *al-muqarrabūn* (vv 10-26) — paradise of nearness
- A.2 *Aṣḥāb al-Yamīn* (vv 27-40) — paradise of the right hand
- A.3 *Aṣḥāb al-Shimāl* / *al-mashʾama* (vv 41-56) — hellfire / al-zaqqūm

**Block B — Death-moment (vv 88-94) — abbreviated 3-class scenario at death:**
- B.1 *fa-ammā in kāna min al-muqarrabīn* (vv 88-89)
- B.2 *wa-ammā in kāna min aṣḥāb al-yamīn* (vv 90-91)
- B.3 *wa-ammā in kāna min al-mukadhdhibīn al-ḍāllīn* (vv 92-94)

This **3-class ring** (A → middle blocks → B) is **structurally unique to Q 56** in the canonical mushaf. The class-LABELS recur (al-muqarrabūn, aṣḥāb al-yamīn) — but the lexical-overlap of full content vocabulary between A and B blocks is NOT statistically significant under permutation null (see `06-novel-findings.md` Q056-F-01).

## 4. Empirical architectural profile

(full detail in `01-empirical-profile.md`)

| Metric | Value | Source |
|:--|:--|:--|
| **UAS rank** | **75/114** | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | **+1.33 pp** (WEAK_OUTLIER) | h-new-590, all_surahs_results X=56, window 53-59 |
| iʿjāz sig_A | **−0.0567** (rank ~63/114, near-corpus-median) | h-new-750 |
| iʿjāz sig_B | +0.0612 (rank 58/114) | h-new-750 |
| Mean FR-content distance | **1.0202** (corpus mean 0.9235; **Q56 rank 92/114 by mean-dist** — content-DISTANT, not central) | h-new-111 |
| Rhyme entropy (nats) | 1.266 (corpus median range; close to 1.31 own count) | h-new-750 |
| Top final-letter | ن (nūn), 57.9% | h-new-750 |
| Q55→Q56 adjacency cost | **0.0949** (1.14% of TSP residual) | h-new-720 |
| Q56→Q57 adjacency cost | **0.2274** (**2.74% of TSP residual** — moderately expensive) | h-new-720 |
| Architectural cell | **Hijra-kink boundary surah** — closest to corpus's Meccan/Medinan structural transition | cross-finding-026 §5 |

**Q 56 is structurally MID-PACK on UAS but content-DISTANT on FR-content** (rank 92/114). Its architectural significance is NOT outlier-driven (unlike Q 33, Q 1, Q 24, Q 9) but is **boundary-driven**: it is the LAST Meccan surah before the Medinan al-Ḥadīd / al-Mujādila / al-Ḥashr / al-Mumtaḥana sequence. The Q56→Q57 canonical adjacency cost (rank 17/113) reflects the Hijra-kink chronology jump, which al-Suyūṭī's *al-Itqān* identifies as the central Meccan/Medinan structural division empirically locked at s=50 in the project's compression-tail law (cross-finding-026 §2).

## 5. Opening formula — temporal-conditional eschatology

Q 56 opens with *idhā waqaʿat al-wāqiʿa* — "When the Inevitable befalls" — a temporal-conditional protasis. This is shared with Q 81 (*idhā ʾl-shamsu kuwwirat*), Q 82 (*idhā ʾl-samāʾu ʾnfaṭarat*), Q 84 (*idhā ʾl-samāʾu ʾnshaqqat*), Q 99 (*idhā zulzilati ʾl-arḍ*) — the *idhā*-eschatological-opening cluster. Q 56 is the LONGEST and the FIRST in mushaf order of this pattern.

## 6. Quick content structure (full detail in `02-content-analysis.md`)

- vv 1-6: cosmic catastrophe — *al-wāqiʿa* befalls; earth shakes; mountains crumble.
- vv 7-9: humanity = three classes (*azwāj thalātha*).
- vv 10-26: **al-Sābiqūn al-muqarrabūn** — paradise of nearness, *surur mawḍūnah*, *ḥūr ʿīn*, *akwāb*, *abārīq*, paradise-of-firsts.
- vv 27-40: **Aṣḥāb al-Yamīn** — paradise of the right hand, *sidr makhḍūd*, *ṭalḥ manḍūd*, *fursh marfūʿa*.
- vv 41-56: **Aṣḥāb al-Shimāl** — hellfire, *samūm wa-ḥamīm*, *zaqqūm*, the *mukadhdhibūn al-ḍāllūn*.
- vv 57-74: **rational arguments for Resurrection** — *afa-raʾaytum* (5×): semen, crops, water, fire, the divine command of *fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm*.
- vv 75-82: **the META-OATH** — *fa-lā uqsimu bi-mawāqiʿ al-nujūm wa-innahu la-qasamun law taʿlamūna ʿaẓīm* (75-76). Asserts Qurʾān as *qurʾānun karīm fī kitābin maknūn lā yamassuhu illā ʾl-muṭahharūn* (77-79) and rebukes denial (80-82).
- vv 83-87: **the death-moment** — *fa-lawlā idhā balaghat al-ḥulqūm* — "when the soul reaches the throat... why do you not bring it back?"
- vv 88-94: **the 3-class death-moment recapitulation** — Block B above.
- v 95: *inna hādhā la-huwa ḥaqqu ʾl-yaqīn*.
- v 96: *fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm* (closing — repeats the v 74 closing).

The double-closing *fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm* (v 74 and v 96) creates a **secondary refrain ring** within Q 56.

## 7. Pre-registered novel findings (this investigation)

See `06-novel-findings.md` for full results. Headline:

| Test | Verdict | Effect |
|:--|:--|:--|
| Q056-F-01 — 3-class ring lexical-overlap | **NULL** | Direction reverses for muqarrabīn cell; Bonferroni-3 0/3 cells significant. Class-labels ring; full vocabulary does not. |
| Q056-F-02 — Sābiqūn vocab uniqueness | **STRONGLY VINDICATED** | 26 rare tokens (≤5 corpus), **10 corpus-hapax** in vv 10-26 (vs threshold ≥3) |
| Q056-F-03 — META-OATH device rate | **VINDICATED** | Exactly 3 surahs corpus-wide: Q 56, Q 75, Q 89 (within pre-committed 1-3 bound) |
| Q056-F-04 — Cosmic-time-marker density | **NULL** | Q 56 ranks 8/114 by density (just outside top-5); pre-commit failed |
| Q056-F-05 — Deathbed hadith concentration | **NULL** | 31.6% of citations in vv 83-96 (above uniform but < 50% threshold) |

## 8. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
