---
surah: 30
surah_name_translit: al-Rūm
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: "5 classical claims audited. al-Bāqillānī iʿjāz al-ghayb (Q 30:2-5) RULES-TUPLE-VINDICATED via Q030-F-02 hapax-PASS-DIRECTED. al-Biqāʿī test→vindication munāsabah Q29→Q30 DIRECTIONAL via Q030-F-01. al-Suyūṭī chronology-of-revelation order DOCUMENTED-NOT-EMPIRICALLY-DECIDED. al-Rāzī cognitive-imperative pedagogy DIRECTIONAL via Q030-F-05 (rank 5/114). 'Ankabūt parable as semantic eponym for Q 29 → vindicated via Q029-F-01 PASS-DIRECTED."
---

# Q 30 al-Rūm — Classical Claims Audit

For each non-trivial classical claim about Q 30, we state the claim with citation, identify the rules-tuple, run an empirical test (or note "not testable empirically"), and assign a verdict.

## Claim 1: Q 30:2-5 is iʿjāz al-ghayb (knowledge of the unseen) — al-Bāqillānī

**Statement**: al-Bāqillānī, *Iʿjāz al-Qurʾān*, argues that Q 30:2-5 (*ghulibati al-Rūm ... sa-yaghlibūn fī biḍʿi sinīn*) is paradigmatic prophetic knowledge of future events, since (a) the prediction was specific (Romans defeated → Romans victorious), (b) the time-bracket was specific (*biḍʿi sinīn* = 3-9 years), (c) the prediction was made when no human party could foresee the outcome, and (d) the prediction was empirically fulfilled (Battle of Nineveh, 627 CE). 

**MW-6 verification tag**: SECONDARY-TRIANGULATED. al-Bāqillānī's *Iʿjāz al-Qurʾān* is widely cited in secondary literature (al-Suyūṭī's *al-Itqān*, Ibn Kathīr's tafsīr, and modern academic surveys) as containing this argument. Direct physical-edition page-number citation is PENDING.

**Rules-tuple for empirical correlate**: `(QAC v0.4 lemma-tags, hafs-kufan, no-tashkeel, lemma-membership-corpus-counts)`.

**Empirical correlate**: [[Q030-F-02-rum-prophecy-hapax-prereg|Q030-F-02]] — Q 30:2-5 contains 3 corpus-hapax-or-near-hapax lemmas (`r~uwm`, `galab`, `biDoE`) out of 6 candidates. Q 27:14 (the comparison historical-claim verse) contains 0. The *lexical-uniqueness signature* of Q 30:2-5 is empirically distinctive.

**Verdict**: **VINDICATED at the lexical-uniqueness axis** (Q030-F-02 PASS-DIRECTED). The classical iʿjāz al-ghayb framing has a direct empirical correlate: the prophecy-pericope's vocabulary (Romans, defeat-noun, biḍʿ) is corpus-rare-to-unique. The historical-fulfillment claim is THEOLOGICAL-PHILOSOPHICAL (out of scope per protocol §10) and is NOT what we vindicate; we vindicate only the lexical-architectural correlate.

**Honest limits**: Q030-F-02's threshold (≥ 3 near-hapax) is achieved EXACTLY (3/6); a tighter threshold (≥ 4) would NOT pass. The verdict is at the pre-committed-but-not-extreme level.

## Claim 2: Q 29 → Q 30 munāsabah — test-of-believers → historical-vindication — al-Biqāʿī

**Statement**: al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*, argues that Q 29 ends on *wa-l-ladhīna jāhadū fīnā la-nahdiyannahum subulanā* (those who strive in Us, We will guide to Our ways), and Q 30 begins with the historical-vindication of that promise — Allah's help (*naṣr*) of the Romans against the Persians as a public-historical proof of Allah's promise-keeping.

**MW-6 verification tag**: SECONDARY-TRIANGULATED. al-Biqāʿī's specific Q 29-Q 30 munāsabah is referenced indirectly through Maʿārif al-Qurʾān's framing (`en-tafsir-maarif-ul-quran/30/2.json`: "In the last verse of Surah ʿAnkabūt Allāh Taʿālā had given the good tiding ... The story that marks the beginning of Surah Ar-Rūm is a manifestation of that very Divine help."). Direct *Naẓm al-durar* page-citation is PENDING (`biqai-nazm-al-durar.pdf` 129MB requires PDF parsing).

**Rules-tuple**: `(QAC roots, no-tashkeel, hafs-kufan)`.

**Empirical correlate**: [[Q030-F-01-alm-exception-subcluster-prereg|Q030-F-01]] — Q 29 + Q 30 pooled vs Q 2, 3, 31, 32 pooled:
- Imtihān-density (test): Q29+30 = 5.02/k, Q2,3,31,32 = 3.33/k. Direction matches (HIGHER in target). Rank 4/15 in C(6,2) enumeration; secondary-perm p = 0.176.
- Historical-prophecy-density: Q29+30 = 29.00/k, Q2,3,31,32 = 17.69/k. Direction matches. Rank 2/15; secondary-perm p = 0.155.
- Asymmetric loading: Q 29 carries imtihān (`ftn` + `jhd`); Q 30 carries historical-prophecy (`glb` + `rwm` + `bDE`).

**Verdict**: **DIRECTIONAL** at α=0.05 single-test, NOT pass at α_bon=0.025 Bonferroni-2. Both axes match the pre-committed direction; both fail the strict Bonferroni level. The al-Biqāʿī munāsabah is **interpretively vindicated** but does not reach law-strength under Bonferroni-2 in the chosen operationalization.

