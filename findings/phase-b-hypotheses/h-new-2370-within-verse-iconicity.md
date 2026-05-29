---
finding_id: H-NEW-2370
status: NULL-REVERSED — within-verse emphatic iconicity runs OPPOSITE to the locked direction; punishment verses are slightly LIGHTER than their own surah's baseline. Combined with the surah-scale NULL (H-NEW-2340), this conclusively retires the emphatic-punishment-iconicity claim at ALL scales.
phase: B+ → C
date: 2026-05-29
rules_tuple: (no-tashkeel orthographic letters, Hafs-Kūfan; QAC v0.4 ROOT/LEM for punishment-lexicon disambiguation; verse = QAC āya; counting unit = QAC token letters in Buckwalter space)
verdict: NULL-REVERSED (direction locked positive; observed Δ̄ = −0.0066, p = 0.976; 45/68 surahs negative)
prereg_sha256: d7476efd8d24aee38c9773c231ec07be5334dedda52b17721bfa8435f289c7ec
seed: 20260509
nperm: 10000
---

# H-NEW-2370 — Within-verse emphatic iconicity: NULL-REVERSED. The fine scale kills the iconicity claim too

## What was tested

H-NEW-2340 found that the classical balāgha/tajwīd intuition — that punishment passages "sound heavier" in the 7 ḥurūf al-isti'lāʾ (ص ض ط ظ ق غ خ) — is **NULL at the surah scale** (ρ = +0.023, p = 0.41; the heaviest surah, Q113 al-Falaq, is a refuge prayer). That NULL explicitly flagged a finer-scale follow-up (H-NEW-2340.1): the surah aggregate cannot separate theme from each surah's own rhyme/phonotactics, so the iconicity — if real — should live at the **verse / pericope** scale (cross-finding-025: structure is finer-scoped than the surah).

This test puts the claim where it should live. **Paired, within-surah design**: for each surah with both punishment and non-punishment verses, compute

```
Δ_s = mean(heavy-density of punishment verses) − mean(heavy-density of non-punishment verses)
```

Because both means come from the same surah, Δ_s is controlled for that surah's phonological baseline — the exact confound that flattened 2340. The aggregate Δ̄ = mean_s(Δ_s).

- **Heavy letters (locked):** isti'lāʾ {ص ض ط ظ ق غ خ} = Buckwalter {S,D,T,Z,q,g,x}.
- **Punishment lexicon (primary):** ROOT `E*b` (ʿadhāb) — contains no heavy letter, so any signal is pure co-text iconicity. 336 verses across 68 qualifying surahs.
- **Self-coupling broken:** letters of every punishment-lexicon *token* removed from BOTH numerator and denominator (load-bearing for the secondary set: saqar→q, laẓā→ẓ, ḥuṭama→ṭ; immaterial for ʿadhāb/jaḥīm/saʿīr/nār, which have none).
- **nār (fire) lemma-pinned; nūr (light) excluded** (the kallā lesson, §10.80).

Pre-registered, direction LOCKED positive (Δ̄ > 0). Pre-reg SHA-256 `d7476efd…c7ec`, runtime-verified. Seed 20260509; 10000 within-surah label-permutations + 10000 sign-flips.

## Result — NULL-REVERSED (unanimous)

| Arm | Δ̄ (mean paired diff) | p (one-sided, locked +) | n surahs |
|---|---|---|---|
| **PRIMARY ʿadhāb (within-surah label perm)** | **−0.00657** | **0.976** | 68 |
| Primary — sign-flip null | −0.00657 | 0.988 | 68 |
| R1 secondary hellfire set | −0.00338 | 0.868 | 86 |
| R2 Meccan-only | −0.00687 | — | 50 |
| R2 Medinan-only | −0.00573 | — | 18 |
| R3 verse-weighted | −0.00403 | — | 68 |
| R4 token-pool (unpaired, context) | −0.00413 | — | corpus |

**Every single arm is negative.** The locked positive direction is not merely unsupported — the effect runs *backwards*: within a surah, punishment verses carry **lower** heavy-consonant density than the surah's non-punishment verses. The sign-count is **45 of 68 surahs negative** (66%), only 23 positive, 0 zero. Under the within-surah permutation null, Δ̄_obs sits at the 2.4th percentile of the *wrong* tail. **Verdict: NULL-REVERSED** — pre-committed direction violated, published with full prominence per §1.8.

