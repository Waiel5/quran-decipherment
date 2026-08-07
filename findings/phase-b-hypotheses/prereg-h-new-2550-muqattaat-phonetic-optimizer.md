---
id: H-NEW-2550
title: Are the 14 muqaṭṭaʿāt letters an articulatory-feature-space optimizer? — the al-Zamakhsharī "half of each genus" claim against the exact C(28,14) null — PRE-REGISTRATION
date: 2026-08-07
phase: B
status: LOCKED-BEFORE-NULL-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260511
n_perm: 10000000
bonferroni_k: 20
alpha_bon: 0.0025
parents: [H-NEW-1730, H-NEW-1740, H-NEW-1810, H-NEW-600]
rules_tuple: (no-tashkeel, grapheme, 28-letter ḥurūf al-muʿjam [hamza-seats folded], basmala-as-v.1-of-Q1-only, Hafs-Kūfan, Mashriqī) + 4 declared variants
---

# PRE-REGISTRATION — H-NEW-2550 — The muqaṭṭaʿāt-14 as a phonetic-feature-space optimizer

**This file is locked BEFORE any computation of the null distribution, any percentile,
or any p-value. Its SHA-256 is embedded in `findings/phase-b-hypotheses/scripts/h-new-2550.py`
and verified at runtime (fail-fast on mismatch), per Protocol §1.2.**

---

## 0. WHAT IS AND IS NOT UNDER TEST — mandatory disclosure, stated before the lock

This test has an unusual epistemic shape and the honesty of the finding depends on
naming it up front.

**The observed statistic is already public in the classical source.** al-Zamakhsharī
(§2 below) does not merely *assert* that the muqaṭṭaʿāt letters take half of each
phonetic genus — he **enumerates the members** of each genus that fall inside the 14.
Anyone who reads the passage (as this investigator did, before the lock, in order to
cite it) thereby knows the observed per-category intersection counts. It would be a
fiction to pre-register them as unobserved, and this pre-registration does not do so.
The T-A observed counts, and the observed deviation statistic `D` derived from them,
are declared KNOWN-BEFORE-LOCK in §9.

**What is genuinely unobserved, and what this test is entirely about, is the NULL.**
No classical or modern source known to this project states where the actual 14-letter
set sits in the distribution of `D` across all C(28,14) = 40,116,600 alternative
14-subsets. That distribution — its mean, its minimum, the mass at the minimum, and
therefore every percentile and every p-value in this test — has not been computed by
anyone, by this investigator or otherwise, at the moment of this lock. It is computed
only after the lock, by the script whose SHA-check binds it to this file.

**Consequently the direction lock in §5 is a real commitment**, and the single question
this finding answers is the one the classical claim never asked:

> Is "half of each phonetic genus" a **real optimization** — a property that
> distinguishes the attested 14 from the alternatives — or a **combinatorial
> inevitability** that almost any 14-subset of 28 would satisfy?

**Pre-stated expectation (and why a NULL here is a first-class result).** For ANY binary
partition of the 28 letters into `(f, f̄)`, the expected size of `S ∩ f` over uniform
random 14-subsets `S` is exactly `|f| · 14/28 = |f|/2`. "Half of each category" is the
*mean of the null distribution*. The null distribution of `D` is therefore centred at a
small value and is tightly concentrated. **The single most likely outcome of this test is
CONFIRMED-BUT-MEANINGLESS**: the classical description is factually exact, and
simultaneously unremarkable. That outcome is pre-registered in §6 as a full-status verdict
with equal prominence (Protocol §1.3), not as a failure. It would establish something the
project has not previously established: that a celebrated classical observation about the
muqaṭṭaʿāt is *true and empty*, and would place a ceiling on how much any future
"the letters were selected for phonetic balance" argument may claim.

---

## 1. The 14 letters — DERIVED FROM THE CORPUS, not asserted

The muqaṭṭaʿāt loci are derived by a detector that never mentions the letters it is
looking for:

> For each surah, take the **first whitespace token of verse 1 and of verse 2** in
> `quran-text/quran-full-tashkeel.json`. A token is a muqaṭṭaʿāt token **iff it contains
> no ordinary vocalisation mark** — i.e. no codepoint in U+064B–U+0652 (tanwīn, fatḥa,
> ḍamma, kasra, shadda, sukūn) and no U+0670 (superscript alif). Muqaṭṭaʿāt are written
> as bare letter-names carrying only maddah (U+0653) and pause marks; every ordinary
> Arabic word in an opening verse carries vocalisation.

The 14-letter set is the **union of the graphemes** of the matched tokens read from
`quran-text/quran-no-tashkeel.json`. Locked MW-6 assertions on this derivation:

- exactly **30 loci** in exactly **29 surahs** (Q 42 contributes two: 42:1 حم, 42:2 عسق);
- the surah list must equal the 29-surah catalogue of
  [[h-new-1740-khalifa-muqattaat-complete-audit|H-NEW-1740]] §1;
- the union must have **exactly 14** members and must equal al-Zamakhsharī's enumerated
  fourteen (§2);
- zero false positives across all 114 × 2 scanned tokens.

Fail-fast on any mismatch.

## 2. The classical claim — VERIFIED ON DISK, quoted, with the provenance of each part

### 2.1 al-Zamakhsharī — the STRONG form (half of **each genus**), with membership lists