This refines the parent [[h-new-93-q29-q30-subpattern|H-NEW-93]] NULL: the joint pattern is real but weaker than law-strength under within-ALM-cluster comparison.

## Claim 3: al-Suyūṭī chronology — Q 30 revelation order

**Statement**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, situates Q 30 in late Meccan period. Per Egyptian-standard chronology (`data/revelation-order.csv`): rev order = 84; Nöldeke order = 74; phase = "Late Meccan."

**MW-6 verification tag**: SECONDARY-TRIANGULATED. The Egyptian-standard revelation-order is widely tabulated; al-Suyūṭī's chronology is the canonical source for rev-order = 84 (out of 114 surahs).

**Rules-tuple**: chronological-reference (no quantitative test required).

**Empirical correlate**: not directly testable — chronology is a historical claim, not a textual-empirical claim. We document it as chronology context.

**Verdict**: **DOCUMENTED-NOT-EMPIRICALLY-DECIDED**. Note: there are minor disputes between al-Suyūṭī's listing and al-Tirmidhī's narrations on the precise placement of Q 30 within the Late Meccan phase relative to Q 29 — but rev-order ∈ {83, 84, 85} is consensus.

## Claim 4: al-Rāzī cognitive-imperative pedagogy (Q 30:21-24)

**Statement**: al-Rāzī, *Mafātīḥ al-ghayb* on Q 30:21-24, reads the cluster *li-qawmin yatafakkarūn / li-l-ʿālimīn / li-qawmin yasmaʿūn / li-qawmin yaʿqilūn* as a four-fold pedagogical hierarchy of cognitive engagement, anchored at the *wa-min āyātihi* (and among His signs) refrain. Q 30 contains 6 *wa-min āyātihi* in a tight 6-verse window (vv. 20-25), the highest concentration in the corpus.

**MW-6 verification tag**: PENDING physical edition page-citation; the doctrinal claim is widely paraphrased in modern tafsīr-secondary.

**Rules-tuple**: `(no-tashkeel, regex-word-boundary, orthographic-word, hafs-kufan)`.

**Empirical correlate**: [[Q030-F-05-cognitive-imperatives-prereg|Q030-F-05]] — Q 30 cognitive-imperative density rank 5/114, rate 3.456/1000-words. Pre-reg threshold was top-3.

**Verdict**: **DIRECTIONAL** — Q 30 is in the top-5 of the corpus, but does NOT achieve the strict top-3 pre-registered threshold. The classical claim of "high cognitive-imperative density in Q 30" is QUANTITATIVELY DOCUMENTED but does not pass the pre-committed strict-rank-3 threshold. Q 88 (rank 1) is a tiny short surah where one match dominates the rate; among medium-length surahs (≥ 100 words), Q 30 is rank 2 (only Q 32 al-Sajda is higher). 

**Refined claim**: Q 30 is in the top-2 cognitive-imperative-dense MEDIUM-LENGTH surahs (≥ 100 words). This is a refinement of the pre-reg, not a re-test; documented as DIRECTIONAL.

## Claim 5: Q 30:30 — fiṭra as primordial nature (Bukhārī #4569 + classical doctrine)

**Statement**: The Bukhārī tradition #4569 (Abū Hurayra) explicitly cites Q 30:30 as evidence that every human is born on the *fiṭra*. The classical *fiṭra*-doctrine (Ibn Taymiyya, al-Ghazālī, all 4 madhāhib) holds that the *fiṭra* is the natural human disposition toward tawḥīd (monotheism), corrupted only by post-natal religious teaching.

**MW-6 verification tag**: VERIFIED-via-corpus (Bukhārī #4569 directly in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`).

**Rules-tuple**: lemma-anchor at QAC root `fTr` (specifically the lemma `fiTorap` derived from the verb form *faṭara al-nāsa*).

**Empirical correlate**: corpus distribution of root `fTr`. The lemma `fiTorap` is bound to Q 30:30 specifically. Root `fTr` appears 20 times in 11 surahs in QAC v0.4 (`data/morphology/quranic-corpus-morphology-0.4.txt`); the *fiṭra*-as-noun specifically (the doctrinal anchor) appears uniquely at Q 30:30. **This is a corpus-anchor verification**.

**Verdict**: **VINDICATED**. Bukhārī #4569 directly cites Q 30:30 as the verse-anchor. The lexical anchor is unique to Q 30:30 in the corpus. The classical *fiṭra* doctrine has its primary verse-anchor here.

## Summary of audit verdicts

| Claim | Source | Empirical correlate | Verdict |
|:--|:--|:--|:--|
| 1. Iʿjāz al-ghayb on Q 30:2-5 | al-Bāqillānī | Q030-F-02 (3 hapax) | **VINDICATED** at lexical-uniqueness axis |
| 2. Q 29 → Q 30 munāsabah | al-Biqāʿī | Q030-F-01 (joint sub-cluster) | **DIRECTIONAL**, not Bonferroni-PASS |
| 3. Q 30 chronology | al-Suyūṭī | (not testable) | **DOCUMENTED** |
| 4. Cognitive-imperative pedagogy (Q 30:21-24) | al-Rāzī | Q030-F-05 (rank 5/114) | **DIRECTIONAL**, not top-3 |
| 5. Fiṭra anchor at Q 30:30 | Bukhārī #4569 + classical doctrine | corpus-anchor | **VINDICATED** |

2 VINDICATED, 2 DIRECTIONAL, 1 DOCUMENTED-NOT-EMPIRICALLY-DECIDED. The directional results are honest NULL on Bonferroni-strict criteria; the vindications hold at single-test level.
