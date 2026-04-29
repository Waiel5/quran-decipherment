#!/usr/bin/env python3
"""H-NEW-269 — qul imperative addressee-pattern test.

Pre-reg:
  findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern-prereg.md

Question:
  Do a few coarse quoted-speech addressee / rhetorical-context opener
  families inside the 332 canonical qul imperatives remain coherent
  after their defining opener token is stripped away?

Design:
  - 4 inferential classes, all defined by the first normalized token
    after qul
  - residual window = next up to 6 words after opener stripping
  - residual representation = set of QAC STEM roots
  - statistic = mean pairwise Jaccard within class
  - null = matched nonclass qul tokens, nearest by residual root mass
  - MW-5 = araytum / araitukum subfamily
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
QAC_FILE = ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-269.json"

SEED = 20260418
N_PERM = 5000
WINDOW_WORDS = 6
ALPHA_BON = 0.05 / 4.0
BON_FAMILY = "h-new-269-qul-addressee-pattern"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
TASHKEEL_RE = re.compile(r"[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]")
PUNCT_RE = re.compile(r"[\u06D4\u06DD\u06DE\u06DF\u060C\u061B\u061F\u0640\u200C\u200D\u200E\u200F\u00B7]+")

INTERROGATIVE_TOKENS = {
    "من",
    "ما",
    "هل",
    "ارايتم",
    "ارايتكم",
    "هاتوا",
    "فاتوا",
    "اغير",
    "افلا",
}
SELF_TOKENS = {"اني", "انني", "انا", "رب", "ربي", "اعوذ", "اللهم", "حسبي"}
ARAYTUM_TOKENS = {"ارايتم", "ارايتكم"}

CLASS_ORDER = [
    "vocative_address",
    "interrogative_or_challenge",
    "self_or_devotional",
    "restrictive_declaration",
]

CLASS_META = {
    "vocative_address": {
        "label": "Vocative address",
        "rule": "first token after qul = يا; strip يا, and strip ايها too if immediately following",
    },
    "interrogative_or_challenge": {
        "label": "Interrogative / challenge",
        "rule": "first token after qul in {من, ما, هل, ارايتم, ارايتكم, هاتوا, فاتوا, اغير, افلا}; strip first token",
    },
    "self_or_devotional": {
        "label": "Self / devotional",
        "rule": "first token after qul in {اني, انني, انا, رب, ربي, اعوذ, اللهم, حسبي}; strip first token",
    },
    "restrictive_declaration": {
        "label": "Restrictive declaration",
        "rule": "first token after qul = انما; strip first token",
    },
}


def normalize_token(word: str) -> str:
    word = TASHKEEL_RE.sub("", word)
    word = PUNCT_RE.sub("", word)
    for src, dst in [
        ("أ", "ا"),
        ("إ", "ا"),
        ("آ", "ا"),
        ("ٱ", "ا"),
        ("ء", "ا"),
        ("ؤ", "و"),
        ("ئ", "ي"),
        ("ى", "ي"),
        ("ة", "ه"),
    ]:
        word = word.replace(src, dst)
    return word.strip()


def classify_after_tokens(after_tokens: list[str]) -> tuple[str, int]:
    if not after_tokens:
        return "other", 0
    first = after_tokens[0]
    if first == "يا":
        drop = 2 if len(after_tokens) > 1 and after_tokens[1] == "ايها" else 1
        return "vocative_address", drop
    if first in INTERROGATIVE_TOKENS:
        return "interrogative_or_challenge", 1
    if first in SELF_TOKENS:
        return "self_or_devotional", 1
    if first == "انما":
        return "restrictive_declaration", 1
    return "other", 0


def load_verse_tokens() -> dict[tuple[int, int], list[str]]:
    with QURAN_JSON.open(encoding="utf-8") as fh:
        quran = json.load(fh)

    verse_tokens: dict[tuple[int, int], list[str]] = {}
    for surah in quran:
        sid = int(surah["id"])
        for verse in surah["verses"]:
            vid = int(verse["id"])
            tokens = [normalize_token(t) for t in verse["text"].split()]
            verse_tokens[(sid, vid)] = [t for t in tokens if t]
    return verse_tokens


def load_roots_by_word() -> dict[tuple[int, int, int], set[str]]:
    roots_by_word: dict[tuple[int, int, int], set[str]] = defaultdict(set)
    with QAC_FILE.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, _, _, feats = parts[:4]
            if "STEM" not in feats:
                continue
            loc_match = LOC_RE.match(loc)
            root_match = ROOT_RE.search(feats)
            if not loc_match or not root_match:
                continue
            sid, vid, wid = int(loc_match.group(1)), int(loc_match.group(2)), int(loc_match.group(3))
            roots_by_word[(sid, vid, wid)].add(root_match.group(1))
    return roots_by_word


def extract_qul_tokens(
    verse_tokens: dict[tuple[int, int], list[str]],
    roots_by_word: dict[tuple[int, int, int], set[str]],
) -> list[dict]:
    out: list[dict] = []
    seen: set[tuple[int, int, int]] = set()

    with QAC_FILE.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, _, _, feats = parts[:4]
            if not (
                "POS:V" in feats
                and "IMPV" in feats
                and "LEM:qaAla" in feats
                and "|2MS" in feats
            ):
                continue
            loc_match = LOC_RE.match(loc)
            if not loc_match:
                continue
            sid, vid, wid = int(loc_match.group(1)), int(loc_match.group(2)), int(loc_match.group(3))
            key = (sid, vid, wid)
            if key in seen:
                continue
            seen.add(key)

            tokens = verse_tokens[(sid, vid)]
            after_tokens = tokens[wid:]
            class_id, strip_words = classify_after_tokens(after_tokens)

            start_wid = wid + strip_words + 1
            end_wid = min(len(tokens), wid + strip_words + WINDOW_WORDS)
            kept_word_ids = list(range(start_wid, end_wid + 1))

            residual_roots: set[str] = set()
            residual_mass = 0
            residual_tokens: list[str] = []
            for kept_wid in kept_word_ids:
                residual_tokens.append(tokens[kept_wid - 1])
                roots_here = roots_by_word.get((sid, vid, kept_wid), set())
                residual_roots.update(roots_here)
                residual_mass += len(roots_here)

            out.append(
                {
                    "id": len(out),
                    "sid": sid,
                    "vid": vid,
                    "wid": wid,
                    "ref": f"{sid}:{vid}:{wid}",
                    "class_id": class_id,
                    "first_token": after_tokens[0] if after_tokens else "",
                    "after_preview": " ".join(after_tokens[:8]),
                    "strip_words": strip_words,
                    "residual_tokens": residual_tokens,
                    "residual_preview": " ".join(residual_tokens[:8]),
                    "residual_roots": sorted(residual_roots),
                    "residual_root_set": residual_roots,
                    "residual_mass": residual_mass,
                }
            )

    out.sort(key=lambda row: (row["sid"], row["vid"], row["wid"]))
    for idx, row in enumerate(out):
        row["id"] = idx
    return out


def build_pairwise_jaccard(tokens: list[dict]) -> list[list[float]]:
    n = len(tokens)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        roots_i = tokens[i]["residual_root_set"]
        for j in range(i + 1, n):
            roots_j = tokens[j]["residual_root_set"]
            union = roots_i | roots_j
            value = len(roots_i & roots_j) / len(union) if union else 0.0
            matrix[i][j] = value
            matrix[j][i] = value
    return matrix


def mean_pairwise_jaccard(ids: list[int], pairwise: list[list[float]]) -> float:
    if len(ids) < 2:
        return 0.0
    total = 0.0
    n_pairs = 0
    for pos, a in enumerate(ids):
        row = pairwise[a]
        for b in ids[pos + 1 :]:
            total += row[b]
            n_pairs += 1
    return total / n_pairs if n_pairs else 0.0


def build_candidate_lists(member_ids: list[int], pool_ids: list[int], tokens: list[dict]) -> dict[int, list[int]]:
    k = min(len(pool_ids), max(40, 2 * len(member_ids)))
    candidates: dict[int, list[int]] = {}
    for member_id in member_ids:
        mass = tokens[member_id]["residual_mass"]
        candidates[member_id] = sorted(
            pool_ids,
            key=lambda pool_id: (
                abs(math.log(tokens[pool_id]["residual_mass"] + 1) - math.log(mass + 1)),
                abs(tokens[pool_id]["residual_mass"] - mass),
                pool_id,
            ),
        )[:k]
    return candidates


def sample_matched_set(
    member_ids: list[int],
    candidate_lists: dict[int, list[int]],
    rng: random.Random,
    max_attempts: int = 200,
) -> list[int] | None:
    for _ in range(max_attempts):
        used: set[int] = set()
        picks: list[int] = []
        remaining = list(member_ids)
        ok = True
        while remaining:
            remaining.sort(key=lambda member_id: sum(1 for c in candidate_lists[member_id] if c not in used))
            member_id = remaining.pop(0)
            choices = [c for c in candidate_lists[member_id] if c not in used]
            if not choices:
                ok = False
                break
            pick = rng.choice(choices)
            used.add(pick)
            picks.append(pick)
        if ok:
            return picks
    return None


def quantile_95(values: list[float]) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = max(0, math.ceil(0.95 * len(ordered)) - 1)
    return ordered[idx]


def top_pairs(ids: list[int], pairwise: list[list[float]], tokens: list[dict], n: int = 5) -> list[dict]:
    rows = []
    for pos, a in enumerate(ids):
        for b in ids[pos + 1 :]:
            rows.append(
                {
                    "a": tokens[a]["ref"],
                    "b": tokens[b]["ref"],
                    "jaccard": round(pairwise[a][b], 6),
                    "a_preview": tokens[a]["residual_preview"],
                    "b_preview": tokens[b]["residual_preview"],
                }
            )
    rows.sort(key=lambda row: (-row["jaccard"], row["a"], row["b"]))
    return rows[:n]


def permutation_test(
    label: str,
    member_ids: list[int],
    pool_ids: list[int],
    tokens: list[dict],
    pairwise: list[list[float]],
    seed: int,
    n_perm: int,
) -> dict:
    observed = mean_pairwise_jaccard(member_ids, pairwise)
    candidates = build_candidate_lists(member_ids, pool_ids, tokens)
    rng = random.Random(seed)

    null_values: list[float] = []
    failed_draws = 0
    for _ in range(n_perm):
        sample = sample_matched_set(member_ids, candidates, rng)
        if sample is None:
            failed_draws += 1
            continue
        null_values.append(mean_pairwise_jaccard(sample, pairwise))

    if not null_values:
        raise RuntimeError(f"{label}: matched null produced zero successful draws")

    null_mean = statistics.mean(null_values)
    null_sd = statistics.stdev(null_values) if len(null_values) > 1 else 0.0
    p_upper = (1.0 + sum(value >= observed for value in null_values)) / (len(null_values) + 1.0)
    z_score = (observed - null_mean) / null_sd if null_sd > 0 else 0.0

    return {
        "n_members": len(member_ids),
        "observed_mean_pairwise_jaccard": observed,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "null_q95": quantile_95(null_values),
        "z_vs_null": z_score,
        "p_perm_upper": p_upper,
        "successful_draws": len(null_values),
        "failed_draws": failed_draws,
        "candidate_pool_k": len(next(iter(candidates.values()))) if candidates else 0,
        "top_pairs": top_pairs(member_ids, pairwise, tokens),
    }


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

    verse_tokens = load_verse_tokens()
    roots_by_word = load_roots_by_word()
    tokens = extract_qul_tokens(verse_tokens, roots_by_word)
    pairwise = build_pairwise_jaccard(tokens)

    total_qul = len(tokens)
    unique_verses = len({(row["sid"], row["vid"]) for row in tokens})
    class_counts = Counter(row["class_id"] for row in tokens)
    class_unique_verses = {
        class_id: len({(row["sid"], row["vid"]) for row in tokens if row["class_id"] == class_id})
        for class_id in class_counts
    }

    print(f"Loaded {total_qul} canonical qul tokens across {unique_verses} verses.", file=sys.stderr)
    print(f"Class counts: {dict(class_counts)}", file=sys.stderr)

    cells: dict[str, dict] = {}
    pass_count = 0
    for offset, class_id in enumerate(CLASS_ORDER, start=1):
        member_ids = [row["id"] for row in tokens if row["class_id"] == class_id]
        pool_ids = [row["id"] for row in tokens if row["class_id"] != class_id]
        result = permutation_test(
            label=class_id,
            member_ids=member_ids,
            pool_ids=pool_ids,
            tokens=tokens,
            pairwise=pairwise,
            seed=SEED + offset,
            n_perm=N_PERM,
        )
        result["label"] = CLASS_META[class_id]["label"]
        result["rule"] = CLASS_META[class_id]["rule"]
        result["unique_verses"] = class_unique_verses[class_id]
        result["share_of_332"] = len(member_ids) / total_qul
        result["examples"] = [
            {
                "ref": row["ref"],
                "first_token": row["first_token"],
                "after_preview": row["after_preview"],
                "residual_preview": row["residual_preview"],
            }
            for row in tokens
            if row["class_id"] == class_id
        ][:10]
        result["bonferroni_pass"] = result["p_perm_upper"] < ALPHA_BON
        if result["bonferroni_pass"]:
            pass_count += 1
        cells[class_id] = result
        print(
            f"{class_id}: n={result['n_members']} obs={result['observed_mean_pairwise_jaccard']:.4f} "
            f"null={result['null_mean']:.4f} z={result['z_vs_null']:.3f} "
            f"p={result['p_perm_upper']:.4f} pass={result['bonferroni_pass']}",
            file=sys.stderr,
        )

    mw5_ids = [row["id"] for row in tokens if row["first_token"] in ARAYTUM_TOKENS]
    mw5_pool = [row["id"] for row in tokens if row["first_token"] not in ARAYTUM_TOKENS]
    mw5 = permutation_test(
        label="mw5_araytum_family",
        member_ids=mw5_ids,
        pool_ids=mw5_pool,
        tokens=tokens,
        pairwise=pairwise,
        seed=SEED + 99,
        n_perm=N_PERM,
    )
    mw5["label"] = "a-ra'aytum / a-ra'aytakum template"
    mw5["rule"] = "first token after qul in {ارايتم, ارايتكم}; strip first token"
    mw5["pass_nominal_005"] = mw5["p_perm_upper"] < 0.05
    mw5["examples"] = [
        {
            "ref": row["ref"],
            "after_preview": row["after_preview"],
            "residual_preview": row["residual_preview"],
        }
        for row in tokens
        if row["first_token"] in ARAYTUM_TOKENS
    ]
    print(
        f"MW-5 araytum: n={mw5['n_members']} obs={mw5['observed_mean_pairwise_jaccard']:.4f} "
        f"null={mw5['null_mean']:.4f} z={mw5['z_vs_null']:.3f} "
        f"p={mw5['p_perm_upper']:.4f} pass={mw5['pass_nominal_005']}",
        file=sys.stderr,
    )

    if not mw5["pass_nominal_005"]:
        verdict = "NULL-BROKEN"
    elif pass_count == 0:
        verdict = "NULL"
    elif pass_count == 1:
        verdict = "PARTIAL-CLASS-ONLY"
    else:
        verdict = "PASS-DIRECTED"

    top_first_tokens = Counter(row["first_token"] for row in tokens).most_common(20)
    inferential_token_count = sum(class_counts[class_id] for class_id in CLASS_ORDER)

    payload = {
        "id": "H-NEW-269",
        "title": "qul imperative addressee-pattern test",
        "prereg_file": str(PREREG_FILE),
        "prereg_sha256": prereg_sha,
        "script": str(Path(__file__)),
        "seed": SEED,
        "n_perm": N_PERM,
        "window_words_after_strip": WINDOW_WORDS,
        "bonferroni_family": BON_FAMILY,
        "bonferroni_k": 4,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(332 canonical qul tokens from Leeds QAC v0.4; no-tashkeel normalized token windows; QAC STEM roots; opener-family stripping; matched nonclass qul null on residual 6-word root mass)",
        "corpus": {
            "qul_tokens": total_qul,
            "qul_unique_verses": unique_verses,
            "class_counts": dict(class_counts),
            "class_unique_verses": class_unique_verses,
            "inferential_class_tokens": inferential_token_count,
            "other_tokens": class_counts["other"],
            "inferential_share_of_332": inferential_token_count / total_qul,
            "top_first_tokens": [{"token": token, "count": count} for token, count in top_first_tokens],
        },
        "class_definitions": CLASS_META,
        "cells": cells,
        "mw5": mw5,
        "pass_count": pass_count,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[out] wrote {OUT_JSON}", file=sys.stderr)


if __name__ == "__main__":
    main()
