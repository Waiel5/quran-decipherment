#!/usr/bin/env python3
"""H-NEW-2960 post-hoc probes. NOT pre-registered.

These cannot create, upgrade or rescue any verdict. They exist to weaken, and to answer three
questions the registered run raised but did not settle:

  P1  Are any muqaṭṭaʿāt-opening demonstratives in the C1-eligible set at all?
  P2  Does the generated lexicon (C2/C3) have face validity as an ESCHATOLOGY axis?
  P3  Is the C2/C3 association a verse-length artefact? (UNIT-DRIFT-DEFECT.md §3 Screen B/C,
      §6.1: stratified permutation at TWO bin widths.)

Writes to its own run directory. The registered run directory is not touched.
"""

import hashlib
import json
import os
import platform
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "h2960", Path(__file__).resolve().parent / "h-new-2960.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)

# Words the classical frame would place squarely in the Hereafter. Used ONLY as a face-validity
# probe of the generated lexicon — never as a classifier, and never to produce a p-value.
FACE_VALIDITY_PROBES = ["qiya`map", "saAEap", "baEava", "jan~ap", "naAr", "Hisaab", "Ha`sib"]

N_DRAWS = 200_000
SEED = 20260509


def sha256(path):
    d = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            d.update(chunk)
    return d.hexdigest()


def stratified_permutation(tokens, frames, word_counts, n_bins, seed, n_draws=N_DRAWS):
    """Permute frame labels WITHIN verse-length bins. Prereg-external; two bin widths reported."""
    verses = sorted({(t["s"], t["v"]) for t in tokens if (t["s"], t["v"]) in frames})
    if not verses:
        return None
    distal = Counter()
    for t in tokens:
        key = (t["s"], t["v"])
        if key in frames and H.deixis_of(t["form"]) == "DISTAL":
            distal[key] += 1
    vals = np.array([distal[k] for k in verses], dtype=np.int32)
    labels = np.array([1 if frames[k] == "ESCH" else 0 for k in verses])
    lengths = np.array([word_counts[k] for k in verses])

    edges = np.quantile(lengths, np.linspace(0, 1, n_bins + 1))
    bin_id = np.clip(np.searchsorted(edges, lengths, side="right") - 1, 0, n_bins - 1)

    observed = int(vals[labels == 1].sum())
    rng = np.random.default_rng(seed)
    groups = [(np.where(bin_id == b)[0], int(labels[bin_id == b].sum())) for b in range(n_bins)]

    ge = 0
    done = 0
    while done < n_draws:
        take = min(20_000, n_draws - done)
        sums = np.zeros(take, dtype=np.int64)
        for idx, k in groups:
            if k == 0 or len(idx) == 0:
                continue
            tiled = np.tile(vals[idx], (take, 1))
            sums += rng.permuted(tiled, axis=1)[:, :k].sum(axis=1)
        ge += int((sums >= observed).sum())
        done += take
    return {"n_bins": n_bins, "observed_S": observed, "n_ge": ge,
            "p": (1 + ge) / (1 + n_draws),
            "bin_sizes": [int(len(i)) for i, _ in groups],
            "bin_esch_counts": [int(k) for _, k in groups]}


