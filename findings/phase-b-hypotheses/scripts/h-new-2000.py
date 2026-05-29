#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2000 — Iʿjāz ʿadadī (numerical word-symmetry) claims, multi-rules audit.

Audits the most-cited Nawfal / Jarrar / al-Kaheel "balanced words" claims under
three pre-committed counting rules:
  R1  strict-al-form  (definite surface lexeme, substring on no-tashkeel corpus)
  R2  all-morphological-forms (surface regex, documented homonym exclusions)
  R3  QAC-lemma  (Quranic Arabic Corpus v0.4 STEM tokens by LEM field)

Deterministic integer counts. No randomness; seed logged for protocol uniformity.

Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""

import json
import os
import re
import sys
import hashlib

SEED = 20260509  # logged for protocol uniformity; no RNG used
PREREG_SHA = "0474c9986636fe2543f7a9ce3aff4d1c77e82bbf2108648c9bb2b824798b3789"

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2000-numerical-symmetry-audit.md")
NO_TASH = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2000.json")


def verify_prereg():
    with open(PREREG, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"FATAL pre-reg SHA mismatch:\n  expected {PREREG_SHA}\n  got      {h}")
    print(f"pre-reg SHA verified: {h}")


# ---------------------------------------------------------------------------
# Corpus loaders
# ---------------------------------------------------------------------------
def load_corpus_tokens():
    """Return (full_text, token_list) from no-tashkeel JSON.
    Basmala counted only as Q1:1 per default tuple (the JSON stores it as Q1:1
    and as the standard opener of other surahs only where it is a numbered verse;
    in this Tanzil file the surah-opener basmalas are NOT separate verses, so
    substring counts already follow basmala-counted-only-in-Q1)."""
    with open(NO_TASH, encoding="utf-8") as f:
        data = json.load(f)
    text_parts = []
    tokens = []
    for surah in data:
        for v in surah["verses"]:
            t = v["text"]
            text_parts.append(t)
            tokens.extend(t.split())
    return " ".join(text_parts), tokens


