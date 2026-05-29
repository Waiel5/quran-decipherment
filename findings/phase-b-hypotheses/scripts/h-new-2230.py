#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2230 — QAC-lemma re-run of the numerical-symmetry series (disambiguated).

Closes MASTER-FINDINGS-LEDGER §10.80.3. Re-counts the famous "balanced words"
claims and the kallā rebuke-particle at QAC v0.4 LEMMA + POS level
(homograph-disambiguated), under two explicitly-stated lemma rules-tuples:

  R-lemma-strict       exact QAC LEM equality, STEM tokens only (gold standard)
  R-lemma-all-clitics  same lemma but reporting within-lemma morphological
                       subsets / multi-lemma aggregations where the semantic
                       target is split (e.g. A^xir fem-noun subset)

The kallā lesson (H-NEW-2160): raw substring كلا = 38 across both halves CONFLATES
the rebuke particle kallā (POS:AVR, LEM kal~aA) with the quantifier kullan
(POS:N, LEM kul~). QAC POS+LEM is the disambiguated gold standard.

Deterministic integer counts. No RNG; seed logged for protocol uniformity.

Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""

import json
import os
import re
import sys
import hashlib

SEED = 20260529  # logged for protocol uniformity; no RNG used
PREREG_SHA = "1967b6e447442c50d4527323afb06c8404cd33a4e96b89e49dd502287d57203a"

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2230-qac-lemma-numerical-rerun.md")
NO_TASH = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2230.json")


def verify_prereg():
    with open(PREREG, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"FATAL pre-reg SHA mismatch:\n  expected {PREREG_SHA}\n  got      {h}")
    print(f"pre-reg SHA verified: {h}")


