# [[h-new-236-2a-other-observables|H-NEW-236.2a]] - Broader observable coverage under the landed M_H top-100 scaffold: 3/3 PASS, with one degenerate compatibility pass

**Finding ID**: [[h-new-236-2a-other-observables|h-new-236-2a]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-2a-other-observables-prereg.md`  
**Pre-reg SHA-256**: `b9b3272e42856f09e9d847491db2466f7e45bfd9228926aed7d955252bcf7ada`  
**Seed**: 20260422  
**Parent**: [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]  
**Related**: [[h-new-239-divine-name-gradient|H-NEW-239]], [[h-new-231-kl-divergence-per-surah|H-NEW-231]], [[h-new-178-alpha-beta-manifold|H-NEW-178]]  
**Grandparent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] -> [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] -> [[h-new-236-generative-simulator|H-NEW-236]] -> [[cross-finding-020-the-complete-equation|cross-finding-020]]  
**Verdict**: **BROAD-GENERALIZATION** by the locked `3/3` count rule. The landed `M_H` top-100 scaffold preserves the [[h-new-239-divine-name-gradient|H-NEW-239]] divine-name-density gradient and the [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL gradient under a fresh imported-family rerun. The [[h-new-178-alpha-beta-manifold|H-NEW-178]] residual cell also passes, but that third pass is **degenerate** rather than strongly probative because the finite parent subset lies almost entirely inside the already-frozen top-100 chain.

---

## Headline

This run asked a new question beyond the parsimony frontier:

> once `M_H` top-100 closes the original [[h-new-236-generative-simulator|H-NEW-236]] 4-observable family,
> does it also preserve independent semantic and compositional order
> signatures, or is that closure narrowly instrument-bound?

Answer:

- **Yes on the two informative external gradients**
- **Yes mechanically on the third, but that third cell has zero simulator variance**

So the honest summary is:

> `M_H` is **not** merely fitting the original Fisher-Rao path family. It
> also preserves the mushaf's front-loaded divine-name-density gradient
> and its front-to-back KL-divergence gradient. But the [[h-new-178-alpha-beta-manifold|H-NEW-178]]
> residual cell should be read as a compatibility check, not as fresh
> independent evidence, because the top-100 scaffold already freezes that
> evaluable subset.

---

## 1. MW-6 positive control

The imported-family rerun passed cleanly:

- parent [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] `L_mufassal_short z = +1.3141`
- reproduced here `z = +1.3166`
- `delta z = +0.0025`

Original-family closure remained intact under the fresh seed:

- `L_path` inside sim 95% CI, percentile `91.7`
- `W_wrap` inside sim 95% CI, percentile `92.8`
- `Block-chi2` inside sim 95% CI, percentile `82.2`
- `L_tail_91_114` inside sim 95% CI, percentile `91.7`

So the run is instrument-valid. The broader-coverage result is being
judged on a stable copy of the landed `M_H` family, not on a drifted
rewrite.

---

## 2. Primary external observables

| Cell | Observable | Empirical | M_H sim mean | M_H sim 95% CI | Empirical pct under M_H | Random mean | Verdict |
|---|---|---:|---:|---:|---:|---:|---|
| A | Spearman(position, divine-name density) over 114 | **-0.4755** | -0.4794 | [-0.4924, -0.4669] | 68.6 | -0.0033 | **PASS** |
| B | Spearman(position, KL from corpus) over 114 | **+0.9201** | +0.9172 | [+0.9121, +0.9224] | 79.5 | -0.0001 | **PASS** |
| C | Spearman(position, alpha-beta residual) over finite H-178 subset | **-0.2557** | -0.2557 | [-0.2557, -0.2557] | 100.0 | +0.0006 | **PASS (degenerate)** |

Top-level count:

- `PASS = 3/3`
- overall pre-registered verdict = **BROAD-GENERALIZATION**

But the evidential weight is unequal across the three cells. Cells A and
B are genuinely informative. Cell C passes because the simulator does
not move the evaluable subset at all.

---

## 3. Informative passes

### 3.1 [[h-new-239-divine-name-gradient|H-NEW-239]] density gradient survives the landed scaffold

Empirical mushaf:

- `rho(position, divine_name_density) = -0.4755`

Under `M_H`:

- sim mean `-0.4794`
- sim 95% CI `[-0.4924, -0.4669]`
- empirical percentile `68.6`

Under random order:

- mean `-0.0033`
- sim 95% CI `[-0.1851, +0.1788]`
- empirical percentile `0.0`

This is a strong generalization result. The front-loaded divine-name
density gradient from [[h-new-239-divine-name-gradient|H-NEW-239]] is **not** a fragile extra feature that
disappears once the mushaf is sampled inside the landed `M_H` family. It
remains squarely inside the simulator envelope while being completely
outside the random-order baseline.

### 3.2 [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL gradient also survives

Empirical mushaf:

- `rho(position, KL_from_corpus) = +0.9201`

Under `M_H`:

- sim mean `+0.9172`
- sim 95% CI `[+0.9121, +0.9224]`
- empirical percentile `79.5`

Under random order:

- mean `-0.0001`
- sim 95% CI `[-0.1835, +0.1889]`
- empirical percentile `100.0`

This is the cleanest broader-coverage result in the run. The very strong
front-to-back KL gradient that [[h-new-231-kl-divergence-per-surah|H-NEW-231]] tied to compositional mode also
falls exactly where the landed `M_H` family expects it. Again, random
order obliterates the structure entirely.

Taken together, Cells A and B show that the landed top-100 scaffold
preserves both:

- a semantic-theological gradient (`divine_name_density`)
- a compositional-vocabulary gradient (`KL_from_corpus`)

That is more than a narrow re-fit of `L_path` and its close cousins.

---

## 4. The degenerate pass

### 4.1 [[h-new-178-alpha-beta-manifold|H-NEW-178]] residual cell passes, but with zero simulator variance

Empirical mushaf:

- `rho(position, alpha_beta_residual) = -0.2557448880`

Under `M_H`:

- sim mean `-0.2557448880`
- sim std `0.0`
- sim 95% CI exactly `[-0.2557448880, -0.2557448880]`

Under random order:

- mean `+0.0006`
- sim 95% CI `[-0.2142, +0.2128]`

This is **not** a fake pass, but it is a weakly informative one.

Why the variance collapses:

- the finite parent residual subset is the surah set
  `Q 2..79` plus `Q 83`
- within the landed `M_H` top-100 hinge scaffold, the contiguous chain
  `Q 2 -> 3 -> ... -> 79` is already fully preserved as hard adjacencies

So the order of almost the entire evaluable [[h-new-178-alpha-beta-manifold|H-NEW-178]] subset is frozen
before the extra-observable check even begins. The resulting
position-vs-residual correlation is therefore inherited exactly rather
than re-derived by a nontrivial family of permutations.

Honest reading:

- **compatibility PASS**
- **independent evidential weight LOW**

The [[h-new-178-alpha-beta-manifold|H-NEW-178]] cell should therefore be treated as supportive but not as
the main reason to claim broad generalization.

---

## 5. Interpretation

### 5.1 What is genuinely new here

[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] only established that the landed `M_H` scaffold closes the
original order-geometry family. [[h-new-236-2a-other-observables|H-NEW-236.2a]] goes further:

- it shows that the same scaffold preserves the mushaf's
  front-loaded divine-name-density geometry
- and preserves the mushaf's front-to-back KL-divergence geometry

So the landed closure is **not** obviously narrow or accidental. The
same scaffold is compatible with independent semantic and compositional
gradients already established elsewhere in the repo.

### 5.2 What this still does not prove

This run does **not** show that `M_H` independently *causes* [[h-new-239-divine-name-gradient|H-NEW-239]] or
[[h-new-231-kl-divergence-per-surah|H-NEW-231]] in the strong standalone sense.

The generator still fixes:

- the classical block partition
- Q 1 lock
- a very dense hard-hinge scaffold (`100 / 113` canonical edges)

So a PASS here means:

> the external observable is preserved under the landed scaffold

not:

> the external observable can be regenerated from scratch by a minimal
> low-saturation principle.

That stronger parsimony question remains separate.

---

## 6. Bottom line

The straight answer is:

- **the landed M_H top-100 scaffold generalizes beyond the original four observables**
- **the strongest evidence is the [[h-new-239-divine-name-gradient|H-NEW-239]] and [[h-new-231-kl-divergence-per-surah|H-NEW-231]] gradients**
- **the [[h-new-178-alpha-beta-manifold|H-NEW-178]] residual cell is compatible but not strongly probative because its evaluable subset is already frozen**

So the result is better than "instrument-bound", but not yet the final
word on how much of the broader mushaf architecture is generated by a
truly minimal scaffold.

---

## 7. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-2a-other-observables-prereg.md`
- Script: `scripts/h_new_236_2a_other_observables.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-2a.json`
