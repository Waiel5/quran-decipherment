---
title: "H-NEW-2950 — The sajdah loci: a glyph census, the 14-vs-15 dispute settled against the Arabic Itqān, and a NULL on textual marking"
author: Waiel Al-Shujaa
date: 2026-08-08
status: CENSUS ESTABLISHED (documentary) + NULL (inferential, underpowered)
frontier_item: F-8 (HANDOFF/FRONTIER-MAP-2026-08-07.md:234)
prereg_path: findings/phase-b-hypotheses/prereg-h-new-2950-sajdah-loci.md
prereg_sha256: 1495116ef07920d7753ed217a491f3b574e79ec3b6d94730cf75d39a7bc52847
script_path: findings/phase-b-hypotheses/scripts/h-new-2950.py
posthoc_script_path: findings/phase-b-hypotheses/scripts/h-new-2950-posthoc.py
run_dir: findings/phase-b-hypotheses/runs/h-new-2950/20260808T062704Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-2950-posthoc/20260808T063420Z
posthoc_run_dir_prior_identical: findings/phase-b-hypotheses/runs/h-new-2950-posthoc/20260808T062921Z
git_commit_at_run: 3b26fd2d7316bd71aaab814877f3dee30f4cc6b7
prior_work: [H-NEW-1330, H-NEW-1331, H-NEW-1510]
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/ABSENCE-CLAIMS.md, findings/PROXY-CLAIMS.md]
corrects: [H-NEW-1331 (classical labelling), H-NEW-1510 (citation locus)]
flags: [CORPUS-INTEGRITY-DEFECT — two truncated files in quran-text/]
---

# H-NEW-2950 — the sajdah loci

## Verdict in one paragraph

**The muṣḥaf marks 15 prostration points, the glyph set is identical across all eight text
variants that carry it, and it is the *union* of the two competing classical counts rather than
either one of them.** The on-disk Arabic *Itqān* gives al-Suyūṭī's own enumeration as **fourteen**
— counting al-Ḥajj twice and explicitly excluding Ṣād from the *ʿazāʾim* — so the mushaf's
fifteenth glyph is Ṣād, marked as a place of prostration that is *mustaḥabba* rather than
emphasised. **The prior manual verse list in this repository agrees with the glyph set exactly;
no finding inherits a discrepancy.** On the inferential side, **F-8 is NULL**: with the
prostration root removed, the loci are not distinguished from surah- and length-matched
neighbours on imperative density (p = 0.434) or second-person address (p = 0.359). A divine-name
enrichment cleared the Bonferroni gate (p = 0.0023) but **dissolves under a post-hoc probe
(p = 0.209)** once the divine names that are the *grammatical object of the prostration verb* are
also removed — it was residual circularity, not marking. **n = 15; this test is underpowered and
a NULL is not evidence of absence.**

Two by-products stand independently of both deliverables:

- **A corpus-integrity defect.** `quran-text/quran-flat-full-tashkeel.txt` and
  `quran-text/quran-flat-min-tashkeel.txt` are **byte-truncated at 1 MiB**, carrying 78.8 % and
  91.9 % of the corpus. Nothing in this repository reads them, which is why it had gone unnoticed.
- **A classical-labelling correction.** H-NEW-1331's PASS is labelled as holding under the
  "classical-Sunnī 14". Under al-Suyūṭī's *actual* fourteen it does not hold — that is the very
  13-surah arm H-NEW-1331 tested and dismissed as Mālikī at p ≈ 0.087.

---

## 1. The census — deliverable 1, documentary, no null model

Glyph: **U+06E9 ARABIC PLACE OF SAJDAH (۩)**. Counted mechanically over every text variant on
disk. This is not an inference and carries no p-value: the codepoint is in the file or it is not.

### 1.1 Per-variant table

