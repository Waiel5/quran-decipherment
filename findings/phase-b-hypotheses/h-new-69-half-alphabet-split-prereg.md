---
id: H-NEW-69
title: Half-alphabet split — does the muqaṭṭaʿāt-set match a classical 14-of-28 grouping?
status: PRE-REGISTERED (decisions locked BEFORE running)
registered: 2026-04-15
spec_locked_at: 2026-04-15
agent: h-new-69-specialist
parent: H-NEW-44.2 (POA-class NULL); H-NEW-44.2.1 (pharyngeal/glottal PASS-DIRECTED); H-NEW-60 (dotless STRONG-PASS)
bonferroni_family: 2026-04-15-Wave-Half-Alphabet
bonferroni_k: 8 (groupings tested; see §4)
alpha_family: 0.05
alpha_per_grouping: 0.00625 (= 0.05 / 8, two-sided exact hypergeometric)
seed: 20260415
rules_tuple: (28-letter Arabic orthographic alphabet, classical Sibawayh/al-Khalīl phonological classifications, hamza folded into alif)
primary_corpus: quran-text/quran-no-tashkeel.json (NOT consulted in this test — universe is the 28-letter alphabet itself)
---

# [[h-new-69-half-alphabet-split|H-NEW-69]] — Half-Alphabet Split: muqaṭṭaʿāt vs Classical 14-of-28 Groupings

## 1. Fixed prior fact

The 14 muqaṭṭaʿāt letters are exactly half the 28-letter Arabic alphabet:

```
U_muq = {ا, ح, ر, س, ص, ط, ع, ق, ك, ل, م, ن, ه, ي}        (|U_muq| = 14)
U_non = {ب, ت, ث, ج, خ, د, ذ, ز, ش, ض, ظ, غ, ف, و}        (|U_non| = 14)
```

Several Arabic phonological / orthographic classifications in classical Arabic
also produce 14-of-28 splits — most famously the shamsiyyah/qamariyyah
divide on whether the lām of the definite article assimilates. This
"exactly 14 vs 14" coincidence is suspicious. The question: does the
muqaṭṭaʿāt-set MATCH any such classical split, or is the half-cut
phonologically arbitrary?

## 2. Question

For each classical grouping G of size |G| = 14 (or where the natural
complement is 14), compute the overlap |U_muq ∩ G| and test under the
null `H0: U_muq is a uniform random 14-of-28 subset` whether the overlap
is significantly higher (or lower) than expected.

## 3. Classical groupings — LOCKED before viewing overlap

All groupings are taken from standard classical Arabic
phonology / morphology references (Sibawayh, al-Khalīl, al-Zamakhsharī,
al-Mubarrad). The classifications are well-established; the EXACT letter
membership is locked here.

### 3.1 Primary 14-of-28 groupings

#### G1 — shamsiyyah (sun letters, 14)

Letters that ASSIMILATE the lām of al-: ال + shamsiyyah → al- + doubled
consonant (e.g., al-shams /aʃ-ʃams/). Per al-Zamakhsharī (al-Mufaṣṣal §82),
Sibawayh (al-Kitāb IV ch. 567), and universal classical agreement:

```
G1 = {ت, ث, د, ذ, ر, ز, س, ش, ص, ض, ط, ظ, ل, ن}        (14 letters)
```

Articulation rationale: all 14 are coronal/dental/alveolar — articulated
where the tip of the tongue can transition smoothly from the lām position.

#### G2 — qamariyyah (moon letters, 14)

Complement of shamsiyyah. Letters that DO NOT assimilate (al-qamar /al-qamar/):

```
G2 = {ا, ب, ج, ح, خ, ع, غ, ف, ق, ك, م, ه, و, ي}        (14 letters)
```

Articulation rationale: pharyngeal, velar, uvular, labial — articulated
remote from the lām position; assimilation phonotactically blocked.

NOTE: G1 and G2 are exact complements; their tests are MIRROR IMAGES.
We treat them as a single 1-test pair (overlap with G1 determines overlap
with G2 deterministically) but report both for transparency.

