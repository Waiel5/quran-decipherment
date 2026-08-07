#!/usr/bin/env python3
"""H-NEW-2560: is the fāṣila a clause seal? Verse-boundary vs syntactic-constituent alignment.

Runs the six registered inferences of
`findings/phase-b-hypotheses/prereg-h-new-2560-fasila-clause-seal.md`
against the Extended Quranic Treebank. The prereg SHA-256 is verified at runtime.
"""

import argparse
import csv
import hashlib
import json
import platform
import random
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_PREREG_SHA = "4432e6fa79d330d5adc614d5175df8a70fd87476442f41bb289a6a248d7c3269"
EXPECTED_EQTB_SHA = "a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7"
EXPECTED_QURAN_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"
EXPECTED_REGISTER_SHA = "a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25"

SEED = 20260509           # prereg §6: H1a, H2, H3, H4, H5
SEED_H1B = 20260510       # prereg §6: H1b
SEED_REPL_H1A = 20260510  # prereg §7 R7
SEED_REPL_H5 = 20260511   # prereg §7 R7
N_PERM = 10_000
TESTS_IN_FAMILY = 6
ALPHA_BON = 0.05 / TESTS_IN_FAMILY
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY

# prereg §5.4 — waqf pause grades and their registered classes
WAQF = {0x6D6: "sla", 0x6D7: "qla", 0x6D8: "mim", 0x6D9: "la",
        0x6DA: "jim", 0x6DB: "muanaqa", 0x6DC: "saktah"}
ANNOT_RANGE = set(range(0x6D6, 0x6EE))          # waqf + rubʿ-ḥizb + sajdah marks
STOP_PREFERRED = {"mim", "qla"}
CONTINUE_PREFERRED = {"sla", "la"}
PROCLITICS = {"يا", "ويا", "ها", "فيا"}          # QAC joins these to the following word
SPAN_RE = re.compile(r"\[(\d+)-(\d+)\]")
# prereg §6 H3 — strata fixed a priori by host-verse EQTB word count
STRATA = (("2-4", 2, 4), ("5-8", 5, 8), ("9-15", 9, 15), ("16-30", 16, 30), ("31+", 31, 10**9))
STRATUM_MIN_N = 100


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def perm_p(observed, null_values, greater_is_extreme=True):
    """prereg §6 — one-sided p = (1 + #{null at least as extreme}) / (n_perm + 1)."""
    if greater_is_extreme:
        extreme = sum(1 for value in null_values if value >= observed - 1e-12)
    else:
        extreme = sum(1 for value in null_values if value <= observed + 1e-12)
    return (1 + extreme) / (len(null_values) + 1)


def decide(observed_direction_ok, p_values):
    return bool(observed_direction_ok and all(p < RAW_GATE for p in p_values))


# --------------------------------------------------------------------------- parsing

