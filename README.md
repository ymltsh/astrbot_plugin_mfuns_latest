# AstrBot MFuns 最新内容插件

获取 MFuns（喵御宅/M站）最新内容的 AstrBot 插件。

## 功能特性

- 获取最新动态（feed）
- 获取最新视频（video）
- 获取最新文章（article）
- 支持自定义返回数量

## 安装方法

1. 在 AstrBot WebUI 的插件管理页面添加插件
2. 输入仓库地址: `https://github.com/ymltsh/astrbot_plugin_mfuns_latest.git`
3. 点击安装

## 使用方法

### 命令调用

```
/mfuns [type] [limit]
```

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | string | all | 内容类型：all, feed, video, article |
| limit | int | 10 | 返回数量，最大 100 |

### 示例

```
/mfuns                    # 获取全部类型最新 10 条
/mfuns video              # 获取最新 10 个视频
/mfuns article 20         # 获取最新 20 篇文章
/mfuns feed 5             # 获取最新 5 条动态
```

## 依赖

- aiohttp >= 3.8.0

## License

MIT
