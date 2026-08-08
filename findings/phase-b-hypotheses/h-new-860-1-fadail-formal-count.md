---
id: H-NEW-860.1
title: "The formal fadāʾil count — H-NEW-860's rubric carried no discriminative information, its anti-alignment was two size-loaded variables meeting, and under a length control the relationship is null in both directions"
phase: B
status: COMPLETE — pre-registered, locked, run, verdict diffed against the prereg's decision section
date: 2026-08-08
author: Waiel Al-Shujaa
repairs: H-NEW-860 (whose §7.1 absence claim is FALSE — ABSENCE-CLAIMS.md §6 FALSE #3)
prereg: findings/phase-b-hypotheses/prereg-h-new-860-1-fadail-formal.md
prereg_sha256: 15f3940478d1842a22ab99fee41e831e22934c7766d299339f477d824444c7f1
run: runs/h-new-860-1/20260807T221459Z
run_posthoc: runs/h-new-860-1/20260807T221832Z-posthoc
script: findings/phase-b-hypotheses/scripts/h-new-860-1.py
script_posthoc: findings/phase-b-hypotheses/scripts/h-new-860-1-posthoc.py
deliverable: findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv
seed: 20260509
seed_replication: 20260519
verdict: "UNDETERMINED on the locked primary arm (ρ = −0.2923, p = 0.0836) — the published ρ = +0.330 does not reproduce; all 18 pre-registered arms carry the OPPOSITE sign, and none survives a length control"
---

# H-NEW-860.1 — the formal fadāʾil count

## 0. The answer, in one place

**H-NEW-860 reported that classical ḥadīth attention is *anti*-aligned with architectural
significance: Spearman ρ(rubric, UAS_rank) = +0.330, p = 0.050, N = 36.** That number rested
on a hand-built 0–10 score which the finding itself called a "rough rubric", substituted
because a formal count "would require a ḥadīth-database … which is not on disk."

**The database was on disk, and had been since 2026-04-28.** Replacing the rubric with a
formal count over all 50,884 records returns four things.

1. **The published +0.330 does not reproduce. Every one of the 18 pre-registered arms carries
   the opposite sign.** The locked primary arm gives **ρ = −0.2923, p = 0.0836** →
   **UNDETERMINED** under the prereg's decision rule. Two of the three instruments at the
   primary cell clear the REVERSES gate, and the instrument closest to what the rubric
   claimed to measure — surah *naming* — reverses at **ρ = −0.6071, p = 8.6 × 10⁻⁵**,
   clearing Bonferroni.
2. **The rubric carried no discriminative information where it operated.** Against the formal
   quotation count over its own 36 surahs, **ρ = +0.055, p = 0.75**. Against the naming count
   it is *negative*, **ρ = −0.315**. Its apparent full-corpus signal (ρ = +0.374) is entirely
   the binary listed-versus-unlisted split — the floor effect H-NEW-860 diagnosed in its own
   full-corpus number without noticing it was the whole of its 36-surah number too.
3. **The mechanism is size, on both sides, and neither side is a ratio.**
   ρ(UAS_value, log surah word count) = **+0.608**; ρ(rubric, log surah word count) =
   **−0.522**. The rubric loaded on short devotional surahs, UAS loads on long ones, and the
   published "anti-alignment" is those two loadings meeting. The formal count loads on long
   surahs (+0.485), same sign as UAS, which is exactly why the coefficient flips.
4. **Under a length control nothing is left in either direction.** Partial Spearman
   controlling log surah word count: **−0.143 (p = 0.41)** on the primary arm, **−0.058
   (p = 0.54)** full-corpus. **The honest terminal statement is that there is no measurable
   relationship between ḥadīth reception and UAS once surah size is held fixed** — not the
   published anti-alignment, and not the alignment the raw formal count appears to show.

**H-NEW-860's §6 conclusion — that the ḥadīth corpus tracks *iʿjāz al-maʿnā* while UAS tracks
*iʿjāz al-fawāṣil*, "empirically separated" — is withdrawn.** No separation was measured. Two
size-loaded variables were correlated.

**The deliverable stands regardless**: `csv/h-new-860-1-reception-weights.csv`, all 6,236
verses with formal counts, per-book breakdown, driving span and eligibility — an instrument
this project has never had.

---

## 1. The absence claim that blocked this for three months

H-NEW-860 §7.1 and §Methodology:

> *"A formal corpus-wide hadith-mention count requires a hadith-database (Maktaba Shamela,
> sunnah.com index) which is not present on disk in this project."*

**FALSE.** `data/literature/hadith/ahmedbaset-json/` is a sunnah.com scrape:
**50,884 records across 17 books**, Arabic + English + narrator, per-book and per-chapter
indices, committed **2026-04-28** — the same day H-NEW-860 was written. Verified here by
direct enumeration: nine canonical books = **40,943**, eight anthologies = **9,941**.

Per `findings/ABSENCE-CLAIMS.md` §1, an absence claim is a claim about a search, and this one
never stated its search. It is FALSE #3 in that document's inventory.

---

## 2. The matching procedure, as executed

Locked in prereg §3 before any coefficient was computed.