def main():
    repo_root = Path(__file__).resolve().parents[3]
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-2960-spatial-deixis.md"
    if sha256(qac) != H.EXPECTED_QAC_SHA:
        sys.exit("ABORT: QAC SHA mismatch")

    rows = H.load_qac(qac)
    census, dem, by_word = H.build_census(rows)
    inl = set(census["inl_surahs"])

    word_counts = Counter()
    for r in rows:
        key = (r["s"], r["v"])
        word_counts[key] = max(word_counts[key], r["w"])

    c1 = H.c1_frames(rows, restricted=False)
    lexicons = {k: H.build_lexicon(rows, c1, k) for k in H.K_VALUES}
    frames = {"C1": c1}
    for k in H.K_VALUES:
        frames[f"C{2 if k == 25 else 3}_k{k}"] = H.lexicon_frames(rows, lexicons[k])

    out = {}

    # ---- P1: are the named confound tokens even in the eligible set?
    openers = [r for r in dem if r["s"] in inl and r["v"] <= 3]
    out["P1_muqattaat_openings"] = {
        "n_opening_dem_tokens": len(openers),
        "loci": [f"{r['s']}:{r['v']}" for r in openers],
        "forms": Counter(r["form"] for r in openers).most_common(),
        "n_in_C1_eligible_set": sum(1 for r in openers if (r["s"], r["v"]) in c1),
        "n_in_C3_eligible_set": sum(1 for r in openers if (r["s"], r["v"]) in frames["C3_k50"]),
        "Q2_2_frame": c1.get((2, 2), "UNCLASSIFIED"),
        "Q2_2_in_C3": frames["C3_k50"].get((2, 2), "UNCLASSIFIED"),
    }

    # ---- P2: face validity of the generated lexicon
    face = {}
    for k, lex in lexicons.items():
        ranks = {w: i + 1 for i, (w, _) in enumerate(lex["top_esch"])}
        dranks = {w: i + 1 for i, (w, _) in enumerate(lex["top_dunya"])}
        face[str(k)] = {
            "top5_esch": [w for w, _ in lex["top_esch"][:5]],
            "top5_dunya": [w for w, _ in lex["top_dunya"][:5]],
            "probe_placement": {
                w: ("ESCH-side rank %d" % ranks[w]) if w in ranks
                else ("DUNYA-side rank %d" % dranks[w]) if w in dranks
                else "not in lexicon"
                for w in FACE_VALIDITY_PROBES
            },
        }
    out["P2_lexicon_face_validity"] = face

    # ---- P3: length-stratified permutation, two bin widths
    p3 = {}
    for fname in ("C2_k25", "C3_k50"):
        toks = [t for t in dem if (t["s"], t["v"]) in frames[fname]]
        p3[fname] = {
            "unstratified_p": H.permutation_test(toks, frames[fname], SEED, N_DRAWS)["p"],
            "quintiles": stratified_permutation(toks, frames[fname], word_counts, 5, SEED),
            "deciles": stratified_permutation(toks, frames[fname], word_counts, 10, SEED),
        }
    out["P3_length_stratified"] = p3

    # ---- P3b: is deixis itself length-loaded? (descriptive)
    lengths = np.array([word_counts[(t["s"], t["v"])] for t in dem])
    is_distal = np.array([H.deixis_of(t["form"]) == "DISTAL" for t in dem])
    edges = np.quantile(lengths, np.linspace(0, 1, 6))
    bins = np.clip(np.searchsorted(edges, lengths, side="right") - 1, 0, 4)
    out["P3b_distal_share_by_verse_length_quintile"] = [
        {"quintile": int(b) + 1,
         "n_dem_tokens": int((bins == b).sum()),
         "mean_verse_words": round(float(lengths[bins == b].mean()), 2),
         "distal_share": round(float(is_distal[bins == b].mean()), 4)}
        for b in range(5)]

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2960-posthoc" / run_id
    os.makedirs(run_dir, exist_ok=False)
    with open(run_dir / "result.json", "x", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2, sort_keys=True)
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as fh:
        json.dump({
            "hypothesis": "H-NEW-2960 (post-hoc, NOT pre-registered)",
            "run_directory": str(run_dir.relative_to(repo_root)),
            "script": str(Path(__file__).resolve().relative_to(repo_root)),
            "prereg": str(prereg.relative_to(repo_root)),
            "prereg_sha256": sha256(prereg),
            "inputs": [{"path": str(qac.relative_to(repo_root)), "sha256": sha256(qac)}],
            "git_commit": H.git_output(repo_root, "rev-parse", "HEAD"),
            "seed": SEED, "n_draws": N_DRAWS,
            "python": sys.version, "platform": platform.platform(),
            "utc": datetime.now(timezone.utc).isoformat(),
        }, fh, ensure_ascii=False, indent=2, sort_keys=True)
    print(json.dumps({"run_dir": str(run_dir.relative_to(repo_root)), **out}, indent=2,
                     ensure_ascii=False)[:4000])


if __name__ == "__main__":
    main()
