#!/usr/bin/env python3
"""
H-NEW-2490 — The ADJACENT DOUBLING-FOR-EMPHASIS device (taʾkīd bi-l-tikrār):
corpus census + genre-concentration test.

The tightest, most semantically-constrained rung of the project's repetition
scale-ladder. Where H-NEW-2450 cast the widest net (ANY low-edit adjacent pair,
any mechanism), this finding isolates the DIRECTIONAL REASSERTION subset: verse/
clause B = verse/clause A repeated verbatim in its lexical CORE, differing only by
an emphatic leading connective (thumma / fa / wa) and optionally one minimal
in-place inflectional change. The textbook rhetorical *taʾkīd bi-l-tikrār*.

Seed family (from MASTER-FINDINGS-LEDGER §10.114 / §10.125):
  {Q75:34-35, Q78:4-5, Q102:3-4} — each is [thumma] + (preceding verse), 0 change.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2490-doubling-emphasis.md
Direction LOCKED (H1, confirmatory, k=1, alpha=0.05):
  the doubling device is GENRE-CONCENTRATED in juzz-amma (mushaf id 78-114),
  i.e. mean per-surah doubling-rate(juzz-amma) > mean(rest).  Reversed -> NULL.
H2 = descriptive census + connective-type distribution (NOT confirmatory).
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.

Instrument notes:
  - quran-no-tashkeel carries waqf/codex glyphs U+06D6-U+06ED -> STRIPPED.
  - QAC v0.4 morphology is the lens used ONLY to separate leading connectives from
    lexical cores and to supply ROOT for the inflection-shift test. The underlying
    canonical text is unchanged.
  - Adjacency = same-surah (i, i+1); 113 cross-surah junctions EXCLUDED.
  - This is COMPOSITIONAL repetition in ONE canonical text -- NOT qira'at / naskh.
"""
import json, hashlib, random, os, csv, unicodedata, re
from collections import Counter, defaultdict

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2490-doubling-emphasis.md")
EXPECTED_SHA = "6a2c133f2322598483a1ed87a94d7e928b588e8dc15d582d7a89668f621e5f87"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2490.json")
H2450 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2450.json")
SEED, NPERM = 20260509, 10000
SUB_CORE = 2          # substantive: >= 2 lexical-core tokens (locked)
AMMA_START = 78       # juzz-amma = mushaf id 78..114 (locked)

# ---- pre-reg lock ----
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

# ---- locked PAUSE set: waqf / codex annotation glyphs U+06D6..U+06ED ----
PAUSE = set(chr(c) for c in range(0x06D6, 0x06EE))

# the three named emphatic connectives, keyed by QAC LEMMA (standalone CONJ word)
CONN_LEM = {"vum~": "thumma", "wa": "wa", "fa": "fa"}   # CONJ lemma -> label
def norm(t):
    t = unicodedata.normalize("NFC", t)
    return "".join(c for c in t if c not in PAUSE)

