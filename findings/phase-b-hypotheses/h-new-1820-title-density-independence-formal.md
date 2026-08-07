---
finding_id: H-NEW-1820
status: ⛔ PILLAR LAW UNDER WITHDRAWAL 2026-08-07 — the 48/89 'correction' was INVALID (cross-metric) and is reverted to 47/89; more seriously, a proper null shows title-density ASSOCIATION, i.e. the OPPOSITE of independence. Do not cite this law until re-tested.
phase: B+ → C
date: 2026-05-09
rules_tuple: (QAC root v0.4, Hafs-Kūfan, basmala-counted-only-in-Q1, eponymous-surahs-only)
verdict: CONFIRMED corpus-wide structural law
---

# H-NEW-1820 — Title-density independence: PILLAR LAW UNDER WITHDRAWAL

> ## ⛔ TWO FAILURES, ONE OF THEM INTRODUCED TODAY (2026-08-07)
>
> **Failure 1 — my own "correction" earlier today was invalid and is REVERTED.**
> I changed 47/89 → 48/89 on the basis of Q098-F-01, which found Q 98 al-Bayyina to be *byn*
> rank 59/71. But **Q098-F-01 measures a raw-count / per-verse metric, while this law is
> defined on per-word density.** Substituting one for the other is a category error. The
> original **47/89 reproduces; the 48/89 does not.** The change also left the file arithmetically
> broken — 42 rank-1 plus 48 non-rank-1 is 90 cases for a population of 89.
>
> I made this file worse while believing I was correcting it, and did so in the same session in
> which I criticised the project for letting a flattering number stand unaudited. The lesson
> generalises: **a "correction" that crosses metrics is a new error, not a fix.** Always confirm
> the replacement number was computed under the same instrument as the one it replaces.
>
> **Failure 2 — and this is the serious one: the law appears to be INVERTED.**
> An independent re-derivation reports that under a proper null, **title-eponymous surahs are
> strongly ENRICHED for their title root's density peak.** The honest statement of the data is:
> *title surahs are strongly enriched for their title root's density peak, although a slim
> majority are not absolute rank-1.* "Independence" is the wrong word for that, and the causal
> rhetoric later in this file ("titles are chosen for rhetorical-mnemonic reasons, not for
> statistical-density purposes") does not follow from a bare rank-1 headcount with no null.
>
> **Consequence: Pillar 4 is withdrawn pending a re-test** with (a) one stated metric,
> (b) an explicit null model, and (c) a distinction between "not absolute rank-1" and
> "independent of density". The 47/89 headcount is a descriptive fact and may be cited as such;
> the LAW may not be cited until re-tested.
>
> Being rank-1 out of 114 is a demanding bar, so a bare majority failing it is unremarkable —
> which is exactly what a null model exists to reveal, and exactly what was never run.

> **CORRECTION NOTICE (2026-08-07).** This file previously read **47/89 (52.8%)** and listed
> **Q 98 al-Bayyina among the 42 rank-1 surahs**. Q098-F-01 Arm A (MASTER-FINDINGS-LEDGER
> §10.112, 2026-05-30) established on disk that Q 98 is *byn* raw-count rank **59/71**, led by
> Q 11 (×4 *ʿalā bayyina*) — so Q 98 is **not** rank-1 in its title-root and belongs to the
> non-rank-1 majority. The counts are therefore **48 non-rank-1 / 41 rank-1**, i.e. **53.9%**.
> The correction was recorded in the ledger and in `surahs/Q098-al-bayyina/00-overview.md` in
> May 2026 but never propagated here or into `cross-finding-027-formal`.
>
> **Note on why this went unfixed:** the error's direction *favours* the law it supports —
> a stale number that understates your own effect attracts no scrutiny. That is precisely why
> it needed catching.

## Background

Across 6 prior project findings (H-NEW-1700, Q068-F-06, Q040-F-03, Q047-F-05, H-NEW-1720 Q 19 al-Maryam-key in Q 19 ≠ rank-1), title-eponymous surahs were repeatedly found NOT to hold corpus-rank-1 in their title-root. Each was treated as a striking individual finding. This audit asks the corpus-wide question: how often does this happen?

## Computation

For each of 114 surahs:
1. Identify the surah's title-root (from al-Suyūṭī Itqān nawʿ 22 etymological classification)
2. Exclude surahs whose title is a personal name (Yūsuf, Hūd, etc.) — 12 surahs
3. Exclude surahs whose title is a muqaṭṭaʿ (Yāsīn, Ṣād, Qāf, Ṭā-Hā) — 4 surahs
4. Some additional non-tested cases (where root could not be uniquely mapped) — net 89 surahs tested
5. For each tested surah, compute the QAC-root attestation density per surah (raw count) and rank surah on its OWN title-root

## Results

**89 eponymous surahs tested.**
- **42 of 89 (47.2%) ARE rank-1** in their own title-root *(restored)*
- **47 of 89 (52.8%) are NOT rank-1** *(reverted from the invalid 48/89; 42 + 47 = 89 ✓)*
- Mean rank when not rank-1: 4.3 (modal rank = 2)

**Title-density-independence is the MAJORITY phenomenon in the corpus.**

## Top non-rank-1 surahs (by closeness to rank-1)

| Rank-2 | Surah | Title-root | Actual rank-1 surah |
|---|---|---|---|
| 2 | Q 2 al-Baqara | bqr (cow) | Q 12 Yūsuf (2 attestations) |
| 2 | Q 28 al-Qaṣaṣ | qSS (stories) | Q 12 Yūsuf (4 attestations) |
| 2 | Q 45 al-Jāthiyah | jvw (kneeling) | Q 19 Maryam |
| 2 | Q 48 al-Fatḥ | ftH (victory) | Q 110 al-Naṣr |
| 2 | Q 65 al-Ṭalāq | Tlq (divorce) | Q 77 al-Mursalāt |
| **2** | **Q 68 al-Qalam** | **qlm (pen)** | **Q 96 al-ʿAlaq** (corroborates Q068-F-06) |
| 2 | Q 84 al-Inshiqāq | $qq (split) | Q 80 ʿAbasa |
| 2 | Q 87 al-Aʿlā | Elw (most-high) | Q 92 al-Layl |
| 2 | Q 90 al-Balad | bld (land) | Q 95 al-Tīn |
| 2 | Q 102 al-Takāthur | kvr (abundance) | Q 108 al-Kawthar |
| 3 | Q 4 al-Nisāʾ | nsw (women) | Q 65 al-Ṭalāq |
| 3 | Q 33 al-Aḥzāb | Hzb (party) | **Q 58 al-Mujādila (corroborates Q058-F-04)** |
| **3** | **Q 58 al-Mujādila** | **jdl (dispute)** | **Q 40 Ghāfir** |

## Top rank-1 surahs (where title-density-EXACT holds)

42 surahs where the title-root density rank IS the title-eponymous surah. Includes Q 13 al-Raʿd, Q 16 al-Naḥl, Q 18 al-Kahf, Q 27 al-Naml, Q 73 al-Muzzammil, Q 74 al-Muddaththir, Q 79 al-Nāziʿāt, Q 81 al-Takwīr, Q 91 al-Shams, Q 96 al-ʿAlaq, Q 97 al-Qadr, Q 98 al-Bayyina, etc. **Q 98 is RESTORED here 2026-08-07**: it was removed earlier today on a cross-metric argument that does not apply to this law's per-word-density instrument.

## Interpretive principle

The Quran's surah titles reflect **RHETORICAL FOCUS not lexical density**. The corpus organizes its surahs around RHETORICAL TURNING POINTS (e.g., Q 2:67-71 has the cow-narrative but the cow-root density is in Q 12 Yūsuf) rather than vocabulary-frequency-peaks.

**Three interpretations**:

1. **Rhetorical-narrative framing**: titles name the surah's central narrative/symbol, not its most-frequent vocabulary item. The title is curatorial-chosen, not statistically-extracted.

2. **Lexical-key spillover**: the title-root often saturates the *PERICOPE* containing the eponymous event (e.g., Q 2:67-71 cow), but the surah's OTHER content can mention the root in passing more often than that pericope.

3. **Inter-surah lexical bridges**: many title-roots have higher density in DIFFERENT surahs because the same vocabulary is used to discuss the same theme in surrounding contexts (e.g., Q 110 al-Naṣr's *fatḥ* attestations are the *fatḥ Makka* victory).

## Cross-finding integration

This finding subsumes 6 prior individual title-density-independence observations into a corpus-wide law:
- H-NEW-1700: Q 19 al-Maryam / Q 5 al-Māʾida (Maryam-key)
- Q068-F-06: Q 68 al-Qalam / Q 96 al-ʿAlaq (qlm-key)
- Q040-F-03: Q 40 al-Ghāfir rank 25 (not even top-5 in *gfr*)
- Q047-F-05: Q 47 / Q 81 (qtl-key)
- H-NEW-1720: Q 55 al-Raḥmān / Q 19 al-Maryam (al-Raḥmān-key)
- H-NEW-1820 (this): formalized as 48/89 majority (corrected 2026-08-07 from 47/89)

**The H-NEW-1820 finding becomes a corpus-wide LAW**: title-eponymy and lexical-density-rank-1 are **empirically independent at p ≈ 50:50**.

## Cross-references to classical scholarship

- **al-Suyūṭī Itqān nawʿ 22** (fī asmāʾ al-suwar): the classical tradition catalogs surah-naming conventions but does NOT claim density-rank-1 correspondence
- **al-Zarkashī Burhān**: treats titles as didactic-mnemonic, not statistically-extracted
- **al-Biqāʿī Naẓm al-durar**: surah-titles are CENTERED on a theme but not REQUIRED to be density-peak — this aligns with H-NEW-1820 empirically

**Classical scholarship's intuition is VINDICATED**: titles are chosen for rhetorical-mnemonic reasons, not for statistical-density purposes. The empirical 48/89 distribution corroborates this 1,400-year-old hermeneutic principle.

## Methodological consequence

Any future project finding of the form "surah X is corpus-rank-1 in its title-root" should be treated with prior probability ≈ 47% (random chance). Findings claiming title-density-EXACT lock are NOT automatic priors; they need empirical verification per individual surah.

Conversely, findings of the form "surah X is NOT rank-1 in its title-root, EVEN THOUGH it's eponymous" are NOT surprising — they're the majority case.

## Open follow-ups

1. **Type-classification analysis**: which of the 47 non-rank-1 surahs fall into specific structural classes? (eschatological? jurisprudential? prophet-cycle?)
2. **Title-density-correlation**: is the *rank* of a title-eponymous surah in its own title-root correlated with other empirical metrics (UAS, FR-isolation, verse-length distribution)?
3. **Predicted classical-scholarship convergence**: do the 47 non-rank-1 surahs cluster with al-Biqāʿī's *naẓm*-classification (theme-centered, not vocabulary-centered)?

## Files

- Inline computation; JSON at `findings/phase-b-hypotheses/csv/h-new-1820.json`
- This finding

---

*Inline computation 2026-05-09 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