### 3.2 Sibawayh majhūra/mahmūsa (voiced/voiceless)

Sibawayh's classification (al-Kitāb IV ch. 565) divides Arabic phonemes
into majhūra (voiced) and mahmūsa (voiceless) by whether the larynx is
"closed" (vibrating vocal folds) or "open" (no vibration). By Sibawayh's
exact letter assignment (which differs slightly from modern phonetic
voicing — notably the inclusion of the historically-glottalized "majhūra"
ṭ, q, hamza):

#### G3 — majhūra (voiced per Sibawayh, 19)

```
G3 = {ء, ا, ب, ج, د, ذ, ر, ز, ض, ط, ظ, ع, غ, ق, ل, م, ن, و, ي}
   = {ا, ب, ج, د, ذ, ر, ز, ض, ط, ظ, ع, غ, ق, ل, م, ن, و, ي}  (after folding ء→ا, 18 letters)
```

(Sibawayh counts hamza as separate; we follow the 28-letter orthographic
convention from [[h-new-44-2-poa-closure|H-NEW-44.2]] where hamza folds into alif. Net |G3| = 18.)

#### G4 — mahmūsa (voiceless per Sibawayh, 10)

```
G4 = {ت, ث, ح, خ, س, ش, ص, ف, ك, ه}        (10 letters)
```

|G3| + |G4| = 18 + 10 = 28. ✓ Exhaustive, mutually exclusive.

NOTE: Neither G3 (18) nor G4 (10) is exactly 14. They are NEAR-14 but not
half-splits. Under hypergeometric testing this is not a problem — the
expected overlap with U_muq scales with |G_i|: E[k_i] = 14 × |G_i| / 28.
We include both as part of the locked-grouping family.

### 3.3 Modern phonetic voicing (alternative classification)

Modern phoneticians (Bakalla 1984; Versteegh 1997) classify Arabic by
acoustic voicing (laryngeal vibration during the consonant). This differs
from Sibawayh's classification in that ṭ, q, ʔ are voiceless in modern
phonetics:

#### G5 — modern-voiced (~13)

```
G5 = {ب, ج, د, ذ, ر, ز, ض, ظ, ع, غ, ل, م, ن, و, ي}        (15 letters)
```

#### G6 — modern-voiceless (~13)

```
G6 = {ا, ت, ث, ح, خ, س, ش, ص, ط, ف, ق, ك, ه}              (13 letters)
```

|G5| + |G6| = 15 + 13 = 28. ✓ (G5 includes alif as not-clearly-voiced-or-voiceless;
we lock it to G5 because alif is functionally a vowel-bearer and
phonologically neutral; this matches Watson 2002 *Phonology and Morphology
of Arabic* p. 17.)

This is INTENTIONALLY tested as ALTERNATIVE to G3/G4 — if Sibawayh's
classification differs from modern phonetic voicing, the muqaṭṭaʿāt
might match one but not the other.

### 3.4 ḥurūf al-ṣafīr (sibilants, 3)

Per Sibawayh / al-Khalīl: the three sibilant letters making the "whistle"
sound:

#### G7 — ṣafīr (3 letters)

```
G7 = {ز, س, ص}        (3 letters)
```

Test is hypergeometric over a small class — same procedure as [[h-new-44-2-poa-closure|H-NEW-44.2]].1.

### 3.5 ḥurūf al-iṭbāq (mufakhkhama / emphatic, 4)

Pharyngealized / velarized "heavy" letters per Sibawayh and al-Mubarrad:

#### G8 — iṭbāq (4 emphatic letters)

```
G8 = {ص, ض, ط, ظ}        (4 letters)
```

NOTE: distinct from "musta'liya" which adds {خ, غ, ق} — we lock to the
4-letter strict iṭbāq class, the most rigorously defined emphatic set.

### 3.6 Locked grouping count

We test 8 groupings in the family:
- G1 shamsiyyah (14)
- G2 qamariyyah (14)        [mirror of G1 — but report independently]
- G3 majhūra-Sibawayh (18)
- G4 mahmūsa-Sibawayh (10)
- G5 modern-voiced (15)
- G6 modern-voiceless (13)
- G7 ṣafīr (3)
- G8 iṭbāq (4)

