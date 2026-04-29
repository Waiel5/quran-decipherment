#!/usr/bin/env python3
"""Letter-multiset primitives for H-NEW-4-EXT-D al-Rāzī ijmāl-tafṣīl KL test.

Companion module to scripts/h_new_24_multiset_boundary.py (H-NEW-24 letter-
multiset surah-boundary detectability). Reuses clean_letters / NORMALIZE /
alphabet conventions from that pipeline to keep H-NEW-24 reproducibility
untouched.

Three exported functions (per H-NEW-4-EXT-D pre-reg,
findings/phase-b-hypotheses/h-new-4-ext-d-prereg.md):

  1. extract_muqattaat_opener_multiset(surah_id, split_q42=False)
  2. extract_body_letter_multiset(surah_id, exclude_opener=True,
                                  body_window=(0.0, 1.0), alpha=0.01)
  3. kl_divergence(P_body, P_open, alpha=0.01)

All probability distributions are dict[str, float] over a fixed 28-letter
Arabic alphabet (rasm-normalized; see ALPHABET below). Support closure is
uniform and deterministic — non-support letters get 0.0 before smoothing
and alpha after.

Rules-tuple: (no-tashkeel, orthographic-token & lemma, graphemes,
counted-only-in-surah-1, hafs-kufan, mashriqi)

Edge-case decisions signed off by classical-scholar 2026-04-13:
 - Q42 (al-Shūrā) two-line muqaṭṭaʿāt (حم / عسق) → union construction
   {ح, م, ع, س, ق} for primary; split-construction available via
   split_q42=True for sensitivity-5 per-cluster breakdown.
 - body_window 0% mark = first non-muqaṭṭaʿāt CHARACTER after opener
   stripping (option (a)), not verse-aligned.

MW-6 citation tag on the muqaṭṭaʿāt catalog: al-Suyūṭī *al-Itqān fī ʿulūm
al-Qurʾān* nawʿ 9 (*fī al-fawātiḥ al-suwar*) — MW-6 PENDING. Catalog is
uncontroversial; upgrade to VERIFIED requires physical-edition cross-check
per AMEND-28.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'

# Rasm-level normalization (matches h_new_24_multiset_boundary.py NORMALIZE).
# Alif variants → ا ; alif maqṣūra → ي ; tāʾ marbūṭa → ه.
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ى': 'ي', 'ة': 'ه',
}
AR_LETTER = re.compile(r'[\u0621-\u064A]')

# Fixed 28-letter Arabic alphabet AFTER rasm normalization. Note that hamza
# (ء) is kept as a standalone letter; wāw-hamza (ؤ) / yāʾ-hamza (ئ) / seat-
# hamza (أ/إ) collapse under NORMALIZE to their base carriers. Pre-reg
# pins "the 28-letter Arabic alphabet"; this is exactly that set in the
# standard classical order with hamza treated as #1 ء per al-Khalīl's
# *Kitāb al-ʿAyn* register tradition (though the order is irrelevant to
# KL computation — it only matters that the support is closed and fixed).
ALPHABET = [
    'ء', 'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ',
    'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل',
    'م', 'ن', 'ه', 'و', 'ي',
]
# That's 29 letters (28 canonical + hamza). The pre-reg says "28-letter
# Arabic alphabet" but in practice the rasm-normalized support includes
# bare hamza (ء) in several muqaṭṭaʿāt-free verses. We keep ء as part of
# the support to avoid dropping mass; the KL computation is invariant to
# the extra zero-slot in both distributions. Flag for classical-scholar
# if a strict 28-letter closure is required.
ALPHA_SET = set(ALPHABET)

# 29 muqaṭṭaʿāt-opening surahs (matches scripts/h_new_31_incipit_class.py
# MUQATTAAT_SURAHS, al-Suyūṭī Itqān nawʿ 9, MW-6 PENDING).
MUQATTAAT_SURAHS = frozenset({
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
})

# Hard-coded opener letter-sets per surah (rasm-normalized). The 14
# distinct patterns mapped to their surah ids. Source: canonical mushaf
# + al-Suyūṭī Itqān nawʿ 9, MW-6 PENDING.
#
# Q42 (al-Shūrā): UNION construction for primary = {ح, م, ع, س, ق}
# per classical-scholar sign-off 2026-04-13 (al-Rāzī Mafātīḥ al-Ghayb
# vol. 27 treats حم / عسق as a single ijmāl event).
MUQATTAAT_OPENER = {
    # الم
    2: ('ا', 'ل', 'م'),
    3: ('ا', 'ل', 'م'),
    29: ('ا', 'ل', 'م'),
    30: ('ا', 'ل', 'م'),
    31: ('ا', 'ل', 'م'),
    32: ('ا', 'ل', 'م'),
    # المص
    7: ('ا', 'ل', 'م', 'ص'),
    # الر
    10: ('ا', 'ل', 'ر'),
    11: ('ا', 'ل', 'ر'),
    12: ('ا', 'ل', 'ر'),
    14: ('ا', 'ل', 'ر'),
    15: ('ا', 'ل', 'ر'),
    # المر
    13: ('ا', 'ل', 'م', 'ر'),
    # كهيعص
    19: ('ك', 'ه', 'ي', 'ع', 'ص'),
    # طه
    20: ('ط', 'ه'),
    # طسم
    26: ('ط', 'س', 'م'),
    28: ('ط', 'س', 'م'),
    # طس
    27: ('ط', 'س'),
    # يس
    36: ('ي', 'س'),
    # ص
    38: ('ص',),
    # حم
    40: ('ح', 'م'),
    41: ('ح', 'م'),
    43: ('ح', 'م'),
    44: ('ح', 'م'),
    45: ('ح', 'م'),
    46: ('ح', 'م'),
    # حم / عسق (Q42 union = 5-letter set)
    42: ('ح', 'م', 'ع', 'س', 'ق'),
    # ق
    50: ('ق',),
    # ن
    68: ('ن',),
}

# Q42 split-construction for sensitivity-5 per-cluster breakdown.
# Two separate sub-openers: حم (verse 1) and عسق (verse 2).
MUQATTAAT_OPENER_Q42_SPLIT = (
    ('ح', 'م'),
    ('ع', 'س', 'ق'),
)

BASELINE_OPENER_N_CHARS = 4  # median letter-count of muqaṭṭaʿāt openers

_QURAN_CACHE = None


def _load_quran():
    global _QURAN_CACHE
    if _QURAN_CACHE is None:
        _QURAN_CACHE = json.loads(QURAN_JSON.read_text())
        _QURAN_CACHE = {s['id']: s for s in _QURAN_CACHE}
    return _QURAN_CACHE


def clean_letters(text):
    """Extract rasm-normalized Arabic letters from text (no whitespace,
    no diacritics, no punctuation). Matches h_new_24_multiset_boundary.py."""
    out = []
    for ch in text:
        if AR_LETTER.match(ch):
            out.append(NORMALIZE.get(ch, ch))
    return ''.join(out)


def _uniform_dist(letters):
    """Uniform-on-support probability distribution over 28-letter alphabet."""
    letters = tuple(letters)
    n = len(letters)
    if n == 0:
        return {ch: 0.0 for ch in ALPHABET}
    p = 1.0 / n
    dist = {ch: 0.0 for ch in ALPHABET}
    for ch in letters:
        if ch in ALPHA_SET:
            dist[ch] = p
    return dist


def _surah_body_letters_after_opener(surah_id):
    """Return the rasm-normalized letter string of surah BODY, with
    muqaṭṭaʿāt opener stripped (for muqaṭṭaʿāt surahs) or first 4 letters
    stripped (for non-muqaṭṭaʿāt surahs).

    Per body_window 0% decision: 0% mark = first non-opener character
    (option (a), classical-scholar sign-off 2026-04-13).
    """
    quran = _load_quran()
    surah = quran[surah_id]
    full = ''.join(v['text'] for v in surah['verses'])
    letters = clean_letters(full)
    if surah_id in MUQATTAAT_SURAHS:
        # Strip the muqaṭṭaʿāt opener. The opener lives in verse 1 (and
        # verse 2 for Q42). We strip as many leading characters as the
        # muqaṭṭaʿāt word-sequence occupies in the raw verses so that the
        # 0% mark lands at the first non-muqaṭṭaʿāt character.
        if surah_id == 42:
            # Q42 verses 1+2 are the full muqaṭṭaʿāt: حم + عسق
            opener_raw = clean_letters(
                surah['verses'][0]['text'] + surah['verses'][1]['text']
            )
        else:
            opener_raw = clean_letters(surah['verses'][0]['text'])
        # Defensive: opener_raw should prefix letters. If not (unexpected
        # normalization edge), fall back to letter-set stripping.
        if letters.startswith(opener_raw):
            return letters[len(opener_raw):]
        # Fallback: strip every character that appears in the opener set
        # from the leading run.
        opener_set = set(MUQATTAAT_OPENER[surah_id])
        idx = 0
        while idx < len(letters) and letters[idx] in opener_set:
            idx += 1
        return letters[idx:]
    # Non-muqaṭṭaʿāt: strip first 4 letters as the "baseline opener."
    return letters[BASELINE_OPENER_N_CHARS:]


def _non_muqattaat_baseline_opener_letters(surah_id):
    """First 4 rasm-normalized letters of a non-muqaṭṭaʿāt surah as the
    baseline 'opener' per pre-reg."""
    quran = _load_quran()
    surah = quran[surah_id]
    full = ''.join(v['text'] for v in surah['verses'])
    letters = clean_letters(full)
    return tuple(letters[:BASELINE_OPENER_N_CHARS])


# ============================================================================
# PUBLIC API
# ============================================================================

def extract_muqattaat_opener_multiset(surah_id, split_q42=False):
    """Return uniform-on-support probability distribution over the 28-letter
    alphabet representing the muqaṭṭaʿāt opener (or baseline first-4-letters
    opener for non-muqaṭṭaʿāt surahs).

    Parameters
    ----------
    surah_id : int (1..114)
    split_q42 : bool, default False
        If True and surah_id==42, returns a tuple of TWO distributions
        (one for حم, one for عسق) for sensitivity-5 Q42-split breakdown.
        Primary test uses split_q42=False (5-letter union).

    Returns
    -------
    dict[str, float]  (or tuple of two such dicts when split_q42=True)
    """
    if surah_id < 1 or surah_id > 114:
        raise ValueError(f"surah_id out of range: {surah_id}")

    if surah_id == 42 and split_q42:
        return tuple(
            _uniform_dist(letters) for letters in MUQATTAAT_OPENER_Q42_SPLIT
        )

    if surah_id in MUQATTAAT_SURAHS:
        return _uniform_dist(MUQATTAAT_OPENER[surah_id])

    # Non-muqaṭṭaʿāt: uniform-on-support over first 4 letters of the surah
    # (with multiplicity collapsed to unique-set per pre-reg "uniform-on-
    # support" construction).
    baseline = _non_muqattaat_baseline_opener_letters(surah_id)
    return _uniform_dist(set(baseline))


def extract_body_letter_multiset(surah_id, exclude_opener=True,
                                 body_window=(0.0, 1.0), alpha=0.01):
    """Return empirical letter probability distribution over the surah body.

    Parameters
    ----------
    surah_id : int (1..114)
    exclude_opener : bool, default True
        If True, strip the muqaṭṭaʿāt opener (or first 4 letters for non-
        muqaṭṭaʿāt surahs) before computing the body distribution. This is
        the standard operationalization per pre-reg.
    body_window : (float, float), default (0.0, 1.0)
        Fractional window (start_pct, end_pct) over the body letter-stream
        AFTER opener stripping. 0% mark = first non-opener character
        (classical-scholar sign-off 2026-04-13 option (a)). Use
        (0.0, 0.2) for early-body, (0.2, 1.0) for late-body per
        sensitivity-4.
    alpha : float, default 0.01
        Laplace smoothing constant. Added to every alphabet slot before
        normalization.

    Returns
    -------
    dict[str, float]  — sums to 1.0 over ALPHABET support.
    """
    if surah_id < 1 or surah_id > 114:
        raise ValueError(f"surah_id out of range: {surah_id}")
    start_pct, end_pct = body_window
    if not (0.0 <= start_pct < end_pct <= 1.0):
        raise ValueError(
            f"body_window must be (start,end) with 0<=start<end<=1, got {body_window}"
        )

    if exclude_opener:
        body_letters = _surah_body_letters_after_opener(surah_id)
    else:
        quran = _load_quran()
        surah = quran[surah_id]
        full = ''.join(v['text'] for v in surah['verses'])
        body_letters = clean_letters(full)

    nb = len(body_letters)
    if nb == 0:
        # Degenerate — shouldn't happen for any real surah, but be safe.
        return {ch: 1.0 / len(ALPHABET) for ch in ALPHABET}

    start_idx = int(round(start_pct * nb))
    end_idx = int(round(end_pct * nb))
    window = body_letters[start_idx:end_idx]

    counts = {ch: 0 for ch in ALPHABET}
    for ch in window:
        if ch in counts:
            counts[ch] += 1

    # Laplace smoothing: add alpha to every slot, normalize.
    A = len(ALPHABET)
    total = sum(counts.values()) + alpha * A
    return {ch: (counts[ch] + alpha) / total for ch in ALPHABET}


def _smooth(P, alpha):
    """Apply Laplace smoothing α to every alphabet slot of P, renormalize."""
    A = len(ALPHABET)
    total = sum(P.get(ch, 0.0) for ch in ALPHABET) + alpha * A
    return {ch: (P.get(ch, 0.0) + alpha) / total for ch in ALPHABET}


def kl_divergence(P_body, P_open, alpha=0.01):
    """Compute D_KL(P_body || P_open) in nats, with Laplace smoothing
    applied to P_open (P_body is assumed already smoothed).

    P_body and P_open are dict[str, float] over ALPHABET. If P_open has
    zero-mass slots (which it always does when the opener is uniform-on-
    support with only a few letters), alpha smoothing is applied here to
    make the divergence finite.

    Per team-lead ruling 2026-04-13, KL is demoted from primary to
    SENSITIVITY-0 (archaeological-continuity record of the MW-10 support-
    size confound). Primary statistic is JS-divergence (see js_divergence).

    Returns
    -------
    float  — non-negative KL divergence in nats.
    """
    p_open_smoothed = _smooth(P_open, alpha)
    kl = 0.0
    for ch in ALPHABET:
        pb = P_body.get(ch, 0.0)
        po = p_open_smoothed[ch]
        if pb > 0.0 and po > 0.0:
            kl += pb * math.log(pb / po)
    return kl


def js_divergence(P_body, P_open, alpha=0.01):
    """Compute Jensen-Shannon divergence between P_body and P_open in nats.

    JS(P, Q) = ½ [D_KL(P ‖ M) + D_KL(Q ‖ M)]  where M = ½ (P + Q)

    JS ∈ [0, log 2] regardless of support asymmetry, symmetric in its
    arguments, and bounded — which eliminates the support-size confound
    that KL-divergence suffers when one distribution has a highly
    concentrated support (e.g., Q50 ق opener with P(ق)=1).

    This is the H-NEW-4-EXT-D PRIMARY statistic per team-lead ruling
    2026-04-13 (MW-10 founding instance; letter_multiset.py self-test
    descriptive catch). Direction preserved from original pre-reg:
    Δ_JS = JS_muqaṭṭaʿāt − JS_baseline < 0 predicted.

    Laplace smoothing is applied to both P_body and P_open before mixture
    computation to handle zero-mass slots gracefully; alpha exposed for
    sensitivity sweeps.

    Returns
    -------
    float  — non-negative JS divergence in nats, bounded above by log 2.
    """
    p_b = _smooth(P_body, alpha)
    p_o = _smooth(P_open, alpha)
    M = {ch: 0.5 * (p_b[ch] + p_o[ch]) for ch in ALPHABET}
    kl_bm = 0.0
    kl_om = 0.0
    for ch in ALPHABET:
        pb = p_b[ch]
        po = p_o[ch]
        m = M[ch]
        if pb > 0.0 and m > 0.0:
            kl_bm += pb * math.log(pb / m)
        if po > 0.0 and m > 0.0:
            kl_om += po * math.log(po / m)
    return 0.5 * (kl_bm + kl_om)


def hellinger_distance(P_body, P_open, alpha=0.0):
    """Compute Hellinger distance between P_body and P_open.

    H(P, Q) = (1/√2) · sqrt(Σ (√p_i − √q_i)²)

    H ∈ [0, 1]. The square-root handles zero-mass slots cleanly, so
    Laplace smoothing is not strictly necessary; alpha defaults to 0.
    Pass a positive alpha only for sensitivity comparison against the
    smoothed JS/KL reference.

    This is H-NEW-4-EXT-D SENSITIVITY-2 per team-lead ruling 2026-04-13.
    Added specifically because Hellinger weights mass-on-support vs
    support-overlap differently than JS, so agreement between the two
    gives stronger robustness than either alone.

    Returns
    -------
    float  — non-negative Hellinger distance, bounded above by 1.
    """
    if alpha > 0.0:
        p_b = _smooth(P_body, alpha)
        p_o = _smooth(P_open, alpha)
    else:
        p_b = {ch: P_body.get(ch, 0.0) for ch in ALPHABET}
        p_o = {ch: P_open.get(ch, 0.0) for ch in ALPHABET}
    acc = 0.0
    for ch in ALPHABET:
        d = math.sqrt(p_b[ch]) - math.sqrt(p_o[ch])
        acc += d * d
    return math.sqrt(acc) / math.sqrt(2.0)


def opener_support_size(surah_id):
    """Return k = cardinality of the opener letter set for surah_id.
    For muqaṭṭaʿāt surahs, k is the unique count of muqaṭṭaʿāt letters.
    For non-muqaṭṭaʿāt surahs, k is the unique count among the first 4
    rasm-normalized body letters (typically 3 or 4). Used for
    support-size stratification in SENSITIVITY-1.
    """
    if surah_id in MUQATTAAT_SURAHS:
        return len(set(MUQATTAAT_OPENER[surah_id]))
    baseline = _non_muqattaat_baseline_opener_letters(surah_id)
    return len(set(baseline))


# ============================================================================
# SELF-TEST
# ============================================================================

def _selftest():
    """Sanity-check the three exported functions. Run as:
        python3 scripts/letter_multiset.py
    """
    import sys

    def _assert(cond, msg):
        if not cond:
            print(f"FAIL: {msg}", file=sys.stderr)
            sys.exit(1)

    # Test 1: Q2 opener → {ا, ل, م} uniform
    p = extract_muqattaat_opener_multiset(2)
    _assert(abs(p['ا'] - 1/3) < 1e-9, f"Q2 P(ا)={p['ا']}, expected 1/3")
    _assert(abs(p['ل'] - 1/3) < 1e-9, f"Q2 P(ل)={p['ل']}, expected 1/3")
    _assert(abs(p['م'] - 1/3) < 1e-9, f"Q2 P(م)={p['م']}, expected 1/3")
    _assert(p['ب'] == 0.0, f"Q2 P(ب)={p['ب']}, expected 0")
    print("PASS: Q2 opener uniform-on-support {ا,ل,م}")

    # Test 2: Q19 opener → {ك, ه, ي, ع, ص} uniform
    p = extract_muqattaat_opener_multiset(19)
    for ch in ('ك', 'ه', 'ي', 'ع', 'ص'):
        _assert(abs(p[ch] - 1/5) < 1e-9, f"Q19 P({ch})={p[ch]}, expected 1/5")
    print("PASS: Q19 opener uniform-on-support {ك,ه,ي,ع,ص}")

    # Test 3: Q50 opener → {ق} → P(ق)=1.0
    p = extract_muqattaat_opener_multiset(50)
    _assert(abs(p['ق'] - 1.0) < 1e-9, f"Q50 P(ق)={p['ق']}, expected 1.0")
    print("PASS: Q50 opener {ق} → P(ق)=1.0")

    # Test 4: Q42 UNION primary = 5 letters, each 1/5
    p = extract_muqattaat_opener_multiset(42)
    for ch in ('ح', 'م', 'ع', 'س', 'ق'):
        _assert(abs(p[ch] - 1/5) < 1e-9, f"Q42 P({ch})={p[ch]}, expected 1/5")
    print("PASS: Q42 opener UNION {ح,م,ع,س,ق}")

    # Test 5: Q42 split construction → tuple of 2 dists
    p1, p2 = extract_muqattaat_opener_multiset(42, split_q42=True)
    _assert(abs(p1['ح'] - 1/2) < 1e-9 and abs(p1['م'] - 1/2) < 1e-9,
            f"Q42 split-1 expected {{ح,م}} each 1/2, got ح={p1['ح']} م={p1['م']}")
    for ch in ('ع', 'س', 'ق'):
        _assert(abs(p2[ch] - 1/3) < 1e-9,
                f"Q42 split-2 P({ch})={p2[ch]}, expected 1/3")
    print("PASS: Q42 split sensitivity-5 (حم / عسق)")

    # Test 6: Q1 (non-muqaṭṭaʿāt) baseline opener = first 4 letters
    # after rasm normalization. Q1:1 is "بسم الله الرحمن الرحيم".
    # Letters = بسماللهالرحمنالرحيم → first 4 = {ب,س,م,ا}
    p = extract_muqattaat_opener_multiset(1)
    nonzero = {ch: v for ch, v in p.items() if v > 0.0}
    print(f"  Q1 baseline opener non-zero letters: {nonzero}")
    _assert(len(nonzero) == 4 and
            all(abs(v - 0.25) < 1e-9 for v in nonzero.values()),
            f"Q1 expected 4 unique letters at 0.25 each, got {nonzero}")
    print("PASS: Q1 baseline opener = first 4 letters uniform")

    # Test 7: Q2 body distribution sums to 1.0
    body = extract_body_letter_multiset(2)
    s = sum(body.values())
    _assert(abs(s - 1.0) < 1e-9, f"Q2 body sum = {s}, expected 1.0")
    _assert(all(v > 0 for v in body.values()),
            "Q2 body should have all positive values after Laplace smoothing")
    print(f"PASS: Q2 body sums to 1.0, all slots positive after smoothing")

    # Test 8: Q2 body_window (0.0, 0.2) early-body is smaller than full
    early = extract_body_letter_multiset(2, body_window=(0.0, 0.2))
    late = extract_body_letter_multiset(2, body_window=(0.2, 1.0))
    _assert(abs(sum(early.values()) - 1.0) < 1e-9, "early body sums to 1")
    _assert(abs(sum(late.values()) - 1.0) < 1e-9, "late body sums to 1")
    print("PASS: Q2 early-body and late-body windows both valid distributions")

    # Test 9: KL divergence Q2 body || Q2 opener is finite and positive
    body = extract_body_letter_multiset(2)
    opener = extract_muqattaat_opener_multiset(2)
    kl = kl_divergence(body, opener)
    _assert(kl > 0 and math.isfinite(kl),
            f"Q2 KL = {kl}, expected finite positive")
    print(f"PASS: Q2 KL(body || opener) = {kl:.4f} nats (finite, positive)")

    # Test 10: KL divergence is zero when distributions identical (sanity)
    p = {ch: 1.0 / len(ALPHABET) for ch in ALPHABET}
    kl = kl_divergence(p, p)
    _assert(abs(kl) < 1e-9, f"KL(p||p) = {kl}, expected 0")
    print("PASS: KL(p||p) = 0 for uniform p")

    # Test 11: Alpha smoothing sensitivity — higher alpha → lower KL
    body = extract_body_letter_multiset(2)
    opener = extract_muqattaat_opener_multiset(2)
    kl_low = kl_divergence(body, opener, alpha=0.001)
    kl_mid = kl_divergence(body, opener, alpha=0.01)
    kl_high = kl_divergence(body, opener, alpha=0.1)
    _assert(kl_low > kl_mid > kl_high,
            f"alpha monotonicity broken: {kl_low:.4f} {kl_mid:.4f} {kl_high:.4f}")
    print(f"PASS: Q2 KL alpha sensitivity "
          f"(0.001={kl_low:.4f}, 0.01={kl_mid:.4f}, 0.1={kl_high:.4f})")

    # Test 12: All 29 muqaṭṭaʿāt surahs produce valid openers
    for sid in sorted(MUQATTAAT_SURAHS):
        p = extract_muqattaat_opener_multiset(sid)
        s = sum(p.values())
        _assert(abs(s - 1.0) < 1e-9,
                f"muqaṭṭaʿāt surah {sid} opener sum = {s}, expected 1.0")
    print(f"PASS: all 29 muqaṭṭaʿāt-opener distributions sum to 1.0")

    # Test 13: All 114 surahs produce valid body distributions
    for sid in range(1, 115):
        body = extract_body_letter_multiset(sid)
        s = sum(body.values())
        _assert(abs(s - 1.0) < 1e-6,
                f"surah {sid} body sum = {s}, expected 1.0")
    print(f"PASS: all 114 surahs produce valid body distributions")

    # Test 14: JS divergence is bounded in [0, log 2] and symmetric
    body = extract_body_letter_multiset(2)
    opener = extract_muqattaat_opener_multiset(2)
    js_bo = js_divergence(body, opener)
    js_ob = js_divergence(opener, body)
    _assert(0 <= js_bo <= math.log(2) + 1e-9,
            f"JS out of bounds: {js_bo}, expected [0, {math.log(2):.4f}]")
    _assert(abs(js_bo - js_ob) < 1e-9,
            f"JS not symmetric: js(b,o)={js_bo}, js(o,b)={js_ob}")
    _assert(abs(js_divergence(body, body)) < 1e-9,
            f"JS(p,p)={js_divergence(body, body)}, expected 0")
    print(f"PASS: JS(Q2 body, Q2 opener) = {js_bo:.4f} nats "
          f"(bounded, symmetric, JS(p,p)=0)")

    # Test 15: Hellinger distance is bounded in [0, 1] and symmetric
    h_bo = hellinger_distance(body, opener)
    h_ob = hellinger_distance(opener, body)
    _assert(0 <= h_bo <= 1 + 1e-9,
            f"Hellinger out of bounds: {h_bo}, expected [0, 1]")
    _assert(abs(h_bo - h_ob) < 1e-9,
            f"Hellinger not symmetric: h(b,o)={h_bo}, h(o,b)={h_ob}")
    _assert(abs(hellinger_distance(body, body)) < 1e-9,
            f"Hellinger(p,p)={hellinger_distance(body, body)}, expected 0")
    print(f"PASS: Hellinger(Q2 body, Q2 opener) = {h_bo:.4f} "
          f"(bounded [0,1], symmetric, H(p,p)=0)")

    # Test 16: opener_support_size behaves as expected
    _assert(opener_support_size(2) == 3, "Q2 k=3 expected (الم)")
    _assert(opener_support_size(19) == 5, "Q19 k=5 expected (كهيعص)")
    _assert(opener_support_size(50) == 1, "Q50 k=1 expected (ق)")
    _assert(opener_support_size(42) == 5, "Q42 k=5 expected (union حم+عسق)")
    _assert(opener_support_size(1) in (3, 4),
            f"Q1 expected k∈{{3,4}}, got {opener_support_size(1)}")
    print("PASS: opener_support_size correct for Q2, Q19, Q50, Q42, Q1")

    # Test 17: Full-corpus descriptive sweep under all three metrics,
    # stratified by opener support size (MW-10 founding instance).
    metrics = {
        'KL':        lambda b, o: kl_divergence(b, o),
        'JS':        lambda b, o: js_divergence(b, o),
        'Hellinger': lambda b, o: hellinger_distance(b, o),
    }
    muq_vals = {name: [] for name in metrics}
    nonmuq_vals = {name: [] for name in metrics}
    by_k = {}  # k → {name: [vals...]}
    for sid in range(1, 115):
        body = extract_body_letter_multiset(sid)
        opener = extract_muqattaat_opener_multiset(sid)
        k = opener_support_size(sid)
        row = by_k.setdefault(k, {name: [] for name in metrics})
        for name, fn in metrics.items():
            v = fn(body, opener)
            row[name].append((sid, v))
            if sid in MUQATTAAT_SURAHS:
                muq_vals[name].append(v)
            else:
                nonmuq_vals[name].append(v)

    print("\n  [descriptive] Full-corpus sweep under 3 metrics:")
    print("  metric       muq_mean    non-muq_mean   Δ (muq - nonmuq)   pre-reg direction")
    print("  ----------   ---------   ------------   ----------------   -----------------")
    for name in ('KL', 'JS', 'Hellinger'):
        mm = sum(muq_vals[name]) / len(muq_vals[name])
        nm = sum(nonmuq_vals[name]) / len(nonmuq_vals[name])
        delta = mm - nm
        print(f"  {name:10s}   {mm:7.4f}    {nm:10.4f}    {delta:+15.4f}   "
              f"{'Δ < 0 expected'}")

    print("\n  [descriptive] MW-10 support-size stratification "
          "(muq-only, by k = opener cardinality):")
    print("  k   n_muq   KL       JS       Hellinger   example surahs")
    print("  --  -----   ------   ------   ---------   -----------------")
    for k in sorted(by_k):
        muq_in_k = [
            (sid, row)
            for sid, row in enumerate(by_k[k]['KL'])
            if row[0] in MUQATTAAT_SURAHS
        ]
        # Rebuild muq-only per-k lists directly
        muq_k_kl = [v for sid, v in by_k[k]['KL'] if sid in MUQATTAAT_SURAHS]
        muq_k_js = [v for sid, v in by_k[k]['JS'] if sid in MUQATTAAT_SURAHS]
        muq_k_h  = [v for sid, v in by_k[k]['Hellinger'] if sid in MUQATTAAT_SURAHS]
        n = len(muq_k_kl)
        if n == 0:
            continue
        muq_ids = sorted(
            sid for sid, _ in by_k[k]['KL'] if sid in MUQATTAAT_SURAHS
        )
        examples = ', '.join(f'Q{sid}' for sid in muq_ids[:5])
        if len(muq_ids) > 5:
            examples += ', ...'
        print(f"  {k}   {n:5d}   "
              f"{sum(muq_k_kl)/n:6.3f}   "
              f"{sum(muq_k_js)/n:6.3f}   "
              f"{sum(muq_k_h)/n:9.3f}   {examples}")

    print("\n  NOTE: these descriptive sweeps are NOT the pre-reg verdict.")
    print("  Computational-tester runs the full permutation test with null")
    print("  model per h-new-4-ext-d-prereg.md.")
    print("  PRIMARY = JS-divergence (team-lead 2026-04-13 ruling).")
    print("  SENSITIVITY-0 = KL (MW-10 archaeological).")
    print("  SENSITIVITY-2 = Hellinger.")

    print("\nALL SELF-TESTS PASSED")


if __name__ == '__main__':
    _selftest()
