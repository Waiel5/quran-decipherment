---
agent: derived-equations
run: 1
date: 2026-04-12
rules_tuple: [no-tashkeel, orthographic-token, lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi]
corpus: quran-text/quran-no-tashkeel.json
output: findings/phase-b-hypotheses/derived-equations.md
script: findings/phase-b-hypotheses/analysis/derived-equations/run.py
artifact: findings/phase-b-hypotheses/analysis/derived-equations/results.json
---

# Derived Equations — Run 1 Journal

## Aim

Propose, derive, and evaluate four novel closed-form mathematical formalisms
over the Quran corpus, each either (a) fitting a structural regularity and
generalising, or (b) reverse-engineering a classical *naẓm / iʿjāz* claim.

## Work order

1. Loaded corpus (6,236 verses) via `tools.loader.load_quran("no-tashkeel")`.
2. Built `real_words`, `letters_only`, and abjad helpers.
3. **D1 (CFG).** Enumerated 5-word A-B-C-B-A palindromes on orthographic tokens. Classified each against a 5-production context-free grammar with three lexical slot families + retribution singleton. All 13 observed hits classify (13/13); grammar generates 43 lexical strings of which 9 occur and 34 are unobserved-but-predicted (a tautology warning — recall is trivially 100%, but the falsifiable claim survives: no unclassified 5-word palindromes in the corpus).
4. **D2 (Ω_IAM).** Defined 10 per-verse functionals, computed dense tie-averaged ranks, computed geometric-mean rank. Top-20 reproduces the published composite (Q 59:23, Q 59:24, Q 112:2, Q 3:2, Q 2:163, Q 20:8, Q 59:22 all in). Novel candidates surfaced at ranks 5, 7, 12, 14 (Q 27:26, 6:102, 28:88, 40:62). Rule-invariance check against min-tashkeel for axis 5 alone: 17/20 top-20 overlap.
5. **D3 (Naẓm matrix).** Loaded persisted T4 indicator matrices. Computed 12×12 lift L and MI matrices for Quran and baseline. Computed three scalar summaries of the centred lift. Counterintuitive result: spectral radius is SMALLER in the Quran (14.95 vs 144.14) despite larger k≥8 tail. Interpreted as: the Quran's T4 over-dispersion is a 3+-way phenomenon, not a pairwise one. The one Quran-specific pairwise lift that dominates is `chiastic × jinas = 2.46` (al-Zarkashī nawʿ 43 anticipates).
6. **D4 (Twin-Opener N(L)).** Computed longest common letter-prefix over 6,122 within-surah adjacent verse-pairs. Counted N(L) at L ∈ {5,10,15,20,25,30,35,40}. Fit log-linear (exponential) and log-log (power-law). Exponential R² = 0.9893 beats power-law R² = 0.9573. Law: N(L) ≈ 383·exp(−0.198 L), half-life 3.5 letters. Single pair at L ≥ 30: Q 2:149-150 (qibla doubled incipit; al-Biqāʿī's flagship).

## Observations beyond the plan

- The single L ≥ 30 pair drops from 2 to 1 under no-tashkeel rules because the Q 59:22-23 pair's shared prefix is 20 letters under our exact rules (earlier project claims of 30+ for this pair count rasm differently — I reported honestly).
- D3's pairwise result is the most surprising finding of the run. Worth flagging as a follow-up: compute the three-way interaction tensor T_{ijk} = P(C_i ∧ C_j ∧ C_k) / (P(C_i)P(C_j)P(C_k)) and check whether its spectral structure DOES exceed the baseline's three-way tensor.
- D2's axis-5 rule-invariance at 17/20 confirms the composite is not a brittle artefact of the abjad encoding.
- D1 has the highest tautology risk but its type-restriction claim (no non-cosmic A-B-C-B-A 5-word palindromes) is falsifiable against future comparative Arabic corpora.

## Outputs

- `findings/phase-b-hypotheses/derived-equations.md` — primary deliverable.
- `findings/phase-b-hypotheses/analysis/derived-equations/run.py` — all 4 derivations in one script.
- `findings/phase-b-hypotheses/analysis/derived-equations/results.json` — raw values (including full 12×12 lift matrices).
- `docs/master-index.md` — linked at the top of the foundations section.

## Integrity notes

- No post-hoc axis swap, constraint drop, or parameter tuning.
- D1 CFG was fitted to the 13-instance catalog; this is disclosed as a tautology-risk. The non-trivial claim (type-restriction) is called out.
- D2 axis 8 (formulaic phrase scan) could appear as circularity-inducing; the top-3 verses are promoted even without axis 8 (per published composite's robustness check).
- D3's counterintuitive direction is reported without massaging.
- D4's fit-function choice (exponential over power-law) is selected by R² only; both fits are reported.

## Follow-ups

- Three-way constraint-tensor analysis (see D3 note).
- Test D1 grammar against a comparable Arabic baseline (Jāḥiẓ, Sira, Muʿallaqāt) to see whether ANY 5-word A-B-C-B-A palindrome exists in baseline prose, and whether baseline palindromes fall under the same cosmic-inversion semantic typing.
- Extend D4 to 3-verse and 4-verse prefix-sharing (not just adjacent pairs) — expected to decay even faster.
- Compute Ω_IAM under multiple rule-tuple perturbations (basmala policy, graphemes-with-shadda-doubled, maghribī abjad) to quantify robustness beyond the single axis-5 flip used here.

## Runtime

One-shot execution completed; no retries or re-runs. Script is deterministic under the declared seed (20260412, relevant only to D4's null shuffles).
