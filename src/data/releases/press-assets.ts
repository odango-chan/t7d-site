export type PressAssetCategory = "logo" | "key-visual" | "poster" | "social";

export interface PressDownload {
  label: string;
  href: string;
  format: "png" | "jpg" | "jpeg" | "webp" | "svg";
}

export interface PressAsset {
  id: string;
  category: PressAssetCategory;
  title: string;
  description?: string;
  previewHref?: string;
  downloads: PressDownload[];
  provenance: {
    upstreamRepo: "odango-chan/touhou-seven-days";
    upstreamAssetId: string;
    upstreamRevision: string;
  };
}

export const pressAssetSections: Array<{
  id: PressAssetCategory;
  label: string;
}> = [
  { id: "logo", label: "Logo" },
  { id: "key-visual", label: "Key Visual" },
  { id: "poster", label: "Poster" },
  { id: "social", label: "Social" },
];

/**
 * Public press downloads only.
 *
 * Do not register production previews, prompts, reference sheets, QA images,
 * source masters, or unaccepted generated artwork here.
 *
 * Accepted assets should use stable files under /public/press/ so external
 * media links do not change when the Astro build hash changes.
 */
export const pressAssets: PressAsset[] = [];
