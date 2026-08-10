#!/usr/bin/env python3
"""
H-NEW-3130 ADDENDUM — POST-HOC, NOT PRE-REGISTERED, NOT VERDICT-BEARING.

Three arms requested by the lead AFTER the confirmatory run had already executed. The
pre-registration is immutable once run (standing rule, 2026-08-08 #1), so none of this can
enter the confirmatory family; it is published as an addendum to the finding instead.

  A. The h-new-2500 SUBSTRING register proxy as a second label source, against the
     scholar-assigned Neuwirth-Sinai labels used as primary. If the two disagree, that
     disagreement is a result about the proxy.
  B. The profile computed WITHOUT Form I. Form I is 12,347 of 19,356 verbs (63.8%) and is a
     DERIVED category (QAC tags no verb `(I)`), so any statistic over "all forms including I"
     is dominated by an inference rather than a reading.
  C. A bound on the heterogeneity of the untagged set: how many untagged verbs are
     demonstrably derived forms QAC failed to tag.

Writes to runs/h-new-3130-addendum/<UTC>/.
"""

import collections
import datetime
import importlib.util
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("h3130", os.path.join(HERE, "h-new-3130.py"))
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

QURAN_JSON = "quran-text/quran-no-tashkeel.json"
LEGAL_MARKERS = ["يا أيها الذين آمنوا", "كتب عليكم"]
ESCHAT_MARKERS = ["يوم القيامة", "الساعة", "يومئذ", "جهنم", "إذا "]
QALA = "قال"
SHORT_MUFASSAL_S = 78
HAMZA = set("A'><}{&")


def proxy_labels(path):
    """Reimplementation of h-new-2500.py's LOCKED hierarchical genre proxy (lines 60-78)."""
    quran = json.load(open(path, encoding="utf-8"))
    meta = {s["id"]: s["type"] for s in quran}
    txt = {s["id"]: [v["text"] for v in s["verses"]] for s in quran}
    out = {}
    counts = {}
    for sid in range(1, 115):
        w = sum(len(t.split()) for t in txt[sid])
        leg = sum(sum(t.count(p) for t in txt[sid]) for p in LEGAL_MARKERS)
        escd = 100.0 * sum(sum(t.count(p) for t in txt[sid]) for p in ESCHAT_MARKERS) / w
        nard = 100.0 * sum(t.count(QALA) for t in txt[sid]) / w
        counts[sid] = {"legal_marker_hits": leg, "eschat_density": escd, "qala_density": nard}
        if meta[sid] == "medinan" and leg >= 1:
            out[sid] = "legal_medinan"
        elif nard >= 1.0:
            out[sid] = "narrative"
        elif sid >= SHORT_MUFASSAL_S or escd >= 1.5:
            out[sid] = "eschatological_mufassal"
        else:
            out[sid] = "liturgical_didactic"
    return out, counts


def untagged_bound(path):
    """(C) How much of the untagged verb set is demonstrably NOT Form I."""
    untag = collections.Counter()
    root_of, asp_of = {}, collections.defaultdict(set)
    nverb = 0
    for line in open(path, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) != 4 or p[0].startswith("LOCATION") or p[0].startswith("#"):
            continue
        f = p[3]
        if "POS:V" not in f:
            continue
        nverb += 1
        lm = re.search(r"LEM:([^|]+)", f)
        rm = re.search(r"ROOT:([^|]+)", f)
        if not lm or not rm:
            continue
        if M.FORM_RE.search(f):
            continue
        lem = lm.group(1)
        untag[lem] += 1
        root_of[lem] = rm.group(1)
        asp_of[lem].add("PERF" if "|PERF|" in f else ("IMPF" if "|IMPF|" in f else "IMPV"))

    def diagnose(lem, root):
        r0 = root[0] if root else ""
        # Unambiguous: these strings cannot be an inflectional prefix.
        if lem.startswith("{sot") or lem.startswith("{st"):
            return "X (ista-)"
        if lem.startswith("{n") and r0 != "n":
            return "VII (in-)"
        if lem.startswith("{") and re.match(r"\{.t", lem) and r0 != "t":
            return "VIII (infixed -t-)"
        # `>a-` is also the 1sg imperfect prefix and `ta-` the 2/3-person imperfect prefix,
        # so these are diagnostic ONLY on a lemma attested in the perfect.
        if "PERF" not in asp_of[lem]:
            return None
        if (lem.startswith(">a") or lem.startswith("'aA") or lem.startswith("A^")) \
                and r0 not in HAMZA:
            return "IV (a-)"
        if lem.startswith("ta") and r0 != "t":
            return "V/VI (ta-)"
        return None

    hits = {}
    for lem in untag:
        d = diagnose(lem, root_of[lem])
        if d:
            hits[lem] = {"root": root_of[lem], "n": untag[lem], "diagnosis": d,
                         "attested": sorted(asp_of[lem])}
    tok = sum(v["n"] for v in hits.values())
    return {
        "untagged_lemmas": len(untag), "untagged_tokens": sum(untag.values()),
        "all_verb_tokens": nverb,
        "confirmed_mistagged_lemmas": len(hits), "confirmed_mistagged_tokens": tok,
        "pct_of_untagged": 100.0 * tok / sum(untag.values()),
        "pct_of_all_verbs": 100.0 * tok / nverb,
        "detail": hits,
    }


