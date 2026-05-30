---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: prereg
test_id: Q094-F-01
date_locked: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q094-F-01 — Pre-Registration: the al-ʿusr / al-yusr reprise (94:5-6) as the corpus's tightest near-verbatim adjacent couplet

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q094_F_01_usr_yusr_reprise.py` and verified at runtime (fail-fast on mismatch).

## Motivation

Q 94 al-Sharḥ closes its central panel with one of the most famous repetitions in the
Qurʾān:

- v 5 `فإن مع العسر يسرا` — *fa-inna maʿa al-ʿusri yusrā* ("for truly, with the hardship comes ease")
- v 6 `إن مع العسر يسرا` — *inna maʿa al-ʿusri yusrā* ("truly, with the hardship comes ease")

The two verses are character-identical **except** that v 5 carries a leading connective fāʾ
(فإن) which v 6 drops (إن). Classical exegesis attaches a precise grammatical reading to this:
because *al-ʿusr* ("the hardship") is **definite** (الـ) in both verses, it denotes one and the
same hardship; because *yusr* ("ease") is **indefinite** (yusrā / يسرا, tanwīn) in both, the two
occurrences denote two *distinct* eases — hence the ḥadīth/āthar transmitted by al-Ḥasan al-Baṣrī
(mursal, via Ibn Jarīr al-Ṭabarī) and reported from Ibn ʿAbbās and Ibn Masʿūd: **"lan yaghliba
ʿusrun yusrayn"** — "one hardship will not overcome two eases" (al-Ṭabarī, *Jāmiʿ al-bayān*, on
Q 94:5; al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 94:5, citing Thaʿlab vs al-Farrāʾ vs
al-Jurjānī; Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 94:5-6: *"fa-l-ʿusr muʿarraf fī al-ḥālayn
fa-huwa mufrad, wa-l-yusr munakkar fa-taʿaddad"*). The dropped fāʾ at v 6 is itself read by
al-Qurṭubī as the syntactic marker of a fresh *ibtidāʾ* (independent restart), not a coordinated
continuation — the *ʿarī min fāʾ aw wāw* observation.

This is the project's first per-surah landing of the **near-verbatim adjacent reprise** structure
— a class of repetition that the strict verbatim refrain census (H-NEW-2310) does NOT capture,
because the two verses are not byte-identical (the fāʾ differs). H-NEW-2310 §1.1 lists 24
intra-surah *verbatim* repeated strings; Q 94:5-6 is absent from that list precisely because of
the one-character delta. This pre-reg promotes the close-reading observation into a falsifiable
corpus-rarity claim about *near*-verbatim adjacency.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes/word-tokens, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Verse text from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. Pause/sajda
diacritic marks (ۖ ۚ ۗ ۛ ۙ ۘ ۞ etc.) stripped before tokenization. Word = whitespace-delimited
orthographic token after mark-stripping. Character edit distance = standard Levenshtein on the
space-stripped normalized verse string. Roots from QAC v0.4
(`/Users/grey/Downloads/quran/data/morphology/root-index.json`, `[surah,verse,word]` attestations).

## Arm A — corpus-exclusivity of the single-connective near-verbatim adjacency (CONFIRMATORY, deterministic)

**Hypothesis A (pre-committed):** Among all adjacent same-surah verse pairs (verse n, verse n+1)
in the corpus, Q 94:5-6 is the **unique** pair whose two normalized verse-strings are identical
except for a single leading connective particle (a leading fāʾ ف or wāw و on exactly one token,
with all other tokens identical and equal token-count).

- **A-H1 (direction-locked, count):** the corpus count of adjacent same-surah pairs that are
  token-identical except for exactly one token, where that one differing token is the other token
  with a single leading ف or و prepended/removed, **= 1**, and that pair **= Q 94:5-6**.
- **A-H2 (whole-string form):** under the stricter whole-string definition (verse-string B equals
  verse-string A with a single leading ف/و character removed, or vice versa), the corpus count
  **= 1** and **= Q 94:5-6**.

**A success criterion:** A-H1 ∧ A-H2 both hold (count = 1, = Q 94:5-6) → Arm A CONFIRMED
(deterministic corpus-singleton).
**A failure criterion:** count = 0 (Q 94:5-6 does not match the operationalization) or count ≥ 2
(not unique) → Arm A NULL / partial.

## Arm B — Q 94:5-6 is the global minimum-edit-distance adjacent couplet (CONFIRMATORY + permutation null)

**Hypothesis B (pre-committed):** Q 94:5-6 is the **tightest** near-verbatim adjacent same-surah
couplet in the corpus by character edit distance, and this tightness is extreme against a
length-matched random-pair null.

- **B-H1 (direction-locked, rank):** restricting to substantive adjacent same-surah pairs (each
  verse ≥3 word-tokens), the **minimum** character (Levenshtein) edit distance over all such pairs
  is achieved **uniquely** by Q 94:5-6, with edit distance = 1. **Direction lock: Q 94:5-6 is rank
  1 (smallest edit distance); edit distance = 1.**
- **B-H2 (no exact-verbatim adjacency):** the count of *exact*-verbatim (edit distance 0) adjacent
  same-surah pairs with ≥2 tokens is **0** — i.e. the Qurʾān never places two byte-identical verses
  in immediate succession, so Q 94:5-6's edit-1 is as close to verbatim adjacency as the corpus
  ever comes. **Direction lock: exact-verbatim-adjacent count = 0.**
- **B-H3 (permutation null, direction-locked):** the observed edit distance between Q 94:5-6
  (=1, normalized to a similarity 1 − edit/maxlen) is **TIGHTER** (smaller edit, higher similarity)
  than a length-matched random-verse-pair null. **Permutation null B (seed=20260509, 10000 perms):**
  draw random pairs of distinct corpus verses each matched to (len(v5), len(v6)) within ±3
  characters; compute character edit distance; the p-value is the fraction of null draws with edit
  distance ≤ 1 (i.e. as tight as or tighter than observed). **Direction lock: p_perm(edit ≤ 1) <
  α_corrected** (the observed near-identity is non-random). Bonferroni: 1 permutation cell (see below).

**B success criterion:** B-H1 (rank-1, edit = 1) ∧ B-H2 (exact-adjacent count = 0) ∧ B-H3
(p < α_corrected, direction TIGHTER) → Arm B CONFIRMED.
**B partial:** 2/3 → DIRECTIONAL.
**B failure / pre-commit violation:** if Q 94:5-6 is NOT rank-1 (some other adjacent pair has a
smaller edit distance) OR B-H3's direction reverses (the null is on average tighter than observed)
→ published as NULL with explicit pre-commit-violation flag.

## Arm C — the definite/indefinite "two-eases" asymmetry (CONFIRMATORY, deterministic, descriptive)

**Hypothesis C (pre-committed):** the classical "one hardship, two eases" reading has an exact
orthographic correlate in the no-tashkeel text: *al-ʿusr* is written with the definite article الـ
in BOTH v 5 and v 6 (one definite referent), while *yusr* is written WITHOUT the article and with
the indefinite accusative spelling يسرا (tanwīn alif) in BOTH (two indefinite referents).

- **C-H1 (deterministic):** the token *العسر* (definite) appears in both v 5 and v 6; the token
  *يسرا* (indefinite, alif-tanwīn spelling, no article) appears in both v 5 and v 6. The two verses
  share a root-Jaccard of exactly **1.0** (identical root-sets {ʿ-s-r, y-s-r} once function-words
  are excluded), confirming they are the same proposition reprised, not two different propositions.

**C success criterion:** C-H1 holds → Arm C CONFIRMED (the grammatical asymmetry that grounds the
classical *yusrayn* reading is an exact orthographic fact, not an interpretive imposition). This arm
is descriptive: it does NOT adjudicate the *theological* "two eases" claim (which is out of scope per
Protocol §10); it only verifies that the definite-ʿusr / indefinite-yusr orthographic asymmetry on
which al-Ḥasan/al-Farrāʾ/Thaʿlab built the reading is really present in the text.
**C failure:** the orthographic asymmetry is absent → Arm C NULL.

## Null distributions

- **Null A / C (Arm A, C context):** deterministic; no permutation.
- **Null B (Arm B B-H3):** length-matched random-verse-pair permutation, seed=20260509, 10000 perms,
  matching window ±3 characters on each member. p_perm = (#{null edit ≤ 1} + 1) / (N_perm + 1).

## Bonferroni

Test family Q094-F-01 has k = 1 permutation cell (B-H3). The deterministic cells (A-H1, A-H2, B-H1,
B-H2, C-H1) are not permutation tests and do not consume α. α_corrected for the single permutation
cell = 0.05 / 1 = 0.05.

## MW protections

- **MW-1 (instrument-prior):** the single-connective-delta definition, the Levenshtein edit metric,
  the ≥3-word substantive filter, and the root-Jaccard are all fixed here before any run.
- **MW-2 (corpus-prior):** Null B uses 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A reports BOTH the token-level (A-H1) and whole-string (A-H2)
  operationalizations; Arm B reports the full ranked edit-distance table (the runner-up edit-2 family).
- **MW-5 (replication):** A-H1, A-H2, B-H1, B-H2, C-H1 are deterministic and fully replicable from the
  no-tashkeel JSON + QAC root-index. B-H3 seed-locked at 20260509; re-run at a second seed (20260530)
  is reported.
- **MW-6 (instrument-control):** B-H3's length-matched random pool is the non-target control; the
  edit-2 runner-up pairs (Q 74:19-20, Q 75:34-35, Q 82:17-18, Q 102:3-4) are the natural in-corpus
  control group (near-misses that did NOT achieve edit-1).
- **MW-7 (post-hoc cap):** the reprise observation was noticed in close reading then promoted to these
  direction-locked PRE-REGISTERED tests BEFORE computation; the single-test α=0.05 cap is respected.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 ∧ A-H2 (count = 1, = Q 94:5-6) | CONFIRMED (deterministic corpus-singleton) |
| B | B-H1 ∧ B-H2 ∧ B-H3 | CONFIRMED |
| B | 2/3 | DIRECTIONAL |
| B | rank ≠ 1 or B-H3 direction reversed | NULL (pre-commit violation, full prominence) |
| C | C-H1 | CONFIRMED (orthographic asymmetry present) |

Final Q094-F-01 verdict = honest combination of Arms A, B, C, reported with equal NULL prominence.

*Locked 2026-05-30. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
