<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-222?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-222?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-222?style=flat-square" alt="platform">
</p>

# 📄 Resume Builder

> Build ATS-optimized, minimalist HTML resumes with pixel-perfect A4 PDF export.
> **Archival Precision** — monochrome, every element earns its place.

A Claude Code / Codex / Cursor skill that generates professional single-page or multi-page resumes from your raw experience data. Designed for ATS scanners, human recruiters, and monochrome printers alike.

## ✨ What It Does

- 🎯 **ATS-optimized**: XYZ+S bullet formula, keyword weaving, structured layout
- 🎨 **Minimalist design**: Pure monochrome (`#222` / `#666` / `#999`), Noto Serif SC + Noto Sans SC
- 📐 **Precise A4**: `width: 210mm` container, Playwright headless browser rendering
- 📄 **Single or multi-page**: Grid layout by default; auto-switches to float when content overflows to page 2

## 🚀 Quick Start

```bash
# Install as a skill (Claude Code / Codex compatible)
# <path-to-skills>/resume-builder/

# Dependencies (for PDF export)
pip install playwright pypdf Pillow
python -m playwright install chromium

# Generate a PDF from any HTML resume
python scripts/generate_pdf.py resume.html resume.pdf
```

## 📁 Skill Structure

```
resume-builder/
├── SKILL.md              # Agent instructions (7-phase workflow)
├── README.md
├── references/
│   ├── template.html     # Working template (CSS + HTML, 450 lines)
│   └── css-system.md     # Design system reference (grid/float/print)
└── scripts/
    └── generate_pdf.py   # Playwright HTML → A4 PDF converter
```

## 🎨 Design System

| Token | Value | Role |
|-------|-------|------|
| Text | `#222` | Primary content |
| Secondary | `#666` | Subtitles, org names |
| Muted | `#999` | Dates, metadata |
| Border | `#E5E5E5` | Dividers |
| Display font | `Noto Serif SC` | Name only |
| Body font | `Noto Sans SC` | Everything else |

> **Why monochrome?** Color adds noise for ATS parsers. Monochrome prints identically on any printer and signals deliberate restraint — not default AI template output.

## 📐 Layout Modes

### Single Page (Grid — default)
```
┌──────────────────────────┐
│ Photo · Name · Contact   │
├──────────────────┬───────┤
│ Experiences      │ Edu   │
│                  │ Skills│
│                  │       │
└──────────────────┴───────┘
```

### Multi Page (Float — auto-switch)
```
Page 1                      Page 2
┌──────────────────┬───────┐ ┌──────────────────────┐
│ Experiences      │ Side  │ │ Experiences (全宽)    │
│                  │ bar   │ │                      │
└──────────────────┴───────┘ └──────────────────────┘
```

## 💬 Usage Examples

Once installed, the skill activates on any resume-related prompt:

```
"帮我做一份后端开发的简历，目标公司字节跳动"
"Build a data engineer resume targeting FAANG"
"更新我的实习经历，加上最近的项目"
"Export my resume to PDF with Playwright"
```

The agent follows a 7-phase workflow: Content Strategy → Design Self-Audit → Build HTML → CSS → Print CSS → PDF Export → Iterate.

## 🔧 Overflow Detection

When content exceeds one page, the skill automatically:

1. Detects page count via `pypdf.PdfReader`
2. Switches CSS from Grid → Float (`margin-right` on main-col keeps columns clean)
3. Reorders DOM (sidebar before main-col for float)
4. Updates print CSS to remove grid overrides
5. Regenerates PDF

## 📄 License

MIT