### 2.1 Normalisation
NFC; delete U+0610–U+061A, U+064B–U+065F, U+0670, U+06D6–U+06ED, U+0640; map
{U+0622, U+0623, U+0625, U+0671} → alif, U+0649 → yāʾ, U+0629 → hāʾ, U+0624 → wāw,
U+0626 → yāʾ; keep only U+0621–U+064A and space. Qurʾān text is the imlāʾī
`quran-text/quran-no-tashkeel.json` — deliberately, because that is the orthography the
ḥadīth corpus is written in.

> **A defect worth recording, because it destroys silently.** Arabic literals inside a regex
> character class are **reordered by bidirectional text handling when the source file is
> written**. A probe's deletion range `[U+0610-U+061A U+064B-U+065F …]` was rewritten on disk
> into one spanning U+0621–U+064A, which stripped **every Arabic letter in both corpora** and
> returned a clean, plausible, entirely empty result. The runner therefore builds every
> character class **from integer codepoints** and **self-tests `norm()` at runtime** against a
> fixed vocalised basmala. Any script in this repository that writes an Arabic character range
> as a literal should be assumed broken until it is tested.

### 2.2 The link rule
A record **R** links to verse **v** iff R contains, at word boundaries, a contiguous span
**S** of v with:

- **length `n = min(N, |v|)` words**, **N = 5** locked primary (N = 4 and N = 6 as arms);
- **`|v| ≥ 4` words** — 600 shorter verses are **INELIGIBLE, not zero**;
- **S distinctive** — occurring in **exactly one verse** (verse-level count) or in verses of
  **exactly one surah** (surah-level count).

**Ownership is computed across every span length in play, from every verse.** Without this,
`بسم الله الرحمن الرحيم` looks verse-unique to Q 1:1 because Q 27:30's spans are longer, and
Q 1:1 collects 49 spurious "citations" that are the invocation formula. Under the locked rule
Q 1:1 and Q 1:2 are non-distinctive and receive no verse-level count — correct, because no
instrument reading text alone can tell a ḥadīth's basmala or taḥmīd from a citation.

**Why distinctiveness is not optional.** Without it, one ḥadīth saying
`يا أيها الذين آمنوا لا …` links to **twenty** verses at once, and at N = 4 the top "verse"
is Q 21:87 with **302** records driven by `أن لا إله إلا` — the shahāda fragment, 247 of them.

**Partial quotations count.** Reception of a verse includes reception of its famous clause.
The driving span and the maximum matched span length are published per verse so this is
auditable.

### 2.3 Multi-book rule — PER RECORD, in the nine books
Locked in prereg §4.1. A ḥadīth in both al-Bukhārī and Muslim counts **twice**. The reason,
fixed in advance: cross-book textual de-duplication needs a similarity threshold, and a
threshold is a free parameter chosen while looking at the records it would merge. Per-record
counting has none. `n_books` (0–9) and the nine per-book columns are published so any
alternative reading is recoverable without a threshold.

The eight anthologies (Riyāḍ al-Ṣāliḥīn, Mishkāt, Bulūgh al-Marām, al-Adab al-Mufrad,
Shamāʾil, three Forties) are **excluded from the primary** — they are drawn *from* the nine
and would multiply-count exactly the most famous material.

### 2.4 The naming instrument
Because the rubric scored *fadāʾil*, which names a surah rather than quoting it, a second
surah-level instrument counts the normalised token `سورة` + optional `ال` + the surah's
canonical name. **394 links over 58 surahs.** **No alias table** — `فاتحة الكتاب`,
`أم الكتاب`, `الزهراوان`, `المعوذتان`, `براءة` are *not* counted, because an alias list has no
principled stopping point and every entry is chosen while looking at the surah it would
raise. The cost was declared in advance and is measured in §9.3.

---

## 3. Does the instrument work?

Three checks, all locked before the outcome was touched.

### 3.1 Recall against explicit citations already in the corpus
Two explicit channels exist independently of the matcher: **986** `(sura:aya)` references in
the English field, and **2,504** brace-delimited `{…}` Arabic quotations.

| arm | verse-level recall | surah-level recall |
|:--|--:|--:|
| N = 4 | 0.827 | 0.858 |
| **N = 5 (locked)** | **0.761** | **0.807** |
| N = 6 | 0.661 | 0.711 |

The shortfall is not all error: it includes allusion without verbatim quotation, and
sunnah.com verse numbering that differs from this corpus's by one or two āyāt.

### 3.2 False positives, against text that cannot cite the Qurʾān
The Qurʾān was matched against **pre-Islamic dīwāns** (75,971 normalised words). Poetry that
predates the Qurʾān cannot quote it, so every link is a formulaic false positive.

| arm | ḥadīth links/Mword | poetry links/Mword | ratio |
|:--|--:|--:|--:|
| N = 4 | 1,674 | 158.0 | 10.6× |
| **N = 5** | **1,175** | **118.5** | **9.9×** |
| N = 6 | 1,003 | 92.1 | 10.9× |

118.5/Mword is an **upper bound** — some poetry hits are a scribal basmala, a real presence
of the string rather than a matcher error.

