---
id: H-NEW-2520
title: Pericope-onset / narrative-onset formula census — wa-idh / idh / wa-lammā / lammā / wa-qālū / qālū
type: pre-registration
date: 2026-05-30
author: Waiel Al-Shujaa
status: LOCKED (pre-observation)
seed: 20260509
n_perm: 10000
bonferroni_family: 3 (idh / lammā / qālū density-concentration tests)
---

# Pre-registration — H-NEW-2520: Pericope-Onset / Narrative-Onset Formula Census

## 0. One-line statement

Build a GENERATOR that enumerates, corpus-wide and with coordinates, every occurrence
of the four classical **narrative-onset markers** that open story-pericopes (*qaṣaṣ* episodes):

1. **wa-idh / idh** (وَإِذْ / إِذْ, "and recall when…") — the *qaṣaṣ*-onset par excellence
   (*wa-idh qāla*, *wa-idh akhadhnā mīthāqakum*); a time-adverb of **recall** that opens a
   remembered past episode.
2. **wa-lammā / lammā** (وَلَمَّا / لَمَّا, "and when…") — the narrative-completion / event-onset
   adverb introducing the next beat of an unfolding story.
3. **wa-qālū / qālū** (وَقَالُوا / قَالُوا, "and they said") — the dialogue-onset, the most common
   speech-turn marker opening reported discourse inside a pericope.

This is the **NARRATIVE-ONSET complement** to H-NEW-2250's idhā-conditional/eschatological
cascade. It is the inverse register: where idhā (إِذَا) is the eschatological "when the sun is
folded up…" conditional concentrated in juzʾ-30, **idh (إِذْ) is the past-recall qaṣaṣ marker**
expected in the long narrative/legal surahs.

## 1. Background / relation to prior findings

- **H-NEW-2250** (§10.88, particle-cascade): verse-initial **idhā** (إِذَا, `LEM:<i*aA`,
  eschatological conditional) concentrates in juzʾ-30 (s≥78) at density 0.0532 vs 0.0205,
  p=0.00010. The idhā cascade peaks in the Takwīr/Infiṭār/Inshiqāq/Mursalāt band. **The present
  finding tests the INVERSE marker** — *idh* (إِذْ, `LEM:<i*`, past-recall), a grammatically
  distinct lemma — and locks the OPPOSITE direction (long surahs, s≤50).
- **H-NEW-2060** (§ first-/last-word taxonomy): the opener-taxonomy census; "idhā 7" openers
  are catalogued there. This finding works at the **verse-head** grain across the whole pericope
  body, not only surah-openers.
- **H-NEW-2260 / cross-finding-025/026** (pericope structure): prophet-cycle pericopes
  (Nūḥ/Mūsā/Ibrāhīm) are bounded narrative episodes. The onset markers enumerated here are the
  **boundary-marking grammatical skeleton** of those episodes — *wa-idh qāla rabbuka…*,
  *fa-lammā jāʾahum…*, *qālū…* dialogue turns.
- **al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān*: the *qaṣaṣ* (Quranic narrative) is treated as a
  distinct genre — "the stories relating to Noah's people as well as those of the ʿĀd, the
  Thamūd, the building of the Kaʿbah" (Itqān, English transl., qaṣaṣ/asbāb discussion; PDF on
  disk `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`). Ibn Abī
  al-Iṣbaʿ (cited in Itqān): "all the narratives of the Qurʾān appear … a single story … appears
  in multiple forms" — the *qaṣaṣ* register.
- **al-Zarkashī** *al-Burhān fī ʿulūm al-Qurʾān* (PDF on disk): the *makkī/madanī* and *mufaṣṣal*
  classifications underwrite the long-narrative (Meccan stories) vs short-mufaṣṣal (eschatology)
  register split that this finding's direction-lock relies on.

## 2. Data sources (all on disk; cite paths)

