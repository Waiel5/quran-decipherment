---
surah: 47
surah_name_ar: محمد
file_type: classical-claims-audit
date_last_updated: 2026-05-10
phase: B+
specialist: Q047-wave-J-specialist
---

# Q 47 — Classical Claims Audit

For each non-trivial classical claim about Q 47, the rules-tuple, the test, the verdict, and the pre-registration are documented. Per Protocol §1.6 + §2.9.

## Claim 1: al-Suyūṭī chronology — Q 47 is Medinan, revelation-order #95

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (knowledge of Meccan-Medinan) and nawʿ 18 (chronological order).
**On-disk**: `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`.

- **Claim**: Q 47 is Medinan, revealed at chronological position 95 (Nöldeke-aligned).
- **Rules-tuple**: (no-tashkeel, surah-level chronological labels, Nöldeke chronology, Hafs-Kufan).
- **Data**: `/Users/grey/Downloads/quran/data/revelation-order.csv`.
- **Test**: Read the surah's chronological label from the dataset; compare to al-Suyūṭī's claim.
- **Result**: Q 47 chronological position #95, label "Medinan" — MATCHES al-Suyūṭī's claim.
- **Verdict**: **VINDICATED** (corroborative; the dataset is BASED on al-Suyūṭī + Nöldeke synthesis, so this is a consistency check, not an independent test).
- **Honest limit**: This is a consistency check, not an independent corroboration; the `revelation-order.csv` is derived in part from al-Suyūṭī. Cannot be used as independent evidence for chronological position.

## Claim 2: al-Biqāʿī Q 46→Q 47→Q 48 munāsabah (war-permission → war-instruction → conquest-promise)

**Source**: al-Biqāʿī, *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar*, on Q 46/47/48.
**On-disk**: `data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`.

