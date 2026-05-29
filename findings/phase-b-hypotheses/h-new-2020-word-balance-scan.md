---
id: H-NEW-2020
title: Exhaustive surface-word exact-frequency balance scan + curated antonym-pair audit
phase: B
date_run: 2026-05-29
seed: 20260509
n_perm: 10000
prereg_sha256: bfeb1abb9d68ba5448236b0833a0b4c9beeb3f6cfa1a5eb6c934806c370a5083
verdict: MIXED — H1 PASS-DIRECTED (1/13 balance, ≤6 threshold), H2 PASS-DIRECTED (dunyā≠ākhira strict ⇒ "115=115" legend FALSIFIED), H3 REVERSAL-published (z=+20.2, Quran is MORE collision-prone than the Zipf reference, not indistinguishable)
ceiling: descriptive cataloguing + classical-claim audit; per-pair verdicts are sharp integer-equality
direction: locked pre-observation (H1 ≤6-of-13; H2 ≠; H3 |z|<2)
related: H-NEW-2010 (root-based sibling generator), H-NEW-1530 (Khalifa-19 audit), H-NEW-1800 (99-names), H-META-1 (numerical-gematric confirmation rate)
---

# H-NEW-2020 — Surface-word exact-frequency balance: the curated antonym audit

## Headline

Of **13** famous antonym / complementary word-pairs — the kind paraded in
modern "numerical iʿjāz" literature as evidence of a divinely-engineered lexical
balance — **exactly 1 balances** under either a strict-word rule or a maximally
permissive all-surface-forms rule. That one is **ṣayf / shitāʾ** (summer/winter),
each occurring once, and only because both words appear together in the single
verse Q 106:2 (*riḥlata al-shitāʾi wa-l-ṣayf*). The flagship claim that gave the
genre its fame — *al-dunyā* and *al-ākhira* each occur **115** times — is
**FALSIFIED at the surface-word level**: `الدنيا` occurs **115** times (a real
corpus fact) but the strict standalone `الآخرة` occurs **71** times. No summation
of ākhira's surface forms lands on 115 either (the broad conflation of
hereafter+last+other gives 194).

The exhaustive scan reframes the whole enterprise: the corpus contains
**3,734,882** content-word pairs that balance *exactly*, including such
evocative coincidences as *al-Qurʾān* = *yahdī* (43 each), *Ibrāhīm* = *aṣḥāb*
(62 each), and — with delicious irony — *al-ākhira* = *yaʿlam* "He knows" (71
each). Any single "balanced pair" is a draw from this ocean. Exact integer
balance is not a signal; it is the **default state** of a 14,870-type vocabulary
whose counts are crammed into a short ladder of small integers.

## Pre-registration

