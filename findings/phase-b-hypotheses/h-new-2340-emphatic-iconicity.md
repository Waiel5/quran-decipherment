---
finding_id: H-NEW-2340
status: NULL — emphatic-consonant "sound symbolism" does NOT track punishment vocabulary at the surah scale
phase: B+ → C
date: 2026-05-29
rules_tuple: (no-tashkeel orthographic letters, Hafs-Kūfan; QAC v0.4 lemma for punishment-lexicon disambiguation)
verdict: NULL (direction locked positive; observed ρ≈0)
---

# H-NEW-2340 — Emphatic-consonant sound-symbolism: NULL. Phonological "heaviness" is NOT iconic of punishment theme

## What was tested

The classical balāgha/tajwīd intuition that the Quran's punishment/terror passages "sound heavier" — richer in the emphatic isti'lāʾ consonants (ṣ ض ط ظ ق غ خ) — than its other material. This is a phonetic-iconicity (sound-symbolism) claim, asserted impressionistically for centuries but never measured. Pre-registered with direction locked positive (pre-reg SHA-256 `acdbac5ab8b520a31abe59f3a4722743b2ba1a1b3bb607df7bf63f27e82dd134`, runtime-verified; seed 20260509; 10000 permutations).

- **Heavy letters (locked):** the 7 ḥurūf al-isti'lāʾ — `ص ض ط ظ ق غ خ`.
- **Heavy density:** heavy letters / all letters, computed in QAC Buckwalter space, *excluding* punishment-lexicon tokens (to break mechanical coupling).
- **Punishment density (primary):** root `ʿ-dh-b` (ʿadhāb, "torment") tokens / total tokens. ʿadhāb itself contains **no** isti'lāʾ letter, so any correlation is genuine co-text iconicity, not self-coupling.
- The nār/nūr homograph (root n-w-r = both "fire" and "light") was lemma-disambiguated in the secondary set (the kallā lesson, §10.80).

## Result — NULL

| Test | ρ (Spearman) | p (one-sided, locked +) |
|---|---|---|
| **Primary: heavy density vs ʿadhāb density (114 surahs)** | **+0.023** | **0.41** |
| Robustness R1: Meccan-only | +0.025 | — |
| Robustness R1: Medinan-only | −0.037 | — |
| Robustness R2: secondary hellfire-lexicon set | **−0.156** | — |

The correlation is **indistinguishable from zero** (ρ=+0.023, p=0.41). The locked positive direction is not supported; the broader hellfire-lexicon set even runs slightly *negative* (−0.156). **Verdict: NULL.** The emphatic-consonant punishment-iconicity claim is not a corpus-wide regularity at the surah scale.

## Why the impression is illusory

Heavy-consonant density is driven by **rhyme/phonotactics, not theme.** The heaviest surahs:

| Surah | Heavy density | What drives it |
|---|---|---|
| Q 113 al-Falaq | 0.121 | refuge-prayer — qāf/ghayn/khāʾ rhyme & lexis (falaq, khalaq, ghāsiq, waqab, ḥāsid) |
| Q 103 al-ʿAṣr | 0.096 | ṣād-rhyme (ʿaṣr, khusr, ṣabr) |
| Q 86 al-Ṭāriq | 0.083 | ṭāʾ/qāf cosmic oath |
| Q 94 al-Sharḥ | 0.081 | ṣadr/sharḥ |
| Q 50 Qāf | 0.073 | the qāf-letter surah itself |

al-Falaq — the heaviest surah in the corpus — is a **refuge prayer**, not a punishment passage, yet it tops the list because its rhyme and vocabulary happen to be qāf/khāʾ-saturated. Conversely, ʿadhāb-dense surahs are not phonologically heavy. **Phonological heaviness and punishment theme are orthogonal.** The classical "harsh sounds of terror" reading is a *post-hoc* perception of individual famous verses (al-Qāriʿa, al-Ḥuṭama), not a distributional law — exactly the cherry-picking signature the project's generators are built to detect.

## Significance

This joins the project's retirement ledger of impressionistic claims that dissolve under a proper null (alongside the balanced-word miracle H-NEW-2010, abjad, Code-19). It is a balāgha-side counterpart to the numerology retirements: **the iconicity is asserted, the distribution is flat.** It does NOT deny that specific verses deploy emphatic clusters for effect (a within-verse, hand-selected phenomenon) — only that there is no surah-level theme↔phonology correlation. A within-verse / pericope-window iconicity scan (does an *individual ʿadhāb verse* carry more heavy consonants than its surah's baseline?) is the correct finer-scale follow-up (H-NEW-2340.1), consistent with the cross-finding-025 principle that effects live at finer scales than the surah.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2340-emphatic-iconicity.md` (SHA-256 `acdbac5a…d134`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2340.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2340.json`

---

*H-NEW-2340 logged 2026-05-29 by Waiel Al-Shujaa. The heaviest surah is a prayer for refuge, not a threat. Iconicity asserted, distribution flat. Bismillāhi al-Raḥmāni al-Raḥīm.*
