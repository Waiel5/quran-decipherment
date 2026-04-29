#!/usr/bin/env python3
"""
Q002_F_master.py — runs all 5 pre-registered Q 2 novel-finding tests.

Embeds SHA256 of each pre-reg file and fails fast on mismatch (PRE-REG-STANDARD-04).
Stdlib only.
"""
from __future__ import annotations
import hashlib, json, math, os, random, re, sys
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_SHAS = {
    "Q002-F-01": ("Q002-F-01-ayat-al-kursi-divine-name-density-prereg.md",
                  "e395b9bb9b8ccc02ff2105520c624a18106b5ccffd061ea4f79771cbcd679b2c"),
    "Q002-F-02": ("Q002-F-02-khawatim-baqara-divine-name-density-prereg.md",
                  "3be0c7c69db7d18ab2938d462ba99c8c028afdcd7e5c8c75131f9e0d135fa8bd"),
    "Q002-F-03": ("Q002-F-03-q2-centrality-test-prereg.md",
                  "8d8088867adcb9575df2cb318b2345d06f0485a247121c91e74fb5f659b53d97"),
    "Q002-F-04": ("Q002-F-04-ring-structure-prereg.md",
                  "3eca733aa682e9e2e114fb8a62e464b3797b00ca099eb0baacb202644ef44127"),
    "Q002-F-05": ("Q002-F-05-q2-282-longest-verse-prereg.md",
                  "fb5441680e8b7d04f3ddf2d10a29c35db94fd0052b15e1e7d5b081b3d60c817a"),
}
PREREG_DIR = ROOT / "surahs" / "Q002-al-baqara"
OUT_DIR    = PREREG_DIR / "csv"
SEED       = 20260428

SAJDA_RE = re.compile(r"[ۖ-ۭۚۛۜ]")  # Arabic sajda/recitation marks
WS_RE    = re.compile(r"\s+")


def _verify_pre_regs():
    for tid, (fname, sha_expected) in PREREG_SHAS.items():
        p = PREREG_DIR / fname
        if not p.exists():
            print(f"FAIL: pre-reg missing for {tid}: {p}", file=sys.stderr); sys.exit(2)
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        if sha != sha_expected:
            print(f"FAIL: SHA mismatch for {tid}: got {sha}, expected {sha_expected}", file=sys.stderr)
            sys.exit(2)
    print("[ok] pre-reg SHA256 checks passed for all 5 tests.")


def _norm(text: str) -> str:
    return WS_RE.sub(" ", SAJDA_RE.sub(" ", text)).strip()


def _verse_words(text: str) -> list[str]:
    return [w for w in _norm(text).split() if w]


def _load_quran(variant: str = "no-tashkeel") -> list[dict]:
    fp = ROOT / "quran-text" / f"quran-{variant}.json"
    return json.loads(fp.read_text())


def _load_99_names() -> list[str]:
    fp = ROOT / "data" / "asma-al-husna.txt"
    out = []
    for line in fp.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


# -------------------------- Q002-F-01 --------------------------------------

def _name_occurrences_in_verse(words: list[str], names: list[str]) -> tuple[int, int, list[str]]:
    """
    Returns (total_occurrences, distinct_names_count, distinct_names_list).
    Multi-token names are matched as adjacent token sequences.
    """
    matched = []
    occ_count = 0
    # Sort names by descending token-length so multi-token names match first
    sorted_names = sorted(names, key=lambda n: -len(n.split()))
    # Build occupancy mask so a token is consumed only once
    n = len(words)
    mask = [False] * n
    for name in sorted_names:
        toks = name.split()
        ln = len(toks)
        for i in range(0, n - ln + 1):
            if any(mask[i:i+ln]):
                continue
            if words[i:i+ln] == toks:
                # match
                occ_count += 1
                if name not in matched:
                    matched.append(name)
                for k in range(i, i+ln):
                    mask[k] = True
    return occ_count, len(matched), matched


