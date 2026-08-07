---
finding_id: H-NEW-2740
title: Pre-registration — is the rasm/imlāʾ divergence set non-randomly distributed?
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
status: LOCKED BEFORE COMPUTATION OF ANY ASSOCIATION STATISTIC
seeds: 20260509 primary / 20260519 replication
n_perm: 10000
bonferroni_k: 5
alpha_bonferroni: 0.01
rules_tuple: >-
  (no-tashkeel-for-comparison [consonantal skeleton], orthographic-token,
  graphemes, basmala-counted-as-written-in-Tanzil [prefixed to first verse of
  each surah except Q9], Hafs-Kufan, Mashriqi/ʿUthmānī-Madinah print vs
  Tanzil-simple imlāʾī)
---

# Pre-registration — H-NEW-2740

**Nothing in this file was written after any association statistic was computed.**
What *was* computed before locking is listed in §10 (design marginals and the
divergence typology), and every such quantity is named there explicitly.

---

## 1. The question, and why this target

Words whose ʿUthmānī spelling diverges from standard orthography (صلوة for صلاة,
ٱلرحمن without alif, أولئك with an otiose wāw). **Are the divergences clustered —
by register, by position within surah or verse, by lexical class — or scattered?**

This target is chosen because it does not have the failure mode that killed nine
standing laws on 2026-08-07 (H-NEW-2680, H-NEW-2720). Those laws measured
properties any contiguous Arabic text has, and a matched partition of al-Bukhārī
reproduced them. **The ʿUthmānic rasm is an orthographic tradition specific to the
transmission of this text**; there is no rasm for al-Bukhārī or al-Jāḥiẓ, so
"a partition of ḥadīth also does this" is not an available refutation.

**That changes which control is the right one; it does not exempt this test from
controls.** §8 states in full what a genre control would and would not mean here.

## 2. The confound that governs the entire design

Tanzil's *simple* text is itself a normalisation with its own conventions. A naive
skeleton diff is dominated by systematic transformations that are orthographic
bookkeeping, not divergence. **The typology is therefore locked before any count is
reported**, and the systematic layers are quarantined by *symmetric* normalisations
applied to **both** texts, each of which must pass an exceptionlessness test (§4.3).

A second confound, equally important: many divergent spellings attach to
high-frequency religious vocabulary. **A positional or register null that conditions
only on counts would rediscover that *ṣalāh* is common.** Every registered inference
in §6 conditions on lexical identity — exactly, by stratification — or on lexical
frequency and orthographic length, and says which.

## 3. Frozen inputs (SHA-256, verified at runtime, `SystemExit` on mismatch)

| file | sha256 |
|:--|:--|
| `data/alt-text/quran-uthmani-txt.txt` | `e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8` |
| `data/alt-text/quran-simple-txt.txt` | `777c190d8e4ab081a80b4f10f5e309f1ab2a87e4d3ea97e5a7eabc59f4fe0b72` |
| `data/hafs-verse-counts.tsv` | `e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba` |
| `findings/phase-b-hypotheses/csv/h-new-2500.json` | `a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25` |
| `findings/phase-b-hypotheses/csv/h-new-2530.json` | `5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c` |
| `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` | `a067ebb34ccabe92376f3008b9cdfb32eea9d6167062172318635e53f500fb05` |

`quran-uthmani-txt.txt` is read by **zero** scripts in this repository before this run.

**Register labels.** Taken from `h-new-2500.json → genre_proxy.surah_genre`, which is
the source `h-new-2530.json` records as reused **verbatim**
(`genre_proxy_source: "h-new-2500.json genre_proxy.surah_genre (reused verbatim)"`).
The runtime asserts the four marginals equal `h-new-2530.json → n_per_genre`
= narrative 31, legal_medinan 20, eschatological_mufassal 40, liturgical_didactic 23.
No label is invented, renamed, or re-derived.

## 4. Instrument (MW-1) — locked

### 4.1 Alignment