**al-Zamakhsharī, *al-Kashshāf ʿan ḥaqāʾiq al-tanzīl*, ad Q 2:1 (fawātiḥ al-Baqara)**,
edition pagination **PageV01P028–PageV01P029**.
On disk: `data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt`
(byte offset ≈ 36 088–37 200) and, identically,
`data/literature/classical-tafsir/raw/zamakhshari-kashshaf-ar-openiti-Q002.txt`
(byte offset ≈ 10 627).

> واعلم أنك إذا تأملت ما أورده الله عز سلطانه في الفواتح من هذه الأسماء، وجدتها **نصف
> أسامى حروف المعجم أربعة عشر سواء**، وهي: الألف، واللام، والميم، والصاد، والراء،
> والكاف، والهاء، والياء، والعين، والطاء، والسين، والحاء، والقاف، والنون — **في تسع
> وعشرين سورة** على عدد حروف المعجم. ثم إذا نظرت في هذه الأربعة عشر وجدتها **مشتملة على
> أنصاف أجناس الحروف**، بيان ذلك أن فيها **من المهموسة نصفها**: الصاد، والكاف، والهاء،
> والسين، والحاء. **ومن المجهورة نصفها**: الألف، واللام، والميم، والراء، والعين،
> والطاء، والقاف، والياء، والنون. **ومن الشديدة نصفها**: الألف، والكاف، والطاء،
> والقاف. **ومن الرخوة نصفها**: اللام، والميم، والراء، والصاد، والهاء، والعين، والسين،
> والحاء، والياء، والنون. **ومن المطبقة نصفها**: الصاد، والطاء. **ومن المنفتحة نصفها**:
> الألف، واللام، والميم، والراء، والكاف، والهاء، والعين، والسين، والحاء، والقاف،
> والياء، والنون. **ومن المستعلية نصفها**: القاف، والصاد، والطاء. **ومن المنخفضة
> نصفها**: الألف، واللام، والميم، والراء، والكاف، والهاء، والياء، والعين، والسين،
> والحاء، والنون. **ومن حروف القلقلة نصفها**: القاف، والطاء. ثم إذا استقريت الكلم
> وتراكيبها، رأيت الحروف التي ألغى الله ذكرها من هذه الأجناس المعدودة مكثورة بالمذكورة
> منها، فسبحان الذي دقت في كل شيء حكمته.

Stated intersection counts: mahmūsa **5**, majhūra **9**, shadīda **4**, rikhwa **10**,
muṭbaqa **2**, munfatiḥa **12**, mustaʿliya **3**, munkhafiḍa **11**, qalqala **2**.
These nine numbers are asserted at runtime against the feature table (§3); mismatch = abort.

### 2.2 al-Suyūṭī — an independent STRONG-form attestation, with a makhārij dimension

**al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on the fawātiḥ al-suwar**, pagination
**PageV03P031**. On disk:
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (byte offset ≈ 717 265).

> وقيل المقصود بها الإعلام بالحروف التي يتركب منها الكلام فذكر منها **أربعة عشر حرفا
> وهي نصف جميع الحروف وذكر من كل جنس نصفه**: فمن **حرف الحلق** الحاء والعين والهاء، ومن
> **التي فوقها** القاف والكاف، ومن **الحرفين الشفهيين** الميم، ومن **المهموسة** السين
> والحاء والكاف والصاد والهاء، ومن **الشديدة** الهمزة والطاء والقاف والكاف، ومن
> **المطبقة** الطاء والصاد، ومن **المجهورة** الهمزة والميم واللام والعين والراء والطاء
> والقاف والياء والنون، ومن **المنفتحة** الهمزة والميم والراء والكاف والهاء والعين
> والسين والحاء والقاف والياء والنون، ومن **المستعلية** القاف والصاد والطاء، ومن
> **المنخفضة** الهمزة واللام والميم والراء والكاف والهاء والياء والعين والسين والحاء
> والنون، ومن **القلقلة** القاف والطاء.

Two differences from al-Zamakhsharī are recorded and disclosed, not smoothed:
(i) al-Suyūṭī writes **الهمزة** (hamza) where al-Zamakhsharī writes **الألف** — the two
scholars agree the muqaṭṭaʿāt "alif" is phonetically the glottal stop. This is exactly the
fork that tuple **T-B** (§4) tests. (ii) al-Suyūṭī's munfatiḥa list has **11** members
(اللام absent) against al-Zamakhsharī's 12; ل is uncontroversially munfatiḥ in every
classical table, so this is treated as a transmission/copyist omission and al-Zamakhsharī's
list is the one asserted. Disclosed, not silently corrected.
al-Suyūṭī additionally extends "half of each genus" to **makhārij** (ḥurūf al-ḥalq,
"those above them", the labials) — which is the classical warrant for tuples **T-D/T-E**.

### 2.3 al-Rāzī — the WEAK form only (this is a negative finding about al-Rāzī)

**al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 2:1**, in *furūʿ ʿalā al-qawl bi-annahā asmāʾ
al-suwar*, point **al-thānī**, pagination ≈ **PageV02P257**. On disk:
`data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt`
(byte offset ≈ 628 493).

