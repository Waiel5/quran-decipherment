---
run: salah-run-1
phase: B
date: 2026-04-12
agent: Phase-B / salah-theology
target: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/salah-theology.md
---

# Ṣalāh Theology — Run Journal

## Approach

1. Read `docs/master-index.md` briefly to situate Phase-B file format and confirm data paths.
2. Loaded `data/morphology/root-index.json` and queried root `Slw`. Confirmed **99** entries — matches the task spec.
3. Cross-checked neighbours: `SlH`, `Sly`, etc. — `Sly` (25 tokens) is a different root ("roasting in fire", cf. Q 4:10 *ṣilliyy*), **not** Slw; excluded.
4. Parsed full morphology file for `ROOT:Slw` lines. Extracted lemma distribution:
   - Salaw`p: 83 (noun `ṣalāh`)
   - Sal~aY`: 12 (verb II `ṣallā`)
   - muSal~iyn: 3 (active participle `muṣallīn`)
   - muSal~FY: 1 (`muṣallā` — place-noun, Q 2:125)
5. Joined with `quran-text/quran-no-tashkeel.json` for Meccan/Medinan typology: 40 Meccan vs 59 Medinan tokens; 39 vs 51 verses. Corpus-normalised Medinan density ~3.6× Meccan.
6. For prayer-time anchors, pulled Arabic + Sahih-International English for Q 17:78, Q 17:79, Q 2:238, Q 2:239, Q 11:114, Q 50:39-40, Q 20:130, Q 24:58, Q 20:14, Q 33:56, Q 70:22-23, Q 70:34, Q 2:142-150, Q 62:9-10, Q 4:101-103.
7. Posture roots: extracted token counts for `qwm` (660), `sjd` (92), `rkE` (**13**), `dEw` (212). Listed all 13 rkE references explicitly.
8. Qibla: searched for `LEM:qibolap` directly in morphology file. Found exactly **7 instances**: Q 2:142, Q 2:143, Q 2:144, Q 2:145 ×3, Q 10:87. **6/7 inside Q 2:142-145**, confirming the lemma is effectively a Baqarah hapax-cluster.
9. Salah+zakah pair:
   - Built verse sets: Slw (90), zkw (56).
   - Same-verse intersection: **28** (50% of all zakāh verses).
   - Adjacent (±1): 1 additional
   - Within ±3 verses: 32 total.
10. Establish-formula scan: parsed qwm lemmas, identified form-IV lemmas `>aqaAma`, `<iqaAm`, `<iqaAmat`, `m~uqiym`, `muqaAm`. Verses with both a form-IV qwm token and a Slw token: **45 / 90** (exactly half).
11. Q 33:56 morphological check: extracted both tokens — `yuSal~u` (form II impf., line 33:56:4) and `Sal~u` (form II imperative, line 33:56:10). Single verse, same root, two different theological registers (divine/angelic blessing vs. believers' verbal invocation).
12. Q 20:14 morphological check: `S~alaw`pa` (noun accusative), verse fuses ʿ-b-d + Slw + DH-K-R.
13. Q 70:22-23, 34 morphological check: `muSal~iyna` (v22), `SalaAti` (v23, v34). Confirmed *dāʾimūn* is unique collocation.
14. Cross-checks:
    - Plural *ṣalawāt*: only 5 surface forms in whole Quran (Q 2:157, 2:238, 9:99, 22:40, 23:9); only 2 in "prescribed prayers" sense.
    - *Muṣallī* active participle: 3 occurrences (Q 70:22, 74:43, 107:4) — **all Meccan**, all identity-labels of saved vs. hypocritical.

## Key statistics verified

- Total Slw tokens: **99**
- Unique verses: **90**
- Surahs touched: **37** (19 Meccan / 18 Medinan)
- Top 6 surahs by token count: 2 (12), 4 (11), 9 (9), 5 (6), 24 (5), 22 (4) — 47/99 tokens
- Prayer-times: canonical 5 assembled from **≥6 verses**, never enumerated
- Qibla lemma: **7 total, 6 inside Q 2:142-145**
- Ṣalāh+zakāh same-verse: **28 verses** (50% of zakāh occurrences)
- Ṣalāh+dhikr same-verse: 12
- Ṣalāh+sujūd same-verse: 4
- Ṣalāh+rukūʿ same-verse: 3
- "Aqim al-ṣalāh" formula (form-IV qwm + Slw): **45 verses**
- Rukūʿ: **13 tokens, 10 verses** — surprisingly scarce ritual-physical root
- *Muṣallī* active participle: 3 tokens, all Meccan, all identity-labels

## Notable finds / surprises

- The 99 count exactly matches Divine Names count. Flagged as H1 but not tested under null model — needs follow-up against the root-stats.csv distribution.
- Q 33:56 is morphologically unique: same root, same verse, two different theological registers (God+angels *yuṣallūna* vs. believers *ṣallū*). The verse is a single triple-register collision.
- *Dāʾimūn ʿalā ṣalātihim* (Q 70:23) is the only Quranic collocation pairing perpetuity with prayer. Its opposition to *mawqūtan* (Q 4:103) structures the timed/continuous dialectic.
- Ṣalāh is Abrahamic-prophetic: explicit attribution to Moses (20:14), Abraham (14:40, 21:73), Ishmael (19:55), Jesus (19:31), Zachariah (3:39), Luqmān (31:17). Never "originated" by Muhammad in the Quranic frame.
- The Quran lexically *refuses* to name the five prayers. Only Q 24:58 names any specific prayer (fajr + ʿishāʾ). Ẓuhr, ʿaṣr, maghrib are never named. Al-ṣalāh al-wusṭā is named but not identified.

## Open tests flagged

- Null model for ṣalāh-count = 99 (match to Tirmidhī Names list).
- Syntactic-position audit of 45 *aqim al-ṣalāh* instances.
- Cross-correlation of ṣalāh with masjid (m-s-j-d).
- Does the formula *aqīmū al-ṣalāh wa-ātū al-zakāh* have a rhyme-signature or positional pattern?

## Output
- Findings file: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/salah-theology.md` (~2900 words, 10 sections, 6 hypotheses H1-H6).
