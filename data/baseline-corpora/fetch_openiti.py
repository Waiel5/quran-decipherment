#!/usr/bin/env python3
"""
Download specific OpenITI text files (raw mARkdown), strip header/markup,
and save to baseline-corpora/raw/.

OpenITI mARkdown rules used here:
  - Lines beginning with `######OpenITI#` mark the file header (not text).
  - Lines beginning with `#META#` are bibliographic metadata.
  - The `#META#Header#End#` marker (or repeated `#META#` block ends) precedes the body.
  - In the body, lines may begin with `#`, `###`, `### |`, `### ||`, etc.
    These are structural markers (book / chapter / paragraph) and should be
    stripped, but the trailing text on those lines is part of the body.
  - `~~` is a hard line break inside a paragraph; replace with space.
  - `%~%` is a soft line break.
  - `@QUR@... @` and `@HADITH@... @` markers tag quoted Quran/hadith.
    For the cross-textual baseline we *strip Quranic quotations* from
    Bukhari and Sira so we don't trivially correlate the baseline with the
    Quran. We do this by deleting any line that contains a Quran-quotation
    marker, and by deleting all `@QUR@.*?@` inline spans.
  - Page markers like `PageV01P123` are stripped.
"""
from __future__ import annotations

import re
import sys
import urllib.request
from pathlib import Path

OUT = Path("/Users/grey/Downloads/quran/data/baseline-corpora/raw")
OUT.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (compatible; QuranBaselineFetcher/1.0; research)"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8", errors="replace")


def strip_openiti(text: str, drop_quranic: bool = False) -> str:
    """Strip OpenITI mARkdown headers/markup. Returns plaintext Arabic."""
    lines = text.split("\n")
    out = []
    in_header = True
    for line in lines:
        # Drop the OpenITI banner line
        if line.startswith("######OpenITI#"):
            in_header = True
            continue
        # All metadata lines
        if line.startswith("#META#"):
            in_header = True
            continue
        # Once we see a non-empty non-meta non-banner line, header is over
        if in_header and not line.strip():
            continue
        in_header = False

        # Drop pure ML markers
        if re.match(r"^\s*###", line):
            # Strip the leading "### " markers; keep trailing text
            line = re.sub(r"^\s*###[\s|]*", "", line)
        # Strip leading single '#' (paragraph marker in mARkdown)
        line = re.sub(r"^\s*#\s*", "", line)
        # Strip structural pipes
        line = line.lstrip("|").lstrip()
        # Strip poetry hemistich markers '%' (used in OpenITI to mark
        # the boundary between two halves of a line of verse)
        line = line.replace("%", " ")

        # Page markers
        line = re.sub(r"PageV\d+P\d+", "", line)
        # Soft/hard breaks
        line = line.replace("~~", " ")
        line = line.replace("%~%", " ")
        # Inline tags: @QUR@xxx@, @HADITH@xxx@
        if drop_quranic:
            # remove Quran-quotation spans entirely
            line = re.sub(r"@QUR\d*@[^@]*@", " ", line)
            # also drop any line that is solely a Quran quote marker
        line = re.sub(r"@[A-Z][A-Z0-9]*@", " ", line)
        line = re.sub(r"@[a-zA-Z]+@", " ", line)
        # Strip ms-marker like ms1
        line = re.sub(r"\bms\d+\b", " ", line)
        # Collapse spaces
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            out.append(line)

    text = "\n".join(out)
    return text


# (slug, raw url, drop_quranic_quotations)
TARGETS = [
    # Mu'allaqat poets (full diwans, much longer than just the mu'allaqa)
    (
        "diwan-imru-al-qais",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001ImruQaysIbnHujr/0001ImruQaysIbnHujr.Diwan/0001ImruQaysIbnHujr.Diwan.Shamela0027112-ara1",
        False,
    ),
    (
        "diwan-tarafa",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001TarafaIbnCabd/0001TarafaIbnCabd.Diwan/0001TarafaIbnCabd.Diwan.Shamela0036422-ara1",
        False,
    ),
    (
        "diwan-zuhayr",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001ZuhayrIbnAbiSulma/0001ZuhayrIbnAbiSulma.Diwan/0001ZuhayrIbnAbiSulma.Diwan.JK007516-ara1",
        False,
    ),
    (
        "diwan-antara",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001CantaraIbnShaddad/0001CantaraIbnShaddad.Diwan/0001CantaraIbnShaddad.Diwan.ShamAY0037906-ara1",
        False,
    ),
    (
        "diwan-amr-ibn-kulthum",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001CamrIbnKulthum/0001CamrIbnKulthum.Diwan/0001CamrIbnKulthum.Diwan.ShamAY0037904-ara1",
        False,
    ),
    (
        "diwan-harith",
        "https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001HarithIbnHilliza/0001HarithIbnHilliza.Diwan/0001HarithIbnHilliza.Diwan.ShamAY0037848-ara1",
        False,
    ),
    (
        "diwan-labid",
        "https://raw.githubusercontent.com/OpenITI/0050AH/master/data/0041LabidIbnRabica/0041LabidIbnRabica.Diwan/0041LabidIbnRabica.Diwan.Shamela0035077-ara1",
        False,
    ),
    # Mutanabbi (full diwan from JK)
    (
        "mutanabbi-diwan",
        "https://raw.githubusercontent.com/OpenITI/0375AH/master/data/0354Mutanabbi/0354Mutanabbi.Diwan/0354Mutanabbi.Diwan.JK007610-ara1.completed",
        False,
    ),
    # Jahiz - Kitab al-Hayawan (Shamela completed version)
    (
        "jahiz-hayawan",
        "https://raw.githubusercontent.com/OpenITI/0275AH/master/data/0255Jahiz/0255Jahiz.Hayawan/0255Jahiz.Hayawan.Shamela0023775-ara1.completed",
        True,
    ),
    # Sira ibn Hisham (Shamela completed)
    (
        "sira-ibn-hisham-openiti",
        "https://raw.githubusercontent.com/OpenITI/0225AH/master/data/0213IbnHisham/0213IbnHisham.SiraNabawiyya/0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1.completed",
        True,
    ),
]


if __name__ == "__main__":
    for slug, url, drop_qur in TARGETS:
        try:
            raw = fetch(url)
        except Exception as e:
            print(f"FAIL {slug}: {e}", file=sys.stderr)
            continue
        clean = strip_openiti(raw, drop_quranic=drop_qur)
        (OUT / f"{slug}.openiti.raw.txt").write_text(raw, encoding="utf-8")
        (OUT / f"{slug}.txt").write_text(clean, encoding="utf-8")
        print(f"{slug}: raw={len(raw)} clean={len(clean)} (drop_qur={drop_qur})")
