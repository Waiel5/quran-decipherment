# cross-finding-010 — run 1 journal

**Agent**: cross-finding-010-specialist  
**Date**: 2026-04-17  
**Parent**: NM-21 (HANDOFF/03-NEXT-MOVES.md)  
**Seed**: 20260417  
**N_perm**: 10,000

## Orientation

Read in order:
1. `HANDOFF/01-WHAT-WE-KNOW.md`
2. `HANDOFF/02-META-ARCHITECTURE.md`
3. `HANDOFF/04-DISCIPLINE.md`
4. `HANDOFF/03-NEXT-MOVES.md` §NM-21
5. `findings/phase-b-hypotheses/h-new-89-meta-cluster-network.md`
6. `findings/phase-b-hypotheses/csv/h-new-89.json`
7. `findings/phase-b-hypotheses/h-new-89-meta-cluster-network-prereg.md`

## Task

Extend H-NEW-89's 11-cluster meta-network to 20+ systems.
Compute (A) updated degree distribution, (B) updated isolate
count under extended clusters, (C) new-cluster-only independence
test. Seed 20260417, Bonferroni k=3, α_bon=0.0167.

## Steps taken

1. Read all orientation files.
2. Read H-NEW-89 finding + pre-reg + JSON + script.
3. Read H-NEW-85 oath-opener (locked 21-surah set).
4. Read H-NEW-74 qul-distribution (Cell 3 locked 5-surah
   qul-pentalogy).
5. Read H-NEW-83 refrain-density (Q 55 + Q 77).
6. Read H-NEW-53 book-reference muqaṭṭāʿat subset (24/29).
7. Verified surah name list in `quran-text/quran-no-tashkeel.json`
   for divine-attribute and prophet-named enumerations.
8. Wrote pre-reg `findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md`
   with 20-cluster lock and three analytical cells locked.
9. Wrote script `scripts/cross_finding_010_extended_network.py`
   including MW-5 positive control + 3 product cells.
10. Executed script (single run, no iteration on results).
11. Wrote findings `findings/phase-b-hypotheses/cross-finding-010-extended-network.md`
12. Wrote this journal.

## Key decisions logged in pre-reg

1. **20 clusters locked** before any run (11 original + 9 new).
2. **Prophet-named at n=7** (not 8): strict reading — surah title
   must be a prophet's personal name. Excludes Q 3 Āl ʿImrān
   (family) and Q 21 al-Anbiyāʾ (category).
3. **Divine-attribute-named at n=5**: {24, 35, 40, 55, 112}.
   Excludes Q 17 al-Isrāʾ and Q 97 al-Qadr (named for divine
   acts, not for the divine person).
4. **C18 musabbiḥāt-7 ADDED alongside C5 musabbiḥāt-inner-5**
   (not replacing). Nested relationship C5 ⊂ C18 is a deliberate
   methodological choice declared in pre-reg.
5. **C19 book-reference-muqaṭṭāʿat-subset** heavily overlaps
   C1-C4 + C17. Declared and accepted.
6. **C20 invocation/refuge** removes Q 1 from isolate list by
   construction. Declared and accepted.
7. **Membership-permuted null** (same as H-NEW-89).
8. **Seed 20260417** for extended run; seed 20260417+1000 for
   MW-5 control; seed 20260417+2000 for cell C null. Separated
   to avoid correlation.

## Expected priors (disclosed before run)

- Q 62 predicted new degree 5-6 via C18 and possibly C19.
- Q 2, Q 3 predicted degree 4 via C19.
- Q 1 predicted to exit isolate set via C20.
- Isolate count predicted to drop from 21 to ~15-18.

## Actual results (post-run)

Priors matched well:
- Q 62: **degree 5** (gained C18 musabbiḥāt-7 only; not C19)
- Q 2, Q 3: **degree 4** (gained C19 as predicted)
- Q 1: **EXITED** isolate set via C20
- Isolate count: **10** (more dramatic drop than predicted)

Surprises:
- Q 112, 113, 114 all emerged at degree 4 — predicted degree-2
  or-3 only
- Q 50 emerged at degree 4 — predicted degree-3
- Q 16-25 zone compressed to 5 true isolates (not predicted)
- Cell C NULL was expected possible but conclusive (p = 1.0)

## Verdicts

- **MW-5**: PASS
- **Cell A**: SHIFT — 7 new degree-4 co-hubs emerge
- **Cell B**: DROP — 21 → 10 isolates
- **Cell C**: NULL — new-only sub-network does not recover Q 62

## Deliverables

- `findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md`
- `scripts/cross_finding_010_extended_network.py`
- `findings/phase-b-hypotheses/csv/cross-finding-010.json` (includes
  full incidence matrix, all top-15 hubs, MW-5 control results,
  permutation-null distributions)
- `findings/phase-b-hypotheses/cross-finding-010-extended-network.md`
- `journal/cross-finding-010-run-1.md`

## Compliance

- PRE-REG-STANDARD-04: YAML frontmatter contains `bonferroni_k: 3`,
  `bonferroni_family`, `alpha_bon: 0.0167` ✓
- MW-5: re-ran H-NEW-89's 11-cluster pipeline and recovered
  Q 62 = 4-hub, 21 isolates, p_iso = 0.0001 exactly ✓
- Honesty: Cell C NULL published with same prominence as the
  Cell A hub-shift and Cell B isolate-drop ✓
- Seed 20260417: used ✓
- Anti-HARK: 20 clusters locked before run; no post-hoc cluster
  additions/removals; all hubs and isolates reported in full ✓
- Single-text principle: one canonical corpus (114 surahs,
  6,236 verses); no "editions" framing ✓

## Honest caveats also noted in findings

1. Cluster overlap between C19 (book-ref muq subset) and C1-C4,
   C17 is heavy and intentional — inflates muqaṭṭāʿat degrees.
2. Cell C null is the most structurally important finding —
   Q 62 hub is ANCHORED to original H-NEW-89 cluster lock.
3. Q 36/38/50 triplet emerging in new-only top-3 is a
   candidate H-NEW-111 classical sub-cluster investigation.
4. Q 112-114 back-terminal hub-triplet is a candidate
   H-NEW-112 investigation.
5. {Q 16, 21, 22, 23, 25} true-isolate core is a candidate
   H-NEW-113 / cross-finding-013 investigation.

## End state

All 5 deliverables written, script completed in 0.7s. No HARK
issues, no specification deviations, MW-5 positive control
passed.
