---
finding_id: h-new-940-prophet-order-conservation-prereg
phase: B
status: pre-registered
date: 2026-05-07
agent: prophet-cycle-order-specialist
hypothesis_family: cross-surah-prophet-order-conservation
seed: 20260507
n_perm: 10000
bonferroni_k: 4
bonferroni_family: H-NEW-940-H2-subaxes
alpha_bon: 0.0125
direction_locked: positive (mean Kendall-tau > 0)
classical_anchor: Ibn Kathīr *al-Bidāya wa-l-nihāya*; al-Suyūṭī *al-Itqān* nawʿ on prophets (the qiṣaṣ chronological-typological tradition)
rules_tuple: (no-tashkeel, QAC-PN-lemma, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# H-NEW-940 — Prophet-Cycle Order Conservation Across Narrative Surahs (PRE-REG)

## 0. SHA256-lock declaration

This pre-reg is locked at the SHA256 emitted by `sha256sum` of this file at commit-time. The run script `/Users/grey/Downloads/quran/scripts/h_new_940_prophet_order_conservation.py` embeds the SHA256 and verifies at runtime.

## 1. Question

Across the 8 surahs containing ≥5 named prophets — **Q 6, Q 7, Q 11, Q 19, Q 21, Q 26, Q 37, Q 38** — does the ORDER in which prophets are introduced (verse-position of first occurrence) correlate POSITIVELY across pairs (i.e., is there a CONSERVED canonical prophet-ordering)? Or is it random?

## 2. Classical claim being tested

**Ibn Kathīr** in *al-Bidāya wa-l-nihāya* (the chronological-historical narrative arc, Adam → Idrīs → Nūḥ → Hūd → Ṣāliḥ → Ibrāhīm → … → Muḥammad) argues that the Quranic prophet-orderings reflect a chronological-historical sequence. **Al-Suyūṭī** in *al-Itqān* (nawʿ 56 *al-ījāz wa-l-iṭnāb*, vol. 3 pp. 229-232, Shamela0011728 ed.) treats prophet-narratives as a typology with paired groupings (people-of-Nūḥ + Hūd + Ṣāliḥ as parallel destruction-pericopes). **Al-Qurṭubī** and **al-Ṭabarī** treat the Q 6:83-87 list as a canonical ordering reference. None has been quantified.

The hypothesis: if classical chronological/typological ordering is real, pairwise Kendall-tau on shared-prophet orderings across surahs will be SIGNIFICANTLY POSITIVE.

## 3. Hypotheses (DIRECTION-LOCKED)

### H1 (corpus-wide):
Mean Kendall-tau across all C(8,2) = 28 surah-pairs (computed on the SHARED-prophet subset of each pair) is significantly POSITIVE under permutation null at p < 0.01.

### H2 (Bonferroni-4 sub-axes, α_bon = 0.0125 each):
- **H2a**: When the chain Adam → Nūḥ → Hūd → Ṣāliḥ is partially or fully present in a surah, the prophets appear in this order (Kendall-tau on the present-subset > 0 under permutation null).
- **H2b**: When the parent-son chain Ibrāhīm → Ismāʿīl → Isḥāq is partially or fully present, it appears in this order.
- **H2c**: When both Mūsā and Hārūn are named, Mūsā precedes Hārūn (binomial test: observed-Mūsā-first proportion across qualifying surahs > 0.5; one-tailed).
- **H2d**: Q 21's prophet-list order vs Q 6:83-87's prophet-list order has Kendall-tau > 0.7 on shared prophets.

### H3 (typology, exploratory):
Construct a CONSENSUS prophet-order via the position-rank median ordering across the 8 surahs. Compute per-surah Kendall-tau to consensus. Test whether deviations correlate with chronological phase (Nöldeke Meccan-Middle / Late / Medinan).

## 4. Data sources

- **Morphology**: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4, PN-tagged proper-noun lemmas with verse-locations)
- **Text**: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (sanity-check)
- **Chronology**: `/Users/grey/Downloads/quran/data/revelation-order.csv` (Nöldeke phases, for H3)

