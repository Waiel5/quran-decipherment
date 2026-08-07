---
title: "H-NEW-2800 — The legal-formula frames: a closed inventory with positional structure"
author: Waiel Al-Shujaa
date: 2026-08-07
finding_id: H-NEW-2800
frontier_item: F-15
status: COMPLETE
verdict: NULL
verdict_long: "CLOSURE-FALSE + POSITION-NULL. The census stands as a descriptive result; every
  registered inference about closure and position fails; the one enrichment that passes its
  registered null fails against the stronger nuisance channel and rests on five verses."
prereg: findings/phase-b-hypotheses/prereg-h-new-2800-legal-formulae.md
prereg_sha256: 4eabc04e7977d9c932d38fed7094efb20d10e5c8daf828eef240044ffe3989bb
script: findings/phase-b-hypotheses/scripts/h-new-2800.py
run: findings/phase-b-hypotheses/runs/h-new-2800/20260807T060054Z/
seed_primary: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 5
alpha_bonferroni: 0.010
rules_tuple: "(no-tashkeel surface; QAC v0.4 morphological FEATURE FIELDS as the only matching
  layer — never raw substrings; orthographic-word indices; verse unit; basmala-counted-only-in-Q1;
  Hafs-Kufan; Mashriqi)"
classical_anchor: "al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān, nawʿ 65, ed. Muḥammad Abū al-Faḍl
  Ibrāhīm 1394/1974, vol. 4 pp. 39–40 — al-Ghazālī on the 500 āyāt al-aḥkām, and ʿIzz al-Dīn b.
  ʿAbd al-Salām naming three of the six frames"
---

# H-NEW-2800 — The legal-formula frames

**Verdict: NULL.** The claim was that a small closed set of legal frames accounts for *most*
legal-register verse onsets and that the frames occupy *characteristic positions* within their
surahs. Measured against a pre-registration sealed before any statistic was computed:

- **Closure is 0.35 %** on the inference-of-record inventory and **6.73 %** on the full
  inventory, against a locked threshold of 50 %. **CLOSURE-FALSE on every reading**, and this
  is settled on this corpus's own numbers with no baseline involved.
- **Neither positional arm passes.** Location p = 0.081, clustering p = 0.529, against
  α = 0.010. The frames sit where a within-surah random placement would put them.
- **The one inference that passes its registered null does not survive the stronger nuisance
  channel** and rests on **five verses**.
- **The genre control splits**, and the arm that splits against the claim is the one that
  carries the weight.

**What does stand is the census.** It was the deliverable regardless of any test, it is
complete, every occurrence is located, and it contains two facts worth more than the
hypothesis it was built to test: the classical *ikhbār* frames are **16 tokens in the whole
corpus**, and the register label this project has been using since H-NEW-2500 is **the same
object as one of the frames**.

---

## 1. The census — the deliverable

Matching is on QAC v0.4 morphological **feature fields**, never on raw substrings. Every
predicate is a conjunction of exact fields over consecutive orthographic words; the predicates
are printed verbatim in the pre-registration §5 and reproduced in §1.3 below.

### 1.1 Class A — the classical *ikhbār* frames

Source of the list: ʿIzz al-Dīn b. ʿAbd al-Salām, quoted by al-Suyūṭī (§6). **Not chosen by
me.**

| id | frame | n | at onset | verses | surahs | every location |
|:--|:--|--:|--:|--:|--:|:--|
| **A1** | *kutiba ʿalaykum* | **5** | 2 | 5 | **1** | 2:178:4, 2:180:1, 2:183:4, 2:216:1, 2:246:26 |
| **A2** | *ḥurrimat ʿalaykum* | **4** | 2 | 4 | 3 | 3:50:11, 4:23:1, 5:3:1, 5:96:9 |
| **A3** | *uḥilla lakum* | **7** | 2 | 7 | 4 | 2:187:1, 4:24:11, 5:1:6, 5:4:6, 5:5:2, 5:96:1, 22:30:11 |

*(locations are `surah:verse:word`, word index 1-based)*

**The entire classical *ikhbār* class is 16 tokens.** `kutiba ʿalaykum` occurs **five times and
in one surah** — all of al-Baqara. A "closed inventory" it certainly is; what it is not is
large enough to account for anything.

