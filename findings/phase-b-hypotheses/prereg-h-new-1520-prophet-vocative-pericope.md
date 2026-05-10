---
id: H-NEW-1520
title: yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test (H-NEW-1360 NULL → ?)
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-1520-prophet-vocative-pericope (single pre-registered test)
alpha_bon: 0.05
direction_of_effect: TIGHTER — mean pairwise root-Jaccard of the 13 yā-ayyuhā-al-nabī pericope-windows is GREATER than the mean of 10,000 length-matched random-pericope-window draws (one-tailed permutation null)
origin: H-NEW-1360 (whole-surah Fisher-Rao cohesion of the 6-surah set {Q 8, 9, 33, 60, 65, 66}) NULL'd at corpus baseline (obs intra-mean FR = 0.9532 vs null mean 0.9240; Cell A p = 0.5734, Cell B p = 0.5835; MW-5 PC valid). The yā-ayyuhā al-nabī vocative is a DISCOURSE marker whose content is the IMMEDIATE NEXT WORDS — the directive Allāh issues to the Prophet. H-NEW-1380 (Iblīs 7-pericope cohesion at z = +4.76) established scale-of-aggregation as a methodological axis under cross-finding-025: a whole-surah NULL does not entail a NULL at narrower aggregation scales. This pre-reg re-tests the prophet-vocative cluster at the pericope-window scale.
verdict_ceiling: PASS-DIRECTED (single pre-registered test; no replication arm in this finding's design — replication queued via H-NEW-1520b at a different seed if needed)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: pericope-window = the vocative verse + the next 2 verses (3-verse window) where the divine directive completes
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt
  null_model: 10,000 random draws of 13 length-3 pericope-windows from the flat verse-index (Q 1:1 .. Q 114:6); wraparound disallowed; window must not cross the last verse of the corpus
  vocative_regex: ياأيها\s+النبي OR يا\s*أيها\s*النبي over no-tashkeel text (single compact pattern: r"يا\s*أيها\s*النبي")
---

# H-NEW-1520 pre-registration — yā-ayyuhā al-nabī prophet-vocative pericope-scale flip test

## Origin

Two prior findings span the prophet-vocative discourse marker at different aggregation scales:

- **H-NEW-1360 (NULL, 2026-05-09)**: 6-surah set {Q 8, 9, 33, 60, 65, 66} carrying the 13 yā-ayyuhā al-nabī attestations is NOT FR-cohesive on whole-surah root-distribution. Cell A uniform p = 0.5734, Cell B length-matched p = 0.5835; MW-5 PC (H-NEW-1190 sub-sample {Q 69, 97, 101}) PASSED at p = 0.0445 — so the instrument is valid and the surah-scale NULL is substantive. The discussion under H-NEW-1360 explicitly characterizes yā-ayyuhā al-nabī as a DISCOURSE marker (direct second-person prophetic command), not a content marker — see MASTER-FINDINGS-LEDGER §10.44.7.
- **H-NEW-1380 (PASS-DIRECTED-REPLICATION, 2026-05-09, z = +4.76)**: 7 Iblīs-narrative pericopes drawn from the same 9-surah set that H-NEW-039 NULL'd at whole-surah scale exhibit corpus-extreme mean pairwise root-Jaccard at pericope scale. Formalized scale-of-aggregation as the second methodological axis under cross-finding-025.

This pre-reg applies the H-NEW-1380 principle to the H-NEW-1360 NULL. The substantive claim of H-NEW-1360's NULL-interpretation is that the discourse marker's "content" is not the surah but the IMMEDIATE NEXT WORDS — the directive issued to the Prophet. If that interpretation is correct, the 13 vocative-window pericopes should cohere on root-Jaccard ABOVE the corpus baseline at pericope scale.

## Hypothesis (single primary test)

**H1**: The 13 yā-ayyuhā al-nabī pericope-windows — each a 3-verse window (vocative-verse, vocative-verse+1, vocative-verse+2) — exhibit TIGHTER mean pairwise root-Jaccard similarity than length-matched random 3-verse-window draws from the corpus.

**13 vocative pericope-windows (LOCKED via regex over no-tashkeel corpus)**:

| # | Surah | Vocative verse | Window (3 verses) |
|:--|:--|:--|:--|
| 1 | Q 8 al-Anfāl | 64 | Q 8:64-66 |
| 2 | Q 8 al-Anfāl | 65 | Q 8:65-67 |
| 3 | Q 8 al-Anfāl | 70 | Q 8:70-72 |
| 4 | Q 9 al-Tawba | 73 | Q 9:73-75 |
| 5 | Q 33 al-Aḥzāb | 1 | Q 33:1-3 |
| 6 | Q 33 al-Aḥzāb | 28 | Q 33:28-30 |
| 7 | Q 33 al-Aḥzāb | 45 | Q 33:45-47 |
| 8 | Q 33 al-Aḥzāb | 50 | Q 33:50-52 |
| 9 | Q 33 al-Aḥzāb | 59 | Q 33:59-61 |
| 10 | Q 60 al-Mumtaḥina | 12 | Q 60:12-13 (truncated to in-surah only — Q 60 has 13 verses) |
| 11 | Q 65 al-Ṭalāq | 1 | Q 65:1-3 |
| 12 | Q 66 al-Taḥrīm | 1 | Q 66:1-3 |
| 13 | Q 66 al-Taḥrīm | 9 | Q 66:9-11 |

**Test statistic**: mean of all C(13,2) = 78 pairwise root-Jaccard values among the 13 pericope-window root-sets.

**Null distribution**: 10,000 random draws; for each of the 13 pericope-windows, draw 13 random length-3 windows from the flat verse-index (window must not cross the last verse of the corpus); compute each window's root-set; compute the mean pairwise root-Jaccard over the 78 unordered pairs. The 13 lengths are all 3 by construction.

**Decision rule**: PASS-DIRECTED if p_perm < 0.05 AND direction matches lock (J_mean > null mean). Single test (k = 1); no Bonferroni adjustment.

## Direction lock

Direction is LOCKED before computation: **J_mean > null mean (TIGHTER)**. Pre-commit violation = J_mean < null mean (strict reversal). Pre-commit violation = NULL with full prominence per Protocol §1.8.

The directional prior is grounded in three reasons:

1. The discourse marker introduces a direct divine directive whose verbal expression should reuse a small core of imperative + ethical/legal-injunction roots (q-w-l, a-m-r, ḥ-r-m, ḥ-l-l, ʿ-l-m, ḥ-k-m, n-s-ʾ, ṭ-l-q, j-h-d, q-t-l, etc.).
2. H-NEW-1380 established the scale-of-aggregation flip principle for one prior NULL pair; this pre-reg tests whether the same principle applies to a DIFFERENT pre-registered NULL (H-NEW-1360), which would replicate H-NEW-1380's scale-of-aggregation principle at H-NEW-level on an independent target set.
3. H-NEW-1360's own interpretive paragraph (MASTER-FINDINGS-LEDGER §10.44.7) predicted this — "the discourse marker's content is the IMMEDIATE NEXT WORDS" — and this pre-reg promotes that predicted claim into a falsifiable test.

## Operational definition

- **Pericope-window** = the 3 consecutive verses (vocative verse, vocative verse + 1, vocative verse + 2) within the same surah. The only edge case is Q 60:12 — Q 60 al-Mumtaḥina has 13 verses, so the 3-verse window from Q 60:12 would require Q 60:14 which does not exist. The pre-reg rule for this edge case is **prefer in-surah completion**: if the 3-verse window would extend past the end of the surah, the window is truncated to just the in-surah verses (i.e. the window length L is min(3, verse_count - vocative_verse + 1)). For Q 60:12, this yields a 2-verse window (Q 60:12-13). The null model uses the SAME length per pericope-window — so the null draw for index 10 is a 2-verse window, not a 3-verse window. This keeps the null length-matched.
- **Root extraction**: `data/morphology/quranic-corpus-morphology-0.4.txt` v0.4; ROOT field of each morphological segment (one ROOT per segment when present); a verse's roots = union of its segments' ROOT fields. Identical to H-NEW-1380's protocol.
- **Pairwise Jaccard**: J(i, j) = |R_i ∩ R_j| / |R_i ∪ R_j|. If both sets empty, J = 0.
- **Mean pairwise Jaccard**: mean over all 78 unordered pairs.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel |
| Token level | QAC v0.4 root-tokens via stem-root field |
| Counting unit | unique-root set per pericope-window |
| Basmala | counted only in Q 1 (Q 1 not in test set; immaterial) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | PERICOPE-WINDOW (3 verses; truncated to in-surah only if vocative is among the last 2 verses) — distinguished from whole-surah scale used in H-NEW-1360 |
| Vocative regex | `r"يا\s*أيها\s*النبي"` over `quran-text/quran-no-tashkeel.json` |
| Cluster size | 13 attestations across 6 surahs |
| Window lengths | [3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3] — the 10th window is length 2 because Q 60:12 is the second-to-last verse of Q 60 (Q 60 has 13 verses) and the 3-verse window would extend past the end of the surah |

## Permutation null protocol

1. Seed RNG = 20260509 (matches H-NEW-1360 and Q038-F-07 / H-NEW-1380 — for cross-test seed-uniformity within the same session; a different-seed run is queued as H-NEW-1520b if PASS).
2. For each of 10,000 permutations:
   - For each window length L in [3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3]: sample `start ~ Uniform[0, 6236 - L]` from the flat verse-index; take the L consecutive verses; compute their root-set.
   - Compute mean pairwise root-Jaccard across the 13 sampled root-sets (78 pairs).
3. p_perm = (count of perm-J ≥ observed-J) / 10,000 (strict one-tailed; same convention as H-NEW-1380).

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| p_perm < 0.05 AND J_mean > null mean | PASS-DIRECTED |
| p_perm ≥ 0.05 AND J_mean > null mean | DIRECTIONAL |
| J_mean < null mean (strict reversal) | PRE-COMMIT-VIOLATION → NULL with full prominence |
| J_mean ≈ null mean (within 0.5 std) | NULL |

## Cross-scale comparison embedded in output JSON

The output JSON will explicitly compare:

- **Whole-surah scale (H-NEW-1360 NULL)**: 6-surah set {Q 8, 9, 33, 60, 65, 66}; intra-mean FR = 0.9532; Cell A p = 0.5734; Cell B p = 0.5835.
- **Pericope-window scale (H-NEW-1520 this finding)**: 13 vocative pericope-windows; J_mean = ?; null mean = ?; z = ?; p_perm = ?.

A FLIP (whole-surah NULL → pericope-window PASS) replicates H-NEW-1380's scale-of-aggregation principle on an independent target set; a NON-FLIP (both NULL) is itself informative — would suggest the discourse-marker prediction is false or the prophet-vocative directives are too lexically heterogeneous (legal/military/marital/eschatological) to cohere even at the directive-window scale.

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: Root-Jaccard + 78-pair mean + length-matched perm null locked above. Identical instrument to H-NEW-1380.
- **MW-2 (corpus-prior)**: 10,000 perms; minimum standard met.
- **MW-3 (alternative-models)**: Not applicable for the single primary test; if PASS-DIRECTED, an alternate-window-size sensitivity arm (window=2, window=5) is queued as H-NEW-1520-sens.
- **MW-4 (over-fitting)**: No fitted parameter. Window size = 3 verses is the default discourse-completion window (see operational definition); not tuned on data.
- **MW-5 (replication)**: H-NEW-1360's MW-5 PC (H-NEW-1190 sub-sample) already established that the FR root-distribution instrument carries signal on a verified PC. For this pre-reg, the PC is implicit (H-NEW-1380 itself is the prior PC at pericope scale on Iblīs); a different-seed replication is queued as H-NEW-1520b.
- **MW-6 (instrument-control)**: H-NEW-1360 NULL on the same theological set at whole-surah scale acts as the scale-of-aggregation control — the null at one scale is itself the control against over-interpreting the PASS at another scale.
- **MW-7 (post-hoc cap)**: Single pre-registered direction; not post-hoc. The prediction "vocative is a discourse marker, content is the immediate next words" was already in print at MASTER-FINDINGS-LEDGER §10.44.7 BEFORE this pre-reg was written.

## Garden-of-forking-paths disclosure

- The 13 vocative attestations are LOCKED via regex `r"يا\s*أيها\s*النبي"` over no-tashkeel corpus. The regex is taken from H-NEW-1360 pre-reg verbatim. Cluster reverification at runtime: the script must find exactly 13 hits across the 6 locked surahs, or it aborts.
- Window size = 3 verses is the default discourse-completion window; documented above. Alternatives (window = 2 or 5) are queued as H-NEW-1520-sens if PASS.
- Edge-case rule (Q 60:12 near end of surah) is locked: prefer in-surah truncation, do NOT spill into the following surah. This is the conservative choice — it shortens window 10 to 2 verses (Q 60:12-13), and the null model matches this length.
- Seed = 20260509 deliberately matches H-NEW-1360 and H-NEW-1380 (within-session consistency). A different-seed replication is queued.

## Connection to existing findings

- **H-NEW-1360 NULL**: same theological set, whole-surah scale, FR root-distribution → NULL. This is the "control" for the scale-of-aggregation claim on this discourse marker.
- **H-NEW-1380 PASS-DIRECTED-REPLICATION**: same instrument (root-Jaccard pericope-pairwise mean), same seed, different target set (Iblīs). This pre-reg replicates H-NEW-1380's scale-of-aggregation principle on an INDEPENDENT theological set.
- **cross-finding-025 (PRELIMINARY-SYNTHESIS)**: marker-thickness threshold rule. H-NEW-1380 added scale-of-aggregation as the second methodological axis. This pre-reg, if PASS, supplies the second supporting finding-pair for the scale-of-aggregation principle (the threshold for codification at cross-finding-025-formal is 2+ supporting pairs per MASTER-FINDINGS-LEDGER §10.51.4).
- **H-NEW-1260** (yā-ayyuhā alladhīna āmanū sister-construction, CONFIRMED) and **H-NEW-1310** (Christ-narrative NULL), **H-NEW-1330** (sajda NULL), **H-NEW-1340** (al-ḥamdu NULL) — the broader cross-finding-025 set within which this test sits.

## Anti-flip

The reverse direction (J_mean < null mean) = pre-commit violation → published as NULL with prominence. Even a clean NULL (J_mean ≈ null mean) is a substantive finding: it would mean the prophet-vocative directives are too heterogeneous (military / marital / legal / eschatological) to cohere even at directive-window scale, which would in turn refine the scale-of-aggregation principle (it does not apply universally; it is itself thematic-set-dependent).

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1520.py` as EXPECTED_SHA. Any mismatch = fail-fast.
