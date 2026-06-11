---
title: "ʿArūḍ Lock-Audit v4 (06) — the 9 newly-crafted bayts of MASTER v4"
auditor: independent ʿarūḍī pass (Opus 4.8) — re-derived every hemistich of the 9 from pronounced phonemes; trusted no prior taqṭīʿ (incl. v3 audit 05)
meter_law: al-Kāmil al-tāmm · ʿarūḍ ṣaḥīḥa (ṣadr ends … u –) · ḍarب maqṭūʿ-iḍмār LOCKED `– – –` · rawiyy nūn sākin (muqayyad) · Family-B long-penult -ūn
date: 2026-06-08
source_of_truth: poem/drafts/master-v4.md §"THE POEM" (Arabic authoritative)
scope: ONLY bayts 1, 3, 8, 9, 10, 20, 21, 23, 28 (the "NEWLY HAND-CRAFTED LINES"); other 21 carry their v3 (audit-05) verdicts unchanged
method: letter-level binary 1/0 string (1=mutaḥarrik, 0=sākin: sukūn/madd/tanwīn-nūn/first-half-shadda) → deterministic syllabifier (1=`u`, 10=`–`; trailing `…100`=super-heavy -ŪN# close = one `–`+hanging rawiyy) → brute-force al-Kāmil foot split {ṣaḥīḥ `uu-u-`, muḍmar `--u-`}+locked ḍarب `---`. Strings cited per failure.
verdict_headline: 4 of the 9 break as written (B3-ʿajuz, B8-ʿajuz, B20-ʿajuz, B21-ṣadr); 5 are CLEAN (B1, B9, B10, B23, B28). After 4 minimal fixes — each verified to land the locked `– – –` (or a ṣaḥīḥ ṣadr ending u–), same Family-B -ūn rhyme word, same archaic image — all 9 scan uniform. Zero īṭāʾ across the 30.
---

# 0. Governing facts (carried from audit-05, re-confirmed from phonemes)

**FACT 1 — the locked ḍarب is `– – –`** (mutfāʿil = maqṭūʿ+iḍмār). Every clean ʿajuz in the 9 lands exactly `– – –`; none lands the bare-sound `u u – –`. All ʿajuz fixes target `– – –`.

**FACT 2 — the hāʾ al-ḍamīr takes its ṣila and lengthens (`-hu→-hū`, `-hi→-hī`) after a moving letter at line-end.** Within the 9, the **B3 ṣadr** (*qarārahū*), **B20 ṣadr** (*lākinnahū*) and **B23 ṣadr** (*yaẓunnuhū*) scan ONLY with this lengthening. Clean, not defects — but the reciter must hold them long.

**FACT 3 — v4 silently reverted two of audit-05's verified ʿajuz rewords.** The v4 header claims "ArudFinal's verified rewords (3, 6, 8, 9, 10, 12, 19, 21, 23)," but the printed text of **B3-ʿajuz** (`…في غَمْرِ الغَوارِبِ مَدْفونْ`) and **B8-ʿajuz** (`تاهَ الخِرّيتُ، وَضَلَّ رَكْبٌ مَشْحونْ`) are the **pre-fix originals**, not the audit-05 rewords. They break exactly as audit-05 diagnosed (B3 = orphaned close after a `u u` bunch; B8 = wall of four heavies `– – – –`). The audit-05 fixes simply need to be re-applied. (B9, B10, B21, B23 ʿajuz/ṣadr WERE carried over correctly and scan.)

---

# 1. Per-bayt verdicts (the 9; both hemistichs each)

Verdict key: **LEGAL** = ṣadr 3 feet ending `… u –`, ʿajuz `[foot][foot][– – –]`. **BREAK** = illegal foot / bunched lights / wrong length / wrong end.

### BAYT 1 — عَفَّتْ مَعالِمُ كُلِّ دارٍ، وَالهُدى ‖ غَضٌّ، وَرَسْمُ الوَحْيِ ظَلَّ المَكْنونْ
- **ṣadr** `--u-uu-u---u-` → `[– – u –][u u – u –][– – u –]` — **LEGAL** (ʿaffat / maʿālimu kul / li dārin wal / hudā; ʿarūḍ ends `u –`).
- **ʿajuz** `--u---u----` → `[– – u –][– – u –][– – –]` — **LEGAL** (ghaḍḍun wa-ras / mu-l-waḥyi ẓal / la-l-maknūn; close `– – –` ✓).
- **Verdict: LEGAL / LEGAL.** No fix. Rhyme **المَكْنونْ** ك·ن·ن (long penult, muqayyad).

### BAYT 3 — بَحْرٌ تَغوصُ وَلا تَنالُ قَرارَهُ ‖ وَالدُّرُّ في غَمْرِ الغَوارِبِ مَدْفونْ
- **ṣadr** `--u-uu-u-uu-u-` → `[– – u –][u u – u –][u u – u –]` — **LEGAL** (needs ṣila: *qarārahū* long).
- **ʿajuz** `--u---u-uu--` → **BREAK.** `…fī ghamri-l-ghawāribi madfūn` = the close lands `… – u u – –`: the rhyme `mad-fūn` (`– –`) is preceded by **two lights** (`ri`, `bi` of *l-ghawāribi*), so the third foot cannot form `– – –`; the line orphans at `– –`. (This is the un-reverted pre-fix original — see Fact 3.)
- **Verdict: LEGAL / BREAK.** Fix below (§2).

### BAYT 8 — لَوْ زاغَ جَدْيٌ أَوْ تَنَكَّرَ مَنْزِلٌ ‖ تاهَ الخِرّيتُ، وَضَلَّ رَكْبٌ مَشْحونْ
- **ṣadr** `--u---u-uu-u-` → `[– – u –][– – u –][u u – u –]` — **LEGAL**.
- **ʿajuz** `----uu-u----` → **BREAK.** `tāha-l-khirrītu…` opens on a **wall of four heavies** `– – – –` (*tā · hal · khir · rī*: الخِرّيت takes the qamarī article-lām, so *ha*+*l* = the heavy *hal*). al-Kāmil's head admits at most `– –` (muḍmar) before a light; `– – – –` is unparseable. (Un-reverted pre-fix original — Fact 3.)
- **Verdict: LEGAL / BREAK.** Fix below (§2).

### BAYT 9 — كَالنَّجْمِ يَهْدي، فَالفَيافي تَنْطَوي ‖ لِأَخي السُّرى الصَّبّارِ، وِرْدٌ مَرْهونْ
- **ṣadr** `--u---u---u-` → `[– – u –][– – u –][– – u –]` — **LEGAL** (kā-n-najmi yah / dī fa-l-fayā / fī tanṭawī; ends `u –`).
- **ʿajuz** `uu-u---u----` → `[u u – u –][– – u –][– – –]` — **LEGAL**. The tricky juncture *li-akhi-s-surā* (hamzat-waṣl of ال drops after the ī; the ī shortens before the assimilated lām→s) scans `u u – u –` either way; close `– – –` ✓.
- **Verdict: LEGAL / LEGAL.** No fix. Rhyme **مَرْهونْ** ر·ه·ن.

### BAYT 10 — السَّدْيُ وَاللُّحْمُ اسْتَوى في نَسْجِها ‖ لَحْنٌ وَمَعْنًى، ثُمَّ بُرْدٌ مَوْضونْ
- **ṣadr** `--u---u---u-` → `[– – u –][– – u –][– – u –]` — **LEGAL** (as-sadyu wa-l / luḥmu-s-tawā / fī nasjihā; ends `u –`).
- **ʿajuz** `--u---u----` → `[– – u –][– – u –][– – –]` — **LEGAL** (laḥnun wa-maʿ / nan thumma bur / dun mawḍūn; close `– – –` ✓). NB v4 here keeps the original `…بُرْدٌ مَوْضونْ`, which scans — it did NOT need audit-05's `نَظْمٌ` reword; both work.
- **Verdict: LEGAL / LEGAL.** No fix. Rhyme **مَوْضونْ** و·ض·ن.

### BAYT 20 — لكِنَّهُ صُنْعُ الإِلهِ، وَجَلَّ أَنْ ‖ يَحْكي صَنيعَتَهُ صَنيعُ المَأْفونْ
- **ṣadr** `--u---u-uu-u-` → `[– – u –][– – u –][u u – u –]` — **LEGAL** (needs ṣila: *lākinnahū* long).
- **ʿajuz** `--u-uuuu----` → **BREAK.** `yaḥkī ṣanīʿatahu ṣanīʿu…` — the word **صَنيعَتَهُ** = *ṣa·nī·ʿa·ta·hu* = `u – u u u`: a run of three lights (`ʿa-ta-hu`) where a watid is due. No al-Kāمil foot tolerates it.
- **Verdict: LEGAL / BREAK.** Fix below (§2).

### BAYT 21 — هاتوا نَظيرَ الحَرْفِ، إِنْ نازَعْتُمُ ‖ رُدَّتْ قُواكُمْ، ثُمَّ عادَ المَطْحونْ
- **ṣadr** `--u---u---uu` → **BREAK.** `…in nāzaʿtumu` ends `… – u u` (*zaʿ · tu · mu*) — the ṣadr must end `… u –` (ṣaḥīḥa ʿarūḍ); a final **two lights** is illegal. (The enclitic connecting vowel `-mu` is the culprit.)
- **ʿajuz** `--u---u----` → `[– – u –][– – u –][– – –]` — **LEGAL** (ruddat quwā / kum thumma ʿā / da-l-maṭḥūn; close `– – –` ✓).
- **Verdict: BREAK / LEGAL.** Fix below (§2).

### BAYT 23 — يَزِنونَ ريحًا، وَالسَّرابَ يَظُنُّهُ ‖ وِرْدًا، فَخابوا، وَاكْتَفَوْا بِالمَظْنونْ
- **ṣadr** `uu-u---u-uu-u-` → `[u u – u –][– – u –][u u – u –]` — **LEGAL** (needs ṣila: *yaẓunnuhū* long at ṣadr-end).
- **ʿajuz** `--u---u----` → `[– – u –][– – u –][– – –]` — **LEGAL** (wirdan fa-khā / bū wa-k-tafaw / bi-l-maẓnūn; *wa-ktafaw* elides the hamzat al-waṣl after *wa*; close `– – –` ✓).
- **Verdict: LEGAL / LEGAL.** No fix (hold the ṣila). Rhyme **المَظْنونْ** ظ·ن·ن.

### BAYT 28 — نُسِجَتْ حُروفٌ كَالدُّروعِ، فَحَلْقَةٌ ‖ شُدَّتْ بِأُخْرى، لا يُحَلُّ المَحْصونْ
- **ṣadr** `uu-u---u-uu-u-` → `[u u – u –][– – u –][u u – u –]` — **LEGAL** (nusijat ḥu / rūfun kā-d-du / rūʿi fa-ḥalqatun; ends `u –`).
- **ʿajuz** `--u---u----` → `[– – u –][– – u –][– – –]` — **LEGAL** (shuddat bi-ukh / rā lā yuḥal / lu-l-maḥṣūn; *bi-ukhrā* keeps hamzat al-qaṭʿ; close `– – –` ✓).
- **Verdict: LEGAL / LEGAL.** No fix. Rhyme **المَحْصونْ** ح·ص·ن. (The accessibility re-diction سابِغات→الدُّروع, تُنْتَضى→يُحَلُّ scans clean.)

---

# 2. The 4 minimal fixes (apply, then lock)

Each fix is the smallest change that lands the locked `– – –` (ʿajuz) or a ṣaḥīḥ `… u –` (ṣadr), **keeps the same Family-B `-ūn` rhyme word, and preserves the archaic image.** Every one re-derived from phonemes and machine-verified.

### FIX B3 ʿajuz — restore audit-05's verified line
> **وَالدُّرُّ في الأَعْماقِ ظَلَّ المَدْفونْ**
> *wad-durru fī-l-aʿmāqi ẓalla-l-madfūn* → `--u---u----` = `[– – u –][– – u –][– – –]` ✓
- Smallest change: swap the broken `في غَمْرِ الغَوارِبِ` (pearl among the wave-crests) for `في الأَعْماقِ ظَلَّ` (in the depths it stayed). Keeps the pearl-buried-in-the-deep image and the rhyme **المَدْفونْ** (definitized — root د·ف·ن unchanged).
- *(If the poet insists on keeping the word غَوارِب, the only metrical home is the bare-sound close `u u – –`: `في قَلْبِ الغَوارِبِ مَدْفونْ` — but that breaks the locked `– – –` uniformity, so it is NOT recommended under the lock.)*

### FIX B8 ʿajuz — restore audit-05's verified line
> **بِهِ ضَلَّ خِرّيتٌ، وَضَلَّ المَشْحونْ**
> *bihi ḍalla khirrītun wa-ḍalla-l-mashḥūn* → `uu-u---u----` = `[u u – u –][– – u –][– – –]` ✓
- Smallest change: take الخِرّيت **off** the article (indefinite *khirrītun*) and front a light `bihi`, dissolving the four-heavy wall. Keeps الخِرّيت (the patron's protected word) and the rhyme **المَشْحونْ** (definitized — root ش·ح·ن unchanged). Sense intact: "by it a [seasoned] guide went astray, and the laden [caravan] strayed."

### FIX B20 ʿajuz — the bunch in صَنيعَتَهُ
> **يَحْكي صَنيعَ اللَّهِ صُنْعُ المَأْفونْ**
> *yaḥkī ṣanīʿa-llāhi ṣunʿu-l-maʾfūn* → `--u---u----` = `[– – u –][– – u –][– – –]` ✓
- Smallest change: replace the un-scannable **صَنيعَتَهُ** (His artifact, *ṣanīʿatahu* — the triple-light tail) with **صَنيعَ اللَّهِ** (God's artifact), and the subject **صَنيعُ** (artifact-of) with **صُنْعُ** (the making-of). Keeps the rhyme **المَأْفونْ** (ء·ف·ن) and the exact image: "…that the **making of the deranged** should mimic **God's artifact**." Grammar: the ṣadr's `أَنْ` reads as *an al-mukhaffafa* + indicative `يَحْكي` (licensed; no manṣūb needed), so the enjambment `…وَجَلَّ أَنْ ‖ يَحْكي…` is sound.

### FIX B21 ṣadr — the two-light ending نازَعْتُمُ
> **هاتوا نَظيرَ الحَرْفِ، إِنْ نازَعْتُمو**
> *hātū naẓīra-l-ḥarfi in nāzaʿtumū* → `--u---u---u-` = `[– – u –][– – u –][– – u –]` ✓ (ends `u –`)
- **Smallest possible change — one letter.** Lengthen the final enclitic `-mu` of the **same verb** نازَعْتُمُ to the long wāw al-jamāʿa **نازَعْتُمو** (*-mū*). The image and word are untouched ("…if you contend"); only the connecting vowel goes long, turning the illegal `… – u u` into a clean `… – u –`. Leads naturally into the (already-legal) ʿajuz *ruddat quwākum…*.

**No other hemistich among the 9 is touched.** B1, B9, B10, B23, B28 stand as written (B3-ṣadr, B20-ṣadr, B23-ṣadr require the Fact-2 ṣila only).

---

# 3. īṭāʾ check across all 30 — CLEAN

Machine ledger of every ʿajuz rhyme-word in master-v4 (30 bayts):

- **30 distinct rhyme WORDS, 30 distinct ROOTS, zero repeats.** ✔
- The 9 audited bayts' rhyme-words and roots:
  B1 المَكْنونْ ك·ن·ن · B3 (ال)مَدْفونْ د·ف·ن · B8 (ال)مَشْحونْ ش·ح·ن · B9 مَرْهونْ ر·ه·ن · B10 مَوْضونْ و·ض·ن · B20 المَأْفونْ ء·ف·ن · B21 المَطْحونْ ط·ح·ن · B23 المَظْنونْ ظ·ن·ن · B28 المَحْصونْ ح·ص·ن.
- **None of the 9 repeats any root or word used in the other 21.** ✔ No fix above alters a rhyme-word (B3/B8 only definitize the same root; B20 keeps maʾfūn; B21's fix is in the ṣadr). 
- Near-root collisions checked and clear: ض·ن·ن (maḍnūn B4) ≠ ض·م·ن (maḍmūn B25); ء·م·ن (maʾmūn B6) ≠ ء·ف·ن (maʾfūn B20); ح·ص·ن (maḥṣūn B28) / ح·ز·ن (maḥzūn B29) / ح·ض·ن (maḥḍūn B30) all distinct (ص/ز/ض); ر·ه·ن (marhūn B9) ≠ ر·ص·ص (marṣūn B12) ≠ ق·ر·ن (maqrūn B7). ✔
- All sākin-nūn (muqayyad); all long penult (Family-B); no muṭlaق `-ūnū` slip; no short-penult (Family-A) slip; no `-in/-an` ridf slip. ✔

---

# 4. Overall ruling

**As written, the 9 newly-crafted bayts of MASTER v4 are NOT yet uniform:** 5 scan clean (B1, B9, B10, B23, B28), but **4 break** — B3-ʿajuz (orphaned close after a `u u` bunch), B8-ʿajuz (wall of four heavies `– – – –`), B20-ʿajuz (triple-light bunch in *ṣanīʿatahu*), B21-ṣadr (two-light ending in *nāzaʿtumu*). Two of these (B3, B8) are regressions: v4 printed the pre-fix originals despite its header claiming the audit-05 rewords were applied.

**With the four §2 fixes applied — all machine-verified from phonemes — every one of the 9 scans as al-Kāmil al-tāmم, ʿarūḍ ṣaḥīḥa (ṣadr ends `… u –`), ḍarب maqṭūʿ-iḍмār LOCKED `– – –`, rawiyy nūn sākin (muqayyad), Family-B long-penult `-ūn`.** Combined with the 21 unchanged bayts (audit-05 verdicts), and given the īṭāʾ ledger is clean (30 distinct roots/words):

> **YES — with these 4 fixes applied, all 30 bayts scan as a uniform al-Kāمil maqṭūʿ (`– – –`) Family-B nūniyya with zero īṭāʾ.**

**Lock notes:**
1. Re-apply the audit-05 rewords that v4 dropped: **B3 → `وَالدُّرُّ في الأَعْماقِ ظَلَّ المَدْفونْ`**; **B8 → `بِهِ ضَلَّ خِرّيتٌ، وَضَلَّ المَشْحونْ`**.
2. Apply the two new fixes: **B20-ʿajuz → `يَحْكي صَنيعَ اللَّهِ صُنْعُ المَأْفونْ`**; **B21-ṣadr → `هاتوا نَظيرَ الحَرْفِ، إِنْ نازَعْتُمو`** (one-letter: `-mu`→`-mū`).
3. Sing the hāʾ al-ḍamīr long at ṣadr-end: **B3 *qarārahū*, B20 *lākinnahū*, B23 *yaẓunnuhū*** — without the ṣila these ṣadrs fall a mora short.
4. Recurring killers confirmed in this batch: (a) a noun/verb trailing **≥2 lights** at the rhyme or ṣadr-end (*ghawāribi*, *ṣanīʿatahu*, *nāzaʿtumu*); (b) the **wall of four heavies** (*tāha-l-khirrīt* → `– – – –`). The fixes remove all four.
