#!/usr/bin/env python3
"""
Q060-F-02 — Women's bayʿa formula CORPUS-EXACT structure test.

Pre-reg SHA256: 08f0033c65aa9907b6ebde476dcdb88048b370e7729316a81595ab3ad9f31962

Two test axes:
  (a) Feminine-plural verbal pledge form 'يبايعنك' is corpus-EXACT to Q 60:12.
  (b) Chained feminine-plural negative-imperatives ≥4 per single verse is
      corpus-EXACT to Q 60:12.

Decision rule: CORPUS-EXACT verdict if both verses-of-occurrence == [Q 60:12].
"""
import json
import re
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PREREG_SHA = "08f0033c65aa9907b6ebde476dcdb88048b370e7729316a81595ab3ad9f31962"

PAT_YUBAYICNAKA = re.compile(r"يبايعنك")
PAT_FA_BAYIC_HUNNA = re.compile(r"فبايعهن")
PAT_MASC_YUBAYICUNA = re.compile(r"يبايعونك|يبايعون(?!\S)")
PAT_FEM_NEG_CHAIN = re.compile(
    r"(?:لا|ولا)\s+(?:يشركن|يسرقن|يزنين|يقتلن|يأتين|يعصينك|يعصين|يحفظن|يبدين|يضربن|يرين|يطمث|يحلل|يكتمن|يفترين|يخلطن)"
)

def verify_prereg_sha(prereg_path):
    h = hashlib.sha256(prereg_path.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        raise RuntimeError(f"Pre-reg SHA mismatch: expected {PREREG_SHA}, got {h}")
    return h

def main():
    prereg_path = REPO_ROOT / "surahs" / "Q060-al-mumtahana" / "preregs" / "Q060-F-02-bayca-corpus-exact-prereg.md"
    sha_check = verify_prereg_sha(prereg_path)
    print(f"Pre-reg SHA verified: {sha_check[:16]}...")

    text_path = REPO_ROOT / "quran-text" / "quran-no-tashkeel.json"
    data = json.load(open(text_path))

    a_hits, masc_hits, multi_hits = [], [], []
    fa_bayic_hunna_hits = []
    for surah in data:
        sid = surah["id"]
        for v in surah["verses"]:
            t = v["text"]
            if PAT_YUBAYICNAKA.search(t):
                a_hits.append({"surah": sid, "verse": v["id"]})
            if PAT_FA_BAYIC_HUNNA.search(t):
                fa_bayic_hunna_hits.append({"surah": sid, "verse": v["id"]})
            if PAT_MASC_YUBAYICUNA.search(t):
                masc_hits.append({"surah": sid, "verse": v["id"]})
            toks = PAT_FEM_NEG_CHAIN.findall(t)
            if len(toks) >= 4:
                multi_hits.append({"surah": sid, "verse": v["id"], "n_chain": len(toks)})

    print(f"Test (a) يبايعنك corpus instances: {len(a_hits)}")
    for h in a_hits:
        print(f"  Q {h['surah']}:{h['verse']}")
    test_a_pass = len(a_hits) == 1 and a_hits[0] == {"surah": 60, "verse": 12}
    print(f"  Test (a) verdict: {'CORPUS-EXACT to Q 60:12' if test_a_pass else 'NULL'}")

    print(f"\nTest (a-ext) فبايعهن corpus instances: {len(fa_bayic_hunna_hits)}")
    print(f"\nComparator masculine يبايعونك corpus instances: {len(masc_hits)}")
    for h in masc_hits:
        print(f"  Q {h['surah']}:{h['verse']}")

    print(f"\nTest (b) ≥4-chain corpus instances: {len(multi_hits)}")
    for h in multi_hits:
        print(f"  Q {h['surah']}:{h['verse']} [n={h['n_chain']}]")
    test_b_pass = len(multi_hits) == 1 and multi_hits[0]["surah"] == 60 and multi_hits[0]["verse"] == 12
    print(f"  Test (b) verdict: {'CORPUS-EXACT to Q 60:12' if test_b_pass else 'NULL'}")

    return {
        "test_a_yubayicna": {"corpus_n": len(a_hits), "pass": test_a_pass},
        "test_b_chain": {"corpus_n": len(multi_hits), "pass": test_b_pass},
    }

if __name__ == "__main__":
    main()
