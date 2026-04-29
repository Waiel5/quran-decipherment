"""H-NEW-114 — Zero-set / absent-structures fingerprint.

Pre-reg: findings/phase-b-hypotheses/h-new-114-zero-set-prereg.md
Seed: 20260417
Bonferroni: k=4, alpha_bon=0.0125

Cells:
    A — Letter-bigram absent-set
    B — Letter-trigram absent-set
    C — Word-bigram (adjacent-token) surprising-absence
    D — 14-letter muqaṭṭāʿat-presence patterns across 114 surahs (descriptive)

Baselines (length-truncated to Quran letter count):
    Bukhārī prose — data/baseline-corpora/raw/bukhari-noquran.txt
    Jāḥiẓ Ḥayawān — data/baseline-corpora/raw/jahiz-hayawan.txt
    Muʿallaqāt (7 poems pooled)
"""
from __future__ import annotations

import json
import os
import random
import sys
from collections import Counter
from itertools import product
from typing import Dict, List, Tuple

import numpy as np

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))
from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words  # noqa: E402

SEED = 20260417
N_PERM = 10_000
ALPHA_BON = 0.0125
N_TOP_WORDS = 100

# 28 core Arabic letters (canonical order).
ALPHABET28 = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
ALPHABET_SET = set(ALPHABET28)
assert len(ALPHABET28) == 28

# 14 muqaṭṭāʿat letters.
MUQ14 = "احرسصطعقكلمنهي"
assert len(MUQ14) == 14

# Normalization maps (locked in pre-reg §NORMALIZATION).
NORMALIZE_MAP = str.maketrans({
    "ٱ": "ا",  # alif wasla
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ؤ": "و",
    "ئ": "ي",
    "ة": "ه",
    "ى": "ي",
})

# Strip ranges: tashkeel U+064B..U+0652, tatweel U+0640, recitation U+06D6..U+06ED,
# plus ZWJ/ZWNJ and any non-letter filtered post-normalization.
STRIP_CODEPOINTS = set()
for cp in range(0x064B, 0x0653):
    STRIP_CODEPOINTS.add(cp)
STRIP_CODEPOINTS.add(0x0640)
for cp in range(0x06D6, 0x06EE):
    STRIP_CODEPOINTS.add(cp)


def normalize(text: str) -> str:
    """Normalize Arabic text per locked pre-reg rules.

    1. Strip tashkeel, tatweel, recitation marks.
    2. Apply NORMALIZE_MAP (alif variants → ا etc.).
    3. Replace any non-{ALPHABET28, whitespace} character with a space.
    4. Collapse whitespace.
    """
    out_chars = []
    for ch in text:
        if ord(ch) in STRIP_CODEPOINTS:
            continue
        out_chars.append(ch)
    stripped = "".join(out_chars).translate(NORMALIZE_MAP)
    # Replace any char not in alphabet and not whitespace with space.
    result = []
    for ch in stripped:
        if ch in ALPHABET_SET:
            result.append(ch)
        elif ch.isspace():
            result.append(" ")
        else:
            result.append(" ")
    return " ".join("".join(result).split())


def tokens_from_normalized(normalized: str) -> List[str]:
    """Whitespace-split normalized text into word tokens (28-letter only)."""
    return [t for t in normalized.split() if t]


# ---------------------------------------------------------------------------
# Corpus loaders
# ---------------------------------------------------------------------------


def load_quran_text() -> Tuple[str, List[List[List[str]]]]:
    """Return (full-normalized-text, surah_verse_tokens).

    surah_verse_tokens[s][v] is a list of normalized word tokens for
    verse v of surah s (0-indexed).
    """
    surahs = load_quran("no-tashkeel")
    full_parts: List[str] = []
    surah_verse_tokens: List[List[List[str]]] = []
    for s in surahs:
        sv: List[List[str]] = []
        for v in s.verses:
            # Use real_words to strip recitation-mark-only tokens first,
            # then normalize each token. Normalization can split a token
            # (e.g., أضاءت → اضا ت because hamza ء is not in the 28-letter
            # alphabet and becomes a space). In that case we keep ALL
            # resulting sub-tokens as separate tokens.
            raw_tokens = real_words(v.text)
            norm_tokens: List[str] = []
            for tok in raw_tokens:
                n = normalize(tok)
                if not n:
                    continue
                for sub in n.split():
                    if sub:
                        norm_tokens.append(sub)
            sv.append(norm_tokens)
            full_parts.extend(norm_tokens)
        surah_verse_tokens.append(sv)
    full_text = " ".join(full_parts)
    return full_text, surah_verse_tokens


