#!/usr/bin/env python3
"""
Q008-F-02 — Q 8:17 yaqīn-formula corpus-singleton test.

Pre-reg SHA: 07b8e87374de1e7a5733169b78a1fc0aaa773abfac7cdbf922de336df11c1f20
Seed: 20260509
"""
import json
import hashlib
import re
from pathlib import Path

EXPECTED_PREREG_SHA = "07b8e87374de1e7a5733169b78a1fc0aaa773abfac7cdbf922de336df11c1f20"
PREREG_PATH = Path(__file__).parent.parent / "preregs" / "Q008-F-02-yaqin-formula-prereg.md"
SEED = 20260509
ALPHA_BON = 0.025

# Verify pre-reg SHA at runtime
with open(PREREG_PATH, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_PREREG_SHA, f"SHA mismatch: expected {EXPECTED_PREREG_SHA}, got {actual}"

# Load corpus
QURAN_ROOT = Path('/Users/grey/Downloads/quran')
with open(QURAN_ROOT / 'quran-text/quran-no-tashkeel.json') as f:
    quran = json.load(f)

# Strict pattern: (و|ف)?ما + V + (إذ|اذ) + V (same surface form) + (...)*0-3 + و?لكنّ?
# We use group capture to enforce V₁ == V₂ via a backreference.
strict_re = re.compile(r'(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)(?:\s+\S+){0,3}\s+و?لكنّ?')
loose_re = re.compile(r'(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)')

strict_hits = []  # (surah, verse, text, V1, V2)
loose_hits = []
strict_v_identical = []

for s in quran:
    for v in s['verses']:
        text = v['text']
        # Strict (V₁=V₂ enforced post-match)
        for m in strict_re.finditer(text):
            v1, v2 = m.group(1), m.group(2)
            loose_hits.append((s['id'], v['id'], text, v1, v2))
            if v1 == v2:
                strict_v_identical.append((s['id'], v['id'], text, v1))
            strict_hits.append((s['id'], v['id'], text, v1, v2))
        # Loose pattern (without wa-lākin requirement)
        for m in loose_re.finditer(text):
            v1, v2 = m.group(1), m.group(2)
            # Don't double-count strict hits
            already = any(h[0] == s['id'] and h[1] == v['id'] for h in loose_hits)
            if not already:
                loose_hits.append((s['id'], v['id'], text, v1, v2))

# Filter strict_v_identical for unique (s, v) tuples
strict_v_identical_unique = list({(s, v): (s, v, t, vb) for s, v, t, vb in strict_v_identical}.values())

# Statistics
N_strict = len(strict_v_identical_unique)
N_loose = len(loose_hits)
q817_strict = any(s == 8 and v == 17 for s, v, _, _ in strict_v_identical_unique)
uniqueness_q817_strict = (N_strict == 1 and q817_strict)
q817_loose_count = sum(1 for s, v, _, _, _ in loose_hits if s == 8 and v == 17)
uniqueness_q817_loose = q817_loose_count / N_loose if N_loose else 0

# Verdicts
H1_pass = (N_strict == 1 and uniqueness_q817_strict)
H2_pass = (N_loose <= 3 and q817_loose_count >= 1)

if H1_pass and H2_pass:
    verdict = "CONFIRMED-CORPUS-SINGLETON"
elif H1_pass and not H2_pass:
    verdict = "DIRECTIONAL"
elif N_strict >= 2:
    verdict = "NULL"
elif N_strict == 0:
    verdict = "PRE-COMMIT-VIOLATION"
else:
    verdict = "PARTIAL"

out = {
    "test_id": "Q008-F-02",
    "title": "Q 8:17 yaqīn-formula corpus-singleton test",
    "prereg_sha256": EXPECTED_PREREG_SHA,
    "prereg_sha256_verified": True,
    "seed": SEED,
    "alpha_bon": ALPHA_BON,
    "strict_pattern": "(?:^|\\s)(?:و|ف)?ما\\s+(\\S+)\\s+(?:إذ|اذ)\\s+(\\S+)(?:\\s+\\S+){0,3}\\s+و?لكنّ? + V₁=V₂",
    "loose_pattern": "(?:^|\\s)(?:و|ف)?ما\\s+(\\S+)\\s+(?:إذ|اذ)\\s+(\\S+)",
    "N_strict_with_V_identity": N_strict,
    "strict_matches": [
        {"surah": s, "verse": v, "V": vb, "text": t[:200]}
        for s, v, t, vb in strict_v_identical_unique
    ],
    "N_loose": N_loose,
    "loose_matches": [
        {"surah": s, "verse": v, "V1": v1, "V2": v2, "text": t[:200]}
        for s, v, t, v1, v2 in loose_hits
    ],
    "q817_strict_match": q817_strict,
    "q817_loose_count": q817_loose_count,
    "uniqueness_q817_strict": uniqueness_q817_strict,
    "uniqueness_q817_loose": uniqueness_q817_loose,
    "H1_pass": H1_pass,
    "H2_pass": H2_pass,
    "verdict": verdict,
    "interpretation": (
        "Q 8:17 contains the corpus-singleton yaqīn-formula 'wa-mā [V] idh [V] wa-lākin'. "
        "The construction is found exactly once in 6,236 verses, vindicating the classical "
        "balāgha tradition (al-Bāqillānī, al-Rāzī) identification of Q 8:17 as the "
        "iʿjāz-keystone of takhrīj al-fāʿil (agency-transfer)."
        if verdict.startswith("CONFIRMED")
        else "Verdict per pre-reg success/failure rule."
    ),
}

OUT_DIR = Path(__file__).parent.parent / "csv"
OUT_DIR.mkdir(exist_ok=True)
with open(OUT_DIR / "Q008-F-02.json", 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"Q008-F-02 verdict: {verdict}")
print(f"  N_strict (V₁=V₂): {N_strict}")
print(f"  N_loose: {N_loose}")
print(f"  Q 8:17 strict match: {q817_strict}")
print(f"  H1 pass: {H1_pass}, H2 pass: {H2_pass}")
print(f"Output: {OUT_DIR / 'Q008-F-02.json'}")
