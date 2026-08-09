#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-NEW-3040 POST-HOC DIAGNOSTICS — every number here is POST-HOC and carries the
MW-7 single-test cap (alpha = 0.05, no confirmatory weight). It exists to answer
questions raised BY the primary run, not to establish anything.

Writes to its OWN run directory. The primary run directory is never touched.

  D1. Is RT-5 a tautology?  Do the bounded contrast and the smoothed log-ratio induce
      the identical ranking of the 114 surahs?  (STANDING RULE 4: check every control
      for tautology.)
  D2. Is RT-2 informative for H2?  It changes only the register labels, which H2 does
      not use.
  D3. How much of rho(M, R) is length?  Product-of-loadings estimate vs the measured
      partial.
  D4. THE OATH TAUTOLOGY.  8 of the 28 Neuwirth-Sinai eschatological surahs carry
      "oath" in their own genre label, and jawab al-qasam takes the emphatic lam,
      which is 59.4% of the epistemic pole.  Re-run H1 with those 8 removed.
  D5. Which E-component drives H1?  Leave-one-component-out on the epistemic pole.
  D6. Is the l:EMPH prefix concentrated in oath surahs?
"""
import os, re, csv, json, math, random, hashlib, collections, datetime

ROOT = "/Users/grey/Downloads/quran"
SCRIPTDIR = os.path.join(ROOT, "findings/phase-b-hypotheses/scripts")
import importlib.util
spec = importlib.util.spec_from_file_location("h3040", os.path.join(SCRIPTDIR, "h-new-3040.py"))
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)

SEED, N_PERM = h.SEED, h.N_PERM
S = list(range(1, 115))

stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3040", stamp + "-posthoc")
os.makedirs(rundir, exist_ok=False)
print("[posthoc run] %s" % rundir)

word_segs, verse_words, nseg = h.load_qac()
wordcount = collections.Counter(); versecount = collections.Counter()
for (s, v, w) in word_segs: wordcount[s] += 1
for (s, v) in verse_words: versecount[s] += 1
RAW = {int(k): v for k, v in json.load(open(h.J2530))["raw_feature_vectors"].items()}
lwc = [math.log(wordcount[s]) for s in S]

D, E, cens, cens_s, tag_tot = h.build_modality(word_segs, h.W_PRIMARY, True)
M_log = [h.contrast_log(D, E, s) for s in S]
M_bnd = [h.contrast_bounded(D, E, s) for s in S]
matB = [[RAW[s][f] for f in h.CF028_FEATS_B] for s in S]
matA = [[RAW[s][f] for f in h.CF028_FEATS_A] for s in S]
R_B, _, _ = h.pc1(matB, h.CF028_FEATS_B, "f_qalu")
R_A, _, _ = h.pc1(matA, h.CF028_FEATS_A, "f_qalu")
leg, esc = h.load_labels_neuwirth()

out = collections.OrderedDict()
out["header"] = ("POST-HOC. MW-7 single-test cap alpha=0.05. No number here has "
                 "confirmatory weight. Primary run directory untouched.")

# ---- D1: RT-5 tautology -------------------------------------------------
r_log, r_bnd = h.ranks(M_log), h.ranks(M_bnd)
ident = (r_log == r_bnd)
ndiff = sum(1 for i in range(114) if abs(r_log[i] - r_bnd[i]) > 1e-9)
out["D1_RT5_tautology"] = {
    "rankings_identical": ident, "n_surahs_with_different_rank": ndiff,
    "spearman_between_the_two_forms": round(h.spearman(M_log, M_bnd), 8),
    "conclusion": ("RT-5 is NOT an independent robustness arm: the bounded contrast and "
                   "the smoothed log-ratio induce the identical ranking, so every rank "
                   "statistic is identical by construction."
                   if ident else "RT-5 is a genuine variation of the ranking."),
}
print("D1 RT-5 identical ranking: %s (%d surahs differ, rho=%.8f)"
      % (ident, ndiff, h.spearman(M_log, M_bnd)))

# ---- D2: RT-2 and H2 ----------------------------------------------------
out["D2_RT2_scope"] = {
    "conclusion": ("RT-2 changes only the register labels. H2 uses all 114 surahs and no "
                   "label, so RT-2's H2 numbers are identical to RT-1's BY CONSTRUCTION "
                   "and are not evidence of robustness for H2. RT-2 is a robustness arm "
                   "for H1 only."),
}

# ---- D3: how much of rho(M,R) is length? --------------------------------
d3 = collections.OrderedDict()
for arm, R in (("ARM_B", R_B), ("ARM_A", R_A)):
    rm = h.spearman(M_log, lwc); rr = h.spearman(R, lwc)
    marg = h.spearman(M_log, R); part = h.partial_spearman(M_log, R, [lwc])
    d3[arm] = {
        "rho_M_logWC": round(rm, 6), "rho_R_logWC": round(rr, 6),
        "product_of_loadings": round(rm * rr, 6),
        "rho_marginal": round(marg, 6), "rho_partial_logWC": round(part, 6),
        "share_of_marginal_removed_by_logWC": round(1 - part / marg, 6) if marg else None,
    }
    print("D3 %s: marginal=%+.4f  product-of-loadings=%+.4f  partial=%+.4f  (%.1f%% removed)"
          % (arm, marg, rm * rr, part, 100 * (1 - part / marg)))
out["D3_length_decomposition"] = d3

# ---- D4: the oath tautology --------------------------------------------
oath_esc, esc_labels = [], {}
with open(h.GENRE_TSV, encoding="utf-8") as fh:
    for row in csv.reader(fh, delimiter="\t"):
        if not row or not row[0].isdigit():
            continue
        n, g = int(row[0]), row[4].lower()
        if "eschatolog" in g:
            esc_labels[n] = row[4]
            if "oath" in g:
                oath_esc.append(n)
esc_no_oath = set(esc) - set(oath_esc)
h1_full = h.h1_test(M_log, S, leg, esc, lwc, SEED, "residualised", None)
h1_noath = h.h1_test(M_log, S, leg, esc_no_oath, lwc, SEED, "residualised", None)
out["D4_oath_tautology"] = {
    "eschat_surahs_whose_own_label_says_oath": sorted(oath_esc),
    "their_labels": {str(k): esc_labels[k] for k in sorted(oath_esc)},
    "n_oath": len(oath_esc), "n_eschat_total": len(esc),
    "H1_full": h1_full, "H1_oath_surahs_removed": h1_noath,
    "note": ("jawab al-qasam takes the emphatic lam (l:EMPH), which supplies %d of %d "
             "epistemic-pole tokens (%.1f%%). If H1 collapsed on removing these surahs "
             "the separation would be partly a definition."
             % (tag_tot["EMPH_pref"], sum(E.values()),
                100 * tag_tot["EMPH_pref"] / sum(E.values()))),
}
print("D4 oath-labelled eschat surahs: %s" % sorted(oath_esc))
print("D4 H1 full            delta=%+.4f p=%.4f" % (h1_full["delta_obs"], h1_full["p_one_sided"]))
print("D4 H1 oath removed    delta=%+.4f p=%.4f" % (h1_noath["delta_obs"], h1_noath["p_one_sided"]))

# ---- D5: leave-one-component-out on the epistemic pole ------------------
def build_E(components):
    Ex = collections.Counter()
    for (s, v, w), sl in word_segs.items():
        if "SUBJ_lan" in components and any("MOOD:SUBJ" in f for (_, _, _, f) in sl):
            if h.trigger_of(word_segs, s, v, w, "SUBJ", h.W_PRIMARY) == "negation_lan":
                Ex[s] += 1
        for (_, _, tag, f) in sl:
            if tag == "CERT" and "CERT" in components: Ex[s] += 1
            elif tag == "FUT" and "FUT" in components: Ex[s] += 1
            elif tag == "EMPH" and "l:EMPH" in f and "EMPH_pref" in components: Ex[s] += 1
    return Ex

ALL = ["CERT", "FUT", "EMPH_pref", "SUBJ_lan"]
d5 = collections.OrderedDict()
for drop in [None] + ALL:
    comps = [c for c in ALL if c != drop]
    Ex = build_E(comps)
    Mx = [math.log((D[s] + 0.5) / (Ex[s] + 0.5)) for s in S]
    t = h.h1_test(Mx, S, leg, esc, lwc, SEED, "residualised", None)
    rho = h.spearman(Mx, R_B)
    key = "full" if drop is None else "drop_" + drop
    d5[key] = {"E_total": sum(Ex.values()), "h1_delta": t["delta_obs"],
               "h1_p": t["p_one_sided"], "rho_M_RB": round(rho, 6)}
    print("D5 %-16s E=%5d  H1 delta=%+8.4f p=%.4f  rho(M,R_B)=%+.4f"
          % (key, sum(Ex.values()), t["delta_obs"], t["p_one_sided"], rho))
out["D5_leave_one_component_out"] = d5

# ---- D6: is l:EMPH concentrated in oath surahs? -------------------------
emph = collections.Counter()
for (s, v, w), sl in word_segs.items():
    for (_, _, tag, f) in sl:
        if tag == "EMPH" and "l:EMPH" in f: emph[s] += 1
tot_w = sum(wordcount.values())
oath_w = sum(wordcount[s] for s in oath_esc)
oath_e = sum(emph[s] for s in oath_esc)
out["D6_emph_concentration"] = {
    "l_EMPH_total": sum(emph.values()),
    "in_oath_labelled_eschat_surahs": oath_e,
    "their_share_of_corpus_words": round(oath_w / tot_w, 6),
    "their_share_of_l_EMPH": round(oath_e / sum(emph.values()), 6),
    "enrichment_ratio": round((oath_e / sum(emph.values())) / (oath_w / tot_w), 4),
    "per_1000_words_in_oath_surahs": round(1000 * oath_e / oath_w, 4),
    "per_1000_words_corpus": round(1000 * sum(emph.values()) / tot_w, 4),
}
print("D6 l:EMPH enrichment in oath-labelled eschat surahs: %.2fx"
      % out["D6_emph_concentration"]["enrichment_ratio"])

with open(os.path.join(rundir, "results.json"), "x", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
with open(os.path.join(rundir, "MANIFEST.txt"), "x", encoding="utf-8") as fh:
    fh.write("H-NEW-3040 POST-HOC diagnostics %s\nprereg sha256 %s\n"
             "script findings/phase-b-hypotheses/scripts/h-new-3040-posthoc.py\n"
             "ALL NUMBERS POST-HOC; MW-7 single-test cap alpha=0.05\n"
             % (stamp, h.EXPECTED_PREREG_SHA))
print("[written] %s/results.json" % rundir)
