#!/usr/bin/env python3
"""
al-Kamil deterministic scanner.
Input: a phoneme skeleton string per hemistich using a tiny alphabet:
   C  = any consonant (single, moving onset slot is implied)
   We do NOT track consonant identity; we track the SYLLABIC skeleton directly.

Simpler, less error-prone approach: I transcribe each hemistich directly into an
explicit list of SYLLABLES, each marked light (v) or heavy (-), by applying classical
waṣl pronunciation by hand. Then the engine ONLY does foot-splitting + legality.
That keeps the mechanical part honest (it cannot 'see' the words) while the
transcription is the scholarly judgment, logged per hemistich.

Mora notation in the input strings:
   u  = light syllable  (CV, short vowel, open)
   -  = heavy syllable   (CVV long-vowel open, OR CVC closed short)
   =  = superheavy (CVVC / CVCC) -> counts as '- u' equivalently? NO.
        In Arabic ʿarūḍ a final superheavy at line end is just heavy (the coda
        is extrametrical at pure line-end) OR resolves – – internally. We avoid
        '=' by transcribing line-internal superheavy as two units '- u'?
        Actually CVVC / CVCC line-internally = one heavy + ... — we handle by
        hand in transcription, emitting the watid/sabab units directly.
   So input is ONLY 'u' and '-' characters (+ spaces ignored).

al-Kamil feet (each = 5 morae, watid majmuʿ + 2 asbab):
   salim   mutaFAAilun   u u - u -
   idmar   mutFAAilun    - - u -      (2nd sabab thaqil -> sabab khafif)
   waqs    muFAAilun     u - u -      (1st light dropped) LEGAL-but-qabih
For the ṢADR (ʿarūḍ ṣaḥīḥa): 3 feet, last foot ends '... u -' (i.e. ends u -).
   so ʿarūḍ foot ∈ {u u - u - , - - u - , u - u -}  (ends u -)  ✓
For the ʿAJUZ: 2 hashw feet + locked ḍarب 'maqṭūʿ+iḍmār' = - - -
   ḍarب foot MUST be exactly '- - -' (3 heavies)
   hashw feet ∈ {u u - u - , - - u - , u - u -}
We brute force a segmentation of the mora string into feet from this inventory.
Report: which feet, whether waqṣ present (qabih flag), or BREAK.
"""
import sys, itertools

SADR_FEET   = ['uu-u-', '--u-', 'u-u-']   # ends 'u -'   (salim, idmar, waqs)
HASHW_FEET  = ['uu-u-', '--u-', 'u-u-']
DARB        = '---'                         # locked maqtuʿ+idmar

WAQS = 'u-u-'

def seg(mora, feet_inventory, last_foot=None, nfeet=None):
    """Return list of all segmentations of `mora` into feet from inventory.
       If last_foot given, the final foot must equal last_foot.
       If nfeet given, require exactly that many feet."""
    results=[]
    def rec(rem, acc):
        if not rem:
            if last_foot is not None and (not acc or acc[-1]!=last_foot):
                return
            if nfeet is not None and len(acc)!=nfeet:
                return
            results.append(list(acc))
            return
        for f in feet_inventory:
            if rem.startswith(f):
                rec(rem[len(f):], acc+[f])
        # also allow the locked darb as a candidate final
        if last_foot is not None and rem==last_foot:
            rec('', acc+[rem])
    rec(mora, [])
    return results

def scan_sadr(mora):
    mora=mora.replace(' ','')
    # ṣadr: any number of feet (canonically 3) all from SADR_FEET, AND the
    # whole string must end in 'u-' (ʿarūḍ ṣaḥīḥa). Foot inventory already ends u-.
    segs = seg(mora, SADR_FEET, nfeet=3)
    if not segs:
        # try without nfeet constraint to see if it's a length problem
        any_seg = seg(mora, SADR_FEET)
        return ('BREAK', mora, any_seg)
    # prefer a segmentation; flag waqṣ
    best=segs[0]
    waqs = any(WAQS in s for s in [best])  # waqṣ feet present
    waqs_positions=[i for i,f in enumerate(best) if f==WAQS]
    tag='OK' if not waqs_positions else f'WAQS@{waqs_positions}'
    return (tag, mora, best)

def scan_ajuz(mora):
    mora=mora.replace(' ','')
    if not mora.endswith(DARB):
        # could still be wrong; report
        segs=[]
    body=mora[:-len(DARB)]
    segs = seg(body, HASHW_FEET, nfeet=2)
    if not (mora.endswith(DARB) and segs):
        any_seg = seg(mora, HASHW_FEET+[DARB])
        return ('BREAK', mora, any_seg)
    best=segs[0]+[DARB]
    waqs_positions=[i for i,f in enumerate(best) if f==WAQS]
    tag='OK' if not waqs_positions else f'WAQS@{waqs_positions}'
    return (tag, mora, best)

if __name__=='__main__':
    pass