### 3.3 Scale
**2,355 of 40,943** records link to at least one verse. **749** of 5,371 eligible verses
carry a count. 3,147 verse-level links. Per book: al-Bukhārī 805, **al-Tirmidhī 568**,
Muslim 478, al-Nasāʾī 377, Abū Dāwūd 328, Ibn Mājah 214, al-Dārimī 182, Aḥmad 111,
Mālik 84. **al-Tirmidhī outranks Muslim**, which is H-NEW-860 §7.3's own qualitative claim
about where fadāʾil material lives, now measured.

---

## 4. The deliverable, and how concentrated it is

`findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv` — **6,236 rows, 22
columns**: `sura, aya, surah_name, n_words, eligible, ineligible_reason, n_hadith,
n_hadith_ambiguous, n_books, n_hadith_all17, n_hadith_surah_level, max_span_words,
driver_span,` and `b_bukhari … b_darimi`.

**Concentration, reported explicitly rather than averaged away:**

- **5,371** verses eligible; **600** ineligible for being under four words; **265** with no
  distinctive span. *Ineligible verses are blank, never zero.*
- **Only 749 of 5,371 eligible verses (13.9 %) are verbatim-quoted at all** in the nine books.
- **The top 20 verses hold 21.3 % of all links; the top 100 hold 49.1 %.**
- **Gini over eligible verses = 0.938.** This is why every statistic in this finding is
  rank-based and why no mean appears anywhere in it.

### The top 20

| # | verse | n | books | verse words | driving span |
|--:|:--|--:|--:|--:|:--|
| 1 | **Q 112:1** al-Ikhlāṣ | **102** | 9 | 4 | `قل هو الله احد` |
| 2 | **Q 87:1** al-Aʿlā | 63 | 8 | 4 | `سبح اسم ربك الاعلي` |
| 3 | **Q 109:1** al-Kāfirūn | 55 | 7 | 4 | `قل يا ايها الكافرون` |
| 4 | Q 64:1 al-Taghābun | 54 | 8 | 17 | `له الملك وله الحمد وهو` |
| 5 | Q 65:2 al-Ṭalāq | 36 | 9 | 30 | `كان يومن بالله واليوم الاخر` |
| 6 | Q 3:77 Āl ʿImrān | 34 | 7 | 27 | `ان الذين يشترون بعهد الله` |
| 7 | Q 33:21 al-Aḥzāb | 33 | 6 | 17 | `في رسول الله اسوه حسنه` |
| 8 | Q 25:68 al-Furqān | 32 | 5 | 22 | `لا يدعون مع الله الها` |
| 9 | **Q 1:7** al-Fātiḥa | 30 | 8 | 9 | `غير المغضوب عليهم ولا الضالين` |
| 10 | Q 2:158 al-Baqara | 27 | 8 | 24 | `ان الصفا والمروه من شعاير` |
| 11 | Q 2:125 al-Baqara | 24 | 8 | 22 | `واتخذوا من مقام ابراهيم مصلي` |
| 12 | **Q 113:1** al-Falaq | 22 | 6 | 4 | `قل اعوذ برب الفلق` |
| 13 | Q 2:187 al-Baqara | 21 | 7 | 65 | `الخيط الابيض من الخيط الاسود` |
| 14 | Q 2:196 al-Baqara | 21 | 7 | 73 | `ثلاثه ايام في الحج وسبعه` |
| 15 | Q 24:37 al-Nūr | 21 | 6 | 19 | `الله واقام الصلاه وايتاء الزكاه` |
| 16 | Q 4:95 al-Nisāʾ | 20 | 6 | 33 | `لا يستوي القاعدون من المومنين` |
| 17 | Q 48:2 al-Fatḥ | 20 | 9 | 15 | `ما تقدم من ذنبك وما` |
| 18 | Q 88:1 al-Ghāshiya | 19 | 7 | 4 | `هل اتاك حديث الغاشيه` |
| 19 | Q 92:5 al-Layl | 18 | 6 | 4 | `فاما من اعطي واتقي` |
| 20 | **Q 114:1** al-Nās | 18 | 5 | 4 | `قل اعوذ برب الناس` |

**Q 112:1 leads by 62 %** over the second place. **Seven of the top twenty are complete
four-word verses** — the corpus's reception at verse level is dominated by short, whole,
liturgically recited units, which is a real finding about how the tradition quotes and is
visible only at verse granularity.

**Āyat al-kursī (Q 2:255) is absent from the top 20, and the reason is a result in itself.**
It carries **1** distinctive record and **14** ambiguous ones. Its famous opening
`الله لا إله إلا هو الحي القيوم` is shared with Q 3:2 and so is non-distinctive (11–12
records). Its distinctive continuation `لا تأخذه سنة ولا نوم` occurs in the nine books
**exactly once**. **The ḥadīth corpus does not quote āyat al-kursī — it names it**:
`آية الكرسي` appears in **13** records. That is a finding about how the tradition cites, and
it is invisible to a quotation instrument and to a surah-level naming instrument alike
(§10.2).

---

## 5. Rubric versus formal count — the number with independent value

This is the deliverable that does not depend on any verdict, and the reason the task asked
for it: **it calibrates every other eyeballed proxy in this repository.**

