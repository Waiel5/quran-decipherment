---
id: H-NEW-65
title: Fātiḥa-as-DNA — does Sūrat al-Fātiḥa microcosmically encode the Quran's structural features across 6 axes?
phase: B
status: PRE-REGISTERED 2026-04-15 (locked BEFORE running script)
agent: h-new-65-specialist
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Wave-H-NEW-65-Fatiha-DNA
bonferroni_k: 6
alpha_bon: 0.00833  # 0.05 / 6
rules_tuple: (no-tashkeel; word-segment substring + first-letter-of-token first-letter rule; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
seed: 20260416
---

# [[h-new-65-fatiha-as-dna|H-NEW-65]] — Fātiḥa-as-DNA: comprehensive 6-axis microcosm test

## Question

Sūrat al-Fātiḥa (Q 1, 7 verses) is classically called **Umm al-Kitāb** ("the Mother of the Book") and is asserted to be a **microcosm** of the Quran — a kernel encoding the rest of the corpus' structural features. H-NEW-59 already tested a **single specific** instantiation (divine-name encoding) and **REFUTED** it at α=0.05. [[h-new-65-fatiha-as-dna|H-NEW-65]] broadens the test across **6 independent axes** to give the classical claim its fairest possible empirical hearing.

A weak microcosm claim only requires Fātiḥa to be representative on at least some axes. A strong microcosm claim requires Fātiḥa to be statistically distinctive (extreme in the "encoding" direction) on multiple axes simultaneously, beyond what a random 7-verse window from the corpus would achieve.

## Garden-of-forking-paths disclosure

Pre-existing knowledge before locking the spec:

- The Fātiḥa contains 4 of 99 al-asmāʾ al-ḥusnā (Allāh, al-Raḥmān, al-Raḥīm, al-Malik via mālik) — H-NEW-59 already showed F=3 distinct names by strict substring rule, p_geq=0.150 → REFUTED.
- The Fātiḥa rhymes overwhelmingly in -m / -īn (raḥīm/al-ʿālamīn/raḥīm/al-dīn/nastaʿīn/al-mustaqīm/al-ḍāllīn). The dominant Quran rhyme classes are nasal (-m, -n) and feminine plural (-āt) — so Fātiḥa's rhyme is plausibly representative.
- Fātiḥa includes a supplication ("ihdinā al-ṣirāṭa al-mustaqīm") which is exegetically said to be the kernel of the prayer relationship.
- Fātiḥa's first-letter-of-each-verse sequence: ب,ا,ا,م,ا,ا,ص (bāʾ, alif, alif, mīm, alif, alif, ṣād) — heavy on alif, no pharyngeal/glottal beyond alif; only ب, م, ص are non-alif.
- Compression intuition: a well-encoded microcosm should compress the rest of the Quran efficiently (high cross-compression ratio); against this, a 36-word text cannot reasonably "encode" 78,000+ words of Arabic.

The pre-existing H-NEW-59 cell-3 result is independently a refutation of axis 1 (lexical-as-divine-names). [[h-new-65-fatiha-as-dna|H-NEW-65]] axis 1 (LEXICAL) is a BROADER lexical question (any lemma, not just divine names) and is therefore an INDEPENDENT test — but the convergence of results across the two narrower-vs-broader formulations is a methodologically important piece of context.

Honest protection: the 6 axes are locked BEFORE running the script; null distributions and pass criteria are pre-committed below. M-9 (convergence-does-not-multiply): this is the SECOND such Fātiḥa-encoding test the project has run; effective independent N for the broader Fātiḥa-as-microcosm hypothesis is bounded above by 2 even if all 6 axes pass.

## Locked methodology

### Data
- Corpus: `quran-text/quran-no-tashkeel.json`, 114 surahs, 6236 verses.
- Fātiḥa = Q 1:1-7 (7 verses, including the basmala as Q 1:1).
- Each axis computes (a) Fātiḥa's value, (b) a null distribution from random 7-verse windows or single verses (per axis specification), (c) a one-sided or two-sided p-value with pre-committed direction.

### Random-7-verse-window null

Two complementary null distributions are used per axis:
- **Sliding-window null (deterministic):** all 6230 contiguous 7-verse windows of the corpus.
- **Random-7-verse-sample null:** for axes where contiguity is irrelevant or where a sample of 100,000 random non-contiguous 7-verse subsets is more appropriate, we sample without replacement under seed 20260416.

The chosen null per axis is locked below.

### Bonferroni
k = 6, α_bon = 0.05 / 6 ≈ 0.00833.

### Pre-committed PASS criterion (overall hypothesis)
The Fātiḥa-as-DNA hypothesis is PASS only if **at least 2 of 6 axes** are Bonferroni-significant in the "Fātiḥa is distinctive in the encoding direction" direction. 1 axis = REFUTED-WEAK. 0 axes = REFUTED-STRONG.

### Seed
20260416 (one day after H-NEW-59's seed 20260415, as instructed).

## The 6 locked axes

### Axis 1 — LEXICAL (general lemma representativeness)

**Question:** Are the words appearing in Fātiḥa drawn preferentially from the Quran's high-frequency lexical pool?

**Test statistic:** mean log-token-frequency of distinct word-types appearing in Fātiḥa, computed against the corpus-wide token frequency table. Fātiḥa-encoding direction predicts UNUSUALLY HIGH mean log-frequency (Fātiḥa over-uses common words, microcosm-of-vocabulary).

**Null model:** sliding-window null over all 6230 contiguous 7-verse windows; for each window, compute the same mean log-token-frequency of its distinct word-types.

**Direction:** one-sided UPPER (Fātiḥa expected to over-use common words).

**PASS:** Fātiḥa's percentile ≥ (1 − α_bon) = 0.99167 of the null distribution.

### Axis 2 — SEMANTIC (theme keyword representativeness)

**Question:** Are Fātiḥa's themes (praise, mercy, judgment, guidance, supplication) representative of corpus-wide thematic distribution?

**Test statistic:** for a locked list of 5 theme keyword-sets (locked BEFORE running):
- Praise: حمد, سبح, مجد, تبرك, تبارك
- Mercy: رحم, رحمن, رحيم, غفر, غفور
- Judgment: دين, حكم, يوم الدين, جزاء, ميزان
- Guidance: هدى, هدي, اهد, صراط, مستقيم
- Supplication: دعا, دعو, ادع, اللهم, نعب

Compute the **count of theme-classes (out of 5) for which the Fātiḥa contains at least one keyword**. Fātiḥa-encoding direction predicts the count to be UNUSUALLY HIGH.

Note: deliberate choice to count THEME-CLASSES not raw tokens, to give a maximally clean encoding signal (Fātiḥa actually does cover all 5 themes by inspection — question is whether 5/5 in 7 verses is statistically distinctive).

**Null model:** for each 7-verse window in the sliding-window null, compute the same count.

**Direction:** one-sided UPPER.

**PASS:** Fātiḥa's percentile ≥ 0.99167.

### Axis 3 — PHONETIC (rhyme pattern representativeness)

**Question:** Is Fātiḥa's rhyme pattern (the verse-final 1-letter cluster) representative of Quran-wide rhyme distribution?

**Test statistic:** for each of Fātiḥa's 7 verses, extract the final letter of the verse (after stripping non-alphabetic chars). Compute the multiset {final_letters}. The corpus-wide rhyme distribution (over all 6236 verse-final letters) gives a probability vector p over the 28 letters. Compute the log-likelihood of Fātiḥa's 7 verse-final letters under p:

  LL_fatiha = Σ_v log(p[final_letter(v)])

Fātiḥa-encoding direction predicts Fātiḥa's verse-final letters to be DRAWN FROM HIGH-FREQUENCY RHYME LETTERS, i.e., LL_fatiha unusually HIGH.

**Null model:** for each 7-verse window in the sliding-window null, compute the same LL.

**Direction:** one-sided UPPER (Fātiḥa expected to use common rhyme letters).

**PASS:** Fātiḥa's percentile ≥ 0.99167.

### Axis 4 — STRUCTURAL (verse-length distribution representativeness)

**Question:** Is Fātiḥa's 7-verse word-count profile representative of the corpus' typical 7-verse window word-count profile?

**Test statistic:** for Fātiḥa, compute the 7-tuple of verse word-counts (4, 4, 2, 3, 4, 3, 9). Compute the **Kolmogorov-Smirnov statistic** between Fātiḥa's empirical CDF over verse-word-count and the corpus-wide empirical CDF over all 6236 verse-word-counts.

Fātiḥa-encoding direction predicts the KS statistic to be UNUSUALLY LOW (Fātiḥa's word-count distribution closely matches corpus-wide). Note: this is the OPPOSITE direction from the other axes (low = encoding); pre-committed.

**Null model:** for each 7-verse window in the sliding-window null, compute the same KS statistic vs the corpus-wide CDF.

**Direction:** one-sided LOWER (Fātiḥa expected to be unusually CLOSE to corpus distribution).

**PASS:** Fātiḥa's percentile ≤ α_bon = 0.00833 (i.e., Fātiḥa is in the bottom 0.83% of KS distances → unusually representative).

### Axis 5 — COMPRESSION (gzip-cross-compression efficiency)

**Question:** Does Fātiḥa "encode" the rest of the Quran in the sense of gzip-compression — does prepending Fātiḥa to a corpus chunk significantly improve compressibility relative to the chunk alone?

**Test statistic:** compute c(rest) = compressed-size of the no-tashkeel-corpus-minus-Fātiḥa as a single UTF-8 string. Compute c(fatiha + rest) = compressed-size of (Fātiḥa-text + sep + rest). Compute the **compression-gain ratio** g_fatiha = (c(rest) - (c(fatiha+rest) - c(fatiha_alone))) / c(rest), i.e., the fractional reduction in marginal compressed size attributable to having Fātiḥa as a prefix dictionary.

Fātiḥa-encoding direction predicts g_fatiha to be UNUSUALLY HIGH (Fātiḥa is a maximally good compression-dictionary for the rest of the Quran).

**Null model:** for 1000 random 7-verse windows (sampled from sliding-window-null indices, seed 20260416), compute g_window using the same procedure.

**Direction:** one-sided UPPER (Fātiḥa expected to be the best 7-verse prefix-dictionary).

**PASS:** Fātiḥa's percentile ≥ 0.99167.

(Reduced n=1000 instead of full 6230 sliding for compute budget; pre-committed.)

### Axis 6 — FIRST-LETTER COVERAGE (alphabet-coverage representativeness)

**Question:** Which letters appear as **first letter of any token** in Fātiḥa? Are pharyngeal/glottal letters {ا, ه, ع, ح} (cf. [[h-new-44-2-poa-closure|H-NEW-44.2]].1) enriched relative to a random 7-verse window?

**Test statistic:** P_fatiha = (count of distinct pharyngeal/glottal letters appearing as first-letter-of-some-token in Fātiḥa, out of 4) / 4. Direction-encoded test: [[h-new-44-2-poa-closure|H-NEW-44.2]].1 already established muqaṭṭaʿāt-letters' pharyngeal/glottal exhaustivity. If Fātiḥa is a microcosm, it should likewise saturate the pharyngeal/glottal class.

**Test statistic (precise):** P_fatiha_count = number of distinct pharyngeal/glottal letters appearing as first-letter-of-some-token in Fātiḥa.

**Null model:** for each 7-verse window in the sliding-window null, compute the same count.

**Direction:** one-sided UPPER (Fātiḥa expected to cover all 4 pharyngeal/glottal letters).

**PASS:** Fātiḥa's percentile ≥ 0.99167.

## MW-5 known-distinctive verse

For axis 2 (semantic theme coverage) and axis 6 (first-letter pharyngeal coverage), the MW-5 sanity check is to confirm that a 7-verse window built around **Q 59:22-24** (Khawātim al-Ḥashr) is detected as a DEEP outlier on the relevant axis (specifically axis 1 lexical for divine-name density and axis 2 semantic theme coverage). For axis 4 (structural KS), Q 26:1-7 (which contains the Ṭā-Sīn-Mīm muqaṭṭaʿāt + 6 narrative verses of variable length) should be detected as a HIGH outlier (highly non-representative). These are non-blocking sanity checks; failure produces a transparency note, not a methodology rewrite.

## Pre-committed honesty controls

- Seed = 20260416. Re-run must reproduce results bit-identically.
- All 6 axes' raw values (Fātiḥa value, null distribution summary, percentile, p-value, pass/fail) are published in `csv/h-new-65.json` regardless of overall verdict.
- The PASS criterion (≥ 2 of 6 Bonferroni-significant) is locked BEFORE running the script.
- The choice of one-sided vs two-sided per axis is pre-committed above and not revised based on results.
- The classical claim "Fātiḥa is microcosm of the Quran" is given the MAXIMALLY CHARITABLE empirical hearing: 6 different axes, each with its own appropriate null, with a low PASS-bar of 2 Bonferroni-significant out of 6.
- Per M-9, this is the SECOND Fātiḥa-encoding test (the first was H-NEW-59 cell 3, REFUTED). If [[h-new-65-fatiha-as-dna|H-NEW-65]] also produces NULL or REFUTED, that compounds the empirical case AGAINST the strong microcosm claim; classical exegetical "microcosm" framings would then need to be reframed as theological/literary rather than statistical.

## Outputs

1. `/Users/grey/Downloads/quran/scripts/h_new_65_fatiha_as_dna.py` — the script
2. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-65.json` — raw per-axis results
3. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-65-fatiha-as-dna.md` — findings file
4. `/Users/grey/Downloads/quran/journal/h-new-65-run-1.md` — run journal

## Cross-references

- H-NEW-59 (divine-names-distribution.md) — Fātiḥa-as-divine-names-encoding REFUTED at α_bon (p=0.150). [[h-new-65-fatiha-as-dna|H-NEW-65]] axis 1 broadens to general lexical, not divine names.
- [[h-new-44-2-poa-closure|H-NEW-44.2]].1 (pharyngeal/glottal exhaustivity in muqaṭṭaʿāt) — [[h-new-65-fatiha-as-dna|H-NEW-65]] axis 6 tests whether Fātiḥa likewise saturates the pharyngeal/glottal class (extending the muqaṭṭaʿāt pattern to the Mother of the Book).
- M-9 (convergence-does-not-multiply): [[h-new-65-fatiha-as-dna|H-NEW-65]] + H-NEW-59 are 2 attempts at the broader microcosm question; effective independent N ≤ 2.
- MASTER-LEDGER (Fātiḥa structural primacy claims).