### 1.2 Class B — the frontier-map frames

Source: `HANDOFF/FRONTIER-MAP-2026-08-07.md` F-15 line 284 plus the dispatch brief, both
written before this pre-registration.

| id | frame | n | at onset | verses | surahs | locations |
|:--|:--|--:|--:|--:|--:|:--|
| **B1** | *fa-man lam yajid* | **3** | **0** | 3 | 3 | 2:196:45, 4:92:48, 5:89:26 |
| **B2** | *yā ayyuhā alladhīna āmanū* | **89** | 88 | 89 | **20** | (all 89 listed in the run JSON) |
| **B3** | *wa-lakum fī … ḥayāt* | **1** | 1 | 1 | 1 | 2:179:1 |

**B1 never once opens a verse.** All three occurrences are deep inside their verses — word 45,
48, 26 — and all three are *kaffāra* dispensations. A frame that never appears at an onset
cannot contribute to onset closure at all, which is a clean fact about the hypothesis rather
than about the data.

**B2 accounts for 89 of the 109 total occurrences and 88 of the 95 onsets.** The inventory is
one frame plus a long tail.

### 1.3 Class G — the generative structural rules

Declared as rules, locked before counting, each a proper superset of a Class-A or Class-B
frame. **Their higher coverage is arithmetic, not evidence** — this was stated in the
pre-registration and is repeated here so no reader mistakes it.

| id | rule (QAC predicate) | n | at onset | surahs |
|:--|:--|--:|--:|--:|
| **G1** | `POS:V ∧ PERF ∧ PASS` + word carrying (`LEM:EalaY` ∨ `l:P+` ∨ `LEM:li`) ∧ 2nd-person pronoun | 21 | 6 | 9 |
| **G2** | `LEM:>ay~uhaA` + (`POS:REL` ∨ `POS:N`) | 153 | 124 | 42 |
| **G3** | `POS:COND` (any lemma) | 1049 | 259 | 81 |

### 1.4 Distribution across the four registers

**All 109 Class A ∪ B occurrences fall in `legal_medinan` surahs. Zero in narrative, zero in
eschatological, zero in liturgical.** For A1 and B2 that is definitional (§2). For the other
four frames — A2, A3, B1, B3, fifteen tokens — it is not, but fifteen tokens landing in the
long Medinan surahs is a thin observation and is treated as one.

| register | verses | words | mean verse length | A∪B onsets | A∪B onset rate |
|:--|--:|--:|--:|--:|--:|
| narrative | 2,678 | 30,333 | 11.33 | 0 | 0.0000 |
| **legal_medinan** | **1,411** | **29,664** | **21.02** | **95** | **0.0673** |
| eschatological_mufaṣṣal | 884 | 6,788 | 7.68 | 0 | 0.0000 |
| liturgical_didactic | 1,263 | 15,590 | 12.34 | 0 | 0.0000 |

---

## 2. The register label is the same object as one of the frames

**This was declared in the pre-registration before any count was taken, and the data confirm
it exactly.**

I was directed to reuse the register labels verbatim from `csv/h-new-2530.json`. That file
does not hold them; its `genre_proxy_source` field points to
`h-new-2500.json genre_proxy.surah_genre`. Following the pointer,
`h-new-2500.json → genre_proxy.decision_procedure` reads:

> `1 legal_medinan: medinan AND (O-believers + kutiba-alaykum)>=1`

and `genre_proxy.legal_markers` reads `["يا أيها الذين آمنوا", "كتب عليكم"]` — **frames B2 and
A1 of the inventory under test.**

Measured on the data:

> **B2's 20 surahs are *exactly* the 20 `legal_medinan` surahs. Set equality.**
> `[2, 3, 4, 5, 8, 9, 22, 24, 33, 47, 49, 57, 58, 59, 60, 61, 62, 63, 64, 66]`

The label and the frame are not correlated; at surah granularity they are **the same object**.
Any statement of the form "the legal register contains these frames" is a restatement of the
label's definition. The 6.73 % full-inventory closure is therefore **not** a measurement of
anything: 88 of its 95 onsets are the marker that assigned the label.

