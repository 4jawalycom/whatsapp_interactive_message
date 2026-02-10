# WhatsApp 4Jawaly API - Rust Samples

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Rust لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Rust - WhatsApp 4Jawaly.md`](../ai-reference/Rust%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Rust reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Rust - WhatsApp 4Jawaly.md`](../ai-reference/Rust%20-%20WhatsApp%204Jawaly.md)

# عينات رسائل واتساب عبر 4Jawaly API - Rust
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات کے نمونے - Rust

## Requirements / المتطلبات / تقاضے

- Rust 1.70+ (install from https://rustup.rs)
- 4Jawaly project credentials: `app_key`, `api_secret`, `project_id`

## Setup / الإعداد / سیٹ اپ

1. Edit `src/main.rs` and set your credentials:
   - `app_key` - مفتاح التطبيق / Application key / ایپ کی کلید
   - `api_secret` - سر API / API secret / API راز
   - `project_id` - معرف المشروع / Project ID / پراجیکٹ آئی ڈی

2. Build and run:
   ```bash
   cargo build
   cargo run
   ```

## API Specification / مواصفات API / API کی تفصیلات

- **Base URL**: `https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}`
- **Method**: POST
- **Auth**: Basic Auth with base64(app_key:api_secret)
- **Content-Type**: application/json

## Message Types / أنواع الرسائل / پیغامات کی اقسام

| Type | Module | Description |
|------|--------|-------------|
| Text | `send_text` | رسالة نصية بسيطة / Simple text message / سادہ ٹیکسٹ پیغام |
| Buttons | `send_buttons` | أزرار تفاعلية (حد أقصى 3) / Interactive buttons (max 3) / انٹرایکٹو بٹن (زیادہ سے زیادہ 3) |
| List | `send_list` | قائمة تفاعلية / Interactive list / انٹرایکٹو لسٹ |
| Image | `send_image` | صورة مع وصف اختياري / Image with optional caption / تصویر (اختیاری کیپشن کے ساتھ) |
| Video | `send_video` | فيديو مع وصف اختياري / Video with optional caption / ویڈیو (اختیاری کیپشن کے ساتھ) |
| Audio | `send_audio` | ملف صوتي / Audio file / آڈیو فائل |
| Document | `send_document` | مستند PDF وغيره / Document (PDF, etc.) / دستاویز |

## Usage Example / مثال الاستخدام / استعمال کی مثال

```rust
use api::Config;
use send_text::send_text;

let config = Config::new("app_key", "api_secret", "project_id");
send_text(&config, "9665XXXXXXXX", "مرحبا!")?;
```

## Project Structure / هيكل المشروع / پراجیکٹ کی ساخت

```
rust/
├── Cargo.toml
├── README.md
└── src/
    ├── main.rs        # Entry point / نقطة الدخول / داخلہ کا نقطہ
    ├── api.rs         # Config & API helper / الإعدادات والمساعدة / ترتیبات اور مدد
    ├── send_text.rs
    ├── send_buttons.rs
    ├── send_list.rs
    ├── send_image.rs
    ├── send_video.rs
    ├── send_audio.rs
    └── send_document.rs
```

## License / الترخيص / لائسنس

MIT