> الثاني: أن الله تعالى أورد في هذه الفواتح **نصف أسامي حروف المعجم: أربعة عشر سواء**،
> وهي: الألف، واللام، والميم، والصاد، والراء، والكاف، والهاء، والياء، والعين، والطاء،
> والسين، والحاء، والقاف، والنون **في تسع وعشرين سورة**.

**Explicit honest limit, locked before the run:** in the copy of *Mafātīḥ al-ghayb* held
by this project, al-Rāzī reports **only the weak form** — 14 letters = half the alphabet,
across 29 surahs. **No per-ṣifa breakdown by al-Rāzī was located on disk.** Targeted
diacritic-insensitive searches of the full 29.7 MB raw for المهموسة / المطبقة /
المستعلية / أجناس الحروف / أنصاف أجناس returned his tajwīd discussion of ḍād-vs-ẓāʾ
(muqaddima, ≈ byte 124 517) and unrelated hits, but not the fawātiḥ ṣifāt breakdown.
The strong form is therefore attributed **to al-Zamakhsharī and al-Suyūṭī only**. Any
future write-up that attributes the per-category claim to al-Rāzī without a located
passage is unsupported.

## 3. The phonetic feature table — 28 letters, with per-assignment provenance

**Instrument fixed before the test (MW-1).** The table below is assembled from sources on
disk. Provenance codes: **[Z]** = al-Zamakhsharī's enumerated lists (§2.1);
**[N]** = Ibn al-Jazarī, *al-Nashr*, as quoted verbatim by al-Suyūṭī, *al-Itqān* nawʿ 38,
PageV01P348–349 (`suyuti-itqan.openiti.raw.txt` ≈ byte 348 700–349 100), the pairwise
ṣifāt comparison (« فالهمزة والهاء اشتركا مخرجا وانفتاحا واستفالا وانفردت الهمزة بالجهر
والشدة … »); **[C]** = closure — forced by [Z]'s stated category size (e.g. mahmūsa must
have exactly 10 members because [Z] states its half is 5, and 9 are fixed by [Z]+[N], so
the 10th is determined); **[M]** = standard classical tajwīd mnemonic (Ibn al-Jazarī,
*al-Muqaddima al-Jazariyya*), **NOT verified in a file in this repository** and flagged
as such.

| # | Letter | mahmūs | shadīd | muṭbaq | mustaʿlī | qalqala | bayniyya (T-C) | makhraj-17 group |
|--:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | ا | – | **✓**[Z] | – | – | – | – | jawf |
| 2 | ب | – | **✓**[C] | – | – | **✓**[M] | – | shafatān |
| 3 | ت | **✓**[N] | **✓**[N] | – | – | – | – | ṭ·d·t |
| 4 | ث | **✓**[N] | – | – | – | – | – | ẓ·th·dh |
| 5 | ج | – | **✓**[N] | – | – | **✓**[M] | – | wasaṭ al-lisān |
| 6 | ح | **✓**[Z][N] | – | – | – | – | – | wasaṭ al-ḥalq |
| 7 | خ | **✓**[N] | – | – | **✓**[N] | – | – | adnā al-ḥalq |
| 8 | د | – | **✓**[N] | – | – | **✓**[M] | – | ṭ·d·t |
| 9 | ذ | – | – | – | – | – | – | ẓ·th·dh |
| 10 | ر | – | – | – | – | – | **✓**[M] | rāʾ |
| 11 | ز | – | – | – | – | – | – | ṣ·s·z |
| 12 | س | **✓**[Z][N] | – | – | – | – | – | ṣ·s·z |
| 13 | ش | **✓**[N] | – | – | – | – | – | wasaṭ al-lisān |
| 14 | ص | **✓**[Z][N] | – | **✓**[Z][N] | **✓**[Z][N] | – | – | ṣ·s·z |
| 15 | ض | – | – | **✓**[N] | **✓**[N] | – | – | ḍād |
| 16 | ط | – | **✓**[Z][N] | **✓**[Z][N] | **✓**[Z][N] | **✓**[Z] | – | ṭ·d·t |
| 17 | ظ | – | – | **✓**[N] | **✓**[N] | – | – | ẓ·th·dh |
| 18 | ع | – | – | – | – | – | **✓**[M] | wasaṭ al-ḥalq |
| 19 | غ | – | – | – | **✓**[N] | – | – | adnā al-ḥalq |
| 20 | ف | **✓**[C] | – | – | – | – | – | fāʾ |
| 21 | ق | – | **✓**[Z] | – | **✓**[Z] | **✓**[Z] | – | aqṣā al-lisān |
| 22 | ك | **✓**[Z] | **✓**[Z] | – | – | – | – | kāf |
| 23 | ل | – | – | – | – | – | **✓**[M] | lām |
| 24 | م | – | – | – | – | – | **✓**[M] | shafatān |
| 25 | ن | – | – | – | – | – | **✓**[M] | nūn |
| 26 | ه | **✓**[Z][N] | – | – | – | – | – | aqṣā al-ḥalq |
| 27 | و | – | – | – | – | – | – | shafatān |
| 28 | ي | – | – | – | – | – | – | wasaṭ al-lisān |

**Category sizes (asserted at runtime):** mahmūsa **10** {ت ث ح خ س ش ص ف ك ه}; shadīda
**8** {ا ب ت ج د ط ق ك}; muṭbaqa **4** {ص ض ط ظ}; mustaʿliya **7** {خ ص ض ط ظ غ ق};
qalqala **5** {ب ج د ط ق}; bayniyya **5** {ر ع ل م ن}.