This bounds the whole register-dependent half of the test and it is not repairable within the
instruction to reuse the labels verbatim. The pre-registration's response — run every
register-dependent inference on a **purged** inventory (locked inventory minus A1 and B2) and
treat the purged number as the inference of record — is what §3 and §4 report.

**This finding is also a flag on H-NEW-2500 / H-NEW-2530 and on cross-finding-028.** The
`legal_medinan` class is defined by two surface strings. That is legitimate as a *proxy* and it
is documented in 2500's own JSON, but any downstream result that reads "feature X separates the
legal register" needs checking against the possibility that X is correlated with those two
strings. This finding does not audit those results; it names the exposure.

---

## 3. H1 — closure. CLOSURE-FALSE, and settled without any baseline

Locked threshold for *"accounts for most legal-register verse onsets"*: **closure ≥ 0.50**.
Denominator: 1,411 verse onsets in the 20 `legal_medinan` surahs.

| inventory | matched onsets | closure | locked label |
|:--|--:|--:|:--|
| **purged (A2, A3, B1, B3) — inference of record** | **5** | **0.00354** | **CLOSURE-FALSE** |
| Class A alone | 6 | 0.00425 | CLOSURE-FALSE |
| Class B alone | 89 | 0.06308 | CLOSURE-FALSE |
| full A ∪ B (contaminated by §2) | 95 | 0.06733 | CLOSURE-FALSE |
| + Class G, the deliberately broad generative rules | 236 | 0.16726 | CLOSURE-FALSE |

**The claim fails by two orders of magnitude on the inference of record and by a factor of
seven on the most generous reading available.** Even throwing in three generative rules
written to be as inclusive as their classical templates allow — every passive-perfect
declarative, every vocative address, every conditional protasis in the language — coverage
reaches 16.7 %.

**No baseline text is involved in this result.** It is a property of this corpus measured
against a threshold locked in advance, and it is the cleanest thing in the finding.

### 3.1 Against the classical scale

al-Ghazālī, via al-Suyūṭī (§6), puts the *āyāt al-aḥkām* at **500 verses** — 8.02 % of 6,236;
the rival figure is 150, or 2.41 %. Corpus-wide, Class A ∪ B opens **95 verses**, **1.52 %**.

This comparison is a scale reference and **not a test**: the classical count is of verses that
*carry a ruling*, by any means, while the measurement here is of verses that *open with one of
six frames*. al-Suyūṭī's own text anticipates the gap in the same sentence —
*"perhaps they meant the explicitly stated ones, since much law is derived from the verses of
narrative, parable and the rest."* Ibn ʿAbd al-Salām, in the passage immediately following,
makes the same distinction structurally: rulings come from the **ṣīgha** (the imperative or
prohibitive *form*) as well as from **ikhbār** (declarative statement). **This inventory tests
only the ikhbār half of a two-part classical taxonomy**, and the classical source says in
advance that the other half is the larger one.

---

## 4. H2 — enrichment. Passes its registered null, fails the stronger channel, rests on five verses

### 4.1 The unit-drift declaration (UNIT-DRIFT-DEFECT.md §5)

**§5.1 — what the denominator is.** The number of verse **onsets**, which equals the number of
verses. It is a count of *opportunities*: a verse presents exactly one onset whether it is 3
words long or 130. Lengthening a verse does not create a second onset.

**§5.2 — its drift, measured, not asserted.**

| channel | Spearman ρ with the `legal_medinan` indicator |
|:--|--:|
| surah **verse count** *(the registered stratifier)* | **+0.0680** |
| surah **mean verse length** | **+0.5733** |
| ρ(verse count, mean verse length) | +0.4526 |

**The registered stratifier is the near-null channel.** The `legal_medinan` surahs are not
distinctively many-versed — they are distinctively **long-versed**: 21.02 words per verse
against 11.33 / 12.34 / 7.68 in the other three registers.

**§5.3 — which null holds size fixed.** The pre-registration locked verse count as H2's
stratifier, on the stated ground that the closure denominator *is* the verse count, and — per
UNIT-DRIFT-DEFECT §5 clause 1 and the H-NEW-2760 lesson — **required both channels to be
measured and both numbers published**. Both are below.

### 4.2 Both numbers

