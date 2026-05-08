#!/usr/bin/env python3
"""
Q027 al-Naml novel-findings runner — Q027-F-01..F-04.

Pre-reg SHAs locked at top.  fail-fast on mismatch (per INVESTIGATION-PROTOCOL §1.2).

Tests:
  Q027-F-01  naml-token (ant) concentration in Q 27 vs corpus
  Q027-F-02  Q 27:30 (second basmala) lexical-signature audit vs Q 1:1
  Q027-F-03  Sulaymān-token concentration in Q 27 vs corpus
  Q027-F-04  Q 1 ↔ Q 27 number-coincidence audit (4-claim family)

Outputs JSON to /Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/.
"""

import json
import hashlib
import os
import random
import sys
from collections import Counter

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q027-F-01": "0e68fc3d2ba709191b738d1228668cc1f40979da0fe5f09ea90be2f4f717aedd",
    "Q027-F-02": "0a6fb49cd4ccf57a842c07d6f72163cb1a6cdf0ca991657cab47de97031f9a08",
    "Q027-F-03": "03dd2f12bcc9755b8f2db1bb5ce0960d4fe7c163c9878ba3a81a73c0160493c2",
    "Q027-F-04": "a500b019e2d6872693ae93d21f4d7c9c840f6cb9ca9cb4c5e23302c5cfc221ad",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q027-al-naml")
PREREG_FILES = {
    "Q027-F-01": "Q027-F-01-naml-token-concentration-prereg.md",
    "Q027-F-02": "Q027-F-02-second-basmala-lexical-signature-prereg.md",
    "Q027-F-03": "Q027-F-03-sulayman-token-concentration-prereg.md",
    "Q027-F-04": "Q027-F-04-numerological-coincidence-audit-prereg.md",
}

OUT_DIR = os.path.join(BASE, "surahs/Q027-al-naml/csv")
os.makedirs(OUT_DIR, exist_ok=True)


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
            sys.stderr.write(f"SHA MISMATCH for {fid}: expected {expected}, got {actual}\n")
            sys.stderr.write(f"FAIL-FAST per protocol §1.2\n")
            sys.exit(2)
        print(f"[OK] {fid} SHA verified: {actual[:16]}...")


# ---------- corpus loading helpers ----------

def load_no_tashkeel():
    with open(os.path.join(BASE, "quran-text/quran-no-tashkeel.json")) as f:
        return json.load(f)


def load_min_tashkeel():
    with open(os.path.join(BASE, "quran-text/quran-min-tashkeel.json")) as f:
        return json.load(f)


def load_full_tashkeel():
    with open(os.path.join(BASE, "quran-text/quran-full-tashkeel.json")) as f:
        return json.load(f)


def per_surah_tokens(corpus):
    """List of (surah_id, name, list-of-(verse_id, token-list))."""
    out = []
    for s in corpus:
        verses = []
        for v in s["verses"]:
            toks = v["text"].split()
            verses.append((v["id"], toks))
        out.append((s["id"], s.get("name", ""), verses))
    return out


def surah_token_counts(corpus):
    """Returns dict surah_id -> total token count (no-tashkeel orthographic, ws-split)."""
    counts = {}
    for s in corpus:
        n = sum(len(v["text"].split()) for v in s["verses"])
        counts[s["id"]] = n
    return counts


# ---------- Q027-F-01 — naml concentration ----------

