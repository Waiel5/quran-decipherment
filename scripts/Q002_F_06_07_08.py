#!/usr/bin/env python3
"""
Q002_F_06_07_08.py — three NEW pre-registered close-read tests for Q 2 al-Baqara.

  F-06  Āyat al-Kursī (Q 2:255) ROOT-LEVEL local distinctiveness
  F-07  Qibla-change pericope (Q 2:131-144 ring replication + lexical-center test)
  F-08  Longest-verse monopoly/plurality of al-Baqara

SHA256-locks each pre-reg (PRE-REG-STANDARD-04), fails fast on mismatch.
Stdlib only. Seed 20260509, 10000 perms.
"""
from __future__ import annotations
import hashlib, json, math, random, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_DIR = ROOT / "surahs" / "Q002-al-baqara"
OUT_DIR = PREREG_DIR / "csv"
SEED = 20260509
N_PERMS = 10000

PREREG_SHAS = {
    "Q002-F-06": ("Q002-F-06-ayat-al-kursi-root-locality-prereg.md",
                  "7044eb7477d3af67a1ffde2d652f05441052a7d469a98725726aadf6d5760409"),
    "Q002-F-07": ("Q002-F-07-qibla-pivot-lexical-center-prereg.md",
                  "be6f15fdf1842fb079c7fa96b9ebf9273390ec00fedb6cc812e9a9d443d8e661"),
    "Q002-F-08": ("Q002-F-08-longest-verse-monopoly-prereg.md",
                  "595773500202c587c8732a118aec2782cfc5704178f77602143d3980ae03ea83"),
}

SAJDA_RE = re.compile(r"[ۖ-ۭۚۛۜ]")
WS_RE = re.compile(r"\s+")


def verify_pre_regs():
    for tid, (fname, sha_expected) in PREREG_SHAS.items():
        p = PREREG_DIR / fname
        if not p.exists():
            print(f"FAIL: pre-reg missing for {tid}: {p}", file=sys.stderr); sys.exit(2)
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        if sha != sha_expected:
            print(f"FAIL: SHA mismatch {tid}: got {sha}", file=sys.stderr); sys.exit(2)
    print("[ok] pre-reg SHA256 checks passed for F-06, F-07, F-08.")


def norm(t): return WS_RE.sub(" ", SAJDA_RE.sub(" ", t)).strip()
def words(t): return [w for w in norm(t).split() if w]


def load_quran(variant="no-tashkeel"):
    return json.loads((ROOT / "quran-text" / f"quran-{variant}.json").read_text())


def load_root_index():
    """root -> list of [surah, verse, word]."""
    return json.loads((ROOT / "data" / "morphology" / "root-index.json").read_text())


def per_verse_root_sets(root_index):
    """ (surah,verse) -> set of roots ; and (surah,verse) -> root-token count (multiplicity)."""
    rsets = defaultdict(set)
    rmass = defaultdict(int)
    for root, locs in root_index.items():
        for (s, v, w) in locs:
            rsets[(s, v)].add(root)
            rmass[(s, v)] += 1
    return rsets, rmass


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    u = len(a | b)
    return (len(a & b) / u) if u else 0.0


# ----------------------------- F-06 ----------------------------------------

