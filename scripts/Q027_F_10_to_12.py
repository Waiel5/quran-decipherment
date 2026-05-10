#!/usr/bin/env python3
"""
Q027 al-Naml Wave-3 novel-findings runner — Q027-F-10..F-12.

Per the 2026-05-10 specialist dispatch: T1/T2/T3 pre-registered tests on
Q 27's corpus-unique dual-basmala + Solomon-Sabaʾ pericope cohesion.

Pre-reg SHAs locked at top; fail-fast on mismatch (INVESTIGATION-PROTOCOL §1.2).

Tests:
  Q027-F-10  Internal basmala corpus-uniqueness (direct grep audit; deterministic)
  Q027-F-11  Q 27 total basmala count == 2; corpus-singleton uniqueness (deterministic)
  Q027-F-12  Solomon-Sabaʾ pericope Q 27:22-44 ↔ Q 34:15-19 root-Jaccard cohesion
             (cross-finding-025-formal pericope-scale test, 10000 perms, seed 20260509)

Outputs JSON to /Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/.
Discipline: seed 20260509; 10000 perms (where applicable).
"""

import json
import hashlib
import os
import random
import sys
from collections import Counter

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q027-F-10": "478ff8f90691dade34d037cb8529d9daaba8a818127dee967d7a811ba6673402",
    "Q027-F-11": "c451f1646b748bb46a76f485a0f9eb918c6596785b5a7abea8cf56eb006ef375",
    "Q027-F-12": "f1e2468b954fa93fbdc3e86e12d0d164f1482d564090551566f309387062bd1f",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q027-al-naml")
PREREG_FILES = {
    "Q027-F-10": "Q027-F-10-internal-basmala-corpus-uniqueness-prereg.md",
    "Q027-F-11": "Q027-F-11-q27-total-basmala-count-prereg.md",
    "Q027-F-12": "Q027-F-12-solomon-sabaq-pericope-cross-finding-025-prereg.md",
}

OUT_DIR = os.path.join(BASE, "surahs/Q027-al-naml/csv")
os.makedirs(OUT_DIR, exist_ok=True)

SEED = 20260509
N_PERM = 10000

BASMALA_NT = "بسم الله الرحمن الرحيم"  # no-tashkeel 6-token form


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg_shas():
    for fid, expected in PREREG_SHAS.items():
        p = os.path.join(PREREG_DIR, PREREG_FILES[fid])
        actual = sha256_file(p)
        if actual != expected:
            sys.stderr.write(
                f"SHA MISMATCH for {fid}: expected {expected}, got {actual}\n"
            )
            sys.stderr.write("FAIL-FAST per INVESTIGATION-PROTOCOL §1.2\n")
            sys.exit(2)
        print(f"[OK] {fid} SHA verified: {actual[:16]}...")


# ---------- corpus loaders ----------

def load_corpus(variant="no-tashkeel"):
    path = os.path.join(BASE, f"quran-text/quran-{variant}.json")
    with open(path) as f:
        return json.load(f)


def load_qac_roots_per_verse():
    qac_path = os.path.join(BASE, "data/morphology/quranic-corpus-morphology-0.4.txt")
    per_verse = {}
    with open(qac_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3] if len(parts) > 3 else ""
            try:
                loc_clean = loc.strip("()")
                s_str, v_str, w_str, seg_str = loc_clean.split(":")
                s, v = int(s_str), int(v_str)
            except Exception:
                continue
            root = None
            for feat in features.split("|"):
                if feat.startswith("ROOT:"):
                    root = feat[5:]
                    break
            if root:
                per_verse.setdefault((s, v), set()).add(root)
    return per_verse


# ---------- Q027-F-10: internal basmala corpus-uniqueness ----------

