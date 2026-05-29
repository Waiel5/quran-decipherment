---
finding_id: H-NEW-2420
title: al-Biqāʿī within-surah sequential naẓm — consecutive verses cohere more than shuffled order
phase: B+
date: 2026-05-29
verdict: PASS-DIRECTED (aggregate) — consecutive-verse cohesion EXCEEDS the within-surah shuffle null at corpus law-strength (97/111 surahs positive, Stouffer Z=+18.70, p≈10⁻⁷⁸; +56.6% relative lift). Direction LOCKED-CORRECT. 33 surahs are individually naẓm-TIGHT (Bonferroni); 33 loose/anthology-like; the prize REVERSAL is Q 55 al-Raḥmān (z=−5.32) — the refrain-DISPERSED surah. NO pre-commit violation.
seed: 20260509
prereg_sha: 301f71184201dfa228912f3a65a1fd7de1e2dd9e675316acad7fcb32a904dce1
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-2420 — al-Biqāʿī's within-surah naẓm, tested verse-by-verse

## The claim and where it lives

Burhān al-Dīn al-Biqāʿī (d. 885/1480), *Naẓm al-durar fī tanāsub al-āyāt
wa-l-suwar*, holds that the Quran is a coherently-ordered whole not only between
sūras (the seam, tested in **H-NEW-2280**) but **within each sūra at the verse
level**: every āya is *munāsib* (fitted, corresponded) to the verse beside it, so
that a sūra is an **ordered naẓm** — a purposefully-sequenced string of verses —
and **not a random verse-bag** (an anthology of independently-revealed verses
arranged arbitrarily). al-Biqāʿī's signature method, applied verse-by-verse across
the whole muṣḥaf, is to open each verse's commentary by stating its *munāsaba* to
the preceding verse (*munāsabat al-āya li-mā qablahā*). The doctrine that the
*order of verses within a sūra* is tawqīfī and bears coherent sequence is the
classical position al-Biqāʿī systematized
(`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`;
`data/literature/classical-tafsir/razi-biqai-munasabat-rings.md`).

This is the **complement** to H-NEW-2280: that finding tested al-Biqāʿī BETWEEN
surahs (the last pericope of N vs the first pericope of N+1) and found a real,
scale-dependent seam trace. This one tests him WITHIN surahs at his own core
granularity — the adjacent verse pair.

It does **not** re-test or rehabilitate the four FALSIFIED al-Biqāʿī *whole-surah
muqaṭṭaʿāt-content* munāsabas (INVESTIGATION-PROTOCOL §3.7); it is a distinct
claim (verse-sequence ordering) at a distinct scale (adjacent verse pairs within
a single surah).

## Method (pre-registered, direction-locked)

- **Adjacency metric.** For a surah's verses v_1…v_L in CANONICAL Hafs-Kufan
  order, `R(v_i)` = union of QAC v0.4 ROOTs over verse i; adjacent-pair Jaccard
  `J(i) = |R(v_i)∩R(v_{i+1})| / |R(v_i)∪R(v_{i+1})|`; the surah statistic
  `A(surah)` = mean of `J(i)` over the L−1 consecutive pairs.
- **Within-surah shuffle null.** Per surah, hold the L verse-root-sets fixed and
  uniformly permute the verse ORDER; recompute mean adjacent-pair Jaccard.
  10000 perms/surah, single master seed 20260509 advanced in ascending surah-id.
  `z_surah = (A_obs − null_mean)/null_std`; one-tailed `p_greater`. The null
  isolates **sequence** — identical content, identical count, scrambled order.
- **Direction LOCKED before computation:** canonical adjacent-cohesion > shuffled
  (z>0), aggregate and per-surah. Reversed (z<0) aggregate = pre-commit-violation
  published as NULL.
- **Eligibility.** Surahs with L<4 (Q 103/108/110) excluded from the
  significance family — confirmed by data: Q 103/108 admit only **1** distinct
  shuffle-mean and Q 110 only **2**, so a Bonferroni-significant p is impossible
  in principle. Eligible family **k = 111** → **α_corrected = 4.50×10⁻⁴**.
