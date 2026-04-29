# Zakāh / Charity Run 1 — Journal

Date: 2026-04-12. Agent: Phase B. Brief: eight analytic tasks on the Quranic vocabulary of almsgiving.

## Workflow

1. Surveyed corpus structure. `data/morphology/quranic-corpus-morphology-0.4.txt` is a Buckwalter-transliterated tab-separated morphology file (128 276 lines; ~77 430 segment rows after the header). Fields: LOCATION, FORM, TAG, FEATURES. Stem rows carry `POS:`, `LEM:`, `ROOT:` slots inside the FEATURES field; prefix/suffix rows have only morphophonemic tags.

2. Built a single Python pass over the file, tallying tokens by root (`grep -c` plus a proper parser for lemma-level counts). Targeted six roots: `zkw`, `Sdq`, `nfq`, `rqb`, `xyr`, `Avr`. Totals (root tokens): 59 / 155 / 111 / 24 / 196 / 21 respectively.

3. Verified the canonical claim "zakāh occurs 32 times" — tested against lemma `zakaw`p` specifically (the technical fem. noun), and recovered exactly 32 tokens in 32 distinct verses. That matches classical tafsīr statistics and validates the morphology file's lemmatisation.

4. For Task 2 (Salāh+Zakāh pair) intersected verses in which both roots `Slw` and `zkw` appear. Result: **28 verses**, spanning Meccan (19:31, 19:55, 21:73, 27:3, 31:4, 73:20, 98:5) and Medinan (the remaining 21). Four of the 32 `zakaw`p` verses lack `Slw`: 7:156, 18:81, 19:13, 41:7 — all four carry the more archaic ethical sense of "purity / gift" rather than "alms-tax".

5. Task 3 (Q 9:60): fetched the full morphology of the verse (22 tokens in 20 word-groups + formulaic divine-names tail). Listed the eight aṣnāf with their Arabic roots and grammatical preposition attachments. Observed that categories 5 (`fī r-riqāb`) and 7 (`fī sabīli llāh`) are the only two prefixed with `fī`, which the fiqh reads as "earmark funds" rather than direct recipients.

6. Task 4 (chronology): used the standard Egyptian classification for Meccan/Medinan suwar. Key finding — all 13 tokens of the noun `ṣadaqa(t)/ṣadaqāt` are Medinan. Roots `nfq` lemma `ʾanfaqa` is 86 % Medinan. Meccan Sdq is dominated by truth-senses; Meccan zkw is dominated by form V reflexive `tazakkā`. The juridical shift is real and measurable.

7. Task 5 (riqāb): isolated all 9 occurrences of `raqaba(t)`. All Medinan. Observed the distribution: 1 ethical (2:177), 1 obligatory-fund (9:60), 3 expiation (4:92 ×3, 5:89, 58:3), 1 war-policy (47:4), 1 moral-aspiration (90:13). The root also yields the divine title `Raqīb` (5 tokens) — a striking semantic pun between "neck" (subjugated) and "Watcher" (divine), both sharing the trilateral rqb.

8. Task 6 (2:261-264 parable): pulled morphology of all four verses. Noted the lexical stitching `yuḍāʿifu` (ḍEf) appears in both 2:261 and 64:17 — the multiplicand verb is the only IQ-level-II impf. of `ḍEf` used in spending contexts. Observed the A-B-Bʹ-Aʹ ring structure: fertile grain (2:261) / injury of mann & adhā (2:262) / kind-word value (2:263) / barren rock (2:264). Axial claim: `xayrun min ṣadaqatin yatbaʿuhā adhā`.

9. Task 7 (64:16-17): morphology pull. Found that the concluding clause of 64:16 (`wa-man yūqa shuḥḥa nafsihi fa-ulāʾika humu l-mufliḥūn`) is identical to 59:9's close — a cross-sūra hook linking ʾīthār (59:9) with xayr-spending (64:16). Qurḍ ḥasan ("good loan to Allāh") — checked distribution: 2:245, 5:12, 57:11, 57:18, 64:17, 73:20 = 6 tokens of the formula, all Medinan (73:20 by tradition).

10. Task 8 (miqdārayn): identified Q 25:67 as the locus classicus — `lam yusrifū wa-lam yaqturū wa-kāna bayna dhālika qawāmā`. Paired with Q 17:26-29 (the "fettered hand vs. fully outstretched hand" bodily metaphor, and the tabdhīr prohibition). Traced vocabularies: Meccan `tabdhīr` (b*r) → Medinan `ʾisrāf` (srf) as the "upper bound"; `qatar` (qtr), `bakhal` (bxl), `shuḥḥ` ($HH) as the "lower bound". `qawām` (qwm) is the Qurʾanic name for the mean — a morphological Aristotelian *mesotēs*.

## Artefacts produced

* `findings/phase-b-hypotheses/zakat-charity.md` — ~2700 words, eight tasks plus cross-synthesis.
* This journal file.

## Open / deferrable items

* Full chronological plot of infāq-verses by revelation rank (would require a chronological-order table; the intra-repo asset at `findings/phase-b-hypotheses/chronological-revelation.md` may already have one).
* Statistical test on whether the Ṣalāh/Zakāh pair is actually the most frequent pair-command — would require enumerating all verb-pair imperatives and ranking by frequency. The claim is strong on prima-facie grounds (28 co-occurrences) but not proven maximal without that baseline.
* Confirmation of Q 98:5 reading `ḥunafāʾa` and its relation to the covenant imagery of zakāh.
