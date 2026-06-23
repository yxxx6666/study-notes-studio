# 原创学习锚点图案协议 v1.4.0

## 定义

原创学习锚点图案是每页学习笔记里的“小型记忆提示符”。

它不是角色。
不是吉祥物。
不是插画主角。
不是固定 IP。

它只承担三个功能：

1. 标记本页重点。
2. 引导阅读路径。
3. 帮助读者形成记忆钩子。

## 设计原则

- 一页一个锚点。
- 锚点服务知识，不服务炫技。
- 使用普通学习物件、路径符号、记忆符号或抽象结构符号。
- 不使用可识别角色、不使用拟人怪物、不建立系列化角色。
- 不复用外部案例的构图、动作、轮廓、角色或视觉壳。

## 图案池

按内容选择一个，不要同时堆多个：

- 出勤 / 开始：小路标、课程门牌、日历角标
- 笔记 / 记录：笔记卡、小铅笔、书签
- 发言 / 讨论：小气泡、举手符号、问号灯泡
- 复习 / 记忆：记忆抽屉、循环箭头、卡片盒
- 拖延 / 时间：小闹钟、沙漏、进度条
- 沟通 / 求助：小信封、办公室门牌、对话框
- 自信 / 心态：小旗帜、指南针、上升箭头
- 社团 / 活动：小徽章、校园地图针
- 时间管理：日程格、优先级小阶梯
- 毕业 / 职业：小简历夹、实习工牌、出口路标

## 尺寸与位置

- 占画面约 6%–12%。
- 放在关键区块旁边，不能压住文字。
- 不要放成页面主角。
- 不要超过核心图解面积。
- 不要和标题、正文、复习提醒争抢视觉中心。

## Prompt 模板

```plain text
Learning anchor motif: add one small original content-linked hand-drawn learning symbol, about 6%-12% of the page, placed near the key section. It should reinforce the main learning idea without becoming a mascot, character, or main illustration. Use ordinary study objects, route symbols, memory symbols, or abstract structure symbols only. Avoid any recognizable character design, creature, mascot, IP-like figure, copied composition, or recurring character system.
```

## 失败信号

- 锚点像角色或吉祥物。
- 锚点比知识结构更抢眼。
- 锚点导致文字变小或挤压。
- 锚点与本页知识点无关。
- 锚点形成固定角色设定。
- 锚点复用了外部案例的构图、动作、轮廓或视觉壳。

## 修复顺序

1. 缩小锚点。
2. 减少细节。
3. 换成普通学习物件。
4. 移到边角或留白处。
5. 仍不稳定时删除锚点，但不得删除知识点。

## 优先级

```plain text
知识点覆盖 > 中文可读 > 3:4 比例 > 图解结构 > 学习锚点图案 > 其他装饰
```
