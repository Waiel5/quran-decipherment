#!/usr/bin/env python3
"""Build LTR English PDF from a markdown deliverable via Chrome headless.

Usage:
  build_ltr_pdf.py <md_path> <pdf_path> <cover_title> <cover_subtitle>

Notes:
  - English/LTR body, serif font stack
  - Arabic blockquotes retain Amiri/Noto Naskh styling (auto by unicode range)
  - A4, 2.5cm margins, page numbers at bottom-center
  - Navy/gold colour palette matching the Arabic build_pdf.py
"""

import subprocess, os, sys, re, html

if len(sys.argv) != 5:
    print('Usage: build_ltr_pdf.py <md_path> <pdf_path> <cover_title> <cover_subtitle>')
    sys.exit(2)

MD_PATH = sys.argv[1]
PDF_PATH = sys.argv[2]
COVER_TITLE = sys.argv[3]
COVER_SUBTITLE = sys.argv[4]
HTML_PATH = PDF_PATH.rsplit('.', 1)[0] + '.html'
DATE_STR = '2026-04-12'

# --- Markdown → HTML (compatible superset of the RTL converter) ---

ARABIC_RE = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')

def has_arabic(s):
    return bool(ARABIC_RE.search(s))


def md_to_html(md):
    lines = md.split('\n')
    out = []
    in_table = False
    table_rows = []
    in_blockquote = False
    blockquote_buf = []
    in_code = False
    code_buf = []
    code_lang = ''

    def flush_blockquote():
        nonlocal in_blockquote, blockquote_buf
        if in_blockquote and blockquote_buf:
            # Decide class: if any line contains Arabic, treat as Arabic quote
            cls = 'arabic' if any(has_arabic(l) for l in blockquote_buf) else 'english'
            out.append(f'<blockquote class="quote-{cls}">')
            for line in blockquote_buf:
                out.append(f'<p>{line}</p>')
            out.append('</blockquote>')
            blockquote_buf = []
        in_blockquote = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            out.append('<table>')
            start = 0
            if len(table_rows) > 1 and re.match(r'^\s*\|?[\s\-:|]+\|?\s*$', table_rows[1]):
                headers = [c.strip() for c in table_rows[0].strip().strip('|').split('|')]
                out.append('<thead><tr>' + ''.join(f'<th>{inline(h)}</th>' for h in headers) + '</tr></thead>')
                start = 2
            out.append('<tbody>')
            for row in table_rows[start:]:
                cells = [c.strip() for c in row.strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
            out.append('</tbody></table>')
            table_rows = []
        in_table = False

    def flush_code():
        nonlocal in_code, code_buf, code_lang
        if in_code:
            code_text = html.escape('\n'.join(code_buf), quote=False)
            out.append(f'<pre class="code"><code>{code_text}</code></pre>')
            code_buf = []
            code_lang = ''
            in_code = False

    def inline(s):
        # Handle Arabic inline spans: wrap runs of Arabic chars for proper font
        # Escape first
        s = html.escape(s, quote=False)
        # bold **text**
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        # italic *text*
        s = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
        # inline code
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        # links [text](url)
        s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
        # Wrap Arabic runs (after other processing) for font targeting
        def wrap_ar(m):
            return f'<span class="ar">{m.group(0)}</span>'
        s = re.sub(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF][\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF\s\u064B-\u065F\u0670\u06D6-\u06ED]*', wrap_ar, s)
        return s

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Fenced code blocks ```
        if stripped.startswith('```'):
            if not in_code:
                flush_blockquote(); flush_table()
                in_code = True
                code_lang = stripped[3:].strip()
            else:
                flush_code()
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Table detection
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                flush_blockquote()
                in_table = True
            table_rows.append(line)
            i += 1
            continue
        else:
            if in_table:
                flush_table()

        # Blockquote detection
        if stripped.startswith('>'):
            if not in_blockquote:
                in_blockquote = True
            content = stripped[1:].strip()
            if content:
                blockquote_buf.append(inline(content))
            i += 1
            continue
        else:
            if in_blockquote and not stripped:
                if i+1 < len(lines) and lines[i+1].strip().startswith('>'):
                    i += 1
                    continue
                else:
                    flush_blockquote()
            elif in_blockquote:
                flush_blockquote()

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = min(len(m.group(1)), 4)
            text = inline(m.group(2))
            out.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+\s*$', stripped) or re.match(r'^\*\*\*+\s*$', stripped):
            out.append('<hr>')
            i += 1
            continue

        # Unordered list
        if re.match(r'^\s*[-*+]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*+]\s+', lines[i]):
                item_text = re.sub(r'^\s*[-*+]\s+', '', lines[i])
                items.append(inline(item_text))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{t}</li>' for t in items) + '</ul>')
            continue

        # Ordered list
        if re.match(r'^\s*\d+\.\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                item_text = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                items.append(inline(item_text))
                i += 1
            out.append('<ol>' + ''.join(f'<li>{t}</li>' for t in items) + '</ol>')
            continue

        # Footer-style italic-only paragraph
        if stripped.startswith('*') and stripped.endswith('*') and len(stripped) > 2 and not stripped.startswith('**'):
            out.append(f'<p class="footer-note"><em>{inline(stripped[1:-1])}</em></p>')
            i += 1
            continue

        if stripped:
            out.append(f'<p>{inline(stripped)}</p>')
        i += 1

    flush_blockquote()
    flush_table()
    flush_code()
    return '\n'.join(out)


with open(MD_PATH, 'r', encoding='utf-8') as f:
    md = f.read()

body = md_to_html(md)

CSS = r"""
@page {
  size: A4;
  margin: 2.5cm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: "Crimson Pro", "EB Garamond", "Georgia", "Times New Roman", serif;
    font-size: 10pt;
    color: #666;
  }
}

html, body {
  direction: ltr;
  text-align: justify;
  font-family: "Crimson Pro", "EB Garamond", "Georgia", "Times New Roman", serif;
  font-size: 11.5pt;
  line-height: 1.6;
  color: #111;
  background: #fff;
  margin: 0;
  padding: 0;
  hyphens: auto;
  font-feature-settings: "kern" 1, "liga" 1, "onum" 1;
}

.ar {
  font-family: "Amiri Quran", "Amiri", "Noto Naskh Arabic", "Scheherazade New", "Scheherazade", "SF Arabic", "Geeza Pro", serif;
  direction: rtl;
  unicode-bidi: isolate;
  font-size: 1.08em;
  line-height: 1.8;
}

.cover {
  page-break-after: always;
  text-align: center;
  padding-top: 5cm;
}
.cover h1.cover-title {
  font-size: 32pt;
  line-height: 1.3;
  margin: 0 0 0.8cm 0;
  color: #1a3a5c;
  border: none;
  letter-spacing: 0.01em;
}
.cover .subtitle {
  font-size: 16pt;
  color: #555;
  margin-bottom: 1.5cm;
  font-style: italic;
  line-height: 1.4;
}
.cover .ornament {
  font-size: 22pt;
  color: #c4a484;
  margin: 1.4cm 0;
  letter-spacing: 0.5em;
}
.cover .banner {
  font-size: 12pt;
  color: #1a3a5c;
  margin-top: 0.6cm;
  font-variant: small-caps;
  letter-spacing: 0.15em;
}
.cover .meta {
  font-size: 11pt;
  color: #777;
  margin-top: 3cm;
  line-height: 1.7;
}

h1 {
  font-size: 20pt;
  color: #1a3a5c;
  border-bottom: 2px solid #c4a484;
  padding-bottom: 0.25em;
  margin-top: 1.2em;
  margin-bottom: 0.5em;
  page-break-after: avoid;
  page-break-before: auto;
}

h2 {
  font-size: 15.5pt;
  color: #1a3a5c;
  margin-top: 1.3em;
  margin-bottom: 0.5em;
  padding-bottom: 0.15em;
  border-bottom: 1px solid #d9c9b3;
  page-break-after: avoid;
}

h3 {
  font-size: 13pt;
  color: #2d4a6e;
  margin-top: 1em;
  margin-bottom: 0.35em;
  page-break-after: avoid;
}

h4 {
  font-size: 11.5pt;
  color: #2d4a6e;
  font-style: italic;
  margin-top: 0.9em;
  margin-bottom: 0.3em;
  page-break-after: avoid;
}

p {
  margin: 0.5em 0;
  text-indent: 0;
  orphans: 3;
  widows: 3;
}

strong {
  color: #b8442d;
  font-weight: 700;
}

em {
  font-style: italic;
  color: #1a3a5c;
}

a {
  color: #2d4a6e;
  text-decoration: none;
  border-bottom: 1px dotted #c4a484;
}

ul, ol {
  padding-left: 1.8em;
  padding-right: 0;
  margin: 0.5em 0;
}

li {
  margin: 0.2em 0;
}

hr {
  border: none;
  border-top: 1px solid #c4a484;
  margin: 1.5em auto;
  width: 40%;
  opacity: 0.6;
}

blockquote.quote-english {
  margin: 1em 0;
  padding: 0.6em 1.1em;
  background: #fbf8f1;
  border-left: 3px solid #c4a484;
  color: #333;
  font-style: italic;
  page-break-inside: avoid;
}
blockquote.quote-english p {
  margin: 0.35em 0;
}

blockquote.quote-arabic {
  margin: 1.1em 0;
  padding: 0.9em 1.1em;
  background: linear-gradient(to right, #fdfaf3, #f5ecd8);
  border-left: 4px solid #c4a484;
  border-radius: 6px;
  font-family: "Amiri Quran", "Amiri", "Noto Naskh Arabic", "Scheherazade New", serif;
  font-size: 14pt;
  line-height: 2.0;
  color: #1a3a5c;
  direction: rtl;
  text-align: right;
  page-break-inside: avoid;
}
blockquote.quote-arabic p {
  margin: 0.35em 0;
}

table {
  border-collapse: collapse;
  margin: 1em auto;
  width: 100%;
  font-size: 10.5pt;
  page-break-inside: avoid;
}

thead {
  background: #1a3a5c;
  color: #fdfaf3;
}

th, td {
  border: 1px solid #c4a484;
  padding: 0.45em 0.65em;
  text-align: left;
  vertical-align: top;
}

tbody tr:nth-child(even) {
  background: #fdfaf3;
}

code {
  background: #f5ecd8;
  padding: 0.08em 0.28em;
  border-radius: 3px;
  font-family: "Menlo", "SF Mono", "Consolas", monospace;
  font-size: 0.88em;
}

pre.code {
  background: #faf5e8;
  border: 1px solid #e4d6b8;
  border-left: 3px solid #c4a484;
  padding: 0.7em 1em;
  font-family: "Menlo", "SF Mono", "Consolas", monospace;
  font-size: 9.5pt;
  line-height: 1.45;
  overflow-x: auto;
  page-break-inside: avoid;
  white-space: pre-wrap;
}
pre.code code {
  background: transparent;
  padding: 0;
  font-size: inherit;
}

.footer-note {
  font-size: 10pt;
  color: #666;
  margin-top: 2em;
  padding-top: 0.8em;
  border-top: 1px dashed #c4a484;
  text-align: center;
}

h1, h2, h3, h4 { break-after: avoid; }
table, blockquote, pre.code { break-inside: avoid; }
"""

HTML = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title>{html.escape(COVER_TITLE)}</title>
<style>
{CSS}
</style>
</head>
<body>

<section class="cover">
  <div class="banner">The Quran Decipherment Project</div>
  <div class="ornament">&#10070; &#10022; &#10070;</div>
  <h1 class="cover-title">{html.escape(COVER_TITLE)}</h1>
  <div class="subtitle">{html.escape(COVER_SUBTITLE)}</div>
  <div class="ornament">&#10070; &#10022; &#10070;</div>
  <div class="meta">
    A research deliverable of the<br>
    Quran Decipherment Project<br>
    <br>
    {DATE_STR}
  </div>
</section>

{body}

</body>
</html>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'HTML written: {HTML_PATH}  ({len(HTML):,} chars)')

chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
cmd = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--hide-scrollbars',
    '--no-pdf-header-footer',
    f'--print-to-pdf={PDF_PATH}',
    f'file://{HTML_PATH}',
]
print('Rendering PDF via Chrome headless...')
proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
print(f'stdout: {proc.stdout[:300]}')
print(f'stderr: {proc.stderr[:300]}')
print(f'return code: {proc.returncode}')

if os.path.exists(PDF_PATH):
    sz = os.path.getsize(PDF_PATH)
    print(f'PDF written: {PDF_PATH}  ({sz:,} bytes, {sz/1024:.1f} KB)')
else:
    print('PDF FAILED TO BUILD')
    sys.exit(1)
