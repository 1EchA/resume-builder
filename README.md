<div align="center">
  <sub>1EchA / AGENT SKILL</sub>
  <h1>Resume Builder</h1>
  <p><strong>根据目标岗位整理经历，生成可编辑的 HTML 简历和 A4 PDF。</strong></p>
  <p>支持职位关键词提取、经历改写、单页压缩和多页排版。</p>
  <p>
    <a href="#30-秒开始"><strong>30 秒开始</strong></a>
    · <a href="examples/single-page.pdf">查看完整 PDF</a>
    · <a href="SKILL.md">阅读 Skill</a>
  </p>
</div>

![Resume Builder：根据目标岗位整理经历并生成 HTML 简历和 A4 PDF](assets/readme-hero-v2.png)

页面默认使用黑白排版，信息层级主要由内容顺序、字号和间距建立。

## 单页样例

下面这份简历使用虚构数据。可以重点看三处：经历是否说清了动作和结果，信息能不能快速扫读，以及导出后是否仍然稳稳落在一张 A4 里。

<p align="center">
  <a href="examples/single-page.pdf">
    <img src="examples/single-page-preview.png" alt="Resume Builder 生成的单页简历样例" width="620">
  </a>
</p>

<p align="center"><sub>点击图片查看完整 PDF · 样例数据均为虚构</sub></p>

## 做简历最容易卡住的三件事

### 材料很多，不知道该留什么

旧简历、JD、成绩单和项目资料通常各说各话。Resume Builder 会先对照目标岗位做取舍：无关的删掉，重要的提前，证据不足的先标出来。

### 经历写了不少，读起来还是像岗位职责

每条经历会按动作、方法、结果和规模重新整理；没有依据的数字不会补写。

### 屏幕上刚好，导出 PDF 就跑版

内容定下来以后，再处理两栏、字号和分页。单页尽量收紧，多页则让后续页面恢复全宽，最后用 Playwright 导出可打印的 A4 PDF。

## 30 秒开始

把仓库克隆到你的 Skill 目录，或让 Agent 直接读取 [`SKILL.md`](SKILL.md)：

```bash
git clone https://github.com/1EchA/resume-builder.git
```

然后直接描述目标，不需要先整理成标准格式：

```text
帮我做一份后端开发简历，目标岗位是字节跳动基础架构。
我有旧简历、成绩单和三个 GitHub 项目，请先帮我筛选内容。
把这份简历压到一页，并导出成 PDF。
```

只有在需要导出 PDF 时，才安装渲染依赖：

```bash
pip install playwright pypdf Pillow
python -m playwright install chromium
python scripts/generate_pdf.py resume.html resume.pdf
```

## 处理顺序

```text
目标岗位
   ↓
经历与关键词整理
   ↓
XYZ+S bullet 重写
   ↓
HTML / CSS 排版
   ↓
A4 PDF 渲染
   ↓
页数检测与布局迭代
```

### 内容整理

- 从 JD 中提取硬技能，并自然写进 Summary 与经历。
- 每段经历保留 2–3 个高信息密度 bullet，按工作逻辑排序。
- 从成绩单、项目和论文中筛选与目标岗位真正相关的内容。
- 重要数字使用受控强调，不靠彩色标签制造重点。

### A4 排版与 PDF 导出

- 精确的 `210mm` A4 容器与独立打印样式。
- `Noto Serif SC` 只用于姓名，`Noto Sans SC` 负责正文。
- 默认两栏 Grid；内容溢出时切换 Float，让第二页恢复全宽。
- 通过 Playwright 导出，避免浏览器打印产生页眉、页脚和布局偏移。

<details>
<summary><strong>设计系统</strong></summary>

| Token | 值 | 用途 |
|---|---|---|
| Primary | `#222` | 正文与核心信息 |
| Secondary | `#666` | 副标题与机构名 |
| Muted | `#999` | 日期与元数据 |
| Border | `#E5E5E5` | 分隔线 |
| Display | `Noto Serif SC` | 姓名 |
| Body | `Noto Sans SC` | 其余内容 |

这里使用纯单色，以保证打印效果稳定，并减少不必要的视觉干扰。

</details>

<details>
<summary><strong>目录与实现细节</strong></summary>

```text
resume-builder/
├── SKILL.md
├── examples/
│   ├── single-page.pdf
│   └── single-page-preview.png
├── references/
│   ├── template.html
│   └── css-system.md
└── scripts/
    └── generate_pdf.py
```

- [`references/template.html`](references/template.html)：可直接工作的 HTML/CSS 起点。
- [`references/css-system.md`](references/css-system.md)：Grid、Float 与打印样式说明。
- [`scripts/generate_pdf.py`](scripts/generate_pdf.py)：Playwright HTML → A4 PDF。

</details>

## 兼容方式

适用于能够加载 Markdown Skill 指令的 Agent 环境，例如 Claude Code、Codex 与 Cursor。具体安装目录由你的 Agent 环境决定；仓库本身不绑定某个平台 API。

## License

MIT