- File: `findings/phase-b-hypotheses/prereg-h-new-2020-word-balance-scan.md`
- SHA256: `bfeb1abb9d68ba5448236b0833a0b4c9beeb3f6cfa1a5eb6c934806c370a5083`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2020.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-2020.json`
- Rules-tuple: `(no-tashkeel, orthographic-token, words, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`; tokenisation strips Qurʾānic recitation marks U+06D4..U+06ED → **77,797** tokens, **14,870** distinct types.

## The two counting rules

- **Rule S (strict-word)**: the single canonical surface form per concept
  (usually the *al-* definite form, which is what the famous claims actually
  count). No prefixed / inflected variants summed.
- **Rule F (all-surface-forms)**: sum a closed, pre-locked allow-list of surface
  variants per concept, hand-pruned for homographs. This is the permissive
  upper-bound short of going to the root (the root version is the sibling
  H-NEW-2010). For the antonym sides built on nouns I locked the *noun* layer on
  both sides for parity (excluding the verbal family) — see Honest Limits.

## Curated-pair verdict table

| # | Pair | S: A | S: B | S balanced? | F: A | F: B | F balanced? | Balanced under any rule? |
|--:|:--|--:|--:|:--:|--:|--:|:--:|:--:|
| 1 | dunyā / ākhira (hereafter) | الدنيا **115** | الآخرة **71** | ✗ | 115 | 194 | ✗ | **✗** |
| 2 | jannah / nār | الجنة 56 | النار 102 | ✗ | 151 | 145 | ✗ (off by 6) | **✗** |
| 3 | jannah / jahannam | الجنة 56 | جهنم 72 | ✗ | 151 | 77 | ✗ | **✗** |
| 4 | malāʾika / shayāṭīn(pl) | الملائكة 38 | الشياطين 13 | ✗ | 73 | 18 | ✗ | **✗** |
| 5 | ḥayāt / mawt (noun) | الحياة 63 | الموت 35 | ✗ | 76 | 50 | ✗ | **✗** |
| 6 | khayr / sharr | خير 116 | شر 15 | ✗ | 188 | 44 | ✗ | **✗** |
| 7 | īmān / kufr (noun) | الإيمان 7 | الكفر 11 | ✗ | 45 | 56 | ✗ | **✗** |
| 8 | hudā / ḍalāl (noun) | الهدى 22 | الضلال 3 | ✗ | 92 | 45 | ✗ | **✗** |
| 9 | nūr / ẓulumāt(pl) | النور 10 | الظلمات 14 | ✗ | 43 | 23 | ✗ | **✗** |
| 10 | **ṣayf / shitāʾ** | الصيف 0 | الشتاء 1 | ✗ | **1** | **1** | **✓** | **✓** |
| 11 | ḥarr / bard | الحر 3 | البرد 0 | ✗ | 5 | 4 | ✗ (off by 1) | **✗** |
| 12 | rajul / nisāʾ | الرجل 0 | النساء 24 | ✗ | 57 | 46 | ✗ | **✗** |
| 13 | qul / qālū | قل 294 | قالوا 250 | ✗ | 333 | 332 | ✗ (off by 1) | **✗** |

**Balanced under any rule: 1 / 13.** Pre-locked H1 threshold was ≤ 6.

## Hypothesis decisions (pre-locked)

| Hypothesis | Pre-locked direction | Observed | Decision |
|:--|:--|:--|:--|
| H1: curated pairs balancing ≤ 6 of 13 | ≤ 6 | **1** | **PASS-DIRECTED** |
| H2: dunyā ≠ ākhira (strict) | unequal | 115 ≠ 71 | **PASS-DIRECTED** (legend FALSIFIED) |
| H3: balance is generic, \|z\| < 2 vs Zipf | \|z\| < 2 | z = **+20.17** | **REVERSAL — published with full prominence** |

## H3 — the pre-commit violation, published honestly (Protocol §1.8)

I pre-locked H3 as "the Quran's fraction of content-word types sharing their
count with another type (`frac_types_in_collision`) is statistically
**indistinguishable** from a size-matched Zipfian reference (|z| < 2)." The
observed value is `frac_types_in_collision = 0.994` against a Zipf-reference
mean of `0.977 ± 0.001`, giving **z = +20.17**. This **breaches** the pre-locked
band. Per Protocol §1.8 I do **not** massage it.

Crucially, the breach is in the *pro-genericity* direction: the Quran's
vocabulary is even **more** collision-saturated than a clean Zipf curve, not
less. (The Zipfian reference spreads a little more probability into its long
unique-count tail; the Quran's empirical counts are packed even more tightly
into the low-integer ladder — 2,397 distinct content words occur exactly twice,
1,008 occur exactly three times, and so on.) So while the *letter* of the
pre-registered band is violated, the *spirit* — that exact balance is generic
and carries no signal — is reinforced, not overturned. The honest label remains:
**REVERSAL on the locked band; finding direction (balance is generic) intact and
strengthened.** It is recorded as a reversal, not silently rewritten.

## Exhaustive scan — exact balance is the default, not a miracle

After removing a closed particle stop-list, tokens of length ≤ 2, and the 8,709
hapax forms (count = 1), **5,999** content-word types with count ≥ 2 remain.
Grouped by their integer count:

| occurs N× | distinct words sharing that count | "balanced pairs" at that count |
|--:|--:|--:|
| 2 | 2,397 | 2,871,606 |
| 3 | 1,008 | 507,528 |
| 4 | 611 | 186,355 |
| 5 | 400 | 79,800 |
| 6 | 285 | 40,470 |
| 7 | 191 | 18,145 |
| 8 | 127 | 8,001 |
| 9 | 116 | 6,670 |
| 10 | 99 | 4,851 |

Total exact-balanced unordered content-word pairs: **3,734,882.**

The script also surfaces, at random, "famous-looking" balanced pairs to make the
cherry-picking concrete:

- *al-Qurʾān* (القرآن) = *yahdī* (يهدي) — 43 each
- *Ibrāhīm* (إبراهيم) = *aṣḥāb* (أصحاب) — 62 each
- *al-ākhira* (الآخرة) = *yaʿlam* (يعلم) "He knows" — 71 each
- *ghafūr* (غفور) = *alīm* (أليم) — 52 each
- *al-nār* (النار) = *rabbakum* (ربكم) — 102 each
- *al-yawm* (اليوم) = *bi-ghayr* (بغير) — 41 each

Each of these could be dressed up as a "remarkable thematic balance" with a
little homiletic effort. They are not. They are the inevitable consequence of
packing ~6,000 words onto a short ladder of small integers.

## Most-surprising near-misses

Three antonym pairs miss exact balance by the smallest possible margin and are
worth flagging precisely because they are the pairs a selective compiler would
be most tempted to round:

- **qul / qālū** — under Rule F (imperative *qul* + wa/fa-prefixed = **333**;
  *qālū* + prefixed = **332**) the two are off by exactly **one**. A single
  token decides it.
- **jannah / nār** — under Rule F (paradise-sense **151** vs fire-sense **145**)
  off by **six**.
- **ḥarr / bard** — under Rule F (**5** vs **4**) off by **one**.

These near-misses are themselves evidence *against* design: a deliberately
balanced lexicon would not stop one short.

## Classical / iʿjāz context

The "balanced-word" thesis is associated with ʿAbd al-Razzāq Nawfal's
*al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm* (1980s) and the popular dunyā=ākhira=115
claim circulated widely thereafter. It belongs to the modern-numerology era,
whose project-internal track record is poor: H-META-1 records a 0% (0/10)
confirmation rate for modern-numerology claims, versus 72% for structural-formal
claims. This finding is consistent: the surface-word balance thesis survives
only by per-pair selection of which pairs to advertise and which counting rule
to apply, exactly the selection-bias critique levelled at al-Khalifa's "Code 19"
by Bilāl Philips (*Qur'an's Numerical Miracle: Hoax and Heresy*, 1987) and
audited in H-NEW-1530. The classical ʿulūm al-Qurʾān tradition (al-Suyūṭī,
*al-Itqān*, nawʿ 17–19 on ʿadad al-suwar wa-l-āyāt wa-l-kalimāt) counts words and
verses but does **not** advance antonym-balance as iʿjāz — that is a 20th-century
overlay.

## Honest limits

1. **Hand-built form-lists.** The Rule-F allow-lists were assembled by substring
   inspection and pruned for homographs by hand, then pre-locked. A different
   analyst could draw slightly different boundaries; the per-pair `note` field in
   the JSON records every contested form. This discretion is the *point*: the
   famous claims live or die on exactly these boundary choices, and making the
   boundary explicit is what converts an anecdote into an audit.
2. **Noun-vs-verb parity.** For ḥayāt/mawt, īmān/kufr, hudā/ḍalāl, nūr/ẓulumāt I
   locked the *noun* layer on both sides (excluding the verbal families) so the
   two arms of each antonym are comparable. A defensible alternative (verbs
   included on both sides) would shift the counts but not the verdict — none of
   these pairs is within striking distance of balance under either choice except
   where already noted.
3. **dunyā=ākhira=115.** `الدنيا` genuinely is 115. The legend's *coincidence*
   only materialises if ākhira's forms are summed in an undisclosed way that
   happens to reach 115; no pre-locked summation here does so. The finding
   exposes the dependency rather than asserting a miracle.
4. **H3 reference model.** The Zipf/geometric reference is one defensible null;
   it was pre-locked as the single H3 test. The breach (z=+20) is reported as a
   reversal. The deeper claim — that exact integer-count balance is generic in
   *any* large word-frequency table — is close to a mathematical certainty, and
   the Zipf comparison only quantifies how strongly the Quran exhibits the
   generic property.
5. **What this does NOT claim.** It does not claim the Quran's vocabulary is
   *random* or unstructured (it is highly structured at the root, rhyme, and
   content-cohesion levels established elsewhere in this project). It claims only
   that *surface-word exact-frequency balance between antonym pairs* is not a
   real architectural feature: it is selective storytelling over a generic
   statistical substrate.

## Bottom line

The surface-word candidate-pattern generator confirms its sibling-root
expectation: **1 of 13** advertised antonym balances survives, and that one
(ṣayf/shitāʾ) is a trivial co-occurrence in a single verse. The flagship
dunyā=ākhira=115 is false at the strict surface level. And against a backdrop of
**3.7 million** equally-exact balanced content-word pairs, no individual balance
can carry evidential weight without an a-priori, pre-registered reason to single
that pair out — which the iʿjāz literature does not supply.

*Run 2026-05-29 by Waiel Al-Shujaa. Directions locked pre-observation; H3
reversal published with full prominence per Protocol §1.8. Bismillāhi
al-Raḥmāni al-Raḥīm.*
