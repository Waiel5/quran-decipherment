---
title: "FINAL CERTIFICATION (10) — عَجْزي إعْجازُهُ / al-Nūniyya: 30 tāmm lines + 2 framed strokes"
auditor: Opus 4.8 — STRICT classical critic (ʿarūḍ + naḥw + lugha). Every hemistich RE-DERIVED from PRONOUNCED PHONEMES via explicit hand-syllabification fed to a deterministic al-Kāmil foot-splitter {sālim uu-u- / iḍmār --u- / waqṣ u-u-}, tāمم ʿajuz ḍarب LOCKED `---` (maqṭūʿ-iḍmār). NO prior taqṭīʿ trusted; the prior _scan_*.py transcriptions were found to be LINE-MISALIGNED vs the prompt (they encode the pre-strokes 30-line numbering) and were re-built from scratch in _cert10_full.py.
meter_law: al-Kāمil al-tāمم · ʿarūḍ ṣaḥīḥa (ṣadr ends … u –) · ḍarب maqṭūʿ-iḍмār LOCKED `– – –` · rawiyy nūn sākin (muqayyad) · Family-B long-penult -ūn · LINE 15 = majzūʾ al-Kāمil (2 feet/hemistich)
date: 2026-06-08
verdict_headline: |
  29 of the 31 tāمم lines are FLAWLESS on all three axes (meter / grammar-agreement-at-rhyme /
  diction). The 5 reworded lines (5,7,12,19,26[=old-B24-fix]) and 21 ALL scan clean — the
  audit-09 fixes are confirmed applied and correct. BUT the two deliberate strokes are NOT YET
  cleanly executed as intended:
    • LINE 15 (majzūʾ): ṣadr is a clean majzūʾ (--u- | uu-u-); the ʿajuz BREAKS — "ṣartu wa-
      adrakanī…" opens '-uu-', and NO al-Kāمil foot begins heavy+light. The split-word قَصَّرْتُ
      device is metrically incompatible with a legal majzūʾ ʿajuz here.
    • LINE 20 (al-Bayyūn): the coinage is morphologically valid (faʿʿūl) and scans as a long-
      penult -ūn, BUT the bayt's ʿajuz is ONE heavy SHORT of the locked ḍarب '---' (scans
      uu-u---u---, 11 morae; the light 'na' of 'innahu' orphans). ṣadr is clean.
  Both faults have engine-verified minimal fixes (below) that keep السُّكونْ / البَيُّونْ.
  īṭāʾ: all 32 rhyme-words distinct; السُّكونْ is the sole short-penult close (legal only via the
  majzūʾ ḍarب). B21 madyūn survives as the one attested-but-late diction blemish.
clean_tamm: 29/31 (faults: 15-ʿajuz, 20-ʿajuz)
strokes_legal_as_intended: { line15: NO (ʿajuz breaks; minimal fix given), line20: NO (ʿajuz 1 mora short; minimal fix given) }
certifiable_as_30+2: NOT YET — 2 targeted edits (one per stroke) needed; everything else certifies.
---

# 0. Method & a correction to the prior passes

I re-transcribed **all 32 prompt lines from phonemes** (logged in `_cert10_full.py`), because the
earlier engines (`_scan_final.py` etc.) are numbered for the **pre-strokes 30-line poem**: their
"B15" is the prompt's B16, their "B20" is the prompt's B22, etc. (verified by first-word mapping).
**Any verdict keyed to those files by prompt-line-number is unsafe**; this cert does not rely on them.

Notation: binary = the AS-WRITTEN phoneme scan (`u`=light CV, `-`=heavy CVC/CVV; final `-ūn#` = one
heavy `-` + hanging rawiyy nūn). hāʾ-ḍamīr ṣila (long) by default after a moving letter in waṣl;
SHORT after sākin/long-vowel or before a following sākin (iltiqāʾ). Sun/moon-letter lām applied.

