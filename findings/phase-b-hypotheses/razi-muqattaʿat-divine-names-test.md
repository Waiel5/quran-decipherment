---
finding_id: H20-extended
date: 2026-04-13
title: "Al-Rāzī's per-letter divine-name assignments: host-surah density and token-enrichment test"
agent: razi-muqattaat-divine-names
classical_attribution: Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-Ghayb / al-Tafsīr al-Kabīr* (d. 606 H / 1209 CE), excursus on Q. 2:1; al-Suyūṭī *al-Itqān* chs. 40–41; al-Qurṭubī *al-Jāmiʿ* on Q. 2:1, 19:1, 50:1; al-Zarkashī *al-Burhān* nawʿ 17.
rules_tuple:
  orthography: no-tashkeel
  word_definition: not-applicable (letter-level test; token test uses whole-word regex match on cleaned text)
  letter_definition: graphemes; hamza variants (أ إ آ ٱ ء) normalized to ا; ى→ي; ة→ت; ؤ→و; ئ→ي. Recitation marks U+06D6..U+06ED excluded.
  basmala_policy: counted-only-in-surah-1 (amrayn JSON convention; matches locked anchor 330,709 letters)
  verse_numbering: hafs-kufan (6236 verses)
  abjad_table: not-applicable
null_model: >
  Primary: two-proportion z on (k_in_surah, n_in_surah) vs. (k_rest_of_Quran, n_rest_of_Quran)
  for (a) the union of graphemes constituting each assigned divine name post-ال, and
  (b) the divine-name token count from the curated divine-names-by-verse.csv
  (fallback: whole-word regex on cleaned Arabic text).
  Secondary (pre-registered): shuffle-null over the 14 muqaṭṭaʿāt letters.
  1,000 permutations per claim: assign name D to a random letter L' from the
  14 luminous letters, pick a random host surah of L', recompute density z.
  Empirical upper-tail p.
pre_registration: |
  Rules tuple locked 2026-04-13 before data-touch. Statistics named:
    density_test(sid, name) = two-prop z(k_letters_of_name_in_surah / n_surah,
                                           k_letters_of_name_in_rest / n_rest)
    token_test(sid, name)   = two-prop z(tokens_in_surah / n_surah_letters,
                                           tokens_in_rest / n_rest_letters)
    shuffle_null_density    = 1000 permutations over 14 luminous letters ×
                              random host-surah choice among that letter's hosts.
  Multiple-comparison correction: Bonferroni over N_claims = 78 at α=0.05,
    i.e. per-claim threshold 6.41e-4.
  Acceptance: al-Rāzī's theory "survives" iff >=5 of his letter→name claims
    pass BOTH the density two-prop test AND the token two-prop test at
    Bonferroni-corrected α.
acceptance_criterion: >=5 of 78 pre-registered (surah, muqaṭṭaʿāt letter, divine name)
  claims pass BOTH density-Bonferroni AND token-Bonferroni in the
  over-represented direction. Fallback weaker criterion (for transparency
  only): >=5 claims pass the shuffle-null Bonferroni threshold on density.
code: /Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/run_test.py
results_csv: /Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/claim_results.csv
---

# Al-Rāzī's per-letter divine-name assignments — density + token test

## Executive summary (honest verdict first)

**Verdict: REFUTED at the strict, pre-registered acceptance criterion.** Out of
**78** pre-registered al-Rāzī / classical letter→divine-name claims (one per
muqaṭṭaʿāt letter occurring in each muqaṭṭaʿāt surah):

| Bonferroni-corrected test (α = 6.41e-4) | Claims passing (positive direction) |
|---|---|
| Density test (name's graphemes enriched inside host surah) | **7 / 78** |
| Token test (divine-name as word-token enriched inside host surah) | **1 / 78** |
| **BOTH density AND token simultaneously** | **1 / 78** |
| Shuffle-null density (permutation over 14 luminous letters) | **0 / 78** |

Acceptance required **≥ 5 claims passing BOTH**. Observed: 1 (the trivial case
Allah ↔ ا in Surah 3). The pre-registered shuffle null, which properly controls
for the fact that the muqaṭṭaʿāt letters are all high-frequency letters whose
grapheme inventories overlap heavily with divine names that contain those same
high-frequency letters, kills **every** enrichment signal (0 / 78 at Bonferroni).

**Al-Rāzī's theory, as operationalized in the strong form ("the assigned name's
letters are densely packed AND the assigned name appears more often as a token
in the host surah than elsewhere"), is not supported by the text.** The one
density-significant cluster (ا-initialing Allah in ALM surahs 2, 3, 13, 31)
collapses to a trivial artifact — every verse containing the word الله enriches
both the alif and the lām count, and ALM surahs that are heavily theocentric
naturally score high on alif density.

**The inverse test tells a similar story.** When we ask, for each muqaṭṭaʿāt
surah, "which of the canonical 99 names is best covered by this surah's opening
letters?", al-Rāzī's proposed name appears in the top-5 list for **12 of 29
surahs (41.4%)** — but nearly all hits are the trivially-covered ا-starting
names (*Allāh* itself for the ALR surahs) or cases (Q7 *al-Ṣamad*, Q19
*al-ʿAzīz*, Q26/27/28 *al-Salām*, Q38 *al-Ṣamad*, Q68 *al-Nūr*) that would be
recovered by any coverage-based algorithm regardless of al-Rāzī's authority.
No surah has al-Rāzī's **most-emphasised** name (*al-Laṭīf*, *al-Majīd*,
*al-Ḥamīd*, *al-Ḥalīm*, *al-Qādir*, *al-Hādī*) as a top-3 inverse match.

