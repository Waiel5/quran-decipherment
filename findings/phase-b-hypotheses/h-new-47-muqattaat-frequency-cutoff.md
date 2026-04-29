---
id: H-NEW-47
title: Muqaṭṭaʿāt vs Top-14-by-Frequency Sharp Cutoff Test
phase: B
status: NULL on sharp-cutoff hypothesis (10/14 overlap, not 14/14); REVEALS systematic exclusion of high-frequency function-letters
date: 2026-04-16
agent: integrator (main session); follows up on H-NEW-44 secondary ρ=−0.54 finding
script: inline (Python; ~30 lines)
data: quran-text/quran-no-tashkeel.json
rules_tuple: (no-tashkeel, graphemes, alef-variants normalized to bare alif)
---

# [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]] — Muqaṭṭaʿāt Sharp-Cutoff Test (RESULT)

## Question

[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary established Spearman ρ = −0.54 between "is-muqaṭṭaʿa-letter" indicator and Quran-frequency-rank. This is a CORRELATION measure. The natural sharp-cutoff hypothesis: are the 14 muqaṭṭaʿāt letters EXACTLY the top-14 by Quran-frequency?

## Result

**NULL on sharp-cutoff.** The 14 muqaṭṭaʿāt set has only **10 of 14 top-frequency letters** (71.4% overlap, not 100%).

| Rank | Letter | Count | In muqaṭṭaʿāt? |
|---|---|---|---|
| 1 | ا | 59,280 | **YES** |
| 2 | ل | 38,191 | **YES** |
| 3 | ن | 27,270 | **YES** |
| 4 | م | 26,735 | **YES** |
| 5 | و | 24,813 | **NO** |
| 6 | ي | 21,973 | **YES** |
| 7 | ه | 14,850 | **YES** |
| 8 | ر | 12,403 | **YES** |
| 9 | ب | 11,491 | **NO** |
| 10 | ت | 10,520 | **NO** |
| 11 | ك | 10,497 | **YES** |
| 12 | ع | 9,405 | **YES** |
| 13 | ف | 8,747 | **NO** |
| 14 | ق | 7,034 | **YES** |
| 15 | س | 6,012 | **YES** (rank 15) |
| 16 | د | 5,991 | NO |
| 17 | ذ | 4,932 | NO |
| 18 | ح | 4,140 | **YES** (rank 18) |

## The four high-frequency exclusions

The 4 top-14-by-frequency letters that are NOT in the muqaṭṭaʿāt set are:
- **و** (rank 5, 24,813 occurrences) — Arabic conjunction "and" / vowel /u:/
- **ب** (rank 9, 11,491) — preposition "by/in/with"
- **ت** (rank 10, 10,520) — feminine marker / verbal prefix
- **ف** (rank 13, 8,747) — conjunction "then/so"

**Pattern:** ALL FOUR are major Arabic function-letters / proclitic particles. They have extreme functional load (و alone is the most-used conjunction in any Semitic language) but minimal lexical-root role.

## The four low-frequency inclusions

Conversely, the 4 muqaṭṭaʿāt letters NOT in top-14 are:
- **س** (rank 15, 6,012) — narrowly missed top-14
- **ح** (rank 18, 4,140) — pharyngeal
- **ص** (much lower) — emphatic sibilant
- **ط** (much lower) — emphatic dental stop

**Pattern:** ح is pharyngeal (matches the [[h-new-44-2-poa-closure|H-NEW-44.2]].1 pharyngeal exhaustivity finding). ص and ط are EMPHATIC consonants — distinctively Arabic, no Indo-European parallel. س is just below the cutoff.

## Mechanism interpretation

The 14 muqaṭṭaʿāt selection appears to follow a **substantive-consonant preference rule**:
- INCLUDE: high-frequency letters that are primarily ROOT-LETTERS (ا, ل, ن, م, ي, ه, ر, ك, ع, ق) plus 4 distinctive substantive consonants (ح, س, ص, ط)
- EXCLUDE: high-frequency letters that are primarily FUNCTION-LETTERS / proclitic particles (و, ب, ت, ف)
- ALSO EXCLUDE: lower-frequency consonants (د, ذ, ج, ز, ش, ض, ظ, خ, غ, ث), plus ى (alif maqsura) and ة (ta marbuta)

This is a TESTABLE refinement of the [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary ρ=−0.54 finding. The correlation IS real and quantitatively confirms Welch (1986), but the mechanism is not "top-K by frequency" — it's "high-frequency root-letters preferred over high-frequency function-letters."

## Follow-up: H-NEW-47.1 queued

A pre-registered test of "muqaṭṭaʿāt set excludes function-letters more than chance":

- Define a "function-letter" set: {و, ف, ب, ل, ك, س, ا, ت, ن, ي} (10 letters that serve as single-letter prefix particles)
  - Note: 6 of these ARE in muqaṭṭaʿāt (ا, ل, ن, ي, ك, س); 4 are NOT (و, ب, ت, ف)
- Test: of the 14 muqaṭṭaʿāt letters, how many are function-letters?
- Conditional test: among the 4 EXCLUDED-from-muqaṭṭaʿāt-but-top-14, what fraction are function-letters? (Observed: 4/4. Hypergeometric null: drawing 4 from the 14 non-muqaṭṭaʿāt letters, what's the chance all 4 are in the function-letter set?)

The conditional test is post-hoc-noticed (this finding); needs independent pre-registration before any verdict.

## Honest caveats

- The sharp-cutoff hypothesis (top-14 = muqaṭṭaʿāt) is FALSIFIED.
- The "function-letter exclusion" mechanism is a POST-HOC narrative reading. It needs independent pre-registration to test rigorously.
- The 10/14 overlap with top-14-by-frequency is striking but trivial under the ρ=−0.54 already-confirmed correlation — drawing 14 letters with negative-correlated frequency rank would naturally overlap with top-14 about ~10/14 times.
- The 4 specific excluded letters (و, ب, ت, ف) being function-letters is the new observation; without pre-registration, this remains exploratory.

## Integrity

- Test: closed-form letter-counting on locked corpus.
- Result: deterministic; no random sampling.
- Sharp-cutoff verdict: NULL.
- Function-letter mechanism: EXPLORATORY-POST-HOC, requires H-NEW-47.1 pre-reg.
- Quranic Arabic letter-frequency table reproduced for transparency.

## Cross-reference

- [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary: ρ=−0.54 letter-frequency correlation (CONFIRMED Welch 1986)
- [[h-new-44-2-poa-closure|H-NEW-44.2]]: POA closure NULL (overall χ² perm p=0.065)
- [[h-new-44-2-poa-closure|H-NEW-44.2]].1: Pharyngeal/glottal exhaustivity (4/4) PASS-DIRECTED at α=0.05 single-test
- [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]] (this file): sharp-cutoff hypothesis NULL; function-letter-exclusion mechanism flagged for follow-up
