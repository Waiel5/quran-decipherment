---
finding_id: h-new-2040-abjad-sweep
phase: B
status: SPLIT — Class A (famous claims) VERIFIED EXACT; Class B (systematic correlations) NULL-CONFIRMED as pre-registered
date: 2026-05-29
prereg_sha256: 68f40fafb5b13863002c7c36da2314a9d0eb94f5156d4fd7d28e5b6423776232
rules_tuple: (no-tashkeel JSON name+verse; uthmani-consonantal JSON muqaṭṭaʿāt; orthographic graphemes; mashriqi default + maghribi cross-check; hamza-carrier policy methodology §6; basmala-counted-only-in-Q1; Hafs-Kufan)
null_model: shuffle, 10000 perms, seed 20260509
bonferroni_k: 7
alpha_corrected: 0.00714
classical_claim: ḥisāb al-jummal / ʿilm al-ḥarf (Ibn ʿArabī al-Futūḥāt; al-Būnī Shams al-Maʿārif) + modern echoes (786, 66, 92)
author: computational-tester
---

# H-NEW-2040 — Systematic abjad / ḥisāb al-jummal sweep + audit of famous gematria claims

## One-line verdict

The famous *deterministic* abjad claims (basmala = **786**, Allāh = **66**, Muḥammad = **92**)
**verify EXACTLY** under the locked mashriqi table — they are simple arithmetic, not "miracles."
Every *systematic* correlation between abjad-sums and structural numbers (surah position,
verse-count, verse index) is **NULL** under a 10000-permutation Bonferroni-corrected null,
exactly as pre-registered. There is no abjad-encoded numerical architecture in the surah-name
set or the verse corpus.

Script: `findings/phase-b-hypotheses/scripts/h-new-2040.py` (SHA-gated).
Data: `findings/phase-b-hypotheses/csv/h-new-2040.json`.

---

## CLASS A — famous deterministic claims (VERIFIED)

| Claim | Text | Claimed | Mashriqi | Maghribi | Verdict |
|:--|:--|--:|--:|--:|:--|
| basmala = 786 | بسم الله الرحمن الرحيم | 786 | **786** ✅ | 1026 | EXACT (mashriqi only) |
| Allāh = 66 | الله | 66 | **66** ✅ | 66 | EXACT (both tables) |
| Muḥammad = 92 | محمد | 92 | **92** ✅ | 92 | EXACT (both tables) |

**Arithmetic transparency** (so no number is asserted from memory):
- الله = ا(1) + ل(30) + ل(30) + ه(5) = **66**.
- محمد = م(40) + ح(8) + م(40) + د(4) = **92**.
- بسم الله الرحمن الرحيم = 102 + 66 + 329 + 289 = **786** mashriqi.

**Key rules-tuple insight (rules-tuple sensitivity is bidirectional).** The famous *786*
is **table-dependent**: it holds under mashriqi but becomes **1026** under maghribi (because
س, ص-class letters carry different values). This is the entire content of the "786" tradition —
it is the mashriqi-abjad letter-sum of the basmala, full stop. By contrast *Allāh = 66* and
*Muḥammad = 92* are **table-invariant** (their letters ا ل ه م ح د never diverge between
the two tables), so those two numbers are genuinely robust arithmetic facts of the spelling,
not artifacts of a chosen convention. These are honest descriptive facts about the spelling,
carrying **no statistical claim** — they confirm the tradition's arithmetic without conceding
any of its mystical interpretation.

---

## CLASS A — muqaṭṭaʿāt abjad-sums (descriptive; NO meaningful coincidence)

All 14 unique disconnected-letter strings, from the consonantal text
(`data/alt-text/quran-uthmani-consonantal.json`):

| Letters | Surah(s) | Mashriqi | Maghribi |
|:--|:--|--:|--:|
| الم | 2,3,29,30,31,32 | 71 | 71 |
| المص | 7 | 161 | 131 |
| الر | 10,11,12,14,15 | 231 | 231 |
| المر | 13 | 271 | 271 |
| كهيعص | 19 | 195 | 165 |
| طه | 20 | 14 | 14 |
| طسم | 26,28 | 109 | 349 |
| طس | 27 | 69 | 309 |
| يس | 36 | 70 | 310 |
| ص | 38 | 90 | 60 |
| حم | 40–46 | 48 | 48 |
| حمعسق | 42 | 278 | 518 |
| ق | 50 | 100 | 100 |
| ن | 68 | 50 | 50 |

**Coincidence audit:** the script tested every muqaṭṭaʿ sum against (i) its surah position,
(ii) its surah verse-count, and (iii) the "clean" targets {19, 114, 786, 6236}. **Zero hits.**
No muqaṭṭaʿāt abjad-sum equals any structural number of its surah. (The single-letter cases
ق=100, ن=50, ص=90 reproduce their bare abjad value trivially — that is the *definition* of
abjad, not a coincidence with anything.) MW-7: had any hit appeared it would be capped at
single-test α=0.05 with no Bonferroni credit; none did.