| file | loci | glyphs | note |
|:--|--:|--:|:--|
| `quran-text/quran-full-tashkeel.json` | **15** | 15 | |
| `quran-text/quran-min-tashkeel.json` | **15** | 15 | |
| `quran-text/quran-no-tashkeel.json` | **15** | 15 | |
| `data/alt-text/quran-uthmani-txt-2.txt` | **15** | 15 | |
| `data/alt-text/quran-uthmani-min-txt-2.txt` | **15** | 15 | |
| `data/alt-text/quran-simple-txt-2.txt` | **15** | 15 | |
| `data/alt-text/quran-simple-min-txt-2.txt` | **15** | 15 | |
| `data/alt-text/quran-simple-clean-txt-2.txt` | **15** | 15 | |
| `data/alt-text/quran-uthmani-txt.txt` and 4 other unkeyed Tanzil files | — | 15 | no `s\|v` prefix, so glyph count only |
| `data/alt-text/quran-uthmani-consonantal.json` | 0 | **0** | consonantal skeleton; see §1.4 |
| `quran-text/quran-flat-no-tashkeel.txt` | — | 15 | 100 % coverage |
| `quran-text/quran-flat-full-tashkeel.txt` | — | **11** | **truncated**, see §1.3 |
| `quran-text/quran-flat-min-tashkeel.txt` | — | **13** | **truncated**, see §1.3 |

> **Eight variants carry a keyed locus set and all eight are byte-identical in it.** The
> apparent disagreement in the two flat files is not textual — §1.3 shows it is file truncation
> and accounts for every missing glyph exactly.

The brief warned not to assume agreement, because the waqf glyphs differed 0-vs-68 across
variants the previous day. **Here they do agree**, and the check was worth running: the two
counts that differ are a corpus defect, not a variant reading.

### 1.2 The 15 loci

| # | locus | # | locus | # | locus |
|--:|:--|--:|:--|--:|:--|
| 1 | **Q 7:206** | 6 | **Q 22:18** | 11 | **Q 38:24** |
| 2 | **Q 13:15** | 7 | **Q 22:77** | 12 | **Q 41:38** |
| 3 | **Q 16:50** | 8 | **Q 25:60** | 13 | **Q 53:62** |
| 4 | **Q 17:109** | 9 | **Q 27:26** | 14 | **Q 84:21** |
| 5 | **Q 19:58** | 10 | **Q 32:15** | 15 | **Q 96:19** |

Surah support: **14 surahs** {7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}. Q 22 is the
only surah carrying two. **15 verses in 14 surahs** — which is why "14" and "15" both circulate
in this repository as descriptions of the same set, one counting surahs and one counting verses.

### 1.3 Corpus-integrity defect — two truncated files

| file | body bytes | coverage | last complete verse | loci past the cut | glyphs |
|:--|--:|--:|:--|--:|--:|
| `quran-flat-full-tashkeel.txt` | **1,048,576** (exactly 1 MiB) | **78.78 %** | Q 40:65 | 4 — Q 41:38, 53:62, 84:21, 96:19 | 11 |
| `quran-flat-min-tashkeel.txt` | 1,048,577 (1 MiB + 1) | **91.90 %** | Q 61:4 | 2 — Q 84:21, 96:19 | 13 |
| `quran-flat-no-tashkeel.txt` | 752,948 | 100.00 % | Q 114:5 | 0 | 15 |

**The arithmetic closes exactly: 15 − 4 = 11 and 15 − 2 = 13.** Both files begin with the header
line `GROUP_CONCAT(text SEPARATOR ' ')` — they are SQL dumps whose output was cut at a 1 MiB
buffer. The no-tashkeel flat file, being smaller than 1 MiB, escaped.

`HANDOFF/FRONTIER-MAP-2026-08-07.md` §D.2 lists both files as **read by zero scripts**, which is
the only reason this has not corrupted a result. **Any future work reading them will silently
lose the last fifth of the corpus.**

### 1.4 The consonantal zero is expected, not a disagreement

`data/alt-text/quran-uthmani-consonantal.json` carries 0 glyphs. It is a derived consonantal
skeleton — it strips diacritics and non-letter marks generally, and U+06E9 goes with them. All
15 verses are present in it; only the marker is gone. This is **not** a variant that disagrees
about where prostration occurs, and it must not be cited as one.

---

## 2. The 14-vs-15 dispute, settled against the on-disk Arabic

### 2.1 What al-Suyūṭī actually writes

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, **nawʿ 35**
(`النوع الخامس والثلاثون: في آداب تلاوته وتاليه`), at page marker `PageV01P380`, in a *masʾala*:

> يسن السجود عند قراءة آية السجدة **وهي أربع عشرة** في الأعراف والرعد والنحل والإسراء ومريم
> **وفي الحج سجدتان** والفرقان والنمل و {الم تنزيل} وفصلت والنجم و {إذا السماء انشقت}
> و {اقرأ باسم ربك} **وأما ص فمستحبة وليست من عزائم السجود** أي متأكداته وزاد بعضهم آخر الحجر
> نقله ابن الفرس في أحكامه.