| arm | observed | null mean | null p95 | rate ratio | p | verdict |
|:--|--:|--:|--:|--:|--:|:--|
| **purged, stratified on verse count** *(registered primary)* | 5 | 1.133 | 3 | **4.415** | **0.0074** | **PASS** at α = 0.010 |
| **purged, stratified on mean verse length** *(the stronger channel)* | 5 | 3.408 | 5 | **1.467** | **0.2983** | **FAIL** |
| full inventory, verse-count strata — **not evidence** (§2) | 95 | 21.405 | 42 | 4.438 | 1.0 × 10⁻⁴ | contaminated |

**The registered inference passes and does not survive the channel that actually carries the
drift.** Against mean verse length the rate ratio falls from 4.415 to 1.467 and the observed
value sits **at** the null 95th percentile rather than above it. Per UNIT-DRIFT-DEFECT §5,
*"a control that does not use the strongest channel is not a control"* — so the honest reading
is that **H2 is not established**.

**And the registered PASS rests on five verses.** Observed = 5; that is the entire purged-onset
count in the corpus (A2 ×2 + A3 ×2 + B3 ×1, B1 contributing zero). H-NEW-2650 was degraded by
its locked rule for an arm on an n = 1 denominator; five is not meaningfully better company.

This is the H-NEW-2760 failure mode reproduced under a pre-registration that anticipated it. The
pre-registration is what makes it visible, and it is why both numbers are here.

---

## 5. H3, H4 — position. Both NULL

`rel(i) = (i − 0.5)/n_verses`; null = within-surah permutation holding per-surah frame counts
fixed. **The observed and permuted values share the identical denominator**, so verse-count
drift cannot act on this comparison — not because normalisation was assumed to confer
invariance (STATE §4.8 forbids that), but because it is literally the same number on both
sides. The run verifies the construction numerically: the null mean is **0.50017** against the
exact 0.5 the construction predicts.

### H3 — location. Direction locked LATER. FAIL.

| | value |
|:--|--:|
| observed mean relative position (n = 109) | **0.53765** |
| null mean | 0.50017 |
| p, locked direction | **0.0814** |
| α | 0.010 |

**The sign is as locked and the effect is not significant.** Not at α = 0.010, and not at 0.05
either. No pre-commit violation: the reverse tail is p = 0.919.

Robustness arms, and the one that matters:

| arm | n | observed | null | p (locked dir.) |
|:--|--:|--:|--:|--:|
| onset occurrences only | 95 | 0.5491 | 0.4997 | 0.0445 |
| `legal_medinan` only | 109 | 0.5377 | 0.5003 | 0.0700 |
| **purged inventory** | **15** | **0.3858** | 0.5000 | 0.9365 *(reverse p = 0.064)* |
| Class A only (the classical frames) | 16 | 0.4200 | 0.5005 | 0.8711 |

**The classical *ikhbār* frames sit EARLY, not late — the opposite of the locked direction.**
Class A's mean relative position is 0.420 and the purged inventory's is 0.386. The full
inventory's 0.538 is B2's doing: *yā ayyuhā alladhīna āmanū* falls late in al-Baqara and the
long Medinan surahs, and B2 is 89 of the 109 tokens.

This is exactly the split disclosed in the pre-registration's direction justification, where I
recorded knowing that `kutiba ʿalaykum` falls late in Q 2 while `ḥurrimat` / `uḥilla` open Q 5,
and locked LATER anyway. The bet was live and it did not pay. Neither side reaches
significance, so nothing is claimed in either direction.

### H4 — clustering. Direction locked MORE CLUSTERED. FAIL.

| | value |
|:--|--:|
| observed mean normalised gap (85 pairs, 15 surahs) | **0.11209** |
| null mean | 0.11156 |
| p | **0.5289** |

**There is no clustering at all.** The observed gap is marginally *larger* than random and the
p-value is a coin flip. Whatever else the *āyāt al-aḥkām* are, in this corpus they are not
positionally bunched: they sit within their surahs exactly as a random placement of the same
count would.

---

## 6. H5, H6 — the genre control. The arm that carries the weight fails

Statistic: **top-8 onset-bigram concentration** — the share of an arm's unit onsets covered by
that arm's **own** 8 most frequent onset bigrams. Each corpus gets its own best 8; al-Bukhārī is
never forced to use this corpus's frames. Same conjunction-strip applied to both.

