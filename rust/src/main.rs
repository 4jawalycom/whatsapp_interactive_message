// عينة رسائل واتساب عبر 4Jawaly API
// WhatsApp message samples via 4Jawaly API
// 4Jawaly API کے ذریعے واٹس ایپ پیغامات کے نمونے

mod api;
mod send_audio;
mod send_buttons;
mod send_document;
mod send_image;
mod send_list;
mod send_text;
mod send_video;

use api::Config;
use send_audio::send_audio;
use send_buttons::send_buttons;
use send_document::send_document;
use send_image::send_image;
use send_list::{send_list, ListRow, ListSection};
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

    println!("\nتم الانتهاء / Done / فارغ");
}
