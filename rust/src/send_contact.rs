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
