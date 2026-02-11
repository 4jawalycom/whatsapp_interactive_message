# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Rust باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Rust using 4Jawaly

## معلومات API | API Information
- Base URL: https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
- Method: POST
- Auth: Basic Auth (base64(app_key:api_secret))
- Content-Type: application/json

## أنواع الرسائل المدعومة | Supported Message Types
1. رسالة نصية (Text)
2. أزرار تفاعلية (Interactive Buttons)
3. قائمة تفاعلية (Interactive List)
4. صورة (Image)
5. فيديو (Video)
6. ملف صوتي (Audio)
7. مستند (Document)
8. موقع جغرافي (Location)
9. جهة اتصال (Contact)

---

## التبعيات | Cargo.toml

```toml
[package]
name = "whatsapp_4jawaly"
version = "0.1.0"
edition = "2021"
description = "WhatsApp message samples for 4Jawaly API"
authors = ["4Jawaly"]
license = "MIT"

[dependencies]
reqwest = { version = "0.12", features = ["json", "blocking"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tokio = { version = "1", features = ["full"] }
base64 = "0.22"
```

---

## نقطة الدخول | main.rs

```rust
// عينة رسائل واتساب عبر 4Jawaly API
// WhatsApp message samples via 4Jawaly API
// 4Jawaly API کے ذریعے واٹس ایپ پیغامات کے نمونے

mod api;
mod send_audio;
mod send_buttons;
mod send_contact;
mod send_document;
mod send_image;
mod send_list;
mod send_location;
mod send_text;
mod send_video;

use api::Config;
use send_audio::send_audio;
use send_buttons::send_buttons;
use send_contact::send_contact;
use send_document::send_document;
use send_image::send_image;
use send_list::{send_list, ListRow, ListSection};
use send_location::send_location;
use send_text::send_text;
use send_video::send_video;

fn main() {
    // إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
    let config = Config::new(
        "your_app_key",
        "your_api_secret",
        "your_project_id",
    );

    let recipient = "9665XXXXXXXX";

    println!("=== 1. إرسال رسالة نصية / Text / ٹیکسٹ ===\n");
    if let Err(e) = send_text(&config, recipient, "نص الرسالة") {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 2. إرسال أزرار تفاعلية / Buttons / بٹن ===\n");
    let buttons = [
        ("btn_yes", "نعم"),
        ("btn_no", "لا"),
        ("btn_help", "مساعدة"),
    ];
    if let Err(e) = send_buttons(
        &config,
        recipient,
        "اختر أحد الخيارات التالية",
        &buttons,
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 3. إرسال قائمة تفاعلية / List / لسٹ ===\n");
    let sections = vec![
        ListSection {
            title: "الخدمات الأساسية".to_string(),
            rows: vec![
                ListRow {
                    id: "svc_sms".to_string(),
                    title: "خدمة الرسائل النصية".to_string(),
                    description: "إرسال رسائل SMS للعملاء".to_string(),
                },
                ListRow {
                    id: "svc_whatsapp".to_string(),
                    title: "خدمة واتساب".to_string(),
                    description: "إرسال رسائل واتساب تفاعلية".to_string(),
                },
            ],
        },
        ListSection {
            title: "الدعم الفني".to_string(),
            rows: vec![ListRow {
                id: "support_ticket".to_string(),
                title: "فتح تذكرة دعم".to_string(),
                description: "تواصل مع فريق الدعم الفني".to_string(),
            }],
        },
    ];
    if let Err(e) = send_list(
        &config,
        recipient,
        "عرض القائمة",
        "قائمة الخدمات",
        "اختر الخدمة المطلوبة من القائمة أدناه",
        Some("4Jawaly Services"),
        &sections,
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 4. إرسال صورة / Image / تصویر ===\n");
    if let Err(e) = send_image(
        &config,
        recipient,
        "https://example.com/image.jpg",
        Some("وصف الصورة"),
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 5. إرسال فيديو / Video / ویڈیو ===\n");
    if let Err(e) = send_video(
        &config,
        recipient,
        "https://example.com/video.mp4",
        Some("وصف الفيديو"),
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 6. إرسال ملف صوتي / Audio / آڈیو ===\n");
    if let Err(e) = send_audio(&config, recipient, "https://example.com/audio.mp3") {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 7. إرسال مستند / Document / دستاویز ===\n");
    if let Err(e) = send_document(
        &config,
        recipient,
        "https://example.com/document.pdf",
        Some("وصف المستند"),
        Some("document.pdf"),
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 8. إرسال موقع جغرافي / Location / مقام ===\n");
    if let Err(e) = send_location(
        &config,
        recipient,
        24.7136,
        46.6753,
        "Riyadh, Saudi Arabia",
        "My Office",
    ) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\n=== 9. إرسال جهة اتصال / Contact / رابطہ ===\n");
    let contacts = vec![serde_json::json!({
        "name": {
            "formatted_name": "Ahmed Ali",
            "first_name": "Ahmed",
            "last_name": "Ali"
        },
        "phones": [{"phone": "+966501234567", "type": "CELL"}]
    })];
    if let Err(e) = send_contact(&config, recipient, &contacts) {
        eprintln!("خطأ / Error / خرابی: {}", e);
    }

    println!("\nتم الانتهاء / Done / فارغ");
}
```

