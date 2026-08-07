#!/usr/bin/env python3
"""
H-NEW-2650 — Validation and correction of the attached-object-pronoun channel.

Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2650-pronoun-channel-validation.md
Pre-reg SHA-256 verified at runtime; SystemExit on mismatch. Frozen inputs SHA-verified.

This test is adversarial against its own parent findings (H-NEW-2540 §2b, H-NEW-2600 §5).
A result that weakens them is the correct outcome if the channel is broken.

NO EQTB FILE IS READ ANYWHERE IN THIS SCRIPT. That is the point of the channel.

Author: Waiel Al-Shujaa.
"""

import collections
import csv
import datetime
import hashlib
import json
import math
import os
import random
import re
import sys

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2650-pronoun-channel-validation.md")
PREREG_SHA = "4d7dbc76aa56e551c4dc38fcb6132c63e39884644344feb0e683c179481edacf"
FROZEN = {
    "qac": (os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt"),
            "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"),
    "revelation_order": (os.path.join(ROOT, "data/revelation-order.csv"),
                         "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7"),
    "quran_no_tashkeel": (os.path.join(ROOT, "quran-text/quran-no-tashkeel.json"),
                          "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"),
}
SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
BONF_K = 5
ALPHA = 0.05 / BONF_K
PARENT_GATE = 0.0005
PAIRS = [("II", "V", "+"), ("I", "VIII", "+"), ("I", "II", "-"), ("I", "IV", "-"), ("III", "VI", "+")]
FORMS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
MIN_TOKENS_PER_FORM_PER_ROOT = 2
SAMPLE_PER_CELL = 10


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gate():
    got = sha256(PREREG)
    if got != PREREG_SHA:
        raise SystemExit(f"PRE-REG TAMPERED: {got} != {PREREG_SHA}")
    print(f"[ok] pre-reg SHA-256 verified: {got}")
    for name, (path, expect) in sorted(FROZEN.items()):
        got = sha256(path)
        if got != expect:
            raise SystemExit(f"FROZEN INPUT {name} CHANGED: {got} != {expect}")
        print(f"[ok] frozen input {name}: {got[:16]}…")


# ------------------------------------------------------------------ QAC parsing
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
AGR_RE = re.compile(r"(?<![A-Za-z0-9:])([123](?:[MF])?(?:[SDP]))(?![A-Za-z0-9])")
PRON_RE = re.compile(r"PRON:([^|]+)")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
FORM_RE = re.compile(r"\|\((I{1,3}|IV|V|VI|VII|VIII|IX|X|XI|XII)\)\|")


def strip_marks(f):
    """Surface form reduced to bare Buckwalter letters, leading gemination mark removed."""
    return re.sub(r"[^A-Za-z]", "", f).lstrip("~")


