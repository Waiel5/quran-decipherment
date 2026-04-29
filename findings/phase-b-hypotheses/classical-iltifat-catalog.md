---
source: classical-scholar (team-discovery synthesis)
delivered: 2026-04-13
integrator: 2026-04-13
retagged: 2026-04-12 (AMEND-12 verbatim-confidence pass)
status: CLASSICAL-SYNTHESIS-ANCHORED (not direct-Suyūṭī-enumeration)
verbatim_confidence:
  six_type_typology: HIGH  # stable cross-text balāgha tradition fact, not single-source recall
  per_surah_aggregation: MEDIUM  # working-notes distillation, not direct from Arabic editions in hand
  zarkashi_only_verses: LOW  # verses added from Zarkashī that Suyūṭī does not explicitly flag
  syn_tagged_entries: LOW  # 20 of 46 surahs inferred from classical examples, not flagged in nawʿ texts consulted (corrected per audit-028 B1/B2: direct TSV row-count yields N=46, events=122, mean=2.65, syn=20 — supersedes prior 45/117/2.6/21)
  nawʿ_numbers: PENDING  # see retag memo below — NOT physically verified
  tansheet_al_sami_phrase: LOW  # classical-scholar 2026-04-12 recall-only paraphrase
primary_sources:
  - al-Zarkashī, al-Burhān fī ʿUlūm al-Qurʾān, **[nawʿ PENDING physical verification — previously recall-tagged as "nawʿ 47"; retracted 2026-04-12 because (a) Burhān has 47 anwāʿ total in Abū l-Faḍl Ibrāhīm 1957 ed. so nawʿ 47 would be the terminal chapter which is implausible for iltifāt, (b) the "nawʿ 47" attribution was a recall-inferred layer on genuine doctrine, same failure mode as the retracted "Burhān nawʿ 51" Ḥashr citation]** "fī l-iltifāt wa-ʿudūl al-khiṭāb", Dār al-Kutub al-ʿIlmiyya Beirut (Muḥammad Abū l-Faḍl Ibrāhīm ed.), vol. 3 pp. 314-339
  - al-Suyūṭī, al-Itqān fī ʿUlūm al-Qurʾān, **[nawʿ PENDING physical verification — previously recall-tagged as "nawʿ 56" in this file and audit-013, but "nawʿ 58" in docs/master-index.md:20 and journal/balagha-run-1.md:57, journal/classical-lataif-run-1.md:52; the internal contradiction alone blocks publication until physically verified]** "fī l-iltifāt", King Fahd Complex 2005 ed., vol. 5 pp. 1836-1858
  - Ibn al-Athīr, al-Mathal al-Sāʾir fī Adab al-Kātib wa-l-Shāʾir (cross-check, secondary reference only)
downstream_users:
  - H-NEW-2 revision (ρ-correlation against per-surah pronoun-chain z-score)
  - H-CLASSIC-37 (iltifāt per-verse × genre partition test)
  - M-6 CANDIDATE pericope-block substrate (validation leg)
downstream_caveat: |
  Downstream finding audit-013 cites "al-Zarkashī nawʿ 47" and "al-Suyūṭī nawʿ 56" as
  pass-through from an earlier classical-scholar delivery. Both nawʿ numbers are now
  PENDING. Downstream findings that re-publish them must (a) either remove the specific
  nawʿ numbers, (b) re-tag them PENDING, or (c) wait for the Phase-2 physical verification
  regime to return. The DOCTRINE behind this catalog (six-type iltifāt typology, classical
  tansheeṭ-al-sāmiʿ function, per-surah density structure) is unaffected; only the
  specific nawʿ-number attributions and the paraphrased Arabic phrase are under retag.
---

# Classical iltifāt-density catalog

46 surahs, 122 events. This is a classically-informed synthesis
suitable for ρ-correlation tests at MEDIUM rigor. It is **not** a
direct literal enumeration from a single source. Downstream tests
must tag findings that rest on this catalog as "classical-synthesis
anchored," not "Suyūṭī-direct."

## Canonical iltifāt typology (al-Zarkashī nawʿ 47)

1. **Person shift** (ʿudūl min ghayba ilā khiṭāb or reverse): Q 1:5 *iyyāka naʿbudu* after Q 1:1-4 third-person.
2. **Number shift** (ʿudūl min wāḥid ilā jamʿ or reverse): Q 10:22.
3. **Tense shift** (māḍī ↔ muḍāriʿ): Q 2:23.
4. **Addressee shift** (mukhāṭab → mukhāṭab ākhar): Q 11:44 *yā arḍu blaʿī māʾaki*.
5. **Speaker shift** (mutakallim → mutakallim ākhar): Q 19:64.
6. **Referential shift** (ism ẓāhir ↔ ḍamīr): Q 35:9.

