---
surah: 29
surah_name_translit: al-ʿAnkabūt
file_type: classical-claims-audit
date_last_updated: 2026-05-10
phase: B+
verdict: "5 classical claims audited; 2 VINDICATED (al-Rāzī spider-parable uniqueness via Q029-F-03 + Q029-F-04; Saʿd b. Abī Waqqāṣ asbāb via Tirmidhī #3273), 1 RULES-TUPLE-FRAGILE (al-Biqāʿī Q 29 → Q 30 munāsabah PARTIAL at whole-surah, NULL at pericope-scale), 1 PARTIALLY-VINDICATED (al-Bāqillānī iʿjāz al-tashbīh — Q 29:41 corpus-singleton supports the doctrine descriptively), 1 NOT-TESTABLE-EMPIRICALLY (al-Wāḥidī asbāb specificity at vv 1-3)"
---

# Q 29 al-ʿAnkabūt — Classical Claims Audit

This file audits 5 non-trivial classical claims about Q 29 with empirical rules-tuple. Pre-registered tests housed at `preregs/Q029-F-NN-*.md`.

## Claim 1 — al-Rāzī (*Mafātīḥ al-ghayb* on Q 29:41): the spider-parable is paradigmatic of *mathal* with corpus-distinctive vehicle

### Statement