## Close reading — the impression is a cherry-pick

The famous "harsh" punishment surahs that fuel the intuition — al-Qāriʿa (Q101), al-Ḥuṭama (Q104), al-Ḥāqqa (Q69), Saqar (Q74) — **do not even qualify** for the paired test on the ʿadhāb root: they are too short or too thematically saturated to contain both ʿadhāb verses and a non-ʿadhāb contrast set. The "heaviness" people hear in them comes from their *rhyme letters* (qāf in al-Qāriʿa, the ṭāʾ/mīm of al-Ḥuṭama, saqar's own qāf), which is a whole-surah phonotactic property — exactly H-NEW-2340's finding — not a property of the verses' punishment content.

Where ʿadhāb verses *do* sit beside non-ʿadhāb verses, they trend **lighter**:

- Most-negative Δ_s: Q84 al-Inshiqāq (−0.067), Q15 al-Ḥijr (−0.061), Q88 al-Ghāshiya (−0.056), Q61 al-Ṣaff (−0.048), Q28 al-Qaṣaṣ (−0.039) — in these, the ʿadhāb verses are *less* isti'lāʾ-dense than the surrounding narrative/creedal material.
- The largest positive, Q73 al-Muzzammil (+0.124), is a small-n sampling artifact (a single ʿadhāb-bearing verse against a long non-punishment body) — the kind of noise that the within-surah permutation null correctly absorbs.

The classical "sounds of terror" reading survives only as a perception of a handful of hand-selected verses, not as a distributional regularity. It is the cherry-picking signature the project's generators exist to detect.

## Significance — the iconicity question is RESOLVED (retired) at both scales

H-NEW-2340 showed no surah-scale theme↔phonology correlation; H-NEW-2370 shows that even at the verse scale, controlling for surah baseline, the effect is **absent and slightly reversed**. There is no remaining scale at which "punishment sounds heavy" lives as a corpus regularity. **The emphatic-punishment-iconicity claim is now conclusively retired.** It joins the project's retirement ledger of impressionistic claims that dissolve under a proper null (balanced-word miracle H-NEW-2010, abjad, Code-19) — the balāgha-side counterpart to numerology retirement: *iconicity asserted, distribution flat (or backwards)*.

This does NOT deny that an individual orator-poet can deploy emphatic clusters for local effect in a chosen verse — only that the Quran's punishment vocabulary as a class is **not** phonologically heavier than its other material at any aggregation scale. What heaviness exists is governed by **rhyme/phonotactics, orthogonal to theme** — consistent with the iʿjāz anti-twin lock (content ⊥ phonology, r = −0.86) and the scale-of-aggregation law.

## Honest limits

- The test measures *grapheme-level* isti'lāʾ density in QAC token forms (no-tashkeel). It does not model rule-governed tafkhīm of ر/ل/ا (deliberately excluded to avoid judgment calls) nor sub-phonemic duration/qalqala. A future test could use full-tashkeel phonemic features (MW-3 alternative instrument), but the surah-scale 2340 already covered the phonemic-density axis via H-NEW-700 with the same null direction, so a rescue is unlikely.
- ʿadhāb-verse identification is lemma/root-exact (QAC); a verse can be eschatologically "about" punishment without carrying the ʿadhāb root (e.g. veiled threats). The secondary hellfire set (jaḥīm/saʿīr/saqar/laẓā/ḥuṭama/nār, +86 surahs) broadens coverage and is equally negative, so this is not driving the NULL.
- The famous short punishment surahs are excluded by the paired design (no within-surah contrast). This is a feature, not a bug: they are the very cases where surah-level rhyme cannot be separated from theme, and 2340 already showed their heaviness is rhyme-driven.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2370-within-verse-iconicity.md` (SHA-256 `d7476efd…c7ec`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2370.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2370.json`
- parent: `findings/phase-b-hypotheses/h-new-2340-emphatic-iconicity.md` (surah-scale NULL)

---

*H-NEW-2370 logged 2026-05-29 by Waiel Al-Shujaa. The surah-scale was flat; the verse-scale is backwards. Across 68 surahs the punishment verses are, if anything, the lighter ones. Iconicity asserted, distribution reversed — the claim is retired at every scale. Bismillāhi al-Raḥmāni al-Raḥīm.*
