import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";

const novel = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/novel",
  }),
});

export const collections = { novel };
