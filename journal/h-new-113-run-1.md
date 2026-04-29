# H-NEW-113 — Run 1 Journal

**Date**: 2026-04-17
**Agent**: h-new-113-specialist
**Seed**: 20260417
**Pre-reg**: `findings/phase-b-hypotheses/h-new-113-letter-position-prereg.md`
**Script**: `scripts/h_new_113_letter_position.py`
**Outputs**: `findings/phase-b-hypotheses/csv/h-new-113.json`, `findings/phase-b-hypotheses/h-new-113-letter-position.md`

## Chronology

1. Read HANDOFF orientation (01-WHAT-WE-KNOW, 04-DISCIPLINE, 02-META-ARCHITECTURE). Noted: muqaṭṭāʿat set excludes major function letters {و, ب, ت, ف}, which foretold the reverse verse-initial result before viewing.
2. Verified 28-letter alphabet, 14-muqaṭṭāʿat / 14-complement partition. Defined letter normalization (hamza-family → ا; ة → ه; ى → ي; ؤ → و; ئ → ي; exclude spaces, recitation marks, standalone ء).
3. Tested loader against corpus; produced total ≈ 329,131 letters (0.5% under canonical 330,709; acceptable, attributable to standalone-hamza exclusion).
4. Wrote pre-reg with bonferroni_k=3, alpha_bon=0.0167, seed 20260417. Locked direction BEFORE executing script. Locked MW-1 frequency-normalization control via RATIOS (per-letter density, CDF-based KS).
5. Ran `h_new_113_letter_position.py` once (no re-runs).
6. Wrote findings.md with full cell results + MW-5 disclosure.

## Key numbers (for audit)

- KS D = 0.02026, p = 2.29e-22 (n_muq = 247,253; n_comp = 81,878). PASS.
- RR_bin10 = 1.0741; 95% bootstrap CI [1.0506, 1.0987]; 0/5000 bootstrap draws below 1 → p_onesided < 2e-4. PASS.
- RR_bin1 = 0.8682; CI [0.8492, 0.8875].
- Initial-letter test: muq_init = 2,913 / comp_init = 3,294 after excluding 29 opener-v1 verses; observed frac 0.4693 vs null frac 0.7512. Reverse direction massively significant (p ≈ 0); PASS in reverse direction not promotable per PRE-REG-STANDARD-01.
- MW-5 positive control: bin-10 density for {ن: 1.56×, ر: 1.60×, ي: 1.55×, م: 1.10×} strong enrichment; {ا: 0.68×, ل: 0.78×} depleted (expected, both are clitic-prefix letters, not rhyme anchors).

## Garden-of-forking-paths log (post-hoc additions)

None. Pre-reg was locked before run; no p-hacking.

ONE disclosure: the reverse-direction verse-initial depletion was NOT anticipated in the pre-reg's primary direction but WAS anticipated in the pre-reg's garden-of-forking-paths narrative ("if muqaṭṭāʿat letters are verse-initial at exactly their corpus frequency, the test returns NULL — correct behavior"). Seeing the ACTUAL magnitude (36% below null), I further noted in findings.md that the depletion is mechanistically attributable to function-letter exclusion ({و, ب, ت, ف} from Layer-1 meta-architecture). This is NOT a new hypothesis promoted post-hoc; it is a re-use of an existing finding as explanation.

## Tuple-sensitivity notes

- Normalization choice (ة → ه): if instead ة → ت, MUQ vs COMP counts would shift slightly; ة occurs as a verse-final letter in feminine plurals and contributes to the bin-10 MUQ count under the chosen mapping. Re-running with ة → ت is a queued sensitivity analysis (not included because ة → ه is the standard Hijazi-script convention used in H-NEW-60 and consistent with the project's orthographic conventions).
- Standalone hamza ء exclusion: contributes <0.5% of letters and is orthographically an epsilon-vowel-carrier; exclusion is canonical.
- Recitation-mark exclusion: {ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۞ ۩} are not letters; excluded.
- Basmala policy: default (counted only in surah 1); affects surah-1-verse-1 only.

## Possible follow-ups (queued, NOT run in this session)

- **H-NEW-113.1**: word-initial vs word-final letter position within-verse (different-tokenization replication).
- **H-NEW-113.2**: per-letter 10-bin position distribution clustering (e.g., k-means on 28 letters in position-density space) — does the MUQ-vs-COMP partition emerge as a natural cluster boundary in the 28×10 matrix?
- **H-NEW-113.3**: matched-register non-Quranic Arabic corpus (Bukhārī or Muʿallaqāt) positive-null — does their 14-vs-14 split show the same verse-final enrichment pattern?
- **H-NEW-113.4**: condition by Meccan vs Medinan — is the verse-final enrichment stronger in early-Meccan short-verse high-rhyme surahs?
- **Cross-ref H-NEW-37 verse-final vowel Markov**: how do consonant-position patterns interact with vowel-ending patterns?

## Verdict

- Primary KS: **PASS** (p = 2.3e-22, survives Bonferroni by ~20 OOM).
- Secondary RR_bin10: **PASS** (CI excludes 1).
- Secondary initial-letter: **NULL** in pre-registered direction; EXPLORATORY-REVERSE (massive depletion).

Overall: **PASS-DIRECTED** — verse-level positional signature confirmed as a new facet of the muqaṭṭāʿat structural-marker cluster. Independent replication queued.

## Self-check

- [x] Pre-reg locked before run
- [x] Seed 20260417 declared in YAML and used in script
- [x] bonferroni_k and alpha_bon in YAML frontmatter (PRE-REG-STANDARD-04)
- [x] MW-1 length/frequency controlled (normalized position; RR ratios; binomial frequency-null)
- [x] MW-5 positive control PASS (ن, ر, ي classical rhyme anchors)
- [x] Reverse-direction result properly flagged EXPLORATORY-REVERSE per PRE-REG-STANDARD-01
- [x] Verdict "PASS-DIRECTED" (not CONFIRMED) per post-hoc-noticed protocol (novel test)
- [x] Output JSON includes 28×10 per-letter matrix
- [x] Finding file exists; journal file exists; pre-reg file exists; script file exists