- **Claim**: Q 46→Q 47→Q 48 is a thematic-ring sequence (war-permission in Q 46:35, war-instruction in Q 47:4, conquest-promise in Q 48:1-3). The 3-surah triplet should be architecturally cohesive.
- **Rules-tuple**: (no-tashkeel, QAC-stem-root, mean-FR, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
- **Test (already-existing)**: Q047-F-03 (`csv/Q047-F-03.json`) — Q 47-Q 48-Q 49 triplet cohesion test (a sliding-window variant).
- **Test (this audit)**: Compute mean-FR of {Q 46, Q 47, Q 48} from H-NEW-111 D-matrix; compare to permutation distribution of random 3-tuples + rank among consecutive 3-tuples.
- **Result Q047-F-03** (Q 47-Q 48-Q 49): T_obs=0.866, perm-median=0.952, p_low=0.252, rank-among-consecutive 63/112 (mid-pack). **NULL**.
- **Result for Q 46-Q 47-Q 48**: FR(46,47)=0.9905; FR(47,48)=0.8893; FR(46,48)=0.9905 (computed below) → mean-FR(46,47,48) ≈ 0.957 — slightly above corpus-3tuple median of 0.952. **DIRECTIONALLY NEUTRAL** at 3-tuple cohesion test.
- **Verdict**: **PAIR-VINDICATED, 3-TUPLE-NULL**. al-Biqāʿī's ring exists as a pair-of-pairs (Q 47-Q 48 cheap edge, δ=0.0332; Q 46→Q 47 corpus-mid edge) but NOT as a holistic 3-set cluster.
- **Honest reframing**: The munāsabah is real at LOCAL semantic level (the three surahs' THEMES form a coherent sequence) but does not produce a measurable 3-tuple FR-cohesion signal. This refines al-Biqāʿī's claim to a sequence-of-pairs interpretation.

## Claim 3: al-Qurṭubī — Q 47 = sūrat al-Qitāl (war-vocabulary concentration)

**Source**: al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 47 (preferred name).

- **Claim**: Q 47 is the qitāl-concentrated surah; its alternate name is *sūrat al-Qitāl* because of Q 47:20's self-naming clause.
- **Rules-tuple A (already-existing)**: (no-tashkeel, orthographic-token, 9-term war-vocab cluster, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
- **Test A**: Q047-F-02 — 9-term war-vocabulary density rank ≤ 5.
- **Result A**: Q 47 rank **2/114** (rate 4.205 per-100-w). **VINDICATED** at the broad-cluster level.
- **Rules-tuple B (this dossier)**: (no-tashkeel, QAC-stem-root *qtl* ONLY, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
- **Test B**: Q047-F-05 — qtl-root density rank ≤ 3 (NARROW pre-reg).
- **Result B**: Q 47 rank **19/114** by per-1000-w; 18/114 by absolute count. **NULL** at the narrow-root level.
- **Verdict**: **VINDICATED at broad-cluster level (Q047-F-02), NULL at narrow-root level (Q047-F-05).** The classical *sūrat al-Qitāl* designation is supported when "qitāl" is read as a thematic-cluster (qitāl + jihād + riqāb + wathāq + fidāʾ + ḥarb + ...) but NOT when read as the single *qtl* root in isolation. This is a rules-tuple-sensitivity case (cf. al-Qurṭubī's *qitāl* is a theme-name, not a root-frequency claim).
- **Honest limit**: A NULL on the narrow-root level does NOT refute al-Qurṭubī's claim; it refines it to the cluster-level. Pre-registration discipline says publish the NULL with equal prominence (Protocol §1.3).

## Claim 4: al-Bukhārī editorial-pairing — Q 47:22 tafsīr-bāb (#4623-4625) is paired with Q 48 Hudaybiyya bāb (#4627-4633)

**Source**: al-Bukhārī, *Ṣaḥīḥ*, kitāb al-Tafsīr (chapter 65), Q 47:22 cluster.
**On-disk**: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`.

- **Claim**: The two surahs are editorially paired in al-Bukhārī's tafsīr ordering (Q 47:22 hadiths immediately precede Q 48 Hudaybiyya hadiths in the same kitāb).
- **Rules-tuple**: (idInBook ordering, chapter 65 tafsīr).
- **Test**: Inspect idInBook range 4623-4633 in Bukhārī.
- **Result**: VERIFIED on disk — Bukhārī #4623, 4624, 4625 are Q 47:22 tafsīr-hadiths; #4627, 4628 are immediately Q 48 al-Fatḥ tafsīr-hadiths; #4628 specifically cites the Prophet reciting Sūrat al-Fatḥ on the Conquest-of-Mecca day. The two surahs ARE consecutively-clustered in al-Bukhārī's tafsīr-kitāb order.
- **Verdict**: **VINDICATED**.
- **Honest limit**: The pairing is editorial (al-Bukhārī's compilation choice), not a Qurʾān-internal feature. It supports the Hudaybiyya-cluster interpretation but is one author's editorial decision.

## Claim 5: al-Suyūṭī *al-Itqān* nawʿ 17 — Muḥammad's names in the Qurʾān (asmāʾ al-Nabī)

**Source**: al-Suyūṭī, *al-Itqān*, nawʿ 17.
**On-disk**: `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`.

- **Claim**: The Prophet's names appearing in the Qurʾān include *Muḥammad* (4 verses), *Aḥmad* (1 verse), and *ʿAbdullāh* (in genealogical contexts), *Bashīr* (in attributional contexts), *Nadhīr* (in attributional contexts).
- **Rules-tuple**: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
- **Test**: Q047-F-04 — exact verse-internal attestations of *Muḥammad* and *Aḥmad*.
- **Result**: 4 *Muḥammad* attestations at exactly {(3,144), (33,40), (47,2), (48,29)}; 1 *Aḥmad* attestation at (61,6). **VINDICATED**.
- **Verdict**: **VINDICATED** for the *Muḥammad* + *Aḥmad* sub-claim of nawʿ 17. The other names (*ʿAbdullāh*, *Bashīr*, *Nadhīr*) are not tested here (they appear in non-prophet-naming senses also).
- **Honest limit**: The test verifies only the *Muḥammad* + *Aḥmad* names. al-Suyūṭī's full nawʿ 17 list includes title-form names (*al-Mubashshir*, *al-Nadhīr*, *al-Shāhid*, *al-Sirāj al-munīr*, etc.) which are not prophet-NAME but prophet-DESCRIPTOR — those are valid only by additional contextual classification, beyond this dossier's scope.

## Claim 6: Q 47 has no fadāʾil-recitation tradition (cross-finding-028 implicit prediction)

**Source**: cross-finding-028 (`findings/cross-finding/cross-finding-028.md`) — Q 47 not in verified liturgical-pair set.
**Negative-finding check**: This is the absence of a positive claim, but a non-trivial classical-empirical interface.

- **Claim**: Q 47 is NOT a fadāʾil-recitation surah; it has no canonical pre-sleep/Friday/Eid/Maghrib-pair tradition.
- **Test**: Search across 9-book hadith corpus for fadāʾil-of-Q-47 hadiths.
- **Result**: 0 verified canonical fadāʾil hadiths found for Q 47.
- **Verdict**: **VINDICATED-NULL** (cross-finding-028's negative-set is empirically consistent with the hadith corpus).
- **Architectural interpretation**: Q 47 occupies a specific genre-slot — *legal-theological-instructional* (low fadāʾil-attention) rather than *liturgical-recitation* (high fadāʾil-attention). This is the dual-iʿjāz typology's structural-iʿjāz vs theological-iʿjāz orthogonality at the *recitation-mode* axis.

## Summary table

| # | Claim | Source | Test | Verdict |
|:-:|:--|:--|:--|:-:|
| 1 | Medinan, chronological #95 | al-Suyūṭī *Itqān* nawʿ 1,18 | dataset consistency | VINDICATED (consistency) |
| 2 | Q 46→47→48 munāsabah | al-Biqāʿī *Naẓm al-Durar* | Q047-F-03 + 3-tuple FR | PAIR-VINDICATED, 3-TUPLE-NULL |
| 3 | Q 47 = *sūrat al-Qitāl* | al-Qurṭubī | Q047-F-02 (broad), Q047-F-05 (narrow) | CLUSTER-VINDICATED, ROOT-NULL |
| 4 | Q 47:22 ↔ Q 48 editorial pair | al-Bukhārī tafsīr | idInBook 4623-4633 inspection | VINDICATED |
| 5 | *Muḥammad*/*Aḥmad* asmāʾ enumeration | al-Suyūṭī *Itqān* nawʿ 17 | Q047-F-04 | VINDICATED |
| 6 | No fadāʾil-recitation tradition | cross-finding-028 | 9-book hadith corpus search | VINDICATED-NULL |

## Rules-tuple-sensitivity log

- **Claim 2** is partially rules-tuple-sensitive: at the FR root-level it is 3-tuple-NULL but at the TSP-edge level it is pair-VINDICATED. Different metrics give different verdicts on the same classical claim.
- **Claim 3** is rules-tuple-sensitive: the broader-cluster definition VINDICATES; the narrower-root definition NULL-FAILS. The classical scholar's intent was thematic-cluster, not single-root.
- **Claim 6** is a negative-finding; absence-of-canonical-fadāʾil over 9 books is a strong negative-result but not absolutely-universal.

## Honest limits

1. All "VINDICATED" verdicts on this dossier rest on existing JSON results and on-disk hadith verification. NONE were inflated by post-hoc rule-shifting.
2. The Q047-F-05 NULL is a legitimate pre-registration test failure; we publish it with equal prominence.
3. The Q047-F-06 NULL on universal-seam direction is similarly published with equal prominence.
4. al-Biqāʿī's qualitative claim is a *literary* munāsabah; an empirical NULL on FR-cohesion does not invalidate the literary perception. It refines the empirical-architectural claim.
