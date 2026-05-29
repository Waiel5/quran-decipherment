---
finding_id: H-NEW-2300
title: Dual-name fāṣila seal-grammar — verse CONTENT predicts the sealing name-PAIR (content↔seal matching)
phase: B
date: 2026-05-29
verdict: EXTENDS H-NEW-2070 (PASS-DIRECTED-CONTENT)
extends: H-NEW-2070
seed: 20260509
n_perm: 10000
pre_reg_sha256: cc1962fba93c68c14026b468d0bef6bc4b66f6b701f85f5eb64168fd7c204cb5
---

# H-NEW-2300 — Dual-name fāṣila seal-grammar: content↔seal matching

**Verdict: EXTENDS H-NEW-2070 (PASS-DIRECTED-CONTENT).** The choice of the
verse-final divine-name PAIR is **semantically conditioned by the verse body**,
not merely a phonological/positional cadence. Both pre-registered statistics pass
the Bonferroni-2 family (α_cell=0.025) against a label-permutation null, and the
sharpest directional sub-claim (forgiveness-content → mercy-seal) is significant
at p≈3×10⁻⁵.

Pre-reg SHA256 `cc1962fba93c68c14026b468d0bef6bc4b66f6b701f85f5eb64168fd7c204cb5`,
seed 20260509, 10,000 perms (verified at runtime).

---

## 1. What this extends

[[h-new-2070-divine-name-pairing|H-NEW-2070]] established the **positional**
*al-fawāṣil* grammar — which name occupies the head (penultimate) slot vs the
seal (final) slot, that the 321 dual-name closings are non-random (p<0.0001), and
the head/seal asymmetry (*raḥīm*/*ḥakīm* seal, *samīʿ* never seals, *ʿalīm*
pivot). It deliberately did NOT touch the **semantic** axis: *why this pair, on
this verse?*

H-NEW-2300 supplies that axis. The classical doctrine (al-Zarkashī *murāʿāt
al-fāṣila*, al-Rāzī *tamkīn al-fāṣila*) asserts the seal is chosen to SUIT the
verse meaning. We test it as a falsifiable association between the verse body's
content-roots and the thematic class of the sealing pair.

---

## 2. Detection (identical to H-NEW-2070) and seal-pair classes

Verse-final pair detector reproduces H-NEW-2070 exactly: **321 verses** close on a
divine-name pair (`quran-text/quran-no-tashkeel.json`; last two tokens both
base-normalize to one of the 97 single-token al-Tirmidhī names).

The 97 participating names are mapped by Buckwalter root to three thematic
super-classes (pre-registered §3):

| Super-class | Names (root) |
|:--|:--|
| **MERCY** | ghafūr/ghaffār (gfr), raḥīm/raḥmān (rHm), tawwāb (twb), wadūd (wdd), ʿafū (Efw), raʾūf (rAf), barr, ḥalīm, shakūr |
| **POWER** | ʿazīz (Ezz), ḥakīm/ḥakam (Hkm), qahhār, jabbār, kabīr/mutakabbir, qadīr/qādir/muqtadir, ʿalī/mutaʿālī, ʿaẓīm, qawī, matīn |
| **KNOW** | ʿalīm (Elm), samīʿ (smE), baṣīr (bSr), khabīr, shahīd, ḥafīẓ, laṭīf, raqīb |

A verse is **pure-class** iff BOTH seal names share a super-class. **212/321**
verses are pure-class (MERCY 94, POWER 62, KNOW 56). Top pairs per class:

| Class | Dominant pairs |
|:--|:--|
| MERCY | *ghafūr+raḥīm* (64), *tawwāb+raḥīm* (9), *raḥmān+raḥīm* (6), *ghafūr+ḥalīm* (4) |
| POWER | *ʿazīz+ḥakīm* (47), *ʿalī+kabīr* (5), *qawī+ʿazīz* (5) |
| KNOW | *samīʿ+ʿalīm* (31), *samīʿ+baṣīr* (11), *laṭīf+khabīr* (5) |

Mixed pairs (e.g. *ʿalīm+ḥakīm* KNOW+POWER, 29; *ʿazīz+raḥīm* POWER+MERCY, 13) are
excluded from the primary test to avoid arbitrary tie-breaking.

---

## 3. Content feature + leakage control

Verse-body content = QAC v0.4 stem-roots
(`data/morphology/quranic-corpus-morphology-0.4.txt`) of all words EXCEPT the final
two (the seal). A separate, theme-defined content-lexicon (§4 of pre-reg) tags
roots as MERCY-content (sin/forgiveness/wrong: *dhanb*, *ithm*, *ẓulm*, *baghy*,
*tawb*, *ghfr*, …), POWER-content (command/decree/dominion/fighting: *mulk*,
*amr*, *qaḍy*, *ktb*, *qitāl*, …), or KNOW-content (knowledge/perception/witness:
*ʿilm*, *samʿ*, *baṣr*, *shahd*, *raʾy*, …).

**Leakage control (PRIMARY):** the two seal-name roots are STRIPPED from the body,
so a verse cannot "match" simply by echoing its own seal. A verse's dominant
content-class = the class with most body-root hits; ties → no-call.

---

## 4. Results

### 4.1 Primary — leakage-stripped, label-permutation null (n_called = 91/212)

| Stat | Observed | Null mean | Null p97.5 | p_perm | Pass (α=0.025) |
|:--|:-:|:-:|:-:|:-:|:-:|
| **H1 mutual information** | **0.1499 bits** | 0.0331 | 0.0919 | **0.00110** | ✅ |
| **H2 match-rate** | **0.4725** | 0.3600 | 0.4615 | **0.01540** | ✅ |

Observed MI is **4.5× the null mean** and clears the 97.5th percentile. Both
direction-locked statistics pass the Bonferroni-2 family.

**Confusion matrix** (seal-class rows × dominant-content-class cols, called verses):

|        | MERCY-content | POWER-content | KNOW-content |
|:--|:-:|:-:|:-:|
| **MERCY-seal** | **29** | 5 | 11 |
| **POWER-seal** | 5 | **7** | 10 |
| **KNOW-seal**  | 6 | 11 | **7** |

The diagonal is positive in all three classes, but the signal is **carried by the
MERCY axis**: 29/45 called mercy-sealed verses have mercy-dominant content. POWER
and KNOW are partly confused with each other (the *ʿazīz/ḥakīm* "power-wisdom-as-
governance" and *ʿalīm/samīʿ* "knowledge" registers share decree/judgment
vocabulary). This is reported as honest texture, not smoothed away.

### 4.2 Secondary directional — MERCY-content enriches MERCY-seal (H3)

2×2 over ALL 212 pure-class verses (leakage-stripped):

|  | MERCY-seal | other-seal |
|:--|:-:|:-:|
| **body has MERCY-content** | 37 | 17 |
| **body lacks MERCY-content** | 57 | 101 |

**Odds-ratio = 3.86; one-sided Fisher exact p = 3.25×10⁻⁵.** A verse whose body
carries sin/forgiveness/wrongdoing vocabulary is ~3.9× more likely to close on a
mercy-pair. This is the cleanest empirical instantiation of the classical claim.

Exemplars (forgiveness-content → mercy-seal, seal-roots stripped from the count):
- Q 2:173 forbidden foods, *necessity without transgression* (Avm/Edw/bgy) →
  *ghafūr raḥīm*.
- Q 3:31 "He will forgive your **sins** (*dhanb*)" → *ghafūr raḥīm*.
- Q 3:89 "except those who **repent** (*tawb*)" → *ghafūr raḥīm*.
- Q 4:110 "whoever does **evil** or **wrongs** himself (*sūʾ*/*ẓulm*)" → *ghafūr raḥīm*.

