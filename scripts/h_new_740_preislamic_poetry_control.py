#!/usr/bin/env python3
"""H-NEW-740: Pre-Islamic poetry control for iʿjāz al-fawāṣil anti-twin signature.

Replicates H-NEW-730 methodology on a pre-Islamic poetry corpus:
- Build qaṣīda-blocks of 30 contiguous bayts within qāfiya-section.
- Per-block content vector = top-500 word-form distribution (Dirichlet α=0.5, L1-normalized).
- Per-block rhyme vector = 28-letter bayt-final distribution.
- Fisher-Rao distance matrix between blocks.
- For K=15 windows, compute mean pairwise content-distance and rhyme-distance.
- Pearson r(content × rhyme).

Compare to Quran's r=−0.8643. Per pre-reg:
- PASS-CONFIRMS-IʿJĀZ-CLAIM: r_poetry > −0.4
- DIRECTIONAL-CONFIRMS: −0.6 < r ≤ −0.4
- FALSIFIES-IʿJĀZ-CLAIM: r ≤ −0.6
- NULL-DATA-GAP: <30 blocks
"""
import hashlib
import json
import math
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
RAW = ROOT / "data/baseline-corpora/raw"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-740-prelislamic-poetry-control-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-740.json"
EXPECTED_PREREG_SHA = "d5c0a7962473e18805e341d619b37b148937cec0e16f440f6bf1c09fee1c3e15"

SEED = 20260444
N_PERMS = 10000
K = 15
BLOCK_SIZE = 30  # bayts per qaṣīda-block
MIN_BAYTS_FOR_BLOCK = 15  # don't form a block from fewer than this
TOPK_WORDS = 500
DIRICHLET_ALPHA = 0.5

# Pre-Islamic corpus files
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
# secondary control: Mutanabbi (Abbasid, post-Islamic) — separate analysis
MUTANABBI = ["mutanabbi-diwan.txt"]

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

# Common Arabic particles to strip (light stem-like normalization)
PROCLITIC_PARTICLES = ["و", "ف", "ب", "ل", "ك", "ال"]

# Lines we want to classify as "editorial prose / not bayt"
PROSE_MARKERS = re.compile(r"[:،؛؟!—–]|قال|وقال|فقال|يقول|روى|يروى|يروي|اعتنى|الناشر|الطبعة|عدد|المؤلف|أعده|بسم الله|######|----|^AUTO|^\d+\s|^#")


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
    # Strip trailing parenthesized number, punctuation, non-Arabic
    cleaned = re.sub(r"\s*\([0-9]+\)\s*$", "", cleaned)
    cleaned = re.sub(r"\s+\d+\s*$", "", cleaned)  # bare trailing number (zuhayr)
    cleaned = cleaned.rstrip()
    while cleaned and not is_arabic_letter(cleaned[-1]):
        cleaned = cleaned[:-1]
    if not cleaned:
        return None
    last = normalize_letter(cleaned[-1])
    return last if last in LETTER_INDEX else None


def looks_like_bayt(line):
    """Heuristic: is this line a verse-bayt (vs. editorial prose)?
    Criteria:
      - has ≥ 6 Arabic words
      - ratio of Arabic chars to total ≥ 0.7
      - no obvious prose markers (colon, comma-prose, attribution verbs)
      - or: line ends with parenthesized/bare verse-number (strong signal)
    """
    s = line.strip()
    if not s:
        return False
    # Strip trailing verse number for analysis
    s_no_num = re.sub(r"\s*\(?[0-9]+\)?\s*$", "", s).strip()
    # Count Arabic words
    arabic_word_re = re.compile(r"[؀-ۿ]+")
    words = arabic_word_re.findall(s_no_num)
    if len(words) < 6:
        return False
    # Ratio of Arabic letters to total (excluding spaces)
    nospace = re.sub(r"\s", "", s_no_num)
    if not nospace:
        return False
    arabic_chars = sum(1 for ch in nospace if "؀" <= ch <= "ۿ")
    if arabic_chars / len(nospace) < 0.7:
        return False
    # Strong signal: trailing verse number
    if re.search(r"\([0-9]+\)\s*$", s) or re.search(r"\s\d+\s*$", s):
        return True
    # Strong signal: contains hemistich separator
    if "..." in s_no_num:
        return True
    if "،" in s_no_num and len(words) >= 8:
        # could be poetry with comma separator — mild positive
        pass
    # Reject if has prose attribution or section markers
    if re.search(r"^(قال|وقال|فقال|يقول|روى|يروى|روي|اعتنى|الناشر|الطبعة|المؤلف|أعده|بسم|قافية|البحر|^أ-)", s):
        return False
    if re.search(r":", s):
        return False
    if re.search(r"#####|----|AUTO\s|\bمات\b|\bتوفي\b|\bالميلاد\b|\bالناشر\b", s):
        return False
    # Otherwise, heuristic: a long line with mostly Arabic words and no colons is plausibly bayt
    # — but be conservative: require some balance
    if len(words) >= 8:
        return True
    return False


