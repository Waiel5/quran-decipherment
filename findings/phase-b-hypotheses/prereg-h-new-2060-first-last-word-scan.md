---
id: H-NEW-2060
title: First-word and last-word cross-surah taxonomy + strict word-level inclusio scan (114 surahs)
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-2060-inclusio (single primary inclusio-count test; taxonomy is descriptive-census, not a hypothesis test)
alpha_bon: 0.05
direction_of_effect: MORE — the observed count of surahs whose first-content-word QAC root equals its last-word QAC root (strict single-word inclusio) is GREATER than the count expected under a label-shuffle null (one-tailed permutation null)
origin: >
  The opening-word taxonomy of the 114 surahs is a classical ʿulūm-al-Qurʾān census topic: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 61 (*fawātiḥ al-suwar* — the surah-openings) classifies the openings into a fixed set of formula-classes (the muqaṭṭaʿāt; praise *al-ḥamdu*; glorification *subḥāna* / *sabbaḥa* / *tabāraka*; the oaths *al-aqsām*; the vocatives *yā-ayyuhā*; the conditional/temporal *idhā*; the imperatives *qul*; the interrogatives; etc.). al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *fawātiḥ al-suwar* gives the same census with the canonical count of ten opening-genera. SEPARATELY, al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, argues that surahs exhibit *barāʿat al-maṭlaʿ* coupled with thematic closure — the opening and the closing of a surah echo one another (an inclusio / ring-closure claim). This pre-reg (a) builds the COMPLETE empirical opener+closer taxonomy of all 114 surahs from QAC v0.4 morphology, and (b) promotes al-Biqāʿī's closure-claim to a STRICT WORD-LEVEL falsifiable test: does the single first-content-word's root reappear as the single last-word's root more often than chance?
verdict_ceiling: PASS-DIRECTED (k=1; single pre-registered inclusio test) for the inclusio arm; the taxonomy arm is a DESCRIPTIVE CENSUS (no verdict ceiling — it is a complete enumeration, reported as-is)
rules_tuple:
  orthography: no-tashkeel (for the displayed opening/closing word forms); QAC v0.4 ROOT field for the inclusio match
  word_definition: orthographic-token — the "first word" = all segments sharing word-index w=1 of the first content verse; the "last word" = all segments sharing the maximum word-index of the final verse
  letter_definition: graphemes (immaterial here)
  basmala_policy: counted-only-in-surah-1 — the basmala is verse 1 of Q 1 only; for Q 2–Q 114 the basmala is NOT a numbered verse (QAC v0.4 reflects this), so "first word after basmala" = word 1 of verse 1; for Q 1 the first word after the basmala = word 1 of verse 2 (*al-ḥamdu*); Q 9 al-Tawba has no basmala, first word = word 1 of verse 1 (*barāʾa*)
  verse_numbering: hafs-kufan
  root_source: data/morphology/quranic-corpus-morphology-0.4.txt (QAC v0.4, the project-canonical root annotation)
  muqattaat_handling: the 29 disjoined-letter openings (POS:INL) carry NO root; for the inclusio test the FIRST CONTENT WORD = the first w-index whose segment bears a ROOT field (skipping the INL token); the opener-class for these 29 is "muqaṭṭaʿāt"
  null_model: 10,000 label-shuffle permutations (seed 20260509) — the 114 last-word root labels are permuted across the 114 surahs and the inclusio-match count recomputed; one-tailed p = P(null match-count ≥ observed)
---

# H-NEW-2060 pre-registration — First-word / last-word cross-surah taxonomy + strict word-level inclusio scan

## Origin and classical anchor

Two distinct classical claims are operationalised here.

**(1) The opening-formula census.** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, **nawʿ 61** (*fī fawātiḥ al-suwar*) and al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* (*fawātiḥ al-suwar*), both classify the openings of the 114 surahs into a fixed taxonomy of opening-genera — canonically counted as **ten** classes: the disjoined letters (*ḥurūf al-muqaṭṭaʿa*); praise (*al-thanāʾ* / *al-ḥamdu*); glorification (*subḥāna* / *sabbaḥa* / *yusabbiḥu* / *tabāraka*); the oaths (*al-aqsām* / the *wa-*formula); the conditionals and temporals (*idhā* / *idhā waqaʿat*); the imperatives (*qul* and other commands); the interrogatives (*hal atāka* / *ʿamma yatasāʾalūn*); the vocatives (*yā-ayyuhā al-nabī* / *yā-ayyuhā al-nās*); the declarative-nominal openings; and the conditional-curse / report openings. This pre-reg builds the COMPLETE empirical version of this census directly from QAC v0.4 morphology — assigning every one of the 114 surahs to an opener class and every one to a closer class — and reports it as a descriptive enumeration.

