---
id: H-NEW-1800
title: 99 asmāʾ al-ḥusnā complete enumeration + alternative-orthography rehabilitation audit
date_locked: 2026-05-10
seed: 20260509
n_perm: 0
bonferroni_k: 1
bonferroni_family: H-NEW-1800-99-names-enumeration (single descriptive cataloguing exercise; no permutation null)
alpha_bon: 0.05
direction_of_effect: of the 34 names absent under strict-substring (H-NEW-1560 Variant A), at least 10 will be rehabilitated under at least one of {Variant B no-ال substring, Variant C consonantal-root substring, Variant D full-tashkeel substring}; the IRRECOVERABLE set (absent under all 4 variants) is the most credibly Quran-absent subset of the al-Tirmidhī list.
origin: H-NEW-1560 reported 34/99 absent under Variant A substring; the prior morphology-strict catalog reported ~41/99 absent under Buckwalter LEM matching; al-Suyūṭī (al-Itqān nawʿ 56) acknowledges that some 99-list names are reconstructive, not Quranically attested in canonical al-X form. This pre-reg locks a complete 4-variant enumeration to identify (a) which absent names can be rehabilitated under alternative orthography and (b) the irrecoverable subset whose absence is independent of rule-tuple choice.
verdict_ceiling: DESCRIPTIVE-ONLY (cataloguing exercise; no permutation null required; PASS-DIRECTED is achievable only via independent replication on a second 99-list, which is a separate test)
rules_tuple:
  orthography_primary: no-tashkeel (Variants A, B, C)
  orthography_secondary: full-tashkeel (Variant D)
  word_definition: orthographic-token (whitespace split)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  name_list_source: data/asma-al-husna.txt (al-Tirmidhī #3507 / al-Walīd b. Muslim chain — gharīb)
  variant_A_rule: strict substring with ال (e.g. الرحمن) in no-tashkeel verse text; identical to H-NEW-1560 detection rule
  variant_B_rule: substring without leading ال (e.g. رحمن) in no-tashkeel verse text; matches verbal/participial occurrences and indefinite forms
  variant_C_rule: consonantal triliteral root substring (e.g. رحم for al-Raḥmān/al-Raḥīm); matches verbal forms, plurals, and any root-attested word; deliberately permissive — false positives expected (e.g. root مكك for الملك conflicts with non-divine king-of-Egypt usages); use only for rehabilitation, NOT for cohesion testing
  variant_D_rule: substring with full-tashkeel (e.g. ٱلرَّحْمَٰن) in full-tashkeel verse text; tests whether diacritical or rasm-orthography variation suppresses the Variant A match (e.g. final hamza-on-yā vs hamza-on-line, alif-maqsura vs alif-tail)
  multi_token_handling: مالك الملك and ذو الجلال والإكرام normalized to single-space whitespace before substring match
  root_derivation_for_C: manual + QAC-cross-checked triliteral root for each of the 99 names, derived from the canonical Buckwalter-encoded QAC root-index (data/morphology/root-index.json) and from standard lexicography (Lane); each name's root locked in the script before run
  rehabilitation_definition: a name absent under Variant A is "rehabilitated" if it appears under at least one of {B, C, D}
  irrecoverable_definition: a name absent under ALL four variants
---

# H-NEW-1800 pre-registration — 99 asmāʾ al-ḥusnā complete enumeration

## Origin

H-NEW-1560 (the divine-names-distribution finding) reported that under the strict-substring rule (with the definite article ال), 34 of the 99 al-Tirmidhī names do not appear anywhere in the Quran. The prior morphology-strict catalog (`divine-names-distribution.md`, Buckwalter LEM with DET-masc-sing-divine constraint) reported ~41 of 99 absent. These two figures bracket the question: what is the true corpus-internal coverage of the al-Tirmidhī enumeration, and which names are systematically absent regardless of rule-tuple permissiveness?

al-Suyūṭī (*al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 56) explicitly acknowledges that the 99-enumeration is reconstructive: some names listed in the al-Walīd b. Muslim chain are derived from Quranic verbal-root forms or from prophetic ḥadīth attribution rather than from canonical *al-X* lexicalized attestations in the Quran. The classical question is: which names are these?

This pre-reg locks a complete 4-variant enumeration that operationalizes the rule-tuple-fragility audit:

- **Variant A** (with ال, no-tashkeel): the H-NEW-1560 rule. Strictest detection.
- **Variant B** (without ال, no-tashkeel): captures non-prefixed forms (e.g. *yuḥyī wa-yumīt* would not match *al-Muḥyī al-Mumīt* under Variant A but root verbs match under B/C).
- **Variant C** (consonantal triliteral root, no-tashkeel): most permissive. Captures any word sharing the root letters. False-positive-prone (e.g. the root مكك for *al-Malik* matches Pharaoh, Joseph's Egyptian king, etc.). Used only as a rehabilitation ceiling.
- **Variant D** (full-tashkeel with ال): tests whether rasm-orthographic variation (e.g. final hamza placement, alif-maqsura vs alif-tail, shaddah-position) suppresses Variant A matches that the full-tashkeel script would rehabilitate.

## Hypothesis

**H1 (rehabilitation)**: of the 34 H-NEW-1560 Variant-A-absent names, at least 10 will be rehabilitated under at least one of {B, C, D}. Mechanism: many of these names are participles or verbal forms whose triliteral root is corpus-attested even when the lexicalized *al-X* substring is not (e.g. al-Muḥyī from root حيي appears as the verb *yuḥyī*; al-Mubdiʾ from root بدا appears as *yubdiʾu*).

**H2 (irrecoverable set)**: a non-empty subset of the 34 will be absent under ALL FOUR variants. These are the most credibly Quran-absent names of the al-Tirmidhī list — their presence in the enumeration is from later prophetic-tradition expansion (e.g. additional ḥadīth chains, Sufi devotional praxis, al-Bayhaqī's expanded list, al-Walīd b. Muslim's own variants), not from the Quranic text.

## Tests / cells

- **Cell 1** (rehabilitation count): k_rehab = #{names absent under A but present under at least one of B,C,D}. Pass-direction: k_rehab ≥ 10 of 34.
- **Cell 2** (irrecoverable count): k_irr = #{names absent under all 4 variants}. Pass-direction: k_irr ≥ 1 (any irrecoverable name is a corpus-empirical reinforcement of al-Suyūṭī's classical observation). Honest pre-commit: k_irr is expected to be small (5-15 of 34) because Variant C is very permissive on triliteral roots.

## Direction lock

Direction LOCKED before computation:
- k_rehab ≥ 10 (rehabilitation hypothesis confirmed)
- k_irr ≥ 1 (irrecoverable subset exists)

The reverse-direction outcomes (k_rehab < 10, or k_irr = 0) are reportable as NULL with explicit reverse-direction annotation and must NOT be reframed.

## A-priori expectation

Honest prediction: ~25 of 34 Variant-A-absent names will be rehabilitated under Variant C (root substring is very permissive). Under Variant B (no-ال substring), expected rehab ≈ 10-15 (many participial forms of al-X are corpus-attested without the article). Under Variant D (full-tashkeel), expected rehab ≈ 2-5 (most Variant A matches and misses are orthography-stable). The irrecoverable set is expected to be in the 3-10 range — the genuinely Quran-absent names.

## Methodology

### Step 1: Load 99-names list
- Source: `/Users/grey/Downloads/quran/data/asma-al-husna.txt`.
- One name per line; comment lines (`#`-prefixed) and empty lines skipped.
- Multi-token entries (#89 مالك الملك, #90 ذو الجلال والإكرام) normalized to single internal whitespace.

### Step 2: Derive Variants B, C, D variants for each name
- **Variant B**: strip leading ال from the canonical name. For multi-token names, strip ال from the FIRST token only (مالك الملك → مالك الملك, since first token has no ال; ذو الجلال والإكرام unchanged since ذو is non-ال).
- **Variant C**: derive triliteral consonantal root. Use the standard lexicographic root for each name (locked in the script as a name → root dict). Cross-check against QAC root-index (`data/morphology/root-index.json`) when available. For names with weak letters (alif/wāw/yāʾ), use the underlying triliteral (e.g. al-Hādī root هدي, al-Walī root ولي, al-Wālī root ولي).
- **Variant D**: locate the full-tashkeel equivalent of the name. Since the canonical name list uses a partial-vocalization form, search the full-tashkeel corpus for the name with any diacritical pattern (rasm-skeleton match where consonant sequence + ال matches). Implemented as: rasm-skeleton(name with ال) against rasm-skeleton(every word in full-tashkeel corpus).

### Step 3: Match each variant against the appropriate corpus
- Variants A, B, C: against `quran-text/quran-no-tashkeel.json` (whitespace-normalized verse text).
- Variant D: against `quran-text/quran-full-tashkeel.json` (whitespace-normalized + diacritic-stripped to rasm).

### Step 4: Compute rehabilitation status per name
For each of the 99 names, record present/absent under each of A, B, C, D. Tag rehabilitation status:
- ALL-FOUR: present under A, B, C, D (the "fully Quran-attested" core).
- A-OK: present under A (and possibly others); H-NEW-1560 attestation.
- REHAB-B: absent under A, present under B.
- REHAB-C: absent under A, B, present under C (root-only).
- REHAB-D: absent under A, B, C, present under D (rasm-only — diacritical orthography mismatch).
- IRRECOVERABLE: absent under all 4.

### Step 5: Cross-reference classical lists
- al-Suyūṭī *al-Itqān*, nawʿ 56 — alternative enumerations noted (al-Ḥākim ~80, expanded lists >300).
- al-Bayhaqī, *al-Asmāʾ wa-l-Ṣifāt* — alternative 99-list (where extracted in our data).
- al-Walīd b. Muslim chain — the al-Tirmidhī source.
- Manual cross-check of irrecoverable set against al-Suyūṭī's nawʿ 56 to confirm classical acknowledgement.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-1800.json` — per-name 4-variant matrix, rehab counts, irrecoverable list.
- `findings/phase-b-hypotheses/h-new-1800-99-names-enumeration.md` — full finding writeup.
- `findings/phase-b-hypotheses/scripts/h-new-1800.py` — locked-SHA runner.

## Honest limits

- **Variant C is over-permissive**: triliteral root substring matches yield massive false positives. Example: al-Malik (root مكك? canonically ملك — same root letters but Quranic occurrences include the king of Egypt in Q 12, malak "angel" if root ملك is used). This is acceptable for *rehabilitation ceiling* purposes — the goal is to identify names whose root-letters appear *anywhere*, not to claim they refer to God specifically. Variant C results are explicitly UPPER-BOUND on Quranic plausible attestation.
- **Variant D's rasm-matching is sensitive to script normalization**. Full-tashkeel uses Unicode codepoints that differ from no-tashkeel (e.g. ٱ vs ا for Allāh's article). The script normalizes to rasm-skeleton before matching.
- **Root derivation is manual**. For each of the 99 names, the triliteral root is determined from standard Arabic lexicography (Lane, Hans Wehr) and locked in the script's NAME_TO_ROOT dictionary BEFORE the SHA-lock. No post-hoc adjustment.
- **The al-Tirmidhī list itself is gharīb**. The 99-enumeration is later-tradition. This pre-reg is not testing the validity of the enumeration; it is cataloging the empirical fact of which names are Quranically attested under which rule-tuples.
- **No FR cohesion test**: this is descriptive cataloguing only. No permutation null is required.

## Cross-finding connections

- **H-NEW-1560** (divine-names-distribution): the primary parent. H-NEW-1800 is a depth-2 extension answering the rule-tuple-fragility question that H-NEW-1560 raised.
- **divine-names-distribution.md** (morphology-strict, prior project finding): another point on the rule-tuple curve — Buckwalter DET-masc-sing-divine. Should converge with H-NEW-1800 Variant A within 5-10 names.
- **H-NEW-1350** (Allāh-density Medinan > Meccan, PASS-DIRECTED p = 10⁻⁴): grounds the single-name (الله) result that dominates the 99-list.
- **al-Suyūṭī, *al-Itqān*, nawʿ 56 (asmāʾ Allāh)**: classical acknowledgement of the reconstructive nature of the 99-enumeration; corroborated empirically here.
- **cross-finding-025** (marker-thickness): the irrecoverable set is the upper-bound on "purely-tradition" names (not corpus-marker-attested at any thickness).

## Pre-registration discipline

- All four variant detection rules locked in this file.
- Triliteral root for each of 99 names will be embedded in the script's NAME_TO_ROOT dict.
- SHA256 of this locked file is computed at the end of pre-registration and embedded in the runner.
- Direction is locked: rehabilitation hypothesis requires ≥10 of 34 V-A-absent names recovered.
- Seed 20260509.
