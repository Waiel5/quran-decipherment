---
id: H-NEW-54
title: Extended Root-Enrichment Scan — 4/10 Revelation-Theme Roots Significantly Enriched in Muqaṭṭaʿāt-Opened Surahs (v1-3)
phase: B
status: PASS-BROAD-FIELD
date: 2026-04-15
agent: h-new-54-specialist
test: hypergeometric two-sided per root, Bonferroni-10
parent: H-NEW-53 (kitāb/qurʾān combined p ≈ 3.17 × 10⁻¹²)
verdict: PASS-BROAD-FIELD (4/10 roots significant after Bonferroni)
rules_tuple: (no-tashkeel; substring/token search on v1-3; surface forms locked in pre-reg)
---

# [[h-new-54-extended-root-enrichment|H-NEW-54]] — Extended Root-Enrichment Scan (RESULT)

## Headline

**4 of 10 pre-registered revelation-theme roots are significantly enriched in muqaṭṭaʿāt-opened surahs' opening 3 verses, surviving Bonferroni-10 correction (α_per = 0.005).**

The enrichment is NOT confined to kitāb/qurʾān: it extends to **āyāt** (signs/verses) and **nazala** (sent down) — the broader semantic field of "written/sent revelation."

| Root | Label | obs/29 | K/114 | E[X] | p (two-sided) | p × 10 (Bonf) | Verdict |
|---|---|---|---|---|---|---|---|
| **k-t-b** | kitāb (book) | **20** | 28 | 7.12 | **2.93 × 10⁻⁹** | 2.93 × 10⁻⁸ | **PASS** |
| **q-r-ʾ** | qurʾān (recite) | **9** | 11 | 2.80 | **1.17 × 10⁻⁴** | 1.17 × 10⁻³ | **PASS** |
| **ʾ-y-ā** | āyāt (signs) | **11** | 16 | 4.07 | **1.93 × 10⁻⁴** | 1.93 × 10⁻³ | **PASS** |
| **n-z-l** | nazala (sent down) | **12** | 20 | 5.09 | **5.97 × 10⁻⁴** | 5.97 × 10⁻³ | **PASS** |
| dh-k-r | dhikr (remembrance) | 5 | 11 | 2.80 | 0.221 | 1.000 | NULL |
| w-ḥ-y | waḥy (inspiration) | 3 | 5 | 1.27 | 0.207 | 1.000 | NULL |
| w-ʿ-d | waʿd (promise) | 0 | 4 | 1.02 | 0.607 | 1.000 | NULL |
| h-d-y | hudā (guidance) | 4 | 15 | 3.82 | 1.000 | 1.000 | NULL |
| r-b-b | rabb (Lord) | 8 | 32 | 8.14 | 1.000 | 1.000 | NULL |
| ʾ-l-h | ilāh (deity) | 2 | 6 | 1.53 | 0.959 | 1.000 | NULL |

(α_per = 0.05 / 10 = 0.005 after Bonferroni.)

## MW-5 positive control

**PASSED.** Roots 1 (kitāb) and 2 (qurʾān) — the [[h-new-53-muqattaat-book-reference|H-NEW-53]] anchor pair — independently both clear α_bon by orders of magnitude (kitāb: 2.93e-09; qurʾān: 1.17e-04). Pipeline replicates [[h-new-53-muqattaat-book-reference|H-NEW-53]].

(The combined [[h-new-53-muqattaat-book-reference|H-NEW-53]] test gave p ≈ 3.17e-12 because it scored a surah as positive for kitāb OR qurʾān. Disaggregating into separate root tests gives slightly weaker — but still extreme — per-root p-values, since each root individually covers fewer surahs. The combination is more powerful than either alone, as expected.)

## The four PASS roots

### 1. k-t-b (kitāb / book) — 20/28 muq vs expected 7.12 of 28

20 of the 28 surahs whose v1-3 contains a "kitāb" form are muqaṭṭaʿāt-opened. Expected if 28 were drawn at random: 7.12.

**Muq surahs** (20): Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 26, 27, 28, 31, 32, 40, 41, 43, 44, 45, 46.

**Non-muq surahs** (8): Q 17, 18, 34, 39, 52, 59, 62, 98 — these are the SUPPORTING evidence that book-reference is *associated* but not *exclusive* to muqaṭṭaʿāt.

### 2. q-r-ʾ (qurʾān / read-recite) — 9/11 muq vs expected 2.80

9 of the 11 surahs whose v1-3 contains a "qurʾān" form are muqaṭṭaʿāt-opened. Expected: 2.80.

**Muq surahs** (9): Q 12, 15, 20, 27, 36, 38, 41, 43, 50.

**Non-muq surahs** (2): Q 55 (al-Raḥmān, "He taught the qurʾān"), Q 72 (al-Jinn, mentions "qurʾānan ʿajaban").