### H5 — arbitrary matched partition (H-NEW-2680's `build_pseudo_corpus`, reused verbatim)

| arm | top-8 concentration |
|:--|--:|
| this corpus, `legal_medinan` (1,409 units) | **0.16111** |
| al-Bukhārī, 200 matched partitions | mean **0.05456**, range 0.0376 – 0.0795 |
| offsets with baseline ≥ observed | **0 of 200**, p = 0.0050 |

**PASS.** Trigram concentration agrees: 0.1065 against 0.0290.

**But this arm handicaps the baseline, and the pre-registration said so before the run.** Onset
formulaicity is boundary-sensitive; arbitrary cuts **destroy** al-Bukhārī's real onsets, so a
baseline *failure* here is **weak** evidence for the claim (STATE §4.7). H5 was never going to
settle anything on its own, which is why H6 exists.

### H6 — al-Bukhārī with its real boundaries

Units split at isnād openers (`حدثنا`, `حدثني`, `أخبرنا`, `أخبرني`) with the **splitting token
dropped** so the comparison is not circular in the splitter; 15,157 units; 200 subsamples of
1,409 to match the legal arm's unit count.

| arm | top-8 concentration |
|:--|--:|
| this corpus, `legal_medinan` | 0.16111 |
| **al-Bukhārī, real boundaries** | **0.29815** (range 0.2605 – 0.3293) |
| subsamples with baseline ≥ observed | **200 of 200**, p = **1.000** |

**FAIL, and by a factor of 1.85.** Given its authored unit boundaries, ḥadīth is **nearly twice
as onset-formulaic** as this corpus's legal register — after the isnād opener has been removed.
Trigram: 0.1572 against 0.1065.

**This is the arm that carries the weight.** It hands the baseline its real boundaries and so
handicaps *this* corpus; by the declared regime a baseline pass here is **strong** evidence
against the claim. It passes at the ceiling.

### 6.1 The two closed sets are of different kinds — a qualification that cuts both ways

*(post-hoc diagnostic D2; MW-7 single-test cap; not a registered inference)*

al-Bukhārī's onset concentration is **onomastic, not formulaic**. Of its top 32 onset bigrams,
**31 contain a name-chain element** (`بن`, `ابن`, `أبي`, `أبو`, `عن`, `عبد`), carrying
**97.6 %** of the top-32 mass: محمد بن (1,026), عبد الله (1,018), مالك عن (478), يحيى بن (466),
شعبة عن (460), سفيان عن (392)…

So ḥadīth's closed onset set is a closed set of **narrator names**, and this corpus's is a set
of **address and predication formulae** (يا أيها 106, إن الذين 39, ما كان 18). They are not the
same kind of object, and "ḥadīth is more formulaic, therefore the claim is generic" is too
quick.

**But this does not rescue the claim, and the reason is §3:** closure is 0.35 % / 6.73 %
against a locked 50 % threshold, measured on this corpus alone with no baseline in sight. The
genre control was never load-bearing here. The claim died on its own numbers.

### 6.2 Within-corpus reference

| register | top-8 onset-bigram concentration |
|:--|--:|
| **legal_medinan** | **0.16111** |
| liturgical_didactic | 0.07490 |
| eschatological_mufaṣṣal | 0.06271 |
| narrative | 0.05474 |

The legal register **is** the most onset-formulaic of the four, by roughly 2–3×. That is a real
descriptive contrast — and 88 of the 106 يا أيها onsets driving it are the label's own defining
marker (§2), so it is substantially a restatement of how the label was assigned.

### 6.3 A known instrument artefact, quantified

*(post-hoc diagnostic D1)*

`quran-text/quran-no-tashkeel.json` tokenises **U+06DE ۞ (rubʿ al-ḥizb)** as a standalone
verse-initial word. It opens **199 verses corpus-wide, 77 of them in the legal arm**, splitting
the real onset bigram (`۞ يا` instead of `يا أيها`). It affects **this corpus only** — the
baseline arms pass through a normaliser that removes it.