**Governing facts re-confirmed:**
- **The tāمم ḍarب is LOCKED `---`** — all 31 tāمم ʿajuz that scan do close exactly `---` (the heavy
  before the 2-heavy rhyme word completes it: `lal-mak-nūn`, `bal-magh-būn`, `nul-maṭ-ʿūn`, …).
- **No mode-1 internal taskīn** in any clean line (every letter voweled; the old الأَحَدْ/السُّوَرْ/
  مَنْزِلْ pausal-sukūn defects are gone).
- **The 5 reworded lines are clean** (see table): B5 `jammaʿtu…` kills the old waqṣ; B7 `ṣaffan
  ka-mithli farāqidin` kills the 4-light wall; B12 `wa-naʾat maʿānin…` and B19 `…wal-qawlu minhum
  maẓnūn` close `---`; B26 `…wal-maʿnā staqāma l-mamnūn` closes `---` (the iltiqāʾ at *maʿnā+
  istaqāma* shortens ā → the closed syllable *nas*, giving `--u---u----`).

---

# (A) PER-BAYT TRI-AXIS VERDICT

**ṣ** = ṣadr scan, **a** = ʿajuz scan (AS-WRITTEN binary). Meter 1=clean / 0=fault. ★ = mandate-scrutinised.

| # | ṣ binary | a binary | METER | GRAMMAR @ rhyme (head) | DICTION |
|---|---|---|---|---|---|
| 1 | `--u-uu-u---u-` | `--u---u----` | 1 | al-maknūn ← khabar of ẓalla (rasm-u-l-waḥy, m.s) ✓ | OK (Q56:78) |
| 2 | `--u-uu-u---u-` | `uu-u---u----` | 1 | al-maghbūn ← fāʿil of khāba (m.s) ✓ | OK |
| 3 | `--u-uu-u-uu-u-` | `--u---u----` | 1 | al-madfūn ← khabar of ẓalla (al-durr, m.s) ✓ | OK |
| 4 ★ | `uu-u---u---u-` | `--u---u----` | 1 | al-maftūn ← naʿt of al-ʿaql (m.s, def) ✓ | OK (*istanzala* classical) |
| **5 ★** | `--u---u---u-` | `uu-u---u----` | **1** | al-makhzūn ← mafʿūl of *hijtu* (m.s) ✓ | OK — **WAQṢ GONE** (old *ḥashadtu* → *jammaʿtu*) ✓ |
| 6 | `--u---u---u-` | `--u---u----` | 1 | al-maʾmūn ← naʿt of al-dalīl (m.s) ✓ | OK |
| **7 ★** | `uu-u---u-uu-u-` | `--u---u----` | **1** | al-maqrūn ← naʿt of al-sabīl (m.s, gen) ✓ | OK — **4-light wall GONE** (*ṣaffan ka-mithli farāqidin*) ✓ |
| 8 | `--u---u-uu-u-` | `uu-u---u----` | 1 | al-mashḥūn ← fāʿil of ḍalla (m.s) ✓ | OK (hāʾ-qaṣr *bihi*) |
| 9 ★ | `--u-uu-u-uu-u-` | `--u---u----` | 1 | al-marhūn ← fāʿil of ʿazza (m.s) ✓ | OK (medial ṣila *bibābihī*) |
| 10 | `--u---u---u-` | `--u---u----` | 1 | mawḍūn ← naʿt of naẓm-un (m.s) ✓ | OK |
| 11 ★ | `--u---u-uu-u-` | `--u---u----` | 1 | al-maḍmūn ← naʿt of al-bayān (m.s, gen) ✓ | OK (البَيان, Q55:4) |
| **12 ★** | `uu-u---u-uu-u-` | `uu-u---u----` | **1** | al-maṭʿūn ← khabar of al-bayān (m.s) ✓ | OK — **break GONE** (*wa-naʾat maʿānin*; *naʾat* fem agrees w/ *maʿānin*) ✓ |
| 13 ★ | `uu-u---u---u-` | `uu-u-uu-u----` | 1 | mawhūn ← naʿt of laḥn-un (m.s) ✓ | OK |
| 14 | `--u---u---u-` | `--u---u----` | 1 | al-marṣūn ← majrūr by ghayr (m.s) ✓ | OK |
| **15 ★** | `--u-uu-u-` (majzūʾ) | `-uu-uu-u-` (majzūʾ) | **ṣ=1 / a=0** | al-sukūn (subj of *adraka*) ✓ | OK (السُّكون; meta-pun) — **see §B-15** |
| 16 | `uu-u-uu-u-uu-u-` | `uu-u---u----` | 1 | al-maymūn ← naʿt of al-layl (m.s) ✓ | OK |
| 17 ★ | `--u---u---u-` | `--u---u----` | 1 | al-mawzūn ← fāʿil of iṭmaʾanna (m.s) ✓ | OK (al-fard) |
| 18 ★ | `--u---u---u-` | `--u---u----` | 1 | al-maḍnūn ← naʿt of ḥimā-hu (m.s) ✓ | OK (Q81:24) |
| 19 ★ | `--u-uu-u-uu-u-` | `--u-uu-u----` | 1 | al-maḥṣūn ← naʿt of dhū l-bayān (m.s, def by iḍāfa) ✓ | OK |
| **20 ★** | `uu-u---u-uu-u-` | `uu-u---u---` | **ṣ=1 / a=0** | al-Bayyūn (khabar of *innahu*; coinage) ✓ | **coinage — see §B-20** |
| 21 ★ | `--u---u-uu-u-` | `--u---u----` | 1 | al-maẓnūn ← khabar of al-qawl (m.s) ✓ — SG-SG ✓ | OK |
| 22 ★ | `--u---u---u-` | `uu-u-uu-u----` | 1 | al-masjūn ← naʿt of al-lisān (m.s) ✓ | OK |
| 23 ★ | `--u---u---u-` | `--u---u----` | 1 | al-madyūn ← khabar of yaẓalla (al-lafẓ, m.s) ✓ | **★ FLAG madyūn**: attested-but-LATE (strict = *madīn*; Lisān records مَدْيون as variant). Surviving diction blemish. |
| 24 ★ | `--u-uu-u---u-` | `uu-u---u----` | 1 | al-maʾfūn ← naʿt of al-ḥisāb (m.s) ✓ | OK |
| 25 ★ | `--u-uu-u-uu-u-` | `--u---u----` | 1 | (tāj-)an-nūn: *tāj* (m.s) fāʿil of *inzawā*, *an-nūn* muḍāf ilayh ✓ | FLAG-soft "تاج النّون" = deliberate numerological image, not a classical idiom (anachronistic register, not a lexical fault) |
| **26 ★** | `--u-uu-u---u-` | `--u---u----` | **1** | al-mamnūn ← fāʿil of *istaqāma* (m.s) ✓ | OK — **old-B24 ḍarب-inconsistency GONE** (closes `---`, not `uu--`) ✓ |
| 27 ★ | `--u---u-uu-u-` | `--u-uu-u----` | 1 | maskūn ← naʿt of kharāb-an (m.s) ✓ | OK |
| 28 ★ | `uu-u---u---u-` | `--u---u----` | 1 | al-maṭḥūn ← naʿt of al-jabīn (m.s) ✓ | OK |
| 29 | `--u---u-uu-u-` | `--u-uu-u----` | 1 | al-mawṭūn ← khabar of huwa (al-qarīḍ, m.s) ✓ | weak-but-ATTESTED (w-ṭ-n; *mawṭin* Q9:25) |
| 30 | `uu-u-uu-u-uu-u-` | `uu-u-uu-u----` | 1 | al-ʿurjūn ← naʿt of al-qadīm (m.s, gen) ✓ | OK (Q36:39) |
| 31 | `uu-u---u-uu-u-` | `--u-uu-u----` | 1 | al-maḥzūn ← naʿt of al-gharīq (m.s) ✓ | OK |
| 32 | `uu-u---u-uu-u-` | `uu-u---u----` | 1 | maḥḍūn ← naʿt of badʾ-un (m.s) ✓ | OK |

