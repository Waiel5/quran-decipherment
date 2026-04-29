---
id: H-NEW-84
title: Sūrat al-Ikhlāṣ as 1/3 of the Quran — quantitative tests of the classical equivalence claim
phase: B
status: PRE-REGISTERED 2026-04-15 (locked BEFORE running script)
agent: h-new-84-specialist
spec_locked_at: 2026-04-15
bonferroni_family: 2026-04-15-Wave-H-NEW-84-Ikhlas-third
bonferroni_k: 7
alpha_bon: 0.00714286  # 0.05 / 7
rules_tuple: (no-tashkeel; word-segment substring rule; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi; Leeds Quranic Arabic Corpus 0.4 for roots)
primary_data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
morphology_data: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
seed: 20260417
---

# [[h-new-84-ikhlas-third|H-NEW-84]] — Sūrat al-Ikhlāṣ "1/3 of the Quran" — quantitative test

## Question

Multiple ḥadīths attribute extraordinary value to **Sūrat al-Ikhlāṣ** (Q 112, 4 verses, 15 word-tokens, 47 Arabic letter-graphemes):

- Bukhārī #5013 (and parallels in Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Aḥmad): **"Whoever recites it [al-Ikhlāṣ] has recited 1/3 of the Quran"** (qaraʾa thuluth al-Qurʾān).
- Classical exegesis (al-Ghazālī, al-Rāzī, al-Qurṭubī, al-Suyūṭī) explains this not as length-equivalence but as **content equivalence**: the Quran reduces to three categories — (a) doctrines about God (tawḥīd / theology), (b) narratives, (c) commandments — and Q 112 fully concentrates category (a).

This claim has never been **quantitatively tested**. [[h-new-84-ikhlas-third|H-NEW-84]] pre-registers and executes 7 independent operationalizations of "1/3-equivalence", Bonferroni-corrected.

## Garden-of-forking-paths disclosure (pre-existing knowledge)

Empirically known BEFORE locking the spec:

- Length ratio: Q 112 has **47 letter-graphemes / 330,709 corpus letters ≈ 0.000142** ≈ **1/7,038** of the Quran by length, vastly less than 1/3. The classical claim is therefore not length-based.
- Token inventory: Q 112 contains **15 word-tokens / 12 unique types**. Exactly **2 are hapax in the Quran** (يلد, يولد — both forms of root w-l-d; root w-l-d appears in many forms elsewhere) and **1 is a true hapax** (الصمد — "the Eternal/Self-Sufficient", the only occurrence in the Quran).
- Roots: per Leeds morphology, Q 112's roots are: q-w-l, ʾ-l-h, ʾ-ḥ-d, ṣ-m-d, w-l-d, k-w-n, k-f-w. That is **7 distinct roots** out of ~1,685 distinct Quranic roots (~0.4%).
- Theological content: Q 112 contains 4 explicit references to Allāh (الله in v.1, الله in v.2, the divine attributes الصمد and أحد — repeated as أحد in v.4). It is the most theologically dense single surah in the Quran.
- Compression intuition: a 47-letter text cannot literally reduce to 1/3 of the corpus by Kolmogorov-style compression; but the classical claim is about **conceptual** rather than informational equivalence.
- The 1/3 claim has TWO classical readings:
  1. **Strong reading**: Q 112 IS literally 1/3 of the Quran's content/value (Bukhārī's plain text).
  2. **Weak/symbolic reading**: Q 112 covers 1/3 of the Quran's THEMATIC categories (al-Ghazālī's "Iḥyāʾ" interpretation: doctrines / narratives / commandments).
  Both are tested below.

This disclosure means [[h-new-84-ikhlas-third|H-NEW-84]] enters the test with **prior expectation that the literal 1/3 claim FAILS** but the **weak categorical/thematic claim has a chance to PASS** — though even there, "1/3" must coincide quantitatively, not just qualitatively.

## Locked methodology

### Data
- Corpus: `quran-text/quran-no-tashkeel.json` (114 surahs, 6236 verses).
- Morphology: Leeds Quranic Arabic Corpus 0.4 for roots/lemmas/POS.
- Q 112 = 4 verses, 15 word-tokens, 12 distinct types, 47 Arabic letter-graphemes.

### Bonferroni
k = 7 operationalizations, α_bon = 0.05 / 7 ≈ **0.00714286**.

### "1/3 equivalence" operationalizations (7 axes)

For each axis, we compute (a) the observed Q 112 value, (b) what the **1/3 equivalence** would predict (a target value), (c) whether the observed value is statistically distinguishable from the target, and (d) the actual ratio.

The hypothesis is tested as: **"the Q 112 value is within ±10% of (1/3 × corpus_value)"** — i.e., a null-hypothesis-style proximity test. We pre-commit a tolerance band of [0.30, 0.37] (±10% around 1/3) for the ratio Q112/corpus, since "1/3" is a discrete claim and any reasonable test must allow some tolerance.

**Per-axis PASS criterion**: ratio R = Q112_value / corpus_value must be in **[0.30, 0.37]** for the axis to PASS.

### Overall PASS criterion (pre-committed)

