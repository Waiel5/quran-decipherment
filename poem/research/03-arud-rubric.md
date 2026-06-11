# ʿArūḍ Audit Rubric — Metrical & Rhyme Certification for a Qurʾān-Order Qaṣīda

**Purpose.** This is a *mechanically-applicable* reference and checklist for scanning Classical Arabic verse against the four candidate meters, plus a qāfiya (rhyme) section and a final meter+rhyme recommendation. Metrical error is the single highest-probability silent failure of a composed qaṣīda. The checklist (§5) is the load-bearing part: it lets a careful reader certify **one bayt at a time** by hand.

**Scope note (honesty).** This rubric encodes the standard al-Khalīl b. Aḥmad al-Farāhīdī system as transmitted through al-Akhfash, then the canonical handbooks (al-Jawharī *ʿArūḍ al-waraqa*; al-Khaṭīb al-Tabrīzī *al-Kāfī fī l-ʿarūḍ wa-l-qawāfī*; al-Damanhūrī *al-Irshād al-shāfī*; al-Hāshimī *Mīzān al-dhahab*). Where handbooks disagree on the *permissibility* of a given ziḥāf in a given meter, I mark it. The example lines are real classical lines; I give the poet. Treat any scansion you cannot independently reproduce by the §5 procedure as **unverified** — do not let a pretty line override the algorithm.

---

## 0. Foundations: the atoms of ʿarūḍ

ʿArūḍ scans **pronounced phonemes**, never orthography. Two rules dominate everything:

1. **A consonant + short vowel (ḥaraka) = one "moving" letter (mutaḥarrik).** Notate `1` (or CV).
2. **A consonant with sukūn, OR a long vowel (ā ī ū), OR tanwīn's nūn, OR a doubled letter's first half (shadda) = one "still" letter (sākin).** Notate `0` (or C / lengthening).

From moving (`1`) and still (`0`) letters al-Khalīl builds two **syllable-units**:

| Unit | Arabic | Pattern | Gloss |
|---|---|---|---|
| **sabab khafīf** (light cord) | سبب خفيف | `1 0` (مو + سا) | moving + still, e.g. `lam`, `qad`, `mā` |
| **sabab thaqīl** (heavy cord) | سبب ثقيل | `1 1` (مو + مو) | two moving, e.g. `laka`, `bika` |
| **watid majmūʿ** (joined peg) | وتد مجموع | `1 1 0` | two moving + still, e.g. `ʿalā`, `lanā`, `fa-ʿūl` |
| **watid mafrūq** (split peg) | وتد مفروق | `1 0 1` | moving + still + moving, e.g. `qāla`→`qā-la`? no: `ʾay-na`, `lay-ta` |
| *(rare)* **fāṣila ṣughrā** | فاصلة صغرى | `1 1 1 0` | three moving + still (= thaqīl + sabab) |
| *(rare)* **fāṣila kubrā** | فاصلة كبرى | `1 1 1 1 0` | four moving + still |

> **The cardinal asymmetry (memorize this).** A **sabab is unstable** — its second (still) letter may be deleted or made-moving by a *ziḥāf*. A **watid is the metrical skeleton** — in a sound (non-ʿilla) foot it is **invariant**. So: *ziḥāfāt almost always strike asbāb; the awtād hold the meter's identity.* If your candidate line forces a change inside a watid in mid-verse, the foot is almost certainly **illegal** (the exceptions are the named ʿilal at the ʿarūḍ/ḍarb only).

**Notation used in this document.** For each example I give three rows:
- **Phoneme row**: the line transliterated, syllabified by `-`.
- **Binary row**: `1`=mutaḥarrik (moving letter), `0`=sākin (still letter), grouped to show asbāb/awtād.
- **Foot row**: the tafʿīla names with their realized pattern.

I also use the compact prosodist shorthand for the *realized syllable* where helpful: **`/`** = a long/heavy syllable (CVC or CV̄, i.e. `1 0`), **`u`** = a short/light syllable (CV, i.e. a lone `1`). (So a watid majmūʿ `1 1 0` = `u /`; a sabab khafīf `1 0` = `/`; a sabab thaqīl `1 1` = `u u`.) Both notations are given so the auditor can cross-check.

**Three scansion gotchas that cause most false "errors":**
- **Hamzat al-waṣl elides.** `wa-l-kitāb` is scanned `wal-ki-tāb`; the alif of `al-` after a vowel carries no syllable.
- **Final-vowel lengthening at the rhyme (iṭlāq).** The rhyme vowel is normally read long: a ḍamma → `ū`, fatḥa → `ā`, kasra → `ī`. This added letter is the **waṣl/khurūj**; it is *built into* the ḍarb's count. Forgetting it under-counts every ʿajuz.
- **Tanwīn is a nūn sākin.** `kitābun` = `ki-tā-bun` = `1 0 / 1 0 / 1 0 1 0`? No: `ki`=`1`,`tā`=`1 0`,`bun`=`1 0`. The `-un` is `b`+`u`(moving)+`n`(still) = watid majmūʿ-shaped `1 1 0`. Count the nūn.

---

## 1. al-Ṭawīl (الطويل) — "the Long"

**Circle:** al-Mukhtalif. **Per bayt (two hemistichs), the sound base:**

```
فَعُولُنْ   مَفَاعِيلُنْ   فَعُولُنْ   مَفَاعِيلُنْ   ‖   فَعُولُنْ   مَفَاعِيلُنْ   فَعُولُنْ   مَفَاعِلُنْ
faʿūlun    mafāʿīlun     faʿūlun    mafāʿīlun     ‖   faʿūlun    mafāʿīlun     faʿūlun    mafāʿilun
 u / /      u / / /        u / /      u / / /            u / /      u / / /        u / /      u / u /
```

- **Foot anatomy:** `faʿūlun` = watid majmūʿ `fa-ʿū`(`1 1 0`) + sabab `lun`(`1 0`) → `u / /`. `mafāʿīlun` = watid majmūʿ `ma-fā`(`1 1 0`) + sabab `ʿī`(`1 0`) + sabab `lun`(`1 0`) → `u / / /`.
- **Standard ʿarūḍ + ḍarb (the only fully-common form):** ʿarūḍ = **maqbūḍa** `mafāʿilun` (`u / u /`); ḍarb = **maqbūḍ** `mafāʿilun` (`u / u /`). The ṣadr's 4th foot is sound `mafāʿīlun`; the ʿajuz's 4th foot (ʿarūḍ) **and** the ḍarb are both qabḍ. (A second, rarer ḍarb is sound `mafāʿīlun` paired with the maqbūḍ ʿarūḍ — "ṣaḥīḥ ḍarb"; treat it as licensed but uncommon.)