| comparison | Spearman ρ | p | Kendall τ |
|:--|--:|--:|--:|
| **rubric × quotation count, on its own 36 surahs** | **+0.055** | **0.752** | +0.041 |
| **rubric × naming count, on its own 36 surahs** | **−0.315** | 0.061 | −0.231 |
| rubric × union, on its own 36 surahs | +0.006 | 0.972 | +0.003 |
| rubric × quotation, all 114 unlisted-as-zero | +0.374 | 4.1 × 10⁻⁵ | +0.297 |
| rubric × naming, all 114 unlisted-as-zero | +0.151 | 0.109 | +0.139 |

**Read the first row and the fourth together.** Across all 114 the rubric looks respectable
at ρ = +0.374 — but that is achieved entirely by the 78 surahs it scored 0 and which are in
fact rarely cited. **Restricted to the 36 surahs where the rubric actually did work — where
it assigned 1 through 10 — its correlation with the formal count is +0.055, indistinguishable
from nothing.** The rubric can tell "some ḥadīth presence" from "none". It cannot rank.

**And against the channel it claimed to measure it is negative.** The rubric scored
*fadāʾil* — praise that names a surah — and its correlation with actual naming is **−0.315**.

### Set overlap

| | rubric top-10 | formal top-10 | overlap |
|:--|:--|:--|--:|
| top 10 | 1, 36, 67, 112, 113, 114, 2, 18, 32, 50 | 2, 4, 3, 33, 5, 112, 6, 9, 87, 24 | **2/10** (Q 2, Q 112) |
| top 20 | + 76, 87, 88, 109, 3, 17, 19, 55, 57, 59 | + 8, 64, 109, 65, 17, 25, 18, 59, 48, 22 | **8/20** |

### The ten worst disagreements, both directions

| rubric over-rated | score | rubric rank | formal rank | formal count |
|:--|--:|--:|--:|--:|
| **Q 67 al-Mulk** | **10** | 3 | 35 | **0** |
| **Q 36 Yāsīn** | **10** | 2 | 30 | 4 |
| Q 76 al-Insān | 5 | 11 | 32 | 3 |
| Q 50 Qāf | 5 | 10 | 27 | 11 |
| Q 114 al-Nās | 10 | 6 | 22 | 18 |
| **Q 1 al-Fātiḥa** | **10** | 1 | 15 | 34 |
| Q 55 al-Raḥmān | 4 | 18 | 31 | 3 |
| Q 97 al-Qadr | 4 | 21 | 33 | 3 |
| Q 32 al-Sajda | 6 | 9 | 21 | 18 |
| Q 113 al-Falaq | 10 | 5 | 14 | 36 |

| rubric under-rated | score | rubric rank | formal rank | formal count |
|:--|--:|--:|--:|--:|
| **Q 33 al-Aḥzāb** | 2 | 34 | **3** | **130** |
| Q 6 al-Anʿām | 2 | 29 | 5 | 101 |
| Q 25 al-Furqān | 2 | 33 | 11 | 48 |
| Q 7 al-Aʿrāf | 1 | 35 | 16 | 26 |
| Q 9 al-Tawba | 3 | 23 | 6 | 92 |
| Q 24 al-Nūr | 3 | 24 | 8 | 61 |
| Q 3 Āl ʿImrān | 4 | 15 | **2** | 195 |
| Q 10 Yūnus | 1 | 36 | 26 | 12 |
| Q 12 Yūsuf | 2 | 30 | 20 | 19 |
| Q 62 al-Jumuʿa | 3 | 26 | 17 | 26 |

**And the rubric's list omits its own runner-up.** **Q 4 al-Nisāʾ is the second-most-cited
surah in the nine books (254 records) and does not appear in the rubric's 36 at all.**
Neither does Q 5 al-Māʾida (125, rank 5), Q 8 al-Anfāl (57), Q 64 al-Taghābun (55) or
Q 65 al-Ṭalāq (54). **Five of the formal top-14 were never scored.**

**H-NEW-860 §5's headline hidden-architecture case is the rubric's largest single error.**
It reported *"Q 33 al-Aḥzāb at UAS rank 1 with hadith-emphasis 2 … near-zero ḥadīth fadāʾil
presence"*. Q 33 is the **fourth most-cited surah in the corpus** — and the **third** among
the 36 the rubric itself listed — with 130 records across six books. The eyeballed score was not merely imprecise; it was wrong in the direction the
finding built its conclusion on.

**Calibration figure for this repository's other proxies: a careful, classically-informed,
citation-anchored hand rubric reproduced the measured quantity at ρ = +0.055 over the range
where it was applied.** That is the number to carry forward.

---

## 6. The re-run correlation

Sign convention, carried verbatim from H-NEW-860: **UAS_rank 1 = most architecturally
distinct**, so **positive ρ with rank = ANTI-alignment**. Our UAS-rank reconstruction
reproduces **36 of 36** of H-NEW-860's published ranks exactly.

### 6.1 The locked primary arm

| | published (rubric) | **formal (this run)** |
|:--|--:|--:|
| Spearman ρ with UAS_rank, N = 36 | **+0.330** (p = 0.050) | **−0.2923** (p = 0.0836) |

**Verdict logic, diffed against prereg §6.2 and printed by the runner before declaration:**