> "It is *sunna* to prostrate when reciting the sajdah verse, and **they are fourteen**: in
> al-Aʿrāf, al-Raʿd, al-Naḥl, al-Isrāʾ, Maryam, **and in al-Ḥajj two prostrations**, al-Furqān,
> al-Naml, {Alif Lām Mīm Tanzīl}, Fuṣṣilat, al-Najm, {When the sky is rent asunder}, and {Recite
> in the name of your Lord}. **As for Ṣād, it is *mustaḥabba* and is not among the *ʿazāʾim* of
> prostration** — that is, the emphasised ones. And some added the end of al-Ḥijr; Ibn al-Faras
> transmitted it in his *Aḥkām*."

### 2.2 The resolution, and it is not what the frontier map assumed

The brief framed the dispute as "Ḥanafī 14 vs Shāfiʿī 15, with Q 38:24 and Q 22:77 contested".
**The on-disk Arabic does not support that framing.** al-Suyūṭī, a Shāfiʿī, gives **fourteen**,
and his fourteen **includes both al-Ḥajj sajdas and excludes Ṣād**:

| set | Q 22:77 | Q 38:24 | count |
|:--|:-:|:-:|--:|
| the thirteen nobody disputes | — | — | 13 verses |
| **al-Suyūṭī's *ʿazāʾim*** (*Itqān* nawʿ 35) | **in** | **out** | **14 verses / 13 surahs** |
| the Ḥanafī count as ordinarily reported | out | in | 14 verses / 14 surahs |
| **the on-disk glyph set** | **in** | **in** | **15 verses / 14 surahs** |

> **The muṣḥaf glyph set is neither school's legal count. It is their union — every place a
> prostration is performed, whether *ʿazīma* or merely *mustaḥabba*.** Ṣād is the fifteenth glyph
> precisely because al-Suyūṭī still holds prostration there to be recommended while denying it is
> among the emphasised ones. The glyph marks the act, not the ruling's strength.

**The set also has a verified upper boundary.** al-Suyūṭī records a sixteenth candidate —
`وزاد بعضهم آخر الحجر`, the end of al-Ḥijr (**Q 15:98**), transmitted from Ibn al-Faras. **Q 15:98
carries no glyph in any variant on disk.** The mushaf marks the union of the mainstream positions
and stops short of the minority addition.

### 2.3 Two source checks, with the searches stated (per `ABSENCE-CLAIMS.md` §1)

**The English *Itqān* PDF does not contain this list.** Search performed on
`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`, extracted with
`pdftotext -enc UTF-8` to 830,557 characters: `prostrat` → 16 hits, `Prostrat` → 0, `sajda` → 0,
`sujud` → 0, `fourteen` → 3, `Fourteen` → 0. **Every one of the 19 hits was read.** None is the
enumeration; the nearest is al-Bayhaqī on not writing prostration signs into the muṣḥaf, which
corresponds to a different passage in the Arabic. The English edition is abridged at exactly this
point.

**This is the brief's warning confirmed on its own example.** A finding that searched only the
English would have declared al-Suyūṭī silent on the sajdah count. He is not; the Arabic carries it
in full, with the dispute, the reasoning and a sixteenth candidate.

**al-Zarkashī is not usable as a text anchor.** `zarkashi-al-burhan-fi-ulum-al-quran.pdf` yields
**1,568 characters** under `pdftotext` (with `Syntax Error: Can't get Fields array`) — it is a
scanned image with no text layer. `سجدة`, `السجدات`, `سجدات`, `عزائم`, `أربع عشرة`, `خمس عشرة`
all return 0, and that is a property of the extraction, not of al-Zarkashī. **Do not cite this
PDF as evidence of what al-Zarkashī does or does not say.**

---

## 3. Does the prior manual list agree with the glyph? — yes, exactly

The frontier map records that prior sajdah work used "a manually supplied verse list, not the
in-corpus glyph". That is accurate as to provenance. **The audit result is that the list is
nonetheless correct.**

| finding | set used | agrees with glyph set? |
|:--|:--|:--|
| **H-NEW-1510** | 15 verses, listed at `prereg-h-new-1510-...md:50-64` | **exact match, all 15** |
| **H-NEW-1330** | 14 surahs {7,13,16,17,19,22,25,27,32,38,41,53,84,96} | **exact match** (surah support of the glyph set) |
| **H-NEW-1331** | same 14 surahs | **exact match** |

