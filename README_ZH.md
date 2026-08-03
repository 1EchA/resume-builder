<p align="center">
  <img src="https://img.shields.io/badge/version-1.1-222?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-222?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/platform-Claude%20Code%20%7C%20Codex%20%7C%20Cursor-222?style=flat-square" alt="platform">
  <br>
  <sub><a href="README.md">English</a></sub>
</p>

# 📄 Resume Builder · 简历生成器

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
├── examples/
│   ├── single-page.pdf   # 样例输出（Grid 布局）
│   └── single-page-preview.png
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

### 多页（Float — 溢出检测后自动切换）

第 1 页：两栏（右侧栏位）。第 2 页起：单栏全宽（侧栏在第 1 页结束）。

## 📸 样例展示

<p align="center">
  <a href="examples/single-page.pdf"><strong>📥 下载完整 PDF</strong></a>
</p>

<p align="center">
  <img src="examples/single-page-preview.png" alt="简历样例" width="600">
</p>

<details open>
<summary><strong>📋 这份样例展示了什么？</strong></summary>

| 区域 | 展示内容 |
|------|----------|
| **头部** | AI 生成形象照 + Serif 姓名 + 联系方式 + 个人综述 |
| **左栏** | 5 段实习/项目经历，XYZ+S 子弹公式，数字指标高亮 |
| **右栏** | 教育背景、核心课程、技术栈三组分类 |
| **排版** | 纯单色 `#222/#666/#999`，`tabular-nums` 等宽数字，`text-wrap: balance` 标题 |
| **打印** | `width: 210mm` 精确 A4 容器，Playwright 无头浏览器渲染 |

</details>

> 样例内容为虚构数据："陈思远" · 华中科技大学软件工程 · 字节跳动/阿里云实习 · DTask/LogStream/RaftKV

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

## 📄 License

MIT
