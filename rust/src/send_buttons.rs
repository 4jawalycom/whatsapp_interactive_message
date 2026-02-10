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
