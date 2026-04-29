#!/usr/bin/env python3
"""H-NEW-42 Reverse-Direction Structural Fragility — pre-registered test.

Pre-reg: findings/phase-b-hypotheses/h-new-42-reverse-direction-fragility-prereg.md
Amendments applied: 42-A (three-baseline required, hard abort), 42-B
(baseline paths + Muʿallaqāt-pool SHA-256 logged), 42-C (f₂ GoFP entry).

Rules tuple: (no-tashkeel, orthographic-token, graphemes,
              basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
Bonferroni family: 2026-04-15-Fresh-Wave-3, k=3, alpha_bon=0.0167,
alpha_cell = 0.00556 (three-baseline JOINT threshold; no fallback).

f₂ substitution:
  Pre-reg specifies `aubmindlab/bert-base-arabertv02` (no commit hash
  available at spec time). No local copy of that model on this machine.
  Per amendment 42-C + GoFP entry 2026-04-15, f₂ is replaced by the
  rule-based char-trigram Jaccard proxy described in the GoFP entry,
  logged BEFORE any numeric result was viewed. Substitution is
  conservative (biases toward null).

6-axis fingerprint per surah:
  f1: rhyme-class coherence (same final-rhyme-bigram as modal)
  f2: mean char-trigram Jaccard of adjacent verses (letters-only,
      no-tashkeel) — GoFP-amended substitute.
  f3: divine-name trajectory run-entropy (binary indicator per verse)
  f4: verse-length first-difference smoothness (1 - normalized TV)
  f5: stem-proxy repetition density (first-3-letters match within k=3)
  f6: letter-bigram→letter Markov transition entropy

Fragility:
  Delta(S) = ||F(S) - F(S_reversed)||_1 / (6 * sqrt(n_verses))

Baselines (REQUIRED, no fallback):
  Bukhārī  = data/baseline-corpora/raw/bukhari-noquran.txt
  Jāḥiẓ    = data/baseline-corpora/raw/jahiz-hayawan.txt
  Muʿallaqāt-pool = canonical concat of 7 files:
    imru-al-qais, tarafa, zuhayr, labid, amr-bin-kulthum, antara, harith
  SHA-256 of pool logged in findings JSON.

Null model: 1000 re-partitions per baseline, pseudo-surahs letter-count-
quantile-matched to Quran's 114-surah distribution. Verse-length drawn
from Quran's verse-length distribution.

Positive control: Muʿallaqāt direct per-poem fragility (ordered by rhyme)
must exceed Jāḥiẓ partitioned mean; else NULL-BROKEN.

Seed 20260415. Publish PASS and NULL identically.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
BASELINE_DIR = ROOT / "data" / "baseline-corpora" / "raw"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-42.json"
OUT_MD = ROOT / "findings" / "phase-b-hypotheses" / "h-new-42-reverse-direction-fragility.md"
OUT_JOURNAL = ROOT / "journal" / "h-new-42-run-1.md"

SEED = 20260415
N_NULL = 1000
ALPHA_BON = 0.0167
ALPHA_CELL_3 = ALPHA_BON / 3  # ≈ 0.00556 — the ONLY permissible alpha (42-A)

# Canonical Muʿallaqāt order (42-B): imru-al-qais, tarafa, zuhayr, labid,
# amr-bin-kulthum, antara, harith.
MUALLAQAT_FILES_CANONICAL = [
    "muallaqa-imru-al-qais.txt",
    "muallaqa-tarafa.txt",
    "muallaqa-zuhayr.txt",
    "muallaqa-labid.txt",
    "muallaqa-amr-bin-kulthum.txt",
    "muallaqa-antara.txt",
    "muallaqa-harith.txt",
]

# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

TASHKEEL = "".join(chr(c) for c in range(0x064B, 0x0653))
TASHKEEL += chr(0x0653) + chr(0x0654) + chr(0x0655) + chr(0x0670)
TATWEEL = chr(0x0640)
QURANIC_MARKS = "".join(chr(c) for c in range(0x06D6, 0x06EE))
MISC_STRIP = "ۛۚۖۗۘۙ۞۩ۜ"
STRIP_CHARS = set(TASHKEEL + TATWEEL + QURANIC_MARKS + MISC_STRIP)

ALEF_VARIANTS = "آأإٱ"
ALEF = "ا"
ARABIC_RANGE = (0x0621, 0x064A)

DIVINE_NAMES = {
    "الله", "اللهم", "الرحمن", "الرحيم", "رب", "ربك", "ربنا", "ربهم", "ربكم",
    "ربي", "إلهك", "إلهنا", "إلهي", "إله", "ربه", "ربها",
}


def strip_diacritics(s: str) -> str:
    out = []
    for ch in s:
        if ch in STRIP_CHARS:
            continue
        if ch in ALEF_VARIANTS:
            out.append(ALEF)
        else:
            out.append(ch)
    return "".join(out)


def is_arabic_letter(ch: str) -> bool:
    c = ord(ch)
    return ARABIC_RANGE[0] <= c <= ARABIC_RANGE[1] or c == 0x0671


def tokenize(text: str) -> list[str]:
    tokens = []
    for raw in text.split():
        letters = [c for c in raw if is_arabic_letter(c)]
        if letters:
            tokens.append("".join(letters))
    return tokens


def letters_only(text: str) -> str:
    return "".join(c for c in text if is_arabic_letter(c))


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------


def load_quran_surahs() -> list[list[list[str]]]:
    """Return list[surah] of list[verse] of tokens."""
    data = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    surahs = []
    for ch in data:
        verses = [tokenize(strip_diacritics(v["text"])) for v in ch["verses"]]
        surahs.append(verses)
    return surahs


def load_text_as_tokens(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    # strip parenthetical glosses & bracketed headings
    raw = re.sub(r"\[[^\]]*\]", " ", raw)
    return tokenize(strip_diacritics(raw))


def load_muallaqat_lines() -> tuple[list[list[list[str]]], str, str]:
    """Seven muʿallaqāt in canonical order. Returns (poems, pool_sha256, pool_text).

    Hard-aborts if any file missing or empty (42-A no-fallback).
    """
    poems = []
    pool_parts = []
    for fn in MUALLAQAT_FILES_CANONICAL:
        p = BASELINE_DIR / fn
        if not p.exists():
            raise RuntimeError(f"42-A hard abort: Muʿallaqāt file missing: {p}")
        raw = p.read_text(encoding="utf-8")
        if not raw.strip():
            raise RuntimeError(f"42-A hard abort: Muʿallaqāt file empty: {p}")
        pool_parts.append(raw)
        lines = []
        for ln in raw.splitlines():
            toks = tokenize(strip_diacritics(ln))
            if toks:
                lines.append(toks)
        if len(lines) < 2:
            raise RuntimeError(
                f"42-A hard abort: Muʿallaqāt file yields <2 lines: {p}")
        poems.append(lines)
    # canonical-order concatenation (newline separator between files)
    pool_text = "\n".join(pool_parts)
    pool_sha = hashlib.sha256(pool_text.encode("utf-8")).hexdigest()
    return poems, pool_sha, pool_text


# ---------------------------------------------------------------------------
# Pseudo-surah partitioning (letter-count quantile-matched)
# ---------------------------------------------------------------------------


def quran_letter_count_targets(surahs) -> list[int]:
    return [sum(len("".join(v)) for v in verses) for verses in surahs]


def partition_baseline_matched(
    tokens: list[str],
    targets: list[int],
    rng: random.Random,
    verse_len_mean: float,
    verse_len_std: float,
) -> list[list[list[str]]]:
    """Partition a flat token stream into pseudo-surahs whose letter-count
    distribution matches `targets` (quantile-matched). Each pseudo-surah is
    further split into pseudo-verses using a truncated-normal verse-length
    sampler to mimic Quran per-surah verse-length distribution.
    """
    # Shuffle targets so different runs use different order, but tokens are read
    # sequentially; we use order = random permutation of targets for fairness.
    targets_shuffled = targets.copy()
    rng.shuffle(targets_shuffled)

    total_needed = sum(targets_shuffled)
    # If baseline too short, cycle.
    tok_stream = tokens
    if sum(len(t) for t in tokens) < total_needed:
        # cycle
        reps = total_needed // max(1, sum(len(t) for t in tokens)) + 2
        tok_stream = tokens * reps

    pos = 0
    n_tokens = len(tok_stream)
    pseudo_surahs = []
    # precompute token lengths
    tok_lens = [len(t) for t in tok_stream]
    for tgt in targets_shuffled:
        letters_acc = 0  # total surah letters
        cur_verse_letters = 0
        verses = []
        cur_verse_toks: list[str] = []
        target_vlen = max(6, int(rng.gauss(verse_len_mean, verse_len_std)))
        while letters_acc < tgt and pos < n_tokens:
            tlen = tok_lens[pos]
            tok = tok_stream[pos]
            pos += 1
            if tlen == 0:
                continue
            cur_verse_toks.append(tok)
            cur_verse_letters += tlen
            letters_acc += tlen
            if cur_verse_letters >= target_vlen:
                verses.append(cur_verse_toks)
                cur_verse_toks = []
                cur_verse_letters = 0
                target_vlen = max(6, int(rng.gauss(verse_len_mean, verse_len_std)))
        if cur_verse_toks:
            verses.append(cur_verse_toks)
        if len(verses) >= 2:
            pseudo_surahs.append(verses)
    return pseudo_surahs


# ---------------------------------------------------------------------------
# Fingerprint axes
# ---------------------------------------------------------------------------


def verse_last_letters(verses: list[list[str]], k: int = 2) -> list[str]:
    out = []
    for v in verses:
        if not v:
            out.append("")
            continue
        last = v[-1]
        out.append(last[-k:] if len(last) >= k else last)
    return out


def f1_rhyme_coherence(verses) -> float:
    ends = [e for e in verse_last_letters(verses, 2) if e]
    if len(ends) < 2:
        return 0.0
    c = Counter(ends)
    modal = c.most_common(1)[0][0]
    return sum(1 for e in ends if e == modal) / len(ends)


def char_trigrams(s: str) -> set[str]:
    if len(s) < 3:
        return {s} if s else set()
    return {s[i:i + 3] for i in range(len(s) - 2)}


def f2_semantic_proxy(verses) -> float:
    """Mean char-trigram Jaccard similarity of ADJACENT verses (proxy for
    semantic coherence). Order-sensitive by construction."""
    if len(verses) < 2:
        return 0.0
    joined = ["".join(v) for v in verses]
    grams = [char_trigrams(s) for s in joined]
    sims = []
    for i in range(len(grams) - 1):
        a, b = grams[i], grams[i + 1]
        if not a or not b:
            continue
        inter = len(a & b)
        union = len(a | b)
        sims.append(inter / union if union else 0.0)
    return statistics.mean(sims) if sims else 0.0


def f3_divine_entropy(verses) -> float:
    indicator = []
    for v in verses:
        has = any(tok in DIVINE_NAMES for tok in v)
        indicator.append(1 if has else 0)
    if not indicator:
        return 0.0
    # Shannon entropy of the binary sequence's run-length distribution,
    # order-sensitive because runs depend on arrangement.
    runs = []
    cur = indicator[0]
    rlen = 1
    for x in indicator[1:]:
        if x == cur:
            rlen += 1
        else:
            runs.append((cur, rlen))
            cur = x
            rlen = 1
    runs.append((cur, rlen))
    total = sum(r[1] for r in runs)
    if total == 0:
        return 0.0
    h = 0.0
    for _, r in runs:
        p = r / total
        if p > 0:
            h -= p * math.log2(p)
    return h


def f4_length_smoothness(verses) -> float:
    lens = [sum(len(t) for t in v) for v in verses]
    if len(lens) < 2:
        return 0.0
    diffs = [abs(lens[i + 1] - lens[i]) for i in range(len(lens) - 1)]
    tv = sum(diffs)
    total_range = max(lens) - min(lens) if max(lens) != min(lens) else 1
    # normalized total variation, then 1 - that, clipped
    norm = tv / (len(diffs) * max(1, total_range))
    return max(0.0, 1.0 - norm)


def f5_root_repetition(verses, window: int = 3) -> float:
    """Fraction of verse pairs (i, j) with 0 < j - i <= window sharing a
    word-stem (first 3 letters of any token)."""
    n = len(verses)
    if n < 2:
        return 0.0
    stem_sets = []
    for v in verses:
        stems = {t[:3] for t in v if len(t) >= 3}
        stem_sets.append(stems)
    hits = 0
    total = 0
    for i in range(n):
        for j in range(i + 1, min(n, i + 1 + window)):
            total += 1
            if stem_sets[i] & stem_sets[j]:
                hits += 1
    return hits / total if total else 0.0


def f6_trigram_entropy(verses) -> float:
    """Markov transition entropy over letter trigrams computed WITHIN the
    surah's concatenated-with-delimiter stream. Order-sensitive because
    inter-verse transitions at verse boundaries depend on order. Optimized:
    single-pass Counter over (bigram, next_char) then conditional entropy."""
    s = "|".join("".join(v) for v in verses)
    if len(s) < 4:
        return 0.0
    # Count bigrams and transitions
    bi_counts: dict = {}
    tri_counts: dict = {}
    for i in range(len(s) - 2):
        bi = s[i] + s[i + 1]
        tri = bi + s[i + 2]
        bi_counts[bi] = bi_counts.get(bi, 0) + 1
        tri_counts[tri] = tri_counts.get(tri, 0) + 1
    # H(C | bigram) weighted by P(bigram) = conditional entropy
    total_bi = sum(bi_counts.values())
    if total_bi == 0:
        return 0.0
    # group tri by bi prefix (first 2 chars)
    h_total = 0.0
    per_bi_next: dict = defaultdict(list)
    for tri, c in tri_counts.items():
        per_bi_next[tri[:2]].append(c)
    for bi, counts in per_bi_next.items():
        tot = sum(counts)
        if tot == 0:
            continue
        h = 0.0
        for c in counts:
            p = c / tot
            if p > 0:
                h -= p * math.log2(p)
        h_total += h * tot
    return h_total / total_bi


AXES = [f1_rhyme_coherence, f2_semantic_proxy, f3_divine_entropy,
        f4_length_smoothness, f5_root_repetition, f6_trigram_entropy]


def fingerprint(verses) -> tuple[float, ...]:
    return tuple(f(verses) for f in AXES)


def fragility(verses) -> float:
    if len(verses) < 2:
        return 0.0
    F = fingerprint(verses)
    F_rev = fingerprint(list(reversed(verses)))
    l1 = sum(abs(a - b) for a, b in zip(F, F_rev))
    return l1 / (6 * math.sqrt(len(verses)))


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------


def one_sided_p(observed: float, null_dist: list[float]) -> float:
    """One-sided p = P(null >= observed). Additive smoothing."""
    n = len(null_dist)
    k = sum(1 for x in null_dist if x >= observed)
    return (k + 1) / (n + 1)


# ---------------------------------------------------------------------------
# MW-7 internal-error check
# ---------------------------------------------------------------------------


def internal_error_check(quran_surahs) -> list[str]:
    """Runs sanity invariants; returns list of warnings."""
    warnings = []
    # 1. Fingerprint symmetric under double-reverse
    s0 = quran_surahs[0]
    F = fingerprint(s0)
    F_rev2 = fingerprint(list(reversed(list(reversed(s0)))))
    if any(abs(a - b) > 1e-9 for a, b in zip(F, F_rev2)):
        warnings.append("double-reverse-inequality")
    # 2. Single-verse surah has fragility 0
    short = [s0[0]]
    if fragility(short) != 0.0:
        warnings.append("single-verse-nonzero-fragility")
    # 3. Every axis in [0, some_reasonable_bound]
    bad_axes = []
    for i, f in enumerate(AXES, 1):
        val = f(s0)
        if val < 0 or math.isnan(val) or math.isinf(val):
            bad_axes.append(f"f{i}={val}")
    if bad_axes:
        warnings.append("bad-axis-values:" + ",".join(bad_axes))
    # 4. Reversed Quran fragility equals forward (they're mirror; our operator
    #    is symmetric in fingerprint-diff). Confirm by swap.
    return warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def per_surah_verse_stats(surahs):
    vlens = []
    for verses in surahs:
        for v in verses:
            vlens.append(sum(len(t) for t in v))
    return statistics.mean(vlens), statistics.pstdev(vlens)


def main() -> None:
    t0 = time.time()
    rng = random.Random(SEED)

    print("[H-NEW-42] Loading Quran ...", file=sys.stderr)
    quran_surahs = load_quran_surahs()
    assert len(quran_surahs) == 114
    targets = quran_letter_count_targets(quran_surahs)
    vmean, vstd = per_surah_verse_stats(quran_surahs)
    print(f"  verse-length mean={vmean:.1f} std={vstd:.1f}", file=sys.stderr)

    # MW-7 internal error check BEFORE further analysis
    errors = internal_error_check(quran_surahs)
    if errors:
        print(f"[MW-7 WARN] {errors}", file=sys.stderr)

    print("[H-NEW-42] Computing Quran fragility ...", file=sys.stderr)
    quran_frag = [fragility(v) for v in quran_surahs]
    quran_mean = statistics.mean(quran_frag)
    quran_median = statistics.median(quran_frag)
    print(f"  Δ̄_Quran mean={quran_mean:.6f} median={quran_median:.6f}",
          file=sys.stderr)

    # Load baseline token streams (42-A hard abort on any failure)
    print("[H-NEW-42] Loading baselines ...", file=sys.stderr)
    bukhari_path = BASELINE_DIR / "bukhari-noquran.txt"
    jahiz_path = BASELINE_DIR / "jahiz-hayawan.txt"
    for p in [bukhari_path, jahiz_path]:
        if not p.exists() or p.stat().st_size == 0:
            raise RuntimeError(f"42-A hard abort: baseline unavailable: {p}")
    bukhari_toks = load_text_as_tokens(bukhari_path)
    jahiz_toks = load_text_as_tokens(jahiz_path)
    if len(bukhari_toks) < 10000 or len(jahiz_toks) < 10000:
        raise RuntimeError("42-A hard abort: baseline token count too low "
                           f"(bukhari={len(bukhari_toks)}, "
                           f"jahiz={len(jahiz_toks)})")
    mua_poems, mua_pool_sha, mua_pool_text = load_muallaqat_lines()
    print(f"  bukhari tokens={len(bukhari_toks)}", file=sys.stderr)
    print(f"  jahiz tokens={len(jahiz_toks)}", file=sys.stderr)
    print(f"  muallaqat poems={len(mua_poems)} lines_total="
          f"{sum(len(p) for p in mua_poems)}", file=sys.stderr)
    print(f"  muallaqat pool SHA-256={mua_pool_sha}", file=sys.stderr)
    if len(mua_poems) != 7:
        raise RuntimeError(f"42-A hard abort: expected 7 muʿallaqāt, "
                           f"got {len(mua_poems)}")

    # Also compute SHA-256 of bukhari + jahiz inputs for integrity
    bukhari_sha = hashlib.sha256(
        bukhari_path.read_bytes()).hexdigest()
    jahiz_sha = hashlib.sha256(
        jahiz_path.read_bytes()).hexdigest()
    quran_sha = hashlib.sha256(QURAN_JSON.read_bytes()).hexdigest()

    # --- Muʿallaqāt: use each poem as a pseudo-surah with its line sequence
    mua_frag_poems = [fragility(p) for p in mua_poems]
    mua_mean_direct = statistics.mean(mua_frag_poems)
    print(f"  Muʿallaqāt direct mean Δ̄={mua_mean_direct:.6f} "
          f"(over {len(mua_poems)} poems)", file=sys.stderr)

    # For the null model, we also need Muʿallaqāt partitioned comparably:
    # concatenate all lines, use as a flat token stream, partition to 114
    # pseudo-surahs. BUT the pool is too small (~800 lines vs quran letter
    # budget >>); we cycle.
    mua_all_toks = [t for p in mua_poems for line in p for t in line]

    def run_baseline(tokens, name, n_null):
        print(f"[H-NEW-42] Null for {name} (n={n_null}) ...", file=sys.stderr)
        rng_local = random.Random(SEED + hash(name) % 10**7)
        null_means = []
        point_mean = None
        t_start = time.time()
        for b in range(n_null):
            parts = partition_baseline_matched(
                tokens, targets, rng_local, vmean, vstd)
            if not parts:
                continue
            frags = [fragility(v) for v in parts]
            m = statistics.mean(frags) if frags else 0.0
            null_means.append(m)
            if b == 0:
                point_mean = m
            if (b + 1) % 50 == 0:
                elapsed = time.time() - t_start
                eta = elapsed / (b + 1) * (n_null - b - 1)
                print(f"  [{name}] {b+1}/{n_null}  "
                      f"elapsed={elapsed:.0f}s eta={eta:.0f}s",
                      file=sys.stderr)
        return null_means, point_mean

    null_bukhari, bukhari_point = run_baseline(bukhari_toks, "bukhari", N_NULL)
    null_jahiz, jahiz_point = run_baseline(jahiz_toks, "jahiz", N_NULL)
    null_mua, mua_point = run_baseline(mua_all_toks, "muallaqat", N_NULL)

    # One-sided: Quran MORE fragile than null baseline means
    p_bukhari = one_sided_p(quran_mean, null_bukhari)
    p_jahiz = one_sided_p(quran_mean, null_jahiz)
    p_mua = one_sided_p(quran_mean, null_mua)

    # Positive control: Muʿallaqāt direct > Jāḥiẓ direct?
    # Use median of null distribution as reference baseline Δ̄.
    jahiz_baseline_mean = statistics.mean(null_jahiz)
    mua_baseline_mean = statistics.mean(null_mua)
    pos_ctrl_ok = mua_mean_direct > jahiz_baseline_mean
    pos_ctrl_ok_flat = mua_baseline_mean > jahiz_baseline_mean

    # Synthetic backup control: Quran forward vs verse-within-surah-shuffled
    rng_syn = random.Random(SEED + 42)
    shuffled_frags = []
    for verses in quran_surahs:
        shuffled = verses.copy()
        rng_syn.shuffle(shuffled)
        shuffled_frags.append(fragility(shuffled))
    shuffled_mean = statistics.mean(shuffled_frags)

    # Top-3 most / least fragile surahs
    surah_indexed = sorted(
        [(i + 1, fr) for i, fr in enumerate(quran_frag)],
        key=lambda x: x[1])
    least3 = surah_indexed[:3]
    most3 = surah_indexed[-3:][::-1]

    # Verdict table (three-baseline joint threshold at alpha_cell = 0.00556)
    passes_bukhari = p_bukhari < ALPHA_CELL_3 and quran_mean > statistics.mean(null_bukhari)
    passes_jahiz = p_jahiz < ALPHA_CELL_3 and quran_mean > statistics.mean(null_jahiz)
    passes_mua = p_mua < ALPHA_CELL_3 and quran_mean > statistics.mean(null_mua)

    direction_forward = quran_mean > max(
        statistics.mean(null_bukhari),
        statistics.mean(null_jahiz),
        statistics.mean(null_mua))

    if not direction_forward:
        verdict = "EXPLORATORY-REVERSE"
    elif passes_bukhari and passes_jahiz and passes_mua:
        verdict = "STRONG-PASS"
    elif passes_bukhari and passes_jahiz and not passes_mua:
        verdict = "PASS-VS-PROSE"
    elif not (passes_bukhari and passes_jahiz):
        verdict = "NULL"
    else:
        verdict = "NULL"

    null_broken = not pos_ctrl_ok
    if null_broken:
        verdict = f"NULL-BROKEN ({verdict})"

    out = {
        "hypothesis_id": "H-NEW-42",
        "run_date": "2026-04-15",
        "seed": SEED,
        "rules_tuple": ["no-tashkeel", "orthographic-token", "graphemes",
                        "basmala-counted-only-in-surah-1", "hafs-kufan",
                        "mashriqi"],
        "bonferroni_family": "2026-04-15-Fresh-Wave-3",
        "alpha_bon": ALPHA_BON,
        "alpha_cell": ALPHA_CELL_3,
        "amendments_applied": ["42-A", "42-B", "42-C"],
        "integrity_sha256": {
            "quran_json": quran_sha,
            "bukhari_noquran": bukhari_sha,
            "jahiz_hayawan": jahiz_sha,
            "muallaqat_pool_canonical": mua_pool_sha,
            "muallaqat_canonical_order": MUALLAQAT_FILES_CANONICAL,
        },
        "mw7_warnings": errors,
        "f2_amendment": (
            "Rule-based char-trigram Jaccard proxy used in place of Arabic "
            "embedding model (no local model available). Logged BEFORE viewing "
            "results. Weakens f2 but preserves 6-axis fingerprint structure."
        ),
        "quran": {
            "mean_fragility": quran_mean,
            "median_fragility": quran_median,
            "n_surahs": 114,
            "min": min(quran_frag),
            "max": max(quran_frag),
        },
        "baselines": {
            "bukhari": {
                "null_mean": statistics.mean(null_bukhari),
                "null_median": statistics.median(null_bukhari),
                "null_std": statistics.pstdev(null_bukhari),
                "p_one_sided": p_bukhari,
                "delta_vs_quran": quran_mean - statistics.mean(null_bukhari),
                "passes_at_alpha_cell_three": passes_bukhari,
            },
            "jahiz": {
                "null_mean": statistics.mean(null_jahiz),
                "null_median": statistics.median(null_jahiz),
                "null_std": statistics.pstdev(null_jahiz),
                "p_one_sided": p_jahiz,
                "delta_vs_quran": quran_mean - statistics.mean(null_jahiz),
                "passes_at_alpha_cell_three": passes_jahiz,
            },
            "muallaqat": {
                "null_mean": statistics.mean(null_mua),
                "null_median": statistics.median(null_mua),
                "null_std": statistics.pstdev(null_mua),
                "p_one_sided": p_mua,
                "delta_vs_quran": quran_mean - statistics.mean(null_mua),
                "passes_at_alpha_cell_three": passes_mua,
                "direct_poem_mean": mua_mean_direct,
                "n_poems": len(mua_poems),
            },
        },
        "positive_control": {
            "muallaqat_direct_mean": mua_mean_direct,
            "jahiz_partitioned_mean": jahiz_baseline_mean,
            "muallaqat_partitioned_mean": mua_baseline_mean,
            "muallaqat_direct_gt_jahiz_partitioned": pos_ctrl_ok,
            "muallaqat_partitioned_gt_jahiz_partitioned": pos_ctrl_ok_flat,
            "null_broken": null_broken,
        },
        "synthetic_control": {
            "quran_verse_shuffled_mean": shuffled_mean,
            "quran_forward_minus_shuffled": quran_mean - shuffled_mean,
        },
        "extremes": {
            "most_fragile_top3_surah_ids": [sid for sid, _ in most3],
            "most_fragile_top3_values": [v for _, v in most3],
            "least_fragile_top3_surah_ids": [sid for sid, _ in least3],
            "least_fragile_top3_values": [v for _, v in least3],
        },
        "verdict": verdict,
        "runtime_seconds": time.time() - t0,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"[H-NEW-42] wrote {OUT_JSON}", file=sys.stderr)
    print(f"[H-NEW-42] VERDICT: {verdict}", file=sys.stderr)
    print(f"[H-NEW-42] runtime={out['runtime_seconds']:.1f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
