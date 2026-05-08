---
id: h-new-960-run-1
date: 2026-05-07
specialist: cross-corpus-rhyme-specialist
phase: B
parent_finding: H-NEW-960
prereg_sha256: 332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19
seed: 20260507
n_bootstrap: 10000
verdict: NULL-RESIDUAL-LIVES-IN-COMPOSITE — direction REVERSED, 0/4 quartiles pass
---

# H-NEW-960 Run-1 Journal

## Timeline

- **2026-05-07 — pre-flight reading complete**: read INVESTIGATION-PROTOCOL §1-12, SKILL.md, HANDOFF/04-DISCIPLINE, h-new-740 + h-new-700 in full, h-new-700.json structure, baseline-corpora/raw/ inventory.

- **2026-05-07 — pre-reg drafted**: `findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy-prereg.md`. Locked H1 direction LOWER (Q < poetry). Bonferroni-4 quartile family (α_bon=0.0125) pre-declared in YAML frontmatter per PRE-REG-STANDARD-04. SHA256 = `332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19`.

- **2026-05-07 — script written**: `scripts/h_new_960_cross_corpus_rhyme_entropy.py`. SHA-locked at runtime; fail-fast on mismatch. Cloned letter-normalization + bayt-line heuristic from H-NEW-740 (auditable provenance). Wilcoxon signed-rank with mid-rank ties + continuity correction implemented from scratch (stdlib only, no scipy).

- **2026-05-07 — primary run**: SHA verified. Loaded 114 surahs / 6236 verses (min-tashkeel) and 13 poetry files / 35 sections / 6618 bayts. All 114 surahs paired with within-section poetry blocks (0 cross-section fallbacks).

  **Result**: Mean H(Quran) = 1.111 bits, Mean H(Poetry) = 1.038 bits, Mean Δ = +0.0724 bits, Wilcoxon p_one_sided_lower = 0.847.
  Quartiles: 0/4 pass at α_bon=0.0125. VS, S, M strongly reversed (Δ +0.30, +0.28, +0.51). L marginally negative (Δ −0.08).

- **2026-05-07 — post-observation diagnostic**: ran no-default-section robustness check (excluded `default` qāfiya bucket containing diwan-antara's 2606-bayt undivided block). Result: Δ = +0.260 (more reversed), p_one_sided_lower = 0.996. **Direction-reversal STRENGTHENED under the cleaner monorhyme corpus.**

- **2026-05-07 — verdict assigned**: NULL-RESIDUAL-LIVES-IN-COMPOSITE. Direction REVERSED → published as NULL with prominence per Protocol §1.8. Substantive residual interpretation: H-NEW-740's cross-corpus iʿjāz al-fawāṣil composite distinctness does not transmit to the letter-axis alone; classical *iʿjāz al-fawāṣil* is properly composite, not letter-uniformity.

## Decision points

1. **Sampling scheme**: pre-reg §4.4 chose within-section sampling with cross-section fallback. Alternative considered: bootstrap-many matched-length blocks per surah. Chosen single-sample for clean Wilcoxon paired test. Direction-bias if cross-section fallback used: HIGHER poetry entropy (favor H1). Run produced 0 cross-section fallbacks; favorability not exercised.

2. **Quartile cuts**: V<5, 5-10, 11-20, V>20 chosen from project mufaṣṣal-tier boundaries before any data observation. Locked in pre-reg §2 H2.

3. **Default-section inclusion**: pre-reg sampled default sections as legitimate (per H-NEW-740 standard). Post-hoc robustness check excluded them as diagnostic only — does NOT alter primary verdict (single primary test). The robustness check serves only to confirm the direction is robust, not to relitigate H1.

4. **Stat choice**: Wilcoxon paired one-sided LOWER (per pre-reg). Sign-test (median Δ test) would give similar reversal direction.

5. **Garden-of-forking-paths**: NO post-observation cuts re-run, NO direction flip, NO α loosening. The pre-reg's H3 NULL band ("RHYME-LETTER-AXIS EQUAL OR FAVOR POETRY") was explicitly anticipated and is the verdict actually reached.

## Key empirical observations

- **Mechanism**: Quran's bimodal architecture (long-Q ultra-monorhyme >100 verses; short-Q multi-rhyme) crosses with poetry's qaṣīda monorhyme convention (uniform within ~30-150 bayt qāfiya-section).
- **Long-surah regime**: Q23, Q4, Q19, Q6, Q26 all Δ < −2.9 bits. Quran sustains single-rāwī monorhyme over 100-200+ verses; no pre-Islamic qaṣīda qāfiya-section reaches this length.
- **Short/medium-surah regime**: Q14, Q89, Q42, Q22, Q88 all Δ > +1.8 bits. Within-qāfiya poetry blocks are 100%-monorhyme by convention; Quran's short surahs use multi-letter rāwī schedules.
- **8 Quran surahs at H=0** (perfect monorhyme): Q48, 54, 63, 72, 76, 91, 92, 97. Top max H = Q14 Ibrāhīm at 2.757 bits.

## Cross-finding implications

- H-NEW-740 unimpeached: the composite (content × rhyme) iʿjāz signature is unaffected by this letter-axis-alone null.
- H-NEW-700 vindicated: the per-surah top-letter dominance pattern that H-NEW-700 documents is exactly the bimodal architecture that drives H-NEW-960's reversal.
- al-Suyūṭī *Itqān* nawʿ 56 (conservative non-attribution of meaning to *rawiyy* choice): EMPIRICALLY VINDICATED again. Letter-axis features are orthogonal to whole-surah meaning and (per H-NEW-960) are not even cross-corpus-distinct.
- al-Bāqillānī *iʿjāz al-fawāṣil*: empirically LOCATED at the composite layer (H-NEW-740), not the letter-uniformity layer (H-NEW-960 NULL).

## Files produced

- Pre-reg: `findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy-prereg.md`
- Script: `scripts/h_new_960_cross_corpus_rhyme_entropy.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-960.json`
- Findings: `findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy.md`
- Journal: this file

## SHA verification log

```
Pre-reg SHA: 332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19
Expected:    332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19
[MATCH — proceed]
```

*Bismillāhi al-Raḥmāni al-Raḥīm.*
