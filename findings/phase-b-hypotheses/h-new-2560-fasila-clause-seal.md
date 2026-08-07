---
id: H-NEW-2560
title: The fāṣila is a clause seal — Quranic verse boundaries coincide with completed syntactic constituents at 8.1× the matched-chance rate, and the classical waqf grades independently confirm the instrument
date: 2026-08-07
phase: B
status: CONFIRMED (5/6) with one published PRE-COMMIT VIOLATION
verdict: "H1a/H1b/H3/H4/H5 PASS at the strict novelty gate; H2 REVERSED — the eschatological register seals LEAST, not most. EQTB-ANNOTATION-LIMITED."
author: Waiel Al-Shujaa
seed: 20260509
seed_h1b: 20260510
seed_replication: 20260511
n_perm: 10000
tests_in_family: 6
alpha_bonferroni: 0.008333
raw_p_gate: 0.000833
prereg_sha256: 4432e6fa79d330d5adc614d5175df8a70fd87476442f41bb289a6a248d7c3269
run_directory: findings/phase-b-hypotheses/runs/h-new-2560/20260807T003258Z
rules_tuple: "(no-tashkeel for the waqf join, EQTB segment-token, dependency arcs, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
data_source: Extended Quranic Treebank (EQTB) via the UD-Quran reproducibility package
---

# H-NEW-2560 — Is the fāṣila a clause seal?


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Pre-reg SHA `4432e6fa…3269`, runtime-verified. Seed 20260509 (H1b 20260510, replication
20260511), 10,000 permutations, k=6 registered inferences, Bonferroni α_bon = 0.008333,
project novelty gate corrected p < 0.005 hence raw gate p < 0.000833.**

The question: does Quranic syntax *close* at the verse-end? Classical scholarship asserts
it does, and the assertion has never been quantified. Using the Extended Quranic Treebank's
dependency annotation, a verse boundary is called **SEALED** when no dependency arc crosses
it. The result is measured against within-verse word boundaries drawn from the *same* verse,
so verse length is matched by construction.

## The results

| # | Registered inference | Observed | Null | p (10,000 perms) | Verdict |
|---|---|---|---|---|---|
| **H1a** | Sealed-rate, āya boundary vs matched within-verse word boundary | **0.8092** | 0.0993 | **1.0×10⁻⁴** | **PASS** |
| **H1b** | Sealed-rate under within-sentence segment-length permutation | **0.1163** | 0.0582 | **1.0×10⁻⁴** | **PASS** |
| **H2** | Sealed-rate, eschatological − legal | **−0.1948** | ≈0 | 1.000 | **REVERSED — pre-commit violation** |
| **H3** | Length-stratified, equal weight per stratum | **0.8135** | 0.0994 | **1.0×10⁻⁴** | **PASS** |
| **H4** | Constituent-split rate, āya boundary vs pseudo | **0.0345** | 0.3828 | **1.0×10⁻⁴** | **PASS** |
| **H5** | Sealed-rate, classical stop-preferred vs continue-preferred | **0.9056 vs 0.7364** | Δ≈0 | **1.0×10⁻⁴** | **PASS** |

`1.0×10⁻⁴` is the floor `1/10001`; no permutation of 10,000 reached the observed value.
H1a replicates at seed 20260510 and H5 at seed 20260511, both at the same floor.

**80.9% of the 6,094 eligible āya boundaries are syntactically sealed, against 9.9% for
word boundaries inside the same verses — a factor of 8.1.** Verse boundaries break a
phrase-level constituent 3.4% of the time; chance word boundaries break one 38.3% of the
time.

## The corpus census (a headline result in its own right)

| Quantity | Value |
|---|---|
| EQTB sentences | 11,693 |
| Sentences spanning **more than one verse** | **838 (7.2%)** |
| Longest sentence | **Q 55:46–76 — one sentence across 31 verses** |
| Sentences beginning mid-verse | 6,769 (57.9%) |
| Internal verse boundaries | 6,122 |
| … coinciding with an EQTB sentence edge | 4,798 (78.4%) |
| … falling strictly inside a sentence | 1,324 (21.6%) |
| Dependency arcs | 103,751 |
| Mean crossing arcs at a verse boundary | 0.233 (max 9) |

