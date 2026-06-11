---
title: "Strict Tri-Axis Audit (09) — عَجْزي إعْجازُهُ, the post-(08)-correction 30 abyāt"
auditor: Opus 4.8 — strict classical critic (ʿarūḍ + naḥw + lugha). Re-derived every hemistich from PRONOUNCED PHONEMES via an explicit hand-syllabification (logged per hemistich) fed to a deterministic brute-force al-Kāمил foot-splitter {ṣaḥīḥ uu-u- / iḍmār --u- / waqṣ u-u-} with the LOCKED maqṭūʿ-iḍмār ḍarب `– – –`. Trusted NO prior taqṭīʿ (audits 01–08). Engine + transcriptions in poem/audits/_scan_*.py.
meter_law: al-Kāمil al-tāمم · ʿarūḍ ṣaḥīḥa (ṣadr ends … u –) · ḍarب maqṭūʿ-iḍмār LOCKED `– – –` · rawiyy nūn sākin (muqayyad) · Family-B long-penult -ūn
date: 2026-06-08
hāʾ_policy: |
  The hāʾ-ḍamīr after a MOVING (voweled) letter takes its ṣila (ishbāʿ) by DEFAULT in waṣl —
  both line-end (‑hu→‑hū, ‑hi→‑hī) AND medially (bi-bābi-HĪ). It is SHORT only (a) after a
  sākin/long vowel (fīhi, ʿanhu, ʿalayhi), (b) before a following sākin where ishbāʿ would
  create iltiqāʾ al-sākinayn (bihi l-lisān → bi-HIL), or (c) by licensed qaṣr where the long
  form would break the foot (a ḍarūra ḥasana, not the ugly taskīn). This policy CORRECTS audit-08,
  which mis-scanned B9 as a hard break by keeping the medial bābihi short before a moving mīm.
verdict_headline: |
  Re-derived from phonemes on all three axes. The (08) corrections RESOLVED the entire GRAMMAR-at-
  rhyme axis (all 30 rhyme words now have a masc-sing head: B19→maqāl, B20→al-lisān, B22→al-ḥisāb,
  B25→kharāb all agree) and 2 of 3 diction faults (لَفيظ and المَعْنَوِيّ both GONE; al-waḥd→al-fard).
  But 5 METER faults remain — 4 hard BREAKS introduced/left by the reword (B7-ṣ 4-light junction,
  B12-a وَنَأى-wall, B19-a orphan close, B24-a sound-maqṭūʿ ḍarب that violates the `– – –` lock)
  plus 1 WAQṢ ṣadr (B5, qabīḥ). 1 DICTION blemish survives (B21 madyūn: Abbasid-acceptable,
  strict-classical dispreferred). FULLY CLEAN on all three axes: 24 of 30. Each fault has a
  machine-verified minimal fix that keeps the Family-B `-ūn` rhyme word and the image.
clean_count: 24/30
still_need_touch: [5, 7, 12, 19, 24, 21]   # 5 meter (incl. B5 waqṣ) + B21 diction
---

# 0. Governing facts (re-confirmed from phonemes)

- **FACT 1 — the ḍarب is LOCKED at `– – –` (maqṭūʿ-iḍмār).** 29 of 30 ʿajuz close exactly `– – –`. The **sole exception is B24**, which closes `u u – –` — the *sound* maqṭūʿ مُتَفاعِلْ (no iḍmār). `uu--` is independently a legal al-Kāمil maqṭūʿ ḍarب, BUT a qaṣīda must keep ONE ḍarب throughout; a single line on `uu--` against 29 on `---` is an **ikhtilāf al-ḍarب** (ḍarب-inconsistency) = a break against the lock. The بِ of *bi-mamnūn* is what supplies the illegal light head. (Verified: tail-of-ʿajuz table, all 30.)
- **FACT 2 — the hāʾ-ḍamīr ṣila is LEGAL and is NOT taskīn** (see `hāʾ_policy`). 12 lines use the line-end ṣila; **B9 uses it medially** (bi-bābi-HĪ, hāʾ preceded by moving bāʾ, followed by moving mīm → ishbāʿ applies → CLEAN). B8 uses the licensed *qaṣr* (short *bihi tāha*) — a ḍarūra ḥasana, passed.
- **FACT 3 — mode-1 internal taskīn is FULLY ABSENT.** I tested every clean line for a hidden silencing of a normally-voweled letter mid-hemistich: NONE. The prior version's الأَحَدْ / السُّوَرْ / مَنْزِلْ taskīn are all gone (this version reads لِلْواحِدِ الفَرْدِ, سُوَرُ الهُدى, مَنازِلُ — every letter voweled). No clean line scans by taskīn.

