---
finding_id: H-NEW-2400
title: Divine-name co-occurrence network (corpus-wide) — backbone, centrality, community structure
type: GENERATOR + pre-registered hypothesis test
date_registered: 2026-05-29
phase: B
status: LOCKED-PRE-OBSERVATION
extends: H-NEW-2070 (verse-final ordered pairs), H-NEW-2300 (content-matched dual-name seals)
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

## 0. One-paragraph statement

H-NEW-2070 enumerated the **verse-final** divine-name *ordered bigram* grammar (54 ordered seal-pairs; *ghafūr+raḥīm*, *ʿazīz+ḥakīm*, *samīʿ+ʿalīm* dominant). H-NEW-2300 showed the verse-final seal-pair is **content-matched** to the verse meaning along a MERCY/POWER/KNOW super-class axis. Those verse-final pairs are a **subset** of the full set of within-verse name co-occurrences. This finding builds the **complete weighted within-verse co-occurrence network** over the 99 asmāʾ al-ḥusnā — every pair of distinct names appearing in the same verse (not only verse-final) — and asks one locked structural question: **is the co-occurrence network non-randomly CLUSTERED by semantic class** (mercy / power / knowledge), above a degree-preserving random-rewire null?

## 1. Classical anchor

- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil (*murāʿāt al-fāṣila* — the closing word/name is chosen to suit the āya's meaning); al-Zarkashī treats the paired divine names as a *naẓm* device.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 59 (*fawāṣil*); his discussion of *al-asmāʾ al-mutazāwija* (the conjoined-name endings, e.g. *al-ʿAzīz al-Ḥakīm*).
- al-Bāqillānī, *Iʿjāz al-Qurʾān* — the governed cadence of the fawāṣil.
- al-Rāzī, *Mafātīḥ al-ghayb* — the 99-names discussion grouping the names into *ṣifāt al-jalāl* (majesty/power) vs *ṣifāt al-jamāl/al-iḥsān* (beauty/mercy) vs the *ṣifāt al-ʿilm* (knowledge) (file: `data/literature/classical-tafsir/razi-99names-extract.md`).
- The *ṣifāt al-jalāl / ṣifāt al-jamāl* binary is the classical theological partition this test operationalises as MERCY (jamāl/iḥsān) vs POWER (jalāl) with KNOWLEDGE as a third epistemic class.

The classical claim, stated empirically: the conjoined / co-occurring divine names are **not** assembled at random but cluster by attribute-family, and the paired endings respect meaning. H-NEW-2400 tests the *network-topological* form of this claim across the whole verse (not just the seal slot).

## 2. Data sources (all on disk)

- `data/asma-al-husna.txt` — 99 names (al-Walīd b. Muslim via al-Tirmidhī #3507; 97 single-token + 2 multi-token *Mālik al-Mulk*, *Dhū al-Jalāl wa-l-Ikrām*).
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4; LEM (Buckwalter lemma) + POS + ROOT per segment. **This is the primary matcher source** (per task: "match the divine names via root/lemma").
- `quran-text/quran-no-tashkeel.json` — verse text, for cross-validation of the verse-final subset (the H-NEW-2070/2300 surface detector).

## 3. Name-matching rule (LOCKED) — lemma-confirmed, not bare-root

**Why lemma, not root.** The bare root over-generates: ROOT `Elm` yields the *verb* `Ealima` (he knew) and *noun* `Eilm` (knowledge), which are **not** the divine name al-ʿAlīm; ROOT `rHm` yields `raHomap` (mercy, the noun). The divine NAME is a specific **lemma** in a specific morphological pattern. Bare-root matching would conflate attribute-words with the names and inflate every node. **Matching is therefore by QAC LEMMA.**

**Lemma→name map (auto-derived, deterministic, in-script):** for each of the 97 single-token al-Tirmidhī names, strip the article `ال`, take its consonantal skeleton (alif/hamza/alif-maqṣūra normalised). For every QAC lemma, transliterate Buckwalter→Arabic consonantal skeleton; a lemma maps to a name iff skeletons are identical **and** the segment's QAC POS is `ADJ` (the attributive epithet register). Allah is matched as `LEM:{ll~ah` with `POS:PN`. The map is printed by the script for audit. Multi-token names (*Mālik al-Mulk*, *Dhū al-Jalāl wa-l-Ikrām*) are out of scope (no single-lemma form).

**PRIMARY matcher M_ADJ (LOCKED):** a token is a divine-name occurrence iff `POS:ADJ` and `LEM` is in the auto-derived name-lemma set, **plus** Allah (`LEM:{ll~ah`, `POS:PN`).
- **Rationale:** (i) `POS:ADJ` is the exact grammatical register of the conjoined fawāṣil seal-names (*ʿazīzun ḥakīm*, *ghafūrun raḥīm*) that H-NEW-2070/2300 enumerate — so the verse-final seal-pairs are provably a subset of this network, satisfying the task's consistency requirement; (ii) it carries **zero ad-hoc per-name exceptions**; (iii) it automatically excludes the dangerous homographs whose substantive reading dominates — *muʾmin* "a believer" (N, 202×), *ḥaqq* "truth" (N, 247×), *al-yawm al-ākhir* "the Last Day" / *al-awwalīn* (N), *malik/mulk* "king/dominion" (N), *nūr* "light" (N), *walī* "guardian" (N) — none of which are functioning as a name of God in the vast majority of attestations.
- **Known cost (honest):** M_ADJ drops names that occur in the Quran predominantly as substantives-used-as-names (al-Raḥmān is N 45× / ADJ 12×; al-Malik; al-Salām). These are recovered in the sensitivity matcher.

**SENSITIVITY matcher M_LEM (pre-registered, reported alongside):** `POS ∈ {ADJ, N, PN}` and `LEM` in the name-lemma set. Wider; re-includes al-Raḥmān-as-N etc. but re-admits the homographs above. Used only to confirm the **backbone edges are robust to matcher choice**; NOT the locked hypothesis test.

## 4. Network construction (LOCKED)

- **Nodes** = distinct attested divine names under the matcher.
- For each verse, take the **set** of distinct names present (multiset collapsed to set — a name appearing twice in a verse contributes one node-presence, no self-loop).
- **Edge weight** `w(a,b)` = number of verses in which names *a* and *b* both appear (undirected). The full verse-final ordered-pair multiset of H-NEW-2070 collapses into a subset of these undirected edges.
- **Degree / strength:** node strength `s(v)` = Σ_b w(v,b); node degree = number of distinct co-occurrence partners.
- **Allah handling:** Allah is a near-universal subject and co-occurs with almost every name; it is reported as the dominant-strength **hub** descriptively, but is **EXCLUDED from the modularity / clustering hypothesis test** (a universal hub trivially connects all classes and would mask or fake modularity). The clustering test runs on the name–name subgraph (Allah removed).

## 5. Semantic-class labelling (LOCKED) — for the clustering test

Each name node is assigned ONE of three super-classes, following al-Rāzī's *ṣifāt* tripartition operationalised in H-NEW-2300 (identical class map, extended to the wider node set). The class map is fixed in the script BEFORE the run and printed for audit:
- **MERCY** (*ṣifāt al-jamāl / al-iḥsān*): raḥmān, raḥīm, ghafūr, ghaffār, tawwāb, wadūd, ʿafū, raʾūf, barr, ḥalīm, shakūr, raʾūf, salām, karīm.
- **POWER** (*ṣifāt al-jalāl*): ʿazīz, ḥakīm, ḥakam, qahhār, jabbār, mutakabbir, kabīr, qadīr, qādir, muqtadir, ʿalī, mutaʿālī, ʿaẓīm, qawī, matīn, ḥamīd, majīd, malik, qayyūm, awwal, ākhir.
- **KNOW** (*ṣifāt al-ʿilm*): ʿalīm, samīʿ, baṣīr, khabīr, shahīd, ḥafīẓ, laṭīf, raqīb, ḥasīb, wakīl.
- Names not assignable to one of the three (e.g. quddūs, badīʿ as ontological) are tagged **OTHER** and excluded from the modularity test (kept in the descriptive network).

The class map is content-independent of the network; it is the classical theological partition, not derived from co-occurrence.

## 6. HYPOTHESIS (DIRECTION LOCKED)

**Pre-registered direction:** divine-name co-occurrence is **NON-random and CLUSTERED by semantic class** — names within the same class co-occur MORE than cross-class, i.e. the network's **class-assortativity / modularity is HIGHER than a degree-preserving random-rewire null**.

- **Primary statistic Q_class** = modularity of the observed weighted name–name graph under the **fixed semantic-class partition** (MERCY/POWER/KNOW), computed as
  Q = (1/2m) Σ_{ij} [ w_ij − k_i k_j / 2m ] δ(class_i, class_j)
  on the Allah-excluded, OTHER-excluded weighted subgraph (m = total edge weight, k = node strength).
- **Secondary statistic r_assort** = weighted attribute assortativity coefficient on the class labels (Newman 2003), same subgraph.
- **LOCKED direction:** observed Q_class and r_assort are **GREATER** than the null.

### Null model (LOCKED)
**Degree-preserving (strength-preserving) random rewire** of the weighted name–name graph: the configuration-model expectation k_i k_j / 2m is already the analytic null inside Q; for the permutation p-value we **shuffle the class labels across nodes** (preserve class-size marginals and the graph topology), recompute Q_class and r_assort, 10000 permutations, seed = 20260509. This is the standard degree-preserving test for "does THIS partition explain the graph better than chance" — it holds node strengths fixed (degree-preserving) and asks whether the *semantic* partition is special.

- **Bonferroni:** k = 2 cells (Q_class, r_assort) → α_corrected = 0.025.
- p_perm(Q) = fraction of permutations with Q_perm ≥ Q_obs; p_perm(r) likewise.

### Pre-registered verdict rule
- **CONFIRMED (PASS-CLUSTERED):** Q_obs and r_obs both above null median AND p_perm(Q) ≤ 0.025 AND p_perm(r) ≤ 0.025. → semantic clustering is real; network confirms classical attribute-family grouping; consistent with H-NEW-2300.
- **PARTIAL:** exactly one of Q/r passes at α=0.025.
- **NULL → PROMINENCE (reverse/formulaic):** Q_obs and r_obs **at or BELOW** null median. Reported with equal prominence. Interpretation: names pair by **rhyme/formula (fāṣila chassis)** not by theme — i.e. the co-occurrence backbone (ghafūr+raḥīm, ʿazīz+ḥakīm) is driven by the -īm/-īr/-īz assonance cadence (H-NEW-2240) and habitual collocation, NOT by semantic affinity. This would itself be a substantive finding (it would mean H-NEW-2300's content-matching is a verse-final-only effect that does NOT propagate to the full-verse network).

## 7. Consistency check vs H-NEW-2070 / H-NEW-2300 (descriptive, not hypothesis)

The script independently rebuilds the H-NEW-2070 verse-final ordered-pair detector (no-tashkeel surface base-match) and verifies that **every verse-final seal-pair edge is present in the full-verse co-occurrence network** with weight ≥ its verse-final count. Reports the overlap between the top-N full-network name–name edges and the H-NEW-2070 top-N seal-pairs. Expectation (NOT locked, descriptive): the full-verse backbone is dominated by the same pairs (ghafūr+raḥīm, ʿazīz+ḥakīm, ʿalīm+ḥakīm).

## 8. Rules-tuple

`(no-tashkeel for verse-final cross-check; QAC-LEMMA + POS for the primary network matcher; within-verse undirected co-occurrence; nodes = single-token al-Tirmidhī names matched by lemma; Allah excluded from clustering test; semantic-class partition = al-Rāzī ṣifāt tripartition fixed pre-run; basmala-counted-only-in-Q1; Hafs-Kūfan; Mashriqī)`

## 9. MW protections

- **MW-1 (instrument-prior):** matcher, modularity formula, assortativity, class map all fixed in this file before run.
- **MW-2 (corpus-prior):** 10000-perm label-permutation null, seed-locked.
- **MW-3 (alternative-models):** two matchers (M_ADJ primary, M_LEM sensitivity); two statistics (Q, r).
- **MW-5 (replication):** report network under both matchers; backbone must be stable.
- **MW-6 (instrument-control):** the label-shuffle null is the degree-preserving control; Allah-exclusion controls the universal-hub artefact.
- **MW-7 (post-hoc cap):** any community detected by data-driven algorithm (e.g. greedy modularity) beyond the fixed-class test is descriptive-only, α=0.05 single-test ceiling, flagged exploratory.

## 10. Output files

- this pre-reg (SHA-256 embedded in the script)
- `findings/phase-b-hypotheses/scripts/h-new-2400.py`
- `findings/phase-b-hypotheses/csv/h-new-2400.json`
- `findings/phase-b-hypotheses/h-new-2400-divine-name-network.md`

*Direction is LOCKED. A reversed result (Q/r at or below null median) is published as NULL with full prominence.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