def Q002_F_01(quran_no_tashkeel, quran_min_tashkeel, names) -> dict:
    print("[Q002-F-01] Computing divine-name density across all 6236 verses...")
    rows = []
    for s in quran_no_tashkeel:
        for v in s["verses"]:
            words = _verse_words(v["text"])
            wl = len(words)
            occ, dn, mn = _name_occurrences_in_verse(words, names)
            rows.append(dict(
                surah=s["id"], verse=v["id"], wlen=wl,
                occ=occ, distinct=dn,
                total_density=occ / wl if wl else 0.0,
                distinct_density=dn / wl if wl else 0.0,
                names=mn,
            ))

    # rank descending by total_density
    by_total = sorted(rows, key=lambda r: (-r["total_density"], -r["occ"], r["wlen"]))
    by_distinct = sorted(rows, key=lambda r: (-r["distinct_density"], -r["distinct"], r["wlen"]))
    # Absolute counts (post-hoc / MW-3 alternative; classical rules-tuple)
    by_occ_abs = sorted(rows, key=lambda r: (-r["occ"], -r["distinct"]))
    by_distinct_abs = sorted(rows, key=lambda r: (-r["distinct"], -r["occ"]))

    rank_map_total = {(r["surah"], r["verse"]): i + 1 for i, r in enumerate(by_total)}
    rank_map_distinct = {(r["surah"], r["verse"]): i + 1 for i, r in enumerate(by_distinct)}
    rank_map_occ_abs = {(r["surah"], r["verse"]): i + 1 for i, r in enumerate(by_occ_abs)}
    rank_map_distinct_abs = {(r["surah"], r["verse"]): i + 1 for i, r in enumerate(by_distinct_abs)}

    target = (2, 255)
    target_row = next(r for r in rows if (r["surah"], r["verse"]) == target)

    # MW-5 replication: min-tashkeel — does Q 2:255 stay top-10?
    min_rows = []
    for s in quran_min_tashkeel:
        for v in s["verses"]:
            words = _verse_words(v["text"])
            occ, dn, _ = _name_occurrences_in_verse(words, names)
            wl = len(words)
            min_rows.append(dict(
                surah=s["id"], verse=v["id"], wlen=wl,
                total_density=occ / wl if wl else 0.0,
                distinct_density=dn / wl if wl else 0.0,
                occ=occ, distinct=dn,
            ))
    min_by_total = sorted(min_rows, key=lambda r: (-r["total_density"], -r["occ"], r["wlen"]))
    min_rank = next(i + 1 for i, r in enumerate(min_by_total) if (r["surah"], r["verse"]) == target)

    # Top-20 by total_density
    top20 = [{"surah": r["surah"], "verse": r["verse"], "wlen": r["wlen"],
              "occ": r["occ"], "distinct": r["distinct"],
              "total_density": round(r["total_density"], 5),
              "distinct_density": round(r["distinct_density"], 5),
              "names": r["names"]}
             for r in by_total[:20]]
    top20_distinct = [{"surah": r["surah"], "verse": r["verse"], "wlen": r["wlen"],
                       "occ": r["occ"], "distinct": r["distinct"],
                       "total_density": round(r["total_density"], 5),
                       "distinct_density": round(r["distinct_density"], 5),
                       "names": r["names"]}
                      for r in by_distinct[:20]]

    # Word-length-only rank (control: is Q 2:255 short?)
    by_wlen_asc = sorted(rows, key=lambda r: r["wlen"])
    wlen_rank_asc = next(i + 1 for i, r in enumerate(by_wlen_asc)
                         if (r["surah"], r["verse"]) == target)

    # Top-15 by absolute occ
    top15_occ_abs = [{"surah": r["surah"], "verse": r["verse"], "wlen": r["wlen"],
                      "occ": r["occ"], "distinct": r["distinct"], "names": r["names"]}
                     for r in by_occ_abs[:15]]
    top15_distinct_abs = [{"surah": r["surah"], "verse": r["verse"], "wlen": r["wlen"],
                           "occ": r["occ"], "distinct": r["distinct"], "names": r["names"]}
                          for r in by_distinct_abs[:15]]

    return {
        "test_id": "Q002-F-01",
        "verse": "Q 2:255 (Āyat al-Kursī)",
        "n_verses": len(rows),
        "wlen": target_row["wlen"],
        "occ": target_row["occ"],
        "distinct_names_count": target_row["distinct"],
        "distinct_names": target_row["names"],
        "total_density": target_row["total_density"],
        "distinct_density": target_row["distinct_density"],
        "rank_total_density": rank_map_total[target],
        "rank_distinct_density": rank_map_distinct[target],
        "rank_absolute_occ": rank_map_occ_abs[target],
        "rank_absolute_distinct": rank_map_distinct_abs[target],
        "min_tashkeel_rank_total": min_rank,
        "wlen_rank_ascending": wlen_rank_asc,
        "top20_by_total_density": top20,
        "top20_by_distinct_density": top20_distinct,
        "top15_by_absolute_occ": top15_occ_abs,
        "top15_by_absolute_distinct": top15_distinct_abs,
    }


