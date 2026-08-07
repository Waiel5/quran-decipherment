---
title: Pillar-law correction notice — what fell on 2026-08-07, what did not, and where every affected file is
author: Waiel Al-Shujaa
date: 2026-08-07
status: CANONICAL CORRECTION NOTICE — additive; no prior claim has been deleted anywhere
source: findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md
---

# Pillar-law correction notice

On 2026-08-07 the four "pillar laws" were, for the first time, put through a **genre control**:
al-Bukhārī's ḥadīth and the pre-Islamic dīwāns were cut into 114 pseudo-surahs matching the
Qurʾān's verse-count and verse-length profile exactly, and each law was re-run on them through
an **instrument-matched** pipeline — the same surface-word instrument applied to the Qurʾān, so
that no comparison is made against the QAC-root headline numbers.

Three of the four laws did not survive that control. This notice is the single authoritative
statement of what changed. It is linked from every corrected file. **Nothing was deleted:** the
original claims remain in place with a notice beside them, because the record of what was
believed and when is itself data.

Full evidence, all run artefacts and every honest limit:
**`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`**
Pre-registration SHA-256 `012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94`,
seeds 20260509 / 20260519, runs under `findings/phase-b-hypotheses/runs/h-new-2680{,b,c}/`.

---

## The one-paragraph version

**Pillar 1 stands.** **Pillars 2 and 3 do not discriminate the Qurʾān from a partitioned dīwān
or ḥadīth collection.** **Pillar 4 was withdrawn the same day** by separate work and replaced by
H-NEW-2710. And **the four p-values may not be multiplied** — the four laws' nulls randomise
different things, so their tails are not commensurable, and no product of them is meaningful.

---

## Law by law

### Pillar 1 — muqaṭṭaʿāt as book-introduction markers (`cross-finding-008`) — **STANDS**

The only law neither baseline satisfies. Given the same generous, Bonferroni-corrected
marker-class search that recovers the muqaṭṭaʿāt in the Qurʾān at p = 4.7×10⁻¹³, al-Bukhārī and
the dīwāns yield **no marker class at all**.

**State it with its honest qualification.** The baselines fail partly because there is nothing
there to find: only **6** Bukhārī pseudo-surahs and **1** poetry pseudo-surah mention *kitāb* or
*qurʾān* in their opening three units, so there is no self-referential target vocabulary to be
marked and no opening marker class to mark it with. The pass is therefore partly **definitional**
rather than a fully discriminating test. "Only scripture talks about itself as a book" is a
weaker claim than "only the Qurʾān has an engineered marker system", and this control does not
separate the two.

### Pillar 2 — mushaf is information-geodesic-optimal under Fisher-Rao (`H-NEW-111`, `cross-finding-011`) — **DOES NOT DISCRIMINATE**

Claimed: L_mushaf = 85.760, z = −11.46, 0 of 10 000 random orderings shorter, within 10.7 % of a
2-opt TSP bound. **The arithmetic reproduces exactly** (independent rebuild: L = 85.7597,
L_Nöldeke = 87.2321, null 104.363/1.623). What fails is the inference.

1. **Both baselines are more extreme than the Qurʾān.** On the instrument-matched surface-word
   instrument: al-Bukhārī **z = −13.84**, pre-Islamic poetry **z = −15.13**, Qurʾān **z = −11.50**.
   Optimality ratios: Bukhārī 1.073, poetry 1.093, Qurʾān 1.130 — the baselines sit *closer* to
   their own TSP optima than the mushaf does to its.
2. **The surah seams contribute nothing detectable.** Cutting the same Qurʾānic verse stream into
   114 blocks of the same size profile but at offsets that ignore every surah boundary gives
   z = −11.23, −13.18, −12.92, −12.33, −12.62 against the real boundaries' −11.50. Four of five
   arbitrary cuts score *more* extreme than the canonical division.
3. **A published sanity anchor is mis-transcribed, and the MW-1 conclusion drawn from it is
   false.** `h-new-111-fisher-rao-mushaf.md` reports length-sorted orderings at L = 107.27 and
   concludes "confirms MW-1 length control is working". Its own `csv/h-new-111.json` records
   **91.0278 / 90.3014**, which an independent rebuild reproduces exactly. Sorting the real
   surahs by length alone, using no vocabulary information whatever, reaches **z = −8.66**, and
   the mushaf is itself close to length-descending (Spearman −0.846).

**What survives.** The *relative* comparison, which never used the random null: the mushaf is a
shorter Fisher-Rao traversal than either reconstructed chronology (85.76 < 87.23 Nöldeke < 89.53
Tanzil), and its margin over a pure length-sorted baseline is **2.80 σ**. That is the honest
effect size. **"11.46 σ below random" must not be cited as evidence of design.**

### Pillar 3 — scale-of-aggregation / pericope-scoping (`cf-025-formal`) — **DOES NOT DISCRIMINATE**

Claimed: thin-marker cohesion NULLs at whole-surah scale and PASSES at pericope scale, 5/5
across marker classes (the 6th, ring-composition, was already retired by `cf-026-formal`).
All five flips reproduce.

