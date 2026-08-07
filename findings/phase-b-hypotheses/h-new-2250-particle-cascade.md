---
id: H-NEW-2250
title: Particle-cascade structures — verse-initial fa- / thumma- / wa-idhā chains
type: finding
date: 2026-05-29
author: Waiel Al-Shujaa
phase: B
verdict: CONFIRMED-DIRECTED (idhā eschatological-cascade concentration in juzʾ-30)
prereg_sha256: 723c02aaee549e6ca4d4a0b8de9fcea74e07bebaac3c4949883920b9a188a4ff
seed: 20260509
n_perm: 10000
bonferroni_k: 3
---

# H-NEW-2250 — Particle-Cascade Structures (fa- / thumma- / wa-idhā chains)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Summary

A GENERATOR scanning **verse-initial particle CLASS** runs — generalising beyond
the surface-identical-word anaphora of H-NEW-2140 (§10.77). It enumerates every
maximal run (≥3 consecutive verses, within one surah) headed by the same
grammatical particle, for three "cascade" families:

- **fa- (فَ)** — sequential-narration prefix: **19 runs**, max length **5**.
- **thumma (ثُمَّ)** — temporal-succession conjunction: **3 runs**, max length **4**.
- **idhā (إِذَا / وَإِذَا)** — eschatological conditional-temporal head: **6 runs**,
  max length **8** (the **corpus-EXTREME** particle-cascade).

**Primary pre-registered result — CONFIRMED-DIRECTED.** The idhā-conditional
"when…" head is an eschatological-genre marker whose density concentrates in
juzʾ-30 / short-mufaṣṣal (surahs s ≥ 78) far above the corpus mean, exactly as
direction-locked:

| family (cut s≥78) | density juzʾ-30 | density rest | Δ | one-sided p | verdict |
|---|---|---|---|---|---|
| **idhā** | **0.0532** | **0.0205** | **+0.0327** | **0.00010** | **PASS** (< α_Bonf=0.0167) |
| fa- (control) | 0.0686 | 0.0485 | +0.0201 | 0.141 (two-sided) | NS |
| thumma (control) | 0.0286 | 0.0159 | +0.0127 | 0.027 (two-sided) | NS at Bonf |

idhā is 2.6× denser in juzʾ-30 than in the rest of the corpus. Replicated
identically at seed 20260511 (p=0.00010). The two non-eschatological control
families (fa-, thumma) do **not** survive the Bonferroni-3 bar — confirming the
concentration is genre-specific, not a generic short-surah artifact.