## H5 — the classical validation, and why it is the load-bearing result

The muṣḥaf carries the pause-mark system descended from **al-Sajāwandī's *ʿIlal
al-wuqūf***, whose five ranks al-Suyūṭī quotes verbatim: *al-waqf ʿalā khams marātib:
lāzim, muṭlaq, jāʾiz, mujawwaz li-wajh, murakhkhaṣ ḍarūra* (**al-Suyūṭī, *al-Itqān fī
ʿulūm al-Qurʾān*, al-nawʿ 28, *fī maʿrifat al-waqf wa-l-ibtidāʾ***; on disk at
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, line 5173). The
same *nawʿ* names the monograph tradition: Abū Jaʿfar al-Naḥḥās, Ibn al-Anbārī, al-Zajjāj,
**al-Dānī**, al-ʿUmānī, **al-Sajāwandī** (line 5094).

4,360 of these marks sit at mid-verse word boundaries in `quran-text/quran-no-tashkeel.json`.
**No verse boundary is in this test at all.** The grades were assigned in the 6th/12th
century with no knowledge of dependency grammar; EQTB was annotated in 2025 with no
reference to waqf marks. They agree:

| Classical grade | Meaning | n | Sealed | Mean crossing arcs |
|---|---|--:|--:|--:|
| **qlā** ۗ | *al-waqf awlā* — stopping preferable | 603 | 0.9071 | **0.103** |
| **mīm** ۘ | *waqf lāzim* — obligatory stop | 22 | 0.8636 | **0.136** |
| **jīm** ۚ | *jāʾiz* — permissible, explicitly neutral *(excluded from the test)* | 1,972 | 0.8469 | **0.193** |
| **ṣlā** ۖ | *al-waṣl awlā* — continuing preferable | 1,681 | 0.7496 | **0.306** |
| **lā** ۙ | ***lā waqf* — do not stop** | 68 | **0.4118** | **0.662** |
| muʿānaqa ۛ | embracing pause | 12 | 0.1667 | 1.000 |
| saktah ۜ | brief silence | 2 | 0.0000 | 1.000 |

Read down the crossing-arc column: **0.103 → 0.136 → 0.193 → 0.306 → 0.662 → 1.000.**
The ordering is monotone across the entire classical ladder, and *jīm* — which the
tradition itself calls neutral and which the registered test therefore excluded — lands
exactly in the middle where the pre-registration predicted it would.

The 68 *lā-waqf* positions are the sharpest cell: where al-Sajāwandī's tradition says
**do not stop here**, the dependency structure is open in 59% of cases and carries 6.4×
the crossing load of a stop-preferred position.

**Why this matters more than H1a.** H1a is close to a restatement of "āya boundaries
coincide with EQTB sentence boundaries" (78.4% vs 7.4% for pseudo-boundaries — see the
circularity section). H5 involves no verse boundary and no sentence-edge mechanism. It
shows the crossing measure tracks *syntactic closure as an independent tradition judged
it*. That is what licenses reading H1a as a fact about the text rather than about the
annotation.

## H2 — REVERSED. Published with full prominence.

The locked direction was **eschatological-mufaṣṣal > legal-Medinan**, on the reasoning
that a short verse is one proposition while a legal period is long and complex. The corpus
says the opposite, and says it decisively:

| Register | Boundaries | Sealed-rate |
|---|--:|--:|
| **legal_medinan** | 1,391 | **0.8950** |
| narrative | 2,647 | 0.8213 |
| liturgical_didactic | 1,240 | 0.7597 |
| **eschatological_mufaṣṣal** | 844 | **0.7002** |

Δ = **−0.1948**, p = 1.000. This is a **pre-commit violation** under
INVESTIGATION-PROTOCOL §1.8. It is not massaged and not rescued. The long legal period
closes at its fāṣila *more* reliably than the short eschatological verse.

*(Note on the run record: the machine verdict string in `result.json` flags only the H4
reversal branch, because the verdict logic did not enumerate an H2-reversal branch. The
underlying fields are unambiguous — `direction_held: false`, `passes_gate: false` — and
the immutable run directory has not been altered. The omission is recorded here rather
than corrected there.)*

### Post-hoc, descriptive only (MW-7 cap: no test, no p-value, not promotable)