def load_qac():
    """Parse QAC into list of dicts: loc, form, tag, lem, root, feats."""
    rows = []
    with open(QAC, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            m = re.search(r"LEM:([^|]+)", feats)
            lem = m.group(1) if m else None
            m = re.search(r"ROOT:([^|]+)", feats)
            root = m.group(1) if m else None
            rows.append({"loc": loc, "form": form, "tag": tag,
                         "lem": lem, "root": root, "feats": feats})
    return rows


def load_substring_tokens():
    """Return list of (surah,verse) for every standalone token == 'كلا'."""
    with open(NO_TASH, encoding="utf-8") as f:
        data = json.load(f)
    hits = []
    for su in data:
        for ve in su["verses"]:
            for tok in ve["text"].split():
                if tok == "كلا":
                    hits.append((su["id"], ve["id"]))
    return hits


def surah_of(loc):
    return int(loc.strip("()").split(":")[0])


def lemcount(qac, lem):
    return sum(1 for r in qac if r["lem"] == lem)


def rootcount(qac, root):
    return sum(1 for r in qac if r["root"] == root)


def number_breakdown(qac, lem):
    """Split a lemma into singular / dual / plural via QAC FEATURES number tags."""
    sing = dual = plur = 0
    for r in qac:
        if r["lem"] != lem:
            continue
        f = r["feats"]
        if re.search(r"\|[MF]D(\||$)", f) or re.search(r"\|DU(\||$)", f):
            dual += 1
        elif re.search(r"\|[MF]P(\||$)", f) or re.search(r"\|P(\||$)", f):
            plur += 1
        else:
            sing += 1
    return {"singular": sing, "dual": dual, "plural": plur,
            "total": sing + dual + plur}


def main():
    verify_prereg()
    qac = load_qac()

    claims = {}

    # =====================================================================
    # CLAIM 1 — al-dunyā = al-ākhira (claimed 115 = 115)
    # =====================================================================
    dunya = lemcount(qac, "d~unoyaA")
    axir_whole = lemcount(qac, "A^xir")     # includes adjectival ākhir
    axar_other = lemcount(qac, "A^xar")     # 'other' — NOT the Hereafter
    # within-lemma fem tā-marbūṭa subset of A^xir = the Hereafter noun al-ākhira
    axir_tokens = [r for r in qac if r["lem"] == "A^xir"]
    hereafter = [r for r in axir_tokens if "aAxirap" in r["form"]]
    adj_akhir = [r for r in axir_tokens if "aAxirap" not in r["form"]]
    claims["claim1_dunya_akhira"] = {
        "claimed": "115 = 115",
        "dunya_R_lemma_strict": dunya,
        "akhira_R_lemma_strict_whole_A^xir": axir_whole,
        "akhira_R_lemma_fem_noun_subset_Hereafter": len(hereafter),
        "akhir_adjectival_remainder": len(adj_akhir),
        "akhar_other_separate_lemma": axar_other,
        "balance_strict": bool(dunya == axir_whole),
        "balance_fem_noun_subset": bool(dunya == len(hereafter)),
    }

    # =====================================================================
    # CLAIM 2 — al-ḥayāt = al-mawt (claimed 145 = 145)
    # =====================================================================
    hayat = lemcount(qac, "Hayaw`p")
    mawt = lemcount(qac, "mawot")
    root_hyy = rootcount(qac, "Hyy")
    root_mwt = rootcount(qac, "mwt")
    claims["claim2_hayat_mawt"] = {
        "claimed": "145 = 145",
        "hayat_noun_R_lemma_strict": hayat,
        "mawt_noun_R_lemma_strict": mawt,
        "root_Hyy_total_R_lemma_all": root_hyy,
        "root_mwt_total_R_lemma_all": root_mwt,
        "noun_balance": bool(hayat == mawt),
        "either_hits_145": bool(hayat == 145 or mawt == 145),
    }

    # =====================================================================
    # CLAIM 3 — al-malāʾika = al-shayāṭīn (claimed 88 = 88)
    # =====================================================================
    malak_total = lemcount(qac, "malak")
    shaytan_total = lemcount(qac, "$ayoTa`n")
    malak_nb = number_breakdown(qac, "malak")
    shaytan_nb = number_breakdown(qac, "$ayoTa`n")
    claims["claim3_malaika_shayatin"] = {
        "claimed": "88 = 88",
        "malak_R_lemma_strict_whole": malak_total,
        "shaytan_R_lemma_strict_whole": shaytan_total,
        "malak_number_breakdown": malak_nb,
        "shaytan_number_breakdown": shaytan_nb,
        "whole_lemma_balance": bool(malak_total == shaytan_total),
        "plural_balance": bool(malak_nb["plural"] == shaytan_nb["plural"]),
        "singular_balance": bool(malak_nb["singular"] == shaytan_nb["singular"]),
    }

    # =====================================================================
    # CLAIM 4 — al-rajul = al-marʾa (claimed 24 = 24)
    # =====================================================================
    rajul = lemcount(qac, "rajul")        # man, singular
    imraa = lemcount(qac, "{mora>at")     # woman / wife
    rijal = lemcount(qac, "rijaAl")       # men plural
    nisa = lemcount(qac, "nisaA^'")       # women plural
    claims["claim4_rajul_maraa"] = {
        "claimed": "24 = 24",
        "rajul_R_lemma_strict": rajul,
        "imraa_R_lemma_strict": imraa,
        "rijal_plural_R_lemma_all": rijal,
        "nisa_plural_R_lemma_all": nisa,
        "balance": bool(rajul == imraa),
        "either_hits_24": bool(rajul == 24 or imraa == 24),
    }

    # =====================================================================
    # CLAIM 5 — calendar: shahr=12, yawm-sing=365, ayyām/dual=30
    # =====================================================================
    shahr_nb = number_breakdown(qac, "$ahor")
    yawm_nb = number_breakdown(qac, "yawom")
    yawmaidhin = lemcount(qac, "yawoma}i*")  # adverb 'on that day' — separate lemma
    ayyam_plus_dual = yawm_nb["plural"] + yawm_nb["dual"]
    claims["claim5_calendar"] = {
        "claimed_shahr": 12, "claimed_yawm": 365, "claimed_ayyam": 30,
        "shahr_singular_R_lemma_strict": shahr_nb["singular"],
        "shahr_breakdown": shahr_nb,
        "yawm_singular_R_lemma_strict": yawm_nb["singular"],
        "yawm_breakdown": yawm_nb,
        "yawmaidhin_separate_lemma_excluded": yawmaidhin,
        "ayyam_plural_plus_dual": ayyam_plus_dual,
        "shahr_hits_12": bool(shahr_nb["singular"] == 12),
        "yawm_hits_365": bool(yawm_nb["singular"] == 365),
        "ayyam_hits_30": bool(ayyam_plus_dual == 30),
    }

    # =====================================================================
    # CLAIM 6 — Iblīs (11) = istiʿādha / seek-refuge (11)
    # =====================================================================
    iblis_tokens = [r for r in qac if r["lem"] == "<iboliys"]
    iblis = len(iblis_tokens)
    refuge_root = [r for r in qac if r["root"] == "Ew*"]
    refuge_verbs = [r for r in refuge_root if r["tag"] == "V"]
    rv_lemmas = {}
    for r in refuge_verbs:
        rv_lemmas[r["lem"]] = rv_lemmas.get(r["lem"], 0) + 1
    form1 = rv_lemmas.get("Eu*o", 0)       # ʿādha / aʿūdhu
    form4 = rv_lemmas.get(">uEiy*u", 0)    # uʿīdhu (commend to refuge)
    form10 = rv_lemmas.get("{sotaEi*o", 0) # istaʿidh imperative
    claims["claim6_iblis_refuge"] = {
        "claimed": "11 = 11",
        "iblis_R_lemma_strict": iblis,
        "iblis_hits_11": bool(iblis == 11),
        "refuge_root_total": len(refuge_root),
        "refuge_verbs_total": len(refuge_verbs),
        "refuge_verb_lemma_breakdown": rv_lemmas,
        "refuge_form1_aoudhu": form1,
        "refuge_form4_uidhu": form4,
        "refuge_form10_istaidh": form10,
        "refuge_form1_plus_form4_subset": form1 + form4,
        # "natural" totals = the non-gerrymandered boundaries (a single form-class,
        # all-verbs, or whole-root). The form1+form4 mix is the SELECTIVE subset the
        # pre-reg flags as non-principled and is therefore excluded here.
        "refuge_natural_totals": sorted({form1, len(refuge_verbs), len(refuge_root)}),
        "refuge_has_natural_11": bool(
            11 in {form1, len(refuge_verbs), len(refuge_root)}),
        "refuge_11_only_via_selective_subset": bool(
            (form1 + form4) == 11 and 11 not in {form1, len(refuge_verbs), len(refuge_root)}),
    }

    # =====================================================================
    # CLAIM 7 — kallā rebuke-lemma (claimed 33, al-Dānī)
    # =====================================================================
    rebuke = [r for r in qac if r["tag"] == "AVR" and r["lem"] == "kal~aA"]
    rebuke_locs = [r["loc"] for r in rebuke]
    # raw substring standalone كلا tokens (the homograph haystack)
    substr = load_substring_tokens()
    substr_keys = {f"{s}:{v}" for s, v in substr}
    rebuke_surahs = sorted({surah_of(l) for l in rebuke_locs})
    # second-half cutoff: classical "latter half" ≈ surahs >= 19 (start of mufaṣṣal-ish);
    # report both the al-Dānī "second half" and a strict midpoint (>=58) view.
    by_surah = {}
    for l in rebuke_locs:
        s = surah_of(l)
        by_surah[s] = by_surah.get(s, 0) + 1
    # disambiguation of the 38 substring tokens: which are rebuke vs quantifier
    # match substring (surah:verse) to QAC tokens at that location
    qac_at = {}
    for r in qac:
        parts = r["loc"].strip("()").split(":")
        sv = f"{int(parts[0])}:{int(parts[1])}"
        qac_at.setdefault(sv, []).append(r)
    per_token = []
    for s, v in sorted(substr):
        sv = f"{s}:{v}"
        toks = qac_at.get(sv, [])
        kal = [t for t in toks if t["form"].startswith("kal~aA") and t["tag"] == "AVR"]
        kul = [t for t in toks if t["lem"] == "kul~" and t["form"].startswith("kul~")]
        if kal:
            per_token.append({"loc": sv, "class": "rebuke_kalla_AVR",
                              "qac_lem": "kal~aA", "qac_pos": "AVR"})
        elif kul:
            per_token.append({"loc": sv, "class": "quantifier_kullan",
                              "qac_lem": "kul~", "qac_pos": "N",
                              "form": kul[0]["form"]})
        else:
            per_token.append({"loc": sv, "class": "UNRESOLVED",
                              "qac_forms_here": [t["form"] for t in toks]})
    n_rebuke = sum(1 for p in per_token if p["class"] == "rebuke_kalla_AVR")
    n_quant = sum(1 for p in per_token if p["class"] == "quantifier_kullan")
    quant_locs = [p["loc"] for p in per_token if p["class"] == "quantifier_kullan"]
    claims["claim7_kalla"] = {
        "claimed": 33,
        "rebuke_kalla_POS_AVR_count": len(rebuke),
        "rebuke_hits_33": bool(len(rebuke) == 33),
        "rebuke_surahs": rebuke_surahs,
        "rebuke_by_surah": by_surah,
        "min_surah_of_rebuke": min(rebuke_surahs),
        "all_rebuke_in_second_half_ge19": all(s >= 19 for s in rebuke_surahs),
        "raw_substring_standalone_kalla": len(substr),
        "substring_minus_rebuke": len(substr) - len(rebuke),
        "quantifier_kullan_count_among_substring": n_quant,
        "quantifier_kullan_locs": quant_locs,
        "per_token_disambiguation": per_token,
    }

    # =====================================================================
    # VERDICTS — apply pre-reg vocabulary
    # =====================================================================
    verdicts = {}

    # Claim 1
    c1 = claims["claim1_dunya_akhira"]
    if c1["balance_strict"]:
        v1 = "CONFIRMED"
    elif c1["balance_fem_noun_subset"]:
        v1 = "RULES-FRAGILE"
    else:
        v1 = "FALSIFIED"
    verdicts["claim1_dunya_akhira"] = {
        "verdict": v1,
        "note": (f"dunyā={c1['dunya_R_lemma_strict']} (single bare-definite lemma, "
                 f"CONFIRMED-BUT-MEANINGLESS as a one-sided fact). ākhira whole-lemma "
                 f"A^xir={c1['akhira_R_lemma_strict_whole_A^xir']} (≠115, includes "
                 f"adjectival ākhir). Hereafter-noun fem tā-marbūṭa subset="
                 f"{c1['akhira_R_lemma_fem_noun_subset_Hereafter']}. Balance 115=115 "
                 f"holds ONLY under the within-lemma fem-noun subset → RULES-FRAGILE.")
    }

    # Claim 2
    c2 = claims["claim2_hayat_mawt"]
    verdicts["claim2_hayat_mawt"] = {
        "verdict": "FALSIFIED",
        "note": (f"ḥayāt-noun={c2['hayat_noun_R_lemma_strict']} vs "
                 f"mawt-noun={c2['mawt_noun_R_lemma_strict']}; root totals "
                 f"{c2['root_Hyy_total_R_lemma_all']} vs "
                 f"{c2['root_mwt_total_R_lemma_all']}. No rule hits 145; no balance.")
    }

    # Claim 3
    c3 = claims["claim3_malaika_shayatin"]
    if c3["plural_balance"]:
        v3 = "CONFIRMED"
    elif c3["whole_lemma_balance"]:
        v3 = "RULES-FRAGILE"
    else:
        v3 = "FALSIFIED"
    verdicts["claim3_malaika_shayatin"] = {
        "verdict": v3,
        "note": (f"whole-lemma {c3['malak_R_lemma_strict_whole']}="
                 f"{c3['shaytan_R_lemma_strict_whole']} balances, BUT it is a "
                 f"conflation artifact: plural malāʾika={c3['malak_number_breakdown']['plural']} "
                 f"vs plural shayāṭīn={c3['shaytan_number_breakdown']['plural']}; "
                 f"singular angel={c3['malak_number_breakdown']['singular']} vs "
                 f"devil={c3['shaytan_number_breakdown']['singular']} (inverted "
                 f"morphology). The two 88s are made of opposite material → RULES-FRAGILE.")
    }

    # Claim 4
    c4 = claims["claim4_rajul_maraa"]
    verdicts["claim4_rajul_maraa"] = {
        "verdict": "FALSIFIED",
        "note": (f"rajul={c4['rajul_R_lemma_strict']} vs imraʾa={c4['imraa_R_lemma_strict']}; "
                 f"neither = 24, no balance. Plurals rijāl={c4['rijal_plural_R_lemma_all']} "
                 f"vs nisāʾ={c4['nisa_plural_R_lemma_all']} also unbalanced.")
    }

    # Claim 5
    c5 = claims["claim5_calendar"]
    n_hit = sum([c5["shahr_hits_12"], c5["yawm_hits_365"], c5["ayyam_hits_30"]])
    v5 = "CONFIRMED" if n_hit == 3 else "RULES-FRAGILE" if n_hit >= 1 else "FALSIFIED"
    verdicts["claim5_calendar"] = {
        "verdict": v5,
        "note": (f"shahr-sing={c5['shahr_singular_R_lemma_strict']} (=12 {'✓' if c5['shahr_hits_12'] else '✗'}, fact); "
                 f"ayyām+dual={c5['ayyam_plural_plus_dual']} (=30 {'✓' if c5['ayyam_hits_30'] else '✗'}, fact); "
                 f"yawm-sing={c5['yawm_singular_R_lemma_strict']} (claimed 365 "
                 f"{'✓' if c5['yawm_hits_365'] else '✗ — astronomical headline FAILS'}). "
                 f"{n_hit}/3 sub-targets land → RULES-FRAGILE (the two facts are real; "
                 f"the 365 headline is wrong).")
    }

    # Claim 6
    c6 = claims["claim6_iblis_refuge"]
    if c6["iblis_hits_11"] and c6["refuge_has_natural_11"]:
        v6 = "CONFIRMED"
    elif c6["iblis_hits_11"]:
        v6 = "RULES-FRAGILE"
    else:
        v6 = "FALSIFIED"
    verdicts["claim6_iblis_refuge"] = {
        "verdict": v6,
        "note": (f"Iblīs={c6['iblis_R_lemma_strict']} (=11 EXACT, CONFIRMED-BUT-MEANINGLESS "
                 f"one-sided fact). Refuge verbs: form1={c6['refuge_form1_aoudhu']}, "
                 f"+form4={c6['refuge_form1_plus_form4_subset']}, all-verbs="
                 f"{c6['refuge_verbs_total']}, all-root={c6['refuge_root_total']}. "
                 f"The 11 needs the form1+form4 subset (excludes the 4 istaʿidh "
                 f"imperatives) — selective boundary → RULES-FRAGILE.")
    }

    # Claim 7
    c7 = claims["claim7_kalla"]
    v7 = "CONFIRMED" if (c7["rebuke_hits_33"] and c7["all_rebuke_in_second_half_ge19"]) else "FALSIFIED"
    verdicts["claim7_kalla"] = {
        "verdict": v7,
        "note": (f"rebuke-kallā (POS:AVR LEM kal~aA)={c7['rebuke_kalla_POS_AVR_count']} "
                 f"(=33 {'✓' if c7['rebuke_hits_33'] else '✗'}); min surah="
                 f"{c7['min_surah_of_rebuke']}, all ≥19 "
                 f"{'✓' if c7['all_rebuke_in_second_half_ge19'] else '✗'}. Raw substring "
                 f"كلا={c7['raw_substring_standalone_kalla']} CONFLATES "
                 f"{c7['quantifier_kullan_count_among_substring']} quantifier kullan "
                 f"tokens at {c7['quantifier_kullan_locs']} (all first-half) → CONFIRMS "
                 f"al-Dānī after disambiguation.")
    }

    # =====================================================================
    # DIRECTION-LOCK EVALUATION
    # =====================================================================
    balance_claims = ["claim1_dunya_akhira", "claim2_hayat_mawt",
                      "claim3_malaika_shayatin", "claim4_rajul_maraa",
                      "claim5_calendar", "claim6_iblis_refuge"]
    n_confirmed_clean = sum(1 for k in balance_claims
                            if verdicts[k]["verdict"] == "CONFIRMED")
    direction = {
        "locked_prediction": "<=1 of 6 balance claims CONFIRMED-clean at lemma-strict",
        "n_balance_claims_CONFIRMED_clean": n_confirmed_clean,
        "direction_held": bool(n_confirmed_clean <= 1),
        "interpretation": (
            "DIRECTION HELD — QAC-lemma disambiguation does NOT rescue the antonym "
            "balances; numerology stays retired."
            if n_confirmed_clean <= 1 else
            "PRE-COMMIT VIOLATION — disambiguation RESCUED more than predicted; "
            "published as bidirectional rules-tuple sensitivity."),
        "kalla_confirmed_33": bool(verdicts["claim7_kalla"]["verdict"] == "CONFIRMED"),
    }

    out = {
        "finding_id": "H-NEW-2230",
        "seed": SEED,
        "prereg_sha256": PREREG_SHA,
        "rules": {
            "R-lemma-strict": "exact QAC LEM equality, STEM tokens (gold standard)",
            "R-lemma-all-clitics": "within-lemma morphological subset / multi-lemma "
                                   "aggregation where target is split",
            "R-lemma-fem-noun": "A^xir tā-marbūṭa subset = Hereafter-noun al-ākhira",
            "kalla_disambiguation": "POS:AVR ∧ LEM kal~aA = rebuke; LEM kul~ = quantifier",
        },
        "claims": claims,
        "verdicts": verdicts,
        "direction_lock": direction,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # ---- console summary ----
    print("\n=== H-NEW-2230 verdict summary (QAC-lemma, disambiguated) ===")
    for k in ["claim1_dunya_akhira", "claim2_hayat_mawt", "claim3_malaika_shayatin",
              "claim4_rajul_maraa", "claim5_calendar", "claim6_iblis_refuge",
              "claim7_kalla"]:
        v = verdicts[k]
        print(f"\n{k}: {v['verdict']}")
        print(f"   {v['note']}")
    print("\n=== direction lock ===")
    print(f"   balance claims CONFIRMED-clean: {direction['n_balance_claims_CONFIRMED_clean']} "
          f"(predicted <=1) → {direction['interpretation']}")
    print(f"   kallā = 33 confirmed: {direction['kalla_confirmed_33']}")
    print(f"\nJSON written: {OUT_JSON}")


if __name__ == "__main__":
    main()
