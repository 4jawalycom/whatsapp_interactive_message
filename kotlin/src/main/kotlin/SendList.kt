// إرسال رسالة بقائمة تفاعلية عبر واتساب
// Send interactive list message via WhatsApp
// واٹس ایپ کے ذریعے انٹرایکٹو لسٹ پیغام بھیجیں

import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONArray
import org.json.JSONObject
import java.util.Base64

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
private const val APP_KEY = "your_app_key"
private const val API_SECRET = "your_api_secret"
private const val PROJECT_ID = "your_project_id"
private const val RECIPIENT = "9665XXXXXXXX"

fun main() {
    // إرسال رسالة قائمة - Send list message - لسٹ پیغام بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء أقسام القائمة - Build list sections - لسٹ سیکشن بنائیں
        val section1Rows = JSONArray()
            .put(JSONObject().apply {
                put("id", "svc_sms")
                put("title", "خدمة الرسائل النصية")
                put("description", "إرسال رسائل SMS للعملاء")
            })
            .put(JSONObject().apply {
                put("id", "svc_whatsapp")
                put("title", "خدمة واتساب")
                put("description", "إرسال رسائل واتساب تفاعلية")
            })

        val section2Rows = JSONArray()
            .put(JSONObject().apply {
                put("id", "support_ticket")
                put("title", "فتح تذكرة دعم")
                put("description", "تواصل مع فريق الدعم الفني")
            })

        val sections = JSONArray()
            .put(JSONObject().apply {
                put("title", "الخدمات الأساسية")
                put("rows", section1Rows)
            })
            .put(JSONObject().apply {
                put("title", "الدعم الفني")
                put("rows", section2Rows)
            })

        val interactive = JSONObject().apply {
            put("type", "list")
            put("header", JSONObject().apply {
                put("type", "text")
                put("text", "قائمة الخدمات")
            })
            put("body", JSONObject().put("text", "اختر الخدمة المطلوبة من القائمة أدناه"))
            put("footer", JSONObject().put("text", "4Jawaly Services"))
            put("action", JSONObject().apply {
                put("button", "عرض القائمة")
                put("sections", sections)
            })
        }

        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "interactive")
            put("interactive", interactive)
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
