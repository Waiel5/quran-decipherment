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

> ### POST-HOC RESULT 2026-08-10 — both diagnostics fire; H2 is reclassified UNINTERPRETABLE
>
> `scripts/h-new-2690-posthoc.py` was written at the time of the primary run and **never executed**.
> It has now been run (`runs/h-new-2690/20260809T095950Z-posthoc/`). Both of its pre-written
> diagnostics fire against this finding. Figures verified from the artefact.
>
> **D2 — the Qurʾān has essentially no metre-specificity above its own matched noise.**
> Median (median baḥr − best baḥr) per unit:
>
> | arm | observed | matched noise | **excess** | n |
> |:--|--:|--:|--:|--:|
> | poetry | 0.12500 | 0.05948 | **2.10×** | 240 |
> | prose | 0.10697 | 0.08916 | **1.20×** | 900 |
> | **Qurʾān** | **0.09091** | **0.08889** | **1.02×** | 899 |
>
> **The instrument works** — poetry separates from its own noise by 2.10×. **The Qurʾān separates by
> 1.02×, i.e. not at all**, and ḥadīth prose shows *more* metre-specificity than the Qurʾān.
>
> **Therefore `inference_verdicts.H2 = "FALSIFIED-buhur-matched"` is RECLASSIFIED UNINTERPRETABLE.**
> H2's criterion flagged 14–16 of 16 buḥūr as "matching"; D2 shows that criterion detects **general
> rhythmic regularity, not conformity to any metre**. A falsification of **al-Bāqillānī** on the
> metricality axis has been standing in this record on an instrument that cannot distinguish the
> Qurʾān from random syllable strings of matched length and heaviness. **It should not be cited as a
> falsification.**
>
> **D1 — H3(b) was never a real test of the text.** Modal best-meter, arm vs its own matched noise:
>
> | arm | modal | share | | noise modal | share |
> |:--|:--|--:|:--|:--|--:|
> | Qurʾān | wāfir | 39.49% | | wāfir | 37.93% |
> | prose | wāfir | 56.67% | | wāfir | 53.44% |
> | poetry | ṭawīl | 58.75% | | ṭawīl | 38.75% |
>
> `D1_quran_and_noise_share_modal: True`. The Qurʾān and its noise return **the same modal metre at
> nearly the same share**; only poetry pulls away. The script's own pre-written reading applies:
> *"the argmin-meter statistic is an instrument attractor and H3(b) was not a real test of the text."*
> H3(b) could not have passed for **any** text of this length and heaviness profile.
>
> **Where that leaves the five registered results:**
>
> | registered | as published | now |
> |:--|:--|:--|
> | H1a Qurʾān less metrical than poetry | PASS | **SURVIVES** |
> | H1b prose less metrical than Qurʾān | PASS | **WITHDRAWN** (H-NEW-2730, unit-length artefact) |
> | H2 no single baḥr matches | FALSIFIED | **UNINTERPRETABLE** |
> | H3(a) mufaṣṣal more metrical than long Medinan | folded into "fail" | **DIRECTION CONFIRMED** +0.07292, p=1e-4 |
> | H3(b) modal metre is rajaz/sarīʿ | fails | **NOT A REAL TEST** |
>
> **One of five survives.** The pre-registration is not edited.

