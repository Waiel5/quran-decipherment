---
surah: 64
test_id: Q064-F-04
title: Q 64 chronology classical-claim audit — Meccan vs Medinan disagreement enumeration
file_type: pre-registration
date_locked: 2026-05-09
seed: n/a (philological audit)
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q064-F-04-chronology-audit
alpha_bon: 0.05
---

# Q064-F-04 — Pre-registration: Q 64 chronology classical-claim audit

## 1. Hypothesis (locked before observation)

Q 64 al-Taghābun is one of a small number of Quranic surahs where classical Meccan/Medinan classification is contested. Standard modern editions (Tanzil Egyptian Standard, Wikipedia/Nöldeke) assign **Medinan**. But the early tafsīr-traditional record preserves a **Meccan-with-Medinan-supplement** position attributed to ʿAṭāʾ ibn Yasār (via Ibn Isḥāq) and others. This pre-reg formalizes the audit.

**H1 (locked direction):** Among classical scholars cited in standard tafsīr survey (al-Ṭabarī, al-Wāḥidī, al-Baghawī, al-Suyūṭī, al-Biqāʿī, ʿAṭāʾ ibn Yasār, Ibn Isḥāq, al-Mawdūdī, al-Zarkashī), there exists at least one **non-trivial dissent** from the majority Medinan classification of Q 64.

**H2 (locked direction):** The dissent is concentrated on Q 64 vv. 1-13 (cosmological + theological main body) being Meccan, with vv. 14-16 (the wives-and-children + taqwā passage) being Medinan as the chronological hinge.

**H3 (locked direction):** The dissent's chronological-anchor evidence (asbāb al-nuzūl) for vv. 14-16 attaches the verses to the Late-Meccan emigration period (Hijra-blocking by family) — placing them precisely at the Mecca→Medina TRANSITION rather than firmly in either era.

**H0 (rare for an audit):** No documented classical dissent exists; classification is uniform.

## 2. Operational definitions

- **Sources surveyed** (locked list, no expansion post-hoc):
  - al-Ṭabarī, *Jāmiʿ al-Bayān*, ad Q 64 (via spa5k-tafsir-api/ar-tafsir-al-tabari/64.json)
  - al-Baghawī, *Maʿālim al-Tanzīl*, ad Q 64 (via spa5k-tafsir-api/ar-tafsir-al-baghawi/64.json)
  - al-Wāḥidī, *Asbāb al-Nuzūl*, ad Q 64:14 (via spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/64.json)
  - Modern *Maʿārif al-Qurʾān* (via spa5k-tafsir-api/en-tafsir-maarif-ul-quran/64.json)
  - al-Suyūṭī, *al-Itqān*, nawʿ 1 (Meccan/Medinan): chronological listing
  - al-Biqāʿī, *Naẓm al-Durar*, ad Q 64
  - Ibn Isḥāq, *Sīrat Rasūl Allāh*, via al-Ṭabarī's isnād chain
- **Audit format**: For each source, record (a) the Meccan/Medinan verdict, (b) any cited isnād authority (Ibn ʿAbbās, ʿAṭāʾ, ʿIkrimah, Mujāhid, Qatāda, etc.), (c) any verse-specific exception.
- **Trivial dissent** = a single asbāb anecdote about one verse without a global classification claim. **Non-trivial dissent** = a claim that the entire surah, or its main body, is the OPPOSITE chronology from majority view.

## 3. Test statistic

- Verdict-by-source table.
- Count of sources with non-trivial dissent.
- Identification of the verses-at-the-hinge (per H2).

## 4. Success / Failure

- **CONFIRMED**: Non-trivial classical dissent documented (H1) AND localized to vv. 14-16 (H2) AND anchored at Hijra (H3). All 3 PASS.
- **PARTIAL**: Some pass.
- **REFUTED**: No dissent found.

## 5. Honest limits known a priori

- Tafsīr survey is necessarily SECONDARY-TRIANGULATED unless the original manuscripts are physically VERIFIED (MW-6 verification tagging required).
- The spa5k-tafsir-api texts are widely-used digital editions; treat them as SECONDARY-TRIANGULATED (not VERIFIED) per MW-6.
- This audit makes NO claim about which chronology is "correct" — it documents the diversity of classical positions.
- Empirical pre-anchor (DISCLOSED): preliminary inspection of al-Baghawī Q 64 entry shows the opening note "مدنية - قال عطاء هي مكية إلا ثلاث آيات..." which seeds H2 directly. The pre-commit is locked at this single anchor; further sources may or may not reinforce.

## 6. Rules-tuple

`(secondary-triangulated tafsīr survey, MW-6 PENDING-physical-verification, qualitative-philological)`.

## 7. Bonferroni

k = 1 (single audit family). α_bon = 0.05.

## 8. SHA256 lock

n/a — qualitative audit, recorded in `06-novel-findings.md` and `05-classical-claims-audit.md`.