Removing it raises the legal arm from **0.16111 to 0.17246**, +0.01136. The H6 gap is 0.13704.
**The artefact deflates this corpus and cannot change either verdict**, but it is an asymmetry
in this corpus's disfavour and is recorded rather than left implicit. The corrected top bigram
is يا أيها at 113, matching G2's 113 legal onsets exactly.

---

## 7. The verdict, and a gap in my own locked rule

**The locked rule has an uncovered cell, and the run fell into it.**

Registered inputs: H1_purged = 0.00354 (< 0.50), H2 = PASS, H3 = FAIL, H4 = FAIL, H5 = PASS,
H6 = FAIL.

| locked branch (pre-reg §7) | evaluates |
|:--|:--|
| `CLOSED-INVENTORY-WITH-POSITION` — H1≥0.5 ∧ H2 ∧ (H3∨H4) ∧ H5 ∧ H6 | **False** |
| `GENRE-SHARED` — H2 ∧ (H3∨H4) ∧ (¬H5 ∨ ¬H6) | **False** — blocked by ¬(H3∨H4) |
| `POSITIONED-BUT-NOT-CLOSED` — H1<0.5 ∧ H2 ∧ (H3∨H4) | **False** — blocked by ¬(H3∨H4) |
| `NULL` — ¬H2 | **False** — H2 passed its registered null |

**All four branches evaluate False.** Every branch except `NULL` requires a positional arm, and
`NULL` requires H2 to fail; the case *"enrichment holds, position does not"* was not
anticipated. The script's final `else` assigned **NULL**. That fallback is **not in the
pre-registration** and is reported as what it is.

Two things make the outcome safe rather than a repeat of H-NEW-2600's failure:

1. **The fallback is the conservative direction.** It assigned the weakest available label to an
   uncovered cell. It did not manufacture a pass.
2. **The strong-channel reading reaches `NULL` through the rule itself.** H2 stratified on mean
   verse length — the channel eight times stronger than the registered one (§4.1), and the one
   UNIT-DRIFT-DEFECT §5 requires — gives p = 0.298, **FAIL**. With H2 = FAIL the `NULL` branch
   fires cleanly and no fallback is needed.

Both routes converge on **NULL**, so the verdict is not an artefact of the gap. The gap is
still a defect in the pre-registration and is recorded as one: **a locked decision rule must
partition the outcome space, not merely enumerate the interesting corners of it.** That belongs
beside STATE §4 lesson 4 as its complement — lesson 4 is *implement the rule you locked*; this
is *lock a rule that covers every cell*.

### Replication (seed 20260519)

| inference | primary | replication | stable |
|:--|:--|:--|:--|
| H2 (registered stratifier) | PASS | PASS | yes |
| H3 | FAIL | FAIL | yes |
| H4 | FAIL | FAIL | yes |
| H5 | PASS | PASS | yes |
| H6 | FAIL | FAIL | yes |

All five verdicts unchanged.

---

## 8. Classical anchor — verified on disk, with one gap declared

**al-Zarkashī cannot be cited and is not.**
`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` is on disk at
29,545,336 bytes, but `pdfinfo` reports
`Producer: Adobe Acrobat 7.05 Image Conversion Plug-in` and `pdftotext -layout` returns a
1,568-byte file with **zero lines**. It is an image-only scan with no OCR on disk. The project
already carries three `nawʿ PENDING` retraction markers against this same work
(`classical-iltifat-catalog.md` l.15, `classical-quantitative-claims-audit.md` l.159,
`abjad-residue-fasila-mechanism.md` l.10). **No page of al-Burhān is cited here.**

**What is cited instead**, verified line by line:

> **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 65
> (النوع الخامس والستون: في العلوم المستنبطة من القرآن), ed. Muḥammad Abū al-Faḍl Ibrāhīm,
> 1394 AH / 1974 CE, vol. 4 pp. 39–40.**
> File `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`
> (OpenITI / Shamela_0011728). Nawʿ heading at line **20725**; page markers `# PageV04P039`,
> `# PageV04P040`.

**(a) The scale of the legal-verse set — line 20976, vol. 4 p. 39:**

> قال الغزالي وغيره: آيات الأحكام خمسمائة آية وقال بعضهم مائة وخمسون قيل ولعل مرادهم المصرح به
> فإن آيات القصص والأمثال وغيرها يستنبط منها كثير من الأحكام.

