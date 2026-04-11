# README

这是一个基于 `Hugo` + `Ananke` 主题的个人博客仓库，站点配置入口在 [hugo.toml](/Users/taoruyi/Downloads/project/personal/try6.github.io/hugo.toml:1)。

我已经在这个目录里实际验证过：

- `hugo` 可以直接构建成功
- `hugo server --bind 127.0.0.1 --port 1313` 可以本地启动预览
- 当前环境里的 Hugo 版本是 `v0.147.1+extended`

## 目录说明

- [content/](/Users/taoruyi/Downloads/project/personal/try6.github.io/content)
  站点内容来源。
- [layouts/](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts)
  你对主题做的本地模板覆盖，真正影响首页和 publication 页面的逻辑主要在这里。
- [themes/ananke/](/Users/taoruyi/Downloads/project/personal/try6.github.io/themes/ananke)
  博客模板本体。
- [static/images/](/Users/taoruyi/Downloads/project/personal/try6.github.io/static/images)
  静态图片资源。
- [public/](/Users/taoruyi/Downloads/project/personal/try6.github.io/public)
  Hugo 编译后的静态站点输出目录。
- [resources/](/Users/taoruyi/Downloads/project/personal/try6.github.io/resources)
  Hugo 的生成缓存。

## 本地启动

先进入仓库根目录：

```bash
cd /Users/taoruyi/Downloads/project/personal/try6.github.io
```

然后启动开发服务器：

```bash
hugo server --bind 127.0.0.1 --port 1313
```

启动成功后，在浏览器打开：

```text
http://localhost:1313/
```

如果你想让草稿文章也显示出来，可以用：

```bash
hugo server -D --bind 127.0.0.1 --port 1313
```

如果你改了文件，Hugo 会自动热更新。

## 你本地怎么编译

生成正式静态文件：

```bash
hugo
```

输出会写到：

```text
public/
```

如果你想更接近 GitHub Actions 的部署方式，可以用：

```bash
hugo --minify
```

## 部署方式

仓库里已经有 GitHub Actions 工作流 [hugo.yaml](/Users/taoruyi/Downloads/project/personal/try6.github.io/.github/workflows/hugo.yaml:1)。

当前逻辑是：

1. push 到 `main`
2. GitHub Actions 用 `Hugo 0.147.1 extended` 构建
3. 把 `public/` 发布到 `gh-pages` 分支

## 目前站点的主要内容结构

- `content/_index.md`
  首页自我介绍
- `content/posts/`
  博客文章
- `content/publications/`
  论文/成果列表
- `content/papers/`
  另一组 paper 风格页面，目前菜单里没有直接入口

## 几个容易忘的细节

- 首页模板在 [layouts/_default/index.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/index.html:1)，不是完全使用主题默认首页。
- `publications` 列表页模板在 [layouts/publications/list.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/publications/list.html:1)。
- 首页 publication 数量目前是模板里直接写死的 `3`，不是自动读取 `home_publications_count`。
- 仓库里有 [assets/publications.css](/Users/taoruyi/Downloads/project/personal/try6.github.io/assets/publications.css:1)，但当前没有接到 `custom_css`，所以实际上没有生效。
- 当前构建会出现一个 Ananke 的 warning，原因是本地 `summary-with-image` 模板还在走旧兼容路径；这不影响构建成功。
- [.gitignore](/Users/taoruyi/Downloads/project/personal/try6.github.io/.gitignore:1) 里把 `resources/` 拼成了 `recources/`，如果你后面发现生成缓存被 Git 跟踪，这就是原因。

## 如果本机没有 Hugo

先确认：

```bash
hugo version
```

如果命令不存在，再安装 Hugo Extended。你当前仓库和工作流使用的是 `0.147.1 extended`，所以本地最好也尽量接近这个版本。

## 交接文档

后续如果要让别的 AI 快速接手，请先看 [AGENTS.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/AGENTS.md:1)。
