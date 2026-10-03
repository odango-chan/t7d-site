# ADR-0001 — Public Site Stack

**Status:** Accepted  
**Date:** 2026-10-03

## Context

`t7d-site` 不是单一小说阅读器，而是《東方七日祭》的长期公开作品门户。

需要持续承载：

- novel reader；
- manga reader；
- public character gallery；
- game landing / downloads / store links；
- public news / release information；
- future illustrations and media。

主生产仓仍是 `odango-chan/touhou-seven-days`，公开站只接收 approved release material。

## Decision

正式公开站使用：

> **Astro + TypeScript + static output + GitHub Pages**

Repository:

> `odango-chan/t7d-site`

## Why

Astro 提供内容型静态站、Markdown / Content Collections、足够自由的小说 / 漫画 / 游戏页面、静态输出，以及 GitHub Pages 官方部署路径。

必要时可以加入少量客户端交互，而不要求整站 SPA 化。

## Alternatives considered

### Hugo

优点：单二进制、极简静态站、构建快。

未采用为正式门户的原因：

- 公开站未来不只有文章；
- 漫画阅读、人物页、游戏发布页等 UI 组合自由度更重要；
- 在不污染 release Markdown 的前提下需要额外 mount / adapter 约束。

Hugo PoC 不继续进入正式维护。

### Custom Go Publisher

优点：可完全服从自有出版模型，也适合未来 PDF / ePub / manifest pipeline。

未采用为网站主框架的原因：

- 会自行承担大量成熟 Web SSG 已解决的问题；
- 官网并不是最适合自研生成器的地方。

Custom Go Publisher 仍可作为未来出版 / 导出工具候选，但与 `t7d-site` Web stack 分离。

## Consequences

- 页面与 public content 在 Astro 体系内维护；
- 主仓 → site 仓之间需要明确 publish boundary；
- 不允许为了 Web 框架反向污染 Canon / Release Markdown；
- 游戏大文件通过 Releases / stores 分发，不通过 Pages；
- Web / PDF / ePub 将来可以共享 release metadata，但不强制使用同一个 renderer。

## Revisit when

只有出现以下情况才重审：

- GitHub Pages 不再满足站点规模；
- Astro 无法满足漫画 / 游戏门户需求；
- content sync 成本明显失控；
- 需要 SSR / server-side account features。

单纯“又出现一个新框架”不构成重审理由。