# -------------------------- Q002-F-02 --------------------------------------

def Q002_F_02(quran_no_tashkeel, names) -> dict:
    print("[Q002-F-02] Computing 3-verse-window divine-name density...")
    # Build a flat list of verses in canonical order
    flat = []
    for s in quran_no_tashkeel:
        for v in s["verses"]:
            words = _verse_words(v["text"])
            occ, dn, mn = _name_occurrences_in_verse(words, names)
            flat.append({"surah": s["id"], "verse": v["id"], "wlen": len(words),
                         "occ": occ, "distinct": dn, "names": mn})
    n = len(flat)

    # In-surah-only sliding windows (cleaner): within each surah, all (i, i+1, i+2) triplets.
    rows = []
    for s in quran_no_tashkeel:
        sid = s["id"]
        verses_s = [r for r in flat if r["surah"] == sid]
        for i in range(len(verses_s) - 2):
            triple = verses_s[i:i+3]
            wl = sum(r["wlen"] for r in triple)
            occ_total = sum(r["occ"] for r in triple)
            distinct_set = []
            for r in triple:
                for nm in r["names"]:
                    if nm not in distinct_set:
                        distinct_set.append(nm)
            rows.append(dict(
                surah=sid,
                vstart=triple[0]["verse"], vend=triple[2]["verse"],
                wlen=wl, occ=occ_total, distinct=len(distinct_set),
                total_density=occ_total / wl if wl else 0.0,
                distinct_density=len(distinct_set) / wl if wl else 0.0,
                names=distinct_set,
            ))

    by_total = sorted(rows, key=lambda r: (-r["total_density"], -r["occ"], r["wlen"]))
    by_distinct = sorted(rows, key=lambda r: (-r["distinct_density"], -r["distinct"], r["wlen"]))

    target = (2, 284, 286)

    def _find(L, t):
        for i, r in enumerate(L):
            if (r["surah"], r["vstart"], r["vend"]) == t:
                return i + 1, r
        return None, None

    rank_total, t_row = _find(by_total, target)
    rank_distinct, _ = _find(by_distinct, target)

    # comparator: Q 59:22-24
    rank59_total, _ = _find(by_total, (59, 22, 24))
    rank59_distinct, _ = _find(by_distinct, (59, 22, 24))

    top20 = [{"surah": r["surah"], "vstart": r["vstart"], "vend": r["vend"],
              "wlen": r["wlen"], "occ": r["occ"], "distinct": r["distinct"],
              "total_density": round(r["total_density"], 5),
              "distinct_density": round(r["distinct_density"], 5),
              "names": r["names"]}
             for r in by_total[:20]]

    return {
        "test_id": "Q002-F-02",
        "window": "Q 2:284-286 (Khawātim al-Baqara)",
        "n_windows": len(rows),
        "wlen": t_row["wlen"],
        "occ": t_row["occ"],
        "distinct_names_count": t_row["distinct"],
        "distinct_names": t_row["names"],
        "total_density": t_row["total_density"],
        "distinct_density": t_row["distinct_density"],
        "rank_total_density": rank_total,
        "rank_distinct_density": rank_distinct,
        "Q59_22_24_rank_total": rank59_total,
        "Q59_22_24_rank_distinct": rank59_distinct,
        "top20_by_total_density": top20,
    }


# -------------------------- Q002-F-03 --------------------------------------

def _load_dist_matrix() -> list[list[float]]:
    fp = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
    d = json.loads(fp.read_text())
    triples = d["D_matrix_upper_triangular"]
    M = [[0.0] * 114 for _ in range(114)]
    for i, j, v in triples:
        i0, j0 = i - 1, j - 1
        M[i0][j0] = v
        M[j0][i0] = v
    return M


