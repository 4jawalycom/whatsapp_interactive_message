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
