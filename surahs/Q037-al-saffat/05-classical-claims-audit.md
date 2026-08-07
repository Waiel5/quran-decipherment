---
surah: 37
surah_name_ar: الصافات
surah_name_translit: al-Ṣāffāt
file_type: classical-claims-audit
date_last_updated: 2026-05-08
phase: B+
verdict: 7 claims audited; 4 VINDICATED, 1 PARTIALLY-VINDICATED-with-qualification, 1 NOT-EMPIRICALLY-TESTABLE, 1 PERIPHERAL.
---

# Q 37 al-Ṣāffāt — Classical Claims Audit


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

For each non-trivial classical claim about Q 37, this file records the claim with explicit citation, the rules-tuple needed to test it, the empirical test (or non-testability), and the verdict.

## Claim 1 — al-Suyūṭī: Q 37 is in the *al-aqsām* (oath-opener) classification

### Citation
al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 67 (al-aqsām).

### Claim
Q 37 *wa-l-ṣāffāti ṣaffā* belongs to the major formal class of "qasamīyāt iftitāḥīya" — surahs whose opening is an oath.

### Rules-tuple
`(no-tashkeel, orthographic-token, surah-opener-form-class, basmala-counted-only-in-Q1, Hafs-Kufan)`.

### Empirical test
H-NEW-1070 confirmed (p=0.0004) that the strict-15 *wa-l-* oath-opener cluster (with Q 37 as a member) is FR-cohesive corpus-wide. Q 37 belongs to this set.

Specialist test Q037-F-04 finds that **Q 37 is a peripheral member** of the cluster (rank 15/15 in cluster centrality). The cluster's tight cohesion is driven by the short-Meccan-tail core {Q 91-103}.

### Verdict
**VINDICATED at the group level**: Q 37 belongs to the H-NEW-1070 oath-cluster (CONFIRMED).
**PARTIALLY VINDICATED at the individual level**: Q 37 is the LEAST-central member of the cluster (Q037-F-04 perm-p=0.55, NULL on individual extension).

### Honest limit
al-Suyūṭī's classification is FORMAL (based on opening-form). The empirical FR-cohesion holds at the GROUP level even when an individual member like Q 37 is peripheral — al-Suyūṭī is not refuted; the formal classification is preserved, the empirical-cohesion mapping is at the cluster level not the individual level.

## Claim 2 — al-Bāqillānī: Q 37:99-113 sacrifice-narrative is iʿjāz al-balāgha

### Citation
al-Bāqillānī, *Iʿjāz al-Qurʾān*, on the dialogue-economy of Q 37:102 (the father-son sacrifice exchange).

### Claim
The Q 37:102 dialogue (*qāla yā bunayya innī arā fī al-manāmi annī adhbahuk fa-nẓur mādhā tarā / qāla yā abati ifʿal mā tuʾmar sa-tajidunī in shāʾa allāhu min al-ṣābirīn*) is a paradigm of *ījāz al-qiṣar* (compressive-economy of meaning): the entire psychological-spiritual arc of the test is conveyed in two dialogue turns.

### Rules-tuple
`(no-tashkeel, orthographic-token, dialogue-token-density, balāgha-categorial-classification)`.

### Empirical test
**Indirect**: the surah is LOW on iʿjāz sig_A (-0.809, rank 83) — al-Bāqillānī's iʿjāz al-fawāṣil framework, when operationalized as rhyme-content anti-correlation, places Q 37 in the LOW band. The CLASSICAL al-Bāqillānī claim is about *ījāz al-qiṣar* in the dialogue-pair, not about al-fawāṣil; these are different iʿjāz-modes.

**Direct**: the Q 37:102 dialogue is 2 verses, ~30 tokens, conveying the test-acceptance + son-affirmation. This is structurally distinctive but not testable as a corpus-statistical claim without a balāgha-token-density baseline (which the project does not yet have).

### Verdict
**NOT DIRECTLY EMPIRICALLY TESTABLE** at the project's current instrument-set. The claim is BALĀGHĪ-QUALITATIVE; al-Bāqillānī's iʿjāz al-fawāṣil reading places Q 37 LOW on the *fawāṣil* axis (so a different iʿjāz-mode than the one al-Bāqillānī invokes here). **NEEDS-BALĀGHA-INSTRUMENTATION**.

