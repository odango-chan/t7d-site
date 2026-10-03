export interface MangaPage {
  id: string;
  assetKey: string;
  alt: string;
}

export interface PublicMangaChapter {
  id: string;
  order: number;
  dayLabel: string;
  title: string;
  subtitle: string;
  publicationStatus: "制作中" | "已公开";
  readingDirection: "ltr";
  colorMode: "bw";
  pages: MangaPage[];
  upstreamRepo: string;
  upstreamStoryPath: string;
  upstreamStorySha: string;
  upstreamManifestPath: string;
  upstreamManifestSha: string;
}

export const mangaChapters: PublicMangaChapter[] = [
  {
    id: "chapter-01",
    order: 1,
    dayLabel: "第一日",
    title: "忽见闲人满此乡",
    subtitle: "第一天嘛，当然不能浪费。",
    publicationStatus: "制作中",
    readingDirection: "ltr",
    colorMode: "bw",
    pages: [],
    upstreamRepo: "odango-chan/touhou-seven-days",
    upstreamStoryPath: "docs/production/comic/chapters/chapter-01.md",
    upstreamStorySha: "004c122283e729015a47b2df3c1061fee23185ce",
    upstreamManifestPath: "assets/comic/chapter-01/manifest.yaml",
    upstreamManifestSha: "c843d65694e773f2d6c92d257183474be17afb72",
  },
];
