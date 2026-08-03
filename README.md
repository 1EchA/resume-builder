<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-222?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-222?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-222?style=flat-square" alt="platform">
  <br>
  <sub><a href="README_ZH.md">中文版</a></sub>
</p>

# 📄 Resume Builder

> Build ATS-optimized, minimalist HTML resumes with pixel-perfect A4 PDF export.
> **Archival Precision** — monochrome, every element earns its place.

An Agent Skill for Claude Code / Codex / Cursor that generates professional single-page or multi-page resumes from raw experience data. Designed for ATS scanners, human recruiters, and monochrome printers alike.

## ✨ Features

- 🎯 **ATS-optimized**: XYZ+S bullet formula, keyword weaving, structured layout
- 🎨 **Minimalist design**: Pure monochrome (`#222` / `#666` / `#999`), Noto Serif SC + Noto Sans SC
- 📐 **Precise A4**: `width: 210mm` container, Playwright headless browser rendering
- 📄 **Single or multi-page**: Grid layout by default; auto-switches to Float when content overflows

## 🚀 Quick Start

```bash
# Install as a skill (Claude Code / Codex compatible)
# <skills-path>/resume-builder/

# Dependencies for PDF export
pip install playwright pypdf Pillow
python -m playwright install chromium

# Generate PDF from HTML
python scripts/generate_pdf.py resume.html resume.pdf
```

## 📁 Structure

```
resume-builder/
├── SKILL.md              # Agent instructions (7-phase workflow)
├── README.md
├── examples/
│   ├── single-page.pdf   # Sample output (Grid layout)
│   └── single-page-preview.png
├── references/
│   ├── template.html     # Working template (CSS + HTML)
│   └── css-system.md     # Design system reference
└── scripts/
    └── generate_pdf.py   # Playwright HTML → A4 PDF
```

## 🎨 Design System

| Token | Color | Role |
|-------|-------|------|
| Text | `#222` | Primary content |
| Secondary | `#666` | Subtitles, org names |
| Muted | `#999` | Dates, metadata |
| Border | `#E5E5E5` | Dividers |
| Display font | `Noto Serif SC` | Name only |
| Body font | `Noto Sans SC` | Everything else |

> **Why monochrome?** Color adds noise for ATS parsers. Monochrome prints identically on any printer and signals deliberate restraint — not default AI template output.

## 📐 Layout

### Single Page (Grid — default)
```
┌──────────────────────────┐
│ Photo · Name · Contact   │
├──────────────────┬───────┤
│ Experiences      │ Edu   │
│                  │ Skills│
└──────────────────┴───────┘
```

### Multi Page (Float — auto-switch when overflow detected)

Page 1: Two-column (sidebar on right). Page 2+: Single-column full-width (sidebar ends on page 1).

## 📸 Sample

<p align="center">
  <a href="examples/single-page.pdf"><strong>📥 Download PDF</strong></a>
</p>

<p align="center">
  <img src="examples/single-page-preview.png" alt="Resume sample" width="600">
</p>

<details open>
<summary><strong>📋 What this demonstrates</strong></summary>

| Section | Content |
|---------|---------|
| **Header** | AI-generated portrait + Serif name + contact row + professional summary |
| **Left column** | 5 internship/project entries, XYZ+S bullet formula, metric highlighting |
| **Right column** | Education, core courses, tech stack (3 categorized groups) |
| **Typography** | Pure monochrome `#222/#666/#999`, `tabular-nums`, `text-wrap: balance` |
| **Print** | `width: 210mm` precise A4, Playwright headless browser rendering |

</details>

> Fictional data: "陈思远" · Huazhong University · ByteDance/Alibaba internships · DTask/LogStream/RaftKV

## 💬 Usage

Once installed, the skill activates on any resume-related prompt:

```
"Build a data engineer resume targeting FAANG"
"Update my internship experience with the latest project"
"帮我做一份前端开发的简历"
"Export my resume to PDF with Playwright"
```

The agent follows a 7-phase workflow: Content Strategy → Design Self-Audit → Build HTML → CSS → Print CSS → PDF Export → Iterate.

## 🔧 Overflow Detection

When content exceeds one page, the skill automatically:

1. Detects page count via `pypdf.PdfReader`
2. Switches CSS from Grid → Float (`margin-right` keeps columns clean)
3. Reorders DOM (sidebar before main-col)
4. Updates print CSS to remove grid overrides
5. Regenerates PDF

## 📄 License

MIT