def load_baseline(paths: List[str]) -> str:
    """Load and concatenate-normalize baseline file(s)."""
    parts = []
    for p in paths:
        with open(p, "r", encoding="utf-8") as fh:
            parts.append(fh.read())
    raw = "\n".join(parts)
    return normalize(raw)


# ---------------------------------------------------------------------------
# Bigram / trigram absent-set on within-word streams
# ---------------------------------------------------------------------------


def within_word_ngrams(tokens: List[str], n: int) -> Counter:
    """Count within-word n-grams across a list of word tokens."""
    c = Counter()
    for tok in tokens:
        if len(tok) < n:
            continue
        for i in range(len(tok) - n + 1):
            c[tok[i:i + n]] += 1
    return c


def within_word_ngram_types(tokens: List[str], n: int) -> set:
    """Return set of n-gram types present in tokens (faster than counting)."""
    s = set()
    for tok in tokens:
        if len(tok) < n:
            continue
        for i in range(len(tok) - n + 1):
            s.add(tok[i:i + n])
    return s


def absent_ngram_set(ngram_counts: Counter, n: int) -> List[str]:
    """Return the list of all n-grams over ALPHABET28 that have count 0."""
    # Only include n-grams composed of 28-letter alphabet chars
    present = set()
    for g, c in ngram_counts.items():
        if c > 0 and all(ch in ALPHABET_SET for ch in g):
            present.add(g)
    absent = []
    for tup in product(ALPHABET28, repeat=n):
        g = "".join(tup)
        if g not in present:
            absent.append(g)
    return absent


def absent_ngram_count_fast(ngram_counts: Counter, n: int) -> int:
    """Fast version: just count absent n-grams without enumerating them."""
    n_possible = 28 ** n
    # All observed ngrams should be over alphabet28 already (guaranteed by
    # normalize()), so the size of ngram_counts IS the present-count.
    return n_possible - len(ngram_counts)


def corpus_absent_count(tokens: List[str], n: int) -> int:
    """Compute absent-ngram-count for a given token list."""
    s = within_word_ngram_types(tokens, n)
    return 28 ** n - len(s)


def truncate_to_letter_count(normalized_text: str, target_letters: int) -> List[str]:
    """Return tokens (whitespace-split) whose cumulative letter count <= target.

    Stops when adding the next token would exceed target.
    """
    toks = normalized_text.split()
    out: List[str] = []
    total = 0
    for t in toks:
        if total + len(t) > target_letters:
            # include partial — prefer strict equality if possible
            remain = target_letters - total
            if remain > 0:
                out.append(t[:remain])
                total += remain
            break
        out.append(t)
        total += len(t)
    return out


def sliding_windows_tokens(normalized_text: str, target_letters: int,
                            n_windows: int = 50) -> List[List[str]]:
    """Return a list of token-windows each with ~target_letters letters.

    Starts windows at evenly-spaced character offsets; each window grows
    forward from its start until `target_letters` letters are accumulated
    from whole tokens. If the corpus is shorter than target_letters, returns
    a single window with the full content. If corpus is longer, builds up
    to n_windows non-overlapping consecutive windows.
    """
    toks = normalized_text.split()
    total_letters = sum(len(t) for t in toks)
    if total_letters <= target_letters:
        return [toks]
    # Greedy non-overlapping partition into chunks of target_letters.
    windows: List[List[str]] = []
    cur: List[str] = []
    cur_letters = 0
    for t in toks:
        if cur_letters + len(t) > target_letters:
            windows.append(cur)
            if len(windows) >= n_windows:
                break
            cur = [t]
            cur_letters = len(t)
        else:
            cur.append(t)
            cur_letters += len(t)
    if cur and len(windows) < n_windows and cur_letters >= int(0.5 * target_letters):
        windows.append(cur)
    return windows


# ---------------------------------------------------------------------------
# Permutation null for bigram / trigram absent-count
# ---------------------------------------------------------------------------


def permute_letter_multiset(letter_stream: List[int], token_lengths: List[int],
                             rng: random.Random) -> List[str]:
    """Shuffle a flat letter stream and re-slice by token_lengths.

    letter_stream: flat list of letter characters (as single-char strings)
    token_lengths: original per-token letter counts

    Returns list of tokens of same lengths with shuffled letter content.
    """
    shuffled = letter_stream.copy()
    rng.shuffle(shuffled)
    out: List[str] = []
    idx = 0
    for ln in token_lengths:
        out.append("".join(shuffled[idx:idx + ln]))
        idx += ln
    return out