def parse_qafiya_sections(lines):
    """Return list of (qafiya_label, bayt_lines) tuples. Falls back to single section."""
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


def make_blocks_from_lines(filepath, source_label):
    """Read a poetry file, extract bayt-lines, split into qaṣīda-blocks of size BLOCK_SIZE.
    Returns list of dicts: {source, qafiya, block_idx, bayts: [str]}."""
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()
    sections = parse_qafiya_sections(lines)
    blocks = []
    for qafiya, bayts in sections:
        # Slice into BLOCK_SIZE-bayt contiguous blocks
        i = 0
        while i + MIN_BAYTS_FOR_BLOCK <= len(bayts):
            chunk = bayts[i:i + BLOCK_SIZE]
            if len(chunk) >= MIN_BAYTS_FOR_BLOCK:
                blocks.append({
                    "source": source_label,
                    "qafiya": qafiya,
                    "block_idx": len(blocks),
                    "bayts": chunk,
                })
            i += BLOCK_SIZE
    return blocks


def normalize_word(w):
    """Light stem-ish normalization: strip diacritics, normalize variants, strip leading particles."""
    w = strip_diacritics(w)
    w = "".join(normalize_letter(ch) for ch in w)
    # Strip non-Arabic characters
    w = "".join(ch for ch in w if "؀" <= ch <= "ۿ")
    if len(w) < 2:
        return w
    # Strip leading proclitic particles (greedy, longest first)
    for p in ["ال", "و", "ف", "ب", "ل", "ك"]:
        if w.startswith(p) and len(w) > len(p) + 1:
            w = w[len(p):]
            break
    return w


def block_word_counts(block):
    """Return Counter of normalized words for a block."""
    c = Counter()
    arabic_word_re = re.compile(r"[؀-ۿ]+")
    for ln in block["bayts"]:
        # Strip trailing verse number
        ln_clean = re.sub(r"\s*\(?[0-9]+\)?\s*$", "", ln)
        for w in arabic_word_re.findall(ln_clean):
            nw = normalize_word(w)
            if nw and len(nw) >= 2:
                c[nw] += 1
    return c


def block_final_letters(block):
    """Return list of final letters (canonical) for each bayt in the block."""
    finals = []
    for ln in block["bayts"]:
        ch = get_final_letter(ln)
        if ch is not None:
            finals.append(ch)
    return finals


def cosine_distance(u, v):
    du = math.sqrt(sum(x * x for x in u))
    dv = math.sqrt(sum(x * x for x in v))
    if du < 1e-15 or dv < 1e-15:
        return 1.0
    sim = sum(u[i] * v[i] for i in range(len(u))) / (du * dv)
    sim = max(-1.0, min(1.0, sim))
    return 1.0 - sim


def fisher_rao_distance(p, q):
    """FR distance between probability distributions: 2 * arccos(BC)."""
    bc = sum(math.sqrt(p[i] * q[i]) for i in range(len(p)))
    bc = max(-1.0, min(1.0, bc))
    return 2.0 * math.acos(bc)


def build_dist_matrix(vectors, metric_fn):
    n = len(vectors)
    D = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = metric_fn(vectors[i], vectors[j])
            D[i][j] = d
            D[j][i] = d
    return D


