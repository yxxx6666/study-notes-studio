# 3:4 比例验证协议 v1.4.0

## 核心规则

“提示词写了 3:4”不等于“产物就是 3:4”。

每页生成后必须检查实际比例。

## 图片模型模式

使用图片模型生成时，final prompt 第一行必须写：

```plain text
STRICT 3:4 VERTICAL IMAGE ONLY. Portrait composition. Do not use 2:3, A4, square, landscape, or any other ratio.
```

生成后检查：

- 如果系统能读取图片尺寸，检查宽高比是否为 0.75。
- 如果不能读取尺寸，必须人工视觉确认是否明显偏离 3:4。
- 如果不是 3:4，先做一次“比例专用重试”，不要同时大改内容。

## 比例专用重试

重试时只强化比例和画布：

```plain text
Regenerate the same page as a strict 3:4 vertical image. Keep the same content and layout idea, but correct the canvas ratio only. No A4. No 2:3. No square.
```

## 确定性 PNG 模式

当用户要求固定像素，或图片模型连续比例失败且用户同意改用确定性绘制时：

- 推荐尺寸：1536 × 2048。
- 每张 PNG 必须检查实际像素尺寸。
- 不使用 HTML。
- 输出前报告每张图片尺寸。

## 禁止事项

- 禁止只凭“我写了 3:4 prompt”就声称通过。
- 禁止比例失败后直接说完成。
- 禁止用户要求图片模型时擅自切换到程序绘制。
- 禁止用户说禁止 HTML 后仍建议 HTML 导出。
