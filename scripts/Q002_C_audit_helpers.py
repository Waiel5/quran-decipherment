#!/usr/bin/env python3
"""
Q002_C_audit_helpers.py — empirical helpers for the Q 2 classical-claims audit.

NOT a pre-registered novel test — these are data-extraction queries
documented in §05 (classical-claims-audit). Stdlib only.
"""
from __future__ import annotations
import json, re, math
from pathlib import Path
from collections import Counter

ROOT = Path("/Users/grey/Downloads/quran")
SAJDA_RE = re.compile(r"[ۖ-ۭۚۛۜ]")
WS_RE    = re.compile(r"\s+")

def _norm(text): return WS_RE.sub(" ", SAJDA_RE.sub(" ", text)).strip()
def _verse_words(text): return [w for w in _norm(text).split() if w]


def main():
    qnt = json.loads((ROOT / "quran-text" / "quran-no-tashkeel.json").read_text())
    print(f"loaded {len(qnt)} surahs")

    # ===== 1. Cow vocabulary density (claim #10) =====
    # Q 2 is named "the Cow" (al-Baqara) from verses 67-71 narrative (5 verses).
    # Test: is "cow"-vocabulary (baqara, ʿijl) dense in Q 2 vs corpus?
    cow_roots = ['بقرة', 'بقر', 'بقرات', 'البقرة']  # surface forms of baqara
    ijl_roots = ['عجل', 'العجل', 'عجلا', 'عجلاً']    # surface forms of ʿijl (calf)

    def count_in_surah(s, terms):
        cnt = 0
        for v in s["verses"]:
            words = _verse_words(v["text"])
            for w in words:
                if w in terms:
                    cnt += 1
        return cnt

    q2 = next(s for s in qnt if s["id"] == 2)
    q2_total_words = sum(len(_verse_words(v["text"])) for v in q2["verses"])
    q2_baqara_count = count_in_surah(q2, cow_roots)
    q2_ijl_count = count_in_surah(q2, ijl_roots)

    corpus_total_words = sum(len(_verse_words(v["text"])) for s in qnt for v in s["verses"])
    corpus_baqara = sum(count_in_surah(s, cow_roots) for s in qnt)
    corpus_ijl = sum(count_in_surah(s, ijl_roots) for s in qnt)

    q2_baqara_density = q2_baqara_count / q2_total_words if q2_total_words else 0
    corpus_baqara_density = corpus_baqara / corpus_total_words if corpus_total_words else 0

    print(f"\n=== Cow-vocabulary density (claim #10) ===")
    print(f"Q 2 total words: {q2_total_words}")
    print(f"Q 2 'baqara/baqar/...' surface-count: {q2_baqara_count}, density: {q2_baqara_density*1000:.4f}/1000 words")
    print(f"Corpus 'baqara' surface-count: {corpus_baqara}, density: {corpus_baqara_density*1000:.4f}/1000 words")
    print(f"Q 2 'ʿijl' surface-count: {q2_ijl_count}")
    print(f"Corpus 'ʿijl' surface-count: {corpus_ijl}")
    print(f"Q 2 fraction of corpus baqara-instances: {q2_baqara_count}/{corpus_baqara} = {q2_baqara_count/max(corpus_baqara,1):.2%}")
    print(f"Q 2 fraction of corpus ʿijl-instances: {q2_ijl_count}/{corpus_ijl} = {q2_ijl_count/max(corpus_ijl,1):.2%}")
    print(f"Q 2 word-share of corpus: {q2_total_words/corpus_total_words:.2%}")

    # ===== 2. Q 2:185 position (claim #7) =====
    # Position of verse 185 in Q 2 (286 verses).
    print(f"\n=== Q 2:185 position (claim #7) ===")
    print(f"Position 185 / 286 = {185/286:.4f}")
    print(f"Distance from center (143) = {abs(185 - 143.5):.1f} verses")
    # Compare to other surah-positional ratios. Is 0.647 noteworthy?
    # Test if 185/286 ≈ 2/π ≈ 0.6366, e ≈ 0.6321, golden = 0.618...
    # No simple constant; 185/286 ≈ 0.6469. Just record.

    # ===== 3. Per-block content cohesion (novel) =====
    # Q 2 blocks per overview: A 1-39, B 40-103, C 104-141, D 142-176, E 177-242, F 243-260, G 261-283, H 284-286
    print(f"\n=== Per-block content cohesion (Q 2) ===")
    blocks = [("A", 1, 39), ("B", 40, 103), ("C", 104, 141), ("D", 142, 176),
              ("E", 177, 242), ("F", 243, 260), ("G", 261, 283), ("H", 284, 286)]

    def cos_set(A, B):
        if not A or not B: return 0.0
        return len(A & B) / math.sqrt(len(A) * len(B))

    block_token_sets = []
    for (name, a, b) in blocks:
        toks = set()
        for v in q2["verses"]:
            if a <= v["id"] <= b:
                toks |= set(_verse_words(v["text"]))
        block_token_sets.append((name, a, b, toks))

    print(f"{'Block':<6}{'verses':<12}{'unique_tokens':<16}{'mean_cos_to_other_blocks':<20}")
    for i, (n, a, b, toks) in enumerate(block_token_sets):
        cos_others = []
        for j, (n2, a2, b2, t2) in enumerate(block_token_sets):
            if i == j: continue
            cos_others.append(cos_set(toks, t2))
        mean_cos = sum(cos_others) / len(cos_others)
        print(f"{n:<6}{a}-{b:<8}{len(toks):<16}{mean_cos:.4f}")

    # internal cohesion = mean cosine between consecutive verses within block
    print(f"\n{'Block':<6}{'verses':<12}{'mean_internal_cos':<20}")
    for (n, a, b) in blocks:
        verse_sets = [set(_verse_words(v["text"])) for v in q2["verses"] if a <= v["id"] <= b]
        if len(verse_sets) < 2:
            continue
        cosines = [cos_set(verse_sets[i], verse_sets[i+1]) for i in range(len(verse_sets)-1)]
        mean_cos = sum(cosines) / len(cosines)
        print(f"{n:<6}{a}-{b:<8}{mean_cos:.4f}")

    # ===== 4. al-Biqāʿī "Q 2 vocabulary distinctness" (claim #4) =====
    # Q 2 vs corpus root frequency from QAC roots (use root-stats.csv if available)
    print(f"\n=== Q 2 vocabulary 'foundational' fraction (claim #4) ===")
    # Use surface-word-token frequency
    from collections import Counter
    q2_words = []
    for v in q2["verses"]:
        q2_words.extend(_verse_words(v["text"]))
    q2_freq = Counter(q2_words)
    corpus_words = []
    for s in qnt:
        for v in s["verses"]:
            corpus_words.extend(_verse_words(v["text"]))
    corpus_freq = Counter(corpus_words)

    # Top-20 most frequent words in Q 2
    print("Top-15 surface words in Q 2:")
    for w, c in q2_freq.most_common(15):
        print(f"  '{w}': {c} (Q 2) / {corpus_freq[w]} (corpus) — Q 2 share: {c/corpus_freq[w]:.1%}")

    # Q 2 unique-vocabulary share of corpus
    corpus_vocab = set(corpus_words)
    q2_vocab = set(q2_words)
    print(f"\nQ 2 vocabulary size (unique surface forms): {len(q2_vocab)}")
    print(f"Corpus vocabulary size: {len(corpus_vocab)}")
    print(f"Q 2 vocab as % of corpus vocab: {len(q2_vocab)/len(corpus_vocab):.1%}")
    # What % of Q 2's vocab is unique to Q 2?
    other_words = set()
    for s in qnt:
        if s["id"] == 2: continue
        for v in s["verses"]:
            other_words |= set(_verse_words(v["text"]))
    q2_unique = q2_vocab - other_words
    print(f"Q 2 words found ONLY in Q 2 (hapax-Q2): {len(q2_unique)} ({len(q2_unique)/len(q2_vocab):.1%} of Q 2 vocab)")

    # ===== 5. Q 2 closing — "ALM open + forgiveness close" (claim #8) =====
    print(f"\n=== Q 2 opening / closing (claim #8) ===")
    print(f"Q 2:1: '{q2['verses'][0]['text']}'")
    print(f"Q 2:286 (last): '{q2['verses'][-1]['text']}'")
    last = q2["verses"][-1]["text"]
    # Look for forgiveness-related roots: g-f-r, t-w-b, ʿ-f-w
    forgiveness_terms = ['اغفر', 'الغفور', 'الغفار', 'تب', 'التواب', 'العفو', 'فاعف', 'وارحمنا']
    found = [t for t in forgiveness_terms if t in last]
    print(f"Forgiveness-words found in Q 2:286: {found}")

    # ===== 6. Q 2 ends with "al-kāfirīn" (claim #9) =====
    last_words = _verse_words(last)
    print(f"Q 2:286 final 5 words: {last_words[-5:]}")

    # ===== 7. Q 2 word count totals (claim #6) =====
    print(f"\n=== Q 2 word count factorisation (claim #6) ===")
    # Multiple narrations of Q 2 word count: 6,121 / 6,144 / 6,221 / etc.
    # Empirical no-tashkeel count:
    print(f"Q 2 empirical word count (no-tashkeel, sajda-stripped): {q2_total_words}")
    # Factor 6,630 (overview-cited classical narration):
    n = 6630
    print(f"Classical narration count {n}: factors = ", end="")
    factors = []
    x = n
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        while x % p == 0:
            factors.append(p); x //= p
    if x > 1: factors.append(x)
    print(factors, "; product:", 1)
    prod = 1
    for f in factors: prod *= f
    print(f"product check: {prod}")


if __name__ == "__main__":
    main()