**makhraj-17 partition** (al-Suyūṭī, *al-Itqān* nawʿ 38, **PageV01P347–348**, quoting the
qurrāʾ and al-Khalīl — « وأما مخارج الحروف فالصحيح عند القراء ومتقدمي النحاة كالخليل أنها
سبعة عشر »; enumerated makhraj-by-makhraj in the source): jawf {ا}; aqṣā al-ḥalq {ه};
wasaṭ al-ḥalq {ع ح}; adnā al-ḥalq {غ خ}; aqṣā al-lisān {ق}; kāf {ك}; wasaṭ al-lisān
{ج ش ي}; ḍād {ض}; lām {ل}; nūn {ن}; rāʾ {ر}; ṭ·d·t {ط د ت}; ṣ·s·z {ص س ز}; ẓ·th·dh
{ظ ث ذ}; fāʾ {ف}; shafatān {ب م و}. The 17th (khayshūm) hosts ghunna, not a letter, and
contributes no group. Sum = 28, asserted at runtime.

**Weakest links, disclosed now:** the four **[M]**-only assignments — ب ∈ qalqala,
ج ∈ qalqala, د ∈ qalqala, and the bayniyya membership {ر ع ل م ن} — rest on the standard
tajwīd mnemonics قطب جد and لن عمر, which this investigator did **not** locate in a file
in this repository. ق and ط ∈ qalqala **are** on disk via [Z]. ب ∈ shadīda and ف ∈ mahmūsa
are **[C]**-derived (forced by al-Zamakhsharī's own stated halves), not assumed.

## 4. Rules-tuples — 5 declared inventories/taxonomies (all classically attested)

| Tuple | Inventory N | Feature set | Classical warrant |
|:--|:-:|:--|:--|
| **T-A** (PRIMARY) | 28 (ḥurūf al-muʿjam; hamza-seats folded to ا و ي; ة→ت; ى→ي) | mahmūsa, shadīda, muṭbaqa, mustaʿliya, qalqala (5 binary) | al-Zamakhsharī's own genera and his own "14 of 28" |
| **T-B** | **29** (ء counted distinct from ا) | same 5 | al-Suyūṭī writes **الهمزة** where al-Zamakhsharī writes **الألف** (§2.2); Sībawayh's inventory separates them. The muqaṭṭaʿāt set takes **ا** (the grapheme actually attested in the corpus), NOT ء — so shadīda ∩ S changes. |
| **T-C** | 28 | mahmūsa, **shadīd / bayniyya / rikhw (3-way)**, muṭbaqa, mustaʿliya, qalqala (7 groups) | al-Zamakhsharī uses the older **binary** shadīd/rikhw split (his rikhwa list contains ل م ر ع ن). Later tajwīd interposes a 5-member mutawassiṭa class. |
| **T-D** | 28 | T-A's 5 **+ the 16 non-empty makhraj-17 groups** (21 features) | al-Suyūṭī extends "half of each genus" to makhārij (§2.2); the 17-makhraj table is *al-Itqān* nawʿ 38 |
| **T-E** | 28 | T-A's 5 **+ makhraj-16 groups**, ا → aqṣā al-ḥalq (20 features) | al-Suyūṭī, same page: « وقال كثير من الفريقين: ستة عشر فأسقطوا مخرج الحروف الجوفية … وجعلوا مخرج الألف من أقصى الحلق » |

Every tuple is a **classically attested** alternative read off the same two pages, not an
investigator-invented variant. This is the exact class of claim the project's
rules-tuple-bidirectionality rule targets: the taxonomy may rehabilitate or demolish the
claim, and both directions are reported.

## 5. Hypotheses and LOCKED direction

Let `L` be the letter inventory (|L| = N), `S` the attested muqaṭṭaʿāt set (|S| = n = 14),
and `F` the tuple's feature set. For a feature `f ⊆ L`:

**H1 (unweighted balance).**
```
D(S) = Σ_{f∈F} | |S ∩ f| − |f| · n/N |
```
For N = 28, `|f|·n/N = |f|/2` — literally al-Zamakhsharī's "half". For T-B (N = 29) the
null-centred target `|f|·14/29` is used, because `E[|S∩f|] = |f|·n/N` under the null; the
literal-half variant is additionally reported as a descriptive companion.

**H2 (corpus-frequency-weighted balance).** With `W(X) = Σ_{ℓ∈X} corpus_count(ℓ)`:
```
D_freq(S) = Σ_{f∈F} | W(S ∩ f) / W(f) − n/N |
```
`E[W(S∩f)/W(f)] = n/N` exactly under the uniform null, so this asks the same "half"
question on the mass axis rather than the type axis.

**LOCKED DIRECTION for H1 and H2, all tuples, all nulls, one-sided and low:**
> **`D(S_actual)` is SMALLER than `D` for a random 14-subset.**
> Evidence for the classical claim = the actual set sits in the LOWER tail.
> Observation of `D_actual` in the UPPER tail is a **pre-commit violation**, published as
> **REVERSED** with full prominence.

**Complement redundancy — locked.** `| |S∩f̄| − |f̄|n/N | = | |S∩f| − |f|n/N |` identically,
so complementary binary features contribute duplicate terms. Exactly **one** member of each
complementary pair is included (mahmūsa not majhūra; shadīda not rikhwa; muṭbaqa not
munfatiḥa; mustaʿliya not munkhafiḍa). This is a locked de-duplication, not a selection.

**Reported alongside every p-value (locked):** null mean, SD, minimum, the exact
percentile of `D_actual`, and the exact fraction of subsets attaining the global minimum.

## 6. Null models

**N1 — uniform subset null, computed EXACTLY (no sampling).** All `C(28,14) = 40,116,600`
subsets (and all `C(29,14) = 77,558,760` for T-B), each equally weighted. Because every
letter's contribution to `D` is a function only of the group-membership profile, the exact
distribution is obtained by enumerating over cell-count vectors weighted by
`Π C(n_i, k_i)` for H1, and by full split-half table enumeration over all subsets for H2.
Both are **exact**, not Monte-Carlo. Reported as exact.
`p_N1 = #{D_null ≤ D_obs} / C(N,14)` — **tie-inclusive**, the conservative choice, since
`D` is heavily tied.

**N2 — corpus-frequency-weighted subset null, Monte Carlo.** 14 letters drawn **without
replacement with probability ∝ corpus grapheme count**. This is the confound-controlling
null: [[h-new-1810-letter-frequency|H-NEW-1810]] established the muqaṭṭaʿāt-14 carry
74.4 % of corpus letter-mass, so a frequency-biased draw asks whether the phonetic balance
survives once that known bias is granted. **10,000,000 draws, seed 20260509**;
`p_N2 = (#{D_null ≤ D_obs} + 1) / (10,000,000 + 1)`. MW-5 replication at seed **20260511**.

The two nulls sit on different rows of the statistical-rigor-protocol §1.6 tree
(pure combinatorial vs corpus-frequency-conditioned), satisfying the two-null requirement.

## 7. Multiple-comparison correction

Family = **5 tuples × 2 hypotheses × 2 nulls = k = 20**.
**α_bon = 0.05 / 20 = 0.0025.** Raw and corrected p reported for every cell. The family
includes every cell that will be run; no cell may be dropped after seeing its value.

## 8. Decision rules — LOCKED, all four outcomes named in advance

Per cell:

- **OPTIMIZER-CONFIRMED** — `p < 0.0025` in the locked (low) direction. The attested set is
  more feature-balanced than the C(28,14) alternatives at corrected significance. The
  "articulatory-feature-space optimizer" reading survives.
- **CONFIRMED-BUT-MEANINGLESS** — the per-category counts reproduce al-Zamakhsharī's
  enumeration (so the classical *description* is factually exact) **AND** `p ≥ 0.0025`.
  **Verdict text is locked in advance**: *"the classical claim is descriptively true and
  statistically empty; 'half of each genus' is the expected value of a random 14-subset,
  not a design signature."* This is a **full-status finding**, published with the same
  prominence as a confirmation (Protocol §1.3), and is the pre-stated most-likely outcome.
- **NULL** — `p ≥ 0.0025` **and** `D_obs` at or above the null median. The set is not even
  descriptively balanced under that tuple.
- **REVERSED (pre-commit violation)** — `D_obs` in the upper tail at
  `p_upper < 0.0025`. Published with full prominence as REVERSED; no re-derivation, no
  massaging, no post-hoc direction flip.

**Headline verdict rule (locked):** the finding's headline follows **T-A × H1 × N1** (the
claim as al-Zamakhsharī states it, on the inventory he states it for, against the exact
uniform null). Tuple-dependence is reported in full; if tuples disagree the headline is
prefixed **RULES-TUPLE-FRAGILE**.

