#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2240 — Verse-final assonance / fāṣila rhyme-class taxonomy.

Builds an algorithmic classifier of all 6236 verse-endings into assonance classes
defined by the PAUSAL RIME (madd/ridf long vowel + rāwī consonant), then:
  (1) corpus census: class frequencies + per-surah dominant class + mono-class count;
  (2) pre-registered, direction-LOCKED within-surah homogeneity test
      (mean within-surah class entropy < corpus-shuffle null), 10000 perms, seed 20260509;
  (3) exploratory blockiness / pericope-shift descriptives (MW-7 capped).

No external dependencies. All numbers from disk.

Author: Waiel Al-Shujaa.  Date: 2026-05-29.
"""

import json, math, hashlib, os, random
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../findings/phase-b-hypotheses
PROJ = os.path.dirname(os.path.dirname(ROOT))                       # .../quran
MIN_PATH  = os.path.join(PROJ, "quran-text", "quran-min-tashkeel.json")
FULL_PATH = os.path.join(PROJ, "quran-text", "quran-full-tashkeel.json")
PREREG    = os.path.join(ROOT, "prereg-h-new-2240-fasila-assonance-taxonomy.md")
OUT_JSON  = os.path.join(ROOT, "csv", "h-new-2240.json")

EXPECTED_PREREG_SHA = "b2b9a8aca1336dde53bad83c323a06d2cc5fedb66894d36467c1c57484790ab2"
SEED = 20260509
N_PERMS = 10000

# ---------------------------------------------------------------- pre-reg lock
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def file_sha(path):
    return sha256_file(path)

# ---------------------------------------------------------------- char sets
LONG_VOWELS = set("اويى")            # alif, waw, ya, alif-maqsura
DAGGER_ALIF = "ٰ"               # ٰ  -> long ā
TA_MARBUTA  = "ة"               # ة
HAMZA       = "ء"               # ء (standalone)
# combining marks / pause marks to strip (NOT long-vowel graphemes)
STRIP_MARKS = set([
    "ً","ٌ","ٍ",        # tanwīn fath/damm/kasr
    "َ","ُ","ِ",        # fatha damma kasra
    "ّ","ْ",                 # shadda sukun
    "ٓ","ٔ","ٕ",        # madda above, hamza above/below
    "ـ",                          # tatweel
    "ۛ","ۜ","۝","۞","۟","۠","ۡ","ۢ",
    "ۣ","ۤ","ۥ","ۦ","ۧ","ۨ","۩","۪",
    "۫","۬","ۭ",        # quranic annotation/pause marks incl sajda ۩(06E9)
    "‌","‍","‎","‏",
])
# hamza-carrier forms map to their consonant role; for rime we only care if the
# FINAL grapheme is a hamza/long vowel. Carriers (ؤ ئ أ إ آ) when final:
HAMZA_CARRIERS = {"ؤ","ئ","أ","إ","آ"}  # ؤ ئ أ إ آ

def clean_final_word(text):
    """Return cleaned final orthographic word (dagger alif -> alif, marks stripped)."""
    toks = text.split()
    # drop a trailing standalone sajda / annotation token
    while toks and all((ch in STRIP_MARKS or ch in ("۩",)) for ch in toks[-1]):
        toks.pop()
    if not toks:
        return ""
    w = toks[-1]
    out = []
    for ch in w:
        if ch == DAGGER_ALIF:
            out.append("ا")        # -> alif
        elif ch in STRIP_MARKS:
            continue
        else:
            out.append(ch)
    return "".join(out)

def classify(text):
    """Deterministic pausal-rime assonance class for one verse text.
    Returns (class_label, coarse_group)."""
    w = clean_final_word(text)
    if not w:
        return ("∅", "other")
    # tā-marbūṭa -> its own -ah class (heard -ah in pause)
    if w[-1] == TA_MARBUTA:
        return ("-ah", "ah")
    last = w[-1]
    prev = w[-2] if len(w) >= 2 else ""
    # --- open endings: final grapheme is itself a long vowel / hamza ---
    if last in ("ا", "ى"):        # alif / alif maqsura  -> open -ā
        return ("-ā", "open-ā")
    if last == "و":                      # waw -> open -ū
        return ("-ū", "open-other")
    if last == "ي":                      # ya -> open -ī
        return ("-ī", "open-other")
    if last == HAMZA or last in HAMZA_CARRIERS:
        # final hamza; preceded by long ā?
        if prev in ("ا",):
            return ("-āʾ", "ā-rime")
        if prev == "و":
            return ("-ūʾ", "open-other")
        if prev == "ي":
            return ("-īʾ", "open-other")
        return ("-ʾ", "other")
    # --- closed endings: last is the rāwī consonant; look at ridf (prev) ---
    rawi = last
    if prev in ("ا",):                   # long ā ridf
        return ("-ā" + rawi, "ā-rime")
    if prev == "و":                       # long ū ridf
        return ("-ū" + rawi, "ū-rime")
    if prev == "ي":                       # long ī ridf
        return ("-ī" + rawi, "ī-rime")
    # no long-vowel ridf -> short closed syllable, keyed by rāwī only
    return ("-" + rawi, "short")

def shannon_nats(counter):
    n = sum(counter.values())
    if n == 0:
        return 0.0
    h = 0.0
    for c in counter.values():
        if c > 0:
            p = c / n
            h -= p * math.log(p)
    return h

# ---------------------------------------------------------------- final-vowel diagnostic (full-tashkeel)
FINAL_SHORT = {
    "َ": "fatha", "ُ": "damma", "ِ": "kasra",
    "ً": "tanwin-fath", "ٌ": "tanwin-damm", "ٍ": "tanwin-kasr",
    "ْ": "sukun",
}
def final_vowel_diag(full_text):
    toks = full_text.split()
    while toks and all(ch in STRIP_MARKS for ch in toks[-1]):
        toks.pop()
    if not toks:
        return "none"
    w = toks[-1]
    for ch in reversed(w):
        if ch in FINAL_SHORT:
            return FINAL_SHORT[ch]
        if "ء" <= ch <= "ي" or ch == DAGGER_ALIF:  # a base letter w/ no haraka
            return "bare/long"
    return "none"

# ---------------------------------------------------------------- main
def main():
    actual = file_sha(PREREG)
    if actual != EXPECTED_PREREG_SHA:
        raise SystemExit("PRE-REG SHA MISMATCH!\n expected %s\n actual   %s" %
                         (EXPECTED_PREREG_SHA, actual))
    print("[ok] pre-reg SHA verified:", actual)

    mn = json.load(open(MIN_PATH, encoding="utf-8"))
    fl = json.load(open(FULL_PATH, encoding="utf-8"))
    min_sha = file_sha(MIN_PATH)
    full_sha = file_sha(FULL_PATH)
    assert len(mn) == len(fl) == 114

    # classify every verse
    per_surah_classes = []         # list of list-of-class per surah, surah-ordered
    per_surah_meta = []
    all_labels = []
    coarse_all = Counter()
    final_vowel_all = Counter()
    label_to_coarse = {}
    for si in range(114):
        s_min = mn[si]; s_full = fl[si]
        assert len(s_min["verses"]) == len(s_full["verses"]), s_min["id"]
        labs = []
        for vi, v in enumerate(s_min["verses"]):
            lab, coarse = classify(v["text"])
            labs.append(lab)
            all_labels.append(lab)
            coarse_all[coarse] += 1
            label_to_coarse[lab] = coarse
            fv = final_vowel_diag(s_full["verses"][vi]["text"])
            final_vowel_all[fv] += 1
        per_surah_classes.append(labs)
        per_surah_meta.append({"surah": s_min["id"], "name": s_min["name"],
                               "type": s_min.get("type"), "n_verses": len(labs)})

    total = sum(len(x) for x in per_surah_classes)
    assert total == 6236, total

    # ---- corpus census ----
    class_freq = Counter(all_labels)
    census = [{"class": c, "count": n, "share": n / total}
              for c, n in class_freq.most_common()]
    coarse_census = [{"group": g, "count": n, "share": n / total}
                     for g, n in coarse_all.most_common()]

    # per-surah dominant
    per_surah_dom = []
    mono_class_80 = []
    dom_shares = []
    entropies = []
    for meta, labs in zip(per_surah_meta, per_surah_classes):
        cnt = Counter(labs)
        dom_c, dom_n = cnt.most_common(1)[0]
        share = dom_n / len(labs)
        ent = shannon_nats(cnt)
        dom_shares.append(share)
        entropies.append(ent)
        per_surah_dom.append({
            "surah": meta["surah"], "name": meta["name"], "type": meta["type"],
            "n_verses": meta["n_verses"], "dominant_class": dom_c,
            "dominant_count": dom_n, "dominant_share": share,
            "n_distinct_classes": len(cnt), "entropy_nats": ent,
            "coarse_dominant": Counter(label_to_coarse[l] for l in labs).most_common(1)[0][0],
        })
        if share >= 0.80:
            mono_class_80.append(meta["surah"])

    H_obs = sum(entropies) / 114.0
    D_obs = sum(dom_shares) / 114.0

    # ---- permutation null (preserve surah sizes; shuffle labels) ----
    sizes = [len(x) for x in per_surah_classes]
    def perm_stats(seed):
        rng = random.Random(seed)
        pool = list(all_labels)
        H_le = 0   # #{H_perm <= H_obs}
        D_ge = 0   # #{D_perm >= D_obs}
        H_perms = []
        for _ in range(N_PERMS):
            rng.shuffle(pool)
            idx = 0
            hsum = 0.0; dsum = 0.0
            for sz in sizes:
                seg = pool[idx:idx + sz]; idx += sz
                cnt = Counter(seg)
                hsum += shannon_nats(cnt)
                dsum += cnt.most_common(1)[0][1] / sz
            Hp = hsum / 114.0; Dp = dsum / 114.0
            H_perms.append(Hp)
            if Hp <= H_obs: H_le += 1
            if Dp >= D_obs: D_ge += 1
        H_perms.sort()
        return H_le, D_ge, H_perms

    H_le, D_ge, H_perms = perm_stats(SEED)
    p_entropy = (H_le + 1) / (N_PERMS + 1)
    p_share   = (D_ge + 1) / (N_PERMS + 1)
    null_mean = sum(H_perms) / len(H_perms)
    null_min  = H_perms[0]
    null_p025 = H_perms[int(0.025 * len(H_perms))]
    null_p975 = H_perms[int(0.975 * len(H_perms))]

    # replications (MW-5)
    rep = {}
    for sd in (20260510, 99):
        hle, dge, _ = perm_stats(sd)
        rep[str(sd)] = {"p_entropy": (hle + 1) / (N_PERMS + 1),
                        "p_share": (dge + 1) / (N_PERMS + 1)}

    # ---- exploratory blockiness (MW-7) : same-surah label shuffle, longest-run + switches ----
    def runs_and_switches(labs):
        switches = sum(1 for i in range(1, len(labs)) if labs[i] != labs[i - 1])
        longest = 1; cur = 1
        for i in range(1, len(labs)):
            if labs[i] == labs[i - 1]:
                cur += 1; longest = max(longest, cur)
            else:
                cur = 1
        return switches, longest
    rng_b = random.Random(SEED)
    obs_switch_total = 0; null_switch_ge = 0
    block_perms = 2000
    block_detail = []
    obs_longest_total = 0; null_longest_le = 0
    for labs in per_surah_classes:
        sw, lr = runs_and_switches(labs)
        obs_switch_total += sw
        obs_longest_total += lr
    # null: shuffle within each surah; statistic = total switches (lower=blockier) & total longest-run (higher=blockier)
    null_switch_dist = []
    null_longest_dist = []
    for _ in range(block_perms):
        tsw = 0; tlr = 0
        for labs in per_surah_classes:
            l2 = labs[:]
            rng_b.shuffle(l2)
            sw, lr = runs_and_switches(l2)
            tsw += sw; tlr += lr
        null_switch_dist.append(tsw)
        null_longest_dist.append(tlr)
    # blockier real text => FEWER switches and LONGER runs than shuffle
    p_block_switch = (sum(1 for x in null_switch_dist if x <= obs_switch_total) + 1) / (block_perms + 1)
    p_block_run    = (sum(1 for x in null_longest_dist if x >= obs_longest_total) + 1) / (block_perms + 1)
    null_switch_mean = sum(null_switch_dist) / block_perms
    null_longest_mean = sum(null_longest_dist) / block_perms

    # per-surah switch rate + longest run (descriptive)
    for meta, labs in zip(per_surah_meta, per_surah_classes):
        sw, lr = runs_and_switches(labs)
        block_detail.append({"surah": meta["surah"], "n_verses": meta["n_verses"],
                             "switches": sw, "switch_rate": sw / max(1, (meta["n_verses"] - 1)),
                             "longest_monoclass_run": lr})

    # ---- verdict logic (locked direction: lower entropy, higher share) ----
    alpha = 0.025  # Bonferroni k=2
    entropy_pass = (H_obs < null_mean) and (p_entropy < alpha)
    # share statistic: locked direction is D_obs ABOVE its null; p_share already counts
    # the upper tail #{D_perm >= D_obs}; significance at the Bonferroni alpha is the gate.
    share_dir_ok = (p_share < alpha)
    reversed_violation = (H_obs > null_mean)  # surahs LESS homogeneous than chance
    if reversed_violation:
        verdict = "NULL — PRE-COMMIT VIOLATION (surahs LESS homogeneous than chance)"
    elif entropy_pass and share_dir_ok:
        verdict = "PASS — surahs significantly rhyme-homogeneous (entropy<<null, share>>null)"
    elif entropy_pass:
        verdict = "PASS-PARTIAL — entropy significant, share marginal"
    else:
        verdict = "NULL — homogeneity not significant"

    result = {
        "id": "H-NEW-2240",
        "title": "Verse-final assonance / fāṣila rhyme-class taxonomy",
        "prereg_sha256": actual,
        "seed": SEED, "n_perms": N_PERMS,
        "rules_tuple": {
            "primary_text": "quran-min-tashkeel.json", "primary_sha256": min_sha,
            "secondary_text": "quran-full-tashkeel.json", "secondary_sha256": full_sha,
            "pause_convention": "waqf/pausal", "reading": "Hafs-Kufan", "n_verses": total,
        },
        "census": {
            "n_distinct_classes": len(class_freq),
            "class_frequency": census,
            "coarse_groups": coarse_census,
            "final_short_vowel_diag_full_tashkeel": dict(final_vowel_all),
        },
        "per_surah": per_surah_dom,
        "mono_class_80pct": {
            "count": len(mono_class_80), "surahs": mono_class_80,
        },
        "homogeneity_test": {
            "H_obs_mean_within_surah_entropy_nats": H_obs,
            "D_obs_mean_dominant_share": D_obs,
            "null_entropy_mean": null_mean, "null_entropy_min": null_min,
            "null_entropy_p2.5": null_p025, "null_entropy_p97.5": null_p975,
            "p_entropy_one_sided_lower": p_entropy,
            "p_share_one_sided_upper": p_share,
            "bonferroni_alpha_k2": alpha,
            "direction_locked": "observed entropy < null (lower=homogeneous)",
            "reversed_pre_commit_violation": reversed_violation,
            "replications": rep,
            "verdict": verdict,
        },
        "exploratory_blockiness_MW7": {
            "note": "within-surah label shuffle; single-test alpha=0.05, does NOT gate verdict",
            "n_perms": block_perms,
            "obs_total_switches": obs_switch_total,
            "null_switch_mean": null_switch_mean,
            "p_blockier_fewer_switches": p_block_switch,
            "obs_total_longest_runs": obs_longest_total,
            "null_longest_mean": null_longest_mean,
            "p_blockier_longer_runs": p_block_run,
            "per_surah": block_detail,
        },
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # console summary
    print("\n=== H-NEW-2240 SUMMARY ===")
    print("distinct assonance classes:", len(class_freq))
    print("top-12 classes:")
    for row in census[:12]:
        print("   %-6s %5d  %.3f" % (row["class"], row["count"], row["share"]))
    print("coarse groups:", [(g["group"], round(g["share"], 3)) for g in coarse_census])
    print("mono-class (>=80%%) surahs: %d -> %s" %
          (len(mono_class_80), mono_class_80))
    print("H_obs (mean within-surah entropy) = %.4f nats" % H_obs)
    print("null entropy mean = %.4f  [2.5%%=%.4f, 97.5%%=%.4f, min=%.4f]" %
          (null_mean, null_p025, null_p975, null_min))
    print("p_entropy (one-sided lower) = %.5f  (alpha=%.3f)" % (p_entropy, alpha))
    print("D_obs (mean dominant share) = %.4f ; p_share = %.5f" % (D_obs, p_share))
    print("replications:", rep)
    print("blockiness: obs switches=%d null~%.1f p=%.4f ; obs longest-run-sum=%d null~%.1f p=%.4f" %
          (obs_switch_total, null_switch_mean, p_block_switch,
           obs_longest_total, null_longest_mean, p_block_run))
    print("VERDICT:", verdict)
    print("written:", OUT_JSON)

if __name__ == "__main__":
    main()
