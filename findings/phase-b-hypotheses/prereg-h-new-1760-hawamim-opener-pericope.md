---
id: H-NEW-1760
title: Ḥawāmīm 7-surah opener-pericope (first 3 verses) root-Jaccard cohesion flip-test (H-NEW-1395 NULL → ?)
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1760-hawamim-opener-pericope (single pre-registered primary test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 7 ḥawāmīm opener-pericopes (each surah's verses 1-3) is GREATER than the mean of 10,000 length-matched random-3-verse-window draws from the flat 6,236-verse corpus index (one-tailed permutation null)
origin: H-NEW-1395 NULLed the 7-surah ḥawāmīm cluster {Q 40, 41, 42, 43, 44, 45, 46} at whole-surah Fisher-Rao root-distribution cohesion (Cell A uniform-7 p=0.2086, Cell B length-matched p=0.0514; MW-5 PC valid p_pc=0.0414). The honest interpretation embedded in H-NEW-1395 §5: "the ḥawāmīm share a SINGLE marker (حم — 2 letters in each surah's v.1)... single thematic/liturgical/orthographic markers are necessary-not-sufficient for FR-cohesion. HM-7 marker thickness ≈ 2 graphemes per surah vs ~1,000-9,000 graphemes per surah." Per cross-finding-025-formal (scale-of-aggregation pericope-flip law, 3/3 prior flips confirmed: H-NEW-1380 Iblīs, H-NEW-1510 sajda, H-NEW-1520 prophet-vocative), this pre-reg re-tests the same theological set at the OPENER-PERICOPE scale (each surah's first 3 verses = HM + initial themes-statement). The marker concentration in the opener-pericope is far higher than in the whole surah — 2/L of opener-pericope tokens are the HM glyph, with the next 2 verses being the surah's thematic preamble (al-Suyūṭī al-Itqān nawʿ 8 on tarjamat al-sūra). This pre-reg formally re-tests whether shifting from whole-surah to opener-pericope scale flips the NULL to a PASS.
verdict_ceiling: PASS-DIRECTED (single pre-registered direction; k=1)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1 (none of Q 40-46 carry independent basmala in test scope; immaterial)
  verse_numbering: hafs-kufan
  detection_rule: opener-pericope = first 3 verses of each ḥawāmīm surah (verses 1, 2, 3); for Q 42 this is HM + ʿSQ + content; for the other six surahs this is HM + 2 content verses (HM + tanzīl al-kitāb... in Q 40/41/45/46; HM + wal-kitāb al-mubīn... in Q 43/44)
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 7 length-3 windows from the flat 6,236-verse corpus index; for each of the 7 windows, draw start ~ Uniform[0, 6236 - 3]; take 3 consecutive verses; compute the window's root-set; mean pairwise Jaccard across 21 unordered pairs; wraparound disallowed
---

# H-NEW-1760 pre-registration — Ḥawāmīm 7-surah opener-pericope root-Jaccard cohesion flip-test

## Origin

**Prior 1 — H-NEW-1395 NULL (whole-surah scale)**: The 7 consecutive ḥawāmīm surahs {Q 40, 41, 42, 43, 44, 45, 46}, the corpus-EXACT HM-opener block, NULLed on whole-surah Fisher-Rao root-distribution cohesion. Cell A uniform-7 p=0.2086, Cell B length-matched p=0.0514 — both miss Bonferroni-corrected α=0.025. PC valid (p_pc=0.0414). H-NEW-1395 §5 explicitly identifies the cause: marker thickness is ~2 graphemes per surah, well below cross-finding-025's 10% threshold for whole-surah FR-cohesion detection.

**Prior 2 — cross-finding-025-formal (scale-of-aggregation pericope-flip law, 3/3 confirmed)**: Triple-flip empirical evidence has elevated the pericope-flip corollary to corpus-wide law strength:

| Marker class | Whole-surah NULL | Pericope-scale PASS | Flip effect-size |
|---|---|---|---|
| Iblīs-narrative | H-NEW-039 (z=+0.24) | H-NEW-1380 (z=+4.76) | +4.52 σ |
| Sajda 14-verse cluster | H-NEW-1330 | H-NEW-1510 (z=+2.685) | corroborating flip |
| yā-ayyuhā al-nabī | H-NEW-1360 | H-NEW-1520 (z=+6.41) | +6.41 σ — largest |

cross-finding-025-formal §1 explicitly queues the ḥawāmīm 7-surah opener-pericope re-test as one of four candidate flips to execute.

**Prior 3 — classical opener-as-tarjama tradition**: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 8 (*fī tarjamat al-sūra wa-ākhirihā*) and al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān* (chapter on *fawātiḥ al-suwar*) describe the opening verses of a surah as its *tarjama* (programmatic statement). For the ḥawāmīm specifically, Ibn Kathīr's tafsīr opening of Sūrat Ghāfir (Q 40) treats the *tanzīl al-kitāb min Allāh al-ʿAzīz* / *wal-kitāb al-mubīn* formulae as the shared "brocade thread" (*dībāj*) of the family. The opener-pericope is therefore the classically-attested scale at which the ḥawāmīm coherence-claim should hold.

## Hypothesis (single primary test)

**H1**: The 7 ḥawāmīm opener-pericopes — each defined as the first 3 verses of the surah (verses 1, 2, 3) — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random 3-verse windows drawn from the flat 6,236-verse corpus index.

**Test statistic**: mean of all C(7,2) = 21 pairwise root-Jaccard values among the 7 opener-pericope root-sets.

**Null distribution**: 10,000 random draws; for each of the 7 opener-pericopes (all length L=3), draw start ~ Uniform[0, 6236 - 3] from the flat verse-index; take the 3 consecutive verses; compute the window's root-set. Compute mean pairwise root-Jaccard across the 21 unordered pairs. The 7 lengths are all 3 by construction (no edge-clipping needed; all ḥawāmīm surahs have ≥35 verses).

**Decision rule**: PASS-DIRECTED if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single test (k=1); no Bonferroni adjustment.

## Opener-pericope inventory (locked, corpus-EXACT 7 ḥawāmīm surahs)

Verified at runtime against `quran-text/quran-no-tashkeel.json`. All 7 surahs have v1 == "حم" exactly.

| # | Surah | Verses | Opener-pericope (vv 1-3) | Note |
|:-:|:--|:-:|:--|:--|
| 1 | Q 40 al-Ghāfir | 85 | v1 = حم; v2 = tanzīl al-kitāb min Allāh al-ʿAzīz al-ʿAlīm; v3 = ghāfir al-dhanb wa-qābil al-tawb... | HM + 2 content verses |
| 2 | Q 41 Fuṣṣilat | 54 | v1 = حم; v2 = tanzīl min al-Raḥmān al-Raḥīm; v3 = kitāb fuṣṣilat āyātuhu qurʾānan ʿarabiyyan... | HM + 2 content verses |
| 3 | Q 42 al-Shūrā | 53 | v1 = حم; v2 = ʿsq; v3 = kadhālika yūḥī ilayka wa-ilā lladhīna min qablika Allāh al-ʿAzīz al-Ḥakīm | **HM + ʿSQ + 1 content verse — Q 42 carries the unique ʿSQ-only v2** |
| 4 | Q 43 al-Zukhruf | 89 | v1 = حم; v2 = wal-kitāb al-mubīn; v3 = innā jaʿalnāhu qurʾānan ʿarabiyyan laʿallakum taʿqilūn | HM + 2 content verses |
| 5 | Q 44 al-Dukhān | 59 | v1 = حم; v2 = wal-kitāb al-mubīn; v3 = innā anzalnāhu fī laylatin mubārakatin innā kunnā mundhirīn | HM + 2 content verses |
| 6 | Q 45 al-Jāthiya | 37 | v1 = حم; v2 = tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm; v3 = inna fī l-samāwāt wa-l-arḍ la-āyāt li-l-muʾminīn | HM + 2 content verses |
| 7 | Q 46 al-Aḥqāf | 35 | v1 = حم; v2 = tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm; v3 = mā khalaqnā l-samāwāt... | HM + 2 content verses |

Length-vector L = (3, 3, 3, 3, 3, 3, 3); sum = 21 verses across 7 opener-pericopes; pairwise comparisons = 21.

**Q 42 treatment (locked)**: Q 42 al-Shūrā uniquely carries a TWO-verse muqaṭṭaʿāt opening — v1 = حم, v2 = عسق. The pre-reg rule, per the parent task brief, is to **uniformly take vv 1-3 across all 7 surahs**. For Q 42 this means the opener-pericope is HM + ʿSQ + 1 content verse (kadhālika yūḥī ilayka). For the other 6 surahs, the opener-pericope is HM + 2 content verses. This is the most conservative choice (same verse-window applied uniformly) and is documented as a locked decision in the garden-of-forking-paths section below.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit violation = J_mean < null mean (strict reversal). Pre-commit violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in four reasons:

1. **Shared opener-formula at the lexical level**: Q 40, 41, 45, 46 all share the *tanzīl al-kitāb* / *tanzīl* root-cluster (n-z-l, k-t-b, ʿ-z-z, ʿ-l-m / ḥ-k-m, r-ḥ-m); Q 43, 44 share *wal-kitāb al-mubīn* (k-t-b, b-y-n) and *qurʾān ʿarabiyya* (q-r-ʾ, ʿ-r-b). Multiple shared content-roots across the 7 opener-pericopes are visible by inspection.
2. **cross-finding-025-formal pericope-flip law**: 3/3 prior NULL→PASS flips confirmed at z=+2.7, +4.76, +6.41. The ḥawāmīm case is structurally analogous (whole-surah NULL on a thin orthographic marker; opener-pericope = the marker's concentration zone).
3. **Classical opener-as-tarjama tradition**: al-Suyūṭī *al-Itqān* nawʿ 8 and Ibn Kathīr (Q 40 opening) explicitly identify the ḥawāmīm opener-formulae as the shared *dībāj* thread.
4. **Marker thickness in opener-pericope vs whole-surah**: per cross-finding-025 marker-thickness law, the marker (HM) is ~2/L tokens at opener-pericope scale (L ≈ 8-15 tokens) — a thickness of ~10-25%, well ABOVE the 10% threshold; whereas at whole-surah scale (~1,000-9,000 tokens) it is ~0.02-0.2% — far BELOW threshold.

## Operational definition

- **Opener-pericope** = the first 3 verses of each ḥawāmīm surah (verses 1, 2, 3 inclusive). All ḥawāmīm surahs have ≥35 verses so no edge-clipping is needed.
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present, taking the first ROOT-tagged feature per segment); a verse's roots = union of its segments' ROOT fields. Identical to H-NEW-1380 / H-NEW-1510 / H-NEW-1520 protocols.
- **Pairwise Jaccard**: J(i, j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J = 0.
- **Mean pairwise Jaccard**: mean over all C(7,2) = 21 unordered pairs.
- **Note on muqaṭṭaʿāt verses**: under QAC v0.4, v1 == حم and v2 == عسق do NOT carry a ROOT-tag (muqaṭṭaʿāt are tagged as INL = initial letters, not as derived roots). The opener-pericope's root-set therefore comes entirely from the content verses (v2 + v3 for 6 surahs; v3 alone for Q 42). This is a known consequence of the QAC tagging convention and is consistent with cross-finding-025's earlier muqaṭṭaʿāt-axis ⊥ content-axis observation. The test asks whether the CONTENT verses immediately following the HM marker are FR-tight — which is the substantive question.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via ROOT field (first ROOT-tag per segment) |
| Counting unit | unique-root set per opener-pericope |
| Basmala | counted only in Q 1 (none of Q 40-46 carry independent basmala in test scope; immaterial) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | OPENER-PERICOPE (first 3 verses) — distinguished from whole-surah scale used in H-NEW-1395 |
| Cluster size | 7 ḥawāmīm surahs (corpus-EXACT) |
| Window lengths | [3, 3, 3, 3, 3, 3, 3] — uniform L=3; no edge-clipping needed |
| Q 42 ʿSQ treatment | uniformly take vv 1-3 (Q 42 thus includes HM + ʿSQ + 1 content verse; other 6 surahs include HM + 2 content verses) |

## Permutation null protocol

1. Seed RNG = 20260509 (matches H-NEW-1395, H-NEW-1380, H-NEW-1510, H-NEW-1520 for cross-test seed-uniformity within Wave-H).
2. For each of 10,000 permutations:
   - For each window length L in [3, 3, 3, 3, 3, 3, 3]: sample `start ~ Uniform[0, 6236 - 3]` from the flat verse-index (sorted ascending by (surah, verse)); take the 3 consecutive verses; compute the window's root-set as the union of its 3 verses' ROOT fields.
   - Compute mean pairwise root-Jaccard across the 7 sampled root-sets (21 pairs).
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as H-NEW-1380 / H-NEW-1510 / H-NEW-1520).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL |
| J_mean < null mean (strict reversal) | PRE-COMMIT-VIOLATION → NULL with full prominence |
| J_mean ≈ null mean (within 0.5 std) | NULL |

## Cross-scale comparison embedded in output JSON

The output JSON will explicitly compare:

- **Whole-surah scale (H-NEW-1395 NULL)**: 7 ḥawāmīm surahs {Q 40-46}; observed d̄(HM-7) = 0.8672; Cell A uniform-7 p=0.2086; Cell B length-matched p=0.0514; PC valid p_pc=0.0414.
- **Opener-pericope scale (H-NEW-1760 this finding)**: 7 ḥawāmīm opener-pericopes (each vv 1-3); J_mean = ?; null mean = ?; z = ?; p_perm = ?.

A FLIP (whole-surah NULL → opener-pericope PASS) would be the **4th** supporting finding-pair for cross-finding-025-formal's pericope-flip law, on the corpus-EXACT ḥawāmīm orthographic family. A NON-FLIP (both NULL) is itself informative — it would suggest the ḥawāmīm opener-formulae are NOT sufficiently lexically converged at the root-Jaccard granularity, refining cross-finding-025's domain of applicability (it may apply to narrative / vocative / liturgical markers but not to orthographic-opener markers).

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 21-pair mean + length-matched perm null locked above. Identical instrument to H-NEW-1380 / H-NEW-1510 / H-NEW-1520.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: Not applicable for the single primary test; if PASS-DIRECTED, an alternate-window-size sensitivity arm (window=2: HM + 1 content; window=5: HM + 4 content) is queued as H-NEW-1760-sens.
- **MW-4 (over-fitting)**: No fitted parameter. Window size = 3 verses matches H-NEW-1520's default discourse-completion window and the classical *tarjama*-of-3-verses convention; not tuned on data.
- **MW-5 (replication)**: H-NEW-1395's MW-5 PC (H-NEW-1190 sub-sample) already established that the FR root-distribution instrument carries signal on a verified PC (p_pc=0.0414). For the pericope-scale instrument (root-Jaccard mean-pairwise), H-NEW-1380 / H-NEW-1510 / H-NEW-1520 are the prior PCs at large z-magnitudes (+4.76 / +2.685 / +6.41). A different-seed replication is queued as H-NEW-1760b if PASS.
- **MW-6 (instrument-control)**: H-NEW-1395 NULL on the same theological set at whole-surah scale acts as the scale-of-aggregation control — the null at one scale is itself the control against over-interpreting the PASS at another scale. The 3/3 prior pericope-flip pattern is itself the corpus-wide instrument-control envelope.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc. The prediction "ḥawāmīm opener-formulae cohere at opener-pericope scale" was already implied by H-NEW-1395 §5 ("the classical coherence-claim either (a) holds on axes other than QAC-root-distribution... testable") and explicitly queued in cross-finding-025-formal §1 bullet 3.

## Garden-of-forking-paths disclosure

- The 7 ḥawāmīm surahs are corpus-EXACT (locked; verified at runtime by checking v1 == "حم" across all 7).
- Window size = 3 verses is the default *tarjama*-window per al-Suyūṭī *al-Itqān* nawʿ 8 / al-Zarkashī *al-Burhān* on *fawātiḥ al-suwar*; also matches the discourse-completion window of H-NEW-1520 (3 verses). Alternatives (window=2 or 5) are queued as H-NEW-1760-sens if PASS.
- Q 42 ʿSQ treatment: uniformly include vv 1-3 across all 7 surahs (Q 42 thus carries HM + ʿSQ + 1 content verse). The alternative (extend Q 42 to vv 1-4 to get 2 content verses) is REJECTED because: (i) it breaks length-uniformity in the null model; (ii) it gives Q 42 a longer pericope than the other 6, biasing toward a larger root-set; (iii) cross-finding-025's earlier muqaṭṭaʿāt-axis ⊥ content-axis observation suggests the muqaṭṭaʿāt verse contributes no root-tagged content regardless. The uniform-vv-1-3 rule is the cleanest, most conservative choice.
- Seed = 20260509 deliberately matches H-NEW-1395 / H-NEW-1380 / H-NEW-1510 / H-NEW-1520 (within-session seed-uniformity). A different-seed replication is queued.
- Direction = TIGHTER (J_mean > null mean) is locked PRE-OBSERVATION based on the 4 priors enumerated above. The reverse direction (J_mean < null mean) is published as NULL with prominence per Protocol §1.8.

## Connection to existing findings

- **H-NEW-1395 NULL**: same theological set, whole-surah scale, FR root-distribution → NULL. This is the "control" for the scale-of-aggregation claim on this orthographic-opener cluster.
- **H-NEW-1380 PASS-DIRECTED-REPLICATION (z=+4.76)**: same instrument (root-Jaccard pericope-pairwise mean), same seed, different target set (Iblīs narrative). The first scale-of-aggregation flip on record.
- **H-NEW-1510 sajda PASS (z=+2.685)**: same instrument, different target set (sajda 15-verse cluster). The second flip.
- **H-NEW-1520 prophet-vocative PASS (z=+6.41)**: same instrument, different target set (yā-ayyuhā al-nabī 13-verse cluster). The third flip — and the largest effect size on record.
- **cross-finding-025-formal (corpus-wide law)**: this pre-reg's PASS would be the 4th supporting finding-pair, on a structurally different marker class (orthographic-opener vs narrative / liturgical / discourse).
- **H-NEW-570** (HM-7 at 20.90 percentile FR-cohesion, pre-Bonferroni): H-NEW-1395 demoted this to formal NULL; H-NEW-1760 may rescue the original moderate signal at a different aggregation scale.
- **Q040-F-02** (HM-cluster verification): provides the runtime check (v1 == حم across all 7 surahs).

## Anti-flip

The reverse direction (J_mean < null mean) = pre-commit violation → published as NULL with prominence. Even a clean NULL (J_mean ≈ null mean) is a substantive finding: it would mean the ḥawāmīm orthographic-opener family does NOT exhibit content-cohesion even at the opener-pericope scale, refining cross-finding-025's domain of applicability (the pericope-flip law may apply to thematic/liturgical/discourse markers but not to orthographic-opener markers per se). This refinement would itself update cross-finding-025-formal.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1760.py` as EXPECTED_SHA. Any mismatch = fail-fast.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
