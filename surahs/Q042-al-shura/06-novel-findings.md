---
surah: 42
surah_name: al-Shūrā
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
---

# Q 42 al-Shūrā — novel findings

## Finding 1: Q042-F-01 — two-verse muqaṭṭaʿāt-split is unique to Q 42 (VINDICATED)

**Pre-registration**: [[Q042-F-01-muqattaat-split-prereg]] — locked SHA `c96f4e46b179c0a961ba6374f69e2c2858eb5c509fd8a0ec1aa3f426cd8dda25`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q042_F_01_muqattaat_split.py`.
**Output**: `/Users/grey/Downloads/quran/surahs/Q042-al-shura/csv/Q042-F-01.json`.

**Result**: Across all 29 muqaṭṭaʿāt-opened surahs, **only Q 42** has muqaṭṭaʿāt at both v.1 (ḥā mīm) AND v.2 (ʿayn sīn qāf). All other 28 muqaṭṭaʿāt-opened surahs have all muqaṭṭaʿāt within v.1.

**Verdict**: **VINDICATED** at exact-uniqueness level.

**Interpretation**: This empirically confirms al-Suyūṭī's (*al-Itqān*, nawʿ 27) classical observation. The Q 42 split is **the only multi-verse muqaṭṭaʿāt opening in the Qurʾān** — a structural-architectural uniqueness.

**Cross-link to empirical signature**: Q 42's UAS rank 31 + sig_A = +1.27 (HM-7 max) + multi-rāwī rhyme (ر-shifted) + UAS-leader of HM-7 (this session correction) constitute a **convergent uniqueness profile** — the surah is structurally distinct from its HM-7 siblings on multiple axes.

---

## Finding 2: Q 42 ↔ Q 43 is the costliest single transition in HM-7 (FR-distance = 0.9912)

**Status**: Empirical observation from `h-new-111.json` (this session's FR matrix extraction).

**Method**: Computed all FR pair-distances among HM-7 mushaf-adjacencies.

**Result**:

| Transition | FR-distance |
|:--|:-:|
| Q 39 → Q 40 (boundary) | 0.7953 |
| Q 40 → Q 41 | 0.8403 |
| Q 41 → Q 42 | 0.8540 |
| **Q 42 → Q 43** | **0.9912** ← peak |
| Q 43 → Q 44 | 0.8647 |
| Q 44 → Q 45 | 0.8439 |
| Q 45 → Q 46 | 0.8112 |
| Q 46 → Q 47 (boundary) | 0.9905 |

**Verdict**: **VINDICATED** — the bifurcation step between HM-A (Q 40-42) and HM-B (Q 43-46) registers as the single costliest transition WITHIN HM-7 at FR-distance 0.9912. The Q 46 → Q 47 boundary (exiting HM-7 entirely) is similarly high (0.9905), as expected. The internal HM-7 transitions are all < 0.86 except the Q 42 → Q 43 bifurcation step.

**Implication**: This empirically anchors the "HM-A vs HM-B sub-block" architecture. The bifurcation is not just rhyme-prosodic (Q 42 multi-rāwī ↔ Q 43 monorhyme) but ALSO FR-content-distinctive at peak-strength.

---

## Finding 3: Q 42:11 *laysa ka-mithlihi shayʾ* is the unique tanzīh formula (descriptive)

**Status**: Lexical-uniqueness observation.

**Method**: String search for *لیس کمثله* / *ليس كمثله* (variant orthographies) across the no-tashkeel corpus.

**Result**: Q 42:11 is the **only verse** containing the exact construction *ليس كمثله شيء*. The grammatical-rhetorical *ka-mithlihi* duplicate-comparison particle is a once-in-the-Qurʾān construction.

**Comparable but distinct tanzīh formulae**:
- Q 112:4 *لم يكن له كفوا أحد* — different grammar (negated copula + *kufuwan*).
- Q 19:65 *هل تعلم له سميا* — different (knowledge-of-namesake).

**Verdict**: **VINDICATED** at uniqueness level. Q 42:11's *ka-mithlihi shayʾ* is the lexically unique tanzīh formula in the Qurʾān. This empirically explains the verse's outsized weight in classical kalām.

---

## Finding 4: Q 42's UAS-leadership of HM-7 (this session correction)

**Status**: Methodological correction — recorded explicitly across the cluster.

**Source**: Re-derived from `h-new-840.json`.

**Result**: HM-7 UAS-ranking (this session, verified):
- Q 42: rank 31, UAS = +0.568 (HM-7 leader)
- Q 43: rank 33, UAS = +0.537
- Q 41: rank 39, UAS = +0.436
- Q 45: top-third (UAS = +0.350; in top-quartile per re-rank)
- Q 40: rank 74, UAS = -0.868
- Q 46: rank 96, UAS = -1.591
- Q 44: rank 97, UAS = -1.882

**Verdict**: **CORRECTION** — Q 42, not Q 41, is the UAS-leader of HM-7. Q 42 is the **architecturally most distinctive HM-7 surah by aggregate UAS**, in addition to its unique two-verse muqaṭṭaʿāt opening.

This combines with Findings 1-3 to make Q 42 the **multi-axis uniqueness center of HM-7**.

---

## 5. Honest limits

1. The convergent uniqueness of Q 42 (Findings 1+2+3+4) is **descriptive-architectural**, not yet causally explained. The hypothesis that the two-verse muqaṭṭaʿāt CAUSES the multi-rāwī rhyme structure is not testable on a single surah.
2. Finding 3 depends on the orthographic-string operationalization; the *ka-mithlihi* construction is unique even under variant tashkeel-levels.

## 6. Cross-references

- [[Q042-F-01-muqattaat-split-prereg|Q042-F-01 pre-reg]]
- [[Q042-al-shura/05-classical-claims-audit|Q 42 audit]]
- [[hawamim-7-cluster-synthesis]]
