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
