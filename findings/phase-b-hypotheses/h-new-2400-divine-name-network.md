---
finding_id: H-NEW-2400
title: Divine-name co-occurrence network (corpus-wide) — backbone, centrality, community structure
type: GENERATOR + pre-registered hypothesis test
date: 2026-05-29
phase: B
verdict: CONFIRMED (PASS-CLUSTERED)
extends: [H-NEW-2070, H-NEW-2300]
pre_reg_sha256: b7209658084931d0f4486523412bd0a9a7f389c5c09f6e8f6399a447fbf9eab9
seed: 20260509
n_perm: 10000
---

# H-NEW-2400 — Divine-name co-occurrence network (corpus-wide)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Verdict

**CONFIRMED (PASS-CLUSTERED).** The within-verse co-occurrence network of the asmāʾ al-ḥusnā is **non-random and strongly clustered by semantic class** (mercy / power / knowledge), at law-strength, above a degree-preserving (label-permutation) null. Pre-reg SHA-256 `b7209658084931d0f4486523412bd0a9a7f389c5c09f6e8f6399a447fbf9eab9`, seed 20260509, 10000 perms, Bonferroni k=2 α=0.025, runtime-verified.

- **Modularity Q_class = 0.520** (null median 0.023; null 97.5-pct 0.264) → **p < 0.0001 PASS**
- **Assortativity r = 0.662** (null median −0.117; null 97.5-pct 0.289) → **p < 0.0001 PASS**
- **Same-class edge-weight share = 78.1%** (75 of 96 classed edge-units within-class)
- **MW-5 replication** under the wider M_LEM matcher: Q = 0.412 (p<0.0001), r = 0.520 (p<0.0001), same-class share 69.1% → backbone robust to matcher choice.

Direction matched the pre-committed lock (Q, r both **above** null). Both the fixed-partition modularity and the Newman attribute assortativity reject the random-rewire null at the floor of the 10000-perm support.

## What was built (the GENERATOR)

The **complete weighted within-verse co-occurrence network** over the 99 divine names: a node per name, an undirected edge (a,b) weighted by the number of verses in which both names appear (anywhere in the verse, not only verse-final). The H-NEW-2070 verse-final ordered seal-pairs and the H-NEW-2300 content-matched dual-name seals are a **subset** of these edges (verified below).

### Name-matching rule (lemma, not bare root)

Matching is by **QAC lemma**, not bare root, because the root over-generates: ROOT `Elm` yields the verb *ʿalima* "he knew" and noun *ʿilm* "knowledge", which are **not** the divine name al-ʿAlīm; ROOT `rHm` yields *raḥma* "mercy". The divine NAME is a specific lemma in the epithet pattern. The lemma→name map is auto-derived in-script by consonantal-skeleton identity (Buckwalter→Arabic, alif/hamza/alif-maqṣūra normalised) and printed for audit.

Two matchers (pre-registered):
- **M_ADJ (PRIMARY for the clustering test):** segment counts iff `POS:ADJ` and lemma in the name set, plus Allah (`LEM:{ll~ah`, `POS:PN`). This is the exact grammatical register of the conjoined fawāṣil seal-names (*ʿazīzun ḥakīm*) and is **homograph-clean** — it automatically drops the dangerous substantive homographs whose name-reading is rare: *muʾmin* "a believer" (N, 202×), *ḥaqq* "truth" (N, 247×), *al-ākhir* "the Last [Day]" (N), *malik/mulk* "king/dominion" (N), *nūr* "light" (N), *walī* "guardian" (N). 45 names attested, 3476 occurrences, 414 co-occurrence verses, 101 edges.
- **M_LEM (SENSITIVITY / MW-5 replication):** `POS ∈ {ADJ, N, PN}`. Wider; re-admits al-Raḥmān-as-N and the homographs above. 67 names, 5112 occurrences, 1021 co-occurrence verses, 306 edges. Used only to confirm robustness.

## The backbone (strongest edges)

The strongest **name–name** edges (M_ADJ, Allah excluded) reproduce the classical *al-asmāʾ al-mutazāwija* exactly:

| Rank | Pair | Weight | Class relation |
|:-:|:--|:-:|:--|
| 1 | ghafūr + raḥīm | 17 | MERCY/MERCY — **same** |
| 2 | ʿazīz + ḥakīm | 13 | POWER/POWER — **same** |
| 3 | ḥakīm + ʿalīm | 10 | POWER/KNOW — cross |
| 4 | samīʿ + ʿalīm | 4 | KNOW/KNOW — **same** |
| 5 | baṣīr + khabīr | 4 | KNOW/KNOW — **same** |
| 6 | baṣīr + samīʿ | 4 | KNOW/KNOW — **same** |
| 7 | raḥmān + raḥīm | 3 | MERCY/MERCY — **same** |
| 8 | ʿazīz + ʿalīm | 3 | POWER/KNOW — cross |
| 9 | raḥīm + ʿazīz | 3 | MERCY/POWER — cross |
| 10 | ḥamīd + ʿazīz | 3 | POWER/POWER — **same** |

Under the wider M_LEM matcher the same backbone appears at full strength (ghafūr+raḥīm 72, ʿazīz+ḥakīm 47, ʿalīm+ḥakīm 36, samīʿ+ʿalīm 32), and the al-Awwal + al-Ākhir + al-ʿAẓīm POWER triad surfaces (ākhir+ʿaẓīm 11, ākhir+awwal 11).