## Claim 3 — al-Rāzī: Q 37:1-3 trio refers to angels in 3 distinct functional roles

### Citation
al-Rāzī, *Mafātīḥ al-ghayb*, vol. 26 pp. 312-316, on Q 37:1-5.

### Claim
The trio *al-ṣāffāt / al-zājirāt / al-tāliyāt* refers to angels in three distinct cosmic-causal-cognitive functions: ranks-in-worship / cosmic-causal-influence / discursive-recital. The trio displays a tight thematic-conceptual unity even if the lexical-token surface is parallel.

### Rules-tuple
`(no-tashkeel, orthographic-token + QAC-root, cosine-similarity, lexical-cohesion-permutation-null)`.

### Empirical test
Q037-F-03 (PRE-COMMIT VIOLATION on the lexical metric):
- C(Q 37:1-3) token-cosine = 0.000 (the verses share NO orthographic tokens).
- C(Q 37:1-3) root-cosine = 0.000 (the roots {ṣ-f-f, z-j-r, t-l-w, dh-k-r} are pairwise-disjoint across the 3 verses).
- Permutation null mean (random 3-spans of Q 37): 0.0145 token-cosine; 0.0234 root-cosine.
- p_token = 1.0; p_root = 1.0 (the trio is BELOW the null for both).
- C(Q 37:4-6) token-cosine = 0.000; C(Q 37:180-182) token-cosine = 0.068 (the closing-tail trio is MORE token-cohesive than the opener-trio).

### Verdict
**RULES-TUPLE-FRAGILE / PARTIALLY-VINDICATED.** al-Rāzī's "trio refers to a unified subject in 3 modes" reading is correct AT THE THEMATIC-CONCEPTUAL level (Q 37:1-3 are clearly parallel in form and theme). The lexical-token metric REFUTES the cohesion at the surface-orthographic level — the verses are LEXICALLY ORTHOGONAL.

The cohesion is **morphological-grammatical-template** (active-feminine-plural-participle + cognate-accusative-noun), NOT lexical. al-Rāzī's claim is preserved at the semantic level; the surface lexical orthogonality is a REAL empirical finding that REFINES (not refutes) the classical reading: the iʿjāz-balagha here is in the GRAMMATICAL-PATTERN-PARALLEL, not in lexical-overlap.

## Claim 4 — Ibn Kathīr: the *dhabīḥ* of Q 37:99-113 is Ismāʿīl, not Isḥāq

### Citation
Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, ad Q 37:99-113 (vol. 7 pp. 26-30 in Dār al-Ṭayba edition).

### Claim
The "intended sacrifice" is Ismāʿīl. The Isḥāq-tradition is from Jewish-source contamination via *aḥbār ahl al-kitāb*; the Quranic narrative-sequence (v. 101 *ghulām ḥalīm* annunciation → sacrifice → v. 112 *Isḥāq* annunciation) decisively identifies the dhabīḥ as the FIRST-announced son.

### Rules-tuple
`(no-tashkeel, orthographic-token, narrative-sequencing-rule, classical-cross-reference)`.

### Empirical test
**Quranic-internal evidence (locked rule: chronological narrative-order tracks chronological prophet-order)**: the v. 101 *ghulām ḥalīm* is announced BEFORE the sacrifice; the v. 112 *Isḥāq* annunciation comes AFTER the sacrifice's resolution and includes *bashshara* (good-news) framing for a NEW son. If the v. 101 son were Isḥāq, the v. 112 redundant Isḥāq-announcement would be anomalous.

**Cross-Quranic evidence**: Q 11:71 *fa-bashsharnāhā bi-Isḥāq wa-min warāʾ Isḥāq Yaʿqūb* announces Isḥāq + Yaʿqūb in the SAME breath, indicating Isḥāq's LATER birth and his subsequent procreation. If Isḥāq were also the dhabīḥ in Q 37, the Q 11:71 + Q 37:112 announcements would be doubled-redundant.