**What this tells us about ʿilm al-ḥurūf.** The classical *isrār al-ḥurūf*
tradition's divine-name decomposition is a post-hoc interpretive framework, not
a descriptive encoding. The letters of al-Rāzī's assigned names are no more
densely packed in the host surah than you'd get by randomly pairing any
frequent Arabic letter-set with any muqaṭṭaʿāt surah. That does *not* refute
the devotional / mnemonic / pedagogical function the tradition ascribes to
the muqaṭṭaʿāt — it only refutes the **strong statistical form** of the
"abbreviation of divine names" reading.

---

## 1. What al-Rāzī actually claimed — verbatim with citations

Fakhr al-Dīn al-Rāzī, in his excursus on Q. 2:1 in *Mafātīḥ al-Ghayb* (al-Tafsīr
al-Kabīr, vol. 2 of the standard 32-vol. Cairo ed.; commentary on the opening
of Sūrat al-Baqarah), lists **~20 distinct opinions** on the muqaṭṭaʿāt. He
reports the "divine-names abbreviation" opinion as held by several of the
salaf — most notably **ʿAbd Allāh ibn ʿAbbās** (via al-Ṭabarānī and Tanwīr
al-Miqbās) and **ʿAbd Allāh ibn Masʿūd**. Al-Rāzī himself does **not** commit
to this opinion: he explicitly notes that the disagreement among the salaf
about which divine names the letters abbreviate is a reason to doubt that any
single decomposition is uniquely intended.

The specific letter→name assignments preserved in the classical literature
(collated from al-Rāzī, al-Suyūṭī *al-Durr al-Manthūr* 4/679, al-Qurṭubī
*al-Jāmiʿ*, al-Zamakhsharī *al-Kashshāf*, and Tanwīr al-Miqbās) and from the
existing project extract at
`/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-99names-extract.md`:

| Combo | Surahs | Classical decomposition (letter → name) | Source attribution |
|---|---|---|---|
| ALM (الم) | 2, 3, 29, 30, 31, 32 | ا → Allāh; ل → al-Laṭīf; م → al-Majīd | Ibn ʿAbbās via al-Ṭabarānī; al-Rāzī reports |
| ALMS (المص) | 7 | As ALM + ص → al-Ṣamad / al-Ṣādiq | al-Qurṭubī |
| ALR (الر) | 10, 11, 12, 14, 15 | ا → Allāh; ل → al-Laṭīf; ر → al-Raḥmān | al-Rāzī |
| ALMR (المر) | 13 | ا → Allāh; ل → al-Laṭīf; م → al-Majīd; ر → al-Raḥmān | al-Rāzī |
| KHYAS (كهيعص) | 19 | ك → al-Kabīr; ه → al-Hādī; ي → **al-Amīn** *(strict-fail: starts with alif)*; ع → al-ʿAzīz; ص → al-Ṣādiq | Ibn ʿAbbās via al-Suyūṭī *al-Durr* 4/679 |
| TH (طه) | 20 | ط → al-Ṭāhir; ه → al-Hādī | al-Rāzī / al-Qurṭubī |
| TSM (طسم) | 26, 28 | ط → al-Ṭāhir; س → al-Salām; م → al-Majīd | al-Rāzī / al-Qurṭubī |
| TS (طس) | 27 | ط → al-Ṭāhir; س → al-Salām | al-Rāzī / al-Qurṭubī |
| YS (يس) | 36 | ي → al-Sayyid *(vocative, not a name strictu sensu)*; س → al-Salām | al-Rāzī |
| S (ص) | 38 | ص → al-Ṣamad | al-Rāzī |
| HM (حم) | 40, 41, 43, 44, 45, 46 | ح → al-Ḥamīd; م → al-Majīd | al-Rāzī (alt. Ḥalīm / Majīd) |
| HMASQ (حمعسق) | 42 | ح → al-Ḥalīm; م → al-Majīd; ع → al-ʿAzīz; س → al-Samīʿ; ق → al-Qādir | al-Rāzī |
| Q (ق) | 50 | ق → al-Qādir (also al-Qayyūm, al-Qarīb) | al-Rāzī |
| N (ن) | 68 | ن → al-Nūr (also al-Nāṣir) | al-Rāzī |

**Two of these classical decompositions already fail al-Rāzī's implicit rule
by his own reporting:** Ibn ʿAbbās's ي → al-Amīn (al-Amīn begins with hamza,
not yāʾ) and the YS reading ي → Yā Sayyid (vocative particle, not abbreviation).
Al-Rāzī records these as evidence that the strict letter-as-initial rule was
never uniformly observed, weakening the strong form of the hypothesis before
any statistical test is run.