**(2) The opening↔closing inclusio (barāʿat al-maṭlaʿ + ḥusn al-khātima / ring-closure).** al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, argues that the *tanāsub* (coherence) of a surah includes a correspondence between its opening and its closing — the close echoes the open. The strictest possible operationalisation of "echo" is **lexical-root identity at the single-word level**: does the root of the surah's first content word reappear as the root of its last word? This pre-reg tests that strict version.

**Relation to H-NEW-189 (do NOT duplicate).** [[h-new-189-medinan-inclusio|H-NEW-189]] / H-NEW-189.1 already tested inclusio at the **first-content-VERSE-roots ∩ last-VERSE-roots** level (set-intersection over all content roots of the first and last verses, simple stemmer) and found the muq-cell NULL but a Medinan>Meccan STRONG-PASS (54.2% vs 11.1%, partial ρ=+0.483 length-controlled). H-NEW-2060 is deliberately at a **stricter and narrower** grain: the SINGLE first-content-WORD root vs the SINGLE last-WORD root (QAC v0.4 roots, not a simple stemmer; one word each, not a whole-verse root-set). The two tests probe different structural scales (verse-block echo vs single-word ring-clasp), so a divergent verdict here is informative, not contradictory. H-NEW-2060 additionally delivers the COMPLETE opener+closer taxonomy, which H-NEW-189 does not.

## Operational definitions (locked, re-derived at runtime from QAC v0.4)

For each surah s ∈ {1..114}:

- **first word** = the orthographic token at word-index w=1 of the FIRST CONTENT VERSE.
  - First content verse = verse 2 for Q 1 (basmala is verse 1), verse 1 for all others (basmala is unnumbered for Q 2–114; Q 9 has none).
- **first content word** (for the inclusio test) = the first word-index whose token bears a QAC `ROOT:` field. For the 29 muqaṭṭaʿāt surahs the w=1 token is POS:INL with no root, so the first content word is the next root-bearing word.
- **last word** = the orthographic token at the MAXIMUM word-index of the surah's FINAL verse; its inclusio root = the ROOT of the root-bearing segment of that final word (if the final word is a bare particle/pronoun with no root, the inclusio root is recorded as null and the surah cannot match).
- **opener class** is assigned from the morphology of the first word (and, where the class needs it, the first two-three tokens), by the locked decision cascade below.
- **closer class** is assigned from the morphology of the final verse's last word by the locked decision cascade below.

### Opener-class decision cascade (locked, evaluated top-down, first match wins)

1. **muqaṭṭaʿāt** — w=1 token is POS:INL.
2. **qul-imperative** — w=1 token lemma is *qul* (ROOT:qwl, IMPV).
3. **al-ḥamdu** — w=1 token root is Hmd (praise opening).
4. **tasbīḥ/glorification** — w=1 token root ∈ {sbḥ (*subḥāna*/*sabbaḥa*/*yusabbiḥu*), brk (*tabāraka*)}.
5. **vocative (yā-ayyuhā / yā-)** — w=1 token is POS:VOC (the *yā* particle) or lemma *yā-ayyuhā*.
6. **oath-wāw** — w=1 token is a CONJ *wa-* prefix immediately followed by a definite/indefinite cosmic-or-natural noun (the *qasam* formula), AND the surah is not an *idhā*-opener. (Strict: matches the H-NEW-1550 cluster plus any additional *wa-* oath openers.)
7. **idhā-conditional/temporal** — w=1 token lemma is *idhā* (POS:T or COND).
8. **interrogative** — w=1 token is an interrogative particle (POS:INTG; e.g. *hal*, *a-*, *ʿamma* = *ʿan mā*).
9. **other-imperative** — w=1 token is an IMPV verb other than *qul* (e.g. *iqraʾ* Q 96 ROOT:qrA).
10. **other-verb** — w=1 token is a non-imperative verb (e.g. *yasʾalūnaka* Q 8, *atā* Q 16, *iqtaraba* Q 21/54, *taballa* etc.).
11. **conditional-particle** — w=1 token is a conditional particle *idhā/idh/in* not caught above, or *wayl* curse-noun openers.
12. **nominal/other** — anything else (a noun/pronoun/particle opening not matched above), recorded with its actual lemma so the residue is fully enumerated.

The cascade is exhaustive: every surah lands in exactly one class. The residue class (12) will be reported with each member's actual first-word lemma so the census is complete and auditable.

### Closer-class decision cascade (locked, evaluated top-down, first match wins)

The closer taxonomy is assigned from the FINAL VERSE (the morphology of its constituent words), since "closing-word classes" in the classical literature (divine-name pairs, exhortation, command) are properties of the closing clause, not a single token:

