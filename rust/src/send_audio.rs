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
