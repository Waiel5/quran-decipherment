---
finding_id: h-new-222
title: Additional classical chronologies — Fisher-Rao path length comparison
status: pre-registered
bonferroni_family: h-new-222
bonferroni_k: 4
alpha_bon: 0.0125
seed: 20260419
date_prereg: 2026-04-17
parent_lineage: [H-NEW-111, H-NEW-212]
---

# [[h-new-222-more-chronologies|H-NEW-222]] — Additional classical chronologies under Fisher-Rao

## Motivation

[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] tested mushaf against four published chronologies (Egyptian 1924,
Nöldeke 1860, Bell 1937, Blachère 1947) and confirmed mushaf still wins.
[[h-new-222-more-chronologies|H-NEW-222]] broadens the classical arm: explicitly test two **traditional
Islamic** chronologies (Ibn ʿAbbās / ʿAbd al-Kāfī version; al-Suyūṭī
al-Itqān via Jaʿbarī–Zanjānī), VERIFY the Tanzil/Egyptian Standard ordering
(already tested as `egyptian_1924` in [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] — included here as a
sanity-check replication), and test Watt-Bell Introduction (1970) — Watt's
revision of Bell's 1937 work, a modern Western academic consensus
reconstruction distinct from Bell 1937 tested earlier.

## Pre-registered chronologies

1. **Ibn ʿAbbās (ʿAbd al-Kāfī version)** — the most widely circulated
   traditional Islamic ordering attributed to Ibn ʿAbbās (d. 687 CE), in
   the 15th-century ʿAbd al-Kāfī transmission widely reproduced by
   Robinson (2003) and understandingislam.today. Differs from Egyptian
   Standard mainly in the ordering of the final Medinan group (e.g.,
   surahs 110, 49, 9, 5, 22, 24, 63, 48, 66, 62, 64, 61).
2. **al-Suyūṭī al-Itqān (Jaʿbarī–Zanjānī transmission)** — Suyūṭī's
   preferred chronology as transmitted via Jābir b. Zayd (Itqān fī
   ʿulūm al-Qurʾān, vol. 1, nawʿ 7). Differs from Ibn ʿAbbās primarily
   in the ordering of surahs 83, 99, 4, and 5. Documented in al-Zanjānī's
   *History of the Quran*.
3. **Tanzil / Egyptian Standard 1924** — ALREADY tested in [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] as
   `egyptian_1924`. Included here as a **sanity-check re-test** (expect:
   exact same L as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], ~89.5297). If L_tanzil in this run ≠
   [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]'s L_egyptian within 1e-4, the run is INSTRUMENT-BROKEN.
4. **Watt-Bell Introduction 1970 (4-phase)** — W. Montgomery Watt's
   revision of Bell's 1937 Introduction (ch. 7), Edinburgh University
   Press 1970. Uses Nöldeke's 4-phase framework (First Meccan, Second
   Meccan, Third Meccan, Medinan) but with Watt's own within-phase
   ordering based on content + stylistic criteria. Distinct from
   Bell 1937 (which is by pericope-date) and from Nöldeke 1860.

## Hypothesis family (Bonferroni k=4)

Acknowledged test family (1-sided lower-tail):

- **PRIMARY-1** — L_ibn_abbas vs null. Is L < random?
- **PRIMARY-2** — L_suyuti_itqan vs null. Is L < random?
- **PRIMARY-3** — L_tanzil (sanity-check replication) vs null.
- **PRIMARY-4** — L_watt_bell vs null. Is L < random?

Bonferroni k=4, α_bon = 0.05 / 4 = 0.0125 per test.

## Primary question: which ordering is SHORTEST?

Descriptive ranking of {L_mushaf (ref), L_ibn_abbas, L_suyuti_itqan,
L_tanzil, L_watt_bell, L_random_mean}. Pre-committed sign-flip
prohibition: no post-hoc rationalization of which chronology "wins".

## Secondary (no Bonferroni cost; descriptive only)

- Spearman ρ between each new chronology and the mushaf / Nöldeke / Bell.
- L_c − L_mushaf (raw and in null-SD units).
- Cross-check: L_tanzil here vs L_egyptian in [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] must match (1e-4).

## MW protections

- **MW-1 length control**: inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (L1-normalized).
- **MW-5 positive control**: inherited (greedy-NN-from-surah-1).
- **Instrument sanity**: L_tanzil ([[h-new-222-more-chronologies|H-NEW-222]]) − L_egyptian ([[h-new-212-alt-chronology-fisher-rao|H-NEW-212]])
  must be < 1e-4 absolute. Broken iff violated.

## Locked parameters

- seed: 20260419 (same as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], which yielded identical null under
  same D matrix — this is DELIBERATE so leaderboard is directly
  comparable to [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]'s leaderboard).
- permutations: 10000
- D matrix: loaded from `findings/phase-b-hypotheses/csv/h-new-111.json`
- rules-tuple: inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC STEM roots, top-500,
  Dirichlet α=0.5, L1-normalized, basmala-in-surah-1-only).

## Acceptance window

For each chronology c ∈ {ibn_abbas, suyuti_itqan, tanzil, watt_bell}:
- PASS if p_c (1-sided lower) < α_bon = 0.0125
- NULL otherwise

Family PASS: at least one chronology passes AND mushaf (reference;
not in family) is shorter than all passing chronologies.

"Does mushaf still win?" = YES if **no** chronology has L_c ≤ L_mushaf.

## Garden of forking paths (logged BEFORE run)

1. **Ibn ʿAbbās list choice**: adopted the ʿAbd al-Kāfī transmission
   (Robinson 2003; understandingislam.today) because it is the most
   widely cited in English-language scholarship. Alternatives exist
   (Mujāhid, ʿAṭāʾ al-Khurāsānī transmissions) but differ only in
   a handful of Medinan orderings. Sensitivity: if a rank swap of
   ±3 positions in the Medinan tail is applied, L changes by < 0.1
   raw (< 0.06 null-SDs). Does not alter verdict direction.
2. **al-Suyūṭī list**: preferred the Jaʿbarī-Zanjānī transmission
   (documented in al-Zanjānī's *Tārīkh al-Qurʾān*, which is Tanzil's
   source). Differences from Ibn ʿAbbās confined to <6 positions.
3. **Watt-Bell**: used the 4-phase framework from truthnet's transcription
   of Watt-Bell ch. 7. Within each phase, order is Watt's reported order
   (not a re-sorting). Imputations: none needed — all 114 surahs are
   placed by Watt within one of the 4 phases with explicit within-phase
   order.
4. **Tanzil inclusion**: included in k=4 family despite being
   prior-tested to make Bonferroni correction explicit and conservative
   (tightening, not loosening α, permitted per feedback
   Bonferroni-tightening rule).
5. **Seed reuse**: deliberately reused [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]'s seed 20260419 so the
   same null-draw is applied — leaderboards are directly
   concatenable. This is NOT p-hacking (no change in decision rule);
   it maximizes cross-study comparability.
6. Tie-breaking for duplicate ranks in any chronology: mushaf-order
   ascending secondary sort.

## Output

- JSON: `findings/phase-b-hypotheses/csv/h-new-222.json`
- Analysis MD: `findings/phase-b-hypotheses/h-new-222-more-chronologies.md`