**No finding inherits a discrepancy, and nothing downstream needs revision on this account.**
H-NEW-1510's prereg §"Pericope inventory" states it cross-verified the glyph in
`quran-text/quran-no-tashkeel.json`; that claim is independently confirmed here.

Under `PROXY-CLAIMS.md` this is the outcome its §2.1 insists is possible: **a hand-assigned
quantity that turns out to be sound.** The rule requires validation, not condemnation, and here
validation passes. It is worth recording as a clean negative audit.

### 3.1 But two citations are wrong, and one of them changes a verdict

**(a) H-NEW-1510 cites a nawʿ that does not exist.** It attributes the prostration-praise complex
to "al-Suyūṭī *al-Itqān* (nawʿ on sujūd al-tilāwa)". **There is no nawʿ on sujūd al-tilāwa in the
*Itqān*.** The material is a *masʾala* inside **nawʿ 35, `في آداب تلاوته وتاليه`** (§2.1). The
substance of the citation is sound; its locus is not. Cite nawʿ 35.

**(b) H-NEW-1331's PASS does not hold under al-Suyūṭī's own enumeration.** H-NEW-1331 reports
sajdah-surahs over-represented for muqaṭṭaʿāt-opening at **1.97× baseline, both cells PASS at
α = 0.05**, on **k = 7 of 14** surahs, and labels the set "classical-Sunnī 14". It then tests
**"Mālikī 13-surah list (excluding Q 38): k = 6/13, p_hyper ≈ 0.087 marginal — would not pass
strict α = 0.05"** as a dismissed sensitivity.

> **That 13-surah arm is also al-Suyūṭī's own *ʿazāʾim* support.** Dropping Ṣād is not a Mālikī
> peculiarity — it is what the Shāfiʿī authority this project cites actually writes. H-NEW-1331's
> headline therefore rests on an inventory the on-disk classical anchor does not endorse, and the
> arm it treated as a minority variant is the mainstream one.

Ṣād is muqaṭṭaʿāt-opened (ص), so it is doing real work in that ratio. **This does not refute
H-NEW-1331** — its 14-surah set is a legitimate object, being the glyph set's surah support — but
its classical framing must be restated, and **the honest strength of the claim is the p ≈ 0.087
arm, not the PASS.** I have not re-run H-NEW-1331; that is queued below.

---

## 4. The test — deliverable 2

### 4.1 Design, and the one decision that matters

Pre-registered at `prereg-h-new-2950-sajdah-loci.md`, SHA-256
`1495116e…c52847`, verified at runtime.

**The tradition chose these loci because they speak of prostration.** Asking whether they mention
prostration measures the selection rule, not the text. **Every feature count therefore removes all
QAC segments with `ROOT:sjd`** (prereg §2). The question becomes: *setting the prostration word
aside, is the locus marked?*

| element | locked value |
|:--|:--|
| instrument | QAC v0.4, `data/morphology/quranic-corpus-morphology-0.4.txt` |
| **F1 (primary)** | imperative count — `POS:V` + `IMPV` |
| F2 | second-person count — `(?:^\|\|)(?:PRON:)?2(?:MS\|MP\|FS\|FP\|D)(?:$\|\|)` |
| F3 | divine-name count — `LEM` ∈ {`{ll~ah`, `r~aHoma\`n`, `rab~`} |
| length variable | distinct QAC word indices per verse |
| candidate pool | verse *i* + the **K = 15** nearest-length **non-sajdah verses of the same surah** |
| statistic | **S = Σ of raw counts over the 15 loci** — a sum, not a density |
| null | one uniform draw per pool, independent across loci |
| p | **exact 15-fold convolution** over the full 16¹⁵ ≈ 1.15 × 10¹⁸ product space |
| direction | one-sided **upper**, all three axes, locked with justification |
| gates | Bonferroni α = 0.05/3 = **0.016667**; novelty gate min(1, 3p) < **0.005** |

**Unit-drift cannot reach this.** The statistic is a sum of integer counts with **no denominator**
(`UNIT-DRIFT-DEFECT.md` Screen A: not a ratio). Length and period are matched *within the
comparison itself* — every control verse is from the same surah and near the same length — rather
than adjusted for afterwards (Screen B). Nothing is hand-assigned (`PROXY-CLAIMS.md` Screen A).