*"al-Ghazālī and others said: the āyāt al-aḥkām are five hundred verses; some said a hundred
and fifty. It is said: perhaps they meant the explicitly stated ones, since much law is derived
from the verses of narrative, parable and the rest."*

**(b) The frames themselves — vol. 4 p. 40, al-Suyūṭī quoting ʿIzz al-Dīn b. ʿAbd al-Salām,
*Kitāb al-Imām fī adillat al-aḥkām*:**

> ويستدل على الأحكام تارة بالصيغة وهو ظاهر وتارة **بالإخبار** مثل **{أحل لكم}**
> **{حرمت عليكم الميتة}**، **{كتب عليكم الصيام}**

*"Rulings are inferred sometimes from the form (ṣīgha) — which is obvious — and sometimes from
declarative statement (ikhbār), such as {uḥilla lakum}, {ḥurrimat ʿalaykum al-mayta},
{kutiba ʿalaykum al-ṣiyām}."*

**This is an independent classical source for the frame list**, which is what F-15's own
confound note demanded. A 7th/13th-century jurist enumerates three declarative legal frames and
all three are Class A. The list was not chosen by me, and it was found *after* the inventory was
already fixed by F-15 and the dispatch brief — it corroborated a list, it did not select one.

**Nothing classical is refuted by this finding.** Ibn ʿAbd al-Salām did not claim his three
frames were frequent, or that they opened verses, or that they exhausted legal discourse — he
named them as *examples* of one of **two** modes, and explicitly called the other mode
(*ṣīgha*, the imperative/prohibitive form) the obvious one. al-Suyūṭī's own sentence warns that
the 500 figure covers only *al-muṣarraḥ bihi*, the explicitly stated. **The classical position
is that the legal register is not carried by a closed declarative inventory. This finding
measures how right that is:** the entire *ikhbār* class is 16 tokens.

**Secondary witness.** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*
(`data/literature/classical-tafsir/raw/qurtubi-jami-ahkam.openiti.raw.txt`, 20,485,460 bytes) —
the canonical *āyāt al-aḥkām* commentary; the three Class-A strings occur 90 times in it as
objects of legal discussion. Recorded as corroboration of genre, not as a measurement.

---

## 9. The two descriptive residues worth registering next

Neither is a registered inference here. Both are **post-hoc**, carry MW-7's single-test α = 0.05
ceiling, have **no null test**, and are named as candidates rather than claimed as results.

**(i) The generative *ikhbār* template G1 is almost exclusive to the legal register, and it is
not circular.** G1 — any passive perfect followed by a preposition with a 2nd-person pronoun —
occurs **21 times: 20 in `legal_medinan`, 1 elsewhere.** The single exception is **Q 11:28**,
*فعميت عليكم* ("so it was obscured to you"), in Hūd's speech — a genuine non-legal instance,
which is the right kind of exception for a template of this shape. Per-1,000-words: 0.674 legal,
0.033 narrative, 0.000 in both remaining registers. **G1 contains A1 but is not a label-defining
marker**, so unlike §2 this concentration is not definitional. It is 21 tokens, which is why it
is a candidate and not a claim.

**(ii) The conditional protasis G3 concentrates on the legal register on the drift-clean
normalisation.** Per **1,000 words** — the per-word rate, not the per-verse rate, precisely
because the legal register's verses are 21.0 words against narrative's 11.3:

| register | G3 per 1,000 words | per 100 verses |
|:--|--:|--:|
| **legal_medinan** | **18.17** | 38.20 |
| liturgical_didactic | 11.80 | 14.57 |
| narrative | 8.84 | 10.01 |
| eschatological_mufaṣṣal | 8.54 | 6.56 |

**2.06× narrative on the per-word normalisation**, on 1,049 tokens across 81 surahs — a far
better-powered signal than anything in the registered inventory, and one that survives the
per-word check that killed H2's rate ratio. A pre-registered test of *conditional-protasis
density as a register discriminator*, with a proper null and a matched ḥadīth control, is the
follow-up this run actually earns. **Legal discourse is carried by the *conditional*, not by a
closed declarative inventory** — which is a restatement of Ibn ʿAbd al-Salām's *ṣīgha* / *ikhbār*
distinction with the weight on the side he said carried it.