def Q002_F_03(D) -> dict:
    print("[Q002-F-03] Computing centrality / leave-one-out shifts...")
    n = 114
    # Mean distance from each surah to all others
    mean_d = [sum(D[i]) / (n - 1) for i in range(n)]
    medoid_idx = min(range(n), key=lambda i: mean_d[i])

    # leave-one-out: remove surah X, recompute mean_d on the remaining 113
    # measure shift_X = sum_{j != X} |mean_d_full[j] - mean_d_minusX[j]|
    # Note: mean_d_minusX[j] = (sum_d[j] - D[j][X]) / (n - 2)
    sum_d = [sum(D[i]) for i in range(n)]
    shift = []
    for X in range(n):
        s = 0.0
        for j in range(n):
            if j == X:
                continue
            full = sum_d[j] / (n - 1)
            mnsX = (sum_d[j] - D[j][X]) / (n - 2)
            s += abs(full - mnsX)
        shift.append((X + 1, s))

    shift_sorted = sorted(shift, key=lambda x: -x[1])
    rank_q2_shift = next(i + 1 for i, (sid, _) in enumerate(shift_sorted) if sid == 2)

    # Total gravitational pull: Σ 1/D[X,j] (j != X). Lower distance = stronger pull.
    grav = []
    for X in range(n):
        s = 0.0
        for j in range(n):
            if j == X: continue
            d = D[X][j]
            if d > 1e-12:
                s += 1.0 / d
        grav.append((X + 1, s))
    grav_sorted = sorted(grav, key=lambda x: -x[1])
    rank_q2_grav = next(i + 1 for i, (sid, _) in enumerate(grav_sorted) if sid == 2)

    # Sum-of-distances mean (alt)
    mean_sorted = sorted(enumerate(mean_d), key=lambda x: x[1])
    rank_q2_meanlow = next(i + 1 for i, (idx, _) in enumerate(mean_sorted) if idx == 1)

    return {
        "test_id": "Q002-F-03",
        "medoid_surah": medoid_idx + 1,
        "Q2_mean_distance": mean_d[1],
        "Q2_shift_rank": rank_q2_shift,
        "Q2_shift_value": dict(shift)[2],
        "Q2_grav_pull_rank": rank_q2_grav,
        "Q2_grav_pull_value": dict(grav)[2],
        "Q2_mean_distance_rank_ascending": rank_q2_meanlow,
        "top10_by_shift": [(s, round(v, 5)) for s, v in shift_sorted[:10]],
        "top10_by_grav_pull": [(s, round(v, 5)) for s, v in grav_sorted[:10]],
        "top10_by_lowest_mean_distance": [(idx + 1, round(v, 5)) for idx, v in mean_sorted[:10]],
    }


# -------------------------- Q002-F-04 --------------------------------------

