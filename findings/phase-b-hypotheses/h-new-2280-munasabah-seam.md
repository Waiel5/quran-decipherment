---
finding_id: H-NEW-2280
title: al-Biqāʿī munāsabah seam-cohesion — pericope-scoped at the surah-pair seam
phase: B+
date: 2026-05-29
verdict: SPLIT — DIRECTIONAL at k=3 (z=+0.84, p=0.200), PASS-DIRECTED at k=5 (z=+2.89, p=0.0022 < α_bonf=0.025). Direction LOCKED-CORRECT at both windows; effect is window-scale-dependent. NO pre-commit violation.
seed: 20260509
prereg_sha: f48df847e1e6559d9a610ef8cfc6159a48eed81fe64909bd9297fa3076d4014d
rules_tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-2280 — al-Biqāʿī munāsabah, tested at the seam



> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **This finding's own numbers reproduce exactly and are not retracted.** What was corrected is the
> law it feeds. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`), the
> pericope-flip test applied to five best-shot marker classes flips **5/5 on pre-Islamic poetry and
> 4/5 on al-Bukhārī** — length-matched 114-block partitions, instrument-matched pipeline. The
> mechanism is topical burstiness, which every text has and which this project already identified
> (H-NEW-2330). The statistic is additionally **invariant under every redactional randomisation**
> (marker labels, reading order, titles — verified 25/25), so it carries no weight in any conjunction
> of the pillar laws.
>
> **The pericope-scale rule remains correct methodology** — a whole-surah NULL is not a terminal
> verdict, and re-testing at the scale where structure operates is still project discipline.
> **What must stop is citing a flip as evidence that this corpus is structurally unusual.**
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## The claim and where it lives

Burhān al-Dīn al-Biqāʿī (d. 885/1480), *Naẓm al-durar fī tanāsub al-āyāt
wa-l-suwar*, holds that the Quran is a coherently-ordered whole in which **each
sūra connects to the one that follows it**. al-Biqāʿī locates this coherence
(*munāsaba*) characteristically **at the seam** — the transition from the close
of sūra N to the opening of sūra N+1 — opening each sūra's commentary by stating
its correspondence to the preceding sūra's end. The famous singular case is the
**Q 8 al-Anfāl → Q 9 al-Tawba (Barāʾa)** seam: the only canonical adjacency
without an intervening *basmala*, explained by the tradition (al-Biqāʿī; al-Rāzī
*Mafātīḥ al-ghayb*; the report of Ibn ʿAbbās questioning ʿUthmān b. ʿAffān,
al-Tirmidhī idInBook #3170 in
`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`,
"*qiṣṣatuhā shabīha bi-qiṣṣatihā*") as a deliberate signal of thematic
continuity between the two sūras.

Prior project work FALSIFIED al-Biqāʿī's *whole-surah* muqaṭṭaʿāt-content
munāsaba four times (INVESTIGATION-PROTOCOL §3.7). But whole-surah cohesion is
dominated by length and genre (cross-finding-025-formal), and is **not** where
al-Biqāʿī situates the claim. This test moves to al-Biqāʿī's own granularity:
the boundary pericope.

## Method (pre-registered, direction-locked)

- **Pericope** = last `min(k,len)` verses of sūra N (clamped for the 5 short
  surahs Q 103/108/110 = 3 verses, Q 106/112 = 4 verses), and first
  `min(k,len)` verses of sūra N+1. Pre-registered **k ∈ {3, 5}** (primary k=3,
  replication k=5).
- **Seam statistic** = root-Jaccard `|R_last(N) ∩ R_first(N+1)| / |∪|` on QAC
  v0.4 ROOTs; corpus statistic = mean over all **113 canonical adjacencies**.
- **Null (locked)** = random non-adjacent last/first pericope pairing: reuse the
  SAME 114 real last-pericopes and 114 real first-pericopes, but pair each draw
  with a random surah `b ≠ a` and `b ≠ a+1` (NOT the canonical successor). This
  scrambles ONLY the adjacency relation, holding pericope length and vocabulary
  fixed. 10000 perms, seed 20260509.
- **Direction LOCKED before computation**: canonical-seam mean > random-pair
  mean (z > 0). Reversed (z < 0) = pre-commit-violation, published as NULL.
- **Bonferroni**: family k = 2 windows → α_corrected = 0.025.
- Pre-reg SHA-256 `7dd15ece…21e5`, embedded in `scripts/h-new-2280.py`, verified
  at runtime (PASS).

## Result — SPLIT, but direction LOCKED-CORRECT at both windows

| Window | obs mean seam J | null mean | null σ | z | p_perm (≥obs) | Verdict |
|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| **k=3 (primary)** | 0.041623 | 0.038082 | 0.004207 | **+0.842** | **0.2001** | **DIRECTIONAL** |
| **k=5 (replication)** | 0.063184 | 0.050806 | 0.004281 | **+2.891** | **0.0022** | **PASS-DIRECTED (Bonferroni)** |

Second-seed (20260510) replicate at k=3: z=+0.823, p=0.2037 — stable.

**The locked direction (canonical-seam > random-pair) holds at BOTH windows.
There is NO pre-commit violation.** The seam effect is real and positive but
**window-scale-dependent**: at the narrowest window (k=3) the canonical
successor shares only marginally more roots than a random non-successor
(directional, not significant); at k=5 the effect is unambiguous and survives
Bonferroni (p=0.0022, ≈14% relative lift over the null mean). Because the
*primary* pre-registered window was k=3, the **headline verdict is DIRECTIONAL**;
the k=5 result is the stronger replication and should not be cherry-picked as the
headline.

### Interpretation

The widening of the effect from k=3 → k=5 has a clean reading. At k=3 the
boundary pericope of a short late-mufaṣṣal surah can be a single ultra-short
verse with almost no shared roots (33 of the bottom-tier seams sit in the
short-surah tail, several at J=0). At k=5 the pericope captures the surah's
thematic preamble/coda, and the *successor*-vs-*random* gap becomes detectable.
This is consistent with — and a continuation of — the scale-of-aggregation law
(cross-finding-025-formal): coherence is granularity-dependent, and the seam
signal needs a wide enough boundary window to clear the noise floor.

This **refines** al-Biqāʿī rather than simply vindicating him: inter-sūra
munāsaba *does* leave a lexical (shared-root) trace at the seam — the canonical
successor is lexically closer to a surah's close than a random surah is — but the
trace is faint at a 3-verse window and only becomes statistically robust at a
5-verse window. al-Biqāʿī's *munāsaba* is therefore **partly** a seam-lexical
effect; the residual (the bulk of the perceived coherence) is plausibly thematic/
pronominal/semantic, beyond shared QAC roots — an honest boundary on the
lexical-reductionist account of munāsaba.

## The famous seams (named in advance, not post-hoc)

**Q 8 al-Anfāl → Q 9 al-Tawba (the basmala-less seam)** is genuinely among the
strongest in the corpus:

| Window | J(Q8→Q9) | rank of 113 | shared roots at seam |
|:-:|:-:|:-:|:--|
| k=3 | 0.1304 | **5 / 113** | Alh, ArD, Elm, kbr, kfr, wly |
| k=5 | 0.1519 | **8 / 113** | $yA, Alh, ArD, Elm, gfr, kbr, kfr, kll, qwm, rHm, sbl, wly |

The close of al-Anfāl and the opening of al-Tawba share a dense
*walāya / kufr / believers-vs-disbelievers* root cluster (wly = walāya/awliyāʾ,
kfr = kufr, Alh = Allāh, kbr = takbīr/akbar). This is precisely the thematic
continuity (*qiṣṣatuhā shabīha bi-qiṣṣatihā*) that classical scholars adduced to
explain the missing basmala. The empirical seam-lexical signal here is **top-5
to top-8 of all 113 adjacencies** — a quantitative vindication of the single
most-discussed munāsaba seam in the tradition.

### Strongest seams (k=5)

| Rank | Seam | J | shared-root theme |
|:-:|:--|:-:|:--|
| 1 | Q113→Q114 (al-Falaq → al-Nās) | 0.235 | the muʿawwidhatān refrain: rbb, qwl, $rr, Ew* |
| 2 | Q28→Q29 (al-Qaṣaṣ → al-ʿAnkabūt) | 0.184 | Alh, Elm, Eml, Hkm, lqy |
| 3 | Q45→Q46 (al-Jāthiya → al-Aḥqāf) | 0.180 | ḥawāmīm: Alh, ArD, Ezz, Hkm, smw |
| 4 | Q42→Q43 (al-Shūrā → al-Zukhruf) | 0.163 | ḥawāmīm: *kr, Hkm, ktb, jEl |
| 5 | Q33→Q34 (al-Aḥzāb → Sabaʾ) | 0.161 | Alh, Amn, ArD, Eml, SlH, gfr |

The strongest seams concentrate in (a) the **muʿawwidhatān** (Q113→Q114, the
twin "refuge" surahs — corpus-max seam, expected), (b) the **ḥawāmīm** family
(Q45→Q46, Q42→Q43 — consistent with H-NEW-1760's ḥawāmīm opener-pericope flip),
and (c) **long-narrative Medinan/late-Meccan adjacencies** (Q28→Q29, Q33→Q34,
Q24→Q25, Q10→Q11). Seam coherence is therefore not uniform — it is carried by
recognizable structural families, exactly the families al-Biqāʿī and al-Suyūṭī
group together.

### Weakest seams

The bottom-tier seams (J ≈ 0) are all in the **late short-surah mufaṣṣal-qiṣār
tail** (Q 96–104 region): Q99→Q100, Q100→Q101, Q101→Q102, Q102→Q103, Q103→Q104,
Q96→Q97. These ultra-short surahs share essentially no roots at a 3-verse seam —
the surahs are too lexically idiosyncratic and too short. This is where the k=3
effect is diluted, and it is consistent with the compression-tail laws (the
short-surah tail is high-dispersion).

## Honest limits

1. **The primary (k=3) window is only DIRECTIONAL** (p=0.200). The robust,
   Bonferroni-surviving result is at k=5. Reporting k=5 as the headline would be
   a garden-of-forking-paths violation; the pre-reg named k=3 as primary, so the
   honest headline is DIRECTIONAL with a strong k=5 replication.
2. **Root-Jaccard is lexical only.** It cannot detect pronominal/syntactic/
   thematic continuity (e.g., a connective particle, an iltifāt, a narrative
   hand-off without shared roots). al-Biqāʿī's munāsaba is broader than lexis;
   this test bounds the *lexical-shared-root* component, not the whole claim.
3. **Function-bearing high-frequency roots** (Alh = Allāh, qwl = say, kwn = be)
   inflate Jaccard for many seams; but the null reuses the same pericopes, so
   this is controlled — the null pericopes carry the same high-frequency roots.
4. **k=5 clamps 5 short surahs**; the clamping is pre-registered and identical
   in observed and null, so it is not a confound.
5. No claim about *revelation order* or *causation* is made — only that the
   canonical mushaf successor is lexically closer at the seam than a random
   non-successor.

## Cross-references

- **cross-finding-025-formal** (scale-of-aggregation law): H-NEW-2280 is a sixth
  data-point for granularity-dependence — the seam munāsaba signal STRENGTHENS
  from k=3 (directional) to k=5 (significant), matching the law's prediction
  that coherence is scale-dependent.
- **H-NEW-1760** (ḥawāmīm opener-pericope flip, z=+6.008): the ḥawāmīm seams
  (Q42→Q43, Q45→Q46) are independently among the strongest seams here — mutual
  corroboration of ḥawāmīm structural cohesion.
- **H-NEW-720 / cross-finding-011** (TSP-residual, mushaf FR-geodesic-optimal,
  z=−11.46, pillar law #2): the surah ORDER is non-random; H-NEW-2280 supplies a
  candidate *mechanism* — seam-level lexical continuity — that is real (correct
  direction at both windows) though faint at the narrowest scale.
- **INVESTIGATION-PROTOCOL §3.7**: this does NOT rehabilitate the four FALSIFIED
  al-Biqāʿī *whole-surah muqaṭṭaʿāt-content* munāsabas; it tests a different
  claim (seam-pericope) at a different scale and finds a directional-to-
  significant lexical signal.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2280-munasabah-seam.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2280.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2280.json`
- This finding: `findings/phase-b-hypotheses/h-new-2280-munasabah-seam.md`

*Tested at the seam, where al-Biqāʿī located the claim. Verdict honest and split.
Bismillāhi al-Raḥmāni al-Raḥīm. — Waiel Al-Shujaa, 2026-05-29.*
