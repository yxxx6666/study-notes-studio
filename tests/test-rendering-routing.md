# 测试：出图引擎路由

## 图片模型优先

输入：

```plain text
使用 image 生图模型生成，比例 3:4。
```

预期：

- 使用图片模型。
- 不擅自切换到 Python / Pillow。
- 生成后检查比例。
- 比例失败时先用图片模型比例重试。

## 禁止 HTML

输入：

```plain text
禁止 HTML。
```

预期：

- 不使用 HTML。
- 不建议 HTML 导出。
- 可继续图片模型或在用户同意后用 Python / Pillow。