## 9. Garden-of-forking-paths disclosure (written BEFORE the run)

### Known before the lock
- **al-Zamakhsharī's nine stated intersection counts** (5/9/4/10/2/12/3/11/2) and hence
  `D_obs` under T-A. Unavoidable: reading the passage is a precondition of citing it. §0.
- While assembling the T-C feature table it became visible that the bayniyya class
  {ر ع ل م ن} lies **entirely inside** the muqaṭṭaʿāt-14, so `D_obs` under T-C is partly
  known pre-lock as well. Disclosed; it changes no locked decision, since T-C's direction
  and threshold are fixed here.
- The 14-letter set, the 29-surah/30-locus census, and the letter-frequency normalisation
  were computed before the lock as **input preparation** and are asserted as MW-6 controls.
  None of them is the test statistic's null.

### Not known before the lock (the entire empirical content)
- Every null distribution, mean, SD, minimum, minimum-mass, percentile and p-value, for
  all 20 cells.

### Choices made after seeing data
- None. All five tuples, both hypotheses, both nulls, the tie-inclusive p-rule, the
  complement de-duplication and the verdict language are fixed above.

### Alternative rule-tuples considered and DISCARDED, with reasons
- **lām-alif (لا) as a 29th letter of the hijāʾī list.** Discarded on principle: لا is an
  orthographic **ligature**, not a phoneme, and has no ṣifa/makhraj of its own. Including
  it would require inventing feature values, which is precisely the forking freedom this
  protocol exists to forbid. Recorded, not run.
- **Modern IPA/distinctive-feature encodings** (voice, continuancy, pharyngealisation as
  articulatory phonology). Discarded: the claim under test is a *classical* claim about
  *classical* genera; scoring it on a modern feature inventory would test a different
  proposition. Flagged as a legitimate separate future test.
