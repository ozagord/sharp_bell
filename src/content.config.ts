import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const blogCollection = defineCollection({
  loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/blog" }),
  schema: z.object({
    title: z.string(),
    author: z.string().optional(),
    categories: z.array(z.string()).optional(),
    description: z.string().default(''),
    tags: z.array(z.string()).optional(),
    date: z.date().or(z.string().transform((str) => new Date(str))),
    coverImage: z.string().optional(),
    headerimg: z.string().optional(),
    coverMeta: z.string().optional(),
    thumbnailImage: z.string().optional(),
    thumbnailImagePosition: z.string().optional(),
    featured: z.boolean().default(false),
  })
});

export const collections = {
  'blog': blogCollection,
};
