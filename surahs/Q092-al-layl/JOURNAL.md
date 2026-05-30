---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 92 al-Layl — Investigation Journal

## 2026-05-30 — full 8-file deep-dive (two-session landing; completion pass)

**Session structure.** A prior pass (timestamps ~00:11–00:18) wrote 00-overview, 01-empirical-profile,
02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, the Q092-F-01 pre-reg, the script, and the
csv/Q092-F-01.json, then stalled before finishing 05/06/07/JOURNAL or committing. This completion pass
re-verified the test and wrote the four missing files. No prior complete file was rewritten.

**Pre-flight (in order):**
1. Read the quran-investigation SKILL.md.
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. `ls surahs/Q092-al-layl/` + read every existing file (00–04, pre-reg, script, csv/Q092-F-01.json).
4. Referenced exemplar `surahs/Q066-al-tahrim/` (05/06/07/JOURNAL structure, depth, tone).

**Data re-verification (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` id 92 → `total_verses = 21`; type Meccan. Verified.
- `data/revelation-order.csv` mushaf_order 92 → Meccan, revelation_order #9, Nöldeke #10, Early Meccan.
- `data/hafs-verse-counts.tsv` mushaf-92 → 21.
- **h-new-111.json** (FR): Q 92 mean FR 0.8438; nearest Q 111 (0.4060); Q 93 rank 4 (0.4338), Q 91 rank 13
  (0.4734); farthest Q 4 (1.299). Reconstructed from `D_matrix_upper_triangular` (1-indexed). Matches 01.
- **h-new-720.json** (TSP): Q 91 → Q 92 delta_raw −0.08683, ascending-rank **1/113** (cheapest seam in the
  mushaf); Q 92 → Q 93 +0.06063, rank 55/113. Recomputed ascending ranks directly. Matches 01/07.
- **h-new-1820** + `csv/h-new-1820.json`: title-density-independence law (47/89 eponymous surahs not rank-1).
- **h-new-2360** (`h-new-2360-antithesis-law.md` + ledger §10.103): antithesis-pairs share MORE content
  (z=+13.0, jadal); the "disjoint-content" candidate law REJECTED; Q 83 showcases were hand-picked rarities.
- **Q083-F-01** (ledger §10.99) + **Q098-F-01 Arm D** (ledger) read for the muqābala-overlap network context.

**Tafsīr re-read in Arabic from disk (for 05-claims-audit):**
- al-Qurṭubī `ar-tafseer-al-qurtubi/92/{1,5,6,17,19}.json`: 92:1 *makkiyya … 21 āya bi-l-ijmāʿ*; 92:5 Abū
  Bakr (Ibn Masʿūd + ʿāmmat al-mufassirīn) + the *khalaf/talaf* angel ḥadīth (Muslim, Abū Hurayra); 92:6
  *bi-l-ḥusnā* = *lā ilāha illā Allāh* / Jannah / al-khalaf (multiple readings); 92:17 al-atqā = Abū Bakr
  (Ibn ʿAbbās); 92:19 the Bilāl-manumission sabab (ʿAṭāʾ + al-Ḍaḥḥāk ← Ibn ʿAbbās).
- al-Ṭabarī 92.json ayah 4: v 4 = *jawāb al-qasam* (Qatāda), *shattā = mukhtalif*.
- **Data-correction logged:** NO orchard-owner sabab on disk for Q 92 (that occasion is Q 68 al-Qalam
  *aṣḥāb al-janna*). Q 92's on-disk asbāb are Abū-Bakr-giving + Bilāl-manumission. Flagged honestly in 05.

**Pre-registration (Q092-F-01) — LOCKED BEFORE COMPUTATION (prior session):**
- Pre-reg `Q092-F-01-giver-miser-antithesis-prereg.md`.
- SHA-256 `6e41fd080525daf5d638f84416339584e3bd6143da457850afc75363d01981b8`, embedded as EXPECTED_SHA.
- Seed 20260509; replication seed 20260601; 10,000 perms.
- Three arms: A = content-overlap permutation (direction LOCKED OVERLAP-positive to the H-NEW-2360 prior);
  B = frame-vs-pole decomposition (deterministic); C = title-density-independence *lyl*-rank (deterministic).

**Computation (completion pass re-ran the script; `csv/Q092-F-01.json` rewritten identically):**
- Runtime SHA check: `[ok] pre-reg SHA verified: 6e41fd0805…01981b8` — PASS (fail-fast not triggered).
- **Arm A:** G = {ETw, Hsn, Sdq, wqy, ysr}; M = {Esr, Hsn, bxl, gny, k\*b, ysr}; shared {Hsn, ysr};
  **J = 0.2222**; null-mean 0.03416, std 0.07108, n_ge 326/10000, **z = +2.646, p_upper = 0.0327**;
  replication seed 20260601 p = 0.0329. Direction OVERLAP-positive — matches lock. pre_commit_violation = False.
  **CONFIRMS H-NEW-2360 overlap.**
- **Arm B:** shared {Hsn, ysr} ⊆ frame {Hsn, ysr} = True; giver-poles {ETw, Sdq, wqy} ∩ miser-poles
  {bxl, gny, k\*b} = ∅ = True; frame in both = True. **PASS (frame-driven).**
- **Arm C:** *lyl* = 92 attestations across 49 surahs; rank-1 = Q 2 (5×); Q 92 count 1, **rank 48/49**.
  **CONFIRMS H-NEW-1820.**

**Decision point.** Arm A's locked OVERLAP-positive direction held (z = +2.65, no pre-commit violation);
no garden-of-forking-paths shift — the analysis matched the pre-reg exactly. Arm A's p = 0.033 clears
α = 0.05 but is reported as a *showcase-scale confirmation* of H-NEW-2360, not a standalone law-strength
result (the corpus law is H-NEW-2360 itself, z = +13.0). Equal-NULL prominence honored throughout (the
finding is positive, but the limits section flags the small-N single-surah scale and the 2-of-9 shared-root
driver). The deterministic Arms B and C are reported with full mechanism (frame/pole partition; raw *lyl*
counts).

**Files produced this pass:** 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL
(this). Prior-pass files (00–04, pre-reg, script, csv) left intact; script re-run only to re-verify SHA +
result. csv/Q092-F-01.json regenerated byte-stable.

**Verdict:** Q092-F-01 = **CONFIRMED (3/3)** — Arm A CONFIRMS H-NEW-2360 (giver/miser muqābala is frame-driven
content-OVERLAP, z = +2.65, p = 0.033) + Arm B PASS (frame-driven) + Arm C CONFIRMS H-NEW-1820 (Q 92 rank
48/49 in *lyl*). Q 92 is the overlap-positive mirror of the Q 83 disjoint showcase and the third independent
confirmation of the jadal-overlap law.

**Queued follow-ups:** (a) lemma/surface-level robustness re-test of Arm A; (b) formal corpus-wide promotion
of the muqābala-overlap network (Q 92 ✓ overlap, Q 83 ✗ disjoint, Q 98 ✓ overlap) as a per-finding map under
H-NEW-2360; (c) the Q 91→Q 92 rank-1 seam as a positional anchor for an early-Meccan cohesion-block study.
