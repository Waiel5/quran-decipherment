---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-06
date_last_updated: 2026-05-29
phase: B+
verdict: NULL (pre-commit honoured) — Āyat al-Kursī is lexically REDUNDANT with its neighbours, not a local lexical peak
prereg_sha: 7044eb7477d3af67a1ffde2d652f05441052a7d469a98725726aadf6d5760409
---

# Q002-F-06 — Āyat al-Kursī (Q 2:255) ROOT-LEVEL local distinctiveness


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Target claim

al-Bukhārī *Ṣaḥīḥ* ḥadīth #4008 (Kitāb al-tafsīr / Sūrat al-Baqara) + Muslim *Ṣaḥīḥ*
(Kitāb ṣalāt al-musāfirīn, ʿUbayy b. Kaʿb chain) — Q 2:255 (*āyat al-kursī*) is the
**greatest verse** (*aʿẓam āya*) of the Quran. (Citation matches the project's
established form in `05-classical-claims-audit.md` claim #2 + `04-hadith-corpus.md`
§2.1; the exact Muslim ḥadīth-number is flagged AWAITING-cross-check there.) Falsifiable
PROXY: a "greatest verse" should at minimum be lexically self-contained — distinct
from its immediate context rather than a continuation of an adjacent passage. This
test is the ROOT-LEVEL local-neighbourhood test that Q002-F-01 (surface-token density)
and Q002-F-03 (whole-corpus centrality) explicitly flagged as pending.

## Pre-registration

`Q002-F-06-ayat-al-kursi-root-locality-prereg.md`
(SHA256 `7044eb7477d3af67a1ffde2d652f05441052a7d469a98725726aadf6d5760409`).
Direction LOCKED: HIGH local-distinctiveness (Q 2:255 in TOP-5% of Q 2 by mean
root-Jaccard distance to its ±3 in-surah neighbours; TOP-10% corpus-wide). Seed
20260509, 10,000-perm in-surah shuffle null. Bonferroni k = 2, α = 0.025.

## Empirical result

From `csv/Q002-F-06.json` (QAC-triliteral-root sets, `data/morphology/root-index.json`):

| Metric | Value |
|:--|:--|
| Q 2:255 root count | 23 |
| Q 2:255 local-distinctiveness (k=3, 1 − mean-Jaccard to 6 neighbours) | 0.9395 |
| **In-surah rank (H1, of 286)** | **117** |
| **Corpus rank (H2, of 6,236)** | **3,960** |
| Permutation null mean | 0.9454 |
| Permutation null SD | 0.0285 |
| **Permutation z** | **−0.209** |
| Permutation p (one-sided, canonical ≥ null) | 0.726 |
| Alt-radius in-surah rank (k=2) | 133 |
| Alt-radius in-surah rank (k=5) | 177 |

## Verdict — NULL on BOTH pre-committed directions (pre-commit honoured)

- **H1 NULL**: rank 117/286 — far outside the pre-committed top-15. Q 2:255 is near
  the MIDDLE of al-Baqara by local lexical distinctiveness.
- **H2 NULL**: rank 3,960/6,236 — below the corpus median (50.4th percentile).
- The permutation z = **−0.209** is slightly NEGATIVE: Q 2:255 is, if anything,
  marginally MORE lexically similar to its real neighbours than to random neighbours
  (not significantly: p = 0.726). This is a mild pre-commit REVERSAL, flagged per
  §1.8 and published with full prominence.
- The NULL is rules-tuple-stable across all three window radii (k=2: rank 133, k=3:
  rank 117, k=5: rank 177).

## Interpretation — why this is informative, not just a miss

Āyat al-Kursī is **embedded** in its lexical context, not isolated from it. Its core
roots (`Alh` Allāh, `Hyy` al-Ḥayy, `qwm` al-Qayyūm, `slm`/`smw` the heavens, `ʿlm`
knowledge, `ʿly`/`ʿẓm` the Exalted/Mighty) are precisely the high-frequency creedal
roots that saturate the surrounding tawḥīd/āyāt passages (Q 2:253-257 is a dense
faith-and-light cluster). The verse is a SUMMIT *within* a creedal massif, not a
lexically alien peak.

This is the third independent confirmation that the hadith "greatest verse" claim does
NOT reduce to a simple lexical-extremity signature:

1. Q002-F-01: NULL on per-word divine-name density (rank 563/6236).
2. Q002-F-03: Q 2 is a cohesion-ANCHOR, not the corpus centroid (Q 112 is).
3. Q002-F-06 (this test): Q 2:255 is NOT a local lexical outlier within al-Baqara.

The convergent picture: **theological greatness (al-Bukhārī #4008) is empirically
orthogonal to lexical distinctiveness.** This is the verse-level analogue of the
project's dual-iʿjāz orthogonality law (structural-iʿjāz ⊥ theological-iʿjāz,
[[h-new-840-unified-architectural-score]]). The "greatest verse" is great by *maʿnā*
(meaning — the most complete single statement of divine sovereignty), in al-Khaṭṭābī's
*iʿjāz al-maʿnā* sense, not by lexical isolation.

## The 9 verses that ARE local lexical outliers in al-Baqara

For contrast, the top of the in-surah distinctiveness ranking (local-distinct = 1.0,
i.e. ZERO root overlap with any of their 6 neighbours) are: vv. 1, 16, 18, 37, 40, 42,
44, 56, 152. These are short transitional/imperative verses (e.g. v1 = ALM
muqaṭṭaʿāt; v152 = "fa-dhkurūnī adhkurkum…", the famous "remember Me" pivot) whose
brevity guarantees disjoint root sets. The metric rewards SHORTNESS-induced disjointness
— which is precisely why a 23-root grand-summary verse like 2:255 cannot top it. This is
a known artefact direction (cf. Q002-F-01 short-verse density inflation) and is reported
transparently.

## Rules-tuple sensitivity

| Rules-tuple | Q 2:255 in-surah rank | Verdict |
|:--|:--|:--|
| `(QAC-root, k=3)` (pre-reg primary) | 117 / 286 | NULL |
| `(QAC-root, k=2)` (MW-3) | 133 / 286 | NULL |
| `(QAC-root, k=5)` (MW-3) | 177 / 286 | NULL |

NULL is stable across all radii — not a knife-edge result.

## Honest limits

- Local-distinctiveness via set-Jaccard is BRITTLE to verse length (short verses score
  high by disjointness). A length-controlled metric (e.g. residualised Jaccard) would
  be a fairer test and is queued.
- The proxy is lexical, not semantic; the hadith claim is theological. A NULL here does
  NOT impugn the hadith — it only refutes the *naive lexical-isolation* interpretation
  of "greatest verse."
- Root sets are from QAC v0.4; lemma-level or surface-level sets could shift ranks.

## Cross-references

- [[Q002-F-01-ayat-al-kursi-divine-name-density|Q002-F-01]] — divine-name density NULL.
- [[Q002-F-03-centrality|Q002-F-03]] — Q 2 cohesion-anchor not centroid.
- [[h-new-840-unified-architectural-score]] — dual-iʿjāz orthogonality (the corpus-level
  law this verse-level NULL mirrors).
- al-Bukhārī #4008, Muslim #810 — see `04-hadith-corpus.md`.

## Status

NULL on both pre-committed directions, stable across 3 radii, mild non-significant
reversal flagged. Pre-commit honoured. The "greatest verse" is great by meaning, not by
lexical isolation.