- **ة counted separately from ت, ى separately from ي.** Discarded to hold the
  normalisation identical to H-NEW-1810 so the frequency vector is directly comparable;
  H-NEW-1810 §"Honest limits" already flags this as a 1–2-letter sensitivity.

### Sibling hypotheses in the same sitting
- H2 (frequency-weighted) is the only sibling, and it is pre-registered here rather than
  reported selectively. Its absolute-mass form is a re-derivation of H-NEW-1810 T3
  (muq-14 = 74.4 % of mass) and is reported **descriptively only**, never as a test.

### Why this test and not those
- Because H-NEW-1810 §"Interpretation" named **"phonetic-articulation balance"** as
  candidate #1 for the muqaṭṭaʿāt selection criterion after falsifying the
  frequency-criterion reading, and left it untested. This is that test.

## 10. MW-1 … MW-7 compliance

- **MW-1** instrument-prior: `D`, `D_freq`, the feature table, the tuples, both nulls and
  the thresholds are all fixed above, before any null is computed.
- **MW-2** corpus-prior: N1 is **exact over the entire subset space** (stronger than any
  permutation count); N2 uses 10⁷ draws, ≫ the 10⁴ minimum.
- **MW-3** alternative models: 5 taxonomies × 2 statistics × 2 nulls.
- **MW-4** over-fitting: no fitted parameters anywhere; `D` has no free constants.
- **MW-5** replication: N2 re-run at seed 20260511; N1 is exact and needs none.
- **MW-6** instrument-control: seven runtime fail-fast assertions — (a) 30 loci / 29
  surahs; (b) derived 14-set == al-Zamakhsharī's fourteen; (c) surah list == H-NEW-1740's
  catalogue; (d) letter-frequency table reproduces all 28 H-NEW-1810 counts + total
  329,131 + standalone hamza 1,578; (e) feature table reproduces al-Zamakhsharī's nine
  stated intersection counts; (f) category sizes 10/8/4/7/5/5 and makhraj groups summing
  to 28; (g) exact enumeration totals equal C(28,14) = 40,116,600 and
  C(29,14) = 77,558,760.
- **MW-7** post-hoc cap: any observation beyond the 20 registered cells is exploratory and
  capped at single-test α = 0.05, and must be labelled as such.

## 11. Relation to the project's standing muqaṭṭaʿāt pillar

The muqaṭṭaʿāt are **book-introduction markers**, and the **letter-axis is orthogonal to
the content-axis** — al-Biqāʿī's content-*munāsaba* reading is FALSIFIED in 4 replications
(full-29, ḥawāmīm-7, ALM-6, ALR-5; [[h-new-600-letter-families|H-NEW-600]],
INVESTIGATION-PROTOCOL §3.7). H-NEW-2550 does **not** revisit the content axis. It tests
the **phonetic** axis, which is untested, and it can only bear on whether the *selection*
of the 14 graphemes has an articulatory rationale — never on what the openings *mean*.
A confirmation here would not resurrect the content-cluster claim; a NULL here removes the
last quantitative candidate H-NEW-1810 left standing for a non-arbitrary selection rule.

## 12. Rules-tuple (canonical statement)

`(no-tashkeel for grapheme counts, full-tashkeel for muqaṭṭaʿāt-locus detection,
orthographic grapheme, 28-letter ḥurūf al-muʿjam with hamza-seats folded [أ إ آ ٱ→ا,
ؤ→و, ئ→ي, ة→ت, ى→ي] and standalone ء excluded, basmala-as-v.1-of-Q1-only, Hafs-Kūfan,
Mashriqī)`, plus the four declared variants of §4.
Sources: `quran-text/quran-no-tashkeel.json`, `quran-text/quran-full-tashkeel.json`.

## 13. Output files

- pre-reg (this file): `findings/phase-b-hypotheses/prereg-h-new-2550-muqattaat-phonetic-optimizer.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2550.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2550.json`
- finding: `findings/phase-b-hypotheses/h-new-2550-muqattaat-phonetic-optimizer.md`

---

## 14. ERRATUM recorded before the lock took effect — full disclosure

A first draft of this file was written out and hashed to
`4ec738f2948fca5d89d8b1c3e29fdf3f87335871aaec0a90166338b70edc2c7c`. It contained one
arithmetic error: the binomial `C(29,14)` (used only as an MW-6 runtime assertion constant
for tuple T-B) was written as **67,863,915**; the correct value is **77,558,760**. The
error was found and corrected **before any null distribution, percentile or p-value had
been computed** — i.e. before the observation this pre-registration exists to precede.

The correction touches no hypothesis, no direction, no null model, no threshold, no
Bonferroni k, and no decision rule; it replaces a wrong integer with the right one in two
places (§6, §10-MW-6). The superseded SHA is recorded here so the edit is auditable rather
than silent, per Protocol §1.8. The binding hash is the SHA-256 of this file **as it now
stands**, embedded in `scripts/h-new-2550.py` and verified at runtime.

---

## 15. AMENDMENT A1 — POST-OBSERVATION. Prior-art disclosure + a second codebook arm

