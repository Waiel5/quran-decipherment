# H-NEW-114 — Zero-Set / Absent-Structures Fingerprint — Run 1

**Date**: 2026-04-17
**Agent**: h-new-114-specialist
**Seed**: 20260417
**N_perm**: 10,000
**Bonferroni**: k=4, α_bon = 0.0125, family `h-new-114-zero-set`

## Dispatch

Dispatched from HANDOFF orientation. Novel inversion test: enumerate what the Quran does NOT contain at four scales (letter-bigram, letter-trigram, word-bigram, muqaṭṭāʿat-letter-presence patterns) and test whether the zero-set is characteristic vs matched Arabic baselines.

## Pre-reg flow

1. Read handoff orientation files 01, 04, 05.
2. Surveyed baseline data at `data/baseline-corpora/raw/` — found Bukhārī, Jāḥiẓ, 7 Muʿallaqāt — same baselines as H-NEW-48.
3. Wrote pre-reg `findings/phase-b-hypotheses/h-new-114-zero-set-prereg.md` with k=4 and the four cells.
4. Built script `scripts/h_new_114_zero_set.py`.
5. Dry-run at N_perm=5 validated mechanics (observed absent-counts extreme vs shuffle-null).
6. **Audit-035 flagged direction-vs-PASS-rule mismatch** mid-flight (before full-N run completed). Killed initial run, amended pre-reg to use matched-Arabic-baseline envelope as PRIMARY PASS for Cells A/B (stricter than shuffle-null) and Poisson-envelope for Cell C. Logged as TIGHTENING amendment (self-verifying per Bonferroni-asymmetry rule). Disclosed in pre-reg's §Garden-of-forking-paths point 10.
7. Rewrote script Cells A/B/C to implement matched-baseline envelope and Poisson-envelope.
8. Ran full 10K-perm analysis.

## Engineering notes

- Initial pure-Python permutations were ~12 s per 100 perms for bigram+trigram. Switched to numpy-based shuffle and base-28 integer encoding of n-grams → ~0.8–1.0 s per 100 perms (16× speedup). Final run-time ~5 min total.
- `normalize()` initially split tokens containing standalone hamza `ء` (not in ALPHABET28) into multiple sub-tokens with internal spaces — fixed by post-normalize whitespace-splitting in `load_quran_text`.
- Bukhari baseline is ~1.25× Quran length (6 length-matched windows); Jāḥiẓ is ~1.3× (4 windows). Muʿallaqāt is only ~30K letters (< 1/10 Quran) — reported descriptively only, excluded from envelope.

## Key intermediate result (logged BEFORE viewing outcome)

Shuffle-null (MW-5 diagnostic) shows absent-bigrams ~1.2 and absent-trigrams ~8,453 under letter-multiset shuffle. Natural Arabic (Quran, Bukhārī, Jāḥiẓ) shows ~115–200 absent-bigrams and ~14,157–16,209 absent-trigrams. Natural-Arabic gap structure is MUCH richer than multiset-alone can explain → confirms structural morphophonological constraint. Then the question becomes whether the Quran's gap-count DIFFERS from matched natural Arabic.

## Results at a glance

- **Cell A (bigram absent-count)**: Quran 146, envelope [114, 152], z=+0.75 → **NULL**
- **Cell B (trigram absent-count)**: Quran 15,827, envelope [14,157, 16,209], z=+0.64 → **NULL**
- **Cell C (surprising absent word-adjacencies, O=0 and E≥1)**: obs 1,469 of 2,262; Poisson μ=347.5, σ=16.1; z=+69.6; p < 10⁻¹⁵ → **PASS** (but likely Arabic-syntactic, not Quran-specific, pending baseline replication C2)
- **Cell D (muqaṭṭāʿat-presence patterns)**: 14 distinct patterns of 16,384; 93/114 surahs carry all 14; singleton-missing letters concentrate in ط/ص/ق/ح; descriptive

## Discipline checklist

- [x] Pre-reg written BEFORE execution
- [x] Direction pre-locked in pre-reg frontmatter (PRE-REG-STANDARD-01)
- [x] Bonferroni declared in YAML frontmatter (PRE-REG-STANDARD-04)
- [x] Seed locked (20260417)
- [x] Garden-of-forking-paths disclosed (novelty of test; amendment audit-035)
- [x] MW-1 length matching: Bukhārī/Jāḥiẓ truncated to Quran length (329,131 letters)
- [x] MW-5 positive control executed and passed (synthetic absent-counts match shuffle-null)
- [x] NULL results published with EQUAL PROMINENCE to PASS (Cells A/B NULL, Cell C PASS — all in findings file)
- [x] Post-hoc amendment audit-035 applied BEFORE viewing primary results and logged as TIGHTENING (self-verifying)
- [x] Cell C PASS flagged as likely Arabic-syntactic pending C2 replication; not over-claimed as Quranic iʿjāz

## Outputs

1. Pre-reg: `findings/phase-b-hypotheses/h-new-114-zero-set-prereg.md`
2. Script: `scripts/h_new_114_zero_set.py`
3. JSON: `findings/phase-b-hypotheses/csv/h-new-114.json`
4. Findings: `findings/phase-b-hypotheses/h-new-114-zero-set.md`
5. Journal: this file.

## Followups queued

- H-NEW-114.C2: Cell C replication on Bukhārī + Jāḥiẓ with each corpus's own top-100 for Quranic-distinctiveness test
- H-NEW-114.D2: formal test of singleton-missing-letter distribution against letter-frequency-weighted null
- Cross-check ط/ص/ق/ح dropout pattern against H-NEW-60 dotless preference (ط,ص,ق are all dotted; H-NEW-60 found muqaṭṭāʿat SKEW dotless — any contradiction?)
