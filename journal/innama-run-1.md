# Journal — innamā run 1

Date: 2026-04-12
Agent: Phase-B, innamā-formula task.

## Approach

Target: map the إنما (innamā) restrictive-emphatic particle across the Qurʾān.

Initial challenge: the Dukes morphology has no `<in~amaA` or `innamā` lemma. I first searched for a combined form and got zero hits; the breakthrough was inspecting 36:82 (kun fa-yakūn, given as a reference verse) and observing that innamā is segmented into *two* successive tokens:

- `<in~a` (POS=ACC, the emphatic accusative particle)
- `maA` or `maA^` (POS=PREV, the preventive "mā al-kāffah")

This faithfully reflects classical grammatical analysis (Sībawayh, Ibn Hishām) — innamā is not a simplex particle but a compound inna+kāff mā, in which the mā *prevents* inna's case-assignment while preserving its emphatic force.

## Extraction

Single awk pass over `data/morphology/quranic-corpus-morphology-0.4.txt` tracking (loc, form, tag) sliding window; emit the location whenever current row is POS=PREV AND previous row is POS=ACC AND previous form is `<in~a`.

**Result: 143 tokens / 134 unique verses.**

Side-benefit: the same mechanism found 11 `>an~a` + PREV (annamā) and 6 `ka>an~a` + PREV (ka-annamā), completing the triad. Also captured two non-innamā PREV cases: `rubbamā` (15:2) and `mimmā` (71:25), which I filtered out.

## Validation against scholar's claims

1. **~150 estimate** → actual 143 for innamā proper, 160 if pooling the -annamā family. ✓
2. **innamā al-muʾminūn in 8:2, 9:71, 23:1, 49:10, 49:15** → only 3 of the 5 contain innamā. 9:71 uses `wa-l-muʾminūn wa-l-muʾminātu...` (no restriction particle); 23:1 uses `qad aflaḥa l-muʾminūn` (emphatic particle qad + perfect). ✗ (partial)
   - But I found a fourth that the scholar missed: **24:62** *innamā al-muʾminūna alladhīna āmanū bi-llāhi wa-rasūlih*. ✓ (augmented)
3. **Q 36:82 kun fa-yakūn** → confirmed; the most emphatic of 6 innamā-introduced kun-verses (only one using *amruhu*, only one with *idhā arāda shayʾan*). ✓
4. **Q 35:28 yakhshā** → confirmed as sole instance of innamā + khashya-of-Allāh (79:45 has yakhshāhā referring to the Hour). ✓
5. **Q 33:33 yurīdu Llāhu li-yudhhiba** → confirmed; unique among yurīd-innamā triplet as the only *positive purgation* instance (others are punitive: 9:55, 9:85). ✓
6. **innamā amthāluhum ka-mathal parable formula** → innamā *rarely* opens parables (only 10:24). The counter-factual ka-annamā handles 5 of the 6 Qurʾānic "as if" similes. Worth noting the scholar phrased this as a "parable formula" but it's actually *not* a common innamā-use. ✓/rebalanced
7. **innamā vs mā...illā** → 558 RES-tokens vs 143 innamā. Innamā is ~1/4 as frequent; grammatical preference confirms Zamakhshariī's pragmatic distinction. ✓
8. **Theological-restriction concentration** → confirmed quantitatively:
   - Meccan density 18.6/1k, Medinan 35.1/1k — **1.88× Medinan preference**.
   - Top density surahs: 16 (An-Naḥl) 8.6%, 29 (ʿAnkabūt) 7.2%, 9 (Tawbah) 7.0%.

## Surprising findings (not in scholar's prompt)

- **Double-innamā verses: 9 total**, almost all marking chiastic antitheses (guidance/misguidance pairs in 10:108, 17:15, 27:92; signs/messenger in 29:50 and 67:26). This is a structural marker deserving its own investigation.
- **18:110 and 41:6 nest innamā + annamā** ("qul innamā anā basharun...yūḥā ilayya annamā ilāhukum ilāhun wāḥid") — two restrictions scoped at different levels.
- **Messenger-role cluster (8 verses) is statistically the largest identifiable theme** — "qul innamā anā" is the formulaic prophetic self-denial.
- **Purification 33:33 is theologically unique** among 143 innamā: the only verse with [innamā + yurīd Allāh + positive purification verbs (yudhhib + yuṭahhir)]. This semantic isolation (not a grammatical claim) explains why the verse is load-bearing in Shīʿī theology — there is *literally no other verse* combining those elements.

## Open questions / follow-ups

- Intersection with Nöldeke chronology: does the messenger-role cluster date to a specific Meccan period?
- Cross-reference with chiasm-detector output on the 9 double-innamā verses.
- Density comparison with iltifat and rhetorical questions: is innamā density correlated or anti-correlated with them per-surah?
- Discrete check: are there verses morphologically tagged ACC+PREV but read as *something other* than innamā by some qirāʾa?

## Artifacts produced

- `findings/phase-b-hypotheses/innama-formula.md` — main analysis (~2500 words).
- `findings/phase-b-hypotheses/csv/innama-verses.csv` — 134 rows, machine-readable.
- This journal.

## Time & method notes

- Total tool calls: ~20.
- Primary bottleneck: unicode text matching for thematic classification — Arabic diacritics required normalization pass before substring matching worked.
- Data trust: Dukes morphology is the gold standard for syntactic segmentation; I accepted its ACC+PREV analysis without dispute.