---

# (A) PER-BAYT TRI-AXIS TABLE

Notation: **ṣ**=ṣadr scan, **a**=ʿajuz scan (binary = the AS-WRITTEN phoneme scan, hāʾ-policy applied). **sila**=legal hāʾ-ḍamīr lengthening (Fact 2). ★=line the mandate told me to scrutinize. Meter "1/0": **1**=clean, **0**=fault (with the shape).

| # | METER ṣ | METER a | GRAMMAR @ rhyme (head named) | DICTION |
|---|---|---|---|---|
| 1 | 1 `--u-uu-u---u-` | 1 `--u---u----` | **al-maknūn** khabar of *ẓalla*; ism=*rasm-u-l-waḥy* (m.s) ✓ | OK (Q56:78 *maknūn*) |
| 2 | 1 sila *mithlahū* `--u-uu-u---u-` | 1 `uu-u---u----` | **al-maghbūn** fāʿil of *khāba* (m.s) ✓ | OK |
| 3 | 1 sila *qarārahū* `--u-uu-u-uu-u-` | 1 `--u---u----` | **al-madfūn** khabar of *ẓalla*; ism=*al-durr* (m.s) ✓ | OK |
| 4 ★ | 1 sila *-tuhū* `uu-u---u---u-` | 1 `--u---u----` | **al-maftūn** naʿt of *al-ʿaql* (m.s, def) ✓ | OK (*istanzala* classical; sense brushes waḥy but lexical-fine) |
| 5 ★ | **0 WAQṢ@foot1** `u-u---u---u-` — *ḥa-shad-tu* = مُفاعِلن (`u – u –`); legal-but-**qabīḥ** | 1 `uu-u---u----` | **al-makhzūn** mafʿūl of *hijtu* (m.s) ✓ | OK (over-active but attested) |
| 6 | 1 `--u---u---u-` | 1 `--u---u----` | **al-maʾmūn** khabar/naʿt of *al-dalīl* (m.s) ✓ | OK |
| 7 ★ | **0 BREAK** `uu-u-u-uuuu-u-` — *manāzilu* (`u – u u`) + *ka-farāqidin* (`u u – u –`) = a **4-light junction** *zi-lu-ka-fa* (`u u u u`); no al-Kāمil foot spans it. NOT taskīn. | 1 `--u---u----` | **al-maqrūn** naʿt of *al-sabīl* (m.s, gen) ✓ | OK (*farāqid* classical) |
| 8 | 1 `--u---u-uu-u-` | 1 hāʾ-qaṣr *bihi* `uu-u---u----` | **al-mashḥūn** fāʿil of *ḍalla* (m.s) ✓ | OK |
| 9 ★ | **1** sila-**medial** *bibābihī* `--u-uu-u-uu-u-` (CORRECTS audit-08's false break) | 1 `--u---u----` | **al-marhūn** fāʿil of *ʿazza* (m.s) ✓ | OK |
| 10 | 1 sila *nasjihī* `--u---u---u-` | 1 `--u---u----` | **mawḍūn** naʿt of *naẓm-un* (m.s) ✓ | OK |
| 11 ★ | 1 `--u---u-uu-u-` | 1 `--u---u----` | **al-maḍmūn** naʿt of *al-bayān* (m.s, gen) ✓ | **OK — لَفيظ ELIMINATED** ✓ (البَيان, Q55:4) |
| 12 ★ | 1 sila *maʿīnuhū* `uu-u---u-uu-u-` | **0 BREAK** `uu----u----` — *wa-naʾā l-maʿnā* packs `u u – – –` (a `----` wall after the watid); no foot. (The reword وَنَأى المَعْنى broke the audit-08 scanning form.) | **al-maṭʿūn** khabar of *al-bayān* (m.s) ✓ | OK |
| 13 ★ | 1 sila *aʿmāqihī* `uu-u---u---u-` | 1 `uu-u-uu-u----` | **mawhūn** naʿt of *laḥn-un* (m.s) ✓ | **OK — المَعْنَوِيّ ELIMINATED** ✓ (لَحْن/رَنين/مَوْهون classical) |
| 14 | 1 `--u---u---u-` | 1 `--u---u----` | **al-marṣūn** majrūr by *ghayr* (m.s) ✓ | OK |
| 15 | 1 `uu-u-uu-u-uu-u-` | 1 `uu-u---u----` | **al-maymūn** naʿt of *al-layl* (m.s) ✓ | OK |
| 16 | 1 `--u---u---u-` | 1 `--u---u----` (*fardi-ṭmaʾanna* merges) | **al-mawzūn** fāʿil of *iṭmaʾanna* (m.s) ✓ | OK (**الأَحَد taskīn GONE** ✓) |
| 17 ★ | 1 sila *lahū* `--u---u---u-` | 1 `--u---u----` | **al-maḍnūn** khabar/naʿt of *ḥimā-hu* (m.s) ✓ | **OK — al-waḥd→al-fard** ✓ (*ḥimā* + *maḍnūn* ḍ-n-n classical, Q81:24) |
| 18 ★ | 1 sila *mithluhū* `--u-uu-u-uu-u-` | 1 `--u-uu-u----` | **al-maḥṣūn** naʿt of *dhū l-bayān* (m.s) ✓ — **clean predicate**: ذو (m.s., def by iḍāfa) + def. naʿt المَحْصون | OK (filler aesthetically, per ChatGPT; not a fault) |
| 19 ★ | 1 `--u---u-uu-u-` | **0 BREAK** `--u-uu-u---` — *fa-maqāluhum maẓnūn* leaves either an orphan `– –` (one mora shy of the ḍarب `– – –`) or an illegal `uu-u` foot; no parse. NOT taskīn. | **maẓnūn** khabar of *maqāl-uhum* (m.s) ✓ — **GRAMMAR FIXED** (was al-muddaʿūn PL + maẓnūn SG) | OK |
| 20 ★ | 1 sila *bihī* `--u---u---u-` | 1 `uu-u-uu-u----` | **al-masjūn** naʿt of *al-lisān* (m.s) ✓ — **NUMBER FIXED** (was al-ʿārifīn PL) | OK |
| 21 ★ | 1 `--u---u---u-` | 1 `--u---u----` | **al-madyūn** khabar of *yaẓalla*; ism=*al-lafẓ* (m.s) ✓ | **★ FLAG — madyūn: Abbasid-acceptable / strict-classical DISPREFERRED.** Strict form *madīn* (دانَ/يَدين). Lisān records مَدْيون as a *variant* (NOT invented). A mukhaḍram critic refuses it; an Abbasid one tolerates it. **SURVIVING diction blemish.** |
| 22 ★ | 1 `--u-uu-u---u-` | 1 `uu-u---u----` | **al-maʾfūn** naʿt of *al-ḥisāb* (m.s) ✓ — **NUMBER FIXED** (was al-qawm *humu* PL) | OK (maʾfūn ʾ-f-n classical) |
| 23 ★ | 1 `--u-uu-u-uu-u-` (*suwaru* proper, no taskīn) | 1 `--u---u----` | **(tāj-)an-nūn**: *tāj* (m.s) fāʿil of *inzawā*, *an-nūn* muḍāf ilayh ✓; *naẓma l-hudā* accus. mafʿūl of *aghfalū* ✓ | **FLAG-soft — تاج النّون**: grammar clean, but "crown of the nūn" is **not a classical idiom** — a deliberate modern/numerological IMAGE (the thesis-beat), not a non-word. Anachronistic register, not a lexical fault. |
| 24 ★ | 1 sila *bismihī* `--u-uu-u---u-` | **0 BREAK** `--u---u-uu--` — close *fa-laysa bi-mamnūn* = `u u – –` = the **sound maqṭūʿ**, NOT the locked muḍmar `– – –`. The بِ (zāʾida) supplies an illegal light head. **Ḍarب-inconsistency** (Fact 1). | **bi-mamnūn** khabar of *laysa* (majrūr bi-bāʾ zāʾida); ism=*al-lafẓ/al-musammā* (m.s) ✓ — **DUAL FIXED** (was *laysā…mamnūn*) | OK |
| 25 ★ | 1 `--u---u-uu-u-` | 1 `--u-uu-u----` | **maskūn** naʿt of *kharāb-an* (m.s) ✓ — **GENDER FIXED** (was *dār* FEM + maskūn) | OK (kharāb classical) |
| 26 | 1 `uu-u---u---u-` | 1 `--u---u----` | **al-maṭḥūn** naʿt of *al-jabīn* (m.s) ✓ | OK (tonally modern per critics; attested) |
| 27 ★ | 1 `--u---u-uu-u-` | 1 `--u-uu-u----` | **al-mawṭūn** khabar of *huwa* (→*al-qarīḍ*, m.s) ✓ | **weak-but-ATTESTED** (w-ṭ-n; *mawṭin* Q9:25; ism-mafʿūl of *waṭana* rare yet regular — NOT failed) |
| 28 ★ | 1 `uu-u-uu-u-uu-u-` (*suwaru* proper) | 1 `uu-u-uu-u----` | **al-ʿurjūn** naʿt of *al-qadīm* (m.s, gen) ✓ | OK (Q36:39; **السُّوَرْ taskīn GONE** ✓) |
| 29 | 1 sila *muthīruhū* `uu-u---u-uu-u-` | 1 `--u-uu-u----` | **al-maḥzūn** naʿt of *al-gharīq* (m.s) ✓ | OK |
| 30 | 1 sila *khitāmihī* `uu-u---u-uu-u-` | 1 sila *qaraʾtuhū* `uu-u---u----` | **maḥḍūn** naʿt of *badʾ-un* (m.s) ✓ | OK (idiom repaired: *rajaʿtu naḥwa l-badʾ*) |

---

# (B) REMAINING-FAULT LIST + minimal verified fix (each keeps Family-B `-ūn` + image)

Every fix below was re-derived from phonemes and machine-verified to land the legal close (binary cited).

### Meter — hard BREAK (4 bayts)

- **B7-ṣ** — 4-light junction *manāzilu* + *ka-farāqidin* (`…zi-lu-ka-fa` = `u u u u`). *manāzil* is **diptote** (mamnūʿ min al-ṣarf), so it cannot take tanwīn to fix it; the cure must close the syllable after it OR restructure.
  **FIX:** `وَتَنَظَّمَتْ صَفًّا كَمِثْلِ فَراقِدٍ` — *wa-tanaẓẓamat ṣaffan ka-mithli farāqidin* → **`uu-u---u-uu-u-`** ✓.
  (*ṣaffan* = accus. ḥāl "in a row"; *farāqid* genitive after *ka-mithli*. Keeps the ranked-guard-stars image; grammar + diction clean.)

- **B12-a** — *wa-naʾā l-maʿnā* packs `u u – – –` (a `----` wall); no foot. The reword **وَنَأى المَعْنى** broke the scanning form.
  **FIX (strict, fem-agreeing):** `وَنَأَتْ مَعانٍ، وَالبَيانُ المَطْعونْ` — *wa-naʾat maʿānin wal-bayānu l-maṭʿūn* → **`uu-u---u----`** ✓ (*naʾat* fem agrees with *maʿānin* = jamʿ ghayr ʿāqil; cures meter AND the masc-verb worry).
  **FIX (alt, definite):** `وَنَبا المَعاني، وَالبَيانُ المَطْعونْ` — *wa-nabā l-maʿānī…* → **`uu-u---u----`** ✓ (masc verb before a fronted broken-plural subject is classically licensed; keeps المَعاني definite). Either passes all three axes; the fem form is the stricter choice.

- **B19-a** — *fa-maqāluhum maẓnūn* orphans at `– –` (one mora shy of `– – –`).
  **FIX:** `عَجْزٌ بِهِمْ، وَالقَوْلُ مِنْهُمْ مَظْنونْ` — *ʿajzun bihim, wal-qawlu minhum maẓnūn* → **`--u---u----`** ✓ (*al-qawl* m.s. supplies the heavy head before *maẓnūn*; grammar SG-SG ✓; keeps المَظْنون + the "their-speech-is-conjecture" sense).

- **B24-a** — close *fa-laysa bi-mamnūn* = `u u – –` (sound maqṭūʿ) breaks the locked `– – –` (Fact 1).
  **FIX:** `وَاللَّفْظُ وَالمَعْنى اسْتَقامَ المَمْنونْ` — *wal-lafẓu wal-maʿnā staqāma l-mamnūn* → **`--u---u----`** ✓ (drops the light-making بِ; *istaqāma* supplies a heavy head; *al-mamnūn* fāʿil m.s.; keeps the welded-word-and-meaning image + the -ūn rhyme).
  *(If "istaqāma l-mamnūn" reads thin, any phrase placing a HEAVY immediately before مَمْنون restores the lock; the constraint is structural, not semantic.)*

### Meter — WAQṢ (qabīḥ, 1 bayt)

- **B5-ṣ** — opens *ḥa-shad-tu* = مُفاعِلن (`u – u –`, waqṣ) at foot-1; legal but **qabīḥ** (the poem uses no other waqṣ).
  **FIX:** `جَمَّعْتُ أَقْلامي وَجَرَّدْتُ القُوى` — *jammaʿtu aqlāmī wa-jarradtu l-quwā* → **`--u---u---u-`** ✓ (opens iḍmār, kills the waqṣ; *jammaʿa* Form-II "to amass" classical; same nouns/sense, one-verb swap). [Alt verified: `سَلَّلْتُ أَقْلامي…` *sallaltu* "I unsheathed my pens" → `--u---u---u-` ✓.]

### Diction — late form (1 bayt)

- **B21** — **madyūn**: Abbasid-acceptable, strict-classical dispreferred (strict = *madīn*). Lisān records it as a variant, so NOT invented. **If the Family-B -ūn lock is absolute,** the cleanest options are (a) **accept madyūn** under Abbasid latitude (the register the whole poem actually occupies — لفظ/معنى/نظم are 5th-c. critical terms), explicitly owning it; or (b) recast the line to drop the debt-image for a fresh unused attested -ūn root, since the obvious substitutes (المَفْتون B4, المَرْهون B9, المَظْنون B19) are already spent (→ īṭāʾ). **Honest call:** madyūn is the single surviving diction blemish; it is *attested-but-late*, not an invented word like the now-purged لَفيظ.

### (soft, not failed)
- **B23 tāj al-nūn** — grammar clean; "crown of the nūn" is a deliberate modern/numerological image, not a classical idiom. Anachronistic register (consistent with the poem's Abbasid-critical content), not a lexical fault. Leave if the thesis-beat is wanted; it is the one overt place the poem "talks like a spreadsheet."
- **B27 mawṭūn / B26 maṭḥūn / B18 dhū l-bayān** — attested; critics call them weak/filler (aesthetic), not non-attested. NOT failed on the diction axis.

---

# (C) FINAL COUNT

**FULLY CLEAN on ALL THREE axes (meter incl. legal ṣila + no taskīn / grammar-agreement at the rhyme / diction): 24 of 30** —
**B1, B2, B3, B4, B6, B8, B9, B10, B11, B13, B14, B15, B16, B17, B18, B20, B22, B23†, B25, B26, B27, B28, B29, B30.**
(†B23 passes meter+grammar+lexical-attestation; the "tāj al-nūn" *image* is flagged soft as anachronistic register, not a hard diction fault. B9 is the audit-08 → audit-09 self-correction: clean under the medial-hāʾ ṣila.)

**STILL NEED A TOUCH (6 of 30):**

| axis | bayts | nature | one-line fix |
|---|---|---|---|
| **Meter — hard BREAK** | **7, 12, 19, 24** | 7-ṣ 4-light *manāzilu-kafarāqidin* · 12-a *naʾā* `----` wall · 19-a orphan close `– –` · 24-a sound-maqṭūʿ `uu--` vs locked `---` | ṣaffan ka-mithli farāqidin / wa-naʾat maʿānin / wal-qawlu minhum maẓnūn / wal-lafẓu wal-maʿnā staqāma l-mamnūn |
| **Meter — WAQṢ (qabīḥ)** | **5** | 5-ṣ مُفاعِلن at foot-1 (*ḥashadtu*) | جَمَّعْتُ أَقْلامي … |
| **Diction (late form)** | **21** | madyūn (Abbasid-ok / strict-dispreferred; *madīn* is strict) | accept under Abbasid latitude OR recast off the debt-image |

## What the (08) corrections genuinely achieved vs. what they broke (re-verified from phonemes)

1. **GRAMMAR-at-rhyme axis — FULLY RESOLVED.** All 30 rhyme words now carry a masc-sing head. The four prior mismatches are fixed: **B19** muddaʿūn(PL)→**maqāl**(SG); **B20** ʿārifīn(PL)→**al-lisān**(SG); **B22** *humu*(PL)→**al-ḥisāb**(SG); **B25** dār(FEM)→**kharāb**(MASC); **B24** *laysā*(dual)→*fa-laysa bi-mamnūn*(sg). No agreement fault survives.
2. **DICTION axis — 2 of 3 fixed.** **لَفيظ** (invented) → البَيان ✓; **المَعْنَوِيّ** (post-classical substantive) → لَحْن/رَنين ✓; al-waḥd → al-fard ✓. **madyūn (B21) left in** — attested-but-late.
3. **Mode-1 internal taskīn — ABSENT** (الأَحَد / السُّوَرْ / مَنْزِلْ all gone; B9's medial lengthening is the legal ṣila, not taskīn).
4. **NEW/LEFT meter faults from the reword (the cross-cutting irony again):** **B7** (the indefinite *kafarāqidin* is right, but *manāzilu* before it makes a 4-light wall — the noun, not the article, is the problem); **B12** (وَنَأى المَعْنى replaced the scanning نَبا/نَأت form and built a `----` wall); **B24** (*bi-mamnūn*'s بِ light-heads the ḍarب off the lock); **B5** waqṣ left unfixed. All four are side-effects of grammar/diction edits, each repairable without touching the rhyme.

## Self-corrections vs prior passes
- **(a) audit-08 scored B9-ṣ a hard BREAK** ("bibābihi mutahayyiban 4-light junction"). **WRONG** — the medial hāʾ-ḍamīr after a moving bāʾ, followed by a moving mīm, takes its ṣila by default (bi-bābi-**hī**); the line scans `--u-uu-u-uu-u-` CLEAN. B9 is clean; this audit fixes the over-call.
- **(b) audit-08 listed B20/B22 as still partly faulty.** Re-derived: **B20** *al-lisānu l-masjūn* (the prompt's wording) is grammar-clean (al-lisān SG) AND scans `uu-u-uu-u----`; **B22** *al-ḥisābi l-maʾfūn* is grammar-clean AND scans. Both pass now.
- **(c) B24's break is a ḍarب-uniformity fault, not a length fault** — the ʿajuz is the right length but closes on the *sound* maqṭūʿ `uu--` instead of the locked muḍmar `---`. Flagged precisely (Fact 1), since `uu--` is otherwise a legal al-Kāmil ḍarب and a coarse scan would pass it.

**Bottom line:** the poem is **NOT yet uniformly clean on all three axes.** **24/30** pass meter AND grammar AND diction; **6** need a touch (4 hard-meter breaks, 1 waqṣ, 1 late-diction). Grammar-at-rhyme is now fully sound; diction is down to one attested-but-late word; the residue is meter — and every one of the five meter faults has a minimal, rhyme-and-image-preserving, phoneme-verified fix above. *Wa-Llāhu aʿlam.*
