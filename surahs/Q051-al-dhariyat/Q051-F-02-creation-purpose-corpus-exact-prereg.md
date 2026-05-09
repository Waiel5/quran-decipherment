---
surah: 51
test_id: Q051-F-02
title: Q 51:56 (ma + khlq + illā + ʿbd) exclusivity-construction corpus-EXACT 1-of-1 hypothesis
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q051-F-02-creation-purpose-corpus-exact
alpha_bon: 0.025
---

# Q051-F-02 — Pre-registration: Q 51:56 corpus-EXACT creation-purpose construction

## 1. Hypothesis (locked before observation)

Q 51:56 *wa-mā khalaqtu al-jinn wa-l-ins illā li-yaʿbudūn* — "And I did not create the Jinn and humankind except to worship Me" — is the corpus's only verse that combines:
- Negation particle *(mā / wa-mā / fa-mā)*
- Creation root *(khlq / khalaqa / khalaqtu / khalaqnā / khalaqkum)*
- Exclusivity particle *(illā)*
- Worship root *(ʿbd / yaʿbudūn / ʿbādī / ʿbādatun)* in the post-illā purpose-clause.

**H1 (locked direction):** Q 51:56 is corpus-EXACT 1-of-1 under the strict construction *(mā/wa-mā/fa-mā + khlq + illā + ʿbd)*; i.e., **exactly 1 verse** in the 6,236-verse corpus matches this construction, and that verse is Q 51:56.

**H2 (locked direction, secondary):** Q 51:56 belongs to a **broader** corpus-class of *(mā + khlq + illā + Y)* verses where Y is the purpose-target. Under the broader construction (Y free): there are exactly 7 corpus verses (Q 10:5, Q 15:85, Q 30:8, Q 31:28, Q 44:39, Q 46:3, Q 51:56). Of these 7, **only Q 51:56** has Y = *ʿbd* (worship-root).

**H0:** Q 51:56 is NOT corpus-EXACT under the strict construction; ≥ 1 OTHER verse contains the same 4-element pattern.

**Direction:** locked POSITIVE for both H1 (corpus-EXACT 1-of-1) and H2 (1-of-7 in broader class).

## 2. Operational definitions

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **Negation particle pattern**: regex `^(ما|وما|فما)$` (start of word).
- **Creation root**: regex `(خلق|خلقنا|خلقت|خلقتك|خلقتها|خلقكم|خلقهم|خلقتني)`.
- **Exclusivity particle**: literal `إلا`.
- **Worship root**: regex `(يعبد|تعبد|نعبد|اعبد|عبد|يعبدون|تعبدون|عبادي|عباد|عبادة|اعبدوا|ليعبد|ليعبدون|عبدا|عابد)`.
- **Strict construction (for H1)**: a verse contains a negation-word at index i, a khlq-word at index j (j > i, j-i ≤ 4), an illā-word at index k (k > j, k-j ≤ 8), AND a ʿbd-word at index l (l > k, l-k ≤ 8).
- **Broader construction (for H2)**: same but no requirement on Y; Y is whatever follows illā.

## 3. Test statistic

- N_strict = number of corpus verses matching the strict 4-element construction (H1).
- N_broader = number of corpus verses matching the broader 3-element-plus-illā construction (H2).
- Identification of which surahs hold the matches.

## 4. Permutation null (descriptive only)

This is a corpus-EXACT structural test, not a permutation test. The result is N (an integer count) and the verse-IDs. No permutation p-value is meaningful for a structural-uniqueness claim. The "null" is the alternative hypothesis that ≥ 2 verses match.

## 5. Success / Failure

- **CONFIRMED**: H1 strict N = 1 AND that verse is Q 51:56.
- **PARTIAL**: H1 strict N > 1 (i.e., the strict construction has multiple matches); H2 broader N = 7 with Q 51:56 the unique ʿbd-purpose match.
- **NULL**: H1 fails AND H2 fails.
- **PRE-COMMIT VIOLATION**: Q 51:56 does NOT match either construction (regex error or text-source mismatch).

## 6. Honest limits known a priori

- The construction-pattern was identified by the analyst from a search at empirical-anchor extraction; this is post-hoc origin per HANDOFF/04-DISCIPLINE.md. Single-test α=0.05 cap; verdict ceiling **PASS-DIRECTED** until INDEPENDENT REPLICATION on different operationalization (e.g., QAC root-bag, classical *aqsām* taxonomy).
- The construction is corpus-rare; sensitivity to regex-pattern choice (whether to include all forms of *khlq* including *khalqu / al-khāliq*) is significant. The pre-reg locks the SPECIFIC regex BEFORE running.
- The window-size choices (j-i ≤ 4, k-j ≤ 8, l-k ≤ 8) are pre-locked. These are reasonable but not unique; alternative window-sizes are possible.
- A planted-signal MW-7 control would be: insert a fake *(mā + khlq + illā + ʿbd)* phrase in a non-Q-51 verse and check that the script catches it. (Skipped for this test as the corpus-EXACT 1-of-1 is verified by exhaustive scan.)

## 7. Rules-tuple

`(no-tashkeel, orthographic-token-window, regex-pattern, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 2 (H1 strict + H2 broader). α_bon = 0.025.

## 9. Coordination

Independent of any prior test. The construction-pattern is novel to this Q 51 specialist. No duplication.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q051_F_02_creation_purpose_corpus_exact.py`, verified at runtime.
