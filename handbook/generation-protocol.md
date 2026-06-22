# 笔记图生成协议

## 生成前先做小规划

每页生成前，先在内部确定：

```text
标题：
内容类型：定义 / 流程 / 对比 / 分类 / 公式 / 案例 / 易错点
版式：
核心要点：3-5 条
高亮词：2-4 个
图解：
复习提醒：
```

不要把这段规划全部输出给用户，除非用户要求看方案。


## v1.2.2 强制比例与超时规则

### 强制 3:4

每次 final prompt 第一行必须包含：

```text
STRICT 3:4 VERTICAL IMAGE ONLY. Portrait canvas, 1536x2048 composition. Do not use 2:3, A4, square, landscape, or any other ratio.
```

禁止使用：

```text
A4-style
2:3
3:4 or 2:3
portrait note page without exact ratio
```

如果生成结果不是 3:4，直接重试，不进入内容返修。

### 单页 prompt 预算

最终进入图片模型的 prompt 只写本页内容，不写全文。

每页最多：

- 标题 1 个
- 核心判断 1 句
- 短要点 3 条，必要时最多 4 条
- 高亮词 2 个，必要时最多 3 个
- 图解 1 个
- 复习提醒 1 句

中文总量默认 60-90 个可见汉字。
如果上一页或当前页生成超过 180 秒，下一次重试必须降到约 60 个可见汉字。


### 逐页反馈与单次调用边界

多页任务必须逐页报告进度：

```text
第 1/5 页已完成，准备生成第 2 页。
```

每次工具调用只生成一页。禁止在同一个脚本或同一次调用中循环生成多页。

### 降载重试

单页超过 180 秒后，只允许降载重试一次。降载版只保留标题、一个简单图解、3 条短句和一句复习提醒。

### 文字错误

出现错字、重复、乱码时，不要叠加更多纠错要求。先减少文字量，再重生；必要时改为无文字底图 + 后期叠字建议。

### 多页逐张生成

多页任务必须先得到 `page-outline` 和 `page-prompts`，然后逐页单独生成。

禁止一次性批量生成多页。
禁止在第 2 页 prompt 中携带第 1 页完整内容。
禁止把所有页的中文正文都放进一次生图调用。

## 单页生成提示词模板

生成图像时使用下面结构。根据内容替换变量。

```text
Create one visual study notes page with STRICT vertical 3:4 aspect ratio, portrait canvas, 1536x2048 composition. Do not use 2:3, A4, square, landscape, or any other ratio.

Overall feeling:
A beautiful but practical handwritten study note made by a top student after class. Clean, focused, useful for review. It should look like a real learning note, not a poster, not a worksheet, not a slide.

Paper and writing:
A full-bleed clean study-note canvas. The entire image canvas is the note page itself. Use a warm off-white or very light cream background directly as the canvas, not pure blank white. No visible paper sheet edge, no surrounding background, no drop shadow, no open notebook, no notebook spine, no book edge, no desk background, no page curl, no camera perspective, no photorealistic paper object or mockup scene. Black gel-pen or fountain-pen handwriting. The handwriting must be neat, readable, natural, and consistent. Use Chinese handwriting if the content is Chinese.

Page title:
{标题，不超过 12 个字，放在顶部，像手写标题，可加短下划线}

One-line overview:
{一句话说明这页解决的问题或核心结论}

Layout:
Use the {版式名称} layout.
{具体说明标题、主体、图解、复习提醒分别放在什么位置。要求分区清楚，但不要正式表格或硬网格。Separate sections mainly with whitespace, small labels, and soft hand-drawn containers. Avoid obvious vertical divider lines, rigid split-screen layout, or PPT-like module boxes.}

Core notes:
Write 3 to 5 short learning points, each point concise and easy to review:
{要点1}
{要点2}
{要点3}
{可选要点4}
{可选要点5}

Highlight words:
Use soft yellow highlighter only on these key terms: {关键词1} / {关键词2} / {关键词3} / {可选关键词4}.
If there is a misconception or contrast, use a small amount of soft pink highlighter for: {可选易错词}.
Do not highlight full sentences.

Mini diagram:
Add one small hand-drawn diagram that explains the relationship: {图解说明}.
The diagram should occupy about 15%-25% of the page and must directly support the learning content.

Review reminder:
Add one short review reminder near the bottom inside a flat pale-yellow reminder block drawn directly on the same canvas: {复习提醒}. Do not make it a realistic sticky note. No shadow, no tape, no curled corner, no floating paper effect.

Visual constraints:
Default output is a full-bleed clean study-note canvas, not a notebook photo and not a paper sheet mockup. The entire image canvas is the note page itself. Use warm off-white or very light cream background directly as the canvas, not pure white. No visible sheet edge, no paper border, no surrounding background, no drop shadow, no desk, no mockup, no photo-realistic paper object, no open notebook, no notebook spine, no page curl, no strong shadow, no camera perspective. Separate sections mainly with whitespace, small labels, and soft hand-drawn containers. Avoid obvious vertical divider lines, rigid split-screen layout, or PPT-like module boxes. The review reminder should be a flat colored block drawn directly on the same canvas, not a realistic sticky note; no shadow, no tape, no curled corner, no floating paper effect, no 3D thickness. Vary the layout according to the knowledge structure; do not always use the same title-body-diagram-reminder arrangement. No formal bullet list markers. No dense textbook paragraphs. No PPT style. No printed worksheet. No formal table. No cute cartoon poster. No excessive stickers. No vintage yellow paper. No complex background. Leave comfortable whitespace. Keep all text readable.
```