# ======================== LOAD QAC MORPHOLOGY ========================
# We build, per (surah, verse), an ordered list of WORDS. Each word is a list of
# morpheme segments: (seg_text_bw, pos, prefix?, root, lemma). From this we derive:
#   - leading_conn: the surface connective ('thumma'/'fa'/'wa') iff the FIRST word's
#     FIRST segment is a CONJ of that set (standalone vum~, or PREFIX f:/w:CONJ).
#   - core_words: word-level list AFTER removing that single leading connective seg;
#     each core word is keyed by its concatenated NON-connective Buckwalter segments,
#     and carries the set of ROOTs among its segments (for the inflection test).
line_re = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")
words = defaultdict(lambda: defaultdict(list))   # words[(s,v)][w] = list of segs
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if line.startswith("#") or not line.startswith("("):
            continue
        m = line_re.match(line.rstrip("\n"))
        if not m:
            continue
        s, v, w, seg = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
        form, pos, feats = m.group(5), m.group(6), m.group(7)
        # NORMALIZE the QAC Buckwalter form: strip the pausal/elongation superscript
        # marker '^' (a codex pause notation, NOT a lexical difference; e.g. Q75:35's
        # '>awolaY`^' vs Q75:34's '>awolaY`' is the SAME word). Instrument note (logged).
        form = form.replace("^", "")
        root = None
        lr = re.search(r"ROOT:([^|]+)", feats)
        if lr:
            root = lr.group(1)
        lem = None
        ll = re.search(r"LEM:([^|]+)", feats)
        if ll:
            lem = ll.group(1)
        # leading emphatic-connective label, by the GRAPHEME the brief names {wa,fa,thumma}:
        #   - standalone CONJ word        -> match on LEMMA (vum~ -> thumma; wa; fa)
        #   - leading 'fa'/'wa' grapheme  -> ANY QAC prefix subtype (CONJ/CAUS/REM/RSLT/
        #     SUP for f; CONJ/CIRC/REM/SUP for w). The connective is the PARTICLE being
        #     prepended; its fine syntactic subtype does not change the rhetorical
        #     doubling (e.g. Q74:19 carries an f:CAUS 'fa', Q82:17 a w:CONJ 'wa').
        #     (Instrument decision, logged: faithful to the locked grapheme definition.)
        conn_label = None
        if "PREFIX|f:" in feats:
            conn_label = "fa"
        elif "PREFIX|w:" in feats:
            conn_label = "wa"
        elif pos == "CONJ" and lem in CONN_LEM:
            conn_label = CONN_LEM[lem]
        words[(s, v)][w].append({
            "form": form, "pos": pos, "root": root, "lem": lem,
            "conn_label": conn_label,
        })

def verse_core(sv):
    """Return (leading_conn, core_words) where core_words is a list of word-keys.
    A word-key = the tuple of its segment forms EXCLUDING a leading connective seg;
    we also return per-word root-set for the inflection test."""
    wmap = words.get(sv)
    if not wmap:
        return None, None
    idxs = sorted(wmap.keys())
    leading_conn = None
    core = []          # list of (wordkey_tuple, frozenset_of_roots)
    for wi, w in enumerate(idxs):
        segs = wmap[w]
        s2 = segs[:]
        # strip a SINGLE leading connective: only on the FIRST word, FIRST segment
        if wi == 0 and s2:
            first = s2[0]
            if first["conn_label"] is not None:
                leading_conn = first["conn_label"]
                s2 = s2[1:]
        if not s2:
            continue   # the whole word was just the connective
        key = tuple(seg["form"] for seg in s2)
        roots = frozenset(seg["root"] for seg in s2 if seg["root"])
        core.append((key, roots))
    return leading_conn, core

