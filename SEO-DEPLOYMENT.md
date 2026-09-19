# PaperMint SEO Deployment Checklist

## Những gì đã có

- 135 URL cốt lõi: trang chủ, công cụ, trợ giúp và 3 trung tâm hướng dẫn.
- 462 URL hướng dẫn: 11 công cụ × 14 nhu cầu × EN/VI/JA.
- 597 URL duy nhất trong sitemap; mọi URL đã được kiểm thử trả HTTP 200.
- Canonical tự tham chiếu, hreflang EN/VI/JA cho cụm hướng dẫn.
- Article, HowTo, FAQPage và BreadcrumbList JSON-LD trên mỗi trang hướng dẫn.
- Liên kết từ trang công cụ đến hướng dẫn, từ trung tâm hướng dẫn đến mọi bài và giữa các bài liên quan.

## Sau khi deploy

1. Mở `https://findtoolpdf.online/sitemap.xml` và xác nhận thấy `core.xml` cùng `guides.xml`.
2. Trong Google Search Console, gửi duy nhất URL `https://findtoolpdf.online/sitemap.xml`.
3. Dùng URL Inspection kiểm tra một trang công cụ và ba trang hướng dẫn đại diện EN, VI, JA.
4. Chỉ yêu cầu index thủ công cho vài trang đại diện; để Google tự thu thập phần còn lại qua sitemap và liên kết nội bộ.
5. Theo dõi mục Pages/Indexing trong 2–6 tuần. Không có cách hợp lệ nào bảo đảm Google index đủ 597 URL ngay lập tức.
6. Nếu Google đánh dấu Crawled/Discovered – currently not indexed, cải thiện nội dung và liên kết của nhóm đó thay vì tạo thêm URL.
7. Không mở thêm ngôn ngữ cho cụm hướng dẫn cho đến khi nội dung được biên tập đầy đủ; route ngoài EN/VI/JA hiện chuyển về bản tiếng Anh.

## Kiểm tra nhanh trước mỗi lần phát hành

```bash
npm run build:css
python generate_sitemap.py
python -m compileall -q app services generate_sitemap.py
```

Kết quả mong đợi của sitemap: `135 core URLs`, `462 guide URLs`, `597 total`.
