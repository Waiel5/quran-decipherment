---
finding_id: Q027-F-05
title: Q 27:30 second-basmala structural-role audit (verbatim corpus-uniqueness, around-text distinctiveness, candidate embedded-quotative-divine-name extension)
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q027-F-05..F-09
alpha_bon: 0.01
acceptance_window: see §6
---

# Q027-F-05 — Second-Basmala Structural Role


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

## 0. Origin and prior

Existing Q027-F-02 verified the **lexical** identity Q 27:30 ≡ Q 1:1 (deterministic; 0 Levenshtein across all 3 tashkeel variants). This pre-reg extends that verdict to **structural / corpus-architectural** dimensions: (a) verbatim 6-token uniqueness, (b) the embedding window's lexical distinctiveness vs corpus 5-verse windows, and (c) extension to candidate **embedded-quotative-divine-name** verses. F-02 said *"the slice is identical"*; F-05 asks *"how rare is the act of embedding the basmala/divine-name as a quoted speech-act, and is the surrounding narrative window itself architecturally distinctive?"*.

## 1. Hypothesis (locked before observation)

**H1.a — Verbatim 6-token uniqueness**: The 6-token sequence
`بسم الله الرحمن الرحيم` (under no-tashkeel) appears as a **substring of an interior verse** in **exactly 2** verses of the corpus (Q 1:1 and Q 27:30). Direction: equality with 2 (an exact integer prediction; pre-commit violation if count differs).

**H1.b — Around-text lexical distinctiveness**: The 5-verse window centered on Q 27:30 (vv. 28–32) is **lexically distinctive** vs corpus-baseline 5-verse windows. Operationalized as: the QAC-stem-root TF profile of [Q 27:28..32] has below-median Jaccard similarity to other 5-verse windows in the corpus. Direction: one-sided lower-tail (Q 27:28-32 is more distinctive than typical).

**H1.c — Embedded-quotative-divine-name extension**: Beyond the verbatim 6-token basmala, the **embedded-quotative-divine-name** category — verses containing `بسم الله` as an interior speech-act NOT at surah-prefix — extends to a **small** corpus set (predicted ≤ 4 verses corpus-wide; tight). Direction: cardinality ≤ 4, with all hits classified into ⟨caller, addressee, narrative-frame⟩ tuples.

**H0.a**: count of verbatim 6-token basmala = 1, or > 2.
**H0.b**: Q 27:28-32 window is at-or-above corpus-median lexical similarity.
**H0.c**: count of embedded-quotative-divine-name verses > 4.

## 2. Operational definitions

- **Verbatim test (H1.a)**: corpus = `quran-text/quran-no-tashkeel.json`. For each verse, check `'بسم الله الرحمن الرحيم' in verse_text`. Count the surahs and verses where this substring appears as an interior fragment of the verse_text (i.e., included in `verses[i].text` regardless of position).
- **Around-text Jaccard (H1.b)**:
  - Tokenize each surah at QAC-stem-root level using `data/morphology/quranic-corpus-morphology-0.4.txt` (root field).
  - For each surah s, slide a 5-verse window across [v_k..v_k+4] for k=1..(V_s−4). Compute the Jaccard of root-set(window) ∩ root-set(corpus minus window).
  - Q 27:28-32 = a single specific window. Compute its Jaccard rank among all corpus 5-verse windows.
  - Direction: lower-tail — Q 27:28-32 is in the bottom 30% (i.e., LESS overlapping with the rest of the corpus than 70% of windows).