# ======================== DOUBLING PREDICATE D ========================
def minimal_core_diff(coreA, coreB):
    """Returns (matches, kind) where kind in:
       'identical'           -> cores equal (0 change)
       'root-inflection'     -> exactly one word substituted, same ROOT shared
       'sawfa-sa'            -> the sole difference is sawfa<->sa future-particle
       None                  -> not a doubling-grade match (>1 change, or content swap)
    Cores are equal-length-or-off-by-one-word lists of (wordkey, rootset)."""
    keysA = [k for k, _ in coreA]; keysB = [k for k, _ in coreB]
    rootsA = [r for _, r in coreA]; rootsB = [r for _, r in coreB]
    if keysA == keysB:
        return True, "identical"
    # sawfa<->sa: a FUT future particle realized as standalone 'sawofa' word vs an
    # 'sa' prefix segment on the verb. Compare by dropping FUT markers from keys.
    def drop_fut(keys):
        out = []
        for k in keys:
            kk = tuple(x for x in k if x not in ("sawofa", "sa"))
            if kk:
                out.append(kk)
            else:
                out.append(("<FUT>",))   # placeholder so positions align
        return out
    # require same word-count for the single in-place substitution test
    if len(keysA) == len(keysB):
        diffs = [i for i in range(len(keysA)) if keysA[i] != keysB[i]]
        if len(diffs) == 1:
            i = diffs[0]
            # sawfa<->sa within the differing word?
            ka, kb = keysA[i], keysB[i]
            ka_nf = tuple(x for x in ka if x not in ("sawofa", "sa"))
            kb_nf = tuple(x for x in kb if x not in ("sawofa", "sa"))
            has_fut_a = ("sawofa" in ka or "sa" in ka)
            has_fut_b = ("sawofa" in kb or "sa" in kb)
            if ka_nf == kb_nf and (has_fut_a or has_fut_b):
                return True, "sawfa-sa"
            # root-shared inflection shift on this single word?
            if rootsA[i] and rootsB[i] and (rootsA[i] & rootsB[i]):
                return True, "root-inflection"
            return None, None
        elif len(diffs) == 0:
            return True, "identical"
        return None, None
    # word-count differs by exactly one ONLY allowed if the extra word IS the
    # sawfa standalone particle vs an sa prefix (handled above by equal-length path
    # after FUT drop). Try the FUT-normalized comparison:
    dfa, dfb = drop_fut(keysA), drop_fut(keysB)
    if dfa == dfb:
        return True, "sawfa-sa"
    return None, None

def doubling(coreA, connA, coreB, connB):
    """B doubles A iff cores match (<=1 minimal change) AND they differ by exactly
    one leading emphatic connective (one member has it, other doesn't, OR different
    connectives). Returns (conn_type, change_kind) or None.
    conn_type: the connective that distinguishes them ('thumma'/'fa'/'wa') or 'bare'
    when cores match with NO connective difference (pure verbatim doubling)."""
    match, kind = minimal_core_diff(coreA, coreB)
    if not match:
        return None
    if connA == connB:
        # no connective difference: 'bare' doubling (expected ~0 adjacent)
        if connA is None:
            return ("bare", kind)
        return ("bare", kind)   # same connective both -> still bare-grade (no contrast)
    # exactly one connective differs -> the distinguishing connective is the one
    # present on whichever member carries it (or, if both carry different ones,
    # record both)
    present = [c for c in (connA, connB) if c is not None]
    if len(present) == 1:
        return (present[0], kind)
    return ("/".join(sorted(present)), kind)

# ======================== BUILD VERSE-GRAIN ROSTER ========================
quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
sname = {s["id"]: s["name"] for s in quran}
raw_text = {}
for s in quran:
    for v in s["verses"]:
        raw_text[(s["id"], v["id"])] = norm(v["text"])

# per-surah ordered verse ids
by_surah = {s["id"]: [v["id"] for v in s["verses"]] for s in quran}

roster = []
per_surah_doublings = defaultdict(int)
per_surah_sub_pairs = defaultdict(int)
conn_dist = Counter()
change_dist = Counter()
for sid, vids in by_surah.items():
    for k in range(len(vids) - 1):
        vi, vj = vids[k], vids[k + 1]
        cA = verse_core((sid, vi)); cB = verse_core((sid, vj))
        if cA[1] is None or cB[1] is None:
            continue
        connA, coreA = cA; connB, coreB = cB
        # substantive: BOTH cores >= SUB_CORE lexical-core words
        if len(coreA) < SUB_CORE or len(coreB) < SUB_CORE:
            continue
        per_surah_sub_pairs[sid] += 1
        res = doubling(coreA, connA, coreB, connB)
        if res is None:
            continue
        conn_type, change_kind = res
        per_surah_doublings[sid] += 1
        conn_dist[conn_type] += 1
        change_dist[change_kind] += 1
        roster.append({
            "ref": f"Q{sid}:{vi}-{vj}", "surah": sid, "name": sname[sid],
            "region": region[sid], "juzz_amma": sid >= AMMA_START,
            "connective": conn_type, "change_kind": change_kind,
            "text_i": raw_text[(sid, vi)], "text_j": raw_text[(sid, vj)],
            "core_len_i": len(coreA), "core_len_j": len(coreB),
        })

