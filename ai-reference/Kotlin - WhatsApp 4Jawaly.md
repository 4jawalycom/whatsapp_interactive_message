# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Kotlin باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Kotlin using 4Jawaly

## معلومات API | API Information
- Base URL: https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
- Method: POST
- Auth: Basic Auth (base64(app_key:api_secret))
- Content-Type: application/json

## أنواع الرسائل المدعومة | Supported Message Types
1. رسالة نصية (Text)
2. أزرار تفاعلية (Interactive Buttons) - حتى 3 أزرار
3. قائمة تفاعلية (Interactive List) - حتى 10 عناصر
4. صورة (Image)
5. فيديو (Video)
6. ملف صوتي (Audio)
7. مستند (Document)
8. موقع جغرافي (Location)
9. جهة اتصال (Contact)

---

## التبعيات | build.gradle.kts
```kotlin
// إعداد مشروع Gradle - Gradle project config - Gradle پروجیکٹ کنفیگریشن
plugins {
    kotlin("jvm") version "1.9.22"
    application
}

group = "com.4jawaly"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("org.json:json:20240303")
}

kotlin {
    jvmToolchain(11)
}

application {
    mainClass.set("SendTextKt")
}
```

## الإعدادات | settings.gradle.kts
```kotlin
rootProject.name = "whatsapp-kotlin-samples"
```

## إرسال رسالة نصية | SendText.kt
```kotlin
// إرسال رسالة نصية عبر واتساب
// Send text message via WhatsApp
// واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں

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

// محتوى الرسالة - Message content - پیغام کا مواد
private const val MESSAGE_BODY = "نص الرسالة"

fun main() {
    // إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء جسم الطلب - Build request body - درخواست کا جسم بنائیں
        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "text")
            put("text", JSONObject().put("body", MESSAGE_BODY))
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
```

## إرسال أزرار تفاعلية | SendButtons.kt
```kotlin
// إرسال رسالة بأزرار تفاعلية عبر واتساب
// Send interactive buttons message via WhatsApp
// واٹس ایپ کے ذریعے انٹرایکٹو بٹن پیغام بھیجیں

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
    // إرسال رسالة أزرار - Send buttons message - بٹن پیغام بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء أزرار التفاعل - Build interactive buttons - انٹرایکٹو بٹن بنائیں
        val buttons = JSONArray()
            .put(JSONObject().apply {
                put("type", "reply")
                put("reply", JSONObject().apply {
                    put("id", "btn_yes")
                    put("title", "نعم")
                })
            })
            .put(JSONObject().apply {
                put("type", "reply")
                put("reply", JSONObject().apply {
                    put("id", "btn_no")
                    put("title", "لا")
                })
            })
            .put(JSONObject().apply {
                put("type", "reply")
                put("reply", JSONObject().apply {
                    put("id", "btn_help")
                    put("title", "مساعدة")
                })
            })

        val interactive = JSONObject().apply {
            put("type", "button")
            put("body", JSONObject().put("text", "اختر أحد الخيارات التالية"))
            put("action", JSONObject().put("buttons", buttons))
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
```

## إرسال قائمة تفاعلية | SendList.kt
```kotlin
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
```

## إرسال صورة | SendImage.kt
```kotlin
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
```

## إرسال موقع جغرافي | SendLocation.kt
```kotlin
// إرسال موقع جغرافي عبر واتساب - Send location via WhatsApp
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.util.Base64

private const val APP_KEY = "your_app_key"
private const val API_SECRET = "your_api_secret"
private const val PROJECT_ID = "your_project_id"
private const val RECIPIENT = "966500000000"
private const val LAT = 24.7136
private const val LNG = 46.6753
private const val ADDRESS = "Riyadh, Saudi Arabia"
private const val NAME = "My Office"

fun main() {
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authB64 = Base64.getEncoder().encodeToString("$APP_KEY:$API_SECRET".toByteArray(Charsets.UTF_8))
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
            println("رمز الاستجابة / Response code: ${response.code}")
            println("\nالاستجابة / Response:\n${response.body?.string() ?: ""}")
        }
    } catch (e: Exception) {
        println("خطأ / Error: ${e.message}")
        e.printStackTrace()
    }
}
```

## إرسال جهة اتصال | SendContact.kt
```kotlin
// إرسال جهة اتصال عبر واتساب - Send contact via WhatsApp
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONArray
import org.json.JSONObject
import java.util.Base64

private const val APP_KEY = "your_app_key"
private const val API_SECRET = "your_api_secret"
private const val PROJECT_ID = "your_project_id"
private const val RECIPIENT = "966500000000"

fun main() {
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authB64 = Base64.getEncoder().encodeToString("$APP_KEY:$API_SECRET".toByteArray(Charsets.UTF_8))
        val nameObj = JSONObject().apply {
            put("formatted_name", "Ahmed Ali")
            put("first_name", "Ahmed")
            put("last_name", "Ali")
        }
        val phoneObj = JSONObject().apply {
            put("phone", "+966501234567")
            put("type", "CELL")
        }
        val contactObj = JSONObject().apply {
            put("name", nameObj)
            put("phones", JSONArray().apply { put(phoneObj) })
        }
        val params = JSONObject().apply {
            put("phone", RECIPIENT)
            put("contacts", JSONArray().apply { put(contactObj) })
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
            println("رمز الاستجابة / Response code: ${response.code}")
            println("\nالاستجابة / Response:\n${response.body?.string() ?: ""}")
        }
    } catch (e: Exception) {
        println("خطأ / Error: ${e.message}")
        e.printStackTrace()
    }
}
```

## إرسال فيديو | SendVideo.kt
```kotlin
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
```

## إرسال ملف صوتي | SendAudio.kt
```kotlin
// إرسال ملف صوتي عبر واتساب
// Send audio file via WhatsApp
// واٹس ایپ کے ذریعے آڈیو فائل بھیجیں

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

// رابط الملف الصوتي - Audio file URL - آڈیو فائل کا لنک
private const val AUDIO_URL = "https://example.com/audio.mp3"

fun main() {
    // إرسال ملف صوتي - Send audio - آڈیو بھیجیں
    try {
        val url = "https://api-users.4jawaly.com/api/v1/whatsapp/$PROJECT_ID"
        val authString = "$APP_KEY:$API_SECRET"
        val authB64 = Base64.getEncoder().encodeToString(authString.toByteArray(Charsets.UTF_8))

        // بناء كائن الصوت - Build audio object - آڈیو آبجیکٹ بنائیں
        val audio = JSONObject().put("link", AUDIO_URL)

        val data = JSONObject().apply {
            put("messaging_product", "whatsapp")
            put("to", RECIPIENT)
            put("type", "audio")
            put("audio", audio)
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
```

## إرسال مستند | SendDocument.kt
```kotlin
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
```