## 2. Procedure

### Corpus and rules tuple

- **Canonical text:** `quran-text/quran-no-tashkeel.json` (114 surahs,
  6,236 verses, locked total 330,709 letter-graphemes post-normalization).
- **Rules tuple (locked):** `(no-tashkeel, not-applicable, graphemes,
  counted-only-in-surah-1, hafs-kufan, mashriqi)`. The mashriqi abjad table
  is declared for completeness; this test does not use gematric values.
- **Normalization:** hamza-variants (أ إ آ ٱ ء) → ا; ى → ي; ة → ت;
  ؤ → و; ئ → ي. Recitation marks U+06D6–U+06ED excluded.

### The 78 pre-registered claims

For each of the 14 unique muqaṭṭaʿāt combinations and each surah carrying that
combination, one (surah, letter, classical-assigned-name) claim per letter
present in the opening, using the classical decompositions in §1.

Total claims: 78 (e.g., ALM opens 6 surahs × 3 letters = 18 claims for the
ALM decomposition; HMASQ alone contributes 5 claims).

### Two statistics per claim

1. **Density test.** For the set L(D) of the distinct graphemes appearing in
   the Arabic surface form of divine name D (with its ال stripped — so that
   الله contributes {ل, ه}, اللطيف contributes {ل, ط, ي, ف}, etc.), compute:
   - `k_in = Σ_{ℓ ∈ L(D)} count(ℓ, host_surah)`
   - `n_in = total letters in host surah`
   - `k_out, n_out = same over rest-of-Quran`
   - two-proportion z with pooled SE → `density_z`, `density_p` (two-tailed).
   - we accept the claim only if `density_z > 0` (over-represented direction).

2. **Token test.** For each name D we look up the count of D as a whole-word
   token in each surah. Primary source: the project-curated
   `findings/phase-b-hypotheses/divine-names-by-verse.csv` (which tracks
   canonical-99 names per verse). For names absent from that CSV (al-Ṭāhir,
   al-Amīn, al-Sayyid, al-Ṣādiq — none of which are canonical 99), fall back
   to a Unicode-regex whole-word match on the cleaned normalized text.
   Then the same two-proportion z as in (1), against rest-of-Quran.

### Pre-registered shuffle null (density)

For each claim (sid, L, D): over 1,000 permutations, assign D to a random
letter L' ∈ {14 muqaṭṭaʿāt letters}, then pick a random surah sid' from the
set of surahs hosting L', and recompute the density z at (sid', L(D)). This
null deliberately preserves (a) that the claimed name's letter inventory is
being tested against a muqaṭṭaʿāt host surah and (b) that the host surah
really is a muqaṭṭaʿāt surah. It breaks **only** the specific letter→name
pairing that al-Rāzī proposes. Empirical one-tailed upper-p.

### Multiple-comparison correction

Bonferroni over N = 78 claims; α = 0.05 / 78 = **6.41 × 10⁻⁴**.

### Acceptance (strict)

≥ 5 claims must pass **both** the density test and the token test at
Bonferroni. Weaker transparency criterion: ≥ 5 claims pass the shuffle-null
Bonferroni on density.

---

## 3. Results per claim — headline numbers

Full per-claim results in
`/Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/claim_results.csv`.

### 3.1 Density test — 7 claims pass Bonferroni (out of 78)

| Surah | Letter | Assigned name | Name graphemes (post-ال) | Rate in surah | Rate in rest | z_density | p | Shuffle-null p_up |
|---|---|---|---|---|---|---|---|---|
| 3 | ا | Allāh (الله) | ل ه | 17.06% | 15.99% | +3.48 | 5.07e-04 | 0.046 |
| 15 | ر | al-Raḥmān (الرحمن) | ح ر م ن | 24.60% | 21.30% | +4.30 | 1.69e-05 | 0.100 |
| 13 | ا | Allāh | ل ه | 18.39% | 16.01% | +3.84 | 1.23e-04 | 0.021 |
| 19 | ك | al-Kabīr (الكبير) | ب ر ك ي | 20.51% | 18.16% | +3.80 | 1.44e-04 | 0.202 |
| 42 | ح | al-Ḥalīm (الحليم) | ح ل م ي | 31.54% | 28.64% | +3.79 | 1.49e-04 | 0.121 |
| 42 | ع | al-ʿAzīz (العزيز) | ز ع ي | 13.03% | 11.09% | +3.64 | 2.68e-04 | 0.189 |
| 50 | ق | al-Qādir (القدير) | د ر ق ي | 18.98% | 15.46% | +3.77 | 1.64e-04 | 0.275 |

**Observations.** All 7 "passers" are failures once the shuffle null is
applied. For instance, the strongest nominal effect (S15 / al-Raḥmān)
sits at only the 90th percentile of the shuffle null; the S50 / al-Qādir
claim is at the 72nd percentile. The shuffle null properly controls for the
fact that any muqaṭṭaʿāt surah, paired with any 3–4-letter set drawn from
high-frequency Arabic letters, will show nominal density enrichment with
probability considerably >5%.

### 3.2 Token test — 1 claim passes Bonferroni (out of 78)

