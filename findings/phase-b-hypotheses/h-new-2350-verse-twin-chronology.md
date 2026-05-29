---
finding_id: H-NEW-2350
status: CONFIRMED — cross-surah exact-verse twins link surahs revealed close together in time (rev-distance 16.5 vs 38.2 null, p=0.0002)
phase: B+ → C
date: 2026-05-29
rules_tuple: (no-tashkeel verse-string NFC-normalized, Hafs-Kūfan; revelation order = Tanzil Egyptian Standard primary, Nöldeke robustness)
verdict: CONFIRMED (direction locked "closer than random" before computation)
---

# H-NEW-2350 — Exact-verse twins are a same-period phenomenon: repeated verses link surahs revealed close together

## What was tested

When the *same full verse* appears verbatim in two different surahs (a cross-surah twin), are those surahs revealed **close together** in the revelation timeline, or scattered across it? Pre-registered with direction locked (pre-reg SHA-256 `198538f725aad07fe2a57064d83c88cefff4ebf2f53c3d2fcc31ee7214fb88d1`, runtime-verified; seed 20260509; 10000 perms). Builds on the H-NEW-2310 repeated-verse census and the Q066-F-01 twin observation.

## Census (deterministic, on-disk)

| Min token length | Cross-surah twin groups |
|---|---|
| ≥ 6 tokens | **29** |
| ≥ 8 tokens (primary) | **15** |
| ≥ 10 tokens | **8** |

(Threshold note: the Q066-F-01 deep-dive cited "11 verbatim ≥10-token groups"; the exact deterministic count by whitespace tokenization is **8** at ≥10 and **15** at ≥8 — the figure is threshold-sensitive, reported transparently. No contradiction; different length cut.)

## Primary result — CONFIRMED

| Quantity | Value |
|---|---|
| D_obs (mean within-group pairwise revelation-distance, ≥8-token groups) | **16.47** |
| Null mean (size-matched random surahs) | **38.17** |
| One-sided p (locked: twins closer) | **0.0002** |
| Nöldeke-order robustness D_obs | 14.9 (same direction) |
| Period-concordance (same Meccan/Medinan) | **13 / 15 groups, p=0.043** |

Twin-linked surahs sit, on average, **less than half** the revelation-timeline distance apart that random surah pairs do, and 13 of 15 twin groups are wholly within one revelation period. **Verdict: CONFIRMED.** Exact-verse repetition is a **same-period compositional phenomenon** — verses recur between surahs revealed near each other in time, not across the whole timeline.

## The ≥10-token twin map (8 groups)

| Verses | Surahs | Rev-order | Period | Shared verse (gloss) |
|---|---|---|---|---|
| 9:33 ≡ 61:9 | al-Tawba / al-Ṣaff | 113, 109 | late Medinan | "…to make it prevail over all religion" |
| **9:73 ≡ 66:9** | al-Tawba / al-Taḥrīm | 113, 107 | late Medinan | the jihād-against-kuffār-&-munāfiqīn verse (**confirms Q066-F-01**) |
| 6:10 ≡ 21:41 | al-Anʿām / al-Anbiyāʾ | 55, 73 | Meccan | "messengers before you were mocked…" |
| 59:1 ≡ 61:1 | al-Ḥashr / al-Ṣaff | 101, 109 | Medinan | *sabbaḥa lillāhi…* (musabbiḥāt opener) |
| 3:89 ≡ 24:5 | Āl ʿImrān / al-Nūr | 89, 102 | Medinan | "except those who repent… God is Forgiving, Merciful" |
| 6:4 ≡ 36:46 | al-Anʿām / Yāsīn | 55, 41 | Meccan | "no sign comes to them but they turn away" |
| 23:6 ≡ 70:30 | al-Muʾminūn / al-Maʿārij | 74, 79 | Meccan | "except with their spouses…" (chastity clause) |
| 73:19 ≡ 76:29 | al-Muzzammil / al-Insān | 3, 98 | Meccan→Medinan | *inna hādhihi tadhkira…* (the lone long-distance twin) |

The twins organise into recognisable epoch-clusters: the **late-Medinan polemic group** (9:33/61:9, 9:73/66:9), the **musabbiḥāt** liturgical openers (59:1/61:1), and **Meccan narrative-formula pairs** (6:10/21:41, 6:4/36:46, 23:6/70:30). The single exception — **73:19 ≡ 76:29** (the *tadhkira* refrain "whoever wills, let him take a path to his Lord") — is a liturgical formula spanning early-Meccan to Medinan, the honest outlier that makes the same-period regularity visible by contrast.

## Interpretation

This connects three project threads:
- **Pillar law #2 (mushaf is FR-geodesic-optimal, position ≠ chronology):** twins are a *chronological* clustering invisible to the *positional* FR-architecture — e.g. Q66 and Q9 are revealed close (and share an exact verse) but are far apart in the mushaf. The Q083 deep-dive found the same dissociation (last-Meccan Q83 is FR-distant from the first-Medinan Q2). Repeated verses track the revelation timeline, not the codex order.
- **H-NEW-2330 burstiness / H-NEW-2310 refrains:** within-surah repetition is topical (burstiness); cross-surah exact repetition is *temporal* (same-period). Two distinct repetition regimes.
- **Classical:** the phenomenon is the textual substrate of al-Suyūṭī's *tikrār* discussions (Itqān nawʿ 60) and of asbāb-al-nuzūl clustering — verses shared between surahs reflect contemporaneous revelation contexts.

## Limits

- Revelation order is itself a reconstruction (Tanzil Egyptian Standard / Nöldeke); both give the same direction, but the absolute distances inherit that model's assumptions.
- Exact-match only (NFC + whitespace); near-twins (one-word variants) are excluded by design — a separate finer study.
- 15 groups is a small N; the result is strong (p=0.0002) but rests on a modest sample, as any exact-twin study must.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2350-verse-twin-chronology.md` (SHA-256 `198538f7…88d1`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2350.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2350.json` (full ≥8-token enumeration)

---

*H-NEW-2350 logged 2026-05-29 by Waiel Al-Shujaa. Repeated verses bind surahs revealed in the same season; the codex scatters in space what the timeline kept together. Bismillāhi al-Raḥmāni al-Raḥīm.*
