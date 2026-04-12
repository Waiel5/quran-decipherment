"""Palindrome hunt across every scale of the Quran.

Phase B novelty. Rules tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (real_words filter applied:
                   recitation-mark-only tokens dropped)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1 (the JSON's native state)
  verse_numbering: hafs-kufan
  abjad_table: mashriqi  (for category 5)
  null_model: not-applicable (we report raw counts + base-rate heuristics)

Writes intermediate tallies as JSON to /tmp/ so the markdown writer can
consume them deterministically.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words, is_letter, graphemes  # noqa: E402
from tools.gematria import word_value, ABJAD_MASHRIQI  # noqa: E402


OUT_DIR = "/tmp/palindrome-hunt"
os.makedirs(OUT_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Utility: strip a token to its Arabic letter graphemes only.
# ---------------------------------------------------------------------------


def letters_only(tok: str) -> str:
    return "".join(ch for ch in tok if is_letter(ch))


def is_palindrome(seq) -> bool:
    return list(seq) == list(reversed(list(seq)))


# ---------------------------------------------------------------------------
# Category 1 & 2: letter-palindrome words and near-palindromes.
# ---------------------------------------------------------------------------


def category_1_and_2(surahs) -> Dict:
    word_locations: Dict[str, List[str]] = defaultdict(list)
    word_count: Counter = Counter()

    for s in surahs:
        for v in s.verses:
            for tok in real_words(v.text):
                stripped = letters_only(tok)
                if not stripped:
                    continue
                word_locations[stripped].append(f"{s.id}:{v.id}")
                word_count[stripped] += 1

    palindromes: List[Tuple[str, int, List[str]]] = []
    near_palindromes: List[Tuple[str, int, List[str], str]] = []

    for w, n in word_count.items():
        if len(w) < 2:
            continue
        if is_palindrome(w):
            palindromes.append((w, n, word_locations[w]))
            continue
        # near-palindrome: distance-1 from a palindrome?
        # A single substitution flips w to reversed(w) only when the
        # mismatching positions form exactly one symmetric pair.
        rev = w[::-1]
        diffs = [i for i in range(len(w)) if w[i] != rev[i]]
        if diffs:
            # Symmetric diffs come in pairs (i, L-1-i). An edit distance
            # of 1 to a palindrome corresponds to exactly one such pair
            # (one substitution turns w into a palindrome). For odd-
            # length words the center counts separately: if only the
            # center differs, the word is already a palindrome.
            paired = set(tuple(sorted((i, len(w) - 1 - i))) for i in diffs)
            if len(paired) == 1:
                near_palindromes.append(
                    (w, n, word_locations[w], f"swap_pair={list(paired)[0]}")
                )

    palindromes.sort(key=lambda t: (-len(t[0]), -t[1]))
    near_palindromes.sort(key=lambda t: (-len(t[0]), -t[1]))
    return {
        "vocab_size": len(word_count),
        "palindromes": palindromes,
        "near_palindromes": near_palindromes,
    }


# ---------------------------------------------------------------------------
# Category 3: word-sequence palindromic verses.
# ---------------------------------------------------------------------------


def category_3(surahs) -> Dict:
    hits = []
    for s in surahs:
        for v in s.verses:
            toks = [letters_only(t) for t in real_words(v.text)]
            toks = [t for t in toks if t]
            if len(toks) < 2:
                continue
            if is_palindrome(toks):
                hits.append((s.id, v.id, toks))
    return {"verses": hits}


# ---------------------------------------------------------------------------
# Category 4: root-sequence palindromic verses (Leeds morphology).
# ---------------------------------------------------------------------------


def load_roots_by_verse() -> Dict[Tuple[int, int], List[str]]:
    """Return dict (surah, verse) -> list of roots in token order.

    We keep one root per token-index; if a token has multiple segments
    (e.g. prefix + stem + suffix), we pick the first segment that has a
    ROOT field. Tokens with no ROOT are retained as None so the list
    matches the Quran's word order; then the caller filters them.
    """
    path = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
    by_tok: Dict[Tuple[int, int, int], str] = {}

    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m:
                continue
            s = int(m.group(1))
            v = int(m.group(2))
            tok = int(m.group(3))
            root_m = re.search(r"ROOT:([^|]+)", features)
            if not root_m:
                continue
            key = (s, v, tok)
            # Keep the FIRST root seen for this token (stem usually comes
            # after prefix segments and has the root; but since different
            # segments rarely disagree, any is fine).
            if key not in by_tok:
                by_tok[key] = root_m.group(1)

    # Now project into ordered lists per verse.
    verse_roots: Dict[Tuple[int, int], List[str]] = defaultdict(list)
    for (s, v, tok), r in sorted(by_tok.items()):
        verse_roots[(s, v)].append(r)
    return verse_roots


def category_4(verse_roots) -> Dict:
    hits = []
    for (s, v), roots in verse_roots.items():
        if len(roots) < 2:
            continue
        if is_palindrome(roots):
            hits.append((s, v, roots))
    hits.sort(key=lambda t: -len(t[2]))
    return {"verses": hits}


# ---------------------------------------------------------------------------
# Category 5: abjad-sequence palindromic verses.
# ---------------------------------------------------------------------------


def category_5(surahs) -> Dict:
    hits = []
    for s in surahs:
        for v in s.verses:
            toks = [letters_only(t) for t in real_words(v.text)]
            toks = [t for t in toks if t]
            vals = [word_value(t, "mashriqi") for t in toks]
            if len(vals) < 2:
                continue
            if is_palindrome(vals):
                hits.append((s.id, v.id, vals, toks))
    hits.sort(key=lambda h: -len(h[2]))
    return {"verses": hits}


# ---------------------------------------------------------------------------
# Category 6: letter-palindromic substrings spanning word boundaries.
# ---------------------------------------------------------------------------


def longest_palindromic_substring(s: str) -> Tuple[int, int, str]:
    """Manacher-like expand-around-center. Returns (start, length, substr)."""
    if not s:
        return (0, 0, "")
    best_l = 0
    best_start = 0
    for i in range(len(s)):
        # odd length center
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        length = r - l - 1
        if length > best_l:
            best_l = length
            best_start = l + 1
        # even length center
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        length = r - l - 1
        if length > best_l:
            best_l = length
            best_start = l + 1
    return (best_start, best_l, s[best_start : best_start + best_l])


def category_6(surahs, min_len: int = 7) -> Dict:
    long_pals: List[Dict] = []
    per_verse_longest: List[Tuple[int, int, int, str]] = []
    for s in surahs:
        for v in s.verses:
            continuous = "".join(ch for ch in v.text if is_letter(ch))
            start, length, sub = longest_palindromic_substring(continuous)
            per_verse_longest.append((s.id, v.id, length, sub))
            if length >= min_len:
                long_pals.append(
                    {
                        "surah": s.id,
                        "verse": v.id,
                        "length": length,
                        "substr": sub,
                        "verse_letters": continuous,
                        "start": start,
                    }
                )
    long_pals.sort(key=lambda d: -d["length"])
    per_verse_longest.sort(key=lambda t: -t[2])
    return {"long_pals": long_pals, "top_per_verse": per_verse_longest[:20]}


# ---------------------------------------------------------------------------
# Category 7: per-surah structural palindromic scores.
# ---------------------------------------------------------------------------


def category_7(surahs, verse_roots) -> Dict:
    results = []
    for s in surahs:
        n = len(s.verses)
        if n < 2:
            continue
        word_lens = []
        letter_lens = []
        abjad_totals = []
        first_root = []
        for v in s.verses:
            toks = [letters_only(t) for t in real_words(v.text)]
            toks = [t for t in toks if t]
            word_lens.append(len(toks))
            letter_lens.append(sum(len(t) for t in toks))
            abjad_totals.append(sum(word_value(t, "mashriqi") for t in toks))
            roots = verse_roots.get((s.id, v.id), [])
            first_root.append(roots[0] if roots else None)

        def palindrome_score(seq, numeric=True):
            matches = 0
            pairs = n // 2
            if pairs == 0:
                return (0, 0)
            for i in range(pairs):
                a = seq[i]
                b = seq[n - 1 - i]
                if numeric:
                    if a == b:
                        matches += 1
                else:
                    if a is not None and a == b:
                        matches += 1
            return (matches, pairs)

        wm, wp = palindrome_score(word_lens, True)
        lm, lp = palindrome_score(letter_lens, True)
        am, ap = palindrome_score(abjad_totals, True)
        rm, rp = palindrome_score(first_root, False)

        results.append(
            {
                "surah": s.id,
                "n_verses": n,
                "word_len_score": (wm, wp),
                "letter_len_score": (lm, lp),
                "abjad_total_score": (am, ap),
                "first_root_score": (rm, rp),
            }
        )
    return {"per_surah": results}


# ---------------------------------------------------------------------------
# Category 8: surah-sequence mirror symmetry.
# ---------------------------------------------------------------------------


def category_8(surahs) -> Dict:
    n = len(surahs)
    lengths = [len(s.verses) for s in surahs]
    letter_counts = []
    abjad_totals = []
    for s in surahs:
        text = " ".join(v.text for v in s.verses)
        text_letters = "".join(ch for ch in text if is_letter(ch))
        letter_counts.append(len(text_letters))
        abjad_totals.append(sum(word_value(t, "mashriqi") for t in real_words(text)))

    def pal_score(seq):
        matches = 0
        pairs = n // 2
        for i in range(pairs):
            if seq[i] == seq[n - 1 - i]:
                matches += 1
        return matches, pairs

    lm, lp = pal_score(lengths)
    letm, letp = pal_score(letter_counts)
    am, ap = pal_score(abjad_totals)

    # Best-mirror-center search: slide a candidate center c in [0, n-1]
    # and count matches on pairs (c-k, c+k). Report the center that
    # maximizes matches for each feature.
    def best_center(seq):
        best = (0, 0, 0)  # (center, matches, pairs)
        for c in range(1, n - 1):
            k = min(c, n - 1 - c)
            matches = 0
            for kk in range(1, k + 1):
                if seq[c - kk] == seq[c + kk]:
                    matches += 1
            if matches > best[1]:
                best = (c, matches, k)
        return best

    return {
        "n_surahs": n,
        "length_palindromicity": (lm, lp),
        "letter_palindromicity": (letm, letp),
        "abjad_palindromicity": (am, ap),
        "best_center_length": best_center(lengths),
        "best_center_letters": best_center(letter_counts),
        "best_center_abjad": best_center(abjad_totals),
        "lengths": lengths,
    }


# ---------------------------------------------------------------------------
# Category 9: whole-Quran 6236-long verse-letter-count sequence.
# ---------------------------------------------------------------------------


def longest_palindromic_subsequence_numeric(seq, cap_len=None):
    """Standard O(n^2) DP — but 6236^2 ≈ 39M, tight but doable."""
    n = len(seq)
    if cap_len is not None:
        n = min(n, cap_len)
        seq = seq[:n]
    # memory: 2 rows only
    prev = [0] * (n + 1)
    cur = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        cur = [0] * (n + 1)
        cur[i] = 1
        for j in range(i + 1, n):
            if seq[i] == seq[j]:
                cur[j] = prev[j - 1] + 2
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[n - 1]


def longest_palindromic_substring_numeric(seq):
    """Longest contiguous palindromic subrun. O(n^2) expand-around-center."""
    n = len(seq)
    best = (0, 0)  # (start, length)
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and seq[l] == seq[r]:
            l -= 1
            r += 1
        length = r - l - 1
        if length > best[1]:
            best = (l + 1, length)
        l, r = i, i + 1
        while l >= 0 and r < n and seq[l] == seq[r]:
            l -= 1
            r += 1
        length = r - l - 1
        if length > best[1]:
            best = (l + 1, length)
    return best


def category_9(surahs) -> Dict:
    seq: List[int] = []
    index: List[Tuple[int, int]] = []
    for s in surahs:
        for v in s.verses:
            letters = sum(1 for ch in v.text if is_letter(ch))
            seq.append(letters)
            index.append((s.id, v.id))

    # is the whole sequence palindromic?
    is_whole_pal = seq == seq[::-1]

    # longest contiguous palindromic subrun
    start, length = longest_palindromic_substring_numeric(seq)
    sub = seq[start : start + length]
    sub_loc_start = index[start]
    sub_loc_end = index[start + length - 1] if length > 0 else (0, 0)

    return {
        "total_verses": len(seq),
        "is_whole_palindromic": is_whole_pal,
        "longest_contiguous_palindromic_subrun_start_idx": start,
        "longest_contiguous_palindromic_subrun_length": length,
        "subrun_values": sub,
        "subrun_start_loc": sub_loc_start,
        "subrun_end_loc": sub_loc_end,
    }


# ---------------------------------------------------------------------------
# Category 10: semantic chiastic heuristic.
# ---------------------------------------------------------------------------

STOP = set(
    "the a an of to and in is for on it that this at as be by from his her their with"
    " him them they we you i our me my your not no but or so was were has have had".split()
)


def toks_en(text: str) -> List[str]:
    return [w for w in re.findall(r"[a-zA-Z]+", text.lower()) if w not in STOP]


def load_sahih() -> Dict[Tuple[int, int], str]:
    path = "/Users/grey/Downloads/quran/data/translations/en.sahih.txt-2.txt"
    out: Dict[Tuple[int, int], str] = {}
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("|", 2)
            if len(parts) != 3:
                continue
            try:
                s = int(parts[0])
                v = int(parts[1])
            except ValueError:
                continue
            out[(s, v)] = parts[2]
    return out


# Minimal antonym dictionary for inverse/semantic-mirror detection.
ANTONYMS: Dict[str, List[str]] = {
    "day": ["night"],
    "night": ["day"],
    "heaven": ["earth"],
    "heavens": ["earth"],
    "sky": ["earth"],
    "earth": ["heaven", "heavens", "sky"],
    "life": ["death"],
    "living": ["dead"],
    "alive": ["dead"],
    "death": ["life"],
    "dead": ["alive", "living"],
    "light": ["darkness", "dark"],
    "dark": ["light"],
    "darkness": ["light"],
    "first": ["last"],
    "last": ["first"],
    "beginning": ["end"],
    "end": ["beginning"],
    "good": ["evil", "bad"],
    "evil": ["good"],
    "bad": ["good"],
    "believers": ["disbelievers"],
    "believer": ["disbeliever"],
    "believed": ["disbelieved"],
    "believe": ["disbelieve"],
    "disbelievers": ["believers"],
    "disbeliever": ["believer"],
    "disbelieved": ["believed"],
    "disbelieve": ["believe"],
    "paradise": ["hell", "hellfire"],
    "hell": ["paradise"],
    "hellfire": ["paradise"],
    "reward": ["punishment"],
    "punishment": ["reward"],
    "guidance": ["astray", "misguidance"],
    "astray": ["guidance"],
    "truth": ["falsehood", "lie"],
    "falsehood": ["truth"],
    "lie": ["truth"],
    "right": ["wrong"],
    "wrong": ["right"],
    "patient": ["impatient"],
    "rich": ["poor"],
    "poor": ["rich"],
    "high": ["low"],
    "low": ["high"],
}


def category_10(surahs, sahih) -> Dict:
    """For each surah, check first-third verses against last-third verses
    for semantic inverse signals (shared theme-noun + opposite polarity).
    """
    hits = []
    for s in surahs:
        n = len(s.verses)
        if n < 6:
            continue
        first_third = [(i, s.verses[i].id) for i in range(max(1, n // 3))]
        last_third = [(i, s.verses[i].id) for i in range(n - max(1, n // 3), n)]
        for i_a, v_a in first_third:
            a_text = sahih.get((s.id, v_a), "")
            if not a_text:
                continue
            a_toks = set(toks_en(a_text))
            for i_b, v_b in last_third:
                if i_b <= i_a:
                    continue
                b_text = sahih.get((s.id, v_b), "")
                if not b_text:
                    continue
                b_toks = set(toks_en(b_text))
                # inverse hits
                inverses = []
                for w in a_toks:
                    for anti in ANTONYMS.get(w, []):
                        if anti in b_toks:
                            inverses.append((w, anti))
                if len(inverses) >= 2:
                    hits.append(
                        {
                            "surah": s.id,
                            "a": v_a,
                            "b": v_b,
                            "a_text": a_text,
                            "b_text": b_text,
                            "inverses": inverses,
                        }
                    )
    return {"candidates": hits}


# ---------------------------------------------------------------------------
# Runner.
# ---------------------------------------------------------------------------


def main():
    print("loading quran...", flush=True)
    surahs = load_quran("no-tashkeel")

    print("loading roots...", flush=True)
    verse_roots = load_roots_by_verse()

    print("category 1 & 2 (letter palindromes & near)...", flush=True)
    c12 = category_1_and_2(surahs)
    print(
        f"  vocab={c12['vocab_size']}, palindromes={len(c12['palindromes'])}, "
        f"near={len(c12['near_palindromes'])}",
        flush=True,
    )

    print("category 3 (word-sequence palindromic verses)...", flush=True)
    c3 = category_3(surahs)
    print(f"  hits={len(c3['verses'])}", flush=True)

    print("category 4 (root-sequence palindromic verses)...", flush=True)
    c4 = category_4(verse_roots)
    print(f"  hits={len(c4['verses'])}", flush=True)

    print("category 5 (abjad-sequence palindromic verses)...", flush=True)
    c5 = category_5(surahs)
    print(f"  hits={len(c5['verses'])}", flush=True)

    print("category 6 (letter palindromes across word boundaries)...", flush=True)
    c6 = category_6(surahs, min_len=7)
    print(
        f"  long hits={len(c6['long_pals'])}; "
        f"longest={c6['long_pals'][0] if c6['long_pals'] else None}",
        flush=True,
    )

    print("category 7 (per-surah structural palindromicity)...", flush=True)
    c7 = category_7(surahs, verse_roots)

    print("category 8 (surah-sequence mirror symmetry)...", flush=True)
    c8 = category_8(surahs)

    print("category 9 (whole-quran verse-letter-count palindromic subrun)...", flush=True)
    c9 = category_9(surahs)
    print(
        f"  whole? {c9['is_whole_palindromic']}; "
        f"longest contiguous = {c9['longest_contiguous_palindromic_subrun_length']} "
        f"at idx {c9['longest_contiguous_palindromic_subrun_start_idx']}",
        flush=True,
    )

    print("category 10 (semantic chiasmus heuristic)...", flush=True)
    sahih = load_sahih()
    c10 = category_10(surahs, sahih)
    print(f"  candidate pairs={len(c10['candidates'])}", flush=True)

    out = {
        "c1_c2": {
            "vocab_size": c12["vocab_size"],
            "palindromes": c12["palindromes"],
            "near_palindromes": c12["near_palindromes"][:60],
            "near_palindromes_total": len(c12["near_palindromes"]),
        },
        "c3": c3,
        "c4": {
            "count": len(c4["verses"]),
            "top": c4["verses"][:20],
        },
        "c5": {
            "count": len(c5["verses"]),
            "top": c5["verses"][:30],
        },
        "c6": {
            "long_pal_count": len(c6["long_pals"]),
            "long_pals": c6["long_pals"][:25],
            "top_per_verse": c6["top_per_verse"],
        },
        "c7": c7,
        "c8": c8,
        "c9": c9,
        "c10": {
            "count": len(c10["candidates"]),
            "top": c10["candidates"][:30],
        },
    }

    with open(os.path.join(OUT_DIR, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
    print(f"wrote {OUT_DIR}/results.json", flush=True)


if __name__ == "__main__":
    main()
