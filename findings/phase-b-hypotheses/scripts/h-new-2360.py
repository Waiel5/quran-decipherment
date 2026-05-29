#!/usr/bin/env python3
"""
H-NEW-2360 — Antithesis = minimal shared frame + disjoint content (corpus-wide LAW-PROMOTION test).

Promotes the 3-way convergence (Q083-F-01 sijjīn↔ʿilliyyīn, Q066-F-01 frame-driven seal,
H-NEW-2290 verse-pair antithesis) to a corpus-wide law-strength claim — or rejects it.

GENERATOR: over every surah, slide non-overlapping W=5 verse-blocks; an ordered same-surah
block-pair (Bi,Bj) is ANTITHETICAL iff one block carries a field's + pole and the other its
− pole (locked 8-field opposed-lexicon, byte-identical to the SHA-locked H-NEW-2290 lexicon).

STRUCTURAL SIGNATURE (pre-registered, direction-locked, Bonferroni k=2, α_bon=0.025):
  Sub-test A (LOCKED z<0): mean content-Jaccard of antithetical pairs is BELOW a random
      same-surah W-block-pair null (content is DISJOINT, lower-tail p<α_bon).
  Sub-test B (LOCKED positive): mean frame-overlap (top-K corpus roots shared) is non-zero
      and NOT significantly depleted vs the random null (a shared minimal FRAME is preserved).

Content roots = block roots MINUS top-K frame roots MINUS pole-marker roots of any field.

Pre-reg SHA256 (verified at runtime): 5ecd80edc6983ff62782a849030fb43559ebed798b92c41c5510bc1533d6c252
Seed: 20260509 (primary), 20260601 (replication) | n_perm: 10000

Rules-tuple: (no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root set per block,
              basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)

All numbers from disk. Single-author: Waiel Al-Shujaa, Quran Decipherment Project.
"""
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2360-antithesis-law.md")
PREREG_SHA = "5ecd80edc6983ff62782a849030fb43559ebed798b92c41c5510bc1533d6c252"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2360.json")

SEED = 20260509
SEED_REP = 20260601
N_PERM = 10000
ALPHA_RAW = 0.05
K_BON = 2
ALPHA_BON = ALPHA_RAW / K_BON  # 0.025

W = 5             # locked block width
FRAME_K = 40      # locked frame size (top-K corpus roots)

# ---------------------------------------------------------------------------
# Locked opposed-field lexicon — byte-identical to the SHA-locked H-NEW-2290
# lexicon (Buckwalter QAC roots / lemma-restricted). Locked typo no-ops (Srk,
# >jr) are retained verbatim so the instrument is reproducible.
# ---------------------------------------------------------------------------
FIELDS = {
    "F1_faith": (
        {"roots": {"Amn"}, "lemma": {}},
        {"roots": {"kfr", "nfq", "Srk"}, "lemma": {}},
    ),
    "F2_guidance": (
        {"roots": {"hdy"}, "lemma": {}},
        {"roots": {"Dll"}, "lemma": {}},
    ),
    "F3_paradise_hellfire": (
        {"roots": set(), "lemma": {"jnn": {"jan~ap"}}},
        {"roots": {"jHm", "sEr", "sqr", "lZy"},
         "lemma": {"Hmm": {"Hamiym"}, "nwr": {"naAr"}, "Hwy": {"haAwiyap"}}},
    ),
    "F4_light_dark": (
        {"roots": set(), "lemma": {"nwr": {"nuwr", "m~uniyr"}}},
        {"roots": set(), "lemma": {"Zlm": {"Zuluma`t"}}},
    ),
    "F5_reward_punish": (
        {"roots": {"vwb", ">jr"},
         "lemma": {"jzy": {"jazaY`", "jazaA^'"}}},
        {"roots": set(),
         "lemma": {"Eqb": {"Ea`qibap", "EiqaAb", "EuqobaY"}}},
    ),
    "F6_righteous_corrupt": (
        {"roots": {"SlH", "brr"}, "lemma": {}},
        {"roots": {"fsd"}, "lemma": {"swA": {"suw^'", "say~i}ap", "say~i_#aAt"}}},
    ),
    "F7_good_foul": (
        {"roots": {"Tyb"}, "lemma": {}},
        {"roots": {"xbv"}, "lemma": {}},
    ),
    "F8_life_death": (
        {"roots": {"Hyy"}, "lemma": {}},
        {"roots": {"mwt"}, "lemma": {}},
    ),
}

# Pole-marker roots (any root that appears in any field's + or − spec, root or lemma key).
POLE_MARKER_ROOTS = set()
for _f, (_pos, _neg) in FIELDS.items():
    POLE_MARKER_ROOTS |= set(_pos["roots"]) | set(_pos["lemma"].keys())
    POLE_MARKER_ROOTS |= set(_neg["roots"]) | set(_neg["lemma"].keys())