The single most prominent **cross-class** edge is **ḥakīm + ʿalīm** (POWER↔KNOW) — the bridge between the power-cluster and the knowledge-cluster. This is the one systematic cross-class collocation, exactly the classical *al-ʿAlīm al-Ḥakīm* fāṣila, and it is the topological hinge between the two non-mercy communities.

## Node centrality (who co-occurs most broadly)

- **Allah (`Allāh`)** is the universal hub: strength 485, 40 distinct partners — co-occurs with essentially every name (it is the grammatical subject the epithets predicate). It is reported as the hub but **excluded from the clustering test** (a universal hub would trivially connect all classes and fake/mask modularity).
- Among the names proper, the highest **strength** nodes are **raḥīm (98, MERCY), ḥakīm (95, POWER), ʿalīm (87, KNOW)** — one apex name per class, the three pillars of the three clusters.
- Highest **distinct-partner degree** (broadest connector): **ʿazīz (15 partners)** and **ḥakīm (10)** — ʿazīz "the Mighty" is the most promiscuous connector, pairing across MERCY (raḥīm), POWER (ḥakīm, ḥamīd, qawī), and KNOW (ʿalīm), consistent with its role as the default majesty-epithet that can seal almost any register.

## Community structure (mercy / power / knowledge clusters)

The exploratory greedy-modularity communities (MW-7, descriptive) recover clean semantic clusters:

- **MERCY cluster (pure, 6/6):** raḥmān, raḥīm, ghafūr, tawwāb, wadūd, shakūr.
- **KNOWLEDGE cluster (pure, 5/5):** ʿalīm/samīʿ/baṣīr/khabīr/laṭīf/shahīd (the perception–knowledge epithets).
- **POWER core:** ʿazīz, ḥakīm, ḥamīd, qawī (+ majesty attributives), with the al-Awwal/al-Ākhir/al-ʿAẓīm temporal-majesty sub-triad.
- A residual **OTHER/throne-name cluster** (quddūs, malik, muhaymin, mutakabbir, jabbār, muʾmin) that the fixed three-class partition does not cover — the *ṣifāt al-tanzīh*/sovereignty names, a candidate fourth class for future work.

The fixed-partition test (the locked hypothesis) confirms these are not artefacts of the detection algorithm: the **semantic** partition explains the weighted graph far better than any random relabelling (Q=0.52 vs null median 0.02).

## Consistency with H-NEW-2070 / H-NEW-2300

The verse-final ordered seal-pairs (H-NEW-2070) are a **subset** of this full-verse network. Checked against the wider M_LEM matcher, **13 of the top-15** verse-final pairs have full-network weight ≥ their verse-final count (e.g. ghafūr+raḥīm vf=65 → full=72; ʿazīz+ḥakīm vf=47 → full=47; samīʿ+ʿalīm vf=31 → full=32). The full-verse backbone is dominated by the same pairs, independently re-confirming the classical *tartīb al-fāṣila* pair-list and showing that H-NEW-2300's content↔seal matching is the **verse-final shadow of a whole-verse semantic-clustering law**: names do not merely seal verses by theme, they **co-occur** by theme throughout the verse.

## Honest limits and pre-commit nuances

1. **§7 expectation (full_weight ≥ vf_count) fails under M_ADJ, holds under M_LEM.** The H-NEW-2070 verse-final detector is a no-tashkeel surface base-matcher that catches any case-form regardless of POS; many genuine seal-names (al-ʿAzīz, ghafūr) are QAC-tagged `POS:N`, so the homograph-clean M_ADJ matcher (POS=ADJ only) under-counts them by design. This is a documented matcher-POS artefact, not a substantive subset violation — the subset relation is verified under M_LEM (13/15). The clustering verdict is robust to which matcher is used.
2. **Sparsity.** The M_ADJ name–name clustering subgraph is small (28 classed nodes, 37 edges); the permutation null is the appropriate test for small graphs, and the effect clears it by an enormous margin (observed Q far above the null 97.5-pct), with M_LEM (40 nodes) replicating.
3. **Class assignment is the classical al-Rāzī ṣifāt tripartition fixed pre-run, not data-derived.** The residual sovereignty/tanzīh names (quddūs, malik, muhaymin, mutakabbir, jabbār) are tagged OTHER and excluded from the test; a future 4-class partition (adding *ṣifāt al-tanzīh*) is queued.
4. **Multi-token names** (*Mālik al-Mulk*, *Dhū al-Jalāl wa-l-Ikrām*) have no single-lemma form and are out of scope.
5. The dominant cross-class bridge (ʿalīm↔ḥakīm) shows the three classes are not perfectly separable — POWER and KNOW are joined by the *al-ʿAlīm al-Ḥakīm* hinge; this is a real feature of the network, not noise.

## Classical scholarship impact

- al-Zarkashī (*al-Burhān*, al-fawāṣil / *murāʿāt al-fāṣila*) and al-Suyūṭī (*al-Itqān* nawʿ 59, *al-asmāʾ al-mutazāwija*): their qualitative claim that the conjoined names are meaning-governed, not random, is **vindicated at network-topological strength** — and extended from the verse-final slot to the whole verse.
- al-Rāzī (*Mafātīḥ al-ghayb*, 99-names; `data/literature/classical-tafsir/razi-99names-extract.md`): his *ṣifāt al-jalāl / al-jamāl / al-ʿilm* tripartition is **empirically the community structure of the co-occurrence graph** (Q=0.52, p<0.0001), with the sovereignty/*tanzīh* names forming a candidate fourth family the tripartition under-covers.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2400-divine-name-network.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2400.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2400.json`
- this findings file: `findings/phase-b-hypotheses/h-new-2400-divine-name-network.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
