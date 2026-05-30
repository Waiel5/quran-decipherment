#!/usr/bin/env python3
"""
H-NEW-2440 — Favor->Command lexical-recall census + within-surah shuffle null.

Does a divine-favor root (appearing in a past-tense divine-action / taʿdid al-niʿam
verse) re-surface in a LATER command/prohibition verse within the same surah more than
a within-surah verse-order shuffle would produce? Seed = al-Duha ytm (93: v6->v9).

Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2440-favor-command-recall.md
Direction LOCKED before computation: observed recall-events > null (one-sided upper).
Seed 20260509, 10000 perms. Rules-tuple: (no-tashkeel, QAC-root+POS/aspect/mood,
segment-level, basmala-not-counted, Hafs-Kufan, Mashriqi).

Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os, statistics
from collections import defaultdict, Counter

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2440-favor-command-recall.md")
EXPECTED_SHA = "f4595836546c879f4c9c74628e0bbf4e2776b67c34a3745710978f6219421015"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2440.json")
SEED = 20260509
SEED_REPL = 20260601
NPERM = 10000
W_PRIMARY = 8
W_VARIANTS = [4, 9999]  # tight pericope + whole-surah (MW-3)

# --- runtime pre-reg integrity check ---
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

# ============================================================
# LOCKED lexicons (byte-identical to pre-reg §2.2 / §2.4)
# ============================================================
FAVOR_LEXICON = {
    "wjd", "Aty", "nEm", "hdy", "jEl", "xlq", "rzq", "nzl", "swy", "Elm",
    "Erf", "fDl", "whb", "njw", "njy", "fkk", "$rH", "rfE", "Hml", "wDE",
    "xff", "Awy", "gny", "ktb", "byn", "sbg", "msk", "Hyy",
}
DIVINE_PERSON = {"1S", "1P", "3MS", "3MP"}
CMD_2P = {"2MS", "2MP", "2FS", "2FP", "2MD", "2D"}
STOPROOTS = {"kwn", "qwl"}  # copula + "to say": trivial co-occurrence
CONTENT_POS = {"N", "PN", "ADJ", "V"}

# ============================================================
# parse QAC
# ============================================================
loc_re = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
def feat(feats, key):
    m = re.search(key + r":([^|]+)", feats)
    return m.group(1) if m else ""

# rows: (s,v,w,seg, form, feats)
rows = []
for line in open(MORPH, encoding="utf-8"):
    if not line.startswith("("):
        continue
    p = line.rstrip("\n").split("\t")
    if len(p) < 4:
        continue
    m = loc_re.match(p[0])
    if not m:
        continue
    s, v, w, seg = map(int, m.groups())
    rows.append((s, v, w, seg, p[1], p[3]))

# segments grouped by verse, kept in (word,seg) order
verse_segs = defaultdict(list)
for r in rows:
    verse_segs[(r[0], r[1])].append(r)
for k in verse_segs:
    verse_segs[k].sort(key=lambda x: (x[2], x[3]))

# ============================================================
# per-verse annotation: favor flag, command flag, content-root set,
# and the specific favor-verb roots / command-verb roots present
# ============================================================
verse_info = {}   # (s,v) -> dict
for (s, v), segs in verse_segs.items():
    is_favor = False
    favor_verb_roots = set()
    is_cmd = False
    cmd_verb_roots = set()
    content_roots = set()
    for i, (s_, v_, w_, seg_, form, feats) in enumerate(segs):
        if "STEM" not in feats:
            continue
        pos = feat(feats, "POS")
        rt = feat(feats, "ROOT")
        if rt and pos in CONTENT_POS and rt not in STOPROOTS:
            content_roots.add(rt)
        if pos == "V":
            toks = feats.split("|")
            # favor: PERF, not PASS, divine person, root in lexicon
            if ("PERF" in toks and "PASS" not in toks
                    and any(t in DIVINE_PERSON for t in toks)
                    and rt in FAVOR_LEXICON):
                is_favor = True
                favor_verb_roots.add(rt)
            # command A: imperative
            if "IMPV" in toks:
                is_cmd = True
                if rt:
                    cmd_verb_roots.add(rt)
            # command B: la-nahy + IMPF JUS 2p
            if "IMPF" in toks and "MOOD:JUS" in toks and any(t in CMD_2P for t in toks):
                back = segs[max(0, i - 2):i]
                if any(feat(b[5], "POS") == "PRO" for b in back):
                    is_cmd = True
                    if rt:
                        cmd_verb_roots.add(rt)
    verse_info[(s, v)] = {
        "favor": is_favor,
        "cmd": is_cmd,
        "favor_roots": favor_verb_roots,
        "cmd_roots": cmd_verb_roots,
        "content": content_roots,
    }

# per-surah ordered verse list
quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
name = {s["id"]: s["transliteration"] for s in quran}
surah_verses = defaultdict(list)
for (s, v) in verse_info:
    surah_verses[s].append(v)
for s in surah_verses:
    surah_verses[s].sort()

# ============================================================
# recall counter (deterministic, on a given verse-ORDER list)
# `order` is a list aligned with content-bearing verse-records;
# returns: recall_events count, and the explicit pair roster.
# ============================================================
def count_recalls(records, W, want_roster=False, reverse=False):
    """
    records: list of dicts in positional order, each {favor,cmd,favor_roots,
             cmd_roots,content}. Position index = ordinal verse number.
    A recall: favor verse at pos i, command verse at pos j, with
       (reverse=False) 0 < j-i <= W   (favor BEFORE command)
       (reverse=True)  0 < i-j <= W   (favor AFTER command; control)
    shared content root R in both verses (excl stoproots already removed).
    recall-EVENT = distinct (surah-local) (R, i, j) tuple. We count tuples.
    secondary: distinct R that participate (per surah) handled by caller.
    """
    n = len(records)
    events = 0
    roster = []
    roots_seen = set()
    for i in range(n):
        if not records[i]["favor"]:
            continue
        fc = records[i]["content"]
        if not fc:
            continue
        lo = i + 1
        hi = min(n, i + 1 + W)
        for j in range(lo, hi):
            if not records[j]["cmd"]:
                continue
            shared = fc & records[j]["content"]
            if not shared:
                continue
            for R in shared:
                events += 1
                roots_seen.add(R)
                if want_roster:
                    roster.append((R, i, j))
    return events, roots_seen, roster

# build per-surah record lists (canonical order) + observed
canonical_records = {}
for s, vs in surah_verses.items():
    canonical_records[s] = [verse_info[(s, v)] for v in vs]

def corpus_count(W, reverse=False):
    """sum of recall-EVENTS over all surahs (events = (R,i,j) tuples)."""
    tot = 0
    for s in surah_verses:
        recs = canonical_records[s]
        if reverse:
            # favor AFTER command: equivalent to running forward on reversed list
            ev, _, _ = count_recalls(list(reversed(recs)), W)
        else:
            ev, _, _ = count_recalls(recs, W)
        tot += ev
    return tot

obs_primary = corpus_count(W_PRIMARY, reverse=False)
obs_reverse = corpus_count(W_PRIMARY, reverse=True)
obs_W = {W_PRIMARY: obs_primary}
for W in W_VARIANTS:
    obs_W[W] = corpus_count(W, reverse=False)

# ============================================================
# build explicit ROSTER (canonical, W=primary) with verse numbers + glosses
# ============================================================
roster_full = []
for s, vs in surah_verses.items():
    recs = canonical_records[s]
    ev, _, rost = count_recalls(recs, W_PRIMARY, want_roster=True)
    for (R, i, j) in rost:
        vf = vs[i]; vc = vs[j]
        roster_full.append({
            "surah": s, "name": name[s], "region": region[s],
            "root": R,
            "favor_verse": vf, "command_verse": vc, "gap": vc - vf,
            "favor_verb_roots": sorted(verse_info[(s, vf)]["favor_roots"]),
            "command_verb_roots": sorted(verse_info[(s, vc)]["cmd_roots"]),
        })
roster_full.sort(key=lambda d: (d["surah"], d["favor_verse"], d["command_verse"], d["root"]))

# distinct (surah, root) recall-EVENTS for reporting
surah_root_events = sorted({(d["surah"], d["root"]) for d in roster_full})

# al-Duha validity check
duha_present = any(d["surah"] == 93 and d["root"] == "ytm"
                   and d["favor_verse"] == 6 and d["command_verse"] == 9
                   for d in roster_full)

# ============================================================
# NULL: within-surah verse-order shuffle, recompute corpus recall-events
# ============================================================
def run_null(seed, W):
    rng = random.Random(seed)
    null = []
    # pre-extract per-surah record lists (immutable verse contents)
    surah_recs = {s: list(canonical_records[s]) for s in surah_verses}
    for _ in range(NPERM):
        tot = 0
        for s in surah_verses:
            recs = surah_recs[s][:]
            rng.shuffle(recs)
            ev, _, _ = count_recalls(recs, W)
            tot += ev
        null.append(tot)
    return null

null_primary = run_null(SEED, W_PRIMARY)
mean_null = statistics.mean(null_primary)
sd_null = statistics.pstdev(null_primary)
ge = sum(1 for x in null_primary if x >= obs_primary)
p_primary = (ge + 1) / (NPERM + 1)
z_primary = (obs_primary - mean_null) / sd_null if sd_null > 0 else float("nan")
direction_ok = obs_primary > mean_null
PASS = bool(direction_ok and p_primary < 0.05 and duha_present)
reversed_violation = bool(obs_primary < mean_null)

# replication (MW-5)
null_repl = run_null(SEED_REPL, W_PRIMARY)
mean_null_repl = statistics.mean(null_repl)
ge_repl = sum(1 for x in null_repl if x >= obs_primary)
p_repl = (ge_repl + 1) / (NPERM + 1)
PASS_repl = bool(obs_primary > mean_null_repl and p_repl < 0.05)

# variant windows (MW-3): null mean + p for each
variant_results = {}
for W in W_VARIANTS:
    nl = run_null(SEED, W)
    mn = statistics.mean(nl)
    ge_v = sum(1 for x in nl if x >= obs_W[W])
    pv = (ge_v + 1) / (NPERM + 1)
    variant_results[W] = {
        "observed": obs_W[W], "null_mean": round(mn, 3),
        "p_value": pv, "direction_ok": obs_W[W] > mn,
        "z": round((obs_W[W] - mn) / statistics.pstdev(nl), 3) if statistics.pstdev(nl) > 0 else None,
    }

# reverse-direction control under the SAME null (MW-6):
# null for the reverse statistic = shuffle then count reverse
def run_null_reverse(seed, W):
    rng = random.Random(seed)
    null = []
    surah_recs = {s: list(canonical_records[s]) for s in surah_verses}
    for _ in range(NPERM):
        tot = 0
        for s in surah_verses:
            recs = surah_recs[s][:]
            rng.shuffle(recs)
            ev, _, _ = count_recalls(list(reversed(recs)), W)
            tot += ev
        null.append(tot)
    return null
null_rev = run_null_reverse(SEED, W_PRIMARY)
mean_null_rev = statistics.mean(null_rev)
z_rev = (obs_reverse - mean_null_rev) / statistics.pstdev(null_rev) if statistics.pstdev(null_rev) > 0 else None

# ============================================================
# census aggregates
# ============================================================
n_favor_verses = sum(1 for k in verse_info if verse_info[k]["favor"])
n_cmd_verses = sum(1 for k in verse_info if verse_info[k]["cmd"])
root_freq = Counter(d["root"] for d in roster_full)
surah_freq = Counter(d["surah"] for d in roster_full)
gap_dist = Counter(d["gap"] for d in roster_full)

# ============================================================
# emit
# ============================================================
out = {
    "finding": "H-NEW-2440",
    "title": "Favor->Command lexical-recall census",
    "prereg_sha256": actual,
    "seed": SEED, "seed_repl": SEED_REPL, "nperm": NPERM,
    "rules_tuple": "(no-tashkeel, QAC-root+POS/aspect/mood, segment-level, basmala-not-counted, Hafs-Kufan, Mashriqi)",
    "window_primary": W_PRIMARY,
    "favor_lexicon": sorted(FAVOR_LEXICON),
    "stoproots": sorted(STOPROOTS),
    "census": {
        "n_favor_verses": n_favor_verses,
        "n_command_verses": n_cmd_verses,
        "total_recall_pairs_tuples": len(roster_full),
        "distinct_surah_root_events": len(surah_root_events),
        "recalled_root_freq": dict(root_freq.most_common()),
        "surahs_with_recalls": dict(sorted(surah_freq.items())),
        "gap_distribution": {str(k): gap_dist[k] for k in sorted(gap_dist)},
    },
    "validity_check_duha_ytm_v6_v9": duha_present,
    "primary_test": {
        "statistic": "corpus total favor->command recall-pair tuples (W=8)",
        "observed": obs_primary,
        "null_mean": round(mean_null, 3),
        "null_sd": round(sd_null, 3),
        "z": round(z_primary, 3),
        "p_value": p_primary,
        "direction_locked": "observed > null (one-sided upper)",
        "direction_ok": direction_ok,
        "reversed_precommit_violation": reversed_violation,
        "alpha": 0.05,
        "PASS": PASS,
    },
    "replication_MW5": {
        "seed": SEED_REPL, "null_mean": round(mean_null_repl, 3),
        "p_value": p_repl, "PASS": PASS_repl,
    },
    "window_variants_MW3": variant_results,
    "reverse_control_MW6": {
        "note": "command->favor (favor AFTER command) recall; the device predicts forward >> reverse",
        "observed_reverse": obs_reverse,
        "null_mean_reverse": round(mean_null_rev, 3),
        "z_reverse": round(z_rev, 3) if z_rev is not None else None,
        "forward_minus_reverse_observed": obs_primary - obs_reverse,
    },
    "roster": roster_full,
    "distinct_surah_root_events": [{"surah": s, "name": name[s], "root": r} for (s, r) in surah_root_events],
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# ---- console summary ----
print("\n========== CENSUS ==========")
print(f"favor verses: {n_favor_verses} | command verses: {n_cmd_verses}")
print(f"recall-pair tuples (W={W_PRIMARY}): {len(roster_full)} | distinct (surah,root) events: {len(surah_root_events)}")
print("top recalled roots:", root_freq.most_common(12))
print("top surahs:", surah_freq.most_common(10))
print(f"\nVALIDITY: al-Duha ytm v6->v9 present = {duha_present}")
print("\n========== PRIMARY TEST (W=8) ==========")
print(f"observed={obs_primary}  null_mean={mean_null:.3f}  sd={sd_null:.3f}  z={z_primary:.3f}  p={p_primary:.5f}")
print(f"direction_ok={direction_ok}  reversed_violation={reversed_violation}  PASS={PASS}")
print(f"replication seed {SEED_REPL}: null_mean={mean_null_repl:.3f} p={p_repl:.5f} PASS={PASS_repl}")
print("\n========== MW-3 window variants ==========")
for W in W_VARIANTS:
    r = variant_results[W]
    print(f"  W={W}: obs={r['observed']} null={r['null_mean']} z={r['z']} p={r['p_value']:.5f} dir_ok={r['direction_ok']}")
print("\n========== MW-6 reverse control ==========")
print(f"forward obs={obs_primary} (z={z_primary:.2f}) vs reverse obs={obs_reverse} (z={z_rev:.2f} vs its own null {mean_null_rev:.2f})")
print(f"\n[ok] wrote {OUT}")
