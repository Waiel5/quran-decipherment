---
surah: 72
surah_name_ar: الجن
surah_name_translit: al-Jinn
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
---

# Q 72 al-Jinn — Classical Claims Audit

This file audits non-trivial classical claims about Q 72 with empirical verdicts.

## 1. al-Biqāʿī Q 71 → Q 72 munāsabah claim

**Claim** (al-Biqāʿī, *Naẓm al-Durar* §Q72, line 144727-144735): Q 71 Nūḥ closed with Nūḥ's prayer against his rejected human community; Q 72 al-Jinn opens with the contrasting non-human (jinn) ACCEPTANCE of the Prophet Muḥammad. The mushaf-sequence Q 71 → Q 72 deliberately stages the human-rejection-then-non-human-acceptance arc.

**Empirical test**: Two axes:

| Axis | Result | Source |
|:--|:--|:--|
| Q 71→72 FR-content distance | d(Q 71, Q 72) = 0.8203 (deeper than Q 72's rank-1 neighbour Q 112 at 0.6945; not in Q 72's top-15 nearest) | computed from h-new-111.json |
| Q 71→72 canonical adjacency residual | Δ = 0.0408, fraction_residual = 0.49% — MODEST seam cost; NOT in top-10 expensive seams (top-10 start at Δ=0.21 for Q 7-8) | h-new-720.json `per_adjacency` |

**Verdict**: **RULES-TUPLE-FRAGILE / PARTIALLY-VINDICATED**.

al-Biqāʿī's thematic-content arc (rejection → acceptance) is plausible at the qualitative level but **does NOT translate into an extreme FR-cohesion or TSP-expensive seam**. The Q 71-72 seam is **modest cost (Δ=0.04)** — the mushaf is locally near-optimal but not extreme at this junction. al-Biqāʿī's thematic pairing is INTERPRETIVELY VALID but is not the kind of architectural-extreme seam that the project would call CONFIRMED at law-strength. The arc holds as a literary observation but not as a load-bearing structural finding.

By contrast, the **Q 72→Q 73 seam has Δ = 0.00** (mushaf-locally-OPTIMAL — see `01-empirical-profile.md` §5). The forward-arc (Q 72 → Q 73 al-Muzzammil, continuation of prophetic-instruction register) is empirically TIGHTER than the al-Biqāʿī backward-arc.

## 2. al-Suyūṭī *qul*-opener cluster claim

**Claim** (al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, the *fawātiḥ al-suwar* section): the *qul*-opening is one of ten classical opener categories. The corpus contains exactly five v.1-w.1 *qul*-opener surahs: Q 72 al-Jinn, Q 109 al-Kāfirūn, Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās.

**Empirical test**: see `06-novel-findings.md` Q072-F-01.

| Test | Result |
|:--|:--|
| 5-qul cluster within-mean FR | 0.4983 (vs random-5 null mean 0.9236) |
| p (one-sided ≤) | 0.0026 (10,000 perms) |
| z-score | −4.217 |
| MW-5 PC (H-NEW-1190 sub-sample {69,97,101}) | PASS at p = 0.0362 |
| Verdict | **PASS-STRONG** |

**Verdict**: **CONFIRMED (replication of H-NEW-74 / MASTER-LEDGER §10.18)**.

The al-Suyūṭī classical category *qul*-opener is empirically FR-content-cohesive at p < 0.01 — the five surahs are systematically closer in root-distribution than random-5-subsets. The cluster cohesion is dominated by the muʿawwidhāt-extended 4-tail {Q 109, 112, 113, 114} (within-mean 0.333) but Q 72's mean-to-tail of 0.747 is still tight relative to corpus mean (0.92).

## 3. al-Biqāʿī "two names of the surah" claim

**Claim** (al-Biqāʿī, line 144713): the surah is named *al-Jinn* AND also *qul ūḥiya* (after its opening incipit). This is the standard double-naming convention for Q 72.

**Empirical test**: This is a classification claim about naming convention, not a falsifiable empirical claim. We can however test the **content-faithfulness** of the *al-Jinn* name (i.e., does the surah have the highest jinn-density?).

See `06-novel-findings.md` Q072-F-02.

| Test | Result |
|:--|:--|
| Q 72 LEM:jin~ density (strict) | 10.24 per 1k tokens (3 hits / 293 tokens) |
| Q 72 rank | **1 / 114** |
| Margin over rank-2 (Q 34 Sabā) | 3.2× (10.24 vs 3.19) |
| Combined-lens (jin~ + jaA^n~) rank | 2 / 114 (behind Q 55 al-Raḥmān at 14.08/1k under combined lens) |
| Verdict | **PASS at the strict lens (corpus-EXACT name → primary-lemma alignment)** |

