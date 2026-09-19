# FindPDFTool — Phase 3

## Added production routes/tools
- `/[lang]/compress-pdf` → `/api/compress`
- `/[lang]/pdf-to-jpg` → `/api/pdf-to-jpg`
- `/[lang]/jpg-to-pdf` → `/api/jpg-to-pdf`
- `/[lang]/rotate-pdf` → `/api/rotate`
- `/[lang]/delete-pdf-pages` → `/api/delete-pages`
- `/[lang]/extract-pdf-pages` → `/api/extract-pages`

## SEO / discovery
- EN + JA purpose-written landing copy for all six new tools.
- Canonical + hreflang tags are generated in `base.html`.
- Corrected domain references to `https://findtoolpdf.online`.
- Sitemap includes all Phase 3 tool URLs for supported languages.
- Home and All Tools pages link to every new tool.
- `robots.txt` blocks API/upload storage and points to the sitemap.

## UX
- Reuses Phase 2 2026 workspace design.
- Upload status, tool-specific controls, error state, processing state.
- Related-tool internal linking.
- AdSense placeholder remains separated from upload/download actions.

## Technical notes
- Compress PDF currently uses lossless pypdf content-stream compression. It intentionally does not aggressively downsample embedded images, so image-heavy PDFs may see modest reductions.
- Multi-page PDF→JPG returns a ZIP; one-page documents return JPG directly.
- Temporary generated files continue to use the existing 10-minute cleanup lifecycle.
- `googletrans` import is now optional so unrelated PDF tools can start even if translation support is unavailable.

## Smoke tests performed
- All Jinja templates parse successfully.
- Python source compiles successfully.
- Six new API endpoints tested against generated sample PDF/JPG files.
- EN/JA tool pages and All Tools page returned HTTP 200.