The qurʾān-form is even MORE muqaṭṭaʿāt-concentrated than kitāb: 9/11 = 81.8% of all v1-3 qurʾān-mentions are in muq surahs. Only 2 non-muq surahs use it in their opening.

### 3. ʾ-y-ā (āyāt / signs-verses) — 11/16 muq vs expected 4.07

11 of the 16 surahs whose v1-3 contains an āyāt-form are muqaṭṭaʿāt-opened.

**Muq surahs** (11): Q 10, 11, 12, 13, 15, 26, 27, 28, 31, 41, 45.

These all use a stock incipit pattern: "تلك آيات الكتاب" / "تلك آيات القرآن" ("These are the signs/verses of the Book/Qurʾān"). It is the prototypical muqaṭṭaʿāt-opener formula at v1 immediately following the disconnected letters.

**Non-muq surahs** (5): Q 8, 17, 24, 54, 62.

This is a **NEW** finding beyond [[h-new-53-muqattaat-book-reference|H-NEW-53]]: muqaṭṭaʿāt-opened surahs use the āyāt formula in opening verses at 11/29 = 37.9%, vs non-muq 5/85 = 5.9%. The "tilka āyātu al-kitāb" formula is essentially a muqaṭṭaʿāt fingerprint.

### 4. n-z-l (nazala / sent down) — 12/20 muq vs expected 5.09

12 of the 20 surahs whose v1-3 contains a "nazala/anzala/tanzīl" form are muqaṭṭaʿāt-opened.

**Muq surahs** (12): Q 3, 7, 12, 13, 14, 20, 32, 40, 41, 44, 45, 46.

The verbs of REVELATION ("sent down," "We sent it down," "the sending down of...") are concentrated in muqaṭṭaʿāt-opened surah openings.

**Non-muq surahs** (8): Q 16, 18, 24, 25, 34, 39, 47, 97.

Q 32 starts "tanzīlu al-kitābi lā rayba fīhi min rabb al-ʿālamīn" (the sending down of the Book, no doubt in it, from the Lord of the worlds) — combining nazala + kitāb + rabb in a single muqaṭṭaʿāt-opener. The pattern is mutually reinforcing.

## The six NULL roots

### dhikr (remembrance) — 5/11, p = 0.221