- Verse text & ordering: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (114 surahs, 6236 verses, Hafs-Kufan).
- Verse-initial morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
  (QAC v0.4, Buckwalter). The first word of each verse is location `(s:v:1:*)`; segment
  `(s:v:1:1)` carries any proclitic prefix (`PREFIX|w:` = wāw, `PREFIX|f:` = fāʾ).

## 3. Detection rules (rules-tuple) — LOCKED

Rules-tuple: `(QAC-v0.4 POS+LEM tags, verse-initial = word-index 1, basmala counted only in
Q1, Hafs-Kufan, Mashriqi)`.

A verse `(s,v)` is assigned a **narrative-onset family** based on word-1 segments. A verse may
be flagged for at most one of the three families (the three lemmas are mutually exclusive on
the relevant stem). The wāw/fāʾ proclitic does not change family membership — *wa-idh* and bare
*idh* are the same idh family (the recall sense is carried by *idh*); the *wa-/fa-* split is
reported as a descriptive sub-census.

- **idh family** (وَإِذْ / إِذْ, narrative-recall): word-1 has a segment whose STEM is the
  time-adverb `<i*` with `POS:T` and `LEM:<i*` (matched EXACTLY — `LEM:<i*` followed by `|` or
  end-of-features, so it does **NOT** match `<i*aA` = idhā, `<i*FA` = idhan, or `<i*on` = idhn
  "permission"). This is the **QAC-disambiguated** separation of narrative-recall *idh* from
  conditional *idhā* — the central methodological point.
  - Sub-census: *wa-idh* = the matched word-1 has segment-1 `PREFIX|w:`; *bare idh* = segment-1
    is itself the `<i*` stem; *fa-idh* = segment-1 `PREFIX|f:`.
- **lammā family** (وَلَمَّا / لَمَّا): word-1 has a segment with `POS:T` and `LEM:lam~aA`
  (matched exactly). Sub-census: *wa-lammā* (segment-1 `PREFIX|w:`), *fa-lammā* (segment-1
  `PREFIX|f:`), *bare lammā*.
- **qālū family** (وَقَالُوا / قَالُوا, dialogue-onset): word-1 has a segment with `POS:V`,
  `ROOT:qwl`, `LEM:qaAla`, perfect (`PERF`), 3rd-person masculine plural (`3MP`) — i.e. the
  verb *qālū* "they said". Sub-census: *wa-qālū* (segment-1 `PREFIX|w:`), *fa-qālū* (`PREFIX|f:`),
  *bare qālū*.

**Maximal-run enumeration (GENERATOR deliverable):** for each family, also enumerate every
maximal block of ≥3 consecutive verses (within one surah) all sharing that family head, with
length and `s:v_start–v_end` coordinates. Runs do not cross surah boundaries.

## 4. Hypotheses — DIRECTION LOCKED

### Primary (pre-registered, direction-locked)

**H1 (qaṣaṣ-recall register: long-surah concentration).** The verse-initial **idh**
(وَإِذْ / إِذْ) recall-onset marker is a **qaṣaṣ / covenant-recall** device that concentrates in
the **LONG narrative/legal surahs (s ≤ 50)** — the al-sabʿ al-ṭiwāl + early-mushaf Meccan-Medinan
narrative band — **NOT** in the short mufaṣṣal. This is the **INVERSE** of the H-NEW-2250
idhā-conditional juzʾ-30 concentration.

- **Direction LOCKED: density(idh, s≤50) > density(idh, s>50).** Higher in the long-surah head.
- Statistic: `Δ_idh = density(s≤50) − density(s>50)`, density = idh-headed verses per verse.
  Predict Δ_idh > 0.
- Null: permutation. Shuffle the idh-head indicator across all 6236 verse slots (preserving the
  total idh-head count), 10,000 perms, seed 20260509; recompute Δ each time; one-sided p =
  fraction of permuted Δ ≥ observed Δ.