def arms_for(P_ch, lenvars, y, keep, nar, leg, iIV, iVVI,
             surah_idx, form_idx, root_id, n_forms, channels, n_perm):
    """H1/D1/D2 under Null A (label shuffle) and Null B (within-root form shuffle)."""
    obs = {
        "H1": {c: M.loo_nearest_centroid_accuracy(P_ch[c], y, keep) for c in lenvars},
        "D1": {c: M.group_diff(P_ch[c], iIV, nar, keep) for c in lenvars},
        "D2": {c: M.group_diff(P_ch[c], iVVI, leg, keep) for c in lenvars},
    }
    kidx = np.where(keep)[0]
    rngA = np.random.default_rng(M.SEED_NULL_A)
    nA = {k: {c: np.empty(n_perm) for c in lenvars} for k in ("H1", "D1", "D2")}
    for i in range(n_perm):
        perm = rngA.permutation(kidx)
        y_p = y.copy(); y_p[kidx] = y[perm]
        n_p = nar.copy(); n_p[kidx] = nar[perm]
        l_p = leg.copy(); l_p[kidx] = leg[perm]
        for c in lenvars:
            nA["H1"][c][i] = M.loo_nearest_centroid_accuracy(P_ch[c], y_p, keep)
            nA["D1"][c][i] = M.group_diff(P_ch[c], iIV, n_p, keep)
            nA["D2"][c][i] = M.group_diff(P_ch[c], iVVI, l_p, keep)
    rngB = np.random.default_rng(M.SEED_NULL_B)
    nB = {k: {c: np.empty(n_perm) for c in lenvars} for k in ("H1", "D1", "D2")}
    for i in range(n_perm):
        f_p = M.within_root_shuffle(form_idx, root_id, rngB)
        P_p = M.profiles_from_counts(M.counts_matrix(surah_idx, f_p, n_forms))
        Pc = channels(P_p)
        for c in lenvars:
            nB["H1"][c][i] = M.loo_nearest_centroid_accuracy(Pc[c], y, keep)
            nB["D1"][c][i] = M.group_diff(Pc[c], iIV, nar, keep)
            nB["D2"][c][i] = M.group_diff(Pc[c], iVVI, leg, keep)
    out = {}
    for stat in ("H1", "D1", "D2"):
        for tag, nulls in (("RAW", nA), ("ROOT", nB)):
            p = {c: M.empirical_p_one_sided(obs[stat][c], nulls[stat][c]) for c in lenvars}
            out["%s-%s" % (stat, tag)] = {
                "observed": obs[stat], "p_by_channel": p,
                "p_worst": max(p.values()), "p_best": min(p.values()),
                "null_mean": {c: float(np.mean(nulls[stat][c])) for c in lenvars},
            }
    return out


