#!/usr/bin/env python3
"""H-NEW-750: per-surah iʿjāz-signature ranking.

Methodology:
  Measure A (global): z(rhyme_entropy) − z(mean_content_distance_to_others)
  Measure B (local):  z(rhyme_entropy) + z(local_cohesion = 1/d̄(s, mushaf neighbors ±2))

Both use:
  - Content distance: H-NEW-111 Fisher-Rao D matrix
  - Rhyme: per-surah Shannon entropy (nats) of verse-final-letter distribution
           on the canonical 28-letter Arabic basis (H-NEW-700 normalization).
"""
import hashlib
import json
import math
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN_NO_TASH = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-750-per-surah-iʿjāz-signature-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-750.json"
EXPECTED_PREREG_SHA = "766439fa44444bca5573929085cec998d6409c25e7f91a9481a840ae239b4e88"

SEED = 20260445

# ---------- Rhyme letter normalization (H-NEW-700 conventions) ----------
ARABIC_LETTERS = [
    "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر",
    "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف",
    "ق", "ك", "ل", "م", "ن", "ه", "و", "ي",
]
LETTER_INDEX = {ch: i for i, ch in enumerate(ARABIC_LETTERS)}

VARIANT_MAP = {
    "ى": "ي",
    "ة": "ه",
    "أ": "ا", "إ": "ا", "آ": "ا",
    "ؤ": "و",
    "ئ": "ي",
    "ٱ": "ا",
}

DIACRITICS_RANGES = [
    (0x0610, 0x061A),
    (0x064B, 0x065F),
    (0x0670, 0x0670),
    (0x06D6, 0x06DC),
    (0x06DF, 0x06E4),
    (0x06E7, 0x06E8),
    (0x06EA, 0x06ED),
]
ORNAMENTS = set("ـۛۖۚۗۘۙۜۥۭۧۤ")


def is_diacritic(cp):
    for lo, hi in DIACRITICS_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def strip_diacritics_and_ornaments(s):
    out = []
    for ch in s:
        if is_diacritic(ord(ch)):
            continue
        if ch in ORNAMENTS:
            continue
        out.append(ch)
    return "".join(out)


def normalize_letter(ch):
    return VARIANT_MAP.get(ch, ch)


def get_final_letter(text):
    cleaned = strip_diacritics_and_ornaments(text).strip()
    while cleaned and not (("ء" <= cleaned[-1] <= "ي") or cleaned[-1] in "ىةؤئٱآأإ"):
        cleaned = cleaned[:-1]
    if not cleaned:
        return None
    last = cleaned[-1]
    last = normalize_letter(last)
    if last in LETTER_INDEX:
        return last
    return None


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_D():
    with open(H_NEW_111) as f:
        d = json.load(f)
    # 1-indexed [1..114], skip [0]
    mat = [[0.0] * 115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist
        mat[j][i] = dist
    return mat


def shannon_entropy_nats(counts):
    total = sum(counts)
    if total == 0:
        return 0.0
    H = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            H -= p * math.log(p)
    return H


def zscore(arr):
    n = len(arr)
    m = sum(arr) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in arr) / n)
    if sd < 1e-15:
        return [0.0] * n
    return [(x - m) / sd for x in arr]


