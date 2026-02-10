// إرسال صورة عبر واتساب
// Send image via WhatsApp
// واٹس ایپ کے ذریعے تصویر بھیجیں

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

// رابط الصورة والوصف - Image URL and caption - تصویر کا لنک اور کیپشن
private const val IMAGE_URL = "https://example.com/image.jpg"
private const val IMAGE_CAPTION = "وصف الصورة"

fun main() {
    // إرسال صورة - Send image - تصویر بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء كائن الصورة - Build image object - تصویر آبجیکٹ بنائیں
        val image = JSONObject().apply {
            put("link", IMAGE_URL)
            put("caption", IMAGE_CAPTION)
        }

        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "image")
            put("image", image)
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