---

## وحدة API | api.rs

```rust
// إعدادات الاتصال والدالة المساعدة للاتصال بالـ API
// API connection settings and helper function for API calls
// API رابطہ کی ترتیبات اور API کالز کے لیے مدد گار فنکشن

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use reqwest::blocking::Client;
use serde_json::Value;

/// إعدادات الاتصال - Connection config - رابطہ کی ترتیبات
#[derive(Clone)]
pub struct Config {
    pub app_key: String,
    pub api_secret: String,
    pub project_id: String,
}

impl Config {
    /// إنشاء إعدادات جديدة - Create new config - نئی ترتیبات بنائیں
    pub fn new(app_key: &str, api_secret: &str, project_id: &str) -> Self {
        Self {
            app_key: app_key.to_string(),
            api_secret: api_secret.to_string(),
            project_id: project_id.to_string(),
        }
    }

    /// إنشاء رأس المصادقة Basic - Build Basic Auth header - Basic Auth header بنائیں
    fn auth_header(&self) -> String {
        let credentials = format!("{}:{}", self.app_key, self.api_secret);
        let encoded = BASE64.encode(credentials.as_bytes());
        format!("Basic {}", encoded)
    }

    /// الحصول على عنوان URL - Get API URL - API URL حاصل کریں
    fn base_url(&self) -> String {
        format!(
            "https://api-users.4jawaly.com/api/v1/whatsapp/{}",
            self.project_id
        )
    }
}

/// إرسال طلب إلى API وطباعة النتيجة
/// Send request to API and print response
/// API کو درخواست بھیجیں اور جواب پرنٹ کریں
pub fn make_api_call(config: &Config, data: Value) -> Result<(), Box<dyn std::error::Error>> {
    let url = config.base_url();
    let auth = config.auth_header();

    // بناء الجسم المغلف - Build wrapped request body - ریگوئسٹ باڈی بنائیں
    let payload = serde_json::json!({
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": data
        }
    });

    let client = Client::new();
    let response = client
        .post(&url)
        .header("Content-Type", "application/json")
        .header("Authorization", &auth)
        .json(&payload)
        .send()?;

    let status = response.status();
    let body = response.text()?;

    // طباعة رمز الاستجابة والجسم
    // Print response status and body
    // جوابی کوڈ اور باڈی پرنٹ کریں
    println!(
        "رمز الاستجابة / Response code / جوابی کوڈ: {}",
        status
    );

    match serde_json::from_str::<Value>(&body) {
        Ok(parsed) => println!(
            "\nالاستجابة / Response / جواب:\n{}",
            serde_json::to_string_pretty(&parsed).unwrap_or_default()
        ),
        Err(_) => println!("\nالنص الخام / Raw body / خام متن:\n{}", body),
    }

    Ok(())
}

/// إرسال طلب بمسار مخصص (location/contact)
/// Send request with custom path - path differs from global messages
pub fn make_custom_path_api_call(
    config: &Config,
    path: &str,
    params: serde_json::Value,
) -> Result<(), Box<dyn std::error::Error>> {
    let url = config.base_url();
    let auth = config.auth_header();

    let payload = serde_json::json!({
        "path": path,
        "params": params
    });

    let client = Client::new();
    let response = client
        .post(&url)
        .header("Content-Type", "application/json")
        .header("Authorization", &auth)
        .json(&payload)
        .send()?;

    let status = response.status();
    let body = response.text()?;

    println!("رمز الاستجابة / Response code / جوابی کوڈ: {}", status);

    match serde_json::from_str::<Value>(&body) {
        Ok(parsed) => println!(
            "\nالاستجابة / Response / جواب:\n{}",
            serde_json::to_string_pretty(&parsed).unwrap_or_default()
        ),
        Err(_) => println!("\nالنص الخام / Raw body / خام متن:\n{}", body),
    }

    Ok(())
}
```