def perm_absent_counts(tokens: List[str], n: int, n_perm: int,
                        rng: random.Random) -> Tuple[int, List[int]]:
    """Return (observed absent-count, null distribution of absent-counts).

    Shuffles letters within the flat stream (preserves letter multiset and
    per-token lengths) and computes absent n-gram count each time.

    Uses numpy for fast shuffling. Encodes 28 letters as ints 0..27 and
    within-word n-grams as base-28 integer codes to accelerate set
    uniqueness.
    """
    letter_stream = [ch for tok in tokens for ch in tok]
    token_lengths = np.array([len(t) for t in tokens], dtype=np.int32)

    # Encode letters as small integers.
    letter_to_int = {ch: i for i, ch in enumerate(ALPHABET28)}
    int_stream = np.array([letter_to_int[ch] for ch in letter_stream], dtype=np.int32)
    N = len(int_stream)

    # For within-word n-gram: we need offsets (start indices for each token
    # where an n-gram can start). An n-gram at global position i is valid iff
    # it does not cross a token boundary. Build a boolean mask:
    # valid[i] = True iff positions i, i+1, ..., i+n-1 are all in the same
    # token.
    # Build a per-position token-id array:
    token_ids = np.empty(N, dtype=np.int32)
    offs = 0
    for tid, tlen in enumerate(token_lengths):
        token_ids[offs:offs + tlen] = tid
        offs += tlen
    valid_starts = np.ones(N - n + 1, dtype=bool)
    for k in range(1, n):
        valid_starts &= (token_ids[:N - n + 1] == token_ids[k:N - n + 1 + k])

    # Observed
    obs_codes = np.zeros(N - n + 1, dtype=np.int64)
    for k in range(n):
        obs_codes = obs_codes * 28 + int_stream[k:k + (N - n + 1)]
    obs_codes = obs_codes[valid_starts]
    obs_present_types = np.unique(obs_codes).size
    n_possible = 28 ** n
    obs_absent = n_possible - obs_present_types

    np_rng = np.random.default_rng(rng.getrandbits(64))
    null_absent: List[int] = []
    for _ in range(n_perm):
        shuf = int_stream.copy()
        np_rng.shuffle(shuf)
        codes = np.zeros(N - n + 1, dtype=np.int64)
        for k in range(n):
            codes = codes * 28 + shuf[k:k + (N - n + 1)]
        codes = codes[valid_starts]
        n_types = np.unique(codes).size
        null_absent.append(n_possible - n_types)
    return obs_absent, null_absent


def two_sided_p(obs: int, null_vals: List[int]) -> float:
    """Two-sided permutation p-value."""
    n = len(null_vals)
    ge = sum(1 for v in null_vals if v >= obs)
    le = sum(1 for v in null_vals if v <= obs)
    p_right = (1 + ge) / (1 + n)
    p_left = (1 + le) / (1 + n)
    return min(1.0, 2.0 * min(p_right, p_left))


# ---------------------------------------------------------------------------
# Cell C — word-bigram surprising-absence
# ---------------------------------------------------------------------------


def verse_flat_tokens(surah_verse_tokens: List[List[List[str]]]) -> Tuple[List[List[str]], List[int]]:
    """Return (list-of-verses (each a list of tokens), list of verse lengths in tokens)."""
    verses: List[List[str]] = []
    lengths: List[int] = []
    for sv in surah_verse_tokens:
        for v in sv:
            verses.append(v)
            lengths.append(len(v))
    return verses, lengths


def adjacent_pair_counts(verses: List[List[str]], top_set: set) -> Counter:
    """Count ordered adjacent-token pairs where both sides are in top_set.

    Adjacency does NOT cross verse boundaries (per pre-reg).
    """
    c: Counter = Counter()
    for v in verses:
        for i in range(len(v) - 1):
            a, b = v[i], v[i + 1]
            if a in top_set and b in top_set:
                c[(a, b)] += 1
    return c


def adjacent_pair_slots(verses: List[List[str]]) -> int:
    return sum(max(0, len(v) - 1) for v in verses)