- **Aggregate combiners (MW-3):** binomial sign test on z-signs, and Stouffer Z
  over per-surah one-tailed p. **Replication (MW-5):** second seed 20260510.
- Pre-reg SHA-256 `301f7118…dce1`, embedded in `scripts/h-new-2420.py`, verified
  at runtime (PASS).

## Result — PASS-DIRECTED at corpus law-strength

| Quantity | Value |
|:--|:--|
| Corpus observed mean A (111 eligible) | **0.068555** |
| Within-surah shuffle null mean | 0.043770 |
| Relative lift | **+56.6%** |
| Surahs with z_surah > 0 / < 0 | **97 / 14** |
| Binomial sign test (one-tailed) | p = 9.43×10⁻¹⁷ |
| **Stouffer combined Z** | **+18.70** |
| Stouffer one-tailed p | ≈ 2.7×10⁻⁷⁸ |
| Replicate seed 20260510 | 97/14, Stouffer Z=+18.68 (stable) |

**Verdict: PASS-DIRECTED.** Consecutive verses are, across the corpus,
substantially more lexically cohesive (root-Jaccard) than their own randomly
re-ordered sequences — a +56.6% relative lift, with 97 of 111 eligible surahs
pointing the locked direction. **al-Biqāʿī's intra-surah naẓm is empirically
real at the shared-root level: the Quran is an ordered text, not a random
verse-bag.** Direction is LOCKED-CORRECT; there is NO pre-commit violation.

This is the WITHIN-surah counterpart to H-NEW-2280's BETWEEN-surah seam result —
and it is much stronger: at the verse-pair scale the naẓm signal is unambiguous
(Z=+18.70) where the seam signal was faint (k=3 directional, k=5 significant).
Coherence is densest at the finest granularity, exactly the prediction of the
scale-of-aggregation law (cross-finding-025/026).

## H2 — which surahs are naẓm-tight, which are anthology-like (the prize)

### NAZM-TIGHT roster (33 surahs, Bonferroni PASS at α=4.50×10⁻⁴)

The verse-order of these surahs is significantly MORE adjacent-cohesive than
chance — al-Biqāʿī's ordered-naẓm in its strongest individual form:

> **Q 2 al-Baqara (z=+10.73)**, Q 7 al-Aʿrāf (+9.58), Q 4 al-Nisāʾ (+9.09),
> Q 12 Yūsuf (+8.99), Q 28 al-Qaṣaṣ (+7.55), Q 5 al-Māʾida (+7.47),
> Q 74 al-Muddaththir (+7.18), Q 16 al-Naḥl (+7.13), Q 11 Hūd (+6.45),
> Q 23 al-Muʾminūn (+6.43), Q 15 al-Ḥijr (+6.39), Q 6 al-Anʿām (+6.29),
> Q 39 al-Zumar (+6.21), Q 69 al-Ḥāqqa (+6.11), Q 9 al-Tawba (+6.05),
> Q 3 Āl ʿImrān (+6.00), Q 20 Ṭāhā (+5.96), Q 78 al-Nabaʾ (+5.93),
> Q 58 al-Mujādila (+5.85), Q 10 Yūnus (+5.37), Q 51 al-Dhāriyāt (+5.29),
> Q 27 al-Naml (+5.26), Q 67 al-Mulk (+5.22), Q 29 al-ʿAnkabūt (+5.20),
> Q 70 al-Maʿārij (+5.07), Q 56 al-Wāqiʿa (+5.02), Q 40 Ghāfir (+4.84),
> Q 30 al-Rūm (+4.51), Q 38 Ṣād (+4.36), Q 8 al-Anfāl (+4.22),
> Q 24 al-Nūr (+4.20), Q 25 al-Furqān (+4.17), Q 43 al-Zukhruf (+3.84).

These are predominantly the **long sustained-discourse and continuous-narrative
surahs**: the seven ṭiwāl (Q 2, 3, 4, 5, 6, 7, 9), the great prophet-narrative
surahs (Q 12 Yūsuf — the single most continuous narrative in the Quran — Q 28,
Q 11, Q 20, Q 27), and the argument-driven Meccan discourses (Q 16, 23, 39, 40).
The pattern matches the classical intuition: where a surah develops a *connected
argument or story*, neighbouring verses recycle the same lexicon, and the
canonical order keeps that lexicon adjacent.