---

## إرسال رسالة نصية | send_text.rs

```rust
// إرسال رسالة نصية عبر واتساب
// Send text message via WhatsApp
// واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں

use crate::api;
use serde_json::json;

/// إرسال رسالة نصية
/// Send text message
/// ٹیکسٹ پیغام بھیجیں
pub fn send_text(
    config: &api::Config,
    to: &str,
    body: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": body
        }
    });

    api::make_api_call(config, data)
}
```

---

## إرسال أزرار تفاعلية | send_buttons.rs

```rust
// إرسال رسالة بأزرار تفاعلية عبر واتساب
// Send interactive buttons message via WhatsApp
// واٹس ایپ کے ذریعے انٹرایکٹو بٹن پیغام بھیجیں

use crate::api;
use serde_json::json;

/// إرسال رسالة أزرار تفاعلية
/// Send interactive buttons message
/// انٹرایکٹو بٹن پیغام بھیجیں
pub fn send_buttons(
    config: &api::Config,
    to: &str,
    body_text: &str,
    buttons: &[(&str, &str)], // (id, title)
) -> Result<(), Box<dyn std::error::Error>> {
    let buttons_json: Vec<serde_json::Value> = buttons
        .iter()
        .map(|(id, title)| {
            json!({
                "type": "reply",
                "reply": {
                    "id": id,
                    "title": title
                }
            })
        })
        .collect();

    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": body_text
            },
            "action": {
                "buttons": buttons_json
            }
        }
    });

    api::make_api_call(config, data)
}
```

---

## إرسال قائمة تفاعلية | send_list.rs

```rust
// إرسال رسالة بقائمة تفاعلية عبر واتساب
// Send interactive list message via WhatsApp
// واٹس ایپ کے ذریعے انٹرایکٹو لسٹ پیغام بھیجیں

use crate::api;
use serde_json::json;

/// صف في القائمة - List row - لسٹ کی قطار
#[derive(Clone)]
pub struct ListRow {
    pub id: String,
    pub title: String,
    pub description: String,
}

/// قسم في القائمة - List section - لسٹ کا سیکشن
#[derive(Clone)]
pub struct ListSection {
    pub title: String,
    pub rows: Vec<ListRow>,
}

/// إرسال رسالة قائمة تفاعلية
/// Send interactive list message
/// انٹرایکٹو لسٹ پیغام بھیجیں
pub fn send_list(
    config: &api::Config,
    to: &str,
    button_text: &str,
    header_text: &str,
    body_text: &str,
    footer_text: Option<&str>,
    sections: &[ListSection],
) -> Result<(), Box<dyn std::error::Error>> {
    let sections_json: Vec<serde_json::Value> = sections
        .iter()
        .map(|sec| {
            let rows: Vec<serde_json::Value> = sec
                .rows
                .iter()
                .map(|row| {
                    json!({
                        "id": row.id,
                        "title": row.title,
                        "description": row.description
                    })
                })
                .collect();
            json!({
                "title": sec.title,
                "rows": rows
            })
        })
        .collect();

    let mut interactive = json!({
        "type": "list",
        "header": {
            "type": "text",
            "text": header_text
        },
        "body": {
            "text": body_text
        },
        "action": {
            "button": button_text,
            "sections": sections_json
        }
    });

    if let Some(footer) = footer_text {
        interactive["footer"] = json!({ "text": footer });
    }

    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": interactive
    });

    api::make_api_call(config, data)
}
```

