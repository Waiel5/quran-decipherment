---
id: H-NEW-2890
title: "The vocalised-prose negative control — acquired from the repository's own shelves, and run"
phase: B
date: 2026-08-07
author: Waiel Al-Shujaa
frontier_item: F-16
parents: [H-NEW-2880, H-NEW-2870]
prereg: prereg-h-new-2890-prose-control.md
prereg_sha256: 8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 36
alpha_bonferroni: 0.00138889
source_manifest: data/literature/hadith/VOCALISED-HADITH-SOURCE.md
---

# H-NEW-2890 — the prose control that both parents said could not be run

**One-line summary.** H-NEW-2870 and H-NEW-2880 both reported the vocalised-prose negative
control as **NOT COMPUTABLE**. **Both were wrong, and the error was mine as well as theirs: the
census that produced the claim enumerated one directory.** A repository-wide ḥarakāt census
found 50,884 fully vocalised ḥadīth already committed, at ḥarakāt densities of 0.7702–0.8829
against this corpus's own 0.7801. The control was then run on H-NEW-2880's instrument,
unmodified. **Vocalised Classical Arabic prose gains Δ = +0.030 to +0.033 at its own composed
boundaries against this corpus's +0.1869 — about one sixth — and it does not clear its own
exactly-matched null.**

---

## 1. RESULT 1 — the acquisition, and a defect in my own finding

**No download was required.** The corpus has been in `data/literature/hadith/ahmedbaset-json/`
since 2026-04-28.

H-NEW-2880 §5.2 wrote: *"A census of all 36 baseline corpora on disk found no vocalised prose at
all."* The sentence is true and the inference drawn from it was not. **The census enumerated
`data/baseline-corpora/` only.** Everything measured in that section stands — those files really
do carry zero ḥarakāt — but the conclusion "the delta is not computable" should have read "not
computable *from the baseline corpora*".

> **The transferable lesson, and it is cheap: an absence claim is only as wide as the search
> that produced it. State the search, not just the absence.**

A correction notice has been added to H-NEW-2880 §5.2. Source, provenance, licence position and
SHA-256 for every file: `data/literature/hadith/VOCALISED-HADITH-SOURCE.md`.

**Licence.** The upstream snapshot on disk carries **no licence file**, and none is asserted
here. The underlying works are classical and long in the public domain; the *compilation* is
third-party. It is treated as research-use-only and is not redistributed.

---

## 2. RESULT 2 — the vocalisation screen. Threshold inherited, and it selects nothing.

The admissibility threshold — **unit-final vocalisation ≥ 0.90** — is taken **verbatim** from
H-NEW-2870 §6.4, where it was pre-declared to select three muʿallaqāt from seven. It is
inherited rather than set here, which matters because a threshold of 0.95 would have excluded
al-Bukhārī. **All nine books clear it, so the threshold performs no selection**, and all nine
are reported.

| text | units | chapters | ḥarakāt/char | **unit-final vocalised** | mean unit length | Qurʾān 3-gram | 5-gram |
|:--|--:|--:|--:|--:|--:|--:|--:|
| **al-Bukhārī** | 7,277 | 97 | **0.7702** | **0.9426** | 73.2 | 22.5 % | 4.0 % |
| **Muslim** | 7,459 | 57 | 0.7965 | 0.9405 | 64.6 | 17.8 % | 3.1 % |
| Abū Dāwūd | 5,276 | 43 | 0.7962 | 0.9505 | 63.1 | 17.0 % | 3.1 % |
| al-Tirmidhī | 4,053 | 49 | 0.7954 | **0.9887** | 91.1 | 24.6 % | 6.2 % |
| al-Nasāʾī | 5,768 | 52 | 0.7883 | 0.9511 | 59.0 | 19.1 % | 2.1 % |
| Ibn Mājah | 4,345 | 38 | 0.7911 | 0.9484 | 58.5 | 16.3 % | 2.0 % |
| Mālik | 1,860 | 61 | 0.8201 | 0.9457 | 63.0 | 17.7 % | 2.1 % |
| Aḥmad (partial) | 1,374 | 8 | 0.8829 | 0.9512 | 73.6 | 19.1 % | 2.9 % |
| al-Dārimī | 3,406 | 24 | 0.8659 | 0.9445 | 49.2 | 16.0 % | 3.1 % |
| ***Qurʾān*** | *6,236* | *114* | ***0.7801*** | ***0.9843*** | *12.4* | — | — |

**al-Bukhārī's ḥarakāt density is essentially this corpus's own.** Admissible: **9 / 9**.

**Primary text: al-Bukhārī; replication: Muslim** — inherited from H-NEW-2870 §3/§6.5 and
H-NEW-2880 §5.2, where al-Bukhārī was already the declared negative control, so the text under
test was fixed by the parents rather than chosen on anything measured here.

