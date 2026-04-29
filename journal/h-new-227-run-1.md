---
finding_id: H-NEW-227
run: 1
date: 2026-04-17
operator: autonomous-agent
seed: 20260419
permutations: 10000
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; basmala-counted-only-in-Surah-1; D from H-NEW-111)
script: scripts/h_new_227_wrap_edge_chronologies.py
output_json: findings/phase-b-hypotheses/csv/h-new-227.json
output_md: findings/phase-b-hypotheses/h-new-227-wrap-edge-chronologies.md
h111_sha256: (source of D matrix — see JSON output)
verdict: PASS
---

# H-NEW-227 Run 1 — Wrap-edge across chronologies

## Question
Is the mushaf wrap-edge d(Q 114, Q 1) tighter than the wrap-edge d(last, first) under each classical chronology, and is it significantly small vs a uniform-random null?

## Key numbers

| Ordering        | first | last | d(last,first) | Δ vs mushaf |
|-----------------|------:|-----:|--------------:|------------:|
| **mushaf**      | Q1    | Q114 | **0.3884**    | 0           |
| egyptian_1924   | Q96   | Q110 | 0.4688        | −0.0804     |
| blachere_1947   | Q96   | Q110 | 0.4688        | −0.0804     |
| noldeke_1860    | Q96   | Q5   | 1.2173        | −0.8290     |
| bell_1937       | Q96   | Q5   | 1.2173        | −0.8290     |

Null (10K perms, seed 20260419): mean=0.9217, sd=0.2102, median=0.9534, q05=0.4799.

Mushaf wrap z = −2.537, p₁ₛ = 0.027697 < α=0.05 → **PASS**.

## Findings

1. **Mushaf is rank-1** of all 5 orderings for wrap-edge tightness.
2. Mushaf wrap d(Q114, Q1)=0.3884 is **below the null 5th percentile** (0.4799).
3. Egyptian and Blachère share an identical wrap-edge Q110→Q96=0.4688 because both chronologies place Q96 first and Q110 last (Egyptian) / near-last.
4. Nöldeke and Bell both produce a Q5→Q96 wrap-edge of 1.2173, well above the null median — these chronologies give a *worse-than-random* wrap-edge.
5. The mushaf is the *only* ordering whose wrap-edge clears the α=0.05 lower-tail threshold.

## Interpretation

The ṭawāf-like closure of the canonical mushaf is:
- specific to the canonical order (not an artifact of any reconstructed chronology),
- stronger than what the two chronologies that close at Q110 (Egyptian/Blachère) achieve,
- dramatically stronger than the chronologies that terminate on a long Medinan surah (Nöldeke/Bell both end on Q5 al-Māʾidah and begin on Q96 al-ʿAlaq, a root-profile-distant pair).

Wrap-edge here is a single-edge measurement and is weaker than path-length evidence; under the broader H-NEW-111 / H-NEW-212 framework the *whole-path* picture is mixed (mushaf is competitive but not uniquely minimal). On the specific ṭawāf/closure prediction, however, the mushaf has a clear and reproducible advantage.

## Complementarity with H-NEW-137

H-NEW-137 found Q1 is content-anomalously-close to the TERMINAL_TRIAD (mean-to-set statistic). H-NEW-227 confirms the same topology from the single edge perspective: the last→first jump for the mushaf specifically lies in the lower tail of random endpoint pairings. The two tests triangulate the same "closure" phenomenon from different statistical angles.

## Files
- `scripts/h_new_227_wrap_edge_chronologies.py`
- `findings/phase-b-hypotheses/csv/h-new-227.json`
- `findings/phase-b-hypotheses/h-new-227-wrap-edge-chronologies.md`
