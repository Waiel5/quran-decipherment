---
surah: 6
test_id: Q006-F-05
title: Q 6:103 lā tudrikuhu al-abṣār — divine-incomprehensibility lexeme density audit (al-Bāqillānī iʿjāz al-tawḥīd)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 4
bonferroni_family: Q006-F-05-divine-incomp
alpha_bon: 0.0125
direction_locked: MAX (Q6:103 = corpus-MAX single verse on combined incomprehensibility score)
---

# Q006-F-05 — Pre-registration: Q 6:103 *lā tudrikuhu al-abṣār* iʿjāz al-tawḥīd audit

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Verse Q 6:103 — *lā tudrikuhu al-abṣāru wa-huwa yudriku al-abṣāra wa-huwa al-laṭīfu al-khabīr* ("vision does not grasp Him, but He grasps vision; He is the Subtle, the All-Aware") — is the **corpus-MAXIMUM single verse on a 4-cell divine-incomprehensibility lexeme score**. al-Bāqillānī (*Iʿjāz al-Qurʾān*) cites this verse as *iʿjāz al-tawḥīd* — the verse that maximally compresses divine-incomprehensibility into a single creedal formula. H1 quantitatively tests this 1000-year-old classical claim.

**Direction:** Q 6:103 = rank 1 / 6,236 verses on the joint score (LOCKED).

**H0:** Q 6:103 ≥ rank 10 on the joint score.

**Pre-commit violation:** Q 6:103 ≥ rank 50.

## 2. Operational definition

**4-cell divine-incomprehensibility lexeme set (locked surface-form regex):**

| Cell | Lexical signature | Theological function |
|:-:|:--|:--|
| C1 | لا تدركه (negative-grasping of Him) | apophatic — eye/vision cannot encompass Him |
| C2 | يدرك (He-grasps + "abṣār" / "qulūb" object) | cataphatic-inverted — He encompasses |
| C3 | اللطيف (al-Laṭīf, the Subtle) | divine-name attribute |
| C4 | الخبير (al-Khabīr, the All-Aware) | divine-name attribute |

**Cell scores per verse v:**
- score_C1(v) = 1 if `\bلا\s+تدركه\b` matches in v, else 0
- score_C2(v) = 1 if `\bيدرك\b` ∧ (verse contains أبصار OR قلوب) — He-grasps with object, else 0
- score_C3(v) = 1 if `\bاللطيف\b` matches, else 0
- score_C4(v) = 1 if `\bالخبير\b` matches, else 0
- joint_score(v) = score_C1 + score_C2 + score_C3 + score_C4 ∈ {0, 1, 2, 3, 4}

**Cell A — primary:** rank of Q 6:103's `joint_score` among all 6,236 verses (descending).
**Cell B — supplementary:** count of verses corpus-wide with joint_score = 4 (perfect-score). Pre-reg expectation: this set is small (≤ 3 verses).
**Cell C — Bonferroni-conservative:** for each of 4 cells, count corpus-wide verses scoring 1; report Q 6:103's overlap-uniqueness.

Bonferroni k=4 (across the 4 cells, since each is a separate lexeme-claim), α_bon = 0.0125.

## 3. Test statistic / Success / Failure

- **CONFIRMED:** Q 6:103 is rank 1 (joint_score = 4 AND no other verse has joint_score = 4) — the verse uniquely satisfies all 4 cells.
- **DIRECTIONAL:** Q 6:103 is in a tied rank-1 set of size ≤ 3 verses.
- **NULL:** Q 6:103 has joint_score < 4, OR there are >3 verses tied at rank 1.
- **Pre-commit violation:** Q 6:103 has joint_score ≤ 1.

Cell B descriptively: list the verses that tie or exceed Q 6:103.

## 4. Garden-of-forking-paths log (BEFORE observation)

Author has read Q 6:103 directly and confirmed that the verse contains:
- لا تدركه (Cell C1 — UNIQUE: this is a corpus rare formula)
- يدرك الأبصار (Cell C2)
- اللطيف (Cell C3)
- الخبير (Cell C4)

Author has NOT computed corpus-wide ranking. Pre-observation expects Q 6:103 to be the unique 4-cell verse, but locks the test in case there are tied verses.

The 4-cell set is derived from al-Bāqillānī's *Iʿjāz al-Qurʾān* discussion of Q 6:103 (the verse cited as paradigmatic *iʿjāz al-tawḥīd*) and from the kalām tradition's distinction between apophatic (C1: negative grasping) and cataphatic (C2-C4: positive divine-attributes) theology. The four cells are the four canonical theological signatures of divine-transcendence-with-attributes.

The test is direction-locked-MAX. Failure (Q 6:103 NOT being uniquely top) would refine al-Bāqillānī's claim — perhaps the verse's iʿjāz status is theological-rhetorical, not lexically-uniquely-distinctive. We publish the result regardless.

## 5. Honest limits known a priori

- The 4-cell lexeme set is one operationalization. al-Bāqillānī's claim is also rhetorical (the *concision* of the verse, the apophatic-cataphatic chiasm in `lā tudrikuhu al-abṣār wa-huwa yudriku al-abṣār`). Lexeme-counting captures lexical density only, not rhetorical-structural compression. A separate test would need to operationalize the chiasm.
- اللطيف and الخبير also appear paired in other verses (e.g., Q 33:34, Q 67:14). These are 2-cell verses, not 4-cell. We expect Q 6:103 to be UNIQUELY 4-cell.
- Cell C2 disambiguation: يدرك as transitive verb requires an object; we restrict to the {abṣār, qulūb} object set per al-Bāqillānī's original formulation.

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at pre-reg-completion. Embedded into `surahs/scripts/Q006_F_05_v103_tawhid_ijaz.py`.
