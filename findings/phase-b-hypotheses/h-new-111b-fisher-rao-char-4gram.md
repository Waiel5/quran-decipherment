# [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] — Fisher-Rao char-4-gram replication of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **The arithmetic here is not retracted.** What fell is the inference drawn from the Fisher-Rao
> permutation null. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`),
> al-Bukhārī scores **z = −13.84** and pre-Islamic poetry **z = −15.13** against the Qurʾān's
> **z = −11.50** on an instrument-matched pipeline, and both baselines sit closer to their own TSP
> optima. Cutting this corpus's own verse stream into 114 blocks of the same size profile at offsets
> that ignore every surah seam gives z = −11.23 to −13.18. **Length-sorting alone reaches z = −8.66**
> (H-NEW-111's write-up mis-transcribed that anchor as 107.27; its own `csv/h-new-111.json` records
> 91.03 / 90.30). The mushaf's honest margin over pure length is **2.80 σ**, not 11.46 σ.
> The *relative* claim survives — mushaf 85.76 < Nöldeke 87.23 < Tanzil 89.53.
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


**Finding ID**: [[h-new-111b-fisher-rao-char-4gram|h-new-111b]]
**Parent**: [[h-new-111-fisher-rao-mushaf|h-new-111]] (Fisher-Rao on root tokens)
**Date**: 2026-04-17
**Specialist**: [[h-new-111b-fisher-rao-char-4gram|h-new-111b]]-specialist
**Pre-reg**: `findings/phase-b-hypotheses/h-new-111b-prereg.md`
**Pre-reg SHA-256**: `6f28cb21faca379bb4bb096432eafb8bdc912509da36f6eb2620ea588b7b27fd`
**Seed**: 20260417 (same as parent for comparability)
**Rules tuple**: (no-tashkeel, char-4-grams with spaces, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kūfan)
**Verdict**: **PARTIAL REPLICATION** — primary and Secondary A replicate strongly; Secondary B (chronology reversal) does NOT replicate on the char-4-gram feature space.

---

## Headline

The Fisher-Rao mushaf-geodesicity signal first reported in [[h-new-111-fisher-rao-mushaf|H-NEW-111]] on
root-token distributions **replicates on an orthogonal feature space**
(per-surah char-4-gram histograms, no-tashkeel), at nearly identical effect
size:

- **z = −11.41** (parent: −11.46)
- **L_mushaf / L_2opt = 1.114** (parent: 1.107)
- **p_primary < 10⁻⁴** (identical to parent)

However, the Nöldeke-reversal component does **not** replicate:
`L_mushaf (89.23) > L_nold (89.10)` by 0.127 units on char-4-grams,
whereas on roots `L_mushaf (85.76) < L_nold (87.23)` by 1.473 units.
Both orderings remain strongly non-random (each p < 10⁻⁴).

---

## Numbers

### PRIMARY (one-sided lower-tail, α_bon = 0.0167)

| Quantity | [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-grams) | [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (roots) |
|---|---|---|
| L_mushaf | **89.226** | 85.760 |
| Null mean | 103.062 | 104.346 |
| Null SD | 1.212 | 1.622 |
| Null min observed | 98.839 | 98.111 |
| Null 5th percentile | 101.047 | 101.663 |
| **z-score** | **−11.41** | **−11.46** |
| #{L_perm ≤ L_mushaf} | 0 / 10,000 | 0 / 10,000 |
| **p_primary** | **< 1/10001 ≈ 10⁻⁴** | < 1/10001 |
| **Bonferroni verdict** | **PASS (by 167×)** | PASS |

Z-scores match to within 0.5% of each other. Both orderings beat every one
of 10,000 random permutations. Feature spaces are independent (roots use
QAC morphological annotation; 4-grams use surface graphemes) but produce
the same effect size.

### SECONDARY A — geodesic-optimality ratio

| Quantity | [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] | [[h-new-111-fisher-rao-mushaf|H-NEW-111]] |
|---|---|---|
| L_greedy_best | 81.485 | 78.836 |
| L_2opt_best | **80.082** | 77.467 |
| **L_mushaf / L_2opt** | **1.114** | **1.107** |

Ratios differ by 0.7%. Both orderings are **within 11%–12% of the 2-opt
upper bound on the TSP optimum** on 114 nodes. This is a PASS of the
pre-registered near-optimal threshold (<1.2) on an orthogonal feature.

### SECONDARY B — Nöldeke chronology reversal (one-sided pre-registered)

| Quantity | [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] | [[h-new-111-fisher-rao-mushaf|H-NEW-111]] |
|---|---|---|
| L_mushaf | 89.226 | 85.760 |
| L_nold (Nöldeke) | **89.100** | 87.232 |
| L_tanzil (Egyptian std) | 91.443 | 89.530 |
| p_nold (1-sided lower vs null) | 10⁻⁴ | 2×10⁻⁴ |
| p_tanzil (1-sided lower vs null) | 10⁻⁴ | similar |
| Δ = L_mushaf − L_nold | **+0.127** | −1.473 |
| Reversal replicated? | **NO** (flipped sign) | — |
| Mushaf vs Tanzil | L_mushaf < L_tanzil by 2.22 | L_mushaf < L_tanzil by 3.77 |

**Both** orderings (mushaf and Nöldeke) beat random at p < 10⁻⁴ on
char-4-grams — consistent with "any reasonable reading order is
non-random at the char-4-gram level". But the MUSHAF-SHORTER-THAN-NOLDEKE
sign from the parent flips to MUSHAF-LONGER by 0.127 units. Mushaf is
still shorter than Tanzil by 2.22 units, so the reversal partially holds
against the Tanzil/Egyptian reconstruction but NOT against Nöldeke.

### MW-5 positive control

Greedy-NN from surah 1 on char-4-gram distances: L = 81.755, p = 10⁻⁴.
**Positive control fires** at α = 10⁻⁴ — null is not broken.

### Sanity anchors

| Ordering | L (char-4-grams) | L (roots, parent) |
|---|---|---|
| Mushaf | 89.23 | 85.76 |
| Nöldeke | 89.10 | 87.23 |
| Tanzil | 91.44 | 89.53 |
| Length-sorted asc | 102.58 | 107.27 |
| Length-sorted desc | 102.58 | 107.27 |
| Null mean | 103.06 | 104.35 |
| 2-opt approx min | 80.08 | 77.47 |

Length-sorted orderings are near null-mean on both features: MW-1
normalization is working as intended.

---

## Interpretation

### What replicates

The **primary geodesicity claim of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]** — that mushaf order is
information-geometrically optimized across the 114-surah simplex — is
confirmed on an orthogonal feature space at near-identical effect size:

- z-score reproduces to within 0.4%
- TSP-ratio reproduces to within 0.7%
- All 10,000 random permutations are longer than mushaf, same as parent

This is a **strong cross-feature replication**. Root-token distributions
(morphological) and char-4-gram distributions (graphemic/phonological)
both rank the mushaf as near-TSP-optimal. The two feature spaces share
information only through the underlying canonical text — a signal this
consistent across independent summaries of the corpus is unlikely to
be a feature-specific artifact.

### What does NOT replicate

The **Nöldeke-chronology reversal** does not replicate on char-4-grams:

- On roots: mushaf beats Nöldeke by 1.47 (clear)
- On char-4-grams: Nöldeke beats mushaf by 0.13 (tiny, opposite sign)

This asymmetry has a plausible reading. Char-4-grams include function
words and their immediate grapheme neighborhoods (high-freq 4-grams are
" من ", "لله ", "الله", " الل", "ن ال"). Function-word frequency tracks
surah LENGTH and REGISTER (Medinan legalistic prose uses more frequent
function-word repetition than Meccan eschatological prose). Nöldeke's
chronology is substantially a grouping-by-register (Early/Middle/Late
Meccan, then Medinan), so it naturally clusters similar-register surahs
adjacently — that clustering helps on a feature space that is
register-sensitive (4-grams) MORE than on a feature space that is
register-normalized (root-distributions, which collapse different
function-word surface forms into their roots).

In other words: on root-distributions, chronology's register-clustering
advantage is smaller than the mushaf's actual coherence advantage; on
char-4-grams, the register-clustering advantage is comparable to the
mushaf's coherence, and the ordering of the two flips narrowly.

This is **consistent with** the parent finding's caveat (§4 of the
parent) that length/register correlates survive MW-1 normalization at
the margins; the parent reported this as a known limit, and [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]
concretely shows where the reversal is marginal.

### Combined-evidence case

The PRIMARY and SECONDARY-A claims are now supported on TWO orthogonal
feature spaces at essentially identical effect sizes. Under Fisher's
combination test for independent p-values (each p ≤ 1×10⁻⁴):

    χ² = −2(ln p₁ + ln p₂) ≥ −2(2·ln 10⁻⁴) = 36.84  on 4 df
    combined p ≤ 1.9×10⁻⁷

This is well past the threshold for cross-finding CONFIRMED status, at
least on the PRIMARY geodesicity claim.

The SECONDARY-B chronology reversal, in contrast, has mixed evidence:
fires at p < 10⁻⁴ against Tanzil under both features, but against
Nöldeke it fires on roots and fails to fire on 4-grams. Treat the
chronology reversal as **feature-space-dependent** and do NOT promote
it beyond PASS-DIRECTED on the root axis alone.

---

## Caveats / honest limits

1. **Secondary B does NOT replicate**, and the sign flips (mushaf
   NARROWLY longer than Nöldeke on 4-grams). This is not a "both flips
   are small so ignore" situation — the parent's reversal was
   pre-registered as a two-sided exploratory test with a specific sign
   observed; here it is pre-registered as one-sided and it fails. The
   [[h-new-111-fisher-rao-mushaf|H-NEW-111]] reversal should be tagged as **feature-specific** in any
   downstream summary.

2. **Char-4-grams are orthogonal to roots in construction but not
   fully independent in information**. Both derive from the same
   canonical text. Orthogonality here means "different feature
   engineering"; p-values from the two features are not strictly
   independent for Fisher combination. A conservative reading would
   replace Fisher with Bonferroni across the two families, giving
   combined p ≤ 2×10⁻⁴ rather than 1.9×10⁻⁷ — still past any
   reasonable CONFIRMED threshold on the PRIMARY claim.

3. **K_char = 2000** covers 59.2% of the sliding-window 4-gram mass
   (global total 417,206 tokens, 37,406 distinct). The cutoff frequency
   at K=2000 is 37. Going to K=5000 would capture more mass but include
   very-low-frequency 4-grams dominated by Poisson noise; K=500 would
   capture less. Robustness to K is NOT tested here (locked pre-hoc);
   belongs to any future [[h-new-111c-fisher-rao-verselen|H-NEW-111c]].

4. **2-opt is an upper bound on TSP optimum**; the true ratio
   L_mushaf / L_min may be slightly larger than 1.114. Since 1.114 is
   well inside the pre-registered <1.2 near-optimal band, this caveat
   does not change the secondary-A verdict.

5. **Verse-concatenation spacing**: I used single-space between verses.
   An alternative would be to omit inter-verse spacing or use a special
   boundary token. Pre-reg locked "single space (mirrors natural
   recitation spacing)". Robustness to this choice is N/A at this time.

6. **MW-5 positive control passes at p = 10⁻⁴ exactly** (the floor of
   the permutation-p estimator). This is structurally the strongest
   possible signal — no random permutation beat the greedy-NN ordering
   over 10,000 draws. The null is sound.

## Connections

- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (parent): replicates on primary + secondary A; diverges
  on secondary B.
- **[[h-new-112-spectral-network|H-NEW-112]]** (Spectral network, if that's the queued replication):
  independent third axis would further solidify the PRIMARY claim.
- **[[h-new-89-meta-cluster-network|H-NEW-89]]** (meta-cluster hub Q 62): cross-check whether Q 62 is a
  hub on the char-4-gram distance matrix too. Queued descriptive.
- **canonical-order-recovery (T3 earlier in project)**: recognition
  (total path length) replicates; reconstruction (rank-order recovery)
  not tested here.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-111b-prereg.md`
- Script: `scripts/h_new_111b_fisher_rao_char_4gram.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-111b.json`
- Journal: `journal/h-new-111b-run-1.md`

## Verdict

**PARTIAL REPLICATION** at PASS-DIRECTED-equivalent strength on PRIMARY
and SECONDARY A; NULL on SECONDARY B under the pre-registered one-sided
reversal direction.

- Primary: **PASS** (p < 10⁻⁴ < 0.0167 Bonferroni-3)
- Secondary A: **PASS** (ratio 1.114 < 1.2 near-optimal band)
- Secondary B: **NULL** (Δ = +0.127, sign flipped vs parent; Nöldeke
  shorter than mushaf on char-4-grams)
- MW-5: PASS
- Cross-finding note: combine [[h-new-111-fisher-rao-mushaf|H-NEW-111]] + [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] for CONFIRMED
  status on the PRIMARY geodesicity claim only. Do NOT promote the
  chronology-reversal claim beyond PASS-DIRECTED (it is feature-space-
  specific to root distributions).