> ## ⚠ CORRECTION 2026-08-10 — this finding's prose contradicts its own run artefact on H3
>
> §3 states that H3 fails because *"the locked direction is not satisfied."* **The run artefact says
> otherwise.** `runs/h-new-2690/20260807T022237Z/result.json` records, in all three pausal tuples:
>
> ```
> H3.direction_ok  = True        <- the direction IS satisfied
> H3.modal_ok      = False
> H3.modal_meter_A = "tawil"
> ```
>
> **H3 fails on clause (b), the modal-meter attribution — not on direction.** The published wording
> therefore conceals a *surviving* directional sub-result: the mufaṣṣal is significantly more metrical
> than long Medinan surahs (diff_B_minus_A = **+0.07292, p = 1×10⁻⁴, replicated**). Correcting this
> **adds** a confirmed result rather than removing one.
>
> **And the refuted half is more strongly refuted than "does not pass" conveys.** Ranking the sixteen
> buḥūr by `H2_per_meter.median_obs` (lower = better fit), **rajaz is 15th of 16 in every tuple**
> (0.33333 / 0.33333 / 0.34336) and takes **zero** modal votes in the mufaṣṣal (ṭawīl 308, wāfir 158,
> madīd 34, munsariḥ 18, kāmil 17, mutaqārib 13). The prediction that sajʿ-dense short surahs sit near
> *rajaz* is not merely unsupported — it is close to inverted.
>
> **A further flag on H2 — NOW SETTLED, see the post-hoc block above; the estimate below was too
> generous and is superseded.** This notice first flagged a metre-specificity spread of
> **1.20× / 1.22× / 1.30×** across the three tuples, computed as a corpus-level median-of-medians
> from `H2_per_meter`, and left the question open pending the post-hoc. **The post-hoc has since run
> and the correct per-unit statistic is 1.02×, not 1.20×.** The aggregate proxy overstated the
> excess; the direction of the concern was right and its magnitude was not. H2 is reclassified
> **UNINTERPRETABLE** on the strength of the per-unit figure, not this one. This is the same
> paired-vs-unpaired defect [[h-new-2730]] §7 used to demote this finding's "metrical structure above
> noise" claim, and it is recorded here as a **replication of that demotion on a second channel** —
> metre-specificity rather than metricality — not as an independent finding.
>
> Also unresolved: [[AUDIT-TANWIN-DELETION-2690]] — this script's `DROP` set deletes 77.66% of the
> corpus's tanwīn before syllabification, in all three pausal tuples. Every quantity above that is
> computed from syllable weight needs re-running under the repaired phonemiser.
>
> The pre-registration is **not** edited. This notice records the discrepancy; it does not rewrite it.

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the scansion three-way ordering does NOT survive a matched control
>
> H-NEW-2690 reported **poetry < this corpus < prose** on `d_min` and read it as
> al-Bāqillānī's *neither* nathr *nor* shiʿr, measured. H-NEW-2730 genre-controlled it.
> **The ordering falls; one of its two legs survives.**
>
> - **The prose leg (H1b) is WITHDRAWN — it is unit length.** Re-cut **this corpus's own
>   verses** to ḥadīth sentence lengths and `d_min` moves **99.4 %** of the way to ḥadīth's
>   value (0.22222 → 0.23953 against al-Dārimī's native 0.23963), using **no baseline text at
>   all**. A matched partition of al-Dārimī lands at **0.22222** — this corpus's own median to
>   five decimals — and one of al-Bukhārī at **0.21893**, with **199 of 200** offsets at or
>   below it. At matched syllable length the two medians are **identical** (0.21739).
> - **The poetry leg (H1a) SURVIVES every length control.** Length explains **5.1 %** of that
>   gap; re-cutting this corpus to bayt lengths moves it only **7.5 %** toward poetry; it holds
>   at full size in the one overlapping length bin (0.21739 against poetry's 0.14815) and
>   passes a per-unit noise control matched on length *and* syllable weight at p = 1 × 10⁻⁴ in
>   both rules-tuples.
> - **`d_min` is not length-invariant in practice.** Length alone explains **28.7 %** of its
>   variance. It normalises by unit length and tiles its templates to unit length, but it is a
>   minimum over ~200 templates and a minimum-of-many falls as the string shortens.
>   **Normalisation is not invariance.**
> - **Matched noise alone reproduces the ordering.** Random strings matched only on length and
>   syllable weight give poetry 0.22222 < this corpus 0.23913 < al-Bukhārī 0.25992 < al-Dārimī
>   0.26549 — the same three-way order, from strings containing no Arabic and no metre. Only
>   **49.2 %** of this corpus's verses are more metrical than their own matched twin — a coin
>   flip — against **88.3 %** of poetry abyāt.
>
> **al-Bāqillānī is untouched**: "neither *nathr* nor *shiʿr*" was never a claim about medians
> of normalised edit distances. What is withdrawn is half of its stated empirical
> operationalisation. **Limit:** there is **no vocalised adab prose on disk**, so al-Jāḥiẓ is
> untestable on this statistic by any means and the prose control is ḥadīth-only.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.5.


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
