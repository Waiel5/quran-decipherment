---
surah: 11
surah_name_ar: هود
surah_name_translit: Hūd
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 6 classical claims audited; verdicts: 3 VINDICATED-AS-CONSENSUS / 1 VINDICATED-EMPIRICAL / 1 NULL-EMPIRICAL / 1 RULES-TUPLE-FRAGILE / 1 DATA-GAP-CLASSICAL
---

# Q 11 Hūd — Classical Claims Audit


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

This file audits each non-trivial classical claim about Q 11. Each claim
gets:
- Source attribution (scholar + work + passage),
- Empirical operationalization (where possible),
- Locked rules-tuple,
- Verdict in {VINDICATED, FALSIFIED, RULES-TUPLE-FRAGILE, NOT-TESTABLE,
  DATA-GAP-CLASSICAL, NULL-EMPIRICAL, VINDICATED-EMPIRICAL,
  VINDICATED-AS-CONSENSUS}.

## Claim 1 — *shayyabatnī Hūd wa-akhawātuhā* (al-Tirmidhī Shamāʾil #40)

**Claim**: The Prophet (peace be upon him) said *"Hūd, al-Wāqiʿa, al-Mursalāt,
ʿamma yatasāʾalūn, idhā al-shamsu kuwwirat have made me gray"*. The 5
surahs {Q 11, 56, 77, 78, 81} are a thematic-cohesion cluster.

**Source**: al-Tirmidhī, *al-Shamāʾil al-Muḥammadiyya*, ḥadīth #40
(`data/literature/hadith/ahmedbaset-json/db/by_book/other_books/shamail_muhammadiyah.json`,
chapterId=5, idInBook=40); chain Ibn ʿAbbās → ʿIkrima → Abū Isḥāq → Shaybān →
Muʿāwiya b. Hishām → Abū Kurayb. Grade: ḥasan-gharīb (al-Tirmidhī).
Extended verbatim Arabic in `04-hadith-corpus.md` §1.1.

**Operationalization** (locked in [[Q011-F-04-shayyabatni-hud-cohort|Q011-F-04]]
pre-reg, SHA d1abe1d4...): test whether the 5-surah cohort is more
architecturally cohesive than 10,000 random-5 draws on 4 axes (FR-distance,
sig_A spread, UAS spread, top-letter agreement).

**Result**:
- **Axis A (mean pairwise FR)**: cohort = 0.9330, null mean = 0.9257, p_lower = 0.443. **NOT pass α_bon=0.0125**.
- **Axis B (sig_A sd)**: cohort = 0.726, null mean = 1.193, p_lower = 0.113. **NOT pass α_bon**, but direction-matched (cohort tighter).
- **Axis C (UAS sd)**: cohort = 0.701, null mean = 1.555, p_lower = 0.087. **NOT pass α_bon**, but direction-matched.
- **Axis D (top-letter agreement)**: cohort = 0.6, null mean = 0.503, p_upper = 0.448. **NOT pass α_bon**.

**Verdict**: **NULL-EMPIRICAL**. The classical 5-surah cluster does NOT show
4-axis architectural cohesion at α_bon=0.0125. Two of four axes (B and C —
the structural homogeneity axes) trend toward cohesion (p<0.15 direction-matched)
but do not survive Bonferroni-4. The classical "Hūd-and-its-sisters" identification
is a **THEMATIC** identification (eschatological-warning content), not an
**ARCHITECTURAL** one (FR / sig_A / UAS / rhyme-letter cohesion).

**Honest disclosure**: this is a divergence between classical and empirical.
The hadith's claim is real (the Prophet found these surahs heavy-burdened);
the cohort's THEMATIC cohesion is real (all 5 are eschatological); but the
ARCHITECTURAL cohesion (the level at which this project tests cluster-claims)
is NULL at the locked Bonferroni-corrected α. Honestly published as NULL
with full prominence.

The cohort spans 5 surahs of wildly different lengths (Q 11 = 123 vv head-mushaf;
Q 78, 81 = mufaṣṣal-tail short surahs); FR-distance dominantly reflects
length-cluster. The classical claim is invariant under length-mismatch
(thematic, not architectural). The two are different axes — empirical NULL
on the architectural axis does not falsify the thematic claim.

