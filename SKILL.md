---
name: resume-builder
description: Build ATS-optimized, minimalist HTML resumes with professional print-ready PDF output. Use this skill when the user asks to create a resume, update their CV, build a professional resume, optimize a resume for ATS, convert resume to PDF, or design a resume layout. Also use when users mention 简历, CV, 求职, job application, or want to tailor their resume for a specific position. Even if the user just says "help me apply for a job" or "I need to update my experience", this skill likely applies. Triggers on any resume-related conversation including reviewing, critiquing, formatting, or exporting existing resumes.
---

# Resume Builder

Build high-end, ATS-optimized, single-page HTML resumes and export them as pixel-perfect PDFs via Playwright. The design philosophy is **Archival Precision** — minimalist, monochrome, every element earns its place.

## Quick Reference

| Resource | Path | When to read |
|----------|------|-------------|
| Full CSS system | `references/css-system.md` | When building CSS from scratch or debugging print layout |
| Working template | `references/template.html` | When creating a new resume as starting point |
| PDF generator | `scripts/generate_pdf.py` | When exporting to PDF |

## Design Philosophy

Every design choice in this template is deliberate, not default. The **Archival Precision** philosophy rests on three principles:

**Monochrome as a feature, not a limitation.** `#222` / `#666` / `#999` / `#E5E5E5` — no accent colors. Why? (1) Resumes are read by humans on screen AND by ATS parsers; color adds noise for both. (2) Monochrome prints identically on any printer — laser, inkjet, or industrial. (3) A splash of color is the default answer for every "modern resume" template — avoiding it signals intentionality.

**Typography as personality.** The name in `Noto Serif SC` carries gravitas without shouting. Body text in `Noto Sans SC` stays crisp at small sizes. This one pairing is the only place personality is expressed — everything else is structure.

**Spend boldness in one place.** The serif name is the signature element. Everything around it — spacing, rules, bullet markers — stays quiet and disciplined. Before finalizing, ask: "Would removing this make the resume feel incomplete?" If the answer is no, cut it.

### Avoiding Template Defaults

AI-generated resume designs cluster around three looks that must be **actively avoided**:
1. Warm cream background + serif display + terracotta accent → reads as "AI-made"
2. Near-black background + acid-green accent → unprintable and gimmicky for a resume
3. Dense newspaper-column layout → ATS-unfriendly

When adapting for a new target role, always check: "Is this change a considered choice for THIS resume, or would I make the same change for any resume?"

## Workflow Overview

```
1. Content Strategy  →  Gather materials, extract ATS keywords, write bullets
2. Design Self-Audit →  Verify design choices before writing code (see Phase 2)
3. Build HTML         →  Two-column grid, header with photo, experience blocks
4. Style with CSS    →  Monochrome palette, Noto fonts, clean spacing
5. Print CSS         →  Override responsive breakpoints for A4 rendering
6. Generate PDF      →  Playwright headless browser, tune font size to fill page
7. Iterate           →  Content audit, spacing adjustments, re-export
```

## Phase 1: Content Strategy

### Gather Information

Ask the user for:
1. **Target role & company** — drives keyword selection and course filtering
2. **Existing resume** — PDF or text, extract with `pymupdf` (`fitz`) if PDF
3. **Course transcript** — Excel file, read with `openpyxl`, filter for role-relevant courses
4. **GitHub repos** — read READMEs to extract project details and metrics
5. **Papers/publications** — title, venue, author position

### ATS Keywords

The Professional Summary is prime ATS real estate. Extract 5–8 hard skills from the job description and weave them in naturally. The summary should read like a human wrote it while passing keyword scanners.

### Writing Experience Bullets

Use the **XYZ+S formula** — this creates bullets that are both scannable and substantive:

- **X** = What you did (action verb + task)
- **Y** = How you did it (specific tools/methods)
- **Z** = Quantified result
- **S** = Scale/scope

Format each bullet with a bold label prefix:
```html
<li><strong>数据清洗与治理</strong>：基于 PostgreSQL 与 DBeaver 编写正则清洗脚本，显著降低脏数据率</li>
```

Use `<span class="metric">` for key numbers to give them visual weight:
```html
<span class="metric">160 万+</span>
```

Keep 2–3 bullets per experience. Order by logical workflow (Input → Process → Output), not importance.

## Phase 2: Design Self-Audit

> [!IMPORTANT]
> Before writing any HTML, pause for a 60-second design audit. Skipping this is how templates become generic.

1. **Color**: Am I staying monochrome? If tempted to add an accent color, justify it in one sentence. If you can't, don't add it.
2. **Typography**: Am I using exactly `Noto Sans SC` + `Noto Serif SC`? No substitutions unless the user explicitly requests a different font.
3. **Structure**: Is every element earning its place? Is anything decorative rather than informative?
4. **Signature**: What's the ONE memorable element in this design? If you can't name it, the layout is too generic — go back and make one deliberate choice.

Only after passing this audit, proceed to Phase 3.

## Phase 3: Build HTML

Read `references/template.html` for the full working template. Key structural decisions:

**Two-column layout**: Default CSS Grid — left column holds experiences, right sidebar holds education/skills. See `references/css-system.md` for both grid and float layout specs.

**Multi-page fallback**: If content overflows (detected in Phase 6), switch to float layout — sidebar gets `float: right` + `margin-right: 260px` on main-col, and sidebar moves before main-col in DOM. This keeps clean column boundaries on page 1 while page 2+ renders full-width.

**Header**: Name in serif font for gravitas, subtitle with role keywords, contact row with clickable `mailto:` and `https://` links.

**Project links**: Wrap titles in invisible-style `<a>` tags so they're clickable in PDF but don't look like hyperlinks:
```html
<a href="https://github.com/user/repo" target="_blank"
   style="color:inherit;text-decoration:none;">Project Title</a>
```

### Sidebar Content Decisions

**Core courses**: Only list courses directly relevant to the target role. Read the transcript Excel with `openpyxl`, filter by relevance (not by grade). For data roles: Python, Data Structures, Statistics, Database, ML. Generic CS courses dilute the message.

**Tech stack**: Group into 2–3 categories matching the role. The categories should tell a story about the candidate's capabilities.

## Phase 4: CSS

Read `references/css-system.md` for the complete CSS reference. Critical reminders:

- `display: block` on `.skill-items` — without this, sidebar items render inline with section titles
- All sizing, spacing, and print overrides are pre-configured in the template — follow `template.html` exactly

## Phase 5: Print CSS

> [!CAUTION]
> A4 page width at 96dpi is ~700px, which falls BELOW the `720px` responsive breakpoint. Every responsive style must be overridden with `!important` in `@media print` — see `references/css-system.md` for the full print CSS.

### Font Size Tuning

The print `font-size` controls page density. Adjust by `0.2px` increments:
- **Too much blank at bottom** → increase font size
- **Overflows to page 2** → decrease font size
- Typical range: `11px` (dense) to `13px` (spacious)

## Phase 6: PDF Generation

**Never rely on browser Ctrl+P** — it breaks layouts and adds headers/footers. Use the bundled Playwright script:

```bash
pip install playwright && python -m playwright install chromium
python scripts/generate_pdf.py resume.html resume.pdf
```

Or inline:
```python
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///' + os.path.abspath('resume.html').replace('\\', '/'))
    page.wait_for_timeout(3000)  # Wait for Google Fonts to load
    page.pdf(path='resume.pdf', format='A4',
             margin={'top': '10mm', 'right': '8mm', 'bottom': '10mm', 'left': '8mm'},
             print_background=True)
    browser.close()
```

If `PermissionError`, the user has the PDF open — write to a different filename.

### Overflow Detection → Float Switch

After the first PDF, check if content overflowed to multiple pages. If so, switch from grid to float layout and regenerate:

```python
from pypdf import PdfReader
reader = PdfReader('resume.pdf')
if len(reader.pages) > 1:
    # 1. Screen CSS: Replace grid with float
    #    .body { display: grid; grid-template-columns: 1fr 220px; gap: 40px; }
    #    → .body { }
    #      .sidebar { float: right; width: 220px; margin-left: 40px; display: flex; flex-direction: column; gap: 28px; }
    #      .main-col { }
    #
    # 2. Print CSS: Replace grid !important overrides with float
    #    .body { display: grid !important; grid-template-columns: ... }
    #    → /* Float mode — sidebar right, main wraps naturally */
    #      .sidebar { float: right !important; width: 200px !important; margin-left: 24px !important; gap: 16px !important; }
    #
    # 3. HTML: Move <aside class="sidebar"> BEFORE <section class="main-col"> in DOM
    #    This ensures float takes effect: sidebar right on page 1, releases on page 2+
    #
    # 4. Regenerate PDF
```

**Why this works**: With grid, every page maintains the two-column layout — page 2 has an empty 200px gap on the right. Switching to float makes page 2+ render full-width because the sidebar content ends on page 1, and the float releases naturally.

**When to skip the switch**: If the user explicitly wants a single-page resume, try adjusting font size (`11px`–`13px` range) to fit everything on one page instead.

## Phase 7: Iterate

After the first PDF, review with the user:
1. **Content accuracy** — verify metrics, project names, dates against original sources (GitHub, papers)
2. **Layout balance** — sidebar should be shorter than main column (this is normal)
3. **Print fit** — tune font size for optimal page fill
4. **Links** — confirm email `mailto:`, GitHub, and project links are clickable in PDF

## Common Pitfalls

| Problem | Root Cause | Fix |
|---------|-----------|-----|
| Sidebar goes horizontal in print | A4 width < 720px breakpoint | Override with `!important` in `@media print` |
| Course items inline with title | `<span>` is inline by default | Add `display: block` to `.skill-items` |
| PDF file locked | User has it open | Write to new filename |
| Too much blank at bottom | Print font-size too small | Increase by 0.2px increments |
| Photo shifts down in print | Responsive margin-top | `.photo { margin-top: 0 !important; }` |
| Content on page 2 | Print font-size too large | Decrease by 0.2px or remove spacing |