roster.sort(key=lambda r: (r["surah"], r["ref"]))

# validity check: all 3 seeds present
SEEDS = {"Q75:34-35", "Q78:4-5", "Q102:3-4"}
present_refs = {r["ref"] for r in roster}
missing = SEEDS - present_refs
assert not missing, f"SEED MISSING from verse-grain roster: {missing} -- predicate bug, halt."
print(f"[ok] all 3 seeds present: {sorted(SEEDS)}")

# ======================== WITHIN-VERSE CLAUSE-GRAIN CENSUS ========================
# Split a verse into clauses at internal connectives (CONJ segments / fa,wa,thumma
# prefixes that are NOT the verse-leading one). Two consecutive clauses double iff
# their lexical cores match (<=1 minimal change) and the second carries a connective
# the first doesn't. Descriptive only (MW-7 cap).
def verse_clauses(sv):
    """Return list of clauses; each clause = (leading_conn, core_words list)."""
    wmap = words.get(sv)
    if not wmap:
        return []
    idxs = sorted(wmap.keys())
    clauses = []
    cur_conn = None; cur_core = []
    for wi, w in enumerate(idxs):
        segs = wmap[w]
        # does this word START a new clause? (a CONJ/connective prefix marks a break,
        # except on the very first word which sets the verse-leading connective)
        first = segs[0]
        starts_clause = False
        this_conn = first["conn_label"]
        if this_conn is not None:
            starts_clause = (wi > 0)
        if wi == 0 and this_conn:
            cur_conn = this_conn
            rest = segs[1:]
        elif starts_clause:
            # flush current clause
            if cur_core:
                clauses.append((cur_conn, cur_core))
            cur_conn = this_conn; cur_core = []; rest = segs[1:]
        else:
            rest = segs
        if rest:
            key = tuple(seg["form"] for seg in rest)
            roots = frozenset(seg["root"] for seg in rest if seg["root"])
            cur_core.append((key, roots))
    if cur_core:
        clauses.append((cur_conn, cur_core))
    return clauses

clause_roster = []
for sid, vids in by_surah.items():
    for vi in vids:
        cls = verse_clauses((sid, vi))
        for a in range(len(cls) - 1):
            cA, coreA = cls[a]; cB, coreB = cls[a + 1]
            if len(coreA) < SUB_CORE or len(coreB) < SUB_CORE:
                continue
            res = doubling(coreA, cA, coreB, cB)
            if res is None:
                continue
            conn_type, change_kind = res
            if conn_type == "bare":
                continue   # within-verse bare repeats are not connective-doublings
            clause_roster.append({
                "ref": f"Q{sid}:{vi}", "surah": sid, "name": sname[sid],
                "region": region[sid], "juzz_amma": sid >= AMMA_START,
                "connective": conn_type, "change_kind": change_kind,
                "clause_i": " ".join("".join(k) for k, _ in coreA),
                "clause_j": " ".join("".join(k) for k, _ in coreB),
                "text": raw_text[(sid, vi)],
            })
clause_roster.sort(key=lambda r: (r["surah"], r["ref"]))
clause_conn_dist = Counter(r["connective"] for r in clause_roster)

# ======================== H1 — GENRE-CONCENTRATION (CONFIRMATORY) ========================
rates = {}
for sid in by_surah:
    if per_surah_sub_pairs[sid] > 0:
        rates[sid] = per_surah_doublings[sid] / per_surah_sub_pairs[sid]
amma = [sid for sid in rates if sid >= AMMA_START]
rest = [sid for sid in rates if sid < AMMA_START]
mean_amma = sum(rates[s] for s in amma) / len(amma) if amma else 0.0
mean_rest = sum(rates[s] for s in rest) / len(rest) if rest else 0.0
delta_obs = mean_amma - mean_rest