### Permitted ziḥāfāt / ʿilal

| Locus | Change | Name | Result | Frequency |
|---|---|---|---|---|
| `faʿūlun` (any) | drop 5th letter (the `n` of `-lun`) → sabab `lun`→`lu`? no — **qabḍ deletes the 5th sākin** | **qabḍ** | `faʿūlu` `u / u` | **very common** (esp. before `mafāʿīlun`) |
| `mafāʿīlun` (any) | drop 5th sākin (`ī`) | **qabḍ** | `mafāʿilun` `u / u /` | **common** |
| `mafāʿīlun` (any) | drop 7th sākin (`n`) | **kaff** | `mafāʿīlu` `u / / u` | common, but never on the ʿarūḍ/ḍarb (would break rhyme count) |
| `faʿūlun` first foot, line-initial | add an extra sabab before it | **khazm** | extra pre-syllable, *extra-metrical* | rare, archaic, license only |

- **Hard rule for Ṭawīl:** `faʿūlun` never loses its watid (`fa-ʿū`); only its trailing sabab is touched (qabḍ). `mafāʿīlun` keeps `ma-fā` (watid); qabḍ/kaff act on its two trailing asbāb. **A line that shortens `faʿūlun` to `faʿū` (`u /`) by deleting a *moving* letter is illegal.**
- **Khabn/iḍmār do not occur in Ṭawīl** (those belong to feet with leading asbāb like `mustafʿilun`/`mutafāʿilun`). If you "find" khabn in Ṭawīl, you mis-segmented.

### Worked examples (scanned)

**Example T-1 — Imruʾ al-Qays, muʿallaqa, opening:**
> قِفَا نَبْكِ مِنْ ذِكْرَى حَبِيبٍ وَمَنْزِلِ — *qifā nabki min dhikrā ḥabībin wa-manzili*

- Phoneme: `qi-fā | nab-ki-min | dhik-rā | ḥa-bī-bin-wa | man-zi-li`
- Re-segmented by foot:
  | `qi-fā-nab` | `ki-min-dhik-rā` | `ḥa-bī-bin` | `wa-man-zi-li` |
  | `1 1 0` `1 0`? | … | | |

  Cleanly, syllable-weights (`/`=heavy,`u`=light):
  `qi-fā` = u / ; `nab` = / → **faʿūlun** `u / /`
  `ki-min` = u / ; `dhik` = / ; `rā` = / → **mafāʿīlun** `u / / /`
  `ḥa-bī` = u / ; `bin` = / → **faʿūlun** `u / /`
  `wa-man` = u / ; `zi-li` = u / → **mafāʿilun** `u / u /` (ʿarūḍ, **qabḍ**)
- Foot row (ṣadr): `faʿūlun mafāʿīlun faʿūlun mafāʿilun` ✓ canonical Ṭawīl with maqbūḍ ʿarūḍ.

**Example T-2 — al-Mutanabbī:**
> عَلَى قَدْرِ أَهْلِ العَزْمِ تَأْتِي العَزَائِمُ — *ʿalā qadri ahli l-ʿazmi taʾtī l-ʿazāʾimu*

- `ʿa-lā` u / ; `qad` / → faʿūlun `u / /`
- `ri-ah` u / ; `li-l` / ; `ʿaz` / → mafāʿīlun `u / / /` (note `ahli l-` elides hamzat al-waṣl: `ah-li-l`)
- `mi-taʾ` u / ; `tī` / → faʿūlun `u / /`
- `l-ʿa-zā` u / ; `ʾi-mu` u / → mafāʿilun `u / u /` (ʿarūḍ maqbūḍ)
- Foot row: `faʿūlun mafāʿīlun faʿūlun mafāʿilun` ✓.

### Feel / register
Ṭawīl is the **monumental, oratorical** meter — the most-used meter in all of Classical Arabic, the default of the muʿallaqāt and of grand panegyric/heroic/sapiential verse. Its long 14-syllable hemistich gives room for a complete thought + its qualification, and the steady `faʿūlun mafāʿīlun…` pulse reads as gravity, breadth, authority. It is the natural meter for sweep, enumeration, and aphorism. *Risk:* its length tempts padding; every foot must earn its place.

---

## 2. al-Kāmil (الكامل) — "the Complete / Perfect"

**Circle:** al-Muʾtalif. **Per bayt, sound base (trimeter, ×3 per hemistich):**

```
مُتَفَاعِلُنْ   مُتَفَاعِلُنْ   مُتَفَاعِلُنْ   ‖   مُتَفَاعِلُنْ   مُتَفَاعِلُنْ   مُتَفَاعِلُنْ
mutafāʿilun   mutafāʿilun   mutafāʿilun   ‖   mutafāʿilun   mutafāʿilun   mutafāʿilun
 uu / u /      uu / u /      uu / u /          uu / u /      uu / u /      uu / u /
```

- **Foot anatomy:** `mutafāʿilun` = **sabab thaqīl** `mu-ta`(`1 1`) + watid majmūʿ `fā-ʿi…`? Precisely: `mutafāʿilun` = `1 1 / 1 1 0 / 1 0` = sabab thaqīl `muta`(`1 1`) + watid majmūʿ `fāʿi`(`1 1 0`)? — the canonical decomposition is **(fāṣila ṣughrā `mutafā` `1 1 1 0`) + (sabab `ʿilun` `1 0`)** OR equivalently sabab-thaqīl + watid + sabab. The practically useful realized weight is `uu / u /` (two shorts, long, short, long).
- **Standard ʿarūḍ + ḍarb:** the most common complete (non-majzūʾ) Kāmil has ʿarūḍ **ṣaḥīḥa** `mutafāʿilun` and ḍarb **ṣaḥīḥ** `mutafāʿilun`. Two other very common ḍarbs: (a) **maqṭūʿ** ḍarb `mutafāʿil`→`fʿilātun`-shaped? — i.e. `mutafāʿilun` → `mutafāʿil` `uu / /` (qaṭʿ); (b) in **majzūʾ al-Kāmil** (two feet/hemistich) the ḍarb may be `mutafāʿilun`, or `mutafāʿilān`/`mutafāʿilātun` (with tadhyīl/tarfīl ʿilal). For a full grand qaṣīda use the **complete tripod with ṣaḥīḥ ḍarb** unless deliberately choosing majzūʾ.

### Permitted ziḥāfāt / ʿilal