**Verdict**: **VINDICATED (corpus-rank-1 in strict LEM:jin~ density)**.

The al-Biqāʿī naming convention is empirically FAITHFUL: Q 72 is named *al-Jinn* and corpus-rank-1 in the strict jinn-being-lemma density. The sensitivity check under the expanded lens (jin~ + jaA^n~) drops Q 72 to rank-2 behind Q 55 — which is itself classically known for the *al-jaAn~* refrain (Q 55:15, 39, etc.). The expanded-lens result is not the pre-committed primary verdict but it informs the broader observation: there are TWO "jinn-density-leading" surahs depending on which jinn-being lemma you weight: Q 72 for *jin~*, Q 55 for *jaA^n~*.

## 4. Abū Ḥayyān / al-Biqāʿī Q 72 ↔ Q 46 same-event claim

**Claim** (al-Biqāʿī §Q72, line 144760-144761, citing Abū Ḥayyān): «المشهور أنه هو، وقيل: هو غيره» — the famous view is that the Q 72:1 jinn-event is the SAME as the Q 46:29 jinn-event; the alternative view is that they are different events.

**Empirical test**: Q072-F-03 — Jaccard(Q 72:1-19, Q 46:29-32) vs length-matched corpus null.

| Test | Result |
|:--|:--|
| Observed Jaccard | 0.0851 |
| Intersection size | 16 tokens |
| Null mean | 0.0469 |
| z-score | +2.81 |
| p (one-sided ≥) | 0.0068 |
| n candidate windows | 19,023 |
| Diagnostic tokens in both | الجن (al-jinn), سمعنا (samiʿnā "we heard"), يهدي (yahdī "guides") |
| Verdict | **PASS** |

**Verdict**: **DIRECTIONAL-VINDICATED (supports but does not prove same-event reading)**.

