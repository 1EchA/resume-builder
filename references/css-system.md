# CSS Reference

Complete CSS design system for the resume template.

## CSS Variables

```css
:root {
    --white: #FFFFFF;
    --bg: #FAFAFA;
    --text: #222222;
    --text-light: #666666;
    --text-muted: #999999;
    --border: #E5E5E5;
    --accent: #333333;
    --font-cn: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    --font-serif: 'Noto Serif SC', 'Songti SC', serif;
}
```

## Base Styles

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 14.5px; }
body {
    font-family: var(--font-cn);
    background: var(--bg);
    color: var(--text);
    padding: 40px 20px;
    -webkit-font-smoothing: antialiased;
}
```

## Resume Container

```css
.resume {
    width: 210mm;             /* Precise A4 width */
    max-width: 100%;          /* Shrink on narrow screens */
    min-height: 297mm;        /* Full A4 height for visual reference */
    margin: 0 auto;
    background: var(--white);
    padding: 48px 56px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
```

## Header

```css
.header {
    display: flex;
    gap: 28px;
    align-items: flex-start;
    padding-bottom: 28px;
    margin-bottom: 28px;
    border-bottom: 2px solid var(--text);
}

.photo {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    overflow: hidden;
    flex-shrink: 0;
}

.photo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
    display: block;
}

.header-info { flex: 1; }

.header-info h1 {
    font-family: var(--font-serif);
    font-size: 2rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}

.header-info .subtitle {
    font-size: 0.9rem;
    color: var(--text-light);
    margin-bottom: 16px;
    letter-spacing: 0.02em;
}

.contact-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 24px;
    font-size: 0.85rem;
    color: var(--text-light);
}

.contact-row a {
    color: var(--text-light);
    text-decoration: none;
    transition: color 0.2s;
}

.contact-row a:hover { color: var(--text); }
.contact-row span.sep { color: var(--border); }
```

## Two-Column Layout

### Grid Mode (Default — Single Page)

CSS Grid provides the cleanest two-column rendering. Use this by default.

```css
.body {
    display: grid;
    grid-template-columns: 1fr 220px;
    gap: 40px;
}

.sidebar {
    display: flex;
    flex-direction: column;
    gap: 28px;
}
```

HTML order (sidebar after main-col):
```html
<div class="body">
    <section class="main-col">...</section>
    <aside class="sidebar">...</aside>
</div>
```

### Float Mode (Multi-Page Switch)

When content overflows to page 2+ (detected via `pypdf` page count), switch to float. The sidebar floats right on page 1, and page 2+ renders full-width because the float releases naturally after sidebar content ends.

```css
.body { }
.sidebar {
    float: right;
    width: 220px;
    margin-left: 40px;
    display: flex;
    flex-direction: column;
    gap: 28px;
}
.main-col { }
```

HTML order (sidebar BEFORE main-col):
```html
<div class="body">
    <aside class="sidebar">...</aside>  <!-- MUST be first for float to work -->
    <section class="main-col">...</section>
</div>
```

> [!IMPORTANT]
> The float switch requires TWO changes: CSS replacement + DOM reordering.
> See SKILL.md Phase 6 "Overflow Detection → Float Switch" for the complete workflow.

## Section Titles

```css
.section-title {
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text);
    margin-bottom: 18px;
    padding-bottom: 8px;
    border-bottom: 2px solid var(--text);
    display: inline-block;
    text-wrap: balance;       /* Prevent orphan words on last line */
}
```

## Experience Items (Left Column)

```css
.exp-item { margin-bottom: 24px; }
.exp-item:last-child { margin-bottom: 0; }

.exp-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2px;
    gap: 12px;
}

.exp-title { font-size: 1rem; font-weight: 600; color: var(--text); line-height: 1.4; }
.exp-date { font-size: 0.78rem; color: var(--text-muted); white-space: nowrap; flex-shrink: 0; font-variant-numeric: tabular-nums; }
.exp-org { font-size: 0.85rem; color: var(--text-light); margin-bottom: 6px; }

.exp-bullets { list-style: none; margin-top: 6px; }
.exp-bullets li {
    position: relative;
    padding-left: 14px;
    font-size: 0.88rem;
    color: var(--text);
    line-height: 1.65;
    margin-bottom: 4px;
}
.exp-bullets li::before {
    content: '·';
    position: absolute;
    left: 2px;
    top: 0;
    color: var(--text-muted);
    font-weight: 700;
}
.exp-bullets strong { font-weight: 600; }
.metric { font-weight: 600; color: var(--text); font-variant-numeric: tabular-nums; }
```

## Sidebar (Right Column)

```css
.edu-school { font-size: 0.92rem; font-weight: 600; display: block; line-height: 1.4; }
.edu-major { font-size: 0.82rem; color: var(--text-light); display: block; }
.edu-period { font-size: 0.78rem; color: var(--text-muted); display: block; margin-top: 2px; font-variant-numeric: tabular-nums; }

.skill-group { margin-bottom: 10px; }
.skill-group:last-child { margin-bottom: 0; }
.skill-label { font-size: 0.82rem; font-weight: 600; color: var(--text); display: block; margin-bottom: 1px; }
.skill-items { display: block; font-size: 0.8rem; color: var(--text-light); line-height: 1.55; }
```

## Responsive

```css
@media (max-width: 720px) {
    .resume { padding: 32px 24px; }
    .header { flex-direction: column; align-items: center; text-align: center; }
    .contact-row { justify-content: center; }
    .body { grid-template-columns: 1fr; gap: 28px; }
    .sidebar { order: -1; flex-direction: row; flex-wrap: wrap; gap: 20px; }
    .sidebar > div { flex: 1; min-width: 140px; }
}
```

## Print CSS

> [!CAUTION]
> The A4 page width (~700px at 96dpi) falls below the 720px responsive breakpoint.
> Every responsive override MUST be countered with `!important` in `@media print`.

### Single-Page Mode (Default)

```css
@media print {
    @page { size: A4; margin: 9mm 8mm; }
    html { font-size: 12.8px; } /* TUNE THIS */
    body { background: white !important; padding: 0 !important; margin: 0 !important; }
    .resume { box-shadow: none !important; padding: 24px 28px !important; width: 210mm !important; max-width: 100% !important; min-height: auto !important; }
    /* Override responsive breakpoint (720px) */
    .header { flex-direction: row !important; align-items: flex-start !important; text-align: left !important; }
    .contact-row { justify-content: flex-start !important; }
    .photo { margin-top: 0 !important; }
    .body { display: grid !important; grid-template-columns: 1fr 200px !important; gap: 24px !important; }
    .sidebar { order: 0 !important; flex-direction: column !important; flex-wrap: nowrap !important; }
    /* Orphan/widow control */
    body { orphans: 3; widows: 3; }
    .section-title { break-after: avoid; page-break-after: avoid; }
    .exp-head { break-after: avoid; }
    .exp-item { margin-bottom: 12px; break-inside: avoid; page-break-inside: avoid; }
}
```

### Font Size Tuning Guide

The print `html { font-size }` controls how much content fills the A4 page:

| Symptom | Fix |
|---------|-----|
| Large blank space at bottom | Increase by 0.2px |
| Content overflows to page 2 | Decrease by 0.2px |
| Content nearly fills page | You're done |

Typical range: `11px` (very dense) to `13px` (spacious). Start at `12px` and adjust.
