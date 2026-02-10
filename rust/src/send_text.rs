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
