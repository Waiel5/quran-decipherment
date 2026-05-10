#!/usr/bin/env python3
"""H-NEW-1390 — Corpus-wide search for OPENING-LINKED CONTENT-DIVERGENT mushaf-adjacent pairs.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1390-opening-linked-content-divergent.md
Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1,
              Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1390-opening-linked-content-divergent.md"
EXPECTED_SHA = "d17f38124d228623f7e512d301f6519590ece5c4cd2c6b543e983a1185a41ec2"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
FR_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
ADJ_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-720.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1390.json"

SEED = 20260509  # locked; no randomization in this enumerative test


def verify_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"OK: pre-reg SHA verified: {actual}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Opener class taxonomy (locked in pre-reg)
# ---------------------------------------------------------------------------
MUQATTA_SINGLETONS = {
    "الم", "الر", "حم", "يس", "طس", "ق", "ص", "ن",
    "كهيعص", "طه", "طسم", "المص", "المر", "حمعسق",
}


def opener_class_strict(words):
    """Return (class, subclass) tuple. subclass is None unless ya-ayyuha-X."""
    if not words:
        return ("empty", None)
    w1 = words[0]
    # basmala (only Q1 in mushaf order)
    if w1 == "بسم":
        return ("basmala", None)
    if w1 == "قل":
        return ("qul", None)
    if w1 == "الحمد":
        return ("al-hamd", None)
    if w1 == "تبارك":
        return ("tabaraka", None)
    if w1 == "سبح":
        return ("sabbaha", None)
    if w1 == "يسبح":
        return ("yusabbihu", None)
    if w1 == "يا":
        if len(words) >= 3 and words[1] == "أيها":
            return ("ya-ayyuha", words[2])  # subclass = addressee word
        return ("ya-other", None)
    if w1 == "تنزيل":
        return ("tanzil", None)
    if w1 == "إذا":
        return ("idha", None)
    if w1 == "قد":
        return ("qad", None)
    if w1 == "إنا":
        return ("inna", None)
    if w1 == "لم":
        return ("lam", None)
    if w1 == "لا":
        return ("la", None)
    if w1 == "هل":
        return ("hal", None)
    if w1 == "أرأيت":
        return ("ar-ayta", None)
    if w1 == "ألم":
        return ("a-lam", None)
    if w1 == "ألهاكم":
        return ("alhakum", None)
    # wa-X oath pattern: starts with wa- prefix attached to a noun (single token starting with و)
    if w1.startswith("و") and len(w1) > 1:
        return ("wa-oath", w1)  # subclass = the oath-noun token
    if w1 in MUQATTA_SINGLETONS:
        return ("muqatta", w1)
    return ("other", w1)


def axis_C_strict_match(cls_a, cls_b):
    """Axis C strict: same class AND same subclass (where applicable)."""
    if cls_a[0] != cls_b[0]:
        return False
    # for classes with subclass-matching: ya-ayyuha, muqatta, wa-oath, other
    if cls_a[0] in ("ya-ayyuha", "muqatta", "wa-oath", "other"):
        return cls_a[1] == cls_b[1]
    return True


def axis_C_loose_match(cls_a, cls_b):
    """Axis C loose: same class only (no subclass match required)."""
    return cls_a[0] == cls_b[0]


# ---------------------------------------------------------------------------
# Axis B: morph-iso first 3 words
# ---------------------------------------------------------------------------
def axis_B(words_a, words_b):
    """word-1 + word-2 identical, word-3 same template (first letter + length ±1)."""
    # Handle empty
    if not words_a or not words_b:
        return False
    # Require at least 2 words on both sides
    if len(words_a) < 2 or len(words_b) < 2:
        return False
    # word-1 must match exactly
    if words_a[0] != words_b[0]:
        return False
    # word-2 must match exactly
    if words_a[1] != words_b[1]:
        return False
    # word-3 template match
    if len(words_a) < 3 and len(words_b) < 3:
        # Both 2-word verses with matching pair
        return True
    if len(words_a) < 3 or len(words_b) < 3:
        # One has 3 words, the other doesn't — not isomorphic
        return False
    w3a, w3b = words_a[2], words_b[2]
    if w3a == w3b:
        return True  # exact match counts as templated match
    # same first letter and length within ±1
    if w3a[0] == w3b[0] and abs(len(w3a) - len(w3b)) <= 1:
        return True
    return False


def main():
    verify_sha()

    # Load data
    quran = json.loads(QURAN.read_text())
    fr = json.loads(FR_PATH.read_text())
    adj = json.loads(ADJ_PATH.read_text())

    # Fisher-Rao matrix (114 x 114), 1-indexed in source
    n = 114
    D = [[0.0] * n for _ in range(n)]
    for i, j, d in fr["D_matrix_upper_triangular"]:
        D[i - 1][j - 1] = d
        D[j - 1][i - 1] = d

    # Per-surah v1 words
    v1_words = {}
    for s in quran:
        sid = s["id"]
        text = s["verses"][0]["text"]
        v1_words[sid] = text.split()

    # Axis A flags: delta_raw <= 0 ⇒ A=TRUE
    axis_A_flags = {}
    for entry in adj["per_adjacency"]:
        n_a = entry["s"]  # Q_n where pair is (Q_n, Q_{n+1})
        axis_A_flags[n_a] = (entry["delta_raw"] <= 0)
    # Sanity: should be 113 entries
    assert len(axis_A_flags) == 113, f"Expected 113 adjacency entries, got {len(axis_A_flags)}"
    a_true_count = sum(1 for v in axis_A_flags.values() if v)
    print(f"Axis A: {a_true_count}/113 clamped-zero seams", file=sys.stderr)

    # Pre-compute FR ranks: for each surah i, sorted list of (rank, neighbor, distance)
    def rank_j_in_i_neighbors(i_one, j_one):
        """Return rank of Q_j in Q_i's nearest-neighbor list (1 = nearest)."""
        i, j = i_one - 1, j_one - 1
        row = list(D[i])
        # Exclude self
        d_ij = row[j]
        # rank = 1 + count of neighbors with strictly smaller distance, ignoring self
        rank = 1
        for k in range(n):
            if k == i or k == j:
                continue
            if row[k] < d_ij:
                rank += 1
        return rank

    # Build 113-row table
    rows = []
    for n_a in range(1, 114):
        n_b = n_a + 1
        words_a = v1_words[n_a]
        words_b = v1_words[n_b]

        A = axis_A_flags[n_a]
        B = axis_B(words_a, words_b)
        cls_a = opener_class_strict(words_a)
        cls_b = opener_class_strict(words_b)
        C_strict = axis_C_strict_match(cls_a, cls_b)
        C_loose = axis_C_loose_match(cls_a, cls_b)

        rank_b_in_a = rank_j_in_i_neighbors(n_a, n_b)
        rank_a_in_b = rank_j_in_i_neighbors(n_b, n_a)
        D_flag = (rank_b_in_a <= 15) and (rank_a_in_b <= 15)

        opening_linked = (A or B or C_strict)
        signature = opening_linked and (not D_flag)

        rows.append({
            "n": n_a,
            "np1": n_b,
            "v1_n": " ".join(words_a[:5]),
            "v1_np1": " ".join(words_b[:5]),
            "A_clamped_zero_seam": A,
            "B_morph_iso_first3": B,
            "C_strict_opener_subclass": C_strict,
            "C_loose_opener_class": C_loose,
            "opener_class_n": list(cls_a),
            "opener_class_np1": list(cls_b),
            "rank_np1_in_n": rank_b_in_a,
            "rank_n_in_np1": rank_a_in_b,
            "D_mutual_top15": D_flag,
            "opening_linked": opening_linked,
            "signature_opening_linked_content_divergent": signature,
            "fr_distance": D[n_a - 1][n_b - 1],
        })

    # Counts
    n_A = sum(1 for r in rows if r["A_clamped_zero_seam"])
    n_B = sum(1 for r in rows if r["B_morph_iso_first3"])
    n_C_strict = sum(1 for r in rows if r["C_strict_opener_subclass"])
    n_C_loose = sum(1 for r in rows if r["C_loose_opener_class"])
    n_D_false = sum(1 for r in rows if not r["D_mutual_top15"])
    n_opening_linked = sum(1 for r in rows if r["opening_linked"])
    n_signature = sum(1 for r in rows if r["signature_opening_linked_content_divergent"])

    p_A = n_A / 113
    p_B = n_B / 113
    p_C_strict = n_C_strict / 113
    p_D_false = n_D_false / 113

    # Expected under independence:
    p_opening_linked = 1 - (1 - p_A) * (1 - p_B) * (1 - p_C_strict)
    p_signature_expected = p_opening_linked * p_D_false
    expected_count = 113 * p_signature_expected
    ratio = (n_signature / expected_count) if expected_count > 0 else float("inf")

    # Verdict
    if n_signature == 0:
        verdict = "PRE-COMMIT VIOLATION (seed Q73-Q74 not recovered)"
    elif n_signature == 1:
        verdict = "NULL (corpus-singleton; Q073-F-02 reframed as observation-only)"
    elif n_signature == 2:
        verdict = "PARTIAL (signature exists but below class threshold of 3)"
    elif n_signature >= 3 and ratio >= 1.5:
        verdict = "PASS-DIRECTED (OPENING-LINKED CONTENT-DIVERGENT class established)"
    elif n_signature >= 3:
        verdict = "DIRECTIONAL (signature exists but at chance level given marginals)"
    else:
        verdict = "UNDEFINED"

    # Signature pairs
    signature_pairs = [
        {"n": r["n"], "np1": r["np1"], "A": r["A_clamped_zero_seam"],
         "B": r["B_morph_iso_first3"], "C_strict": r["C_strict_opener_subclass"],
         "C_loose": r["C_loose_opener_class"], "rank_np1_in_n": r["rank_np1_in_n"],
         "rank_n_in_np1": r["rank_n_in_np1"], "v1_n": r["v1_n"], "v1_np1": r["v1_np1"]}
        for r in rows if r["signature_opening_linked_content_divergent"]
    ]

    out = {
        "test_id": "H-NEW-1390",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "title": "OPENING-LINKED CONTENT-DIVERGENT mushaf-adjacent pair corpus scan",
        "n_pairs_scanned": 113,
        "marginals": {
            "n_A_clamped_zero": n_A,
            "n_B_morph_iso": n_B,
            "n_C_strict_opener_subclass": n_C_strict,
            "n_C_loose_opener_class": n_C_loose,
            "n_D_false": n_D_false,
            "n_opening_linked": n_opening_linked,
            "p_A": p_A,
            "p_B": p_B,
            "p_C_strict": p_C_strict,
            "p_D_false": p_D_false,
            "p_opening_linked": p_opening_linked,
        },
        "expected_signature_under_independence": {
            "p_signature_expected": p_signature_expected,
            "expected_count": expected_count,
        },
        "observed_signature_count": n_signature,
        "ratio_observed_to_expected": ratio,
        "verdict": verdict,
        "signature_pairs": signature_pairs,
        "all_rows": rows,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))

    # Console summary
    print(f"\n=== H-NEW-1390 RESULTS ===")
    print(f"Marginals (of 113 mushaf-adjacent pairs):")
    print(f"  A clamped-zero seam: {n_A} (p={p_A:.4f})")
    print(f"  B morph-iso first 3 words: {n_B} (p={p_B:.4f})")
    print(f"  C strict opener subclass match: {n_C_strict} (p={p_C_strict:.4f})")
    print(f"  C loose opener class match: {n_C_loose}")
    print(f"  D mutual top-15: {113-n_D_false} TRUE / {n_D_false} FALSE (p_D_FALSE={p_D_false:.4f})")
    print(f"  Opening-linked (A∨B∨C_strict): {n_opening_linked}")
    print(f"\nExpected joint signature under independence: {expected_count:.4f}")
    print(f"Observed joint signature count: {n_signature}")
    print(f"Ratio observed/expected: {ratio:.4f}")
    print(f"\nSignature pairs:")
    for sp in signature_pairs:
        print(f"  Q{sp['n']}→Q{sp['np1']}: A={sp['A']}, B={sp['B']}, C_strict={sp['C_strict']}, "
              f"rank_np1_in_n={sp['rank_np1_in_n']}, rank_n_in_np1={sp['rank_n_in_np1']}")
        print(f"    {sp['v1_n']}  |  {sp['v1_np1']}")
    print(f"\nVerdict: {verdict}")
    print(f"\nWritten to: {OUT}")


if __name__ == "__main__":
    main()