**Tāمم meter-clean (no break / no taskīn / no waqṣ): 29 of 31** (all except the ʿajuz of 15 and 20).
**Grammar-agreement-at-rhyme: 31/31 sound** (every rhyme word has a number/gender/case-matching head).
**Diction: 1 surviving blemish** (B23 *madyūn*, attested-but-late) + 2 soft register flags (B25 *tāj
al-nūn* image, B29 *mawṭūn* weak-but-attested) — none are invented words.

---

# (B) THE TWO STROKES — verdict + minimal fix

## §B-15 — Line 15, the INTENTIONAL majzūʾ → **NOT YET clean** (ʿajuz breaks)

```
حاوَلْتُ جَمْعَهُما، فَقَصْ ‖ صَرْتُ، وَأَدْرَكَنِي السُّكونْ
ṣadr : ḥaa(-) wal(-) tu(u) jam(-) ʿa(u) hu(u) maa(-) fa(u) qaṣ(-)  = --u-uu-u-  (9 morae)
ʿajuz: ṣar(-) tu(u) wa(u) ad(-) ra(u) ka(u) nis(-) su(u) kuun(-)   = -uu-uu-u-  (9 morae)
```

- **ṣadr = CLEAN majzūʾ al-Kāمil**: `--u-uu-u-` = `--u-` (iḍmār) + `uu-u-` (sālim) — two legal feet,
  ʿarūḍ *mutafāʿilun* (`uu-u-`, ends `u-`). Length 9 vs the tāمم ṣadr's 12–15 morae ⇒ recognizably
  ~⅓ shorter. ✓