def verify_sha():
    actual = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if actual != PREREG_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH\n expected {PREREG_SHA}\n actual   {actual}\n"
                 "ABORT (pre-commit discipline).")
    print(f"[ok] pre-reg SHA verified: {actual}")


LINE_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")


def load_qac():
    """Return (per_verse_rootlemma, per_verse_roots, freq_counter).
    per_verse_rootlemma[(s,v)] = set of (root,lemma) tuples (STEM segments).
    per_verse_roots[(s,v)]     = set of roots.
    freq_counter[root]         = corpus token frequency (STEM segments)."""
    per_rl = {}
    per_r = {}
    freq = Counter()
    with open(QAC, encoding="utf-8") as fh:
        for line in fh:
            m = LINE_RE.match(line.rstrip("\n"))
            if not m:
                continue
            feats = m.group(7)
            if "STEM" not in feats:
                continue
            rm = ROOT_RE.search(feats)
            if not rm:
                continue
            s, v = int(m.group(1)), int(m.group(2))
            root = rm.group(1).strip()
            lm = LEM_RE.search(feats)
            lemma = lm.group(1).strip() if lm else ""
            per_rl.setdefault((s, v), set()).add((root, lemma))
            per_r.setdefault((s, v), set()).add(root)
            freq[root] += 1
    return per_rl, per_r, freq


def block_poles(per_rl, sid, vstart, vend):
    """For a block, return dict field -> set of {'+','-'} poles present."""
    rl = set()
    for v in range(vstart, vend + 1):
        rl |= per_rl.get((sid, v), set())
    out = {}
    for fname, (pos, neg) in FIELDS.items():
        poles = set()
        if any(r in pos["roots"] for (r, _l) in rl) or \
           any(r in pos["lemma"] and l in pos["lemma"][r] for (r, l) in rl):
            poles.add("+")
        if any(r in neg["roots"] for (r, _l) in rl) or \
           any(r in neg["lemma"] and l in neg["lemma"][r] for (r, l) in rl):
            poles.add("-")
        if poles:
            out[fname] = poles
    return out


def is_antithetical(poles_i, poles_j):
    """Return list of fields giving an unambiguous cross-block + / − contrast."""
    fields = []
    for fname in FIELDS:
        pi = poles_i.get(fname, set())
        pj = poles_j.get(fname, set())
        plus_i, minus_i = "+" in pi, "-" in pi
        plus_j, minus_j = "+" in pj, "-" in pj
        # unambiguous contrast: (+ in i, - in j, NOT (+ in j and - in i)) or symmetric
        case1 = plus_i and minus_j and not (plus_j and minus_i)
        case2 = minus_i and plus_j and not (minus_j and plus_i)
        if case1 or case2:
            fields.append(fname)
    return fields


def block_root_set(per_r, sid, vstart, vend):
    s = set()
    for v in range(vstart, vend + 1):
        s |= per_r.get((sid, v), set())
    return s


def build_blocks(corpus, per_r, w):
    """surah_id -> list of (vstart, vend, root_set) for non-overlapping w-blocks."""
    blocks = {}
    for sd in corpus:
        sid = sd["id"]
        nv = sd["total_verses"]
        bl = []
        vs = 1
        while vs + w - 1 <= nv:
            ve = vs + w - 1
            bl.append((vs, ve, block_root_set(per_r, sid, vs, ve)))
            vs += w
        if len(bl) >= 2:
            blocks[sid] = bl
    return blocks


def content_set(root_set, frame):
    return root_set - frame - POLE_MARKER_ROOTS


def jaccard(a, b):
    u = a | b
    return (len(a & b) / len(u)) if u else None


def all_same_surah_pairs(blocks):
    """List of (sid, i, j) for all i<j within each surah."""
    pairs = []
    for sid, bl in blocks.items():
        n = len(bl)
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((sid, i, j))
    return pairs


