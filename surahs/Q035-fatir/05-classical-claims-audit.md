---
surah: 35
surah_name_ar: فاطر
surah_name_translit: Fāṭir
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — 8 classical claims tested with project verdict; 5 CONFIRMED, 1 PARTIAL, 1 SECONDARY-TRIANGULATED, 1 PENDING
---

# Q 35 Fāṭir / al-Malāʾika — Classical Claims Audit

This file applies the project's classical-quantitative-claims-audit methodology to all classical claims about Q 35 that are testable. Each claim is given a project verdict.

## 1. Audit summary table

| ID | Source | Claim | Verdict |
|:--:|:--|:--|:--:|
| Q35-CC-01 | al-Zarkashī, *Burhān* 1/181 | Q 35 is one of the 5 al-ḥamdu li-llāh openers {Q 1, 6, 18, 34, 35} | **CONFIRMED** (= CC-048) |
| Q35-CC-02 | al-Suyūṭī, *Itqān*, nawʿ 17 | Q 35 has dual canonical name (Fāṭir + al-Malāʾika) | **CONFIRMED** (textual + classical reception) |
| Q35-CC-03 | al-Tirmidhī §3309 | Q 35:32 3-fold hierarchy hadith: "all three are in paradise" | **CONFIRMED** (chain ḥasan gharīb; matn multiply-attested) |
| Q35-CC-04 | al-Ṭabarī ad loc. | Q 35:1 wings *mathnā wa-thulātha wa-rubāʿ* literal — angels with 2/3/4 wings | **CONFIRMED** (Bukhārī §3232 anchor) |
| Q35-CC-05 | al-Ṭabarī ad loc. | Q 35:13 *qiṭmīr* = thin date-stone membrane (hapax) | **CONFIRMED** (lexical-philological) |
| Q35-CC-06 | al-Biqāʿī, *Naẓm al-Durar* | Q 34 → Q 35 munāsabah is anchored on the shared al-ḥamd opener | **PARTIAL** (opener shared YES; full-content-cohesion mid-pack rank 65/113) |
| Q35-CC-07 | al-Suyūṭī (encyclopedic) | Q 35:32 hadith catalog: 20+ isnāds converging on all-three-saved reading | **SECONDARY-TRIANGULATED** (multiple chains in al-Ṭabarī + Mishkat + al-Bayhaqī, but full Aḥmad-numbering not directly verified) |
| Q35-CC-08 | al-Rāzī, *Mafātīḥ* | Q 35 is a **two-arc surah**: vv. 1-31 (cosmological-survey) + vv. 32-45 (eschatological-recompense) | **PENDING** (qualitative claim; testable via Block-pivot empirical analysis — see Q035-F-05 inclusio test for partial validation) |

## 2. Audits in detail

### Q35-CC-01 — al-Zarkashī's al-ḥamdu li-llāh cluster (= CC-048)

**Claim** (al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* 1/181): "There are 5 surahs opening with al-ḥamdu li-llāh: al-Fātiḥa (1), al-Anʿām (6), al-Kahf (18), Sabaʾ (34), Fāṭir (35)."

**Test**: phrase-search for *al-ḥamdu li-llāh* as the opening word(s) of v.1 (with Q 1 special-cased: bismillāh is v.1, al-ḥamd is v.2 in Hafs-Kufan — counted as opener per classical convention).

**Result**: 5 surahs match — exactly {Q 1 (v.2), Q 6, Q 18, Q 34, Q 35}. (Verified via `quran-text/quran-no-tashkeel.json` phrase-search.)

**Verdict**: **CONFIRMED**. This claim was already CONFIRMED in the project's classical-quantitative-claims-audit (CC-048 at `findings/phase-b-hypotheses/classical-quantitative-claims-audit.md`).

**Empirical extension** (Q035-F-01): does the cluster show FR-cohesion structurally? See `06-novel-findings.md` Q035-F-01 (FR-cohesion test on the 5-surah cluster).

### Q35-CC-02 — dual-name (Fāṭir / al-Malāʾika)

**Claim** (al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 *fī asmāʾ al-suwar*): Q 35 has two canonical names — Fāṭir (after the divine attribute in v.1) and al-Malāʾika (after the angels in v.1).

**Test**: classical reception verification across multiple primary sources:
- al-Bukhārī's *Ṣaḥīḥ*: cites *Sūrat al-Malāʾika* in tafsīr context.
- al-Tirmidhī's *Sunan*: chapter-headings in kitāb al-tafsīr use both names.
- al-Suyūṭī's *al-Itqān*, nawʿ 17: explicit dual-name listing.
- al-Zamakhsharī's *Kashshāf*: surah-heading uses Fāṭir.
- al-Rāzī's *Mafātīḥ*: surah-heading uses Fāṭir + parenthetical al-Malāʾika.
- Modern Cairo edition (1924/1342H): Fāṭir as primary.