The reversal has a mechanism, and it is one the project has already documented on an
orthogonal axis. Multi-verse sentences are *most* concentrated in the register that seals
least:

| Register | Multi-verse sentences | Verse boundaries swallowed |
|---|--:|--:|
| eschatological_mufaṣṣal | **13.61%** | 257 |
| narrative | 9.37% | 608 |
| liturgical_didactic | 7.62% | 309 |
| legal_medinan | **2.94%** | 150 |

The eschatological register's signature device is the ***idhā* conditional cascade**
([[h-new-2250-particle-cascade|H-NEW-2250]], §10.88; a pillar of
[[cross-finding-028-formal-register-coded-discourse-grammar|cross-finding-028-formal]]).
A cascade is a *protasis chain that withholds its apodosis* — and EQTB analyses **Q 81:1–14
as one sentence spanning fourteen verses**, the protasis running *idhā l-shamsu
kuwwirat …* until *ʿalimat nafsun mā aḥḍarat* discharges it at v.14.

al-Zamakhsharī states the governing grammar directly on Q 81:1: *li-anna «idhā» yaṭlubu
al-fiʿla li-mā fīhi min maʿnā al-sharṭ* — "because *idhā* demands a verb, by virtue of the
conditional sense in it" (**al-Zamakhsharī, *al-Kashshāf*, on Q 81:1**;
`data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt` line 70650).
The particle opens a dependency that must be discharged, and in the mufaṣṣal it is
discharged many āyāt later.

So the honest replacement for the falsified hypothesis is: **the eschatological register
is built on a device that deliberately suspends syntactic closure across verse
boundaries.** That statement is post-hoc and carries no p-value here. It is a candidate
for a future pre-registered test, not a finding.

## H3 — not a length artefact

The effect holds inside every stratum, and each stratum clears the gate on its own:

| Host-verse words | n | Sealed (true) | Sealed (null) | p |
|---|--:|--:|--:|--:|
| 2–4 | 1,082 | 0.6201 | 0.0401 | 1.0×10⁻⁴ |
| 5–8 | 1,405 | 0.7744 | 0.0967 | 1.0×10⁻⁴ |
| 9–15 | 1,904 | 0.8624 | 0.1154 | 1.0×10⁻⁴ |
| 16–30 | 1,432 | 0.8953 | 0.1203 | 1.0×10⁻⁴ |
| 31+ | 271 | 0.9151 | 0.1246 | 1.0×10⁻⁴ |

Sealing rises monotonically with verse length — 0.62 → 0.92 — which is the same fact H2
reports from the register side, since short verses are disproportionately eschatological.

## The circularity assessment — stated plainly

This was pre-registered as the material risk (pre-reg §3) and the assessment does not
change after seeing results.

**What is contaminated.** Because a dependency analysis of a sentence is largely connected,
SEALED is *near-equivalent* to "this verse boundary is also an EQTB sentence edge." The
exhibit: true boundaries sit at a sentence edge 78.4% of the time; matched pseudo-boundaries
7.4%. Anyone reading H1a must read it as, substantially, that statement.

**What rules out the strong form of the worry.** If annotators had segmented sentences *by*
āya, we would see ~100% of sentences beginning verse-initially and zero multi-verse
sentences. We observe **57.9% beginning mid-verse and 838 multi-verse sentences, one
spanning 31 verses**. Segmentation is syntax-driven.

**What cannot be excluded from this data.** The weak form — that annotators used the āya
boundary as a *tie-breaking prior*, splitting there when the syntax permitted. Nothing in
EQTB distinguishes that from a property of the text.

**What answers it anyway.** H4 operates on sub-sentential constituent spans (0.0345 vs
0.3828), and H5 operates entirely at mid-verse positions against an independent 12th-century
annotation. Neither can be produced by a sentence-segmentation convention. The verdict is
therefore **SUPPORTED, EQTB-ANNOTATION-LIMITED** rather than CIRCULARITY-LIMITED — but
H1a's number alone would not have earned that.

## The exception roster — where the Quran runs on

The 6,122 boundaries with the highest crossing load. These are the corpus's *taḍmīn*
points:

| Boundary | Crossing arcs | Host words | Register | Splits a constituent |
|---|--:|--:|---|---|
| **Q 9:111** | **9** | 37 | legal_medinan | **yes** |
| Q 23:2 | 5 | 5 | narrative | no |
| Q 81:19 | 5 | 4 | eschatological | no |
| Q 14:32 | 4 | 25 | narrative | no |
| Q 16:5 | 4 | 8 | liturgical_didactic | no |
| Q 20:105 | 4 | 7 | narrative | yes |
| Q 23:3 | 4 | 5 | narrative | no |
| Q 37:45 | 4 | 5 | narrative | no |
| Q 56:29 | 4 | 2 | liturgical_didactic | no |
| Q 68:10 | 4 | 5 | narrative | no |

**Q 9:111** — *āyat al-bayʿa*, the covenant of purchase — is the corpus maximum at 9
crossing arcs, and is one of only two entries in the top ten (with Q 20:105) that also
break a phrase-level constituent. **Q 23:2, 23:3, 23:4** form a contiguous run, and EQTB reads **Q 23:1–9 as a
single sentence**: the *alladhīna hum…* relative chain hangs off *al-muʾminūn* in v.1 and
cannot close until v.9. Q 56:29 (*wa-ṭalḥin manḍūd*, two words) is a coordinated member of
a list.

**An honest limit on the roster.** The dispatch anticipated cross-referencing these against
*lā-waqf* marks at the same verse-ends. That check is **not possible**, and the reason is
itself informative: the muṣḥaf system places **no waqf mark at any verse-end** (all 4,364
marks are mid-verse). al-Suyūṭī gives the doctrine — where the connection to what follows
is merely verbal, one may pause but not resume from what follows, *illā an yakūna raʾs āya*,
"unless it be a verse-end," which most practitioners permit on the authority of the ḥadīth
of Umm Salama (*al-Itqān*, nawʿ 28, line 5245). The classical system **cannot** mark a
verse-end as "do not stop," because the āya-end is licensed by default.

## What the classical tradition already said, and what is new

The tradition stated this thesis and also stated its exception, both of which are now
quantified. All quotations verified on disk in `suyuti-itqan.openiti.raw.txt`:

- ***rūʾūs al-āy fī nafsihā maqāṭiʿ*** — "the verse-ends are in themselves points of
  severance," and *al-qaṭʿ* "occurs only at a verse-end" (*al-Itqān*, nawʿ 28, line 5376).
  **This is H1a: 0.8092 vs 0.0993.**
- **al-Bayhaqī, *Shuʿab al-īmān***, quoted in the same *nawʿ* (line 5367): *al-afḍal
  al-waqf ʿalā rūʾūs al-āyāt **wa-in taʿallaqat bi-mā baʿdahā*** — pausing at verse-ends is
  preferable **even if they are syntactically connected to what follows**. The tradition
  knew that some verse-ends run on. **That class is now measured: 21.6% of boundaries are
  sentence-internal, 19.1% carry at least one crossing arc.**
- The reciters divided on exactly this axis: **ʿĀṣim and al-Kisāʾī** pause *ḥaythu tamma
  al-kalām* — where the sense is complete — while **Abū ʿAmr** deliberately pauses at
  verse-ends, *huwa aḥabbu ilayya* (*al-Itqān*, nawʿ 28, line 5364). H-NEW-2560 measures
  how often the two rules agree: **80.9% of the time.**
- **Umm Salama** (Abū Dāwūd, cited *al-Itqān* nawʿ 28, line 5370): the Prophet, when he
  recited, *qaṭaʿa qirāʾatahu āyatan āyatan* — severed his recitation verse by verse.

The contribution is therefore not the thesis but the **magnitude, the null, and the
independent instrument**: an 8.1× ratio against a length-matched null, a phrase-level
confirmation at 0.034 vs 0.383, and a monotone reproduction of the entire al-Sajāwandī
grade ladder from a dependency treebank that knew nothing of it.

This also supplies a syntactic mechanism for the project's existing **al-Bāqillānī
*iʿjāz al-fawāṣil*** result, the r = −0.86 content×rhyme anti-twin lock
([[h-new-730-content-rhyme-anticorrelation]]): the fāṣila is not only a phonological and
semantic juncture but a **syntactic** one.

## Honest limits

