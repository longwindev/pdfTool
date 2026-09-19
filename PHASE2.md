# FindPDFTool — Phase 2

Implemented:
- 2026-style tool workspace UI for Merge PDF, Split PDF, PDF to Text, Image to PDF.
- Responsive shared tool hero, trust strip, upload/config cards, drag-over state.
- Redesigned result/download page with output metadata and temporary-storage notice.
- Related-tools navigation to increase useful page depth/session flow.
- AdSense-safe reserved placements after the primary workspace/download action.
- Consent-aware Auto Ads loader using publisher `ca-pub-5107605542667246`.
- Existing FastAPI processing endpoints and localized result routes retained.

Important AdSense note:
- Manual `data-ad-slot` values are intentionally NOT hardcoded. Create responsive ad units in your own AdSense account and insert the real slot IDs later.
- Auto Ads script is loaded after the current cookie consent is accepted.
