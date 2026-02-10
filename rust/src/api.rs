// إعدادات الاتصال والدالة المساعدة للاتصال بالـ API
// API connection settings and helper function for API calls
// API رابطہ کی ترتیبات اور API کالز کے لیے مدد گار فنکشن

use base64::{engine::general_purpose::STANDARD as BASE64, Engine};
use reqwest::blocking::Client;
use serde_json::Value;

/// إعدادات الاتصال - Connection config - رابطہ کی ترتیبات
#[derive(Clone)]
pub struct Config {
    pub app_key: String,
    pub api_secret: String,
    pub project_id: String,
}

impl Config {
    /// إنشاء إعدادات جديدة - Create new config - نئی ترتیبات بنائیں
    pub fn new(app_key: &str, api_secret: &str, project_id: &str) -> Self {
        Self {
            app_key: app_key.to_string(),
            api_secret: api_secret.to_string(),
            project_id: project_id.to_string(),
        }
    }

    /// إنشاء رأس المصادقة Basic - Build Basic Auth header - Basic Auth header بنائیں
    fn auth_header(&self) -> String {
        let credentials = format!("{}:{}", self.app_key, self.api_secret);
        let encoded = BASE64.encode(credentials.as_bytes());
        format!("Basic {}", encoded)
    }

    /// الحصول على عنوان URL - Get API URL - API URL حاصل کریں
    fn base_url(&self) -> String {
        format!(
            "https://api-users.4jawaly.com/api/v1/whatsapp/{}",
            self.project_id
        )
    }
}

/// إرسال طلب إلى API وطباعة النتيجة
/// Send request to API and print response
/// API کو درخواست بھیجیں اور جواب پرنٹ کریں
pub fn make_api_call(config: &Config, data: Value) -> Result<(), Box<dyn std::error::Error>> {
    let url = config.base_url();
    let auth = config.auth_header();

    // بناء الجسم المغلف - Build wrapped request body - ریگوئسٹ باڈی بنائیں
    let payload = serde_json::json!({
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": data
        }
    });

    let client = Client::new();
    let response = client
        .post(&url)
        .header("Content-Type", "application/json")
        .header("Authorization", &auth)
        .json(&payload)
        .send()?;

    let status = response.status();
    let body = response.text()?;

    // طباعة رمز الاستجابة والجسم
    // Print response status and body
    // جوابی کوڈ اور باڈی پرنٹ کریں
    println!(
        "رمز الاستجابة / Response code / جوابی کوڈ: {}",
        status
    );

    match serde_json::from_str::<Value>(&body) {
        Ok(parsed) => println!(
            "\nالاستجابة / Response / جواب:\n{}",
            serde_json::to_string_pretty(&parsed).unwrap_or_default()
        ),
        Err(_) => println!("\nالنص الخام / Raw body / خام متن:\n{}", body),
    }

    Ok(())
}
