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

## 单页生成提示词模板

生成图像时使用下面结构。根据内容替换变量。

```text
Create one vertical A4-style visual study notes page, 3:4 aspect ratio.

Overall feeling:
A beautiful but practical handwritten study note made by a top student after class. Clean, focused, useful for review. It should look like a real learning note, not a poster, not a worksheet, not a slide.

Paper and writing:
A clean flat single-page note on soft warm off-white paper with very subtle texture, like a scanned handwritten study sheet. The paper should be warm off-white, not pure blank white. No open notebook, no notebook spine, no book edge, no desk background, no page curl, no camera perspective, no strong shadow, no photorealistic mockup scene. Black gel-pen or fountain-pen handwriting. The handwriting must be neat, readable, natural, and consistent. Use Chinese handwriting if the content is Chinese.

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
Add one short review reminder near the bottom or on one small sticky note: {复习提醒}.

Visual constraints:
Default output is a clean flat single-page note, not a notebook photo. Use subtle warm off-white paper texture, not pure white. Separate sections mainly with whitespace, small labels, and soft hand-drawn containers. Avoid obvious vertical divider lines, rigid split-screen layout, or PPT-like module boxes. If using a sticky note, keep it flat and lightly drawn with no heavy drop shadow or realistic 3D effect. Vary the layout according to the knowledge structure; do not always use the same title-body-diagram-sticky-note arrangement. No formal bullet list markers. No dense textbook paragraphs. No PPT style. No printed worksheet. No formal table. No cute cartoon poster. No excessive stickers. No vintage yellow paper. No complex background. No open notebook, no notebook spine, no desk, no page curl, no strong shadow, no camera perspective. Leave comfortable whitespace. Keep all text readable.
```

## 背景模式规则

默认使用“成品笔记页模式”：

```text
clean flat single-page note
scanned handwritten study sheet
soft off-white paper
no notebook background
no desk scene
no perspective
```

只有用户明确要求展示、宣传、样机、真实笔记本场景时，才使用“展示样机模式”：

```text
open notebook mockup
soft natural light
desk background
realistic presentation scene
```

不要把展示样机模式作为默认输出。

## 多页生成规则

如果需要多页：

1. 先拆主题
2. 每页一个小主题
3. 每页版式可以变化
4. 每页高亮词不要重复太多
5. 最后一页可以做总结或易错提醒

推荐页数：

- 短段内容：1 页
- 一节课：2-3 页
- 长课程 / 长文：3-5 页
- 超过 5 页时，先问用户是否继续扩展

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
Regenerate with fewer decorations. Keep only one small sticky note or tape element, remove extra stickers and large illustrations, use clean whitespace, and make the page feel like a focused study note.
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
