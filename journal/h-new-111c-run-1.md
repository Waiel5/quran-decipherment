# Journal: H-NEW-111c — Fisher-Rao on verse-length histograms, run 1

**Date**: 2026-04-17
**Specialist**: h-new-111c-specialist
**Seed**: 20260417
**Pre-reg SHA-256**: `ab350056a658e48588cc0bb7b561ed6bd649371336405876a6e2667ccf2bbcf7`

## Timeline

1. Read HANDOFF/04-DISCIPLINE.md, parent h-new-111 findings + pre-reg.
2. Located parent script `scripts/h_new_111_fisher_rao_mushaf.py` — used as
   template.
3. Noted h-new-111b is a parallel replication (char-4-grams); this is the
   SECOND of two orthogonal replications.
4. **Pre-reg written BEFORE any computation** (no histogram inspection).
   - Bin edges locked as `[1,5,10,15,25,40,60,100,∞]`, 8 bins.
   - Bonferroni family = h-new-111c-verse-length-hist, k=3, α_bon=0.0167.
   - **Garden-of-forking-paths disclosed upfront**: this feature is less
     orthogonal to Uthmanic length-sorting than char-4-grams; the mushaf's
     mufaṣṣal long-to-short structure may mechanically produce a "pass"
     that does not reflect deep information-geometric optimality.
   - Sanity anchors `L_length_sorted_asc/desc_by_nverses` and
     `L_mean_verselen_sorted_asc/desc` added pre-hoc to specifically test
     the confound.
5. Script written after pre-reg locked.
6. Run on 2026-04-17 — results:
   - L_mushaf = 77.655
   - Null: mean 138.15, sd 6.15, min 113.83; z = −9.84; p = 1×10⁻⁴ (PASS primary)
   - L_2opt_best = 28.70; ratio = 2.71 (FAILS pre-reg <1.2 band, also
     outside <2.0 band)
   - L_nold = 61.71, L_tanzil = 95.34; sign REVERSED (mushaf LONGER than
     Nöldeke on rhythm axis, opposite of parent H-NEW-111).
   - MW-5: p = 1×10⁻⁴ (PASS)
   - Sanity anchors: mean-verse-length sorted (L≈52) beats mushaf (77.66)
     decisively; #verses sorted (L≈111) is worse than mushaf.

## Honest surprise

Expected behavior under mechanical confound: mushaf ≈ length-sorted.
OBSERVED: mushaf is CLEARLY NOT a length-sort (it's much better than sort-
by-nverses and much worse than sort-by-mean-verse-length). So the mushaf
ordering carries SOME rhythmic information, but not enough to be either
TSP-near-optimal on rhythm OR to beat Nöldeke chronology on rhythm.

**Interpretive conclusion** (written post-result, flagged as such):
rhythm and root axes are measuring genuinely different aspects of surah-
level structure. H-NEW-111's claim that mushaf is near-optimal on roots
is NOT just Uthmanic length-sorting in disguise, because if it were, this
test — which IS influenced by length — should have replicated the 1.1
ratio. It got 2.7 instead.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-111c-prereg.md`
- Script: `scripts/h_new_111c_fisher_rao_verselen.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-111c.json`
- Findings: `findings/phase-b-hypotheses/h-new-111c-fisher-rao-verselen.md`

## No amendments to pre-reg after view

All thresholds and directions were locked in the pre-reg frontmatter
BEFORE the script ran. The observed ratio (2.71) is reported against the
pre-registered band and explicitly labeled as failing it; no threshold
loosening. This is compliant with PRE-REG-STANDARD-01/04 and the
Bonferroni asymmetry rule.

## Next steps

- Await h-new-111b result. If 111b is clean, parent H-NEW-111 can promote.
- If both replications behave unexpectedly, flag the whole family to
  team-lead for rethinking.