def cell_c_compute(surah_verse_tokens: List[List[List[str]]],
                    n_perm: int, rng: random.Random) -> dict:
    import math
    verses, v_lengths = verse_flat_tokens(surah_verse_tokens)
    # Global token stats.
    all_toks = [t for v in verses for t in v]
    tok_counts = Counter(all_toks)
    top_words = [w for w, _ in tok_counts.most_common(N_TOP_WORDS)]
    top_set = set(top_words)
    N_tokens = len(all_toks)

    # Observed adjacent pair counts within top-100 pairs (within-verse).
    obs_pairs = adjacent_pair_counts(verses, top_set)
    n_slots = adjacent_pair_slots(verses)

    # Expected under independence: E_ij = P(i) * P(j) * n_slots
    p_of: Dict[str, float] = {w: tok_counts[w] / N_tokens for w in top_words}
    surprising = []  # (pair, E, O)
    zero_expected_ge1 = 0
    # Also gather E values for all E>=1 pairs (regardless of O) for Poisson env.
    e_values_ge1 = []
    for i in top_words:
        for j in top_words:
            if i == j:
                continue
            E = p_of[i] * p_of[j] * n_slots
            O = obs_pairs.get((i, j), 0)
            if E >= 1.0:
                e_values_ge1.append(E)
                if O == 0:
                    zero_expected_ge1 += 1
                    surprising.append((i, j, E, O))
    surprising.sort(key=lambda t: -t[2])

    # Poisson-envelope null: under independence each pair (i,j) with E_ij
    # independently has P(O=0) = exp(-E_ij). Expected total surprising-zeros
    # = sum exp(-E_ij) over E_ij >= 1.
    mu_null = sum(math.exp(-E) for E in e_values_ge1)
    var_null = sum(math.exp(-E) * (1 - math.exp(-E)) for E in e_values_ge1)
    sd_null = math.sqrt(var_null)
    z_poisson = (zero_expected_ge1 - mu_null) / sd_null if sd_null > 0 else float("inf")
    # 1-sided upper-tail p via Gaussian tail approximation
    # (Poisson-sum CLT)
    import statistics
    # Use survival of normal distribution via error function
    p_poisson_upper = 0.5 * math.erfc(z_poisson / math.sqrt(2))

    # Auxiliary permutation null (secondary, 2-sided)
    null_counts: List[int] = []
    for _ in range(n_perm):
        shuf = all_toks.copy()
        rng.shuffle(shuf)
        idx = 0
        perm_verses: List[List[str]] = []
        for ln in v_lengths:
            perm_verses.append(shuf[idx:idx + ln])
            idx += ln
        perm_pairs = adjacent_pair_counts(perm_verses, top_set)
        cnt = 0
        for i in top_words:
            for j in top_words:
                if i == j:
                    continue
                if p_of[i] * p_of[j] * n_slots < 1.0:
                    continue
                if perm_pairs.get((i, j), 0) == 0:
                    cnt += 1
        null_counts.append(cnt)

    p_val_perm = two_sided_p(zero_expected_ge1, null_counts)

    return {
        "n_top_words": N_TOP_WORDS,
        "n_tokens": N_tokens,
        "n_adjacent_slots": n_slots,
        "n_candidate_ordered_pairs": N_TOP_WORDS * (N_TOP_WORDS - 1),
        "n_pairs_with_E_ge_1": len(e_values_ge1),
        "n_surprising_zero_absences_obs": zero_expected_ge1,
        "poisson_mu_null": mu_null,
        "poisson_sd_null": sd_null,
        "poisson_z": z_poisson,
        "poisson_p_upper_1sided": p_poisson_upper,
        "perm_null_mean": sum(null_counts) / len(null_counts),
        "perm_null_min": min(null_counts),
        "perm_null_max": max(null_counts),
        "perm_p_two_sided": p_val_perm,
        "pass_primary_alpha_bon_0125": p_poisson_upper < ALPHA_BON,
        "top_10_surprising": [
            {"pair_1": i, "pair_2": j, "expected": round(E, 3), "observed": O}
            for (i, j, E, O) in surprising[:10]
        ],
        "n_surprising_total_obs": len(surprising),
    }


# ---------------------------------------------------------------------------
# Cell D — muqaṭṭāʿat-presence patterns
# ---------------------------------------------------------------------------