Both texts are 6,236 verses. Word counts differ (82,260 vs 82,627) because the
ʿUthmānī text joins some words the simple text separates (vocative يٰ, هٰأنتم,
أن لو). **Deterministic greedy merge rule**: where the simple side has a surplus of
*d* tokens in a verse, at each position choose *m* ∈ {1 … min(d,4)+1} minimising
Levenshtein distance between the ʿUthmānī token's skeleton and the concatenated
skeleton of the next *m* simple tokens, tie-breaking to the smallest *m*.
Merged pairs are tagged class **FAṢL** and are excluded from the edit-operation
classifier (their divergence is a word-division fact, not a letter fact).
**Success criterion, locked: the rule must align 6,236/6,236 verses.** Any failure
is reported, not patched after the fact.

### 4.2 Skeleton

Strip: all ḥarakāt (U+064B–U+0652), superscript alef (U+0670), maddah/hamza
combining marks (U+0653–U+065F), tatweel (U+0640), and every Quranic annotation
sign (U+06D6–U+06ED — this includes the small wāw ۥ, small yāʾ ۦ, small high
rounded zero ۟, and the sajdah sign). What remains is the base-letter string.

### 4.3 The four convention normalisations (symmetric, applied to BOTH texts)

Each quarantines a transformation that is a *dotting or diacritic convention*, not a
rasm fact. Each is declared SYSTEMATIC only if it passes an **exceptionlessness
test** with **zero** counterexamples; a layer that fails is reported as failing and
its tokens are returned to the divergence set.

| layer | normalisation | exceptionlessness test (locked) |
|:--|:--|:--|
| **N1** | ٱ (U+0671) → ا | count of ٱ in the simple text must be 0 |
| **N2** | ى → ي | count of **word-final ي** in the ʿUthmānī skeleton must be 0 |
| **N3** | آ → ا | count of آ in the ʿUthmānī skeleton must be 0 |
| **N4** | أ,إ → ا ; ؤ → و ; ئ → ي ; ء → ∅ | none — declared *conservative by construction*: applied symmetrically it can only remove divergences, never create them, so it shrinks the reported divergence set |

N4 is additionally the historically correct move: hamza was not written in the
ʿUthmānic rasm at all, so a rasm-level comparison must be hamza-blind.

### 4.4 The divergence set

A token pair is **divergent** iff its two skeletons differ after N1–N4.
Everything removed by N1–N4 is **SYSTEMATIC**; everything remaining is the
**residual rasm divergence set**.

## 5. The typology — locked before any inference

Residual divergences are classified by the edit operation between the two
skeletons, mapped onto the six-fold scheme **al-Suyūṭī states verbatim** in
*al-Itqān fī ʿulūm al-Qurʾān*, al-nawʿ al-sādis wa-l-sabʿūn (*fī marsūm al-khaṭṭ
wa-ādāb kitābatihi*):

> قلت، وسنحصر أمر الرسم في الحذف والزيادة والهمز والبدل والفصل، وما فيه قراءتان
> فكتب على إحداها

(on disk at `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`,
line 23252; the section opens at line 23216).

| class | operation (ʿUthmānī → simple) | classical name |
|:--|:--|:--|
| **HADHF-ALIF** | simple inserts ا | al-ḥadhf |
| **HADHF-YA** | simple inserts ي | al-ḥadhf |
| **HADHF-WAW** | simple inserts و | al-ḥadhf |
| **HADHF-LAM** | simple inserts ل | al-ḥadhf |
| **ZIYADA-ALIF** | simple deletes ا | al-ziyāda |
| **ZIYADA-WAW** | simple deletes و | al-ziyāda |
| **ZIYADA-YA** | simple deletes ي | al-ziyāda |
| **BADAL-WAW-ALIF** | و ↔ ا substitution | al-badal |
| **BADAL-YA-ALIF** | ي ↔ ا substitution | al-badal |
| **BADAL-OTHER** | any other substitution | al-badal |
| **FASL** | word-division disagreement (§4.1) | al-waṣl wa-l-faṣl |
| **HAMZ** | everything removed by N4 | al-hamz |
| **MIXED** | more than one operation class in one token | — |

**al-Suyūṭī's sixth category (*mā fīhi qirāʾatān*) is not an edit operation** and is
not assigned by the classifier; it is addressed descriptively in the audit (§7).

