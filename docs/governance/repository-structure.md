# Repository Structure & File Governance

**Owner:** t7d-site  
**Applies to:** public website repository  
**Issue:** #2

`t7d-site` 是《東方七日祭》的**公开作品门户仓**。它长期承载小说、漫画、人物、游戏、新闻与公开发布信息，但不是生产真源仓。

治理目标：

> 目录先表达 ownership，再表达文件类型；公开内容、站点代码、媒体资产和仓库工具不得混放。

## 1. Target tree

```text
t7d-site/
├─ .github/
│  └─ workflows/
├─ docs/
│  ├─ governance/
│  │  ├─ repository-structure.md
│  │  └─ publishing-boundary.md
│  ├─ architecture/
│  │  └─ ...
│  └─ decisions/
│     └─ adr-XXXX-*.md
├─ src/
│  ├─ assets/
│  │  ├─ brand/
│  │  ├─ characters/
│  │  ├─ novel/
│  │  ├─ manga/
│  │  └─ game/
│  ├─ components/
│  │  ├─ common/
│  │  ├─ novel/
│  │  ├─ manga/
│  │  ├─ characters/
│  │  └─ game/
│  ├─ content/
│  │  ├─ novel/
│  │  ├─ manga/
│  │  └─ news/
│  ├─ data/
│  │  ├─ characters/
│  │  ├─ game/
│  │  ├─ releases/
│  │  └─ site/
│  ├─ layouts/
│  ├─ lib/
│  ├─ pages/
│  ├─ scripts/
│  └─ styles/
├─ public/
│  ├─ favicon.*
│  ├─ robots.txt
│  ├─ site.webmanifest
│  └─ verification-*
├─ tests/
│  ├─ smoke/
│  └─ e2e/
├─ tools/
│  ├─ sync/
│  └─ checks/
├─ AGENTS.md
├─ README.md
├─ package.json
├─ package-lock.json
├─ astro.config.mjs
├─ tsconfig.json
└─ .gitignore
```

目录只按实际需求创建；禁止为了“看起来完整”提交空目录。

## 2. Root whitelist

根目录只允许仓级入口和构建配置。

允许：

- `README.md`
- `AGENTS.md`
- `LICENSE*`（如后续需要）
- `package.json` / `package-lock.json`
- `astro.config.mjs` / `tsconfig.json`
- lint / formatter / test 的仓级配置
- `.gitignore`
- `.github/`
- `docs/`
- `src/`
- `public/`
- `tests/`
- `tools/`

不允许把 feature 设计文档、发布说明、小说 / 漫画文本、截图、临时 JSON、一次性脚本、下载包继续堆在 root。

## 3. `src/pages/` — route owner

这里只负责 URL 路由与 page composition。

- URL = 目录结构；
- `novel/`、`manga/`、`characters/`、`game/`、`news/` 按 domain 分区；
- page 文件不存长篇业务数据；
- page 文件不成为样式、数据、同步逻辑的 owner；
- 少量 singleton route 可以暂时使用 `about.astro` 这种 flat 形式；一旦该 domain 出现第二个 route，就升级为目录。

## 4. `src/content/` — public editorial content

用于 Astro Content Collections 管理的**公开内容**。

- `novel/` — 已批准公开的小说 release copy；
- `manga/` — 漫画章节 metadata / public reading manifest；
- `news/` — 本站拥有的公开新闻 / 更新日志。

上游内容必须保留 provenance：

```yaml
upstreamRepo:
upstreamPath:
upstreamSha:
releaseStatus:
```

这里不放 Canon 草稿、prompt、QA、Issue 摘要。正常情况下不直接修改 upstream-owned prose。

## 5. `src/data/` — structured public data

用于不是文章、但需要跨页面复用的公开结构化数据：

- `characters/` — 公开人物卡；
- `game/` — 平台、商店、系统要求；
- `releases/` — 公开版本 metadata；
- `site/` — 导航、外链、站点级 metadata。

只导出公开页面真正需要的字段，禁止复制完整 Character Canon。

## 6. `src/assets/` vs `public/`

### `src/assets/`

默认媒体入口：

- Logo / brand art；
- accepted character portraits；
- novel illustrations；
- manga Web pages；
- game screenshots。

示例：