def run_F10(corpus_nt):
    out = {
        "finding_id": "Q027-F-10",
        "prereg_sha": PREREG_SHAS["Q027-F-10"],
        "rules_tuple": "(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "deterministic substring search; no permutation null",
        "target_substring": BASMALA_NT,
    }
    hits = []
    for s in corpus_nt:
        sid = s["id"]
        for v in s["verses"]:
            if BASMALA_NT in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    out["total_hits"] = len(hits)
    out["hits"] = hits
    # Partition into Q1 vs non-Q1
    q1_hits = [h for h in hits if h["surah"] == 1]
    non_q1_hits = [h for h in hits if h["surah"] != 1]
    out["q1_hits"] = q1_hits
    out["non_q1_hits"] = non_q1_hits
    out["non_q1_count"] = len(non_q1_hits)

    # Pre-registered locked direction: non_q1_count == 1, hit is Q 27:30
    expected_non_q1 = (1, 27, 30)  # (count, surah, verse)
    pass_count = (len(non_q1_hits) == 1)
    pass_loc = (
        pass_count
        and non_q1_hits[0]["surah"] == 27
        and non_q1_hits[0]["verse"] == 30
    )
    if pass_loc:
        verdict = "PASS-CONFIRMED"
    elif pass_count:
        verdict = "PRE-COMMIT-VIOLATION (count==1 but hit not at Q 27:30)"
    else:
        verdict = f"FALSIFIED (non_q1_count={len(non_q1_hits)}, expected 1)"
    out["verdict"] = verdict
    out["locked_direction"] = "corpus-singleton: count(non-Q1 hits) == 1 AND hit == Q 27:30"

    # Cross-validate under min-tashkeel + full-tashkeel
    cross_validation = {}
    for variant, target_token in [
        ("min-tashkeel", "بِسمِ اللَّهِ الرَّحمٰنِ الرَّحيمِ"),
        ("full-tashkeel", "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ"),
    ]:
        try:
            c = load_corpus(variant)
            vh = []
            for s in c:
                for v in s["verses"]:
                    if target_token in v["text"]:
                        vh.append({"surah": s["id"], "verse": v["id"]})
            cross_validation[variant] = {
                "target_token": target_token,
                "total_hits": len(vh),
                "hits": vh,
            }
        except Exception as e:
            cross_validation[variant] = {"error": str(e)}
    out["cross_validation"] = cross_validation

    return out


# ---------- Q027-F-11: Q 27 total basmala count ----------

def run_F11(corpus_nt):
    out = {
        "finding_id": "Q027-F-11",
        "prereg_sha": PREREG_SHAS["Q027-F-11"],
        "rules_tuple": "(no-tashkeel, orthographic-substring, basmala-as-surah-opener AND basmala-as-interior-verse counted separately, Hafs-Kufan, Mashriqi)",
        "method": "deterministic per-surah interior-substring count + opener-bookkeeping",
        "target_substring": BASMALA_NT,
    }

    # Interior substring count per surah
    interior = {}
    interior_hits_per_surah = {}
    for s in corpus_nt:
        sid = s["id"]
        cnt = 0
        hits = []
        for v in s["verses"]:
            if BASMALA_NT in v["text"]:
                cnt += 1
                hits.append({"verse": v["id"], "text": v["text"]})
        interior[sid] = cnt
        if hits:
            interior_hits_per_surah[sid] = hits

    out["interior_basmala_count_per_surah"] = interior
    out["interior_basmala_hits"] = interior_hits_per_surah

    # Opener-count per surah: 1 for all except Q 9; Q 1's basmala IS v.1 so opener counted as
    # part of interior under Form A (basmala-counted-only-in-Q1)
    # Form A (default, Hafs-Kufan canonical):
    #   total[s] = interior[s] (Q 1 already counts; Q 9 = 0 opener and 0 interior)
    #   But for Q 2-Q 8, Q 10-Q 114, the surah-header basmala is NOT a numbered verse;
    #   it sits outside interior counts. Under Form A, we use "counted-only-in-Q1" meaning
    #   only Q 1's basmala-as-v.1 enters the numbered-verse count; the 112 header basmalas
    #   are not counted.
    # Total-attestation (header + interior): for accounting purposes use Form B.

    # Form A — strict numbered-verse-counts under Hafs-Kufan
    form_a = {}
    for sid in range(1, 115):
        form_a[sid] = interior.get(sid, 0)
    # By Form A: Q 1 has 1 (interior), Q 27 has 1 (interior at v.30), others 0.

    # Form B — total ATTESTATIONS counting header + interior (113 surahs have header
    # = all except Q 9; Q 1's header IS its v.1 and is counted once not twice)
    form_b = {}
    for sid in range(1, 115):
        header = 0 if sid == 9 else 1
        interior_count = interior.get(sid, 0)
        if sid == 1:
            # Q 1's "header" IS v.1 — counted once
            form_b[sid] = max(header, interior_count)
        else:
            form_b[sid] = header + interior_count
    # By Form B: Q 1 has 1, Q 9 has 0, Q 27 has 2 (header + v.30), others have 1.

    out["form_A_strict_numbered_verse_counts"] = form_a
    out["form_B_total_attestations_including_headers"] = form_b

    # Locked check: under Form A, Q 27 is the unique non-Q1 surah with count >= 1 (== 1)
    # under Form B, Q 27 is the unique surah with count == 2

    # Form A: surahs with count >= 1
    form_a_positive = {sid: c for sid, c in form_a.items() if c >= 1}
    # Form B: surahs with count == 2
    form_b_twos = {sid: c for sid, c in form_b.items() if c == 2}

    out["form_A_surahs_with_count_geq_1"] = form_a_positive
    out["form_B_surahs_with_count_eq_2"] = form_b_twos

    # Locked verdict (Form B is the primary test for the "Q 27 = 2 basmalas" headline)
    form_b_q27_total = form_b.get(27, 0)
    form_b_others_with_2 = {sid: c for sid, c in form_b.items() if c == 2 and sid != 27}
    pass_q27 = (form_b_q27_total == 2)
    pass_unique = (len(form_b_others_with_2) == 0)
    if pass_q27 and pass_unique:
        verdict = "PASS-CONFIRMED"
    elif pass_q27 and not pass_unique:
        verdict = f"PRE-COMMIT-VIOLATION (Q 27 has 2 but other surahs also have 2: {form_b_others_with_2})"
    else:
        verdict = f"FALSIFIED (Q 27 Form-B count = {form_b_q27_total}, expected 2)"
    out["verdict"] = verdict
    out["form_B_q27_count"] = form_b_q27_total
    out["form_B_other_surahs_with_count_eq_2"] = form_b_others_with_2
    out["locked_direction"] = "Form-B: Q 27 count == 2; no other surah has count == 2"

    # Q 9 check (no basmala — important corpus baseline)
    out["form_A_q9_count"] = form_a.get(9, 0)
    out["form_B_q9_count"] = form_b.get(9, 0)

    return out


