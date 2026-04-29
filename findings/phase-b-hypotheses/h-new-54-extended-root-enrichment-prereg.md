---
id: H-NEW-54
title: Extended Root-Enrichment Scan — Are Muqaṭṭaʿāt-Opened Surahs Enriched in Other Revelation-Theme Roots in v1-3?
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-54-specialist
test: hypergeometric two-sided per root, Bonferroni-10
parent_finding: H-NEW-53 (kitāb/qurʾān enrichment p ≈ 3.17 × 10⁻¹²)
rules_tuple: (no-tashkeel; substring search on verses 1-3; surface forms locked below)
---

# [[h-new-54-extended-root-enrichment|H-NEW-54]] — Extended Root-Enrichment Scan (PRE-REG)

## Question

[[h-new-53-muqattaat-book-reference|H-NEW-53]] confirmed muqaṭṭaʿāt-opened surahs (n=29) are massively enriched (24/29 = 82.8%) for **kitāb** OR **qurʾān** references in opening 3 verses (vs 11.8% in non-muqaṭṭaʿāt). p = 3.17 × 10⁻¹².

**The follow-up question**: is the enrichment specific to kitāb/qurʾān, or does it generalize to a broader semantic field of "revelation-theme" roots?

We pre-register a 10-root family. Each root tested independently with hypergeometric two-sided p; Bonferroni-corrected at α_per = 0.005.

## Family of 10 roots (LOCKED 2026-04-15, BEFORE testing)

The 10 roots are:

1. **ك-ت-ب** (k-t-b / kitāb / book) — already tested [[h-new-53-muqattaat-book-reference|H-NEW-53]]; included for replication
2. **ق-ر-ء** (q-r-ʾ / qurʾān / read-recite) — already tested [[h-new-53-muqattaat-book-reference|H-NEW-53]]; included for replication
3. **آ-ي-ا** (ʾ-y-ā / āyāt / signs-verses)
4. **ذ-ك-ر** (dh-k-r / dhikr / remembrance, reminder, mention)
5. **ن-ز-ل** (n-z-l / nazala / sent down — REVELATION)
6. **و-ح-ي** (w-ḥ-y / waḥy / inspiration-revelation)
7. **و-ع-د** (w-ʿ-d / waʿd / promise — covenant)
8. **هـ-د-ي** (h-d-y / hudā / guidance)
9. **ر-ب-ب** (r-b-b / rabb / Lord)
10. **ا-ل-ه** (ʾ-l-h / ilāh / deity)

The root-set is locked to these 10 BEFORE running.

## Surface forms per root (LOCKED 2026-04-15, BEFORE testing)

Substring matching (no-tashkeel orthography) for compactness; for `r-b-b` we use TOKEN-boundary matching to avoid known false positives (أربعة "four", ربما "perhaps", اقترب "approach", etc.). All other roots use simple substring matching.

For roots 1–2 we match the PUBLISHED [[h-new-53-muqattaat-book-reference|H-NEW-53]] form lists exactly to ensure replication.

```
KITAB        = {كتاب, كتب, الكتاب, الكتب, كتابك, كتابه, كتابي, كتابهم, كتابا, كتابنا}
QURAN        = {قرآن, القرآن, قرءان, القرءان, قرءن, قرآنا, قرآنه}
AYAT         = {آية, آيات, الآيات, آياته, آياتنا, آياتي, آياتك, آياتها, آياتهم,
                آيتنا, الآية, لآيات, لآية, بآياتنا, بآياتي, بآياته, بآيات}
DHIKR        = {ذكر, الذكر, ذكرى, تذكرة, ذكرا, ذاكر, يذكر, تذكر, يتذكر, مذكر,
                مدكر, تذكرون, يذكرون, الذكرى, بالذكر, لذكر, فاذكر, اذكر, ذكره}
NAZALA       = {نزل, أنزل, تنزيل, ينزل, ننزل, نزلنا, أنزلنا, منزل, منزلين,
                تنزل, تنزلت, منزلون, نزله, نازلون, منزلا, تنزله, منازل}
WAHY         = {وحي, وحيا, الوحي, يوحي, يوحى, أوحى, أوحينا, نوحي, نوحيه, موح, يوحون}
WAD          = {وعد, الوعد, وعدنا, وعدا, وعدكم, وعده, وعدنى, موعود, ميعاد,
                الموعد, الميعاد, موعد, وعدتكم, وعدتم, يعد, وعدتنا}
HUDAA        = {هدى, الهدى, هدي, مهتد, تهتد, اهد, يهدي, هاد, الهداية,
                هديتنا, لهدى, يهتد, مهديا, هدانا}
RABB (TOKEN) = {رب, ربك, ربه, ربهم, ربنا, ربي, ربكم, الرب, ربها, ربهما, ربكما,
                برب, بربك, بربه, بربهم, بربنا, بربكم, بربها,
                وربك, وربه, وربهم, وربنا, وربي, وربكم, وربها,
                لرب, لربك, لربه, لربهم, لربنا, لربي, لربكم, لربها, فرب}
ILAH         = {إله, الإله, إلها, إلهك, إلهي, إلهنا, إلهكم, إلههم, آله, ءاله, الإلاه}
```

