#!/usr/bin/env python3
"""
Q060-F-04 — uswa hasana CORPUS-EXACT 3-instance + Q 33↔Q 60 paired-exemplar.

Pre-reg SHA256: 1754e381458e58b6458ee9190950c488cb63c0a35d252d703596e4fedf7a0b7d

Hypotheses:
  H1a: pattern 'أسوة حسنة' is corpus-EXACT to 3 verses across 2 surahs:
       Q 33:21 + Q 60:4 + Q 60:6.
  H1b: Q 33:21 and Q 60:6 share a verbatim ≥7-word continuous phrase.

Decision rule: CORPUS-EXACT 3-instance paired-exemplar architecture if both pass.
"""
import json
import re
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PREREG_SHA = "1754e381458e58b6458ee9190950c488cb63c0a35d252d703596e4fedf7a0b7d"

PAT_USWA_HASANA = re.compile(r"أسوة\s+حسنة")

def verify_prereg_sha(prereg_path):
    h = hashlib.sha256(prereg_path.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        raise RuntimeError(f"Pre-reg SHA mismatch: expected {PREREG_SHA}, got {h}")
    return h

def lcs(s1, s2):
    """Longest common substring (chars)."""
    m, n = len(s1), len(s2)
    longest = 0
    bx = 0
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
                if table[i + 1][j + 1] > longest:
                    longest = table[i + 1][j + 1]
                    bx = i + 1
    return s1[bx - longest:bx], longest

def main():
    prereg_path = REPO_ROOT / "surahs" / "Q060-al-mumtahana" / "preregs" / "Q060-F-04-uswa-hasana-paired-exemplar-prereg.md"
    sha_check = verify_prereg_sha(prereg_path)
    print(f"Pre-reg SHA verified: {sha_check[:16]}...")

    text_path = REPO_ROOT / "quran-text" / "quran-no-tashkeel.json"
    data = json.load(open(text_path))

    hits = []
    for surah in data:
        for v in surah["verses"]:
            if PAT_USWA_HASANA.search(v["text"]):
                hits.append({"surah": surah["id"], "verse": v["id"], "text": v["text"]})

    print(f"\nuswa hasana corpus instances: {len(hits)}")
    for h in hits:
        print(f"  Q {h['surah']}:{h['verse']}")

    # H1a check
    expected_locations = {(33, 21), (60, 4), (60, 6)}
    actual_locations = {(h["surah"], h["verse"]) for h in hits}
    h1a_pass = (len(hits) == 3) and (actual_locations == expected_locations)
    print(f"H1a verdict: {'PASS' if h1a_pass else 'NULL'}")

    # H1b: LCS Q 33:21 ↔ Q 60:6
    q33_v21 = next(v["text"] for v in data[32]["verses"] if v["id"] == 21)
    q60_v6 = next(v["text"] for v in data[59]["verses"] if v["id"] == 6)
    shared, n_chars = lcs(q33_v21, q60_v6)
    n_words = len(shared.strip().split())
    print(f"\nQ 33:21 ↔ Q 60:6 LCS: '{shared.strip()}'")
    print(f"  chars: {n_chars}, words: {n_words}")
    h1b_pass = n_words >= 7
    print(f"H1b verdict: {'PASS' if h1b_pass else 'NULL'}")

    overall = (
        "CORPUS-EXACT 3-instance paired-exemplar architecture (Muhammad↔Ibrahim)"
        if (h1a_pass and h1b_pass)
        else "PARTIAL"
    )
    print(f"\nOverall: {overall}")

    return {
        "h1a_pass": h1a_pass,
        "h1b_pass": h1b_pass,
        "shared_block": shared.strip(),
        "shared_words": n_words,
        "verdict": overall,
    }

if __name__ == "__main__":
    main()
