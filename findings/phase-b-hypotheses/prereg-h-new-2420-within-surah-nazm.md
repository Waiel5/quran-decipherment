---
finding_id: H-NEW-2420
title: al-Biqāʿī within-surah sequential naẓm — do consecutive verses cohere more than shuffled order?
phase: B+
date: 2026-05-29
status: PRE-REGISTERED (direction-locked BEFORE computation)
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# PRE-REGISTRATION — H-NEW-2420

## Classical claim under test

Burhān al-Dīn Abū al-Ḥasan Ibrāhīm b. ʿUmar **al-Biqāʿī** (d. 885/1480), in
*Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar* ("The String of Pearls on the
Coherence of the Verses and the Sūras"), advances the doctrine that the Quran is
a coherently-ordered text not only at the inter-sūra seam (tested in H-NEW-2280)
but **within each sūra at the verse level**: each āya is *munāsib* (fitted,
corresponded) to the āya beside it, so that the sūra is an *ordered naẓm* — a
purposefully-sequenced string of verses — not a random verse-bag (an anthology
of independently-revealed verses arranged arbitrarily). al-Biqāʿī's signature
method is to open each verse's commentary by stating its *munāsaba* to the verse
that precedes it (*munāsabat al-āya li-mā qablahā*). The doctrine that the order
of verses *within* a sūra is **tawqīfī** (divinely fixed) and bears coherent
sequence is the classical consensus that al-Biqāʿī systematized verse-by-verse
across the entire muṣḥaf.

Source on disk: al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*
(`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`, 738 pp.); the
ring-structure / adjacent-munāsabāt notes
`data/literature/classical-tafsir/razi-biqai-munasabat-rings.md`.

H-NEW-2280 tested the **BETWEEN-surah** seam (last pericope of N vs first
pericope of N+1) and found a real, scale-dependent lexical seam trace
(k=3 DIRECTIONAL, k=5 PASS-DIRECTED). This pre-reg tests the **complementary
WITHIN-surah** claim: the *intra-surah verse-sequencing* — al-Biqāʿī's core
verse-to-verse naẓm. The two together bound al-Biqāʿī's full munāsaba doctrine
at both the inter-surah and intra-surah granularities.

This does NOT re-test, nor rehabilitate, the four FALSIFIED al-Biqāʿī
*whole-surah muqaṭṭaʿāt-content* munāsabas (INVESTIGATION-PROTOCOL §3.7); it is a
distinct claim (verse-sequence ordering) at a distinct scale (adjacent verse
pairs within a single surah).

## Hypothesis (direction-LOCKED before any computation)

> **H1 (locked, aggregate):** Across the corpus, the observed mean
> adjacent-verse root-Jaccard cohesion (mean over consecutive verse pairs of a
> surah's CANONICAL verse order) EXCEEDS the mean of a within-surah
> verse-shuffle null (the same verses re-ordered at random). Aggregated across
> surahs (Stouffer-combined per-surah z, and a sign/count summary), the
> aggregate effect is positive: **aggregate z > 0** — consecutive verses cohere
> more than shuffled order.

> **H2 (locked, per-surah roster):** Some surahs individually have adjacent
> cohesion significantly ABOVE their own within-surah shuffle distribution
> (the *naẓm-tight* surahs); others are shuffle-indistinguishable
> (*loose / anthology-like*). The per-surah pass-set is reported as the prize
> deliverable. Direction per surah is locked the same way: PASS requires
> observed > shuffle-mean (z_surah > 0) AND Bonferroni-significant.

Locked direction (both H1 and H2): **canonical adjacent-cohesion > shuffled
adjacent-cohesion (z > 0, one-tailed greater).**

### Failure / NULL / pre-commit-violation conditions (locked)

Aggregate (H1):
- **PASS-DIRECTED**: aggregate z > 0 AND the aggregate permutation/sign test
  p_greater < 0.05.
- **DIRECTIONAL**: aggregate z > 0 but p_greater ≥ 0.05.
- **NULL**: aggregate z ≈ 0, p_greater ≥ 0.05, not reversed.
- **PRE-COMMIT-VIOLATION (published as NULL with full prominence)**: aggregate
  observed mean is LESS than shuffle mean (aggregate z < 0). Per
  INVESTIGATION-PROTOCOL §1.8 this is published prominently and REFINES
  al-Biqāʿī: it would mean adjacent verses are NOT more lexically cohesive than
  random within-surah orderings — the perceived naẓm would be
  thematic/pronominal/rhetorical rather than reducible to shared QAC roots
  between neighbours, OR (a real possibility) that verses are *anti-clustered*
  (the surah deliberately spaces related vocabulary apart — a "dispersion"
  rather than "adjacency" design).

Per-surah (H2):
- A surah PASSES (is *naẓm-tight*) iff z_surah > 0 AND its per-surah permutation
  p_greater < α_bonferroni (see below).
- A surah is *loose / anthology-like* iff z_surah is not significantly positive
  (p ≥ α_bonferroni), regardless of sign.
- A surah with z_surah < 0 (canonical order LESS cohesive than shuffle) is
  flagged as an individual reversed/dispersion case and reported with prominence.

A corpus-aggregate NULL or REVERSED result is a **first-class finding**: it
would show that al-Biqāʿī's perceived intra-surah naẓm is not a shared-root
adjacency effect — a substantive empirical claim about the *nature* of naẓm.

## Adjacency metric (PRE-REGISTERED)

For a surah with verses v_1 … v_L (canonical Hafs-Kufan order as listed in
`quran-text/quran-no-tashkeel.json`):

- `R(v_i)` = union of QAC v0.4 ROOTs over the morphological segments of verse i
  (first ROOT-tagged feature per segment; identical convention to
  h-new-1380/1510/1520/1760/2280).
- Adjacent-pair Jaccard: `J(i) = |R(v_i) ∩ R(v_{i+1})| / |R(v_i) ∪ R(v_{i+1})|`
  (0 if union empty).
- **Surah adjacency statistic** `A(surah)` = mean of `J(i)` over the
  `L − 1` consecutive pairs of the surah's CANONICAL verse order.
- **Corpus observed statistic** = mean of `A(surah)` over the eligible surahs
  (defined below), AND the per-surah `A` values themselves.

## Null model (PRE-REGISTERED) — within-surah verse-shuffle

For each surah independently:
- Hold the surah's verse-root-sets fixed (the SAME L verse-root-sets).
- One null replicate = a uniformly random permutation of the L verses; recompute
  the mean adjacent-pair Jaccard over the `L − 1` consecutive pairs of the
  permuted order.
- Repeat **n_perm = 10000** times with **seed = 20260509**
  (`random.Random(20260509)`; the SAME master seed is used, advancing the RNG
  state surah-by-surah in ascending surah-id order, so the run is fully
  deterministic and reproducible).
- `null_mean(surah)`, `null_std(surah)` over the 10000 shuffle-means.
- `z_surah = (A_obs − null_mean) / null_std`.
- `p_greater(surah) = #{shuffle-mean ≥ A_obs} / n_perm`
  (reported floor 1/n_perm when zero exceedances).

This null **isolates the ORDER**: identical verse content, identical verse
count, identical multiset of verse-root-sets — only the *sequence* is scrambled.
A positive result therefore cannot be an artifact of a surah having
high-overlap vocabulary in general; it must reflect that the *canonical
adjacency* places more-overlapping verses next to each other than a random
ordering does.

### Eligibility (PRE-REGISTERED)

- The shuffle null is only informative when the number of distinct attainable
  adjacent-mean values is large enough to resolve a Bonferroni-significant tail.
  A surah of length L has L! orderings; the minimum attainable per-surah p is
  ~1/(number of distinct adjacent-mean values). For very short surahs this floor
  exceeds α_bonferroni and a PASS is *impossible in principle*.
- **Locked rule:** surahs with **L < 4 verses** (the 3-verse surahs Q 103
  al-ʿAṣr, Q 108 al-Kawthar, Q 110 al-Naṣr) are **excluded from the per-surah
  significance family** (their p-floor with only ~3 distinct orderings cannot
  clear Bonferroni) and from the aggregate inferential mean; they are reported
  descriptively only.
- **Eligible family** = the 111 surahs with L ≥ 4. (Q 1 has L=7 with the basmala
  as verse 1 per rules-tuple; it is eligible.)
- Bonferroni family size **k = 111** → **α_corrected = 0.05 / 111 = 4.50×10⁻⁴**.

## Aggregate combination (PRE-REGISTERED)

Two pre-registered aggregate views (MW-3 alternative-models):
1. **Sign / count summary**: number of eligible surahs with z_surah > 0 vs < 0;
   binomial sign test against 50/50 (one-tailed, more-positive).
2. **Stouffer combined z**: convert each surah's one-tailed p_greater to a
   z, combine as `Z = Σ z_i / sqrt(n)`; report the combined Z and its
   one-tailed p. (Per-surah permutation p of exactly 0 is floored at
   0.5/n_perm before z-conversion to avoid infinite z.)

Both must point the locked direction (more positive than chance) for an
aggregate PASS-DIRECTED.

## Per-surah reporting (locked)

- Full per-surah table: L, A_obs, null_mean, null_std, z_surah, p_greater,
  Bonferroni verdict (naẓm-tight / loose), region (Meccan/Medinan), length-class.
- The **naẓm-tight roster** (surahs passing Bonferroni) — the prize.
- The **loose / anthology-like roster** (shuffle-indistinguishable).
- Any **reversed/dispersion** surahs (z_surah < 0) flagged with prominence.
- **Correlation analyses (descriptive, locked in advance):**
  (a) Spearman ρ of z_surah vs surah length L;
  (b) Mann-Whitney / mean-z comparison Meccan vs Medinan (region);
  (c) Spearman ρ of z_surah vs revelation order (Nöldeke), from
  `data/revelation-order.csv`.
  These contextual correlations are descriptive (not part of the locked
  inferential family) and reported with that caveat.

## Replication & controls (MW-mapping)

- **MW-1 (instrument-prior):** root-Jaccard on QAC v0.4 ROOT, fixed before run
  (identical instrument to H-NEW-2280 and the pericope-flip family).
- **MW-2 (corpus-prior):** 10000-perm permutation null PER SURAH.
- **MW-3 (alternative-models):** two aggregate combiners (sign test + Stouffer);
  also report the aggregate under both inclusion of all 114 and the eligible 111.
- **MW-5 (replication):** a second-seed (20260510) replicate of the aggregate
  sign-count and Stouffer-Z reported as a robustness check.
- **MW-6 (instrument-control):** the within-surah shuffle IS the control — same
  verses, scrambled order; isolates sequence from content.
- **MW-7 (post-hoc cap):** the region/length/chronology correlations are
  descriptive context, capped at single-test interpretation; the named
  inferential claims are H1 (aggregate) and H2 (per-surah Bonferroni roster)
  only.

## Bonferroni

- Per-surah family: k = 111 eligible surahs → **α_corrected = 4.50×10⁻⁴**.
- Aggregate H1: a single corpus-level claim (sign test + Stouffer); reported at
  α = 0.05 (it is one inferential test, not a family). Both raw and, where a
  family applies, Bonferroni p reported.

## Output files

- This pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2420-within-surah-nazm.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2420.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2420.json`
- Findings: `findings/phase-b-hypotheses/h-new-2420-within-surah-nazm.md`

## Data provenance

- `quran-text/quran-no-tashkeel.json` — verse structure / surah lengths / order.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4 ROOTs per verse.
- `data/revelation-order.csv` — Nöldeke chronology (for the descriptive
  chronology correlation).
- al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*
  (`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`).

*Pre-registered by Waiel Al-Shujaa, 2026-05-29, BEFORE any computation.
Bismillāhi al-Raḥmāni al-Raḥīm.*