**This section was written AFTER the primary run.** It is flagged as post-observation
throughout and is bound by three constraints, each verifiable by diffing against the
locked text above: it **adds prior-art disclosure**, it **adds test cells** (which
*tightens* the correction), and it **changes no locked direction and no threshold in the
loosening direction**. Nothing in §5 (direction), §6 (nulls), §8 (decision rules) or the
identity of the **primary** tuple is altered. Per Protocol §1.8 the amendment is recorded
here rather than folded silently into the locked text.

### A1.1 Prior art that the original lock missed — and how it moves the prior

A reconnaissance of the project's 906 files surfaced four muqaṭṭaʿāt-inventory findings
that the original §9 disclosure did not cite. They should have been cited; they are cited
now, and their effect on the prior is stated **before** the amended cells are computed.

| Finding | Question | Verdict |
|:--|:--|:--|
| **H-NEW-69** (2026-04-15, seed 20260415, k=8) | Does the muq-14 **COINCIDE** with any classical 14-of-28 grouping (shamsiyya/qamariyya, Sībawayh voicing, modern voicing, ṣafīr, iṭbāq)? | **NULL** — 0/8 at α_bon=0.00625, 0/8 even at unprotected α=0.05 |
| **H-NEW-44.2** (2026-04-16, 100k perms, k=8+1) | How do the muq-14 **distribute across al-Khalīl's 8 POA classes**? | **NULL** — 0/8 per-class; overall χ²=12.67, df=7, perm p=0.065 |
| **H-NEW-44.2.1** | Are all 4 pharyngeal/glottal letters muqaṭṭaʿāt? | PASS-DIRECTED, p=0.049 |
| **H-NEW-60** | Dotless preference | STRONG-PASS, 11/13 dotless, p=0.0009 |

**LOWERED PRIOR, stated explicitly:** H-NEW-69's NULL is evidence *against* the muq-14
being a designed phonetic partition. If the set matches no classical binary grouping, the
hypothesis that it was selected to realise a phonetic design is weakened before this test
begins. H-NEW-44.2's NULL does the same on the place-of-articulation axis. The
pre-registered expectation of §0 — CONFIRMED-BUT-MEANINGLESS as the most likely outcome —
is therefore **strengthened**, not weakened, by the prior art.

**How H-NEW-2550's question differs from H-NEW-69's.** H-NEW-69 asked a **matching**
question: *is the muq-14 the same set as some classical grouping G?* (statistic: overlap
k, per-grouping hypergeometric). H-NEW-2550 asks an **optimization** question: *does the
muq-14 split every genus near exact-half simultaneously?* (statistic: joint summed
deviation D, exact enumeration over the whole subset space). The tests are distinct.

**But they are closer than they look, and the amendment must say so.** For a grouping G,
"matches G" means k ≈ |G| or k ≈ 0 — i.e. **maximal** D. "Splits G at half" means
k ≈ |G|/2 — i.e. **minimal** D. **Perfect balance and perfect matching are opposite ends
of the same axis.** H-NEW-69's headline NULL is literally reported as *"k=9 vs E=9.0 for
majhūra, k=5 vs E=5.0 for mahmūsa … a striking NULL — the muqaṭṭaʿāt selection is
voicing-NEUTRAL"*, and it further notes that the observed split *"IS the expected ratio
under random selection given the asymmetric class sizes — not a meaningful pattern."*
That is this finding's thesis, stated qualitatively and one genus at a time, four months
earlier. H-NEW-2550's additive contribution is therefore narrower than the original brief
implied, and is exactly: **(i)** the JOINT statistic over all five genera at once rather
than genus-by-genus; **(ii)** the EXACT enumeration establishing whether the joint value
is a global optimum; **(iii)** the exact mass at that optimum — the number H-NEW-69's
per-grouping hypergeometrics cannot produce; **(iv)** the taxonomy-dependence test;
**(v)** the frequency-conditioned null. Claims (i)–(v) are what this finding may assert as
new. It may **not** assert that "the muqaṭṭaʿāt split the classical genera at chance
level" is a new discovery: **H-NEW-69 found that first**, and the finding will say so.

