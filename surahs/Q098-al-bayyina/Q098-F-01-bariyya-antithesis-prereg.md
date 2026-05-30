---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
file_type: prereg
test_id: Q098-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q098-F-01 — Pre-Registration: al-Bayyina title-density falsification + the khayr↔sharr al-bariyya minimal-pair muqābala

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q098_F_01_bariyya_antithesis.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 98 al-Bayyina ("the Clear Proof") is an 8-verse Medinan surah (Hafs-Kūfan) whose closing pericope
(vv 6-7) carries the corpus's most surface-symmetric antithesis: a verse ending
`أولئك هم شر البرية` ("those are the WORST of creation") immediately followed by a verse ending
`أولئك هم خير البرية` ("those are the BEST of creation"). The two verse-tails are identical except
for a single substituted word, a genuine lexical antonym (sharr ↔ khayr), on a rhyme-word
(al-bariyya) that the qurrāʾ and mufassirūn (al-Zamakhsharī, al-Rāzī) gloss as a derivative of the
root b-r-ʾ "to create." Four pre-registered, direction-locked arms test the surah's distinctive
structural signatures.

1. **Title-density (Arm A — FALSIFICATION-direction).** The project's H-NEW-1820 (title-density
   independence) summary-list asserted Q 98 al-Bayyina is in the "title-density-EXACT (rank-1)" set
   for its title-root. That assertion was made in a summary list and never verified per-surah on disk.
   H-NEW-1820's own corpus law is that title-eponymy and density-rank-1 are INDEPENDENT (47/89 = 52.8%
   of eponymous surahs are NOT rank-1). We DIRECTION-LOCK the prediction consistent with the H-NEW-1820
   law: **Q 98 al-Bayyina is NOT corpus-rank-1 in its title-root byn** (neither by raw root-attestation
   count nor by exact eponymous surface-form البينة). If it IS rank-1, the H-NEW-1820 summary holds and
   Arm A is a (boring) confirmation; if it is NOT rank-1, Arm A CORRECTS the H-NEW-1820 summary list and
   adds a data-point to the title-density-independence law.

2. **al-bariyya corpus-rarity (Arm B).** The rhyme-word al-bariyya (البرية) is claimed to be a
   corpus-rare lexical item. **Direction-lock: البرية occurs in exactly 2 corpus positions, both in
   Q 98 (v6, v7) — a Q 98-exclusive hapax-pair.**

3. **The minimal-pair muqābala (Arm C — the headline).** Among all corpus *adjacent* (consecutive
   same-surah) verse-pairs that are ANTITHETICAL on the faith↔disbelief field (one verse carries root
   Amn [believe], the other carries kfr/nfq/Srk [disbelieve/hypocrisy/associate] — the SHA-locked
   H-NEW-2290 / H-NEW-2360 faith-field instrument), Q 98:6-7 is hypothesized to be the corpus-UNIQUE
   pair whose verse-tails align with **exactly one substituted word** over **≥3 matched trailing
   words**, AND where that single pivot is a genuine lexical antonym. **Direction-lock: the count of
   adjacent faith-antithetical verse-pairs with (single-substitution aligned tail) ∧ (matched-tail ≥3)
   ∧ (pivot ∈ {khayr,sharr} antonym set) is exactly 1, = Q 98:6-7.**

4. **Content-disjointness vs null (Arm D — permutation).** Classical muqābala theory (and the
   Q083-F-01 "destiny-catalogue" precedent) suggests an antithesis sets two lexically DISJOINT contents
   against a shared frame. H-NEW-2360 found the OPPOSITE corpus-wide: block-scale antithetical pairs
   OVERLAP in content (jadal signature, z=+13.0 reversal). Q 98:6-7 is a verse-pair (not a W=5 block),
   and shares only one content root at the QAC-root level (brA). We test whether Q 98:6-7's
   content-root-Jaccard is BELOW (more disjoint than) a length-matched random-verse-pair null.
   **Direction-lock (classical/Q83 intuition): J(v6,v7) < null_mean (lower-tail, more disjoint).**

   *MW-7 transparency:* during close reading I observed that Q 98:6-7's root-Jaccard is near the MEDIAN
   of adjacent faith-antithetical pairs (i.e. NOT an extreme disjoint outlier). The PRECISE
   seed-locked length-matched permutation null below was NOT run before this lock. Arm D's locked
   direction (disjoint) is the classical prior; I expect it to FAIL/REVERSE, which would be a clean
   honest NULL replicating the H-NEW-2360 jadal-overlap law at verse-pair scale. Arm D is capped at
   single-test α=0.05 and is the ONLY permutation cell.

## Rules-tuple