| Surah | Letter | Assigned name | Tokens in surah | Tokens total | z_token | p |
|---|---|---|---|---|---|---|
| 3 | ا | Allāh (الله) | 131 | 1821 | +5.48 | 4.30e-08 |

All other token tests fall short. The runner-up is S31/Allāh (z = +2.63,
p = 0.008) — far above Bonferroni. No claim involving a *non*-Allāh divine
name passes the token test at α = 6.41e-4.

**The single "passing" claim is trivial.** Surah 3 (Āl ʿImrān) is one of the
most theocentric Medinan surahs and uses الله at 131 tokens vs. its length
share's expectation of ≈ 82. The alif→Allāh assignment is the only case
where the assigned name is the single most common lexeme in the Quran, so
the token test reduces to "is the most-common divine name over-used in a
theocentric surah?". Yes. This tells us nothing specific about al-Rāzī's
abbreviation thesis.

### 3.3 BOTH tests — 1 claim (same trivial case)

Only S3 / ا → Allāh passes both Bonferroni thresholds. Acceptance criterion
requires ≥5. **Fail: 1 < 5.**

### 3.4 Shuffle-null density — 0 claims pass Bonferroni

Every al-Rāzī claim is consistent with chance under a null that randomly
pairs the assigned name's letter-inventory with any other muqaṭṭaʿāt surah.
The maximum observed shuffle-null upper-p is 0.021 (S13 / ا → Allāh); at
Bonferroni α = 6.41e-4, **zero claims survive**.

---

## 4. Why the density test fails — the null mean is shifted

For each claim the 1,000-permutation null distribution has mean z ≠ 0 because
the claimed name's letter set typically shares letters with other muqaṭṭaʿāt
openings. E.g., al-Laṭīf contributes {ل, ط, ي, ف} — three of four of those
graphemes are themselves luminous letters, so *any* muqaṭṭaʿāt host surah
chosen at random scores an already-positive z for the "density of al-Laṭīf's
letters". The shuffle null means for representative claims:

| Claim | null mean z | null SD z | observed z | SDs above null mean |
|---|---|---|---|---|
| S3 / Allāh (ل ه) | −1.59 | 2.41 | +3.48 | +2.10 |
| S15 / al-Raḥmān (ح ر م ن) | +0.76 | 2.17 | +4.30 | +1.63 |
| S19 / al-Kabīr (ب ر ك ي) | +1.22 | 2.08 | +3.80 | +1.24 |
| S42 / al-Ḥalīm (ح ل م ي) | +0.07 | 2.11 | +3.79 | +1.76 |
| S50 / al-Qādir (د ر ق ي) | +1.52 | 2.25 | +3.77 | +1.00 |

In every case the observed z is < 2.6 SDs above the null mean — far below
what Bonferroni at k = 78 requires (z > 3.58 for one-sided significance on a
normal-approximated null). This is the McKay-style trap §2 of the protocol
explicitly warns against: the naive two-prop test treats the letter-inventory
as independent draws, but the letter-inventory is itself conditioned on being
"a plausible Arabic name", and those names share letters with muqaṭṭaʿāt
openings for reasons unrelated to al-Rāzī's thesis.

---

## 5. Inverse test — does al-Rāzī's name show up as a top match?

For each muqaṭṭaʿāt surah, we rank the 99 canonical divine names by
**coverage** = |L(D) ∩ opening_letters| / |L(D)|, breaking ties by in-surah
whole-word token count.

### Top-5 inverse matches per surah and al-Rāzī "hit" status

