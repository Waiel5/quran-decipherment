#!/usr/bin/env python3
"""H-NEW-2620 POST-HOC diagnostics. **NOT PRE-REGISTERED.**

Everything computed here was noticed by reading the pre-registered rosters produced by
`h-new-2620.py`. Under Investigation Protocol §1.7 MW-7 these carry a single-test
alpha=0.05 ceiling and NO confirmatory verdict may be issued from them. They are
published because they explain what the pre-registered rosters actually contain.

Reads the immutable pre-registered run; writes to a separate directory. Nothing in the
pre-registered run directory is touched.

Author: Waiel Al-Shujaa.
"""

import json
import math
import os
import random
import re
import sys
from datetime import datetime, timezone

ROOT = "/Users/grey/Downloads/quran"
RUN = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2620/20260807T005200Z")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
SEED = 20260509
N_PERM = 10000

sys.path.insert(0, os.path.join(ROOT, "findings/phase-b-hypotheses/scripts"))
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "h2620", os.path.join(ROOT, "findings/phase-b-hypotheses/scripts/h-new-2620.py"))
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)

WS = re.compile(r"\s+")


def main():
    t0 = datetime.now(timezone.utc)
    outdir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2620",
                          t0.strftime("%Y%m%dT%H%M%SZ") + "-posthoc")
    if os.path.exists(outdir):
        H.die("directory exists: %s" % outdir)

    res = json.load(open(os.path.join(RUN, "result.json"), encoding="utf-8"))
    quran = json.load(open(QURAN, encoding="utf-8"))
    text = {}
    order = []
    for s in quran:
        for v in s["verses"]:
            k = (s["id"], v["id"])
            text[k] = WS.sub(" ", v["text"]).strip()
            order.append(k)

    # ---- verse-level scores from the pre-registered run
    scores = {}
    with open(os.path.join(RUN, "verse-scores.tsv"), encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            f = line.rstrip("\n").split("\t")
            row = dict(zip(hdr, f))
            scores[(int(row["surah"]), int(row["verse"]))] = {
                "A_resid": float(row["A_resid"]), "D_resid": float(row["D_resid"]),
                "DISPUTE_resid": float(row["DISPUTE_resid"]),
            }

    # ---- D1. repetition census
    seen = {}
    is_repeat, rep_count = {}, {}
    counts = {}
    for k in order:
        counts[text[k]] = counts.get(text[k], 0) + 1
    for k in order:
        t = text[k]
        rep_count[k] = counts[t]
        is_repeat[k] = 1 if (t in seen) else 0
        seen.setdefault(t, k)
    n_repeat = sum(is_repeat.values())
    n_distinct = len(counts)

    A = [scores[k]["A_resid"] for k in order]
    rep = [float(is_repeat[k]) for k in order]
    rho_rep = H.spearman(A, rep)

    # permutation null on the repeat label (post-hoc, alpha ceiling 0.05)
    rng = random.Random(SEED)
    perm = list(rep)
    ranksA = H.midranks(A)
    le = 0
    for _ in range(N_PERM):
        rng.shuffle(perm)
        if H.pearson(ranksA, H.midranks(perm)) <= rho_rep:
            le += 1
    p_rep = (1 + le) / (1.0 + N_PERM)

    mean_rep = sum(scores[k]["A_resid"] for k in order if is_repeat[k]) / max(1, n_repeat)
    mean_first = sum(scores[k]["A_resid"] for k in order if not is_repeat[k]) / (len(order) - n_repeat)
    med_rep = H.median([scores[k]["A_resid"] for k in order if is_repeat[k]])
    med_first = H.median([scores[k]["A_resid"] for k in order if not is_repeat[k]])

    # ---- D2. how much of the pre-registered Roster B is repetition?
    rosterB = res["rosters"]["B_structurally_extreme_exegetically_ignored_S590"]
    rosterBp = res["rosters"]["B_prime_structurally_extreme_exegetically_ignored_S840"]

    def repeat_share(roster):
        ks = [(r["surah"], r["verse"]) for r in roster]
        return {
            "n": len(ks),
            "n_repeat_occurrence": sum(is_repeat[k] for k in ks),
            "n_text_occurring_more_than_once": sum(1 for k in ks if rep_count[k] > 1),
            "surahs": sorted({k[0] for k in ks}),
        }

    # ---- D3. dispute-marker lemma echo: does the QURANIC VERSE itself contain a marker?
    self_marker = {k: (1 if H.count_markers(text[k]) > 0 else 0) for k in order}
    P = [scores[k]["DISPUTE_resid"] for k in order]
    sm = [float(self_marker[k]) for k in order]
    rho_echo = H.spearman(P, sm)
    n_self = sum(self_marker.values())
    rosterAp = res["rosters"]["A_prime_most_dispute_markers"]
    echo_in_roster = sum(self_marker[(r["surah"], r["verse"])] for r in rosterAp)

    ranksP = H.midranks(P)
    rng = random.Random(SEED + 1)
    perm = list(sm)
    ge = 0
    for _ in range(N_PERM):
        rng.shuffle(perm)
        if H.pearson(ranksP, H.midranks(perm)) >= rho_echo:
            ge += 1
    p_echo = (1 + ge) / (1.0 + N_PERM)

    # ---- D4. post-hoc corrected roster: first occurrences only
    S590 = {r["surah"]: r["S590_surah"] for r in rosterB}
    res590 = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-590.json"),
                            encoding="utf-8"))["all_surahs_results"]
    s590 = {r["X"]: abs(r["delta_pct"]) for r in res590}
    top28 = set(sorted(s590, key=lambda s: -s590[s])[:28])
    cand = [k for k in order if k[0] in top28 and not is_repeat[k] and rep_count[k] == 1]
    cand.sort(key=lambda k: (scores[k]["A_resid"], k))
    rosterB2 = [{"ref": "Q %d:%d" % k, "surah": k[0], "verse": k[1],
                 "A_resid": scores[k]["A_resid"], "D_resid": scores[k]["D_resid"],
                 "DISPUTE_resid": scores[k]["DISPUTE_resid"],
                 "S590_surah": s590[k[0]], "text": text[k]} for k in cand[:30]]

    # ---- D5. is the mild negative I1 tendency just repetition?
    # Re-run the I1 partial with per-surah repetition rate added as a third nuisance,
    # and again on first-occurrence verses only.
    surah_rep_rate = []
    for s in range(1, 115):
        ks = [k for k in order if k[0] == s]
        surah_rep_rate.append(sum(is_repeat[k] for k in ks) / float(len(ks)))
    S590v = [s590[s] for s in range(1, 115)]
    surah_tokens = [0] * 114
    for k in order:
        surah_tokens[k[0] - 1] += len(text[k].split(" ")) if text[k] else 0

    def agg(vals_by_key, keyset):
        out_ = []
        for s in range(1, 115):
            xs = [vals_by_key[k] for k in keyset if k[0] == s]
            out_.append(H.median(xs) if xs else 0.0)
        return out_

    nuis2 = [H.normal_scores([float(s) for s in range(1, 115)]),
             H.normal_scores([math.log(t) for t in surah_tokens])]
    nuis3 = nuis2 + [H.normal_scores(surah_rep_rate)]

    Aby = {k: scores[k]["A_resid"] for k in order}
    R_all = agg(Aby, order)
    firsts = [k for k in order if not is_repeat[k]]
    R_first = agg(Aby, firsts)

    e2 = H.PartialEngine(nuis2, 114)
    e3 = H.PartialEngine(nuis3, 114)
    i1_registered = e2.corr(e2.prep(H.normal_scores(S590v)), e2.prep(H.normal_scores(R_all)))
    i1_reprate = e3.corr(e3.prep(H.normal_scores(S590v)), e3.prep(H.normal_scores(R_all)))
    i1_firstonly = e2.corr(e2.prep(H.normal_scores(S590v)), e2.prep(H.normal_scores(R_first)))
    rho_S590_reprate = H.spearman(S590v, surah_rep_rate)

    # ---- D6. dispute roster with lemma-echo verses removed
    clean = [k for k in order if not self_marker[k]]
    clean.sort(key=lambda k: (-scores[k]["DISPUTE_resid"], k))
    rosterA2 = [{"ref": "Q %d:%d" % k, "surah": k[0], "verse": k[1],
                 "DISPUTE_resid": scores[k]["DISPUTE_resid"],
                 "A_resid": scores[k]["A_resid"], "text": text[k]} for k in clean[:30]]

    out = {
        "id": "H-NEW-2620-POSTHOC",
        "status": "POST-HOC — not pre-registered; MW-7 single-test alpha=0.05 ceiling; "
                  "no confirmatory verdict may be issued from this file",
        "source_run": os.path.relpath(RUN, ROOT),
        "seed": SEED, "n_perm": N_PERM,
        "D1_repetition": {
            "distinct_verse_texts": n_distinct,
            "verses_that_are_a_later_occurrence": n_repeat,
            "pct_of_corpus": round(100.0 * n_repeat / len(order), 2),
            "spearman_A_resid_vs_is_repeat": rho_rep,
            "p_one_sided_negative_posthoc": p_rep,
            "median_A_resid_later_occurrence": med_rep,
            "median_A_resid_first_occurrence": med_first,
            "mean_A_resid_later_occurrence": mean_rep,
            "mean_A_resid_first_occurrence": mean_first,
        },
        "D2_roster_B_composition": {
            "B_S590": repeat_share(rosterB),
            "B_prime_S840": repeat_share(rosterBp),
        },
        "D3_dispute_lemma_echo": {
            "verses_whose_own_text_contains_a_marker_word": n_self,
            "pct_of_corpus": round(100.0 * n_self / len(order), 2),
            "spearman_DISPUTE_resid_vs_self_marker": rho_echo,
            "p_one_sided_positive_posthoc": p_echo,
            "roster_A_prime_top30_with_self_marker": echo_in_roster,
        },
        "D4_roster_B2_first_occurrence_only": rosterB2,
        "D5_is_I1_just_repetition": {
            "I1_as_registered": i1_registered,
            "I1_plus_surah_repetition_rate_nuisance": i1_reprate,
            "I1_first_occurrence_verses_only": i1_firstonly,
            "spearman_S590_vs_surah_repetition_rate": rho_S590_reprate,
        },
        "D6_roster_A2_dispute_lemma_echo_removed": rosterA2,
    }

    os.makedirs(outdir)
    with open(os.path.join(outdir, "posthoc.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    print("[D1] distinct verse texts %d; later-occurrence verses %d (%.2f%%)"
          % (n_distinct, n_repeat, 100.0 * n_repeat / len(order)))
    print("[D1] rho(A_resid, is_repeat) = %+.4f  p(one-sided neg, post-hoc) = %.5f"
          % (rho_rep, p_rep))
    print("[D1] median A_resid: later-occurrence %+.4f vs first-occurrence %+.4f"
          % (med_rep, med_first))
    print("[D2] Roster B : %d/30 are later occurrences; %d/30 have text appearing >1x; surahs %s"
          % (out["D2_roster_B_composition"]["B_S590"]["n_repeat_occurrence"],
             out["D2_roster_B_composition"]["B_S590"]["n_text_occurring_more_than_once"],
             out["D2_roster_B_composition"]["B_S590"]["surahs"]))
    print("[D2] Roster B': %d/30 are later occurrences; %d/30 have text appearing >1x; surahs %s"
          % (out["D2_roster_B_composition"]["B_prime_S840"]["n_repeat_occurrence"],
             out["D2_roster_B_composition"]["B_prime_S840"]["n_text_occurring_more_than_once"],
             out["D2_roster_B_composition"]["B_prime_S840"]["surahs"]))
    print("[D3] %d verses (%.2f%%) contain a dispute-marker word in their OWN text"
          % (n_self, 100.0 * n_self / len(order)))
    print("[D3] rho(DISPUTE_resid, self_marker) = %+.4f  p(one-sided pos, post-hoc) = %.5f"
          % (rho_echo, p_echo))
    print("[D3] %d of the top-30 DISPUTE roster carry a marker in their own verse" % echo_in_roster)
    print("[D4] corrected roster (first occurrences only): top 5")
    for r in rosterB2[:5]:
        print("     %-9s A_resid=%+.3f  %s" % (r["ref"], r["A_resid"], r["text"][:60]))
    print("[D5] I1 as registered            = %+.4f" % i1_registered)
    print("[D5] I1 + surah-repetition-rate  = %+.4f" % i1_reprate)
    print("[D5] I1 first-occurrence verses  = %+.4f" % i1_firstonly)
    print("[D5] rho(S590, surah repetition rate) = %+.4f" % rho_S590_reprate)
    print("[D6] dispute roster with lemma-echo verses removed: top 8")
    for r in rosterA2[:8]:
        print("     %-9s DISP=%+.3f  %s" % (r["ref"], r["DISPUTE_resid"], r["text"][:58]))
    print("[done] %s" % outdir)


if __name__ == "__main__":
    main()