```text
src/assets/characters/reimu/portrait-v1.webp
src/assets/novel/day-01/opener-v1.webp
src/assets/manga/chapter-01/page-001.webp
src/assets/game/screenshots/stage-01-v1.webp
```

### `public/`

只放必须原路径透传、不参与 Astro pipeline 的文件：

- favicon；
- robots.txt；
- site.webmanifest；
- 平台验证文件；
- 极少数必须保持固定 URL 的 static artifact。

禁止把 feature JS、CSS、小说正文、漫画章节图、人物 portrait、游戏截图、临时文件放进 `public/`。

因此 reader behavior 属于 `src/scripts/`。

## 7. Media policy

`t7d-site` 只保存**Web release assets**。

允许：WebP / AVIF / PNG / SVG / JPEG 和已 Accepted 的 Web 分辨率媒体。

禁止提交：

- PSD / CLIP / CSP / Krita / EXR 等工作源；
- 原始超高分辨率 production art；
- 未审图像；
- prompts；
- ZIP / 7z / DMG / EXE / APK / IPA / HAP / APP；
- 游戏完整安装目录。

游戏二进制发布到 GitHub Releases、App Store / TestFlight、Android / HarmonyOS 商店或其他正式分发平台。站点只保存 release metadata 与链接。

如果漫画 / 视频资产未来明显推高仓体积，再迁对象存储 / CDN；不要先用 Git LFS 把公开站变成归档仓。

## 8. `src/components/`

组件按 domain 拆：

- `common/` — 至少两个 domain 真正共享；
- `novel/`
- `manga/`
- `characters/`
- `game/`

不要一开始把所有 Card / Button 都扔进 `common/`。

## 9. `src/lib/`, `src/scripts/`, `tools/`

### `src/lib/`

站点构建 / 运行时可复用模块，例如 content normalization、URL helper、release metadata、media helper。

### `src/scripts/`

浏览器侧、由站点 bundle 管理的小型交互，例如 reader preference、manga reader gesture。

### `tools/`

仓库维护工具，不进入浏览器：

- `tools/sync/` — 从主仓同步 approved release content；
- `tools/checks/` — provenance / public-boundary / broken-link checks。

不要建立单个巨大 `scripts/` 垃圾目录。

## 10. `docs/`

文档按职责分类：

- `docs/governance/` — repository structure、publishing boundary、命名与贡献规则；
- `docs/architecture/` — content sync、site architecture、media pipeline、deployment；
- `docs/decisions/` — 长期决策原因，命名 `adr-0001-*.md`。

Issue 负责工作追踪，不代替 ADR。

## 11. Naming

- directories：lowercase kebab-case；
- Astro components / layouts：PascalCase；
- TypeScript / data modules：kebab-case；
- content IDs：稳定机器名，如 `day-01.md`、`chapter-01.md`；
- manga pages：`page-001.webp`；
- 禁止 `misc`、`temp`、`others`、`new`、`final` 这类目录名。

媒体路径承担语义，文件名保持短：

```text
characters/reimu/portrait-v1.webp
manga/chapter-01/page-001.webp
```

版本只用于人工接受的源资产；build hash 产物不手工版本化。

## 12. Generated files

永不提交：

- `node_modules/`
- `dist/`
- `.astro/`
- `coverage/`
- `.cache/`
- local preview output
- package manager cache
- OS / editor temp files。

CI artifact 不是 Git source。

## 13. Public safety

公开站仓默认假设：

> **仓里的每一个 tracked byte 都可能被任何人看到。**

因此不要提交 API key、signing certificate、store secret、private analytics key、unpublished plot、internal review、user data 或 private production material。

secret 只进入 GitHub Actions environment / repository secrets。

## 14. Directory admission rule

新增一级目录前必须能回答：

1. 谁拥有它？
2. 为什么现有目录不能承载？
3. 它是 source、content、asset、tool 还是 generated？
4. 是否会成为“临时先放这里”的入口？
5. 是否公开安全？

答不清楚，不新增。

## 15. Immediate cleanup

本规则落地后立即执行：

- `PUBLICATION.md` → `docs/governance/publishing-boundary.md`；
- `public/reader.js` → `src/scripts/reader.ts`；
- root 新增 `AGENTS.md`；
- README 增加 repository map；
- `.gitignore` 扩展 generated / local rules。

当前少量 flat singleton page 可以暂留；后续 domain 扩展时再迁目录，不做无意义搬家。