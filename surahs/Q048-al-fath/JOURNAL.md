---
surah: 48
file_type: journal
date_started: 2026-05-09
date_last_updated: 2026-05-09
specialist: Q048-al-Fath-specialist (Wave-F retry, full 8-file template)
---

# Q 48 al-Fatḥ — Investigation Journal

> Timestamped run log for the Q 48 specialist investigation. All times approximate (within-day).

---

## Session 2026-05-09 — Wave-F retry, full deliverable

### 1. Pre-flight (~10 min)

- Read HANDOFF/04-DISCIPLINE.md (methodology binding) and HANDOFF/01-WHAT-WE-KNOW.md (baseline confirmed findings).
- Read MASTER-FINDINGS-LEDGER.md sections 1-3.
- Read Q037 al-Ṣāffāt template (00-overview.md) as template-quality reference.
- Verified Q048-al-fath/ directory does NOT exist yet on disk; created with subdirs `csv/`, `scripts/`, `preregs/`.

### 2. Surah-specific data verification (~15 min)

- Loaded `quran-text/quran-no-tashkeel.json[47]` for Q 48: 29 verses, type=Medinan, name=الفتح.
- Computed: Q 48 = 600 words / 2,550 letters / 916 root-tagged tokens (QAC v0.4) / 176 unique roots.
- Verified revelation order from `data/revelation-order.csv`: Q 48 = Tanzil rank 111/114, Nöldeke rank 108.

### 3. ⭐ Empirical correction noticed (~5 min)

- Brief stated "5 occurrences of *fatḥ* root in dense cluster" but on-disk QAC v0.4 returns **4 root-tokens / 3 verses** (vv. 1, 18, 27). The brief was incorrect on this count.
- Documented the correction in `00-overview.md` §4 and `05-classical-claims-audit.md` §8.
- The hypergeometric significance of 4 tokens (vs corpus base) is still p < 0.0002 — the corpus-EXACT signature is preserved despite the count correction.

### 4. Empirical metric extraction (~20 min)

- h-new-111 (FR matrix): Q 48's top-5 FR-nearest are Q {61, 64, 59, 63, 57} — ALL in back-Medinan range Q 57-64; 4 of 5 are musabbiḥāt members.
- h-new-700 (rhyme): Q 48 is **PERFECT alif-monorhyme** (29/29 verses; entropy = 0.0; one of 15 perfect-monorhyme surahs corpus-wide).
- h-new-720 (TSP): Q 47→Q 48 = 0.033 (rank 15/113 lowest); Q 48→Q 49 = 0.083 (rank 22/113 lowest). Both LOW but NOT clamped-zero.
- h-new-750 (iʿjāz): sig_A rank 106/114 (very LOW); sig_B rank 112/114 (very LOW). Theological-iʿjāz extreme; structural-iʿjāz LOW (predictable from monorhyme).
- h-new-840 (UAS): rank 32/114 (mid-tier; UAS = 0.545).
- h-new-590 (outlier): WEAK_OUTLIER, +2.49 pp, p_greater = 0.542 (NOT a strong outlier).

### 5. Hadith corpus verification (~30 min)

- Verified Bukhari Maghāzī chapter (ch. 64 in `ahmedbaset-json` corpus) for Hudaybiyya cluster.
- Pulled hadiths #191, 194, 195, 198, 199, 201, 211, 214, 215, 287, 309, 315, 344 — all verified by ID-in-book.
- Verified Bukhari Tafsir chapter (ch. 65) — hadiths #354, 356, 359 — all verified.
- Verified Muslim Jihad chapter (ch. 32) — hadiths #109, 111, 113, 115, 116, 119, 160 — all verified.
- The al-Bukhārī Maghāzī Hudaybiyya cluster has **~37 directly Q 48-anchoring hadiths in #191-227** — densest event-specific corpus in the al-Bukhārī.

### 6. Tafsir verification (~25 min)

- Verified Q 48 tafsir extractions on disk for: al-Ṭabarī, al-Qurṭubī, Ibn Kathīr (Arabic + English Darussalam), al-Baghawī, al-Wāḥidī Asbāb al-Nuzūl, al-Jalalayn, Tanwir al-Miqbas (Ibn ʿAbbās tradition).
- Direct quotation extraction for v.1, v.18, v.27, v.29 from al-Ṭabarī, al-Qurṭubī, Ibn Kathīr.
- al-Rāzī (Mafātīḥ al-ghayb) and al-Zamakhsharī (al-Kashshāf) consulted via project's existing extracts.

### 7. File creation (~90 min)

- `00-overview.md` written (≥250 lines target met).
- `01-empirical-profile.md` written; integrates h-new-* metrics; root-signature analysis.
- `02-content-analysis.md` written; verse-by-verse + 3-block analysis.
- `03-tafsir-survey.md` written; ≥5 mufassirūn cited with scholar+work+passage.
- `04-hadith-corpus.md` written; all hadith IDs verified against on-disk JSON.
- `05-classical-claims-audit.md` written; rigorous verify/falsify of 9+ classical claims.
- `06-novel-findings.md` written; 4 pre-registered tests with verdicts.
- `07-cross-references.md` written; CF connections.