def label_perm_p(seed):
    rng = random.Random(seed)
    labeled = list(rates.keys()); n_amma = len(amma)
    ge = 0; nulls = []
    for _ in range(NPERM):
        pick = set(rng.sample(labeled, n_amma))
        ma = sum(rates[s] for s in pick) / n_amma
        others = [s for s in labeled if s not in pick]
        mr = sum(rates[s] for s in others) / len(others)
        d = ma - mr; nulls.append(d)
        if d >= delta_obs:
            ge += 1
    return (ge + 1) / (NPERM + 1), sum(nulls) / len(nulls)

p_h1, null_mean_h1 = label_perm_p(SEED)
p_h1_rep, _ = label_perm_p(SEED + 10)   # MW-5 replication

H1_reversed = delta_obs <= 0
H1_pass = (delta_obs > 0) and (p_h1 < 0.05)
if H1_reversed:
    H1_verdict = "NULL (pre-commit violation: reversed -- device is NOT juzz-amma-concentrated)"
elif H1_pass:
    H1_verdict = "PASS (genre-concentrated in juzz-amma)"
else:
    H1_verdict = "NULL (direction held but not significant)"

# MW-3 alternative cut: Meccan vs Medinan
mecc = [sid for sid in rates if region[sid] == "meccan"]
medn = [sid for sid in rates if region[sid] == "medinan"]
mean_mecc = sum(rates[s] for s in mecc) / len(mecc) if mecc else 0.0
mean_medn = sum(rates[s] for s in medn) / len(medn) if medn else 0.0
delta_mm = mean_mecc - mean_medn
# label-perm for Meccan>Medinan
def mm_perm(seed):
    rng = random.Random(seed); labeled = list(rates.keys()); nm = len(mecc); ge = 0
    for _ in range(NPERM):
        pick = set(rng.sample(labeled, nm))
        ma = sum(rates[s] for s in pick) / nm
        others = [s for s in labeled if s not in pick]
        mr = sum(rates[s] for s in others) / len(others)
        if (ma - mr) >= delta_mm:
            ge += 1
    return (ge + 1) / (NPERM + 1)
p_mm = mm_perm(SEED + 1)

# ======================== MW-6 — H-NEW-2450 SUBSET CHECK ========================
mw6 = {"note": "H-NEW-2450 csv not found; subset-check skipped"}
if os.path.exists(H2450):
    h2450 = json.load(open(H2450))
    # 2450 low-edit roster (char-edit <= 3) refs
    low2450 = {r["ref"] for r in h2450.get("roster", []) if r.get("char_edit", 99) <= 3}
    doub_refs = {r["ref"] for r in roster}
    overlap = sorted(low2450 & doub_refs)
    rejected = sorted(low2450 - doub_refs)   # 2450 low-edit pairs NOT doublings
    mw6 = {
        "h2450_low_edit_le3_count": len(low2450),
        "h2450_low_edit_refs": sorted(low2450),
        "doublings_among_2450_low_edit": overlap,
        "rejected_by_D_not_doublings": rejected,
        "interpretation": ("D is a STRICT SUBSET selector: it accepts the reassertion "
                           "pairs and rejects the parallel-template/rhyme-swap pairs."),
    }