def parse_eqtb(path):
    """Return per-surah row tables plus the arc and constituent inventories."""
    surahs = defaultdict(list)
    with open(path, encoding="utf-16", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            surahs[int(row["chapter_id"])].append((
                int(row["tid"]), int(row["sentence_id"]), int(row["token_id"]),
                int(row["verse_id"]), int(row["word_id"]), row["location"] != "_",
                int(row["ref_token_id"]), row["is_constituent"], row["constituents_loc"],
            ))
    return surahs


def build_surah(rows):
    """Linear index, cut inventory, crossing counts and constituent-split flags.

    prereg §5.1 — one cut rule: the index immediately before the first row of the next
    unit, which deterministically attaches synthetic rows to the left.
    """
    rows.sort()
    n = len(rows)
    index_of = {}
    verse_rows = defaultdict(list)
    word_first = {}
    for idx, row in enumerate(rows):
        _, sentence, token, verse, word, real, _, _, _ = row
        index_of[(sentence, token)] = idx
        verse_rows[verse].append(idx)
        if real and (verse, word) not in word_first:
            word_first[(verse, word)] = idx

    # prereg §5.1 integrity gate — verse row blocks must be contiguous
    for verse, idxs in verse_rows.items():
        if idxs[-1] - idxs[0] + 1 != len(idxs):
            raise SystemExit(f"non-contiguous verse block at verse {verse}: aborting")

    cross_delta = [0] * (n + 1)
    split_delta = [0] * (n + 1)
    n_arcs = 0
    for _, sentence, token, _, _, _, ref, is_cons, cons_loc in rows:
        if ref != token:
            a, b = index_of[(sentence, token)], index_of.get((sentence, ref))
            if b is not None:
                lo, hi = (a, b) if a < b else (b, a)
                cross_delta[lo] += 1
                cross_delta[hi] -= 1
                n_arcs += 1
        if is_cons == "1":
            for start, end in SPAN_RE.findall(cons_loc or ""):
                a = index_of.get((sentence, int(start)))
                b = index_of.get((sentence, int(end)))
                if a is None or b is None:
                    continue
                lo, hi = (a, b) if a < b else (b, a)
                split_delta[lo] += 1
                split_delta[hi] -= 1

    cross, split, running_c, running_s = [0] * n, [0] * n, 0, 0
    for idx in range(n):
        running_c += cross_delta[idx]
        running_s += split_delta[idx]
        cross[idx] = running_c
        split[idx] = running_s

    verses = sorted(verse_rows)
    n_words = {v: max((w for (vv, w) in word_first if vv == v), default=0) for v in verses}
    return {
        "rows": rows, "n": n, "index_of": index_of, "verse_rows": verse_rows,
        "word_first": word_first, "cross": cross, "split": split,
        "verses": verses, "n_words": n_words, "n_arcs": n_arcs,
        "sentence_of": [r[1] for r in rows],
    }


def parse_waqf(path):
    """Map (surah, verse) -> {word_index_j: grade}, meaning the cut AFTER word j.

    prereg §5.4 — marks are standalone tokens; one declared proclitic merge rule.
    """
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    words, marks = {}, {}
    for surah in data:
        for verse in surah["verses"]:
            key = (int(surah["id"]), int(verse["id"]))
            seq, found = [], {}
            for token in verse["text"].split():
                if token and all(ord(ch) in ANNOT_RANGE for ch in token):
                    for ch in token:
                        if ord(ch) in WAQF:
                            found[len(seq)] = WAQF[ord(ch)]
                elif seq and seq[-1] in PROCLITICS:
                    seq[-1] += token
                else:
                    seq.append(token)
            words[key] = len(seq)
            marks[key] = found
    return words, marks


# --------------------------------------------------------------------------- assembly

def assemble(surahs, waqf_words, waqf_marks, registers):
    built = {c: build_surah(rows) for c, rows in surahs.items()}
    boundaries = []          # one record per true internal verse boundary
    waqf_positions = []      # one record per usable mid-verse waqf mark
    waqf_excluded_verses, waqf_excluded_marks = [], 0
    sentence_segments = defaultdict(list)

    for chapter in sorted(built):
        info = built[chapter]
        cross, split, word_first = info["cross"], info["split"], info["word_first"]
        sentence_of, verse_rows = info["sentence_of"], info["verse_rows"]
        verses = info["verses"]

        for verse in verses[:-1]:
            cut = verse_rows[verse + 1][0] - 1
            n_w = info["n_words"][verse]
            candidates = []
            for j in range(1, n_w):
                nxt = word_first.get((verse, j + 1))
                if nxt is not None:
                    candidates.append(nxt - 1)
            sealed = cross[cut] == 0
            same_sentence = sentence_of[cut] == sentence_of[cut + 1]
            boundaries.append({
                "chapter": chapter, "verse": verse, "cut": cut,
                "sealed": sealed, "cross": cross[cut], "split": split[cut] > 0,
                "n_words": n_w, "sentence_internal": same_sentence,
                "cand_sealed": [1 if cross[k] == 0 else 0 for k in candidates],
                "cand_split": [1 if split[k] > 0 else 0 for k in candidates],
                "register": registers.get(str(chapter), "unknown"),
            })
            if same_sentence:
                sentence_segments[sentence_of[cut]].append(cut)

        for verse in verses:
            key = (chapter, verse)
            if waqf_words.get(key) != info["n_words"][verse]:
                if waqf_marks.get(key):
                    waqf_excluded_marks += len(waqf_marks[key])
                if key not in waqf_excluded_verses:
                    waqf_excluded_verses.append(key)
                continue
            for j, grade in waqf_marks.get(key, {}).items():
                nxt = word_first.get((verse, j + 1))
                if j <= 0 or nxt is None:
                    waqf_excluded_marks += 1
                    continue
                cut = nxt - 1
                waqf_positions.append({
                    "chapter": chapter, "verse": verse, "after_word": j, "grade": grade,
                    "sealed": cross[cut] == 0, "cross": cross[cut],
                })
    return built, boundaries, waqf_positions, sentence_segments, waqf_excluded_verses, waqf_excluded_marks


# --------------------------------------------------------------------------- tests

def stratum_of(n_words):
    for name, lo, hi in STRATA:
        if lo <= n_words <= hi:
            return name
    return None


def run_pseudo_family(eligible, seed, n_perm=N_PERM):
    """H1a, H3, H4 share one set of draws (prereg §6)."""
    rng = random.Random(seed)
    n = len(eligible)
    true_sealed = sum(b["sealed"] for b in eligible)
    true_split = sum(b["split"] for b in eligible)
    strata_index = [stratum_of(b["n_words"]) for b in eligible]
    strata_names = [s for s, _, _ in STRATA]
    strata_n = {s: sum(1 for x in strata_index if x == s) for s in strata_names}
    active = [s for s in strata_names if strata_n[s] >= STRATUM_MIN_N]
    true_stratum = {s: 0 for s in strata_names}
    for b, s in zip(eligible, strata_index):
        if b["sealed"]:
            true_stratum[s] += 1

    cand_sealed = [b["cand_sealed"] for b in eligible]
    cand_split = [b["cand_split"] for b in eligible]
    sizes = [len(c) for c in cand_sealed]

    null_sealed, null_split, null_strat_mean = [], [], []
    stratum_null_totals = {s: [] for s in strata_names}
    random_value = rng.random
    for _ in range(n_perm):
        total_sealed = total_split = 0
        per_stratum = {s: 0 for s in strata_names}
        for i in range(n):
            j = int(random_value() * sizes[i])
            hit = cand_sealed[i][j]
            total_sealed += hit
            total_split += cand_split[i][j]
            if hit:
                per_stratum[strata_index[i]] += 1
        null_sealed.append(total_sealed / n)
        null_split.append(total_split / n)
        for s in strata_names:
            stratum_null_totals[s].append(per_stratum[s])
        null_strat_mean.append(
            sum(per_stratum[s] / strata_n[s] for s in active) / len(active) if active else float("nan")
        )

    true_strat_mean = (sum(true_stratum[s] / strata_n[s] for s in active) / len(active)) if active else float("nan")
    return {
        "n_eligible": n,
        "true_sealed_rate": true_sealed / n,
        "true_split_rate": true_split / n,
        "null_sealed": null_sealed, "null_split": null_split,
        "null_strat_mean": null_strat_mean, "true_strat_mean": true_strat_mean,
        "strata_n": strata_n, "active_strata": active,
        "true_stratum_rate": {s: (true_stratum[s] / strata_n[s]) if strata_n[s] else None for s in strata_names},
        "null_stratum_rate_mean": {
            s: (sum(stratum_null_totals[s]) / len(stratum_null_totals[s]) / strata_n[s]) if strata_n[s] else None
            for s in strata_names
        },
        "stratum_p": {
            s: perm_p(true_stratum[s], stratum_null_totals[s]) if strata_n[s] >= STRATUM_MIN_N else None
            for s in strata_names
        },
    }


def run_h1b(built, boundaries, seed, n_perm=N_PERM):
    """Permute the multiset of row-segment lengths inside each multi-verse sentence."""
    by_sentence = defaultdict(list)
    for b in boundaries:
        if b["sentence_internal"]:
            by_sentence[(b["chapter"], built[b["chapter"]]["sentence_of"][b["cut"]])].append(b["cut"])
    universe = []
    blocks = []
    for (chapter, sentence), cuts in sorted(by_sentence.items()):
        info = built[chapter]
        idxs = [i for i, s in enumerate(info["sentence_of"]) if s == sentence]
        lo, hi = min(idxs), max(idxs)
        cuts = sorted(cuts)
        lengths = []
        prev = lo - 1
        for cut in cuts:
            lengths.append(cut - prev)
            prev = cut
        lengths.append(hi - prev)
        blocks.append((chapter, lo, hi, lengths, len(cuts)))
        universe.extend(cuts)
    if not universe:
        return None
    true_sealed = sum(1 for b in boundaries if b["sentence_internal"] and b["sealed"])
    rng = random.Random(seed)
    null = []
    for _ in range(n_perm):
        sealed = 0
        for chapter, lo, hi, lengths, k in blocks:
            cross = built[chapter]["cross"]
            order = lengths[:]
            rng.shuffle(order)
            pos = lo - 1
            for length in order[:k]:
                pos += length
                if cross[pos] == 0:
                    sealed += 1
        null.append(sealed / len(universe))
    return {
        "n_universe": len(universe),
        "n_sentences": len(blocks),
        "true_sealed_rate": true_sealed / len(universe),
        "null": null,
    }


def run_h2(boundaries, seed, n_perm=N_PERM):
    per_surah = defaultdict(lambda: [0, 0])
    register_of = {}
    for b in boundaries:
        cell = per_surah[b["chapter"]]
        cell[0] += 1
        cell[1] += int(b["sealed"])
        register_of[b["chapter"]] = b["register"]
    chapters = sorted(per_surah)
    labels = [register_of[c] for c in chapters]

    def contrast(assignment):
        totals = defaultdict(lambda: [0, 0])
        for chapter, label in zip(chapters, assignment):
            n, y = per_surah[chapter]
            totals[label][0] += n
            totals[label][1] += y
        esch, legal = totals["eschatological_mufassal"], totals["legal_medinan"]
        if not esch[0] or not legal[0]:
            return float("nan")
        return esch[1] / esch[0] - legal[1] / legal[0]

    observed = contrast(labels)
    rng = random.Random(seed)
    null = []
    shuffled = labels[:]
    for _ in range(n_perm):
        rng.shuffle(shuffled)
        null.append(contrast(shuffled))
    rates = {}
    totals = defaultdict(lambda: [0, 0])
    for chapter in chapters:
        n, y = per_surah[chapter]
        totals[register_of[chapter]][0] += n
        totals[register_of[chapter]][1] += y
    for label, (n, y) in totals.items():
        rates[label] = {"n_boundaries": n, "sealed_rate": y / n}
    return {"observed_delta": observed, "null": null, "register_rates": rates}


def run_h5(waqf_positions, seed, n_perm=N_PERM):
    stop = [p for p in waqf_positions if p["grade"] in STOP_PREFERRED]
    cont = [p for p in waqf_positions if p["grade"] in CONTINUE_PREFERRED]
    if not stop or not cont:
        return None
    flags = [int(p["sealed"]) for p in stop] + [int(p["sealed"]) for p in cont]
    n_stop = len(stop)
    observed = sum(flags[:n_stop]) / n_stop - sum(flags[n_stop:]) / len(cont)
    rng = random.Random(seed)
    null = []
    pool = flags[:]
    for _ in range(n_perm):
        rng.shuffle(pool)
        null.append(sum(pool[:n_stop]) / n_stop - sum(pool[n_stop:]) / len(cont))
    by_grade = {}
    for grade in ("mim", "qla", "jim", "sla", "la", "muanaqa", "saktah"):
        rows = [p for p in waqf_positions if p["grade"] == grade]
        if rows:
            by_grade[grade] = {
                "n": len(rows),
                "sealed_rate": sum(p["sealed"] for p in rows) / len(rows),
                "mean_cross": sum(p["cross"] for p in rows) / len(rows),
            }
    return {
        "n_stop_preferred": n_stop, "n_continue_preferred": len(cont),
        "sealed_rate_stop": sum(flags[:n_stop]) / n_stop,
        "sealed_rate_continue": sum(flags[n_stop:]) / len(cont),
        "observed_delta": observed, "null": null, "by_grade": by_grade,
    }


# --------------------------------------------------------------------------- main

def self_check():
    """Synthetic sanity check of the cut/crossing machinery (prereg §5.1-5.2)."""
    rows = [
        # tid, sentence, token, verse, word, real, ref, is_cons, cons_loc
        (0, 1, 0, 1, 1, True, 0, "0", "_"),
        (1, 1, 1, 1, 2, True, 0, "1", "[0-1]"),
        (2, 2, 0, 2, 1, True, 0, "0", "_"),
        (3, 2, 1, 2, 2, True, 0, "0", "_"),
    ]
    info = build_surah([list(r) and tuple(r) for r in rows])
    assert info["cross"] == [1, 0, 1, 0], info["cross"]
    assert info["split"] == [1, 0, 0, 0], info["split"]
    # boundary after verse 1 is cut 1 -> sealed; the interior cut 0 is crossed
    assert info["cross"][1] == 0 and info["cross"][0] == 1
    assert perm_p(1.0, [0.0] * 9) == 0.1
    assert perm_p(0.0, [1.0] * 9, greater_is_extreme=False) == 0.1
    assert stratum_of(3) == "2-4" and stratum_of(40) == "31+"
    print("self-check: PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eqtb", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.eqtb:
        parser.error("--eqtb is required")

    repo = Path(__file__).resolve().parents[3]
    prereg = repo / "findings/phase-b-hypotheses/prereg-h-new-2560-fasila-clause-seal.md"
    quran = repo / "quran-text/quran-no-tashkeel.json"
    register_path = repo / "findings/phase-b-hypotheses/csv/h-new-2500.json"
    script = Path(__file__).resolve()

    hashes = {"prereg": sha256(prereg), "eqtb": sha256(args.eqtb), "quran_no_tashkeel": sha256(quran),
              "register_h_new_2500": sha256(register_path), "script": sha256(script)}
    expected = {"prereg": EXPECTED_PREREG_SHA, "eqtb": EXPECTED_EQTB_SHA,
                "quran_no_tashkeel": EXPECTED_QURAN_SHA, "register_h_new_2500": EXPECTED_REGISTER_SHA}
    for key, want in expected.items():
        if hashes[key] != want:
            raise SystemExit(f"{key} SHA mismatch: expected {want}, found {hashes[key]}")

    registers = json.load(open(register_path, encoding="utf-8"))["genre_proxy"]["surah_genre"]
    waqf_words, waqf_marks = parse_waqf(quran)
    surahs = parse_eqtb(args.eqtb)
    built, boundaries, waqf_positions, _segments, wx_verses, wx_marks = assemble(
        surahs, waqf_words, waqf_marks, registers)

    eligible = [b for b in boundaries if b["cand_sealed"]]
    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo / "findings/phase-b-hypotheses/runs/h-new-2560" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    print(f"[census] boundaries={len(boundaries)} eligible={len(eligible)} waqf={len(waqf_positions)}", flush=True)
    fam = run_pseudo_family(eligible, SEED)
    print("[h1a/h3/h4] primary draws done", flush=True)
    fam_repl = run_pseudo_family(eligible, SEED_REPL_H1A)
    print("[h1a] replication draws done", flush=True)
    h1b = run_h1b(built, boundaries, SEED_H1B)
    h2 = run_h2(boundaries, SEED)
    h5 = run_h5(waqf_positions, SEED)
    h5_repl = run_h5(waqf_positions, SEED_REPL_H5)
    print("[h1b/h2/h5] done", flush=True)

    p_h1a = perm_p(fam["true_sealed_rate"], fam["null_sealed"])
    p_h3 = perm_p(fam["true_strat_mean"], fam["null_strat_mean"])
    p_h4 = perm_p(fam["true_split_rate"], fam["null_split"], greater_is_extreme=False)
    p_h1b = perm_p(h1b["true_sealed_rate"], h1b["null"]) if h1b else None
    p_h2 = perm_p(h2["observed_delta"], h2["null"])
    p_h5 = perm_p(h5["observed_delta"], h5["null"]) if h5 else None

    mean_null_sealed = sum(fam["null_sealed"]) / len(fam["null_sealed"])
    mean_null_split = sum(fam["null_split"]) / len(fam["null_split"])
    mean_null_strat = sum(fam["null_strat_mean"]) / len(fam["null_strat_mean"])

    # ---- robustness / rosters (prereg §7)
    sentence_internal = [b for b in boundaries if b["sentence_internal"]]
    verses_per_sentence = defaultdict(set)
    for chapter, info in built.items():
        for (sentence, _), idx in info["index_of"].items():
            verses_per_sentence[(chapter, sentence)].add(info["rows"][idx][3])
    vps = defaultdict(int)
    for key, verses in verses_per_sentence.items():
        vps[len(verses)] += 1

    pseudo_sentence_edge = 0
    pseudo_total = 0
    rng_r2 = random.Random(SEED)
    for b in eligible:
        info = built[b["chapter"]]
        n_w = b["n_words"]
        cands = [info["word_first"][(b["verse"], j + 1)] - 1 for j in range(1, n_w)
                 if (b["verse"], j + 1) in info["word_first"]]
        if not cands:
            continue
        cut = cands[int(rng_r2.random() * len(cands))]
        pseudo_total += 1
        pseudo_sentence_edge += int(info["sentence_of"][cut] != info["sentence_of"][cut + 1])

    roster = sorted(boundaries, key=lambda b: -b["cross"])[:40]
    exception_roster = [{
        "surah": b["chapter"], "verse": b["verse"], "crossing_arcs": b["cross"],
        "register": b["register"], "host_verse_words": b["n_words"],
        "splits_constituent": b["split"],
        "waqf_marks_in_host_verse": sorted(waqf_marks.get((b["chapter"], b["verse"]), {}).values()),
        "waqf_marks_in_next_verse": sorted(waqf_marks.get((b["chapter"], b["verse"] + 1), {}).values()),
    } for b in roster]

    result = {
        "id": "H-NEW-2560",
        "prereg_sha256": hashes["prereg"],
        "tests_in_family": TESTS_IN_FAMILY,
        "alpha_bonferroni": ALPHA_BON,
        "raw_p_gate": RAW_GATE,
        "corrected_novelty_gate": CORRECTED_GATE,
        "n_permutations": N_PERM,
        "census": {
            "surahs": len(built),
            "verses": sum(len(info["verses"]) for info in built.values()),
            "internal_verse_boundaries": len(boundaries),
            "eligible_boundaries_min2_words": len(eligible),
            "eqtb_sentences": len(verses_per_sentence),
            "eqtb_sentences_spanning_multiple_verses": sum(n for k, n in vps.items() if k > 1),
            "verses_per_sentence_distribution": dict(sorted(vps.items())),
            "boundaries_sentence_internal": len(sentence_internal),
            "boundaries_at_sentence_edge": len(boundaries) - len(sentence_internal),
            "total_arcs": sum(info["n_arcs"] for info in built.values()),
        },
        "h1a_fasila_vs_matched_pseudo": {
            "n_eligible": fam["n_eligible"],
            "true_sealed_rate": fam["true_sealed_rate"],
            "mean_null_sealed_rate": mean_null_sealed,
            "effect": fam["true_sealed_rate"] - mean_null_sealed,
            "p_one_sided": p_h1a, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h1a),
            "direction_locked": "true > pseudo",
            "direction_held": fam["true_sealed_rate"] > mean_null_sealed,
            "passes_gate": decide(fam["true_sealed_rate"] > mean_null_sealed, [p_h1a]),
            "seed": SEED,
            "replication_seed_20260510": {
                "true_sealed_rate": fam_repl["true_sealed_rate"],
                "mean_null_sealed_rate": sum(fam_repl["null_sealed"]) / len(fam_repl["null_sealed"]),
                "p_one_sided": perm_p(fam_repl["true_sealed_rate"], fam_repl["null_sealed"]),
            },
        },
        "h1b_within_sentence_segment_permutation": (None if not h1b else {
            "n_universe": h1b["n_universe"], "n_sentences": h1b["n_sentences"],
            "true_sealed_rate": h1b["true_sealed_rate"],
            "mean_null_sealed_rate": sum(h1b["null"]) / len(h1b["null"]),
            "p_one_sided": p_h1b, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h1b),
            "direction_locked": "true > permuted",
            "direction_held": h1b["true_sealed_rate"] > sum(h1b["null"]) / len(h1b["null"]),
            "passes_gate": decide(h1b["true_sealed_rate"] > sum(h1b["null"]) / len(h1b["null"]), [p_h1b]),
            "seed": SEED_H1B,
        }),
        "h2_register_contrast": {
            "observed_delta_eschat_minus_legal": h2["observed_delta"],
            "register_rates": h2["register_rates"],
            "p_one_sided": p_h2, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h2),
            "direction_locked": "eschatological_mufassal > legal_medinan",
            "direction_held": h2["observed_delta"] > 0,
            "passes_gate": decide(h2["observed_delta"] > 0, [p_h2]),
            "seed": SEED,
        },
        "h3_length_stratified": {
            "strata_bins": [s[0] for s in STRATA],
            "strata_n": fam["strata_n"], "active_strata": fam["active_strata"],
            "true_stratum_sealed_rate": fam["true_stratum_rate"],
            "null_stratum_sealed_rate": fam["null_stratum_rate_mean"],
            "per_stratum_p": fam["stratum_p"],
            "equal_weight_true": fam["true_strat_mean"],
            "equal_weight_null_mean": mean_null_strat,
            "effect": fam["true_strat_mean"] - mean_null_strat,
            "p_one_sided": p_h3, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h3),
            "direction_locked": "equal-weight true > equal-weight null",
            "direction_held": fam["true_strat_mean"] > mean_null_strat,
            "passes_gate": decide(fam["true_strat_mean"] > mean_null_strat, [p_h3]),
            "seed": SEED,
        },
        "h4_constituent_integrity": {
            "true_split_rate": fam["true_split_rate"],
            "mean_null_split_rate": mean_null_split,
            "effect_null_minus_true": mean_null_split - fam["true_split_rate"],
            "p_one_sided": p_h4, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h4),
            "direction_locked": "true < pseudo (fewer broken constituents)",
            "direction_held": fam["true_split_rate"] < mean_null_split,
            "passes_gate": decide(fam["true_split_rate"] < mean_null_split, [p_h4]),
            "seed": SEED,
        },
        "h5_classical_waqf_validation": (None if not h5 else {
            "n_stop_preferred": h5["n_stop_preferred"],
            "n_continue_preferred": h5["n_continue_preferred"],
            "sealed_rate_stop_preferred": h5["sealed_rate_stop"],
            "sealed_rate_continue_preferred": h5["sealed_rate_continue"],
            "observed_delta": h5["observed_delta"],
            "mean_null_delta": sum(h5["null"]) / len(h5["null"]),
            "p_one_sided": p_h5, "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p_h5),
            "direction_locked": "stop-preferred > continue-preferred",
            "direction_held": h5["observed_delta"] > 0,
            "passes_gate": decide(h5["observed_delta"] > 0, [p_h5]),
            "seed": SEED,
            "by_grade_ladder": h5["by_grade"],
            "replication_seed_20260511_p": perm_p(h5_repl["observed_delta"], h5_repl["null"]),
            "waqf_join": {
                "usable_marks": len(waqf_positions),
                "excluded_verses": [f"{c}:{v}" for c, v in wx_verses],
                "excluded_marks": wx_marks,
            },
        }),
        "robustness": {
            "R2_circularity_exhibit": {
                "true_boundaries_at_eqtb_sentence_edge_rate":
                    (len(boundaries) - len(sentence_internal)) / len(boundaries),
                "pseudo_boundaries_at_eqtb_sentence_edge_rate":
                    pseudo_sentence_edge / pseudo_total if pseudo_total else None,
                "note": "SEALED is near-equivalent to coinciding with an EQTB sentence edge; "
                        "these two rates make that visible.",
            },
            "R3_crossing_arcs": {
                "mean_cross_true_boundaries": sum(b["cross"] for b in boundaries) / len(boundaries),
                "max_cross_true_boundary": max(b["cross"] for b in boundaries),
            },
            "R4_sealed_given_sentence_internal": {
                "n": len(sentence_internal),
                "true_sealed_rate": (sum(b["sealed"] for b in sentence_internal) / len(sentence_internal))
                                    if sentence_internal else None,
            },
            "R6_exception_roster_top40": exception_roster,
            "R8_all_register_rates": h2["register_rates"],
        },
        "annotation_limit": (
            "EQTB dependency and constituent accuracy is the material limit. H1a is "
            "near-equivalent to EQTB sentence-boundary coincidence and is circularity-exposed; "
            "H5 is the only inference in the family that is independent of EQTB sentence "
            "segmentation. No matched Classical-Arabic dependency-treebank control exists on "
            "disk, so nothing here is shown to be Quran-specific."
        ),
    }

    h1a_ok = result["h1a_fasila_vs_matched_pseudo"]["passes_gate"]
    h3_ok = result["h3_length_stratified"]["passes_gate"]
    h5_ok = bool(h5) and result["h5_classical_waqf_validation"]["passes_gate"]
    h4_reversed = bool(fam["true_split_rate"] > mean_null_split)
    if not h5_ok:
        verdict = "CIRCULARITY-LIMITED — instrument not validated independently of verse layout"
    elif h1a_ok and h3_ok:
        verdict = "FĀṢILA-AS-CLAUSE-SEAL SUPPORTED; EQTB-ANNOTATION-LIMITED"
    elif h1a_ok and not h3_ok:
        verdict = "LENGTH-ARTEFACT — H1a passed but the length-stratified control failed"
    else:
        verdict = "NULL — H1a did not pass its locked direction/gate"
    if h4_reversed:
        verdict += "; H4 PRE-COMMIT VIOLATION (true boundaries split MORE constituents)"
    result["verdict"] = verdict

    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    def git(*a):
        return subprocess.check_output(["git", *a], cwd=repo, text=True).strip()

    manifest = {
        "id": "H-NEW-2560",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "git_commit": git("rev-parse", "HEAD"),
        "git_status_porcelain": git("status", "--porcelain"),
        "hashes_sha256": hashes, "expected_hashes_sha256": expected,
        "python": sys.version, "platform": platform.platform(),
        "seeds": {"primary": SEED, "h1b": SEED_H1B,
                  "replication_h1a": SEED_REPL_H1A, "replication_h5": SEED_REPL_H5},
        "n_permutations": N_PERM,
        "eqtb_path": str(args.eqtb.resolve()),
        "run_directory": str(run_dir.relative_to(repo)),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir), "verdict": verdict,
        "h1a": [fam["true_sealed_rate"], mean_null_sealed, p_h1a],
        "h1b": [h1b["true_sealed_rate"], p_h1b] if h1b else None,
        "h2": [h2["observed_delta"], p_h2],
        "h3": [fam["true_strat_mean"], mean_null_strat, p_h3],
        "h4": [fam["true_split_rate"], mean_null_split, p_h4],
        "h5": [h5["sealed_rate_stop"], h5["sealed_rate_continue"], p_h5] if h5 else None,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