## 背景模式规则

默认使用“全画布成品笔记页模式”：

```text
full-bleed clean study-note canvas
the entire canvas is the note page
warm off-white or light cream canvas background
no visible paper sheet edge
no surrounding background
no drop shadow
no notebook background
no desk scene
no perspective
no paper mockup
```

只有用户明确要求展示、宣传、样机、真实笔记本场景时，才使用“展示样机模式”：

```text
open notebook mockup
soft natural light
desk background
realistic presentation scene
```

不要把展示样机模式作为默认输出。默认也不要生成“纸张放在背景上”的样机效果。

## 多页生成规则

如果需要多页：

1. 先拆主题
2. 先输出 page-outline 和 page-prompts
3. 每页一个小主题
4. 每页版式可以变化
5. 每页高亮词不要重复太多
6. 最后一页可以做总结或易错提醒
7. 按顺序逐页单独生成
8. 每次只把当前页 final prompt 发给图片模型
9. 如果单页超过 180 秒无结果，立即按超时降级规则重试

推荐页数：

- 短段内容：1 页
- 一节课：2-3 页
- 长课程 / 长文：3-5 页
- 超过 5 页时，先问用户是否继续扩展

## 提醒块规则

默认把“复习提醒”做成平面提示色块，而不是实物便利贴。

推荐提示词：

```text
a flat pale-yellow reminder block drawn directly on the same canvas
no shadow
no tape
no curled corner
no floating paper effect
no realistic sticky note
no 3D thickness
```

避免提示词：

```text
sticky note
post-it note
taped note
realistic paper note
drop shadow
```

只有用户明确要求手账、便利贴或样机氛围时，才可以使用真实便利贴。

## 版式防模板化规则

每次生成前，先判断内容结构，再选择版式。

不要默认套用同一套构图。尤其避免所有页面都变成：

```text
顶部标题
中间左右分栏
下方小图解
右下便利贴
```

更好的做法：

- 对比内容：可以左右分区，但用留白和小标签分开，不画硬竖线。
- 流程内容：用轻路径或阶梯式阅读动线。
- 概念内容：用定义卡 + 例子 + 易错提醒。
- 分类内容：用中心发散或松散分组。
- 公式内容：把公式放中间，周围做条件和误区标注。

版式要变化，但阅读顺序必须清楚。

## 常见修正提示

### 太像讲义

```text
Regenerate this as a real handwritten study note, not a printed worksheet. Reduce dense paragraphs, create clear visual zones, keep only 3-5 concise learning points, add one relevant mini diagram, and preserve readable Chinese handwriting.
```

### 太花哨

```text
Regenerate with fewer decorations. Use only one flat pale-yellow reminder block drawn directly on the canvas, remove extra stickers, tape effects, shadows, and large illustrations, use clean whitespace, and make the page feel like a focused study note.
```

### 重点不明显

```text
Regenerate with clearer learning hierarchy. Make the title more visible, highlight only 2-4 true key terms in yellow, add a one-line overview under the title, and make the review reminder more memorable.
```

### 字太难读

```text
Regenerate with neater, larger, more readable handwritten Chinese. Keep the hand-written feeling but avoid messy cursive or decorative fonts. Maintain enough spacing between lines.
```

### 内容太满

```text
Split this into two separate study-note pages. Each page should cover one subtopic only, with 3-5 points, one mini diagram, and one review reminder.
```