def spearman_rho(x, y):
    def ranks(v):
        sorted_pairs = sorted(enumerate(v), key=lambda p: p[1])
        r = [0] * len(v)
        i = 0
        while i < len(sorted_pairs):
            j = i
            while j + 1 < len(sorted_pairs) and sorted_pairs[j + 1][1] == sorted_pairs[i][1]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[sorted_pairs[k][0]] = avg_rank
            i = j + 1
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(rx)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx > 0 and dy > 0 else 0.0


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-750: per-surah iʿjāz-signature ===")
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print("WARNING: prereg SHA mismatch!")
    print(f"Seed: {SEED}\n")

    # --- Load Quran text and compute per-surah final-letter distributions ---
    with open(QURAN_NO_TASH) as f:
        quran = json.load(f)
    assert len(quran) == 114, f"expected 114 surahs, got {len(quran)}"

    rhyme_entropy = [0.0] * 115  # 1-indexed
    n_verses = [0] * 115
    final_letter_counts = [None] * 115
    top_letter_per_surah = [None] * 115

    for surah in quran:
        sid = surah["id"]
        verses = surah["verses"]
        # For surah 1, the H-NEW-700 convention treated basmala-counted-only-in-surah-1
        # We follow same: use all verses as listed (basmala is verse 1 of Q1 only here).
        counts = [0] * 28
        for v in verses:
            fl = get_final_letter(v["text"])
            if fl is not None:
                counts[LETTER_INDEX[fl]] += 1
        rhyme_entropy[sid] = shannon_entropy_nats(counts)
        n_verses[sid] = len(verses)
        final_letter_counts[sid] = counts
        if sum(counts) > 0:
            top_idx = max(range(28), key=lambda i: counts[i])
            top_letter_per_surah[sid] = (ARABIC_LETTERS[top_idx], counts[top_idx] / sum(counts))

    # --- Load content distance matrix ---
    D = load_D()

    # --- Measure A: mean content distance to all other surahs ---
    mean_content_distance = [0.0] * 115
    for s in range(1, 115):
        d_sum = 0.0
        n = 0
        for i in range(1, 115):
            if i == s:
                continue
            d_sum += D[s][i]
            n += 1
        mean_content_distance[s] = d_sum / n

    # --- Measure B: local mushaf-neighborhood cohesion (±2) ---
    local_cohesion = [0.0] * 115
    for s in range(1, 115):
        neighbors = [s + k for k in (-2, -1, 1, 2) if 1 <= s + k <= 114]
        d_sum = sum(D[s][n] for n in neighbors)
        d_mean = d_sum / len(neighbors)
        # Higher = more locally-cohesive (smaller distance)
        local_cohesion[s] = 1.0 / d_mean if d_mean > 1e-15 else 0.0

    # --- Z-scores on the 1..114 vector ---
    rh = [rhyme_entropy[s] for s in range(1, 115)]
    mc = [mean_content_distance[s] for s in range(1, 115)]
    lc = [local_cohesion[s] for s in range(1, 115)]
    z_rh = zscore(rh)
    z_mc = zscore(mc)
    z_lc = zscore(lc)

    # --- iʿjāz signatures ---
    # A: z(rhyme_entropy) − z(mean_content_distance)  HIGH = content-central + rhyme-diverse
    sig_A = [z_rh[i] - z_mc[i] for i in range(114)]
    # B: z(rhyme_entropy) + z(local_cohesion)
    sig_B = [z_rh[i] + z_lc[i] for i in range(114)]

    # --- Rankings ---
    surah_ids = list(range(1, 115))
    rank_A = sorted(range(114), key=lambda i: -sig_A[i])  # 0 = highest signature
    rank_B = sorted(range(114), key=lambda i: -sig_B[i])

    rank_A_pos = [0] * 115
    rank_B_pos = [0] * 115
    for r, idx in enumerate(rank_A):
        rank_A_pos[surah_ids[idx]] = r + 1  # 1-indexed
    for r, idx in enumerate(rank_B):
        rank_B_pos[surah_ids[idx]] = r + 1

    # --- Cross-measure consistency ---
    rho_AB = spearman_rho(sig_A, sig_B)
    print(f"--- Cross-measure consistency ---")
    print(f"  Spearman ρ(rank_A, rank_B) = {rho_AB:+.4f}")

    # --- Top/bottom 10 ---
    print(f"\n--- TOP-10 by Measure A (global content-distance) ---")
    for r in range(10):
        i = rank_A[r]
        sid = surah_ids[i]
        print(f"  #{r+1}: Q{sid:3d} | sig_A={sig_A[i]:+.3f} | rh_ent={rh[i]:.3f} | mc_dist={mc[i]:.4f} | n_v={n_verses[sid]:4d}")

    print(f"\n--- BOTTOM-10 by Measure A ---")
    for r in range(10):
        i = rank_A[-(r + 1)]
        sid = surah_ids[i]
        print(f"  #{114 - r}: Q{sid:3d} | sig_A={sig_A[i]:+.3f} | rh_ent={rh[i]:.3f} | mc_dist={mc[i]:.4f} | n_v={n_verses[sid]:4d}")

    print(f"\n--- TOP-10 by Measure B (local cohesion) ---")
    for r in range(10):
        i = rank_B[r]
        sid = surah_ids[i]
        print(f"  #{r+1}: Q{sid:3d} | sig_B={sig_B[i]:+.3f} | rh_ent={rh[i]:.3f} | local_coh={lc[i]:.3f} | n_v={n_verses[sid]:4d}")

    print(f"\n--- BOTTOM-10 by Measure B ---")
    for r in range(10):
        i = rank_B[-(r + 1)]
        sid = surah_ids[i]
        print(f"  #{114 - r}: Q{sid:3d} | sig_B={sig_B[i]:+.3f} | rh_ent={rh[i]:.3f} | local_coh={lc[i]:.3f} | n_v={n_verses[sid]:4d}")

    # --- Pre-committed predictions ---
    print(f"\n--- PRE-COMMIT PREDICTIONS ---")
    predictions = [
        ("Q 112 al-Ikhlāṣ", 112, "top-5", "top-5", lambda r: r <= 5, lambda r: r <= 5),
        ("Q 113 al-Falaq",  113, "top-15", "top-15", lambda r: r <= 15, lambda r: r <= 15),
        ("Q 114 al-Nās",    114, "top-15", "top-15", lambda r: r <= 15, lambda r: r <= 15),
        ("Q 1 al-Fātiḥa",     1, "top-30", "top-30", lambda r: r <= 30, lambda r: r <= 30),
        ("Q 2 al-Baqara",     2, "bottom-15", "bottom-15", lambda r: r >= 100, lambda r: r >= 100),
        ("Q 33 al-Aḥzāb",    33, "bottom-30", "bottom-30", lambda r: r >= 85, lambda r: r >= 85),
    ]
    n_hits_A = 0
    n_hits_B = 0
    n_hits_either = 0
    pred_results = []
    for label, sid, pred_a, pred_b, fa, fb in predictions:
        ra = rank_A_pos[sid]
        rb = rank_B_pos[sid]
        hit_a = fa(ra)
        hit_b = fb(rb)
        hit_either = hit_a or hit_b
        if hit_a:
            n_hits_A += 1
        if hit_b:
            n_hits_B += 1
        if hit_either:
            n_hits_either += 1
        marker_a = "HIT" if hit_a else "MISS"
        marker_b = "HIT" if hit_b else "MISS"
        marker_e = "HIT" if hit_either else "MISS"
        print(f"  {label:20s} | A: rank {ra:3d} ({pred_a}) [{marker_a}] | B: rank {rb:3d} ({pred_b}) [{marker_b}] | EITHER: [{marker_e}]")
        pred_results.append({
            "label": label, "surah": sid,
            "rank_A": ra, "pred_A": pred_a, "hit_A": hit_a,
            "rank_B": rb, "pred_B": pred_b, "hit_B": hit_b,
            "hit_either": hit_either,
        })

    print(f"\n  Hits-A: {n_hits_A}/6  Hits-B: {n_hits_B}/6  Hits-EITHER: {n_hits_either}/6")

    # --- Verdict ---
    if n_hits_either >= 4 and rho_AB >= 0.5:
        verdict = f"STRICT PASS — {n_hits_either}/6 predictions hit (EITHER); cross-measure ρ={rho_AB:+.4f}"
    elif n_hits_either >= 3 and rho_AB >= 0.3:
        verdict = f"DIRECTIONAL — {n_hits_either}/6 predictions hit; cross-measure ρ={rho_AB:+.4f}"
    else:
        verdict = f"NULL/WEAK — {n_hits_either}/6 predictions hit; cross-measure ρ={rho_AB:+.4f}"
    print(f"\n=== VERDICT: {verdict} ===")

    # --- Build per-surah table for output ---
    per_surah = []
    for i, sid in enumerate(surah_ids):
        entry = {
            "surah": sid,
            "n_verses": n_verses[sid],
            "rhyme_entropy_nats": rh[i],
            "top_final_letter": top_letter_per_surah[sid][0] if top_letter_per_surah[sid] else None,
            "top_final_letter_frac": top_letter_per_surah[sid][1] if top_letter_per_surah[sid] else None,
            "mean_content_distance": mc[i],
            "local_cohesion": lc[i],
            "z_rhyme_entropy": z_rh[i],
            "z_mean_content_distance": z_mc[i],
            "z_local_cohesion": z_lc[i],
            "sig_A": sig_A[i],
            "sig_B": sig_B[i],
            "rank_A": rank_A_pos[sid],
            "rank_B": rank_B_pos[sid],
        }
        per_surah.append(entry)

    out = {
        "id": "H-NEW-750",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "rules_tuple": [
            "no-tashkeel", "QAC-STEM root tokens", "QAC v0.4",
            "basmala-counted-only-in-surah-1", "mushaf order", "Hafs-Kufan",
            "28-letter Arabic rhyme basis (H-NEW-700 normalization)",
        ],
        "n_surahs": 114,
        "per_surah": per_surah,
        "top10_A": [{"rank": r + 1, "surah": surah_ids[rank_A[r]], "sig_A": sig_A[rank_A[r]]} for r in range(10)],
        "bottom10_A": [{"rank": 114 - r, "surah": surah_ids[rank_A[-(r + 1)]], "sig_A": sig_A[rank_A[-(r + 1)]]} for r in range(10)],
        "top10_B": [{"rank": r + 1, "surah": surah_ids[rank_B[r]], "sig_B": sig_B[rank_B[r]]} for r in range(10)],
        "bottom10_B": [{"rank": 114 - r, "surah": surah_ids[rank_B[-(r + 1)]], "sig_B": sig_B[rank_B[-(r + 1)]]} for r in range(10)],
        "spearman_rho_A_B": rho_AB,
        "predictions": pred_results,
        "n_hits_A": n_hits_A,
        "n_hits_B": n_hits_B,
        "n_hits_either": n_hits_either,
        "alpha_bon": 0.025,
        "bonferroni_k": 2,
        "verdict": verdict,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