## Per-surah catalog (TSV-compatible)

Columns: `surah | count | exemplar_verses | source_tag`
- `count` = number of distinct iltifāt events classically flagged in sources consulted
- `source_tag`: Z = al-Zarkashī nawʿ 47; S = al-Suyūṭī nawʿ 56; Z+S = both; syn = synthesis/inference from their examples

```
surah	count	exemplars	source_tag
1	1	Q1:5	Z+S
2	7	Q2:21,Q2:23,Q2:49,Q2:143,Q2:172,Q2:196,Q2:281	Z+S
3	4	Q3:11,Q3:26,Q3:180,Q3:195	S
4	5	Q4:1,Q4:37,Q4:75,Q4:108,Q4:174	Z+S
5	3	Q5:23,Q5:70,Q5:117	S
6	6	Q6:12,Q6:63,Q6:99,Q6:102,Q6:140,Q6:161	Z+S
7	4	Q7:57,Q7:117,Q7:171,Q7:206	S
9	2	Q9:14,Q9:120	syn
10	4	Q10:22,Q10:23,Q10:61,Q10:104	Z+S
11	3	Q11:44,Q11:69,Q11:119	Z+S
12	3	Q12:29,Q12:78,Q12:107	S
13	2	Q13:15,Q13:16	syn
14	2	Q14:31,Q14:52	S
16	5	Q16:1,Q16:48,Q16:72,Q16:91,Q16:125	Z+S
17	4	Q17:1,Q17:45,Q17:78,Q17:111	Z+S
18	2	Q18:23,Q18:110	syn
19	3	Q19:18,Q19:64,Q19:96	Z+S
20	4	Q20:50,Q20:83,Q20:124,Q20:135	S
21	3	Q21:25,Q21:87,Q21:112	S
22	2	Q22:31,Q22:78	syn
23	2	Q23:62,Q23:99	S
24	3	Q24:33,Q24:55,Q24:63	syn
25	3	Q25:17,Q25:48,Q25:77	S
26	2	Q26:216,Q26:227	syn
27	3	Q27:60-64,Q27:91	Z+S
28	2	Q28:70,Q28:88	syn
29	2	Q29:56,Q29:69	syn
30	2	Q30:11,Q30:58	S
31	2	Q31:32,Q31:34	syn
32	1	Q32:11	syn
33	4	Q33:6,Q33:33,Q33:53,Q33:56	S
34	2	Q34:9,Q34:49	syn
35	3	Q35:9,Q35:27,Q35:45	Z+S
36	3	Q36:22,Q36:82,Q36:83	S
37	2	Q37:180-182	syn
39	3	Q39:7,Q39:53,Q39:74	S
40	2	Q40:60,Q40:84	syn
41	2	Q41:12,Q41:54	syn
42	2	Q42:51,Q42:52	S
43	2	Q43:84,Q43:89	syn
50	1	Q50:45	syn
55	1	Q55:33	syn
56	1	Q56:83	syn
67	1	Q67:13	syn
76	1	Q76:29-30	S
114	1	Q114:1	syn
```

Total surahs covered: 46
Total events catalogued: 122
Mean count per catalogued surah: 2.65
Max density: Q 2 (7 events, raw)
Surahs with events tagged `syn` only: downstream sensitivity tests
should re-run excluding these.

## Normalization options for downstream ρ-correlation

Three normalizations available; classical-scholar recommendation is
(b) per-verse as primary metric, (a) raw count as sensitivity.

- (a) RAW COUNT — favors long surahs trivially (more opportunity).
- (b) PER-VERSE — `count / N_verses`. Length-controlled. Primary.
- (c) PER-WORD — `count / N_words`. Alternative length-control.

Under (b), short dhikr-heavy surahs (Q 1, Q 112, Q 113, Q 114) rank
high, which matches classical intuition that iltifāt is a signature
of dense prophetic address, not a long-surah artefact.

## Critical caveats for downstream use

1. **This is NOT exhaustive.** Zarkashī and Suyūṭī between them
   catalog hundreds of iltifāt events across the Quran; the 117-event
   distillation above represents only the explicitly-flagged
   exemplars (those cited by name in nawʿ 47 / nawʿ 56). A fuller
   enumeration is available on request to classical-scholar
   ("Zarkashī vol. 3 pp. 320-339 full exemplar enumeration").

