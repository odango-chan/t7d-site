# t7d-site

Public website for **東方七日祭 ～ Seven Days of Leisure**.

> 非官方东方 Project 二次创作站点，与上海爱丽丝幻乐团 / Team Shanghai Alice 无隶属关系。

## Role

`t7d-site` 是面向读者 / 玩家公开的作品门户，不是剧情、人物或美术生产真源。

生产真源：

- `odango-chan/touhou-seven-days`

本站只接收已经批准公开的 release material。

## Stack

- Astro 7.3.5
- TypeScript
- static output
- GitHub Pages
- minimal client-side enhancement

长期技术决策见：

- [ADR-0001: Public Site Stack](docs/decisions/adr-0001-public-site-stack.md)

## Sections

- `/` — 作品首页
- `/novel/` — 小说阅读
- `/manga/` — 漫画阅读 / 发布
- `/characters/` — 公开人物目录；`/characters/<id>/` — 公开人物设定资料
- `/game/` — 游戏介绍 / Releases / 商店入口
- `/press/` — 已批准公开的媒体 / 宣传素材下载
- `/news/` — 后续公开更新
- `/about/` — 项目与二创声明

## Repository map

```text
.github/          GitHub workflows
docs/
  governance/    仓库规则 / 发布边界
  architecture/  网站架构与同步设计
  decisions/     ADR
src/
  assets/        Web-ready accepted media
  components/    reusable UI by domain
  content/       public editorial release content
  data/          structured public data
  layouts/       Astro layouts
  lib/           shared site/build modules
  pages/         routes
  scripts/       bundled browser behavior
  styles/        design tokens / global / domain styles
public/          passthrough-only static files
tests/           smoke / e2e when needed
tools/           sync / repository checks when needed
```

目录只在实际需要时创建，不提交空目录。

完整规则：

- [Repository Structure & File Governance](docs/governance/repository-structure.md)
- [Publishing Boundary](docs/governance/publishing-boundary.md)

## Current public release

小说已同步当前 Release Draft：

- Day 1～Day 7
- Extra / Day 8
- 可跳过的新读者导读《第一次来到幻想乡》

公开副本保留逐文件 upstream provenance；正常正文修改仍先回生产真源，再重新发布。

## Content ownership


公开小说等上游内容在本站是**发布副本**，必须保留 provenance，例如：

```yaml
upstreamRepo: odango-chan/touhou-seven-days
upstreamPath: docs/production/novel/chapters/day-01.md
upstreamSha: ...
releaseStatus: Release Draft Candidate
```

正常内容修改先回主仓，再重新发布到本站。

## Media / game releases

Web 图片进入 `src/assets/`。

游戏安装包、APK、DMG、EXE、IPA、HAP 等**不进入这个仓**。站点只提供：

- GitHub Releases 链接
- App Store / TestFlight
- Android / HarmonyOS 商店
- 其他正式分发入口

## Local development

```bash
npm install
npm run dev
```

Build:

```bash
npm run build
```

## GitHub Pages

Deployment is handled by GitHub Actions using Astro's official Pages action.

For this public repository, standard GitHub-hosted Actions runners are free under GitHub's current billing rules.

Before the first public deployment, set:

`Settings → Pages → Source → GitHub Actions`
