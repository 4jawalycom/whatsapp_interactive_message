// إرسال جهة اتصال عبر واتساب
// Send contact via WhatsApp
// واٹس ایپ کے ذریعے رابطہ بھیجیں

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
private const val RECIPIENT = "966500000000"

fun main() {
    // إرسال جهة اتصال - Send contact - رابطہ بھیجیں
    // هيكل مختلف: path message/contact مع params مباشرة
    // Different structure: path message/contact with direct params
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        val nameObj = JSONObject().apply {
            put("formatted_name", "Ahmed Ali")
            put("first_name", "Ahmed")
            put("last_name", "Ali")
        }
        val phoneObj = JSONObject().apply {
            put("phone", "+966501234567")
            put("type", "CELL")
        }
        val phonesArray = JSONArray().apply { put(phoneObj) }
        val contactObj = JSONObject().apply {
            put("name", nameObj)
            put("phones", phonesArray)
        }
        val contactsArray = JSONArray().apply { put(contactObj) }
        val params = JSONObject().apply {
            put("phone", RECIPIENT)
            put("contacts", contactsArray)
        }
        val payload = JSONObject().apply {
            put("path", "message/contact")
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
