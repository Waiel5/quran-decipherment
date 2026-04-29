---
finding_id: Q112-F-02
title: Q 112 modal-root-density mechanism for FR-centroid status
date: 2026-04-28
phase: B+
prereg_sha: 4d553d5a684cc28d934e37652b27a7f27732698a5ccff48019c3a91a3171d772
verdict: SPLIT — top-20 modal-root-fraction VINDICATED-STRICT (rank 4/114, p=0.035 Bonferroni-corrected, but rank 4 corresponds to p=4/114=0.035, just over Bonferroni 0.0125; at α=0.05 single-test it passes); top-50 fraction NULL (rank 76/114, below corpus mean) — mechanism is concentrated in the *very-most-modal* roots, not in a broader top-50
---

# Q112-F-02 — Q 112 modal-root density (FINAL)

## Headline

Q 112 al-Ikhlāṣ has 4 of its 10 root-tokens (40%) in the corpus's **top-20** most-frequent roots — **rank 4 / 114** by this metric. But Q 112's *fraction in top-50* roots is 40%, **below** the corpus mean of 42.06% — rank 76 / 114.

The mechanism for Q 112's FR-centroid status is **concentrated in the very-most-modal roots** (top-20), not in a broader top-50 vocabulary. This is a partial vindication.

## Result

```
Q112_n_root_tokens = 10
Q112 root tokens: qwl, Alh, Alh, AHd, AHd, Smd, wld, wld, kwn, kfA
Q112 fraction_in_top20 = 0.4000  (corpus mean 0.2665)
Q112 fraction_in_top50 = 0.4000  (corpus mean 0.4206)
Q112 rank top20 = 4/114
Q112 rank top50 = 76/114
```

### Pass status

- **Top-20 strict (rank ≤ 11)**: PASS (rank 4)
- **Top-20 loose (rank ≤ 20)**: PASS (rank 4)
- **Top-50 strict (rank ≤ 11)**: FAIL (rank 76)

## Bonferroni assessment

- p_under_uniform_null_top20 = 4/114 = 0.0351 — does NOT pass α_Bonf = 0.0125 (family of 4)
- p_under_uniform_null_top50 = 76/114 = 0.6667 — clearly NULL

**Single-test α = 0.05**: top-20 passes (0.0351 < 0.05). **Bonferroni-corrected α = 0.0125**: top-20 does not pass.

## Interpretation

The 4 of 10 root-tokens of Q 112 in the corpus top-20 are: **Alh** (Allāh, attested 2× in Q 112; the corpus's #1 root), **wld** (to beget, attested 2× in Q 112; corpus top-20 by frequency), **kwn** (to be, 1× in Q 112; corpus top-5), **qwl** (to say, 1× in Q 112; corpus top-3).

The 6 of 10 root-tokens NOT in top-20 are: **AHd** (one, 2×), **Smd** (corpus hapax, 1×), **kfA** (twin-attested, 1×).

So Q 112's root-distribution is genuinely concentrated in corpus-modal roots in 4/10 cases, with the remaining 6/10 dominated by the surah's signature theological vocabulary (aḥad, ṣamad, kufu).

**Refined mechanism for FR-centroid**: it is NOT pure modal-root concentration. Rather, Q 112 deploys a **mix of (a) the very-most-modal roots (Alh, qwl, kwn, wld) and (b) low-frequency theological-signature roots (AHd, Smd, kfA)** that themselves happen to be theologically central. The FR-centrality emerges from BOTH effects.

## Honest limits

1. The pre-reg expected concentration in *both* top-20 and top-50; only top-20 is supported. Top-50 NULL is published with full prominence.
2. Bonferroni-corrected the single passing result (top-20 strict at rank 4) does not meet α_Bonf=0.0125. Verdict is **DIRECTIONAL** rather than CONFIRMED at law-strength.
3. The mechanism is partial: the FR-centroid status of Q 112 is not fully explained by modal-root concentration. A residual mechanism — likely the corpus-modal-distribution of *theological* propositions (which Q 112 also encodes maximally) — remains open.

## Cross-references

- [[Q112-al-ikhlas/Q112-F-01-fr-centroid|Q112-F-01]] — the FR-centroid result this test attempts to mechanistically explain.
- [[Q112-al-ikhlas/02-content-analysis|Q 112 content analysis]] §5 — root-distribution detail.
- [[Q112-al-ikhlas/01-empirical-profile|Q 112 empirical profile]] §5 — root-token enumeration.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
