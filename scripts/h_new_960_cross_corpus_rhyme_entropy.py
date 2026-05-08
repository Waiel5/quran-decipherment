#!/usr/bin/env python3
"""H-NEW-960: Cross-corpus rhyme-letter Shannon-entropy distinctness test.

Per-surah Quran rhyme-letter Shannon entropy vs matched-length pre-Islamic
poetry block rhyme-letter Shannon entropy. Wilcoxon paired (one-sided LOWER),
Bonferroni-4 on verse-length quartiles, 10000 bootstrap.

Methodology:
- Quran (114 surahs): for each surah, last orthographic letter of each verse,
  normalized to 28-letter alphabet (per H-NEW-740 normalization rules);
  Shannon entropy H(Q_s) = -Σ p_i log2(p_i).
- Pre-Islamic poetry: 7 muʿallaqāt + 6 dīwāns from data/baseline-corpora/raw/.
  Bayt-line filter via H-NEW-740's `looks_like_bayt()` heuristic. Concatenated
  bayt-line stream PER QĀFIYA-SECTION preserves contiguity & monorhyme.
- For each surah of length V_s, sample one matched-length poetry block:
  - prefer same-length window WITHIN a qāfiya-section (preserves natural
    monorhyme unit)
  - if V_s > max-section-size, fall back to V_s contiguous bayts in the
    concatenated all-poetry stream (cross-section permitted; bias direction
    documented in pre-reg §4.4)
- Wilcoxon signed-rank paired, ONE-SIDED H1: H(Q) < H(P)
- Quartile (H2): VS<5, 5-10, 11-20, >20 verses; α_bon = 0.0125 each
- Bootstrap CI on mean(Δ) and means

Pre-reg: findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy-prereg.md
SHA-locked at runtime; fail-fast on mismatch.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
RAW = ROOT / "data/baseline-corpora/raw"
QURAN_MIN = ROOT / "quran-text/quran-min-tashkeel.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-960.json"
EXPECTED_PREREG_SHA = "332cb8293bbd50a2949fe5cd3a61137ef2e6c5225b167dfe9711e1a4353b1f19"

SEED = 20260507
N_BOOTSTRAP = 10000

MUALLAQAT = [
    "muallaqa-imru-al-qais.txt",
    "muallaqa-tarafa.txt",
    "muallaqa-zuhayr.txt",
    "muallaqa-labid.txt",
    "muallaqa-amr-bin-kulthum.txt",
    "muallaqa-antara.txt",
    "muallaqa-harith.txt",
]
DIWANS = [
    "diwan-imru-al-qais.txt",
    "diwan-tarafa.txt",
    "diwan-labid.txt",
    "diwan-antara.txt",
    "diwan-zuhayr.txt",
    "diwan-harith.txt",
]

ARABIC_LETTERS = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
LETTER_INDEX = {ch: i for i, ch in enumerate(ARABIC_LETTERS)}
VARIANT_MAP = {
    "ى": "ي", "ة": "ه",
    "أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا",
    "ؤ": "و", "ئ": "ي",
}
DIACRITICS_RANGES = [
    (0x0610, 0x061A), (0x064B, 0x065F),
    (0x0670, 0x0670), (0x06D6, 0x06DC),
    (0x06DF, 0x06E4), (0x06E7, 0x06E8),
    (0x06EA, 0x06ED),
]
ORNAMENTS = set("ـۛۖۚۗۘۙۜۥۭۧۤ")


# ----------------------------------------------------------------------
# Letter normalization / final-letter extraction (cloned from H-NEW-740)
# ----------------------------------------------------------------------

def is_diacritic(cp):
    for lo, hi in DIACRITICS_RANGES:
        if lo <= cp <= hi:
            return True
    return False


def strip_diacritics(s):
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


def is_arabic_letter(ch):
    return ("ء" <= ch <= "ي") or ch in "ىةؤئٱآأإ"


def get_final_letter(text):
    cleaned = strip_diacritics(text).strip()
    cleaned = re.sub(r"\s*\([0-9]+\)\s*$", "", cleaned)
    cleaned = re.sub(r"\s+\d+\s*$", "", cleaned)
    cleaned = cleaned.rstrip()
    while cleaned and not is_arabic_letter(cleaned[-1]):
        cleaned = cleaned[:-1]
    if not cleaned:
        return None
    last = normalize_letter(cleaned[-1])
    return last if last in LETTER_INDEX else None


# ----------------------------------------------------------------------
# Bayt-line heuristic (cloned from H-NEW-740)
# ----------------------------------------------------------------------

def looks_like_bayt(line):
    s = line.strip()
    if not s:
        return False
    s_no_num = re.sub(r"\s*\(?[0-9]+\)?\s*$", "", s).strip()
    arabic_word_re = re.compile(r"[؀-ۿ]+")
    words = arabic_word_re.findall(s_no_num)
    if len(words) < 6:
        return False
    nospace = re.sub(r"\s", "", s_no_num)
    if not nospace:
        return False
    arabic_chars = sum(1 for ch in nospace if "؀" <= ch <= "ۿ")
    if arabic_chars / len(nospace) < 0.7:
        return False
    if re.search(r"\([0-9]+\)\s*$", s) or re.search(r"\s\d+\s*$", s):
        return True
    if "..." in s_no_num:
        return True
    if re.search(r"^(قال|وقال|فقال|يقول|روى|يروى|روي|اعتنى|الناشر|الطبعة|المؤلف|أعده|بسم|قافية|البحر|^أ-)", s):
        return False
    if re.search(r":", s):
        return False
    if re.search(r"#####|----|AUTO\s|\bمات\b|\bتوفي\b|\bالميلاد\b|\bالناشر\b", s):
        return False
    if len(words) >= 8:
        return True
    return False


def parse_qafiya_sections(lines):
    """Return list of (qafiya_label, [bayt_line]) preserving section order."""
    qafiya_re = re.compile(r"^قافية\s+(\S+)")
    sections = []
    cur_label = "default"
    cur_bayts = []
    for ln in lines:
        m = qafiya_re.match(ln.strip())
        if m:
            if cur_bayts:
                sections.append((cur_label, cur_bayts))
            cur_label = m.group(1)
            cur_bayts = []
            continue
        if looks_like_bayt(ln):
            cur_bayts.append(ln)
    if cur_bayts:
        sections.append((cur_label, cur_bayts))
    return sections


# ----------------------------------------------------------------------
# Shannon entropy
# ----------------------------------------------------------------------

def shannon_entropy_bits(letter_counts):
    total = sum(letter_counts)
    if total <= 0:
        return float("nan")
    h = 0.0
    for c in letter_counts:
        if c > 0:
            p = c / total
            h -= p * math.log2(p)
    return h


def letter_counts_from_finals(finals):
    v = [0] * 28
    for ch in finals:
        if ch in LETTER_INDEX:
            v[LETTER_INDEX[ch]] += 1
    return v


# ----------------------------------------------------------------------
# Wilcoxon signed-rank (one-sided, paired, with mid-rank ties)
# ----------------------------------------------------------------------

def wilcoxon_signed_rank_one_sided_lower(diffs):
    """Return (W_minus, p_one_sided_normal_approx).

    Test: H1 mean(diffs) < 0, where diffs = H(Q) - H(P).
    Following the standard Wilcoxon formulation:
      - drop zero diffs
      - rank |diffs| with mid-ranks for ties
      - W+ = sum of ranks where diff > 0
      - W- = sum of ranks where diff < 0
      - For LOWER alternative (Q < P), expect W- > W+
      - z = (W+ - mean) / sd, where mean = n(n+1)/4, sd² = n(n+1)(2n+1)/24
        (with tie correction)
      - p = Phi(z)  [one-sided, smaller W+ → smaller p]
    """
    nz = [d for d in diffs if d != 0.0]
    n = len(nz)
    if n == 0:
        return {"n_nonzero": 0, "W_plus": 0.0, "W_minus": 0.0,
                "z": float("nan"), "p_one_sided_lower": float("nan")}
    abs_d = [abs(d) for d in nz]
    # rank with mid-ranks
    indexed = sorted(range(n), key=lambda i: abs_d[i])
    ranks = [0.0] * n
    i = 0
    tie_groups = []
    while i < n:
        j = i
        while j + 1 < n and abs_d[indexed[j + 1]] == abs_d[indexed[i]]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg_rank
        if j > i:
            tie_groups.append(j - i + 1)
        i = j + 1
    W_plus = sum(ranks[k] for k in range(n) if nz[k] > 0)
    W_minus = sum(ranks[k] for k in range(n) if nz[k] < 0)
    mean_w = n * (n + 1) / 4.0
    var_w = n * (n + 1) * (2 * n + 1) / 24.0
    # tie correction
    tie_term = sum(t * (t * t - 1) for t in tie_groups) / 48.0
    var_w -= tie_term
    if var_w <= 0:
        z = float("nan")
        p_lower = float("nan")
    else:
        sd_w = math.sqrt(var_w)
        # continuity correction: shift toward mean by 0.5
        # H1: lower alternative → W+ small → z negative
        # use z = (W+ - mean + 0.5) / sd  for lower-tail p
        if W_plus < mean_w:
            z = (W_plus + 0.5 - mean_w) / sd_w
        else:
            z = (W_plus - 0.5 - mean_w) / sd_w
        # Phi(z) = 0.5 * (1 + erf(z/sqrt(2)))
        p_lower = 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
    return {"n_nonzero": n, "W_plus": W_plus, "W_minus": W_minus,
            "z": z, "p_one_sided_lower": p_lower}


# ----------------------------------------------------------------------
# Bootstrap
# ----------------------------------------------------------------------

def bootstrap_paired(qs, ps, n_reps, rng):
    """Bootstrap (paired) means and Δ. Returns dict with means, deltas, CIs."""
    n = len(qs)
    deltas = [qs[i] - ps[i] for i in range(n)]
    boot_q = []
    boot_p = []
    boot_d = []
    for _ in range(n_reps):
        idxs = [rng.randrange(n) for _ in range(n)]
        bq = sum(qs[i] for i in idxs) / n
        bp = sum(ps[i] for i in idxs) / n
        bd = sum(deltas[i] for i in idxs) / n
        boot_q.append(bq)
        boot_p.append(bp)
        boot_d.append(bd)
    boot_q.sort()
    boot_p.sort()
    boot_d.sort()
    def pct(arr, q):
        i = int(q * (len(arr) - 1))
        return arr[i]
    return {
        "n_reps": n_reps,
        "mean_Q": sum(qs) / n,
        "mean_P": sum(ps) / n,
        "mean_delta": sum(deltas) / n,
        "Q_ci95": [pct(boot_q, 0.025), pct(boot_q, 0.975)],
        "P_ci95": [pct(boot_p, 0.025), pct(boot_p, 0.975)],
        "delta_ci95": [pct(boot_d, 0.025), pct(boot_d, 0.975)],
        "frac_delta_below_0": sum(1 for x in boot_d if x < 0) / len(boot_d),
    }


# ----------------------------------------------------------------------
# Sampling matched-length poetry blocks
# ----------------------------------------------------------------------

def sample_matched_block(V, sections_with_meta, full_stream, rng):
    """Return finals[] of length V, sampling rule:
       1. Try to find a section with size >= V; pick a uniform-random
          contiguous window of length V within that section.
       2. If no section has >= V bayts, fall back to a contiguous window of
          length V across the full concatenated bayt stream
          (cross-section, cross-source). Document via cross_section flag.
    """
    candidates = [(label, src, finals)
                  for (label, src, finals) in sections_with_meta
                  if len(finals) >= V]
    if candidates:
        # choose section uniformly at random
        label, src, finals = candidates[rng.randrange(len(candidates))]
        max_start = len(finals) - V
        start = rng.randint(0, max_start)
        return {"finals": finals[start:start + V],
                "section": label, "source": src,
                "cross_section": False, "start": start}
    # fallback: full stream
    if len(full_stream) < V:
        return None
    max_start = len(full_stream) - V
    start = rng.randint(0, max_start)
    return {"finals": full_stream[start:start + V],
            "section": "MULTI", "source": "MULTI",
            "cross_section": True, "start": start}


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    print("=== H-NEW-960: Cross-corpus rhyme-letter Shannon-entropy distinctness ===",
          flush=True)
    actual_sha = sha(PREREG)
    print(f"Pre-reg SHA: {actual_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if actual_sha != EXPECTED_PREREG_SHA:
        print("!!! SHA MISMATCH — abort", file=sys.stderr)
        sys.exit(1)
    print(f"Seed: {SEED}")
    print(f"N_BOOTSTRAP: {N_BOOTSTRAP}\n")

    # -------- Quran loading --------
    print("=== Loading Quran (min-tashkeel) ===")
    quran = json.load(open(QURAN_MIN))
    assert len(quran) == 114, f"expected 114 surahs, got {len(quran)}"
    quran_records = []  # list of dict: surah, V, finals, entropy, top_letter, top_frac
    for surah_obj in quran:
        sid = surah_obj["id"]
        verses = surah_obj["verses"]
        V = len(verses)
        finals = []
        for v in verses:
            f = get_final_letter(v["text"])
            if f is not None:
                finals.append(f)
        counts = letter_counts_from_finals(finals)
        H = shannon_entropy_bits(counts)
        # diagnostics
        n = sum(counts)
        top_idx = max(range(28), key=lambda i: counts[i]) if n > 0 else None
        quran_records.append({
            "surah": sid,
            "V": V,
            "n_finals_used": len(finals),
            "H_bits": H,
            "top_letter": ARABIC_LETTERS[top_idx] if top_idx is not None else None,
            "top_frac": counts[top_idx] / n if n > 0 else float("nan"),
        })
    print(f"  Loaded 114 surahs; total verses across mushaf: {sum(r['V'] for r in quran_records)}")
    H_quran_mean = sum(r["H_bits"] for r in quran_records) / 114
    print(f"  Mean Quran rhyme-letter entropy: {H_quran_mean:.4f} bits")
    print(f"  Min: Q{min(quran_records, key=lambda r: r['H_bits'])['surah']} "
          f"= {min(r['H_bits'] for r in quran_records):.4f}")
    print(f"  Max: Q{max(quran_records, key=lambda r: r['H_bits'])['surah']} "
          f"= {max(r['H_bits'] for r in quran_records):.4f}")

    # -------- Poetry loading --------
    print("\n=== Loading pre-Islamic poetry corpus ===")
    sections_with_meta = []  # list of (qafiya_label, source, [finals])
    full_stream = []  # concatenated finals across whole corpus
    sources_loaded = []
    total_bayts = 0
    for fname in MUALLAQAT + DIWANS:
        path = RAW / fname
        if not path.exists():
            print(f"  MISSING: {fname}", flush=True)
            continue
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        sections = parse_qafiya_sections(lines)
        n_sect_added = 0
        n_bayts_added = 0
        for label, bayts in sections:
            finals = []
            for ln in bayts:
                fl = get_final_letter(ln)
                if fl is not None:
                    finals.append(fl)
            if len(finals) >= 5:  # require minimal section size to be useful
                sections_with_meta.append(
                    (label, fname.replace(".txt", ""), finals))
                full_stream.extend(finals)
                n_sect_added += 1
                n_bayts_added += len(finals)
        sources_loaded.append({
            "file": fname,
            "sections_kept": n_sect_added,
            "bayts_kept": n_bayts_added,
        })
        total_bayts += n_bayts_added
        print(f"  {fname}: {n_sect_added} sections, {n_bayts_added} bayts kept")
    print(f"  TOTAL: {len(sections_with_meta)} sections, "
          f"{total_bayts} bayts across {len(sources_loaded)} files")
    print(f"  full_stream len: {len(full_stream)}")
    section_sizes = sorted((len(f) for (_, _, f) in sections_with_meta), reverse=True)
    print(f"  Largest sections: {section_sizes[:10]}")
    print(f"  Total sections >=5: {len(sections_with_meta)}")

    # Data-gap check
    if total_bayts < 1000:
        print(f"\n!!! NULL-DATA-GAP: only {total_bayts} bayts — pre-reg threshold not met", flush=True)
        # still emit Q-only
        out = {
            "id": "H-NEW-960",
            "prereg_sha": actual_sha,
            "seed": SEED,
            "status": "NULL-DATA-GAP",
            "n_poetry_bayts": total_bayts,
            "quran_only": {
                "mean_H_bits": H_quran_mean,
                "records": quran_records,
            },
        }
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        with open(OUT_JSON, "w") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
        print(f"Wrote {OUT_JSON}")
        return

    # -------- Matched-length sampling --------
    print("\n=== Matched-length poetry block sampling ===")
    rng = random.Random(SEED)
    paired = []
    cross_section_count = 0
    failures = []
    for r in quran_records:
        V = r["V"]
        sample = sample_matched_block(V, sections_with_meta, full_stream, rng)
        if sample is None:
            failures.append({"surah": r["surah"], "V": V, "reason": "stream_too_short"})
            continue
        if sample["cross_section"]:
            cross_section_count += 1
        # entropy
        cnt = letter_counts_from_finals(sample["finals"])
        Hp = shannon_entropy_bits(cnt)
        n_p = sum(cnt)
        top_idx = max(range(28), key=lambda i: cnt[i]) if n_p > 0 else None
        paired.append({
            "surah": r["surah"],
            "V": V,
            "H_quran_bits": r["H_bits"],
            "H_poetry_bits": Hp,
            "delta": r["H_bits"] - Hp,
            "poetry_section": sample["section"],
            "poetry_source": sample["source"],
            "poetry_cross_section": sample["cross_section"],
            "poetry_start": sample["start"],
            "quran_top_letter": r["top_letter"],
            "quran_top_frac": r["top_frac"],
            "poetry_top_letter": ARABIC_LETTERS[top_idx] if top_idx is not None else None,
            "poetry_top_frac": cnt[top_idx] / n_p if n_p > 0 else float("nan"),
        })
    print(f"  Paired {len(paired)} of 114 surahs")
    print(f"  Cross-section fallbacks (V > max-section): {cross_section_count}")
    if failures:
        print(f"  Failures: {failures}")

    # -------- H1 primary test --------
    print("\n=== H1: primary Wilcoxon paired one-sided LOWER ===")
    qs = [p["H_quran_bits"] for p in paired]
    ps = [p["H_poetry_bits"] for p in paired]
    deltas = [p["delta"] for p in paired]
    wilcoxon_h1 = wilcoxon_signed_rank_one_sided_lower(deltas)
    mean_d = sum(deltas) / len(deltas)
    print(f"  N paired: {len(paired)}")
    print(f"  Mean H(Quran) = {sum(qs)/len(qs):.4f} bits")
    print(f"  Mean H(Poetry) = {sum(ps)/len(ps):.4f} bits")
    print(f"  Mean Δ = H(Q) - H(P) = {mean_d:+.4f} bits")
    print(f"  Wilcoxon: n_nonzero={wilcoxon_h1['n_nonzero']}, "
          f"W+={wilcoxon_h1['W_plus']:.1f}, W-={wilcoxon_h1['W_minus']:.1f}")
    print(f"  z = {wilcoxon_h1['z']:.4f}, "
          f"p (one-sided LOWER) = {wilcoxon_h1['p_one_sided_lower']:.6e}")

    # bootstrap
    print("\n=== Bootstrap (paired, 10000 reps) ===")
    boot_rng = random.Random(SEED + 1)
    boot = bootstrap_paired(qs, ps, N_BOOTSTRAP, boot_rng)
    print(f"  Mean Δ = {boot['mean_delta']:+.4f}; 95% CI: "
          f"[{boot['delta_ci95'][0]:+.4f}, {boot['delta_ci95'][1]:+.4f}]")
    print(f"  Frac bootstrap-Δ < 0: {boot['frac_delta_below_0']:.4f}")

    # -------- H2 quartile breakdown --------
    print("\n=== H2: quartile-by-verse-length breakdown ===")
    quartiles = {
        "VS_under_5": [p for p in paired if p["V"] < 5],
        "S_5_to_10":  [p for p in paired if 5 <= p["V"] <= 10],
        "M_11_to_20": [p for p in paired if 11 <= p["V"] <= 20],
        "L_over_20":  [p for p in paired if p["V"] > 20],
    }
    alpha_bon = 0.05 / 4
    quart_results = {}
    n_pass = 0
    for qname, qpairs in quartiles.items():
        n = len(qpairs)
        if n < 5:
            quart_results[qname] = {
                "n": n, "status": "INSUFFICIENT",
                "alpha_bon": alpha_bon, "passes": False,
            }
            print(f"  {qname}: n={n} INSUFFICIENT")
            continue
        d_q = [p["delta"] for p in qpairs]
        wilq = wilcoxon_signed_rank_one_sided_lower(d_q)
        mean_d_q = sum(d_q) / n
        passes = wilq["p_one_sided_lower"] < alpha_bon
        if passes:
            n_pass += 1
        quart_results[qname] = {
            "n": n,
            "mean_H_quran": sum(p["H_quran_bits"] for p in qpairs) / n,
            "mean_H_poetry": sum(p["H_poetry_bits"] for p in qpairs) / n,
            "mean_delta": mean_d_q,
            "wilcoxon": wilq,
            "alpha_bon": alpha_bon,
            "passes": passes,
            "status": "PASS" if passes else "FAIL",
        }
        print(f"  {qname}: n={n}  meanΔ={mean_d_q:+.4f}  "
              f"p={wilq['p_one_sided_lower']:.4e}  "
              f"(α_bon={alpha_bon}) → {'PASS' if passes else 'FAIL'}")
    print(f"  Quartile pass count: {n_pass}/4")

    # -------- Verdict --------
    print("\n=== Verdict ===")
    H1_p = wilcoxon_h1["p_one_sided_lower"]
    if mean_d > 0:
        verdict = "NULL-RESIDUAL-LIVES-IN-COMPOSITE — direction REVERSED (poetry lower-entropy or equal); H-NEW-740 composite distinctness does NOT carry to letter-axis alone"
    elif H1_p < 1e-5 and n_pass == 4:
        verdict = "HIGH-STRENGTH-CONFIRMS — H1 p<10⁻⁵ and H2 4/4 quartiles pass at α_bon"
    elif H1_p < 1e-5 and n_pass >= 3:
        verdict = "CONFIRMS — H1 p<10⁻⁵ and H2 ≥3/4 quartiles pass"
    elif H1_p < 1e-3:
        verdict = "DIRECTIONAL-CONFIRMS"
    elif H1_p < 0.05:
        verdict = "WEAK-DIRECTIONAL"
    else:
        verdict = "DIRECTION-LOCKED-NULL — direction correct but not significant at α=0.05"
    print(f"  {verdict}")

    # -------- Output JSON --------
    out = {
        "id": "H-NEW-960",
        "prereg_sha": actual_sha,
        "seed": SEED,
        "n_bootstrap": N_BOOTSTRAP,
        "alpha_h1": 1e-5,
        "bonferroni_k": 4,
        "alpha_bon": alpha_bon,
        "rules_tuple": "(min-tashkeel, last-orthographic-letter, 28-letter-normalized, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_quran_surahs": 114,
        "n_paired": len(paired),
        "cross_section_fallbacks": cross_section_count,
        "n_poetry_bayts_total": total_bayts,
        "n_poetry_sections": len(sections_with_meta),
        "sources_loaded": sources_loaded,
        "mean_H_quran_bits": sum(qs) / len(qs),
        "mean_H_poetry_bits": sum(ps) / len(ps),
        "mean_delta_bits": mean_d,
        "H1_wilcoxon": wilcoxon_h1,
        "H1_p_one_sided_lower": H1_p,
        "H2_quartiles": quart_results,
        "H2_pass_count": n_pass,
        "bootstrap": boot,
        "paired_records": paired,
        "quran_records": quran_records,
        "verdict": verdict,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
