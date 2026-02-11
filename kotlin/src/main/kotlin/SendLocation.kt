// إرسال موقع جغرافي عبر واتساب
// Send location via WhatsApp
// واٹس ایپ کے ذریعے مقام بھیجیں

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
private const val RECIPIENT = "966500000000"

// بيانات الموقع - Location data - مقام کا ڈیٹا
private const val LAT = 24.7136
private const val LNG = 46.6753
private const val ADDRESS = "Riyadh, Saudi Arabia"
private const val NAME = "My Office"

fun main() {
    // إرسال موقع جغرافي - Send location - مقام بھیجیں
    // هيكل مختلف: path message/location مع params مباشرة
    // Different structure: path message/location with direct params
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        val params = JSONObject().apply {
            put("phone", RECIPIENT)
            put("lat", LAT)
            put("lng", LNG)
            put("address", ADDRESS)
            put("name", NAME)
        }
        val payload = JSONObject().apply {
            put("path", "message/location")
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