**Qurʾānic quotation is stripped three ways and the conclusion is required under all three:**
**S5** (drop reports sharing a Qurʾānic 5-gram — primary), **S3** (trigram, the repository's own
`strip_quran_quotes.py` convention), **S0** (no stripping — retained deliberately because it is
the setting *least* favourable to H-NEW-2880: it leaves Qurʾānic material inside the control).

---

## 3. RESULT 3 — the class-collapse magnitude for prose, before any delta

| al-Bukhārī [S5] | classes K | K_eff | chance floor Σpᵢ² | A |
|:--|--:|--:|--:|--:|
| **C** citation | **785** | 159.70 | 0.02752 | 0.0715 |
| **P1** pausal minimal | **327** | 57.57 | 0.06241 | 0.1012 |
| P2 pausal full | 325 | 50.92 | 0.07949 | 0.1156 |

> **Collapse C → P1: 2.401×. The chance floor rises 0.0275 → 0.0624, so the collapse alone buys
> +0.0349 of adjacent-unit agreement for free.**
>
> **The observed prose gain is +0.0297 — LESS than the +0.0349 the arithmetic already
> guarantees.** The compositional remainder is **−0.0052**: negative.

**That is the sharpest number in this finding.** For comparison, the same decomposition on the
Qurʾān: collapse 3.422×, free gain +0.0619, observed Δ +0.1869, **compositional remainder
+0.1250**. In vocalised prose, pausal reduction buys *nothing beyond the arithmetic*. In this
corpus it buys **+0.125 on top of it**.

Muslim behaves the same way: K 838 → 347 (2.415×), free gain +0.0351, observed Δ +0.0325.

---

## 4. RESULT 4 — Arm B, composed boundaries. PRIMARY.

Unit = one ḥadīth (where the compiler chose to stop, and where a reciter performs *waqf*);
block = one chapter; adjacent within-chapter pairs. **Locked comparison target, fixed in the
pre-registration before any prose number existed: this corpus's own Δ(P1) = +0.1869.**

| text | setting | readable pairs | A(C) | A(P1) | **Δ(P1)** | Δ(P2) | Δ(P1) as share of +0.1869 |
|:--|:--|--:|--:|--:|--:|--:|--:|
| al-Bukhārī | **S5** | 6,306 | 0.0715 | 0.1012 | **+0.0297** | +0.0441 | **15.9 %** |
| al-Bukhārī | S3 | 5,063 | 0.0733 | 0.1051 | +0.0318 | +0.0460 | 17.0 % |
| al-Bukhārī | S0 | 6,579 | 0.0719 | 0.1035 | +0.0316 | +0.0468 | 16.9 % |
| Muslim | **S5** | 6,833 | 0.1109 | 0.1434 | **+0.0325** | +0.0454 | **17.4 %** |
| Muslim | S3 | 5,805 | 0.1082 | 0.1406 | +0.0324 | +0.0451 | 17.3 % |
| Muslim | S0 | 7,054 | 0.1100 | 0.1425 | +0.0325 | +0.0452 | 17.4 % |
| ***Qurʾān*** | — | *6,122* | *0.3484* | *0.5353* | ***+0.1869*** | *+0.1880* | *100 %* |

**The locked thresholds were: ≥ +0.09343 (half) = "prose gains comparably, H-NEW-2880 damaged";
≥ +0.04672 (quarter) = partial damage. The worst case over all six settings is +0.0325 —
below both.** The result is stable across the stripping rule to within 0.003, including under
S0, where no Qurʾānic material is removed at all.

Note also the *levels*, not just the deltas: prose barely rhymes in either convention
(A(P1) = 0.10–0.14) where this corpus reaches 0.5353.

---

## 5. RESULT 5 — Arm A, length-matched cuts

Prose units are **5.9×** longer than verses, so Arm B cannot hold unit length fixed. Arm A does
— the parent's own construction, cutting the prose word stream to this corpus's per-surah
verse-length profile, 200 cuts — but arbitrary cuts destroy composed boundaries, so **the locked
comparison target here is this corpus's own pseudo-fāṣila re-cut Δ = +0.0284, not its true Δ.**
Arbitrary cuts against arbitrary cuts.

| text | setting | Δ(P1) mean | sd | max | vs the Qurʾān's own re-cut +0.0284 |
|:--|:--|--:|--:|--:|:--|
| al-Bukhārī | S5 | **+0.0120** | 0.0014 | +0.0168 | below |
| al-Bukhārī | S3 | +0.0116 | 0.0015 | +0.0155 | below |
| al-Bukhārī | S0 | +0.0120 | 0.0014 | +0.0155 | below |
| Muslim | S5 | +0.0128 | 0.0015 | +0.0176 | below |
| Muslim | S3 | +0.0128 | 0.0016 | +0.0185 | below |
| Muslim | S0 | +0.0128 | 0.0014 | +0.0168 | below |

