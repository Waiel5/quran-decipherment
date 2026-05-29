# Pre-registration — H-NEW-2340: Emphatic-consonant sound-symbolism (does phonological "heaviness" track punishment vocabulary?)

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE computation)
**Seed:** 20260509 · **Permutations:** 10000
**Rules-tuple:** (no-tashkeel orthographic letters, Hafs-Kūfan; QAC v0.4 lemma for the punishment-lexicon disambiguation)

## Background & the iconicity claim

Classical balāgha and tajwīd note that the "heavy" emphatic letters (ḥurūf al-isti'lāʾ / tafkhīm) give a harsh, weighty acoustic texture — and that the Quran's punishment/terror passages (al-Qāriʿa, al-Ḥuṭama, Saqar) "sound" heavier than its mercy passages. This is a sound-symbolism (phonetic-iconicity) claim, asserted impressionistically for centuries but, to our knowledge, never measured on the corpus. We test it.

## Definitions

- **Heavy letters (locked set):** the 7 ḥurūf al-isti'lāʾ — `ص ض ط ظ ق غ خ`. (Fixed classical tajwīd category; not data-selected. `ر`/`ل`/`ا` tafkhīm is context-dependent and excluded to avoid judgment calls.)
- **Heavy-consonant density of a surah:** (count of heavy letters) / (count of all Arabic consonant+long-vowel letters), computed over the surah text **after removing the tokens of the punishment lexicon** (to break the mechanical coupling whereby some punishment-words themselves contain heavy letters, e.g. saqar, ḥuṭama).
- **Punishment-vocabulary density:** (punishment-lexicon tokens) / (total tokens), per surah.
- **Punishment lexicon (locked, QAC-lemma disambiguated):** primary = root `ʿ-dh-b` (عذب, "torment/punishment" — unambiguous). Secondary robustness set adds hell-fire terms via QAC lemma to **avoid the nār/nūr homograph** (root n-w-r is shared by نار "fire" and نور "light"): include only lemma `nār` (fire), plus `jaḥīm`, `saʿīr`, `saqar`, `laẓā`, `ḥuṭama`. The نور "light" lemma is EXCLUDED.

## Primary hypothesis (direction LOCKED)

> **H1:** Across the 114 surahs, heavy-consonant density (computed on non-punishment text) is **positively** correlated with ʿadhāb-density.
> Statistic: Spearman ρ. Null: permute the surah-pairing (shuffle which surah's heaviness is matched to which surah's ʿadhāb-density), 10000×, seed 20260509. One-sided p = fraction of |null ρ| ≥ ρ_obs in the locked (positive) direction.

If ρ_obs ≤ 0 (reversed/absent), publish as NULL with full prominence.

## Confound control (pre-specified, gating the interpretation)

The full-corpus correlation may be driven by the Meccan register (short Meccan surahs may have both more eschatology and different phonology). Therefore:
- **Robustness R1:** recompute ρ within Meccan surahs only. If the effect is purely a Meccan-vs-Medinan artifact, R1 vanishes — reported honestly either way.
- **Robustness R2:** recompute with the secondary hell-fire lexicon added.

**Verdict logic:** CONFIRMED requires H1 pass (p<0.05, positive) AND R1 same-sign. If H1 passes but R1 vanishes, verdict = CONFIRMED-BUT-REGION-CONFOUNDED (the iconicity is a register effect, not a within-register one). If H1 fails, NULL.

## Quality gates

- Direction locked; reversal → NULL with prominence.
- All counts from quran-text/quran-no-tashkeel.json + QAC lemma; no values from memory.
- Homograph nār/nūr explicitly disambiguated (the kallā lesson, §10.80).

## Files

- This pre-reg (SHA-256 self-locked; embedded in scripts/h-new-2340.py, runtime-verified)
- scripts/h-new-2340.py · csv/h-new-2340.json · h-new-2340-emphatic-iconicity.md
