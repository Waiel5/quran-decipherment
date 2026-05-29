---
id: H-NEW-2090
title: Surah-position / verse-count arithmetic-coincidence scan — NULL (chance-consistent)
date: 2026-05-29
status: NULL (PASS-DIRECTED for the pre-registered NULL hypothesis)
prereg: findings/phase-b-hypotheses/prereg-h-new-2090-surah-arithmetic.md
prereg_sha256: 5a6599038a283ce0886b9b8ce3f1cb15d99621f05d8546d3c304348918aed77d
script: findings/phase-b-hypotheses/scripts/h-new-2090.py
data: findings/phase-b-hypotheses/csv/h-new-2090.json
seed: 20260509
n_perm: 10000
bonferroni_k: 8
alpha_bon: 0.00625
verdict: NULL — 0 of 8 arithmetic-coincidence cells exceed chance
---

# H-NEW-2090 — Surah-position / verse-count arithmetic coincidences are chance-consistent

## One-line result

Across an exhaustive pre-registered scan of 8 arithmetic relations between a surah's mushaf-position N and its Hafs-Kūfan verse-count, **0 of 8 cells exceed the permutation-null chance expectation** at Bonferroni α = 0.00625. The observed coincidence-counts are not merely chance-consistent — for most cells they sit **at or below the null mean**. The popular "surah N encodes its verse-count" family of claims is empirically empty.

## The skeptic's headline numbers

| Cell | Relation | Observed hits | Null mean | Null max | p (excess) | Verdict |
|:--|:--|--:|--:|--:|--:|:--|
| 1 | verse_count = N (the famous claim) | **0** | 0.88 | 7 | 1.000 | chance |
| 2 | verse_count = 2N | 1 | 0.51 | 6 | 0.401 | chance |
| 3 | verse_count = N/2 | 0 | 0.65 | 6 | 1.000 | chance |
| 4 | \|verse_count − N\| ≤ 1 | 1 | 2.64 | 12 | 0.931 | chance |
| 5 | N prime AND verse_count prime | 7 | 8.45 | 17 | 0.825 | chance |
| 6 | verse_count = digit-reverse(N) | 0 | 0.98 | 6 | 1.000 | chance |
| 7 | linear grid \|vc − (aN+b)\| = 0, a∈{1,2,3}, b∈{−2..2} | 4 | 8.26 | 20 | 0.973 | chance |
| 8 | N divides verse_count | 6 | 4.85 | 13 | 0.336 | chance |

**Cells exceeding chance (Bonferroni): 0 / 8.** Verdict: NULL.

The most telling line is Cell 1. There is **not a single surah** in the entire Quran whose verse-count equals its position number. The chance expectation under random re-assignment of verse-counts to positions is ~0.88 such coincidences; the corpus delivers zero. The "surah N has N verses" devotional claim has no instance to point to.

## The famous "Q 36 Yāsīn = 36" anecdote, debunked

Sūrat Yāsīn sits at mushaf-position 36 and has **83 verses** (`data/hafs-verse-counts.tsv` row 36), not 36. There is no arithmetic relation between 36 and 83 in any pre-registered cell. The "36" is purely its ordinal position; the number is not echoed in the verse-count, the verse-length, or any simple function thereof. Yāsīn does not appear in any of the exact-hit lists. The anecdote survives in popular discourse only because the *position* number 36 is memorable, not because 36 encodes anything about the sūra's structure.

## Where the (chance-level) hits actually fall

- **Cell 2 (2N)**: the lone hit is **Q 30 al-Rūm** — 60 verses = 2 × 30. One hit; null mean 0.51; p = 0.40. Coincidence.
- **Cell 4 (off-by-one)**: the lone hit is **Q 54 al-Qamar** — 55 verses, |55 − 54| = 1. Far below the null mean of 2.64.
- **Cell 5 (co-primality)**: positions 13, 43, 97, 101, 103, 107, 113 have both a prime position and a prime verse-count (Q 13 = 43 v., Q 43 = 89 v., Q 97 = 5 v., Q 101 = 11 v., Q 103 = 3 v., Q 107 = 7 v., Q 113 = 5 v.). Seven hits — but the null mean is 8.45, so the corpus has *fewer* prime-prime co-occurrences than chance.
- **Cell 7 (linear grid)**: 4 surahs caught by the entire 15-cell (a,b) grid (positions 25, 30, 32, 54). Null mean 8.26. The deliberately generous net — exactly the kind of net a numerologist implicitly casts — catches *half* the chance expectation. This is the clearest demonstration that the "design" is illusory: a permissive grid finds fewer hits in the real corpus than in a random shuffle.
- **Cell 8 (divisibility)**: 6 surahs where position divides verse-count (Q 1: 7=7·1, Q 2: 286=143·2, Q 4: 176=44·4, Q 5: 120=24·5, Q 16: 128=8·16, Q 30: 60=2·30). Six hits, null mean 4.85, p = 0.34 — slightly above chance but nowhere near significance. Driven mechanically by the front-loaded long surahs (small N, large vc) where divisibility is easy.

## Why the corpus is *below* chance on so many cells

