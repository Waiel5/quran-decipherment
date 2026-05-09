---
surah: 62
test_id: Q062-F-04
title: Classical Friday-recitation hadith corpus audit (Q 62 + Q 63 vs Q 62 + Q 88)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 4
bonferroni_family: Q062-specialist
alpha_bon: 0.0125
parent_finding: cross-finding-009 cluster-network C7_friday liturgical-prominence anchor
---

# Q062-F-04 — Pre-registration: Classical Friday-recitation hadith audit

## 1. Hypotheses under audit (each as a separate locked-claim cell)

**Claim 1 (brief-stated assertion under audit):** "Bukhārī ḥadīth on Q 62 + Q 63 Friday recitation" exists in the on-disk digital corpus.

**Claim 2 (canonical-tradition claim):** The Q 62 + Q 63 al-Munāfiqūn pair is recited at Friday Ẓuhr per the Abū Hurayra-Marwān-Madīna chain (Ibn Abī Rāfiʿ → Jaʿfar → Marwān-Abū Hurayra leadership reconstruction).

**Claim 3 (competing canonical-tradition claim):** A second Friday-pair tradition has Q 62 followed by Q 88 al-Ghāshiya, attributed to al-Nuʿmān b. Bashīr via al-Ḍaḥḥāk b. Qays.

For each claim, the test is YES/NO at the on-disk hadith-corpus search level.

## 2. Operational definition

- **Source corpus**: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/*.json` (9 books: bukhari, muslim, tirmidhi, nasai, abudawud, ibnmajah, malik, darimi, ahmed). SHA-256 of each book file captured at run-time.
- **Match predicate**:
  - **Arabic**: any of {`سورة الجمعة`, `بسورة الجمعة`, `بِسُورَةِ الْجُمُعَةِ`} appearing as a substring in `arabic`.
  - **English** (case-insensitive in `english.text` ∪ `english.narrator`): any of {"surah al-jumu", "sūrat al-jumu", "al-jumu’ah", "al-jumua", "al-jumuah"}.
- **Chain classification**:
  - **Abū Hurayra chain**: hits whose narrator-field references `abu hurai` or `abi rafi` AND whose body references `al-munafiq`/`hypocrite`/`when the hypocrites` or `المنافقون`.
  - **Nuʿmān b. Bashīr chain**: hits whose narrator references `nuʿmān`/`al-nu`/`nu'man` OR whose body references `overwhelming event`/`has the story`/`الغاشية`/`al-ghāshiya`.

## 3. Test statistic

- Per claim, 1 of {VERIFIED, NOT-FOUND}.
- Per claim, list of (book, idInBook) attestations.
- Per book, total Q 62-Friday-recitation hits.

## 4. Permutation null

None — this is an MW-6 verification audit (existence claim), not a probabilistic-distribution test. The output is hadith-citation tagging.

## 5. Success / Failure

- **CONFIRMED on Claim 1**: Bukhārī-internal Q 62 Friday recitation hit exists.
- **CORRECTED on Claim 1**: Bukhārī-internal Q 62 Friday recitation hit does NOT exist; the brief's "Bukhārī" attribution is a citation error and the Q 62 + Q 63 chain is anchored at Tirmidhī / Abū Dāwūd / Ibn Mājah / Mālik / Muslim / Nasāʾī / Dārimī (one or more).
- **VERIFIED on Claim 2**: at least 1 hit in the Abū Hurayra chain in canonical books.
- **VERIFIED on Claim 3**: at least 1 hit in the Nuʿmān b. Bashīr chain.

## 6. Honest limits known a priori

- **Digital-corpus dependency**: ahmedbaset-json is one digital corpus; classical printed editions may carry different hadith-numbering. Per MW-6, all numeric anchors are tagged VERIFIED-DIGITAL, not VERIFIED-PHYSICAL.
- **Substring search**: false negatives possible if a hadith uses a synonym phrasing not captured by the predicate set. Mitigation: predicate set covers the canonical Arabic and standard English transliterations.
- **The two Friday-pair traditions are NOT mutually exclusive**: a Prophet may have used both at different occasions; the classical fiqh literature reads both as legitimate.
- **Bukhārī is not the universally-canonical anchor for every Q-N hadith**; the audit corrects a specific brief-stated attribution, not a categorical claim about Bukhārī's canon-status.

## 7. Falsification

If Bukhārī DOES contain a Q 62-Friday-recitation hadith in the digital corpus, then Claim 1 is VERIFIED and the brief's attribution is correct. If Q 62 + Q 63 chain is NOT found in any of the 9 books, then Claim 2 is FALSIFIED — implausible but a real falsifier.

## 8. Cross-references

- Parent: cross-finding-009 META-cluster network, C7_friday liturgical-cluster anchor.
- Sibling: H-NEW-68 Friday-recitation cluster shape-cohesion (NULL — Friday cluster is FUNCTIONAL, not shape-based).
- HANDOFF/01-WHAT-WE-KNOW.md "META-CLUSTER NETWORK" Q 62 4-cluster meta-hub.

## 9. Replication

- Script: `surahs/Q062-al-jumuah/scripts/Q062_F_all_tests.py` function `q062_f_04`.
- Output: `surahs/Q062-al-jumuah/csv/Q062-F-04.json`.
- 9 hadith-book SHA-256 captured into the JSON at run-time.
