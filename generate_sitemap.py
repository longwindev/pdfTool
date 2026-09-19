from datetime import date
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom

from app.content.seo_guides import GUIDE_LANGUAGES, guide_slugs

BASE_URL = "https://findtoolpdf.online"
ALL = ["en", "vi", "ja", "zh", "ru", "pt", "de", "ko", "fr", "es"]
REVIEWED_EXTRA = ["en", "ja"]
CORE = [
    ("", "daily", "1.0"), ("pdf-to-word", "weekly", "1.0"),
    ("merge", "weekly", "0.9"), ("split", "weekly", "0.9"),
    ("to-text", "weekly", "0.9"), ("image-to-pdf", "weekly", "0.9"),
    ("help/tools", "monthly", "0.6"), ("help/faq", "monthly", "0.5"),
    ("help/about", "monthly", "0.5"), ("help/contact", "monthly", "0.4"),
    ("help/privacy", "yearly", "0.3"), ("help/terms", "yearly", "0.3"),
]
EXTRA = [
    ("compress-pdf", "weekly", "0.9"), ("pdf-to-jpg", "weekly", "0.9"),
    ("jpg-to-pdf", "weekly", "0.9"), ("rotate-pdf", "weekly", "0.9"),
    ("delete-pdf-pages", "weekly", "0.9"), ("extract-pdf-pages", "weekly", "0.9"),
]

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML = "http://www.w3.org/1999/xhtml"
ET.register_namespace("", NS)
ET.register_namespace("xhtml", XHTML)
TODAY = date.today().isoformat()
OUT = Path("app/sitemaps")
OUT.mkdir(parents=True, exist_ok=True)


def pretty(root: ET.Element) -> str:
    return minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")


def add_url(root: ET.Element, lang: str, suffix: str, languages, changefreq: str, priority: str):
    suffix = f"/{suffix}" if suffix else "/"
    node = ET.SubElement(root, f"{{{NS}}}url")
    ET.SubElement(node, f"{{{NS}}}loc").text = f"{BASE_URL}/{lang}{suffix}"
    ET.SubElement(node, f"{{{NS}}}lastmod").text = TODAY
    ET.SubElement(node, f"{{{NS}}}changefreq").text = changefreq
    ET.SubElement(node, f"{{{NS}}}priority").text = priority
    ET.SubElement(node, f"{{{XHTML}}}link", {"rel": "alternate", "hreflang": "x-default", "href": f"{BASE_URL}/en{suffix}"})
    for alternate in languages:
        ET.SubElement(node, f"{{{XHTML}}}link", {"rel": "alternate", "hreflang": alternate, "href": f"{BASE_URL}/{alternate}{suffix}"})


core_root = ET.Element(f"{{{NS}}}urlset")
for pages, languages in ((CORE, ALL), (EXTRA, REVIEWED_EXTRA)):
    for page, frequency, priority in pages:
        for language in languages:
            add_url(core_root, language, page, languages, frequency, priority)
for language in GUIDE_LANGUAGES:
    add_url(core_root, language, "guides", GUIDE_LANGUAGES, "weekly", "0.7")
(OUT / "core.xml").write_text(pretty(core_root), encoding="utf-8")

guide_root = ET.Element(f"{{{NS}}}urlset")
for tool_slug, use_slug in guide_slugs():
    suffix = f"guides/{tool_slug}/{use_slug}"
    for language in GUIDE_LANGUAGES:
        add_url(guide_root, language, suffix, GUIDE_LANGUAGES, "monthly", "0.6")
(OUT / "guides.xml").write_text(pretty(guide_root), encoding="utf-8")

index_root = ET.Element(f"{{{NS}}}sitemapindex")
for filename in ("core.xml", "guides.xml"):
    node = ET.SubElement(index_root, f"{{{NS}}}sitemap")
    ET.SubElement(node, f"{{{NS}}}loc").text = f"{BASE_URL}/sitemaps/{filename}"
    ET.SubElement(node, f"{{{NS}}}lastmod").text = TODAY
Path("app/sitemap.xml").write_text(pretty(index_root), encoding="utf-8")

print(f"Generated {len(core_root)} core URLs and {len(guide_root)} guide URLs ({len(core_root) + len(guide_root)} total).")
