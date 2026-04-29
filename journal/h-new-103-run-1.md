# H-NEW-103 — Musabbiḥāt 4-form sub-typology — Run 1 Journal

**Date**: 2026-04-17
**Agent**: h-new-103-specialist
**Seed**: 20260417
**Status**: COMPLETE — PASS-DIRECTED on primary; MW-5 PASS

## Timeline

1. **Read orientation** — HANDOFF/01-WHAT-WE-KNOW, /04-DISCIPLINE, /03-NEXT-MOVES (NM-13).
2. **Read prior** — `findings/phase-b-hypotheses/h-new-58c-musabbihat-tense-split.md`: confirmed 5-surah cluster structure, perfect/imperfect binary, within-tense 24-56 char prefixes, cross-tense exactly 0. That finding is PASS-DIRECTED (post-hoc, p=0.0001 single-test).
3. **Inspected v1 of all 7 musabbiḥāt** in min-tashkeel to ratify the classical 4-form canon:
   - Q 17: سُبحٰنَ الَّذى أَسرىٰ (NOUN / maṣdar — subḥāna)
   - Q 57, 59, 61: سَبَّحَ لِلَّهِ (PERFECT — sabbaḥa)
   - Q 62, 64: يُسَبِّحُ لِلَّهِ (IMPERFECT — yusabbiḥu)
   - Q 87: سَبِّحِ اسمَ رَبِّكَ (IMPERATIVE — sabbiḥ)
4. **Wrote pre-reg** with Bonferroni k=4 in YAML frontmatter per PRE-REG-STANDARD-04; direction locked; MW-5 declared; garden-of-forking-paths disclosed H-NEW-58c prior explicitly.
5. **Wrote script** `scripts/h_new_103_musabbihat_4form.py`:
   - Loads no-tashkeel (for similarity), min-tashkeel (for form verification).
   - Loads QAC 0.4 morphology for root-Jaccard.
   - Loads revelation-order.csv for period/Nöldeke.
   - 3 pair metrics: char-prefix, root-Jaccard, verse-length sim.
   - Null: permute form-label multiset {NOUN:1, PERFECT:3, IMPERFECT:2, IMPERATIVE:1} over 7 surahs.
6. **Ran** → results:
   - Cell A: form ratification exact.
   - Cell B: Δ_char_prefix = +33.59, p = **0.0049** (α_Bon = 0.0125) → **PASS**. MW-5 PASS (within=35.0, cross=1.4).
   - Cell C: finite-verb forms 5/5 Medinan; non-finite 2/2 Meccan (exploratory).
   - Cell D: Friday-function is Q 62 + Q 87 (imperfect + imperative), NOT form-bound → NEGATIVE functional correlate.
7. **Wrote findings file** and JSON.

## Key numbers

- n_within_pairs = 4 (3 perfect-perfect + 1 imperfect-imperfect)
- n_cross_pairs = 17
- within-form char-prefix mean = 35.00
- cross-form char-prefix mean = 1.41
- Δ = +33.59, permutation p = 0.0049 (10K perms, seed 20260417)
- root_jaccard Δ = +0.081, p = 0.0383 (trending, not at α_Bon)
- verse_len_sim Δ = +0.25, p = 0.0853 (not at α_Bon)
- MW-5 within-CP = 35.00 (≥10 required) — PASS
- MW-5 cross-CP = 1.41 (≤5 required) — PASS

## Surprises / anomalies

1. **Q 17 shares 3 chars with all 3 perfect-form surahs** ("سبح" — the root radicals match, then NOUN diverges at ان vs َ). This slightly raises the cross-form mean but does not threaten the PASS.
2. **Q 87 shares 4 chars with all 3 perfect-form surahs** ("سبح " — three radicals + space). Same story.
3. **Q 17 shares 0 chars with Q 62/Q 64** (imperfect). The "يسبح" y-prefix kills the match immediately. Consistent with "subḥāna" and "yusabbiḥu" having NO common leading morpheme.
4. **Q 59-61 char-prefix = 55** here vs 56 in H-NEW-58c. 1-char diff is whitespace-stripping protocol. Null design unchanged.
5. **Cell C "finite=Medinan, non-finite=Meccan" partition** is a structural observation I did not expect going in. All 5 FINITE verb musabbiḥāt are Medinan; both non-finite are Meccan. n=7 precludes a strong test but it's a striking 2×2 partition with Fisher two-sided ≈ 0.048. Flagged as exploratory.
6. **Cell D NULL**: Q 62 is the Friday surah; Q 64 isn't. Q 87 is ALSO Friday-liturgical. Friday-function does NOT align with the perfect/imperfect split. This is honest counter-evidence to a "imperfect = ongoing/liturgical" narrative — the imperfect form is NOT a liturgical marker.

## Discipline checks

- [x] Pre-reg BEFORE run.
- [x] Bonferroni declared in YAML (k=4, α_bon=0.0125, family h-new-103-musabbihat-4form).
- [x] Direction locked pre-run (within > cross).
- [x] Seed fixed (20260417).
- [x] MW-5 positive control declared + passed.
- [x] Garden-of-forking-paths disclosed H-NEW-58c prior.
- [x] PASS and NULL published equally (cell D NEGATIVE published at same prominence).
- [x] Verdict = PASS-DIRECTED (not CONFIRMED) — acknowledges post-hoc lineage from H-NEW-58c.

## Outputs

- `findings/phase-b-hypotheses/h-new-103-musabbihat-4form-prereg.md`
- `scripts/h_new_103_musabbihat_4form.py`
- `findings/phase-b-hypotheses/csv/h-new-103.json`
- `findings/phase-b-hypotheses/h-new-103-musabbihat-4form.md`
- `journal/h-new-103-run-1.md` (this file)

## Candidate follow-ups

1. Independent replication on a different axis — divine-name density per form, or rhyme-class per form, or semantic embedding similarity — to promote PASS-DIRECTED → CONFIRMED.
2. "Finite-Medinan / non-finite-Meccan" cross-tab is striking; could test at larger family of tasbīḥ-invocations across corpus.
3. Cross-reference with H-NEW-89 meta-cluster: does "form" belong as a 12th cluster system?