# ======================== OUTPUT ========================
region_tally = Counter(r["region"] for r in roster)
amma_tally = sum(1 for r in roster if r["juzz_amma"])
out = {
    "finding": "H-NEW-2490",
    "title": "Adjacent doubling-for-emphasis (taʾkīd bi-l-tikrār): census + genre-concentration",
    "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi); QAC v0.4 segment lens for connective/core separation",
    "definition": ("B doubles A iff lexical cores match (<=1 minimal change: root-shared "
                   "inflection OR sawfa<->sa) AND they differ by exactly one leading "
                   "emphatic connective {thumma, fa, wa}. Substantive core >= 2 words."),
    "bands": {"substantive_min_core_words": SUB_CORE, "juzz_amma_start": AMMA_START},
    "counts": {
        "verse_grain_doublings": len(roster),
        "verse_grain_juzz_amma": amma_tally,
        "clause_grain_doublings": len(clause_roster),
        "substantive_adjacent_pairs_total": sum(per_surah_sub_pairs.values()),
    },
    "connective_distribution_verse_grain": dict(conn_dist.most_common()),
    "change_kind_distribution_verse_grain": dict(change_dist.most_common()),
    "connective_distribution_clause_grain": dict(clause_conn_dist.most_common()),
    "region_tally_verse_grain": dict(region_tally),
    "H1_genre_concentration": {
        "statistic": "Delta = mean per-surah doubling-rate(juzz-amma 78-114) - mean(rest 1-77)",
        "mean_rate_juzz_amma": round(mean_amma, 6),
        "mean_rate_rest": round(mean_rest, 6),
        "delta_obs": round(delta_obs, 6),
        "n_juzz_amma_surahs": len(amma), "n_rest_surahs": len(rest),
        "null_mean": round(null_mean_h1, 6),
        "p_one_sided": round(p_h1, 5),
        "p_replication_seed": round(p_h1_rep, 5),
        "direction_locked": "juzz-amma rate > rest",
        "alpha": 0.05, "k_confirmatory": 1,
        "verdict": H1_verdict,
    },
    "MW3_meccan_medinan": {
        "mean_rate_meccan": round(mean_mecc, 6),
        "mean_rate_medinan": round(mean_medn, 6),
        "delta_meccan_minus_medinan": round(delta_mm, 6),
        "p_one_sided": round(p_mm, 5),
        "note": "secondary genre axis (non-confirmatory)",
    },
    "MW6_h2450_subset_check": mw6,
    "verse_grain_roster": roster,
    "clause_grain_roster": clause_roster,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)

# ---- console summary ----
print("\n=== VERSE-GRAIN CENSUS ===")
print(f"doublings: {len(roster)}  (juzz-amma {amma_tally})  | region {dict(region_tally)}")
print(f"connective distribution: {dict(conn_dist.most_common())}")
print(f"change-kind distribution: {dict(change_dist.most_common())}")
for r in roster:
    print(f"  {r['ref']:>12}  [{r['connective']:>9}|{r['change_kind']:>15}]  "
          f"{r['region'][:4]}  {r['text_i']}  ||  {r['text_j']}")
print("\n=== WITHIN-VERSE CLAUSE-GRAIN CENSUS (descriptive) ===")
print(f"clause doublings: {len(clause_roster)}  | connective {dict(clause_conn_dist.most_common())}")
for r in clause_roster[:40]:
    print(f"  {r['ref']:>10}  [{r['connective']:>6}]  {r['text']}")
if len(clause_roster) > 40:
    print(f"  ... (+{len(clause_roster)-40} more in JSON)")
print("\n=== H1 GENRE-CONCENTRATION (CONFIRMATORY) ===")
print(f"rate juzz-amma={mean_amma:.5f}  rate rest={mean_rest:.5f}  Delta={delta_obs:.5f}")
print(f"null mean={null_mean_h1:.5f}  p={p_h1:.5f}  (repl p={p_h1_rep:.5f})")
print(f"H1 -> {H1_verdict}")
print("\n=== MW-3 Meccan vs Medinan ===")
print(f"rate Meccan={mean_mecc:.5f}  rate Medinan={mean_medn:.5f}  Delta={delta_mm:.5f}  p={p_mm:.5f}")
print("\n=== MW-6 H-NEW-2450 subset check ===")
if "doublings_among_2450_low_edit" in mw6:
    print(f"2450 low-edit(<=3): {mw6['h2450_low_edit_le3_count']}")
    print(f"  accepted by D (doublings): {mw6['doublings_among_2450_low_edit']}")
    print(f"  rejected by D (non-reassertion): {mw6['rejected_by_D_not_doublings']}")
print(f"\nWrote {OUT}")
