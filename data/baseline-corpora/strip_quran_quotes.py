#!/usr/bin/env python3
"""
Strip Quranic quotations from Bukhari (and any other corpus).

Approach: build a set of all Quran word-trigrams, then walk through the
target corpus and remove any token whose preceding+self+following trigram
is in the Quran trigram set. This is conservative — we drop tokens, not
trigrams — but it suffices to deplete the Quran-overlap signal.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from analyze import load_quran_text, normalize, tokenize

RAW = Path("/Users/grey/Downloads/quran/data/baseline-corpora/raw")


def trigrams(toks: list[str]) -> set[tuple[str, str, str]]:
    return {(toks[i], toks[i+1], toks[i+2]) for i in range(len(toks) - 2)}


def strip_quran(corpus_text: str, quran_trigrams: set) -> tuple[list[str], int]:
    norm = normalize(corpus_text)
    toks = tokenize(norm)
    keep = [True] * len(toks)
    dropped = 0
    for i in range(1, len(toks) - 1):
        tri = (toks[i-1], toks[i], toks[i+1])
        if tri in quran_trigrams:
            for j in (i-1, i, i+1):
                if keep[j]:
                    keep[j] = False
                    dropped += 1
    out = [t for t, k in zip(toks, keep) if k]
    return out, dropped


def main():
    print("Loading Quran...", file=sys.stderr)
    q_text = load_quran_text()
    q_toks = tokenize(normalize(q_text))
    q_tri = trigrams(q_toks)
    print(f"Quran trigrams: {len(q_tri)}", file=sys.stderr)

    targets = ["bukhari.txt"]
    for fname in targets:
        path = RAW / fname
        text = path.read_text(encoding="utf-8")
        out_toks, dropped = strip_quran(text, q_tri)
        out_text = " ".join(out_toks)
        out_path = RAW / fname.replace(".txt", "-noquran.txt")
        out_path.write_text(out_text, encoding="utf-8")
        orig_n = len(tokenize(normalize(text)))
        print(f"  {fname}: {orig_n} -> {len(out_toks)} tokens "
              f"(dropped {dropped} = {dropped/orig_n*100:.1f}%)")
        print(f"  saved {out_path.name}")


if __name__ == "__main__":
    main()
