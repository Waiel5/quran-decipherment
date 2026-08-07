---
surah: 36
finding_id: Q036-F-07
title: Q 36:13-32 "town destroyed for rejecting prophets" lexical cohesion test — NULL
date: 2026-05-09
phase: B+
verdict: NULL (pre-committed direction not satisfied)
pre_reg_sha256: 6f71e1877fff6e799a5a2b2c494452fb117198396468cc3284737fe68802e82d
---

# Q036-F-07 — The aṣḥāb al-qarya pericope is NOT more lexically aligned with parallel town-pericopes than with the rest of Q 36


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Pre-committed direction

H₁ (locked before observation): root-Jaccard(Q 36:13-32, {Q 7:73-93 ∪ Q 11:42-95 ∪ Q 27:45-58}) > root-Jaccard(Q 36:13-32, Q 36-ambient), with p_perm ≤ 0.05 under a 10,000-permutation null over random 20-verse contiguous spans of Q 36.

## Result

| Quantity | Value |
|:--|:-:|
| Pericope (Q 36:13-32) root-set size | 72 |
| Parallel union (Q 7+11+27) root-set size | 269 |
| Q 36 ambient (vv. 1-12 + 33-83) root-set size | 180 |
| J(pericope, parallel-union) | **0.1718** |
| J(pericope, Q 36-ambient) | **0.1943** |
| Δ = J₁ − J₂ | **−0.0225** |
| p_perm (10,000 perms, seed 20260509) | **0.1876** |
| Robustness J(pericope, Q 11:42-95-alone) | 0.1789 |

**The pre-committed direction is reversed by a small margin** (−0.0225). The Q 36:13-32 pericope shares **slightly more** roots with the rest of Q 36 (J = 0.19) than with the parallel town-destruction pericopes elsewhere (J = 0.17). The permutation null gives p_perm = 0.19 — well outside the pre-locked α = 0.05.

**Verdict**: **NULL** (published with equal prominence). The lexical-cohesion prediction fails.

## Interpretation — what this means

The reading "Q 36:13-32 is a typed instance of the corpus's destroyed-town pericope" is **not corroborated at the root-vocabulary level**. The pericope's roots are slightly more aligned with Q 36's own ambient material (its surrounding muqaṭṭāʿat-and-cosmic-signs-and-eschatology framing) than with parallel pericopes in Q 7 / Q 11 / Q 27.

Three plausible mechanisms:

1. **Local cohesion dominates inter-pericope cohesion.** Surahs are root-distribution-coherent at the surah level; a sub-pericope drawn from a Meccan surah will share more roots with its own surah's other Meccan content than with a Meccan pericope drawn from a different surah. This is the project's standing finding across [[h-new-660-compression-tail-gradient|H-NEW-660]] (d̄_content surah-wise) and [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] (verse-FR fractal).

2. **The town-pericope vocabulary is genre-distinct, not type-distinct.** The named-prophet destructions of Q 7 / Q 11 / Q 27 use named-prophet vocabulary (Hūd, Ṣāliḥ, Lūṭ, Shuʿayb roots) that Q 36 does NOT use — Q 36's pericope is the *unnamed-city + unnamed-messengers + unnamed-believing-man* configuration. This is a content-typological distinction that root-Jaccard cannot capture as cohesion.

3. **Q 36's pericope has unique vocabulary.** Q 36:20-27 contains the *muʾadhdhin* / believing-man speech which is rhetorically and lexically unique in the corpus (e.g., *yā layta qawmī yaʿlamūn* — "would that my people knew", Q 36:26). These uniquely-Q 36 roots inflate J₂ (alignment with ambient Q 36) without inflating J₁.

This is an **instructive NULL**: the **content-type relation** (Q 36 belongs to the destroyed-town typology) is real at the **narrative / theological** level but NOT at the **root-vocabulary-distribution** level.

## Robustness checks

- Q 11:42-95 alone (the largest parallel) gives J = 0.179 — slightly higher than the union but still below J₂ = 0.194 ambient. The direction is preserved.
- The 10,000-permutation null (random 20-verse spans of Q 36) gives p = 0.19, meaning the observed effect is not even directionally close to significance — the pericope is a typical Q 36 span, not an aberration.

## Honest limits

- **Set-based Jaccard does not capture frequency**. A TF-weighted cosine variant or a frequency-novelty-restricted Jaccard could yield a different result. These are queued POST-HOC and would not retract this NULL.
- **Mass-shared theological roots dominate**. Roots like Allāh, rabb, rasūl, qāla appear in every span; this is the project-standard limitation of root-Jaccard.
- **The parallel-pericope selection is rules-tuple-locked at three pericopes**. Adding more parallels (Q 26 narrative cluster, Q 54 destruction cycle) might shift J₁ marginally but the direction is already wrong by ~0.02.
- **The "aṣḥāb al-qarya" classical reading is theologically and rhetorically valid**. The empirical NULL here is on a specific quantitative form of the claim, not on the typological reading itself.

## Cross-references

- `02-content-analysis.md` §2 — Block B (vv. 13-32) narrative summary.
- `03-tafsir-survey.md` §3 — al-Ṭabarī, al-Rāzī on aṣḥāb al-qarya identification.
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — surah-level content cohesion law explains why local-ambient cohesion dominates.
- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — verse-level FR fractal: Q 36's verse-order is information-geodesically optimal, supporting local-cohesion mechanism.
- [[cross-finding-025-marker-thickness|cross-finding-025]] — marker-thickness rule: pericope-classification on a thin lexical marker NULL's on root-FR (Wave-H result).

## Output

- `csv/Q036-F-07.json` — full JSON with permutation distribution stats and robustness checks.

*Pre-reg sha-256 `6f71e1877fff6e79…cc3284737fe68802e82d` verified at runtime.*