Bonferroni `k_bonf = 8`. α_per_grouping = 0.05 / 8 = 0.00625.

(G1 and G2 are mathematically equivalent under the hypergeometric test
since k_2 = 14 - k_1 deterministically, but we count them both in the
Bonferroni family for transparency about WHICH groupings were inspected.
The Bonferroni count is intentionally CONSERVATIVE.)

## 4. Test — exact hypergeometric per grouping

For each grouping G with size |G| = c, observed overlap k = |U_muq ∩ G|:

Under H0: U_muq is a uniform 14-element subset of the 28-letter alphabet,
the count k is hypergeometric(N=28, K=c, n=14):

```
P(k_obs = k) = C(c, k) × C(28-c, 14-k) / C(28, 14)
```

Per-grouping reported quantities:
- Observed k
- Expected E[k] = 14 × c / 28 = c / 2
- Jaccard overlap = |U_muq ∩ G| / |U_muq ∪ G|
- One-sided enrichment p = P(K ≥ k_obs)
- One-sided depletion p = P(K ≤ k_obs)
- Two-sided exact p = `min(2 × min(p_enrich, p_deplete), 1.0)` (doubled-smaller-tail)

Best-matching grouping = grouping with smallest two-sided p (ties broken
by lexicographic order G1 < G2 < ... < G8).

## 5. MW-5 positive control (planted-signal pipeline check)

Construct synthetic muqaṭṭaʿāt-set `U_planted = G1` (sun letters
exactly). Expected behavior: hypergeometric P(k=14 | N=28, K=14, n=14)
= 1/C(28,14) = 1/40,116,600 = 2.49e-8 — extreme enrichment (p ≈ 5e-8
two-sided after doubling). Test pipeline must report G1 with p < 1e-7
on this planted signal.

If pipeline fails to detect, NULL-BROKEN.

A second MW-5b planted signal: `U_planted_v2 = G1 with 1 swap`
(swap one sun letter ت → one moon letter ك): k_obs = 13 vs c=14, p =
P(K≥13 | N=28, K=14, n=14) + P(K≤1 | N=28, K=14, n=14) =
2 × 14 × 14 / 40116600 = 1.96e-5 × 2 = 9.78e-6 (also extreme). Pipeline
must detect at p < 0.001.

## 6. MW-7 internal-error gate

Before writing verdict:
- All 8 p-values must be in [0, 1]
- Sum of "letters covered by all 8 groupings" should reproduce 28
- All 14 muqaṭṭaʿāt letters present in alphabet universe
- Hypergeometric closed-form result reproducible to 6 decimal places

If any check fails → NULL-BROKEN, no verdict.

## 7. Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| ≥1 grouping significant after Bonferroni-8 (p < 0.00625) AND classical interpretation aligns | STRONG-PASS — muqaṭṭaʿāt MATCH classical grouping |
| ≥1 grouping significant after Bonferroni-8 but interpretation ambiguous | PASS — match identified, mechanism speculative |
| ≥1 grouping significant at unprotected α=0.05 only | PASS-DIRECTED (single-test, requires replication) |
| 0 groupings significant at unprotected α=0.05 | NULL — muqaṭṭaʿāt do not match any tested classical grouping |
| Positive control fails | NULL-BROKEN |

## 8. Phonotactic combinatorial side-test (auxiliary, NOT Bonferroni-counted)

After the primary 8-grouping test, we report a phonotactic descriptive
analysis of U_muq vs U_non as a class:

(a) **Coronal density**: count of coronal letters in each set
(coronal = {ت,ث,د,ذ,ر,ز,س,ش,ص,ض,ط,ظ,ل,ن} = 14 — these are exactly the
shamsiyyah G1; coverage is determined by the G1 test).

(b) **Sonorant count**: {ر, ل, م, ن, و, ي} = 6 sonorants in alphabet —
how many in U_muq vs U_non.

