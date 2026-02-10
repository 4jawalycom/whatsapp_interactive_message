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