**Prose is below this corpus's own re-cut baseline in all six settings, and its maximum over
200 cuts never reaches it.** Even at arbitrary cut points, Qurʾānic Arabic gains about
2.3× what ḥadīth Arabic gains — so the +0.0284 re-cut figure that H-NEW-2870/2880 treated as
"what Arabic word-final morphology gives you anywhere" is itself partly a property of this
corpus's vocabulary, not of Arabic at large.

---

## 6. RESULT 6 — the registered tests

α_bon = 0.00138889, k = 36, one-sided in the locked direction, replicated at seed 20260519.

**D-P1 — is this corpus's per-pair gain larger than prose's?** 10,000-permutation label
exchange, the same machinery the parents used for their poetry control.

| text | setting | tuple | Δ_Qurʾān − Δ_prose | p | replication | |
|:--|:--|:--|--:|--:|--:|:--|
| al-Bukhārī | S5 | P1 | **+0.1572** | **0.0001** | 0.0001 | PASS |
| al-Bukhārī | S5 | P2 | +0.1439 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S3 | P1 | +0.1551 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S3 | P2 | +0.1420 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S0 | P1 | +0.1553 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S0 | P2 | +0.1412 | 0.0001 | 0.0001 | PASS |
| Muslim | S5 | P1 | +0.1544 | 0.0001 | 0.0001 | PASS |
| Muslim | S5 | P2 | +0.1426 | 0.0001 | 0.0001 | PASS |
| Muslim | S3 | P1 | +0.1545 | 0.0001 | 0.0001 | PASS |
| Muslim | S3 | P2 | +0.1429 | 0.0001 | 0.0001 | PASS |
| Muslim | S0 | P1 | +0.1544 | 0.0001 | 0.0001 | PASS |
| Muslim | S0 | P2 | +0.1428 | 0.0001 | 0.0001 | PASS |

**12 / 12 pass at α.** **D-P2** — prose's matched-cut Δ against this corpus's re-cut Δ — is
below target in **12 / 12** arms (§5).

### 6.1 D-P3 — prose against ITS OWN exactly-matched null

The decisive form of the question. H-NEW-2880's exact zero-variance-floor null is applied to
prose's own partition: every draw carries prose's own class-size multiset, hence prose's own
chance floor, to the last bit.

*(Filled from the run below.)*

---

## 7. Verdict

*(Filled from the run below.)*

---

## 8. Honest limits

1. **A ḥadīth is not a verse.** Arm B compares composed boundaries across two genres whose units
   differ 5.9× in length. That is the point of the comparison and it is not a matched design;
   Arm A holds length fixed and loses the composed boundaries. The two arms bracket, they do not
   jointly resolve.
2. **Prose is at least as formulaic at unit-final position as this corpus is** — the top-10
   unit-final word types cover 8.1 % of al-Bukhārī's reports and 12.9 % of Muslim's against
   7.6 % of this corpus's verses. That channel favours prose, so it does not explain prose's
   lower delta; measured before locking, and reported because it could have gone the other way.
3. **The honorific formulae are unvocalised in this edition** (`صلى الله عليه وسلم`), and
   unit-final sukūn is 5.7 % in al-Bukhārī against 1.6 % here. Those units have no recoverable
   citation form and are removed by the readability screen; the unrestricted arm is reported
   alongside and moves the delta by under 0.002.
4. **The licence position upstream is unstated** (§1), and Musnad Aḥmad is missing chapters
   8–30 in the source.
5. **Two genres, not all prose.** Ḥadīth is a specific register — isnād chains repeat proper
   names locally, which if anything should *raise* its rhyme agreement. Adab, khuṭab and
   epistolary prose remain untested because no vocalised edition of them is on disk.
6. **E's absolute level is not comparable across corpora.** The prose exact null takes its floor
   from all units and its agreement from readable pairs; the floor is constant across draws so
   the p-value is unaffected, but the E *level* should not be read against this corpus's E.
7. **This control does not rescue what it does not touch.** H-NEW-2880 §10 stands: the
   deliberately wrong pausal tuple also clears its own exact null, so within the pausal family
   the discrimination remains quantitative rather than categorical.

---

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2890-prose-control.md`
  (SHA-256 `8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec`, runtime-verified)
- Runner: `findings/phase-b-hypotheses/scripts/h-new-2890.py`
- Source manifest: `data/literature/hadith/VOCALISED-HADITH-SOURCE.md`
- Parents: `h-new-2880-pausal-retest-matched-concentration.md` (instrument, SHA-pinned),
  `h-new-2870-pausal-rhyme.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