def main():
    M.self_check()
    qac = os.path.join(M.REPO, M.QAC_REL)
    toks = M.parse_qac(qac)
    genre = M.load_genre(os.path.join(M.REPO, M.GENRE_REL))
    lens = M.surah_lengths(qac)
    n_perm = M.N_PERM

    lenvars = {
        "L0": None,
        "L1": np.log(np.array([max(lens[s]["verses"], 1) for s in range(1, 115)], float)),
        "L2": np.log(np.array([max(lens[s]["words"], 1) for s in range(1, 115)], float)),
        "L3": np.log(np.array([max(lens[s]["mean_verse_len"], 1e-9) for s in range(1, 115)],
                              float)),
    }

    def channels(P):
        return {c: (P if x is None else M.residualise(P, x)) for c, x in lenvars.items()}

    # ---------------- A. the h-new-2500 substring proxy as a second label source
    prox, prox_counts = proxy_labels(os.path.join(M.REPO, QURAN_JSON))
    sinai = {s: M.coarsen(genre[s]["sinai"], M.C1_ORDER) for s in range(1, 115)}
    # agreement on the two constructs the proxy and the scholar labels share
    agree_nar = sum(1 for s in range(1, 115)
                    if (prox[s] == "narrative") == (sinai[s] == "narrative"))
    agree_leg = sum(1 for s in range(1, 115)
                    if (prox[s] == "legal_medinan") == (sinai[s] == "legal"))
    cross = collections.defaultdict(collections.Counter)
    for s in range(1, 115):
        cross[prox[s]][sinai[s]] += 1

    surah_idx, form_idx, root_id, forms = M.build_token_arrays(toks, "T1", None, False)
    counts = M.counts_matrix(surah_idx, form_idx, len(forms))
    P = M.profiles_from_counts(counts)
    P_ch = channels(P)
    iIV = [forms.index("IV")]
    iVVI = [forms.index(f) for f in ("V", "VI")]

    classes_p = sorted(set(prox.values()))
    cmap_p = {c: i for i, c in enumerate(classes_p)}
    y_p = np.array([cmap_p[prox[s]] for s in range(1, 115)])
    keep = counts.sum(axis=1) > 0
    nar_p = np.array([prox[s] == "narrative" for s in range(1, 115)])
    leg_p = np.array([prox[s] == "legal_medinan" for s in range(1, 115)])
    arms_proxy = arms_for(P_ch, lenvars, y_p, keep, nar_p, leg_p, iIV, iVVI,
                          surah_idx, form_idx, root_id, len(forms), channels, n_perm)

    # ---------------- B. profile WITHOUT Form I
    keep_forms = [i for i, f in enumerate(forms) if f != "I"]
    forms_noI = [forms[i] for i in keep_forms]
    counts_noI = counts[:, keep_forms]
    P_noI = M.profiles_from_counts(counts_noI)
    P_noI_ch = channels(P_noI)
    mask_noI = np.isin(form_idx, keep_forms)
    si2, fi2, ri2 = surah_idx[mask_noI], form_idx[mask_noI], root_id[mask_noI]
    remap = {old: new for new, old in enumerate(keep_forms)}
    fi2 = np.array([remap[v] for v in fi2], dtype=np.int64)
    order = np.argsort(ri2, kind="stable")
    si2, fi2, ri2 = si2[order], fi2[order], ri2[order]

    def channels_noI(Pm):
        return {c: (Pm if x is None else M.residualise(Pm, x)) for c, x in lenvars.items()}

    iIV2 = [forms_noI.index("IV")]
    iVVI2 = [forms_noI.index(f) for f in ("V", "VI")]
    sinai_classes = sorted([c for c, n in collections.Counter(sinai.values()).items()
                            if n >= M.CLASS_MIN])
    cmap_s = {c: i for i, c in enumerate(sinai_classes)}
    y_s = np.array([cmap_s.get(sinai[s], -1) for s in range(1, 115)])
    keep_noI = (y_s >= 0) & (counts_noI.sum(axis=1) > 0) & np.isfinite(P_noI).all(axis=1)
    nar_s = np.array([sinai[s] == "narrative" for s in range(1, 115)])
    leg_s = np.array([sinai[s] == "legal" for s in range(1, 115)])
    arms_noI = arms_for(P_noI_ch, lenvars, y_s, keep_noI, nar_s, leg_s, iIV2, iVVI2,
                        si2, fi2, ri2, len(forms_noI), channels_noI, n_perm)

    # ---------------- C. untagged-set bound
    bound = untagged_bound(qac)

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(M.REPO, "findings/phase-b-hypotheses/runs/h-new-3130-addendum", stamp)
    os.makedirs(run_dir, exist_ok=False)
    payload = {
        "status": "POST-HOC ADDENDUM — NOT PRE-REGISTERED, NOT VERDICT-BEARING",
        "reason": "requested after the confirmatory run; the prereg is immutable once run",
        "parent_run": "runs/h-new-3130/20260809T090605Z",
        "A_proxy": {
            "proxy_class_sizes": dict(collections.Counter(prox.values())),
            "proxy_vs_sinai_crosstab": {k: dict(v) for k, v in cross.items()},
            "agreement_narrative_of_114": agree_nar,
            "agreement_legal_of_114": agree_leg,
            "arms": arms_proxy,
        },
        "B_no_form_I": {"forms": forms_noI, "arms": arms_noI},
        "C_untagged_bound": bound,
    }
    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print("ADDENDUM run: %s" % run_dir)
    print()
    print("A. h-new-2500 SUBSTRING PROXY vs Neuwirth-Sinai")
    print("   proxy classes:", dict(collections.Counter(prox.values())))
    print("   agreement on 'narrative': %d/114 (%.1f%%)   on 'legal': %d/114 (%.1f%%)"
          % (agree_nar, 100 * agree_nar / 114, agree_leg, 100 * agree_leg / 114))
    for k in ("H1-RAW", "H1-ROOT", "D1-RAW", "D1-ROOT", "D2-RAW", "D2-ROOT"):
        a = arms_proxy[k]
        print("   %-9s obs_L0=%+.4f  p_worst=%.5f  p_best=%.5f" %
              (k, a["observed"]["L0"], a["p_worst"], a["p_best"]))
    print()
    print("B. PROFILE WITHOUT FORM I (forms %s)" % ",".join(forms_noI))
    for k in ("H1-RAW", "H1-ROOT", "D1-RAW", "D1-ROOT", "D2-RAW", "D2-ROOT"):
        a = arms_noI[k]
        print("   %-9s obs_L0=%+.4f  p_worst=%.5f  p_best=%.5f" %
              (k, a["observed"]["L0"], a["p_worst"], a["p_best"]))
    print()
    print("C. UNTAGGED-SET BOUND")
    print("   untagged: %d lemmas / %d tokens" % (bound["untagged_lemmas"],
                                                  bound["untagged_tokens"]))
    print("   demonstrably mis-tagged derived forms: %d lemmas / %d tokens "
          "= %.2f%% of untagged, %.2f%% of all verbs"
          % (bound["confirmed_mistagged_lemmas"], bound["confirmed_mistagged_tokens"],
             bound["pct_of_untagged"], bound["pct_of_all_verbs"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
