"""
Q001-F-02 — Central-word identification in Q 1.

Pre-reg: surahs/Q001-al-fatiha/Q001-F-02-central-word-prereg.md
Pre-reg SHA256 (locked): badefd870db1ee0acb8935ce467fb183aeff08a854a68305f83492971ef7f3c5
"""
import json
import hashlib
import os

PROJECT = "/Users/grey/Downloads/quran"
PREREG_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/Q001-F-02-central-word-prereg.md"
PREREG_SHA_EXPECTED = "badefd870db1ee0acb8935ce467fb183aeff08a854a68305f83492971ef7f3c5"
OUT_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/csv/Q001-F-02.json"


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    sha = sha256_file(PREREG_PATH)
    assert sha == PREREG_SHA_EXPECTED, f"SHA mismatch {sha}"

    out = {"test_id": "Q001-F-02", "prereg_sha": sha, "variants": {}}

    for fname, key in [
        ("quran-no-tashkeel.json", "no-tashkeel"),
        ("quran-min-tashkeel.json", "min-tashkeel"),
        ("quran-full-tashkeel.json", "full-tashkeel"),
    ]:
        data = json.load(open(f"{PROJECT}/quran-text/{fname}"))
        q1 = data[0]
        flat = []
        for v in q1["verses"]:
            for w in v["text"].split():
                flat.append({"verse": v["id"], "word": w})
        N = len(flat)
        if N % 2 == 1:
            mid_idx = (N + 1) // 2  # 1-indexed
            central = flat[mid_idx - 1]
            mid_indices = [mid_idx]
        else:
            mid_indices = [N // 2, N // 2 + 1]
            central = [flat[mid_indices[0] - 1], flat[mid_indices[1] - 1]]

        out["variants"][key] = {
            "N": N,
            "central_indices_1based": mid_indices,
            "central_word_record": central,
            "verse_of_central": (central["verse"] if isinstance(central, dict) else [c["verse"] for c in central]),
        }

    # Verdict on no-tashkeel
    nt = out["variants"]["no-tashkeel"]
    central_verse = nt["verse_of_central"] if isinstance(nt["verse_of_central"], int) else nt["verse_of_central"][0]
    out["verdict_central_in_v5"] = "VINDICATED" if central_verse == 5 else "NULL"
    out["central_word_no_tashkeel"] = nt["central_word_record"]

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nOutput: {OUT_PATH}")


if __name__ == "__main__":
    main()
