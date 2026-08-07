---
surah: 46
surah_name: al-Aḥqāf
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: HM-7 cluster member, HM-B closer (final ḥawāmīm), boundary surah to non-muqaṭṭaʿāt Medinan Q 47
---

# Q 46 — Sūrat al-Aḥqāf (The Sand-Dunes / The Curving Sands)


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

## 1. Identifiers

| Field | Value |
|:--|:--|
| Surah # | 46 |
| Arabic name | الأحقاف |
| Transliteration | al-Aḥqāf |
| English | "The Sand-Dunes" / "The Curving Sands" / "The Winding Tracts of Sand" |
| Verses (Hafs-Kufan) | 35 |
| Words (no-tashkeel, this session) | 676 |
| Letters (no-tashkeel, this session) | 2,698 |
| Type | Meccan |
| Position in mushaf | 46 (closes the ḥawāmīm-7 block, Q 40-46; **last** ḥawāmīm) |
| Position in revelation order | 66 (al-Suyūṭī chronology) — late Meccan |
| Opening formula | حم (verse 1, single muqaṭṭaʿāt) followed by *tanzīl al-kitāb min Allāh al-ʿAzīz al-ḥakīm* (v. 2) |
| Bismala status | Standard (not counted as verse) |
| Length class | mufaṣṣal-ṭiwāl (35 verses; **shortest** of HM-7) |

Verse, word, letter counts computed from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (this session).

## 2. The name *al-Aḥqāf* and Q 46:21

The surah is named after the geographic locus of the ʿĀd-Hūd narrative at Q 46:21:

> *وَاذْكُرْ أَخَا عَادٍ إِذْ أَنْذَرَ قَوْمَهُ بِالْأَحْقَافِ* — "And recall the brother of ʿĀd, when he warned his people at the **Aḥqāf**…" (Q 46:21, verbatim from `quran-text/quran-no-tashkeel.json`).

**Empirical fact (this session, verified)**: The root ح-ق-ف (Hqf) is a **CORPUS HAPAX**: it occurs **once and only once in the entire Qurʾān**, at Q 46:21, word-position 7 (`/Users/grey/Downloads/quran/data/morphology/root-index.json`: `"Hqf": [[46, 21, 7]]`). The eponymous root of Sūrat al-Aḥqāf is a single-token name. This makes Q 46 one of the strongest single-attestation eponym surahs in the corpus.

Classical glosses on *al-aḥqāf*:
- **al-Ṭabarī, *Jāmiʿ al-bayān*, ad Q 46:21**: *al-aḥqāf* is the plural of *ḥiqf* — "long, curving, winding hills/dunes of sand"; the geographic region of ʿĀd in southern Arabia (al-Aḥqāf in Yemen / al-Shiḥr / al-Yaman, multiple Companion-traditions).
- **al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, ad Q 46:21**: catalogs Companion-traditions identifying al-Aḥqāf with the region between ʿUmān and Ḥaḍramawt; Ibn ʿAbbās, Mujāhid, Qatāda agree on the *winding-sand-dune* lexical sense.

## 3. Position in the ḥawāmīm-7 cluster — HM-B closer

Q 46 is the **closing surah** of the ḥawāmīm-7 cluster (Q 40-46), the only consecutive 7-surah block in the Quran sharing a حم muqaṭṭaʿāt opening. Empirically (per [[hawamim-7-cluster-bifurcation]]) it falls into the **HM-B sub-block** (Q 43-46), the **near-monorhyme** prosodic cluster.

| Surah | rhyme entropy (bits) | distinct finals | top final |
|:-:|:-:|:-:|:-:|
| Q 40 | 2.413 | 8 | ن (38%) |
| Q 41 | 2.146 | 10 | ن (56%) |
| Q 42 | 2.565 | 9 | ر (38%) |
| — bifurcation midline — | | | |
| Q 43 | 0.594 | 3 | ن (88%) |
| Q 44 | 0.818 | 2 | ن (75%) |
| Q 45 | 0.700 | 2 | ن (81%) |
| **Q 46** | **0.952** | **3** | **ن (74.3%)** |

(Q 46 entropy 0.9518 bits, distinct finals = 3 (ن=26, م=8, ر=1), top final ن = 26/35 = 74.3%; computed this session from `quran-text/quran-min-tashkeel.json` and confirmed against `findings/cross-finding/csv/hawamim-7-cluster-bifurcation.json`.)

Q 46 is the **highest-entropy member of HM-B** (0.95 bits vs HM-B mean ~0.77 bits) but still well below HM-A's lowest (Q 41 = 2.15). The 3-final structure (ن، م، ر) is intermediate between HM-B's strict 2-final monorhyme and HM-A's 8-10-final dispersion.

