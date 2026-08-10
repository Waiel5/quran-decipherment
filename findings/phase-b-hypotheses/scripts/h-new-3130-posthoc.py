#!/usr/bin/env python3
"""
H-NEW-3130 POST-HOC — NOT VERDICT-BEARING, NOT PRE-REGISTERED.

Three quantities the confirmatory run does not contain, published separately so they can
never be mistaken for registered results:

  (1) a p-value for the ROOT-B (residualised-profile) H1 arm. My pre-registration §4.3
      registered ROOT-B for D1 and D2 and registered only an *observed* accuracy for H1,
      with no null. That is a defect in the pre-registration, not in the runner. The gap
      matters because ROOT-A and ROOT-B disagree in DEGREE and only ROOT-A carries a p.
  (2) per-register descriptive form shares — why D1 reversed.
  (3) the per-register confusion of the H1 classifier — what the 33.6% is actually made of.

Writes to runs/h-new-3130-posthoc/<UTC>/. Reuses the confirmatory runner by import so the
extraction, coarsening and statistics are literally the same code.
"""

import collections
import datetime
import importlib.util
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("h3130", os.path.join(HERE, "h-new-3130.py"))
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

SEED_POSTHOC = 20260509     # same register-shuffle seed as Null A


def main():
    M.self_check()
    qac = os.path.join(M.REPO, M.QAC_REL)
    toks = M.parse_qac(qac)
    genre = M.load_genre(os.path.join(M.REPO, M.GENRE_REL))
    lens = M.surah_lengths(qac)

    surah_idx, form_idx, root_id, forms = M.build_token_arrays(toks, "T1", None, False)
    counts = M.counts_matrix(surah_idx, form_idx, len(forms))
    P = M.profiles_from_counts(counts)
    E = M.loso_root_expected(surah_idx, form_idx, root_id, len(forms))
    D = P - E

    lab = [M.coarsen(genre[s]["sinai"], M.C1_ORDER) for s in range(1, 115)]
    sizes = collections.Counter(lab)
    classes = sorted([c for c, n in sizes.items() if n >= M.CLASS_MIN])
    cmap = {c: i for i, c in enumerate(classes)}
    y = np.array([cmap.get(l, -1) for l in lab])
    keep = (y >= 0) & (counts.sum(axis=1) > 0) & np.isfinite(P).all(axis=1)

    lenvars = {
        "L0": None,
        "L1": np.log(np.array([max(lens[s]["verses"], 1) for s in range(1, 115)], float)),
        "L2": np.log(np.array([max(lens[s]["words"], 1) for s in range(1, 115)], float)),
        "L3": np.log(np.array([max(lens[s]["mean_verse_len"], 1e-9) for s in range(1, 115)],
                              float)),
    }

    # (1) ROOT-B H1 with a null
    out_h1 = {}
    for ch, x in lenvars.items():
        Dc = D if x is None else M.residualise(D, x)
        Pc = P if x is None else M.residualise(P, x)
        obs_d = M.loo_nearest_centroid_accuracy(Dc, y, keep)
        obs_p = M.loo_nearest_centroid_accuracy(Pc, y, keep)
        rng = np.random.default_rng(SEED_POSTHOC)
        kidx = np.where(keep)[0]
        null = np.empty(M.N_PERM)
        for i in range(M.N_PERM):
            perm = rng.permutation(kidx)
            y_p = y.copy()
            y_p[kidx] = y[perm]
            null[i] = M.loo_nearest_centroid_accuracy(Dc, y_p, keep)
        out_h1[ch] = {
            "accuracy_raw_profile": obs_p,
            "accuracy_root_residualised": obs_d,
            "null_mean": float(null.mean()), "null_sd": float(null.std()),
            "p_label_shuffle": M.empirical_p_one_sided(obs_d, null),
        }

    # (2) per-register descriptive shares
    iIV = forms.index("IV")
    iV, iVI = forms.index("V"), forms.index("VI")
    desc = {}
    for c in sorted(set(lab)):
        rows = [s for s in range(114) if lab[s] == c and keep[s]]
        if not rows:
            continue
        desc[c] = {
            "n_surahs": len(rows),
            "mean_form_IV_share": float(np.mean(P[rows, iIV])),
            "mean_form_V_VI_share": float(np.mean(P[rows, iV] + P[rows, iVI])),
            "mean_root_expected_IV": float(np.mean(E[rows, iIV])),
            "mean_residual_IV": float(np.mean(D[rows, iIV])),
            "mean_verb_tokens": float(np.mean(counts[rows].sum(axis=1))),
            "mean_verse_len": float(np.mean([lens[s + 1]["mean_verse_len"] for s in rows])),
        }

    # (3) confusion of the H1 classifier at L0
    X = P[keep]
    yy = y[keep]
    K = len(classes)
    sums = np.zeros((K, X.shape[1]))
    cnts = np.zeros(K)
    np.add.at(sums, yy, X)
    np.add.at(cnts, yy, 1.0)
    own_sum = sums[yy] - X
    own_cnt = cnts[yy] - 1.0
    cent = sums / np.maximum(cnts[:, None], 1)
    d = ((X[:, None, :] - cent[None, :, :]) ** 2).sum(axis=2)
    own_cent = own_sum / np.maximum(own_cnt[:, None], 1)
    d[np.arange(len(yy)), yy] = ((X - own_cent) ** 2).sum(axis=1)
    pred = np.argmin(d, axis=1)
    conf = {}
    for i, c in enumerate(classes):
        rows = yy == i
        conf[c] = {
            "n": int(rows.sum()),
            "recall": float((pred[rows] == i).mean()) if rows.sum() else None,
            "predicted_as": {classes[j]: int((pred[rows] == j).sum())
                             for j in range(K) if (pred[rows] == j).sum()},
        }

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(M.REPO, "findings/phase-b-hypotheses/runs/h-new-3130-posthoc", stamp)
    os.makedirs(run_dir, exist_ok=False)
    payload = {
        "status": "POST-HOC — NOT PRE-REGISTERED, NOT VERDICT-BEARING",
        "parent_run": "runs/h-new-3130/20260809T090605Z",
        "prereg_gap": "prereg §4.3 registered a null for ROOT-B D1/D2 but not for ROOT-B H1",
        "seed": SEED_POSTHOC, "n_perms": M.N_PERM,
        "root_B_H1": out_h1,
        "per_register_descriptive": desc,
        "H1_confusion_L0": conf,
        "classes": classes,
    }
    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print("POST-HOC run: %s" % run_dir)
    print()
    print("(1) ROOT-B H1 — accuracy on the root-residualised profile, vs label shuffle")
    for ch in ["L0", "L1", "L2", "L3"]:
        o = out_h1[ch]
        print("   %s raw=%.4f  root-residualised=%.4f  null=%.4f(sd %.4f)  p=%.5f"
              % (ch, o["accuracy_raw_profile"], o["accuracy_root_residualised"],
                 o["null_mean"], o["null_sd"], o["p_label_shuffle"]))
    print()
    print("(2) per-register descriptive shares")
    print("   %-11s %4s %10s %10s %10s %10s %8s" % ("register", "n", "IV_share",
                                                    "V+VI", "root_exp_IV", "resid_IV", "mvl"))
    for c, v in sorted(desc.items(), key=lambda kv: -kv[1]["mean_form_IV_share"]):
        print("   %-11s %4d %10.4f %10.4f %10.4f %+10.4f %8.2f"
              % (c, v["n_surahs"], v["mean_form_IV_share"], v["mean_form_V_VI_share"],
                 v["mean_root_expected_IV"], v["mean_residual_IV"], v["mean_verse_len"]))
    print()
    print("(3) H1 classifier per-register recall at L0")
    for c, v in conf.items():
        print("   %-11s n=%3d recall=%.3f  ->  %s" % (c, v["n"], v["recall"], v["predicted_as"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
