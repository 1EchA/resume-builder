# Resume Builder

构建 ATS 优化的极简 HTML 简历，通过 Playwright 导出为 A4 PDF。

## 目录

```
resume-builder/
├── SKILL.md              # 技能主指令（AI 加载入口）
├── README.md             # 本文件
├── references/
│   ├── template.html     # 工作模板（CSS + HTML 合一）
│   └── css-system.md     # CSS 设计系统参考文档
└── scripts/
    └── generate_pdf.py   # Playwright PDF 导出脚本
```

## 核心设计

- **单色极简**：`#222 / #666 / #999 / #E5E5E5`，无彩色 accent
- **两栏布局**：Grid 默认（单页最优），溢出自动切 Float（第 2 页全宽）
- **A4 精确**：`width: 210mm`，Playwright 渲染，打印 CSS 覆盖响应式断点
- **字体**：Noto Serif SC（姓名）+ Noto Sans SC（正文）

## 使用方式

Skill 由 AI agent 自动加载。手动运行时：

```bash
# 1. 生成简历 HTML（基于 template.html）
# 2. 导出 PDF
pip install playwright pypdf Pillow
python -m playwright install chromium
python scripts/generate_pdf.py resume.html resume.pdf
```

## 版本历史

- v1.1 — Float 多页支持（grid → overflow detection → float switch）
- v1.0 — 初始版本：Grid 单页，Playwright PDF
