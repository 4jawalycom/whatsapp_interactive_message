# نماذج كوتلين لإرسال رسائل واتساب باستخدام OkHttp

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Kotlin لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Kotlin - WhatsApp 4Jawaly.md`](../ai-reference/Kotlin%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Kotlin reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Kotlin - WhatsApp 4Jawaly.md`](../ai-reference/Kotlin%20-%20WhatsApp%204Jawaly.md)

# Kotlin Samples for WhatsApp Interactive Messages using OkHttp
# OkHttp استعمال کرتے ہوئے واٹس ایپ میسجز کے لیے Kotlin نمونے

## الوصف / Description / تفصیل

هذا المجلد يحتوي على نماذج Kotlin قائمة بذاتها لإرسال رسائل واتساب عبر واجهة 4Jawaly API باستخدام مكتبة OkHttp.

This folder contains standalone Kotlin samples for sending WhatsApp messages via the 4Jawaly API using the OkHttp library.

اس فولڈر میں 4Jawaly API کے ذریعے واٹس ایپ میسجز بھیجنے کے لیے OkHttp لائبریری استعمال کرتے ہوئے خودمختار Kotlin نمونے شامل ہیں۔

## الملفات / Files / فائلیں

| الملف | الوظيفة | File | Purpose |
|-------|----------|------|---------|
| `SendText.kt` | إرسال رسالة نصية | SendText.kt | Send text message |
| `SendButtons.kt` | إرسال رسالة بأزرار تفاعلية | SendButtons.kt | Send interactive buttons message |
| `SendList.kt` | إرسال رسالة بقائمة تفاعلية | SendList.kt | Send interactive list message |
| `SendImage.kt` | إرسال صورة | SendImage.kt | Send image |
| `SendVideo.kt` | إرسال فيديو | SendVideo.kt | Send video |
| `SendAudio.kt` | إرسال ملف صوتي | SendAudio.kt | Send audio file |
| `SendDocument.kt` | إرسال مستند | SendDocument.kt | Send document |

## كيفية التشغيل / How to Run / کیسے چلائیں

1. قم بتعديل الثوابت في بداية كل ملف:
   - `APP_KEY` - مفتاح التطبيق
   - `API_SECRET` - السر السري
   - `PROJECT_ID` - معرف المشروع
   - `RECIPIENT` - رقم المستلم (مثال: 9665XXXXXXXX)

2. إنشاء Gradle Wrapper (إذا لم يكن موجوداً):
   ```bash
   gradle wrapper
   ```

3. تشغيل المشروع:
   ```bash
   ./gradlew run -PmainClass=SendTextKt
   ./gradlew run -PmainClass=SendButtonsKt
   ./gradlew run -PmainClass=SendListKt
   ./gradlew run -PmainClass=SendImageKt
   ./gradlew run -PmainClass=SendVideoKt
   ./gradlew run -PmainClass=SendAudioKt
   ./gradlew run -PmainClass=SendDocumentKt
   ```

1. Edit the constants at the top of each file:
   - `APP_KEY` - Application key
   - `API_SECRET` - API secret
   - `PROJECT_ID` - Project ID
   - `RECIPIENT` - Recipient number (e.g., 9665XXXXXXXX)

2. Generate Gradle Wrapper (if not present):
   ```bash
   gradle wrapper
   ```

3. Run the project:
   ```bash
   ./gradlew run -PmainClass=SendTextKt
   ./gradlew run -PmainClass=SendButtonsKt
   # ... etc
   ```

## المتطلبات / Requirements / ضروریات

- Kotlin 1.8+
- Kotlin 1.8 or above
- Kotlin 1.8 یا اس سے اوپر
- JVM 11+
- OkHttp
- org.json