```
rho_pub = +0.330   half-bar = +0.165   alpha = 0.05
rho_f   = -0.2923  p_f = 0.0836  same_sign = False  clears_half = False
REVERSES   <- (not same_sign) and p<0.05           : False
SURVIVES   <- same_sign and p<0.05 and rho>=half   : False
WEAKENS    <- same_sign and (p>=0.05 or rho<half)  : False
UNDETERMINED <- (not same_sign) and p>=0.05        : True
```

**VERDICT = UNDETERMINED.** The published finding does not reproduce; the formal count points
the other way but does not clear the published significance bar.

### 6.2 All 18 pre-registered arms — every one is negative

| instrument | N | cell | n | ρ vs UAS_rank | p | clears Bonferroni α = 0.00278 |
|:--|--:|:--|--:|--:|--:|:--|
| Q | 4 | A | 36 | −0.3726 | 0.0252 | |
| Q | 4 | B | 114 | −0.3392 | 2.2 × 10⁻⁴ | ✔ |
| **Q** | **5** | **A** | **36** | **−0.2923** | **0.0836** | ← **primary** |
| Q | 5 | B | 114 | −0.3353 | 2.7 × 10⁻⁴ | ✔ |
| Q | 6 | A | 36 | −0.1800 | 0.2934 | |
| Q | 6 | B | 114 | −0.2757 | 0.0030 | |
| **N** | any | **A** | 36 | **−0.6071** | **8.6 × 10⁻⁵** | ✔ |
| **N** | any | **B** | 114 | **−0.5121** | **5.8 × 10⁻⁹** | ✔ |
| U | 4 | A | 36 | −0.3655 | 0.0284 | |
| U | 4 | B | 114 | −0.3426 | 1.9 × 10⁻⁴ | ✔ |
| U | 5 | A | 36 | −0.3192 | 0.0577 | |
| U | 5 | B | 114 | −0.3424 | 1.9 × 10⁻⁴ | ✔ |
| U | 6 | A | 36 | −0.2037 | 0.2334 | |
| U | 6 | B | 114 | −0.3002 | 0.0012 | ✔ |

*(The naming instrument does not depend on span length, so its three rows per cell are
identical. The locked k = 18 therefore over-counts the 14 distinct tests — this **tightens**
α and needs no ratification.)*

**All 18 are negative. Not one is positive.** Under the locked verdict rule, the N = 4
quotation arm (−0.3726, p = 0.025) and both naming arms would each return **REVERSES**. The
pre-designated primary returns UNDETERMINED only because N = 5 was chosen over N = 4 — and
**that choice was made pre-lock, on the false-positive evidence in §3.2 and §2.2, before any
coefficient existed.** Stating it plainly: had the equally defensible N = 4 been locked, this
finding would read REVERSES. The locked answer is the one reported.

### 6.3 Cell B, against H-NEW-860's own full-corpus numbers

| | published | formal |
|:--|--:|--:|
| Pearson r(·, UAS_value), N = 114 | +0.210 (p = 0.025) | +0.417 (p = 3.8 × 10⁻⁶) |
| Spearman ρ(·, UAS_value), N = 114 | +0.161 (p = 0.086) | +0.342 (p = 1.9 × 10⁻⁴) |
| Spearman ρ(·, UAS_rank), N = 114 | −0.065 (p = 0.495) | −0.335 (p = 2.7 × 10⁻⁴) |

The full-corpus association is *stronger* with the formal count than with the rubric. §7
shows it is size.

---

## 7. The length control, and what actually generated the published number

`findings/UNIT-DRIFT-DEFECT.md` §5's standing requirement, discharged.

### 7.1 The declared drift of every variable in play

| variable | ρ with log surah word count |
|:--|--:|
| **UAS value** | **+0.608** (p = 7 × 10⁻¹³) |
| **rubric score** (36 surahs) | **−0.522** (p = 0.0011) |
| formal quotation count | +0.485 (p = 4.6 × 10⁻⁸) |
| formal naming count | **+0.660** (p = 1.5 × 10⁻¹⁵) |
| H-NEW-590 outlier strength | −0.071 (p = 0.452) — **clean** |
| verse-level count × verse word count | +0.180 |

### 7.2 The mechanism

**H-NEW-860 correlated two variables that both load on surah size, with opposite signs.** The
rubric scored the short devotional surahs highest — Q 1, Q 36, Q 67, Q 112, Q 113, Q 114 all
at 10 — giving ρ = −0.522 with log word count. UAS loads the other way at +0.608. Two
opposite loadings on a shared nuisance channel produce a negative product with UAS_value and
therefore a **positive** ρ with UAS_**rank**. **That positive +0.330 is the "anti-alignment".**

The formal count loads on size with the *same* sign as UAS (+0.485 against +0.608), which is
the whole of why the coefficient flips to −0.292. **Neither sign is about ḥadīth or about
architecture.**

### 7.3 The controls

| control | result |
|:--|--:|
| **Partial Spearman controlling log word count, primary arm** | **−0.1426, p = 0.407** |
| Stratified permutation, k = 5 quintiles, seed 20260509 | p = 0.4178 |
| Stratified permutation, k = 5, replication seed 20260519 | p = 0.4180 |
| Stratified permutation, k = 10 deciles, seed 20260509 | p = 0.0852 |
| Stratified permutation, k = 10, replication seed 20260519 | p = 0.0785 |