def Q002_F_04(quran_no_tashkeel, n_perms: int = 10000) -> dict:
    print(f"[Q002-F-04] Ring-structure on Q 2 with {n_perms} perms...")
    q2 = next(s for s in quran_no_tashkeel if s["id"] == 2)
    verse_words = [set(_verse_words(v["text"])) for v in q2["verses"]]
    n = len(verse_words)
    assert n == 286

    def cos(a: set[str], b: set[str]) -> float:
        if not a or not b:
            return 0.0
        return len(a & b) / math.sqrt(len(a) * len(b))

    def ring_score(order: list[int]) -> float:
        # i = 0..142 -> pair (order[i], order[n-1-i])
        # Only the first half (n//2 = 143 pairs); central (143, 144) is the last symmetric pair
        scores = []
        for i in range(n // 2):
            a, b = order[i], order[n - 1 - i]
            scores.append(cos(verse_words[a], verse_words[b]))
        return sum(scores) / len(scores)

    canonical_order = list(range(n))
    obs = ring_score(canonical_order)

    rng = random.Random(SEED)
    null_dist = []
    for _ in range(n_perms):
        perm = canonical_order[:]
        rng.shuffle(perm)
        null_dist.append(ring_score(perm))
    null_dist.sort()
    n_perms_actual = len(null_dist)
    n_geq = sum(1 for s in null_dist if s >= obs)
    p_one_sided = (n_geq + 1) / (n_perms_actual + 1)
    null_mean = sum(null_dist) / n_perms_actual
    null_sd = math.sqrt(sum((x - null_mean) ** 2 for x in null_dist) / (n_perms_actual - 1))
    z = (obs - null_mean) / null_sd if null_sd > 0 else 0.0

    # Block-pair test: 9 blocks per Farrin/Cuypers (approx, from §00-overview)
    # Blocks: A 1-39, B 40-103, C 104-141, D 142-176, E 177-242, F 243-260, G 261-283, H 284-286
    # Note we have 8 blocks, not 9 — Farrin's 9-block scheme places verse 143 as central pivot.
    # We use Farrin's nine-section division (best-known approximation):
    #   1: 1-39, 2: 40-46, 3: 47-103, 4: 104-141, 5: 142-152 (pivot block w/ v.143),
    #   6: 153-176, 7: 177-242, 8: 243-283, 9: 284-286
    farrin_blocks = [
        (1, 39), (40, 46), (47, 103), (104, 141), (142, 152),
        (153, 176), (177, 242), (243, 283), (284, 286)
    ]
    block_token_sets = []
    for (a, b) in farrin_blocks:
        toks = set()
        for v in q2["verses"]:
            if a <= v["id"] <= b:
                toks |= set(_verse_words(v["text"]))
        block_token_sets.append(toks)

    # ring pairs at block level: (1, 9), (2, 8), (3, 7), (4, 6); central=5
    block_pair_scores = []
    for i in range(4):
        block_pair_scores.append(cos(block_token_sets[i], block_token_sets[8 - i]))
    block_pair_score = sum(block_pair_scores) / 4

    # Block-level permutation null
    rng2 = random.Random(SEED + 1)
    null_block = []
    for _ in range(n_perms):
        perm = list(range(9))
        rng2.shuffle(perm)
        s = 0.0
        for i in range(4):
            s += cos(block_token_sets[perm[i]], block_token_sets[perm[8 - i]])
        null_block.append(s / 4)
    n_geq_b = sum(1 for s in null_block if s >= block_pair_score)
    p_block = (n_geq_b + 1) / (n_perms + 1)

    # MW-6 control: same test on Q 3 Āl ʿImrān (200 verses)
    q3 = next(s for s in quran_no_tashkeel if s["id"] == 3)
    q3_words = [set(_verse_words(v["text"])) for v in q3["verses"]]
    n3 = len(q3_words)
    canonical3 = list(range(n3))

    def ring_score_q3(order: list[int]) -> float:
        scores = []
        for i in range(n3 // 2):
            a, b = order[i], order[n3 - 1 - i]
            scores.append(cos(q3_words[a], q3_words[b]))
        return sum(scores) / len(scores)

    obs3 = ring_score_q3(canonical3)
    rng3 = random.Random(SEED + 2)
    null3 = []
    for _ in range(n_perms):
        perm = canonical3[:]
        rng3.shuffle(perm)
        null3.append(ring_score_q3(perm))
    n_geq3 = sum(1 for s in null3 if s >= obs3)
    p_q3 = (n_geq3 + 1) / (n_perms + 1)

    return {
        "test_id": "Q002-F-04",
        "n_perms": n_perms,
        "verse_pair_test": {
            "ring_score_canonical": obs,
            "null_mean": null_mean,
            "null_sd": null_sd,
            "z": z,
            "p_one_sided": p_one_sided,
            "n_perms_geq_obs": n_geq,
        },
        "block_pair_test (Farrin 9-block)": {
            "ring_score_canonical": block_pair_score,
            "block_pair_scores": block_pair_scores,
            "p_one_sided": p_block,
        },
        "Q3_control": {
            "ring_score_canonical": obs3,
            "p_one_sided": p_q3,
        },
    }


# -------------------------- Q002-F-05 --------------------------------------

def Q002_F_05(quran_no_tashkeel) -> dict:
    print("[Q002-F-05] Q 2:282 length extremity...")
    rows = []
    for s in quran_no_tashkeel:
        for v in s["verses"]:
            words = _verse_words(v["text"])
            text = _norm(v["text"])
            letters = sum(1 for c in text if c not in (" ",))
            rows.append((s["id"], v["id"], len(words), letters))

    word_counts = [r[2] for r in rows]
    letter_counts = [r[3] for r in rows]
    mu_w = sum(word_counts) / len(word_counts)
    sd_w = math.sqrt(sum((x - mu_w) ** 2 for x in word_counts) / (len(word_counts) - 1))
    mu_l = sum(letter_counts) / len(letter_counts)
    sd_l = math.sqrt(sum((x - mu_l) ** 2 for x in letter_counts) / (len(letter_counts) - 1))

    by_words = sorted(rows, key=lambda r: -r[2])
    by_letters = sorted(rows, key=lambda r: -r[3])

    rank_words = next(i + 1 for i, r in enumerate(by_words) if (r[0], r[1]) == (2, 282))
    rank_letters = next(i + 1 for i, r in enumerate(by_letters) if (r[0], r[1]) == (2, 282))

    target_w = next(r for r in rows if (r[0], r[1]) == (2, 282))
    z_w = (target_w[2] - mu_w) / sd_w
    z_l = (target_w[3] - mu_l) / sd_l

    # gap to second
    sorted_w_desc = sorted(word_counts, reverse=True)
    gap_w = (sorted_w_desc[0] - sorted_w_desc[1]) / sd_w
    sorted_l_desc = sorted(letter_counts, reverse=True)
    gap_l = (sorted_l_desc[0] - sorted_l_desc[1]) / sd_l

    return {
        "test_id": "Q002-F-05",
        "verse": "Q 2:282 (Āyat al-Dayn / debt-contract)",
        "n_verses": len(rows),
        "word_count": target_w[2],
        "letter_count": target_w[3],
        "corpus_mean_words": mu_w,
        "corpus_sd_words": sd_w,
        "corpus_mean_letters": mu_l,
        "corpus_sd_letters": sd_l,
        "z_words": z_w,
        "z_letters": z_l,
        "rank_by_words": rank_words,
        "rank_by_letters": rank_letters,
        "gap_to_second_words_sd": gap_w,
        "gap_to_second_letters_sd": gap_l,
        "top10_by_words": [{"surah": r[0], "verse": r[1], "words": r[2], "letters": r[3]}
                           for r in by_words[:10]],
        "top10_by_letters": [{"surah": r[0], "verse": r[1], "words": r[2], "letters": r[3]}
                             for r in by_letters[:10]],
    }


# -------------------------- main -------------------------------------------

def main():
    _verify_pre_regs()
    qnt = _load_quran("no-tashkeel")
    qmt = _load_quran("min-tashkeel")
    names = _load_99_names()
    print(f"[ok] loaded {sum(len(s['verses']) for s in qnt)} verses, {len(names)} divine names.")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    res = {}
    res["Q002-F-01"] = Q002_F_01(qnt, qmt, names)
    res["Q002-F-02"] = Q002_F_02(qnt, names)
    D = _load_dist_matrix()
    res["Q002-F-03"] = Q002_F_03(D)
    res["Q002-F-04"] = Q002_F_04(qnt, n_perms=10000)
    res["Q002-F-05"] = Q002_F_05(qnt)

    for tid, r in res.items():
        out = OUT_DIR / f"{tid}.json"
        out.write_text(json.dumps(r, ensure_ascii=False, indent=2))
        print(f"[ok] wrote {out}")

    # high-level summary print
    print("\n========== Q002 NOVEL FINDINGS — SUMMARY ==========")
    print(f"Q002-F-01  Āyat al-Kursī divine-name density:")
    print(f"  rank by total_density: {res['Q002-F-01']['rank_total_density']} / {res['Q002-F-01']['n_verses']}")
    print(f"  rank by distinct_density: {res['Q002-F-01']['rank_distinct_density']}")
    print(f"  total occ: {res['Q002-F-01']['occ']}, distinct: {res['Q002-F-01']['distinct_names_count']}")
    print(f"  names matched: {res['Q002-F-01']['distinct_names']}")
    print(f"Q002-F-02  Khawātim al-Baqara (Q 2:284-286):")
    print(f"  rank by total_density: {res['Q002-F-02']['rank_total_density']} / {res['Q002-F-02']['n_windows']}")
    print(f"  rank by distinct: {res['Q002-F-02']['rank_distinct_density']}")
    print(f"  Q 59:22-24 comparator rank_total: {res['Q002-F-02']['Q59_22_24_rank_total']}")
    print(f"Q002-F-03  Q 2 centrality:")
    print(f"  Q2 LOO-shift rank: {res['Q002-F-03']['Q2_shift_rank']} / 114")
    print(f"  Q2 grav-pull rank: {res['Q002-F-03']['Q2_grav_pull_rank']}")
    print(f"  Q2 mean-distance rank (ascending): {res['Q002-F-03']['Q2_mean_distance_rank_ascending']}")
    print(f"Q002-F-04  Ring-structure:")
    print(f"  verse-pair p={res['Q002-F-04']['verse_pair_test']['p_one_sided']:.4f}, z={res['Q002-F-04']['verse_pair_test']['z']:.2f}")
    print(f"  block-pair p={res['Q002-F-04']['block_pair_test (Farrin 9-block)']['p_one_sided']:.4f}")
    print(f"  Q3 control p={res['Q002-F-04']['Q3_control']['p_one_sided']:.4f}")
    print(f"Q002-F-05  Q 2:282 length:")
    print(f"  rank_by_words: {res['Q002-F-05']['rank_by_words']} / {res['Q002-F-05']['n_verses']}")
    print(f"  z_words: {res['Q002-F-05']['z_words']:.2f}")
    print(f"  gap_to_second (sd): {res['Q002-F-05']['gap_to_second_words_sd']:.2f}")


if __name__ == "__main__":
    main()
