---
id: H-NEW-49.1
title: Prophet-Named Surahs Are Enriched in Muqaṭṭaʿāt — directed single-test PASS
phase: B
status: PASS-DIRECTED at α=0.05 single-test (closed-form hypergeometric)
date: 2026-04-16
agent: integrator
parent: H-NEW-49 PARTIAL-PASS (PROPHET_PERSON × muqaṭṭaʿāt χ² p=0.016)
test: closed-form hypergeometric, no random sampling
verdict: PASS-DIRECTED
---

# [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] — Prophet-Named Surahs in Muqaṭṭaʿāt (RESULT)

## Result

**PASS-DIRECTED at α=0.05 single-test** under both definitions of "prophet-named":

### Specialist's PROPHET_PERSON taxonomy (n=11)
- 7 of 11 PROPHET_PERSON surahs open with muqaṭṭaʿāt (64%)
- Expected under uniform null: 2.80
- Hypergeometric P(X ≥ 7 | n=11, K=29, N=114) = **0.00563**
- PASS at α=0.05; survives even Bonferroni-5

### Conservative prophet-named list (n=8)

Counting ONLY surahs explicitly named after a known prophet/messenger:
| Q | Surah | Prophet | Muqaṭṭaʿāt? |
|---|---|---|---|
| 10 | Yūnus | Jonah | YES (الر) |
| 11 | Hūd | Hūd | YES (الر) |
| 12 | Yūsuf | Joseph | YES (الر) |
| 14 | Ibrāhīm | Abraham | YES (الر) |
| 19 | Maryam | Mary | YES (كهيعص) |
| 31 | Luqmān | Luqmān | YES (الم) |
| 47 | Muḥammad | Muḥammad | NO |
| 71 | Nūḥ | Noah | NO |

- 6 of 8 = **75%** open with muqaṭṭaʿāt
- Expected under uniform null: 8 × 29/114 = 2.04
- Hypergeometric P(X ≥ 6 | n=8, K=29, N=114) = **0.00333**
- PASS at α=0.05 single-test; survives Bonferroni-15

## Interpretation

The 6 muqaṭṭaʿāt-opening prophet-named surahs are precisely the EARLY/MIDDLE-MECCAN narrative-prophetic surahs (Q 10-19 cluster + Q 31 Luqmān). The 2 NON-muqaṭṭaʿāt prophet-named surahs are:
- **Q 47 Muḥammad** — Medinan, focused on commands/legal injunctions, not narrative
- **Q 71 Nūḥ** — short late-Meccan surah (28 verses), in the muqaṭṭaʿāt-free zone Q 69-114

The pattern aligns with [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] / [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] STRONG-PASS findings: muqaṭṭaʿāt openings concentrate in LONG, NARRATIVE surahs. Prophet-named surahs — by their nature — tend to be narrative.

## Cross-finding context

This adds a 7th independent axis to the muqaṭṭaʿāt design picture (cross-finding-006):

| Axis | Test | Verdict |
|---|---|---|
| 1. Letter frequency | [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary | ρ = −0.54 |
| 2. POA pharyngeal/glottal | [[h-new-44-2-poa-closure|H-NEW-44.2]].1 | PASS-DIRECTED p=0.049 |
| 3. Surah-position clustering | [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] | PARTIAL-PASS p=2e-5 |
| 4. Surah-length skew | [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] | STRONG-PASS 4/4 |
| 5. Length-after-chronology | [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] | STRONG-PASS 6/7 |
| 6. Cardinality-position decline | [[h-new-51-cardinality-position-decline|H-NEW-51]] | PASS-DIRECTED p=2e-5 partial |
| **7. PROPHET_PERSON enrichment** | **[[h-new-49-1-prophet-enrichment|H-NEW-49.1]]** | **PASS-DIRECTED p=0.0033** |

## Honest caveats

- Post-hoc-noticed in [[h-new-49-surah-name-class|H-NEW-49]] wave; PASS-DIRECTED per single-test α=0.05 protocol; NOT CONFIRMED.
- Conservative 8-prophet list is more defensible than specialist's 11-element PROPHET_PERSON class (which may include borderline cases).
- Independent replication would test on an INDEPENDENT data dimension (e.g., do prophet-named surahs in NON-Quranic sacred texts also have a "marker" pattern?).
- Mechanism: this finding is fully consistent with the broader "muqaṭṭaʿāt mark long narrative surahs" pattern; the prophet-name correlation may be derivative of length+narrative correlation.

## Integrity

- Closed-form hypergeometric calculation; reproducible by inspection.
- Two definitions tested (8 and 11) for robustness.
- Both definitions PASS at α=0.05 single-test directed.