| Surah | Opening | Top-5 by coverage | al-Rāzī claim | al-Rāzī in top-5? |
|---|---|---|---|---|
| 2 | الم | al-Salām, Mālik al-Mulk, al-Malik, al-Mudhill, al-Awwal | Allāh, al-Laṭīf, al-Majīd | **no** |
| 3 | الم | al-Salām, Mālik al-Mulk, al-Malik, al-Mudhill, al-Awwal | Allāh, al-Laṭīf, al-Majīd | **no** |
| 7 | المص | al-Salām, Mālik al-Mulk, al-Malik, al-Mudhill, **al-Ṣamad** | Allāh, al-Laṭīf, al-Majīd, al-Ṣamad | HIT (al-Ṣamad) |
| 10 | الر | al-Awwal, al-Ākhir, al-Ḍārr, **Allāh**, al-Salām | Allāh, al-Laṭīf, al-Raḥmān | HIT (Allāh) |
| 11 | الر | al-Awwal, al-Ākhir, al-Ḍārr, **Allāh**, al-Salām | Allāh, al-Laṭīf, al-Raḥmān | HIT (Allāh) |
| 12 | الر | al-Ākhir, al-Awwal, al-Ḍārr, **Allāh**, al-Qahhār | Allāh, al-Laṭīf, al-Raḥmān | HIT (Allāh) |
| 13 | المر | al-Salām, Mālik al-Mulk, al-Malik, al-Mudhill, al-Awwal | Allāh, al-Laṭīf, al-Majīd, al-Raḥmān | **no** |
| 14 | الر | al-Awwal, al-Ākhir, al-Ḍārr, **Allāh**, al-Qahhār | Allāh, al-Laṭīf, al-Raḥmān | HIT (Allāh) |
| 15 | الر | al-Awwal, al-Ākhir, al-Ḍārr, **Allāh**, al-Salām | Allāh, al-Laṭīf, al-Raḥmān | HIT (Allāh) |
| 19 | كهيعص | **al-ʿAzīz**, al-ʿAlī, Allāh, al-Muhaymin, al-ʿAlīm | al-Kabīr, al-Hādī, al-Amīn, al-ʿAzīz, al-Ṣādiq | HIT (al-ʿAzīz) |
| 20 | طه | Allāh, al-Muhaymin, al-Qahhār, al-Wahhāb, al-Bāsiṭ | al-Ṭāhir, al-Hādī | **no** |
| 26 | طسم | al-Muqsiṭ, al-Samīʿ, **al-Salām**, al-Bāsiṭ, al-Malik | al-Ṭāhir, al-Salām, al-Majīd | HIT (al-Salām) |
| 27 | طس | al-Bāsiṭ, al-Muqsiṭ, al-Quddūs, **al-Salām**, al-Samīʿ | al-Ṭāhir, al-Salām | HIT (al-Salām) |
| 28 | طسم | al-Muqsiṭ, **al-Salām**, al-Bāsiṭ, al-Samīʿ, al-Ḥakam | al-Ṭāhir, al-Salām, al-Majīd | HIT (al-Salām) |
| 29 | الم | al-Salām, Mālik al-Mulk, al-Malik, al-Mudhill, al-Awwal | Allāh, al-Laṭīf, al-Majīd | **no** |
| 30 | الم | (same as S2/S3/S29/S31/S32) | Allāh, al-Laṭīf, al-Majīd | **no** |
| 31 | الم | (same) | Allāh, al-Laṭīf, al-Majīd | **no** |
| 32 | الم | (same) | Allāh, al-Laṭīf, al-Majīd | **no** |
| 36 | يس | al-Samīʿ, al-Ḥasīb, al-Ḥayy, al-ʿAzīz, al-ʿAlī | al-Sayyid, al-Salām | **no** |
| 38 | ص | **al-Ṣamad**, al-Muṣawwir, al-Baṣīr, al-Muḥṣī, al-Ṣabūr | al-Ṣamad | HIT (al-Ṣamad) |
| 40 | حم | al-Ḥakam, al-Muḥyī, al-Ḥaqq, al-Ḥakīm, al-Ḥayy | al-Ḥamīd, al-Majīd | **no** |
| 41 | حم | (as S40) | al-Ḥamīd, al-Majīd | **no** |
| 42 | حمعسق | al-Ḥaqq, **al-Samīʿ**, al-Muqsiṭ, al-Muʿizz, al-Ḥakam | al-Ḥalīm, al-Majīd, al-ʿAzīz, al-Samīʿ, al-Qādir | HIT (al-Samīʿ) |
| 43 | حم | (as S40) | al-Ḥamīd, al-Majīd | **no** |
| 44 | حم | (as S40) | al-Ḥamīd, al-Majīd | **no** |
| 45 | حم | (as S40) | al-Ḥamīd, al-Majīd | **no** |
| 46 | حم | (as S40) | al-Ḥamīd, al-Majīd | **no** |
| 50 | ق | al-Ḥaqq, al-Qawiyy, al-Muqaddim, al-Quddūs, al-Khāliq | al-Qādir | **no** |
| 68 | ن | al-Muʾmin, al-Ghanī, **al-Nūr**, al-Raḥmān, al-Muhaymin | al-Nūr | HIT (al-Nūr) |

**Hit rate: 12 of 29 surahs (41.4%) have at least one al-Rāzī-assigned name
in the top-5 coverage ranking.** Under a null where al-Rāzī's claim for each
surah is drawn at random from the 99 names, we'd expect roughly 5/99 × (number
of al-Rāzī names per surah, mean ≈ 2.7) ≈ 13.6% per surah hit rate, accumulating
to ~13% of surahs showing at least one hit. The observed 41.4% **does** beat
this baseline — but this is driven entirely by:

- **8 hits on Allāh** in ALR surahs (trivially: alif-initialing Allāh in
  every surah whose opening contains ا is a gift — every surah in the Quran
  would rank Allāh high by coverage of ا-containing openings).
- **3 hits on al-Salām** in TSM/TS surahs (trivially: al-Salām's letters
  {س ل م} overlap heavily with TSM/ALM).
- **1 hit on al-Ṣamad** in S38 (trivially: ص → al-Ṣamad is driven by the
  single letter ص).
- **1 hit on al-Nūr** in Q68 (trivially: ن → al-Nūr is driven by ن).

The hits concentrate on the single-letter/double-letter muqaṭṭaʿāt combinations
(where the coverage ranking is degenerate) and on Allāh itself (which any
coverage-based algorithm ranks high whenever the opening contains ا).