def run(per_rl, per_r, corpus, frame, w, seed, frame_k_label):
    blocks = build_blocks(corpus, per_r, w)
    # precompute poles + content/frame sets per block
    poles = {}
    content = {}
    frameset = {}
    for sid, bl in blocks.items():
        poles[sid] = []
        content[sid] = []
        frameset[sid] = []
        for (vs, ve, rs) in bl:
            poles[sid].append(block_poles(per_rl, sid, vs, ve))
            content[sid].append(content_set(rs, frame))
            frameset[sid].append(rs & frame)

    all_pairs = all_same_surah_pairs(blocks)

    # identify antithetical pairs
    anti = []          # (sid,i,j,fields)
    for (sid, i, j) in all_pairs:
        fields = is_antithetical(poles[sid][i], poles[sid][j])
        if fields:
            anti.append((sid, i, j, fields))

    # observables on antithetical pairs
    anti_jac = []
    anti_frame = []
    census = []
    for (sid, i, j, fields) in anti:
        jc = jaccard(content[sid][i], content[sid][j])
        fo = len(frameset[sid][i] & frameset[sid][j])
        anti_frame.append(fo)
        if jc is not None:
            anti_jac.append(jc)
        census.append({
            "surah": sid,
            "block_i_verses": [blocks[sid][i][0], blocks[sid][i][1]],
            "block_j_verses": [blocks[sid][j][0], blocks[sid][j][1]],
            "fields": fields,
            "content_jaccard": jc,
            "frame_overlap": fo,
            "shared_content_roots": sorted(content[sid][i] & content[sid][j]),
            "shared_frame_roots": sorted(frameset[sid][i] & frameset[sid][j]),
        })

    n_anti = len(anti)
    n_anti_jac = len(anti_jac)
    jbar_anti = sum(anti_jac) / n_anti_jac if n_anti_jac else 0.0
    fbar_anti = sum(anti_frame) / n_anti if n_anti else 0.0
    zero_frame_frac = (sum(1 for x in anti_frame if x == 0) / n_anti) if n_anti else 1.0

    # population of same-surah pairs WITH defined content-jaccard (for the Jaccard null)
    pop_jac = []
    pop_frame = []
    for (sid, i, j) in all_pairs:
        jc = jaccard(content[sid][i], content[sid][j])
        if jc is not None:
            pop_jac.append(jc)
        pop_frame.append(len(frameset[sid][i] & frameset[sid][j]))

    rng = random.Random(seed)
    # Sub-test A null: draw equal-size (n_anti_jac) random sample of same-surah-pair
    #   content-Jaccards; null distribution of the MEAN.
    null_jbar = []
    for _ in range(N_PERM):
        samp = rng.sample(pop_jac, n_anti_jac) if n_anti_jac <= len(pop_jac) else pop_jac
        null_jbar.append(sum(samp) / len(samp))
    nA_mean = sum(null_jbar) / len(null_jbar)
    nA_sd = (sum((x - nA_mean) ** 2 for x in null_jbar) / len(null_jbar)) ** 0.5
    zA = (jbar_anti - nA_mean) / nA_sd if nA_sd else 0.0
    p_lower_A = sum(1 for x in null_jbar if x <= jbar_anti) / len(null_jbar)
    p_upper_A = sum(1 for x in null_jbar if x >= jbar_anti) / len(null_jbar)

    # Sub-test B null: equal-size (n_anti) random sample of same-surah-pair frame-overlaps.
    rng2 = random.Random(seed + 7)
    null_fbar = []
    for _ in range(N_PERM):
        samp = rng2.sample(pop_frame, n_anti) if n_anti <= len(pop_frame) else pop_frame
        null_fbar.append(sum(samp) / len(samp))
    nB_mean = sum(null_fbar) / len(null_fbar)
    nB_sd = (sum((x - nB_mean) ** 2 for x in null_fbar) / len(null_fbar)) ** 0.5
    zB = (fbar_anti - nB_mean) / nB_sd if nB_sd else 0.0
    p_lower_B = sum(1 for x in null_fbar if x <= fbar_anti) / len(null_fbar)

    return {
        "frame_k_label": frame_k_label,
        "block_width": w,
        "n_blocks_total": sum(len(bl) for bl in blocks.values()),
        "n_surahs_with_blocks": len(blocks),
        "n_same_surah_pairs": len(all_pairs),
        "n_antithetical_pairs": n_anti,
        "n_antithetical_pairs_with_content_jaccard": n_anti_jac,
        "subtest_A_content_disjoint": {
            "jbar_anti": jbar_anti,
            "null_mean": nA_mean,
            "null_sd": nA_sd,
            "z": zA,
            "p_lower_one_sided_LOCKED": p_lower_A,
            "p_upper_one_sided_reversal": p_upper_A,
            "direction_observed": "DISJOINT (z<0, locked)" if zA < 0 else "OVERLAPPING (z>=0, REVERSAL)",
        },
        "subtest_B_shared_frame": {
            "fbar_anti": fbar_anti,
            "zero_frame_fraction": zero_frame_frac,
            "null_mean": nB_mean,
            "null_sd": nB_sd,
            "z": zB,
            "p_lower_one_sided_depletion": p_lower_B,
            "frame_preserved": (fbar_anti > 0 and zero_frame_frac < 0.5 and p_lower_B >= ALPHA_BON),
        },
        "census": census,
    }