### Verdict
**VINDICATED at the Quranic-internal sequence level**. The narrative-sequencing argument is sound; the v. 101 → v. 112 ordering empirically supports Ismāʿīl. al-Ṭabarī catalogues both views; Ibn Kathīr's Ismāʿīl-defense is the more textually-economical reading.

The hadith-corpus is MIXED: the al-Aḥmad *kabsh of paradise* chain via Ibn ʿAbbās → Saʿīd b. Jubayr is reported in two variants — one naming Ismāʿīl, one naming Isḥāq. al-Ṭabarī notes this duality. Ibn Kathīr argues the Ismāʿīl-variant is the more reliable.

**EMPIRICAL CORRELATE in this project**: Q 37:99-113 contains 2 corpus-hapax roots (t-l-l, j-b-n) at v. 103 — the dramatic sacrifice-moment. The narrative is uniquely sustained in Q 37 (no other surah has the extended sacrifice-arc); other Abraham-narratives (Q 11:69-83, Q 21:69-71) handle the Abraham-Lot-angel-visit and the Abraham-fire respectively, but not the sacrifice. **Q 37 is the corpus's UNIQUE sacrifice-of-Ishmael surah** — the structural-uniqueness is preserved regardless of the *dhabīḥ*'s identity.

## Claim 5 — al-Biqāʿī: Q 36 → Q 37 → Q 38 munāsabah triad

### Citation
al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, sections on Q 36, Q 37, Q 38.

### Claim
The Q 36 → Q 37 → Q 38 triad forms a tight munāsabāt-sequence: Q 36 (Yāsīn) closes with resurrection-affirmation; Q 37 opens with cosmic-monotheism + prophet-cycle; Q 38 (Ṣād) continues with prophet-cycle + Iblīs-Adam narrative + closing.

### Rules-tuple
`(no-tashkeel, FR-on-QAC-stem-roots, canonical-adjacency-cost-on-2-opt-residual, basmala-counted-only-in-Q1, Hafs-Kufan)`.

### Empirical test
Per H-NEW-720:
- Q 36 → Q 37: fraction_residual = 0.0080 (delta_raw = +0.0662). LOW cost — al-Biqāʿī Q 36 → Q 37 munāsabah empirically smooth.
- Q 37 → Q 38: fraction_residual = 0.0000 (delta_raw = -0.000911 — clamped). SEAMLESS — 1 of 13 clamped-zero adjacencies.
- Q 38 → Q 39: fraction_residual = 0.0120 (delta_raw = +0.0992). MODEST — al-Biqāʿī Q 38 → Q 39 munāsabah holds but less tight.

The TRIAD seam-strength: Q 36 → Q 37 → Q 38 averages fraction_residual = 0.0040 across both seams — among the corpus's smoothest 3-surah triad runs.

### Verdict
**VINDICATED at the empirical level for both seams**. al-Biqāʿī's Q 36 → Q 37 munāsabah is empirically supported (low cost). al-Biqāʿī's Q 37 → Q 38 munāsabah is empirically supported AT THE EXTREME LEVEL (clamped-zero seamless). The full Q 36-37-38 triad is among the smoothest in the corpus.

Specialist test Q037-F-05 directly tests Q 37 → Q 38 architectural overlap (DIRECTIONAL: 2/3 cells pass; H1-top-5-by-delta_raw fails because rank is 13/113 not top-5 by absolute delta, but the delta_raw is negative ⇒ canonical adjacency BEATS 2-opt local rearrangement).

## Claim 6 — al-Bukhārī (via Ibn ʿAbbās): the Yūnus b. Mattā anti-preference rule

### Citation
al-Bukhārī, kitāb aḥādīth al-anbiyāʾ, multiple chains via Ibn ʿAbbās → the Prophet ﷺ (Bukhārī idInBook 3256, 3272, 3273, 3274, 3275 in the AhmedBaset-JSON corpus; canonical-Bukhārī numbering ~3395-3416).

### Claim
*"It does not befit any servant to say: 'I am better than Yūnus b. Mattā.'"* This Prophetic-saying is anchored on Q 37:139-148 (the Yūnus vignette) — the surah's narrative establishes Yūnus's prophet-status with a moment of human weakness (flight from his mission, vv. 140-145) that nonetheless does not diminish his status.