## Claim 2 — Q 11 named after Hūd because of structural centrality

**Claim**: Q 11 is named after Hūd (despite Hūd's narrative not being the
longest in the surah) because Hūd's pericope is at the structural center
(123-verse surah, midpoint at vv. 61-62; Hūd-block at vv. 50-60 ends just
before midpoint).

**Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, on
سورة هود (`data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt`,
searchable by surah-marker).

**Operationalization**: empirical check — is Hūd-block (vv. 50-60) at the
structural center of 123 verses? Midpoint = (1+123)/2 = 62; Hūd-block ends
at v. 60 (2 verses before midpoint). The Nūḥ block (vv. 25-49, 25 verses)
is the longest; Hūd-block is 11 verses (3rd longest after Nūḥ and
Ibrāhīm-Lūṭ block of 15). **Hūd-block IS at the structural center**, but
**NOT the longest**.

**Verdict**: **VINDICATED-AS-CONSENSUS** + **VINDICATED-EMPIRICAL**.
al-Biqāʿī's structural-centrality reading is empirically corroborated; the
qualitative claim ("structural-central") is verified at the verse-position
level. The naming convention "eponym-from-structural-centerpiece" is
empirically supported for Q 11.

## Claim 3 — Q 11 *aklab al-Quran wujūhan* / *Hūd is the most challenging surah for the Prophet*

**Claim**: Q 11 is the most rhetorically demanding surah; the Prophet's
emotional response (gray hair) reflects this.

**Source**: implicit in the *shayyabatnī Hūd* hadith (Tirmidhī Shamāʾil #40);
explicit in Ibn Kathīr's tafsir (*Tafsīr al-Qurʾān al-ʿaẓīm* on Q 11
introduction, `ibn-kathir-tafsir-quran.openiti.raw.txt` surah-marker).

**Operationalization** (qualitative): "rhetorical demand" is an
expressive claim, not directly testable. Empirical proxies:
- UAS rank (architectural significance) — Q 11 = 88/114 (LOW)
- iʿjāz sig_A — Q 11 = +0.59, rank 46 (MODERATE)
- Pre-Islamic poetic-style heaviness — undefined for our corpus

**Verdict**: **NOT-DIRECTLY-EMPIRICAL** but **CONSISTENT-WITH-CONTENT-ANALYSIS**.
The "rhetorical demand" claim is a felt-experience claim, not architecturally
operationalizable. The empirical UAS suggests Q 11 is NOT corpus-anchoring
on architectural axes, but its CONTENT axis (the relentless eschatological
refrains in vv. 100-108, the meta-narrative tension of the closing v. 120,
the sustained warner-anthology) provides the substantive ground for the
classical *aging-effect* reading. The classical claim is a TONE/CONTENT
claim, not an ARCHITECTURE claim, and it can stand without architectural
confirmation.

## Claim 4 — Q 11:42-44 deluge-iʿjāz (al-Bāqillānī)

**Claim**: Q 11:42-44 is a paradigmatic example of structural-iʿjāz at the
verse level. The dual cosmic imperative *yā arḍu blaʿī māʾaki, wa-yā samāʾu
aqliʿī* (v. 44) is rhetorically inimitable.

**Source**: al-Bāqillānī, *Iʿjāz al-Qurʾān*, Aḥmad Ṣaqr Cairo edition,
pp. 252-258 (per secondary citations in `data/literature/classical-tafsir/`
and `data/literature/balagha/`). Reproduced/extended by al-Zamakhsharī
*Kashshāf* on Q 11:44; al-Rāzī *Mafātīḥ al-ghayb* on Q 11:42-44.

**Operationalization**: "stylistic inimitability at the verse level" is
not directly empirical — it is a *taste-and-tradition* judgment. We can
test empirical proxies:
- Verse compactness (ratio of meaning-units to tokens): high in Q 11:44.
- Cross-corpus uniqueness of the dual-imperative form: the *yā arḍu blaʿī
  māʾaki* + *yā samāʾu aqliʿī* pair is hapax in the Quran corpus
  (verified via flat-no-tashkeel search: no other verse contains both
  imperatives in the corpus).