(c) **Stop count**: {ب, ت, د, ط, ك, ق, ء/ا} → in U_muq vs U_non.

(d) **Fricative count**: {ث, ح, خ, ذ, ز, س, ش, ص, ض, ظ, ع, غ, ف, ه} (14
fricatives) — in U_muq vs U_non.

These are reported as DESCRIPTIVE FACTS only; if any pattern appears
striking, it would require its own pre-reg.

## 9. Garden-of-forking-paths log (pre-run, BEFORE seeing data)

Decisions made BEFORE viewing overlap counts:

1. Primary alphabet = 28-letter orthographic (alif first, yāʾ last;
   hamza folded into alif). LOCKED.
2. 8 groupings as enumerated in §3. NO post-hoc addition / removal.
3. Bonferroni `k_bonf = 8`. NO post-hoc reweighting.
4. Two-sided test via doubled-smaller-tail. LOCKED.
5. Best-matching = smallest two-sided p; tie-break = lexicographic.
   LOCKED.
6. Phonotactic side-test (§8) is DESCRIPTIVE only — NOT a verdict input.
7. Sibawayh's majhūra-classification source = al-Kitāb IV ch. 565.
   Modern voicing source = Watson 2002. Both LOCKED before run.
8. ḥurūf al-iṭbāq strict 4-letter set (not 7-letter musta'liya).
   LOCKED.
9. ḥurūf al-zalāqa (6) and ḥurūf al-iṣmāt (22) are NOT in the family —
   they are not 14-of-28 splits and adding them would inflate Bonferroni
   without information gain on the half-alphabet question. EXCLUDED.
10. Sun/moon letters: standard al-Zamakhsharī al-Mufaṣṣal listing.
    LOCKED.

## 10. Prior art / classical anchoring

- **al-Zamakhsharī**, *al-Mufaṣṣal fī ʿilm al-ʿarabiyya*, ed. Jens Peter
  Broch (1879), §82 "fī al-lām al-shamsiyya wa-l-qamariyya" — the
  canonical 14-of-14 sun/moon split.
- **Sibawayh**, *al-Kitāb*, ed. ʿAbd al-Salām Hārūn (1988), vol. IV
  ch. 565 "fī ʿadd al-ḥurūf wa-makhārijihā wa-ṣifātihā" — POA + voicing
  classifications.
- **al-Khalīl b. Aḥmad**, *Kitāb al-ʿAyn*, ed. al-Makhzūmī &
  al-Sāmarrāʾī, vol. I introduction — 8 makhraj scheme, ḥurūf al-ṣafīr,
  iṭbāq.
- **Watson, J. C. E.** (2002) *The Phonology and Morphology of Arabic*,
  OUP — modern phonetic voicing reference.
- **Bakalla, M. H.** (1984) *Arabic Linguistics: An Introduction and
  Bibliography*, Mansell — classical/modern POA/voicing comparison.
- **No prior source we can locate has tested whether the muqaṭṭaʿāt-set
  matches the shamsiyyah/qamariyyah split**, even though this is
  arguably the most natural Arabic 14-of-28 partition. This pre-reg
  fills that gap.

## 11. Integrity commitment

- Publish ALL 8 per-grouping p-values regardless of significance.
- Publish Jaccard overlap, exact k vs E[k], one-sided + two-sided p,
  significance flag at α = 0.00625.
- Publish phonotactic side-test descriptors regardless.
- Publish MW-5 + MW-5b positive controls.
- If any decision (1)-(10) is amended after viewing data, the amendment
  is logged + the original-spec verdict is also published.
- Closed-form analytic test; no random seed needed for the primary 8-grouping
  test. Seed 20260415 reserved for any sampling MW checks.

## 12. Reproducibility

Script: `scripts/h_new_69_half_alphabet_split.py`
JSON output: `findings/phase-b-hypotheses/csv/h-new-69.json`
Findings: `findings/phase-b-hypotheses/h-new-69-half-alphabet-split.md`
Journal: `journal/h-new-69-run-1.md`

Closed-form hypergeometric — runtime expected < 5 seconds.