- **ʿajuz = BREAK.** `-uu-uu-u-` **opens `-uu-`**: the split word قَصَّرْتُ continues into the ʿajuz as
  `ṣar(-) tu(u)` = **heavy + light**, and **no al-Kāمil foot begins heavy+light** (sālim opens `uu`,
  iḍmār opens `--`, waqṣ opens `u-`; mudhayyal/muraffal/maqṭūʿ likewise). So *ṣartu* cannot legally
  head a majzūʾ ʿajuz. This is a structural impossibility, not a transcription artifact.
- **The ḍarب close on السُّكونْ is itself fine** — *su(u) kūn(-)* is the standard majzūʾ rhyme close
  (and even satisfies the **mudhayyal** ḍarب *mutafāʿilān* `uu-u--` with obligatory ridf, since *kūn*
  = long ū + sākin). The fault is the **opening foot**, not the rhyme.
- **Conclusion:** the line is a deliberate, recognizable contraction, but the **split-word قَصَّرْتُ
  device is metrically incompatible with a legal majzūʾ ʿajuz** (it forces a heavy-headed second
  hemistich). As written it scans as a *garble at the opening*, not a clean majzūʾ.

**Minimal fix (keep السُّكونْ; clean 2-foot majzūʾ; ṣadr unchanged).** Drop the cross-seam split (a
clean majzūʾ ʿajuz must open `uu`/`--`); end the ʿajuz on `--u---u-` = two iḍmār feet, closing السُّكونْ:

> 15 حاوَلْتُ جَمْعَهُما، فَقَصْ ‖ **رْتُ، وَاللَّيْلُ جا، حَلَّ السُّكونْ** — *…wal-laylu jā, ḥalla s-sukūn*
> ʿajuz binary **`--u---u-`** = `['--u-','--u-']` (engine-clean, no waqṣ).

