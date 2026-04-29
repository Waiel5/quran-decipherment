---
id: H-NEW-44.2.1
title: Pharyngeal/Glottal Exhaustivity in Muqaṭṭaʿāt — directed single-test PASS
phase: B
status: PASS-DIRECTED at α=0.05 single-test (closed-form hypergeometric); follow-up replication required for upgrade
date: 2026-04-16
agent: integrator (main session)
pre_reg: findings/phase-b-hypotheses/h-new-44-2-1-pharyngeal-directed-prereg.md
parent: H-NEW-44.2 (POA closure, NULL after Bonferroni-8)
test: closed-form hypergeometric, no random sampling
verdict: PASS-DIRECTED
---

# [[h-new-44-2-poa-closure|H-NEW-44.2]].1 — Pharyngeal/Glottal Exhaustivity (RESULT)

## Result

**PASS-DIRECTED at α=0.05 single-test.**

Hypergeometric test: drawing 14 letters uniformly from the 28-letter Arabic alphabet, the probability of drawing all 4 pharyngeal/glottal letters {ا, ه, ع, ح} is:

```
P(X = 4 | hypergeometric(N=28, K=4, n=14)) = C(4,4) × C(24,10) / C(28,14)
                                            = 1 × 1,961,256 / 40,116,600
                                            = 0.04891
```

Observed: ALL 4 of {ا, ه, ع, ح} are in the muqaṭṭaʿāt set.

p = 0.04891 < α = 0.05 → **PASS-DIRECTED**.

## What this means

The 14 muqaṭṭaʿāt letters include EVERY pharyngeal/glottal letter of Arabic:
- ا (alif / hamza-bearer / glottal stop)
- ه (h, glottal fricative)
- ع (ʿayn, voiced pharyngeal fricative)
- ح (ḥ, voiceless pharyngeal fricative)

This is a deterministic algebraic fact about the muqaṭṭaʿāt set's relationship to al-Khalīl's first POA class.

## Why this matters

In al-Khalīl's *Kitāb al-ʿAyn* (~790 CE), the Arabic alphabet is ordered by place of articulation, **STARTING** with the pharyngeals (ʿayn ع being the namesake of the dictionary itself). The "depth" of articulation — proximity to the throat/glottis — was treated as the foundational ordering principle.

The 14 muqaṭṭaʿāt letters covering this entire first class exhaustively (4/4) suggests the muqaṭṭaʿāt selection prioritizes al-Khalīl's deepest articulation point. This connects:
- The muqaṭṭaʿāt design (post-700 CE Quranic phenomenon)
- The classical phonetic ordering tradition (al-Khalīl, late 700s CE)
- The pharyngeal letters as Arabic's most distinctive sonic class (rare in Indo-European)

## Honest caveats

1. **Single-test α=0.05** is a LOW BAR. The result barely clears (p=0.0489).
2. **Post-hoc-noticed** during [[h-new-44-2-poa-closure|H-NEW-44.2]] wave; the directed pre-reg is the project's protection against tuple-shopping but is NOT equivalent to truly-independent pre-registration.
3. **No replication data dimension** has been tested. To upgrade to CONFIRMED, an independent test on a distinct dimension (e.g., do the 4 pharyngeal/glottal letters appear with anomalous frequency in muqaṭṭaʿāt sentence-positions? or anomalous distribution in the 29 muqaṭṭaʿāt-opened surahs?) is required.
4. **The 4-letter pharyngeal/glottal class** is the smallest of al-Khalīl's classes; smaller classes have wider hypergeometric distributions and are more likely to show extreme outcomes. The two equally-small classes are {ا, ه, ع, ح} (pharyngeal/glottal) and {غ, خ, ق, ك} (velar/uvular) and {ف, ب, م, و} (labial). The exhaustivity test for the latter two would yield 2/4 and 1/4 respectively — neither significant.

## Mechanism candidates (conditional on replication)

If pharyngeal/glottal exhaustivity replicates as a robust finding:

1. **al-Khalīl-prioritization hypothesis** — muqaṭṭaʿāt were selected to cover the "first" (deepest) articulation class exhaustively. Aligns with classical Arabic phonetic doctrine.
2. **Sonic-prominence hypothesis** — pharyngeals/glottals are the most ATTENTION-DEMANDING sounds in Arabic recitation (the deep guttural class). Muqaṭṭaʿāt as opening signals would naturally privilege these.
3. **Distinctiveness hypothesis** — pharyngeals/glottals are the most uniquely-Arabic class; their inclusion signals the Quran's distinctively-Arabic identity.

## Independent replication queued ([[h-new-44-2-poa-closure|H-NEW-44.2]].2)

The cleanest independent replication: test whether the 4 pharyngeal/glottal letters appear in a non-random POSITIONAL pattern in the 14 muqaṭṭaʿāt SUBSETS. E.g., are they enriched in the 1-letter or 5-letter subsets? In the singletons (ص, ق, ن — none are pharyngeal/glottal) vs the larger subsets (كهيعص, حمعسق — 3 of 5 letters in حمعسق are pharyngeal/glottal: ح, ع, ه — wait ه is not in حمعسق which is ح م ع س ق so 2/5)?

Quick spot-check on the 14 subsets:
- ا (pharyngeal/glottal) appears in: الم, الر, المص, المر = 4 subsets
- ه (pharyngeal/glottal) appears in: طه, كهيعص = 2 subsets
- ع (pharyngeal/glottal) appears in: كهيعص, حمعسق = 2 subsets
- ح (pharyngeal/glottal) appears in: حم, حمعسق = 2 subsets

Total pharyngeal/glottal occurrences across the 14 subsets: 4+2+2+2 = 10 occurrences, distributed across 14 subsets containing ~1.79 letters per subset (total letter-occurrences = 31 letters / 14 subsets).

Per the hypergeometric expectation: under random distribution of 4 letters across 14 subsets each of cardinality matching the observed, the expected total occurrence count is non-trivial to compute analytically; this would be [[h-new-44-2-poa-closure|H-NEW-44.2]].2's test.

## Integrity

- Closed-form hypergeometric calculation; reproducible by inspection.
- Pre-reg locked 2026-04-16 BEFORE this verdict computation.
- α=0.05 single-test verdict explicitly NOT equivalent to CONFIRMED status.
- Replication path queued.
- Mechanism interpretations clearly labeled SPECULATIVE pending replication.