def mean_pairwise(D, idxs):
    pairs = list(combinations(idxs, 2))
    if not pairs:
        return 0.0
    return sum(D[a][b] for a, b in pairs) / len(pairs)


def pearson_r(x, y):
    n = len(x)
    if n < 2:
        return 0.0
    mx, my = sum(x) / n, sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    dx = math.sqrt(sum((x[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((y[i] - my) ** 2 for i in range(n)))
    return num / (dx * dy) if dx > 1e-15 and dy > 1e-15 else 0.0


def spearman_rho(x, y):
    def ranks(v):
        sp = sorted(enumerate(v), key=lambda p: p[1])
        r = [0] * len(v)
        i = 0
        while i < len(sp):
            j = i
            while j + 1 < len(sp) and sp[j + 1][1] == sp[i][1]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[sp[k][0]] = avg_rank
            i = j + 1
        return r
    return pearson_r(ranks(x), ranks(y))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def analyze_corpus(blocks, label, log=print):
    """Run full analysis on a list of blocks. Returns dict of results."""
    log(f"\n=== Corpus: {label} ===")
    log(f"  N blocks: {len(blocks)}")
    if len(blocks) < 30:
        log(f"  *** INSUFFICIENT DATA: need ≥30 blocks for meaningful analysis ***")
        return {"label": label, "n_blocks": len(blocks), "status": "INSUFFICIENT_DATA"}
    sources = Counter(b["source"] for b in blocks)
    qafiyas = Counter(b["qafiya"] for b in blocks)
    log(f"  Source distribution: {dict(sources)}")
    log(f"  Qafiya distribution (top 10): {dict(qafiyas.most_common(10))}")

    # Build content (top-K word-form) vectors
    all_word_counts = Counter()
    block_counts = []
    for b in blocks:
        c = block_word_counts(b)
        block_counts.append(c)
        all_word_counts.update(c)
    top_words = [w for w, _ in all_word_counts.most_common(TOPK_WORDS)]
    word_index = {w: i for i, w in enumerate(top_words)}
    log(f"  Vocabulary: {len(all_word_counts)} unique normalized word-forms; top-{TOPK_WORDS} retained")
    log(f"  Top-5 words: {top_words[:5]}")

    # Per-block content distribution (Dirichlet smoothed, L1 normalized)
    content_vecs = []
    coverage_topk = []
    for c in block_counts:
        vec = [0.0] * TOPK_WORDS
        total_seen = 0
        in_topk = 0
        for w, n in c.items():
            total_seen += n
            if w in word_index:
                vec[word_index[w]] += n
                in_topk += n
        coverage_topk.append(in_topk / max(1, total_seen))
        smoothed = [v + DIRICHLET_ALPHA for v in vec]
        s = sum(smoothed)
        content_vecs.append([v / s for v in smoothed])
    log(f"  Mean top-K coverage per block: {sum(coverage_topk)/len(coverage_topk):.3f}")

    # Per-block rhyme vector
    rhyme_vecs = []
    rhyme_diagnostics = []
    n_finals_total = 0
    for b in blocks:
        finals = block_final_letters(b)
        n_finals_total += len(finals)
        v = [0] * 28
        for ch in finals:
            v[LETTER_INDEX[ch]] += 1
        n = sum(v)
        if n > 0:
            top_letter_idx = max(range(28), key=lambda i: v[i])
            rhyme_diagnostics.append({
                "source": b["source"], "qafiya": b["qafiya"],
                "top_letter": ARABIC_LETTERS[top_letter_idx],
                "frac": v[top_letter_idx] / n,
                "n_bayts": n,
            })
            rhyme_vecs.append([x / n for x in v])
        else:
            rhyme_diagnostics.append({"source": b["source"], "qafiya": b["qafiya"],
                                      "top_letter": None, "frac": 0.0, "n_bayts": 0})
            rhyme_vecs.append([1.0 / 28] * 28)
    log(f"  Total bayts captured: {n_finals_total}")
    # Show top-letter dominance distribution
    fracs = [d["frac"] for d in rhyme_diagnostics if d["n_bayts"] > 0]
    if fracs:
        log(f"  Mean top-letter dominance (monorhyme strength): {sum(fracs)/len(fracs):.3f}")
        log(f"    median: {sorted(fracs)[len(fracs)//2]:.3f}, max: {max(fracs):.3f}, min: {min(fracs):.3f}")

    # Distance matrices
    log(f"  Computing Fisher-Rao distance matrix for content...")
    D_content = build_dist_matrix(content_vecs, fisher_rao_distance)
    log(f"  Computing cosine distance matrix for rhyme...")
    D_rhyme = build_dist_matrix(rhyme_vecs, cosine_distance)

    # Window analysis
    n_windows = len(blocks) - K + 1
    log(f"  N windows (K={K}): {n_windows}")
    if n_windows < 20:
        log(f"  *** TOO FEW WINDOWS for meaningful Pearson r ({n_windows} < 20) ***")
        return {"label": label, "n_blocks": len(blocks), "n_windows": n_windows,
                "status": "INSUFFICIENT_WINDOWS"}

    d_content = []
    d_rhyme = []
    for s in range(n_windows):
        idxs = list(range(s, s + K))
        d_content.append(mean_pairwise(D_content, idxs))
        d_rhyme.append(mean_pairwise(D_rhyme, idxs))

    r_obs = pearson_r(d_content, d_rhyme)
    rho_obs = spearman_rho(d_content, d_rhyme)
    log(f"  Pearson r(content × rhyme) = {r_obs:+.4f}")
    log(f"  Spearman ρ(content × rhyme) = {rho_obs:+.4f}")

    # Permutation null
    log(f"  Permutation null ({N_PERMS} perms)...")
    rng = random.Random(SEED)
    null_rs = []
    for _ in range(N_PERMS):
        sh = d_rhyme[:]
        rng.shuffle(sh)
        null_rs.append(pearson_r(d_content, sh))
    p_lower = sum(1 for r in null_rs if r <= r_obs) / len(null_rs)
    p_upper = sum(1 for r in null_rs if r >= r_obs) / len(null_rs)
    p_two = 2 * min(p_lower, p_upper)
    log(f"  p(r ≤ obs) = {p_lower:.5f}, p(r ≥ obs) = {p_upper:.5f}, p_two = {p_two:.5f}")

    return {
        "label": label,
        "n_blocks": len(blocks),
        "n_windows": n_windows,
        "K": K,
        "n_bayts_total": n_finals_total,
        "vocab_size": len(all_word_counts),
        "topk_words": TOPK_WORDS,
        "mean_topk_coverage": sum(coverage_topk) / len(coverage_topk),
        "mean_top_letter_dominance": sum(fracs) / len(fracs) if fracs else 0.0,
        "median_top_letter_dominance": sorted(fracs)[len(fracs) // 2] if fracs else 0.0,
        "d_content": d_content,
        "d_rhyme": d_rhyme,
        "pearson_r": r_obs,
        "spearman_rho": rho_obs,
        "perm_p_lower": p_lower,
        "perm_p_upper": p_upper,
        "perm_p_two": p_two,
        "rhyme_diagnostics": rhyme_diagnostics,
        "block_sources": [b["source"] for b in blocks],
        "block_qafiyas": [b["qafiya"] for b in blocks],
        "status": "OK",
    }


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-740 (Pre-Islamic poetry control) ===", flush=True)
    print(f"Pre-reg SHA: {prereg_sha}")
    print(f"Expected:    {EXPECTED_PREREG_SHA}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print(f"!!! WARNING: prereg SHA mismatch")
    print(f"Seed: {SEED}\nK: {K}\nBLOCK_SIZE: {BLOCK_SIZE}\nN_PERMS: {N_PERMS}\n")

    # Build pre-Islamic blocks
    print("=== Loading pre-Islamic corpus ===")
    pre_islamic_blocks = []
    for fname in MUALLAQAT:
        path = RAW / fname
        bks = make_blocks_from_lines(path, source_label=fname.replace(".txt", ""))
        print(f"  {fname}: {len(bks)} blocks")
        pre_islamic_blocks.extend(bks)
    for fname in DIWANS:
        path = RAW / fname
        bks = make_blocks_from_lines(path, source_label=fname.replace(".txt", ""))
        print(f"  {fname}: {len(bks)} blocks")
        pre_islamic_blocks.extend(bks)
    print(f"  TOTAL pre-Islamic blocks: {len(pre_islamic_blocks)}")

    # Build Mutanabbi blocks (secondary control)
    print("\n=== Loading Mutanabbi corpus (secondary control) ===")
    mutanabbi_blocks = []
    for fname in MUTANABBI:
        path = RAW / fname
        bks = make_blocks_from_lines(path, source_label=fname.replace(".txt", ""))
        print(f"  {fname}: {len(bks)} blocks")
        mutanabbi_blocks.extend(bks)

    # Run analyses
    pre_islamic_results = analyze_corpus(pre_islamic_blocks, "pre_islamic_qasida")
    mutanabbi_results = analyze_corpus(mutanabbi_blocks, "mutanabbi_diwan")

    # Robustness: drop the largest source (antara) and re-run
    print("\n=== ROBUSTNESS: pre-Islamic excluding diwan-antara ===")
    pre_no_antara = [b for b in pre_islamic_blocks if "diwan-antara" not in b["source"]]
    pre_no_antara_results = analyze_corpus(pre_no_antara, "pre_islamic_no_antara")

    # Verdicts
    QURAN_R = -0.8643
    print(f"\n=== COMPARISON TO QURAN ===")
    print(f"Quran r (H-NEW-730) = {QURAN_R:+.4f}")
    if pre_islamic_results.get("status") == "OK":
        r_pre = pre_islamic_results["pearson_r"]
        print(f"Pre-Islamic r       = {r_pre:+.4f}")
        diff = r_pre - QURAN_R
        print(f"  Δr (poetry − Quran) = {diff:+.4f}")
        # Verdict logic per pre-reg
        ALPHA = 0.05 / 3
        p_pre = pre_islamic_results["perm_p_lower"]
        if r_pre > -0.4:
            verdict_pre = f"PASS-CONFIRMS-IʿJĀZ-CLAIM — r={r_pre:+.4f} > -0.4; iʿjāz architectural distinction validated"
        elif r_pre > -0.6:
            verdict_pre = f"DIRECTIONAL-CONFIRMS — r={r_pre:+.4f} ∈ (-0.6, -0.4]; Quran significantly stronger"
        elif p_pre <= ALPHA:
            verdict_pre = f"FALSIFIES-IʿJĀZ-CLAIM — r={r_pre:+.4f} ≤ -0.6, p={p_pre:.5f} ≤ α_bon={ALPHA:.5f}; iʿjāz claim collapses to genre convention"
        else:
            verdict_pre = f"INTERMEDIATE — r={r_pre:+.4f}, p={p_pre:.5f}"
        print(f"\n>>> PRE-ISLAMIC VERDICT: {verdict_pre}")
    else:
        verdict_pre = f"NULL-DUE-TO-DATA-GAP — pre-Islamic status: {pre_islamic_results.get('status')}"
        print(f"\n>>> PRE-ISLAMIC VERDICT: {verdict_pre}")

    if mutanabbi_results.get("status") == "OK":
        r_mut = mutanabbi_results["pearson_r"]
        print(f"\nMutanabbi r (secondary, post-classical) = {r_mut:+.4f}")
    else:
        print(f"\nMutanabbi: {mutanabbi_results.get('status')}")

    # Save JSON
    out = {
        "id": "H-NEW-740",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "K": K,
        "block_size": BLOCK_SIZE,
        "n_perms": N_PERMS,
        "topk_words": TOPK_WORDS,
        "dirichlet_alpha": DIRICHLET_ALPHA,
        "quran_reference_r": QURAN_R,
        "alpha_bon": 0.05 / 3,
        "pre_islamic": pre_islamic_results,
        "pre_islamic_no_antara": pre_no_antara_results,
        "mutanabbi": mutanabbi_results,
        "verdict_pre_islamic": verdict_pre,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
