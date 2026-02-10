// إرسال فيديو عبر واتساب
// Send video via WhatsApp
// واٹس ایپ کے ذریعے ویڈیو بھیجیں

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

// رابط الفيديو والوصف - Video URL and caption - ویڈیو کا لنک اور کیپشن
private const val VIDEO_URL = "https://example.com/video.mp4"
private const val VIDEO_CAPTION = "وصف الفيديو"

fun main() {
    // إرسال فيديو - Send video - ویڈیو بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء كائن الفيديو - Build video object - ویڈیو آبجیکٹ بنائیں
        val video = JSONObject().apply {
            put("link", VIDEO_URL)
            put("caption", VIDEO_CAPTION)
        }

        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "video")
            put("video", video)
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
