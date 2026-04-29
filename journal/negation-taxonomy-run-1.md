---
agent: negation-taxonomy-run-1
date: 2026-04-12
phase: phase-b-hypotheses
---

# Journal — Negation Taxonomy

## Approach

1. Read master-index, paired-opposites, rhetorical-questions findings
   to position negation work within the existing agent corpus. Confirmed:
   - Negation and questioning are ORTHOGONAL rhetorical channels
     (rhyme/Q independence, ring/Q clustering — see rhet-q §4).
   - Negation is partly how antithesis gets marked (kfr, bṭl,
     ẓulumāt are lexical/morphological negations).
2. Inspected Dukes QAC v0.4 morphology — POS:NEG tag exists. Pulled
   all 2,688 NEG tokens, grouped by lemma.
3. Verified that `laysa` is NOT POS:NEG (it's tagged V with ROOT:lys)
   and `ghayr` is NOT POS:NEG (it's tagged N). Added both via lemma
   filter. Also added `illa` (POS:RES/EXP, 663 tokens) as the
   exception-complement for negation-exception constructions.
4. Built per-surah, per-particle, per-period (Meccan/Medinan) counts.
5. Ran specific formula scans:
   - `lā ilāha illā X` (NEG laA + ROOT Alh + illā window)
   - `mā kāna li-X` (NEG maA + V kwn + P li)
   - `fa-lā uqsimu` (verse-initial laA + ROOT qsm)
   - Divine-apophatic (`lā + 3MS imperfect + divine-in-verse`)
   - Prohibitive vs declarative lā (by 2nd-person marking)
6. Cross-referenced ring centers against NEG tokens.
7. Wrote up findings in the main taxonomy document.

## Key findings

- **Shahāda distribution**: 30 *huwa* + 2 *Allāh* + 3 *ana* + 1 *anta*.
  The popular ritual "illā Allāh" is a minority Quranic form; the
  *huwa* version dominates. Not a finding I had expected.
- **lan tarānī** (Q 7:143) is a Quranic hapax — lan + root r'y in
  window occurs only once. Classical theology's weight on this verse
  is corroborated by its grammatical singularity.
- **Al-Ikhlāṣ's 3 lam-negations in 2 verses** is the densest
  apophatic-triad in the Quran. Exactly 3 *lam* tokens in vv 3-4 carry
  the full theological declaration.
- **Prohibitive vs declarative lā = 197 vs 825** (4.2:1 declarative).
  I expected closer parity; the heavy declarative lean is striking
  and suggests Quranic rhetoric is more polemical-descriptive than
  legal-prescriptive at the particle level.
- **11 zero-negation surahs**, all short Meccan
  (97/99/101/102/103/104/106/108/110/113/114). Declarative/
  eschatological mode is negation-free.
- **mā kāna li-X**: 54 verses (my extractor found more than the initial
  pass — 54, not 36; I re-ran with correct prefix detection including
  "PREFIX|l:P+"). Al-Tawbah is densest host (7 instances).
- **Ring-center negation count**: only Al-Baqarah 2:143 of the 5
  Bonferroni rings contains a NEG token — below 43% base rate. Rings
  structurally prefer questions, not negations.

## Surprises

1. The Shahāda's default is *huwa*, not *Allāh*. The popular ritual
   form is a minority Quranic shape.
2. Meccan/Medinan inversion of *lan*: every other particle is Meccan-
   skewed; lan is Medinan-skewed (54.7%). Absolute-future negation is
   a covenantal-Medinan device.
3. Declarative lā is 4x prohibitive lā. The "thou shalt not" picture
   of Islamic scripture is partly a projection; the Quran's lā is
   mostly descriptive.
4. Al-Ikhlāṣ's density (0.75) is anomalously high for a short surah.
   Its 3-lam cluster carries the theological weight.

## Gaps / limitations

- The 173 divine-apophatic count uses a crude "Allāh/huwa-in-verse"
  filter. A dependency-parse would reclassify some hits.
- I did not separately count `bi-lā` compounds (as a preposition+
  negation construction). QAC treats these as a P prefix + NEG token,
  which my counts pick up under lā.
- I did not investigate Meccan-Medinan contrast within sub-families
  (e.g. does *lā ikrāha* pattern differ from *lā + imperfect* in
  period?). Possible extension.
- No pre-registered tests; the ring-center 1-of-5 result is
  qualitative.

## Runtime

- Morphology parse: ~3 s over 128k tokens.
- Per-particle aggregation + all formula scans: <5 s total.
- CSV output: 114 rows written.

## Files written

- `/findings/phase-b-hypotheses/negation-taxonomy.md` (main output,
  3200 words)
- `/findings/phase-b-hypotheses/negation-per-surah.csv`
- `/journal/negation-taxonomy-run-1.md` (this file)