def load_verbs():
    words = collections.defaultdict(list)
    with open(FROZEN["qac"][0], encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            loc = tuple(int(x) for x in m.groups())
            words[loc[:3]].append((loc[3], parts[1], parts[2], parts[3]))
    for k in words:
        words[k].sort()

    verbs = []
    for wloc in sorted(words):
        segs = words[wloc]
        for i, (idx, surface, tag, feat) in enumerate(segs):
            if tag != "V":
                continue
            agrs = AGR_RE.findall(feat)
            if len(agrs) != 1:
                raise SystemExit(f"agreement multiplicity != 1 at {wloc}:{idx}: {feat}")
            fm = FORM_RE.search(feat)
            rm = ROOT_RE.search(feat)
            clitics = []
            for (idx2, f2, t2, ft2) in segs[i + 1:]:
                if t2 != "PRON":
                    continue                       # EMPH / REL are SKIPPED, not terminators
                kind = ft2.split("|")[0]
                pm = PRON_RE.search(ft2)
                if not pm:
                    continue
                clitics.append({"seg": idx2, "surface": f2, "kind": kind, "pgn": pm.group(1)})
            verbs.append({
                "loc": f"({wloc[0]}:{wloc[1]}:{wloc[2]}:{idx})",
                "surah": wloc[0], "verse": wloc[1],
                "surface": surface,
                "form": fm.group(1) if fm else "I",
                "root": rm.group(1).strip() if rm else None,
                "agr": agrs[0],
                "aspect": "PERF" if "|PERF" in feat else ("IMPV" if "|IMPV" in feat else "IMPF"),
                "passive": "|PASS" in feat,
                "clitics": clitics,
            })
    return verbs


# ------------------------------------------------- RULE-NEW: closed decision list
def classify_clitic(f, p, s, g, a):
    """Return 'OBJECT' or 'SUBJECT' plus the rule index that fired. Pre-reg §4."""
    b = strip_marks(f)
    if b[:1] in ("h", "k"):
        return "OBJECT", 1
    if b[:1] in ("t", "w", "y", "u"):
        return "SUBJECT", 2
    if p == "1S":
        return "OBJECT", 3
    if p == "1P":
        if s == 0 and g == "1P" and a == "PERF":
            return "SUBJECT", 4
        return "OBJECT", 4
    return "SUBJECT", 5


def rule_new(v):
    """Corrected: >=1 post-verb SUFFIX PRON classified OBJECT."""
    s = 0
    for c in v["clitics"]:
        if c["kind"] != "SUFFIX":
            continue
        verdict, _ = classify_clitic(c["surface"], c["pgn"], s, v["agr"], v["aspect"])
        if verdict == "OBJECT":
            return True
        s += 1
    return False


def rule_old(v):
    """Reconstructed original: any post-verb PRON whose PGN differs from verb agreement."""
    return any(c["pgn"] != v["agr"] for c in v["clitics"])


# ------------------------------------------------------------------ statistics
def log_comb(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def binom_tail_ge(n, k):
    return sum(math.exp(log_comb(n, i) - n * math.log(2.0)) for i in range(k, n + 1))


def sign_test_two_sided(n_pos, n_neg):
    """Exact two-sided binomial sign test at p=0.5 over discordant roots."""
    n = n_pos + n_neg
    if n == 0:
        return 1.0
    k = max(n_pos, n_neg)
    return min(1.0, 2.0 * binom_tail_ge(n, k))


def pair_stats(verbs, form_a, form_b, detector):
    """Within-root paired comparison, >=2 tokens per form per root, PASS excluded."""
    by_root = collections.defaultdict(lambda: {form_a: [], form_b: []})
    for v in verbs:
        if v["passive"] or v["root"] is None:
            continue
        if v["form"] == form_a:
            by_root[v["root"]][form_a].append(detector(v))
        elif v["form"] == form_b:
            by_root[v["root"]][form_b].append(detector(v))
    roots, n_pos, n_neg, n_tie = [], 0, 0, 0
    ya = na = yb = nb = 0
    for r in sorted(by_root):
        A, B = by_root[r][form_a], by_root[r][form_b]
        if len(A) < MIN_TOKENS_PER_FORM_PER_ROOT or len(B) < MIN_TOKENS_PER_FORM_PER_ROOT:
            continue
        pa, pb = sum(A) / len(A), sum(B) / len(B)
        roots.append({"root": r, "n_a": len(A), "y_a": sum(A), "n_b": len(B), "y_b": sum(B),
                      "p_a": pa, "p_b": pb})
        ya += sum(A); na += len(A); yb += sum(B); nb += len(B)
        if pa > pb:
            n_pos += 1
        elif pa < pb:
            n_neg += 1
        else:
            n_tie += 1
    pooled_a = ya / na if na else float("nan")
    pooled_b = yb / nb if nb else float("nan")
    return {
        "form_a": form_a, "form_b": form_b, "n_roots": len(roots),
        "tokens_a": na, "objects_a": ya, "pooled_rate_a": pooled_a,
        "tokens_b": nb, "objects_b": yb, "pooled_rate_b": pooled_b,
        "gap": pooled_a - pooled_b if na and nb else float("nan"),
        "roots_a_gt_b": n_pos, "roots_a_lt_b": n_neg, "roots_tied": n_tie,
        "sign_test_two_sided_p": sign_test_two_sided(n_pos, n_neg),
        "roots": roots,
    }


# ------------------------------------------------------------------ main
def main():
    gate()
    verbs = load_verbs()
    print(f"[load] {len(verbs)} verbs")

    # ---- coverage assertion (pre-reg §4)
    inventory, covered, rules_used = collections.Counter(), 0, collections.Counter()
    for v in verbs:
        s = 0
        for c in v["clitics"]:
            if c["kind"] != "SUFFIX":
                continue
            inventory[(c["surface"], c["pgn"])] += 1
            verdict, which = classify_clitic(c["surface"], c["pgn"], s, v["agr"], v["aspect"])
            rules_used[(which, verdict)] += 1
            covered += 1
            s += 1
    total = sum(inventory.values())
    if covered != total:
        raise SystemExit(f"COVERAGE FAILURE: {covered} != {total}")
    print(f"[ok] classifier covers {covered}/{total} post-verb SUFFIX PRON tokens across "
          f"{len(inventory)} distinct (form,PGN) pairs — 100%")

    # ---- per-form differential error analysis (pre-reg §6)
    per_form = {}
    for F in FORMS:
        pool = [v for v in verbs if v["form"] == F and not v["passive"]]
        with_pron = [v for v in pool if v["clitics"]]
        old = [v for v in with_pron if rule_old(v)]
        new = [v for v in with_pron if rule_new(v)]
        old_set = {v["loc"] for v in old}
        new_set = {v["loc"] for v in new}
        fn = new_set - old_set          # RULE-NEW says object, RULE-OLD missed
        fp = old_set - new_set          # RULE-OLD says object, RULE-NEW says subject-only
        per_form[F] = {
            "verbs_total": len(pool), "verbs_with_post_pron": len(with_pron),
            "N_old": len(old_set), "N_new": len(new_set),
            "FN_count": len(fn), "FP_count": len(fp),
            "FN_rate_of_new": len(fn) / len(new_set) if new_set else None,
            "FP_rate_of_old": len(fp) / len(old_set) if old_set else None,
            "rate_old_of_all": len(old_set) / len(pool) if pool else None,
            "rate_new_of_all": len(new_set) / len(pool) if pool else None,
        }

    # ---- the five pairs under both rules
    pairs_out = {}
    for a, b, locked in PAIRS:
        key = f"{a}->{b}"
        so = pair_stats(verbs, a, b, rule_old)
        sn = pair_stats(verbs, a, b, rule_new)
        def verdict(st):
            if st["n_roots"] == 0 or math.isnan(st["gap"]):
                return "NO-DATA"
            sign = "+" if st["gap"] > 0 else ("-" if st["gap"] < 0 else "0")
            return sign
        pairs_out[key] = {
            "locked_sign": locked,
            "rule_old": {k: v for k, v in so.items() if k != "roots"},
            "rule_new": {k: v for k, v in sn.items() if k != "roots"},
            "sign_old": verdict(so), "sign_new": verdict(sn),
            "sign_held_old": verdict(so) == locked, "sign_held_new": verdict(sn) == locked,
            "sig_old_alpha": so["sign_test_two_sided_p"] <= ALPHA,
            "sig_new_alpha": sn["sign_test_two_sided_p"] <= ALPHA,
            "sig_old_parent_gate": so["sign_test_two_sided_p"] <= PARENT_GATE,
            "sig_new_parent_gate": sn["sign_test_two_sided_p"] <= PARENT_GATE,
            "roots_new": sn["roots"],
        }

    # ---- Form VI zero claim (pre-reg §6.2)
    vi_new = [v for v in verbs if v["form"] == "VI" and not v["passive"] and rule_new(v)]
    form_vi = {
        "claim": "H-NEW-2540 §2b: no Form VI token carries an object pronoun (0/33)",
        "form_vi_verbs_nonpassive": sum(1 for v in verbs if v["form"] == "VI" and not v["passive"]),
        "form_vi_object_bearing_under_rule_new": len(vi_new),
        "claim_survives": len(vi_new) == 0,
        "examples": [{"loc": v["loc"], "surface": v["surface"], "root": v["root"],
                      "clitics": v["clitics"]} for v in vi_new[:20]],
    }

    # ---- locked verdict (pre-reg §6.1)
    signs_held = all(pairs_out[f"{a}->{b}"]["sign_held_new"] for a, b, _ in PAIRS)
    lost_sig = [k for k, p in pairs_out.items() if p["sig_old_alpha"] and not p["sig_new_alpha"]]
    flipped = [k for k, p in pairs_out.items() if not p["sign_held_new"]]
    degraded = []
    for a, b, _ in PAIRS:
        fa, fb = per_form[a]["FN_rate_of_new"], per_form[b]["FN_rate_of_new"]
        if fa is not None and fb is not None and abs(fa - fb) > 0.10:
            degraded.append({"pair": f"{a}->{b}", "FN_a": fa, "FN_b": fb, "delta": abs(fa - fb)})
    if flipped or lost_sig:
        channel_verdict = "CHANNEL COMPROMISED"
    elif degraded:
        channel_verdict = "CHANNEL DEGRADED"
    else:
        channel_verdict = "CHANNEL SOUND"

    # ---- blinded validation sample
    quran = json.load(open(FROZEN["quran_no_tashkeel"][0], encoding="utf-8"))
    vtext = {(s["id"], v["id"]): v["text"] for s in quran for v in s["verses"]}
    samples, key_rows = [], []
    rng = random.Random(SEED_PRIMARY)
    sid = 0
    for F in FORMS:
        for detected in (True, False):
            cell = sorted(
                (v for v in verbs
                 if v["form"] == F and not v["passive"] and rule_new(v) == detected),
                key=lambda v: v["loc"])
            rng.shuffle(cell)
            for v in cell[:SAMPLE_PER_CELL]:
                sid += 1
                sample_id = f"S{sid:03d}"
                samples.append({
                    "sample_id": sample_id, "verb_location": v["loc"], "verb_surface": v["surface"],
                    "verse_text": vtext.get((v["surah"], v["verse"]), ""),
                    "review_has_attached_object_pronoun": "",
                    "review_clitic_span": "", "review_is_direct_object": "", "review_notes": "",
                })
                key_rows.append({"sample_id": sample_id, "verb_location": v["loc"],
                                 "form": F, "rule_new_detected": detected,
                                 "rule_old_detected": rule_old(v), "root": v["root"],
                                 "agr": v["agr"], "aspect": v["aspect"], "clitics": v["clitics"]})
    rng2 = random.Random(SEED_REPLICATION)
    order = list(range(len(samples)))
    rng2.shuffle(order)

    # ---- write immutable run dir
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2650", ts)
    os.makedirs(rundir, exist_ok=False)
    result = {
        "finding_id": "H-NEW-2650",
        "prereg_sha256": PREREG_SHA,
        "frozen_inputs": {k: v[1] for k, v in FROZEN.items()},
        "eqtb_used": False,
        "bonferroni_k": BONF_K, "alpha_corrected": ALPHA, "parent_gate": PARENT_GATE,
        "classifier_coverage": {"tokens": covered, "distinct_form_pgn_pairs": len(inventory),
                                "by_rule": {f"rule{r}_{v}": c for (r, v), c in sorted(rules_used.items())}},
        "per_form_differential_error": per_form,
        "pairs": pairs_out,
        "form_vi_zero_claim": form_vi,
        "channel_verdict": channel_verdict,
        "sign_flips": flipped, "lost_significance": lost_sig, "degraded_pairs": degraded,
        "validation_sample_rows": len(samples),
    }
    with open(os.path.join(rundir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "validation-sample.tsv"), "x", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(samples[0].keys()), delimiter="\t")
        w.writeheader()
        for r in samples:
            w.writerow(r)
    with open(os.path.join(rundir, "validation-key.json"), "x", encoding="utf-8") as fh:
        json.dump({"seed": SEED_PRIMARY, "replication_seed": SEED_REPLICATION,
                   "replication_order": order, "rows": key_rows}, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({"finding_id": "H-NEW-2650", "utc": ts,
                   "prereg": "findings/phase-b-hypotheses/prereg-h-new-2650-pronoun-channel-validation.md",
                   "prereg_sha256": PREREG_SHA,
                   "script": "findings/phase-b-hypotheses/scripts/h-new-2650.py",
                   "frozen_inputs": {k: {"path": os.path.relpath(v[0], ROOT), "sha256": v[1]}
                                     for k, v in FROZEN.items()},
                   "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
                   "eqtb_used": False,
                   "outputs": ["result.json", "validation-sample.tsv", "validation-key.json"]},
                  fh, ensure_ascii=False, indent=1)

    # ---- console report
    print("\n=== PER-FORM DIFFERENTIAL ERROR (RULE-OLD assessed against RULE-NEW) ===")
    print(f"{'form':<5}{'verbs':>7}{'w/PRON':>8}{'N_old':>7}{'N_new':>7}{'FN':>6}{'FP':>5}"
          f"{'FN_rate':>9}{'FP_rate':>9}{'rate_old':>10}{'rate_new':>10}")
    for F in FORMS:
        d = per_form[F]
        fr = "n/a" if d["FN_rate_of_new"] is None else f"{d['FN_rate_of_new']:.4f}"
        fpr = "n/a" if d["FP_rate_of_old"] is None else f"{d['FP_rate_of_old']:.4f}"
        print(f"{F:<5}{d['verbs_total']:>7}{d['verbs_with_post_pron']:>8}{d['N_old']:>7}"
              f"{d['N_new']:>7}{d['FN_count']:>6}{d['FP_count']:>5}{fr:>9}{fpr:>9}"
              f"{d['rate_old_of_all']:>10.4f}{d['rate_new_of_all']:>10.4f}")

    print("\n=== FIVE FORM PAIRS ===")
    for a, b, locked in PAIRS:
        p = pairs_out[f"{a}->{b}"]
        o, n = p["rule_old"], p["rule_new"]
        print(f"\n  {a} -> {b}   locked {locked}   roots(new)={n['n_roots']}")
        print(f"    RULE-OLD  {o['objects_a']}/{o['tokens_a']}={o['pooled_rate_a']:.4f} vs "
              f"{o['objects_b']}/{o['tokens_b']}={o['pooled_rate_b']:.4f}  gap={o['gap']:+.4f}  "
              f"{o['roots_a_gt_b']}/{o['roots_a_lt_b']}/{o['roots_tied']}  p={o['sign_test_two_sided_p']:.3e}  "
              f"sign {'HELD' if p['sign_held_old'] else 'FLIPPED'}")
        print(f"    RULE-NEW  {n['objects_a']}/{n['tokens_a']}={n['pooled_rate_a']:.4f} vs "
              f"{n['objects_b']}/{n['tokens_b']}={n['pooled_rate_b']:.4f}  gap={n['gap']:+.4f}  "
              f"{n['roots_a_gt_b']}/{n['roots_a_lt_b']}/{n['roots_tied']}  p={n['sign_test_two_sided_p']:.3e}  "
              f"sign {'HELD' if p['sign_held_new'] else 'FLIPPED'}  "
              f"{'sig' if p['sig_new_alpha'] else 'NOT-sig'}@{ALPHA}")

    print(f"\n=== FORM VI ZERO CLAIM ===")
    print(f"  non-passive Form VI verbs: {form_vi['form_vi_verbs_nonpassive']}")
    print(f"  object-bearing under RULE-NEW: {form_vi['form_vi_object_bearing_under_rule_new']}")
    print(f"  2540 §2b 'zero out of 33' survives: {form_vi['claim_survives']}")
    for e in form_vi["examples"][:6]:
        print(f"     {e['loc']} {e['surface']} root={e['root']} {e['clitics']}")

    print(f"\n=== VERDICT: {channel_verdict} ===")
    if flipped:
        print(f"  sign flips: {flipped}")
    if lost_sig:
        print(f"  lost significance: {lost_sig}")
    for d in degraded:
        print(f"  degraded: {d['pair']} FN rates {d['FN_a']:.4f} vs {d['FN_b']:.4f} (Δ={d['delta']:.4f})")
    print(f"\n[run] {rundir}")
    print(f"[validation sample] {len(samples)} rows, review columns BLANK by design")


if __name__ == "__main__":
    main()