**Declared in advance as a ceiling on the whole study:** al-Suyūṭī's *badal*
chapter also lists a closed set of words written with tāʾ maftūḥa where standard
orthography has tāʾ marbūṭa (رحمت، نعمت، سنت، امرأت، كلمت، لعنت، شجرت، قرت، بقيت،
فطرت …). **Tanzil's simple text does not normalise this class** — the ة count is
identical in both texts (2,344 = 2,344, computed before locking). This class is
therefore **invisible to any diff between these two files**, and the divergence set
measured here is bounded by what Tanzil chose to normalise. This is stated in §9 as
the study's first honest limit and is not to be soft-pedalled in the finding.

## 6. Registered inferences — directions locked here, before observation

Five cells. **Bonferroni α = 0.05 / 5 = 0.01.** 10,000 permutations, seed 20260509;
replication at seed 20260519. Permutation p-values reported as
(1 + #{null ≥ obs}) / (1 + n_perm).

### I1 — Frequency concentration. WELL POWERED. Direction LOCKED: POSITIVE.

**Unit:** simple-text consonantal skeleton *type* (empty skeletons excluded).
A type is **divergent** if every one of its tokens diverges, **non-divergent** if
none does; types whose tokens do both ("alternating") are **excluded from I1** and
analysed in I2–I4.

**Statistic:** stratify types by simple-skeleton **length** (characters, capped at
12). Within each stratum compute
mean(log₁₀ token-frequency | divergent) − mean(log₁₀ token-frequency | non-divergent);
pool across strata weighted by stratum type-count. **Δ_pooled.**

**Null:** permute the divergent/non-divergent labels **within each length stratum**,
preserving each stratum's divergent count and the frequency distribution exactly.

**Direction, locked, with justification:** **Δ_pooled > 0** — divergence rate rises
with frequency. Scribal economy targets frequent items, and al-Suyūṭī's *ḥadhf*
lists are dominated by the highest-frequency vocabulary in the corpus (الله، الرحمن،
سبحان، أولئك، الكتب، العلمين، الصلوة). **Length is stratified out because it is the
mechanical confound running the other way** — longer words contain more alifs and
so are likelier to diverge, while Zipf makes frequent words short; stratification
removes it, and its uncorrected direction is *against* the locked prediction.

**PASS** iff p_perm < 0.01 **and** Δ_pooled > 0. If Δ_pooled < 0 this is a
**pre-commit violation** and is published as NULL with full prominence.

### I2 — Verse-final (fāṣila) position. UNDERPOWERED — declared now. Direction LOCKED.

**Set:** the **alternating** strata, keyed on the **pausal form** of the simple word
(the fully-vowelled simple token with the final ḍamma/kasra/fatḥa or tanwīn-ḍamm/
tanwīn-kasr removed — **tanwīn-fatḥ is NOT removed**, because it *is* written in the
rasm as an alif). Justification for the pausal key: the rasm does not encode iʿrāb
at all, so two tokens differing only in case-ending are the same rasm target.
**Primary analysis set:** strata with exactly two attested rasm variants of
different length.

**Statistic:** within each stratum, the binary is LONG (the longer rasm variant) vs
SHORT. Statistic = number of LONG tokens at verse-final position, summed over
strata. **Null:** permute the LONG/SHORT labels within each stratum (each stratum's
variant counts fixed), so lexical identity is conditioned on **exactly**.

**Direction, locked, with justification:** **LONG enriched at verse-final position.**
al-Suyūṭī's *ziyāda* chapter names الظنونا، الرسولا، السبيلا (Q 33) as carrying an
added alif; the added letter serves the fāṣila. Letter *addition* is therefore
predicted at pause.

**Declared in advance:** the design marginals give 86 strata, 1,237 tokens,
informative (minority-cell) mass **131**, and **40** verse-final tokens in the whole
primary set — so the expected count under the null is on the order of **4 events**.
**This arm cannot detect anything but a very large effect, and a NULL here is a
statement about the corpus's supply of lexically-conditioned variation, not
evidence of absence.**

### I3a — Register, omnibus. UNDERPOWERED — declared now. NO direction (justified).

Same stratified set as I2. Statistic: within-stratum-centred χ²-style dispersion of
the SHORT-variant rate across the four registers of `surah_genre`.
**No direction is locked because no defensible a-priori ordering of four registers
exists**; a directionless omnibus is registered instead of a fabricated direction.

### I3b — Register, one directional contrast. Direction LOCKED.

**SHORT (defective) rate higher in `eschatological_mufassal` than in
`legal_medinan`.** Justification: defective → plene is the attested direction of
Arabic orthographic development, so earlier material should carry more defective
spelling; `h-new-2500`'s own decision procedure defines `legal_medinan` as Medinan
and `eschatological_mufassal` as s ≥ 78 or eschatological-dense, which is the
late/early contrast. **Declared in advance:** `eschatological_mufassal` contributes
only **61** of the 1,237 primary-set tokens. This arm is very weak.

### I4 — Relative position within surah. UNDERPOWERED. TWO-SIDED (justified).

Same stratified set. Statistic: within-stratum mean difference in relative verse
position (ayah / n_ayat) between SHORT and LONG tokens, pooled.
**Two-sided: no defensible directional prior exists, and inventing one to gain a
factor of two would be exactly the pre-commit abuse this protocol exists to
prevent.**

### Verdict labels (the script's logic will be diffed against this list)

- **LEXICALLY-DETERMINED** — if the descriptive result is that ≥ 90 % of divergent
  tokens belong to types with a single, invariant rasm spelling.
- **CONCENTRATED** — I1 passes.
- **CONDITIONED** — any of I2/I3a/I3b/I4 passes at α = 0.01 in the locked direction.
- **NULL** — for each arm that does not pass.
- **PRE-COMMIT VIOLATION** — a locked direction reverses; published as NULL with
  full prominence.

## 7. Classical-claim audit (descriptive; no p-values, no Bonferroni cell)

al-Suyūṭī, *al-Itqān*, nawʿ 76, makes closed, checkable claims. Each is checked
against the ʿUthmānī text and reported VINDICATED / FALSIFIED / PARTIAL. These are
**descriptive verifications, not registered inferences**, and carry no α.

- **C1** *badal* by wāw is exactly: الصلوة، الزكوة، الحيوة، الربوا (unannexed)، الغدوة،
  مشكوة، النجوة، منوة.
- **C2** the yāʾ is omitted from إبرهم **in al-Baqara** (وحذفت الياء من "إبرهم" في البقرة).
- **C3** indefinite كتب is written plene (كتاب) in exactly four places: "لكل أجل كتاب"،
  "كتاب معلوم"، "كتاب ربك"، "كتاب مبين" في النمل.
- **C4** سموات is written plene only in Fuṣṣilat (إلا "سبع سموات" في فصلت).
- **C5** *ziyāda* of alif in الظنونا، الرسولا، السبيلا (Q 33).

**Standing caveat, declared now:** al-Suyūṭī describes the ʿUthmānic rasm as
transmitted by al-Dānī; Tanzil's ʿUthmānī text encodes the **modern King Fahd
Complex (Madinah) print**. Agreement is expected but not guaranteed, and a mismatch
is evidence about the two traditions, not automatically an error in either.

**Anchors NOT on disk and therefore NOT cited:** al-Dānī *al-Muqniʿ fī rasm maṣāḥif
al-amṣār* and Abū Dāwūd *Mukhtaṣar al-tabyīn*. `findings/classical-sources/
dani-23-site-supplement.tsv` is al-Dānī's *al-Bayān fī ʿadd āy*, a **verse-counting**
work, and **must not be cited as an orthography anchor**. al-Dānī is cited here only
**as quoted inside al-Itqān**, which is openable.

## 8. Controls — what a genre control would and would not mean here

**Stated explicitly because the standard matched-partition control does not apply,
and silence would be the dishonest option.**

1. **It cannot be constructed.** The H-NEW-2680/2720 control cuts al-Bukhārī or
   al-Jāḥiẓ into 114 pseudo-surahs and re-runs the statistic. Here the statistic is
   a **diff between two orthographic editions of the same text**. No second
   orthographic edition of al-Bukhārī exists — there is no ḥadīth rasm tradition.
   A pseudo-surah partition has nothing to diff against, so the control has no
   analogue, not merely no data.
2. **What that buys.** "A partition of Bukhārī also does this" is unavailable as a
   refutation. That is a real advantage over the nine laws that fell.
3. **What it does NOT buy — and this is the part that must travel with any positive
   result.** The absence of the *Arabic-genre* control does not make a positive
   result a property of *this text*. The relevant reference class is not another
   Arabic text; it is **another scribal tradition**. Item-specific defective
   spellings concentrated in high-frequency vocabulary are a general property of
   manuscript transmission under scribal economy. **A positive I1 would therefore be
   evidence about scribal practice, not about the composition of the text**, and it
   must be reported that way.
4. **The control that IS run.** Every inference here uses a within-corpus
   permutation null, and I2–I4 condition on lexical identity exactly by
   stratification. That is the strongest available control, and it is weaker than a
   cross-tradition control would be.
5. **The missing instrument, named.** A second Arabic text with both an attested
   divergent scribal orthography and a modern normalisation, at comparable scale.
   Not on disk; plausibly not existing.

## 9. Honest limits — declared before the run

1. **The Tanzil ceiling.** The divergence set is bounded by what Tanzil's simple
   text normalises. The tāʾ-maftūḥa *badal* class is entirely invisible (§5). Any
   count reported is a count of *Tanzil-visible* divergence, never of "the rasm".
2. **I2, I3a, I3b, I4 are underpowered by construction**, with the marginals given
   in §6. A NULL from them is close to uninformative about small effects.
3. **N4 removes real hamza divergence** along with convention. It is symmetric and
   shrinks the divergence set, so it is conservative, but the HAMZ class is a
   quarantine bucket, not an analysis.
4. **The register labels are a surah-level proxy** built by `h-new-2500`'s
   four-rule decision procedure, not independent annotation, and every token in a
   surah inherits one label.
5. **The alignment merge rule is a heuristic**, chosen for determinism. It is
   verified only by 6,236/6,236 coverage, not by hand-checking every merge.
6. **A single verse-division and a single reading tradition.** Ḥafṣ ʿan ʿĀṣim,
   Kūfan verse count. The qirāʾāt dimension of al-Suyūṭī's sixth category is
   touched descriptively and not tested.

## 10. Garden of forking paths — entries made BEFORE the run

Recorded so the record is not reconstructed afterwards.

1. **What was computed before this file was locked, and is therefore not
   protected by it:** the character inventories of both texts; the alignment
   failure counts under three successive merge rules; the layer accounting
   (22,315 → 6,919 divergent tokens); the top residual type-pairs and edit-operation
   signatures — **these are what the typology in §5 was curated from, and that
   curation is openly post-hoc, as the brief requires it to be**; the number of
   alternating strata under two stratification keys; the design marginals quoted in
   §6; the identity of the ة counts. **No association between divergence and
   register, verse position, surah position, or frequency has been computed.**
2. **Stratification key chosen on power grounds, before any outcome.** Strict
   fully-vowelled key gives 74 primary strata / informative mass 109; the pausal key
   gives 86 / 131. The pausal key was chosen, and the linguistic justification
   (the rasm does not encode iʿrāb) is given in §6-I2 — it is not a post-hoc
   rationalisation of a power choice, but the power comparison did come first and is
   recorded here.
3. **Bonferroni k = 5 counts I3a and I3b separately.** Counting them as one cell
   would loosen α; counting them separately tightens it. Tightening is
   self-verifying under this project's rule.
4. **I1 was added to the design after the descriptive work showed that ~95 % of
   divergent tokens are lexically determined**, which left I2–I4 underpowered. I1 is
   a different question (which *types* diverge) from I2–I4 (which *token* gets which
   variant), it is registered here with its direction locked before computation, and
   the fact that it exists because the first design was thin is recorded rather than
   hidden.
5. **Run directories are never deleted.**

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any association statistic existed.
Bismillāhi al-Raḥmāni al-Raḥīm.*