### LOOSE / anthology-like roster (33 surahs, z>0 but not Bonferroni)

These surahs are **shuffle-indistinguishable** — their canonical verse-order is
no more adjacent-cohesive than a random ordering of the same verses. Notably this
includes Q 1 al-Fātiḥa (z=+0.72), the muʿawwidhatān Q 113/114, Q 109 al-Kāfirūn,
and — strikingly — **Q 37 al-Ṣaffāt (L=182, z=+0.45)**, a *very long* surah that
is nonetheless loose. al-Ṣaffāt is a fast-moving chain of short rhyming
narrative verses with sparse, rapidly-turning vocabulary; length does not buy
adjacency-cohesion. Most loose surahs are short Meccan units (mean L=27.8) whose
verses are aphoristic and lexically self-contained — closer to al-Biqāʿī's
"verse-bag" pole, where each āya stands alone.

### REVERSED / dispersion (14 surahs; only one is significant)

Fourteen eligible surahs have z<0 (canonical order LESS cohesive than shuffle).
Thirteen of them sit at |z|<1.3 — statistically null, just sampling noise around
zero. **One is a genuine, strong reversal — and it is the most interesting single
finding in this study:**

> **Q 55 al-Raḥmān — z = −5.32 — the refrain-DISPERSED surah.**

al-Raḥmān contains the corpus's most famous refrain,
*fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* ("which of your Lord's favours will you
two deny?"), which on QAC roots is the set `{rbb, Alw, k*b}` and recurs in **31
of the surah's 78 verses**. In the CANONICAL order, **zero** of those 31 refrain
verses are adjacent to each other — the refrain is *interleaved* between the
thematic descriptions of God's favours, a deliberate **spacing** device. The
within-surah shuffle, by contrast, randomly clumps refrains together (and two
adjacent refrain verses have Jaccard = 1.0), so the *shuffle* mean (0.1695) is
far ABOVE the canonical mean (0.0235). al-Raḥmān is therefore the one surah whose
verse-order is significantly **anti-adjacent by design**: its naẓm is a *rhythm
of dispersion*, not of clustering. This is not a failure of al-Biqāʿī's thesis —
it is a different ordering principle (refrain-as-punctuation) that the
adjacency-cohesion instrument correctly flags as the structural opposite of the
narrative surahs. It converges with **H-NEW-2310** (refrain-spacing regularity):
the Quran's refrains are placed to *space*, not to *bunch*.

## Is naẓm-tightness correlated with length, region, or genre?

- **Length — POWER, not bigger effect.** z_surah correlates ρ_Spearman = **0.647**
  with surah length. But this is overwhelmingly a *statistical-power* artifact,
  not "long surahs have tighter naẓm": the **relative effect-size**
  (A_obs−null)/null correlates only ρ = **0.129** with length. Long surahs have
  more verse-pairs → a tighter null → more power to detect the *same-size* effect.
  The naẓm effect itself is roughly length-independent. Q 37 al-Ṣaffāt (L=182,
  loose) is the clean counterexample to a naive length reading.
- **Region — essentially flat.** mean z = **+2.89** Meccan (n=84) vs **+2.69**
  Medinan (n=27): no meaningful regional difference. Naẓm-tightness is not a
  Meccan/Medinan signature. (Both rosters split ~3:1 Meccan:Medinan, mirroring
  the corpus.)
- **Chronology — weak.** z_surah vs Nöldeke revelation order ρ = **+0.189**
  (weak positive; descriptive only, MW-7 capped).
- **Genre is the real driver.** The tight roster is *continuous narrative /
  sustained legal-discourse* (Yūsuf, al-Baqara, the ṭiwāl); the loose roster is
  *aphoristic short Meccan* + the *anthology-opener* Q 1; the lone strong
  reversal is *refrain-structured* (al-Raḥmān). Naẓm-tightness tracks **discourse
  type**, not length, region, or date.

**Orthogonal to UAS.** Of the UAS top-10 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17),
Q 2/9/24/12/10/23 are naẓm-TIGHT, Q 33/17 are tight-raw-only, **Q 1 is loose**,
and **Q 55 is the strong reversal**. Architectural-significance (UAS) and
sequential-naẓm-tightness are different axes: a surah can be a corpus hub (high
UAS) while being adjacency-loose (Q 1) or adjacency-anti (Q 55).