Given five best-shot marker classes each, **pre-Islamic poetry flips 5/5 and al-Bukhārī flips
4/5.** The poetry classes are ordinary content words (`عبلة`, ʿAntara's beloved; `عبس`); the
Bukhārī ones are jurisprudential vocabulary (`الماء`, `الإمام`). The mechanism is topical
burstiness, which every text has — and the project already names burstiness as the substrate
(H-NEW-2330, cited inside `cf-026-formal` itself).

Separately: **Pillar 3 is mathematically invariant under every redactional null.** Randomising
marker labels, reading order and title assignment leaves the statistic unchanged, because none
of the three is an argument of it (verified 25/25). In the conjunction it contributes exactly
zero: L1∧L2∧L3 = L1∧L2 identically.

**What survives.** Pericope-scoping remains a correct and useful *methodological* rule — test at
the scale where structure operates. It is not evidence about this corpus specifically.

### Pillar 4 — title-density independence (`H-NEW-1820`) — **WITHDRAWN 2026-08-07**

Withdrawn and replaced by **`h-new-2710-title-density-retest.md`** (TOPICALITY-EXPLAINED). The
`48/89` figure was itself an invalid cross-metric substitution and the original 47/89 is
restored as a description only. Against a naive null the eponymy effect is overwhelming, so the
"independence" reading is wrong; against a null matched on frequency **and dispersion** the
residual is only a rate ratio of **1.285**, with median rank indistinguishable (p = 0.76), so the
proposed *inversion* is wrong too. The real explanation is topicality.

Independently corroborated from the conjunction side: the Pillar-4 criterion is an
**acceptance-of-the-null** test, satisfied by moderateness, and **every** synthetic corpus in
every null and both seeds fails it *from below*. It was never a design-direction constraint.

---

## The methodological result — the four p-values may not be multiplied

Each law's null randomises a different thing, so the four are not tails of a common
randomisation:

| operation on the corpus | Pillar 1 | Pillar 2 | Pillar 3 | Pillar 4 |
|---|:-:|:-:|:-:|:-:|
| permute surah **order** | invariant | **moves** | invariant | invariant |
| permute verses **across** surahs | moves | **moves** | **moves** | **moves** |
| reassign the 29 marker **labels** | **moves** | invariant | invariant | invariant |
| reassign the 89 **titles** | invariant | invariant | invariant | **moves** |

Surah-order permutation — the null of Pillar 2 — leaves the other three **exactly** unchanged.
A single valid joint null does exist (composing verse reallocation with label, title and order
randomisation), and under it **0 of 2 000** synthetic corpora satisfy all four — but that is a
resolution floor, `p < 5×10⁻⁴`, not a measurement, and it cannot be pushed lower because one
law alone already zeroes the survivor count.

The one exactly-licensed multiplication is Pillar 1 × Pillar 2 under the redactional null, where
the two statistics are functions of disjoint, independently drawn randomisation layers
(φ = +0.0003): `p ≤ 3.17×10⁻¹² × 10⁻⁴ ≈ 3×10⁻¹⁶`. Its Pillar-2 factor carries none of the
evidential meaning it appears to, for the reasons above.

**Anywhere a document multiplies these p-values, or says the laws "jointly" establish something,
it is asserting something this project has now formally shown to be unlicensed.**

---

## What is NOT affected

Do not over-read this notice. Untouched by it:

- **`cross-finding-008` and the muqaṭṭaʿāt evidence base** — Pillar 1 stands.
- **The muṭāwaʿa work** — H-NEW-2540, H-NEW-2600, H-NEW-2650.
- **The exactness hunt (H-NEW-2660) and constraint-stacking (H-NEW-2670)** — independent, and
  H-NEW-2670 reaches a convergent methodological conclusion from the opposite direction.
- **`h-new-2710`** — it is the replacement for Pillar 4, not a casualty.
- **Every numerology refutation** — Code-19, golden ratio, word-count balances, 786-uniqueness,
  *sabʿ samāwāt* = 7, iʿjāz ʿilmī. Those NULLs are unaffected.
- **The compression-tail laws, the anti-twin correlation, the Khawātim al-Ḥashr cluster, the
  wrap-around closure (z = −4.17), the UAS ranking, and the classical-scholarship scorecard** —
  none was tested here, and none is retracted by this notice.

---

## Two statistical misstatements corrected in the public-facing pages

Found by separate audit of `poem/al-nuniyya-en.html` and present in the Arabic commentary too.
The poem's own text is untouched — it is art. Only the scientific annotations were corrected.

1. **r = −0.86 is not "orthogonality" or "independence".** A correlation of −0.86 is a *strong
   negative dependence*: the two dimensions trade off against one another almost perfectly.
   Orthogonality would be r ≈ 0. The finding is real and interesting — content-cohesion and
   rhyme-dispersion are near-perfect antagonists in this corpus and not in the controls — but it
   is the opposite of independence, and the annotations said independence.
2. **R² = 0.986 does not describe surah lengths.** The modelled response in H-NEW-660 is
   **windowed content-cohesion distance** d̄_content(s) as a function of position, not the decay
   of surah length. The annotation attributed the fit to length tapering.

---

## Where every affected file is

The complete file-level inventory, with counts and correction status, is
**`findings/PILLAR-CORRECTION-INVENTORY-2026-08-07.md`**.

Two classes of file are deliberately **not** corrected, per standing project convention:

- **Pre-registration files** (46 of them). A pre-reg is SHA-locked and its hash is embedded in
  the script that ran against it. Editing one would break the lock and destroy the very
  tamper-evidence that makes it worth anything. They record what was believed at lock time and
  must stay exactly as they were.
- **Journals and dated session handoffs.** Per the standing rule in
  `findings/CROSS-FINDING-INDEX.md`, these are dated records of what was true on the day they
  were written and are never retro-corrected.

---

*Notice written 2026-08-07 by Waiel Al-Shujaa. A law that a dīwān also satisfies is not a law about the Qurʾān. Bismillāhi al-Raḥmāni al-Raḥīm.*