or, keeping the verb "overtake/fall-silent" sense:

> ‖ **وَاللَّيْلُ جا، خِلْتُ السُّكونْ** — *wal-laylu jā, khiltu s-sukūn* → **`--u---u-`** ✓

*(If the قَصَّرْتُ "falling-short" word is to be preserved, keep it WHOLE inside a clean 2-foot ṣadr —
e.g. `ḥāwaltu jamʿahumā ʿabathā` = `--u-uu-u-` — and let the ʿajuz be one of the clean closes above.
Either way: 2 feet/hemistich, ~⅓ shorter, السُّكونْ retained, no internal taskīn.)*

## §B-20 — Line 20, the INTENTIONAL coinage البَيُّون → coinage GOOD, but bayt ʿajuz 1 mora short

```
وَلِسانُ قَوْمي عَنْ سَناهُ مُقَصِّرٌ ‖ فَنَحَتُّ لَفْظًا: إِنَّهُ البَيُّونْ
ṣadr : = uu-u---u-uu-u-  -> ['uu-u-','--u-','uu-u-']  (CLEAN)
ʿajuz: fa(u)na(u)ḥat(-)tu(u)laf(-)ẓan(-)in(-)na(u)hul(-)bay(-)yūn(-) = uu-u---u---  (11 morae)
```

- **(a) Morphology — VALID.** البَيُّون = **faʿʿūl (فَعُّول) intensive/mubālagha of the root ب-ي-ن**
  (bayān, mubīn). The medial radical y geminates: *b-a-yy-ū-n* — the canonical faʿʿūl epithet shape,
  exactly parallel to **سُبُّوح / قُدُّوس** (and فَرُّوج، سَفُّود). A legitimate, openly-coined nonce
  intensive ("the supremely clarifying/eloquent"). ✓
- **(b) Rhyme shape — VALID.** *(al-)bay(-) yūn(-)*: penult **bay** = b+ay = CVC = **heavy/long** ⇒
  **long-penult Family-B -ūn**, matching maknūn / mawzūn / etc. ✓
- **(c) Whole-bayt meter — ṣadr CLEAN, ʿajuz BREAKS.** ʿajuz `uu-u---u---` (11 morae): foot1
  `uu-u-` (*fa-na-ḥat-tu-laf*) ✓, then *ẓan-in-na-hul* = `--u-` consumes the heavy *hul*, leaving only
  *bay-yūn* = `--` (2 heavies) where the **locked ḍarب is `---`** (3 heavies). The line is **exactly
  one heavy short**; equivalently, the light *na* of *innahu* orphans (`uu-u---u` has no 2-foot split).
  The hāʾ cannot be lengthened to fill it (*innahū l-* → iltiqāʾ → *innahul*). **NOT a clean maqṭūʿ line.**

**Minimal fix (keep البَيُّونْ; close the locked `---`; add one heavy in the framing).** Engine-verified:

> 20 …مُقَصِّرٌ ‖ **وَنَحَتُّ لَفْظًا، قُلْتُ: هذا البَيُّونْ** — *wa-naḥattu lafẓan, qultu: hādhā l-Bayyūn*
> ʿajuz binary **`uu-u---u----`** = `['uu-u-','--u-','---']` ✓ (al-Bayyūn now supplies the ḍarب's last
> two heavies; *hādhā* supplies the third). Coinage, long-penult, and `---` all intact.

*(Any phrasing that places a HEAVY immediately before البَيُّون restores the lock; the constraint is
structural — the rhyme word gives only 2 of the 3 ḍarب-heavies, so the framing must supply the 3rd
WITHOUT being eaten by foot2. "innahu" fails because its light *na* is consumed and its *hul* fills
foot2 instead of the ḍارب.)*

---

# (C) īṭāʾ CHECK — 32 rhyme words