- **REVERSAL RULE:** if observed Δ_idh ≤ 0 (idh is NOT denser in s≤50), the primary hypothesis is
  published as **NULL with full prominence / pre-commit reversal**, regardless of the census.

### Secondary (direction-locked, same register prediction)

**H1b (lammā same register).** *lammā* (وَلَمَّا / لَمَّا) is also a narrative-event marker;
direction LOCKED the SAME way: density(s≤50) > density(s>50). Δ_lammā > 0.

**H1c (qālū same register).** *qālū* (وَقَالُوا / قَالُوا) is the dialogue-onset of reported
narrative speech; direction LOCKED the SAME way: density(s≤50) > density(s>50). Δ_qālū > 0.

### Bonferroni family
Three direction-locked density tests (idh / lammā / qālū) → **Bonferroni k=3,
α_cell = 0.05/3 = 0.0167**. The PRIMARY claim is H1 (idh); H1b/H1c are corroborating
narrative-register tests in the same family. A test is CONFIRMED-DIRECTED only if its
one-sided p < 0.0167.

### Secondary (descriptive enumeration — the GENERATOR deliverable)
**H2.** A full corpus-wide census of all three families: count, per-surah distribution, the
wa-/fa-/bare sub-split, and every maximal run (≥3) with coordinates. Pre-committed to reporting
ALL occurrences and runs (no cherry-picking), ranked by surah-density and run-length. This is
delivered regardless of H1 outcome.

## 5. Success / failure criteria (per test)

- **CONFIRMED (directed):** Δ > 0 AND one-sided perm-p < 0.0167 (Bonferroni-3).
- **DIRECTIONAL:** Δ > 0 but 0.0167 ≤ p < 0.05.
- **NULL:** Δ > 0 but p ≥ 0.05, OR
- **NULL / PRE-COMMIT REVERSAL:** Δ ≤ 0 (wrong direction) — published with full prominence.
- **Overall verdict:** CONFIRMED if H1 (idh) confirms; the lammā/qālū outcomes refine the
  register-breadth interpretation. The census (H2) is the honest deliverable regardless.

## 6. MW protections

- **MW-1 (instrument-prior):** detection rules (exact LEM disambiguation idh≠idhā, POS:T,
  ROOT:qwl 3MP PERF) fixed above before any run.
- **MW-2 (corpus-prior):** 10,000-perm permutation null per family.
- **MW-3 (alternative-models):** the primary cut is s≤50 (al-Suyūṭī/al-Zarkashī Hijra/mufaṣṣal
  kink). A robustness re-run with the secondary cut s≤49 vs s≥50 and with the s≥78 juzʾ-30
  comparison (to directly contrast with H-NEW-2250's idhā cut) is reported as a secondary lens.
- **MW-5 (replication):** second seed 20260511 for the null; result must agree.
- **MW-6 (instrument-control / genre-specificity):** idhā (conditional, H-NEW-2250) is the
  built-in CONTROL — if idh concentrates in s≤50 while idhā concentrates in s≥78, the two
  homographic-but-distinct lemmas occupy OPPOSITE registers, confirming genre-specificity at
  the grammatical-disambiguation level (the central novel claim).
- **MW-7 (post-hoc cap):** no post-hoc-noticed claim promoted above α=0.05.

## 7. Output files

- This pre-reg (SHA-locked).
- Script: `findings/phase-b-hypotheses/scripts/h-new-2520.py` (embeds SHA, verifies at runtime).
- JSON: `findings/phase-b-hypotheses/csv/h-new-2520.json`.
- Findings: `findings/phase-b-hypotheses/h-new-2520-pericope-onset.md`.

## 8. Equal NULL prominence pledge

If H1 reverses or fails, the finding is published as NULL with the same prominence as a
confirmation. The onset-marker census is the honest deliverable either way. The wa-idh
narrative-skeleton map is the GENERATOR, independent of the significance verdict.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