al-Rāzī's commentary on Q 29:41 (cross-referenced via secondary literature; physical-edition page-citation MW-6-PENDING for Cairo 1934 edition) treats the spider-parable as paradigmatic of *mathal* (similitude) where the vehicle (spider's web) is **uniquely apt** for the tenor (idol-worshippers' apparent shelter). The classical reading distinguishes the spider-web parable from other Quranic *amthāl* on grounds that:
- The vehicle is a CORPUS-DISTINCTIVE animal (per al-Rāzī's note that the parable is unique in style).
- The common property (fragility-of-shelter) is uniquely instantiated.
- The lemma *ʿankabūt* is not used elsewhere in the Quran (al-Rāzī's claim, indirectly attested).

### Rules-tuple

`(QAC v0.4, LEM+ROOT tags, no-tashkeel, Hafs-Kufan)`.

### Empirical test

- **Q029-F-03** (corpus-singleton verification): VINDICATED — *Eankabuwt* lemma is corpus-singleton (2 tokens, 1 verse: Q 29:41 alone).
- **Q029-F-04** (typological-uniqueness verification): VINDICATED — Q 29:41 is the unique corpus-instance of the joint schema {animal-vehicle + shelter-lemma + frailty-root}. 3/3 sub-claims PASSED.

### Verdict: **VINDICATED**

al-Rāzī's qualitative claim about the spider-parable's corpus-distinctive character is now law-strength under QAC v0.4 lemma-tagging: the parable is empirically corpus-unique on three independent axes (lemma, frailty-superlative, joint-schema).

## Claim 2 — Tirmidhī #3273 (Saʿd b. Abī Waqqāṣ asbāb for Q 29:8)

### Statement

Tirmidhī #3273: Muṣʿab b. Saʿd ← Saʿd: "Four āyāt were revealed about me ... Umm Saʿd had said: 'Did not Allah command you to honor [your parents]. By Allah! I will not eat or drink anything until I die or you renounce [Islam].' ... So this āyah was revealed: 'And We have enjoined on man to be dutiful to his parents; but if they strive to make you associate [partners] with Me, of which you have no knowledge, then obey them not (29:8).'"

### Rules-tuple

`(hadith-corpus, Tirmidhī ed., chain-grading)`.

### Empirical test

- **Hadith-existence**: VERIFIED — Tirmidhī #3273 exists in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` at idInBook=3273, chapterId=47 (per `04-hadith-corpus.md` §1).
- **Verse-anchoring**: VERIFIED — Tirmidhī text explicitly cites Q 29:8.
- **Grading**: standard Tirmidhī assessment is *ḥasan ṣaḥīḥ*; the precise grading text was NOT in the spa5k extract for this entry (MW-6 PENDING physical-edition verification).
- **Parallel chains**: cross-narrations exist in Muslim *Faḍāʾil al-Ṣaḥābah* and al-Bukhārī *Adab al-Mufrad* (per Wāḥidī's anthologizing).

### Verdict: **VINDICATED**

The Saʿd b. Abī Waqqāṣ asbāb tradition for Q 29:8 is the unanimous classical anchor. The Tirmidhī text is present in our corpus and explicitly cites Q 29:8. Grading is conventionally *ḥasan ṣaḥīḥ*; physical-edition verification deferred.

## Claim 3 — al-Biqāʿī (*Naẓm al-durar*): Q 29 → Q 30 munāsabah as "promise → fulfillment"

### Statement

al-Biqāʿī's *Naẓm al-durar* (Damascus 1969/2003 edition) on the Q 29 → Q 30 surah-pair: Q 29:69 (*jāhadū fīnā la-nahdiyannahum subulanā*) announces divine guidance; Q 30:1-5 (*ghulibati al-Rūm fī adnā al-arḍi wa-hum min baʿdi ghalabihim sayaghlibūn*) is the historical-vindication of that guidance via the Byzantine-Persian prophecy. The pair forms a "promise → fulfillment" rhetorical-structural coupling.

### Rules-tuple

`(no-tashkeel, FR-distance on root-distribution, pericope and whole-surah scales)`.

### Empirical test

- **Q030-F-08 (whole-surah ALM-6 cluster)**: PARTIAL — Cell A NULL (p=0.418), Cell B length-matched PASS (p=0.0225). Q 29 ↔ Q 30 specifically: d_FR(29, 30) = 0.9153 (rank 7/15 within ALM cluster) — NOT a tight FR-pair.
- **Q029-F-02 (ALM-4 pericope cluster {Q 29, Q 30, Q 31, Q 32})**: NULL — pre-committed direction NOT MET. Pericope mean Jaccard = 0.0434 vs null mean 0.0497 (z = -0.25, p = 0.557, direction reversed). 4 of 6 pairs have J=0 (Q 29:1-3 ↔ Q 30:1-3 = 0; Q 29:1-3 ↔ Q 31:1-3 = 0; Q 30:1-3 ↔ Q 31:1-3 = 0; Q 30:1-3 ↔ Q 32:1-3 = 0).
- **Descriptive within-cluster** (from Q030-F-08): only Q 29 ↔ Q 32 (J=0.143) and Q 31 ↔ Q 32 (J=0.118) at pericope-scale have any root-overlap.

### Verdict: **RULES-TUPLE-FRAGILE → NULL at pericope scale**

al-Biqāʿī's qualitative *munāsabah* claim does NOT translate into root-distribution cohesion at either whole-surah scale (PARTIAL, length-confounded) or pericope-scale (NULL with reverse direction). The *munāsabah* operates at the THEMATIC / RHETORICAL level (Q 29 promise → Q 30 historical vindication) but NOT at the lexical-root level captured by Jaccard or FR-distance.

This is an instance of **cross-finding-025 (marker-thickness rule)**: the Q 29 → Q 30 connection is real qualitatively (promise/fulfillment + shared ALM opener + chronological adjacency) but the multi-axis correlation is too thin to drive root-Jaccard cohesion. The marker-thickness rule predicts NULL on root-FR for thin pairs without strong content-correlation; the empirical result confirms.

## Claim 4 — al-Bāqillānī (*Iʿjāz al-Qurʾān*): iʿjāz al-tashbīh — the inimitability of similitude

### Statement

al-Bāqillānī's *Iʿjāz al-Qurʾān* (Cairo 1374/1954 al-Saqqā ed.) identifies iʿjāz al-tashbīh as one of the rhetorical-inimitability axes of the Quran. The doctrine: Quranic similitudes are uniquely apt and corpus-distinctive in ways that pre-Islamic Arabic poetry does not match. The Q 29:41 spider-parable is a paradigmatic instance.

### Rules-tuple

`(QAC v0.4 lemma + root tagging, no-tashkeel, cross-corpus comparison pending)`.

### Empirical test

- **Q029-F-04**: VINDICATED descriptively — Q 29:41 is corpus-unique on the joint schema (3/3 sub-claims).
- **Cross-corpus test (pre-Islamic poetry control)**: NOT RUN HERE. Pre-Islamic poetry baseline at `data/baseline-corpora/raw/` could in principle be scanned for the same schema (animal-shelter-fragility) — queued as Q029-F-05 (post hoc to this audit, not pre-registered).

### Verdict: **PARTIALLY-VINDICATED (intra-Quran)**

al-Bāqillānī's *iʿjāz al-tashbīh* claim is vindicated WITHIN the Quran for the Q 29:41 case (the parable schema is corpus-unique). The full *iʿjāz* claim requires a cross-corpus comparison to pre-Islamic poetry, which is queued but not part of this audit. The intra-Quran result is law-strength; the cross-corpus comparison is pending.

## Claim 5 — al-Wāḥidī (*Asbāb al-nuzūl*): Q 29:1-3 occasion-of-revelation is the persecuted Meccan converts

### Statement

al-Wāḥidī (Cairo ed.) on Q 29:1-3: "These verses were revealed about some people in Mecca who embraced Islam. The Companions of the Prophet ﷺ in Medina wrote to them saying that their faith and embracing of Islam will not be accepted from them until they emigrate from Mecca. For this reason, they left Mecca with the intention of joining [the Prophet ﷺ and the believers in Medina; but were chased and afflicted by the Quraysh]." Cites al-Shaʿbī.

### Rules-tuple

`(asbāb al-nuzūl tradition; chain to al-Shaʿbī; standard al-Wāḥidī edition)`.

### Empirical test

- **Asbāb-existence**: VERIFIED — present in `data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/29/1.json` (per `04-hadith-corpus.md`).
- **Internal consistency with Q 29 content**: VERIFIED — the imtihān (testing) doctrine at Q 29:1-3 + the migration-verse Q 29:56 (*inna arḍī wāsiʿah*) are internally aligned with the persecution-and-Hijra context.
- **Specificity verifiable empirically?**: NO. The asbāb claim is about historical occasion (specific persons in Mecca, ca. 614-622 CE) — historical-asbāb specificity is not testable by corpus-distributional methods.

### Verdict: **NOT-TESTABLE-EMPIRICALLY**

The asbāb tradition is internally consistent and well-attested in the classical asbāb anthology, but its truth-value is a historical claim, not a corpus-distributional claim. We log it as VERIFIED-AT-SOURCE and NOT-TESTABLE empirically. This is the honest verdict per Protocol §2.9.

## Summary

| Claim | Source | Verdict |
|:--|:--|:--|
| 1 | al-Rāzī Q 29:41 spider-parable uniqueness | **VINDICATED** (Q029-F-03 + Q029-F-04 PASS 3/3) |
| 2 | Tirmidhī #3273 Saʿd asbāb for Q 29:8 | **VINDICATED** (hadith-corpus verified) |
| 3 | al-Biqāʿī Q 29 → Q 30 munāsabah | **RULES-TUPLE-FRAGILE → NULL at pericope** (Q029-F-02 NULL; Q030-F-08 PARTIAL) |
| 4 | al-Bāqillānī iʿjāz al-tashbīh | **PARTIALLY-VINDICATED (intra-Quran)** (Q029-F-04 PASS; cross-corpus pending) |
| 5 | al-Wāḥidī asbāb for Q 29:1-3 | **NOT-TESTABLE-EMPIRICALLY** (verified-at-source) |

## Honest limits

- Claim 1's al-Rāzī page-citation is MW-6-PENDING (physical edition not yet on disk).
- Claim 2's *ḥasan ṣaḥīḥ* grading was not in the spa5k extract; MW-6 PENDING.
- Claim 3 is a NULL pre-commit-direction-failure at pericope-scale — this is a strong negative finding under cross-finding-025. The qualitative *munāsabah* survives at the thematic level only.
- Claim 4 requires a cross-corpus pre-Islamic-poetry control to be fully tested (queued).
- Claim 5 is honest about the limit of empirical testing for historical-occasion claims.
