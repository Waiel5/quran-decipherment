---
finding_id: h-new-940
phase: B
status: MIXED — H1 directional-only (perm p=0.047 vs locked α=0.01); H2a PASSES Bonferroni-4; H2b/c/d FAIL; H3 yields a 23-prophet consensus order
date: 2026-05-07
agent: prophet-cycle-order-specialist
prereg: h-new-940-prophet-order-conservation-prereg.md
prereg_sha256: 2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66
seed: 20260507
n_perm: 10000
direction_locked: positive mean Kendall-tau
verdict: H1=DIRECTIONAL (perm p=0.047, fails locked α=0.01); H2a=CONFIRMED (p=0.001, Bonferroni-4); H2b=NULL; H2c=NULL; H2d=NULL; H3=DESCRIPTIVE
classical_anchor:
  - Ibn Kathīr — al-Bidāya wa-l-nihāya, prophet-cycle chronological narrative
  - al-Suyūṭī — al-Itqān fī ʿulūm al-Qurʾān, nawʿ 56 (al-ījāz wa-l-iṭnāb), vol. 3 pp. 229-232 (Shamela0011728), on parallel destruction-pericopes
rules_tuple: (no-tashkeel, QAC-PN-lemma, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-940 — Prophet-Cycle Order Conservation Across Narrative Surahs


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

## TL;DR

The corpus-wide claim that prophet-orderings are conserved (mean Kendall-τ > 0 at p < 0.01) DOES NOT clear the locked threshold (observed mean τ = +0.144, perm p = 0.047 — directional but inadequate at the pre-registered α). However, ONE of the four Bonferroni-corrected sub-axes survives at extreme strength: **the pre-Abrahamic chain Ādam → Nūḥ → Hūd → Ṣāliḥ is preserved with τ = 1.0 in every surah where ≥2 of these prophets co-occur** (4/4 qualifying surahs, perm p = 0.001 < α_bon = 0.0125). The Ibrāhīm-Ismāʿīl-Isḥāq parent-son chain, the Mūsā→Hārūn priority, and the Q 21 ↔ Q 6:83-87 alignment all FAIL Bonferroni.

The honest summary is: **prophet-orderings are NOT corpus-wide conserved; only the most temporally remote pre-Abrahamic destruction-cycle ordering is rigid**. This matches al-Suyūṭī's nawʿ-56 grouping of "people of Nūḥ, Hūd, Ṣāliḥ" as parallel destruction-pericopes, but FALSIFIES the broader Ibn-Kathīr-style chronological-historical-conservation claim across the full prophet-set.

---

## 1. Method recap (executed under locked pre-reg)

- **8 surahs analyzed** (≥5 named prophets each): Q 6, 7, 11, 19, 21, 26, 37, 38.
- **25 prophets recognized** (al-Suyūṭī's canonical list), mapped to QAC v0.4 PN-lemmas; Dhū al-Kifl handled by verse-anchor at Q 21:85 and Q 38:48 (root `kfl`).
- **Per-surah ORDER vector** = list of prophet names sorted by (verse, word, segment) of first-occurrence.
- **Pairwise Kendall's τ** on shared-prophet subset of each surah-pair.
- **Permutation null** (10,000 perms, seed 20260507): each surah's prophet-order independently uniform-shuffled.
- **Bonferroni-4** across H2a-d (α_bon = 0.0125 each).
- Pre-reg SHA256 verified at runtime: `2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66`.

## 2. Per-surah prophet-orders (honest catalog)

| Surah | K | Order (left = first-mention) |
|:---|:-:|:---|
| Q 6 | 18 | Ibrāhīm, Isḥāq, Yaʿqūb, Nūḥ, Dāwūd, Sulaymān, Ayyūb, Yūsuf, Mūsā, Hārūn, Zakariyyā, Yaḥyā, ʿĪsā, Ilyās, Ismāʿīl, al-Yasaʿ, Yūnus, Lūṭ |
| Q 7 | 8 | Ādam, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā, Hārūn |
| Q 11 | 9 | Mūsā, Nūḥ, Hūd, Ṣāliḥ, Ibrāhīm, Lūṭ, Isḥāq, Yaʿqūb, Shuʿayb |
| Q 19 | 12 | Zakariyyā, Yaʿqūb, Yaḥyā, Hārūn, ʿĪsā, Ibrāhīm, Isḥāq, Mūsā, Ismāʿīl, Idrīs, Ādam, Nūḥ |
| Q 21 | 15 | Mūsā, Hārūn, Ibrāhīm, Lūṭ, Isḥāq, Yaʿqūb, Nūḥ, Dāwūd, Sulaymān, Ayyūb, Ismāʿīl, Idrīs, Dhū al-Kifl, Zakariyyā, Yaḥyā |
| Q 26 | 8 | Mūsā, Hārūn, Ibrāhīm, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb |
| Q 37 | 8 | Nūḥ, Ibrāhīm, Isḥāq, Mūsā, Hārūn, Ilyās, Lūṭ, Yūnus |
| Q 38 | 11 | Nūḥ, Lūṭ, Dāwūd, Sulaymān, Ayyūb, Ibrāhīm, Isḥāq, Yaʿqūb, Ismāʿīl, al-Yasaʿ, Dhū al-Kifl |

Notable patterns the data reveals:
- **Q 11 is the "narrative chronicle" surah** — its ordering after the Mūsā prologue is the closest to a strict pre-Abrahamic-then-Abrahamic chronology (Nūḥ → Hūd → Ṣāliḥ → Ibrāhīm → Lūṭ).
- **Q 19 is the only inverted-order surah** (Kendall-τ to consensus = −0.091) — it begins with Zakariyyā/Yaḥyā/ʿĪsā (the late-time prophets) and ends with Nūḥ. This is the one major counter-example to chronological conservation.
- **Q 38 places Dāwūd-Sulaymān-Ayyūb at the FRONT** (positions 3-5), not at chronological-end. This is a thematic ordering (forbearance/judgment cycle), not chronological.

## 3. H1 — Corpus-wide Kendall-τ (PRE-REGISTERED PRIMARY)

### Result

| Quantity | Value |
|:---|:---|
| Mean Kendall-τ across 28 surah-pairs | **+0.144** |
| Permutation null mean | +0.0005 |
| Permutation null std | 0.0810 |
| Z-score | +1.78 |
| Permutation p (one-tailed, positive) | **0.0469** |
| Pre-registered α | 0.01 |
| **Verdict** | **DIRECTIONAL (positive direction confirmed; significance threshold not cleared)** |

The corpus-wide signal is genuinely positive but only ~1.8σ from random. Of the 28 pairs, **17 are positive, 9 negative, 2 zero** — a 17/26 = 65 % majority-positive count, which is itself nominally significant under a binomial (one-tailed binomial p = 0.084) but does not clear α=0.01 either.

### Pairwise τ extremes

| Strongest positive | τ | Strongest negative | τ |
|:---|---:|:---|---:|
| Q 7 ↔ Q 38 (n_shared=2: Nūḥ, Lūṭ) | +1.000 | Q 7 ↔ Q 19 | −0.667 |
| Q 11 ↔ Q 38 | +0.800 | Q 7 ↔ Q 21 | −0.667 |
| Q 21 ↔ Q 26 | +0.800 | Q 11 ↔ Q 19 | −0.600 |
| Q 6 ↔ Q 37 | +0.786 | Q 19 ↔ Q 37 | −0.400 |
| Q 11 ↔ Q 26 | +0.714 | Q 26 ↔ Q 38 | −0.333 |

**Q 19 generates 3 of the 5 strongest negative τ-values** (vs Q 7, Q 21, Q 11). The *Maryam* surah's chronologically-reversed structure (late-prophet → early-prophet) is the principal cause of H1's failure to clear α=0.01.

### Direction is locked-positive

Per pre-reg §3 H1, direction is locked POSITIVE before observation. Observed direction MATCHES (+0.144 > 0); no pre-commit violation. The signal exists; it simply does not clear the strict α=0.01 threshold under the locked null.

## 4. H2a — Ādam → Nūḥ → Hūd → Ṣāliḥ chain (PASSES Bonferroni-4)

**Pre-Abrahamic chain conservation.**

| Surah | Present prophets | Sub-order observed | τ to canonical |
|:---|:---|:---|---:|
| Q 7 | {Ādam, Nūḥ, Hūd, Ṣāliḥ} | Ādam → Nūḥ → Hūd → Ṣāliḥ | **+1.0** |
| Q 11 | {Nūḥ, Hūd, Ṣāliḥ} | Nūḥ → Hūd → Ṣāliḥ | **+1.0** |
| Q 19 | {Ādam, Nūḥ} | Ādam → Nūḥ | **+1.0** |
| Q 26 | {Nūḥ, Hūd, Ṣāliḥ} | Nūḥ → Hūd → Ṣāliḥ | **+1.0** |

**Mean τ = +1.0** across 4 qualifying surahs.
**Permutation p = 0.001** under sub-order shuffling (10,000 perms).
**Bonferroni-4 corrected α = 0.0125**.
**Verdict: PASSES.**

This is the single strongest result. **In every surah where ≥2 prophets from the {Ādam, Nūḥ, Hūd, Ṣāliḥ} set co-occur, they appear in the historical/typological canonical order.** This confirms al-Suyūṭī's nawʿ-56 observation that the destruction-pericope cluster (qawm Nūḥ, qawm Hūd, qawm Ṣāliḥ) is templated, plus the pre-historical priority of Ādam.

The fragility-test: Q 38 contains Nūḥ but neither Hūd nor Ṣāliḥ (and no Ādam), so it does NOT qualify. Had Q 38 contained Hūd-then-Nūḥ, the result would have been disturbed.

## 5. H2b — Ibrāhīm → Ismāʿīl → Isḥāq parent-son chain (FAILS)

**Surahs where ≥2 of these 3 prophets co-occur:**

| Surah | Present | Sub-order | τ |
|:---|:---|:---|---:|
| Q 6 | All 3 | Ibrāhīm → Isḥāq → Ismāʿīl | +0.333 |
| Q 11 | {Ibrāhīm, Isḥāq} | Ibrāhīm → Isḥāq | +1.0 |
| Q 19 | All 3 | Ibrāhīm → Isḥāq → Ismāʿīl | +0.333 |
| Q 21 | All 3 | Ibrāhīm → Isḥāq → Ismāʿīl | +0.333 |
| Q 37 | {Ibrāhīm, Isḥāq} | Ibrāhīm → Isḥāq | +1.0 |
| Q 38 | All 3 | Ibrāhīm → Isḥāq → Ismāʿīl | +0.333 |

Mean τ = **+0.556**, perm p = 0.060. **FAILS** Bonferroni-4 (α = 0.0125), **also fails** raw α = 0.05.

**Why?** The Quran consistently puts **Isḥāq before Ismāʿīl** (Q 6, Q 19, Q 21, Q 38 all do this), which inverts the canonical biblical-historical genealogy (Ismāʿīl is the elder son). The text's preferred order is **Ibrāhīm → Isḥāq → Ismāʿīl** rather than the historically expected **Ibrāhīm → Ismāʿīl → Isḥāq**. Classical reading: this is the *kitāb* (Isaac line, narrative dignity given to Isaac at Q 21:72 and Q 19:49 as *gift* from God) being placed before the *millat-Ibrāhīm* honorific Ismāʿīl mentions.

So **H2b fails because its canonical assumption is wrong**: the Quran's canonical chain is Ibrāhīm-Isḥāq-Ismāʿīl, not Ibrāhīm-Ismāʿīl-Isḥāq. Pre-commit-violation note: this is not a direction-flip on observation; it is a wrong a-priori canonical chain. If we test the alternative {Ibrāhīm, Isḥāq, Ismāʿīl} as canonical, ALL 6 qualifying surahs would have τ = +1.0. We do NOT report this re-tested canonical as confirmed (post-hoc), but flag it as a strong directional finding for H-NEW-940.1 follow-up.

## 6. H2c — Mūsā → Hārūn binomial (FAILS)

**Surahs naming both:**

| Surah | Mūsā position | Hārūn position | Mūsā first? |
|:---|---:|---:|:---:|
| Q 6 | 8 | 9 | ✓ |
| Q 7 | 6 | 7 | ✓ |
| Q 19 | 7 | 3 | ✗ (Hārūn precedes!) |
| Q 21 | 0 | 1 | ✓ |
| Q 26 | 0 | 1 | ✓ |
| Q 37 | 3 | 4 | ✓ |

5 / 6 = 0.833 Mūsā-first.
Binomial one-tailed p (n=6, k≥5 | p=0.5) = **0.109**.
**FAILS** α_bon = 0.0125; also fails raw α = 0.05 with this n.

**Q 19 is the spoiler**: Hārūn appears at Q 19:28 in the Maryam pericope (where Maryam is addressed as "Sister of Hārūn", a non-Mosaic Hārūn — likely the brother of Maryam's father ʿImrān, per al-Ṭabarī tafsir on Q 19:28 — though the QAC PN-lemma is the same, and the strict pre-reg honors lemma-identity not contextual-disambiguation), well before Mūsā's mention at Q 19:51. This is a known classical disambiguation problem (cf. al-Ṭabarī's *Jāmiʿ al-bayān* on Q 19:28). Under the locked rules-tuple (PN-lemma, no contextual disambiguation), Q 19 reverses Mūsā-Hārūn priority.

**Honest note**: if Q 19's "Hārūn" were excluded as referring to a different person (al-Ṭabarī flags both readings — same prophet OR a different Hārūn), the test would become 5/5 = 1.0 with binomial p = 0.031, still failing α_bon = 0.0125. The H2c claim is empirically weak across the 8-surah set even on the most permissive reading.

## 7. H2d — Q 21 vs Q 6:83-87 (FAILS)

**Q 6:83-87 prophet-order** (full subset):
Ibrāhīm → Isḥāq → Yaʿqūb → Nūḥ → Dāwūd → Sulaymān → Ayyūb → Yūsuf → Mūsā → Hārūn → Zakariyyā → Yaḥyā → ʿĪsā → Ilyās → Ismāʿīl → al-Yasaʿ → Yūnus → Lūṭ

**Q 21 prophet-order**:
Mūsā → Hārūn → Ibrāhīm → Lūṭ → Isḥāq → Yaʿqūb → Nūḥ → Dāwūd → Sulaymān → Ayyūb → Ismāʿīl → Idrīs → Dhū al-Kifl → Zakariyyā → Yaḥyā

**Shared = 13 prophets**.
**Kendall-τ = +0.359**.
**Perm p = 0.049**.
**Pre-registered threshold τ > 0.7 NOT MET; perm p does NOT clear α_bon = 0.0125.**

The Q 21 surah is structured around Mūsā-Hārūn FIRST (the "successful prophet" template), then Ibrāhīm cycle, then Lūṭ-Dāwūd-Sulaymān-Ayyūb, then minor-prophet appendix. Q 6's *al-Anʿām* list at 6:83-87 is a "creedal roll-call" structured around Abraham's family-tree extension. The two are SAME-MOTIVATED but DIFFERENTLY-STRUCTURED: Q 21 is narrative-dramatic, Q 6 is genealogical-creedal.

**Verdict**: classical scholars (al-Qurṭubī on Q 21, al-Ṭabarī on Q 6:83-87) read both as exhaustive prophet-rosters, but the Quran's own ordering DIVERGES between the two. The classical "shared canonical roll-call" assumption is empirically partial — about 36 % of pairwise concordance, well below the 70 % threshold the pre-reg required.

## 8. H3 — Consensus order and deviation typology

### Consensus order across 23 prophets (those appearing in ≥2 of the 8 surahs)

Sorted by mean normalized rank within each surah they appear in:

1. Nūḥ
2. Ibrāhīm
3. Dāwūd
4. Mūsā
5. Hūd
6. Sulaymān
7. Isḥāq
8. Yaʿqūb
9. Hārūn
10. Ādam
11. Ayyūb
12. Zakariyyā
13. Ṣāliḥ
14. ʿĪsā
15. Lūṭ
16. Yaḥyā
17. Ilyās
18. Ismāʿīl
19. Idrīs
20. al-Yasaʿ
21. Shuʿayb
22. Dhū al-Kifl
23. Yūnus

**Strikingly, this consensus is NOT al-Suyūṭī's chronological order** (which would put Ādam-Idrīs first, Muḥammad last). It is instead a **narrative-prominence order** in which Nūḥ leads (because he appears early in 7/8 surahs, often as the first-named after the addressee-Prophet), Ibrāhīm second (genealogical pivot), then the Davidic kingdom (Dāwūd-Sulaymān cluster), Mūsā and Hārūn (the most-narrated cycle), and the minor prophets in tail.

### Per-surah deviation from consensus

| Surah | Nöldeke phase | τ to consensus | Notable deviation |
|:---|:---|---:|:---|
| Q 6 | Late Meccan | +0.634 | creedal/genealogical, near-consensus |
| Q 7 | Late Meccan | +0.214 | weak consensus alignment (it has 8 prophets in classical chronological order, but its Nūḥ-first then Hūd → Ṣāliḥ reorders the Davidic block out) |
| Q 11 | Late Meccan | +0.556 | strong destruction-pericope chain; matches consensus |
| Q 19 | Middle Meccan | **−0.091** | **reverses consensus** (Zakariyyā-Yaḥyā-ʿĪsā first, Nūḥ last) |
| Q 21 | Middle Meccan | +0.448 | Mūsā-Hārūn-front, then near-consensus |
| Q 26 | Middle Meccan | +0.571 | Mūsā-Hārūn-front, then 5 destruction-pericopes |
| Q 37 | Middle Meccan | **+0.857** | strongest consensus alignment |
| Q 38 | Middle Meccan | +0.600 | Davidic-block-first then Abrahamic |

**Typology emerging**:
- **Genealogical/creedal surahs** (Q 6, Q 19) place the *family-tree* logic first, deviating from narrative-prominence consensus.
- **Destruction-pericope surahs** (Q 7, Q 11, Q 26) follow the chronological-historical destruction sequence.
- **Mixed-narrative surahs** (Q 21, Q 37, Q 38) blend Mosaic-front with genealogical-Abrahamic.
- **Q 19 is the unique inverter**: it reads the prophet-history *backwards* in time (late-prophets first), serving as the *Maryam* mid-Meccan dramatic-introduction architecture.

**No clean Nöldeke-phase × deviation correlation** emerges in this small N=8 set. The pre-registered "late-Meccan deviates Mūsā-direction, early-Meccan deviates Nūḥ-direction" prediction is not supported: Q 7 (Late Meccan) is Ādam-Nūḥ-front (consensus aligned, not Mūsā-front), and Q 26 (Middle Meccan) is Mūsā-front. The chronological-style hypothesis fails by inspection.

## 9. Summary table

| Hypothesis | Pre-reg α | Observed | p | Verdict |
|:---|---:|---:|---:|:---|
| H1 corpus-wide mean τ > 0 | 0.01 | +0.144 | 0.047 | **DIRECTIONAL** (positive direction confirmed; α=0.01 not cleared) |
| H2a Ādam-Nūḥ-Hūd-Ṣāliḥ chain | 0.0125 | +1.000 | **0.001** | **CONFIRMED** |
| H2b Ibrāhīm-Ismāʿīl-Isḥāq | 0.0125 | +0.556 | 0.060 | **NULL** (canonical-assumption-wrong: text prefers Isḥāq-before-Ismāʿīl) |
| H2c Mūsā → Hārūn priority | 0.0125 | 5/6 (83%) | 0.109 | **NULL** (Q 19 spoiler) |
| H2d Q 21 ↔ Q 6:83-87 τ > 0.7 | 0.0125 | +0.359 | 0.049 | **NULL** |
| H3 consensus order | descriptive | — | — | **23-prophet narrative-prominence order; no clean phase-typology** |

## 10. Classical-cross-reference

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 56 *al-ījāz wa-l-iṭnāb*, vol. 3 pp. 229-232 (Shamela0011728 ed.)** groups "qawm Nūḥ, Hūd, Ṣāliḥ" as parallel destruction-pericopes. **Data CONFIRMS** at H2a (perfect τ=1 over qualifying surahs).
- **Ibn Kathīr, *al-Bidāya wa-l-nihāya*, vol. 1** gives the chronological succession Ādam → Idrīs → Nūḥ → Hūd → Ṣāliḥ → Ibrāhīm. **Data PARTIALLY CONFIRMS** the Ādam-Nūḥ-Hūd-Ṣāliḥ chain (H2a) but **DOES NOT** confirm full chronological conservation across the wider prophet-set (H1 only marginally positive).
- **al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 6:83-87** treats the Anʿām roll-call as a canonical reference. Q 21's roll-call has been classically read as a parallel. **Data REFUTES** the strong-parallel reading: τ = +0.359 is far below the pre-registered threshold of 0.7.
- **al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 19:28 *ʾukhta Hārūn*** documents the classical dispute over which Hārūn is meant. The H2c failure exposes this: under strict PN-lemma matching, Q 19's "Hārūn" precedes "Mūsā" (since Maryam is addressed as Hārūn's-sister at v. 28, before Mūsā is mentioned at v. 51). This is exactly the disambiguation al-Ṭabarī flags.
- **al-Biqāʿī, *Naẓm al-Durar*** (general): the surah-internal *munāsaba* logic is not a chronological-historical conservation logic; it is a thematic-rhetorical logic. **Data ALIGNS** with this — Q 19's reverse-time order, Q 38's Davidic-front, Q 6's genealogical-front are all rhetorical, not chronological.

## 11. Honest limits

1. **N=8 surahs is small**. Only 28 surah-pairs contribute; pair-level τ has high variance (few pairs have only 2 shared prophets, where τ ∈ {+1, −1} only). Median |shared| = 5.
2. **Canonical-chain assumptions can be wrong** (H2b case). The pre-reg's choice of Ibrāhīm-Ismāʿīl-Isḥāq inverted the actual Quranic preference. We do NOT report the corrected chain as confirmed (would be post-hoc); we flag it as queued for H-NEW-940.1.
3. **Q 19's Hārūn ambiguity** (H2c) is not adjudicated under the locked rules-tuple. Under contextual-disambiguation, the H2c result might shift to 5/5 = 1.0 (still p=0.031, still fails α_bon).
4. **Permutation null shuffles each surah's order independently**; a stronger null would constrain shared-prophet co-attestations to preserve marginal counts (we did the simpler null).
5. **The 25-prophet list excludes ʿUzayr, Luqmān, Dhū al-Qarnayn** whose prophet-status is contested — none of these names appear in the 8-surah set anyway, so this exclusion is inert here.
6. **Maryam, Iblīs, Āzar are NOT prophets** in al-Suyūṭī's list (Maryam is a saintly woman, not a prophet; Iblīs is the adversary; Āzar is Ibrāhīm's father). They appear in QAC PN-lemma but are correctly excluded from prophet-counts.

## 12. Garden-of-forking-paths log (DURING run)

- The script's chronology lookup initially used column-0 (`revelation_order`) instead of column-1 (`mushaf_order`). This caused the H3 narrative table to print wrong Nöldeke phases. Fixed BEFORE re-running primary statistics; primary H1/H2 results are NOT affected (they don't depend on chronology). H3 phase-labels in this findings doc are post-fix-correct. **No pre-commit violation**: chronology lookup is a presentation detail of H3 (which is descriptive), not a primary statistic.
- No other forking-path divergences. All H1 / H2a / H2b / H2c / H2d tests executed exactly as pre-registered.

## 13. Queued follow-ups

- **H-NEW-940.1**: pre-register the Ibrāhīm → Isḥāq → Ismāʿīl chain (Quran's actual canonical preference, classically anchored by Q 21:72 *wahabnā lahu Isḥāqa wa-Yaʿqūba* gift-prophecy and Q 19:49 same; al-Ṭabarī tafsir reads Isḥāq's prior-mention as theological-prioritization of the Israelite line within the Abrahamic family). Test on the same 8-surah set. Expected: τ = 1.0 across all 6 qualifying surahs, p_perm well under 0.001.
- **H-NEW-940.2**: replicate H-NEW-940 on the broader narrative set (relax to ≥3 prophets/surah). Adds Q 5, 17, 22, 27, 51 etc. Power should increase substantially.
- **H-NEW-940.3**: test the sub-axis "qaṣaṣ-block" (Q 7 + Q 11 + Q 26) — these three "destruction-pericope" surahs — for τ > 0.9 conservation (they should be highly mutually-conserved per al-Suyūṭī's nawʿ-56).
- **H-NEW-940.4**: test ordering-deviation against compression-tail position (s ≥ 50 vs s < 50). Hypothesis: long-narrative surahs (s ≤ 50) preserve canonical ordering more than late-mufaṣṣal surahs.
- **Disambiguation sensitivity**: under contextual-disambiguation (Q 19 Hārūn ≠ Mūsā's brother), recompute H2c. Expected proportion 5/5 = 1.0, binomial p=0.031.

## 14. Reproducibility

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation-prereg.md`
- Pre-reg SHA256: `2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_940_prophet_order_conservation.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-940.json`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-940-run-1.md`
- Seed: 20260507
- Permutations: 10,000
- Stdlib only.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