---

## 10. Honest limits

1. **The register label is circular and coarse.** §2 — it is the same object as B2 at surah
   granularity. It is also *surah*-level, so the closure denominator includes every verse of
   Q 2, Q 4, Q 5, Q 9 including narrative, polemic and creed. A low closure fraction is
   therefore partly denominator dilution. Neither is repairable under the instruction to reuse
   the labels verbatim, and both were declared in advance.
2. **H2's registered PASS rests on five verses** and does not survive the stronger nuisance
   channel. It should not be cited as an enrichment result.
3. **One baseline genre.** al-Jāḥiẓ and the dīwāns are not run: adab prose and pre-Islamic
   poetry are not legal discourse and cannot answer H5/H6's question. This test distinguishes
   this corpus from **ḥadīth** and from nothing else — and per STATE §5.4 three genres cannot
   establish what Arabic in general does.
4. **`bukhari-noquran.txt` is a single 4.6 MB line** with no preserved unit boundaries. H6's
   isnād-opener split is a **reconstruction**, not the editor's segmentation, and its units
   average 33.0 words against the legal arm's 21.0. Unit *count* is matched; unit *length* is
   not.
5. **QAC v0.4 is an instrument** and every count inherits its morphological decisions. There is
   no second Arabic morphological annotation of this corpus on disk to cross-check against.
6. **Class G's coverage is arithmetic.** G1/G2/G3 are supersets by construction; their higher
   numbers are not evidence for a closed inventory and are not reported as such.
7. **The locked verdict rule did not partition the outcome space** (§7). The verdict is safe
   because two independent routes reach it, not because the rule was sound.
8. **A found bug, declared.** The first version of the post-hoc diagnostics script had its
   Arabic character-range regex silently reordered by bidirectional text handling
   (`[ؐ-ًؚ-ٰ…]` instead of `[ؐ-ًؚ-ٟ…]`), which swallowed
   every Arabic letter and produced a zero-length word stream. It was caught because the stream
   was empty. **The primary run is unaffected** — its pattern is byte-identical to H-NEW-2680's
   and yields 526,250 Bukhārī words; the two normalisers were verified to produce *identical*
   output before the diagnostics were re-run. Both scripts now write these ranges as explicit
   `\uXXXX` escapes. Any future script typing an Arabic character range as a literal is exposed
   to the same silent corruption. The crashed run left an **empty** run directory at
   `findings/phase-b-hypotheses/runs/h-new-2800-diagnostics/20260807T060353Z/`. It is retained
   rather than removed, per the standing rule that no run directory is ever deleted; it is the
   marker of the failed attempt and its emptiness is the record.

---

## 11. Cross-references

- **Flags** `h-new-2500-*` and `h-new-2530-*` and **cross-finding-028**: the `legal_medinan`
  class is defined by two surface strings, one of which is set-identical to its member surahs
  (§2). Downstream register-separation results need checking against that exposure. Not audited
  here.
- **Reuses** H-NEW-2680's `build_pseudo_corpus` verbatim and its §4.7 boundary-sensitivity
  regime declaration.
- **Applies** `findings/UNIT-DRIFT-DEFECT.md` §5 in full, and **reproduces H-NEW-2760's failure
  mode** under a pre-registration that anticipated it: the registered stratifier was the
  near-null channel (ρ = +0.068) and the strong one (ρ = +0.573) reverses the verdict (§4).
- **Extends** the project's established-negatives line (STATE §3): another pre-registered,
  correctly-nulled retirement, and one where the classical source was never making the claim.
- **Does not touch** al-Bāqillānī, the compression family, or the muqaṭṭaʿāt line.

---

*Run 2026-08-07 by Waiel Al-Shujaa. Pre-registration sealed at SHA-256
`4eabc04e…89bb` before any statistic was computed; verified at runtime. Run directory
`findings/phase-b-hypotheses/runs/h-new-2800/20260807T060054Z/`, immutable, retained.
The claim was that a closed set of frames carries the legal register. The classical source
said in advance that it does not, and named the larger half. The measurement agrees with the
classical source. Bismillāhi al-Raḥmāni al-Raḥīm.*