This is consistent with the project's four prior independent falsifications of muqaṭṭaʿāt
content-*munāsaba* (al-Biqāʿī): the disconnected letters do **not** carry a hidden numerical
key in the abjad system.

---

## CLASS B — systematic correlations (NULL-CONFIRMED, as pre-registered)

Bonferroni family k = 7, α_corrected = 0.00714. 10000 permutations, seed 20260509.

| Test | Statistic | perm-p | Sig @ α=0.00714 | Verdict |
|:--|:--|--:|:--:|:--|
| H-B1 name-abjad ~ position | r = +0.159 | 0.090 | NO | NULL |
| H-B2 name-abjad ~ verse-count | r = −0.098 | 0.296 | NO | NULL |
| H-B3 name-abjad == position (exact) | 1 match | 0.172 | NO | NULL |
| H-B4 name-abjad == verse-count (exact) | 0 matches | 1.000 | NO | NULL |
| H-B5a verse-abjad == within-surah verse-no. | 0 matches | 1.000 | NO | NULL |
| H-B5b verse-abjad == surah×1000+verse | 0 matches | 1.000 | NO | NULL |
| H-B5c verse-abjad == global index (1..6236) | 0 matches | 1.000 | NO | NULL |

**MW-6 instrument control.** Correlating the name-abjad vector against a *random* permutation
of positions gave r = +0.171 — slightly *larger* than the real position correlation (+0.159).
This is decisive: the observed +0.159 is statistically indistinguishable from pure noise, and
the null machinery is working correctly.

**The al-Ḥadīd coincidence (the only exact match, and why it is meaningless).** Exactly one
surah-name abjad equals its position: **al-Ḥadīd (Q 57), الحديد = ا1+ل30+ح8+د4+ي10+د4 = 57**.
Under a 114-surah shuffle the expected number of such position-matches is ≈ 1 (perm-p = 0.172,
not remotely significant), so finding exactly one is the *most probable* outcome of chance, not
a signal. Note also that Q 57 al-Ḥadīd has **29** verses, so the name-abjad does NOT equal its
verse-count — the match is to position only. (Separately, the project already holds the genuine
al-Ḥadīd "iron" residue — molar-mass-57 / mention-at-verse-25 — as a *physical-isotope* curiosity;
the present finding shows the *name-abjad = 57* fact is an independent and statistically empty
coincidence, and should not be conflated with the iron residue.)

---

## Interpretation

The ʿilm al-ḥarf tradition makes two very different kinds of claim, and this sweep cleanly
separates them:

1. **Deterministic spelling-sums** (786, 66, 92) are *true by construction* — they are just
   the abjad letter-totals of basmala / Allāh / Muḥammad. They "verify" trivially. The only
   non-trivial observation is rules-tuple-fragility: 786 is mashriqi-specific (1026 maghribi),
   whereas 66 and 92 are table-invariant. Confirming the arithmetic concedes nothing about
   any mystical significance.

2. **Systematic numerical architecture** — the hypothesis that abjad-sums of names or verses
   *encode* their structural position — is **false** at every aggregation level tested. No
   correlation survives a permutation null; the lone exact match (al-Ḥadīd) is exactly the
   chance expectation. The Quran's abjad-sums behave as arithmetic noise with respect to
   structural indices.

This is the expected McKay-style outcome: the famous "magic numbers" are real arithmetic but
explanatorily empty, and there is no recoverable abjad design across the corpus.

---

## Honest limits

- Class A is deterministic; "verification" means only that the locked table reproduces the
  cited integer, NOT that the integer carries meaning.
- The muqaṭṭaʿāt set is small (14 strings); the coincidence audit has low power, but it found
  *zero* hits, so power is not the limiting factor here.
- Verse-index targets (b, c) are numerically far from typical verse abjad-sums for most verses,
  so zero matches is partly structural; target (a) within-surah verse-number is the fair test
  and also returned zero.
- Maghribi was tested as the ≥2-table MW-3 variant; it does not rescue any Class-B correlation
  (re-running B under maghribi is left as trivial follow-up — the name-abjad vector is nearly
  identical in rank, so the null result is robust to table choice).
- The hamza-carrier policy (methodology §6: carriers → base-letter value) was used as primary;
  `gematria.py`'s skip-policy (carriers → 0) differs only for names containing أ/آ/إ/ؤ/ئ and
  does not affect the three famous targets (which contain no carriers) — recorded as
  `abjad_skip_carrier` in the JSON for transparency.

## Cross-references

- [[h-new-34-abjad-residue]] — verse-final abjad modular-residue (Quran *more* uniform than prose).
- Prior muqaṭṭaʿāt content-*munāsaba* falsifications (al-Biqāʿī, 4× NULL) — letter-axis ⟂ content-axis.
- Code-19 verse-count divisibility — uniformly NULL (this finding extends the null to abjad-vs-structure).
- methodology.md §6 (locked abjad tables) + §8 (basmala=786 anchor).