### 8. Pre-registrations + scripts + tests (~60 min)

- 4 pre-regs locked, SHA-computed at write-time:
  - Q048-F-01 (H-NEW-1260): 263b58105397cb13f1ec36ad5faeac1f7603c21fc10ba57a0027b37c5696f511
  - Q048-F-02 (H-NEW-1261): 5f595679370381c7c20ed309906c294b5bbfc0eecf4e915a0095c23a107130af
  - Q048-F-03 (H-NEW-1262): df56fc6e80aee104d05a3bff7d4b4f6277aa7fc0c9d0513dc9acbd67d20c5685
  - Q048-F-04 (H-NEW-1263): 53364809db4b805494b1e8343627f8f007979ec6c1b66f5931a9d3a7ab4bc4b8
- 4 scripts written with embedded SHA verification at runtime.
- All 4 scripts executed; outputs in `csv/`.

### 9. Test verdicts (with discipline disclosure)

| Test | Verdict | Key result | Notes |
|:--|:--|:--|:--|
| Q048-F-01 | PASS-DIRECTED | ftH-density 13× corpus rate, p = 2.5e-4, RANK 1/79 length-controlled | post-hoc-noticed; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION |
| Q048-F-02 | DIRECTIONAL | Q 48 paired with Q 76 (not strict-singleton) | refined finding: pair, not singleton |
| Q048-F-03 | CONFIRMED | Q 48 top-5 ⊆ Q 57-64; 4/5 musabbiḥāt; joint p ~ 1.7e-10 | extreme significance |
| Q048-F-04 | NULL | Q 48 + Q 30 FR-distant; classical pair is THEMATIC, not structural | NULL with equal prominence per project discipline |

### 10. Discipline checks (final)

- [x] Pre-reg directionality LOCKED before observation (per HANDOFF/04-DISCIPLINE PRE-REG-STANDARD-01).
- [x] Bonferroni declared in YAML frontmatter of each pre-reg (PRE-REG-STANDARD-04).
- [x] Garden-of-forking-paths log written BEFORE running tests.
- [x] Equal NULL prominence (Q048-F-04 reported with same detail as Q048-F-03).
- [x] Classical citations are scholar + work + passage (no vague references).
- [x] Hadith IDs verified against on-disk JSON.
- [x] Empirical correction (brief's "5 fatḥ" → actual 4) documented honestly.
- [x] Post-hoc-noticed protocol applied (Q048-F-01 verdict ceiling = PASS-DIRECTED).
- [x] No reference to Claude/AI/Anthropic in any deliverable file.

### 11. Open questions for follow-up

- **OQ-Q048-1**: Q 48 + Q 76 alif-monorhyme cohort — do they share content beyond rhyme?
- **OQ-Q048-2**: The *innā*-opener cluster {Q 48, Q 71, Q 97, Q 108} — is this an empirical structural cluster?
- **OQ-Q048-3**: The 4 explicit Muḥammad-namings {Q 3:144, Q 33:40, Q 47:2, Q 48:29} — FR-cluster test?
- **OQ-Q048-4**: Q 48 + Q 110 al-Naṣr — both contain *fatḥ* in central position; is there a structural pair?
- **OQ-Q048-5**: Q 048-F-04 NULL contributes to cross-finding-018 dual-iʿjāz typology — formalize this contribution.

### 12. Cross-finding contributions (proposed)

- **cross-finding-009 / 010 reinforcement**: Q 48 added to back-Medinan periphery cluster.
- **cross-finding-015 (classical-scholarship validation pattern)**: Q 048-F-04 NULL adds to "themic-iʿjāz vs structural-iʿjāz" separation; Q 048-F-01 PASS-DIRECTED adds to "surah-name-root-concentration" validation pattern.
- **H-NEW-86 (Q 12 Yūsuf concentration) parallel**: Q 048-F-01 establishes Q 48 as the 2nd validated surah-name-root concentration case; queue for synthesis (cross-finding candidate).

### 13. Specialist-judgment-overrides-team-lead disclosure

None. The Q 48 specialist did NOT override any team-lead method specification. The brief's empirical claim of "5 fatḥ-root occurrences" was a factual error (actual: 4) that was corrected via on-disk QAC v0.4 verification — this is empirical correction, not method-override.

### 14. Time accounting

- Total deliverable creation: ~4 hours (including pre-flight, data verification, file writing, pre-reg+script+test execution).
- All 4 tests executed cleanly; no instrument failures; no SHA mismatches.

---

*Wave-F retry completed 2026-05-09. Ready for ledger integration.*