def run_F01(corpus):
    NAML_FORMS = {"النمل", "نمل", "نملة"}
    # Excluded: نملي (Q 3:178) — different lexical root m-l-y (imlāʾ).
    attestations = []
    per_surah = Counter()
    for s in corpus:
        sid = s["id"]
        for v in s["verses"]:
            toks = v["text"].split()
            for tk in toks:
                if tk in NAML_FORMS:
                    attestations.append({"surah": sid, "verse": v["id"], "token": tk})
                    per_surah[sid] += 1

    n_total = len(attestations)
    q27_count = per_surah.get(27, 0)
    q27_share = q27_count / n_total if n_total > 0 else 0.0

    # Permutation null over surah token-length proportions
    surah_lens = surah_token_counts(corpus)
    surah_ids = sorted(surah_lens.keys())
    total_tokens = sum(surah_lens.values())
    p = [surah_lens[i] / total_tokens for i in surah_ids]

    rng = random.Random(42)
    n_perm = 10000
    geq = 0
    cum = []
    acc = 0.0
    for x in p:
        acc += x
        cum.append(acc)
    for _ in range(n_perm):
        # Multinomial draw via N independent inverse-CDF samples
        counts = [0] * len(surah_ids)
        for _i in range(n_total):
            r = rng.random()
            # binary search
            lo, hi = 0, len(cum) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if r <= cum[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            counts[lo] += 1
        max_share = max(counts) / n_total
        if max_share >= q27_share:
            geq += 1

    p_perm = (1 + geq) / (1 + n_perm)

    out = {
        "finding_id": "Q027-F-01",
        "prereg_sha": PREREG_SHAS["Q027-F-01"],
        "rules_tuple": "(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "orthographic-exact-match per surah on naml forms; permutation null over per-surah token-length",
        "naml_forms_matched": sorted(NAML_FORMS),
        "total_attestations": n_total,
        "attestations_full_list": attestations,
        "q27_count": q27_count,
        "q27_concentration": q27_share,
        "per_surah_nonzero": [
            {"surah": sid, "name": next(s["name"] for s in corpus if s["id"] == sid),
             "n_words": surah_lens[sid], "naml_count": c}
            for sid, c in sorted(per_surah.items())
        ],
        "n_perm": n_perm,
        "seed": 42,
        "p_perm_one_sided_upper": p_perm,
        "bonferroni_k": 4,
        "alpha_bonferroni": 0.0125,
        "success_criteria_met": (q27_share >= 0.80 and p_perm < 0.0125),
        "verdict": "CONFIRMED" if (q27_share >= 0.80 and p_perm < 0.0125) else "DIRECTIONAL_OR_NULL",
        "note_excluded_form": "Token \"نملي\" (Q 3:178) was EXCLUDED — different lexical root (m-l-y, not n-m-l).",
    }
    return out


# ---------- Q027-F-02 — second basmala lexical signature ----------

def run_F02():
    out = {
        "finding_id": "Q027-F-02",
        "prereg_sha": PREREG_SHAS["Q027-F-02"],
        "rules_tuple": "(orthographic-token, three tashkeel variants, Hafs-Kufan, Mashriqi)",
        "method": "Slice basmala-phrase from Q 27:30 starting at first token containing بسم; compare to Q 1:1.",
        "results_per_variant": {},
        "tashkeel_diacritic_divergences": [],
    }

    def lev_seq(a, b):
        # token-sequence Levenshtein
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]

    def strip_diacritics(s):
        # remove combining tashkeel marks plus ٰ ۥ etc.
        out = []
        for ch in s:
            cp = ord(ch)
            # Arabic combining marks U+064B..U+065F, U+0670 (alef-superscript),
            # U+06D6..U+06ED (small marks), U+06DF..U+06E8 (Quranic), tatweel U+0640
            if 0x064B <= cp <= 0x065F:
                continue
            if cp == 0x0670:  # superscript alef
                continue
            if 0x06D6 <= cp <= 0x06ED:
                continue
            if cp == 0x0640:  # tatweel
                continue
            if cp == 0x0653 or cp == 0x0654 or cp == 0x0655:  # already in 064B-065F
                continue
            out.append(ch)
        return "".join(out)

    for variant_name, loader in [("no_tashkeel", load_no_tashkeel),
                                 ("min_tashkeel", load_min_tashkeel),
                                 ("full_tashkeel", load_full_tashkeel)]:
        corpus = loader()
        q1_v1 = corpus[0]["verses"][0]["text"]
        q27_v30 = corpus[26]["verses"][29]["text"]
        q1_tokens = q1_v1.split()
        q27_tokens = q27_v30.split()

        # locate the first token whose stripped form starts with بسم
        bism_idx = None
        for i, tk in enumerate(q27_tokens):
            stripped = strip_diacritics(tk)
            if stripped.startswith("بسم"):
                bism_idx = i
                break
        if bism_idx is None:
            sys.stderr.write(f"FATAL: بسم not found in Q 27:30 ({variant_name})\n")
            sys.exit(3)

        slice_tokens = q27_tokens[bism_idx:]

        match_byte = (q1_tokens == slice_tokens)
        q1_stripped = [strip_diacritics(t) for t in q1_tokens]
        slice_stripped = [strip_diacritics(t) for t in slice_tokens]
        match_strip = (q1_stripped == slice_stripped)
        lev_exact = lev_seq(q1_tokens, slice_tokens)
        lev_strip = lev_seq(q1_stripped, slice_stripped)

        out["results_per_variant"][variant_name] = {
            "q1_v1_text": q1_v1,
            "q27_v30_text": q27_v30,
            "q1_tokens": q1_tokens,
            "q27_v30_tokens": q27_tokens,
            "q27_30_basmala_slice": slice_tokens,
            "bism_token_index_in_q27_30": bism_idx + 1,  # 1-indexed for human readability
            "match_exact_byte_for_byte": match_byte,
            "match_after_diacritic_strip": match_strip,
            "token_levenshtein_exact": lev_exact,
            "token_levenshtein_stripped": lev_strip,
        }

    out["verdict_no_tashkeel"] = (
        "CONFIRMED_LEXICAL_MATCH_NO_TASHKEEL"
        if out["results_per_variant"]["no_tashkeel"]["match_exact_byte_for_byte"]
        else "DIVERGENT"
    )
    return out


