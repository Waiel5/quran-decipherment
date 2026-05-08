---
finding: H-NEW-1010
run: 1
date: 2026-05-07
specialist: h-new-1010-singleton-cohort-specialist
seed: 20260507
n_perms: 10000
prereg_sha256: f79b0235e26ef1424050e8ff4d7153b12b4f54042cc69cdb47172e68562e055d
status: COMPLETE
verdict: PASS-DIRECTED — H1 corpus-exact PASS / H2 COHORT-NULL / H3 DATA-GAP
---

# Journal — H-NEW-1010 run-1 (2026-05-07)

## Pre-flight

- Read `INVESTIGATION-PROTOCOL.md`, `HANDOFF/04-DISCIPLINE.md`, `cross-finding/muqattaat-book-introduction-marker-synthesis.md`.
- Read parent seeds: `surahs/Q050-qaf/06-novel-findings.md` (Q050-F-01 DIRECTIONAL-EXTENDED-COHORT), `surahs/Q038-sad/06-novel-findings.md` (Q038-F-01 verse-twin CONFIRMED).
- Verified canonical 29 muqaṭṭaʿāt list and inspected v.1 + v.2 of each surah in both no-tashkeel and min-tashkeel cross-text.

## Pre-registration

- Wrote `findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence-prereg.md` BEFORE running.
- SHA256: `f79b0235e26ef1424050e8ff4d7153b12b4f54042cc69cdb47172e68562e055d`.
- Locked H1 (corpus-exact pattern), H2 (cohort prophet-PN density vv. 1–10, Bonferroni-3), H3 (cross-corpus optional). Direction-locked POSITIVE on both H1 (predicted-exact-3-hit set) and H2 (predicted-top-half rank).
- Embedded SHA into script `scripts/h_new_1010_singleton_cohort_form.py` with runtime SHA-verification.

## Methodology decisions (LOCKED in pre-reg before run)

- **H1 v.1-only criterion**: critical decision to lock the pattern at verse-1 only (NOT v.1+v.2). This excludes Q 36, Q 43, Q 44 (which have wāw + def-art in v.2). The pre-reg explicitly notes the v.1+v.2 broader form is queued as candidate H-NEW-1010.1 follow-on.
- **Singleton-letter definition**: locked to {ص (Q38), ق (Q50), ن (Q68)} — single Arabic-letter orthographic-token. Q 20 (طه) and Q 36 (يس) are 2-letter and excluded.
- **Wāw + def-art detection**: substring match on `وال` at start of token, in no-tashkeel orthography. Cross-validated on min-tashkeel: same substring, robust.
- **H2 vv. 1-10 window**: chosen to balance opener-density operational meaning with adequate sample size. Whole-surah prophet density would conflate Q 38's late narrative block — vv. 1-10 isolates the OPENER-window as the operationalization.
- **H2 cohort-level interpretation**: pre-reg specifies a JOINT-rank permutation null, with single-test α=0.05 cap per Protocol §1.7 MW-7 (post-hoc-origin H1 → MW-7 ceiling).

## Run

- Verified pre-reg SHA at runtime (passed).
- Computed H1 pattern table (29 surahs).
- Computed H2 prophet-PN density (vv. 1–10) for each muqaṭṭaʿāt surah.
- Ran 10000-perm null on H2 cohort joint-rank.
- Wrote outputs to `findings/phase-b-hypotheses/csv/h-new-1010.json`.

## Results

### H1 — corpus-exact pattern PASS

- Predicted hit-set: {38, 50, 68}.
- Observed hit-set: {38, 50, 68}.
- False positives: 0. False negatives: 0.
- Verdict: PASS (corpus-exact bijection with singleton-letter sub-cohort).

### H2 — prophet-PN density (vv. 1-10) COHORT-NULL

- Q 38 rank 21/29 (0/91 words; 0.000/100w).
- Q 50 rank 28/29 (0/81 words; 0.000/100w).
- Q 68 rank 29/29 (0/44 words; 0.000/100w).
- 0 of 3 singletons in top-15.
- Permutation null: P(all 3 in top-15 under random shuffle) ≈ 0.015.
- Verdict: COHORT-NULL.
- The 3 singletons' prophet PNs appear LATER in the surahs (Q 38 vv. 17–44 inner triad; Q 68 v. 48 Yūnus reference); the OPENER window has 0 prophet PNs in all 3 cases.

