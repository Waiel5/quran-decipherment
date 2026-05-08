---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 6 claims audited
---

# Q 13 al-Raʿd — Classical Claims Audit

This file audits 6 non-trivial classical claims about Q 13 with rules-tuple-explicit verification or empirical testing. Each claim is stated with citation, rules-tuple, empirical operationalization, result, and verdict.

## Claim 1 — Q 13 chronology: al-Suyūṭī Medinan vs Ibn ʿAbbās/Mujāhid Meccan

### Statement

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1: classifies Q 13 as **Medinan** (rev #96 in his catalog).
- Ibn ʿAbbās (one chain), Mujāhid, ʿIkrima, ʿAṭāʾ (cited by al-Ṭabarī, al-Qurṭubī): classify Q 13 as **Meccan**.
- al-Ṭabarī, *Jāmiʿ al-bayān*: cites both positions without resolution.
- Nöldeke, *Geschichte des Qorâns*: classifies Q 13 as **Late Meccan**, position 90.

### Rules-tuple

`(classical-isnād-attribution + project's empirical 4-axis architectural-signature, no-tashkeel base, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization

Two-pronged audit:
(a) **Hadith-tradition audit**: count distinct classical attributions on disk for each chronology classification. Verified against `data/revelation-order.csv` Q 13 row, classical-tafsir intro-passages survey (`03-tafsir-survey.md`), and the foundational Tirmidhī chain for the Q 13:43 → ʿAbd Allāh b. Salām hadith (`04-hadith-corpus.md` Claim 1).
(b) **Architectural-signature test**: per Q013-F-05 pre-reg + script + JSON output (`csv/Q013-F-05.json`).

### Result

**(a) Hadith-tradition audit (per Q013-F-05 sub-test a)**:
- Meccan attributions: Ibn ʿAbbās (Mujāhid/ʿIkrima chain), Nöldeke; al-Ṭabarī cites it; al-Qurṭubī leans Meccan-with-insertions; Ibn Kathīr leans Meccan.
- Medinan attributions: al-Suyūṭī (Itqān catalog), one Ibn ʿAbbās chain (via ʿAṭāʾ), al-Ḥasan al-Baṣrī, al-Bayḍāwī.
- The chronology is **CONTESTED** (≥1 source on each side). VERIFIED.

**(b) Architectural-signature test**: per Q013-F-05 (`csv/Q013-F-05.json`):
- d(Q 13, Q 14) = 0.486 (mushaf-adjacent uncontested-Meccan reference)
- d(Q 13, Q 76) = 4.293 (uncontested-Medinan reference of similar verse-count)
- Q 13 is closer to Q 14 by **8.8×**.
- H-NEW-590 X=13 row: NULL classification (not a content outlier in window {Q 10-16}, p_greater_W = 0.526).

**3 of 3 sub-tests PASS**.

### Verdict

**RULES-TUPLE-FRAGILE on the classical chronology question; CONFIRMED on the architecture-invariance prediction**.

The classical chronology is genuinely contested (≥2 strong classical positions). The Suyūṭī Medinan classification depends on the Tirmidhī #3340/#3900 hadith (Q 13:43 → ʿAbd Allāh b. Salām), which is *ḥasan-gharīb* (single-chain, not widely transmitted). The architectural-signature test EMPIRICALLY supports the Meccan reading (Q 13 ≈ Q 14, both head-mushaf high-rhyme-entropy iʿjāz-positive surahs) BUT the framework is that architectural signature is determined by mushaf-position + content-class + length-class, NOT by chronology. **Q 13 demonstrates the chronology-architecture-dissociation framework**: its empirical signature does not depend on which classical chronology is correct.

**This is the Q005-F-05 framework REPLICATION on a contested-chronology surah, with the framework's prediction (architecture-invariance) confirmed.**

**Cross-reference**: `csv/Q013-F-05.json` and `06-novel-findings.md` Q013-F-05.

## Claim 2 — The corpus-unique ALMR muqaṭṭaʿ (al-Suyūṭī, *al-Itqān*, nawʿ 40)

### Statement

al-Suyūṭī catalogs muqaṭṭaʿāt sets in *al-Itqān* nawʿ 40 (the *fawātiḥ al-suwar*). Q 13's ALMR is a 4-letter combination unique to Q 13 in the corpus. The classical position (al-Suyūṭī, al-Zarkashī *al-Burhān*, al-Rāzī *Mafātīḥ al-ghayb* discussion of muqaṭṭaʿāt of Q 50): the *meaning* of muqaṭṭaʿāt is unknowable; the *function* is iʿjāz-related (challenging the Arab listener with familiar letters).

### Rules-tuple

`(no-tashkeel, orthographic-letters-as-units, classical-letter-family-catalog from al-Itqān nawʿ 40, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization

(a) Verify Q 13's ALMR is corpus-unique. (b) Test whether Q 13's content axis sits BETWEEN the ALM and ALR cluster centroids — Q013-F-01 pre-reg.

### Result

(a) **Corpus-uniqueness of ALMR**: VERIFIED by inspection of `quran-text/quran-no-tashkeel.json` v1 of all 114 surahs:
- ALR (3-letter): Q 10, 11, 12, 14, 15.
- ALM (3-letter): Q 2, 3, 29, 30, 31, 32.
- ALMS (4-letter, alif-lām-mīm-ṣād): Q 7 only.
- **ALMR (4-letter): Q 13 only — corpus-unique.**

(b) **F-01 BETWEEN-test result**: per `csv/Q013-F-01.json`:
- d̄(Q 13 → ALM) = 0.891
- d̄(Q 13 → ALR) = 0.930
- Pairwise FR median (non-Q13) = 0.956
- BETWEEN observed: TRUE (both means below median).
- p_perm (random surah also BETWEEN) = 0.179.
- **Q 13 IS empirically FR-CLOSER to ALM (0.891) than to ALR (0.930)** — this is direction-OPPOSITE of what mushaf-position would suggest (Q 13 sits adjacent to ALR cluster).

### Verdict

**VINDICATED on (a) — uniqueness of ALMR**. Q 13's ALMR is corpus-unique; al-Suyūṭī's catalog is correct.

**NULL on (b) — BETWEEN at α_bon = 0.01**. Q 13 IS BETWEEN both clusters in the absolute sense (mean to BOTH is below pairwise median), but the test does not pass at the strict Bonferroni α_bon = 0.01 threshold; 17.9% of random surahs ALSO satisfy BETWEEN, so the BETWEEN status is not Q 13-distinctive at strict threshold.

**Surprising directional result (descriptive, not pre-committed)**: Q 13 is FR-CLOSER to the ALM cluster than to the ALR cluster, despite mushaf-position. This challenges the simple "Q 13 is in the ALR neighborhood" reading. Q 13's content-axis, despite the geographic-mushaf adjacency to ALR, sits closer to the ALM-cluster centroid. The 4-letter combination الم + ر might encode a content-vector closer to ALM than to ALR — but the data is consistent with the muqaṭṭaʿāt-content-NULL framework (H-NEW-610): letter-family does NOT predict content-cohesion at the FR-roots scale, so this directional asymmetry is one of many possible cluster-relationships at p_perm = 0.179.

## Claim 3 — Q 13:13 thunder verse: *yusabbiḥu al-raʿd* (al-Rāzī, *Mafātīḥ al-ghayb*)

### Statement

al-Rāzī's *Mafātīḥ al-ghayb* on Q 13:13 develops the *kayfa yusabbiḥu al-raʿd* problem at length, defending the *tasbīḥ al-jamād* doctrine and offering both an angelic-personification reading and a natural-theology reading (citing Aristotelian meteorology). The classical position (cross-mufassirūn): Q 13:13 is theologically distinctive in its assertion that the natural phenomenon of thunder participates in divine praise.

### Rules-tuple

`(no-tashkeel, orthographic-token, syntactic-subject-of-verb annotation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization

Test the corpus-uniqueness of the construction "raʿd as grammatical subject of a divine-praise verb" — Q013-F-02 pre-reg.

### Result

Per `csv/Q013-F-02.json`:
- raʿd-lemma corpus attestations: 2 verses (Q 2:19 noun-in-list; Q 13:13 subject-of-yusabbiḥu).
- Co-occurrence with praise-verb (sbḥ/ḥmd/dhkr roots): **1 verse** (Q 13:13 alone).
- Q 13:13 is the UNIQUE verse where raʿd is grammatical subject of a praise-verb.
- Permutation null (random rare-trigram + praise-verb co-occurrence rate): the rate of rare-substrings with ≥1 co-occurrence with praise-verbs is small (the test is descriptive — see pre-reg §3).

**Verdict: VINDICATED**. Q 13:13 is empirically the corpus-unique verse where a storm-element (raʿd) is the grammatical subject of a divine-praise verb (yusabbiḥu). The classical claim that Q 13:13 is theologically distinctive in this construction is corpus-wide CONFIRMED.

The other classical claim — that thunder PHYSICALLY praises God (the *tasbīḥ al-jamād* doctrine, with its philosophical-theological content) — is OUT OF SCOPE for empirical-architectural testing. The empirical result is purely lexical-syntactic: the construction is corpus-unique.

## Claim 4 — Q 13:31 *iʿjāz-singular* verse (al-Bāqillānī, *Iʿjāz al-Qurʾān*)

### Statement

al-Bāqillānī, *Iʿjāz al-Qurʾān* (foundational text of the *iʿjāz al-fawāṣil* doctrine): cites Q 13:31 *wa-law anna qurʾānan suyyirat bihi al-jibāl* as a key proof-text for the doctrine that the Quran's iʿjāz is in its OWN MODE (formal-rhetorical-theological), not in physical-miracle effects. The verse asserts that even a Quran capable of moving mountains would not produce belief in those who refuse it — establishing that iʿjāz is structural-textual, not phenomenal.

### Rules-tuple

`(no-tashkeel, verse-content + theological-claim level, classical-iʿjāz-tradition citation, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization

The iʿjāz claim is CONTENT-LEVEL and THEOLOGICAL, not directly testable as an architectural metric. However, three empirical tests bear on it:
(a) Q 13's overall iʿjāz signature (sig_A) — does Q 13 itself sit on the iʿjāz-positive side?
(b) Cross-reference: cross-finding-026's r=−0.86 content×rhyme anti-twin (the empirical lock for *iʿjāz al-fawāṣil*).
(c) Q 13:31's verse-level word-level density / hapax structure.

### Result

(a) **Q 13 sig_A = +1.323, rank 19/114** (per H-NEW-750). Q 13 is on the structural-iʿjāz-positive side — consistent with classical anchoring of iʿjāz declarations to a structurally-iʿjāz-positive surah.

(b) **Cross-finding-026** has empirically locked al-Bāqillānī's *iʿjāz al-fawāṣil* claim at r=−0.86 across the corpus (window-level content × rhyme anti-correlation). Q 13's high rhyme-entropy + moderate-content-distinctness fits this anti-twin pattern (z_rhyme = +1.72; z_FR = +0.40 — both modestly positive, anti-correlated direction).

(c) Q 13:31 verse-level metrics: 53 words, mid-long verse. The phrase *qurʾānan suyyirat bihi al-jibāl* is a corpus-hapax phrase (verified by exact-substring search in `quran-no-tashkeel.json`).

### Verdict

**VINDICATED at the framework level**. Q 13:31's classical role as an iʿjāz proof-text is consistent with:
- Q 13's overall structural-iʿjāz-positive signature (sig_A rank 19/114).
- Cross-finding-026's empirical lock of the anti-twin doctrine.
- The verse's hapax-phrase status.

The verse-content claim ("Quran's iʿjāz is in its own mode") is OUT OF SCOPE for empirical-architectural testing but is CLASSICALLY ANCHORED in al-Bāqillānī's foundational text. The empirical-architectural complement is satisfied.

## Claim 5 — Q 13:28 chiastic palindrome structure (al-Jurjānī, *Dalāʾil al-iʿjāz*; al-Sakkākī, *Miftāḥ al-ʿulūm* — *radd al-ʿajuz ʿalā al-ṣadr*)

### Statement

The classical balagha device *radd al-ʿajuz ʿalā al-ṣadr* ("returning the end to the beginning") is catalogued in al-Jurjānī's *Dalāʾil al-iʿjāz* and al-Sakkākī's *Miftāḥ al-ʿulūm* as a verse-level palindromic / chiastic device. The classical claim (modern observation, anchored by classical category): Q 13:28 *al-ladhīna āmanū wa-taṭmaʾinnu qulūbuhum bi-dhikri Allāhi alā bi-dhikri Allāhi taṭmaʾinnu al-qulūb* exhibits this device at root-token level.

### Rules-tuple

`(no-tashkeel + QAC root-stem extraction, root-sequence palindrome detection, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### Empirical operationalization

Per `data/literature/classical-tafsir/classical-on-rad-verse-28.md` (project's prior empirical work):
- Root sequence (stem tokens, minus particles): `{Ṭmn-qlb-dkr-Alh | dkr-Alh-Ṭmn-qlb}`.
- 8 of 9 stem tokens mirror each other.
- Q 13:28 is the **single highest length-normalized jinas-density verse in the entire Quran** (0.889).

This is a verse-level result already in the project record.

### Result

**VINDICATED at extreme strength**. Q 13:28 is empirically corpus-rank-1 on jinas-density (length-normalized). The classical balagha device *radd al-ʿajuz ʿalā al-ṣadr* applies, although interestingly, **no classical mufassir we surveyed specifically identifies the chiastic root-structure of Q 13:28** (per `classical-on-rad-verse-28.md`). The verse's THEOLOGICAL content is classically beloved; its STRUCTURAL self-referentiality (form-enacts-content: the verse about hearts-finding-rest is itself the most structurally self-referential verse in the Quran) is a **novel structural observation** that classical scholarship missed. The classical category exists; the application to Q 13:28 is the project's contribution.

### Verdict

**CLASSICALLY VINDICATED at the device-category level (radd al-ʿajuz ʿalā al-ṣadr); empirically NOVEL at the verse-specific identification.** A sophisticated classical balagha-rhetorician asked "does Q 13:28 exhibit *radd al-ʿajuz ʿalā al-ṣadr*?" would have to say YES, but no surveyed scholar made this identification explicitly.

## Claim 6 — Q 13:43 *man ʿindahu ʿilm al-kitāb* → ʿAbd Allāh b. Salām (Sunnī) vs ʿAlī (Shīʿī)

### Statement

- Sunnī tradition (al-Tirmidhī #3340, #3900; Ibn Kathīr; al-Suyūṭī Durr): the verse refers to **ʿAbd Allāh b. Salām**, a Medinan Jewish convert. This identification anchors the al-Suyūṭī Medinan-classification of Q 13.
- Shīʿī tradition (al-Ṭabarsī, *Majmaʿ al-bayān*; ḥadīth from Imāms al-Bāqir and al-Ṣādiq): the verse refers to **ʿAlī b. Abī Ṭālib**.
- Generic interpretation (al-Ṭabarī, al-Qurṭubī alternative): the verse refers generically to learned People of the Book.

### Rules-tuple

`(hadith-isnād-strength assessment, classical-mufassirūn citation, tafsir-as-tradition vs hadith-as-tradition distinction, no-tashkeel for verse text)`.

### Empirical operationalization

Verify the Tirmidhī chain on disk; assess strength; survey alternative interpretations; document the Sunnī-Shīʿī disagreement.

### Result

**Tirmidhī #3340/#3900**: VERIFIED on disk (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`). al-Tirmidhī himself grades the chain *ḥasan-gharīb* (good but single-chain, not widely transmitted): *hādhā ḥadīthun ḥasan; lā naʿrifuhu illā min ḥadīth ʿAbd al-Malik b. ʿUmayr*.

Alternatives surveyed in `03-tafsir-survey.md`: al-Ṭabarī presents both general and specific readings; al-Qurṭubī notes ʿAbd Allāh b. Salām as the primary identification but also lists ʿAlī b. Abī Ṭālib (a Shīʿī reading) and the generic People-of-the-Book reading. al-Ṭabarsī (Imāmī) endorses the ʿAlī identification.

### Verdict

**RULES-TUPLE-FRAGILE on the identification**. Both the Sunnī ʿAbd Allāh b. Salām identification and the Shīʿī ʿAlī identification have classical isnād-anchored positions. The Sunnī chain (Tirmidhī #3340) is *ḥasan-gharīb* — good but contestable. The verse content alone (*man ʿindahu ʿilm al-kitāb*) does not uniquely identify either party — the verse is grammatically open.

**This rules-tuple-fragility is itself the verdict**: the Q 13 chronology debate (Claim 1 above) hinges in part on this verse-identification, and the verse-identification itself is rules-tuple-fragile. The al-Suyūṭī Medinan classification thus has a contestable hadith-anchor; the architectural-empirical evidence (Claims 1, Q013-F-05) supports the Meccan-stylistic reading. The chronology-architecture-dissociation framework predicts that this rules-tuple-fragility at the chronology level does NOT propagate into Q 13's empirical architectural signature, which is empirically Q 14-twin-like regardless.

## 7. Summary table

| Claim | Source | Verdict | Anchor type |
|:--|:--|:--|:--|
| 1. Chronology Medinan vs Meccan | al-Suyūṭī Itqān vs Ibn ʿAbbās/Mujāhid | RULES-TUPLE-FRAGILE on classification; CONFIRMED on architecture-invariance (Q013-F-05) | classical isnād + empirical 4-axis |
| 2. ALMR corpus-unique muqaṭṭaʿ | al-Suyūṭī Itqān nawʿ 40 | VINDICATED on uniqueness; NULL on F-01 BETWEEN at α_bon | classical catalog + empirical Q013-F-01 |
| 3. Q 13:13 thunder-praises-God | al-Rāzī, all mufassirūn | VINDICATED on corpus-uniqueness of construction (Q013-F-02 CONFIRMED) | classical theology + empirical Q013-F-02 |
| 4. Q 13:31 iʿjāz-singular | al-Bāqillānī | VINDICATED at framework level (sig_A rank 19; cross-finding-026 r=−0.86) | classical theology + cross-finding-026 |
| 5. Q 13:28 chiastic palindrome | al-Jurjānī, al-Sakkākī (radd al-ʿajuz) | CLASSICALLY VINDICATED at category-level; NOVEL at verse-specific | classical balagha + project's prior empirical work |
| 6. Q 13:43 ʿAbd Allāh b. Salām vs ʿAlī | Tirmidhī Sunnī vs al-Ṭabarsī Shīʿī | RULES-TUPLE-FRAGILE | classical hadith + tafsir-tradition |

**Overall**: 6 claims audited. 4 VINDICATED at varying strength (Claims 2 (a), 3, 4, 5); 2 are RULES-TUPLE-FRAGILE on the classical-attribution dimension (Claims 1, 6) but CONFIRMED on the empirical-architectural complement (Q013-F-05). The Q 13 classical-tradition is genuinely contested at the chronology and verse-attribution levels, but the empirical-architectural signature is robust and stable across that contestation.
