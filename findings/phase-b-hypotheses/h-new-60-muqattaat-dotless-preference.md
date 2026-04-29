---
id: H-NEW-60
title: Muqaṭṭaʿāt Letters Are Significantly Dotless — pre-i'jām script signature
phase: B
status: STRONG-PASS-DIRECTED at p=0.0009 single-test; PASS-Bonferroni-4 on per-class breakdown
date: 2026-04-16
agent: integrator (main session)
test: closed-form hypergeometric on i'jām-class distribution
verdict: STRONG-PASS-DIRECTED
rules_tuple: (28-letter Arabic alphabet, standard i'jām dot-counts)
---

# [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] — Muqaṭṭaʿāt Dotless Preference (RESULT)

## Headline

**11 of 14 muqaṭṭaʿāt letters are dotless (79%)**. Only 13 of 28 alphabet letters are dotless (46.4%). The muqaṭṭaʿāt set systematically prefers letters that have NO i'jām (dot marks).

Hypergeometric P(X ≥ 11 | n=14, K=13, N=28) = **0.000919**. PASS-DIRECTED at α=0.001 single-test.

Per-dot-class Bonferroni-4 (α=0.0125):
- **0 dots: ENRICHED** (11/13 = 85%, expected 6.5; p=0.0018) ✓
- **1 dot: DEPLETED** (1/10 = 10%, expected 5.0; p=0.0044) ✓
- 2 dots: 2/3 = 67% (n.s.)
- 3 dots: 0/2 = 0% (n.s. due to small class size)

## Per-letter table

| Class | Letters in alphabet | In muqaṭṭaʿāt | Not in muqaṭṭaʿāt |
|---|---|---|---|
| 0 dots (13) | ا ح د ر س ص ط ع ك ل م ه و | **ا ح ر س ص ط ع ك ل م ه** (11) | د و (2) |
| 1 dot (10) | ب ج خ ذ ز ض ظ غ ف ن | **ن** (1) | ب ج خ ذ ز ض ظ غ ف (9) |
| 2 dots (3) | ت ق ي | **ق ي** (2) | ت (1) |
| 3 dots (2) | ث ش | (0) | ث ش (2) |

The triple-dot letters {ث, ش} are BOTH excluded. The single-dot letters are almost all excluded (only ن is included). The dotless letters are almost all included (only د, و excluded). This is an extremely sharp pattern.

## Total dot density

- Total dots across muqaṭṭaʿāt letters: **5** (1 from ن + 2 from ق + 2 from ي)
- Total dots across alphabet: **22**
- Mean dots per muqaṭṭاʿat letter: **0.36**
- Mean dots per alphabet letter: **0.79**
- Ratio: muqaṭṭāʿat have **less than half** the dot density of the alphabet average

## Historical-linguistic interpretation

Pre-Islamic Arabic script (mukhaṭṭamāt al-ʿArab al-jāhiliyya, the early Arabic of the 6th-7th centuries CE) was **undotted**. The i'jām (dotting system) that distinguishes letters sharing the same skeleton (rasm) — e.g., ب/ت/ث/ن/ي all share the same basic shape but differ by dots — was developed later, traditionally attributed to:
- al-Aswad al-Duʾalī or Yaḥyā b. Yaʿmar (~7th century CE) for the recitation marks
- al-Khalīl b. Aḥmad al-Farāhīdī (~8th century CE) for the systematic standardization

**The muqaṭṭaʿāt as a letter SELECTION appears to PRESERVE the pre-dotting Hijazi script's letter inventory** — i.e., letters whose IDENTITY does not depend on dot-distinction.

If this interpretation is correct:
- The muqaṭṭaʿāt design predates the i'jām system
- The muqaṭṭaʿāt prefer letters that can be recognized from RASM (skeletal shape) ALONE
- The dotted letters (which require i'jām for disambiguation) are systematically avoided

This is consistent with a 7th-century revelatory date and inconsistent with later (8th+ century) editorial composition.

## What this DOES NOT claim

- The muqaṭṭaʿāt design is "miraculous" — no theological claim about origin.
- That the dot-count was the SOLE selection criterion — [[h-new-44-2-poa-closure|H-NEW-44.2]] showed POA is NOT a strong selector; the dot-count is one of several criteria.
- That this is the historically PROVEN dating mechanism — it's a CONSISTENT-WITH observation, not a strict dating proof.

## Mechanism candidates (not exclusive)

1. **Pre-i'jām preservation hypothesis**: muqaṭṭaʿāt SELECT for letters that don't need dots, reflecting the original undotted Hijazi script.

2. **Visual prominence hypothesis**: dotless letters have CLEANER, more iconic shapes; for a recitation/calligraphy tradition, undotted letters may be visually preferred.

3. **Cognitive-load hypothesis**: dotless letters are LESS COGNITIVELY DEMANDING to identify; muqaṭṭaʿāt as opening signals would naturally prefer high-recognition letters.

4. **Hijazi-script identity hypothesis**: dotless letters mark the muqaṭṭāʿat as distinctively-Arabic in their pre-classical form.

## Cross-finding context

This adds an additional axis to cross-finding-006 / cross-finding-008:

| Axis | Test | Verdict |
|---|---|---|
| 1. Letter frequency | [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary | ρ = −0.54 |
| 2. POA pharyngeal exhaustivity | [[h-new-44-2-poa-closure|H-NEW-44.2]].1 | PASS-DIRECTED p=0.049 |
| 3. Surah-position clustering | [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] | PARTIAL-PASS p=2e-5 |
| 4. Surah-length skew | [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] | STRONG-PASS 4/4 |
| 5. Length-after-chronology | [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] | STRONG-PASS 6/7 |
| 6. Cardinality-position decline | [[h-new-51-cardinality-position-decline|H-NEW-51]] | PASS-DIRECTED p=2e-5 |
| 7. Prophet-named enrichment | [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] | PASS-DIRECTED p=0.003 |
| 8. Book-reference enrichment | [[h-new-53-muqattaat-book-reference|H-NEW-53]] | STRONG-PASS p=3e-12 |
| 9. Formulaic openings | [[h-new-57-formulaic-openings|H-NEW-57]] | STRONG-PASS p=2e-9 |
| 10. Multi-feature classifier | [[h-new-55-classifier|H-NEW-55]] | STRONG-PASS AUC=0.92 |
| 11. Extended writing-cluster | [[h-new-56-five-exceptions|H-NEW-56]] | STRONG-PASS p=8.6e-13 |
| **12. Dotless preference** | **[[h-new-60-muqattaat-dotless-preference|H-NEW-60]]** | **STRONG-PASS-DIRECTED p=0.0009** |

The muqaṭṭaʿāt design is now characterized at **12 independent axes**. The dotless-preference axis is unique in its potential historical-linguistic implication.

## Honest caveats

1. **Post-hoc-noticed**: I observed the dotless preference during inspection of the muqaṭṭaʿāt letter set after [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary established the frequency correlation.
2. **Single test directed**: per the project's discipline, this is PASS-DIRECTED, not CONFIRMED. Independent replication on a distinct dimension would upgrade.
3. **The historical-linguistic interpretation is SPECULATIVE**. The PATTERN is mathematically clear; the MECHANISM (pre-i'jām preservation) is one of several plausible explanations.
4. **Class-size sensitivity**: The 2- and 3-dot classes are too small for individual significance testing under Bonferroni-4. The single-test directed result is the cleanest framing.
5. **The 2 dotless exceptions** (د and و): د is a coronal stop, و is a labial glide. Both are common letters; their exclusion isn't obviously explained by the dot-preference framework alone.

## Verdict

**STRONG-PASS-DIRECTED at p=0.0009 single-test**. Per Bonferroni-4 per-class: PASS on dotless-enrichment AND on single-dot-depletion (both Bonferroni-significant). 

Recommendation: include in cross-finding-006/008 as the 12th independent muqaṭṭaʿāt-design axis.

## Integrity

- Closed-form hypergeometric (reproducible by inspection).
- Dot-count assignments per standard Arabic orthography.
- Per-letter breakdown listed for audit.
- Post-hoc-noticed status disclosed.
- Historical-linguistic interpretation labeled SPECULATIVE.