2. **Zero ≠ absent.** Surahs NOT in the catalog (including most of
   Q 8, Q 15, Q 44-49, Q 51-54, Q 57-66, Q 68-75, Q 77-111) are
   **NOT confirmed zero-iltifāt** — they are "not-classically-flagged-
   in-sources-consulted." Downstream ρ-correlation and Mann-Whitney
   tests MUST treat missing surahs as NaN, NOT zero. Silent
   zero-imputation is forbidden at integrator level.

3. **Verse references from working notes.** Every verse above is
   from classical-scholar's internal working notes, not directly
   from the Arabic Burhān / Itqān text in hand. Before any finding
   using this catalog reaches publishable status, classical-scholar
   must physically verify 5-10 random entries against Arabic
   editions. This is gated under the CLASSICAL-VERIFICATION-HASHR
   / catalog-spot-check pre-publication regime.

4. **ρ-correlation gating protocol**:
   - Primary test: Spearman ρ(iltifāt_per_verse, target_feature), n = 46 (NaN-respected).
   - Significance threshold: p < 0.01 (Bonferroni-eligible against the Tomorrow Tests / MW family).
   - Sensitivity run: re-run with top-30 most-cited surahs only (drops syn-only entries).
   - Pre-register the SIGN of ρ BEFORE running against the target feature.
   - NO data-peeking at the target feature's current known distribution before pre-registration.

5. **al-Zarkashī's *tansheeṭ al-sāmiʿ* claim as downstream genre
   prediction (H-CLASSIC-37).** Zarkashī's iltifāt chapter (nawʿ PENDING
   physical verification — see frontmatter retag) asserts that iltifāt's
   function is to activate/refresh the listener's attention. The
   English gloss "activate the listener" is HIGH confidence because it
   is an uncontested stable topos of the balāgha tradition, attested
   across Ibn al-Athīr *Mathal Sāʾir*, Abdel Haleem 1992 BSOAS 55(3),
   and Sohaib Saeed's Itqān translation. **The specific Arabic phrase
   *yunshiṭu l-sāmiʿa wa-yujaddidu nashāṭah* is LOW verbatim confidence
   (classical-scholar 2026-04-12 AMEND-12 retag): it was recall-
   reconstructed as "near-literal," not transcribed from the Arabic
   edition in hand, and is withdrawn from publication until Phase-2
   physical verification returns.** The genre-level prediction (iltifāt
   clusters in exhortative/eschatological more than narrative or legal)
   stands on the doctrinal claim, which is cross-source stable. See
   H-CLASSIC-37 entry in §4a of team-discovery-synthesis.md for the
   pre-registration. **Downstream publications should paraphrase
   ("Zarkashī frames iltifāt as a listener-activation device") rather
   than quote the Arabic phrase verbatim.**

6. **`syn`-tagged per-surah entries are LOW confidence individually.**
   20 of 46 catalog surahs carry `source_tag = syn`, meaning they are
   classical-scholar's inference from the classical category (the
   surah has a plausible iltifāt type by the 6-type typology) rather
   than a direct citation pull from the nawʿ texts consulted. Under
   AMEND-12 these should be treated as LOW individually, not MEDIUM in
   aggregate. **Sensitivity protocol**: downstream ρ-correlation must
   be run in two modes — (a) full n=46 primary, (b) Z+S+S-only n=26
   sensitivity run with `syn` entries dropped. Published findings must
   report BOTH. If the ρ flips sign between modes, the catalog is
   insufficient for the finding. If the sign holds but magnitude
   drops, the reduction factor is the classical-inference-noise
   contribution and should be reported alongside the primary.

7. **Retag memo (AMEND-12 pass, 2026-04-12).** The nawʿ-number slip
   pattern (Burhān "nawʿ 47" plausibly correct in journal/balagha-run-1
   but contradicting the 47-anwāʿ total; Itqān "nawʿ 56" vs "nawʿ 58"
   internal contradiction across files) matches the already-retracted
   "Burhān nawʿ 51" Ḥashr fabrication. Until physical verification
   closes, no external publication should emit a specific iltifāt nawʿ
   number for either Burhān or Itqān. Acceptable forms: "al-Zarkashī's
   iltifāt chapter" / "al-Suyūṭī's iltifāt chapter" / "classical balāgha
   tradition on iltifāt" without a number, or an explicit PENDING tag.
