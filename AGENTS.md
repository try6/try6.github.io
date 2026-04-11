# AGENTS.md

## Repo Purpose

This repository is a personal academic blog built with `Hugo` and the vendored `Ananke` theme.
The live site URL configured in [hugo.toml](/Users/taoruyi/Downloads/project/personal/try6.github.io/hugo.toml:1) is `https://try6.github.io/`.

The site currently mixes:

- a homepage profile/introduction page
- a `posts` section for blog posts
- a `publications` section for publication records
- a `papers` section with paper-style content pages, currently not exposed in the main menu

## Stack

- Static site generator: `Hugo`
- Theme: local copy of `themes/ananke`
- Verified local Hugo version in this workspace: `hugo v0.147.1+extended`
- Deployment: GitHub Actions builds `public/` and publishes to `gh-pages`

No Node-based build step is required for normal site development. The theme ships a `package.json`, but this repo can be built directly with Hugo.

## High-Level Structure

- [hugo.toml](/Users/taoruyi/Downloads/project/personal/try6.github.io/hugo.toml:1)
  Main site config: base URL, menu, theme, homepage params.
- [content/](/Users/taoruyi/Downloads/project/personal/try6.github.io/content)
  Site content.
- [layouts/](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts)
  Local template overrides on top of Ananke.
- [static/images/](/Users/taoruyi/Downloads/project/personal/try6.github.io/static/images)
  Static image assets used by homepage/posts/publications.
- [themes/ananke/](/Users/taoruyi/Downloads/project/personal/try6.github.io/themes/ananke)
  Vendored theme source.
- [public/](/Users/taoruyi/Downloads/project/personal/try6.github.io/public)
  Generated output directory.
- [resources/](/Users/taoruyi/Downloads/project/personal/try6.github.io/resources)
  Hugo-generated asset cache.

## Content Model

### Home

- [content/_index.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/content/_index.md:1)
  Homepage hero text and intro copy.

### Posts

- Stored as leaf bundles under `content/posts/<slug>/index.md`
- Examples:
  - [content/posts/scaling-law/index.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/content/posts/scaling-law/index.md:1)
  - [content/posts/granular_model/index.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/content/posts/granular_model/index.md:1)
- Homepage shows latest posts from section `posts`

### Publications

- Stored as flat markdown files under `content/publications/*.md`
- Custom front matter fields in active use:
  - `year`
  - `authors`
  - `journal`
  - `link`
  - `featured`
  - `featured_image`
- Example:
  - [content/publications/company_scaling.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/content/publications/company_scaling.md:1)
- The dedicated publications page groups entries by `year`
- Homepage only shows entries where `featured: true`

### Papers

- Stored under `content/papers/<slug>/index.md`
- Example:
  - [content/papers/company_prediction/index.md](/Users/taoruyi/Downloads/project/personal/try6.github.io/content/papers/company_prediction/index.md:1)
- The main menu entry for `Papers` is commented out in [hugo.toml](/Users/taoruyi/Downloads/project/personal/try6.github.io/hugo.toml:28), so this section exists but is not part of current primary navigation

## Local Template Overrides

The site behavior is mainly defined by a few local templates:

- [layouts/_default/index.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/index.html:1)
  Custom homepage layout. It:
  - renders homepage body content
  - renders latest posts
  - renders featured publications
  - contains a commented-out block for papers
- [layouts/publications/list.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/publications/list.html:1)
  Custom list page for publications grouped by year.
- [layouts/_default/summary-with-image.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/summary-with-image.html:1)
  Local summary renderer for cards with optional image.

Everything else mostly falls back to the Ananke theme defaults.

## Important Implementation Notes

- `site.Params.ananke.show_recent_posts` is not set in local config, but is provided by the theme default config and currently resolves to `true`.
- `home_publications_count` exists in [hugo.toml](/Users/taoruyi/Downloads/project/personal/try6.github.io/hugo.toml:15), but is not currently used by any template. The homepage hardcodes `first 3` featured publications in [layouts/_default/index.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/index.html:68).
- `assets/publications.css` exists, but it is not wired into `params.custom_css`, so it currently does not affect the rendered site.
- [layouts/_default/summary-with-image.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/summary-with-image.html:1) still triggers an Ananke warning about legacy partial usage. This is a warning only; the site still builds successfully.
- `public/` is generated output. Running `hugo` updates many tracked files there.
- `.gitignore` currently ignores `public/`, but contains a typo: `recources/` instead of `resources/`.

## Build And Preview

Verified commands in this workspace:

- Preview locally:
  - `hugo server --bind 127.0.0.1 --port 1313`
- Production build:
  - `hugo`
- CI-style production build:
  - `hugo --minify`

The local dev server serves at `http://localhost:1313/`.

## Deployment

[.github/workflows/hugo.yaml](/Users/taoruyi/Downloads/project/personal/try6.github.io/.github/workflows/hugo.yaml:1) builds with Hugo `0.147.1` and deploys `./public` to the `gh-pages` branch on every push to `main`.

## Recommended Change Strategy For Future Agents

- Prefer editing `content/` for copy/content updates.
- Prefer editing `layouts/` only when changing homepage or publication rendering behavior.
- Avoid modifying `themes/ananke/` unless the change truly belongs in the vendored theme.
- Treat `public/` and `resources/` as generated artifacts unless the human explicitly wants them committed or inspected.
- If changing homepage publication count, update [layouts/_default/index.html](/Users/taoruyi/Downloads/project/personal/try6.github.io/layouts/_default/index.html:68) rather than only editing `home_publications_count`.