### 4.2 Results — primary arm

| axis | observed | null E[S] | exact p | gate | verdict |
|:--|--:|--:|--:|:--|:--|
| **F1 imperative (PRIMARY)** | 5 | 4.375 | **0.4335** | α = 0.0167 | **NULL** |
| F2 second-person | 23 | 20.375 | **0.3588** | α = 0.0167 | **NULL** |
| F3 divine-name | 17 | 8.062 | **0.002292** | α = 0.0167 | PASS-DIRECTED, **not** novelty gate (3p = 0.0069) |

**Replication arm** (seed 20260519, K = 10 — a *tighter* match): F1 **0.5065**, F2 **0.3836**,
F3 **0.004787**. Same picture at both pool widths.

**Headline verdict, per the locked logic: NULL.** Prereg §7.2 states that if F1 fails its gate the
headline is NULL whatever the secondaries do, and that a secondary passing while the primary fails
is a descriptive observation requiring its own prospective pre-registration — **not** support for
F-8. That is applied here without exception.

### 4.3 F1 fails decisively, and the per-locus data says why

**Twelve of the fifteen loci contain zero imperatives once the prostration verb is removed.** The
survivors are Q 22:77 (3), Q 53:62 (1), Q 96:19 (1).

The registered diagnostic (prereg §7.3 — **not gated, cannot support a PASS**) re-runs the axes
*without* the `ROOT:sjd` exclusion: F1 rises to 9 observed against 4.625 expected, **p = 0.0789 —
still short of the gate even in its circular form.**

> **Four of the nine imperatives at the sajdah loci are the prostration command itself.** F-8's
> leading axis fails not merely after the anti-circularity control but before it. The loci are not
> imperative-dense; they contain an imperative *to prostrate*, and little else.

### 4.4 The power statement, registered in advance and honoured

**n = 15. This test is underpowered.** Three floors, all computed on the actual pools:

| floor | value | meaning |
|:--|--:|:--|
| realised on these pools (F1) | 4.0 × 10⁻¹⁴ | smallest p attainable given the observed ties |
| tie-free floor, 16⁻¹⁵ | 1.16 × 10⁻¹⁹ | if every pool had a unique maximum |
| sign-test floor, 2⁻¹⁵ | **3.05 × 10⁻⁵** | from the weaker "all 15 exceed their pool median" |

> **The binding constraint at n = 15 is power, not p-resolution.** The floors are small; what is
> scarce is the ability to detect a modest effect. **A NULL here is not evidence that the loci are
> unmarked** — it is evidence that any marking is not large enough for fifteen verses to reveal
> under a surah- and length-matched null. This sentence was written into the pre-registration
> before the numbers existed and is repeated unchanged.

---

## 5. Post-hoc — the F3 observation dissolves

**Not pre-registered. Cannot create, upgrade or rescue any verdict.** Run separately at
`runs/h-new-2950-posthoc/20260808T063420Z/`; the registered run directory was not touched. An
earlier run at `…/20260808T062921Z/` used a cosmetically different script and **reproduces every
number below exactly**; both directories are retained.

**The problem.** Removing `ROOT:sjd` deletes the verb *prostrate* but leaves its grammatical
object. `فَٱسۡجُدُواْ لِلَّهِ` (Q 53:62) loses `usjudū` and keeps `li-llāh`. **The divine name at
these loci is frequently the thing being prostrated to** — which is as definitional as the verb.
My §2 exclusion was too narrow and I did not see it until the per-locus texts were read.

**The probe.** Also remove divine-name tokens within 2 word positions of a `ROOT:sjd` token:

| | observed | E[S] | exact p |
|:--|--:|--:|--:|
| registered F3 | 17 | 8.06 | **0.00229** |
| **F3 with sjd-adjacent divine names also removed** | **10** | 7.56 | **0.2086** |

