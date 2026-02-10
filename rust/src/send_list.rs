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