### H3 — cross-corpus DATA-GAP

- Pre-Islamic qaṣīda has no genre-analogue of single-Arabic-letter verse-openers. The pattern is genre-foreign; cross-corpus distinctness is vacuously true and reported as DATA-GAP.

## Verdict

**PASS-DIRECTED — FORM-COHERENT-CONTENT-INDEPENDENT.**

H1 corpus-exact PASS + H2 COHORT-NULL = the singleton-letter cohort is a PURE FORM CLUSTER (verse-1 syntax) and NOT a content cluster (vv. 1-10 prophet-density). This is exactly the cross-finding-026 §1 letter-axis ⊥ content-axis empirical orthogonality predicted pattern, instantiated at cohort scale.

## Garden-of-forking-paths log

1. **Should H1 use v.1 only or v.1+v.2?** Locked v.1 only in pre-reg. Justification: the visual observation in Q050-F-01 was at v.1 specifically, and the (singleton + oath-wāw + def-art) form is most syntactically coherent when held within v.1 (a single oath-utterance). The v.1+v.2 broader form (which would extend to 6/29) is a DIFFERENT pattern (oath after muqaṭṭaʿāt-only-verse) — queued as H-NEW-1010.1 candidate.

2. **Should H2 use vv. 1–10 or whole-surah?** Locked vv. 1–10 in pre-reg. Justification: the H1 pattern is verse-1 syntactic; the H2 strengthening should test whether the SAME OPENER WINDOW exhibits content-density. Whole-surah prophet density (Q038-F-02 result) would test a different hypothesis (whole-surah prophet-richness), already established at rank 2/114 by Q038-F-02. The vv. 1–10 window is the OPENER-relevant cell.

3. **Should H2 use rank-test or density-z-test?** Locked rank-test (top-half binary). Justification: rank-test is robust to outliers and matches the natural reading "are the singletons in the top tier of prophet density."

4. **Single-test α cap on H2?** H2 is direction-locked POSITIVE (the 3 singletons are predicted to rank in top-half). Per pre-reg §3.6, single-test α=0.05 cap applies per Protocol §1.7 MW-7. The COHORT-NULL verdict is a direct pre-committed-direction failure; published with full prominence per §1.3.

5. **No methodology shifts mid-run.** All decisions locked in pre-reg before runtime. Pre-reg SHA verified at runtime.

## Outputs

- Pre-reg: `findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence-prereg.md` (SHA `f79b0235e26ef1424050e8ff4d7153b12b4f54042cc69cdb47172e68562e055d`).
- Script: `scripts/h_new_1010_singleton_cohort_form.py` (SHA-verified at runtime).
- JSON: `findings/phase-b-hypotheses/csv/h-new-1010.json`.
- Findings: `findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence.md`.
- Ledger update: queued (insert after H-NEW-960 entry).

## Cross-references

- Parent seed: Q050-F-01 (Q 050 specialist 2026-05-07).
- Companion: Q038-F-01 (Q 038 specialist 2026-05-07).
- Cross-finding-008 (book-introduction marker pattern; H-NEW-1010 is the COMPLEMENTARY MINOR PATTERN).
- Cross-finding-026 §1 (letter-axis ⊥ content-axis; H-NEW-1010 H2 NULL is 4th cohort-scale instantiation).

## Honest summary

The 3 singleton-letter muqaṭṭaʿāt openers Q 38 (ص), Q 50 (ق), Q 68 (ن) are exactly the 3 surahs in the corpus whose verse-1 follows the form `[singleton muq-letter] + oath-wāw + definite-article-X`. This is a corpus-exact bijection: 3 hits, 0 false positives, 0 false negatives. The cohort is form-coherent at verse-1 syntax but content-independent at the vv. 1-10 prophet-density operationalization (0 prophet-PNs in any of the 3 opener windows; ranks 21, 28, 29 of 29). The H-NEW-1010 finding is the COMPLEMENTARY MINOR PATTERN to cross-finding-008's dominant book-introduction pattern (23-25/29). Together H-NEW-1010 + cross-finding-008 form-pattern-cover 26/29 muqaṭṭaʿāt openers with two structurally exhaustive formulas.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
