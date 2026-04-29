---
prereg_id: Q043-F-03
title: Q 43 *al-Raḥmān* lemma-token density — top-5 corpus-wide
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T19:15:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-03 — Q 43 *Raḥmān* lemma density

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Q 43 ranks **in the top-5** of all 114 surahs by *al-Raḥmān*-lemma density (per 1000 orthographic tokens, no-tashkeel). The classical exegetical observation (al-Ṭabarī, al-Rāzī, Ibn Kathīr) that Q 43 is *Raḥmān*-saturated is therefore empirically anchored.

## 2. Null

**H0**: Q 43's *al-Raḥmān* density is below top-5; or below the corpus median.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (project default).
- Source: `quran-text/quran-no-tashkeel.json`.
- Lemma identification: substring match for `رحمن` within whitespace-separated orthographic tokens. This catches: الرحمن, للرحمن, بالرحمن, الرحمنِ etc. — all morphological variants of the al-Raḥmān divine name (the Quranic *al-Raḥmān* lemma surface form).
- Per-surah density: count_lemma / total_tokens × 1000.
- Test: rank Q 43 in the descending density list across 114 surahs.

## 4. Direction lock

Pre-committed direction: **Q 43 rank ≤ 5** (top-5).

If observed direction reversed (Q 43 rank > 50, i.e., below median): **NULL with pre-commit violation flag**.

## 5. Bonferroni

Member of the Q 43 novel-findings family (k=4). Bonferroni-corrected α = 0.05/4 = 0.0125. Per-test interpretation below uses gap-magnitude (the rank-claim is exact, not parametric).

## 6. Success / failure criteria

- **VINDICATED**: Q 43 rank ∈ {1..5} corpus-wide.
- **DIRECTIONAL**: Q 43 rank ∈ {6..10}.
- **NULL**: Q 43 rank > 10.
- **PRE-COMMIT VIOLATION**: Q 43 rank > 50.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q043-F-03.json` with: Q 43 count, Q 43 tokens, Q 43 density, Q 43 rank, top-15 surahs, classical-context note.

## 9. Rationale

Q 43 uses the divine name *al-Raḥmān* heavily — the existing 02-content-analysis flagged 7 surface tokens. al-Ṭabarī ad Q 43:33 (citing the wealth-restraint passage where *al-Raḥmān* is the addressee-name) and al-Rāzī ad Q 43:36 (the *qarīn*-assignment for those who turn from *al-Raḥmān*) treat the *Raḥmān*-saturation as a thematic marker. This pre-reg formalizes the density-claim.

## 10. Honest limits

- Substring-matching `رحمن` will also catch any non-al-Raḥmān forms with the same letter sequence (extremely rare in the Quran corpus; the substring is essentially unique to the divine name).
- The lemma-density operationalization differs from the QAC-root operationalization (QAC root rḥm includes *raḥma*, *raḥīm*, *raḥmān*); using lemma-substring isolates the *al-Raḥmān* divine-name specifically — the pre-committed operationalization for this test.
- Q 1 has very high density due to its tiny token count (29 tokens, 2 *al-Raḥmān* attestations) — the corpus-wide rank is sensitive to short-surah artifacts. The pre-commit accepts the corpus-wide rank as-is.
