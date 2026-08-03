<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-222?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-222?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-222?style=flat-square" alt="platform">
  <br>
  <sub><a href="#中文">中文</a> · <a href="#english">English</a></sub>
</p>

---

<h1 id="中文">📄 Resume Builder · 简历生成器</h1>

> 构建 ATS 优化的极简 HTML 简历，通过 Playwright 导出像素级 A4 PDF。
> **Archival Precision** — 单色极简，每个元素都有存在的理由。

适用于 Claude Code / Codex / Cursor 的 Agent Skill，从原始经历数据生成专业单页或多页简历。专为 ATS 扫描器、HR 审阅和单色打印机设计。

## ✨ 功能

- 🎯 **ATS 优化**：XYZ+S bullet 写作公式、关键词嵌入、结构化布局
- 🎨 **极简设计**：纯单色（`#222` / `#666` / `#999`），Noto Serif SC + Noto Sans SC
- 📐 **精确 A4**：`width: 210mm` 容器，Playwright 无头浏览器渲染
- 📄 **单页 / 多页**：默认 Grid 布局；内容溢出时自动切换 Float 模式

## 🚀 快速开始

```bash
# 安装为 Skill（Claude Code / Codex 兼容）
# <skills-path>/resume-builder/

# PDF 导出依赖
pip install playwright pypdf Pillow
python -m playwright install chromium

# 从 HTML 生成 PDF
python scripts/generate_pdf.py resume.html resume.pdf
```

## 📁 目录结构

```
resume-builder/
├── SKILL.md              # Agent 指令（7 阶段工作流）
├── README.md
├── examples/             # 样例输出
│   ├── single-page.pdf   # 单页版（Grid 布局）
│   └── multi-page.pdf    # 多页版（Float 切换）
├── references/
│   ├── template.html     # 工作模板（CSS + HTML）
│   └── css-system.md     # 设计系统参考
└── scripts/
    └── generate_pdf.py   # Playwright PDF 导出
```

## 🎨 设计系统

| Token | 色值 | 用途 |
|-------|------|------|
| 正文 | `#222` | 主要内容 |
| 次级 | `#666` | 副标题、机构名 |
| 弱化 | `#999` | 日期、元数据 |
| 分割线 | `#E5E5E5` | 边框 |
| 标题字体 | `Noto Serif SC` | 仅姓名 |
| 正文字体 | `Noto Sans SC` | 其余全部 |

> **为什么纯单色？** 颜色对 ATS 解析器是噪声；单色在任何打印机上输出一致；避免 AI 默认模板的套路配色。

## 📐 布局模式

### 单页（Grid — 默认）
```
┌──────────────────────────┐
│ 照片 · 姓名 · 联系方式    │
├──────────────────┬───────┤
│ 经历              │ 教育  │
│                  │ 技能  │
└──────────────────┴───────┘
```

## 📸 样例预览

[![preview](examples/single-page-preview.png)](examples/single-page.pdf)

> 虚构人物"陈思远" · 后端开发方向 · 5 段经历 · Grid 两栏布局 · [📥 下载 PDF](examples/single-page.pdf)

## 💬 使用示例

Skill 安装后，任何简历相关的对话都会自动触发：

```
"帮我做一份后端开发的简历，目标公司字节跳动"
"更新我的实习经历，加上最近的项目"
"Export my resume to PDF"
```

Agent 遵循 7 阶段工作流：内容策略 → 设计自查 → 构建 HTML → CSS → 打印 CSS → PDF 导出 → 迭代。

## 🔧 溢出检测

当内容超过一页时，Skill 自动执行：

1. `pypdf.PdfReader` 检测页数
2. CSS 从 Grid 切换为 Float（`margin-right` 保持栏位整洁）
3. DOM 重新排序（sidebar 移到 main-col 之前）
4. 打印 CSS 移除 grid 覆盖
5. 重新生成 PDF

---

<p align="center"><sub><a href="#">↑ Top</a></sub></p>

---

<h1 id="english">📄 Resume Builder</h1>

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
├── examples/             # Sample outputs
│   ├── single-page.pdf   # Single-page (Grid layout)
│   └── single-page.pdf   # Grid layout preview
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

## 📐 Layout Modes

### Single Page (Grid — default)
```
┌──────────────────────────┐
│ Photo · Name · Contact   │
├──────────────────┬───────┤
│ Experiences      │ Edu   │
│                  │ Skills│
└──────────────────┴───────┘
```

## 📸 Sample Preview

[![preview](examples/single-page-preview.png)](examples/single-page.pdf)

> Fictional "陈思远" · Backend Engineer · 5 entries · Grid two-column · [📥 Download PDF](examples/single-page.pdf)

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
3. Reorders DOM (sidebar before main-col for float)
4. Updates print CSS to remove grid overrides
5. Regenerates PDF

## 📄 License

MIT