| Locus | Change | Name | Result | Frequency |
|---|---|---|---|---|
| leading `mu-ta` (sabab thaqīl) of any `mutafāʿilun` | make the 2nd letter (the `t`-vowel) sākin, i.e. `1 1`→`1 0` | **iḍmār** (إضمار) | `mustafʿilun`-shaped `mutfāʿilun` = `/ / u /` | **extremely common** — the defining license of Kāmil |
| trailing `-lun` (sabab khafīf) | drop the `n` (5th-from-relevant sākin) — *here* the **qaṭʿ/ʿilla** on ḍarb | **qaṭʿ** | `mutafāʿil` `uu / /` | common as a ḍarb form |
| fāṣila body | rare **waqṣ** (drop the 2nd moving letter `t`) | **waqṣ** | `mufāʿilun`-shaped `u / u /`? (`mafāʿilun`) | rare/heavy |
| ḍarb of majzūʾ | add letters | **tarfīl / tadhyīl** | `mutafāʿilātun` / `mutafāʿilān` | form-defining, not free |

- **The Kāmil identity is the *thaqīl* opening `uu`.** Under **iḍmār** the `uu` collapses to a single `/` and the foot becomes audibly identical to `mustafʿilun` (`/ / u /`) — which is *Rajaz*. This is legal and pervasive; **a Kāmil line may mix sound `mutafāʿilun` and iḍmār `mutfāʿilun` foot-by-foot.** What you must verify is that *at least the meter's overall identity stays Kāmil* (e.g. the rhyme-foot and the dominant pattern), and that no foot violates the watid `fā-ʿi-lun` core.
- **Heavy/avoid:** waqṣ and ʿaql (deleting the 5th moving letter) are tolerated but harsh; a canon-grade qaṣīda should lean on iḍmār and keep the rest sound.

### Worked examples (scanned)

**Example K-1 — ʿAntara, muʿallaqa, opening:**
> هَلْ غَادَرَ الشُّعَرَاءُ مِنْ مُتَرَدَّمِ — *hal ghādara sh-shuʿarāʾu min mutaraddami*

- `hal-ghā` = / / ; `da` = u ; `ra` = u … re-grouped to feet (heavy where elision/shadda):
  Foot 1: `hal-ghā-da-ra` → iḍmār: `/ / u /`? Precisely `hal`/ `ghā`/ `da`u `ra`u — pattern `/ / u u`? Resolve with the watid: **`mutfāʿilun`** realized `hal-ghā-da-ral`? The standard scansion is **`hal ghādara` = mutafāʿilun under iḍmār → mustafʿilun `/ / u /`**, taking `hal-ghā`=`/ /` (iḍmār-collapsed sabab), `da-ra-l`(of "ash-shuʿ") = watid+ `… `.
- Practically, ʿAntara's line scans as Kāmil with **iḍmār in the 1st foot** and sound feet after; the muʿallaqa is the textbook Kāmil exemplar. Foot row: `mutFāʿilun(iḍmār) | mutafāʿilun | mutafāʿilun`.

> **Auditor's caution:** K-1's first foot is the canonical demonstration that an iḍmār foot *looks like* `mustafʿilun`. Do **not** therefore reclassify the line as Rajaz: the rest of the qaṣīda's feet and its rhyme-foot are `mutafāʿilun`-bodied, fixing the meter as Kāmil. **Meter is identified at the level of the bayt/poem, not a single foot.**

**Example K-2 — al-Mutanabbī (Kāmil):**
> وَإِذَا أَتَتْكَ مَذَمَّتِي مِنْ نَاقِصٍ — *wa-idhā atatka madhammatī min nāqiṣin*

- `wa-i-dhā` = `u u /`? `wa`u `i`u `dhā`/ → opens `uu /` = **sound mutafāʿilun head** ✓
- `a-tat-ka` continues the watid; foot 1 `mutafāʿilun` `uu / u /`.
- `ma-dham-ma-tī` second foot, with shadda on `m` (`dham-ma`) giving the `/`s.
- Reliable takeaway: the line alternates sound and iḍmār feet; ʿarūḍ ṣaḥīḥa. Foot row (ṣadr): `mutafāʿilun mutafāʿilun mutafāʿilun` (with iḍmār permitted on any).

### Feel / register
Kāmil is **resonant, rolling, declarative** — second only to Ṭawīl in prestige, and arguably the most *musical* of the long meters because the `uu` openings give it a drumlike forward lean. It carries celebration, pride, exhortation, and devotional grandeur extremely well; its tripod structure makes for naturally balanced, quotable hemistichs and is friendly to **"thunderclap" closing aphorisms**. The iḍmār license lets you vary texture without leaving the meter — a major compositional advantage. Strongly suited to a Qurʾān-praise qaṣīda.

---

## 3. al-Basīṭ (البسيط) — "the Spread-out / Extended"

**Circle:** al-Mukhtalif. **Per bayt, sound base:**

```
مُسْتَفْعِلُنْ   فَاعِلُنْ   مُسْتَفْعِلُنْ   فَاعِلُنْ   ‖   مُسْتَفْعِلُنْ   فَاعِلُنْ   مُسْتَفْعِلُنْ   فَعِلُنْ
mustafʿilun    fāʿilun    mustafʿilun    fāʿilun    ‖   mustafʿilun    fāʿilun    mustafʿilun    faʿilun
 / / u /        / u /       / / u /        / u /           / / u /        / u /       / / u /        u u /
```

- **Foot anatomy:** `mustafʿilun` = sabab khafīf `mus`(`1 0`) + sabab khafīf `taf`(`1 0`) + watid majmūʿ `ʿi-lun`(`1 1 0`) → `/ / u /`. `fāʿilun` = sabab khafīf `fā`(`1 0`) + watid majmūʿ `ʿi-lun`(`1 1 0`) → `/ u /`.
- **Standard ʿarūḍ + ḍarb:** the canonical complete Basīṭ has ʿarūḍ **makhbūna** `faʿilun` (`u u /`) and ḍarb **makhbūn** `faʿilun` (`u u /`). A second very common ḍarb is **maqṭūʿ** `faʿlun`/`fāʿil` → `fāʿil` (`/ u /`→ `/ / `? realized `faʿlun` `/ /`). (Thus the famous two ḍarbs of complete Basīṭ: makhbūn `faʿilun` and maqṭūʿ `faʿlun`.)

### Permitted ziḥāfāt / ʿilal

| Locus | Change | Name | Result | Frequency |
|---|---|---|---|---|
| `mustafʿilun` — drop 2nd sākin (`s` of `mus`) | | **khabn** | `mafāʿilun`? no → `mutafʿilun` `mafāʿilun`-weight `u / u /`? precisely `mustafʿilun`→`mutafʿilun` realized `u / u /`? — standard result is **`mafāʿilun`-shaped** `u / u /` (`mutafʿilun`) | **common** |
| `fāʿilun` — drop 2nd sākin (`ā`) | | **khabn** | `faʿilun` `u u /` | **common** |
| `mustafʿilun` — drop 4th sākin (`f`) | | **ṭayy** | `mustaʿilun`→`muftaʿilun` `/ u u /` | common (esp. mid-line) |
| both khabn+ṭayy together | | **khabl** | `faʿilatun`-weight `u u u /`? (`muftaʿilun`→`faʿilatun`) | heavier, less common |
| ʿarūḍ/ḍarb | qaṭʿ on final `fāʿilun`→`faʿlun` | **qaṭʿ** | `faʿlun` `/ /` | common ḍarb |