`(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. Pause/sajda diacritic
marks stripped before tokenization. Word = whitespace-delimited orthographic token after mark-stripping.
Roots from QAC v0.4 (`data/morphology/root-index.json`, `[surah,verse,word]` attestations). Title-root
byn per al-Suyūṭī *Itqān* nawʿ-22 etymological class (al-Bayyina ← b-y-n); QAC root key `byn`.

## Arm A — title-density-EXACT (DIRECTION-LOCKED FALSIFICATION)

- **A-H1 (raw root rank):** Q 98 is NOT corpus-rank-1 in raw `byn` attestation count. Direction lock:
  rank(Q98, byn raw count) > 1.
- **A-H2 (exact title-word rank):** Q 98 is NOT corpus-rank-1 in the exact eponymous surface form
  البينة (and بينة). Direction lock: ≥1 other surah has ≥ Q 98's count of البينة/بينة.
- **Verdict:** A-H1 ∧ A-H2 hold → Arm A = title-density-EXACT FALSIFIED (Q 98 joins the 47/89
  non-rank-1 set; H-NEW-1820 summary-list entry corrected). Either fails → Arm A = title-density-EXACT
  CONFIRMED (the H-NEW-1820 summary holds for Q 98).

## Arm B — al-bariyya corpus hapax-pair (DETERMINISTIC)

- **B-H1:** surface البرية/برية occurs in exactly 2 corpus positions. Direction lock: count = 2.
- **B-H2:** both positions are in Q 98 (v6 and v7). Direction lock: positions = {(98,6),(98,7)}.
- **Verdict:** B-H1 ∧ B-H2 → Arm B CONFIRMED (Q 98-exclusive hapax-pair). Either fails → Arm B NULL.

## Arm C — the khayr↔sharr minimal-pair muqābala (DIRECTION-LOCKED, DETERMINISTIC)

Operationalization (all locked here):
- **Adjacent antithetical pair:** consecutive same-surah verses (s,v),(s,v+1) where one verse's QAC
  root-set intersects the faith-pole {Amn} and the other's intersects the disbelief-pole {kfr,nfq,Srk}
  (byte-identical to the H-NEW-2290/2360 F1 lexicon).
- **Single-substitution aligned tail:** read both verses' word-lists from the END; count matched
  trailing words; allow EXACTLY ONE positional mismatch (the pivot) and continue matching after it;
  matched-tail = number of word-positions that match (excluding the pivot). A second mismatch stops the
  scan.
- **Antonym pivot set (locked):** {frozenset({khayr,sharr})} = {خير, شر}.

- **C-H1 (direction-locked):** the count of adjacent faith-antithetical verse-pairs satisfying
  (single-substitution aligned tail) ∧ (matched-tail ≥ 3) ∧ (pivot is the locked khayr↔sharr antonym)
  is EXACTLY 1, and that pair = ((98,6),(98,7)).
- **Verdict:** C-H1 holds → Arm C CONFIRMED (corpus-UNIQUE minimal-pair antonym muqābala). Count ≠ 1
  or the unique pair ≠ Q 98:6-7 → Arm C NULL (pre-commit violation if a DIFFERENT pair is found).

## Arm D — content-disjointness vs length-matched null (PERMUTATION, seed 20260509, 10000 perms)

- **D statistic:** J(v6,v7) = QAC-root Jaccard of Q 98:6 and Q 98:7.
- **Null D:** draw 10,000 random corpus verse-pairs (a,b), a length-matched to n_roots(98,6) within ±2
  roots, b length-matched to n_roots(98,7) within ±2 roots, excluding the seal pair; compute J(a,b).
  p_lower = (#{null J ≤ obs} + 1)/(N_perm + 1).
- **D-H1 (direction-locked, classical/Q83 prior):** J(v6,v7) < null_mean AND p_lower < α=0.05
  (Q 98:6-7 is MORE content-disjoint than length-matched random pairs).
- **Verdict:** D-H1 holds → Arm D CONFIRMED (disjoint muqābala). J(v6,v7) > null_mean → Arm D NULL
  (pre-commit violation, full prominence) — replicates the H-NEW-2360 jadal-overlap law at verse-pair
  scale. J(v6,v7) < null_mean but p ≥ 0.05 → Arm D DIRECTIONAL.

## Bonferroni

Test family Q098-F-01 has k = 1 permutation cell (Arm D). The deterministic cells (A, B, C) do not
consume α. α_corrected for Arm D = 0.05 / 1 = 0.05.

## MW protections

- **MW-1 (instrument-prior):** byn root key, البينة/البرية surface regex, the faith-field F1 lexicon,
  the single-substitution-aligned-tail algorithm, the antonym-pivot set, and the root-Jaccard are all
  fixed in this file before any run.
- **MW-2 (corpus-prior):** Arm D uses 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A tests BOTH raw-root-count and exact-surface-form operationalizations.
- **MW-5 (replication):** Arms A, B, C are deterministic and fully replicable from the no-tashkeel JSON +
  QAC root-index; Arm D is seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm C's full corpus census of adjacent faith-antithetical pairs is the
  non-target control set (Q 98:6-7 must beat every other corpus pair); Arm D's length-matched random
  pool is the non-target control.
- **MW-7 (post-hoc cap):** the al-bariyya hapax and the khayr↔sharr minimal pair were noticed during
  close reading, then promoted to PRE-REGISTERED direction-locked tests here before computation. Arm D's
  root-Jaccard ballpark (near-median) was explored before locking; this is disclosed, Arm D's locked
  direction is the classical prior (not the peeked direction), and Arm D is capped at single-test α=0.05.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 | title-density-EXACT FALSIFIED (H-NEW-1820 summary corrected) |
| B | B-H1 ∧ B-H2 | CONFIRMED (Q 98-exclusive bariyya hapax-pair) |
| C | C-H1 | CONFIRMED (corpus-UNIQUE khayr↔sharr minimal-pair muqābala) |
| D | D-H1 (J<null, p<0.05) | CONFIRMED (disjoint muqābala) |
| D | J > null_mean | NULL (pre-commit violation, full prominence) |
| D | J < null_mean, p≥0.05 | DIRECTIONAL |

Final Q098-F-01 verdict = honest combination of all four arms, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
