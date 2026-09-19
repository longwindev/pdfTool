# FindPDFTool Phase 5 — Auto Ads + domain rollback

## Production domain
https://findtoolpdf.online

## Added
- Google Search Console verification:
  `rOgrVIhA3zvWKRtYJcDfE-y4-e90Qz6qnMkGVMKHuUg`
- AdSense Auto Ads script for publisher:
  `ca-pub-5107605542667246`
- Removed all manual AdSense slot environment variables and manual ad placement rendering.
- Removed stale/incorrect AdSense loader references, including the old publisher found in `to_text.html`.
- Canonical URLs, hreflang, sitemap and robots now use `findtoolpdf.online`.

## Environment
SITE_URL=https://findtoolpdf.online
ADSENSE_CLIENT=ca-pub-5107605542667246
GA_MEASUREMENT_ID=G-CT33X6QTYH

No manual AdSense ad-unit slot environment variables are required.
