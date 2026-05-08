---
surah: 30
test_id: Q030-F-02
title: Q 30:2-5 Roman-Persian-war prophecy verse lexical uniqueness (hapax count)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perms: not-applicable (deterministic lemma-membership)
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (post-hoc single-test cap; replication queue: H-NEW-1XXX prospective)
hypothesis_anchor: al-Bāqillānī, *Iʿjāz al-Qurʾān* — Q 30:2-5 as iʿjāz al-ghayb
---

# Q030-F-02 — Pre-registration: Roman-Persian war prophecy verse lexical uniqueness

## 1. Hypothesis (LOCKED before observation)

**H1:** The Q 30:2-5 prophecy pericope contains **at least 3 corpus-hapax-or-near-hapax lemmas** (where "near-hapax" = lemma attested in ≤ 2 surahs in QAC v0.4 lemma-set).

The candidate-set is frozen: `{r~uwm, biDoE, siniyn, galab, gulibat-passive-form-as-distinct-lemma, dunyā/adnaY-comparative}`. The test is a **lemma-membership count**, not a permutation test.

**H0:** Fewer than 3 of the 6 candidate lemmas are corpus-hapax or near-hapax.

**Direction:** ≥3 hapax-or-near-hapax in Q 30:2-5 (LOCKED).

## 2. Operational definition

For each candidate lemma:
- Count its total QAC v0.4 attestations corpus-wide.
- Count distinct surahs in which it appears.
- Classify:
  - **strict-hapax**: 1 attestation only.
  - **lemma-corpus-hapax**: confined to a single surah (any number of tokens).
  - **near-hapax**: confined to ≤ 2 surahs.
  - **non-hapax**: ≥ 3 surahs.

**Test statistic**: count of lemmas in the 6-candidate set classified as `near-hapax` or stricter.

## 3. Comparison anchor (Q 27:14)

For comparative interpretation only (not part of the test), report the same hapax-count for Q 27:14 (*wa-jaḥadū bi-hā wa-staiqanat-hā anfusuhum ẓulman wa-ʿuluwwan; fa-nẓur kayfa kāna ʿāqibatu al-mufsidīn*) — another classical "historical-claim" verse — to contextualize Q 30:2-5's hapax density.

## 4. Bonferroni and α

k=1 (single direct count). α_bon = α_single = 0.05. The "test" is a deterministic count against a pre-registered threshold; no permutation is applied.

## 5. Success / Failure

| Outcome | Verdict |
|:--|:--|
| ≥ 3 hapax-or-near-hapax in 6-candidate set | **PASS-DIRECTED** (single-test cap: classical iʿjāz al-ghayb claim has lexical correlate) |
| 2 hapax-or-near-hapax | **DIRECTIONAL** (partial) |
| ≤ 1 hapax | **NULL** |

## 6. Rules-tuple

`(QAC v0.4, LEM tags, hafs-kufan, no-tashkeel)`.

## 7. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q030_F_02_rum_prophecy_hapax.py`.

## 8. Honest a-priori limits

- Lemma-tagging in QAC is the gold-standard but not error-free; specific edge cases (e.g., is `gulibat` a distinct lemma from `galaba`?) carry annotation-dependent uncertainty.
- The 6-lemma candidate set is curated from the Q 30:2-5 surface form (see verse text). Curated-from-the-target-text is a known confound; the corpus-hapax status of these lemmas is the empirically interesting question, not the curation.
- Q 30:2-5 is short (only 4 verses, ~40 words). A high hapax-rate is partly expected from any narrowly-scoped poetic/narrative verse-set.