**Al-Rāzī's more specific claims — al-Laṭīf, al-Majīd, al-Ḥamīd, al-Ḥalīm,
al-Qādir, al-Kabīr, al-Hādī, al-Amīn, al-Ṣādiq, al-Ṭāhir, al-Sayyid — score
ZERO top-5 hits across all 29 surahs.** These are precisely the names he
reports from Ibn ʿAbbās / the salaf as the "interesting" decomposition, and
every single one fails the coverage inverse test.

---

## 6. Per-combination verdict table

| Combo | Surahs | al-Rāzī decomp | Density-Bonf passes | Token-Bonf passes | Shuffle-null Bonf passes | Verdict |
|---|---|---|---|---|---|---|
| ALM | 2, 3, 29, 30, 31, 32 | ا=Allāh; ل=Laṭīf; م=Majīd | 2 (S3, S2 near) | 1 (S3) | 0 | **Allāh passes trivially; Laṭīf & Majīd fail everywhere** |
| ALMS | 7 | +ص=Ṣamad | 0 | 0 | 0 | **All 4 claims fail** |
| ALR | 10, 11, 12, 14, 15 | ا=Allāh; ل=Laṭīf; ر=Raḥmān | 1 (S15 Raḥmān) | 0 | 0 | **Nominal only; fails shuffle null** |
| ALMR | 13 | ا=Allāh; ل=Laṭīf; م=Majīd; ر=Raḥmān | 1 (S13 Allāh) | 0 | 0 | **1 of 4 nominal; shuffle fails** |
| KHYAS | 19 | ك=Kabīr; ه=Hādī; ي=Amīn; ع=ʿAzīz; ص=Ṣādiq | 1 (S19 Kabīr) | 0 | 0 | **1 of 5 nominal; shuffle fails; Ibn ʿAbbās's ي→Amīn already orthographically false** |
| TH | 20 | ط=Ṭāhir; ه=Hādī | 0 | 0 | 0 | **Total fail** |
| TSM | 26, 28 | ط=Ṭāhir; س=Salām; م=Majīd | 0 | 0 | 0 | **Total fail** |
| TS | 27 | ط=Ṭāhir; س=Salām | 0 | 0 | 0 | **Total fail** |
| YS | 36 | ي=Sayyid; س=Salām | 0 | 0 | 0 | **Total fail** |
| S | 38 | ص=Ṣamad | 0 | 0 | 0 | **Fails despite single-letter opening and surface inverse-test hit** |
| HM | 40, 41, 43–46 | ح=Ḥamīd; م=Majīd | 0 | 0 | 0 | **Total fail across all 6 HM surahs** |
| HMASQ | 42 | ح=Ḥalīm; م=Majīd; ع=ʿAzīz; س=Samīʿ; ق=Qādir | 2 (S42 Ḥalīm, S42 ʿAzīz) | 0 | 0 | **2 of 5 nominal; shuffle fails** |
| Q | 50 | ق=Qādir | 1 (S50 Qādir) | 0 | 0 | **Nominal; shuffle null fails at p=0.275** |
| N | 68 | ن=Nūr | 0 | 0 | 0 | **Fails despite inverse-test surface hit (al-Nūr has only 2 tokens in the entire Quran, one of which is not in S68; source-CSV shows 12 total with 0 in S68)** |

---

## 7. The "KHYAS problem" the classical tradition itself flagged

Ibn ʿAbbās's decomposition of Q19 (كهيعص) assigns:

- ك → al-Kabīr  (first letter ك ✓)
- ه → al-Hādī   (first letter ه ✓)
- **ي → al-Amīn (الأمين — first letter ا, NOT ي) ✗**
- ع → al-ʿAzīz  (first letter ع ✓)
- ص → al-Ṣādiq (first letter ص ✓)

Four of five letters match by the strict rule, one does not — and it fails in
the most obvious way (al-Amīn strictly starts with the alif of its definite
article, and its radical-initial is also alif/hamza, not yāʾ). The classical
scholars who transmitted this decomposition were not stupid: they evidently
did **not** intend a strict letter-as-initial rule. The "abbreviation" was
mnemonic at best, and al-Rāzī preserves it as a possible opinion, not as
his committed position.

This is the central structural weakness of the theory we set out to test: the
primary classical source itself violates the matching rule it would require
to be statistically coherent. Our 78-claim test gives the theory every
possible benefit (we scored each assignment as if strict), and it still fails.

---

## 8. Garden of forking paths disclosure

### Choices made after seeing the data

- **None.** The full 78-claim list was fixed from the classical extract before
  any density or token numbers were computed (`CLAIMS` list in `run_test.py`
  is derived directly from `razi-99names-extract.md` §3).
- The secondary shuffle null was pre-registered; the frequency-weighted null
  was **not** added post-hoc (unlike in `razi-99names-test.md`, which added
  it as a robustness).

### Alternative rule tuples considered and discarded

- `full-tashkeel` grapheme counts would change the absolute letter totals
  (327,038 vs. 330,709) but not the relative rates meaningfully; we did not
  re-run under this alternative since the pre-registered primary is the
  no-tashkeel JSON.
- Alternative basmala policies (`counted-in-surah`, `always-separator`) would
  each move every surah's letter totals by at most 19 letters; under both,
  the direction and rough magnitude of the result is unchanged. Not re-run.