And power-content → power-seal:
- Q 3:18 *dominion/mulk* + "no god but He" → *ʿazīz ḥakīm*.
- Q 33:25 the Confederates' **battle** (*qitāl*) → *qawī ʿazīz* ("Strong, Mighty").
- Q 39:1 "the **sending-down of the Book** (*ktb*)" → *ʿazīz ḥakīm*.

### 4.3 Leakage sensitivity (MW-6, instrument-control)

Keeping the seal's own roots in the body (NOT the claim under test) inflates the
effect to MI=0.366 (p<0.0001), match-rate=0.626 (p<0.0001) — exactly the
self-echo we control for. The leakage-stripped primary is the conservative,
defensible number.

---

## 5. Verdict and scope

**EXTENDS H-NEW-2070 (PASS-DIRECTED-CONTENT).** The dual-name fāṣila is governed by
TWO orthogonal grammars:
1. **Positional** (H-NEW-2070): head/seal slot assignment, p<0.0001.
2. **Semantic** (H-NEW-2300): the pair's thematic class tracks the verse body's
   content, MI p=0.0011, mercy-axis Fisher p=3×10⁻⁵.

Together they upgrade the *al-fawāṣil* doctrine from a positional-collocational
constraint to a **content-conditioned seal-selection rule**. The seal is not a
formulaic flourish; it is chosen *li-yumakkin al-maʿnā* — to settle the meaning —
as al-Rāzī's *tamkīn al-fāṣila* asserts.

---

## 6. Classical connection

- **al-Zarkashī**, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *al-fawāṣil*
  (*murāʿāt al-fāṣila*): the fāṣila is chosen in concord with the verse meaning.
- **al-Rāzī**, *Mafātīḥ al-ghayb*: the recurrent *tamkīn al-fāṣila* observation
  that the body "settles" the closing epithet so it is felt as necessary.
- **al-Suyūṭī**, *al-Itqān*, nawʿ 59 (*fawāṣil*; *asmāʾ mutazāwijah*).

These works name the doctrine but never tabulated it; H-NEW-2300 supplies the
falsifiable corpus test and confirms the matching is real, with the MERCY axis as
its sharpest carrier. (Citations at the level the project attests in
H-NEW-2070 §10.78.6; no unverified page-numbers asserted.)

---

## 7. Honest limits

1. **Three-class compression.** MERCY/POWER/KNOW collapses 97 names into three
   buckets; finer thematic structure (e.g. *wisdom* vs *might* inside POWER) is
   lost, which is exactly where the POWER↔KNOW confusion lives.
2. **Signal is MERCY-dominated.** The omnibus MI passes, but POWER and KNOW
   diagonals are weak; do NOT claim each class is independently matched. The
   honest claim is "content predicts seal, driven by the forgiveness↔mercy link."
3. **Content-call coverage.** Only 91/212 pure-class verses carry a content-lexicon
   root with an unambiguous dominant class; the lexicon is theme-curated, not
   exhaustive. A richer semantic embedding could move the estimate either way.
4. **QAC root coverage.** Function words and proper names lack roots; the body
   profile is a content-root profile, not a full-semantics profile.
5. **Mixed pairs excluded** from the primary; the bidirectional/mixed seals
   (*ʿalīm+ḥakīm*, *ʿazīz+raḥīm*) are precisely where a verse may blend themes,
   and are not adjudicated here.

---

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2300-dual-name-fasila-seal.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2300.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2300.json`
- Finding: `findings/phase-b-hypotheses/h-new-2300-dual-name-fasila-seal.md` (this file)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