**Seven of the seventeen tokens are adjacent to the prostration verb, and removing them takes the
observation from p = 0.0023 to p = 0.21.** I read all seven: six are genuinely the verb's
complement (Q 13:15 `wa-li-llāhi yasjudu`; Q 22:18 `anna llāha yasjudu lahu`; Q 22:77 `wa-sjudū
… rabbakum`; Q 25:60 both `li-l-Raḥmān` and the objectors' echo; Q 53:62 `fa-sjudū li-llāhi`).
**One is over-removal** — Q 19:58's `āyāti l-Raḥmān`, where the divine name is the possessor of
the *signs*, not the object of prostration. Restoring that single token gives observed 11,
E = 7.63, **p = 0.1295 — still NULL.**

> **F3 was residual circularity, not textual marking.** The window is a crude proxy for
> grammatical government and it over-removes; it is reported because it can only weaken an
> observation that was already not a pass, and because the conclusion holds either way.

---

## 6. Honest limits

1. **n = 15, and it governs everything.** See §4.4. The NULL retires the *claim*, not the
   *possibility*.
2. **Three loci are poorly length-matched.** Mean |Δ words| across all pools is **3.74**, and
   **68.4 % of pool members are within 2 words** — but Q 38:24 (32 words, mean |Δ| 17.2, max 21),
   Q 19:58 (29 words, mean 13.5) and Q 22:18 (37 words, mean 11.1) are long verses whose surahs
   do not contain fifteen comparably long ones. Their pools are systematically *shorter*, which
   biases the observed counts **upward** — against the NULL and in favour of the F3 observation
   that already dissolved. **I state the direction but do not lean on it:** H-NEW-740 is the
   worked case of direction-of-bias reasoning getting the sign backwards. The actual check is the
   K = 10 replication arm, which agrees.
3. **F3's adjacency window is a proxy for syntax.** A dependency-parsed version using
   `data/syntax/` would be the right instrument. Not run here.
4. **Three axes are not the whole hypothesis space.** Rhyme position, pericope boundary, oath
   particles and vocative density are untested at this unit.
5. **The classical claim is about recitation, not text.** Nothing here bears on practice.
6. **The Ḥanafī 14 is reported from the standard secondary framing, not verified on disk.** I
   verified al-Suyūṭī's fourteen in the Arabic *Itqān* directly. I did **not** locate a Ḥanafī
   primary text in this repository and am not asserting one exists. The union reading in §2.2
   rests on al-Suyūṭī plus the glyph, both verified.

---

## 7. What this settles, and what it queues

**Settled:**
- The glyph count is **15**, the loci are enumerated, and **eight variants agree exactly**.
- The set is the **union** of the competing counts, with **Q 15:98 verified absent** as its
  upper boundary.
- **The prior manual list is correct.** No downstream finding inherits an error from it.
- **F-8 is NULL** on imperative density and second-person address.
- `quran-flat-full-tashkeel.txt` and `quran-flat-min-tashkeel.txt` are **truncated**.

**Queued (each needs its own prospective pre-registration):**
- **H-NEW-2951** — re-run H-NEW-1331 with al-Suyūṭī's 13-surah *ʿazāʾim* support as the registered
  primary and the 14-surah glyph support as the sensitivity, reversing the current framing.
- **H-NEW-2952** — F3 with true dependency government from `data/syntax/` rather than a word window.
- **H-NEW-2953** — repair or delete the two truncated flat files, and grep for any reader.

---

## Sources

- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` — nawʿ 35
  `النوع الخامس والثلاثون: في آداب تلاوته وتاليه`, masʾala at `PageV01P380` (§2.1, verbatim).
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4,
  SHA-256 `a1d12923…5d8c46`.
- `quran-text/quran-no-tashkeel.json` — SHA-256 `253f72f3…35918a`.
- `findings/phase-b-hypotheses/prereg-h-new-2950-sajdah-loci.md` — SHA-256 `1495116e…c52847`.
- Run: `findings/phase-b-hypotheses/runs/h-new-2950/20260808T062704Z/{result,manifest}.json`.
- Post-hoc: `findings/phase-b-hypotheses/runs/h-new-2950-posthoc/20260808T063420Z/{result,manifest}.json`
  (and the identical earlier run at `…/20260808T062921Z/`).
- Prior work: `h-new-1330-sajda-surahs-cluster.md`,
  `h-new-1331-sajda-muqattaat-overrepresentation.md`,
  `prereg-h-new-1510-sajda-pericope-replication.md`,
  `h-new-1510-sajda-pericope-replication.md`.
- Method: `findings/UNIT-DRIFT-DEFECT.md`, `findings/ABSENCE-CLAIMS.md`,
  `findings/PROXY-CLAIMS.md`, `STATE-OF-THE-PROJECT-2026-08-07.md` §0.
- Frontier: `HANDOFF/FRONTIER-MAP-2026-08-07.md:234` (F-8), `:577`, `:583-586` (D.2).
