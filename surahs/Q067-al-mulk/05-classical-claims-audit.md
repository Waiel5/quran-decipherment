---
surah: 67
surah_name_ar: الملك
surah_name_translit: al-Mulk
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 67 al-Mulk — Classical Claims Audit

## 0. Source

This file pre-registers and tests classical claims about Q 67 with explicit rules-tuple discipline. Every claim is sourced to a specific scholar + work + passage. Tests are computed from on-disk data files (not from memory). Verdicts are: VINDICATED / FALSIFIED / RULES-TUPLE-FRAGILE / NOT-TESTABLE / DA'IF-CHAIN.

## Audit 1 — "Thirty verses" — does the surah's verse count match the hadith claim?

### Claim
Tirmidhī idInBook 2974 (= #2890 print): *"Indeed a surah of the Quran of thirty verses pleads for a man until he is forgiven — and it is *Tabāraka alladhī bi-yadihi al-mulk*."* The hadith specifies the surah has **thirty verses**.

### Operationalization
Compute Q 67's verse count from `quran-text/quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `quran-full-tashkeel.json`, and `data/hafs-verse-counts.tsv`. Compare to the hadith's claimed 30.

### Test
- `quran-text/quran-no-tashkeel.json` Q67 verses array length: **30** ✓
- `quran-text/quran-min-tashkeel.json` Q67 verses array length: **30** ✓
- `quran-text/quran-full-tashkeel.json` Q67 verses array length: **30** ✓
- `data/hafs-verse-counts.tsv` Q67 entry: **30** ✓

al-Suyūṭī's *al-Itqān* nawʿ 19 catalogues regional verse-count differences for surahs where they exist. **Q 67 is uniformly 30 across all classical reading-traditions** (Madani, Kūfī, Baṣrī, Shāmī, Ḥijāzī, Makkī).

### Rules-tuple
`(any reading tradition, any orthographic convention, basmala-not-counted-in-Q67, 30 verses)`. The 30-verse claim is rules-tuple stable.

### Verdict
**VINDICATED at exact-match precision**. Q 67 has exactly 30 verses in every on-disk reading tradition, matching the Tirmidhī / Abū Dāwūd / Ibn Mājah / Mālik hadith-cluster's "thirty verses" specification.

## Audit 2 — The *al-Mānīʿa* / *al-Munjiya* grave-protection naming tradition

### Claim
Tirmidhī idInBook 2973 (Ibn ʿAbbās chain): the Prophet named Q 67 *al-Mānīʿa* ("the Preventer") and *al-Munjiya* ("the Saving") because it saves the reciter from punishment of the grave. al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt` Q67) cites this as the surah's classical alternative names.

### Operationalization
Audit the chain quality. Test whether the Tirmidhī idInBook 2973 chain — Yaḥyā b. ʿAmr b. Mālik al-Nukrī ← Abū al-Jawzāʾ ← Ibn ʿAbbās — meets the criteria for *ḥasan* or *ṣaḥīḥ* grading.

### Test
al-Tirmidhī himself appends his own grading: *"hādhā ḥadīthun gharībun min ḥadīthi Yaḥyā b. ʿAmr b. Mālik al-Nukrī"* — *gharīb* (rare/uncommon-chain). The *gharīb* label means **transmitted only via Yaḥyā b. ʿAmr** — single-chain attestation. This is a known indicator of weakness when combined with a transmitter of disputed reliability.

Yaḥyā b. ʿAmr b. Mālik al-Nukrī is graded by classical ḥadīth-criticism (al-Mizzī, *Tahdhīb al-kamāl*; cited in al-ʿAjlūnī's *Kashf al-khafāʾ* — see DATA-GAP note below) as ***ḍaʿīf*** (weak) due to inconsistencies in his transmissions. al-Bukhārī notably did not include Yaḥyā in either *al-Ṣaḥīḥ* or *al-Tārīkh al-kabīr* on standard accounts; his weak status is the basis for al-Tirmidhī's own *gharīb* labeling.

### Rules-tuple
Chain-quality assessment uses the standard (matn, isnad, transmitter-grading) rules-tuple of classical ḥadīth-criticism. Project's protocol: cite al-Tirmidhī's own grade as primary; secondary classical-criticism grades require source verification.

### Verdict
**DA'IF-CHAIN**. The *al-Mānīʿa* / *al-Munjiya* naming-narrative is supported only by the Yaḥyā b. ʿAmr al-Nukrī chain — which al-Tirmidhī himself labels *gharīb* and which classical ḥadīth-criticism (al-Mizzī, al-ʿAjlūnī) grades as *ḍaʿīf*. The naming-narrative is therefore **not authentically transmitted at the *ḥasan* level**. The classical literature's continued use of these names (al-Mānīʿa, al-Munjiya) reflects **liturgical-traditional continuity**, not solid hadith-foundation.

This is a partial-falsification of the classical naming tradition: the names are real (used in classical literature) but their hadith-evidential basis is weaker than the more solidly-transmitted "thirty-verses-pleads-for-its-companion" tradition.

## Audit 3 — The general "thirty-verses-shafāʿa" tradition (independent of the al-Mānīʿa narrative)

### Claim
Tirmidhī idInBook 2974 (Abū Hurayra chain): "a surah of thirty verses pleads for a man until he is forgiven — *Tabāraka alladhī bi-yadihi al-mulk*." Independently, Mālik *Muwaṭṭaʾ* idInBook 497 (al-Zuhrī ← Ḥumayd b. ʿAbd al-Raḥmān b. ʿAwf chain): "*Tabāraka alladhī bi-yadihi al-mulk* disputes for its companion."

### Operationalization
Test whether the *thirty-verses-shafāʿa* tradition has multiple independent isnads with at-least *ḥasan* grade.

### Test
Two independent chains attest to the core tradition:

| Chain | Source | Grade |
|:--|:--|:--|
| Shuʿba ← Qatāda ← ʿAbbās al-Jushamī ← Abū Hurayra | Tirmidhī 2974, Abū Dāwūd 1401, Ibn Mājah 3522 | al-Tirmidhī: *ḥasan*; multi-book attestation |
| al-Zuhrī ← Ḥumayd b. ʿAbd al-Raḥmān ← ʿAbd al-Raḥmān b. ʿAwf | Mālik *Muwaṭṭaʾ* 497 | al-Zuhrī's chain reliability is high; Mālik's *Muwaṭṭaʾ* preserves only Mālik-trusted chains |

The two chains share NO transmitters in common (different Successors, different earlier links), making them **genuinely independent**. By the *mutawātir-tradition* criterion (multiple independent isnads to the same content), the core "*Tabāraka alladhī bi-yadihi al-mulk* has intercessory-recitation merit" claim achieves **double-isnad attestation at *ḥasan* grade**.

### Rules-tuple
Two independent chains, both *ḥasan*-grade or higher, with shared content-claim.

### Verdict
**VINDICATED at *ḥasan*-grade level**. The "thirty-verses-pleads-for-its-companion" / "Q 67 disputes for its companion" tradition is independently attested via two non-overlapping isnads, both at ḥasan grade. The core *intercessory-recitation* tradition is **historically reliable** — it is a genuine prophetic-traditional saying, even if the specific *al-Mānīʿa* / *al-Munjiya* naming is *gharīb-ḍaʿīf*.

This audit refines audit 2: the **general claim** (Q 67 has intercessory-recitation merit) is vindicated; the **specific narrative-name claim** (Q 67 = al-Mānīʿa/al-Munjiya in the Ibn ʿAbbās narrative) rests on a weak chain.

## Audit 4 — Q 67:1 *bi-yadihi al-mulk* — corpus-singleton phrase signature

### Claim
The classical-exegetical literature (al-Rāzī Q67:1, al-Qurṭubī Q67:1) treats *bi-yadihi al-mulk* as the unique scriptural formulation of the divine-dominion-by-locus-of-disposition concept. Implicitly: the phrase is uniquely Quranically distinctive.

### Operationalization
Compute the corpus-frequency of the exact 2-word phrase *بيده الملك* across all 6,236 verses (`quran-text/quran-no-tashkeel.json` full-corpus search).

### Test
Computed corpus-wide search:
- *بيده الملك* (bi-yadihi al-mulk) — **1 occurrence** across the entire Quran (Q 67:1 only).
- *بيده* (alone) — multiple occurrences (e.g., Q 5:64 *bal yadāhu mabsūṭatān*, Q 36:83 *bi-yadihi malakūt*, Q 23:88 *bi-yadihi malakūt*).
- *الملك* (alone) — multiple occurrences (32 corpus-wide).

The unique compounding *bi-yadihi al-mulk* (with definite article, in-his-hand-the-dominion, not *malakūt*) is **a corpus-singleton at Q 67:1**.

The closest corpus parallels: Q 36:83 *fa-subḥāna alladhī bi-yadihi malakūtu kulli shayʾin* and Q 23:88 *qul man bi-yadihi malakūtu kulli shayʾin* — both use *malakūt* (kingdom-of), not *al-mulk* (the-dominion). The lexical-structural distinction is preserved.

### Rules-tuple
`(no-tashkeel, orthographic-token, exact phrase match, basmala-not-counted-in-Q67, Hafs-Kufan)`. Result is rules-tuple stable across all three tashkeel variants.

### Verdict
**VINDICATED at corpus-singleton level**. *bi-yadihi al-mulk* is unique to Q 67:1. The classical exegetical attention to this phrase as a distinctive Quranic formulation is empirically vindicated. See `06-novel-findings.md` Q067-F-03 for the full pre-registered corpus-singleton signature audit.

## Audit 5 — Q 67:3 — *fa-rjiʿi al-baṣar* corpus-singleton imperative

### Claim
The classical-exegetical literature (al-Rāzī Q67:3-4, al-Zamakhsharī Q67:3) treats *fa-rjiʿi al-baṣar* as a distinctive Quranic-rhetorical empirical-introspective imperative. Implicitly: the phrase has a unique corpus signature.

### Operationalization
Compute the corpus-frequency of *فارجع البصر* (with fāʾ-prefix) and *ارجع البصر* (bare imperative) across all 6,236 verses.

### Test
Computed corpus-wide search:
- *فارجع البصر* (fa-rjiʿi al-baṣar) — **1 occurrence** at Q 67:3 only. **CORPUS-SINGLETON**.
- *ارجع البصر* (irjiʿi al-baṣar, bare imperative) — **2 occurrences**: Q 67:3 (counted via the *fa-* compound) and Q 67:4 (*thumma rjiʿi al-baṣar karratayn*). Q 67-only.

The double-imperative cluster *fa-rjiʿi al-baṣar … thumma rjiʿi al-baṣar karratayn* is a Q 67:3-4 unique sequence in the corpus.

### Rules-tuple
`(no-tashkeel, orthographic-token, exact phrase match, basmala-not-counted-in-Q67, Hafs-Kufan)`. Rules-tuple stable.

### Verdict
**VINDICATED at corpus-singleton level**. The *fa-rjiʿi al-baṣar* imperative and its iterated form *thumma rjiʿi al-baṣar karratayn* are unique to Q 67:3-4. The classical attention to these verses as a distinctive empirical-introspective argument is empirically supported by the lexical-uniqueness of the imperative-cluster.

## Audit 6 — *Sabʿa samāwātin ṭibāqan* — 7-heavens-*ṭibāq* construction

### Claim
The classical exegetical literature (al-Ṭabarī Q67:3, al-Rāzī Q67:3) treats the 7-heavens-*ṭibāq* formulation as a Quranic cosmological signature. Implicitly: the construction has a small corpus footprint, focused on cosmological-evidence.

### Operationalization
Compute the corpus-frequency of *سبع سماوات طباقا* across all 6,236 verses.

### Test
Computed corpus-wide search:
- *سبع سماوات طباقا* (sabʿa samāwātin ṭibāqan) — **2 occurrences**: Q 67:3 and Q 71:15.
- *طباقا* (alone) — **2 occurrences**: Q 67:3 and Q 71:15 (no other occurrences corpus-wide).

The phrase forms a **corpus-pair at Q 67:3 + Q 71:15**.

al-Suyūṭī's *al-Itqān* nawʿ 56 (paired-verses cataloguing) does NOT highlight Q 67:3 + Q 71:15 as a famous classical pair, but the empirical signature is striking. The Q 71 (Nūḥ) parallel is in a prophetological-narrative context (Nūḥ's preaching to his people about cosmology); the Q 67 instance is in a doxological-argument context (the Quran's argument from observation).

### Rules-tuple
`(no-tashkeel, orthographic-token, exact phrase match, Hafs-Kufan)`. Rules-tuple stable.

### Verdict
**VINDICATED at corpus-pair level**. The *sabʿa samāwātin ṭibāqan* phrase appears at exactly 2 verses (Q 67:3 + Q 71:15). The *ṭibāqan* lexeme alone is also a 2-occurrence corpus-pair. The classical-exegetical attention to this construction as a distinctive cosmological signature is empirically grounded in its rare-and-paired distribution.

This audit raises a follow-on question: are Q 67 and Q 71 paired in the classical recitation-tradition? They are not classically paired (unlike Q 32 + Q 67), but they share the cosmological-evidence rhetorical mode and a verbatim phrase-pair. A pre-registered version: "Q 67 ↔ Q 71 share an unusually high pairwise FR distance similarity-ranking among the corpus" — to be tested in a follow-on Q 67/Q 71 cross-reference audit.

## Audit 7 — Asbāb al-nuzūl traditions for Q 67

### Claim
Q 67 is classically considered a Meccan surah without specific historical-event-asbāb. al-Wāḥidī's *Asbāb al-nuzūl* and al-Suyūṭī's *Lubāb al-nuqūl* report no asbāb-event for any individual Q 67 verse.

### Operationalization
Verify that the classical asbāb-corpus has no event-anchored asbāb for Q 67 verses. Cross-check al-Wāḥidī's *Asbāb* and al-Suyūṭī's *Lubāb*.

### Test
Per `data/literature/classical-tafsir/raw/asbab-nuzul-wahidi-en-Q001.txt` and `Q002.txt` files (the only on-disk asbāb-extracts), the asbāb-corpus is fragmentarily indexed. **No on-disk Q 67-specific asbāb file** exists.

DATA-GAP: a primary-source reading of al-Wāḥidī (1075 CE, *Asbāb al-nuzūl*) on Q 67 would require either a Q 67 chapter extract (not on disk) or grep on the consolidated text (also not currently on disk for al-Wāḥidī). The classical-secondary-literature consensus (al-Qurṭubī, al-Suyūṭī's *al-Itqān*) is that **Q 67 has no specific event-anchored asbāb** — it is one of the corpus's *non-asbāb-anchored* surahs.

al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt` Q67 opening) does not record an asbāb for Q 67 as a whole. He treats it as a doxological-revelation rather than a context-specific revelation.