def cell_d_compute(surah_verse_tokens: List[List[List[str]]]) -> dict:
    # For each surah, 14-bit presence vector for MUQ14.
    bit_of = {ch: i for i, ch in enumerate(MUQ14)}
    patterns: List[int] = []
    per_surah: List[dict] = []
    for s_idx, sv in enumerate(surah_verse_tokens):
        letters_present = set()
        for verse in sv:
            for tok in verse:
                for ch in tok:
                    if ch in bit_of:
                        letters_present.add(ch)
        mask = 0
        for ch in letters_present:
            mask |= (1 << bit_of[ch])
        patterns.append(mask)
        per_surah.append({
            "surah": s_idx + 1,
            "mask": mask,
            "n_muq_letters_present": bin(mask).count("1"),
            "absent_muq_letters": [ch for ch in MUQ14 if ch not in letters_present],
        })

    # How many distinct patterns, and how many 2^14 - present = absent.
    n_distinct = len(set(patterns))
    n_possible = 2 ** 14
    # Full-14 present
    full_mask = (1 << 14) - 1
    n_full = sum(1 for p in patterns if p == full_mask)

    # For each 14-letter subset that is the COMPLEMENT of the present-set
    # (i.e., the "which muq letters are absent" subset), count occurrences.
    # Singletons: count surahs missing exactly-one letter and which letter.
    singleton_missing: Counter = Counter()
    for mask in patterns:
        missing_bits = full_mask ^ mask
        if bin(missing_bits).count("1") == 1:
            for ch, b in bit_of.items():
                if missing_bits & (1 << b):
                    singleton_missing[ch] += 1
                    break

    # All observed patterns (keep ALL; there are 14 in practice)
    pattern_counts = Counter(patterns)
    top_patterns = pattern_counts.most_common()

    # Structured gap: are there muqaṭṭāʿat letters UNIVERSALLY present (in all 114)?
    universal_present = [ch for ch in MUQ14
                          if all(mask & (1 << bit_of[ch]) for mask in patterns)]
    never_present_in_any_surah = [ch for ch in MUQ14
                                    if not any(mask & (1 << bit_of[ch]) for mask in patterns)]

    return {
        "n_surahs": len(patterns),
        "n_possible_patterns": n_possible,
        "n_distinct_patterns_observed": n_distinct,
        "n_patterns_unused": n_possible - n_distinct,
        "n_surahs_full_14": n_full,
        "n_surahs_missing_exactly_1_muq_letter": sum(
            1 for m in patterns if bin(full_mask ^ m).count("1") == 1
        ),
        "most_common_patterns": [
            {"mask": mask, "present_letters": [ch for ch in MUQ14 if mask & (1 << bit_of[ch])],
             "count": cnt}
            for mask, cnt in top_patterns
        ],
        "singleton_missing_letters": dict(singleton_missing),
        "muq_letters_universally_present_114": universal_present,
        "muq_letters_never_present": never_present_in_any_surah,
        "per_surah_sample_short": [
            d for d in per_surah if d["n_muq_letters_present"] < 14
        ][:30],
    }


# ---------------------------------------------------------------------------
# MW-5 positive control
# ---------------------------------------------------------------------------


