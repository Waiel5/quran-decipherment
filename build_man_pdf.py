#!/usr/bin/env python3
"""Build RTL Arabic PDF from 'al-Rajul fī Qalb al-Amr' essay via Chrome headless."""

import subprocess, os, textwrap, re, html

ROOT = '/Users/grey/Downloads/quran'
MD_PATH = f'{ROOT}/الرجل-في-قلب-الأمر.md'
HTML_PATH = f'{ROOT}/al-Rajul-fi-Qalb-al-Amr.html'
PDF_PATH = f'{ROOT}/al-Rajul-fi-Qalb-al-Amr.pdf'

# --- minimal Markdown → HTML conversion tuned for our file ---

def md_to_html(md):
    lines = md.split('\n')
    out = []
    in_table = False
    table_rows = []
    in_blockquote = False
    blockquote_buf = []

    def flush_blockquote():
        nonlocal in_blockquote, blockquote_buf
        if in_blockquote and blockquote_buf:
            out.append('<blockquote class="quran">')
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

    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        return s

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

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

        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            text = inline(m.group(2))
            out.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        if re.match(r'^---+\s*$', stripped):
            out.append('<hr>')
            i += 1
            continue

        if re.match(r'^\s*[-*]\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                item_text = re.sub(r'^\s*[-*]\s+', '', lines[i])
                items.append(inline(item_text))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{t}</li>' for t in items) + '</ul>')
            continue

        if re.match(r'^\s*\d+\.\s+', line):
            items = []
            while i < len(lines) and re.match(r'^\s*\d+\.\s+', lines[i]):
                item_text = re.sub(r'^\s*\d+\.\s+', '', lines[i])
                items.append(inline(item_text))
                i += 1
            out.append('<ol>' + ''.join(f'<li>{t}</li>' for t in items) + '</ol>')
            continue

        if stripped.startswith('*') and stripped.endswith('*') and len(stripped) > 2 and not stripped.startswith('**'):
            out.append(f'<p class="footer-note"><em>{inline(stripped[1:-1])}</em></p>')
            i += 1
            continue

        if stripped:
            out.append(f'<p>{inline(stripped)}</p>')
        i += 1

    flush_blockquote()
    flush_table()
    return '\n'.join(out)


with open(MD_PATH, 'r', encoding='utf-8') as f:
    md = f.read()

body = md_to_html(md)

CSS = r"""
@page {
  size: A4;
  margin: 2.2cm 2cm 2.4cm 2cm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: "Amiri", "Noto Naskh Arabic", "Geeza Pro", serif;
    font-size: 10pt;
    color: #666;
  }
}

html, body {
  direction: rtl;
  text-align: justify;
  font-family: "Amiri Quran", "Amiri", "Noto Naskh Arabic", "Scheherazade New", "Scheherazade", "SF Arabic", "Geeza Pro", serif;
  font-size: 13pt;
  line-height: 1.9;
  color: #111;
  background: #fff;
  margin: 0;
  padding: 0;
  hyphens: none;
  word-spacing: 0.04em;
  font-feature-settings: "kern" 1, "liga" 1, "calt" 1;
}

.cover {
  page-break-after: always;
  text-align: center;
  padding-top: 6cm;
}
.cover h1 {
  font-size: 32pt;
  line-height: 1.4;
  margin: 0 0 1cm 0;
  color: #1a3a5c;
  border: none;
}
.cover .subtitle {
  font-size: 18pt;
  color: #555;
  margin-bottom: 1.5cm;
}
.cover .ornament {
  font-size: 26pt;
  color: #c4a484;
  margin: 2cm 0;
  letter-spacing: 0.5em;
}
.cover .meta {
  font-size: 12pt;
  color: #777;
  margin-top: 3cm;
  line-height: 1.8;
}

h1 {
  font-size: 22pt;
  color: #1a3a5c;
  border-bottom: 2px solid #c4a484;
  padding-bottom: 0.25em;
  margin-top: 1.2em;
  margin-bottom: 0.5em;
  page-break-after: avoid;
}

h2 {
  font-size: 17pt;
  color: #1a3a5c;
  margin-top: 1.3em;
  margin-bottom: 0.5em;
  padding-bottom: 0.15em;
  border-bottom: 1px solid #d9c9b3;
  page-break-after: avoid;
}

h3 {
  font-size: 14pt;
  color: #2d4a6e;
  margin-top: 1em;
  margin-bottom: 0.35em;
  page-break-after: avoid;
}

h4 {
  font-size: 12pt;
  color: #2d4a6e;
  margin-top: 0.8em;
  page-break-after: avoid;
}

p {
  margin: 0.55em 0;
  text-indent: 0;
}

strong {
  color: #b8442d;
  font-weight: 700;
}

em {
  font-style: italic;
  color: #1a3a5c;
}

ul, ol {
  padding-right: 1.8em;
  padding-left: 0;
  margin: 0.6em 0;
}

li {
  margin: 0.25em 0;
}

hr {
  border: none;
  border-top: 1px solid #c4a484;
  margin: 1.5em auto;
  width: 40%;
  opacity: 0.6;
}

blockquote.quran {
  margin: 1.2em 0;
  padding: 1em 1.2em;
  background: linear-gradient(to left, #fdfaf3, #f5ecd8);
  border-right: 4px solid #c4a484;
  border-radius: 6px;
  font-family: "Amiri Quran", "Amiri", "Noto Naskh Arabic", "Scheherazade New", serif;
  font-size: 15.5pt;
  line-height: 2.2;
  color: #1a3a5c;
  page-break-inside: avoid;
}

blockquote.quran p {
  margin: 0.4em 0;
}

table {
  border-collapse: collapse;
  margin: 1em auto;
  width: 100%;
  font-size: 11.5pt;
  page-break-inside: avoid;
}

thead {
  background: #1a3a5c;
  color: #fdfaf3;
}

th, td {
  border: 1px solid #c4a484;
  padding: 0.5em 0.7em;
  text-align: right;
  vertical-align: middle;
}

tbody tr:nth-child(even) {
  background: #fdfaf3;
}

code {
  background: #f5ecd8;
  padding: 0.1em 0.3em;
  border-radius: 3px;
  font-family: "Menlo", "SF Mono", monospace;
  font-size: 0.9em;
  direction: ltr;
  unicode-bidi: embed;
}

.footer-note {
  font-size: 10.5pt;
  color: #666;
  margin-top: 2em;
  padding-top: 1em;
  border-top: 1px dashed #c4a484;
  text-align: center;
}

h1, h2, h3, h4 { break-after: avoid; }
p, li { orphans: 3; widows: 3; }
table, blockquote { break-inside: avoid; }
"""

HTML = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>الرجل في قلب الأمر</title>
<style>
{CSS}
</style>
</head>
<body>

<!-- Cover page -->
<section class="cover">
  <div class="ornament">﷽</div>
  <h1>الرجلُ في قلبِ الأمرِ كلِّه</h1>
  <div class="subtitle">مقالةٌ عن محمَّدٍ ﷺ في ضوءِ نتائجِ مشروعِ تفكيكِ القرآن</div>
  <div class="ornament">❖ ✦ ❖</div>
  <div class="meta">
    دراسةٌ تجمعُ بين السيرةِ النبويَّةِ والتحليلِ الحاسوبيّ<br>
    والبلاغةِ العربيَّةِ الكلاسيكيَّةِ وتاريخِ أواخرِ العصرِ القديم<br>
    <br>
    ١٤٤٧ هـ &mdash; ٢٠٢٦ م &mdash; مشروع التحليل الشامل للقرآن الكريم
  </div>
</section>

<!-- Main content -->
{body}

</body>
</html>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'HTML written: {HTML_PATH}  ({len(HTML):,} chars)')

# Render to PDF via Chrome headless
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
proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
print(f'stdout: {proc.stdout[:500]}')
print(f'stderr: {proc.stderr[:500]}')
print(f'return code: {proc.returncode}')

if os.path.exists(PDF_PATH):
    sz = os.path.getsize(PDF_PATH)
    print(f'PDF written: {PDF_PATH}  ({sz:,} bytes, {sz/1024:.1f} KB)')
else:
    print('PDF FAILED TO BUILD')