Classical citations on the ḥawāmīm as a unit (carried forward from [[Q040-ghafir/00-overview|Q 40 overview]] §3 — these apply to Q 46 as the cluster's closing member):
- **Ibn Masʿūd** (via Abū ʿUbayd al-Qāsim b. Sallām, *Faḍāʾil al-Qurʾān*; cited in Ibn Kathīr, opening of Sūrat Ghāfir — see `data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt`): *al-ḥawāmīm dībāj al-Qurʾān* — "the ḥawāmīm are the brocade of the Qurʾān".
- **Ibn ʿAbbās** (ibid.): *li-kulli shayʾin lubābun, wa-lubābu al-Qurʾāni al-ḥawāmīm*.
- **Saʿīd b. Jubayr / Ibn Masʿūd** (ibid.): *idhā waqaʿta fī Āl Ḥā Mīm fa-qad waqaʿta fī rawḍātin ataʾannaqu fīhinna*.

## 4. Distinctive features

- **Corpus-hapax eponym (Hqf root)** at Q 46:21 — the *aḥqāf* topographic name appears nowhere else.
- **The Hūd / ʿĀd narrative** (Q 46:21-26) — a condensed retelling of the destruction of ʿĀd; cross-references to Q 7:65-72, Q 11:50-60, Q 26:123-140, Q 41:13-16.
- **The JINN-listening narrative** (Q 46:29-32) — *idh ṣarafnā ilayka nafaran min al-jinni yastamiʿūna al-Qurʾān* — "when We diverted to you a party (*nafar*) of the jinn listening to the Qurʾān". Together with Q 72 al-Jinn, these are the only two passages in the Qurʾān explicitly narrating jinn-encounter with the recited Qurʾān.
- **Q 46:15** (*thalāthūna shahran*) — pregnancy + nursing duration verse: *wa-ḥamluhu wa-fiṣāluhu thalāthūna shahran* — "his bearing and weaning is thirty months". The classical fiqh-anchor verse for the doctrine that minimum gestation = 6 months (cross-referenced with Q 31:14 *fiṣāluhu fī ʿāmayn*; the 30-month - 24-month subtraction yields 6-month minimum gestation).
- **Q 46:35** (*ūlū al-ʿazm*) — the closing verse: *fa-ṣbir kamā ṣabara ūlū al-ʿazmi mina al-rusul* — "be patient as the Resolute Messengers were patient". This is the classical anchor for the *ūlū al-ʿazm* (Resolute Messengers) doctrine identifying Nūḥ, Ibrāhīm, Mūsā, ʿĪsā, Muḥammad as the five highest-tier prophets (per al-Suyūṭī, *al-Itqān*, nawʿ 67).
- **Boundary surah**: Q 46 is the **last ḥawāmīm**; the transition Q 46 → Q 47 Muḥammad represents a triple discontinuity — (i) muqaṭṭaʿāt → no-muqaṭṭaʿāt, (ii) Meccan → Medinan, (iii) common-noun-named → person-named. Empirical adjacency cost is anchored at h-new-720 rank 42/113 (see §5).

## 5. Empirical fingerprint (cross-reference)

| Metric | Value | Source |
|:--|:--|:--|
| UAS rank | **91 / 114** | `h-new-840.json`, this-session re-rank |
| UAS score | **−1.591** | h-new-840 (entry: `{"surah": 46, "UAS": −1.5907}`) |
| Outlier-strength Δ%ile | **−2.34 (NULL)** | h-new-590 (`p_greater_W = 0.5271`) |
| iʿjāz signature sig_A | **−0.384** | h-new-750 (`{"surah":46,"sig_A":−0.3835}`) |
| iʿjāz signature sig_B | **−0.769** | h-new-750 |
| Top rāwī | ن (74.3%) | this session, min-tashkeel |
| Rhyme entropy (final-letter) | **0.952 bits**, 3 distinct finals | computed; matches HM-7 bifurcation file |
| 2-char rhyme suffixes | -ūn (13), -īn (13), -īm (7), -ḥm (1) | computed (regex on min-tashkeel) |
| Q 45 → Q 46 canonical-adjacency cost | 0.0959 (rank **37/113**) | h-new-720 |
| Q 46 → Q 47 canonical-adjacency cost | 0.0873 (rank **42/113**) | h-new-720 |
| Q 46 ↔ Q 41 FR-distance | **0.7254** (Q 46's nearest neighbor corpus-wide) | h-new-111, this-session reconstruction |
| Q 46 ↔ Q 72 (al-Jinn) FR-distance | 0.8854 | h-new-111 |
| Q 46 ↔ Q 11 Hūd FR-distance | 0.8518 | h-new-111 |
| Q 46 ↔ Q 7 al-Aʿrāf FR-distance | 0.8709 | h-new-111 |

Q 46's UAS rank 91/114 places it in the **bottom quartile** by Unified Architectural Significance — Q 46 is NOT a standalone architectural outlier. Its significance is sub-cluster (HM-B closer; HM-7 bookend). Compare to:
- Q 44 al-Dukhān UAS=−1.882 rank 95
- Q 45 al-Jāthiyah UAS=+0.350 rank 50
- Q 43 al-Zukhruf UAS=+0.537 rank 41

The HM-B sub-block carries Q 44 and Q 46 in the bottom quartile, with Q 43/45 at mid-corpus. Q 46's profile = **mild anchor + anti-fawāṣil (sig_A negative) + low UAS** — the *consolidated low-distinctness* signature.

## 6. Twin-axis classification

| Axis | Position |
|:--|:--|
| Structural-iʿjāz (al-Bāqillānī) | mild **anti**-iʿjāz (sig_A=−0.38; rank 72/114) |
| Theological-iʿjāz (al-Khaṭṭābī) | not in *thuluth al-Qurʾān* tradition; Q 46:35 *ūlū al-ʿazm* is a doctrinal anchor |
| Compression-tail | s=46 ≤ 50 → pre-kink (intra-50 baseline; d̄_content ≈ 0.96, d̄_rhyme ≈ 0.36) |
| Outlier | mild anchor (Δ=−2.34, p=0.527 NULL) |
| Cluster role | **HM-B closer; HM-7 final member; boundary to non-HM Medinan Q 47** |

Architectural type (per [[cross-finding-026-iʿjāz-architecture]]): **anti-iʿjāz / consolidated-monorhyme** sub-type. Q 46 falls in the same anti-iʿjāz cell as several short late-Meccan surahs but is anomalously LONG (35 verses) for the cell — the consolidated-monorhyme is achieved at mufaṣṣal-ṭiwāl scale, not just at short-surah scale.

## 7. Cross-references

- [[Q045-al-jathiyah/00-overview|Q 45 al-Jāthiyah]] — preceding HM-B neighbor (NOT yet built)
- [[Q047-muhammad/00-overview|Q 47 Muḥammad]] — following non-HM Medinan neighbor (NOT yet built); high-cost boundary
- [[Q040-ghafir/00-overview|Q 40 Ghāfir]] — HM-7 opener (HM-A); empirical reciprocal
- [[Q041-fussilat/00-overview|Q 41 Fuṣṣilat]] — Q 46's FR-NEAREST neighbor corpus-wide (FR=0.7254); HM-A
- [[Q011-hud/00-overview|Q 11 Hūd]] — Hūd-narrative twin (NOT yet built)
- [[Q007-al-araf/00-overview|Q 7 al-Aʿrāf]] — Hūd-narrative twin (NOT yet built)
- [[Q072-al-jinn/00-overview|Q 72 al-Jinn]] — jinn-listening twin (NOT yet built; investigation pending Wave-D 8-surah alif-monorhyme cluster)
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 46 = HM-B member
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Δ=−2.34 NULL
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — pre-kink position s=46
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 45→46 rank 37/113; Q 46→47 rank 42/113
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 91
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 46 cell membership

## 8. Honest limits

1. **UAS rank 91 is bottom-quartile** — Q 46 is NOT a corpus-extreme on the standalone metrics. Its significance lies in (i) HM-B closer role, (ii) corpus-hapax eponym (Hqf), (iii) the jinn-narrative as one of two corpus loci.
2. The "boundary cost" Q 46→Q 47 ranks 42/113 — moderate, NOT extreme. The high-cost-transition framing in the user prompt requires audit-level pre-registration before being treated as a structural finding (see [[06-novel-findings|Q046-F-01]]).
3. Q 46's classical name *al-Aḥqāf* maps to a single-verse hapax (Q 46:21); the eponymity is concentrated, not distributed.
4. Sister-surahs Q 11, Q 7, Q 72 are NOT yet built as full investigations — cross-references are unidirectional.
5. The HM-B prosodic monorhyme is established at the cluster level ([[hawamim-7-cluster-bifurcation]]); Q 46's individual contribution to the monorhyme is the moderately-mixed 3-final pattern (74% ن, 23% م, 3% ر), distinguishing it from the strictest monorhymes Q 44 (75% ن, 25% م) and Q 45 (81% ن, 19% م).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