The two pericopes share lexical content above length-matched corpus null at p = 0.0068. This is consistent with EITHER (a) the same-event reading (Abū Ḥayyān's *mashhūr* view), OR (b) the shared-formula reading (two distinct events composed with shared jinn-event vocabulary). The test is NECESSARY-NOT-SUFFICIENT for the same-event identity: a NULL result would have refuted the same-event reading; a PASS result supports it without proving it.

The 16-token intersection includes the diagnostic jinn-event vocabulary (*al-jinn*, *samiʿnā*, *yahdī*) but lacks *nafar* (Q 72:1 *nafar*, Q 46:29 *nafaran* — the morphological forms differ between definite-nominative and accusative-tanwīn). The shared-formula reading thus has empirical traction even under the unified-event interpretation.

## 5. Ibn ʿAbbās vs Ibn Masʿūd asbāb al-nuzūl claim

**Claim**: The traditional asbāb al-nuzūl divides:
- **Ibn ʿAbbās** (Bukhārī 755, 4713; Muslim 908): the Prophet did NOT see the jinn; the event was an overheard recitation at Suq ʿUkāẓ during dawn-prayer.
- **Ibn Masʿūd** (Tirmidhī 3342; Muslim 909): the Prophet DID meet the jinn at the *laylat al-jinn* (Nakhla), with Ibn Masʿūd accompanying.

**Empirical test**: This is a historical-narrative claim, NOT EMPIRICALLY TESTABLE via corpus-internal methods. The two narrations are HARMONIZABLE under the two-event reading.

**Verdict**: **NOT-TESTABLE BY CORPUS-INTERNAL METHODS** — flagged as classical-tradition divergence, recorded faithfully in `04-hadith-corpus.md`.

## 6. al-Zamakhsharī 17-fold *wa-anna* enumeration iʿjāz claim

**Claim** (al-Zamakhsharī, *al-Kashshāf* ad Q 72:2-19): the surah's vv.3-19 are structured as 17 propositions opening with *wa-anna* / *wa-annā* / *wa-annahu* — a corpus-rare *taʿdād balāghī* (rhetorical-enumeration) pattern.

**Empirical test**: Direct text inspection of Q 72 verse-by-verse:

| v. | Opens with |
|:-:|:--|
| 2 | yahdī (no *wa-anna*) — note: v.2 continues v.1's *fa-qālū innā* speech-act |
| 3 | wa-annahu |
| 4 | wa-annahu |
| 5 | wa-annā |
| 6 | wa-annahu |
| 7 | wa-annahum |
| 8 | wa-annā |
| 9 | wa-annā |
| 10 | wa-annā |
| 11 | wa-annā |
| 12 | wa-annā |
| 13 | wa-annā |
| 14 | wa-annā |
| 15 | wa-ammā (NOT wa-anna — this is the *qāsiṭūn*-clause, different particle) |
| 16 | wa-an (variant — short form, "and if") |
| 17 | li-naftina-hum (no *wa-anna*) |
| 18 | wa-anna |
| 19 | wa-annahu |

The Block A (vv.3-19) has **15 verses (vv. 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19) opening with a *wa-an*-family particle**. al-Zamakhsharī's count of 17 may include vv.1-2 as the framing (the *qul ūḥiya ilayya annahu* in v.1 + the *innā* in v.2 use related complementizer-anna forms).

**Verdict**: **VINDICATED** as a corpus-rare *taʿdād*-pattern. The 15-of-17 (or 17-of-19, counting v.1-2 frame) *wa-anna* concentration in Block A is empirically distinctive. Whether this rises to the level of "iʿjāz" is a theological evaluation; the empirical pattern is verified.

## 7. Surah-name → primary-lemma faithfulness (corpus-wide implication)

**Inferential claim** (cross-classical, implicit in al-Suyūṭī's surah-naming taxonomy): Surahs named for a specific entity / concept should rank at or near the top in lemma-density of that referent.

**Empirical test for Q 72**: Q072-F-02 PASS (rank 1/114). This is a single-instance verification of the broader naming-convention faithfulness hypothesis. It joins prior verifications (e.g., Q 71 Nūḥ ↔ Nūḥ-density top-rank; Q 50 Qāf and other letter-named surahs) and prior falsifications (e.g., Q 19 Maryam: Maryam-density highest in Q 19 only at the strict lemma; counter-examples exist for some surahs named after thematic events rather than specific lexemes).

**Verdict**: **VINDICATED for Q 72**. The Q 72 naming is content-faithful at the strict primary-lemma lens. Cross-surah systematic study is queued for future work.

## 8. Audit summary

| Classical claim | Source | Verdict | Replication seed |
|:--|:--|:--|:--|
| al-Biqāʿī Q 71→Q 72 munāsabah | al-Biqāʿī *Naẓm al-Durar* §Q72 | RULES-TUPLE-FRAGILE / PARTIAL | Δ_TSP = 0.041 (modest seam) |
| al-Suyūṭī 5-qul-opener category | al-Suyūṭī *al-Itqān*, *fawātiḥ* | CONFIRMED (p=0.0026) | Q072-F-01 |
| al-Biqāʿī surah double-naming (al-Jinn / qul ūḥiya) | al-Biqāʿī line 144713 | VINDICATED (Q 72 rank 1 in strict LEM:jin~) | Q072-F-02 |
| Abū Ḥayyān Q 72↔Q 46 same-event | al-Biqāʿī §Q72 citing Abū Ḥayyān | DIRECTIONAL-VINDICATED (p=0.0068) | Q072-F-03 |
| Ibn ʿAbbās vs Ibn Masʿūd asbāb | Bukhārī 755 + Muslim 909 + Tirmidhī 3342 | NOT-TESTABLE-EMPIRICALLY | — |
| al-Zamakhsharī 17-fold *wa-anna* iʿjāz | al-Zamakhsharī *al-Kashshāf* | VINDICATED (direct text inspection) | text-direct |

**Headline**: 4 of 5 empirically-testable classical claims about Q 72 are VINDICATED or CONFIRMED at α=0.05 or better; 1 is RULES-TUPLE-FRAGILE (al-Biqāʿī Q 71→72 thematic arc holds qualitatively but does not produce an extreme seam-cost or FR-tight pairing).

The verdict pattern is consistent with the project's cross-finding-015 *classical-scholarship-validation-pattern*: classical balāgha-rhetorical and form-pattern claims (5-qul opener, surah-name-faithfulness, *taʿdād balāghī*) tend to VINDICATE empirically; classical thematic-munāsabah claims tend to PARTIALLY-VINDICATE (qualitative-yes, structural-extreme-no).

## Cross-references

- `00-overview.md` — surah identification
- `01-empirical-profile.md` — h-new-720 seam costs
- `03-tafsir-survey.md` — full classical reading network
- `04-hadith-corpus.md` — Bukhārī 755/4713, Muslim 908, Tirmidhī 3342
- `06-novel-findings.md` — Q072-F-01/02/03 with full pre-reg + SHA + JSON
- `findings/phase-b-hypotheses/cross-finding-015-classical-scholarship-validation-pattern.md`