**Both bin widths were pre-registered and both are reported**, per UNIT-DRIFT §6.1
requirement 2. They disagree, and the disagreement runs the *opposite* way to the usual case:
**the finer stratification makes the observation look more extreme, not less** (p = 0.418 →
p = 0.079), because tighter length bins shrink the null's spread from sd 0.104 to 0.085.
Neither clears α = 0.05. §6.1's caveat about fitted models does not apply — the statistic is
a correlation, which holds no size column, so stratified permutation is decisive here.

**Post-hoc, on the arms the locked run did not null-test:**

| cell | instrument | raw ρ | **partial ρ** | partial p |
|:--|:--|--:|--:|--:|
| A (36) | quotation | −0.2923 | **−0.1426** | 0.407 |
| A (36) | naming | −0.6071 | **−0.3125** | 0.064 |
| A (36) | union | −0.3192 | **−0.1602** | 0.351 |
| B (114) | quotation | −0.3353 | **−0.0584** | 0.537 |
| B (114) | naming | −0.5121 | **−0.1860** | 0.048 |
| B (114) | union | −0.3424 | **−0.0606** | 0.522 |

**Every arm collapses.** The one that stays nominally significant, naming at cell B
(−0.186, p = 0.048), does not clear Bonferroni α = 0.00278.

**Terminal statement.** Under a formal count with surah size held fixed, **there is no
measurable relationship between ḥadīth reception and UAS in either direction.** The published
anti-alignment is withdrawn, and the apparent alignment in the raw formal count is withdrawn
with it.

### 7.4 A gap in UNIT-DRIFT's own screens, found by this case

**Screen A asks whether the headline statistic is "a ratio with a unit count in the
denominator". For this claim the answer is NO, for both variables, and the defect is present
anyway.**

The rubric is a 0–10 hand score. UAS is a sum of three z-scores. Neither divides by anything.
Yet ρ(UAS, log word count) = +0.608 and ρ(rubric, log word count) = −0.522, and their
correlation is almost entirely those two loadings.

Screen B does not catch it either: this is neither an ordering nor a grouping, but a
**correlation between two variables**.

> **Proposed amendment, for the ledger keeper.** Add to `UNIT-DRIFT-DEFECT.md` §3:
> **Screen A′ — is either variable a composite, index, or hand score whose construction loads
> on unit size?** and to Screen B: **a correlation between two variables is a third shape of
> "the comparison", and it carries the defect whenever either variable is size-loaded.**
> One Spearman against log unit size per variable settles it, and it is the same one line of
> code the rest of the document already asks for. H-NEW-840's `status: SYNTHESIS` composite is
> the type case, and it has now generated at least one published claim.

---

## 8. The residual roster

**Descriptive only.** No p-value is attached, per prereg §7.3, and H-NEW-2620's tafsīr
analogue returned NULL.

The raw roster's low end is dominated by very short surahs — the instrument's floor, not
neglect — so the **length-controlled** roster is the one to read: reception rank residualised
on log surah word count.

### 8.1 Structurally extreme, cited far less than their length predicts

| surah | UAS rank | outlier rank | formal count | words | length residual |
|:--|--:|--:|--:|--:|--:|
| **Q 26 al-Shuʿarāʾ** | 14 | **8** | **3** | 1,320 | +46.5 |
| Q 51 al-Dhāriyāt | 15 | 113 | 2 | 360 | +35.5 |
| Q 16 al-Naḥl | 30 | 30 | 8 | 1,844 | +33.9 |
| Q 27 al-Naml | 23 | 108 | 6 | 1,159 | +31.0 |
| **Q 23 al-Muʾminūn** | **9** | 111 | 7 | 1,052 | +28.5 |
| **Q 55 al-Raḥmān** | **7** | **5** | **3** | 352 | +27.0 |
| Q 52 al-Ṭūr | 19 | 110 | 3 | 312 | +24.8 |
| Q 37 al-Ṣāffāt | 79 | 19 | 9 | 865 | +20.1 |
| **Q 10 Yūnus** | **8** | 106 | 12 | 1,839 | +17.9 |
| Q 30 al-Rūm | 56 | 17 | 9 | 817 | +17.6 |

**Q 55 al-Raḥmān and Q 26 al-Shuʿarāʾ are the sharpest entries** — top-10 on both structural
measures, three formal records each. Q 55 is a real case with a real cause: its
`فبأي آلاء ربكما تكذبان` refrain repeats 31 times, so it is non-distinctive at verse level by
construction, and the surah-level instrument still finds almost nothing.

**H-NEW-860 §5's list survives only in part.** Q 10, Q 23, Q 25 and Q 7 were listed there as
hidden architecture. On the formal count **Q 25 (48 records) and Q 7 (26) are not under-cited
at all** — they were artefacts of the rubric. **Q 10 and Q 23 hold up.** Q 33, its headline
case, is refuted outright (§5).

### 8.2 Cited far more than their length predicts, structurally ordinary