**Instrument corroboration (a benefit of the late discovery).** H-NEW-69 and H-NEW-165,
two independent prior pre-registrations, reproduce four of this test's five category
memberships from unrelated sources: H-NEW-69 G3 majhūra |G|=18 with k=9, G4 mahmūsa |G|=10
with k=5, G8 iṭbāq |G|=4 with k=2 (all identical to §3's table); H-NEW-165's locked
codebook gives ḥurūf al-tafkhīm = {خ ص ض ط ظ غ ق} (identical to §3's mustaʿliya) and
qalqala = {ق ط ب ج د} (identical to §3's qalqala). The fifth, shadīda, is enumerated by
al-Zamakhsharī himself. The §3 table was therefore **not** a free researcher choice — it is
pinned by a runtime fail-fast against al-Zamakhsharī's nine stated counts **and**
independently corroborated by two prior locks.

### A1.2 Two added tuples from a differently-sourced codebook (T-F, T-G)

The H-NEW-165 locked codebook (`h-new-165-phonological-predictor-prereg.md` §"Feature
codebook", sourced to Ibn Jinnī / al-Khalīl / Watson 2002 / Holes 2004, and shown
codebook-invariant across 4 variants by H-NEW-165.2) is added as an independent
sensitivity arm.

**It cannot become the PRIMARY tuple, for two reasons that are facts about the codebook,
not preferences:**

1. **It is defined only over the 14 muqaṭṭaʿāt letters.** Its per-letter table has 14 rows.
   The statistic `D` needs `|f|` over the **full 28-letter inventory**; supplying the
   missing 14 rows would be precisely the unlogged degree of freedom the reuse instruction
   exists to prevent.
2. **Its voicing coding is explicitly modern-adjusted and places ق in mahmūs** (its own
   text: *"we follow Ibn Jinnī's majhūra = jahr for consistency with modern phonetics"*,
   with a visible in-line self-correction). al-Zamakhsharī's claim is stated in the
   **classical** majhūra/mahmūsa categories and he explicitly lists **القاف** among the
   majhūra taken by the 14. Scoring his claim in a codebook that reclassifies ق would test
   a different proposition than the source makes.

Independently of both points, **primacy was locked before observation and cannot be
reassigned after it.** T-A remains primary; relabelling would be a pre-commit violation.

The parts of the H-NEW-165 codebook that ARE defined over all 28 letters are used, and the
place-of-articulation partition is taken from **H-NEW-44.2**'s full-28 al-Khalīl 8-POA
table (on disk, pre-registered 2026-04-16):

- **T-F** — 165-codebook ṣifāt only, 7 features: mahmūs (11), stops (7), ḥurūf al-tafkhīm
  (7), pharyngealized = tafkhīm ∪ {ع ح} (9), sonorant {ا ل م ر ي ن و} (7), idhlāq
  {ف ر م ن ل ب} (6), qalqala {ق ط ب ج د} (5).
- **T-G** — T-F **+ the 8 al-Khalīl POA classes of H-NEW-44.2** (15 features).

Two disclosures on T-F/T-G: (a) H-NEW-165's voice lists cover 27 of 28 letters, omitting
ج; ج is completed to majhūr as the **forced** closure (16+11=27, and it is the classical
value) — a completion, not a choice, and flagged. (b) tafkhīm ⊂ pharyngealized are nested,
not complementary, so both are retained; only genuinely complementary pairs are
de-duplicated, exactly as in §5.

### A1.3 Correction family — TIGHTENED, never loosened

Family grows from **k = 20** (5 tuples × 2 hypotheses × 2 nulls) to
**k = 28** (7 tuples × 2 hypotheses × 2 nulls). **α_bon moves from 0.0025 to
0.05/28 = 0.00178571** — strictly tighter. Every verdict already issued under
α_bon = 0.0025 is re-checked against the tighter threshold, and any cell that fails the
tighter one is **demoted**. No cell is promoted by this amendment.

> **Arithmetic correction, disclosed:** a first draft of this amendment wrote the family
> as k = 24 and α_bon = 0.00208333. That was a slip — 7 × 2 × 2 = 28. The correct k = 28
> is **tighter**, and the correction is consequential: it moves α_bon below
> T-A × H1 × N2 (p = 0.001828), demoting the only cell that had cleared. The correction is
> applied because it is right and because it runs in the conservative direction
> (tightening self-verifies; only loosening would need ratification). It is recorded here
> rather than quietly applied precisely because it *removes* this finding's sole positive
> result.

**Additionally, T-F and T-G cells are post-observation and are MW-7-capped**: they may
corroborate or contradict, but they may not by themselves establish a CONFIRMED verdict.
Both constraints — the tightened family α *and* the MW-7 cap — apply simultaneously.

### A1.4 T-D / T-E are a REPLICATION, not a discovery

**H-NEW-44.2 already tested the muq-14 against al-Khalīl's 8 POA classes and returned
NULL** (χ² perm p = 0.065). Tuples T-D/T-E ask the same substantive question with a finer
partition (al-Suyūṭī's 17/16 makhārij) and a different statistic (summed deviation vs χ²).
Whatever they return must be reported as **convergent replication of H-NEW-44.2**, and the
finding may not present a makhraj result as novel. Locked here, before the amended run.

### A1.5 What is NOT amended

Direction (§5, one-sided low, all tuples/hypotheses/nulls); both null models (§6); all
four verdict labels and their conditions (§8); the primary tuple (T-A); the headline rule
(T-A × H1 × N1); seeds 20260509 / 20260511; n_MC = 10⁷. The exact-enumeration results for
T-A…T-E are deterministic and the MC seeds are fixed, so every number already reported for
those five tuples must reproduce **bit-identically** on the amended run; this is asserted
rather than assumed.

### A1.6 Hash chain

| Stage | SHA-256 |
|:--|:--|
| draft (arithmetic erratum, §14) | `4ec738f2948fca5d89d8b1c3e29fdf3f87335871aaec0a90166338b70edc2c7c` |
| **binding lock, verified at the primary run** | `3faabc4df31f794db38b6c9495b296501f23fd917c902f0275c9744c38b7d0ed` |
| post-amendment (this file) | recorded in `csv/h-new-2550.json → prereg_sha256_amended` |

The **binding lock for the primary result is `3faabc4d…d0ed`** — the hash of this file as
it stood before any observation. The amended hash certifies only the amended run. The
script carries both and verifies the current file at runtime.

---

*Pre-registration locked 2026-08-07 by Waiel Al-Shujaa, before any computation of the null
distribution, any percentile, or any p-value. The observed statistic is the classical
source's own claim; the null is what nobody has computed. Bismillāhi al-Raḥmāni al-Raḥīm.*