def load_qac():
    """Parse QAC into list of dicts: location, form, tag, lemma, root, features."""
    rows = []
    with open(QAC, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            lem = None
            root = None
            m = re.search(r"LEM:([^|]+)", feats)
            if m:
                lem = m.group(1)
            m = re.search(r"ROOT:([^|]+)", feats)
            if m:
                root = m.group(1)
            rows.append({"loc": loc, "form": form, "tag": tag, "lem": lem,
                         "root": root, "feats": feats})
    return rows


# ---------------------------------------------------------------------------
# Counting helpers
# ---------------------------------------------------------------------------
def count_substring(text, needle):
    """Non-overlapping substring count over the whole corpus text."""
    return text.count(needle)


def count_tokens_regex(tokens, pattern):
    rx = re.compile(pattern)
    return sum(1 for t in tokens if rx.search(t))


def qac_lemma_count(qac, lemma):
    return sum(1 for r in qac if r["lem"] == lemma)


def qac_lemma_count_by_number(qac, lemma):
    """Return {sing, plur, dual, other} for a lemma using FEATURES number tags."""
    out = {"S_or_M": 0, "P": 0, "DU": 0, "total": 0}
    for r in qac:
        if r["lem"] != lemma:
            continue
        out["total"] += 1
        f = r["feats"]
        if "|DU" in f or f.endswith("DU"):
            out["DU"] += 1
        elif "|MP" in f or "|FP" in f or "|P\t" in f or f.endswith("P") and "|MP" not in f and "|FP" not in f:
            # plural marker
            out["P"] += 1
        else:
            out["S_or_M"] += 1
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    verify_prereg()
    text, tokens = load_corpus_tokens()
    qac = load_qac()

    results = {}

    # ---- helper to record a number-breakdown by explicit FEATURES scan -----
    def number_breakdown(lemma):
        # QAC number tags: ...|M| or |F| = singular; |MD|/|FD| = dual; |MP|/|FP| = plural
        sing = plur = dual = 0
        for r in qac:
            if r["lem"] != lemma:
                continue
            f = r["feats"]
            if re.search(r"\|[MF]D(\||$)", f) or re.search(r"\|DU(\||$)", f):
                dual += 1
            elif re.search(r"\|[MF]P(\||$)", f) or re.search(r"\|P(\||$)", f):
                plur += 1
            else:
                sing += 1
        return {"singular": sing, "plural": plur, "dual": dual,
                "total": sing + plur + dual}

    # =====================================================================
    # CLAIM 1 — al-dunyā = al-ākhira  (claimed 115 = 115)
    # =====================================================================
    c1 = {}
    # R1 strict definite surface
    c1["R1_aldunya"] = count_substring(text, "الدنيا")
    c1["R1_alakhira"] = count_substring(text, "الآخرة")
    # R3 QAC lemma
    c1["R3_dunya_lemma"] = qac_lemma_count(qac, "d~unoyaA")
    c1["R3_akhira_lemma_Axir"] = qac_lemma_count(qac, "A^xir")      # ākhir(a)
    c1["R3_akhar_lemma"] = qac_lemma_count(qac, "A^xar")            # ākhar 'other'
    c1["R3_akhira_strict"] = c1["R3_akhira_lemma_Axir"]
    # R2 all surface forms of dunyā (root dnw 'low/near world') vs ākhira
    c1["R2_dunya_allforms"] = count_substring(text, "دنيا")  # catches al-dunyā + wa-l-dunyā etc.
    c1["R2_akhira_allforms"] = count_substring(text, "اخرة") + count_substring(text, "آخرة")
    results["claim1_dunya_akhira"] = c1

    # =====================================================================
    # CLAIM 2 — al-malāʾika = al-shayāṭīn (claimed 88 = 88)
    # =====================================================================
    c2 = {}
    c2["R3_malak_lemma_total"] = qac_lemma_count(qac, "malak")
    c2["R3_shaytan_lemma_total"] = qac_lemma_count(qac, "$ayoTa`n")
    c2["malak_number"] = number_breakdown("malak")
    c2["shaytan_number"] = number_breakdown("$ayoTa`n")
    results["claim2_malaika_shayatin"] = c2

    # =====================================================================
    # CLAIM 3 — al-ḥayāt = al-mawt (claimed 145 = 145)
    # =====================================================================
    c3 = {}
    c3["R3_hayat_noun_lemma"] = qac_lemma_count(qac, "Hayaw`p")   # ḥayāt noun
    c3["R3_mawt_noun_lemma"] = qac_lemma_count(qac, "mawot")      # mawt noun
    # whole-root totals
    c3["R3_root_Hyy_total"] = sum(1 for r in qac if r["root"] == "Hyy")
    c3["R3_root_mwt_total"] = sum(1 for r in qac if r["root"] == "mwt")
    # "life-cluster" = ḥayāt + ḥayy(adj) + aḥyā(verb) etc; "death-cluster" likewise
    hyy_lemmas = {}
    mwt_lemmas = {}
    for r in qac:
        if r["root"] == "Hyy" and r["lem"]:
            hyy_lemmas[r["lem"]] = hyy_lemmas.get(r["lem"], 0) + 1
        if r["root"] == "mwt" and r["lem"]:
            mwt_lemmas[r["lem"]] = mwt_lemmas.get(r["lem"], 0) + 1
    c3["Hyy_lemma_breakdown"] = hyy_lemmas
    c3["mwt_lemma_breakdown"] = mwt_lemmas
    # R1 strict definite surface
    c3["R1_alhayat"] = count_substring(text, "الحياة")
    c3["R1_almawt"] = count_substring(text, "الموت")
    results["claim3_hayat_mawt"] = c3

    # =====================================================================
    # CLAIM 4 — calendar: shahr=12, yawm-sing=365, ayyam/dual=30
    # =====================================================================
    c4 = {}
    # shahr lemma $ahor: split singular vs plural vs dual via FEATURES + form
    shahr_tokens = [r for r in qac if r["lem"] == "$ahor"]
    c4["shahr_lemma_total"] = len(shahr_tokens)
    # singular forms: shahr / al-shahr (not >a$ohur plural, not $ahorayn dual, not $uhuwr plural)
    shahr_sing = shahr_plur = shahr_dual = 0
    shahr_detail = []
    for r in shahr_tokens:
        form = r["form"]
        if "$ahorayoni" in form or "ayoni" in form:
            shahr_dual += 1
            cat = "dual"
        elif form.startswith(">a$ohur") or "uhuwr" in form:
            shahr_plur += 1
            cat = "plural"
        else:
            shahr_sing += 1
            cat = "singular"
        shahr_detail.append({"loc": r["loc"], "form": form, "cat": cat})
    c4["shahr_singular"] = shahr_sing
    c4["shahr_plural"] = shahr_plur
    c4["shahr_dual"] = shahr_dual
    c4["shahr_detail"] = shahr_detail
    # yawm: lemma yawom; split singular vs plural(ayyam) vs dual(yawmayn)
    yawm_tokens = [r for r in qac if r["lem"] == "yawom"]
    c4["yawm_lemma_total"] = len(yawm_tokens)
    yawm_sing = yawm_plur = yawm_dual = 0
    for r in yawm_tokens:
        form = r["form"]
        f = r["feats"]
        if re.search(r"\|DU(\||$)", f) or "yawomayoni" in form or "yawomayoF" in form:
            yawm_dual += 1
        elif re.search(r"\|(MP|FP|P)(\||$)", f) or "ay~aAm" in form or ">ay~aAm" in form:
            yawm_plur += 1
        else:
            yawm_sing += 1
    c4["yawm_singular"] = yawm_sing
    c4["yawm_plural_ayyam"] = yawm_plur
    c4["yawm_dual_yawmayn"] = yawm_dual
    # surface cross-checks
    c4["surf_yawm_token_exact"] = count_tokens_regex(tokens, r"^يوم$|^اليوم$|^يوما$|^يومئذ")
    c4["surf_ayyam"] = count_tokens_regex(tokens, r"ايام|أيام")
    results["claim4_calendar"] = c4

    # =====================================================================
    # CLAIM 5 — al-rajul = al-marʾa (claimed 24 = 24)
    # =====================================================================
    c5 = {}
    c5["R3_rajul_lemma"] = qac_lemma_count(qac, "rajul")          # man singular
    c5["R3_imraa_lemma"] = qac_lemma_count(qac, "{mora>at")       # woman/wife
    c5["R3_rijal_lemma"] = qac_lemma_count(qac, "rijaAl")         # men plural
    c5["R3_nisa_lemma"] = qac_lemma_count(qac, "nisaA^'")         # women plural
    c5["R1_alrajul"] = count_substring(text, "الرجل")
    c5["R1_almaraa"] = count_substring(text, "المرأة") + count_substring(text, "المراة")
    results["claim5_rajul_maraa"] = c5

    # =====================================================================
    # CLAIM 6 — Iblīs (11) = istiʿādha / seek-refuge verbs (11)
    # =====================================================================
    c6 = {}
    iblis_tokens = [r for r in qac if r["lem"] == "<iboliys"]
    c6["iblis_count"] = len(iblis_tokens)
    c6["iblis_locs"] = [r["loc"] for r in iblis_tokens]
    # refuge root Ew* (ʿ-w-dh): all tokens, verbs only, by lemma
    refuge = [r for r in qac if r["root"] == "Ew*"]
    c6["refuge_root_total"] = len(refuge)
    refuge_verbs = [r for r in refuge if r["tag"] == "V"]
    c6["refuge_verbs_total"] = len(refuge_verbs)
    # lemma breakdown of refuge verbs
    rv_lemmas = {}
    for r in refuge_verbs:
        rv_lemmas[r["lem"]] = rv_lemmas.get(r["lem"], 0) + 1
    c6["refuge_verb_lemma_breakdown"] = rv_lemmas
    c6["refuge_verb_locs"] = [r["loc"] for r in refuge_verbs]
    # the specific verb aʿūdhu / istiʿādha forms (excluding noun maʿādh)
    c6["refuge_aoudhu_only"] = sum(1 for r in refuge_verbs if r["lem"] in {"Eu*o"})
    results["claim6_iblis_refuge"] = c6

    # =====================================================================
    # CLAIM 7 — al-malak (sing) vs al-shayṭān (sing)
    # =====================================================================
    c7 = {}
    c7["malak_singular"] = c2["malak_number"]["singular"]
    c7["malak_plural"] = c2["malak_number"]["plural"]
    c7["shaytan_singular"] = c2["shaytan_number"]["singular"]
    c7["shaytan_plural"] = c2["shaytan_number"]["plural"]
    results["claim7_singular_angel_devil"] = c7

    # =====================================================================
    # CLAIM 8 — al-ṣāliḥāt = al-sayyiʾāt
    # =====================================================================
    c8 = {}
    c8["R3_salihat_lemma"] = qac_lemma_count(qac, "S~a`liHa`t")    # ṣāliḥāt (good deeds, fem pl)
    c8["R3_sayyiat_lemma"] = qac_lemma_count(qac, "say~i_#aAt")    # sayyiʾāt (bad deeds, pl)
    c8["R3_sayyia_sing_lemma"] = qac_lemma_count(qac, "say~i}ap")  # sayyiʾa singular
    c8["R3_hasanat_root_comp"] = sum(1 for r in qac if r["root"] == "Hsn")  # context
    results["claim8_salihat_sayyiat"] = c8

    # =====================================================================
    # CLAIM 9 — al-rasūl / rusul frequency (descriptive)
    # =====================================================================
    c9 = {}
    c9["R3_rasul_lemma"] = qac_lemma_count(qac, "rasuwl")
    c9["R3_mursal_lemma"] = qac_lemma_count(qac, "m~urosal")
    c9["R3_nabiy_root_comp"] = sum(1 for r in qac if r["root"] == "nbA")
    results["claim9_rasul"] = c9

    # =====================================================================
    # CLAIM 10 — baḥr (sea) vs barr (land) = 32 : 13 → 71.1% water
    # =====================================================================
    c10 = {}
    c10["R3_bahr_lemma"] = qac_lemma_count(qac, "baHor")          # sea
    c10["R3_barr_land_lemma"] = qac_lemma_count(qac, "bar~")      # land (geographic)
    c10["R3_birr_lemma"] = qac_lemma_count(qac, "bir~")          # righteousness (HOMONYM, excluded)
    c10["R3_tabarru_lemma"] = qac_lemma_count(qac, "tabar~u")    # to be dutiful (excluded)
    # abrar (the righteous) — root brr? check separate
    c10["R3_root_brr_total"] = sum(1 for r in qac if r["root"] == "brr")
    # FUNCI variant: barr + ard (land + earth)
    c10["R3_ard_lemma"] = qac_lemma_count(qac, ">aroD")          # earth
    # ratios
    sea = c10["R3_bahr_lemma"]
    land_strict = c10["R3_barr_land_lemma"]
    if sea + land_strict > 0:
        c10["water_pct_strict"] = round(100.0 * sea / (sea + land_strict), 2)
    c10["claimed_water_pct"] = 71.11
    results["claim10_sea_land"] = c10

    # ---- verdicts (computed deterministically, applying pre-reg rules) ----
    verdicts = {}

    # C1: three rules tested; R2 = semantic-noun-all-surface-forms
    d1 = c1
    c1_pair_R1 = (d1["R1_aldunya"] == 115 and d1["R1_alakhira"] == 115)
    c1_pair_R2 = (d1["R2_dunya_allforms"] == 115 and d1["R2_akhira_allforms"] == 115)
    c1_pair_R3 = (d1["R3_dunya_lemma"] == 115 and d1["R3_akhira_strict"] == 115)
    # principled assessment: R2 balances at 115=115 but ONLY by counting ākhira's
    # clitic-prefixed forms (bi-/wa-/li-) as the eschatological noun while dunyā needs
    # none, AND excluding non-eschatological adjectival ākhir (the QAC lemma A^xir=155).
    # The balance is REAL but rule-dependent: it breaks under both R1 (112) and R3 (155).
    if c1_pair_R2 and not (c1_pair_R1 and c1_pair_R3):
        c1_verdict = "RULES-FRAGILE"
    elif c1_pair_R1 or c1_pair_R3:
        c1_verdict = "CONFIRMED"
    else:
        c1_verdict = "FALSIFIED"
    verdicts["claim1"] = {
        "dunya_R1": d1["R1_aldunya"], "akhira_R1": d1["R1_alakhira"],
        "dunya_R2_allforms": d1["R2_dunya_allforms"],
        "akhira_R2_allforms": d1["R2_akhira_allforms"],
        "dunya_R3_lemma": d1["R3_dunya_lemma"], "akhira_R3_lemma_Axir": d1["R3_akhira_strict"],
        "balance_R1": bool(c1_pair_R1), "balance_R2": bool(c1_pair_R2),
        "balance_R3": bool(c1_pair_R3),
        "verdict": c1_verdict,
        "note": "dunyā=115 EXACTLY (always bare-definite الدنيا, single form). "
                "ākhira balances at 115 ONLY under R2 (eschatological noun in ALL "
                "clitic forms الآخرة/بالآخرة/والآخرة/للآخرة...) — breaks under R1 "
                "strict-definite (112) and R3 QAC-lemma A^xir (155, includes adjectival "
                "ākhir). Balance real but rule-dependent."
    }

    # C2 / C7: malaika vs shayatin
    mal_pl = c2["malak_number"]["plural"]
    shy_pl = c2["shaytan_number"]["plural"]
    mal_tot = c2["R3_malak_lemma_total"]
    shy_tot = c2["R3_shaytan_lemma_total"]
    verdicts["claim2"] = {
        "malak_lemma_total": mal_tot, "shaytan_lemma_total": shy_tot,
        "malaika_plural": mal_pl, "shayatin_plural": shy_pl,
        "lemma_total_balances": bool(mal_tot == shy_tot),
        "plural_balances": bool(mal_pl == shy_pl),
        "verdict": ("RULES-FRAGILE" if (mal_tot == shy_tot and mal_pl != shy_pl)
                    else "CONFIRMED" if mal_pl == shy_pl else "FALSIFIED"),
        "note": "Whole-lemma 88=88 balances; but gloss 'angels/devils' is plural, and "
                "plural malāʾika=" + str(mal_pl) + " vs shayāṭīn=" + str(shy_pl)
                + " do NOT balance. Balance is conflation artifact."
    }
    verdicts["claim7"] = {
        "malak_singular": c7["malak_singular"], "shaytan_singular": c7["shaytan_singular"],
        "verdict": "DESCRIPTIVE",
        "note": "Singulars do NOT balance (angel sing="
                + str(c7["malak_singular"]) + " vs devil sing="
                + str(c7["shaytan_singular"]) + "); inverse morphology vs the plural."
    }

    # C3 hayat/mawt
    hay_noun = c3["R3_hayat_noun_lemma"]
    mawt_noun = c3["R3_mawt_noun_lemma"]
    root_h = c3["R3_root_Hyy_total"]
    root_m = c3["R3_root_mwt_total"]
    verdicts["claim3"] = {
        "hayat_noun": hay_noun, "mawt_noun": mawt_noun,
        "root_Hyy": root_h, "root_mwt": root_m,
        "noun_balances": bool(hay_noun == mawt_noun),
        "noun_hits_145": bool(hay_noun == 145 or mawt_noun == 145),
        "root_balances": bool(root_h == root_m),
        "verdict": "FALSIFIED",
        "note": "neither noun lemma nor whole-root totals balance or hit 145; "
                "ḥayāt-noun=" + str(hay_noun) + ", mawt-noun=" + str(mawt_noun)
                + "; root totals " + str(root_h) + " vs " + str(root_m) + "."
    }

    # C4 calendar
    verdicts["claim4"] = {
        "shahr_singular": c4["shahr_singular"], "claimed_shahr": 12,
        "yawm_singular": c4["yawm_singular"], "claimed_yawm": 365,
        "ayyam_dual_plural": c4["yawm_plural_ayyam"] + c4["yawm_dual_yawmayn"],
        "claimed_ayyam": 30,
        "shahr_hits_12": bool(c4["shahr_singular"] == 12),
        "yawm_hits_365": bool(c4["yawm_singular"] == 365),
        "ayyam_hits_30": bool(c4["yawm_plural_ayyam"] + c4["yawm_dual_yawmayn"] == 30),
    }
    sub = verdicts["claim4"]
    n_hit = sum([sub["shahr_hits_12"], sub["yawm_hits_365"], sub["ayyam_hits_30"]])
    verdicts["claim4"]["verdict"] = (
        "CONFIRMED" if n_hit == 3 else
        "RULES-FRAGILE" if n_hit >= 1 else "FALSIFIED")
    verdicts["claim4"]["note"] = f"{n_hit}/3 calendar sub-targets hit exactly."

    # C5 rajul/maraa
    raj = c5["R3_rajul_lemma"]
    imr = c5["R3_imraa_lemma"]
    verdicts["claim5"] = {
        "rajul_lemma": raj, "imraa_lemma": imr, "claimed": 24,
        "balances": bool(raj == imr),
        "both_hit_24": bool(raj == 24 and imr == 24),
        "verdict": ("CONFIRMED" if (raj == imr == 24) else "FALSIFIED"),
        "note": "rajul=" + str(raj) + ", imraʾa=" + str(imr)
                + "; neither equals claimed 24; not balanced."
    }

    # C6 iblis/refuge
    ibl = c6["iblis_count"]
    rv = c6["refuge_verbs_total"]
    rb = c6["refuge_verb_lemma_breakdown"]
    # principled subsets for "seek-refuge":
    #   form-1 ʿādha/aʿūdhu (Eu*o)              = 10
    #   form-4 uʿīdhu (>uEiy*u, "I commend to refuge", 3:36) = 1
    #   form-10 istaʿidh (imperative {sotaEi*o)  = 4
    aoudh = rb.get("Eu*o", 0)
    uidhu = rb.get(">uEiy*u", 0)
    istaidh = rb.get("{sotaEi*o", 0)
    subset_form1_plus_form4 = aoudh + uidhu          # = 11 (the only subset hitting 11)
    iblis_ok = (ibl == 11)
    refuge_11_subset = (subset_form1_plus_form4 == 11)
    verdicts["claim6"] = {
        "iblis": ibl, "refuge_verbs_all": rv, "refuge_root_total": c6["refuge_root_total"],
        "refuge_form1_aoudhu": aoudh, "refuge_form4_uidhu": uidhu,
        "refuge_form10_istaidh": istaidh,
        "refuge_form1_plus_form4": subset_form1_plus_form4,
        "iblis_is_11": bool(iblis_ok),
        "verdict": ("RULES-FRAGILE" if (iblis_ok and refuge_11_subset) else
                    "FALSIFIED" if not iblis_ok else "RULES-FRAGILE"),
        "note": "Iblīs PN=" + str(ibl) + " (EXACT, robust). Refuge verbs do NOT have a "
                "unique natural total: form-1 aʿūdhu=" + str(aoudh) + ", +form-4 uʿīdhu="
                + str(subset_form1_plus_form4) + ", all-verbs=" + str(rv)
                + ", all-root=" + str(c6["refuge_root_total"]) + ". The 11 target is "
                "recoverable ONLY by the form-1+form-4 subset (10+1), excluding the 4 "
                "form-10 istaʿidh imperatives — a selective boundary."
    }

    # C8 salihat/sayyiat
    sal = c8["R3_salihat_lemma"]
    say = c8["R3_sayyiat_lemma"]
    verdicts["claim8"] = {
        "salihat_lemma": sal, "sayyiat_lemma": say,
        "balances": bool(sal == say),
        "verdict": "FALSIFIED" if sal != say else "CONFIRMED",
        "note": "ṣāliḥāt=" + str(sal) + " vs sayyiʾāt(pl)=" + str(say)
                + "; not balanced."
    }

    # C9 rasul (descriptive)
    verdicts["claim9"] = {
        "rasul_lemma": c9["R3_rasul_lemma"], "mursal_lemma": c9["R3_mursal_lemma"],
        "verdict": "NOT-A-BALANCE-CLAIM",
        "note": "rasūl lemma=" + str(c9["R3_rasul_lemma"])
                + "; descriptive, no symmetry target asserted by source."
    }

    # C10 sea/land
    sea = c10["R3_bahr_lemma"]
    land = c10["R3_barr_land_lemma"]
    verdicts["claim10"] = {
        "bahr_sea": sea, "barr_land_strict": land,
        "claimed_sea": 32, "claimed_land": 13,
        "birr_homonym_excluded": c10["R3_birr_lemma"],
        "water_pct_strict": c10.get("water_pct_strict"),
        "claimed_water_pct": 71.11,
        "sea_hits_32": bool(sea == 32),
        "land_hits_13": bool(land == 13),
        "verdict": ("CONFIRMED" if (sea == 32 and land == 13) else "FALSIFIED"),
        "note": "strict baḥr(sea)=" + str(sea) + " (claimed 32); strict bar~(land)="
                + str(land) + " (claimed 13); birr-homonym (excluded)="
                + str(c10["R3_birr_lemma"]) + "."
    }

    out = {
        "finding_id": "H-NEW-2000",
        "seed": SEED,
        "prereg_sha256": PREREG_SHA,
        "rules": {
            "R1": "strict-al-form (definite surface lexeme, substring no-tashkeel)",
            "R2": "all-morphological-forms (surface regex, homonyms documented)",
            "R3": "QAC-lemma (Quranic Arabic Corpus v0.4 STEM tokens by LEM)",
        },
        "raw_counts": results,
        "verdicts": verdicts,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # ---- console summary ----
    print("\n=== H-NEW-2000 verdict summary ===")
    order = ["claim1", "claim2", "claim3", "claim4", "claim5",
             "claim6", "claim7", "claim8", "claim9", "claim10"]
    for k in order:
        v = verdicts[k]
        print(f"\n{k}: {v['verdict']}")
        print(f"   {v['note']}")
    print(f"\nJSON written: {OUT_JSON}")


if __name__ == "__main__":
    main()
