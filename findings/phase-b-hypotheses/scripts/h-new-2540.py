#!/usr/bin/env python3
"""H-NEW-2540: root-stratified Form II→V direct-object test."""

import argparse
import csv
import hashlib
import itertools
import json
import math
import os
import platform
import random
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


EXPECTED_PREREG_SHA = "affe3762bd942a0612b86d7bb4ef60e27b76802ba49fd9510e9880881eb4ab5e"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_EQTB_SHA = "a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7"
EXPECTED_CHRONOLOGY_SHA = "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7"
EXPECTED_QURAN_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"
SEED = 20260509
# Prereg §5: Null A uses 20260509; H1 Null B uses 20260510; H2 Null B uses 20260511.
SEED_NULL_A = 20260509
SEED_H1_NULL_B = 20260510
SEED_H2_NULL_B = 20260511
N_PERM = 10_000
TESTS_IN_FAMILY = 4
ALPHA_BON = 0.0125
# Prereg §5: the project novelty rule is stricter than Bonferroni. The raw decision
# gate is 0.005/4 = 0.00125; equivalently min(1, 4p) < 0.005.
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY
ROMAN = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII")
LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
FORM_RE = re.compile(r"\((I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII)\)")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_form(value):
    if not value or value in {"_", "-", "ـ"}:
        return "I"
    match = FORM_RE.search(value)
    return match.group(1) if match else value.strip("()")


def base_relation(value):
    return (value or "").split("<<", 1)[0].strip().split(" ", 1)[0].lower()


def parse_qac(path):
    verbs = {}
    duplicates = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 4 or fields[2] != "V":
                continue
            location, surface, _, features = fields
            match = LOCATION_RE.fullmatch(location)
            root_match = re.search(r"(?:^|\|)ROOT:([^|]+)", features)
            if not match or not root_match:
                continue
            form_match = FORM_RE.search(features)
            if location in verbs:
                duplicates.append(location)
            verbs[location] = {
                "location": location,
                "chapter": int(match.group(1)),
                "verse": int(match.group(2)),
                "word": int(match.group(3)),
                "segment": int(match.group(4)),
                "surface": surface,
                "root": root_match.group(1),
                "form": form_match.group(1) if form_match else "I",
                "passive": "|PASS" in features,
                "features": features,
            }
    return verbs, duplicates


