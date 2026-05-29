---
finding_id: H-NEW-2280
title: al-Biqāʿī munāsabah seam-cohesion test (pericope-scoped at the surah-pair seam)
phase: B+
date: 2026-05-29
status: PRE-REGISTERED (direction-locked BEFORE computation)
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# PRE-REGISTRATION — H-NEW-2280

## Classical claim under test

Burhān al-Dīn Abū al-Ḥasan Ibrāhīm b. ʿUmar **al-Biqāʿī** (d. 885/1480), in
*Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar* ("The String of Pearls on the
Coherence of the Verses and the Sūras"), advances the doctrine that the Quran is
a coherently-ordered text in which **each sūra is connected to the sūra that
follows it** (*munāsabat al-sūra li-mā qablahā / li-mā baʿdahā*). al-Biqāʿī
treats the *transition between* a sūra and its successor as a deliberate
rhetorical seam — he characteristically opens each sūra's commentary by stating
its *munāsaba* (correspondence) to the closing material of the preceding sūra
and the opening material of the following one. The most famous single case is
the seam **Q 8 al-Anfāl → Q 9 al-Tawba (Barāʾa)**: the *only* canonical
adjacency lacking an intervening *basmala*, which classical scholars (al-Biqāʿī
and before him al-Rāzī, *Mafātīḥ al-ghayb*, and the tradition of Ibn ʿAbbās
questioning ʿUthmān b. ʿAffān, al-Tirmidhī idInBook #3170 in
`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`)
explain precisely by appeal to the thematic continuity
("*qiṣṣatuhā shabīha bi-qiṣṣatihā*") between the end of al-Anfāl and the
beginning of al-Tawba.

al-Biqāʿī therefore locates inter-sūra coherence **at the seam**, not in the
bulk of the sūra. Prior project work (the four FALSIFIED al-Biqāʿī
muqaṭṭaʿāt-content-munāsaba replications, INVESTIGATION-PROTOCOL §3.7) tested
*whole-surah* cohesion of letter-defined clusters and found NULL; but
whole-surah cohesion is dominated by length and genre (cross-finding-025-formal)
and is **not where al-Biqāʿī actually situates the claim**. This pre-reg tests
the claim at the granularity al-Biqāʿī uses: the boundary pericope.

## Hypothesis (direction-LOCKED before any computation)

> **H1 (locked):** Across the 113 canonical mushaf adjacencies (Q 1→Q 2, …,
> Q 113→Q 114), the mean root-Jaccard cohesion between the **last pericope of
> sūra N** and the **first pericope of sūra N+1** is GREATER than the mean
> root-Jaccard of a null of random (non-adjacent) last-pericope/first-pericope
> sūra pairs. Direction: **z > 0** (canonical-seam cohesion > random-pair
> baseline).

Locked direction: **canonical-seam > random-pair (z > 0, one-tailed greater).**

### Failure / NULL / pre-commit-violation conditions (locked)

- **PASS-DIRECTED**: z > 0 AND permutation p_greater < 0.05.
- **DIRECTIONAL**: z > 0 but p_greater ≥ 0.05.
- **NULL**: z ≈ 0 with p_greater ≥ 0.05 and not reversed.
- **PRE-COMMIT-VIOLATION (published as NULL with prominence)**: the observed
  canonical-seam mean is LESS than the null mean (z < 0). Per
  INVESTIGATION-PROTOCOL §1.8, this is published with full prominence and
  REFINES al-Biqāʿī: it would mean munāsabah is NOT a seam-lexical (shared-root)
  effect — the coherence al-Biqāʿī perceives would be thematic/semantic/
  pronominal rather than reducible to shared QAC roots at the boundary.

A NULL or reversed result is a **first-class finding**: it would show that
al-Biqāʿī's perceived inter-sūra coherence is not captured by lexical-root
overlap at the seam, which is itself a substantive empirical claim about the
*nature* of munāsabah.

## Pericope definition (PRE-REGISTERED, two k values)

- **Pericope window k ∈ {3, 5}** (two pre-registered windows; primary = k=3,
  replication = k=5, per MW-5).
- **Last pericope of sūra N** = its last `min(k, len(N))` verses.
- **First pericope of sūra N+1** = its first `min(k, len(N+1))` verses.
- **Clamping rule (locked):** for the 5 surahs with fewer than 5 verses (Q 103,
  Q 108, Q 110 = 3 verses; Q 106, Q 112 = 4 verses) the pericope is clamped to
  the full surah length. This keeps all 113 adjacencies intact. The first
  pericope of Q 1 is irrelevant (Q 1 has no predecessor seam); the basmala is
  counted only within Q 1 per the rules-tuple, so the first pericope of every
  surah N+1 (N≥1) is its first content verses as listed in
  `quran-text/quran-no-tashkeel.json` (which carries no standalone basmala verse
  except inside Q 1). For Q 9, which has no basmala, the first pericope is simply
  vv 1–k.

## Seam statistic

For canonical adjacency N→N+1:
- `R_last(N)`  = union of QAC ROOTs over the last `min(k,len N)` verses of N.
- `R_first(N+1)` = union of QAC ROOTs over the first `min(k,len N+1)` verses of N+1.
- `J(N→N+1)` = |R_last ∩ R_first| / |R_last ∪ R_first|  (0 if union empty).
- **Observed seam statistic** = mean of `J` over all 113 canonical adjacencies.

## Null model (PRE-REGISTERED)

**Random non-adjacent last/first pericope pairing.** The null isolates the
*seam-adjacency* effect from generic "last-verses vs first-verses share
function-word-bearing roots" baseline:

- The pool of 114 surah "last-k pericopes" {L_1…L_114} and 114 surah "first-k
  pericopes" {F_1…F_114} is fixed (each computed once).
- One null replicate = a random derangement-style pairing of 113 (last_a,
  first_b) draws where for each draw `a` and `b` are random surah indices with
  **b ≠ a and b ≠ a+1** (i.e. NOT the canonical successor of `a`, and not the
  same surah), then mean-J is taken over the 113 random pairs.
- This is repeated **n_perm = 10000** times with **seed = 20260509**
  (`random.Random(20260509)`).
- z = (obs_mean − null_mean) / null_std; p_greater = #{null ≥ obs}/n_perm.

This null preserves the marginal pericope-length and pericope-vocabulary
distributions (we reuse the SAME real pericopes), changing ONLY the
adjacency relation. A positive result therefore cannot be an artifact of
last/first pericopes sharing generic roots; it must reflect that the
*canonical successor* shares more than a random non-successor.

## Per-seam reporting (locked)

- Report the full 113-entry per-seam J table.
- Report the strongest seams (top-10 by J) and weakest seams (bottom-10).
- **Q 8 → Q 9 (al-Anfāl → al-Tawba, basmala-less seam)** reported explicitly
  with its J value, shared roots, and its rank among the 113.

## Replication & controls (MW-mapping)

- **MW-1 (instrument-prior):** root-Jaccard on QAC v0.4 ROOT, fixed before run
  (identical instrument to H-NEW-1380/1510/1520/1760 pericope tests).
- **MW-2 (corpus-prior):** 10000-perm permutation null.
- **MW-3 (alternative-models):** report both k=3 and k=5 windows.
- **MW-5 (replication):** k=5 replicates k=3; a second seed (20260510) replicate
  reported as a robustness check (not the primary, primary seed = 20260509).
- **MW-6 (instrument-control):** the random non-adjacent null IS the control
  (same pericopes, scrambled adjacency).
- **MW-7 (post-hoc cap):** the Q 8→Q 9 single-seam callout is descriptive
  (named in advance here), not a post-hoc hypothesis.

## Bonferroni

The hypothesis family is the corpus-level mean comparison at **k ∈ {3, 5}** →
k_family = 2 → α_corrected = 0.05 / 2 = **0.025**. Both raw and Bonferroni
p reported. (The 113 per-seam J values are descriptive, not a 113-test family;
the locked inferential test is the single corpus-mean comparison per k.)

## Output files

- This pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2280-munasabah-seam.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2280.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2280.json`
- Findings: `findings/phase-b-hypotheses/h-new-2280-munasabah-seam.md`

## Data provenance

- `quran-text/quran-no-tashkeel.json` — verse structure / surah lengths.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4 ROOTs per verse.
- al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*
  (`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`).

*Pre-registered by Waiel Al-Shujaa, 2026-05-29, BEFORE any computation.
Bismillāhi al-Raḥmāni al-Raḥīm.*
