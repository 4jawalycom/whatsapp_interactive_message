// إرسال مستند عبر واتساب
// Send document via WhatsApp
// واٹس ایپ کے ذریعے دستاویز بھیجیں

import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.util.Base64

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
private const val APP_KEY = "your_app_key"
private const val API_SECRET = "your_api_secret"
private const val PROJECT_ID = "your_project_id"
private const val RECIPIENT = "9665XXXXXXXX"

// رابط المستند والوصف واسم الملف - Document URL, caption and filename - دستاویز کا لنک، کیپشن اور فائل کا نام
private const val DOCUMENT_URL = "https://example.com/document.pdf"
private const val DOCUMENT_CAPTION = "وصف المستند"
private const val DOCUMENT_FILENAME = "document.pdf"

fun main() {
    // إرسال مستند - Send document - دستاویز بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء كائن المستند - Build document object - دستاویز آبجیکٹ بنائیں
        val document = JSONObject().apply {
            put("link", DOCUMENT_URL)
            put("caption", DOCUMENT_CAPTION)
            put("filename", DOCUMENT_FILENAME)
        }

        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "document")
            put("document", document)
        }
        val params = JSONObject().apply {
            put("url", "messages")
            put("method", "post")
            put("data", data)
        }
        val payload = JSONObject().apply {
            put("path", "global")
            put("params", params)
        }

        val client = OkHttpClient()
        val request = Request.Builder()
            .url(url)
            .addHeader("Content-Type", "application/json")
            .addHeader("Authorization", "Basic $authB64")
            .post(payload.toString().toRequestBody("application/json".toMediaType()))
            .build()

        client.newCall(request).execute().use { response ->
            println("رمز الاستجابة / Response code / جوابی کوڈ: ${response.code}")
            println("\nالاستجابة / Response / جواب:\n${response.body?.string() ?: ""}")
        }
    } catch (e: Exception) {
        // خطأ في الاتصال - Connection error - رابطہ میں خرابی
        println("خطأ / Error / خرابی: ${e.message}")
        e.printStackTrace()
    }
}