def main():
    verify_sha()
    corpus = json.load(open(QURAN, encoding="utf-8"))
    per_rl, per_r, freq = load_qac()
    print(f"[ok] loaded {len(corpus)} surahs; {len(freq)} distinct roots")

    frame = set(r for r, _ in freq.most_common(FRAME_K))
    print(f"[ok] frame = top-{FRAME_K} roots: {sorted(frame)}")

    print(f"[run] PRIMARY (W={W}, K={FRAME_K}, seed={SEED}) ...")
    primary = run(per_rl, per_r, corpus, frame, W, SEED, f"K{FRAME_K}")

    A = primary["subtest_A_content_disjoint"]
    B = primary["subtest_B_shared_frame"]
    print(f"   n_anti={primary['n_antithetical_pairs']} "
          f"(jac-eligible {primary['n_antithetical_pairs_with_content_jaccard']})")
    print(f"   A: Jbar_anti={A['jbar_anti']:.5f} null={A['null_mean']:.5f} "
          f"z={A['z']:+.3f} p_lower={A['p_lower_one_sided_LOCKED']:.4g} [{A['direction_observed']}]")
    print(f"   B: Fbar_anti={B['fbar_anti']:.4f} null={B['null_mean']:.4f} z={B['z']:+.3f} "
          f"zero-frame={B['zero_frame_fraction']:.3f} preserved={B['frame_preserved']}")

    # Verdict gates
    low_power = primary["n_antithetical_pairs"] < 30
    A_pass = (A["z"] < 0) and (A["p_lower_one_sided_LOCKED"] < ALPHA_BON)
    A_reversed = (A["z"] >= 0)
    B_pass = B["frame_preserved"]

    if A_pass and B_pass:
        verdict = "LAW-STRENGTH (corpus-wide): disjoint content + shared minimal frame"
    elif A_pass or B_pass:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    if A_reversed:
        verdict += " | SUB-TEST-A PRE-COMMIT VIOLATION (content NOT disjoint)"
    if low_power:
        verdict += " | LOW-POWER (<30 antithetical pairs; cap DIRECTIONAL)"

    # -------- Robustness (MW-3) ----------
    print("[run] robustness R1 (W=7) ...")
    r1 = run(per_rl, per_r, corpus, frame, 7, SEED, f"K{FRAME_K}_W7")

    print("[run] robustness R3 (K=25, K=60) ...")
    frame25 = set(r for r, _ in freq.most_common(25))
    frame60 = set(r for r, _ in freq.most_common(60))
    r3_k25 = run(per_rl, per_r, corpus, frame25, W, SEED, "K25")
    r3_k60 = run(per_rl, per_r, corpus, frame60, W, SEED, "K60")

    print("[run] robustness R4 (replication seed) ...")
    r4 = run(per_rl, per_r, corpus, frame, W, SEED_REP, f"K{FRAME_K}_repseed")

    # R2: raw content-Jaccard WITHOUT frame removal -- recompute quickly by treating
    # frame as empty set (pole markers still removed for fairness to the contrast).
    print("[run] robustness R2 (no frame removal) ...")
    r2 = run(per_rl, per_r, corpus, set(), W, SEED, "noFrameRemoval")

    result = {
        "finding_id": "h-new-2360",
        "title": "Antithesis = minimal shared frame + disjoint content — corpus-wide law-promotion test",
        "prereg_sha256": PREREG_SHA,
        "seed_primary": SEED, "seed_replication": SEED_REP, "n_perm": N_PERM,
        "alpha_raw": ALPHA_RAW, "k_bonferroni": K_BON, "alpha_bon": ALPHA_BON,
        "block_width_locked": W, "frame_k_locked": FRAME_K,
        "frame_roots": sorted(frame),
        "pole_marker_roots_excluded_from_content": sorted(POLE_MARKER_ROOTS),
        "rules_tuple": "(no-tashkeel, QAC v0.4 STEM-ROOT tokens, content-root set per block, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "primary": primary,
        "subtest_A_pass_alpha_bon": A_pass,
        "subtest_A_reversed": A_reversed,
        "subtest_B_pass": B_pass,
        "low_power": low_power,
        "robustness": {
            "R1_W7": {k: r1[k] for k in ("n_antithetical_pairs", "subtest_A_content_disjoint", "subtest_B_shared_frame")},
            "R2_no_frame_removal": {k: r2[k] for k in ("n_antithetical_pairs", "subtest_A_content_disjoint")},
            "R3_K25": {k: r3_k25[k] for k in ("n_antithetical_pairs", "subtest_B_shared_frame")},
            "R3_K60": {k: r3_k60[k] for k in ("n_antithetical_pairs", "subtest_B_shared_frame")},
            "R4_replication_seed": {k: r4[k] for k in ("n_antithetical_pairs", "subtest_A_content_disjoint", "subtest_B_shared_frame")},
        },
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    print(f"[ok] wrote {OUT}")
    print(f"[VERDICT] {verdict}")


if __name__ == "__main__":
    main()
