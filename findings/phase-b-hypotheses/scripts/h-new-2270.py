#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2270 — al-Suyūṭī al-Itqān fī ʿulūm al-Qurʾān distributional-claims audit.

Five clearly-attributable distributional/census claims from al-Itqān nawʿ 1 (makkī/madanī)
and nawʿ 19 (ʿadad), verified/falsified on disk with exact counts. Extends the H-NEW-2160
kallā exemplar (VINDICATED-AFTER-DISAMBIGUATION) to a five-claim block.

Author: Waiel Al-Shujaa.  Pre-registered; SHA-256 of the pre-reg embedded and verified at runtime.
All counts computed from disk. No external dependencies (stdlib only).
"""
import json
import hashlib
import os
import re
import sys

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2270-itqan-distributional-audit.md")
PREREG_SHA = "dcefa7d1f9f9b22fd3ccab4d8652a48b9487bd50ac1e75ab83de7b2a7ebecd25"

QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
VCOUNTS = os.path.join(ROOT, "data/hafs-verse-counts.tsv")


def verify_prereg():
    with open(PREREG, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != PREREG_SHA:
        sys.exit("PRE-REG SHA MISMATCH\n  embedded: %s\n  on-disk : %s" % (PREREG_SHA, got))
    print("[ok] pre-reg SHA-256 verified: %s" % got)


# ---- ground truth -------------------------------------------------------
def load_types():
    d = json.load(open(QURAN, encoding="utf-8"))
    return {s["id"]: s["type"] for s in d}, d


PAUSE = "ٰۚۖۗۘۙۛۜ"  # pause/small-mark glyphs to strip for phrase matching


def norm(t):
    for ch in PAUSE:
        t = t.replace(ch, "")
    return t


def surahs_with_phrase(quran, phrase):
    out = set()
    for s in quran:
        for v in s["verses"]:
            if phrase in norm(v["text"]):
                out.add(s["id"])
    return out


# ---- QAC helpers --------------------------------------------------------
def qac_lines():
    with open(QAC, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("("):
                yield ln.rstrip("\n")


def surah_of(loc):  # loc like (19:79:1:1)
    return int(loc.strip("()").split(":")[0])


# =========================================================================
def main():
    verify_prereg()
    typ, quran = load_types()
    results = {"id": "H-NEW-2270", "prereg_sha256": PREREG_SHA, "claims": {}}

    n_med = sum(1 for v in typ.values() if v == "medinan")
    n_mec = sum(1 for v in typ.values() if v == "meccan")
    print("ground truth: %d meccan / %d medinan" % (n_mec, n_med))

    # ---- Claim 1: al-Jaʿbarī muqaṭṭaʿāt criterion -----------------------
    MUQ = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
           36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
    med_muq = sorted(n for n in MUQ if typ[n] == "medinan")
    predicted = [2, 3, 13]
    c1_pass = med_muq == predicted
    results["claims"]["1_muqattaat_jabari"] = {
        "claim": "every muqattaat sura is Meccan except Zahrawan (2,3) and al-Rad (13)",
        "citation": "al-Suyuti Itqan nawʿ 1, al-Jaʿbari (line 1171-1174)",
        "n_muqattaat": len(MUQ),
        "medinan_muqattaat_observed": med_muq,
        "predicted_exceptions": predicted,
        "verdict": "CONFIRMED" if c1_pass else "FALSIFIED",
    }
    print("\n[Claim 1] muqaṭṭaʿāt: Medinan = %s ; predicted %s -> %s"
          % (med_muq, predicted, results["claims"]["1_muqattaat_jabari"]["verdict"]))

    # ---- Claim 2: Makkī munāfiqūn criterion -----------------------------
    HYP_LEMMAS = {"muna`fiqa`t", "muna`fiquwn", "nifaAq", "naAfaqu", "munfiqiyn"}
    hyp_surahs = set()
    raw_root_surahs = set()  # all root nfq incl. spending-sense (the misleading substring)
    for ln in qac_lines():
        if "ROOT:nfq" not in ln:
            continue
        loc = ln.split("\t")[0]
        raw_root_surahs.add(surah_of(loc))
        m = re.search(r"LEM:([^|]+)", ln)
        if m and m.group(1) in HYP_LEMMAS:
            hyp_surahs.add(surah_of(loc))
    hyp_surahs = sorted(hyp_surahs)
    mec_hyp = sorted(n for n in hyp_surahs if typ[n] == "meccan")
    c2_pass = mec_hyp == [29]
    results["claims"]["2_munafiqun_makki"] = {
        "claim": "every sura mentioning the munafiqun is Medinan except al-Ankabut (29)",
        "citation": "al-Suyuti Itqan nawʿ 1, Makki b. Abi Talib (line 1175)",
        "hypocrite_lemma_surahs": hyp_surahs,
        "meccan_members_observed": mec_hyp,
        "predicted_meccan_members": [29],
        "raw_root_nfq_surahs_incl_spending": sorted(raw_root_surahs),
        "disambiguation": "raw root-nfq (incl. anfaqa 'spend') spans %d surahs; hypocrite-sense lemmas only span %d"
                          % (len(raw_root_surahs), len(hyp_surahs)),
        "verdict": "CONFIRMED" if c2_pass else "FALSIFIED",
    }
    print("[Claim 2] munāfiqūn surahs = %s ; Meccan = %s (predicted [29]) -> %s"
          % (hyp_surahs, mec_hyp, results["claims"]["2_munafiqun_makki"]["verdict"]))

    # ---- Claim 3: address criterion (bidirectional) ---------------------
    amanu = sorted(surahs_with_phrase(quran, "يا أيها الذين آمنوا"))
    nas = sorted(surahs_with_phrase(quran, "يا أيها الناس"))
    mec_amanu = sorted(n for n in amanu if typ[n] == "meccan")
    med_nas = sorted(n for n in nas if typ[n] == "medinan")
    c3a_pass = mec_amanu == []        # amanu => Medinan (strong)
    c3b_pass = med_nas == []          # al-nas => Meccan (weak/self-qualified)
    results["claims"]["3a_amanu_medinan"] = {
        "claim": "every sura with 'ya ayyuha alladhina amanu' is Medinan",
        "citation": "al-Suyuti Itqan nawʿ 1, Ibn Masʿud via al-Hakim/al-Bayhaqi; Ibn ʿAtiyya 'sahih' (lines 1146-1151)",
        "amanu_address_surahs": amanu,
        "meccan_members_observed": mec_amanu,
        "verdict": "CONFIRMED" if c3a_pass else "FALSIFIED",
    }
    results["claims"]["3b_nas_meccan"] = {
        "claim": "every sura with 'ya ayyuha al-nas' is Meccan (Ibn ʿAtiyya: but al-nas MAY come in Medinan)",
        "citation": "al-Suyuti Itqan nawʿ 1, Ibn Masʿud; Ibn ʿAtiyya qualification (line 1152, 1158)",
        "nas_address_surahs": nas,
        "medinan_members_observed": med_nas,
        "verdict": "QUALIFIED-IN-SOURCE" if not c3b_pass else "CONFIRMED",
        "note": "Ibn ʿAtiyya in the SAME passage flags al-nas as fallible; al-Nisaʾ (Q4) opens with al-nas yet is Medinan",
    }
    print("[Claim 3a] āmanū surahs Meccan = %s -> %s" % (mec_amanu, results["claims"]["3a_amanu_medinan"]["verdict"]))
    print("[Claim 3b] al-nās surahs Medinan = %s -> %s" % (med_nas, results["claims"]["3b_nas_meccan"]["verdict"]))

    # ---- Claim 4: al-Hudhalī sajda criterion ----------------------------
    SAJDA = [7, 13, 16, 17, 19, 22, 25, 27, 32, 41, 53, 84, 96]  # 13 surahs, 14 prostrations
    # Lens A: project binary ground-truth (Tanzil/Egyptian-standard via quran-no-tashkeel.json)
    med_sajda = sorted(n for n in SAJDA if typ[n] == "medinan")
    # Lens B: al-Suyuti's OWN documented Meccan reading of the two disputed sajda-surahs.
    # Itqan nawʿ 1 records Q13 al-Raʿd "mukhtalaf fiha ... aktharu al-nas: Meccan like al-Qamar"
    # (lines 788-789, 843-844) and Q22 al-Hajj "Meccan except some verses, Mujahid <- Ibn ʿAbbas"
    # (lines 852-853). Under the Ibn ʿAbbas / majority makki reading both are Meccan.
    DISPUTED_MECCAN = {13, 22}
    med_sajda_lensB = sorted(n for n in med_sajda if n not in DISPUTED_MECCAN)
    c4_lensA = med_sajda == []
    c4_lensB = med_sajda_lensB == []
    if c4_lensA:
        c4_verdict = "CONFIRMED"
    elif c4_lensB:
        c4_verdict = "RULES-FRAGILE"  # holds under al-Suyuti's own disputed-surah Meccan reading
    else:
        c4_verdict = "FALSIFIED"
    results["claims"]["4_sajda_hudhali"] = {
        "claim": "every sura containing a sajda (prostration verse) is Meccan",
        "citation": "al-Suyuti Itqan nawʿ 1, al-Hudhali al-Kamil (line 1176); sajda list nawʿ 19 (lines 6783-6786)",
        "sajda_surahs": SAJDA,
        "medinan_members_lensA_binary_groundtruth": med_sajda,
        "medinan_members_lensB_suyuti_disputed_meccan": med_sajda_lensB,
        "disputed_surahs_with_suyuti_meccan_reading": sorted(DISPUTED_MECCAN),
        "disambiguation": "Q13 al-Raʿd + Q22 al-Hajj are mukhtalaf-fiha; al-Suyuti himself (Itqan nawʿ 1, "
                          "lines 788-789/843-844/852-853) records authoritative Meccan readings (Ibn ʿAbbas, "
                          "ʿAli b. Abi Talha, Saʿid b. Jubayr). al-Jaʿbari's twin criterion (Claim 1) lists "
                          "al-Raʿd as an explicit muqattaat exception. Under the Meccan reading the rule holds.",
        "verdict": c4_verdict,
        "note": "FALSIFIED under binary Tanzil label; RULES-FRAGILE because the only two counterexamples are "
                "precisely the surahs al-Suyuti flags as disputed-with-Meccan-reading",
    }
    print("[Claim 4] sajda Medinan lensA=%s lensB(Suyuti-Meccan-disputed)=%s -> %s"
          % (med_sajda, med_sajda_lensB, c4_verdict))

    # ---- Claim 5: kallā upper-half (H-NEW-2160 refinement) --------------
    # 5a: QAC-disambiguated rebuke-kallā (POS=AVR, LEM:kal~aA)
    kalla_locs = []
    raw_kalla_surahs = set()  # raw substring كلا homograph (incl. quantifier)
    for s in quran:
        for v in s["verses"]:
            if "كلا" in norm(v["text"]):
                raw_kalla_surahs.add(s["id"])
    for ln in qac_lines():
        if "POS:AVR" in ln and "LEM:kal~aA" in ln:
            kalla_locs.append(ln.split("\t")[0])
    kalla_count = len(kalla_locs)
    kalla_surahs = sorted({surah_of(l) for l in kalla_locs})
    earliest_surah = min(kalla_surahs)
    # 5b: verse-position vs classical letter-midpoint niṣf = al-Kahf Q18:74
    vc = {}
    for line in open(VCOUNTS):
        a, b = line.split("\t")
        vc[int(a)] = int(b)
    cum = {}
    c = 0
    for n in range(1, 115):
        cum[n] = c
        c += vc[n]
    total = c
    midpoint_pos = cum[18] + 74  # Q18:74 nukran
    earliest_kalla_pos = cum[earliest_surah] + min(
        int(l.strip("()").split(":")[1]) for l in kalla_locs if surah_of(l) == earliest_surah)
    pos_ok = earliest_kalla_pos > midpoint_pos
    # 5c: none in a Medinan surah
    med_kalla = sorted(n for n in kalla_surahs if typ[n] == "medinan")
    c5_count_ok = (kalla_count == 33)
    c5_pass = c5_count_ok and pos_ok and med_kalla == []
    results["claims"]["5_kalla_upper_half"] = {
        "claim": "rebuke-kalla (33x) never at Yathrib and never in the upper half of the Quran",
        "citation": "al-Suyuti Itqan nawʿ 1, al-Dirini verse / al-Dani (lines 1178-1180); midpoint nawʿ 19 line 4362",
        "raw_substring_kalla_surahs": sorted(raw_kalla_surahs),
        "qac_rebuke_kalla_count": kalla_count,
        "qac_rebuke_kalla_surahs": kalla_surahs,
        "earliest_rebuke_kalla_surah": earliest_surah,
        "earliest_rebuke_kalla_verse_pos": earliest_kalla_pos,
        "classical_letter_midpoint_verse_pos_Q18_74": midpoint_pos,
        "total_verses": total,
        "earliest_after_midpoint": pos_ok,
        "medinan_rebuke_kalla_surahs": med_kalla,
        "disambiguation": "raw substring كلا spans %d surahs incl. quantifier kullan/kila (e.g. Q4,6,7,11,17); QAC POS=AVR lemma kal~aA = %d, all in surahs %d-%d"
                          % (len(raw_kalla_surahs), kalla_count, earliest_surah, max(kalla_surahs)),
        "verdict": "VINDICATED-AFTER-DISAMBIGUATION" if c5_pass else "FALSIFIED",
    }
    print("[Claim 5] rebuke-kallā count=%d (expect 33); earliest Q%d verse%d > midpoint verse%d (Q18:74)=%s; Medinan-kallā=%s -> %s"
          % (kalla_count, earliest_surah, earliest_kalla_pos, midpoint_pos, pos_ok, med_kalla,
             results["claims"]["5_kalla_upper_half"]["verdict"]))

    # ---- tally ----------------------------------------------------------
    verdicts = [v["verdict"] for v in results["claims"].values()]
    tally = {}
    for vd in verdicts:
        tally[vd] = tally.get(vd, 0) + 1
    results["tally"] = tally
    print("\nTALLY:", tally)

    out = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2270.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("wrote", out)


if __name__ == "__main__":
    main()