- ≥ 3 of 7 axes PASS → **PASS-WEAK** (some sense in which Q 112 = 1/3 of Quran).
- ≥ 5 of 7 axes PASS → **PASS-STRONG** (substantive 1/3-equivalence).
- 1-2 axes PASS → **REFUTED-WEAK** (incidental or single-aspect hit).
- 0 axes PASS → **REFUTED-STRONG** (no quantitative 1/3 sense).

### The 7 locked axes

#### Axis 1 — LENGTH (graphemic letters)
**Predicted**: Q 112 letter-count = 1/3 × corpus letter-count = 110,236 letters.
**Observed**: 47 letters.
**Ratio**: 47 / 330,709 = 0.000142.
This axis is included **knowing it will fail catastrophically** — it tests the null literal reading. PASS would require Ratio ∈ [0.30, 0.37].

#### Axis 2 — TOKEN COUNT
**Predicted**: Q 112 word-token-count = 1/3 × corpus word-token-count.
**Observed**: 15 tokens out of 82,375 (note: this is not the methodology.md anchor of 77,797 because of the simpler split; we use the simpler whitespace-split for internal consistency within the script and report both).
**Ratio**: 15 / 82,375 = 0.000182.
Will fail; included for completeness.

#### Axis 3 — INFORMATION CONTENT (Shannon entropy fraction)
**Test**: under a Shannon character-frequency model fit to the entire Quran, compute the **bits-of-information** in Q 112 (sum of −log₂ p(c) over Q 112's characters using corpus marginal). Compute the same for the entire Quran. The ratio is then **bits(Q 112) / bits(entire Quran)** = roughly proportional to length (for an iid character model), so this axis approximates Axis 1 by design. PASS requires ratio ∈ [0.30, 0.37]. Will fail; included as the **Shannon information-content** operationalization mentioned in the [[h-new-84-ikhlas-third|H-NEW-84]] brief.

#### Axis 4 — UNIQUE LEMMA / ROOT COVERAGE
**Test**: number of distinct **roots** appearing in Q 112 / number of distinct roots in the entire Quran. Per Leeds, Q 112's roots are: q-w-l, ʾ-l-h, ʾ-ḥ-d, ṣ-m-d, w-l-d, k-w-n, k-f-w (7 roots). Total distinct Quran roots ≈ 1,685.
**Predicted**: Q 112 root-count / total roots ∈ [0.30, 0.37] → Q 112 should contain 506-624 distinct roots.
**Observed**: 7 / ~1,685 ≈ 0.0042.
Will fail; tests the literal "covers 1/3 of vocabulary" reading.

#### Axis 5 — THEOLOGICAL CATEGORY COVERAGE (al-Ghazālī's 3-category schema)
**Test**: This is the **MOST CHARITABLE** axis to the classical claim. Per al-Ghazālī's Iḥyāʾ interpretation of the ḥadīth: the Quran reduces to 3 thematic categories:
1. **Tawḥīd / theology** (about God, His names, attributes, oneness) — Q 112's category
2. **Narratives** (qaṣaṣ al-anbiyāʾ, historical accounts)
3. **Commandments** (aḥkām, legal/ritual prescriptions)

We define each category by a locked keyword list (substrings):
- **Theology**: الله, ربك, ربكم, ربنا, إله, إلهك, إلهكم, إلهنا, الرحمن, الرحيم, الملك, القدوس, السلام, المؤمن, المهيمن, العزيز, الجبار, المتكبر, الخالق, البارئ, المصور, الغفار, القهار, الوهاب, أحد, الصمد, واحد, ربك العالمين
- **Narratives**: قال (when introducing speech of named figures), إذ قال, موسى, عيسى, إبراهيم, نوح, آدم, يوسف, يعقوب, سليمان, داود, يونس, زكريا, يحيى, لوط, شعيب, هود, صالح, إدريس, ذو القرنين, القرن, القرى, قوم, مدين, ثمود, عاد, فرعون, هامان, قارون, السبت, اليتامى, الكوثر, البيت, مكة, طوى
- **Commandments**: حرم, حلال, أوفوا, لا تقربوا, لا تأكلوا, الصلاة, الزكاة, الصيام, الصوم, الحج, اعتدلوا, واتقوا, نكاح, طلاق, ميراث, دين, الربا, الأنصار, الجهاد, الكفر, الفطرة, اليمين, الكفارة, الهدي, القسط, العدل

For each verse in the corpus, compute its dominant category by which category has the most keyword hits (ties → all-tied count). Compute **fraction of corpus verses dominated by category 1 (theology)**. The hadith equates Q 112 to 1/3 of the Quran's content — and per the classical interpretation, this **theological fraction** SHOULD be **1/3** of the corpus's verses (since theology is one of three equivalent categories).

**PASS criterion** (Axis 5 specific): the **fraction of corpus verses dominantly theological** ∈ [0.30, 0.37].

This axis tests the **al-Ghazālī interpretation directly**: if it PASSES, it would be the strongest evidence that the ḥadīth has a quantitative basis (independent of Q 112's brevity).

#### Axis 6 — THEOLOGICAL CONCEPT CONCENTRATION (relative)
**Test**: Q 112 is the **most theologically concentrated** surah by definition; here we ask whether Q 112's per-token theological-keyword density is ~3× the corpus average. If Q 112 concentrates 1/3 of theology in 1/N letters, and theology is 1/3 of corpus, then Q 112's theology-concentration relative to corpus is ~(corpus_size/Q112_size) × 1/3 — vastly higher than 3×.

Specifically: compute **theology_keywords_in_Q112 / Q112_tokens** and **theology_keywords_in_corpus / corpus_tokens**. Compute their ratio R_concentration = (Q112_density / corpus_density). PASS criterion: ratio R_concentration is within [3.0/1.1, 3.0×1.1] = [2.73, 3.30]. (i.e., Q 112 is exactly 3× more theology-dense than corpus average — the "1/3" interpreted as concentration factor of 3.)

#### Axis 7 — DIVINE-NAME / ATTRIBUTE COVERAGE
**Test**: of the **99 names of Allāh** (al-asmāʾ al-ḥusnā), how many appear (as substrings) in Q 112? **Q 112 contains** by direct inspection: الله (Allāh), الصمد (al-Ṣamad), أحد (al-Aḥad — implicit form of "the One"). Also the negation in v.4 implies absence-of-equivalence ≈ "no kufūʾ" (peerlessness). Plus arguably the implications of v.3 (no progenitor / no progeny) imply **al-Awwal** and **al-Ākhir**.
**Conservative count**: 3 names (Allāh, al-Ṣamad, al-Aḥad). 99 names → ratio R = 3/99 = 0.0303. PASS criterion: ratio ∈ [0.30, 0.37] → would require 30-37 names. Will fail.

We use a locked list of **99 names** (the standard list compiled from Tirmidhī #3507, plus al-Bayhaqī's variant) and detect each by substring search.

## MW-5 known-distinctive verse

For Axis 5 (theological coverage), a sanity check is that **Q 1 (al-Fātiḥa)**, **Q 2:255 (āyat al-kursī)**, and **Q 59:22-24 (khawātim al-ḥashr)** should all classify as **theology-dominant**. For Axis 7, Q 59:22-24 should contain ≥ 15 of the 99 names.

## Pre-committed honesty controls

- Seed 20260417 (one day after [[h-new-65-fatiha-as-dna|H-NEW-65]]'s 20260416, to maintain seed cadence).
- All 7 axes' raw values + ratios + targets + pass/fail published in `csv/h-new-84.json`.
- The PASS criterion (≥ 3 of 7 axes in [0.30, 0.37]) is locked BEFORE running.
- Tolerance band [0.30, 0.37] is locked BEFORE running.
- The 99-names list is locked BEFORE running.
- Theme keyword lists are locked BEFORE running.
- Axes 1-4 and 7 will almost certainly FAIL — this is acknowledged. The interesting question is whether **Axes 5 and 6** PASS, since they directly test al-Ghazālī's 3-category interpretation.
- The classical claim is given the **maximally charitable** test: the interpretation that has the best chance of holding (Axis 5: theology = 1/3 of corpus content) is included.

## Honest framing

The 1/3 ḥadīth is unlikely to hold under any **literal** quantitative test (Axes 1-4, 7). The test is designed to characterize:
1. **HOW SMALL** the literal length-ratio is (1/7,038, not 1/3) — quantifying the gap.
2. **WHETHER** the al-Ghazālī interpretation (1/3 of corpus = theology) is itself empirically justified (Axis 5).
3. **WHAT INTERPRETATION** of "1/3" if any survives statistical scrutiny.

A NULL result across all 7 axes would suggest the ḥadīth is a **theological / spiritual valuation statement** rather than a statistical claim — consistent with how most contemporary scholars read it. A PASS on Axis 5 specifically would **rehabilitate** the classical 3-category schema as an empirically grounded thematic taxonomy.

## Outputs

1. `/Users/grey/Downloads/quran/scripts/h_new_84_ikhlas_third.py` — the script
2. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-84.json` — raw per-axis results
3. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-84-ikhlas-third.md` — findings
4. `/Users/grey/Downloads/quran/journal/h-new-84-run-1.md` — run journal

## Cross-references

- **Bukhārī #5013, #5014, #5015**; Muslim 811-812; Tirmidhī 2901; Abū Dāwūd 1461; Nasāʾī 995; Aḥmad 9580.
- **al-Ghazālī**, *Iḥyāʾ ʿulūm al-dīn* — 3-category schema (theology / narratives / commandments).
- **al-Suyūṭī**, *al-Itqān*, ch. on *faḍāʾil al-suwar*.
- **Ibn Taymiyya**, *Tafsīr Sūrat al-Ikhlāṣ* — theological tafsīr.
- [[h-new-65-fatiha-as-dna|H-NEW-65]] (Fātiḥa-as-DNA) — methodologically parallel "single surah encodes corpus" test.
- H-NEW-59 (divine-names-distribution) — relevant to Axis 7.
- M-9 (convergence-does-not-multiply) — [[h-new-84-ikhlas-third|H-NEW-84]] is the FIRST quantitative test of this specific claim, so no convergence dampening applies.