1. **EQTB dependency and constituent accuracy is the material limit.** No human validation
   sample was reviewed for this finding. Every number is annotation-conditional.
2. **H1a is circularity-exposed** in the weak form described above; H4 and H5 are what carry
   the conclusion.
3. **No cross-corpus control.** There is no matched Classical-Arabic dependency treebank on
   disk. **Nothing here is shown to be Quran-specific** — a comparable result might well hold
   for any text whose scribal tradition segments at sense-units. This is the single largest
   gap and the obvious next test.
4. **H2 is a falsified hypothesis**, and its mechanism is post-hoc.
5. The waqf marks are the modern muṣḥaf convention descended from al-Sajāwandī, not an
   autograph of *ʿIlal al-wuqūf*; the transmission passed through the Egyptian and Madinah
   printing traditions. Provenance of the digital text: Tanzil (`data/SOURCES.md`).
6. 3 verses (20:94, 37:130, 72:16) and 3 marks are excluded by the join gate; 28 verse
   boundaries are ineligible for H1a because their host verse is a single word.

## Files

- Pre-registration: `prereg-h-new-2560-fasila-clause-seal.md` (SHA `4432e6fa…3269`)
- Script: `scripts/h-new-2560.py`
- Immutable run: `runs/h-new-2560/20260807T003258Z/{result.json, manifest.json}`
- Summary: `csv/h-new-2560.json`
- Data manifest: `data/syntax/UD-QURAN-SOURCE.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*

---

## Run provenance and a retained duplicate run

Two run directories exist under `runs/h-new-2560/` and **both are retained deliberately**:

- `20260807T003258Z` — the first execution. Its `manifest.json` records a non-portable local
  input path, so it is **not committed**, but it is **kept on disk**.
- `20260807T004157Z` — a re-execution from a neutral input path. This is the committed run.

`result.json` is **byte-for-byte identical** across the two, verified by SHA-256. Every seed in
the script is a fixed literal, so the analysis is fully deterministic.

**Why both are kept.** Earlier in this project (H-NEW-2540 §8.1) a superseded run directory was
deleted on the reasoning that it was uncommitted and byte-identical to its replacement. That was
a protocol violation: "it was identical" is exactly the claim an audit trail exists to let someone
else verify. The standing correction — **run directories are never deleted, including uncommitted
and superseded ones** — is applied here. A run that cannot be committed is retained rather than
removed, and the reason is recorded.

---

## H5 rules-tuple disclosure — the waqf annotation is NOT identical across text variants

**Added 2026-08-07 after an independent audit. This is a disclosure the original write-up
owed and did not give.** The project rule is explicit: *rules-tuple specified, and every claim
tested under ≥2 tashkeel variants.* H5 was run under one.

Counting the Sajāwandī glyphs directly in each variant on disk:

| glyph | grade | `quran-full-tashkeel` | `quran-min-tashkeel` | `quran-no-tashkeel` |
|:--|:--|--:|--:|--:|
| ۖ *ṣlà* | *al-waṣl awlā* — continue | 1651 | 1682 | 1682 |
| ۗ *qlà* | *al-waqf awlā* — stop | 511 | 603 | **603** |
| ۘ *mīm* | *lāzim* — must stop | 21 | 22 | **22** |
| ۙ *lā* | *lā waqf* — do not stop | **0** | 68 | **68** |
| ۚ *jīm* | *jāʾiz* — neutral (excluded) | 2083 | 1972 | 1972 |
| ۛ *muʿānaqa* | embracing | 6 | 12 | 12 |
| ۜ *saktah* | brief silence | 8 | 7 | 5 |
| | **total** | **4280** | **4366** | **4364** |

`scripts/h-new-2560.py:453` reads **`quran-text/quran-no-tashkeel.json`**. That reproduces the
reported class sizes exactly: STOP-PREFERRED = *qlà* 603 + *mīm* 22 = **625**; CONTINUE-PREFERRED
= *ṣlà* 1682 + *lā* 68 = 1750, against a reported 1749 (one boundary excluded by the
mid-verse eligibility filter). The arithmetic is sound and the numbers are internally consistent.

**What was not disclosed: the variants disagree substantially, and one of them cannot run this
test at all.** `quran-full-tashkeel.json` contains **zero** ۙ *lā* marks — the *strongest*
continue-preferred signal in the ladder is simply absent from that file — and it carries 92 fewer
*qlà* and 111 more *jīm*. Under the full-tashkeel tuple the CONTINUE-PREFERRED class would
collapse to *ṣlà* alone and STOP-PREFERRED would fall from 625 to 532.

**Status of H5 under this disclosure.** The result stands as computed and its arithmetic is
verified, but it is **SINGLE-TUPLE** and must be labelled so until re-run under the
full-tashkeel inventory. I decline to predict the outcome: *ṣlà* supplies 1682 of the 1750
continue-preferred boundaries, so losing the 68 *lā* marks may matter little — but *qlà* also
drops by 92, and asserting robustness without running it would be exactly the unearned
confidence this protocol exists to prevent. **A second-tuple replication is queued as required
work, not optional.**

This does not touch H1a/H1b/H3/H4, which use no waqf data.

---

## H5 MAJOR CORRECTION — the effect is sentence-edge coincidence, and the claim of independence was FALSE

**Added 2026-08-07 after independent audit. This substantially demotes H5 and retracts the
strongest sentence in this file's own machine output.**

`result.json` states: *"H5 is the only inference in the family that is independent of EQTB
sentence segmentation."* **That claim is false, and it was never tested.** An independent
recomputation decomposed H5 by whether each waqf-marked boundary coincides with an **EQTB
sentence edge**:

| class | n | sealed rate | **at EQTB sentence edge** |
|:--|--:|--:|--:|
| STOP-PREFERRED | 532 | 0.9098 | **0.8891** |
| CONTINUE-PREFERRED | 1650 | 0.7485 | **0.6467** |
| *jīm* (neutral, excluded from H5) | 2079 | 0.8475 | 0.8153 |

Fisher exact on sentence-edge coincidence: **OR = 4.38, p = 4.34×10⁻³⁰**. Stop-preferred marks
are overwhelmingly sitting where EQTB *ended a sentence*.

**The decisive test — restrict to SENTENCE-INTERNAL waqf marks**, i.e. those the sentence
segmentation cannot explain (59 stop-preferred, 583 continue-preferred):

| direction | Fisher exact p |
|:--|--:|
| **locked** (stop-preferred seals more) | **0.9690 — FAILS** |
| reversed | 0.0621 — *trending backwards* |

**Once EQTB sentence-edge coincidence is removed, the locked direction does not merely weaken —
it fails outright and trends toward reversal.**

### What this means

H5 as computed largely measures **"al-Sajāwandī's stop marks fall where EQTB ended a
sentence."** If EQTB's sentence segmentation was itself informed by verse boundaries or by the
same traditional pause conventions al-Sajāwandī codified — and nothing on disk excludes that —
then H5 is **circular in exactly the way this file already conceded for H1a**, and the
concession was simply not carried across to H5.

**H5 is demoted from CONFIRMED to CIRCULARITY-DOMINATED / NOT INDEPENDENT.** It may not be
cited as validation of the classical waqf tradition against an independent parse. The honest
residual claim is far narrower: *al-Sajāwandī's stop-preferred marks and EQTB's sentence
boundaries agree closely* — two analyses of the same sentences agreeing, with the direction of
influence unestablished.

**Second-tuple replication (also completed independently):** under `quran-full-tashkeel`
(stop 532, continue 1650) the headline gap is +0.161 versus +0.169 under `no-tashkeel`, so the
rules-tuple disclosure above resolves favourably — the raw effect is tuple-robust. **That does
not rescue H5**, because the tuple was never the problem; the sentence-edge confound is, and it
is present in both tuples.

### Correction to the family verdict

The file's headline of "5/6 PASS" should be read as: **H1b survives as the least
circularity-exposed arm; H1a, H3, H4 and now H5 are all sentence-segmentation-exposed to
degrees this run did not measure; H2 is a published reversal.** A properly independent test of
the classical waqf tradition requires either a treebank whose sentence segmentation is
documented as verse-blind and pause-blind, or a non-syntactic prosodic instrument. Neither
exists on disk.

**Process note.** The claim of independence was asserted in the machine output rather than
tested. Asserting an independence property is not the same as demonstrating it, and a
robustness claim that carries the weight of a headline must be computed, not stated.
