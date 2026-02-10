# نماذج PHP التقليدية لإرسال رسائل واتساب تفاعلية
# PHP Legacy (5.6/7.x) Samples for WhatsApp Interactive Messages
# واٹس ایپ انٹرایکٹو میسجز کے لیے پرانی PHP نمونے

## الوصف / Description / تفصیل

هذا المجلد يحتوي على نماذج PHP تقليدية متوافقة مع الإصدارات 5.6 و 7.x لإرسال رسائل واتساب عبر واجهة 4Jawaly API.

This folder contains legacy PHP samples compatible with versions 5.6 and 7.x for sending WhatsApp messages via the 4Jawaly API.

اس فولڈر میں واٹس ایپ میسجز بھیجنے کے لیے 4Jawaly API کے ذریعے ورژن 5.6 اور 7.x کے ساتھ مطابقت رکھنے والے پرانے PHP نمونے شامل ہیں۔

## الملفات / Files / فائلیں

| الملف | الوظيفة | File | Purpose |
|-------|----------|------|---------|
| `send_text.php` | إرسال رسالة نصية | send_text.php | Send text message |
| `send_buttons.php` | إرسال رسالة بها أزرار تفاعلية | send_buttons.php | Send interactive buttons message |
| `send_list.php` | إرسال رسالة بقائمة تفاعلية | send_list.php | Send interactive list message |
| `send_image.php` | إرسال صورة | send_image.php | Send image |
| `send_video.php` | إرسال فيديو | send_video.php | Send video |
| `send_audio.php` | إرسال ملف صوتي | send_audio.php | Send audio file |
| `send_document.php` | إرسال مستند | send_document.php | Send document |

## كيفية التشغيل / How to Run / کیسے چلائیں

1. قم بتعديل المتغيرات في بداية كل ملف:
   - `$app_key` - مفتاح التطبيق
   - `$api_secret` - السر السري
   - `$project_id` - معرف المشروع
   - `$recipient` - رقم المستلم (مثال: 9665XXXXXXXX)

2. تشغيل الملف من سطر الأوامر:
   ```bash
   php send_text.php
   ```

1. Edit the variables at the top of each file:
   - `$app_key` - Application key
   - `$api_secret` - API secret
   - `$project_id` - Project ID
   - `$recipient` - Recipient number (e.g., 9665XXXXXXXX)

2. Run the file from the command line:
   ```bash
   php send_text.php
   ```

## المتطلبات / Requirements / ضروریات

- PHP 5.6 أو أحدث (متوافق مع 7.x)
- PHP 5.6 or above (compatible with 7.x)
- PHP 5.6 یا اس سے اوپر (7.x کے ساتھ مطابقت رکھتا ہے)
- امتداد cURL مُمكّن
- cURL extension enabled
- cURL ایکسٹینشن فعال
