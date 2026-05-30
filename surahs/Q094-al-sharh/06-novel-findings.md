---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q094-F-01 — ALL THREE ARMS CONFIRMED (corpus-singleton single-connective adjacency + global min-edit + definite/indefinite orthographic asymmetry)
seed: 20260509
n_perm: 10000
---

# Q 94 al-Sharḥ — Pre-Registered Novel Findings

One pre-registered three-arm test, run with seed 20260509 (replicated at 20260530) and 10,000
permutations, pre-reg SHA-256 locked before computation and verified at runtime (fail-fast on mismatch).

- **Pre-reg:** `surahs/Q094-al-sharh/Q094-F-01-usr-yusr-reprise-prereg.md` (also `preregs/`)
- **Pre-reg SHA-256:** `2dd938018b303e0da9e8a1313d3fe710fe83123913e6aaa705c1975908f71d2a`
- **Script:** `scripts/Q094_F_01_usr_yusr_reprise.py` (also `surahs/Q094-al-sharh/scripts/`) — verifies SHA at runtime ("SHA OK" printed)
- **JSON:** `surahs/Q094-al-sharh/csv/Q094-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The test promotes the close-reading observation about Q 94:5-6 — *fa-inna maʿa al-ʿusri yusrā* (v 5) /
*inna maʿa al-ʿusri yusrā* (v 6), character-identical save the leading connective fāʾ — into three
falsifiable, direction-locked corpus claims.

---

## Q094-F-01 Arm A — the single-connective near-verbatim adjacency is corpus-UNIQUE (CONFIRMED)

**Hypothesis (pre-committed):** among all adjacent same-surah verse pairs, Q 94:5-6 is the **unique** pair
whose two normalized verse-strings are identical except for a single leading connective particle (a
leading fāʾ ف or wāw و on exactly one token, all other tokens identical, equal token-count).

**Result (`csv/Q094-F-01.json` → `arm_A`):**
- **A-H1 (token-level):** corpus single-connective-delta hits = **`[[94, 5, 6, "فإن", "إن"]]`** — exactly
  one, = Q 94:5-6, the differing token being *فإن* (v 5) vs *إن* (v 6). **A-H1 = true.**
- **A-H2 (whole-string):** verse-string-B = verse-string-A with a single leading ف/و removed → hits =
  **`[[94, 5, 6]]`** — exactly one, = Q 94:5-6. **A-H2 = true.**

**Verdict: CONFIRMED (deterministic corpus-singleton).** Q 94:5-6 is the **only** place in the Quran where
two adjacent same-surah verses are identical except for a single leading connective fāʾ/wāw. This is the
exact textual datum on which al-Qurṭubī's *ibtidāʾ*-vs-*nasaq* reading rests (v 6's bareness of fāʾ marks
a fresh start) — see `05-classical-claims-audit.md` Claim 4.

---

## Q094-F-01 Arm B — Q 94:5-6 is the global minimum-edit-distance adjacent couplet (CONFIRMED)

**Hypothesis (pre-committed):** Q 94:5-6 is the tightest near-verbatim adjacent same-surah couplet in the
corpus by character (Levenshtein) edit distance, and this tightness is extreme vs a length-matched
random-pair null.

**Result (`csv/Q094-F-01.json` → `arm_B`):**
- **B-H1 (rank-1, edit=1):** over all **5,821** substantive (≥3-word) adjacent same-surah pairs, the
  minimum edit distance is **1**, achieved **uniquely** by Q 94:5-6 (rank-1 pairs = `[[94, 5, 6]]`).
  **B-H1 = true.**
- **B-H2 (no exact-verbatim adjacency):** count of exact-verbatim (edit-0) adjacent same-surah pairs (≥2
  tokens) = **0**. The Quran never places two byte-identical verses in immediate succession, so Q 94:5-6's
  edit-1 is as close to verbatim adjacency as the corpus ever comes. **B-H2 = true.**
- **B-H3 (permutation null, direction TIGHTER):** observed edit = 1; length-matched random-pair null
  (pool_a = 734, pool_b = 668) gives null-mean edit **12.83** (seed 20260509) / **12.81** (seed 20260530)
  — the observed is dramatically *tighter* than null. p_perm(edit ≤ 1) = **0.0003** (seed 1, 2/10000) and
  **0.0001** (seed 2, 0/10000), both < α_corrected = 0.05. Direction (TIGHTER) holds. **B-H3 = true.**

The ranked edit-distance table (the **MW-3 alternative-model** disclosure and **MW-6 in-corpus control**):
the runner-up family is the **edit-2** group — **Q 74:19-20, Q 75:34-35, Q 82:17-18, Q 102:3-4** — all
four are near-verbatim adjacent reprises with a *two*-character delta, none reaching edit-1. (Q 99:7-8 is
edit-3; Q 37:165-166, Q 56:39-40, Q 91:2-3 are edit-4.) Q 94:5-6 is alone at edit-1, two characters
tighter than its nearest competitor.

**Verdict: CONFIRMED (3/3).** Q 94:5-6 is the single tightest near-verbatim adjacent couplet in the entire
corpus, the corpus has zero exact-verbatim adjacencies, and the edit-1 is extreme against a length-matched
null at both seeds. This is the project's first per-surah landing of the **near-verbatim adjacent reprise**
structure.

---

## Q094-F-01 Arm C — the definite-ʿusr / indefinite-yusr orthographic asymmetry (CONFIRMED)

**Hypothesis (pre-committed):** the classical "one hardship, two eases" reading has an exact orthographic
correlate — *al-ʿusr* is written definite (الـ) in both v 5 and v 6 (one definite referent); *yusr* is
written indefinite (يسرا, alif-tanwīn, no article) in both (two indefinite referents); and the two verses
share a root-Jaccard of exactly 1.0 (the same proposition reprised).

**Result (`csv/Q094-F-01.json` → `arm_C`):**
- *العسر* present in v 5: **true**; in v 6: **true** (definite in both states).
- *يسرا* present in v 5: **true**; in v 6: **true** (indefinite, alif-tanwīn, in both states).
- v 5 roots = `["Esr", "ysr"]`; v 6 roots = `["Esr", "ysr"]`; **root-Jaccard = 1.0** (identical set;
  ʿ-s-r = Buckwalter `Esr`, distinct from ʿ-sh-r `E$r` "ten" per the §10.106 homograph guardrail).
  **C-H1 = true.**

**Verdict: CONFIRMED (orthographic asymmetry present).** The grammatical substrate of the *yusrayn*
reading (definite ʿusr repeated identically; indefinite yusr repeated; same root-proposition) is a genuine
textual fact, not an interpretive imposition. This is **descriptive only**: it does NOT adjudicate the
*theological* two-eases claim (out of scope, Protocol §10), nor does it favor Thaʿlab's reading over
al-Farrāʾ's *taʾkīd* reading or refute al-Jurjānī's *qawl madkhūl* objection — it verifies the asymmetry on
which all three classical positions operate (see `03-tafsir-survey.md`, `05-classical-claims-audit.md`).

---

## Bonferroni / family summary

Q094-F-01 has **k = 1 permutation cell** (B-H3); α_corrected = 0.05 / 1 = 0.05. The deterministic cells
(A-H1, A-H2, B-H1, B-H2, C-H1) are not permutation tests and do not consume α. For the Q 94 surah session
this is the single landed test, so no further cross-test correction is needed.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A-H1 | deterministic | single-connective hits = [Q94:5-6] only | PASS |
| A-H2 | deterministic | whole-string hits = [Q94:5-6] only | PASS |
| **A overall** | — | corpus-unique single-fāʾ adjacency | **CONFIRMED** |
| B-H1 | deterministic | min-edit = 1, unique = Q94:5-6 (of 5,821) | PASS |
| B-H2 | deterministic | exact-verbatim adjacencies = 0 | PASS |
| B-H3 | permutation (α=0.05) | obs 1 vs null 12.83; p 0.0003 / 0.0001 | PASS |
| **B overall** | — | global min-edit, extreme vs null | **CONFIRMED (3/3)** |
| C-H1 | deterministic | def-ʿusr ×2, indef-yusr ×2, J=1.0 | PASS |
| **C overall** | — | orthographic asymmetry present | **CONFIRMED** |

## MW protections applied

- **MW-1 (instrument-prior):** the single-connective-delta definition, the Levenshtein metric, the ≥3-word
  substantive filter, and the root-Jaccard were all fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** B-H3 used 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A reports BOTH the token-level (A-H1) and whole-string (A-H2)
  operationalizations; Arm B reports the full ranked edit-distance table (the edit-2 runner-up family).
- **MW-5 (replication):** A-H1, A-H2, B-H1, B-H2, C-H1 are deterministic and fully replicable from the
  no-tashkeel JSON + QAC root-index; B-H3 re-run at a second seed (20260530) gives p = 0.0001 (vs 0.0003),
  same direction and verdict.
- **MW-6 (instrument-control):** B-H3's length-matched random pool is the non-target control; the edit-2
  runner-up pairs (Q 74:19-20, Q 75:34-35, Q 82:17-18, Q 102:3-4) are the natural in-corpus control group
  (near-misses that did NOT reach edit-1).
- **MW-7 (post-hoc cap):** the reprise was noticed in close reading then promoted to direction-locked
  PRE-REGISTERED tests BEFORE computation; the single-test α=0.05 cap is respected.

## What the finding teaches (and its honest scope)

1. **A new rung on the repetition ladder.** H-NEW-2310's verbatim refrain census (24 intra-surah verbatim
   repeats) does NOT list Q 94:5-6, because the strings differ by the fāʾ. Q 94 adds a distinct repetition
   type — **near-verbatim adjacent reprise** — invisible to byte-exact refrain counting (links the
   project's within-verse reduplication H-NEW-2100 → verse-initial anaphora H-NEW-2140 → distributed
   verbatim refrain H-NEW-2310). The edit-2 runner-up family (Q 74/75/82/102) suggests a small corpus-wide
   class of "near-verbatim adjacent reprises" worth a corpus-wide census (queued Q094-F-02).
2. **The single character carries the exegetical weight.** The corpus-unique distinguishing feature of
   Q 94:5-6 — the leading fāʾ — is exactly what al-Qurṭubī reads as marking the *ibtidāʾ* of a "second,
   distinct ease." A one-grapheme delta is doing classical-exegetical work, and the empirical finding shows
   that delta is not just present but corpus-singular.
3. **Equal NULL prominence / honest scope.** All three arms passed cleanly; there was **no** pre-commit
   violation and **no** direction reversal in this test. The honest limit is the *scope*: Arm C verifies the
   grammatical asymmetry, NOT the theology of "two eases," and NOT the choice between the *taʾkīd* and
   *two-eases* schools — both of which the tradition itself debates (al-Jurjānī's objection). The finding is
   a structural/orthographic fact, not a theological adjudication.

## Honest limits

- Arm B's "tightest" is on the character-Levenshtein metric over space-stripped strings; a token-level or
  phoneme-level edit metric could re-rank the near-verbatim field, but the edit-1 vs edit-2 gap is robust
  to any reasonable character-level definition (the runner-ups differ by two characters, not one).
- Arm B's "≥3-word substantive" filter excludes very short verses; lowering it could admit shorter
  near-identical pairs (e.g. oath/refrain fragments), so the rarity is threshold-specific — but the
  exact-verbatim-adjacent count = 0 (B-H2) holds at the ≥2-token level too.
- B-H3's permutation pool matches verse length ±3 characters; a tighter or wider tolerance would shift the
  null mean slightly but cannot rescue an observed edit of 1 from a null mean near 13.

## Cross-finding integration

- **H-NEW-2310** (refrain census) — Q 94:5-6 is the near-verbatim complement the verbatim census omits; the
  new "near-verbatim adjacent reprise" rung.
- **H-NEW-2100 / H-NEW-2140** — within-verse reduplication / verse-initial anaphora; Q 94:5-6 is *inter*-verse
  near-verbatim reprise — a third repetition mode.
- **H-NEW-2350 / H-NEW-2380** (exact- and near-twin verses are same-period phenomena) — Q 94:5-6 is an
  *intra*-surah (single-surah) reprise, the limiting case of "same period"; complements the *inter*-surah
  twin census.
- **H-NEW-2280** (munāsabah-seam) — the Q 93 → Q 94 consolation-pair seam (rank 10/113) is the adjacency
  correlate of the surah's consolation register (see `01-empirical-profile.md`, `05-claims-audit` Claim 6).
- **§10.106 homograph guardrail** — Arm C's `Esr` (ʿ-s-r) vs `E$r` (ʿ-sh-r) distinction follows the
  same root-disambiguation discipline established in the number-word census.

---

*Computed 2026-05-30, seed 20260509 (replicated 20260530), 10,000 perms, SHA-locked pre-reg verified at
runtime ("SHA OK: 2dd9380…f71d2a"). Script: `scripts/Q094_F_01_usr_yusr_reprise.py`; JSON: `csv/Q094-F-01.json`.*
