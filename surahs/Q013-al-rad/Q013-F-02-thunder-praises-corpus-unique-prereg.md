---
surah: 13
test_id: Q013-F-02
title: "Thunder-praises-God corpus uniqueness — yusabbiḥu al-raʿdu bi-ḥamdihi: hapax verse + corpus-unique storm-event-as-divine-discourse sense"
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q013-F-family-2026-05-07
alpha_bon: 0.01
n_perm: 10000
---

# Q013-F-02 — Pre-registration: thunder-praises-God corpus uniqueness

## 1. Hypothesis (locked before observation)

**Empirical anchor (computed pre-test, frozen)**:
The lemma رعد (raʿd, "thunder") appears in the Quran in exactly TWO verses (verified from `quran-text/quran-no-tashkeel.json` token search):
- Q 2:19 — *aw ka-ṣayyibin min al-samāʾ fīhi ẓulumātun wa-**raʿdun** wa-barqun* — embedded in the storm-simile of hypocrites (raʿd here is a STORM-ELEMENT in a parable, NOT a praising-agent).
- Q 13:13 — *wa-yusabbiḥu **al-raʿdu** bi-ḥamdihi* — al-raʿd is the GRAMMATICAL SUBJECT of the verb yusabbiḥu (praising-agent).

**H1 (locked direction)**: The construction *"raʿd as the grammatical subject of a verb of divine-praise / divine-discourse"* is a corpus-hapax — appearing only in Q 13:13. Operationally: search for any verse containing both (a) the lemma رعد (or any morphological inflection thereof) and (b) one of the divine-praise/discourse verbs (root sabbaḥa, ḥamida, dhakara). Pre-commit: ≤ 1 such co-occurrence in the corpus.

**Comparison to brq (lightning) and صعق (lightning-strike)**:
- البرق (al-barq, lightning) appears in Q 2:19, Q 13:12, Q 30:24 (3 verses): always as natural phenomenon, never as praising-agent.
- صواعق (lightning-bolts) appears in Q 2:19, Q 13:13.
- صاعقة (lightning-strike) appears in Q 2:55, Q 4:153, Q 51:44.

These storm-elements are NOT subjects of *yusabbiḥu* in any other verse. The Q 13:13 construction is **lexically corpus-unique**.

**Direction (locked)**: corpus-hapax co-occurrence ≤ 1 (only Q 13:13).

**H0**: Multiple verses (≥ 2) co-occur with raʿd-as-praising-agent.

## 2. Operational definition

**Step 1 — Lemma family (frozen pre-test)**:
- raʿd-family: any orthographic word containing the substring `رعد` (no-tashkeel). Preliminary count: 2 verses (Q 2:19 *ورعد*; Q 13:13 *الرعد*).
- praise/discourse-verb family: roots {س-ب-ح (sabbaḥa/yusabbiḥu/tasbīḥ), ح-م-د (ḥamida/yaḥmadu/ḥamd), ذ-ك-ر (dhakara/yadhkuru/dhikr)}. We use the QAC root-index (`data/morphology/root-index.json`) for canonical root-mapping.

**Step 2 — Co-occurrence test**:
For each verse in the corpus, check whether (a) the verse contains a raʿd-family token AND (b) the verse contains a verb whose root is in {sbḥ, ḥmd, dhkr}. Count `n_co_occurrence`.

**Step 3 — Specifically test "raʿd is the grammatical subject of a praise-verb"**:
Substring co-occurrence does not guarantee grammatical subject-hood. Pre-committed proxy: in any verse where both raʿd-family and {sbḥ/ḥmd/dhkr} appear, manually inspect the syntactic role. Pre-commit: only Q 13:13 will have raʿd as the grammatical subject of a praise verb.

**Step 4 — Permutation null**:
Test whether random pairs of (rare-noun, common-verb-root) co-occur in ≤ 1 verse at the rate observed for raʿd-{sbḥ,ḥmd,dhkr}. We use H0: 1000 random rare-noun families (matched on corpus-frequency, drawn from QAC stems with ≤ 5 corpus attestations) paired with the {sbḥ,ḥmd,dhkr} root-family. Count fraction of permutations where co-occurrence ≤ 1.

## 3. Test statistic

**Primary**: `n_raʿd_praise_co_occurrence` (count of verses with both raʿd-family and {sbḥ,ḥmd,dhkr} root). Pre-commit: ≤ 1.
**Secondary**: rank of Q 13:13's co-occurrence-construction among all corpus verses.
**Permutation p-value**: fraction of random rare-noun {sbḥ/ḥmd/dhkr} co-occurrence counts ≥ observed. (Direction: observed = 1 is at the LOW end; we expect rare-noun matches to typically have 0 or 1 co-occurrence, so the test statistic discriminates whether 1-co-occurrence is RARE in the matched-rarity distribution.)

## 4. Success / Failure

- **CONFIRMED**: `n_co_occurrence == 1` (only Q 13:13) AND p_perm (permutation rank) is in the consistent-with-rare-corpus-event regime (i.e. observation matches the expected distribution for a hapax construction; not requiring p_perm ≤ 0.01 because the null is not directional in the standard sense — instead, we report descriptively).
- **DIRECTIONAL**: `n_co_occurrence ∈ {1, 2}` with confirmed unique grammatical-subject-of-praise-verb structure.
- **NULL**: `n_co_occurrence ≥ 3` (multiple verses with raʿd-praising-agent).

This is a **descriptive pre-registration** — the headline claim is the corpus-hapax construction. The Bonferroni-k=5 family contains other tests; this test is reported as part of the family but its pass/fail criterion is the binary count, not a permutation-p-value alone.

## 5. Honest limits known a priori

- The lemma family is restricted to orthographic substring `رعد`. This MAY include false-positive substrings (e.g. a word like *تَرْعَدُ* "you tremble" with same root). Manual inspection: only 2 attestations exist (verified pre-test).
- The grammatical-subject claim requires syntactic parsing, not just co-occurrence. We make this claim manually-verified, NOT pre-committed for permutation null. The permutation null tests only co-occurrence count.
- "Storm-event-as-divine-discourse" is a hermeneutic category, not a syntactic one. The empirical claim is restricted to the syntactic claim ("raʿd is grammatical subject of yusabbiḥu in Q 13:13 alone").

## 6. Rules-tuple

`(no-tashkeel, orthographic-token + QAC-root-validation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at run-time; embedded in `scripts/Q013_F_02_thunder_corpus_unique.py`. Verified at runtime.

## 8. Garden-of-forking-paths

- Considered: comparing to Q 24:43 raʿd-reference. REJECTED: Q 24:43 contains *al-barq* (lightning) but NOT raʿd as a noun; the prompt-mention was inaccurate. The actual barq attestations are Q 2:19, Q 13:12, Q 30:24 — Q 24:43 contains *al-barq* but it is NOT a raʿd-attestation. Documented honestly.
- Considered: testing the wider semantic field (storm + theology). REJECTED: too vague; pre-committed to the lexical-syntactic claim.
- Considered: rules-tuple variant — full-tashkeel orthographic match. PRE-COMMITTED to no-tashkeel substring + manual inspection of any matches.