## Procedure (LOCKED)

1. Load `quran-no-tashkeel.json` via `tools.loader.load_quran("no-tashkeel")`.
2. Use the locked muqaṭṭaʿāt-opened set (n=29):
   `MUQ = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
   36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}`
3. For each surah, concatenate verses 1, 2, 3 (literal v.id ≤ 3) into a single text-window.
4. For each root family separately:
   - Compute `K_root` = number of surahs (out of N=114) whose v1-3 window contains ANY listed surface form.
     - For RABB: tokenize the v1-3 window on Arabic-letter runs and match exact token equality.
     - For all other roots: substring match.
   - Compute `obs_root` = number of muqaṭṭaʿāt-opened surahs (out of n=29) whose v1-3 window contains ANY listed surface form.
   - Hypergeometric **two-sided** p: `p = 2 × min(P(X ≥ obs), P(X ≤ obs))`, capped at 1.
   - Use `scipy.stats.hypergeom.sf(obs-1, N=114, K_root, n=29)` and `cdf(obs, N, K_root, n)`.
5. Apply Bonferroni-10 across the family: α_per = 0.05 / 10 = 0.005.
6. Per-root verdict:
   - **PASS** (significant after Bonferroni, enriched): obs > expected AND p < 0.005
   - **PASS-DEPLETED** (significant after Bonferroni, depleted): obs < expected AND p < 0.005
   - **NULL**: p ≥ 0.005

## Composite verdict

- 0 roots significant → composite NULL
- 1–3 roots significant → composite EXPLORATORY-PARTIAL
- 4–7 roots significant → composite PASS-BROAD-FIELD
- 8–10 roots significant → composite STRONG-PASS-FIELD-WIDE

## MW-5 positive control

The combined kitāb-OR-qurʾān test ([[h-new-53-muqattaat-book-reference|H-NEW-53]]) gave p ≈ 3.17 × 10⁻¹². Roots 1 and 2 tested SEPARATELY are subsets and so each must independently give a p value strongly below 0.005 (specifically: kitāb alone is expected to dominate, qurʾān alone is expected to also be significantly enriched).

If EITHER kitāb or qurʾān fails to clear p < 0.005 in this independent run, the pipeline is suspect. (We expect both to clear by orders of magnitude.)

## Garden-of-forking-paths log

Decisions made BEFORE running the test:

- **Root family selected**: 10 roots representing the canonical "revelation-theme" semantic field. Selection driven by:
  - 2 already in [[h-new-53-muqattaat-book-reference|H-NEW-53]] (replication anchors)
  - 4 directly revelatory: āyāt, dhikr, nazala, waḥy
  - 1 covenant: waʿd
  - 1 guidance: hudā
  - 2 theological: rabb, ilāh
  
- **NOT included** (deliberate exclusions to prevent gerrymandering):
  - q-l-m (pen) — could be argued semantically book-related but extends the field too far
  - s-t-r (line/inscription) — same
  - k-l-m (word/speech) — same
  - r-s-l (messenger) — separate semantic field (prophetology, not revelation-content)
  - n-b-y (prophet) — same as r-s-l
  - All Allah-name attributes (al-Raḥmān, al-Ḥakīm, etc.) — too broad
  - Eschatological roots (ʾ-kh-r, q-y-m) — separate field

- **Surface form lists**: substring matching is approximate. False positive risk: minimal for most roots; HIGH for r-b-b → so we use TOKEN-boundary matching for r-b-b only.

- **Two-sided test**: chosen because depletion is also informative (e.g., if a root is significantly UNDER-represented in muq surahs, that's also worth reporting). Hypergeometric two-sided uses `2 × min(p_upper, p_lower)`, capped at 1.

- **Bonferroni-10**: families of 10. We do NOT apply additional outer correction because this is a single closed family.

## Pre-commit declaration

Per the project's [Bonferroni tightening vs loosening](feedback_bonferroni_tightening_vs_loosening.md) rule: this pre-reg LOCKS the family at 10 roots. Adding more roots after seeing results would require ratification. Tightening (e.g., adding more roots) is allowed; loosening (removing roots after seeing results) is not.

## Seed and reproducibility

- SEED = 20260416 (irrelevant for closed-form hypergeometric, included for any auxiliary computations).
- All forms LOCKED in this pre-reg file.
- Script: `scripts/h_new_54_extended_root_enrichment.py`
- JSON output: `findings/phase-b-hypotheses/csv/h-new-54.json`
- Findings: `findings/phase-b-hypotheses/h-new-54-extended-root-enrichment.md`

## Pre-reg SHA cross-reference

The script will compute SHA-256 of THIS pre-reg file at run time and embed it in the JSON output for tamper-evidence.
