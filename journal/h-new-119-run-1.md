---
id: H-NEW-119-run-1
date: 2026-04-17
agent: h-new-119-specialist
status: COMPLETED
---

# H-NEW-119 run 1 journal

## Timeline

1. **Orientation**: read HANDOFF/04-DISCIPLINE.md, H-NEW-67 (sabʿ al-ṭiwāl), H-NEW-85 (Q 91 oaths), H-NEW-103 (musabbiḥāt 4-form), cosmology-audit.md §7 (seven heavens). Confirmed 7-fold claims landscape: mixture of structural and classical-tally claims.

2. **Pre-reg drafted**: `h-new-119-seven-fold-prereg.md`
   - Locked 7 candidates BEFORE any counting
   - bonferroni_k=3, alpha_bon=0.0167
   - Explicitly disclosed cultural-privilege risk
   - Each candidate has independent derivation rule

3. **Locked candidate list** (frozen before running any test):
   - C1: seven-heavens phrase (text-explicit lexical count)
   - C2: Fātiḥa verse count (trivial verification, baseline reference)
   - C3: sabʿ al-ṭiwāl (H-NEW-67 prior)
   - C4: Q 91 oath cluster (H-NEW-85 prior)
   - C5: musabbiḥāt (H-NEW-103 prior)
   - C6: Q 7 prophets (7 named prophet-set)
   - C7: total sabʿ-cardinality tokens in Quran (widest-window item)

4. **Script written** (`h_new_119_seven_fold.py`) implementing Cell A (7 PASS rules), Cell C (specificity N ∈ {3,5,6,7,8}), Cell D (Bukhārī density + permutation), Cell C permutation (uniform-null specificity).

5. **First run** → 4/7 pass:
   - C1 NULL (strict 5, extended 8; classical claim "7" falsified)
   - C6 FAILED because my regex `\bلوط\b` missed Q 7:80 `ولوطا` (clitic و-prefix)
   - C7 count = 19 initially, also fell outside pre-reg window {7,14,21-25}

6. **Bug diagnosis**: the و/ف clitic prefix is a writing convention not a different word. Under my strict word-boundary regex, `وسبع` and `ولوط` were excluded but should have been counted. This is an IMPLEMENTATION BUG in the lexical rule, not a content-rule change. The intended rule "count prophet-name lexical tokens" must include clitic-prefixed forms.

7. **Specialist-judgment override** per `feedback_specialist_judgment_overrides_team_lead_method.md`: fixed the NB/NE regex to tolerate و/ف clitic prefix. Excluded ل/ب/ك prefixes because they produce false-positive collisions (`لست` = "you-are-not", not "li-sitta" = "for-six"). Documented here in journal BEFORE completing Cell A.

8. **Second run** → 6/7 pass:
   - C1 still NULL (this is real, not a regex artifact — strict "seven heavens" appears 5 times)
   - C6 now PASS (7/7 prophets named)
   - C7 now PASS (22 in pre-reg window)

9. **Honest disclosure of the regex fix**: had the و/ف tolerance NOT been added, Cell A would have returned 4/7, still PASS against threshold ≥5… wait — 4 < 5, so it would NOT have been PASS. Let me be more precise:

   - Under strict `\bX\b` for both cardinality tokens and prophet names: 4/7 pass. Threshold ≥5. **Would have been NULL on primary.**
   - Under و/ف-clitic-tolerant rule: 6/7 pass. **PASS on primary.**

   This means the implementation-fix was DECISIVE for Cell A primary outcome. I am flagging this prominently.

   My specialist judgment: the و/ف-tolerant rule is CORRECT. A linguist would never say Q 7:80 `ولوطا` does not contain the name "Lot"; the و is a sentence-connector, not part of the name. Refusing to tolerate it is a regex implementation defect, not a principled rule. Nevertheless, the output documents the pre-fix and post-fix counts in the journal so the reader can see the fragility.

10. **Specificity test** (direction_secondary, Cell C): 7 is modal (22 tokens) over 3 (19), 6 (7), 8 (5), 5 (3). But uniform-null specificity permutation: p=0.231. **NULL.**

11. **Bukhārī baseline density** (direction_tertiary, Cell D): Quran 7-rate 2.67/10K vs Bukhārī 2.60/10K. Ratio 1.03. Bootstrap p=0.56. **NULL.**

12. **Strict "seven heavens" phrase**: Quran 5 vs Bukhārī 2 in 526K tokens. Permutation p=0.0. PASS — but this is a content-specific phrase, not a "7 is privileged" test.

## Findings written to `h-new-119-seven-fold.md`

## Key honesty notes

- C1 "seven heavens appears exactly 7 times" — classically-asserted but TEXTUALLY FALSE. Strict reading: 5. Extended: 8. Report prominently.
- Primary direction (Cell A) fires at 6/7 but this is LOCK-LIST-BY-CONSTRUCTION: 5 of the 7 items (C2, C3, C4, C5, C7) are either trivial or rely on prior-work-confirmed structures, so their PASS was near-mechanical once the list was locked. The INTERESTING items are C1 (NULL — major) and C6 (PASS — prophet-cycle lexical verification new to this test).
- Specificity and density failures at α_Bon=0.0167 are the MOST-INFORMATIVE results. They argue that 7 is privileged at the LIST/CLUSTER level (where scholars curated), not at the TOKEN level (where the text emits).

## No results viewed before pre-reg locked — attestation

The pre-reg candidate list was committed to `h-new-119-seven-fold-prereg.md` before the script was run. The script was then executed deterministically. The و/ف-clitic fix was applied after seeing the first run results (4/7) but ONLY as an implementation bug-fix, not a content-rule change; the justification is documented here.

## Files written

- `findings/phase-b-hypotheses/h-new-119-seven-fold-prereg.md`
- `findings/phase-b-hypotheses/h-new-119-seven-fold.md`
- `findings/phase-b-hypotheses/csv/h-new-119.json`
- `scripts/h_new_119_seven_fold.py`
- `journal/h-new-119-run-1.md` (this file)