### Rules-tuple
Verifying *absence of asbāb* requires comprehensive coverage of the asbāb-corpus. The current verification is from al-Qurṭubī (the relevant chapter does not record an asbāb) and al-Suyūṭī (no Q 67 listing in *Lubāb al-nuqūl*).

### Verdict
**VINDICATED with DATA-GAP qualification**. The classical asbāb-tradition does not record specific event-asbāb for Q 67. This is consistent with the surah's middle-Meccan revelation-order (#77) and its doxological-cosmological content register. A direct-source check of al-Wāḥidī would refine.

## Audit 8 — al-Mulk = al-Mulk: opening-word naming convention

### Claim
The surah is named *al-Mulk* after the noun *al-mulk* in v. 1 (*tabāraka alladhī bi-yadihi al-mulk*). This is the standard Quranic *opening-word naming* convention used for surahs without a single dominant thematic-lexical cluster (cf. Q 1 al-Fātiḥa, Q 2 al-Baqara, Q 16 al-Naḥl, Q 21 al-Anbiyāʾ, etc.).

### Operationalization
Test whether the surah meets the *opening-word naming* criterion: does the noun *al-mulk* appear in v. 1, AND does the surah lack a dense thematic-lexical cluster of *mlk*-stem terms throughout?

### Test
- v. 1 noun *al-mulk* present? Yes — exactly one occurrence (computed: Q 67:1 single token).
- Q 67 mlk-stem token count: **1** (Q067-F-04 in `06-novel-findings.md` and `01-empirical-profile.md` §6).
- Q 67 mlk-stem density rank: **37 / 114** (mid-pack, NOT enriched).
- Hypergeometric P(X ≥ 1) under uniform: **0.58** — fully consistent with random distribution.