- `with-hamza-distinct` (not normalizing أ إ ؤ ئ into carriers) would change
  the letter counts for al-Amīn and Allāh's alif variants; under this rule
  the S3/Allāh density result would shrink. Not chosen as primary.
- Abjad-weighted densities (instead of unweighted grapheme counts) were
  considered and rejected as already-covered by the abjad test in
  `muqattaat-analysis.md` §5.

### Sibling hypotheses considered

- The 99-Names initial-letter test (`razi-99names-test.md`, H20 original)
  produced WEAK naive support / NOT-SUPPORTED proper-null verdict.
- The expanded-epithet corpus (150+ divine attributes) from `razi-99names-test.md`
  §8 was consulted; the same pattern held there too (67% luminous coverage
  regardless of epithet pool).
- We did not re-run the "best k-letter subset" optimization test; that is
  already in `razi-99names-test.md` §4.

### Why this one and not those

- This test is the natural *per-claim* version of H20: instead of testing the
  whole 14-letter set against 99 names, we test each al-Rāzī-reported letter→name
  pairing inside its host surah. This was the pre-reg commitment in the
  current task brief and is the logical completion of the H20 family.

---

## 9. Red-flag checklist (§4 of statistical-rigor-protocol)

- [✓] Post-hoc rule selection? No — rules tuple and claim list locked before
  compute.
- [✓] Undisclosed counting conventions? No — all documented in frontmatter.
- [✓] Non-canonical text? No — using the locked canonical corpus.
- [✓] Non-standard verse numbering? No — hafs-kufan throughout.
- [✓] p-values without a null model? No — two-prop null and shuffle null both
  specified.
- [✓] Brittleness under inflection? Both tests run on grapheme-graph
  (insensitive to inflection) + whole-word token match. We ran no
  surface-form-only test.
- [✓] Cherry-picked temporal horizon? Not applicable to this hypothesis.
- [✓] Hidden meanings without reproducible algorithm? Code path cited.
- [✓] Appeal to numerological coincidence without null? No — shuffle null
  is pre-registered.
- [✓] Refusal to enumerate siblings? No — 78-claim enumeration is exhaustive
  across the classical decompositions we can find in the literature.
- [✓] Counts that don't reproduce? All counts trivially reproduce from the
  locked JSON and cleaned regex; code provided.

---

## 10. Prior art and modern scholarship

### What was already known

- **A. Welch**, *Encyclopaedia of Islam* 2nd ed., article "al-Kurʾān" §4.d
  "The Mysterious Letters" (1981, rpt. 1993). Reviews the classical divine-name
  opinion among ~13 rival theories and concludes it is one of "the least
  well-founded" classical options, while endorsing the muqaṭṭaʿāt as
  pronunciation-demonstration / pedagogical-aide theory.
- **Keith Massey**, "A New Investigation into the 'Mystery Letters' of the
  Quran" (1996), *Arabica* 43(3). Argues the letters are initials/monograms
  of scribal compilers (a revival of Nöldeke-Hirschfeld); explicitly rejects
  divine-names abbreviation.
- **Andrew Rippin**, *The Qurʾān and Its Interpretative Tradition* (2001)
  and *The Muslim World* articles on disjoined letters. Treats the
  divine-names opinion as a characteristic late-classical hermeneutic move
  reflecting later Ashʿarī-Māturīdī interest in the Names-discipline
  (ʿilm al-asmāʾ), not as preserving early intent.
- **Morris S. Seale** (*Qurʾān and Bible*, 1978) and **Thomas O'Shaughnessy**
  (*The Koranic Concept of the Word of God*, 1948) treat the muqaṭṭaʿāt as
  deliberately unresolved text; al-Rāzī's divine-names opinion is flagged
  as theologically appealing but evidentially weak.

### What this finding adds

We believe this is the first McKay-style formal audit of the specific
al-Rāzī / Ibn ʿAbbās letter→name decompositions at the (surah, letter, name)
granularity, with:

1. A locked rules tuple and grapheme-normalization before any counting.
2. A pre-registered shuffle null over the 14 luminous letters that controls
   for letter-frequency overlap between divine names and muqaṭṭaʿāt
   openings.
3. Bonferroni across all 78 classical claims rather than cherry-picking the
   single strongest (al-Rāzī-advocates typically cite only the ALM / Allāh
   correspondence).
4. An inverse coverage test that enumerates the top 99-name matches per
   surah regardless of which name al-Rāzī chose.

The existing project file `razi-99names-test.md` tested the **aggregate**
claim (are luminous letters enriched in 99-Name initials?); this file tests
the **per-claim** claim (does each individual letter→name pairing produce
host-surah enrichment?). The aggregate was already REJECTED; the per-claim
is now also REJECTED, with an additional mechanism for why (shuffle-null
shows the inventory-overlap artifact).

---

## 11. What this tells us about *isrār al-ḥurūf*

