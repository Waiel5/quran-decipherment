#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2010 — Exhaustive root-frequency exact-equality balance scan (candidate generator)
            + permutation null on semantic over-representation.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2010-root-frequency-balance-scan.md
SHA256 locked & verified at runtime (fail-fast on mismatch).

Rules-tuple: (no-tashkeel, QAC-root, total-attestations, basmala-as-QAC, Hafs-Kufan, Mashriqi).

Author: Waiel Al-Shujaa.  Bismillahi al-Rahmani al-Rahim.
"""
import json, csv, hashlib, sys, random
from collections import defaultdict
from itertools import combinations

ROOT = "/Users/grey/Downloads/quran/"
PREREG = ROOT + "findings/phase-b-hypotheses/prereg-h-new-2010-root-frequency-balance-scan.md"
PREREG_SHA = "c0d92b61a614af48cf14bbf455d86f39de9629facce6aef708be6887b9ce72b2"
ROOT_INDEX = ROOT + "data/morphology/root-index.json"
ROOT_STATS = ROOT + "data/morphology/root-stats.csv"
OUT = ROOT + "findings/phase-b-hypotheses/csv/h-new-2010.json"
SEED_PRIMARY = 20260509
SEED_REPLICATE = 20260530
N_PERM = 10000

# ---------------------------------------------------------------- SHA gate
def verify_sha():
    h = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH\n  expected {PREREG_SHA}\n  got      {h}\n"
                 "Refusing to run — pre-commit integrity violated (Protocol 1.2).")
    print(f"[ok] pre-reg SHA verified: {h}")

# ------------------------------------------------------- load + cross-validate
def load_counts():
    idx = json.load(open(ROOT_INDEX, encoding="utf-8"))
    freq = {r: len(v) for r, v in idx.items()}
    stats = {}
    with open(ROOT_STATS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            stats[row["root"]] = int(row["total_occurrences"])
    mism = [(r, freq[r], stats.get(r)) for r in freq if stats.get(r) != freq[r]]
    if mism:
        sys.exit(f"COUNT CROSS-VALIDATION FAILED: {mism[:10]}")
    print(f"[ok] {len(freq)} roots; root-index vs root-stats agree exactly (0 mismatches)")
    return freq

# ----------------------------------------------------- pre-registered gazetteer
# Tier-A antonym families (verbatim from paired-opposites.csv; both sides are members).
# Multi-root sides are tuples; every root in a family is a co-member.
ANTONYM_FAMILIES = {
    "heaven/earth":         ["smw", "ArD"],
    "life/death":           ["Hyy", "mwt"],
    "dunya/akhira":         ["dnw", "Axr"],
    "sun/moon":             ["$ms", "qmr"],
    "guidance/misguidance": ["hdy", "Dll"],
    "day/night":            ["ywm", "nhr", "lyl"],
    "secret/open":          ["srr", "Eln"],
    "east/west":            ["$rq", "grb"],
    "faith/disbelief":      ["Amn", "kfr"],
    "male/female":          ["*kr", "Anv"],
    "good/evil":            ["Hsn", "swA"],
    "truth/falsehood":      ["Hqq", "bTl"],
    "ease/difficulty":      ["ysr", "Esr"],
    "light/darkness":       ["nwr", "Zlm"],
    "wealthy/poor":         ["gny", "fqr"],
    "seen/unseen":          ["$hd", "gyb"],
    "remember/forget":      ["*kr", "nsy"],
    "first/last":           ["Awl", "Axr"],
    # heaven/hell DROPPED: hell-root (jhnm/nar) absent from root-index as a root; logged.
    "give/withhold":        ["Aty", "mnE", "bxl"],
    "near/far":             ["qrb", "bEd"],
    "pure/impure":          ["Thr", "njs", "rjs"],
    "obedience/disobed":    ["TwE", "ESy"],
    "grateful/ungrateful":  ["$kr", "kfr"],
    "mercy/wrath":          ["rHm", "gDb"],
    "reward/punishment":    ["Ajr", "E*b"],
    "speak/silent":         ["qwl", "Smt", "nSt"],
}
DROPPED_FAMILIES = {"heaven/hell": "hell-root jhnm/nar absent as a QAC root; root-level only"}

# Tier-BC co-thematic / synonym groups (locked).
COTHEMATIC_FAMILIES = {
    "know/sign":            ["Elm", "Ayy"],
    "path/deny":            ["sbl", "k*b"],
    "command/God-conscious":["Amr", "wqy"],
    "no-other-god":         ["gyr", "Alh"],
    "garden/god":           ["jnn", "Alh"],
    "guide/besides":        ["hdy", "dwn"],
    "give/follow":          ["Aty", "tbE"],
    "disbeliever/wrongdoer":["kfr", "Zlm"],
    "remember/night":       ["*kr", "lyl"],
    "religion/word":        ["dyn", "qwl"],
    "glorify/prostrate":    ["sbH", "sjd"],
}

GLOSS = {
    "smw":"heaven/sky","ArD":"earth/land","Hyy":"life/to live","mwt":"death/to die",
    "dnw":"this world (dunya)/nearness","Axr":"hereafter/last","$ms":"sun","qmr":"moon",
    "hdy":"guidance/to guide","Dll":"misguidance/to stray","ywm":"day","nhr":"daytime/river",
    "lyl":"night","srr":"secret/to conceal","Eln":"open/to declare","$rq":"east/sunrise",
    "grb":"west/sunset","Amn":"faith/to believe","kfr":"disbelief/ingratitude","*kr":"male/to remember/mention",
    "Anv":"female","Hsn":"good/beautiful","swA":"evil/bad","Hqq":"truth/right","bTl":"falsehood/vain",
    "ysr":"ease","Esr":"difficulty","nwr":"light","Zlm":"darkness/wrongdoing","gny":"wealthy/rich",
    "fqr":"poor/poverty","$hd":"witness/seen","gyb":"unseen/hidden","nsy":"to forget","Awl":"first/former",
    "Aty":"to give/bring","mnE":"to withhold","bxl":"to be stingy","qrb":"near/to approach",
    "bEd":"far/after","Thr":"pure/to purify","njs":"impure","rjs":"filth/abomination",
    "TwE":"obedience/to obey","ESy":"disobedience/to rebel","$kr":"gratitude/to thank","rHm":"mercy",
    "gDb":"wrath/anger","Ajr":"reward/wage","E*b":"punishment/torment","qwl":"to say/speech",
    "Smt":"to be silent","nSt":"to listen silently","Elm":"knowledge/to know","Ayy":"sign/verse",
    "sbl":"path/way","k*b":"to deny/call a lie","Amr":"command/matter","wqy":"God-consciousness/to guard",
    "gyr":"other (than)","Alh":"deity/god (Allah)","dwn":"besides/below","tbE":"to follow",
    "dyn":"religion/judgment","sbH":"to glorify (tasbih)","sjd":"to prostrate","$Tn":"Satan/devil",
    "qrA":"to recite/read (Quran)","jnn":"garden/paradise/jinn",
}

ARABIC = {
    "smw":"سمو","ArD":"ارض","Hyy":"حيي","mwt":"موت","dnw":"دنو","Axr":"اخر","$ms":"شمس","qmr":"قمر",
    "hdy":"هدي","Dll":"ضلل","ywm":"يوم","nhr":"نهر","lyl":"ليل","srr":"سرر","Eln":"علن","$rq":"شرق",
    "grb":"غرب","Amn":"امن","kfr":"كفر","*kr":"ذكر","Anv":"انث","Hsn":"حسن","swA":"سوا","Hqq":"حقق",
    "bTl":"بطل","ysr":"يسر","Esr":"عسر","nwr":"نور","Zlm":"ظلم","gny":"غني","fqr":"فقر","$hd":"شهد",
    "gyb":"غيب","nsy":"نسي","Awl":"اول","Aty":"اتي","mnE":"منع","bxl":"بخل","qrb":"قرب","bEd":"بعد",
    "Thr":"طهر","njs":"نجس","rjs":"رجس","TwE":"طوع","ESy":"عصي","$kr":"شكر","rHm":"رحم","gDb":"غضب",
    "Ajr":"اجر","E*b":"عذب","qwl":"قول","Smt":"صمت","nSt":"نصت","Elm":"علم","Ayy":"ايي","sbl":"سبل",
    "k*b":"كذب","Amr":"امر","wqy":"وقي","gyr":"غير","Alh":"اله","dwn":"دون","tbE":"تبع","dyn":"دين",
    "sbH":"سبح","sjd":"سجد","$Tn":"شطن","qrA":"قرا","jnn":"جنن",
}

def build_tagsets(freq):
    """root -> frozenset of family-names it belongs to (only roots present in index)."""
    tags = defaultdict(set)
    for fam, roots in {**ANTONYM_FAMILIES, **COTHEMATIC_FAMILIES}.items():
        present = [r for r in roots if r in freq]
        missing = [r for r in roots if r not in freq]
        if missing:
            print(f"[warn] family {fam}: missing roots {missing} (excluded as co-members)")
        for r in present:
            tags[r].add(fam)
    return {r: frozenset(s) for r, s in tags.items()}

def pair_is_meaningful(rx, ry, tagsets):
    """True if some family contains BOTH rx and ry."""
    a = tagsets.get(rx); b = tagsets.get(ry)
    if not a or not b:
        return False, []
    common = a & b
    return (len(common) > 0), sorted(common)

# ---------------------------------------------------------------- exhaustive scan
def exhaustive_scan(freq):
    inv = defaultdict(list)
    for r, c in freq.items():
        inv[c].append(r)
    inv = {c: sorted(rs) for c, rs in inv.items()}
    buckets = {c: rs for c, rs in inv.items() if len(rs) >= 2}
    total_pairs = sum(len(rs)*(len(rs)-1)//2 for rs in buckets.values())
    return inv, buckets, total_pairs

# ---------------------------------------------------------------- observed M
def count_meaningful(freq, tagsets, restrict=None):
    """
    Count exact-balance pairs that are meaningful.
    restrict: None -> all families; 'antonym' -> Tier-A only; 'cothematic' -> Tier-BC only.
    Returns (M, list_of_meaningful_pair_dicts).
    """
    if restrict == "antonym":
        allowed = set(ANTONYM_FAMILIES)
    elif restrict == "cothematic":
        allowed = set(COTHEMATIC_FAMILIES)
    else:
        allowed = set(ANTONYM_FAMILIES) | set(COTHEMATIC_FAMILIES)
    inv, buckets, _ = exhaustive_scan(freq)
    M = 0
    found = []
    for c, rs in buckets.items():
        labelled = [r for r in rs if r in tagsets]
        for rx, ry in combinations(labelled, 2):
            common = (tagsets[rx] & tagsets[ry]) & allowed
            if common:
                M += 1
                found.append({"count": c, "root_a": rx, "root_b": ry,
                              "families": sorted(common)})
    return M, found

# ---------------------------------------------------------------- permutation null
def perm_null(freq, tagsets, seed, n_perm, restrict=None):
    """
    Shuffle the assignment of tag-sets to roots, holding the frequency distribution
    and the multiset of tag-sets constant. Recount meaningful same-count pairs.
    """
    if restrict == "antonym":
        allowed = set(ANTONYM_FAMILIES)
    elif restrict == "cothematic":
        allowed = set(COTHEMATIC_FAMILIES)
    else:
        allowed = set(ANTONYM_FAMILIES) | set(COTHEMATIC_FAMILIES)

    inv, buckets, _ = exhaustive_scan(freq)
    # tag-set multiset (only for labelled roots)
    labelled_roots = sorted(tagsets.keys())
    tagset_list = [tagsets[r] for r in labelled_roots]
    all_roots = sorted(freq.keys())

    rng = random.Random(seed)
    M_null = []
    for _ in range(n_perm):
        # choose which roots receive the (fixed multiset of) tag-sets
        recipients = rng.sample(all_roots, len(tagset_list))
        shuffled_sets = tagset_list[:]
        rng.shuffle(shuffled_sets)
        perm_tags = {rt: shuffled_sets[i] for i, rt in enumerate(recipients)}
        m = 0
        for c, rs in buckets.items():
            lab = [r for r in rs if r in perm_tags]
            for rx, ry in combinations(lab, 2):
                if (perm_tags[rx] & perm_tags[ry]) & allowed:
                    m += 1
        M_null.append(m)
    return M_null

def pval(M_obs, M_null):
    ge = sum(1 for m in M_null if m >= M_obs)
    return (ge + 1) / (len(M_null) + 1)

# ---------------------------------------------------------------- decoy control (MW-6)
def decoy_tagsets(freq, tagsets, seed):
    """Same group SIZES, but members are arbitrary roots (semantically meaningless)."""
    rng = random.Random(seed)
    fams = {**ANTONYM_FAMILIES, **COTHEMATIC_FAMILIES}
    present_roots = sorted(freq.keys())
    decoy = defaultdict(set)
    for fam, roots in fams.items():
        k = len([r for r in roots if r in freq])
        picks = rng.sample(present_roots, k)
        for r in picks:
            decoy[r].add(fam)
    return {r: frozenset(s) for r, s in decoy.items()}

# ---------------------------------------------------------------- semantic surprise ranking
TIER_RANK = {"A": 0, "B": 1, "C": 2}
def tier_of(families):
    """A if any antonym family; else C (cothematic). (Tier-B synonyms folded into C here.)"""
    if any(f in ANTONYM_FAMILIES for f in families):
        return "A"
    return "C"

def main():
    verify_sha()
    freq = load_counts()
    tagsets = build_tagsets(freq)
    print(f"[info] {len(tagsets)} roots carry a semantic-group tag")

    inv, buckets, total_pairs = exhaustive_scan(freq)
    print(f"[info] exhaustive scan: {len(inv)} distinct counts; "
          f"{len(buckets)} shared-count buckets; {total_pairs} exact-balance pairs total")

    # observed M (full + variants)
    M_full, found_full = count_meaningful(freq, tagsets, None)
    M_anto, found_anto = count_meaningful(freq, tagsets, "antonym")
    M_cot,  found_cot  = count_meaningful(freq, tagsets, "cothematic")
    print(f"[obs] meaningful same-count pairs: full={M_full}  antonym-only={M_anto}  cothematic-only={M_cot}")

    # null distributions
    print("[run] permutation null (full gazetteer, primary seed)...")
    null_full = perm_null(freq, tagsets, SEED_PRIMARY, N_PERM, None)
    null_anto = perm_null(freq, tagsets, SEED_PRIMARY, N_PERM, "antonym")
    null_cot  = perm_null(freq, tagsets, SEED_PRIMARY, N_PERM, "cothematic")
    print("[run] replication null (full gazetteer, replicate seed)...")
    null_full_rep = perm_null(freq, tagsets, SEED_REPLICATE, N_PERM, None)

    # decoy control
    print("[run] decoy-gazetteer control...")
    dtags = decoy_tagsets(freq, tagsets, SEED_PRIMARY)
    M_decoy = _decoy_M(freq, dtags)
    null_decoy = _decoy_null(freq, dtags, SEED_PRIMARY, N_PERM)

    def summ(name, M, null):
        import statistics as st
        return {"name": name, "M_obs": M, "n_perm": len(null),
                "null_mean": round(st.mean(null), 4),
                "null_median": st.median(null),
                "null_max": max(null), "null_min": min(null),
                "p_one_tailed_ge": pval(M, null),
                "exceeds_median": M > st.median(null)}

    results = {
        "full":        summ("full-gazetteer", M_full, null_full),
        "antonym":     summ("antonym-only", M_anto, null_anto),
        "cothematic":  summ("cothematic-only", M_cot, null_cot),
        "full_replicate": summ(f"full-gazetteer-seed-{SEED_REPLICATE}", M_full, null_full_rep),
        "decoy_control":  summ("decoy-gazetteer (MW-6)", M_decoy, null_decoy),
    }

    # ----- ranked top-30 (descriptive generator output)
    # rank: tier(A<C), then smaller bucket, then higher count
    def bucket_size(c): return len(inv[c])
    enriched = []
    for p in found_full:
        t = tier_of(p["families"])
        enriched.append({
            "count": p["count"],
            "bucket_size": bucket_size(p["count"]),
            "root_a": p["root_a"], "arabic_a": ARABIC.get(p["root_a"], ""), "gloss_a": GLOSS.get(p["root_a"], ""),
            "root_b": p["root_b"], "arabic_b": ARABIC.get(p["root_b"], ""), "gloss_b": GLOSS.get(p["root_b"], ""),
            "families": p["families"],
            "tier": t,
        })
    enriched.sort(key=lambda d: (TIER_RANK[d["tier"]], d["bucket_size"], -d["count"]))
    top30 = enriched[:30]

    # ----- also: descriptive list of high-count shared buckets (the generator face)
    high_buckets = []
    for c in sorted(buckets, reverse=True):
        if c >= 50:
            high_buckets.append({"count": c, "n_roots": len(buckets[c]),
                                 "roots": [{"r": r, "ar": ARABIC.get(r, ""), "gloss": GLOSS.get(r, "")}
                                           for r in buckets[c]]})

    out = {
        "id": "H-NEW-2010",
        "title": "Exhaustive root-frequency exact-equality balance scan + semantic over-representation null",
        "prereg_sha256": PREREG_SHA,
        "rules_tuple": "(no-tashkeel, QAC-root, total-attestations, basmala-as-QAC, Hafs-Kufan, Mashriqi)",
        "seed_primary": SEED_PRIMARY, "seed_replicate": SEED_REPLICATE, "n_perm": N_PERM,
        "n_roots": len(freq),
        "scan": {
            "n_distinct_counts": len(inv),
            "n_shared_buckets": len(buckets),
            "total_exact_balance_pairs": total_pairs,
            "n_roots_unique_count": sum(1 for rs in inv.values() if len(rs) == 1),
            "bucket_size_distribution": {str(k): v for k, v in
                sorted(__import__("collections").Counter(len(rs) for rs in inv.values()).items())},
        },
        "dropped_families": DROPPED_FAMILIES,
        "n_tagged_roots": len(tagsets),
        "T1_test": results,
        "all_meaningful_pairs_full": found_full,
        "ranked_top30_most_surprising": top30,
        "high_count_shared_buckets_ge50": high_buckets,
        "antonym_families_exact_balance_status": _antonym_status(freq),
    }
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"[ok] wrote {OUT}")

    # console verdict
    r = results["full"]
    print("\n========== T1 VERDICT (full gazetteer) ==========")
    print(f"  M_obs = {r['M_obs']}   null mean={r['null_mean']} median={r['null_median']} max={r['null_max']}")
    print(f"  p(one-tailed, >=) = {r['p_one_tailed_ge']}")
    print(f"  exceeds null median: {r['exceeds_median']}")
    if r["M_obs"] < results["full"]["null_median"]:
        print("  --> PRE-COMMIT VIOLATION DIRECTION (under-represented). Publish NULL w/ reversal flag.")
    elif r["p_one_tailed_ge"] < 0.05:
        print("  --> T1 PASS-DIRECTED (meaningful balances over-represented; modest).")
    else:
        print("  --> T1 NULL (no over-representation beyond chance).")
    print("=================================================")
    print("\nTop-5 most-surprising exact balances:")
    for d in top30[:5]:
        print(f"  count={d['count']:4d} bucket={d['bucket_size']}  "
              f"{d['root_a']}({d['gloss_a']}) = {d['root_b']}({d['gloss_b']})  "
              f"[tier {d['tier']}; {d['families']}]")

# helper machinery for decoy (kept separate for clarity)
def _decoy_M(freq, dtags):
    inv, buckets, _ = exhaustive_scan(freq)
    allowed = set(ANTONYM_FAMILIES) | set(COTHEMATIC_FAMILIES)
    M = 0
    for c, rs in buckets.items():
        lab = [r for r in rs if r in dtags]
        for rx, ry in combinations(lab, 2):
            if (dtags[rx] & dtags[ry]) & allowed:
                M += 1
    return M

def _decoy_null(freq, dtags, seed, n_perm):
    inv, buckets, _ = exhaustive_scan(freq)
    allowed = set(ANTONYM_FAMILIES) | set(COTHEMATIC_FAMILIES)
    labelled = sorted(dtags.keys())
    tagset_list = [dtags[r] for r in labelled]
    all_roots = sorted(freq.keys())
    rng = random.Random(seed + 7)
    out = []
    for _ in range(n_perm):
        recipients = rng.sample(all_roots, len(tagset_list))
        sl = tagset_list[:]; rng.shuffle(sl)
        pt = {rt: sl[i] for i, rt in enumerate(recipients)}
        m = 0
        for c, rs in buckets.items():
            lab = [r for r in rs if r in pt]
            for rx, ry in combinations(lab, 2):
                if (pt[rx] & pt[ry]) & allowed:
                    m += 1
        out.append(m)
    return out

def _antonym_status(freq):
    """For each antonym family, report whether its two sides have EXACTLY equal root counts."""
    status = {}
    for fam, roots in ANTONYM_FAMILIES.items():
        present = [(r, freq[r]) for r in roots if r in freq]
        counts = {r: c for r, c in present}
        # for multi-root sides we just report all member counts; "exact balance" =
        # any two members share a count
        cs = list(counts.values())
        exact = len(cs) != len(set(cs))
        status[fam] = {"members": counts, "any_exact_equal_within_family": exact}
    return status

if __name__ == "__main__":
    main()
