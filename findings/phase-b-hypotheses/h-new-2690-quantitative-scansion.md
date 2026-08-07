---
id: H-NEW-2690
title: Real quantitative scansion — the Qurʾān sits BETWEEN poetry and prose on metricality
date: 2026-08-07
author: Waiel Al-Shujaa
status: PARTIAL — H1a and H1b PASS in both rules-tuples (poetry < Qurʾān < prose); H2 and H3 do NOT pass
prereg: prereg-h-new-2690-quantitative-scansion.md
run: runs/h-new-2690/20260807T022237Z/
seed: 20260509
---

# H-NEW-2690 — al-Bāqillānī's "neither prose nor poetry", measured

**Verdict: PARTIAL. The positive control PASSED, and the two locked ordering hypotheses PASS in
both rules-tuples. H2 and H3 do not.**

## 1. The instrument works — the gate that had to be cleared first

The pre-registration made the muʿallaqāt a hard gate: **report meter-recovery accuracy before
any Qurʾān number, and if the scanner cannot recover known meters, report that the scanner is
broken instead.**

| poem | known meter | recovered | per-bayt accuracy |
|:--|:--|:--|--:|
| Muʿallaqa of Imruʾ al-Qays | *ṭawīl* | **ṭawīl** | 0.680 |
| Muʿallaqa of Zuhayr | *ṭawīl* | **ṭawīl** | 0.968 |
| Muʿallaqa of ʿAmr b. Kulthūm | *wāfir* | **wāfir** | 0.718 |

**3/3 poems correct, 0.771 per-bayt accuracy over 240 abyāt.** `control_gate_passed: true`.

This is real scansion: CV templates and sabab/watid sequences extracted from the vocalised text,
not the letter-count proxy of H-NEW-48. That earlier test modelled each baḥr as a Gaussian
centred at 1.6 × syllables_per_bayt and compared **verse letter-counts** — it never extracted a
template and never scanned anything. This supersedes it rather than replicating it.

Vocalisation coverage of `quran-full-tashkeel.json`: **0.918**.

## 2. The result — the Qurʾān is intermediate

Statistic: `d_min`, length-invariant distance to the nearest classical metrical template
(lower = more metrical). Both locked hypotheses pass, in **both** rules-tuples:

| tuple | n (Qurʾān) | median d_min | H1a Qurʾān > poetry | H1b prose > Qurʾān |
|:--|--:|--:|:--|:--|
| P_forceheavy | 6211 | 0.2222 | **PASS**, p = 1×10⁻⁴ | **PASS**, p = 1×10⁻⁴ |
| P_pausal | 6209 | 0.2188 | **PASS**, p = 1×10⁻⁴ | **PASS**, p = 1×10⁻⁴ |

So the ordering is **poetry < Qurʾān < prose**: the Qurʾān is measurably *less* metrical than
classical poetry and measurably *more* metrical than prose. Both directions were locked before
computing, and both replicate. Qurʾān median d_min 0.2222 vs its own phoneme-shuffled noise
floor 0.2394 — metrical structure above noise, but not poetry's.

**This operationalizes al-Bāqillānī's *Iʿjāz al-Qurʾān* claim that the text is neither *nathr*
nor *shiʿr*** — as a measured intermediate position rather than a rhetorical assertion.

## 3. What does NOT pass — reported with equal prominence

- **H2 (no single baḥr match): does NOT pass.** The registered no-match criterion was not met.
- **H3 (short mufaṣṣal closer to *rajaz*/*sarīʿ* than long Medinan): does NOT pass** — the
  statistic is significant but the locked direction is not satisfied.

Two of four registered hypotheses fail. The headline is H1a/H1b only.

## 4. Honest limits — and the one that matters most tonight

1. **This has NOT had the H-NEW-2720 treatment.** Tonight's sweep found that 0 of 9 standing
   laws discriminate the Qurʾān from *length-matched partitions* of Bukhārī and al-Jāḥiẓ, and
   that **unit size alone explained 91.5% of the compression tail and half the anti-twin**.
   `d_min` is designed to be length-invariant and the three-way ordering is harder to fake than
   a two-way extremity claim — but **designed-to-be-invariant is not the same as verified-
   invariant.** A matched-partition control on this statistic is REQUIRED before this is cited
   as a discriminating result. Until then treat it as promising and unconfirmed.
2. The prose baseline is a corpus, not a matched partition. See limit 1.
3. Template inventory and pausal handling are modelling choices; both tuples agree, which helps,
   but neither is the classical ʿarūḍ tradition's own procedure.
4. Nothing here shows the position is unique to the Qurʾān among religious or elevated Arabic
   prose — no such control was run.

## 5. Cross-references

- Supersedes **H-NEW-48** (length-distribution proxy, no scansion).
- The required next step is a **H-NEW-2720-style matched-partition control** on `d_min`. Given
  that sweep's outcome, the honest prior is that this may not survive it. It is published now
  because the positive control passed and the directions were locked — not because it is safe.