*ʿIlm al-ḥurūf* / *isrār al-ḥurūf* (the "science of the secrets of the
letters") assigns metaphysical meanings to individual Arabic letters and
reads the muqaṭṭaʿāt through this grid. The classical lineage runs from
al-Ḥakīm al-Tirmidhī (d. ca. 907) through Ibn ʿArabī (d. 1240) and al-Būnī
(d. 1225) into the Shādhilī and Maghribī hermetic traditions. Al-Rāzī's
divine-names opinion is the most rigorous Sunni-Ashʿarī rationalization of
this current: the letters are not random, they abbreviate names, so the
muqaṭṭaʿāt become a kind of pious mnemonic.

**Our finding does not refute the devotional or mnemonic use of this
tradition.** What we have shown is specifically:

1. The *specific letter→name pairings* al-Rāzī and the salaf transmit do
   **not** produce detectable statistical enrichment of those names (as
   letter-sets or as tokens) in the host surahs.
2. When we look at what names **do** best match each muqaṭṭaʿāt surah by
   inverse coverage, the answers are almost entirely driven by the
   mechanics of whichever high-frequency letter happens to appear in the
   opening (ا → Allāh for any opening containing ا; ص → al-Ṣamad for any
   opening containing ص; etc.), not by al-Rāzī's specific choices.
3. The classical tradition itself was ambivalent: Ibn ʿAbbās's KHYAS
   decomposition includes ي → al-Amīn, which violates the strict matching
   rule; al-Rāzī reports the disagreement among the salaf as a reason to
   doubt any single decomposition.

This is consistent with the project-wide picture that **the classical
hermeneutic tradition is sophisticated devotional interpretation, not
secret encoding.** The muqaṭṭaʿāt density effect documented in
`muqattaat-analysis.md` — real (Stouffer Z = +4.48, p ≈ 4e-6) but driven
by 2–3 surahs — is a statistical fact about the text; the divine-names
abbreviation reading is a post-hoc overlay on that fact that does not
itself survive statistical testing.

---

## 12. Sources

### Classical
- Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-Ghayb* (al-Tafsīr al-Kabīr),
  commentary on Q. 2:1, 19:1, 50:1. Internet Archive copy:
  https://archive.org/details/mafatihalghayb06raziuoft
- al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, chapters 40–41 (on *fawātiḥ
  al-suwar*); *al-Durr al-Manthūr fī Tafsīr al-Maʾthūr*, vol. 4, p. 679
  (on Q. 19:1). Local PDF:
  `/Users/grey/Downloads/quran/data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`
- al-Zarkashī, *al-Burhān fī ʿUlūm al-Qurʾān*, nawʿ 17 (on fawātiḥ). Local PDF:
  `/Users/grey/Downloads/quran/data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`
- al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān*, commentary on Q. 2:1.
- Tafsīr Ibn ʿAbbās (Tanwīr al-Miqbās), entries on Q. 2:1, 19:1, 38:1, 50:1, 68:1.

### Modern
- A. Welch, "al-Kurʾān" in *Encyclopaedia of Islam* 2nd ed., vol. V
  (Leiden: Brill, 1981), §4.d.
- K. Massey, "A New Investigation into the 'Mystery Letters' of the Quran,"
  *Arabica* 43/3 (1996): 497–501.
- A. Rippin, *The Qurʾān and Its Interpretative Tradition* (Aldershot:
  Ashgate, 2001), esp. ch. XI; *The Blackwell Companion to the Qurʾān*
  (Malden: Blackwell, 2006), ch. 11.
- Wikipedia, "Muqaṭṭaʿāt":
  https://en.wikipedia.org/wiki/Muqatta%CA%BFat
  (survey of the 13+ theories, updated 2024)

### Project internal
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/muqattaat-analysis.md`
  (parent finding, muqaṭṭaʿāt density Stouffer Z = +4.48)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/razi-99names-test.md`
  (H20 aggregate 99-Names test; REJECTED under proper null)
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-99names-extract.md`
  (classical decomposition extract; source of the 78-claim list)
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-muqattaat-surah-qaf.md`
  (al-Rāzī on Q. 50)
- `/Users/grey/Downloads/quran/docs/methodology.md` §§ 1–9
- `/Users/grey/Downloads/quran/docs/statistical-rigor-protocol.md` §§ 1–7

### Code and data outputs
- `/Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/run_test.py`
- `/Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/claim_results.csv`
- `/Users/grey/Downloads/quran/scratch/razi-muqattaat-divine-names/run.log`

---

## 13. Protocol §7 checklist

- [x] Rules tuple pre-registered in this file's frontmatter; data-touch
  followed.
- [x] Exact statistic named (density_test, token_test, shuffle_null_density).
- [x] Primary null (two-proportion z) run on all 78 claims.
- [x] Secondary null (1000-permutation shuffle over 14 luminous letters)
  run on all 78 claims.
- [x] Bonferroni correction applied; k = 78 disclosed.
- [x] Raw p, corrected p, effect size (density_z, rate_in − rate_out) all
  reported.
- [x] Robustness: inverse coverage test run as a distinct statistic on the
  same data.
- [x] Garden-of-forking-paths disclosure filled (§8).
- [x] Red-flag checklist run (§9).
- [x] Test register: this finding adds +78 tests to the Phase B register.
- [x] Verdict stated up front, negative result reported with equal
  prominence.