1. **divine-name-pair** — the final verse ends in (or contains as its terminal nominal clause) two consecutive divine-attribute names (e.g. *ʿazīzun ḥakīm*, *ghafūrun raḥīm*, *samīʿun ʿalīm*) — detected as two adjacent ADJ/N tokens that are members of the asma-al-husna list (`data/asma-al-husna.txt`) at the verse end.
2. **single-divine-name** — final verse ends in one such divine-attribute name.
3. **command/imperative** — final verse's terminal clause contains an IMPV verb (e.g. *fa-sabbiḥ*, *qul*).
4. **exhortation/eschatological** — final verse contains an eschatological/reward-punishment terminal nominal (*al-jaḥīm*, *al-naʿīm*, *khālidūn*, *al-nār*, *al-jannah*) or a *taqwā*/reward clause.
5. **other** — recorded with the final word's actual lemma; residue fully enumerated.

The closer cascade is reported descriptively; the closer taxonomy is a census, not a hypothesis test.

## Hypothesis (primary test — the ONLY inferential arm)

**H1 (inclusio):** The number of surahs for which `root(first content word) == root(last word)` is GREATER than expected if the 114 last-word roots were randomly re-assigned to surahs.

- **Test statistic:** N_match = #{ s : root_first(s) == root_last(s), both non-null }.
- **Null:** 10,000 label-shuffle permutations of the 114 last-word roots across surahs (seed 20260509); one-tailed p = (1 + #{perm N_match ≥ observed}) / (1 + 10000).
- **Direction LOCKED:** observed N_match > null mean (MORE). Reversed (observed < null mean) is impossible for a non-negative count unless observed is below the null mean, in which case it is published as NULL.
- **Decision rule:**

| Outcome | Verdict |
|:--|:--|
| p ≤ 0.05 AND N_match ≥ 10 (pre-stated threshold) | PASS-DIRECTED |
| p ≤ 0.05 AND N_match < 10 | PARTIAL (significant but below the pre-stated ≥10 effect-size floor) |
| p > 0.05 | NULL |

The pre-stated effect-size floor of **N_match ≥ 10** comes directly from the task brief ("≥10 surahs show inclusio"). It is reported alongside the permutation p so the reader sees both significance and the raw count.

## Corpus-unique opener/closer (descriptive)

The script additionally flags any opener-class with exactly ONE member (a corpus-SINGLETON opening genre) and any first-content-word root or last-word root that is a corpus-singleton at the surah-opening or surah-closing position. These are reported descriptively (MW-7 single-test cap; no inferential claim).

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior):** opener/closer cascades + N_match statistic + label-shuffle null all specified above before any run.
- **MW-2 (corpus-prior):** 10,000 permutations.
- **MW-3 (alternative-models):** The inclusio test is reported both at the STRICT single-word grain (this test) AND cross-referenced against H-NEW-189's verse-set grain, which is the alternative operationalisation. No additional fitted model.
- **MW-4 (over-fitting):** no fitted parameter; the cascade is fixed and exhaustive.
- **MW-5 (replication):** a second seed (20260510) re-run of the permutation null is reported as the replication arm; the verdict must hold across both seeds.
- **MW-6 (instrument-control):** the label-shuffle null IS the negative control — it destroys the first↔last pairing while preserving both marginal root-distributions.
- **MW-7 (post-hoc cap):** corpus-unique flags and any non-pre-registered observation carry single-test α=0.05 and are reported descriptively only.

## Garden-of-forking-paths disclosure

- The inclusio test is at the SINGLE-WORD grain by design (the strictest "ring-clasp" reading of al-Biqāʿī). The wider verse-set grain is already covered by H-NEW-189; this pre-reg does not re-run it.
- "First content word" skips the muqaṭṭaʿāt INL token (which has no root) — locked before the run. The alternative (treating the INL token itself as the first word, hence no muq surah can ever match) is a degenerate choice and is rejected in advance; it is reported as a sensitivity line only.
- The N_match ≥ 10 effect floor is taken verbatim from the task brief and is not tuned.
- Seed 20260509 matches the broader session for cross-test comparability; replication seed 20260510.

## Anti-flip

A clean NULL (observed N_match ≈ null mean) is itself informative: it would mean the surah-level single-word ring-clasp is NOT a corpus-wide architectural regularity, and that al-Biqāʿī's closure-claim — to the extent it holds (H-NEW-189) — operates at the VERSE-BLOCK grain (Medinan-enriched) rather than the single-word grain. The descriptive taxonomy stands regardless of the inclusio verdict.

## Pre-commit attestation

Locked by SHA256. The run script `scripts/h-new-2060.py` computes the SHA256 of THIS file at runtime and aborts (fail-fast) on mismatch. SHA embedded as EXPECTED_SHA after this file is finalised.