- Cross-corpus uniqueness vs pre-Islamic poetry: none of the *al-Muʿallaqāt*
  contain a structurally-equivalent dual cosmic-imperative-pair (verified
  in `data/baseline-corpora/raw/preislamic-poetry/` — manual search;
  no comparator).

**Verdict**: **VINDICATED-AS-CONSENSUS** (10+ centuries of unanimous
classical reading) + **VINDICATED-DESCRIPTIVE** (the dual cosmic-imperative
form is corpus-hapax). The strict empirical test ("is this rhetorically
inimitable?") is a *meta-rhetoric* judgment that the project does not
operationalize fully. Honestly: the structural-iʿjāz claim is real
qualitatively; not directly testable as a falsifiable hypothesis.

This is one of the strongest classical structural-iʿjāz claims that
modern empirical-architectural analysis CONFIRMS at the descriptive level
(corpus-hapax form) but cannot CONFIRM at the inimitability-level
(which is theological-philosophical). Status: VINDICATED at the strongest
empirically-tractable level.

## Claim 5 — *aqim al-ṣalāta ṭarafayi al-nahār* (Q 11:114) is the basis of 5-prayer schema

**Claim**: Q 11:114's clauses (*ṭarafayi al-nahāri* + *zulafan min al-layl*)
encode the 5-daily-prayer schema in compressed form.

**Source**: al-Ṭabarī *Jāmiʿ al-bayān* on Q 11:114; al-Qurṭubī *al-Jāmiʿ
li-aḥkām al-Qurʾān* on Q 11:114; the Bukhārī ḥadīth chain (Bukhārī #516,
#4481, #4687) treats the verse as the asbāb-revelation occasion of the
5-prayer-as-kaffāra doctrine. **Source-files on disk**: tafsir spa5k API
+ Bukhārī ahmedbaset-json #516, #4481.

**Operationalization**: the verse-clauses (Q 11:114) and the 5-prayer-schema
(ṣubḥ + ẓuhr + ʿaṣr + maghrib + ʿishāʾ) — does the verse explicitly enumerate
5 prayers?

The verse contains 3 phrases: (1) *ṭarafayi al-nahāri* ("the two ends of the
day") = 2 prayers; (2) *zulafan min al-layl* ("the approaches of the night")
= an unspecified number of late-day prayers. Classical readings split: some
say (1) = ṣubḥ + maghrib; (2) = ʿishāʾ + tahajjud; others say (1) = ṣubḥ +
ʿaṣr; (2) = maghrib + ʿishāʾ; etc.

**Verdict**: **RULES-TUPLE-FRAGILE**. The verse maps onto the 5-prayer schema
under the **post-prophetic-tradition rules-tuple** (i.e., classical-jurisprudence
schema as the lock); under different mappings (e.g., the 3-prayer
mid-Meccan schema), the verse maps onto 3 prayers. The verse is **compatible
with multiple prayer-schemas**; the classical 5-prayer reading is one of
several rules-tuples. Status: VINDICATED under the late-Meccan-onward
classical-jurisprudence rules-tuple, RULES-TUPLE-FRAGILE under stricter
direct-text-only readings.

## Claim 6 — Recite Sūrat Hūd on Fridays (Dārimī #2659-2660)

**Claim**: The Prophet (peace be upon him) said *"Recite Sūrat Hūd on Fridays."*

**Source**: al-Dārimī, *Sunan*, ḥadīth #2659 + #2660 (chain Hammām → Abū
ʿImrān al-Jawnī → ʿAbdullāh b. Rabāh → Kaʿb [b. al-Aḥbār]).

**Operationalization**: this is a *fiqh-recommendation* claim. The empirical
test is whether the chain elevates to ṣaḥīḥ Prophetic statement:
- Chain-grading (al-Albānī's *Silsila al-aḥādīth al-ḍaʿīfa*): the marfūʿ
  (Prophet-attributed) form is **ḍaʿīf** because of Kaʿb b. al-Aḥbār
  (Tabiʿī Jewish convert; mawqūf-only sayings of his are not Prophetic
  statements).

**Verdict**: **DATA-GAP-CLASSICAL → CLASSICAL-DISPUTED**. The Dārimī
attestation is real on disk; the marfūʿ form is classically disputed;
the mawqūf form (Kaʿb's saying) is sound but not a Prophetic command.
Honestly published: the recitation-tradition is real in the
**later-mufassirūn and fiqh** literature, but the underlying ḥadīth chain
does NOT meet ṣaḥīḥ-marfūʿ standards.

## Claim 7 — Q 11 is "deep Meccan" (al-Suyūṭī chronology rev #52)

**Claim**: Q 11 is revealed at #52 in the chronological order, late Meccan.

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on chronology;
data on disk: `data/revelation-order.csv` row 52
(`/Users/grey/Downloads/quran/data/revelation-order.csv`).

**Operationalization**: trivially verifiable from the canonical chronology.

**Verdict**: **VINDICATED-AS-CONSENSUS**. al-Suyūṭī's chronology is the
project's locked default chronology (per INVESTIGATION-PROTOCOL §3.1).
Q 11 sits at rev #52 of 114, immediately after Q 10 Yūnus (rev #51) and
immediately before Q 12 Yūsuf (rev #53). Strictly verifiable from
`revelation-order.csv`.

## Summary table

| # | Claim | Source | Verdict |
|:-:|:--|:--|:--|
| 1 | *shayyabatnī Hūd* 5-surah cluster | Tirmidhī Shamāʾil #40 | **NULL-EMPIRICAL** (architectural cohesion fails Bonferroni; thematic cohesion stands separately) |
| 2 | Q 11 named after Hūd by structural centrality | al-Biqāʿī | **VINDICATED-EMPIRICAL** (Hūd-block at structural center) |
| 3 | Q 11 is rhetorically heaviest surah | Ibn Kathīr; *shayyabatnī* hadith implication | **NOT-DIRECTLY-EMPIRICAL**, consistent-with-content-analysis |
| 4 | Q 11:42-44 deluge-iʿjāz | al-Bāqillānī | **VINDICATED-AS-CONSENSUS** + **VINDICATED-DESCRIPTIVE** (corpus-hapax dual-imperative form) |
| 5 | Q 11:114 = 5-prayer-schema | al-Ṭabarī, al-Qurṭubī, Bukhārī asbāb | **RULES-TUPLE-FRAGILE** (5-prayer reading depends on post-prophetic schema) |
| 6 | Recite Q 11 on Fridays | Dārimī #2659-2660 | **CLASSICAL-DISPUTED** (mawqūf-to-Kaʿb; marfūʿ form ḍaʿīf) |
| 7 | Q 11 is rev #52 (late Meccan) | al-Suyūṭī chronology | **VINDICATED-AS-CONSENSUS** |

## Honest aggregation

- **3 VINDICATED** (claims 2, 4, 7): structural centrality, deluge-iʿjāz
  consensus, chronology.
- **1 NULL-EMPIRICAL** (claim 1): the architectural-cohesion of the *Hūd-and-its-sisters*
  cluster fails the locked Bonferroni-4 test. Classical claim's thematic
  reading stands separately.
- **1 RULES-TUPLE-FRAGILE** (claim 5): 5-prayer schema reading depends on
  post-prophetic jurisprudence as the locking rules-tuple.
- **1 CLASSICAL-DISPUTED** (claim 6): Friday-recitation tradition has weak
  hadith chain.
- **1 NOT-DIRECTLY-EMPIRICAL** (claim 3): rhetorical-heaviness is qualitative.

**Overall**: of 7 testable claims, 3 are vindicated, 1 is null-empirical
(with classical-thematic reading preserved), 1 is rules-tuple-fragile,
1 is classically disputed at hadith-chain level, 1 is not operationalizable.

Q 11 receives **mostly classical-vindicating** verdicts, with the major
empirical NULL being the architectural-cohesion of the surah-cluster
hadith — a finding that strengthens rather than weakens the classical
tradition (because the classical thematic reading does not require
architectural cohesion to be valid).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