## Honest limits

1. **Root-Jaccard is lexical only.** It cannot see pronominal continuity,
   connective particles, syntactic hand-offs, or thematic flow without shared
   roots. al-Biqāʿī's naẓm is broader than shared lexis; this test bounds the
   *shared-root adjacency* component. The 33 "loose" surahs may still have strong
   non-lexical naẓm invisible to this instrument — the NULL here is "no
   shared-root adjacency signal," not "no coherence."
2. **The length–z correlation is a power confound**, explicitly disentangled
   above (effect-size ρ=0.13 vs z ρ=0.65). z-magnitude must NOT be read as
   "degree of naẓm"; it is "detectability of naẓm."
3. **High-frequency function-bearing roots** (Alh=Allāh, qwl=say, kwn=be) inflate
   Jaccard, but the within-surah shuffle reuses the SAME verse-root-sets, so this
   is fully controlled — the null verses carry the identical high-frequency roots.
4. **Short surahs are low-power**; many "loose" verdicts for short Meccan surahs
   are non-rejections, not evidence of incoherence. The 3 L<4 surahs are excluded
   (their shuffle null cannot resolve Bonferroni — confirmed: 1–2 distinct means).
5. **Q 55's reversal is real but is an ordering-PRINCIPLE difference**, not a
   defect: it is the signature of refrain-as-spacing, corroborated by H-NEW-2310.
6. No claim about *revelation order*, *authorship*, or *causation*; only that the
   canonical verse-sequence is more shared-root-adjacent than a random
   re-ordering of the same verses.

## Cross-references

- **H-NEW-2280** (al-Biqāʿī seam, BETWEEN surahs): this is the WITHIN-surah
  complement. Together they bound al-Biqāʿī's munāsaba doctrine at both scales —
  faint-but-real at the inter-surah seam (k=5 z=+2.89), strong at the
  intra-surah verse pair (Z=+18.70). The two halves of *Naẓm al-durar* both leave
  a shared-root trace; the within-surah one is far the stronger.
- **cross-finding-025 / cross-finding-026** (scale-of-aggregation law; cohesion-
  vs-chiasmus bifurcation): H-NEW-2420 is a clean confirmation of the COHESION
  arm — distributional cohesion is densest at the finest scale (verse pair). It is
  NOT a chiasmus claim (no positional mirror is tested), so it does not touch the
  anti-chiastic arm (H-NEW-2220/2290).
- **H-NEW-2330** (lexical burstiness): the mechanism. Topical roots clump within a
  surah; the canonical order places the clumps adjacently, which is exactly what
  this test measures. Burstiness is the lexical substrate; adjacency-cohesion is
  its sequential expression.
- **H-NEW-2310** (refrain-spacing regularity): explains the Q 55 al-Raḥmān
  reversal — refrains are placed to SPACE, producing anti-adjacency.
- **H-NEW-840** (UAS): naẓm-tightness is empirically ORTHOGONAL to UAS (Q 1 loose,
  Q 55 reversed despite top-10 UAS).
- **INVESTIGATION-PROTOCOL §3.7**: this does NOT rehabilitate the four FALSIFIED
  al-Biqāʿī *whole-surah muqaṭṭaʿāt-content* munāsabas; different claim
  (verse-sequence), different scale (adjacent pairs), and it PASSES where the
  whole-surah letter-cluster claim NULLed.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2420-within-surah-nazm.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2420.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2420.json`
- This finding: `findings/phase-b-hypotheses/h-new-2420-within-surah-nazm.md`

*Tested verse-by-verse, where al-Biqāʿī located the within-surah claim. The
Quran is an ordered naẓm, not a random verse-bag; al-Raḥmān orders by dispersion,
not adjacency. Verdict honest. Bismillāhi al-Raḥmāni al-Raḥīm. — Waiel
Al-Shujaa, 2026-05-29.*