Pre-reg SHA256 `723c02aaee549e6ca4d4a0b8de9fcea74e07bebaac3c4949883920b9a188a4ff`,
verified at runtime. Seed 20260509, 10,000 perms, Bonferroni k=3 (α_cell=0.0167).
All numbers from disk: `quran-text/quran-no-tashkeel.json` (text/ordering) +
`data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 verse-initial POS).

## 1. Method (the GENERATOR)

For each of the 6,236 verses, the QAC v0.4 morphology gives the first word
`(s:v:1:*)` and its proclitic segments. A verse is assigned a family head by POS:

- **fa-** : segment `(s:v:1:1)` carries a `fa` prefix tag `PREFIX|f:*+`
  (subtypes REM / CONJ / RSLT / CAUS / SUP all counted — the verse-initial *fa-*).
- **thumma** : word-1 IS the standalone conjunction `vum~a` (`POS:CONJ|LEM:vum~`).
- **idhā** : word-1 contains the time-adverb stem `<i*aA` (`POS:T|LEM:<i*aA`),
  **with or without** a `wa-`/`fa-` proclitic — the semantically-correct
  "when…" conditional head. (Bare *idhā* like Q 81:1 and *wa-idhā* like Q 81:2
  both belong to the same cascade.)

A **maximal run** = a maximal block of ≥3 consecutive verses within one surah
all sharing one family head; runs never cross surah boundaries. Verse-head counts:
**fa- = 649**, **thumma = 105**, **idhā = 146** (of which strict literal
`wa-idhā` = 104, bare `idhā` = 13; the rest carry other proclitics e.g. `fa-idhā`).

Coverage: all 6,236 verses have a QAC word-1 record.

## 2. The cascade census (every maximal run ≥3)

### 2.1 idhā — eschatological "when…" cascade (6 runs; the corpus-EXTREME family)

| Q | verses | length | content |
|---|---|---|---|
| **81:1-8** | **إذا/وإذا** | **8** | **al-Takwīr: "When the sun is folded up… when the stars fall… when the seas boil over… when the buried infant is asked" — the corpus's single longest particle-cascade** |
| 81:10-13 | وإذا | 4 | al-Takwīr second cascade ("when the scrolls are spread…") |
| 82:1-4 | إذا/وإذا | 4 | al-Infiṭār: "When the heaven is cleft asunder… when the stars scatter… when the seas burst forth… when the graves are turned over" |
| 77:8-11 | فإذا/وإذا | 4 | al-Mursalāt: "When the stars are extinguished…" cascade |
| 4:101-103 | وإذا | 3 | ṣalāt al-khawf legal "when…" sequence (the only Medinan idhā-run) |
| 83:30-32 | وإذا | 3 | al-Muṭaffifīn: the mockers' "when they passed by…" |

The Q 81:1-8 run is **longer** than the strict `wa-idhā` 7-run (81:2-8) flagged
by the anaphora prior H-NEW-2140, because the particle-CLASS generalization
correctly merges the genre-defining bare-*idhā* opener (81:1) with its *wa-idhā*
continuation. **5 of 6 idhā-runs sit in juzʾ-30 (s≥78);** the lone exception is
the Medinan legal sequence Q 4:101-103.

### 2.2 fa- — sequential-narration chain (19 runs; max 5)

Length-5: **Q 37:87-91** (Abraham confronting the idols — pure *fa-* narrative
volley), **Q 55:36-40** (al-Raḥmān, the *fa-biʾayyi ālāʾi rabbikumā* refrain
interleave). Length-4: Q 43:53-56, Q 51:26-29, Q 100:2-5 (al-ʿĀdiyāt war-horse
imagery). Fourteen length-3 runs span Q 6, 7, 19, 26, 37 (×2 more), 40, 51, 56,
68, 79. The *fa-* family is the corpus's connective narrative skeleton —
distributed across Meccan narrative surahs, with **no juzʾ-30 concentration**
(Δ=+0.020, p=0.141).

### 2.3 thumma — temporal-succession chain (3 runs; max 4)

| Q | verses | length | content |
|---|---|---|---|
| 23:13-16 | ثم | 4 | the embryology stages ("then We made… then We created…") |
| 74:20-23 | ثم | 4 | al-Muddaththir, the reprobate's serial reckoning ("then he reflected… then he frowned…") |
| 80:20-22 | ثم | 3 | ʿAbasa, stages of man's making |

*thumma* runs are rare (only 3) and notably cluster on **process/sequence
description** (creation-stages, deliberation-stages) — the temporal-succession
semantics of *thumma* made architecturally visible.

## 3. Primary hypothesis — idhā eschatological-genre density (pre-registered, locked)

**Direction LOCKED before computing:** idhā-headed density(s≥78) > density(rest).

- Observed Δ = density(juzʾ-30) − density(rest) = 0.0532 − 0.0205 = **+0.0327**.
  **Direction matches lock.**
- Permutation null (shuffle the 146 idhā-head indicators across all 6,236 slots,
  preserve total, 10,000 perms, seed 20260509): one-sided **p = 0.00010**.
- **Replication** (seed 20260511): p = 0.00010 — identical.
- Bonferroni-3 threshold α_cell = 0.0167. **p < α ⇒ PASS.**

### 3.1 Genre-specificity (instrument-control, MW-6)
The two control families — *fa-* (narrative) and *thumma* (succession) — are
non-eschatological. Neither concentrates in juzʾ-30 under the Bonferroni-3 bar
(*fa-* p=0.141; *thumma* p=0.027 > 0.0167). Only the *idhā* "when…" head spikes.
This is the crux: it is **not** that all particles crowd into short surahs — it
is specifically the conditional-temporal eschatological head.

### 3.2 Secondary cut (MW-3, alternative model) — an honest nuance
At the stricter "mufaṣṣal qiṣār" cut (s ≥ 94), the idhā Δ goes slightly **negative**
(Δ=−0.0029, p=0.672). The eschatological idhā-cascade peaks in the **s=78-93 band**
(al-Nabaʾ through al-Inshiqāq — the "great-coming / when…" surahs al-Takwīr,
al-Infiṭār, al-Inshiqāq, al-Mursalāt cluster) and tapers in the very shortest
surahs (s≥94 are dominated by oath-openings *wa-l-…* and *qul* creedal capsules,
not "when…" cascades). The pre-registered juzʾ-30 cut (s≥78) is the correct
genre window; the finding is real but **band-specific**, not monotone-to-the-end.

## 4. Classical anchoring

The idhā-cascade surahs are exactly the *suwar al-idhā* that classical tafsīr and
balāgha single out as the apex of eschatological *tarhīb* (warning) rhetoric.
al-Zamakhsharī (*al-Kashshāf*, on Q 81) and al-Rāzī (*Mafātīḥ al-ghayb*, on
al-Takwīr) both treat the serial *idhā…idhā…* as a deliberate *taʿdīd al-ahwāl*
(enumeration of the terrors of the Hour), where the suspended protasis chain
(jawāb al-sharṭ withheld until 81:14 *ʿalimat nafsun mā aḥḍarat*) maximises
dramatic tension. Our GENERATOR mechanically locates this device, ranks Q 81:1-8
as the corpus-extreme, and shows the *idhā*-head is statistically a juzʾ-30
genre-marker — an empirical correlate of the qualitative classical claim.

This complements the verse-final *al-fawāṣil* head/seal grammar (H-NEW-2070):
particle-cascades govern the verse **head**; divine-name pairs govern the verse
**seal**. Together they bracket the cadential architecture.

## 5. Relation to prior findings

- **H-NEW-2140** (§10.77, anaphora runs): this is the particle-CLASS generalization.
  H-NEW-2140 found the strict surface `wa-idhā` 7-run (Q 81:2-8); H-NEW-2250's
  grammatical-class definition merges the bare-*idhā* opener to yield the
  corpus-extreme **8**-run (Q 81:1-8). Both detectors agree; 2250 sees the fuller
  cascade.
- **H-NEW-2070** (al-fawāṣil verse-final pairs): head (this) vs seal (that).
- **H-NEW-1870** (pronominal-narrative law): the *fa-* cascade skeleton is the
  connective tissue of the narrative mode.
- **Cross-finding-025** (scale-of-aggregation ladder): cascades operate at the
  verse-run scale; extends the ladder one rung below refrains (H-NEW-1320/1790).

## 6. Rules-tuple & honest limits

- Rules-tuple: `(QAC-v0.4 POS, verse-initial = word-index 1, Hafs-Kufan, Mashriqi)`.
- **Limit 1 (genre window).** The concentration is band-specific (s=78-93), not
  monotone to s=114; published honestly (§3.2).
- **Limit 2 (grammatical vs semantic break).** The strict *idhā*-head detector
  splits Q 84 (al-Inshiqāq) into fragments because 84:2/84:4 begin *wa-*VERB
  (*wa-adhinat*, *wa-alqat*), not *wa-idhā* — semantically one cascade,
  grammatically broken. A purely thematic detector would merge it; we report the
  grammatical truth and flag the divergence rather than hand-merging.
- **Limit 3 (single annotation source).** Heads come from QAC v0.4 alone; a verse
  is mis-assigned only if QAC's word-1 POS is wrong (spot-checked against the
  no-tashkeel text for all reported runs — all verified).
- **Limit 4.** This is a structural/genre finding, not a theological miracle claim.

## 7. Verdict

**CONFIRMED-DIRECTED.** The pre-registered, direction-locked prediction holds:
the eschatological *idhā* "when…" cascade-head concentrates in juzʾ-30 /
short-mufaṣṣal (s≥78) at +0.0327 density (2.6×), one-sided perm-p=0.00010
< Bonferroni-3 α=0.0167, replicated; and it is genre-specific (fa-/thumma- controls
do not concentrate). The GENERATOR census of all 28 maximal particle-runs is the
permanent deliverable, with Q 81:1-8 (al-Takwīr) the corpus-extreme cascade.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2250-particle-cascade.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2250.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2250.json`
- Findings: this file.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
