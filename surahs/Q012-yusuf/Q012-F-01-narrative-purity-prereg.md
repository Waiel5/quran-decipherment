---
surah: 12
test_id: Q012-F-01
title: Narrative-purity index across the 114 surahs (Q 12 = aḥsan al-qaṣaṣ test)
file_type: pre-registration
date_locked: 2026-04-28
seed: 12010
---

# Q012-F-01 — Pre-registration: narrative-purity index

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 12 Yūsuf has the **highest narrative-vocabulary density per verse** among the 114 surahs. The Quran's self-referential epithet *aḥsan al-qaṣaṣ* (Q 12:3) corresponds empirically to the surah being maximally narrative-vocabulary saturated.

**H0:** Q 12 ranks no better than median (≥ rank 57) on narrative-purity.

**Direction:** Q 12 > all other surahs on `frac_narrative_verses` (LOCKED).

## 2. Operational definition

**Narrative-marker set** (Arabic, no-tashkeel, word-boundary regex):
- Speech reporters: قال، قالت، قالوا، قلنا، قل
- Sequence connectives: فلما، ولما، إذ، إذا، ثم، بينما
- Existence/state: كان، وكان
- Motion/event verbs: جاء، جاءت، جاءوا، ذهب، ذهبوا، أتى، أتوا
- Visual narrative: رأى، رأيت، رأوا
- Sending/dispatching: أرسل، بعث

**Per-surah metrics**:
1. `frac_narrative_verses` = (verses containing ≥1 marker) / (total verses)
2. `marker_density_per_word` = (total marker tokens) / (total words)
3. `narrative_purity_score` = 0.5 · frac_narrative_verses + 0.5 · (marker_density / 0.30)

## 3. Test statistic

**Primary**: Q 12's rank on `frac_narrative_verses` (1 = highest).
**Secondary**: Q 12's rank on `marker_density_per_word`.
**Composite**: rank on `narrative_purity_score`.

## 4. Success / Failure

- **Strict success (CONFIRMED)**: Q 12 ranks 1/114 on `frac_narrative_verses`.
- **Directional**: Q 12 in top 5/114 on the composite score.
- **NULL**: Q 12 ≥ rank 57.
- **Pre-commit violation**: Q 12 strongly *low* (< rank 90) on the primary.

## 5. Honest limits known a priori

- Tiny short surahs (Q 110, Q 113) may inflate `marker_density_per_word` by accident of small denominators. Therefore, the **primary** statistic is `frac_narrative_verses`, which is mid-magnitude robust across surah-length.
- Marker set is small and curated; does not exhaust narrative cues. This is a deliberately conservative proxy.
- "Narrative-vocabulary density" ≠ "is a narrative". Q 110 (an-Naṣr) is doxological-imperative-styled but uses "qul" + sequencing markers. The *semantic* claim that Q 12 is uniquely a continuous-narrative arc is supported by `00-overview.md` §4 directly (independent observation).

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q012_F_01_narrative_purity.py`.