def F06(quran, rsets):
    print("[Q002-F-06] root-level local distinctiveness of Q 2:255 ...")
    K = 3  # locked window radius

    def surah_verses(sid):
        s = next(x for x in quran if x["id"] == sid)
        return [v["id"] for v in s["verses"]]

    def local_distinct(sid, verse_ids, idx):
        """mean (1 - Jaccard) of verse at position idx to its in-surah +-K neighbours."""
        v = verse_ids[idx]
        rv = rsets.get((sid, v), set())
        ds = []
        for off in list(range(-K, 0)) + list(range(1, K + 1)):
            j = idx + off
            if 0 <= j < len(verse_ids):
                ds.append(1.0 - jaccard(rv, rsets.get((sid, verse_ids[j]), set())))
        return sum(ds) / len(ds) if ds else 0.0

    # ---- H1: in-surah rank within Q 2 (286 verses) ----
    vids2 = surah_verses(2)
    scores2 = [(vids2[i], local_distinct(2, vids2, i)) for i in range(len(vids2))]
    scores2_sorted = sorted(scores2, key=lambda x: -x[1])
    rank_in_surah = next(i + 1 for i, (vid, _) in enumerate(scores2_sorted) if vid == 255)
    val_255 = dict(scores2)[255]

    # ---- alternative radii (MW-3) ----
    def local_distinct_k(sid, verse_ids, idx, k):
        v = verse_ids[idx]; rv = rsets.get((sid, v), set()); ds = []
        for off in list(range(-k, 0)) + list(range(1, k + 1)):
            j = idx + off
            if 0 <= j < len(verse_ids):
                ds.append(1.0 - jaccard(rv, rsets.get((sid, verse_ids[j]), set())))
        return sum(ds) / len(ds) if ds else 0.0

    alt_ranks = {}
    for k in (2, 5):
        sc = [(vids2[i], local_distinct_k(2, vids2, i, k)) for i in range(len(vids2))]
        sc_sorted = sorted(sc, key=lambda x: -x[1])
        alt_ranks[f"k={k}"] = next(i + 1 for i, (vid, _) in enumerate(sc_sorted) if vid == 255)

    # ---- H2: corpus-wide rank (each verse vs its own in-surah +-3) ----
    corpus_scores = []
    for s in quran:
        sid = s["id"]
        vids = [v["id"] for v in s["verses"]]
        for i in range(len(vids)):
            corpus_scores.append(((sid, vids[i]), local_distinct(sid, vids, i)))
    corpus_sorted = sorted(corpus_scores, key=lambda x: -x[1])
    rank_corpus = next(i + 1 for i, (key, _) in enumerate(corpus_sorted) if key == (2, 255))
    n_corpus = len(corpus_scores)

    # ---- MW-2: 10000-perm in-surah shuffle null ----
    rng = random.Random(SEED)
    pos255 = vids2.index(255)
    rv255 = rsets.get((2, 255), set())
    null_vals = []
    base_ids = vids2[:]
    for _ in range(N_PERMS):
        perm = base_ids[:]
        rng.shuffle(perm)
        # 255 stays at its canonical position pos255; neighbours come from shuffled order
        ds = []
        for off in list(range(-K, 0)) + list(range(1, K + 1)):
            j = pos255 + off
            if 0 <= j < len(perm):
                ds.append(1.0 - jaccard(rv255, rsets.get((2, perm[j]), set())))
        null_vals.append(sum(ds) / len(ds) if ds else 0.0)
    n_geq = sum(1 for x in null_vals if x >= val_255)
    p_perm = (n_geq + 1) / (N_PERMS + 1)
    null_mean = sum(null_vals) / len(null_vals)
    null_sd = math.sqrt(sum((x - null_mean) ** 2 for x in null_vals) / (len(null_vals) - 1))
    z = (val_255 - null_mean) / null_sd if null_sd else 0.0

    top10_in_surah = [{"verse": vid, "local_distinct": round(val, 5)}
                      for vid, val in scores2_sorted[:10]]

    h1 = "VINDICATED" if rank_in_surah <= 15 else "NULL"
    h2 = "VINDICATED" if rank_corpus <= 624 else "NULL"

    return {
        "test_id": "Q002-F-06", "seed": SEED, "window_radius_k": K, "n_perms": N_PERMS,
        "Q2_255_root_count": len(rv255),
        "Q2_255_local_distinct_k3": round(val_255, 5),
        "rank_in_surah_286": rank_in_surah, "H1_threshold_top15": 15, "H1_verdict": h1,
        "rank_corpus_6236": rank_corpus, "n_corpus": n_corpus,
        "H2_threshold_top624": 624, "H2_verdict": h2,
        "perm_null_mean": round(null_mean, 5), "perm_null_sd": round(null_sd, 5),
        "perm_z": round(z, 3), "perm_p_one_sided": round(p_perm, 5),
        "alt_radius_in_surah_ranks": alt_ranks,
        "top10_most_locally_distinct_verses_Q2": top10_in_surah,
    }


# ----------------------------- F-07 ----------------------------------------

def ring_score(rset_list):
    n = len(rset_list)
    half = n // 2
    if half == 0:
        return 0.0
    tot = sum(jaccard(rset_list[i], rset_list[n - 1 - i]) for i in range(half))
    return tot / half