- **Basīṭ identity:** the alternation **`mustafʿilun` (4-unit) / `fāʿilun` (3-unit)**. Khabn (on either foot) is the everyday license; ṭayy is the common "crisper" alternative on `mustafʿilun`. The watid `ʿi-lun` at the tail of every foot is invariant — never delete inside it.
- **Heavy/avoid:** khabl (`faʿilatun`-shaped `u u u /`) is metrically legal but rhythmically slack; for canon-grade verse keep it rare.

### Worked examples (scanned)

**Example B-1 — al-Mutanabbī:**
> الخَيْلُ وَاللَّيْلُ وَالبَيْدَاءُ تَعْرِفُنِي — *al-khaylu wa-l-laylu wa-l-baydāʾu taʿrifunī*

- `al-khay` = / / ; `lu` = u ; `wal` = / → **mustafʿilun** `/ / u /` (`al-khay-lu-wal`)
- `lay-lu` = / u ; `wal` = / → **fāʿilun** `/ u /` (`lay-lu-wal`)
- `bay-dā` = / / ; `ʾu` = u ; `taʿ` = / → **mustafʿilun** `/ / u /`
- `ri-fu-nī` = u u / → **faʿilun** `u u /` (ʿarūḍ makhbūna) — with `taʿ-ri-fu-nī` distributing as foot4 `fāʿilun`→khabn `faʿilun`.
- Foot row (ṣadr): `mustafʿilun fāʿilun mustafʿilun faʿilun` ✓.

**Example B-2 — Kaʿb b. Zuhayr, *Bānat Suʿād*, opening:**
> بَانَتْ سُعَادُ فَقَلْبِي اليَوْمَ مَتْبُولُ — *bānat suʿādu fa-qalbī l-yawma matbūlu*

- `bā-nat` = / / ; `su` = u ; `ʿā` = / → **mustafʿilun** `/ / u /`
- `ʿā-du-fa`? regroup: foot2 `fāʿilun` = `su-ʿā-du`? Take `dā-du` /… The reliable foot row is the textbook Basīṭ: `mustafʿilun fāʿilun mustafʿilun fāʿilun`. The ḍarb `matbūlu` → `faʿlun`/`fāʿil` (maqṭūʿ) `/ /`.
- Foot row (ʿajuz ḍarb): ends `… mustafʿilun faʿlun` (maqṭūʿ ḍarb). ✓

### Feel / register
Basīṭ is **stately, balanced, "spread-out"** — its name evokes its expansive, evenly-paced gait. The long/short foot alternation (`mustafʿilun`/`fāʿilun`) gives a rocking, processional quality: excellent for praise, lament (*Bānat Suʿād* is Basīṭ), inscription, and sober grandeur. It is slightly *less* headlong than Kāmil and slightly *less* sweeping than Ṭawīl — more like measured marble. Very strong for an architectural/ordered theme (the "order" of the Qurʾān). *Risk:* the regularity can feel metronomic; use ṭayy/khabn to vary.

---

## 4. al-Wāfir (الوافر) — "the Abundant / Exuberant"

**Circle:** al-Muʾtalif. **Per bayt, complete (the standard catalectic form):**

```
مُفَاعَلَتُنْ   مُفَاعَلَتُنْ   فَعُولُنْ   ‖   مُفَاعَلَتُنْ   مُفَاعَلَتُنْ   فَعُولُنْ
mufāʿalatun    mufāʿalatun    faʿūlun    ‖   mufāʿalatun    mufāʿalatun    faʿūlun
 u / uu /       u / uu /       u / /          u / uu /       u / uu /       u / /
```

- **Foot anatomy:** `mufāʿalatun` = watid majmūʿ `mu-fā`(`1 1 0`) + **fāṣila ṣughrā** `ʿa-la-tun`(`1 1 1 0`) → realized `u / uu /` (short, long, two-shorts, long). The 3rd foot `faʿūlun` (`u / /`) is the **maqṭūf/ʿilla** terminal: the underlying base of Wāfir in al-Khalīl's circle is `mufāʿalatun mufāʿalatun mufāʿalatun`, but the **complete Wāfir always ends each hemistich in `faʿūlun`** by the ʿilla of **qaṭf** (deletion of the fāṣila's last sabab + sukūn of what remains) on the 3rd foot. So treat `faʿūlun` as the *fixed* terminal foot, not a free variant.
- **Standard ʿarūḍ + ḍarb:** ʿarūḍ **maqṭūfa** `faʿūlun`; ḍarb **maqṭūf** `faʿūlun`. (A *majzūʾ* Wāfir exists with ḍarb `mufāʿalatun` sound, or `mafāʿīlun` by ʿaṣb — but the grand-qaṣīda default is the complete `…faʿūlun` form above.)

### Permitted ziḥāfāt / ʿilal

| Locus | Change | Name | Result | Frequency |
|---|---|---|---|---|
| `mufāʿalatun` — make the fāṣila's middle moving letter (the `la`, 5th letter) **sākin** | | **ʿaṣb** (عَصْب) | `mufāʿaltun`→`mafāʿīlun`-weight `u / / /` | **extremely common** — the defining license of Wāfir |
| `mufāʿalatun` — delete the 5th moving letter (`l`) | | **ʿaql** (عَقْل) | `mufāʿatun`→`mufāʿalun` `u / u /` | rarer/heavier |
| `mufāʿalatun` — delete 7th sākin (`n`) | | **naqṣ** (combines kaff+ʿaṣb) | `mufāʿaltu`/`mafāʿīlu` `u / / u` | rare; mostly on ḍarb of majzūʾ |
| 3rd foot | qaṭf → fixed `faʿūlun` | **qaṭf** (ʿilla) | `faʿūlun` `u / /` | obligatory terminal, not optional |

- **The Wāfir identity is the *fāṣila* `…ʿalatun` (`uu /` with a moving `la`).** Under **ʿaṣb** the moving `la` goes still and `mufāʿalatun` becomes audibly `mafāʿīlun` (`u / / /`). This is legal and pervasive; **a Wāfir line freely mixes sound `mufāʿalatun` and ʿaṣb `mafāʿīlun` foot-by-foot.** The watid `mu-fā` is invariant.
- **Heavy/avoid:** ʿaql and naqṣ are tolerated but harsh; lean on ʿaṣb. The terminal `faʿūlun` is *not* a place to experiment — it is fixed by qaṭf.

