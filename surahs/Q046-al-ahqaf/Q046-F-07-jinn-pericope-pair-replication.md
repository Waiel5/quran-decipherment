---
finding_id: Q046-F-07
surah: 46
surah_name: al-Aḥqāf
file_type: novel-finding
date: 2026-05-10
verdict: PASS-DIRECTED (replicates Q072-F-03)
prereg_sha: 8702e3dce71929b3a523b66684151b04153e160ca5943a66207097835291e852
---

# Q046-F-07 — Q 46:29-32 jinn-pericope ↔ Q 72 root-Jaccard pair

## Verdict

**PASS-DIRECTED.** Q 46:29-32 (the 4-verse jinn-listening-to-Quran pericope) shares root-Jaccard **0.1538** with Q 72 al-Jinn, vs null median **0.0531** (random 4-verse blocks from non-Q46-non-Q72 surahs, n_perm=10000). One-sided upper-tail p = **0.0072** (below Bonferroni α = 0.0167).

This cross-direction replication of Q072-F-03 (Wave 2026-04-28) is confirmed at p < 0.01.

## Pericope ↔ surah Jaccard

| Metric | Value |
|:--|--:|
| Q 46:29-32 unique roots | (see csv) |
| Q 72 unique roots | (see csv) |
| Observed Jaccard | 0.1538 |
| Null median | 0.0531 |
| Observed/null ratio | **2.90×** |
| p (one-sided upper) | 0.0072 |

The pericope-to-surah Jaccard is ~2.9× the random-block baseline — a robust pair-tightness.

## Interpretation

The two corpus jinn-listening-to-Quran loci share root-distribution at a tightness substantially above chance. This:

1. **Replicates Q072-F-03** from the Q 46 direction (MW-5 cross-direction confirmation).
2. **Strengthens the cross-finding-021** synthesis (verse-pericope-pair cohesion as a corpus-architecture signature).
3. **Provides a verse-level FR-cohesion data-point** that operates at sub-surah granularity (Q 46:29-32 is 4 verses out of 35; the cohesion is local to the pericope, not the surah).

The two passages narrate the same event from different angles:
- **Q 46:29-32**: "We turned a group of jinn toward you [Muḥammad] to listen to the Quran ... they returned to their people as warners ..." (third-person external description).
- **Q 72:1-19**: "Say: 'It has been revealed to me that a group of the jinn listened ...' they said: '... we have heard a wondrous Quran ...'" (first-person internal jinn-speech).

The root-Jaccard tightness reflects the shared narrative material; the bifurcation into external-narration vs internal-quotation is a *deixis-switch* (al-iltifāt class per Abdel Haleem 1992).

## Cross-references

- [[Q072-al-jinn/Q072-F-03|Q072-F-03]] — original pair-test from Q 72 side.
- [[Q046-al-ahqaf/Q046-F-02|Q046-F-02]] — Q 46 jinn-listening Jaccard (existing).
- [[1992-abdel-haleem-grammatical-shift-iltifat-bsoas|Abdel Haleem 1992]] — *iltifāt* class.
- [[cross-finding-025-marker-thickness-rule]] — local-pericope tightness vs whole-surah tightness.

## Substantive observation: the iltifāt of the jinn-pair

The Q 46 ↔ Q 72 pair is one of the corpus's clearest examples of *iltifāt across surahs*:
- Q 46:29-32 narrates with God-as-speaker, Muḥammad as object, jinn as observed party (3rd-person).
- Q 72:1-19 has Muḥammad commanded to *say* what was revealed: the jinn speak in *direct quotation* (1st-person reported speech).

The deixis-switch is structural, not arbitrary: the same event is encoded twice in the corpus, once externally and once internally. This is a corpus-architectural feature that would be invisible at the within-surah scale.

## Honest limits

- The 4-verse pericope is short; root-set Jaccard is sensitive to small variations.
- The sampling null draws contiguous 4-verse blocks from all eligible surahs; chronology-matched or content-class-matched nulls would be stronger.
- The "iltifāt of the jinn-pair" observation is descriptive-substantive and would require its own pre-reg to promote to a CONFIRMED finding.
- MW-5 (replication): satisfied by the cross-direction confirmation (Q072-F-03 + Q046-F-07).

## Files

- pre-reg: `preregs/Q046-F-07-jinn-pericope-pair-replication-prereg.md`
- script: `scripts/Q046_F_07_jinn_pericope_pair.py`
- output: `csv/Q046-F-07.json`