def F07(quran, rsets, rmass):
    print("[Q002-F-07] qibla pericope ring replication + lexical center ...")
    q2 = next(s for s in quran if s["id"] == 2)
    vids = [v["id"] for v in q2["verses"]]

    # ---- H1: ring replication of Q 2:131-144 (14 verses) ----
    win = list(range(131, 145))  # 131..144 inclusive
    rset_win = [rsets.get((2, v), set()) for v in win]
    obs = ring_score(rset_win)
    rng = random.Random(SEED)
    null = []
    for _ in range(N_PERMS):
        perm = rset_win[:]
        rng.shuffle(perm)
        null.append(ring_score(perm))
    n_geq = sum(1 for x in null if x >= obs)
    p_ring = (n_geq + 1) / (N_PERMS + 1)
    nm = sum(null) / len(null)
    nsd = math.sqrt(sum((x - nm) ** 2 for x in null) / (len(null) - 1))
    z_ring = (obs - nm) / nsd if nsd else 0.0

    # ---- MW-6 control: arbitrary non-pericope 14-verse window 100-113 ----
    cwin = list(range(100, 114))
    rset_c = [rsets.get((2, v), set()) for v in cwin]
    obs_c = ring_score(rset_c)
    rng2 = random.Random(SEED + 1)
    null_c = []
    for _ in range(N_PERMS):
        perm = rset_c[:]; rng2.shuffle(perm); null_c.append(ring_score(perm))
    p_c = (sum(1 for x in null_c if x >= obs_c) + 1) / (N_PERMS + 1)

    # ---- H2: lexical-center (word-mass and root-mass cumulative midpoints) ----
    word_counts = [len(words(v["text"])) for v in q2["verses"]]
    total_w = sum(word_counts)
    cum = 0; word_mid_verse = None
    for v, wc in zip(vids, word_counts):
        cum += wc
        if cum >= total_w / 2:
            word_mid_verse = v; break

    root_counts = [rmass.get((2, v), 0) for v in vids]
    total_r = sum(root_counts)
    cum = 0; root_mid_verse = None
    for v, rc in zip(vids, root_counts):
        cum += rc
        if cum >= total_r / 2:
            root_mid_verse = v; break

    # verse-count midpoint (the naive "143 is the middle verse" reckoning)
    verse_mid = vids[len(vids) // 2]  # 286/2 -> index 143 -> verse 144

    def classify(v):
        if 142 <= v <= 152:
            return "VINDICATED"
        if 131 <= v <= 160:
            return "DIRECTIONAL"
        return "NULL"

    return {
        "test_id": "Q002-F-07", "seed": SEED, "n_perms": N_PERMS,
        "H1_ring_window": "Q2:131-144",
        "ring_score_canonical": round(obs, 5),
        "ring_null_mean": round(nm, 5), "ring_null_sd": round(nsd, 5),
        "ring_z": round(z_ring, 3), "ring_p_one_sided": round(p_ring, 6),
        "H1_verdict": "VINDICATED" if p_ring < 0.05 else "NULL",
        "MW6_control_window": "Q2:100-113",
        "control_ring_score": round(obs_c, 5), "control_p_one_sided": round(p_c, 5),
        "total_words": total_w, "word_mass_midpoint_verse": word_mid_verse,
        "total_root_tokens": total_r, "root_mass_midpoint_verse": root_mid_verse,
        "verse_count_midpoint_verse": verse_mid,
        "H2_word_mid_verdict": classify(word_mid_verse),
        "H2_root_mid_verdict": classify(root_mid_verse),
    }


# ----------------------------- F-08 ----------------------------------------

def F08(quran):
    print("[Q002-F-08] longest-verse monopoly/plurality ...")
    rows = []
    for s in quran:
        for v in s["verses"]:
            t = norm(v["text"])
            wc = len([w for w in t.split() if w])
            lc = sum(1 for c in t if c != " ")
            rows.append({"surah": s["id"], "verse": v["id"], "words": wc, "letters": lc})

    def topN_count(metric, N):
        srt = sorted(rows, key=lambda r: (-r[metric],
                                          -(r["letters"] if metric == "words" else r["words"]),
                                          r["surah"], r["verse"]))
        top = srt[:N]
        cnt = defaultdict(int)
        for r in top:
            cnt[r["surah"]] += 1
        return top, dict(cnt)

    out = {"test_id": "Q002-F-08", "seed": SEED}
    for metric in ("words", "letters"):
        for N in (10, 15, 20):
            top, cnt = topN_count(metric, N)
            multi = {s: c for s, c in cnt.items() if c >= 2}
            q2c = cnt.get(2, 0)
            others_ge2 = {s: c for s, c in multi.items() if s != 2}
            argmax = max(cnt.items(), key=lambda kv: (kv[1], -kv[0]))
            out[f"{metric}_top{N}"] = {
                "top_verses": [{"surah": r["surah"], "verse": r["verse"],
                                "words": r["words"], "letters": r["letters"]} for r in top],
                "per_surah_count": cnt,
                "surahs_with_2plus": multi,
                "Q2_count": q2c,
                "other_surahs_with_2plus": others_ge2,
                "argmax_surah": argmax[0], "argmax_count": argmax[1],
                "Q2_is_unique_holder_of_2plus": (q2c >= 2 and len(others_ge2) == 0),
                "Q2_is_strict_plurality": (argmax[0] == 2 and
                                           list(cnt.values()).count(argmax[1]) == 1),
            }
    # Primary verdicts (word count, N=10)
    p = out["words_top10"]
    out["H1_monopoly_verdict"] = "VINDICATED" if p["Q2_is_unique_holder_of_2plus"] else "NULL"
    out["H2_plurality_verdict"] = "VINDICATED" if p["Q2_is_strict_plurality"] else "NULL"
    # MW-7 refinement: is Q2 the unique holder of 3+?
    cnt10 = p["per_surah_count"]
    holders_3plus = {s: c for s, c in cnt10.items() if c >= 3}
    out["MW7_unique_holder_of_3plus"] = (cnt10.get(2, 0) >= 3 and
                                         all(s == 2 for s in holders_3plus))
    out["MW7_holders_3plus"] = holders_3plus
    return out


def main():
    verify_pre_regs()
    quran = load_quran("no-tashkeel")
    ri = load_root_index()
    rsets, rmass = per_verse_root_sets(ri)
    print(f"[ok] {sum(len(s['verses']) for s in quran)} verses; "
          f"{len(ri)} roots; {len(rsets)} verses with root data.")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    res = {
        "Q002-F-06": F06(quran, rsets),
        "Q002-F-07": F07(quran, rsets, rmass),
        "Q002-F-08": F08(quran),
    }
    for tid, r in res.items():
        (OUT_DIR / f"{tid}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2))
        print(f"[ok] wrote {OUT_DIR / (tid + '.json')}")

    print("\n========== Q002 F-06/07/08 SUMMARY ==========")
    f6 = res["Q002-F-06"]
    print(f"F-06  Q2:255 in-surah rank {f6['rank_in_surah_286']}/286 [{f6['H1_verdict']}]; "
          f"corpus rank {f6['rank_corpus_6236']}/{f6['n_corpus']} [{f6['H2_verdict']}]; "
          f"perm z={f6['perm_z']} p={f6['perm_p_one_sided']}")
    f7 = res["Q002-F-07"]
    print(f"F-07  ring 131-144 score={f7['ring_score_canonical']} z={f7['ring_z']} "
          f"p={f7['ring_p_one_sided']} [{f7['H1_verdict']}]; control p={f7['control_p_one_sided']}; "
          f"word-mid v{f7['word_mass_midpoint_verse']} [{f7['H2_word_mid_verdict']}] "
          f"root-mid v{f7['root_mass_midpoint_verse']} [{f7['H2_root_mid_verdict']}] "
          f"verse-mid v{f7['verse_count_midpoint_verse']}")
    f8 = res["Q002-F-08"]
    p = f8["words_top10"]
    print(f"F-08  top10-by-words per-surah: {p['per_surah_count']}")
    print(f"      Q2 count={p['Q2_count']} unique-2+? {p['Q2_is_unique_holder_of_2plus']} "
          f"[H1 {f8['H1_monopoly_verdict']}]; plurality? {p['Q2_is_strict_plurality']} "
          f"[H2 {f8['H2_plurality_verdict']}]; MW7 unique-3+? {f8['MW7_unique_holder_of_3plus']}")


if __name__ == "__main__":
    main()