## 5. Prophet → QAC LEM mapping (locked)

The 25 canonical named-prophets per al-Suyūṭī, *al-Itqān* discussion of prophets, mapped to QAC v0.4 PN-lemmas (verified by direct grep against morphology file):

| Prophet (translit) | QAC LEM | Notes |
|---|---|---|
| Ādam | `A^dam` | |
| Idrīs | `<idoriys` | |
| Nūḥ | `nuwH` | |
| Hūd | `huwd` | NOT `huwd2` (which = "Jews", al-yahūd plural) |
| Ṣāliḥ | `Sa\`liH2` | with backtick; `Sa\`liH` (no 2) is the adjective |
| Ibrāhīm | `<iboraAhiym` | |
| Lūṭ | `luwT` | |
| Ismāʿīl | `<isomaAEiyl` | |
| Isḥāq | `<isoHaAq` | |
| Yaʿqūb | `yaEoquwb` | |
| Yūsuf | `yuwsuf` | |
| Shuʿayb | `$uEayob` | |
| Mūsā | `muwsaY\`` | |
| Hārūn | `ha\`ruwn` | |
| Yūnus | `yuwnus` | |
| Dāwūd | `daAwud` | |
| Sulaymān | `sulayoma\`n` | |
| Ayyūb | `>ay~uwb` | |
| Ilyās | `<iloyaAs` | also covers Ilyāsīn (Q 37:130) — same lemma |
| al-Yasaʿ | `{loyasaEa` | |
| Dhū al-Kifl | (verse-anchor only: Q 21:85 word-3, Q 38:48 word-3) | not a single PN-lemma; uses noun `kifol` ROOT:kfl |
| Zakariyyā | `zakariy~aA` | |
| Yaḥyā | `yaHoyaY\`` | |
| ʿĪsā | `EiysaY` | |
| Muḥammad | `muHam~ad` | also `>aHomad` (Q 61:6) treated as same prophet |

**Dhū al-Kifl handling**: Hard-coded as PN at exactly two attestations Q 21:85 (word-position 3) and Q 38:48 (word-position 3), per QAC tokens `(21:85:4:2)` and `(38:48:5:2)` for the lemma `kifol` co-occurring with `dhā` (the "owner-of-the-cloak" formula). This is the SAME treatment given by classical lexicographers (al-Bayḍāwī, al-Rāzī).

## 6. Per-surah extraction procedure

For each of the 8 surahs Q ∈ {6, 7, 11, 19, 21, 26, 37, 38}:
1. Iterate QAC morphology file for all PN tokens whose LEM matches one of the 25 prophet lemmas (plus Dhū al-Kifl verse-anchors).
2. For each prophet in this surah, record `first_loc = (verse, word, segment)` of first occurrence (lexicographic minimum).
3. Sort prophets by `first_loc` to produce per-surah ORDER vector.

**Compound-name resolution** (e.g., Mūsā wa-Hārūn at Q 7:142): If two prophets are named in the same verse, ranking is by word-position within verse (Mūsā before Hārūn if Mūsā has the lower word-position).

## 7. Kendall-tau computation (pairwise)

For surah-pair (a, b):
1. shared = prophets named in BOTH a and b.
2. If |shared| < 2: skip the pair.
3. Compute Kendall's τ on the rank-vectors of shared prophets across a's order and b's order (concordant-discordant pair count, normalized by n(n-1)/2).
4. Aggregate: corpus-wide statistic = unweighted mean over the C(8,2) = 28 pairs (only pairs with |shared| ≥ 2 contribute).

## 8. Permutation null (10,000 perms, seed 20260507)

For each permutation:
- For each surah, randomly shuffle its prophet-order vector (uniform over the K_s! permutations of its K_s prophets).
- Recompute mean Kendall-tau across all 28 pairs.

p-value = fraction of perms with null mean-τ ≥ observed mean-τ (one-tailed, positive direction).