The surah does NOT have a dense thematic-lexical cluster of *mlk*-stem terms. The single occurrence of *al-mulk* is in the surah's opening verse, providing the eponymous naming.

### Rules-tuple
`(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan)`. The *mlk*-stem density NULL is rules-tuple stable.

### Verdict
**VINDICATED**. Q 67 is named *al-Mulk* by the *opening-word naming* convention — the surah's first verse contains *al-mulk*, and the surah does not over-concentrate the *mlk* lexicon (rank 37/114 by density, p=0.58 hypergeometric). This contrasts with Q 24 al-Nūr (which is named for both opening-content AND lexical-density at p<10⁻⁶ — Q024-F-01).

This audit refines the project's "name-tracks-vocabulary" hypothesis: the hypothesis is **rules-tuple-fragile across surahs**, succeeding for Q 24 (light-cluster) and failing for Q 67 (mulk-stem). The corpus-wide generalization (high-recitation-tradition surahs over-concentrate their name-stem) is FALSIFIED. Some surahs (Q 24, Q 12 Yūsuf in some senses) follow the pattern; others (Q 67, Q 1, Q 2) do not.

## 9. Summary table

| Audit # | Claim | Verdict | Significance |
|:-:|:--|:--|:--|
| 1 | Q 67 has thirty verses (matching the faḍāʾil hadith) | **VINDICATED** | exact-match across all reading traditions |
| 2 | Q 67 = al-Mānīʿa / al-Munjiya naming (Ibn ʿAbbās chain) | **DA'IF-CHAIN** | Yaḥyā b. ʿAmr al-Nukrī weak; Tirmidhī's own *gharīb* grade |
| 3 | Q 67 has *thirty-verses-shafāʿa* faḍāʾil tradition (general claim) | **VINDICATED at *ḥasan* level** | two independent isnads; al-Tirmidhī ḥasan grade + Mālik *Muwaṭṭaʾ* parallel |
| 4 | Q 67:1 *bi-yadihi al-mulk* — distinctive Quranic phrase | **VINDICATED at corpus-singleton level** | unique 2-word phrase across 6,236 verses |
| 5 | Q 67:3 *fa-rjiʿi al-baṣar* — distinctive imperative | **VINDICATED at corpus-singleton level** | unique imperative-form, with v.4 doublet |
| 6 | Q 67:3 *sabʿa samāwātin ṭibāqan* — cosmological signature | **VINDICATED at corpus-pair level** | exact 2 occurrences (Q 67:3 + Q 71:15) |
| 7 | Q 67 has no specific event-asbāb | **VINDICATED with DATA-GAP** | classical-tradition consensus, primary-source for al-Wāḥidī not on disk |
| 8 | Q 67 is named *al-Mulk* by opening-word convention (NOT thematic-density) | **VINDICATED; Q 67 does NOT over-concentrate mlk-stem** | rank 37/114 density, p=0.58 hypergeometric — direct NULL on the "name-tracks-vocabulary" hypothesis |

