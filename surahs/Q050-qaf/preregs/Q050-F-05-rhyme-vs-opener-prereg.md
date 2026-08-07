---
finding_id: Q050-F-05
title: "Q 50 verse-final-letter (rāwī) profile vs Q 38 / Q 68 — and the muqaṭṭaʿ-letter ⊥ rāwī orthogonality"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q050-F-05-rhyme-vs-opener
alpha_raw: 0.05
alpha_bon: 0.0167
direction: "NULL — the singleton-letter cohort's verse-final letter (rāwī) is NOT predicted by its muqaṭṭaʿ-opener letter. Specifically: Q 50 (opener=ق) does NOT have ق as its dominant rāwī (predicted: د); Q 38 (opener=ص) does NOT have ص as its dominant rāwī (predicted: ب); Q 68 (opener=ن) DOES have ن as its dominant rāwī (predicted: ن). This produces 1/3 = 33% match rate, vs random expected ~1/28 = 3.6%."
rules_tuple: "(min-tashkeel for rhyme analysis, last-grapheme of last word per verse after mushaf-mark stripping, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)"
---

# Q050-F-05 — Singleton-letter rāwī orthogonality test


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

## Hypothesis (LOCKED)

The 3-surah singleton-letter cohort opens with letters {ق, ص, ن}. Their dominant verse-final letters (rāwī) are:
- Q 50 → د (per H-NEW-700 rhyme_letter_diagnostics, 60% د)
- Q 38 → ب (per H-NEW-700, 39.8% ب)
- Q 68 → ن (per H-NEW-700, 80.8% ن)

The pre-registered direction is **NULL on opener-rāwī alignment**:
- For 1 of the 3 surahs (Q 68) the opener letter MATCHES the dominant rāwī.
- For 2 of the 3 (Q 50, Q 38) it DOES NOT.

The pre-committed test is whether a 1/3 hit rate exceeds random-pair-of-letters chance more than expected.

## Operationalization

For each singleton-letter surah X ∈ {50, 38, 68}:
1. Compute X's dominant verse-final letter rāwī(X) from min-tashkeel text (last grapheme of last word per verse after stripping mushaf marks).
2. Compute X's muqaṭṭaʿ-opener letter L(X).
3. Test 1: Is rāwī(X) == L(X)? (binary)

For the 3-surah cohort:
- empirical match-rate = (number of matches) / 3.

For the random null:
- For N=10000 iterations, sample a random "(opener letter, dominant rāwī of random surah)" pairing from the 28-letter alphabet (uniform) and the corpus's actual dominant-rāwī distribution.
- match-rate-null = simulated probability of a 3-iid-trial match-count.

## Direction (LOCKED)

NULL on individual surahs Q 50 and Q 38 (predicted no match); POSITIVE on Q 68 (predicted match). At the cohort level: 1/3 hit rate is consistent with INDEPENDENCE (opener letter is not constrained to match rāwī).

## Bonferroni

3 sub-tests in family. α_bon = 0.05/3 = 0.0167.

## Rules-tuple (LOCKED)

`(min-tashkeel for rhyme analysis, last-grapheme of last word per verse after mushaf-mark stripping, basmala-not-counted-in-Q50/Q38/Q68, Hafs-Kufan, mushaf-order)`

Source for verse-final letter: `quran-text/quran-no-tashkeel.json` (project default) — verified consistent with H-NEW-700's rhyme_letter_diagnostics output.

## Success criteria

| Per-surah outcome | Match? | Verdict |
|:--|:--|:--|
| Q 50: rāwī = د, opener = ق | NO | Q-50 NULL on opener-rāwī alignment (CONFIRMED-NULL) |
| Q 38: rāwī = ب, opener = ص | NO | Q-38 NULL on opener-rāwī alignment (CONFIRMED-NULL) |
| Q 68: rāwī = ن, opener = ن | YES | Q-68 MATCH (CONFIRMED-MATCH) |

Cohort-level: 1/3 match.

| Null comparison | Verdict |
|:--|:--|
| Cohort match-rate ≤ corpus-null 95th percentile | **NULL on cohort opener-rāwī alignment** (confirms muqaṭṭaʿ-letter ⊥ rāwī orthogonality at singleton-letter scale) |
| Cohort match-rate exceeds 95th percentile | DIRECTIONAL |

## Failure criteria

If Q 68's match is the ONLY match AND the cohort-level rate ≤ 95% null → CONFIRMED-NULL on the joint claim. This is the predicted result.

## Honest priors

- H-NEW-130 confirmed muqaṭṭaʿāt-letter hub-architecture at the LETTER level (not at content-axis).
- The dual-iʿjāz typology orthogonality finding (H-NEW-700 / H-NEW-840) treats letter-axis and rhyme-axis as separate.
- This pre-reg INSTANTIATES the orthogonality at the singleton-letter cohort. It is a predicted NULL — and this makes the pre-reg's success metric "null vindicates orthogonality" (per INVESTIGATION-PROTOCOL §1.3, NULL with full prominence).

## Output files

- Pre-reg: this file.
- Script: `scripts/Q050_F_05_rhyme_vs_opener.py`.
- JSON: `csv/Q050-F-05.json`.
- Findings: `06-novel-findings.md` §Q050-F-05.