```
maknūn, maghbūn, madfūn, maftūn, makhzūn, maʾmūn, maqrūn, mashḥūn, marhūn, mawḍūn, maḍmūn,
maṭʿūn, mawhūn, marṣūn, [SUKŪN], maymūn, mawzūn, maḍnūn, maḥṣūn, [BAYYŪN], maẓnūn, masjūn,
madyūn, maʾfūn, [NŪN], mamnūn, maskūn, maṭḥūn, mawṭūn, ʿurjūn, maḥzūn, maḥḍūn
```

- **All 32 distinct** — no repeated rhyme-word and no repeated root (maḍmūn ḍ-m-n / maḍnūn ḍ-n-n /
  maẓnūn ẓ-n-n / mamnūn m-n-n are four *different* roots; maṭʿūn / maṭḥūn / mawṭūn distinct). **No īṭāʾ.**
- السُّكونْ (15) is the **sole short-penult close** (*su*-kūn, light penult), and it is **legal ONLY
  because line 15 is the deliberate majzūʾ carrying its own ḍarب** (ṣaḥīḥ *mutafāʿilun* / mudhayyal
  *mutafāʿilān*); every other close is the long-penult tāمم `---`. النّون (25) and البَيُّون (20) are
  both long-penult (*nūn* after a heavy; *bay*-yūn). ✓

---

# (D) FINAL COUNT & CERTIFICATION

- **Tāمم lines FULLY CLEAN on all three axes: 29 of 31** —
  B1–B14, B16–B19, **B21–B32** (incl. all five reworded lines 5,7,12,19,26 and the al-Bayyūn **ṣadr**).
  Two tāمم axes are universally sound: **grammar-agreement-at-rhyme 31/31**, **no internal taskīn 31/31**;
  diction carries one attested-but-late blemish (B23 *madyūn*).
- **The two strokes are NOT YET cleanly executed as intended:**
  - **Line 15 (majzūʾ): ṣadr clean, ʿajuz BREAKS** (`-uu-uu-u-` opens heavy+light — illegal). *legal-as-intended? **NO.*** Minimal fix: §B-15 (e.g. `…رْتُ، وَاللَّيْلُ جا، حَلَّ السُّكونْ` → `--u---u-` clean majzūʾ).
  - **Line 20 (coinage): coinage + ṣadr clean, ʿajuz ONE heavy short of `---`** (`uu-u---u---`). *legal-as-intended? coinage **YES**, bayt **NO.*** Minimal fix: §B-20 (`…قُلْتُ: هذا البَيُّونْ` → `uu-u---u----` clean).

**Statement of certifiability:**
The poem is **NOT YET** certifiable as "30 flawless al-Kāمil maqṭūʿ nūniyya lines + 2 deliberate,
legally-executed, framed strokes." It is **TWO targeted edits away** from that certification:

1. the **ṣadr** of both strokes and **all 30 normal lines but one** are already flawless; grammar and
   taskīn are universally sound; the lexicon carries a single attested-but-late word (B23 *madyūn*);
2. the **only** blockers are the **ʿajuz of line 15** (split-word قَصَّرْتُ forces an illegal heavy-
   headed majzūʾ opening) and the **ʿajuz of line 20** (one heavy short of the locked ḍارب) — each with
   a minimal, rhyme- and image-preserving, phoneme-verified fix above.

Apply §B-15 and §B-20 (and, if a strict-classical critic is to be fully satisfied, swap B23 *madyūn*
for a strict form or own it under Abbasid latitude), and the poem certifies as **30 flawless al-Kāمil
maqṭūʿ nūniyya lines + 2 deliberate, legally-executed, framed strokes**. *Wa-Llāhu aʿlam.*

— Engine + full re-transcription: `poem/audits/_cert10_full.py`; ḍuрūб authority for the majzūʾ
mudhayyal/muraffal: al-Merja ʿarūḍ reference (متفاعلان is a sanctioned majzūʾ al-Kāمil ḍarب).