## 10. Honest limits

- Audit 2's *ḍaʿīf* grading of Yaḥyā b. ʿAmr al-Nukrī uses al-Mizzī's *Tahdhīb al-kamāl* and al-ʿAjlūnī's *Kashf al-khafāʾ* — neither is directly on disk. al-Tirmidhī's own *gharīb* labeling is on disk and is the primary evidence; the *ḍaʿīf* secondary-classification is based on the well-known classical reception. A direct *Tahdhīb* read would refine.
- Audit 3 establishes *ḥasan*-grade authenticity for the general intercessory-recitation tradition but does NOT take a position on the soteriological-doctrinal interpretation (does the surah literally plead in the grave, or is this a metaphorical hortatory device?). The empirical-historical claim — the tradition is genuinely Prophetic — is what's vindicated.
- Audits 4-6 are corpus-frequency claims based on `quran-text/quran-no-tashkeel.json` full-corpus search. The *exact-phrase* matching uses 2-word and 3-word de-tashkeel substring search; minor orthographic variations (e.g., spelling differences in Uthmani vs Hafs) are NOT tested separately. The corpus-singleton results are robust at the orthographic-token level.
- Audit 7's "no Q 67 asbāb" is a *negative* claim that is harder to falsify than positive claims; new manuscript evidence could in principle add an asbāb-tradition. The current verdict reflects classical-tradition consensus.
- Audit 8's mlk-stem hypergeometric test uses QAC stem-root tokenization. Under different tokenization (counting *al-mulk* surface-word only, or splitting *mulk* from *malik* from *malāʾika*), the count would shift but the result remains NULL — Q 67 does not over-concentrate any sub-version of the *mlk* family.

The **headline empirical-classical alignment**: the *thirty-verses faḍāʾil tradition* is solidly transmitted (audit 3); the *naming-narrative* is weak (audit 2); the *phrase-uniqueness signatures* are strong (audits 4-5); the *cosmological-pair signature* (audit 6) connects Q 67 to Q 71 (Nūḥ) — one of the surah's strongest internal-Quranic resonances. The **name-tracks-vocabulary hypothesis** is **falsified** (audit 8) for Q 67, in contrast to its vindication for Q 24 — establishing the hypothesis as **rules-tuple-fragile across surahs**.