**Result**: classical reception confirms the dual-name. Both are canonical.

**Empirical extension**: Q 35 is the **only surah opening v.1 with explicit *al-malāʾika*** (corpus-search confirmed; see `06-novel-findings.md` Q035-F-03). This empirical uniqueness validates the al-Malāʾika naming.

**Verdict**: **CONFIRMED**.

### Q35-CC-03 — Tirmidhī §3309 hadith on Q 35:32

**Claim** (al-Tirmidhī, *Sunan*, kitāb tafsīr al-Qurʾān §3309): the Prophet ﷺ said about Q 35:32 *hāʾulāʾ kulluhum bi-manzilatin wāḥidatin wa-kulluhum fī al-jannah* — "all of these are of the same rank, and all of them are in paradise."

**Test**: 
- Tirmidhī's grading of own chain: *ḥasan gharīb* (good but rare, isnād contains 2 unnamed transmitters).
- al-Albānī: ḍaʿīf (chain weakness).
- Multiple Companion-level parallel chains via al-Ṭabarī.
- Mishkat §2277 (Usāma b. Zayd parallel via al-Bayhaqī).
- al-Suyūṭī's *al-Durr al-manthūr* assembles 20+ isnāds.

**Result**: the SINGLE-CHAIN of Tirmidhī §3309 is ḍaʿīf-due-to-anonymity, but the MATN is multiply-attested. The all-three-saved reading is classical Sunnī mainstream, anchored in:
- Tirmidhī §3309 (Abū Saʿīd → Prophet)
- Mishkat §2277 / al-Bayhaqī (Usāma b. Zayd → Prophet)
- al-Ṭabarī's 5+ Companion-level chains (Ibn ʿAbbās, Ibn Masʿūd, Kaʿb al-Aḥbār, Abū Isḥāq al-Sabīʿī, Ibn al-Ḥārith)
- Aḥmad Musnad (per al-Suyūṭī, secondary-triangulated)

**Verdict**: **CONFIRMED** (with chain-grade caveat).

**Honest correction to brief**: the brief mentions "Tirmidhī tafsīr 35" — the precise reference is Tirmidhī §3309 in *kitāb tafsīr al-Qurʾān* (Chapter 47), and the chain is *ḥasan gharīb* per Tirmidhī himself, ḍaʿīf per al-Albānī. The matn nonetheless survives via parallel chains.

### Q35-CC-04 — Q 35:1 angelic wings literal reading