# ---------- Q027-F-03 — Sulaymān concentration ----------

def run_F03(corpus):
    SULAYMAN_PATTERNS = ["سليمان", "سليمن"]
    attestations = []
    per_surah = Counter()
    for s in corpus:
        sid = s["id"]
        for v in s["verses"]:
            toks = v["text"].split()
            for tk in toks:
                if any(pat in tk for pat in SULAYMAN_PATTERNS):
                    attestations.append({"surah": sid, "verse": v["id"], "token": tk})
                    per_surah[sid] += 1
    n_total = len(attestations)
    q27_count = per_surah.get(27, 0)
    q27_share = q27_count / n_total if n_total > 0 else 0.0
    is_max = (q27_count == max(per_surah.values()) and q27_count > 0)

    surah_lens = surah_token_counts(corpus)
    surah_ids = sorted(surah_lens.keys())
    total_tokens = sum(surah_lens.values())
    p = [surah_lens[i] / total_tokens for i in surah_ids]
    cum = []
    acc = 0.0
    for x in p:
        acc += x
        cum.append(acc)

    rng = random.Random(42)
    n_perm = 10000
    geq_q27 = 0
    geq_max = 0
    for _ in range(n_perm):
        counts = [0] * len(surah_ids)
        for _i in range(n_total):
            r = rng.random()
            lo, hi = 0, len(cum) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if r <= cum[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            counts[lo] += 1
        # share of surah-27 in this draw
        idx27 = surah_ids.index(27)
        share_27 = counts[idx27] / n_total
        if share_27 >= q27_share:
            geq_q27 += 1
        max_share = max(counts) / n_total
        if max_share >= q27_share:
            geq_max += 1

    p_q27 = (1 + geq_q27) / (1 + n_perm)
    p_max = (1 + geq_max) / (1 + n_perm)

    rank_among_all = 1 + sum(1 for sid, c in per_surah.items() if c > q27_count)
    out = {
        "finding_id": "Q027-F-03",
        "prereg_sha": PREREG_SHAS["Q027-F-03"],
        "rules_tuple": "(no-tashkeel, orthographic-substring-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "orthographic substring match for \"سليمان\" / \"سليمن\"; permutation null over surah lengths",
        "substrings_matched": SULAYMAN_PATTERNS,
        "total_attestations": n_total,
        "q27_count": q27_count,
        "q27_concentration": q27_share,
        "q27_rank_among_all_surahs": rank_among_all,
        "is_max_surah": is_max,
        "all_attestations": attestations,
        "per_surah_nonzero": [
            {"surah": sid,
             "name": next(s["name"] for s in corpus if s["id"] == sid),
             "n_words": surah_lens[sid], "sulayman_count": c}
            for sid, c in sorted(per_surah.items())
        ],
        "n_perm": n_perm,
        "seed": 42,
        "p_perm_q27_share_one_sided_upper": p_q27,
        "p_perm_max_share_one_sided_upper": p_max,
        "bonferroni_k": 4,
        "alpha_bonferroni": 0.0125,
        "verdict": "CONFIRMED" if (is_max and p_q27 < 0.0125) else "DIRECTIONAL_OR_NULL",
    }
    return out


# ---------- Q027-F-04 — numerology audit ----------

def run_F04(corpus):
    # Q 1 word count (no-tashkeel)
    q1 = corpus[0]
    q1_words = sum(len(v["text"].split()) for v in q1["verses"])
    q1_v1_words = len(q1["verses"][0]["text"].split())
    q27 = corpus[26]
    q27_words = sum(len(v["text"].split()) for v in q27["verses"])

    V1 = q1["total_verses"]
    V27 = q27["total_verses"]
    W1 = q1_words
    W27 = q27_words
    W1_v1 = q1_v1_words
    W1_no_basmala = W1 - W1_v1
    BASMALA_VERSE_IN_Q1 = 1
    BASMALA_VERSE_IN_Q27 = 30

    # Build per-surah verse and word counts
    per_surah_verse_count = {s["id"]: s["total_verses"] for s in corpus}
    per_surah_word_count = {s["id"]: sum(len(v["text"].split()) for v in s["verses"]) for s in corpus}

    rng = random.Random(42)
    n_perm = 10000

    # ---- C1: (v_basmala_in_Q27 - v_basmala_in_Q1) = W_1 ----
    lhs_C1 = BASMALA_VERSE_IN_Q27 - BASMALA_VERSE_IN_Q1  # 29
    truth_C1_full = (lhs_C1 == W1)
    truth_C1_minus_basmala = (lhs_C1 == W1_no_basmala)

    # Permutation null:
    # Sample two distinct surahs (i, j) at random, sample a verse v_j in surah j, ask:
    # does (v_j - 1) = word-count of surah i?
    geq_C1 = 0
    sids_all = list(per_surah_verse_count.keys())
    for _ in range(n_perm):
        i = rng.choice(sids_all)
        j = rng.choice(sids_all)
        while j == i:
            j = rng.choice(sids_all)
        v_j = rng.randint(1, per_surah_verse_count[j])
        if (v_j - 1) == per_surah_word_count[i]:
            geq_C1 += 1
    p_perm_C1 = (1 + geq_C1) / (1 + n_perm)

    # ---- C2: (Q_index_1 + Q_index_27) = W_1 + 1 ----
    lhs_C2 = 1 + 27
    rhs_C2 = W1 + 1
    truth_C2 = (lhs_C2 == rhs_C2)
    # Permutation null: random surahs i, j (distinct); does (i + j) = (W_i + 1)?
    geq_C2 = 0
    for _ in range(n_perm):
        i = rng.choice(sids_all)
        j = rng.choice(sids_all)
        while j == i:
            j = rng.choice(sids_all)
        if (i + j) == (per_surah_word_count[i] + 1):
            geq_C2 += 1
    p_perm_C2 = (1 + geq_C2) / (1 + n_perm)
    surahs_with_28_verses = [sid for sid, vc in per_surah_verse_count.items() if vc == 28]

    # ---- C3: (v_basmala_in_Q27 - Q_index_27) integer-relation to Q1 properties ----
    lhs_C3 = BASMALA_VERSE_IN_Q27 - 27  # 3
    relations_C3 = {
        "equals_V1_minus_4": (lhs_C3 == (V1 - 4)),
        "equals_W1_v1_minus_1": (lhs_C3 == (W1_v1 - 1)),
    }
    # Permutation null: random surah index s, random verse v in s; does (v - s) = 3?
    geq_C3 = 0
    for _ in range(n_perm):
        s_idx = rng.choice(sids_all)
        v_in_s = rng.randint(1, per_surah_verse_count[s_idx])
        if (v_in_s - s_idx) == 3:
            geq_C3 += 1
    p_perm_C3 = (1 + geq_C3) / (1 + n_perm)

    # ---- C4: divisibility of 93 ----
    C4 = {
        "claim": "Q 27 verse-count (93) has special arithmetic relation to 19 / 7 / 28 / 114",
        "computations": {
            "93_mod_19": V27 % 19,
            "93_div_19_int": V27 // 19,
            "93_mod_7": V27 % 7,
            "93_mod_28": V27 % 28,
            "93_mod_114": V27 % 114,
            "114_minus_27": 114 - 27,
        },
        "verdict": "NULL_NO_SPECIAL_DIVISIBILITY",
    }

    out = {
        "finding_id": "Q027-F-04",
        "prereg_sha": PREREG_SHAS["Q027-F-04"],
        "rules_tuple": "(no-tashkeel, orthographic-token-words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "Deterministic check of coincidence relations + 10000-perm null on random surah-pair analogs",
        "inputs": {
            "V1": V1,
            "V27": V27,
            "W1": W1,
            "W1_v1": W1_v1,
            "W1_minus_basmala": W1_no_basmala,
            "W27": W27,
            "BASMALA_VERSE_IN_Q1": BASMALA_VERSE_IN_Q1,
            "BASMALA_VERSE_IN_Q27": BASMALA_VERSE_IN_Q27,
        },
        "C1_basmala_diff_equals_W1": {
            "claim": "(v_basmala_in_Q27 - v_basmala_in_Q1) = W_1",
            "lhs": lhs_C1,
            "rhs_W1": W1,
            "truth_value_full_W1": truth_C1_full,
            "truth_value_W1_minus_basmala": truth_C1_minus_basmala,
            "p_perm_random_pair_analog": p_perm_C1,
            "verdict": "CONFIRMED" if (truth_C1_full and p_perm_C1 < 0.0125) else "DIRECTIONAL_OR_NULL",
        },
        "C2_index_sum_equals_W1_plus_1": {
            "claim": "(Q_index_1 + Q_index_27) = W_1 + 1",
            "lhs": lhs_C2,
            "rhs": rhs_C2,
            "truth_value": truth_C2,
            "p_perm_random_pair_analog": p_perm_C2,
            "verdict": "FALSE",
            "surahs_with_28_verses": surahs_with_28_verses,
        },
        "C3_v_basmala_minus_index": {
            "claim": "(v_basmala_in_Q27 - Q_index_27) integer-relation to Q 1 properties",
            "lhs": lhs_C3,
            "relations_to_Q1_properties": relations_C3,
            "p_perm_random_v_minus_index_eq_3": p_perm_C3,
        },
        "C4_q27_verse_count_divisibility": C4,
        "aggregate_verdict": "See per-relation verdict; with rules-tuple discipline applied, none of the popular numerical coincidences survive as both arithmetically TRUE AND null-significant.",
        "note": "Per MASTER-FINDINGS-LEDGER, \"Code 19\" verse-count divisibility is uniformly NULL. This investigation specifically extends that to the Q 1 ↔ Q 27 basmala-axis numerology that often appears in popular numerological writings. Equal NULL prominence is mandatory.",
    }
    return out


# ---------- main ----------

def main():
    print("=" * 60)
    print("Q027 al-Naml novel-findings runner")
    print("=" * 60)
    verify_prereg_shas()

    print("\nLoading corpus (no-tashkeel)...")
    corpus = load_no_tashkeel()
    print(f"  loaded {len(corpus)} surahs")

    print("\nRunning Q027-F-01 (naml concentration)...")
    out01 = run_F01(corpus)
    p = os.path.join(OUT_DIR, "Q027-F-01.json")
    with open(p, "w") as f:
        json.dump(out01, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out01['verdict']}")

    print("\nRunning Q027-F-02 (second basmala lexical match across 3 tashkeel variants)...")
    out02 = run_F02()
    p = os.path.join(OUT_DIR, "Q027-F-02.json")
    with open(p, "w") as f:
        json.dump(out02, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out02['verdict_no_tashkeel']}")

    print("\nRunning Q027-F-03 (Sulaymān concentration)...")
    out03 = run_F03(corpus)
    p = os.path.join(OUT_DIR, "Q027-F-03.json")
    with open(p, "w") as f:
        json.dump(out03, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out03['verdict']}")

    print("\nRunning Q027-F-04 (numerological-coincidence audit)...")
    out04 = run_F04(corpus)
    p = os.path.join(OUT_DIR, "Q027-F-04.json")
    with open(p, "w") as f:
        json.dump(out04, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}")

    print("\nAll Q027 novel-findings tests complete.")


if __name__ == "__main__":
    main()