Verse-counts are heavily concentrated at small values in the back half of the mushaf (the short Meccan sūras, vc 3–30, occupy positions 78–114), while the identity/near-identity relations would require *large* verse-counts at *large* positions. The mushaf's actual length-ordering (roughly long→short) is structurally **anti-correlated** with the position-equals-count requirement. So the real corpus systematically *under*-produces these coincidences relative to a random shuffle that ignores the length-gradient. This is consistent with the project's established compression-tail laws (d̄ gradients with a kink near position 50): the mushaf is organized by a length/density principle, not by an arithmetic position-encoding.

## Descriptive auxiliaries (reported, never promoted — MW-7)

### D1 — sum invariants (locked arithmetic facts)
- Σ verse-counts = **6236** (matches al-Suyūṭī, *al-Itqān*, nawʿ 17; corpus-locked in MASTER-FINDINGS-LEDGER §1).
- Σ surah-numbers (1..114) = **6555** = 114·115/2.
- Difference = 6555 − 6236 = **319** = 11 × 29.
- Factorizations: 6236 = 2² × 1559 (1559 prime); 6555 = 3 × 5 × **19** × 23; 319 = 11 × 29.

Note the 6555 factorization contains a **19** — the number on which al-Khalifa's "Code 19" numerology is built. This is a textbook post-hoc trap: 6555 is simply the triangular number T(114), and *any* triangular number's factorization will contain whatever small primes it happens to contain. 19 | 6555 because 6555 = 19 × 345; this carries no design content and is reported only to pre-empt the Khalifa-genre reading. The al-Khalifa "Code 19" framework was already decisively rejected project-wide (cross-finding-022, Wave-K). No promotion.

### D2 — position-letter name coincidences (anecdote, un-testable)
- **Q 50 Sūrat Qāf**: opens with the lone letter qāf (abjad 100). Position 50 ≠ 100; verse-count 45. No arithmetic link.
- **Q 68 al-Qalam**: opens with nūn (abjad 50). Position 68 ≠ 50.
- **Q 42 al-Shūrā**: opens ḤM ʿSQ (contains qāf). Position 42, 53 verses. No link.

These are NAME/letter coincidences, not amenable to the verse-count shuffle null, and are explicitly anecdote-capped at single-test α with no promotion. (The muqaṭṭaʿāt letter-axis is established to be orthogonal to content — FALSIFIED-as-content 4× — so a letter↔position arithmetic channel is a priori implausible.)

### D3 — running-sum claim
The cumulative verse-count from position 1 reaches 7 at position 1 and 293 at position 2; it never re-equals a (small) position index thereafter. No clean "running total hits position N" instance exists.

## Methodology recap

- Verse-counts: `data/hafs-verse-counts.tsv` (114 rows, Σ = 6236, asserted at runtime).
- Null: 10000 random permutations (seed 20260509) re-assigning the verse-count multiset across positions 1..114; each cell's coincidence-count recomputed per permutation. Cell 5 holds the structural prime-position mask fixed and shuffles only the landed verse-counts.
- One-sided test in the EXCESS direction (more coincidences than chance), Bonferroni k = 8, α_bon = 0.00625. Direction locked pre-registration.
- MW-2 (≥10000 perms ✓), MW-6 (the shuffle is itself the instrument-control ✓), MW-7 (all anecdotes capped, no promotion ✓).

## Honest limits

- The space of "simple arithmetic relations" between two integers is unbounded; 8 cells + a 15-point linear grid cannot exhaust a determined numerologist's search. But the result is robust precisely because even this *generous, pre-registered* net catches only chance-level (and frequently sub-chance) hits. A search that finds fewer signals than random noise is not hiding a signal.
- The null shuffles the *pairing*, not the verse-count values; it tests "is the position↔count assignment designed," which is the relevant question. Whether the verse-count *multiset itself* is unusual is a separate question, out of scope.
- Position-letter (D2) coincidences are genuinely un-shuffle-testable and remain anecdote.

## Verdict

**NULL — confirmed in the pre-registered direction.** The number of surah-position/verse-count exact arithmetic coincidences does not exceed chance; for the majority of relations it falls below chance, driven by the mushaf's length-ordering. The famous "Q 36 Yāsīn = 36" and "surah N has N verses" claims have **zero** corpus instances. This extends the project's skeptical audit (alongside the already-FALSIFIED "6,666 verses" and al-Khalifa Code-19 claims) to the position↔count arithmetic channel: there is no arithmetic design in the surah/verse-count pairing.

## Cross-finding connections

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (ʿadad al-suwar wa-l-āyāt) — the 6236 total is vindicated here at exact integer precision.
- Popular "6,666 verses" tradition — FALSIFIED (MASTER-FINDINGS-LEDGER §4); this finding extends the skeptical audit.
- al-Khalifa "Code 19" / muqaṭṭaʿāt summation — decisively rejected (cross-finding-022); D1's 6555 = 19 × 345 shown to be a triangular-number artifact, not design.
- Compression-tail laws (h-new-660/700/770) — the mushaf's length/density ordering is the reason position↔count coincidences fall *below* chance; structure is length-driven, not arithmetic-position-driven.
- muqaṭṭaʿāt letter-axis ⊥ content-axis (FALSIFIED 4×) — supports the a-priori implausibility of a position/letter arithmetic channel (D2).
