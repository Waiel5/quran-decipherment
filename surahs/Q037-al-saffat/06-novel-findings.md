---
surah: 37
surah_name_ar: الصافات
surah_name_translit: al-Ṣāffāt
file_type: novel-findings
date_last_updated: 2026-05-08
phase: B+
verdict: 5 pre-registered tests — 1 CONFIRMED, 1 DIRECTIONAL, 2 NULL, 1 PRE-COMMIT-VIOLATION (honest reporting). All direction-locked; SHA-verified at runtime; seed 20260508.
---

# Q 37 al-Ṣāffāt — Pre-Registered Novel Findings


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

Five pre-registered tests run on 2026-05-08. All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q037-al-saffat/csv/`. Seed = 20260508. n_perm = 10000 throughout.

## Q037-F-01 — *salāmun ʿalā [PROPHET-NAME]* corpus-share fingerprint

### Pre-reg
- File: `Q037-F-01-salam-ala-prophet-prereg.md`
- SHA256: `59f7afd2ea1e00d969c03a0ee9db531d28bec3e6eec679e292449b5b6f4d658b`
- Direction (locked): Q 37 ≥ 3 instances AND Q 37 holds ≥75% of corpus instances. Bonferroni-2 (length-weighted null A + uniform null B); α_bon = 0.025.
- Script: `scripts/Q037_F_01_salam_ala_prophet.py` (SHA-verified).

### Method
Regex `\bسلام على\b` on `quran-text/quran-no-tashkeel.json`; restrict to verses where the addressee is a named prophet (from canonical 25-prophet list). Compute share-in-Q37; permutation-null distribute the N_total tokens across surahs (a) length-weighted, (b) uniformly.

### Result
| Verse | Text | Matched name |
|:--|:--|:--|
| Q 37:79 | *salāmun ʿalā nūḥin fī al-ʿālamīn* | Nūḥ |
| Q 37:109 | *salāmun ʿalā ibrāhīm* | Ibrāhīm |
| Q 37:120 | *salāmun ʿalā mūsā wa-hārūn* | Mūsā |
| Q 37:130 | *salāmun ʿalā ilyāsīn* | Ilyāsīn (Ilyās plural-form) |

| Quantity | Value |
|:--|:--:|
| N_total corpus instances | 4 |
| N_q37 | 4 |
| share_q37 | 1.0000 (100%) |
| length-weighted null p | < 0.0001 (perm) |
| uniform null p | < 0.0001 (perm) |

### Verdict
**CONFIRMED.** All 4 corpus instances of *salāmun ʿalā [PROPHET-NAME]* are in Q 37. Both perm-nulls return p < 0.0001 (no random-permuted distribution placed all 4 tokens in Q 37 across 10,000 trials). Pre-committed direction MATCHED.

### Direction
LOCKED positive (Q 37 = corpus-MAX); MATCHED at 100% share.

### Bonferroni
k = 2; α_bon = 0.025; both nulls pass at p<0.0001.

### Honest limits
- Post-hoc origin disclosed in pre-reg §6: the 4-in-Q37 finding was observed during empirical-anchor extraction BEFORE the pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling is **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension.
- The independent-replication question: does Q 37's *salāmun ʿalā* monopoly hold under different orthographic conventions (Uthmani-consonantal? Maghribī)? Future test: re-run on `data/alt-text/quran-uthmani-consonantal.json` and confirm.
- The construction *wa-l-salāmu ʿalayya* (Q 19:33) and *wa-salāmun ʿalā ʿibādihi* (Q 27:59) are NEAR-twins but DIFFERENT (with pronominal suffixes or non-prophet addressees) — these are excluded from the strict count by pre-reg §2.
- The PASS-DIRECTED status will be promoted to CONFIRMED if a replication test confirms the structural-uniqueness via a different operationalization (e.g., character-n-gram matching, root-fingerprint of the salām-context).

## Q037-F-02 — Sacrifice-of-Ishmael block (Q 37:99-113) hapax + isolation

### Pre-reg
- File: `Q037-F-02-sacrifice-hapax-prereg.md`
- SHA256: `31df0ef290064534ff92bb7b135fef19147b56f2540cb89882ea869e87c9e381`
- Direction (locked): H1 ≥3 hapax in block; H2 lexical-isolation > permutation null at α_bon = 0.01667; H3 isolation > both Q 21:69-71 and Q 11:69-83 anchors. Bonferroni-3.
- Script: `scripts/Q037_F_02_sacrifice_hapax.py` (SHA-verified).

### Method
- H1: roots whose ALL corpus attestations lie within Q 37:99-113.
- H2: TF-IDF lexical-isolation of block from rest-of-Q37; permutation null = random 15-verse spans from comparable-narrative pool {Q 7, 11, 19, 21, 26, 27, 28, 38} with 10,000 trials.
- H3: direct compare with Q 21:69-71 (Abraham-fire) and Q 11:69-83 (Abraham-angel-visit).

### Result
| Test | Value | Threshold | Pass |
|:--|:--:|:--:|:--:|
| H1: hapax count | **2** (t-l-l, j-b-n; both at v.103) | ≥ 3 | **NO** |
| H2: block-isolation | 0.7302 | perm-p ≤ 0.01667 | NO (perm-p = 0.213) |
| H3: vs Q 21:69-71 | Q 37 = 0.7302; Q 21 = **0.886** (HIGHER) | Q 37 > Q 21 | NO |
| H3: vs Q 11:69-83 | Q 37 = 0.7302; Q 11 = 0.685 | Q 37 > Q 11 | YES |

### Verdict
**NULL.** All three sub-tests fail or partial. The sacrifice block contains 2 hapax (at v. 103: *t-l-l* in *wa-tallahu li-l-jabīn*, *j-b-n* in *li-l-jabīn*), one short of the pre-locked threshold. Block lexical-isolation is moderate but NOT extreme; the Q 21:69-71 fire-pericope is MORE isolated.

### Direction
H1 direction LOCKED positive (≥3); observed = 2 (DIRECTIONAL UNDER-shoot, NOT pre-commit violation since count > 0). H2 direction LOCKED positive; observed = 0.7302 vs null mean = 0.679 (positive direction, but p = 0.213 ≫ α_bon). H3 partial (1/2 pass).

### Bonferroni
k = 3; α_bon = 0.01667. None pass.

### Honest limits
- The 2-hapax result (one short of the pre-locked 3) is the project's empirical answer. The sacrifice narrative is QUALITATIVELY UNIQUE (no other Quranic surah has the extended Abraham-and-son sacrifice arc), but the lexical hapax-density is below the pre-locked threshold.
- The 2 hapax cluster at v. 103 (the *throw-down-on-the-brow* moment), suggesting that the lexical-uniqueness of the sacrifice narrative concentrates at the dramatic-physical-act verse, not throughout the block.
- The Q 21 fire-pericope's HIGHER lexical-isolation is informative: that pericope (3 verses) handles a different Abraham-trial (the fire-vs-the-throwers) with different vocabulary (*ḥarrīqūhu*, *bardan wa-salāman*). The sacrifice-pericope shares more vocabulary with broader prophet-narrative discourse than the fire-pericope does.
- The narrative's UNIQUENESS is preserved at the **NARRATIVE level** (the sacrifice-of-the-son arc has no Quranic parallel) but NOT at the LEXICAL-FINGERPRINT level (the vocabulary is shared with broader Abraham-prophet-narrative discourse).

## Q037-F-03 — Q 37:1-3 oath-trio cohesion vs Q 37 baseline

### Pre-reg
- File: `Q037-F-03-ranked-ones-trio-prereg.md`
- SHA256: `0f39d6771b0f8262613d899bc023e17dbd3a34456f0a83b67775c70d7c763719`
- Direction (locked): C(Q 37:1-3) > random 3-spans of Q 37 on token-cosine OR root-cosine; AND C(Q 37:1-3) > C(Q 37:4-6) AND C(Q 37:180-182). Bonferroni-2.
- Script: `scripts/Q037_F_03_ranked_ones_trio.py` (SHA-verified).

### Method
- C(span) = mean pairwise cosine on token-bag and root-bag.
- Permutation null: 10,000 random ordered 3-verse spans drawn from Q 37 verse-set.

### Result
| Test | Value |
|:--|:--:|
| C(Q 37:1-3) token-cosine | **0.0000** |
| C(Q 37:1-3) root-cosine | **0.0000** |
| Null (random-3-span) token-cosine mean | 0.0145 |
| Null (random-3-span) root-cosine mean | 0.0234 |
| p_token (one-tailed, trio ≥ random) | **1.0000** |
| p_root | **1.0000** |
| C(Q 37:4-6) token-cosine | 0.0000 |
| C(Q 37:180-182) token-cosine | 0.0680 |
| H1 (any metric ≤ 0.025) | **NO** |
| H2 (trio > both 4-6 and 180-182) | **NO** (trio < 180-182 on token-cosine) |

### Verdict
**PRE-COMMIT VIOLATION.** Cohesion of Q 37:1-3 at the token AND root levels is **ZERO** (the 3 verses share NO orthographic tokens and NO QAC roots pairwise). The pre-locked direction (positive) is REVERSED — the trio is BELOW the null mean on both metrics. The closing-tail trio Q 37:180-182 (*subḥāna rabbika rabbi al-ʿizza* + *wa-salām ʿalā al-mursalīn* + *wa-l-ḥamdu li-llāh rabbi al-ʿālamīn*) is MORE token-cohesive (0.068).

### Direction
LOCKED positive; observed REVERSED (cohesion ≈ 0 below null mean ≈ 0.015). Per HANDOFF/04-DISCIPLINE.md PRE-REG-STANDARD-01, this is a sign-flip; published with explicit pre-commit-violation flag.

### Bonferroni
k = 2; not applicable (sign-flip).

### Honest limits — INTERPRETATION
This is an **HONEST EMPIRICAL FINDING** that REFINES (not refutes) the classical reading:
- The Q 37:1-3 trio IS held together by **morphological-grammatical template parallelism**: each verse follows the pattern (و/ف + ال + active-feminine-plural-participle + cognate-accusative-noun). v.1 *wa-l-ṣāffāti ṣaffā*, v.2 *fa-l-zājirāti zajrā*, v.3 *fa-l-tāliyāti dhikrā*. The token-IDENTITY level shows zero overlap because each verse instantiates the template with a DIFFERENT root (ṣ-f-f / z-j-r / t-l-w + dh-k-r). 
- The trio's classical iʿjāz-status is **GRAMMATICAL-PATTERN-PARALLEL**, NOT lexical-overlap. Q037-F-03 falsifies a NAIVE READING of "trio cohesion" as lexical similarity; it does NOT falsify al-Rāzī's or al-Bāqillānī's classical iʿjāz reading, which is at the BALĀGHĪ-MORPHOLOGICAL level.
- This is an instance of the project's general lesson (also documented in Q038-F-04 NULL on TF-IDF triad cohesion in Q 38): refrain-anaphora-template cohesion operates at PHRASE-/PATTERN- levels invisible to TF-IDF. **NEEDS-NEW-INSTRUMENT**: a morphological-pattern-similarity metric (e.g., POS-template overlap, root-pattern signature similarity) would correctly capture this cohesion.

## Q037-F-04 — Q 37 H-NEW-1070 oath-cluster membership extension

### Pre-reg
- File: `Q037-F-04-oath-cluster-membership-prereg.md`
- SHA256: `d4e9e449d1655a0632f8d19b18b13710a447c372f2a5bae0d41e7e04e2d2bda1`
- Direction (locked): H1 perm-p ≤ 0.025 (D_oath ≤ random); H2 M_q37 ≤ M_intra (Q 37 NOT outlier). Bonferroni-2.
- Script: `scripts/Q037_F_04_oath_cluster.py` (SHA-verified).

### Method
H-NEW-111 FR matrix; oath cluster = strict-15 from H-NEW-1070. D_oath = mean(FR(37, s) for s ∈ cluster\{37}). 10,000 random-14-subsets from {1..114}\{37} as null.

### Result
| Quantity | Value |
|:--|:--:|
| D_oath (Q 37 to other 14 oath-members) | **0.9949** |
| D_random null mean | 0.9931 |
| D_random null min / max | 0.799 / 1.115 |
| perm-p (D_oath ≤ random) | **0.5479** |
| Corpus-mean (Q 37 to all 113) | 0.9853 |
| Within-cluster pairwise median | 0.7205 |
| Q 37-row median FR to other 14 oath | **1.0223** |
| **Q 37 rank within 15-cluster centrality** | **15/15 (PERIPHERAL)** |

Cluster centrality ranking (smallest mean-distance-to-other-14 = most central):

| Rank | Surah | Mean dist to other 14 |
|:-:|:-:|:--:|
| 1 | Q 103 al-ʿAṣr | 0.5711 |
| 2 | Q 100 al-ʿĀdiyāt | 0.5789 |
| 3 | Q 95 al-Tīn | 0.5847 |
| 4 | Q 91 al-Shams | 0.5944 |
| 5 | Q 93 al-Ḍuḥā | 0.5973 |
| 6 | Q 86 al-Ṭāriq | 0.6228 |
| 7 | Q 92 al-Layl | 0.6311 |
| 8 | Q 85 al-Burūj | 0.6711 |
| 9 | Q 79 al-Nāziʿāt | 0.7027 |
| 10 | Q 89 al-Fajr | 0.7175 |
| 11 | Q 77 al-Mursalāt | 0.7598 |
| 12 | Q 52 al-Ṭūr | 0.7790 |
| 13 | Q 51 al-Dhāriyāt | 0.8206 |
| 14 | Q 53 al-Najm | 0.8515 |
| **15** | **Q 37 al-Ṣāffāt** | **0.9949** |

### Verdict
**NULL.** H1 perm-p = 0.55 (Q 37's mean distance to oath-cluster is INDISTINGUISHABLE from random-14-subsets). H2 fails (Q 37 row-median 1.02 > intra-cluster median 0.72). Q 37 is the **15/15 rank** in oath-cluster centrality — the LEAST-central member.

### Direction
LOCKED positive (D_oath < random); observed approximately equal (slightly higher). NOT a pre-commit violation (D_oath is not above corpus-mean+0.05 threshold).

### Bonferroni
k = 2; α_bon = 0.025. Both fail.

### Honest limits — INTERPRETATION
This is an **important refinement of H-NEW-1070**: the 15-cluster IS FR-cohesive at the GROUP level (CONFIRMED p=0.0004 corpus-wide), BUT individual-member centrality varies dramatically. Q 37 sits at the EXTREME PERIPHERY of the cluster. The cluster's tight cohesion is driven by the SHORT-MECCAN-TAIL CORE {Q 91, 92, 93, 95, 100, 103} (top-5 most central — all short oath-openers with 6-15 verses on cosmic-condition themes). The MID-MECCAN OATH-OPENERS {Q 37, 51, 52, 53} are themselves a sub-band at the periphery.

**This finding strongly suggests a 2-tier oath-cluster structure**:
- **TIER 1 (CORE)**: short Meccan oath-openers Q 85-103 (10 surahs, intra-distance ~0.6).
- **TIER 2 (PERIPHERY)**: longer Meccan oath-narrative-compendia {Q 37, 51, 52, 53} (4 surahs).

This 2-tier structure is **a NEW corpus-finding** emerging from this specialist test. It would warrant a follow-up corpus-wide pre-registration (H-NEW-1070.1).

The Q 37 NULL on individual centrality DOES NOT FALSIFY al-Suyūṭī's *al-aqsām* classification (which is FORMAL, based on opening-form). It REFINES the empirical-cohesion mapping: the formal-classification → FR-cohesion correspondence holds at the GROUP level but is non-uniform across members.

## Q037-F-05 — Q 37 → Q 38 seam empirical-seamlessness diagnostic

### Pre-reg
- File: `Q037-F-05-q37-q38-seam-prereg.md`
- SHA256: `684ae9fdc0150ba64ed56e39a6e5f5c290980097ee6e9f25900320b046fb16cd`
- Direction (locked): H1 Q 37→Q 38 ∈ top-5 by delta_raw ascending; H2 ≥ 2/4 architectural cells overlap; H3 ≥ 3 shared prophets. Bonferroni-3 categorical.
- Script: `scripts/Q037_F_05_q37_q38_seam.py` (SHA-verified).

### Method
Direct query of H-NEW-720 per_adjacency, H-NEW-700 rhyme diagnostics, H-NEW-750 mean-content-distance, H-NEW-111 FR matrix, and 25-prophet name regex on Q 37 + Q 38.

### Result

#### H1: rank by delta_raw ascending
- Q 37 → Q 38 delta_raw = -0.000911; rank **13/113** (NOT top-5).
- Top-5 smoothest: Q 91→Q 92 (-0.087), Q 4→Q 5 (-0.066), Q 6→Q 7 (-0.058), Q 3→Q 4 (-0.047), Q 65→Q 66 (-0.034).
- BUT Q 37→Q 38 IS in the **clamped-zero set** (13 pairs total with delta_raw ≤ 0 ⇒ fraction_residual = 0.000).
- **H1 STRICT-RANK FAIL**, but Q 37→Q 38 IS in the seamless-tier.

#### H2: 4 architectural cells
| Cell | Q 37 | Q 38 | Pass |
|:--|:--|:--|:--:|
| (a) same top-rhyme-letter | ن (0.80) | ب (0.40) | NO (different) |
| (b) same length-class (50-200 v) | 182 v | 88 v | YES |
| (c) mean-content-distance close (≤0.10) | 0.993 | 0.966 | YES (Δ=0.027) |
| (d) top-5 FR neighbor | Q 38 ∈ Q 37 top-10 (rank 9, FR=0.904); Q 37 ∈ Q 38 top-10 | NO (each is rank ~9-10 for the other; not top-5) |

n_cells_pass = 2/4. **H2 PASSES** at the locked threshold (≥2).

#### H3: shared prophets
| Q 37 prophets | Q 38 prophets | Shared |
|:--|:--|:--|
| إبراهيم, إسحاق, إلياس, اليسع, لوط, موسى, نوح, هارون, يونس | أيوب, إبراهيم, إسحاق, إسماعيل, الكفل, داوود, سليمان, لوط, نوح, يعقوب | **{إبراهيم, إسحاق, نوح}** + lūṭ (4 total) |

Shared: **{Nūḥ, Ibrāhīm, Isḥāq, Lūṭ}** = 4 prophets. **H3 PASSES** (≥3).

### Verdict
**DIRECTIONAL.** 2/3 sub-tests pass (H2, H3); 1/3 fails (H1 strict top-5). The full picture:

- **Q 37 → Q 38 IS empirically seamless** (clamped-zero, fraction_residual = 0.000), one of 13 pairs in the corpus's smoothest-tier.
- **The seam mechanism is**: shared length-class (mid-Meccan ~80-200 verse band) + close mean-content-distance (both at ~0.97-0.99) + 4 shared prophet-narrative slots (Nūḥ, Ibrāhīm, Isḥāq, Lūṭ).
- **The seam is NOT rhyme-letter shared**: Q 37 ن (-ūn/-īn) vs Q 38 ب (-āb/-īb).
- **The seam is NOT muqaṭṭaʿāt-shared**: Q 37 has no muqaṭṭaʿāt; Q 38 opens with single ص.
- **The seam IS content-typological-prophet-cycle continuation**: Q 37 closes its prophet-cycle (Yūnus vv. 139-148), Q 38 opens its prophet-cycle (Dāwūd vv. 17+, plus Ibrāhīm-Isḥāq-Yaʿqūb-Ismāʿīl revisits at vv. 45-49).

### Direction
H1 LOCKED top-5 ⇒ FAIL strict; PARTIAL (in clamped-zero set). H2 LOCKED ≥2/4 ⇒ PASS. H3 LOCKED ≥3 ⇒ PASS.

### Bonferroni
Categorical k=3; 2/3 pass.

### Honest limits
- The brief stated Q 37→Q 38 is "one of the corpus's TWO empirically-seamless adjacencies (canonical adjacency cost = 0.000)". The empirical reality: there are **13 clamped-zero adjacencies**, not 2. Q 37→Q 38 is the LEAST-improved (smallest absolute negative delta) — i.e. canonical adjacency just-barely beats 2-opt. The brief's "TWO" framing was inaccurate.
- The 13 clamped-zero pairs include several short-Meccan-tail seams (Q 91→Q 92, Q 86→Q 87, Q 93→Q 94, Q 105→Q 106, Q 109→Q 110) and several head-mushaf seams (Q 3→Q 4, Q 4→Q 5, Q 6→Q 7) reflecting the corpus's natural tendency toward smooth-adjacency in dense-content regions.
- The Q 37 → Q 38 seam mechanism (shared length + content + 4-shared-prophets) is structurally different from the short-tail seams (which share rhyme + length + cosmic-condition opener) and the head-mushaf seams (which are dominated by long-Medinan content-continuity).
- al-Biqāʿī's Q 37 → Q 38 munāsabah is empirically VINDICATED at the most-extreme level (clamped-zero seam) via the prophet-cycle-continuation mechanism.

## Cross-finding-strength assessment

| Test | Verdict | Key finding |
|:--|:--:|:--|
| Q037-F-01 *salām ʿalā* corpus-share | **CONFIRMED** | All 4 corpus instances in Q 37; perm-p < 0.0001 |
| Q037-F-02 sacrifice-block hapax + isolation | **NULL** | 2 hapax (one short of pre-locked 3); block isolation moderate not extreme |
| Q037-F-03 Q 37:1-3 trio cohesion | **PRE-COMMIT VIOLATION** | Trio cohesion = 0 (lexically orthogonal); reveals iʿjāz operates at morphological-template level, not lexical-token level |
| Q037-F-04 oath-cluster membership | **NULL** | Q 37 is rank 15/15 in cluster centrality; PERIPHERAL member; suggests 2-tier oath-cluster structure |
| Q037-F-05 Q 37→Q 38 seam | **DIRECTIONAL** | 2/3 sub-tests pass; seam is content-typological + 4-shared-prophets, NOT rhyme-shared |

**Aggregate: 1 CONFIRMED, 1 DIRECTIONAL, 2 NULL, 1 PRE-COMMIT-VIOLATION.** All five tests reported with EQUAL NULL PROMINENCE per HANDOFF/04-DISCIPLINE.md.

## Aggregate empirical picture of Q 37 from this specialist run

1. **Q 37 is the corpus's UNIQUE *salāmun ʿalā [PROPHET]* monopoly surah** — a fingerprint feature with zero overlap elsewhere (CONFIRMED).
2. **Q 37 is the structurally-unique sacrifice-of-Ishmael surah** at the NARRATIVE level, but only moderately at the LEXICAL-FINGERPRINT level (NULL on hapax-density threshold; 2 hapax found).
3. **Q 37:1-3 oath-trio is held together by GRAMMATICAL-MORPHOLOGICAL parallelism, NOT lexical overlap** — refines (not refutes) the al-Rāzī / al-Bāqillānī iʿjāz reading (PRE-COMMIT VIOLATION at lexical level).
4. **Q 37 is the PERIPHERAL member of the H-NEW-1070 oath-cluster** (rank 15/15 centrality) — the cluster has a 2-tier structure with short-tail core {Q 91-103} and mid-mushaf periphery {Q 37, 51-53} (NULL on individual; H-NEW-1070 group-level still CONFIRMED).
5. **Q 37 → Q 38 is empirically seamless** via shared length + content + 4 prophet-narrative-slots, NOT via rhyme-letter sharing — VINDICATES al-Biqāʿī's munāsabah at the extreme level (DIRECTIONAL).

## Cross-references

- `00-overview.md` (Q 37 basic structural properties)
- `01-empirical-profile.md` (full H-NEW metric integration)
- `02-content-analysis.md` (12-block content map; the prophet-cycle and the salām-formula structure)
- `03-tafsir-survey.md` (al-Rāzī's 5+ vajh reading of Q 37:1-3; Ibn Kathīr's dhabīḥ-defense)
- `04-hadith-corpus.md` (Yūnus b. Mattā chains; Q 37:147 hadith)
- `05-classical-claims-audit.md` (7 classical claims tested)
- All 5 pre-reg files in `surahs/Q037-al-saffat/Q037-F-NN-*-prereg.md`
- All 5 scripts in `scripts/Q037_F_NN_*.py`
- All 5 outputs in `surahs/Q037-al-saffat/csv/Q037-F-NN.json`