# ---------- Q027-F-12: Solomon-Sabaʾ pericope cohesion ----------

def get_pericope_roots(qac_roots, surah, verses):
    rset = set()
    for v in verses:
        rset.update(qac_roots.get((surah, v), set()))
    return rset


def jaccard(a, b):
    if not a and not b:
        return 0.0
    inter = a & b
    union = a | b
    return len(inter) / len(union) if union else 0.0


def get_surah_verse_count(corpus_nt, sid):
    for s in corpus_nt:
        if s["id"] == sid:
            return len(s["verses"])
    return 0


def random_contiguous_window(rng, corpus_nt, n_verses, exclude_surahs):
    """Draw a random contiguous N-verse window from a random surah not in exclude."""
    candidates = []
    for s in corpus_nt:
        if s["id"] in exclude_surahs:
            continue
        nv = len(s["verses"])
        if nv >= n_verses:
            candidates.append((s["id"], nv))
    if not candidates:
        return None
    sid, nv = rng.choice(candidates)
    start_idx = rng.randint(0, nv - n_verses)
    # Find the actual verse IDs (which start at 1)
    verses = [start_idx + 1 + i for i in range(n_verses)]
    return sid, verses


def run_F12(corpus_nt, qac_roots):
    out = {
        "finding_id": "Q027-F-12",
        "prereg_sha": PREREG_SHAS["Q027-F-12"],
        "rules_tuple": "(no-tashkeel, QAC v0.4 stem-ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "pericope-window root-Jaccard with permutation null over length-matched random pericope-pairs",
        "seed": SEED,
        "n_perm": N_PERM,
    }

    # Pericope A: Q 27:22-44 (23 verses)
    pericope_A_verses = list(range(22, 45))
    R_A = get_pericope_roots(qac_roots, 27, pericope_A_verses)
    # Pericope B: Q 34:15-19 (5 verses)
    pericope_B_verses = list(range(15, 20))
    R_B = get_pericope_roots(qac_roots, 34, pericope_B_verses)

    J_obs = jaccard(R_A, R_B)
    shared = R_A & R_B
    union = R_A | R_B

    out["pericope_A"] = {"surah": 27, "verses": pericope_A_verses, "n_unique_roots": len(R_A)}
    out["pericope_B"] = {"surah": 34, "verses": pericope_B_verses, "n_unique_roots": len(R_B)}
    out["shared_roots_count"] = len(shared)
    out["union_roots_count"] = len(union)
    out["shared_roots"] = sorted(shared)
    out["J_obs"] = J_obs

    # Permutation null: 10000 random pericope-pairs, length-matched
    N_A = len(pericope_A_verses)  # 23
    N_B = len(pericope_B_verses)  # 5
    rng = random.Random(SEED)
    null_jacs = []
    valid_perms = 0
    fail_perms = 0
    for _ in range(N_PERM):
        wa = random_contiguous_window(rng, corpus_nt, N_A, exclude_surahs={27, 34})
        if wa is None:
            fail_perms += 1
            continue
        sa, va = wa
        wb = random_contiguous_window(rng, corpus_nt, N_B, exclude_surahs={27, 34, sa})
        if wb is None:
            fail_perms += 1
            continue
        sb, vb = wb
        ra = get_pericope_roots(qac_roots, sa, va)
        rb = get_pericope_roots(qac_roots, sb, vb)
        null_jacs.append(jaccard(ra, rb))
        valid_perms += 1

    if not null_jacs:
        out["error"] = "no valid permutations"
        return out

    null_mean = sum(null_jacs) / len(null_jacs)
    null_var = sum((x - null_mean) ** 2 for x in null_jacs) / len(null_jacs)
    null_std = null_var ** 0.5
    z = (J_obs - null_mean) / null_std if null_std > 0 else 0.0
    # one-sided upper-tail p
    n_ge = sum(1 for x in null_jacs if x >= J_obs)
    p_perm = n_ge / len(null_jacs)

    out["null_mean"] = null_mean
    out["null_std"] = null_std
    out["n_perm_valid"] = valid_perms
    out["n_perm_fail"] = fail_perms
    out["z_score"] = z
    out["p_perm_one_sided_upper"] = p_perm
    out["n_null_ge_obs"] = n_ge

    direction_match = (J_obs > null_mean)
    out["direction_match"] = direction_match
    out["locked_direction"] = "J_obs > null_mean (one-sided upper-tail)"

    if direction_match and p_perm <= 0.05:
        verdict = "PASS-CONFIRMED"
    elif direction_match and p_perm <= 0.10:
        verdict = "PASS-DIRECTED"
    elif direction_match and p_perm <= 0.50:
        verdict = "NULL-DIRECTIONAL (weak direction, not significant)"
    elif not direction_match:
        verdict = "PRE-COMMIT-VIOLATION (reversed direction)"
    else:
        verdict = "NULL"
    out["verdict"] = verdict

    # Aux: per-verse-normalized concordance — average per-verse overlap of pericope-B verses with R_A
    per_verse_conc = []
    for v in pericope_B_verses:
        rv = qac_roots.get((34, v), set())
        if rv:
            per_verse_conc.append(len(rv & R_A) / len(rv))
        else:
            per_verse_conc.append(0.0)
    out["aux_per_verse_concordance_B_in_A"] = {
        "per_verse": per_verse_conc,
        "mean": sum(per_verse_conc) / len(per_verse_conc) if per_verse_conc else 0.0,
    }

    return out