### Worked examples (scanned)

**Example W-1 — ʿAmr b. Kulthūm, muʿallaqa, opening:**
> أَلَا هُبِّي بِصَحْنِكِ فَاصْبَحِينَا — * alā hubbī bi-ṣaḥniki fa-ṣbaḥīnā*

- `a-lā` = u / ; `hub` = / ; `bī` = / → **mafāʿīlun** (ʿaṣb of mufāʿalatun) `u / / /`  (`a-lā-hub-bī`)
- `bi-ṣaḥ` = u / ; `ni-ki` = uu ; `fa`? regroup: `bi-ṣaḥ-ni-ki-fa` → **mufāʿalatun** `u / uu /` (sound, moving `ki`)
- `ṣ-ba-ḥī-nā` → terminal **faʿūlun** `u / /`  (`faṣ`elides waṣl-alif → `faṣ-ba-ḥī-nā`)
- Foot row (ṣadr): `mafāʿīlun(ʿaṣb) mufāʿalatun faʿūlun` ✓ — the textbook line showing sound + ʿaṣb feet in one hemistich.

**Example W-2 — ʿAmr b. Kulthūm (same muʿallaqa, famous boast):**
> إِذَا بَلَغَ الفِطَامَ لَنَا صَبِيٌّ — *idhā balagha l-fiṭāma lanā ṣabiyyun*

- `i-dhā` = u / ; `ba-la` = uu ; `gha…`→ **mufāʿalatun** `u / uu /` (`i-dhā-ba-la-ghal`)
- `fi-ṭā` = u / ; `ma` / ; `la`? → **mafāʿīlun(ʿaṣb)** `u / / /` (`fi-ṭā-ma-la`)
- `nā-ṣa-biy-yun`→ terminal **faʿūlun** `u / /` (shadda on `y`: `ṣa-biy-yun`)
- Foot row: `mufāʿalatun mafāʿīlun(ʿaṣb) faʿūlun` ✓.