- **Embedded-quotative test (H1.c)**:
  - Search for the substring `بسم الله` in each verse_text of the corpus (no-tashkeel).
  - Exclude surah-prefix occurrences (the "basmala-counted-only-in-Q1" rule means surah-prefix basmalas are NOT verses 1 of those surahs in this JSON — they are not in the JSON's verses[] array).
  - Catalog all matches with verse contents, narrative voice (1st-person / 3rd-person / quoted-speech), and speaker (if quoted speech).

## 3. Test statistics

- **H1.a stat**: integer count of verses containing the verbatim 6-token sequence. Pass = exactly 2.
- **H1.b stat**: percentile rank of Q 27:28-32 Jaccard among all corpus 5-verse windows. Pass = bottom 30%ile.
- **H1.c stat**: integer count of verses containing `بسم الله` as substring corpus-wide. Pass = ≤ 4.

## 4. Direction (LOCKED before observation)

- H1.a: count == 2.
- H1.b: percentile rank ≤ 30 (bottom-tail = distinctive).
- H1.c: count ≤ 4.

## 5. Permutation null (for H1.b only — H1.a and H1.c are deterministic-exact tests)

For H1.b — random-window null:
- Build the full set W of all 5-verse contiguous windows in the corpus (for surahs with V_s ≥ 5).
- For each window w in W, compute Jaccard(root-set(w), root-set(corpus minus w)).
- p_perm = #(rank(w) ≤ rank(Q 27:28-32) under one-sided lower-tail) / |W|.
- Seed 20260507 (used only for any reshuffling; the rank is deterministic — seed reserved for any tie-breaks or replication.)

## 6. Bonferroni and acceptance

- bonferroni_k = 5 (Q027-F-05..F-09 family); α_bon = 0.05/5 = 0.01.
- **Acceptance windows** (locked before observation):
  - **CONFIRMED** = all 3 of H1.a, H1.b, H1.c PASS.
  - **DIRECTIONAL** = 2 of 3 PASS.
  - **MIXED** = 1 of 3 PASS.
  - **NULL** = 0 of 3 PASS.
  - **PRE-COMMIT VIOLATION** = H1.a count ≠ 2 (the tightest pre-commit; would require explicit retraction).

## 7. Rules-tuple

- H1.a, H1.c: `(no-tashkeel, orthographic-exact-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- H1.b: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Roots: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- Numerical claims: only after computation; cite JSON output `csv/Q027-F-05.json`.

## 9. Honest a-priori limits

- The "embedded-quotative-divine-name" category (H1.c) is sensitive to the search-string (`بسم الله` = 2 tokens, includes alif-lam-allāh). Substring matching may yield false positives if `الله` appears in tight phrasing with `بسم` for other reasons (e.g., shahāda formulas) — but in a no-tashkeel orthographic search, the bigram `بسم الله` is essentially uniquely the bismi-llāh formula. Sensitivity check: report ALL matches verbatim with surrounding context.
- The Jaccard test (H1.b) is sensitive to window size (5 verses) and root-set vs token-set choice. The 5-verse window centered on Q 27:30 (vv. 28-32) is the **declared center**; pre-committed before computation. We do not vary window size post-hoc.
- The 5-verse-windows null pool is large (~6000 windows); the percentile estimate is precise.
- H1.a is deterministic — count is integer. The test is structurally identical to F-02 but expanded scope (substring, not slice-from-بسم); no probabilistic component.

## 10. Cross-references

- Q027-F-02 (lexical-identity, CONFIRMED) — F-05 extends with structural / window distinctiveness + extension class.
- [[h-new-111-fisher-rao-mushaf]] — global FR matrix.
- [[h-new-660-compression-tail-gradient]] — for Q 27 head-zone classification.

## 11. Garden-of-forking-paths log

- The 5-verse window vv. 28-32 was selected pre-observation as the canonical center (basmala verse v.30 ± 2). No post-hoc shifting.
- The cap "≤ 4" for H1.c was set before search; based on a-priori survey of Solomon's letter (Q 27:30) + Noah's ark (Q 11:41 has the *bismi-llāh* phrase per classical commentary) as known candidates plus a slack of 2.
- Verbatim 6-token search uses no-tashkeel; sensitivity check under min-tashkeel and full-tashkeel is reported but does not move the pre-committed verdict.