def mw5_positive_control(tokens: List[str], rng: random.Random, n_synth: int = 10) -> dict:
    """Verify shuffle-null letter-multiset generator.

    Synthetic text: draw N_letters letters from Quran's letter-multiset uniformly,
    then re-slice by token lengths. For each, compute absent-bigram and
    absent-trigram counts. These should approximately match the shuffle-null
    because the construction is the SAME (uniform permutation of multiset).
    """
    letter_stream = [ch for tok in tokens for ch in tok]
    token_lengths = [len(t) for t in tokens]
    abs_bi = []
    abs_tri = []
    for _ in range(n_synth):
        shuf = permute_letter_multiset(letter_stream, token_lengths, rng)
        cb = within_word_ngrams(shuf, 2)
        ct = within_word_ngrams(shuf, 3)
        abs_bi.append(len(absent_ngram_set(cb, 2)))
        abs_tri.append(len(absent_ngram_set(ct, 3)))
    return {
        "n_synth": n_synth,
        "synthetic_absent_bigrams": abs_bi,
        "synthetic_absent_trigrams": abs_tri,
        "synthetic_absent_bigrams_mean": sum(abs_bi) / len(abs_bi),
        "synthetic_absent_trigrams_mean": sum(abs_tri) / len(abs_tri),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    rng = random.Random(SEED)

    print("Loading Quran...")
    quran_full_text, surah_verse_tokens = load_quran_text()
    quran_tokens = quran_full_text.split()
    N_Q_letters = sum(len(t) for t in quran_tokens)
    print(f"Quran: {len(quran_tokens):,} tokens, {N_Q_letters:,} letters after normalization")

    # Load baselines
    print("Loading baselines...")
    baseline_dir = os.path.join(REPO, "data", "baseline-corpora", "raw")
    bukhari_text = load_baseline([os.path.join(baseline_dir, "bukhari-noquran.txt")])
    jahiz_text = load_baseline([os.path.join(baseline_dir, "jahiz-hayawan.txt")])
    mual_paths = [os.path.join(baseline_dir, f"muallaqa-{name}.txt") for name in
                   ["imru-al-qais", "tarafa", "zuhayr", "labid", "antara",
                    "amr-bin-kulthum", "harith"]]
    mual_paths = [p for p in mual_paths if os.path.exists(p)]
    muallaqat_text = load_baseline(mual_paths)

    bukhari_toks = truncate_to_letter_count(bukhari_text, N_Q_letters)
    jahiz_toks = truncate_to_letter_count(jahiz_text, N_Q_letters)
    # Muallaqat is only ~38K letters; we don't truncate upward (we use what's available)
    mual_toks = [t for t in muallaqat_text.split() if t]

    for name, toks in [("Bukhari", bukhari_toks), ("Jahiz", jahiz_toks),
                        ("Muallaqat", mual_toks)]:
        nl = sum(len(t) for t in toks)
        print(f"  {name}: {len(toks):,} tokens, {nl:,} letters")

    results: dict = {
        "meta": {
            "seed": SEED,
            "n_perm": N_PERM,
            "alpha_bon": ALPHA_BON,
            "bonferroni_k": 4,
            "bonferroni_family": "h-new-114-zero-set",
            "alphabet28": ALPHABET28,
            "muq14": MUQ14,
            "n_quran_tokens": len(quran_tokens),
            "n_quran_letters": N_Q_letters,
            "n_bukhari_tokens": len(bukhari_toks),
            "n_bukhari_letters": sum(len(t) for t in bukhari_toks),
            "n_jahiz_tokens": len(jahiz_toks),
            "n_jahiz_letters": sum(len(t) for t in jahiz_toks),
            "n_muallaqat_tokens": len(mual_toks),
            "n_muallaqat_letters": sum(len(t) for t in mual_toks),
        }
    }

    # --- Cell A: letter bigram ---
    print("\n=== Cell A — Letter-bigram absent-set ===")
    q_bi = within_word_ngrams(quran_tokens, 2)
    q_abs_bi = absent_ngram_set(q_bi, 2)
    print(f"Quran within-word bigram types present: {len(q_bi):,} / 784")
    print(f"Quran absent bigrams (zero-count): {len(q_abs_bi)}")

    # Baseline per-window absent-counts (PRIMARY: matched-Arabic-envelope)
    bukhari_win = sliding_windows_tokens(bukhari_text, N_Q_letters, n_windows=50)
    jahiz_win = sliding_windows_tokens(jahiz_text, N_Q_letters, n_windows=50)
    print(f"Bukhari length-matched windows: {len(bukhari_win)}")
    print(f"Jahiz length-matched windows: {len(jahiz_win)}")

    bu_bi_abs_per_window = [corpus_absent_count(w, 2) for w in bukhari_win]
    jh_bi_abs_per_window = [corpus_absent_count(w, 2) for w in jahiz_win]
    # Muallaqat — descriptive only (too short)
    mu_bi_abs = corpus_absent_count(mual_toks, 2)
    envelope_bi = bu_bi_abs_per_window + jh_bi_abs_per_window
    env_bi_mean = sum(envelope_bi) / len(envelope_bi)
    env_bi_sd = (sum((x - env_bi_mean) ** 2 for x in envelope_bi) / max(1, len(envelope_bi) - 1)) ** 0.5
    env_bi_min = min(envelope_bi)
    env_bi_max = max(envelope_bi)
    obs_bi = len(q_abs_bi)
    # z-score
    z_bi = (obs_bi - env_bi_mean) / (env_bi_sd + 1e-9) if env_bi_sd > 0 else float("inf")
    # PASS: Quran outside envelope range [min, max]
    outside_envelope = (obs_bi < env_bi_min or obs_bi > env_bi_max)
    print(f"Quran absent-bigrams: {obs_bi}")
    print(f"Matched-baseline envelope: Bukhari windows {bu_bi_abs_per_window}, Jahiz windows {jh_bi_abs_per_window}")
    print(f"  envelope: mean={env_bi_mean:.2f}, sd={env_bi_sd:.2f}, min={env_bi_min}, max={env_bi_max}")
    print(f"  z_A = {z_bi:.3f}; outside-envelope={outside_envelope}")
    print(f"  Muallaqat absent (descriptive, short ~30K letters): {mu_bi_abs}")

    # Shuffle-null MW-5 diagnostic (not primary PASS)
    print(f"Running {N_PERM} permutations for MW-5 shuffle-null diagnostic (Cell A)...")
    obs_bi_check, null_bi = perm_absent_counts(quran_tokens, 2, N_PERM, rng)
    assert obs_bi_check == obs_bi
    p_bi_shuf = two_sided_p(obs_bi, null_bi)
    null_mean_bi = sum(null_bi) / len(null_bi)
    print(f"  shuffle-null: mean={null_mean_bi:.2f}, min={min(null_bi)}, max={max(null_bi)}, p2s={p_bi_shuf:.6f}")

    results["cell_A"] = {
        "quran_absent_bigram_count": obs_bi,
        "baseline_envelope_bukhari_per_window": bu_bi_abs_per_window,
        "baseline_envelope_jahiz_per_window": jh_bi_abs_per_window,
        "baseline_envelope_mean": env_bi_mean,
        "baseline_envelope_sd": env_bi_sd,
        "baseline_envelope_min": env_bi_min,
        "baseline_envelope_max": env_bi_max,
        "z_vs_baseline_envelope": z_bi,
        "outside_envelope_min_max": outside_envelope,
        "primary_pass_alpha_bon_0125": outside_envelope and abs(z_bi) >= 2.5,
        "muallaqat_absent_bigram_count_descriptive": mu_bi_abs,
        "shuffle_null_mean": null_mean_bi,
        "shuffle_null_min": min(null_bi),
        "shuffle_null_max": max(null_bi),
        "shuffle_null_p_two_sided_diagnostic": p_bi_shuf,
        "quran_absent_bigrams": sorted(q_abs_bi),
    }

    # --- Cell B: letter trigram ---
    print("\n=== Cell B — Letter-trigram absent-set ===")
    q_tri = within_word_ngrams(quran_tokens, 3)
    q_abs_tri = absent_ngram_set(q_tri, 3)
    print(f"Quran within-word trigram types present: {len(q_tri):,} / 21,952")
    print(f"Quran absent trigrams (zero-count): {len(q_abs_tri):,}")

    bu_tri_abs_per_window = [corpus_absent_count(w, 3) for w in bukhari_win]
    jh_tri_abs_per_window = [corpus_absent_count(w, 3) for w in jahiz_win]
    mu_tri_abs = corpus_absent_count(mual_toks, 3)
    envelope_tri = bu_tri_abs_per_window + jh_tri_abs_per_window
    env_tri_mean = sum(envelope_tri) / len(envelope_tri)
    env_tri_sd = (sum((x - env_tri_mean) ** 2 for x in envelope_tri) / max(1, len(envelope_tri) - 1)) ** 0.5
    env_tri_min = min(envelope_tri)
    env_tri_max = max(envelope_tri)
    obs_tri = len(q_abs_tri)
    z_tri = (obs_tri - env_tri_mean) / (env_tri_sd + 1e-9) if env_tri_sd > 0 else float("inf")
    outside_envelope_tri = (obs_tri < env_tri_min or obs_tri > env_tri_max)
    print(f"Quran absent-trigrams: {obs_tri}")
    print(f"Matched-baseline envelope: Bukhari windows {bu_tri_abs_per_window}, Jahiz windows {jh_tri_abs_per_window}")
    print(f"  envelope: mean={env_tri_mean:.2f}, sd={env_tri_sd:.2f}, min={env_tri_min}, max={env_tri_max}")
    print(f"  z_B = {z_tri:.3f}; outside-envelope={outside_envelope_tri}")
    print(f"  Muallaqat absent (descriptive): {mu_tri_abs}")

    print(f"Running {N_PERM} permutations for MW-5 shuffle-null diagnostic (Cell B)...")
    obs_tri_check, null_tri = perm_absent_counts(quran_tokens, 3, N_PERM, rng)
    assert obs_tri_check == obs_tri
    p_tri_shuf = two_sided_p(obs_tri, null_tri)
    null_mean_tri = sum(null_tri) / len(null_tri)
    print(f"  shuffle-null: mean={null_mean_tri:.2f}, min={min(null_tri)}, max={max(null_tri)}, p2s={p_tri_shuf:.6f}")

    results["cell_B"] = {
        "quran_absent_trigram_count": obs_tri,
        "baseline_envelope_bukhari_per_window": bu_tri_abs_per_window,
        "baseline_envelope_jahiz_per_window": jh_tri_abs_per_window,
        "baseline_envelope_mean": env_tri_mean,
        "baseline_envelope_sd": env_tri_sd,
        "baseline_envelope_min": env_tri_min,
        "baseline_envelope_max": env_tri_max,
        "z_vs_baseline_envelope": z_tri,
        "outside_envelope_min_max": outside_envelope_tri,
        "primary_pass_alpha_bon_0125": outside_envelope_tri and abs(z_tri) >= 2.5,
        "muallaqat_absent_trigram_count_descriptive": mu_tri_abs,
        "shuffle_null_mean": null_mean_tri,
        "shuffle_null_min": min(null_tri),
        "shuffle_null_max": max(null_tri),
        "shuffle_null_p_two_sided_diagnostic": p_tri_shuf,
        # Store first 500 absent trigrams as a sample
        "quran_absent_trigrams_sample_500": sorted(q_abs_tri)[:500],
    }

    # --- Cell C: word-bigram surprising-absence ---
    print("\n=== Cell C — Word-bigram surprising-absence (top-100) ===")
    rng_c = random.Random(SEED + 1)
    cell_c_res = cell_c_compute(surah_verse_tokens, N_PERM, rng_c)
    print(f"Surprising-absence (O=0, E>=1) count: {cell_c_res['n_surprising_zero_absences_obs']}")
    print(f"  of {cell_c_res['n_pairs_with_E_ge_1']} candidate pairs with E>=1")
    print(f"Poisson μ_null={cell_c_res['poisson_mu_null']:.2f}, sd={cell_c_res['poisson_sd_null']:.2f}, z={cell_c_res['poisson_z']:.3f}")
    print(f"  POISSON 1-sided upper p: {cell_c_res['poisson_p_upper_1sided']:.6g}")
    print(f"Perm null mean: {cell_c_res['perm_null_mean']:.2f}, perm-2s-p: {cell_c_res['perm_p_two_sided']:.6f}")
    print("Top-10 surprising absent adjacencies:")
    for d in cell_c_res["top_10_surprising"]:
        print(f"  ({d['pair_1']}, {d['pair_2']}): E={d['expected']}, O={d['observed']}")

    results["cell_C"] = cell_c_res

    # --- Cell D: muqaṭṭāʿat presence patterns ---
    print("\n=== Cell D — Muqaṭṭāʿat-letter-presence patterns (descriptive) ===")
    cell_d_res = cell_d_compute(surah_verse_tokens)
    print(f"N distinct patterns observed: {cell_d_res['n_distinct_patterns_observed']} / {cell_d_res['n_possible_patterns']}")
    print(f"N surahs with full-14 present: {cell_d_res['n_surahs_full_14']}")
    print(f"N surahs missing exactly 1 muq letter: {cell_d_res['n_surahs_missing_exactly_1_muq_letter']}")
    print(f"Singleton-missing-letters: {cell_d_res['singleton_missing_letters']}")
    print(f"Muq letters universally present in all 114: {cell_d_res['muq_letters_universally_present_114']}")
    results["cell_D"] = cell_d_res

    # --- MW-5 positive control ---
    print("\n=== MW-5 Positive Control ===")
    rng_m = random.Random(SEED + 2)
    mw5 = mw5_positive_control(quran_tokens, rng_m, n_synth=10)
    print(f"Synthetic absent-bigrams mean: {mw5['synthetic_absent_bigrams_mean']:.2f}")
    print(f"Synthetic absent-trigrams mean: {mw5['synthetic_absent_trigrams_mean']:.2f}")
    print(f"Observed Quran absent-bigrams: {obs_bi} (vs synth ~ {mw5['synthetic_absent_bigrams_mean']:.0f})")
    print(f"Observed Quran absent-trigrams: {obs_tri} (vs synth ~ {mw5['synthetic_absent_trigrams_mean']:.0f})")
    # Positive control passes if synthetic absent-counts are CLOSE to shuffle-null mean
    mw5["shuffle_null_bigram_mean"] = null_mean_bi
    mw5["shuffle_null_trigram_mean"] = null_mean_tri
    mw5["pc_pass_bigram"] = abs(mw5["synthetic_absent_bigrams_mean"] - null_mean_bi) < 20
    mw5["pc_pass_trigram"] = abs(mw5["synthetic_absent_trigrams_mean"] - null_mean_tri) < 200
    results["mw5_positive_control"] = mw5

    # --- Summary ---
    results["summary"] = {
        "cell_A_obs": obs_bi,
        "cell_A_envelope_mean": env_bi_mean,
        "cell_A_envelope_min_max": [env_bi_min, env_bi_max],
        "cell_A_z_vs_baseline_envelope": z_bi,
        "cell_A_outside_envelope": outside_envelope,
        "cell_A_primary_pass": outside_envelope and abs(z_bi) >= 2.5,
        "cell_A_shuffle_diag_p": p_bi_shuf,
        "cell_B_obs": obs_tri,
        "cell_B_envelope_mean": env_tri_mean,
        "cell_B_envelope_min_max": [env_tri_min, env_tri_max],
        "cell_B_z_vs_baseline_envelope": z_tri,
        "cell_B_outside_envelope": outside_envelope_tri,
        "cell_B_primary_pass": outside_envelope_tri and abs(z_tri) >= 2.5,
        "cell_B_shuffle_diag_p": p_tri_shuf,
        "cell_C_obs": cell_c_res["n_surprising_zero_absences_obs"],
        "cell_C_poisson_mu": cell_c_res["poisson_mu_null"],
        "cell_C_poisson_z": cell_c_res["poisson_z"],
        "cell_C_poisson_p_upper": cell_c_res["poisson_p_upper_1sided"],
        "cell_C_primary_pass": cell_c_res["pass_primary_alpha_bon_0125"],
        "cell_C_perm_p2s_aux": cell_c_res["perm_p_two_sided"],
        "cell_D": "descriptive",
    }

    # Write JSON
    out_path = os.path.join(REPO, "findings", "phase-b-hypotheses", "csv", "h-new-114.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
