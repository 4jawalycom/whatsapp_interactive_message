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