---

## إرسال صورة | send_image.rs

```rust
// إرسال صورة عبر واتساب
// Send image via WhatsApp
// واٹس ایپ کے ذریعے تصویر بھیجیں

use crate::api;
use serde_json::json;

/// إرسال صورة
/// Send image message
/// تصویر بھیجیں
pub fn send_image(
    config: &api::Config,
    to: &str,
    link: &str,
    caption: Option<&str>,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut image = json!({
        "link": link
    });

    if let Some(cap) = caption {
        image["caption"] = json!(cap);
    }

    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "image",
        "image": image
    });

    api::make_api_call(config, data)
}
```

---

## إرسال فيديو | send_video.rs

```rust
// إرسال فيديو عبر واتساب
// Send video via WhatsApp
// واٹس ایپ کے ذریعے ویڈیو بھیجیں

use crate::api;
use serde_json::json;

/// إرسال فيديو
/// Send video message
/// ویڈیو بھیجیں
pub fn send_video(
    config: &api::Config,
    to: &str,
    link: &str,
    caption: Option<&str>,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut video = json!({
        "link": link
    });

    if let Some(cap) = caption {
        video["caption"] = json!(cap);
    }

    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "video",
        "video": video
    });

    api::make_api_call(config, data)
}
```

---

## إرسال ملف صوتي | send_audio.rs

```rust
// إرسال ملف صوتي عبر واتساب
// Send audio file via WhatsApp
// واٹس ایپ کے ذریعے آڈیو فائل بھیجیں

use crate::api;
use serde_json::json;

/// إرسال ملف صوتي
/// Send audio message
/// آڈیو بھیجیں
pub fn send_audio(
    config: &api::Config,
    to: &str,
    link: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "audio",
        "audio": {
            "link": link
        }
    });

    api::make_api_call(config, data)
}
```

---

## إرسال مستند | send_document.rs

```rust
// إرسال مستند عبر واتساب
// Send document via WhatsApp
// واٹس ایپ کے ذریعے دستاویز بھیجیں

use crate::api;
use serde_json::json;

/// إرسال مستند
/// Send document message
/// دستاویز بھیجیں
pub fn send_document(
    config: &api::Config,
    to: &str,
    link: &str,
    caption: Option<&str>,
    filename: Option<&str>,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut document = json!({
        "link": link
    });

    if let Some(cap) = caption {
        document["caption"] = json!(cap);
    }

    if let Some(name) = filename {
        document["filename"] = json!(name);
    }

    let data = json!({
        "messaging_product": "whatsapp",
        "to": to,
        "type": "document",
        "document": document
    });

    api::make_api_call(config, data)
}
```

---

## إرسال موقع جغرافي | send_location.rs

```rust
// إرسال موقع جغرافي عبر واتساب
// Send location via WhatsApp
// واٹس ایپ کے ذریعے مقام بھیجیں

use crate::api;
use serde_json::json;

/// إرسال موقع جغرافي
/// Send location
/// مقام بھیجیں
pub fn send_location(
    config: &api::Config,
    to: &str,
    lat: f64,
    lng: f64,
    address: &str,
    name: &str,
) -> Result<(), Box<dyn std::error::Error>> {
    let params = json!({
        "phone": to,
        "lat": lat,
        "lng": lng,
        "address": address,
        "name": name
    });

    api::make_custom_path_api_call(config, "message/location", params)
}
```

---

## إرسال جهة اتصال | send_contact.rs

```rust
// إرسال جهة اتصال عبر واتساب
// Send contact via WhatsApp
// واٹس ایپ کے ذریعے رابطہ بھیجیں

use crate::api;
use serde_json::json;

/// إرسال جهة اتصال
/// Send contact
/// رابطہ بھیجیں
pub fn send_contact(
    config: &api::Config,
    to: &str,
    contacts: &[serde_json::Value],
) -> Result<(), Box<dyn std::error::Error>> {
    let params = json!({
        "phone": to,
        "contacts": contacts
    });

    api::make_custom_path_api_call(config, "message/contact", params)
}
```