| surah | UAS rank | outlier rank | formal count | words | length residual |
|:--|--:|--:|--:|--:|--:|
| **Q 87 al-Aʿlā** | **114** | 65 | **63** | **72** | **−64.3** |
| Q 62 al-Jumuʿa | 95 | 81 | 26 | 177 | −39.6 |
| Q 88 al-Ghāshiya | 68 | 61 | 20 | 92 | −37.1 |
| Q 66 al-Taḥrīm | 77 | 84 | 22 | 254 | −31.2 |
| Q 5 al-Māʾida | 66 | 101 | 125 | 2,837 | −27.1 |
| Q 60 al-Mumtaḥana | 73 | 67 | 22 | 352 | −26.0 |
| Q 63 al-Munāfiqūn | 63 | 92 | 15 | 181 | −18.9 |
| Q 75 al-Qiyāma | 72 | 81 | 12 | 164 | −16.1 |

**Q 87 al-Aʿlā is the single sharpest residual in the corpus: dead last on UAS (rank 114),
72 words, and the ninth most-cited surah in the nine books.** Q 62, Q 88, Q 63 — the ʿīd and
jumuʿa recitation set — cluster with it. That cluster is real and is the one part of
H-NEW-860's qualitative §4 that the formal count supports.

**Fifteen surahs have zero formal reception**: Q 45, 67, 78, 79, 85, 86, 90, 91, 94, 100,
101, 103, 105, 106, 107. Two of them were scored by the rubric — **Q 67 at 10** and Q 78 at 3.
Q 67's zero is an instrument artefact and is diagnosed in §9.1.

---

## 9. Post-hoc diagnostics

Everything in this section is **POST-HOC** and changes no locked verdict.

### 9.1 Why al-Mulk reads zero — the four-word incipit

Q 67 was the rubric's rank-3 at score 10 and returns **0** under the locked N = 5.

- Q 67:1 = `تبارك الذي بيده الملك وهو علي كل شيء قدير` (9 words).
- The **four**-word incipit `تبارك الذي بيده الملك` occurs in **6** records.
- The **five**-word extension `تبارك الذي بيده الملك وهو` occurs in **0**.

**The tradition cites this surah by a four-word title and never continues into the fifth
word.** N = 5 cannot see it. At N = 4 the surah returns 6.

**How general is this?** Only **four** surahs show the pattern (four-word opening cited ≥ 5
times and more than twice its five-word extension): **Q 5** (`يا أيها الذين آمنوا`, 97 vs 2 —
a formula, correctly excluded), **Q 76** (12 vs 3), **Q 98** (8 vs 2), **Q 67** (6 vs 0). It
is a bounded defect, and Q 67 is its worst case.

### 9.2 Span sensitivity on the rubric's top ten

| surah | rubric | N = 4 | **N = 5** | N = 6 |
|:--|--:|--:|--:|--:|
| Q 1 | 10 | 30 | **30** | 6 |
| Q 36 | 10 | 10 | **4** | 4 |
| Q 67 | 10 | 6 | **0** | 0 |
| Q 112 | 10 | 111 | **111** | 111 |
| Q 113 | 10 | 36 | **36** | 36 |
| Q 114 | 10 | 18 | **18** | 18 |
| Q 2 | 9 | 485 | **328** | 257 |
| Q 18 | 9 | 44 | **37** | 25 |
| Q 32 | 6 | 31 | **17** | 17 |
| Q 50 | 5 | 14 | **11** | 11 |

Counts are stable for the short liturgical surahs and span-sensitive for the long ones —
long surahs are quoted in longer stretches and are cut differently by the threshold. This is
why all three spans were pre-registered and all three are reported.

### 9.3 External cross-check against this repository's own earlier extractions

This repository already contains per-surah ḥadīth extractions built **2026-04-28** by a
different method — alias-rich name search plus hand-tagged motifs, Arabic and English. A
second, independently constructed measurement.

| surah | independent (2026-04-28) | this run, union | quotation | naming | their method |
|:--|--:|--:|--:|--:|:--|
| Q 1 | 59 | 34 | 30 | 8 | alias-rich names (`أم الكتاب`, `السبع المثاني`) + English |
| Q 2 | 126 | **427** | 328 | 132 | alias + English |
| Q 6 | 14 | **101** | 98 | 5 | hand-tagged verse motifs |
| Q 19 | **236** | 21 | 20 | 2 | hand-tagged narrative motifs |
| Q 33 | **272** | 130 | 130 | 7 | hand-tagged verse + English motifs |

**This is not a validation of magnitude and must not be read as one — it is a demonstration
that "reception" is not one quantity.** The divergences are explained, in both directions:

- **Q 1 (59 vs 34)** — exactly the cost declared in advance for refusing an alias table
  (prereg §3.6). `فاتحة الكتاب` and `أم الكتاب` are not counted here.
- **Q 2 (126 vs 427)** and **Q 6 (14 vs 101)** — theirs counts *names and tagged motifs*;
  this run counts every record quoting any verse. Quotation dominates for long surahs.
- **Q 19 (236 vs 21)** — theirs counts ḥadīth mentioning ʿĪsā ibn Maryam and related
  narrative motifs. That is thematic resonance, not citation of Sūrat Maryam.
- **Q 33 (272 vs 130)** — theirs includes thematic hijāb and azwāj material.

**Three constructs are in play — verbatim quotation, explicit naming, and thematic
resonance — and they do not rank surahs the same way.** This finding measures the first two
and says so. Any future work using "reception" must name which one it means.

---

## 10. Honest limits