def parse_eqtb(path):
    verbs_by_location = {}
    duplicates = []
    object_edges_by_head = defaultdict(list)
    with open(path, encoding="utf-16", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            sentence_id = int(row["sentence_id"])
            token_id = int(row["token_id"])
            location = row["location"]
            if row["pos"] == "V" and location != "_":
                if location in verbs_by_location:
                    duplicates.append(location)
                verbs_by_location[location] = {
                    "sentence_id": sentence_id,
                    "token_id": token_id,
                    "root": row["root"],
                    "form": normalize_form(row["verb_form"]),
                }
            if location != "_" and base_relation(row["rel_label"]) == "obj":
                ref = row["ref_token_id"]
                if ref and ref not in {"_", "-1"}:
                    object_edges_by_head[(sentence_id, int(ref))].append({
                        "dependent_location": location,
                        "dependent_surface": row["uthmani_token"],
                        "relation": row["rel_label"],
                    })
    return verbs_by_location, object_edges_by_head, duplicates


def load_periods(path):
    periods = {}
    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            periods[int(row["mushaf_order"])] = row["period"]
    return periods


def join_tokens(qac_verbs, eqtb_verbs, object_edges, periods):
    joined = []
    unmatched = []
    agreement = {"form_compared": 0, "form_agree": 0, "root_compared": 0, "root_agree": 0}
    for location, qac in qac_verbs.items():
        eqtb = eqtb_verbs.get(location)
        if not eqtb:
            unmatched.append(location)
            continue
        if eqtb["form"]:
            agreement["form_compared"] += 1
            agreement["form_agree"] += int(eqtb["form"] == qac["form"])
        if eqtb["root"] and eqtb["root"] not in {"_", "-", "ـ"}:
            agreement["root_compared"] += 1
            agreement["root_agree"] += int(eqtb["root"] == qac["root"])
        head = (eqtb["sentence_id"], eqtb["token_id"])
        joined.append({
            **qac,
            "period": periods.get(qac["chapter"], "Unknown"),
            "has_object": bool(object_edges.get(head)),
            "object_edges": object_edges.get(head, []),
        })
    agreement["form_rate"] = agreement["form_agree"] / agreement["form_compared"]
    agreement["root_rate"] = agreement["root_agree"] / agreement["root_compared"]
    return joined, unmatched, agreement


def cells_for(tokens, form_a, form_b, min_count, outcome="has_object", period=None):
    counts = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for token in tokens:
        if token["form"] not in {form_a, form_b} or (period and token["period"] != period):
            continue
        counts[token["root"]][token["form"]][0] += 1
        counts[token["root"]][token["form"]][1] += int(token[outcome])
    return {
        root: {form_a: tuple(forms[form_a]), form_b: tuple(forms[form_b])}
        for root, forms in counts.items()
        if forms[form_a][0] >= min_count and forms[form_b][0] >= min_count
    }


def weighted_stat(cells, form_a, form_b):
    numerator = denominator = 0.0
    for forms in cells.values():
        n_a, y_a = forms[form_a]
        n_b, y_b = forms[form_b]
        p_a = (y_a + 0.5) / (n_a + 1.0)
        p_b = (y_b + 0.5) / (n_b + 1.0)
        weight = 2.0 * n_a * n_b / (n_a + n_b)
        numerator += weight * (p_a - p_b)
        denominator += weight
    return numerator / denominator if denominator else float("nan")


def unsmoothed_macro(cells, form_a, form_b):
    differences = []
    for forms in cells.values():
        n_a, y_a = forms[form_a]
        n_b, y_b = forms[form_b]
        differences.append(y_a / n_a - y_b / n_b)
    return sum(differences) / len(differences) if differences else float("nan")


def mantel_haenszel_or(cells, form_a, form_b):
    numerator = denominator = 0.0
    for forms in cells.values():
        n_a, a = forms[form_a]
        n_b, c = forms[form_b]
        b, d = n_a - a, n_b - c
        total = n_a + n_b
        numerator += a * d / total
        denominator += b * c / total
    if denominator == 0:
        return math.inf if numerator > 0 else float("nan")
    return numerator / denominator


def swapped_cells(cells, form_a, form_b, mask):
    roots = sorted(cells)
    return {
        root: {
            form_a: cells[root][form_b] if mask[index] else cells[root][form_a],
            form_b: cells[root][form_a] if mask[index] else cells[root][form_b],
        }
        for index, root in enumerate(roots)
    }


def permutation_test(cells, form_a, form_b, exact=False, seed=SEED, n_perm=N_PERM, two_sided=False):
    observed = weighted_stat(cells, form_a, form_b)
    root_count = len(cells)
    if exact:
        masks = itertools.product((False, True), repeat=root_count)
        values = [weighted_stat(swapped_cells(cells, form_a, form_b, mask), form_a, form_b) for mask in masks]
        if two_sided:
            p_value = sum(abs(value) >= abs(observed) - 1e-15 for value in values) / len(values)
        else:
            p_value = sum(value >= observed - 1e-15 for value in values) / len(values)
        return observed, p_value, len(values), "exact"
    rng = random.Random(seed)
    extreme = 0
    for _ in range(n_perm):
        mask = [bool(rng.getrandbits(1)) for _ in range(root_count)]
        value = weighted_stat(swapped_cells(cells, form_a, form_b, mask), form_a, form_b)
        extreme += abs(value) >= abs(observed) if two_sided else value >= observed
    return observed, (extreme + 1) / (n_perm + 1), n_perm, "monte-carlo"


def token_label_test(cells, form_a, form_b, seed=SEED, n_perm=N_PERM):
    """Permute object labels within each root while preserving its margins."""
    observed = weighted_stat(cells, form_a, form_b)
    rng = random.Random(seed)
    extreme = 0
    for _ in range(n_perm):
        permuted = {}
        for root, forms in cells.items():
            n_a, y_a = forms[form_a]
            n_b, y_b = forms[form_b]
            total_positive = y_a + y_b
            positive_slots = set(rng.sample(range(n_a + n_b), total_positive))
            perm_y_a = sum(index < n_a for index in positive_slots)
            perm_y_b = total_positive - perm_y_a
            permuted[root] = {
                form_a: (n_a, perm_y_a),
                form_b: (n_b, perm_y_b),
            }
        extreme += weighted_stat(permuted, form_a, form_b) >= observed
    return observed, (extreme + 1) / (n_perm + 1), n_perm, "within-root-token-label"


def summarize_family(tokens, form_a, form_b, min_count, exact, seed_null_b):
    cells = cells_for(tokens, form_a, form_b, min_count)
    observed, p_root, root_null_size, root_null_kind = permutation_test(
        cells, form_a, form_b, exact=exact, seed=SEED_NULL_A
    )
    _, p_token, token_null_size, token_null_kind = token_label_test(
        cells, form_a, form_b, seed=seed_null_b
    )
    result = {
        "forms": [form_a, form_b],
        "min_tokens_per_form_per_root": min_count,
        "eligible_roots": len(cells),
        "root_cells": cells,
        "weighted_rate_difference": observed,
        "unsmoothed_macro_difference": unsmoothed_macro(cells, form_a, form_b),
        "mantel_haenszel_or": mantel_haenszel_or(cells, form_a, form_b),
        "p_root_swap_one_sided": p_root,
        "p_token_label_one_sided": p_token,
        "root_null_kind": root_null_kind,
        "root_null_size": root_null_size,
        "token_null_kind": token_null_kind,
        "token_null_size": token_null_size,
        "direction_positive": observed > 0,
        "seed_null_a": SEED_NULL_A,
        "seed_null_b": seed_null_b,
        "raw_gate": RAW_GATE,
        "p_root_swap_bonferroni": min(1.0, TESTS_IN_FAMILY * p_root),
        "p_token_label_bonferroni": min(1.0, TESTS_IN_FAMILY * p_token),
        "passes_strict_gate": observed > 0 and p_root < RAW_GATE and p_token < RAW_GATE,
    }
    return result


def describe_family(tokens, form_a, form_b, min_count):
    cells = cells_for(tokens, form_a, form_b, min_count)
    return {
        "forms": [form_a, form_b],
        "min_tokens_per_form_per_root": min_count,
        "eligible_roots": len(cells),
        "root_cells": cells,
        "weighted_rate_difference": weighted_stat(cells, form_a, form_b),
        "unsmoothed_macro_difference": unsmoothed_macro(cells, form_a, form_b),
        "mantel_haenszel_or": mantel_haenszel_or(cells, form_a, form_b),
        "inference": "descriptive-only; no additional null run",
    }


def leave_one_root_out(cells, form_a, form_b):
    values = {}
    for root in cells:
        reduced = {key: value for key, value in cells.items() if key != root}
        values[root] = weighted_stat(reduced, form_a, form_b)
    return {
        "min": min(values.values()) if values else None,
        "max": max(values.values()) if values else None,
        "values": values,
    }


def period_directions(tokens, form_a, form_b):
    output = {}
    for period in ("Meccan", "Medinan"):
        cells = cells_for(tokens, form_a, form_b, 1, period=period)
        output[period] = {
            "eligible_roots": len(cells),
            "weighted_rate_difference": weighted_stat(cells, form_a, form_b),
        }
    return output


def passive_control(all_joined):
    encoded = [{**token, "passive_outcome": token["passive"]} for token in all_joined]
    cells = cells_for(encoded, "II", "V", 2, outcome="passive_outcome")
    return {
        "eligible_roots": len(cells),
        "weighted_passive_rate_difference_II_minus_V": weighted_stat(cells, "II", "V"),
        "inference": "descriptive orthogonality control; no additional null run",
    }


def write_validation_sample(sample_path, key_path, tokens, verses):
    """Prereg §6.8/§8 — seed-locked blinded sample, {II,V,III,VI}x{Obj+,Obj-}, <=10/cell.

    The TSV hides form, root and the machine `has_object` verdict so a reviewer can
    annotate independently; `validation-key.json` reveals the strata after review.
    """
    strata = defaultdict(list)
    for token in tokens:
        if token["form"] not in {"II", "V", "III", "VI"}:
            continue
        strata[(token["form"], bool(token["has_object"]))].append(token)

    rng = random.Random(SEED)
    rows, key = [], {}
    for stratum in sorted(strata, key=lambda item: (item[0], item[1])):
        members = sorted(strata[stratum], key=lambda token: token["location"])
        chosen = rng.sample(members, min(10, len(members)))
        for token in chosen:
            rows.append(token)
            key[token["location"]] = {
                "form": token["form"],
                "root": token["root"],
                "machine_has_object": bool(token["has_object"]),
                "stratum": f"{stratum[0]}|{'Obj+' if stratum[1] else 'Obj-'}",
                "object_edges": token["object_edges"],
            }
    rng.shuffle(rows)

    with open(sample_path, "x", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow([
            "sample_id", "verb_location", "verb_surface", "verse_text",
            "review_has_overt_direct_object", "review_object_span", "review_notes",
        ])
        for index, token in enumerate(rows, start=1):
            writer.writerow([
                f"S{index:03d}",
                token["location"],
                token["surface"],
                verses.get((token["chapter"], token["verse"]), ""),
                "", "", "",
            ])

    with open(key_path, "x", encoding="utf-8") as handle:
        json.dump(
            {
                "note": "Revealed AFTER independent review. Blank review columns in the "
                        "machine run are intentional; results remain "
                        "dependency-annotation-limited until reviewed.",
                "seed": SEED,
                "cell_cap": 10,
                "sample_id_by_location": {
                    token["location"]: f"S{index:03d}" for index, token in enumerate(rows, start=1)
                },
                "key": key,
            },
            handle, ensure_ascii=False, indent=2, sort_keys=True,
        )
        handle.write("\n")
    return {"rows": len(rows), "strata": {f"{k[0]}|{'Obj+' if k[1] else 'Obj-'}": len(v) for k, v in strata.items()}}


def load_verses(path):
    """quran-no-tashkeel.json: list of surahs, each with `id` and nested `verses`."""
    with open(path, encoding="utf-8") as handle:
        raw = json.load(handle)
    verses = {}
    for surah in raw:
        chapter = int(surah["id"])
        for verse in surah["verses"]:
            verses[(chapter, int(verse["id"]))] = verse["text"]
    return verses


def git_output(repo_root, *args):
    return subprocess.check_output(["git", *args], cwd=repo_root, text=True).strip()


def self_check():
    positive = {
        "r1": {"II": (4, 4), "V": (4, 0)},
        "r2": {"II": (2, 1), "V": (2, 0)},
    }
    reversed_cells = {
        root: {"II": forms["V"], "V": forms["II"]}
        for root, forms in positive.items()
    }
    assert weighted_stat(positive, "II", "V") > 0
    assert weighted_stat(reversed_cells, "II", "V") < 0
    observed, p_value, size, kind = permutation_test(positive, "II", "V", exact=True)
    assert observed > 0 and 0 < p_value <= 1 and size == 4 and kind == "exact"
    _, token_p, token_size, token_kind = token_label_test(positive, "II", "V", n_perm=100)
    assert 0 < token_p <= 1 and token_size == 100 and token_kind == "within-root-token-label"
    print("self-check: PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--eqtb", type=Path, help="Path to extracted EQTB Quranic.csv")
    parser.add_argument("--run-id", help="Immutable run directory name; defaults to UTC timestamp")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.eqtb:
        parser.error("--eqtb is required")

    repo_root = Path(__file__).resolve().parents[3]
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-2540-form-v-valency.md"
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"
    chronology = repo_root / "data/revelation-order.csv"
    quran = repo_root / "quran-text/quran-no-tashkeel.json"
    script = Path(__file__).resolve()
    hashes = {
        "prereg": sha256(prereg), "qac": sha256(qac), "eqtb": sha256(args.eqtb),
        "chronology": sha256(chronology), "quran_no_tashkeel": sha256(quran),
        "script": sha256(script),
    }
    expected = {
        "prereg": EXPECTED_PREREG_SHA, "qac": EXPECTED_QAC_SHA, "eqtb": EXPECTED_EQTB_SHA,
        "chronology": EXPECTED_CHRONOLOGY_SHA, "quran_no_tashkeel": EXPECTED_QURAN_SHA,
    }
    for key, expected_hash in expected.items():
        if hashes[key] != expected_hash:
            raise SystemExit(f"{key} SHA mismatch: expected {expected_hash}, found {hashes[key]}")

    # Prereg §4.5 / §6.7 — all integrity gates abort BEFORE a run directory exists.
    qac_verbs, qac_duplicates = parse_qac(qac)
    eqtb_verbs, object_edges, eqtb_duplicates = parse_eqtb(args.eqtb)
    if qac_duplicates or eqtb_duplicates:
        raise SystemExit(
            f"duplicate real locations abort the run: "
            f"qac={len(qac_duplicates)} {qac_duplicates[:5]} "
            f"eqtb={len(eqtb_duplicates)} {eqtb_duplicates[:5]}"
        )
    periods = load_periods(chronology)
    verses = load_verses(quran)
    all_joined, unmatched, agreement = join_tokens(qac_verbs, eqtb_verbs, object_edges, periods)
    if agreement["form_rate"] < 1.0 or agreement["root_rate"] < 1.0:
        raise SystemExit(
            "QAC/EQTB lineage mismatch aborts the run (prereg §6.7 requires 100%): "
            f"form_rate={agreement['form_rate']:.6f} root_rate={agreement['root_rate']:.6f}"
        )
    active_joined = [token for token in all_joined if not token["passive"]]

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2540" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    h1 = summarize_family(active_joined, "II", "V", min_count=2, exact=False, seed_null_b=SEED_H1_NULL_B)
    h2_cells = cells_for(active_joined, "III", "VI", 1)
    h2 = summarize_family(
        active_joined, "III", "VI", min_count=1, exact=len(h2_cells) <= 20, seed_null_b=SEED_H2_NULL_B
    )
    h1_cells = cells_for(active_joined, "II", "V", 2)
    sensitivity = describe_family(active_joined, "II", "V", min_count=1)

    result = {
        "id": "H-NEW-2540",
        "registered_alpha_bonferroni": ALPHA_BON,
        "tests_in_family": TESTS_IN_FAMILY,
        "raw_p_gate": RAW_GATE,
        "corrected_novelty_gate": CORRECTED_GATE,
        "h1_primary_II_to_V": h1,
        "h2_secondary_III_to_VI": h2,
        "sensitivity_II_to_V_min1": sensitivity,
        "h1_leave_one_root_out": leave_one_root_out(h1_cells, "II", "V"),
        "h1_period_directions_min1": period_directions(active_joined, "II", "V"),
        "passive_orthogonality_control": passive_control(all_joined),
        "join": {
            "qac_verbs": len(qac_verbs),
            "eqtb_verbs": len(eqtb_verbs),
            "joined_verbs": len(all_joined),
            "joined_active_verbs": len(active_joined),
            "unmatched_qac_verbs": len(unmatched),
            "unmatched_eqtb_verbs": len(set(eqtb_verbs) - set(qac_verbs)),
            "qac_duplicate_locations": len(qac_duplicates),
            "eqtb_duplicate_locations": len(eqtb_duplicates),
            "qac_eqtb_agreement": agreement,
            "lineage_gate": "100% required; run aborts otherwise (prereg §6.7)",
        },
        "annotation_limit": (
            "Dependency-annotation-limited: EQTB Obj accuracy is the material limit. "
            "validation-sample.tsv review columns are blank until qualified reviewers "
            "report precision, recall and differential error by form (prereg §6.8)."
        ),
    }
    if h1["passes_strict_gate"] and h2["passes_strict_gate"]:
        verdict = "DUAL-FAMILY SUPPORT"
    elif h1["passes_strict_gate"]:
        verdict = "FORM-II→V SUPPORTED; III→VI NULL/UNRESOLVED"
    elif h1["direction_positive"]:
        verdict = "NULL — H1 direction held but did not pass"
    else:
        verdict = "NULL/REVERSED — H1 locked direction failed"
    verdict += "; DEPENDENCY-ANNOTATION-LIMITED"
    result["verdict"] = verdict

    result_path = run_dir / "result.json"
    with open(result_path, "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    sample_meta = write_validation_sample(
        run_dir / "validation-sample.tsv", run_dir / "validation-key.json", active_joined, verses
    )

    manifest = {
        "id": "H-NEW-2540",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "git_commit": git_output(repo_root, "rev-parse", "HEAD"),
        "git_status_porcelain": git_output(repo_root, "status", "--porcelain"),
        "hashes_sha256": hashes,
        "expected_hashes_sha256": expected,
        "python": sys.version,
        "platform": platform.platform(),
        "seed": SEED,
        "seeds": {"null_a": SEED_NULL_A, "h1_null_b": SEED_H1_NULL_B, "h2_null_b": SEED_H2_NULL_B},
        "n_permutations": N_PERM,
        "validation_sample": sample_meta,
        "eqtb_path": str(args.eqtb.resolve()),
        "run_directory": str(run_dir.relative_to(repo_root)),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir),
        "verdict": verdict,
        "h1_p": [h1["p_root_swap_one_sided"], h1["p_token_label_one_sided"]],
        "h2_p": [h2["p_root_swap_one_sided"], h2["p_token_label_one_sided"]],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