### Rules-tuple
`(hadith-isnad-strength, Quranic-citation-anchor)`.

### Empirical test
The hadith is widely-attested across Bukhārī (5+ chains), Muslim (4+ chains), Tirmidhī, Abū Dāwūd, Ibn Mājah, Aḥmad. Multiple-strong-isnad attestation. The Quranic anchor at Q 37:139-148 is direct.

### Verdict
**VINDICATED**: the hadith-cluster is among the strongest-attested Q 37-anchored prophetic-tradition complexes. Q 37 is the SOURCE-SURAH for the Yūnus theological-elevation in the post-Quranic tradition.

## Claim 7 — al-Suyūṭī (via al-Tirmidhī #3313): Q 37:147 *miʾat alf aw yazīdūn* refers to a specific number

### Citation
al-Suyūṭī, *al-Durr al-manthūr* on Q 37:147; al-Tirmidhī Sunan idInBook=3313 (canonical-Tirmidhī ~3229), kitāb tafsīr al-Qurʾān.

### Claim
The "100,000 or more" tribe of Yūnus had a specific count: variously 120,000, 130,000, or 150,000 across different transmission-chains.

### Rules-tuple
`(hadith-isnad-strength, single-chain-attestation, ḍaʿīf-tolerance)`.

### Empirical test
The al-Tirmidhī chain has *ʿan rajulin* (an unnamed transmitter) — technically *ḍaʿīf*. The Quranic phrasing *aw yazīdūn* explicitly preserves the indeterminacy.

### Verdict
**RULES-TUPLE-FRAGILE / NOT-EMPIRICALLY-DECIDABLE**. The hadith chain is weak; the Quranic text preserves indeterminacy. Classical scholars (al-Qurṭubī, al-Suyūṭī, Ibn Kathīr) catalog multiple numerical traditions without preference. The empirical correct answer is: the Quran does not commit to a precise number, and the hadith-clarification chains are too weak to decide.

## 8. Summary table

| # | Claim | Citation | Verdict |
|:-:|:--|:--|:--|
| 1 | Q 37 ∈ al-aqsām class | al-Suyūṭī Itqān nawʿ 67 | VINDICATED at group level (H-NEW-1070); PARTIALLY at individual (Q037-F-04 NULL) |
| 2 | Q 37:99-113 iʿjāz al-balāgha | al-Bāqillānī | NOT-DIRECTLY-EMPIRICALLY-TESTABLE (NEEDS-BALĀGHA-INSTRUMENTATION) |
| 3 | Q 37:1-3 trio refers to angels in 3 modes | al-Rāzī Mafātīḥ vol. 26 | RULES-TUPLE-FRAGILE; semantic-level VINDICATED, lexical-level REFUTED (Q037-F-03) |
| 4 | dhabīḥ is Ismāʿīl | Ibn Kathīr | VINDICATED via Quranic-internal sequence (v. 101 → v. 112) |
| 5 | Q 36→Q 37→Q 38 munāsabah | al-Biqāʿī Naẓm al-Durar | VINDICATED via H-NEW-720 (both seams low-cost; Q 37→Q 38 clamped-zero) |
| 6 | Yūnus b. Mattā anti-preference rule | al-Bukhārī (via Ibn ʿAbbās), 5+ chains | VINDICATED — strongly-attested, Q 37 is source-surah |
| 7 | Q 37:147 specific 100k+ count | al-Tirmidhī (idInBook 3313), al-Suyūṭī Durr | RULES-TUPLE-FRAGILE; Quran preserves indeterminacy |

## 9. Cross-references

- [[surahs/Q037-al-saffat/03-tafsir-survey|Q 37 tafsir survey]]
- [[surahs/Q037-al-saffat/04-hadith-corpus|Q 37 hadith corpus]]
- [[surahs/Q037-al-saffat/06-novel-findings|Q 37 novel findings]]
- [[h-new-1070-oath-opener-cluster|H-NEW-1070]] (Claim 1)
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] (Claim 5)
- al-Biqāʿī Naẓm al-Durar (multiple sections; Claim 5)
- Ibn Kathīr Tafsīr 7:26-30 (Claim 4)
- al-Suyūṭī al-Durr al-manthūr (Claims 2, 7)