Modest tilt toward muq (5/11 = 45%, expected 25%) but does NOT clear α_bon. Worth follow-up with weaker α: at uncorrected α=0.05, the trend is borderline. Q 19:2 starts "dhikru raḥmati rabbika" (the mention of your Lord's mercy) — but this verse-opening usage of dhikr is rare.

### waḥy (inspiration) — 3/5, p = 0.207

Only 5 surahs total in v1-3. Q 42 is the canonical case ("kadhālika yūḥī ilayka wa-ila lladhīna min qablika"). Sample is too thin to reach Bonferroni significance, but the 3/5 ratio (60%) is consistent with enrichment direction.

### waʿd (promise) — 0/4, p = 0.607

ZERO muq surahs have waʿd in v1-3. The 4 hits are Q 6, 60, 85, 104 — all non-muq. Promise/covenant is NOT a muqaṭṭaʿāt-opener theme.

### hudā (guidance) — 4/15, p = 1.000

EXACTLY at expected (4 vs E[X] = 3.82). Hudā shows NO muq enrichment in v1-3 — it is a Quran-wide motif distributed across all surahs, not muq-localized. Notably Q 2:2 ("hudan li-l-muttaqīn") IS in the hits, but the formula is generic.

### rabb (Lord) — 8/32, p = 1.000

EXACTLY at expected (8 vs E[X] = 8.14). Rabb-language is uniformly distributed across surah openings — a foundational divine address NOT specifically tied to muqaṭṭaʿāt. This is theologically interesting: the muqaṭṭaʿāt-opened surahs do not preferentially invoke "the Lord" in their first 3 verses.

### ilāh (deity) — 2/6, p = 0.959

Tiny effect (2 vs E[X] = 1.53), no significance. The two hits are Q 3 and Q 40, both "lā ilāha illā huwa" formulae that happen to fall in v1-3.

## Pattern of significance: REVELATION CLUSTER

The 4 PASS roots cluster semantically as the **revelation-content field**:
- **kitāb** (the written Book)
- **qurʾān** (the recited revelation)
- **āyāt** (the verses/signs that constitute the Book)
- **nazala** (the verb of "sending down" — i.e., the act of revelation)

The 6 NULL roots cluster as **theological / volitional / kerygmatic** themes:
- **dhikr, waḥy, waʿd**: related but at a different level of abstraction
- **hudā, rabb, ilāh**: divine attributes/addresses, not revelation-content

**This sharpens the [[h-new-53-muqattaat-book-reference|H-NEW-53]] finding**: muqaṭṭaʿāt-opened surahs are not enriched in revelation-themes generally — they are SPECIFICALLY enriched in **revelation-content meta-references**. They open by saying "This is THE BOOK / These are THE VERSES of the Book / The Book was SENT DOWN to you" — but they do NOT preferentially open with "the Lord" or "guidance" or "promise."

This is consistent with the al-Zarkashī / Welch reading: muqaṭṭaʿāt function as **bibliographic openers** — letter-of-the-Book + meta-reference to the Book itself. They don't function as theological openers in general.

## Cross-finding context

[[h-new-54-extended-root-enrichment|H-NEW-54]] ADDS a 9th independent axis to the muqaṭṭaʿāt design picture (cross-finding-006):

| Axis | Test | Verdict |
|---|---|---|
| 1. Letter frequency | [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary | ρ = −0.54 |
| 2. POA pharyngeal exhaustivity | [[h-new-44-2-poa-closure|H-NEW-44.2]].1 | PASS-DIRECTED p=0.049 |
| 3. Surah-position clustering | [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] | PARTIAL-PASS p=2e-5 |
| 4. Surah-length skew | [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] | STRONG-PASS 4/4 |
| 5. Length-after-chronology | [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] | STRONG-PASS 6/7 |
| 6. Cardinality-position decline | [[h-new-51-cardinality-position-decline|H-NEW-51]] | PASS-DIRECTED p=2e-5 |
| 7. Prophet-named enrichment | [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] | PASS-DIRECTED p=0.003 |
| 8. Book-reference enrichment | [[h-new-53-muqattaat-book-reference|H-NEW-53]] | STRONG-PASS-DIRECTED p ≈ 10⁻¹² |
| **9. Extended-revelation-field** | **[[h-new-54-extended-root-enrichment|H-NEW-54]]** | **PASS-BROAD-FIELD 4/10 roots** |

[[h-new-54-extended-root-enrichment|H-NEW-54]] demonstrates that the [[h-new-53-muqattaat-book-reference|H-NEW-53]] effect is not an artifact of two cherry-picked roots: it BROADENS to a 4-root semantic cluster (kitāb, qurʾān, āyāt, nazala) all reaching Bonferroni-10 significance.

## Honest caveats

1. **Surface form sets are imperfect.** Substring matching may miss rare orthographic variants and may include false positives. We mitigated for r-b-b by using token-boundary matching. Other roots use simple substring; checked manually for false positives in the 10 surfaces given (low rate).

2. **The 4 PASS roots are CORRELATED.** Many surahs co-occur kitāb + āyāt + nazala in v1-3 (e.g., Q 32:2: "tanzīlu al-kitābi lā rayba fīhi"). The 4 tests are not independent. Bonferroni-10 is conservative against this dependence — true family-wise α is closer to ~0.01 (looser), so the PASS verdicts are robust.

3. **NULL roots may yet pass with refined surface forms.** dhikr in particular is plausibly under-counted (some of its inflected forms may have been missed). This is documented but not chased — the pre-reg locks the form list.

4. **Direction of inference**: this finding does NOT establish that muqaṭṭaʿāt CAUSE the revelation-meta-reference. It establishes a strong CO-OCCURRENCE pattern at v1-3. The co-occurrence is consistent with both:
   - "muqaṭṭaʿāt are part of the revelation-meta-introduction structural template"
   - "scribes/composers preferentially placed muqaṭṭaʿāt at the start of surahs whose theme was the Book itself"

5. **6 of 10 roots NULL is itself informative.** Had we found ALL 10 roots significant, that would suggest the muq selection was just biased toward "richer" surah openings. The selectivity (4 PASS, 6 NULL) ARGUES AGAINST a generic "muq surahs are content-richer" effect, and FOR a specific revelation-content focus.

## Verdict

**PASS-BROAD-FIELD.** The kitāb/qurʾān enrichment generalizes specifically to the 2 additional revelation-content roots (āyāt, nazala). Six other revelation-theme roots are NOT enriched.

This is consistent with the muqaṭṭaʿāt-as-bibliographic-openers reading. The finding strengthens [[h-new-53-muqattaat-book-reference|H-NEW-53]] by demonstrating semantic specificity (the enrichment is about revelation-CONTENT meta-references, not divine attributes or covenant or guidance generally).

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-54-extended-root-enrichment-prereg.md`
- Script: `scripts/h_new_54_extended_root_enrichment.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-54.json`
- This findings doc: `findings/phase-b-hypotheses/h-new-54-extended-root-enrichment.md`
- Journal: `journal/h-new-54-run-1.md`

## Integrity

- Closed-form hypergeometric (deterministic; reproducible by inspection).
- Pre-reg locked BEFORE running; SHA-256 embedded in JSON output.
- All 10 roots reported (PASS and NULL) with identical detail.
- Positive control PASSED ([[h-new-53-muqattaat-book-reference|H-NEW-53]] anchor pair both replicate).
- Bonferroni-10 correctly applied; verdict robust to dependence between PASS roots.
- Surface form lists fully documented; precision/recall trade-offs disclosed.