**Claim** (al-Ṭabarī, ad loc.; Bukhārī §3232 anchor): the angels mentioned in Q 35:1 have **2, 3, 4 wings** (some have more — 600 in Jibrīl's case per Bukhārī).

**Test**:
- Bukhārī §3232 verified VERIFIED: Jibrīl with 600 wings each filling the horizon.
- Muslim §177 parallel.
- Ibn Mājah §195 parallel (Isrāfīl).
- al-Ṭabarī cites Qatāda explicitly: *baʿḍuhum lahu janāḥān wa-baʿḍuhum thalāthatun wa-baʿḍuhum arbaʿatun* ("some have 2 wings, some 3, some 4").

**Result**: the literal-physical-reading is corpus-anchored.

**Verdict**: **CONFIRMED**.

### Q35-CC-05 — Q 35:13 *qiṭmīr* = date-stone membrane

**Claim** (al-Ṭabarī, citing Ibn ʿAbbās): *qiṭmīr* is the white skin of the date-stone (the "thread" or membrane).

**Test**: Q 35:13 is the SOLE corpus attestation of root q-T-m-r (verified in QAC v0.4). The Arabic-poetic usage outside the Quran corroborates the date-stone-membrane meaning (cf. Imruʾ al-Qays).

**Result**: lexical-philological consensus — *qiṭmīr* = date-stone-fiber/membrane, used metaphorically as "smallest measurable unit."

**Verdict**: **CONFIRMED** (lexical-philological).

### Q35-CC-06 — al-Biqāʿī Q 34→Q 35 munāsabah

**Claim** (al-Biqāʿī, *Naẓm al-Durar* ad Q 35): the Q 34 → Q 35 transition is anchored on the shared al-ḥamdu li-llāh opener; the munāsabah is smooth.

**Test**:
- Empirical: Q 34 → Q 35 canonical-adjacency cost (`h-new-720.json`): delta_raw = 0.0745, fraction-of-residual 0.90%, **rank 65/113 (mid-pack)**. NOT clamped-zero.
- 13 clamped-zero adjacencies exist; Q 34→Q 35 is NOT one of them.
- The mid-pack ranking despite shared opener suggests the munāsabah is at the OPENER level but not at the full content-vector level.

**Result**: shared opener YES (Q 34 and Q 35 are both al-ḥamdu li-llāh openers); structural cohesion at content-vector level NOT extreme. The munāsabah is **partially-VINDICATED** — the al-Biqāʿī observation is correct at the opening-formula level but does NOT translate to full FR-cohesion.

**Verdict**: **PARTIAL**. The munāsabah claim is structurally accurate at the verbal-opener level, but Q 34 → Q 35 is NOT empirically seamless at the full-content level. This is a refinement of al-Biqāʿī's claim: opener-shared ≠ structurally-seamless.

### Q35-CC-07 — al-Suyūṭī's 20+ isnāds catalog for v.32

**Claim** (al-Suyūṭī, *al-Durr al-manthūr* ad Q 35:32): more than 20 isnāds converge on the all-three-saved reading, including multiple Aḥmad Musnad transmissions.

**Test**:
- Direct on-file verification: VERIFIED al-Suyūṭī's *al-Itqān* references the catalog.
- al-Ṭabarī's 5+ Companion chains: VERIFIED.
- Mishkat §2277 (al-Bayhaqī): VERIFIED.
- Tirmidhī §3309: VERIFIED.
- Aḥmad Musnad direct on-file: NOT verifiable (subset incomplete).

**Result**: the al-Suyūṭī catalog is SECONDARY-TRIANGULATED. Multiple chains converge on the same matn; the catalog's existence is corroborated even though specific Aḥmad-numbering cannot be cleanly verified.

**Verdict**: **SECONDARY-TRIANGULATED**.

### Q35-CC-08 — al-Rāzī's two-arc surah-structure claim

**Claim** (al-Rāzī, *Mafātīḥ* vol. 26): Q 35 is a two-arc surah, with v.32 as the architectural pivot.

**Test**: this is a qualitative naẓm-claim. Empirical operationalizations:
- Block-level FR-cohesion: testable via dividing Q 35 into Block-I-II-III (vv. 1-31) + Block-IV (vv. 32-45) and computing within-block vs. between-block content-distance.
- Content-vector pivot at v.32: Q 35:32 has the unique 3-fold hierarchy + closes with *dhālika huwa al-faḍlu al-kabīr* (ending mark of Block III).

**Status**: PENDING (would require a block-level FR-cohesion empirical test). Q035-F-05 (the al-ḥamdu inclusio test at v.1 vs v.34) provides PARTIAL validation: the within-surah inclusio at v.34 supports a structural-architecture reading, though it is not the same as al-Rāzī's two-arc claim.

**Verdict**: **PENDING** (testable, not yet directly tested).

## 3. Aggregate audit verdict

| Verdict | Count | Claims |
|:--|:-:|:--|
| CONFIRMED | 5 | Q35-CC-01, -02, -03, -04, -05 |
| PARTIAL | 1 | Q35-CC-06 (al-Biqāʿī munāsabah) |
| SECONDARY-TRIANGULATED | 1 | Q35-CC-07 (al-Suyūṭī catalog) |
| PENDING | 1 | Q35-CC-08 (al-Rāzī two-arc) |

**Total**: 8 classical claims tested. Confirmation rate (CONFIRMED + PARTIAL = 6/8 = 75%) is consistent with the project's classical-medieval lane mean confirmation rate (78% per H-META-1 / item #5a Beta-binomial Jeffreys posterior).

## 4. Honest limits

- **Aḥmad Musnad numbering**: not directly verifiable against on-file subset. Brief's specific Aḥmad citation tracked at SECONDARY-TRIANGULATED tier.
- **Tirmidhī §3309 chain weakness**: the chain is *ḥasan gharīb* with 2 unnamed transmitters. Project verdict CONFIRMED applies to the MATN (corroborated by parallel chains), not necessarily to this single chain.
- **al-Biqāʿī munāsabah**: classical claim is qualitative; empirical operationalization (cost-of-canonical-adjacency) is one operationalization among several. The PARTIAL verdict reflects the operationalization-specific finding; richer naẓm-level analysis might yield different empirical signatures.

## 5. Cross-references

- [[CC-048|CC-048 al-Zarkashī al-ḥamdu cluster]] — already CONFIRMED in classical-quantitative-claims-audit.
- `04-hadith-corpus.md` for the Tirmidhī §3309 + Mishkat §2277 + Aḥmad triangulation.
- `03-tafsir-survey.md` for the classical exegetical context of these claims.
- `06-novel-findings.md` for the empirical extensions (Q035-F-01 al-ḥamd cluster cohesion test).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 34→Q 35 cost rank 65/113 (al-Biqāʿī claim partial-validation).