### Feel / register
Wāfir is **abundant, surging, full-throated** — the name *al-wāfir* ("the copious") fits its sound: the rolling `mufāʿalatun` with its bunched short syllables makes it the most *exuberant and emphatic* of the long meters. It is the classic meter of **proud assertion, boast (fakhr), challenge, and high emotion** (ʿAmr b. Kulthūm's defiant muʿallaqa is the archetype). For a qaṣīda asserting the Qurʾān's overwhelming order *as a challenge/proof* (taḥaddī register), Wāfir's surge is rhetorically apt; for serene contemplation it can feel too hot. The ʿaṣb license gives texture control. *Risk:* the terminal `faʿūlun` is short — landing it cleanly each bayt requires discipline.

---

## 4b. Quick comparison matrix

| Meter | Hemistich feet | Realized weight (sound) | Defining license | Mood | "Thunderclap" fit |
|---|---|---|---|---|---|
| **Ṭawīl** | faʿūlun mafāʿīlun ×2 | `u//‖u///‖u//‖u/u/` | qabḍ | monumental, oratorical, broad | high (long runway) |
| **Kāmil** | mutafāʿilun ×3 | `uu/u/` ×3 | iḍmār | resonant, rolling, musical | **very high** |
| **Basīṭ** | mustafʿilun fāʿilun ×2 | `//u/‖/u/` ×2 | khabn, ṭayy | stately, processional, architectural | high |
| **Wāfir** | mufāʿalatun ×2 + faʿūlun | `u/uu/ ×2 ‖ u//` | ʿaṣb | surging, exuberant, defiant | medium-high |

---

## 5. ★ THE AUDIT CHECKLIST — certify ONE bayt by hand ★

> Run this on **each hemistich** (ṣadr, then ʿajuz) of every bayt. A bayt passes only if **both** hemistichs pass §5 and the line passes the qāfiya check §7. Keep a worksheet per bayt.

**STEP 1 — Strip orthography to phonemes (taqṭīʿ kitābī → ṣawtī).**
- Write the hemistich in transliteration or fully-vowelled Arabic, sounding every letter you actually pronounce.
- **Apply elision:** delete hamzat al-waṣl after a vowel (`wa-l-`, `fī-l-`, `qālū-l-`); the alif of `al-` mid-phrase carries no syllable.
- **Spell out what's pronounced but unwritten:** a shadda = **two** letters (first sākin); a long vowel ā/ī/ū = a letter of madd (sākin); tanwīn = a **nūn sākin** appended.
- **Drop what's written but silent:** the alif of the plural `ūā` (`katabū` → `ka-ta-bū`, no alif), silent alif in `miʾa`, etc.
- Output: a bare consonant-vowel string.

**STEP 2 — Mark each letter moving (`1`) or still (`0`).**
- `1` (mutaḥarrik) = consonant carrying a short vowel (fatḥa/ḍamma/kasra).
- `0` (sākin) = consonant with sukūn, OR a madd letter (ā/ī/ū), OR the nūn of tanwīn, OR the first half of a shadda.
- Write the binary string under the phonemes. **Every letter gets exactly one symbol.**

**STEP 3 — Segment into asbāb / awtād (taqṭīʿ).**
- Scan **left-to-right**, greedily forming units using the pegs as anchors:
  - `1 1 0` = **watid majmūʿ** (`u /`).  `1 0 1` = watid mafrūq.
  - `1 0` = **sabab khafīf** (`/`).  `1 1` = **sabab thaqīl** (`uu`-head).
  - `1 1 1 0` = **fāṣila ṣughrā**.
- A clean rule of thumb: **find the awtād first** (the `1 1 0` clusters), then whatever lies between/around them are asbāb. The awtād are the meter's skeleton; they should fall at regular positions.
- Convert to the **realized-weight string** (`/` for heavy `1 0`, `u` for light lone `1`) as a cross-check. A 14-syllable Ṭawīl hemistich, an `uu/u/`×3 Kāmil, etc., should be visible.

**STEP 4 — Match against the target meter's legal tafāʿīl + permitted ziḥāfāt.**
- Lay the meter's sound template beside your segmented string, foot by foot.
- For **each foot**, ask: is it the **sound** tafʿīla, or a **named, permitted** variant from that meter's table (§1–§4)?
  - Ṭawīl: faʿūlun (±qabḍ) / mafāʿīlun (±qabḍ, ±kaff).
  - Kāmil: mutafāʿilun (±iḍmār; ḍarb may be qaṭʿ).
  - Basīṭ: mustafʿilun (±khabn, ±ṭayy) / fāʿilun (±khabn); ʿarūḍ+ḍarb makhbūn or maqṭūʿ.
  - Wāfir: mufāʿalatun (±ʿaṣb) ×2 + faʿūlun (fixed terminal).
- **Verify the watid is intact** in every mid-line foot. If a transformation you need would delete or alter a *moving* letter inside a watid, **stop — it is illegal** (only named ʿilal at the ʿarūḍ/ḍarb may touch a foot's frame, and only as listed).

**STEP 5 — Flag any foot that cannot be derived legally.**
- A foot fails if: (a) its weight matches **no** sound-or-permitted-variant of the meter; or (b) it requires a ziḥāf **not licensed** for that meter (e.g. khabn in Ṭawīl, iḍmār in Basīṭ); or (c) it requires changing a watid mid-line; or (d) it adds/drops a syllable the count can't absorb.
- **Common real failures to hunt for:**
  - **Syllable miscount from a missed shadda or tanwīn** → a foot comes out one unit short/long. (Re-do Step 1.)
  - **Treating a written-but-silent alif as a syllable**, or **missing an elision** → spurious extra/short foot.
  - **A short vowel where the meter needs a long** (or vice-versa): e.g. an open `CV` where the foot's watid needs `CV+sākin`. This is the classic "it reads fine aloud but scans wrong" defect — catch it only by the binary string, not by ear.
  - **Wrong ʿarūḍ/ḍarb:** the final foot of the ʿajuz must match the qaṣīda's chosen ḍarb *every line* (this is also a rhyme constraint — see §7).
- Mark each failing foot with the rule it violates. **One unlegislated foot = the bayt is rejected** (fix or discard).

**STEP 6 — Internal consistency across the qaṣīda.**
- The **ʿarūḍ** (last foot of ṣadr of the *opening* bayt) and the **ḍarb** (last foot of every ʿajuz) are fixed for the whole poem once chosen in the maṭlaʿ. Confirm every bayt's ḍarb is the same shape; confirm you have not silently switched (e.g. Kāmil ṣaḥīḥ vs. maqṭūʿ) between lines.
- Confirm the meter never "drifts" (e.g. a Kāmil line that accidentally becomes pure Rajaz because *every* foot took iḍmār and the rhyme-foot lost its `uu` — keep enough sound feet that the meter's identity is unambiguous).

**STEP 7 — Qāfiya check (apply §6–§7 below).**

> **Pass criterion:** the bayt is certified iff every foot of both hemistichs is sound or a named-permitted variant (Steps 4–5), the ḍarb matches the poem (Step 6), and the rhyme passes §7 with no ʿuyūb.

### 5b. A fully-worked certification (Ṭawīl, Example T-1 re-run through the checklist)

Line: قِفَا نَبْكِ مِنْ ذِكْرَى حَبِيبٍ وَمَنْزِلِ (ṣadr only, for illustration).

1. **Phonemes:** `qi fā nab ki min dhik rā ḥa bī bin wa man zi li`. (No waṣl-elision needed; `ḥabībin` tanwīn → nūn sākin `bin`.)
2. **Binary:** `qi`1 `f`1`ā`0 `n`1`b`0 `k`1 `m`1`n`0 `dh`1`k`0 `r`1`ā`0 `ḥ`1 `b`1`ī`0 `b`1`n`0 `w`1 `m`1`n`0 `z`1 `l`1 → string: `1 |10| 10| 1| 10| 10| 10| 1| 10| 10| 1| 10| 1| 1`.
3. **Segment / weight:** `qi-fā`=`1 10`=watid `u/`; `nab`=`10`=sabab `/` → **faʿūlun** `u//`. `ki-min`=`u/`; `dhik`=`/`; `rā`=`/` → **mafāʿīlun** `u///`. `ḥa-bī`=`u/`; `bin`=`/` → **faʿūlun** `u//`. `wa-man`=`u/`; `zi-li`=`u/`?? — `zi`=`1`,`li`=`1` → that's `uu`, giving `wa-man-zi-li` = `u/ u u`? Recount: the ʿarūḍ is **maqbūḍ mafāʿilun** `u/u/`. `wa`1 `man`(`1 0`) `zi`1 `li`(in rhyme position the final short lengthens → `lī` `1 0`). So `wa-man-zi-lī` = `u / u /` ✓ once iṭlāq is applied to the rhyme.
4. **Match:** foot1 faʿūlun ✓, foot2 mafāʿīlun ✓, foot3 faʿūlun ✓, foot4 mafāʿilun (qabḍ of mafāʿīlun) ✓ — all sound/permitted for Ṭawīl.
5. **Flags:** none. (Note how the rhyme-lengthening in Step 1/3 was essential; skipping it would have produced a false "short foot" flag — this is exactly the trap Step 5 warns about.)
6. **ḍarb:** maqbūḍ `mafāʿilun` — set as the poem's ḍarb. ✓
7. **Qāfiya:** rawiyy = `l` (lām) of `-zili`; see §7.

**Result: CERTIFIED (ṣadr).** Repeat for ʿajuz.

---

## 6. Qāfiya (القافية) — anatomy

**What the qāfiya *is*.** Not merely the last word: the qāfiya runs from the **last sākin of the last word back to the nearest preceding sākin, plus the moving letter before that** (al-Khalīl's definition). Practically it is the **rhyming tail** that must recur identically every bayt.

**Letters of the qāfiya (al-ḥurūf):**

| Letter | Arabic | Definition | Notation role |
|---|---|---|---|
| **rawiyy** | الرويّ | the **anchor consonant** the whole poem rhymes on; the poem is named for it (qaṣīda lāmiyya, mīmiyya, dāliyya…). **Must be identical every bayt.** | the load-bearing rhyme letter |
| **waṣl** | الوصل | a letter immediately **after** the rawiyy: either the lengthened iṭlāq vowel (ā/ū/ī/h of saktah) born of the rawiyy's own ḥaraka, or a hāʾ. | the "trailing" rhyme sound |
| **khurūj** | الخروج | a further letter after a **hāʾ** waṣl (when the hāʾ itself has a vowel that lengthens). | extension of waṣl |
| **ridf** | الردف | a **long vowel (ā/ī/ū) or līn (aw/ay)** *immediately before* the rawiyy. If present in one rhyme it **must** be present (and of compatible class) in all. | pre-rawiyy length |
| **taʾsīs** | التأسيس | an **alif separated from the rawiyy by exactly one moving letter** (pattern `ā · C · rawiyy`). If present, it binds all rhymes. | the "founding" alif |
| **dakhīl** | الدخيل | the single moving letter **between taʾsīs and rawiyy**; its vowel may vary (less strict than rawiyy). | the "intruder" |
| **majrā / ḥadhw / nafādh / ishbāʿ / rass** | — | the *vowels* attached to rawiyy (majrā), pre-ridf (ḥadhw), pre-hāʾ (nafādh), etc. These vowels must stay consistent; mismatch = iqwāʾ/iṣrāf/sinād (see §7). | rhyme-vowel harmony |

**The three rhyme "depths" you must declare before composing:**
1. **mujarrad (bare):** rawiyy + iṭlāq vowel only — e.g. `-rū`, `-dī`, `-mā`. Easiest, most flexible. Recommended for a long qaṣīda.
2. **murdaf:** has a **ridf** (long vowel before rawiyy) — e.g. `-ūr`, `-ār`, `-īr` (النور, البحار, السطور-class endings center here when the rawiyy is `r`). Binds you to keep that long vowel every line.
3. **muʾassas:** has a **taʾsīs alif** two slots before rawiyy — e.g. `-āCiL`. Most ornate, most constraining.

---

## 7. ʿUyūb al-qāfiya (rhyme defects) — what the auditor must catch

Apply to the **rhyme-tail of every bayt against the maṭlaʿ's rhyme**. Each is a hard defect in canon-grade verse.

| Defect | Arabic | One-line definition | How to catch |
|---|---|---|---|
| **īṭāʾ** | الإيطاء | **Repeating the same rhyme-WORD** (same root+meaning) within ~7 lines (some say anywhere). | Keep a running list of every rhyme-word; flag any reuse (esp. identical lexeme/meaning). |
| **iqwāʾ** | الإقواء | The **rawiyy's vowel (majrā) changes** between lines — classically a swap between **ḍamma and kasra** on the rawiyy (e.g. `-rū` vs `-rī` as the *intended* rhyme). | Read the rawiyy's case-vowel each line; it must be constant. Mixing ‑u/‑i = iqwāʾ. |
| **iṣrāf** | الإصراف | Like iqwāʾ but the swap involves **fatḥa vs (ḍamma/kasra)** on the rawiyy. (Some treat iqwāʾ/iṣrāf as one family: *any* majrā-vowel inconsistency.) | Same check; fatḥa appearing where ḍamma/kasra rhyme was set = iṣrāf. |
| **sinād** | السناد | **Inconsistency in a *supporting* element** of the rhyme across lines — five sub-types: sinād al-ridf (ridf present in some lines, absent in others), s. al-taʾsīs (taʾsīs alif inconsistent), s. al-ḥadhw (pre-ridf vowel differs), s. al-ishbāʿ (dakhīl vowel differs), s. al-tawjīh (vowel on the letter *before* a sākin rawiyy differs). | For each supporting letter (ridf, taʾsīs, dakhīl, tawjīh-vowel), verify it is present-and-consistent in **every** line. |
| **taḍmīn** | التضمين | The rhyme/sense is **left grammatically incomplete**, forcing the meaning to spill into the next bayt (enjambment that makes the bayt non-self-standing at the rhyme). | Each bayt should be syntactically complete at its rhyme; flag a rhyme-word that only resolves in the following line. |
| *(also watch)* **īṭāʾ jaliyy vs khafiyy** | — | jaliyy = identical word; khafiyy = same word different (in)flection. Both flagged in strict audit. | — |
| *(also)* **taʾsīs/ridf "intrusion"** | اقتحام / sinād-family | adding a ridf/taʾsīs in one line that the rhyme didn't establish. | covered under sinād. |

> **Auditor's rule of thumb:** set the rhyme **skeleton** from the maṭlaʿ (rawiyy letter + its vowel + presence/absence of ridf + presence/absence of taʾsīs), then every subsequent bayt must reproduce that exact skeleton. Any deviation maps to one of the defects above.

### Recommended rawiyy choices for a Qurʾān-order qaṣīda

| Rawiyy | Form | Rhyme-word wealth | Difficulty | Notes for this theme |
|---|---|---|---|---|
| **rāʾ (ر), murdaf `-ūr` / `-ār`** | e.g. `النور، السطور، البحور، الدهور، الظهور، الصدور، البدور` (‑ūr); `الأسرار، الأنوار، البحار، الأقدار` (‑ār) | **very rich** | medium (ridf binds the long vowel every line) | **Top pick.** The thematic vocabulary clusters here: *al-nūr* (light), *al-suṭūr* (the lines/script), *al-buḥūr* (the seas/meters), *al-duhūr* (the ages), *al-qadr*→*al-aqdār*. `r` is sonorous and resonant — ideal for grandeur. The `-ūr` murdaf rhyme rings like a bell on each ḍarb. |
| **dāl (د), `-ūd`/`-ād`/`-dī`** | `الخلود، الوجود، الشهود، الحدود، السجود` (‑ūd); `العدد، السند، الأبد، الأحد` (‑ad/‑dad) | rich | medium | Strong, hard-closing consonant — good for "thunderclap" finality. *al-ʿadad* (number), *al-aḥad* (the One), *al-abad* (eternity), *al-sujūd* fit a math-order + worship theme. Plosive `d` lands aphorisms hard. |
| **mīm (م), `-ām`/`-ūm`/`-mī`** | `النظام، الكلام، الأحكام، الإحكام، الأرقام، التمام` (‑ām); `العلوم، النجوم، الرقوم، المعلوم` (‑ūm) | rich | medium | *al-niẓām* (the order/system), *al-iḥkām* (perfect ordering — Qurʾānic, cf. هود:1), *al-arqām* (the numerals), *al-tamām* (completion). `m` hums — softer grandeur, very Qurʾān-praise. |
| **bāʾ (ب), `-āb`/`-ūb`** | `الكتاب، الخطاب، الإعجاب، الألباب، الحساب` (‑āb) | rich | medium | *al-kitāb* (the Book!), *al-ḥisāb* (the reckoning/计算), *al-iʿjāb*→*iʿjāz*-adjacent, *ūlū l-albāb* (people of understanding). Thematically central (الكتاب). Plosive close. |

**Trade-off summary:** `-ūr`/`-ār` (rāʾ) maximizes *both* rhyme-word availability *and* thematic resonance and is my recommendation; a **bare** `-rū`/`-rī` rāʾ rhyme would be even easier but sacrifices the bell-like ridf. `dāl` and `bāʾ` give harder, more percussive closes (better for sheer "thunderclap" landings, slightly less lush). `mīm` is the softest/most hymnal.

---

## 8. ★ RECOMMENDATION ★

**Recommended meter: al-Kāmil (complete, tripod `mutafāʿilun ×3`), ʿarūḍ ṣaḥīḥa + ḍarb ṣaḥīḥ.**
**Recommended rawiyy: rāʾ (ر) with a murdaf `-ūr` rhyme** (waṣl ū; e.g. النور، السطور، البحور، الدهور، الصدور، الظهور، البدور، النشور), with `-ār` as a fallback rhyme-family if `-ūr` words thin out.

**Why this meter.**
- **Grandeur with momentum.** Kāmil is the most *musical* of the prestige long-meters; its `uu` foot-heads give a forward, drumlike surge that reads as celebration and conviction — exactly the register for praising the Qurʾān's overwhelming order. It is canonically weighty (used across the highest panegyric and devotional verse) without Ṭawīl's tendency to sprawl.
- **"Thunderclap" landings.** The tripod hemistich (`mutafāʿilun mutafāʿilun mutafāʿilun`) ends each ʿajuz on a strong watid+sabab close that, paired with a resonant `-ūr` ḍarb, lands aphorisms hard and clean. Self-contained, quotable hemistichs come naturally — ideal for sapiential "thunderclap" lines about number, order, and inimitability.
- **Texture control without illegality.** The **iḍmār** license (`uu`→`/`, foot becomes `mustafʿilun`-shaped) lets you vary nearly every line's opening for emphasis or to fit hard vocabulary, while staying unambiguously in-meter. This dramatically lowers the metrical-error rate of a long composition versus Ṭawīl (whose qabḍ is subtler to hear) — a decisive practical advantage given that **metrical error is the #1 silent failure mode**.
- **Auditability.** Kāmil's foot is uniform (one tafʿīla repeated), so the §5 checklist runs fast and errors are conspicuous: any foot that is neither sound `mutafāʿilun` nor iḍmār `mutfāʿilun` is immediately suspect.

**Why this rhyme.**
- The target lexicon for a Qurʾān-*order* poem lives in the rāʾ family: **النور** (light), **السطور** (the written lines), **البحور** (the seas — *and* the prosodic "meters," a built-in double-entendre on this very topic), **الدهور** (the ages), **القدر→الأقدار** (measure/decree), plus صدور، ظهور، بدور، نشور، شطور. This is the **richest** thematically-loaded rhyme pool, minimizing īṭāʾ risk over a long poem.
- The **murdaf `-ūr`** (ridf = long ū before rawiyy r) gives a sonorous, ringing close on every ḍarb — `r` is the most resonant Arabic liquid, and the bell-like `-ūr` is grand without being heavy. It binds you to keep the long ū every line (an easy, audible constraint to police).

**Runner-up (if a harder, more percussive close is wanted):** al-Kāmil with **dāl** rawiyy `-ūd`/`-ad` (الخلود، الأحد، العدد، الأبد) — plosive `d` lands "thunderclaps" even harder; slightly thinner rhyme pool. **Alternative meter if a more austere, architectural feel is preferred:** al-Basīṭ (whose "spread-out," processional gait suits the *structural order* theme) with the same `-ūr` rāʾ rhyme. **For a taḥaddī (challenge) register**, Wāfir + `-ūr` would surge well, but its short terminal `faʿūlun` is harder to land consistently — choose it only if the poem's stance is defiant proof rather than serene praise.

---

## 9. One-page auditor cheat-sheet (print this)

```
SCAN ONE HEMISTICH:
 1. Sound out phonemes. Elide waṣl-hamza. Shadda=2 letters(1st sākin).
    Long vowel=sākin. Tanwīn=nūn sākin. Drop silent alif. Lengthen rhyme vowel.
 2. Mark every letter: 1=moving(short-voweled C), 0=still(sukūn/madd/tanwīn-n/1st-of-shadda).
 3. Segment: 110=watid(u/) ; 10=sabab(/) ; 11=sabab-thaqīl(uu) ; 1110=fāṣila.
    Find the awtād first; they are the skeleton and must NOT change mid-line.
 4. Overlay the meter template:
      ṬAWĪL : faʿūlun(±qabḍ) mafāʿīlun(±qabḍ/kaff) | …×4 ; ʿarūḍ+ḍarb=maqbūḍ mafāʿilun
      KĀMIL : mutafāʿilun(±iḍmār) ×3 ; ḍarb ṣaḥīḥ (or maqṭūʿ)
      BASĪṬ : mustafʿilun(±khabn/ṭayy) fāʿilun(±khabn) ×2 ; ʿarūḍ+ḍarb makhbūn(or maqṭūʿ)
      WĀFIR : mufāʿalatun(±ʿaṣb) ×2 + faʿūlun(fixed)
 5. FLAG a foot if: weight matches no sound/permitted variant; needs an unlicensed
    ziḥāf for this meter (khabn∉Ṭawīl, iḍmār∉Basīṭ…); alters a watid mid-line;
    or mis-counts a syllable (recheck shadda/tanwīn/elision/rhyme-lengthening).
 6. Confirm the ḍarb is the SAME shape as the maṭlaʿ, every line. Meter must not drift.

CHECK THE QĀFIYA (every line vs. maṭlaʿ):
 • rawiyy letter identical?              (else: not the same rhyme)
 • rawiyy vowel identical?               (else: IQWĀʾ ḍamma/kasra | IṢRĀF w/ fatḥa)
 • ridf present-or-absent consistently?  (else: SINĀD al-ridf)
 • taʾsīs alif consistent?               (else: SINĀD al-taʾsīs)
 • rhyme-word never repeated?            (else: ĪṬĀʾ)
 • bayt complete at the rhyme?           (else: TAḌMĪN)

PASS = every foot sound/permitted + ḍarb constant + rhyme skeleton constant + no ʿayb.
```

---

### Sources / lineage
al-Khalīl b. Aḥmad al-Farāhīdī (founder of ʿarūḍ; the five circles, the 15 meters; al-Akhfash added al-mutadārak → 16). Canonical handbooks: al-Jawharī, *Kitāb ʿarūḍ al-waraqa*; al-Khaṭīb al-Tabrīzī, *al-Kāfī fī l-ʿarūḍ wa-l-qawāfī*; Ibn ʿAbd Rabbih, *al-ʿIqd al-farīd* (prosody chapters); al-Damanhūrī, *al-Irshād al-shāfī ʿalā matn al-Kāfī*; Aḥmad al-Hāshimī, *Mīzān al-dhahab fī ṣināʿat shiʿr al-ʿArab*; Ṣafāʾ Khulūṣī, *Fann al-taqṭīʿ al-shiʿrī wa-l-qāfiya* (modern). Example lines from the Muʿallaqāt (Imruʾ al-Qays, ʿAntara, ʿAmr b. Kulthūm), Kaʿb b. Zuhayr (*Bānat Suʿād*), and al-Mutanabbī.

> **Final caution to the auditor:** trust the **binary string (Step 2)**, never the ear alone. The most dangerous errors *sound* fine but scan wrong (a short syllable where a long is required, a missed shadda, a swallowed waṣl-hamza). Re-derive every flagged foot from phonemes before accepting or rejecting it.