## 9. H2 sub-tests (Bonferroni-4)

### H2a (Adam → Nūḥ → Hūd → Ṣāliḥ chain):
For surahs containing ≥2 of these 4 prophets, compute Kendall-tau on the sub-list against the canonical ordering [Adam, Nūḥ, Hūd, Ṣāliḥ]. Aggregate to mean. Permutation null: shuffle sub-list ordering per qualifying surah. p < 0.0125 required.

### H2b (Ibrāhīm → Ismāʿīl → Isḥāq):
Same procedure on this 3-prophet chain.

### H2c (Mūsā → Hārūn binomial):
Across all surahs naming both, count surahs where Mūsā's `first_loc` < Hārūn's `first_loc`. Binomial test against p_null = 0.5, one-tailed (alternative: > 0.5). Bonferroni-corrected α = 0.0125.

### H2d (Q 21 vs Q 6:83-87):
Restrict Q 6's prophet-order to verses 83-87 only. Restrict Q 21 to its full prophet-list. Compute Kendall-tau on shared prophets. Threshold τ > 0.7 (point estimate); also report permutation p-value.

## 10. H3 (consensus + deviation typology)

1. Build consensus order: for each prophet appearing in ≥2 of the 8 surahs, compute mean rank across those surahs (rank = position in surah's order). Sort prophets by mean rank → consensus order.
2. For each surah, compute Kendall-tau between its order and consensus.
3. Group surahs by Nöldeke phase (per `data/revelation-order.csv`). Test whether late-Meccan surahs deviate Mūsā-direction (Mūsā is earlier in their order than in consensus) and early-Meccan deviate Nūḥ-direction.

This is exploratory; reports descriptive statistics + qualitative typology.

## 11. Acceptance / failure criteria

| Test | Acceptance | Failure |
|---|---|---|
| H1 | mean τ > 0 AND perm p < 0.01 | mean τ ≤ 0 OR perm p ≥ 0.01 |
| H2a | sub-mean τ > 0 AND perm p < 0.0125 | else |
| H2b | sub-mean τ > 0 AND perm p < 0.0125 | else |
| H2c | binomial p < 0.0125 (one-tailed) | else |
| H2d | observed τ > 0.7 AND perm p < 0.0125 | else |
| H3 | descriptive (no formal acceptance) | — |

Direction-locked: NEGATIVE mean-τ on H1 = pre-commit violation, published as NULL with full prominence.

## 12. Garden-of-forking-paths log (BEFORE run)

- **Choice of 8 surahs**: pre-registered as the 8 surahs containing ≥5 named prophets (per the task spec). Determined upstream by the convener; not a free parameter.
- **Choice of 25 prophets**: al-Suyūṭī's 25-named list (excludes ḥanīfan, ṣiddīqun honorifics; excludes ʿUzayr, Luqmān, Dhū al-Qarnayn whose prophethood is contested classically).
- **Compound-name tie-break**: word-position within verse. Alternative would be alphabetical, but classical sources (e.g., al-Suyūṭī on *Mūsā wa-Hārūn*) treat the listed-first prophet as the primary actor.
- **Hūd vs huwd2 disambiguation**: locked to LEM `huwd` (the prophet) only; LEM `huwd2` is the noun "Jews" and is excluded.
- **Dhū al-Kifl handling**: hard-coded verse-anchor (Q 21:85, Q 38:48), since QAC does not assign a single PN-lemma. Consistent with classical treatment.
- **Ilyāsīn at Q 37:130**: same lemma `<iloyaAs` as Ilyās; treated as one prophet.
- **Aḥmad at Q 61:6**: not in the 8-surah set. If it were, would be merged with Muḥammad. Q 61 not in analysis set.

## 13. Reproducibility

- Script: `/Users/grey/Downloads/quran/scripts/h_new_940_prophet_order_conservation.py`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-940.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-940-run-1.md`
- Seed: 20260507
- Stdlib only.
