---
finding_id: Q005-F-03
prereg_date: 2026-05-07
prereg_type: per-verse semantic-cluster density rank
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q005 deep-dive (F-01..F-05)
alpha_bon: 0.01
rules_tuple: "(no-tashkeel, QAC-LEMMA + QAC-ROOT tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi)"
---

# Q005-F-03 — Q 5:3 completion-of-religion cluster density

## 1. Background

Q 5:3 contains the famous `al-yawma akmaltu lakum dīnakum wa-atmamtu ʿalaykum niʿmatī wa-raḍītu lakumu l-islāma dīnan` — the "completion of religion" declaration. al-Bukhārī (#45) records ʿUmar ibn al-Khaṭṭāb identifying this verse as revealed at ʿArafāt (the Day of Hajj), Friday. al-Suyūṭī (*al-Itqān*, nawʿ 8) discusses competing claims for the LAST-revealed verse and notes the Q 5:3 position (cited via Sufyān b. ʿUyayna). al-Tirmidhī #3043 also reports the ʿArafāt context.

Empirical question: does Q 5:3 contain the corpus-DENSEST cluster of {dīn, niʿmah, akmaltu/k-m-l, atmamtu/t-m-m, raḍītu/r-ḍ-w} within a single verse?

## 2. Frozen 5-cluster (lemma + root)

| Concept | QAC marker |
|:--|:--|
| dīn | LEMMA `diyn` |
| niʿmah | LEMMA `niEomap` (also accept ROOT `nEm` for `niEomap`/`>anoEama` family) |
| akmaltu / completion | ROOT `kml` |
| atmamtu / fulfillment | ROOT `tmm` |
| raḍītu / acceptance | ROOT `rDw` |

(Cluster is intentionally scoped to the specific Q 5:3 phrase — these are the EXACT words of that declaration. Other near-synonyms are excluded.)

## 3. Hypothesis (DIRECTION-LOCKED)

**H1 (primary)**: Q 5:3 has the corpus-RANK-1 verse-level density of the 5-cluster (count of cluster-tokens in verse / number of words in verse), where cluster requires ≥ 3 distinct cluster-members in the verse to qualify.

**H1' (auxiliary)**: Q 5:3 has the corpus-RANK-1 *raw count* of distinct 5-cluster members co-attested in a single verse (i.e., 5 of 5).

## 4. Null

**H0**: Q 5:3 ranks below position 1 in the verse-density measure.

## 5. Method

1. For each verse (s, v) in the corpus, count tokens of {LEMMA `diyn`, LEMMA `niEomap`, ROOT `kml`, ROOT `tmm`, ROOT `rDw`} via QAC v0.4.
2. For each verse, compute (a) the count of *distinct* cluster-members present (0..5) and (b) the verse's word count.
3. Density(verse) = total cluster tokens / verse-word-count, conditional on distinct-member-count ≥ 3.
4. Rank verses across the corpus.
5. Permutation null: shuffle the 5-cluster tokens across all verses (preserving each verse's word count), recompute Q 5:3's rank, repeat 10000× under seed 20260507. p_perm = fraction of permutations where the verse occupying Q 5:3's position attains rank ≤ 1.

## 6. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| Q 5:3 rank-1 in density AND p_perm < α_bon = 0.01 | VINDICATED Q 5:3 = corpus-densest completion-cluster |
| Q 5:3 rank-1 but p_perm ≥ α_bon | DIRECTIONAL |
| Q 5:3 rank ≥ 2 | NULL |

## 7. Garden-of-forking-paths log

- The 5-cluster {dīn, niʿmah, k-m-l, t-m-m, r-ḍ-w} is the EXACT phrase-vocabulary of Q 5:3 — frozen before running. NO substitution-of-near-synonyms is permitted post-hoc.
- The "≥ 3 distinct members" gate is a methodological pre-commit to avoid trivial maxima from short verses with a single high-frequency lemma. This is a tight gate.
- Rank-1 is a HIGH bar. NULL is the more probable verdict; we accept that.

## 8. Pre-commit locked.