# ---------- main ----------

def main():
    print("Verifying pre-reg SHAs...")
    verify_prereg_shas()

    print("Loading no-tashkeel corpus...")
    corpus_nt = load_corpus("no-tashkeel")
    print(f"  loaded {len(corpus_nt)} surahs")

    print("Running Q027-F-10 (internal basmala corpus-uniqueness)...")
    out_10 = run_F10(corpus_nt)
    with open(os.path.join(OUT_DIR, "Q027-F-10.json"), "w") as f:
        json.dump(out_10, f, ensure_ascii=False, indent=2)
    print(f"  verdict: {out_10['verdict']}")
    print(f"  hits: {out_10['total_hits']} total; non-Q1: {out_10['non_q1_count']}")

    print("Running Q027-F-11 (Q 27 total basmala count)...")
    out_11 = run_F11(corpus_nt)
    with open(os.path.join(OUT_DIR, "Q027-F-11.json"), "w") as f:
        json.dump(out_11, f, ensure_ascii=False, indent=2)
    print(f"  verdict: {out_11['verdict']}")
    print(f"  Form-B Q 27 count: {out_11['form_B_q27_count']}")
    print(f"  Form-B others with count == 2: {out_11['form_B_other_surahs_with_count_eq_2']}")

    print("Loading QAC roots per verse...")
    qac_roots = load_qac_roots_per_verse()
    print(f"  loaded roots for {len(qac_roots)} verses")

    print("Running Q027-F-12 (Solomon-Sabaʾ pericope cohesion)...")
    out_12 = run_F12(corpus_nt, qac_roots)
    with open(os.path.join(OUT_DIR, "Q027-F-12.json"), "w") as f:
        json.dump(out_12, f, ensure_ascii=False, indent=2)
    print(f"  verdict: {out_12['verdict']}")
    print(f"  J_obs = {out_12['J_obs']:.4f}; null_mean = {out_12['null_mean']:.4f}; z = {out_12['z_score']:.3f}; p_perm = {out_12['p_perm_one_sided_upper']:.4f}")

    print("All three tests complete. JSONs written to", OUT_DIR)


if __name__ == "__main__":
    main()