1. **This instrument measures verbatim quotation and explicit canonical naming. It does not
   measure allusion, paraphrase, thematic commentary, or occasion-of-revelation
   attribution.** §9.3 quantifies how much that leaves out: for Q 19 it is an order of
   magnitude.
2. **865 verses cannot receive a verse-level count** — 600 under four words, 265 with no
   distinctive span. They are `eligible = false`, never zero.
   **Named units below and across surah level are invisible to both channels**, and the gap
   is measurable: `آية الكرسي` 13 records, `فاتحة الكتاب` 58, `أم الكتاب` 23, `المعوذتين` 16,
   `خواتيم` 48, `الزهراوين` 1 — **159 naming events the locked instruments do not count**, by
   the alias decision fixed in prereg §3.6. Q 1, Q 2, Q 113 and Q 114 absorb most of it.
3. **Chain grade is not modelled.** A mawḍūʿ chain counts as a ṣaḥīḥ one. The corpus carries
   no grading field, and H-NEW-860's rubric had the same property.
4. **Musnad Aḥmad is incomplete upstream** — 1,374 records, chapters 8–30 absent from the
   source scrape. Aḥmad is under-weighted throughout; the per-book columns make it visible.
5. **UAS remains a corrected synthesis index** with `status: SYNTHESIS`, no null hypothesis
   and no test statistic (H-NEW-840; corrections in H-NEW-2680, H-NEW-2720). **Nothing here
   rehabilitates it, and no claim about the Qurʾān rests on any coefficient in §6 or §7.**
   What has been tested is whether H-NEW-860's stated result reproduces. It does not.
6. **The N = 5 / N = 4 choice is a real researcher degree of freedom and is disclosed in
   §6.2.** It was fixed pre-lock on false-positive evidence, and it is the difference between
   the reported UNDETERMINED and a REVERSES.
7. **Cell A inherits the rubric's own surah selection** — deliberately, for like-for-like
   comparison. §5 shows that selection omitted the second-most-cited surah in the corpus.
8. **Per-record counting across books is a choice** (prereg §4.1). `n_books` and the nine
   per-book columns are published so the alternative is recoverable.

---

## 11. What should change in the repository

1. **H-NEW-860's verdict line and its §6 dual-iʿjāz conclusion should be marked withdrawn.**
   Its §7.1 absence claim should be corrected in the file that carries it, per
   ABSENCE-CLAIMS.md §4 — not only here.
2. **H-NEW-860 §5's hidden-architecture list needs revision.** Q 33 is refuted (4th
   most-cited in the corpus); Q 25 and Q 7 are not under-cited; Q 10 and Q 23 hold up.
3. **UNIT-DRIFT-DEFECT.md §3 should gain Screen A′** (§7.4): a composite or hand score with
   no denominator can carry the defect, and this repository's most-cited composite does.
4. **The reception-weight table is now available to any finding that needs it** —
   `csv/h-new-860-1-reception-weights.csv`. It is the first per-verse reception instrument in
   this project.
5. **Calibration for every other eyeballed proxy here: ρ = +0.055.** Any finding resting on a
   hand-built score over a range it did not measure should be treated as unverified until the
   measurement exists.

---

## 11a. Run record

- Locked run `runs/h-new-860-1/20260807T221459Z/` — `result.json`, `console.log`, `MANIFEST.txt`
  (SHA-256 of every input and output). Mode `'x'`, `exist_ok=False`, no file inside it
  rewritten; checkpoints went to `scratch/h-new-860-1-checkpoints/`, outside it.
- Post-hoc run `runs/h-new-860-1/20260807T221832Z-posthoc/`.
- **`runs/h-new-860-1/20260807T221825Z-posthoc/` is empty and is left in place deliberately.**
  The first post-hoc invocation created its directory and then aborted on a `NameError`
  before writing anything. **A run directory is never deleted in this repository**, so the
  empty one stands as the record that an attempt was made and failed. It contains no results
  and none are missing.

All 23 headline figures in this finding were re-verified against `result.json` and the
deliverable CSV after writing.

---

## 12. Cross-references

- **[[h-new-860-hadith-architectural-alignment|H-NEW-860]]** — the parent, repaired here.
- **`findings/ABSENCE-CLAIMS.md`** §6 FALSE #3 — the false absence that blocked this.
- **`findings/UNIT-DRIFT-DEFECT.md`** — §5 discharged in §7; §3 amendment proposed in §7.4.
- **`STATE-OF-THE-PROJECT-2026-08-07.md`** §0 — the control-first rule; the length control
  here was run first, not second.
- **[[h-new-840-unified-architectural-score|H-NEW-840]]** — UAS; its size loading (+0.608) is
  measured here for the first time.
- **[[h-new-590-outlier-spectrum|H-NEW-590]]** — outlier strength; **clean** on size
  (ρ = −0.071), the only structural variable in this test that is.
- **H-NEW-2900 / H-NEW-2890** — the corpus census that made this runnable.
- **H-NEW-2620** — the tafsīr analogue of the residual roster; returned NULL.

---

*Run 2026-08-08 by Waiel Al-Shujaa against a pre-registration locked before any coefficient
existed. The rubric could tell presence from absence and nothing more, and what it correlated
with was size. Bismillāhi al-Raḥmāni al-Raḥīm.*
