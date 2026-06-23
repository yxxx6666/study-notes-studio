# 清爽彩色手写笔记视觉基因 v1.4.0

## 一句话方向

像学霸用黑笔、荧光笔和彩色圆珠笔整理出的复习页：清爽、有颜色、有层级，但不花、不满、不像信息图。

不是极简黑白。
不是商业信息图。
不是 PPT 卡片页。
不是公众号知识海报。

## 视觉骨架

- 黑色手写线条是骨架。
- 彩色笔只负责信息层级。
- 留白必须舒服。
- 一页一个核心图解。
- 一页一个原创学习锚点。
- 文字短而准，像复习标签，不像正文排版。

## 常规学习笔记配色

<table header-row="true">
<tr><td>颜色</td><td>用途</td><td>限制</td></tr>
<tr><td>黑色</td><td>标题、正文、图解主线</td><td>主体色，占最大比例</td></tr>
<tr><td>荧光黄</td><td>关键词、高频考点</td><td>只高亮词，不涂整句</td></tr>
<tr><td>浅蓝</td><td>分区、补充说明、边注</td><td>轻描边或小标签</td></tr>
<tr><td>浅绿</td><td>正向结论、稳定系统、可持续</td><td>少量使用</td></tr>
<tr><td>浅粉 / 红色</td><td>易错、提醒、不要这样理解</td><td>只用于提醒，不做大警告框</td></tr>
<tr><td>淡橙</td><td>路径、箭头、步骤流向</td><td>只标主路径</td></tr>
</table>

## 颜色数量

每页最多使用 4–5 种学习笔记色。

推荐默认：

```plain text
黑色 + 荧光黄 + 浅蓝 + 淡橙 + 少量浅粉/红色
```

如果内容偏系统稳定，可以加入浅绿。

## 禁止过度极简

不要做成纯黑白草稿。
不要只有黑线和白底。
不要把“干净”理解成“没有颜色”。

学习笔记需要颜色层级，颜色必须像真实学生文具：荧光笔、彩色圆珠笔、浅色标注。

## 禁止过度彩色

不要做成彩色信息图。
不要满页色块。
不要每个模块不同大色块。
不要高饱和商业配色。
不要用颜色做装饰。

颜色只服务：关键词、路径、分区、提醒。

## final prompt 必加句

```plain text
Use a clean colorful handwritten study-note style: black pen lines as the skeleton, with restrained study-note colors such as soft yellow highlighter, pale blue section marks, light green positive highlights, soft pink/red correction marks, and muted orange arrows. Do not make it monochrome or overly minimal. Colors should look like real student note-taking tools, not a commercial infographic palette.
```

## QA 判断

合格：

- 像真实学生复习页。
- 有黑色手写骨架。
- 有少量常规学习笔记色。
- 有层级，但不花。
- 有颜色，但不像商业信息图。

失败：

- 纯黑白，太像草稿。
- 色块太多，像信息图。
- 图标太多，像模板页。
- 颜色像商业海报。
- 没有手写复习感。
