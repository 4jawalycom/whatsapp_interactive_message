# نماذج روبي لإرسال رسائل واتساب باستخدام المكتبة القياسية
# Ruby Samples for WhatsApp Interactive Messages using Standard Library
# واٹس ایپ انٹرایکٹو میسجز کے لیے Standard Library استعمال کرتے ہوئے Ruby نمونے

## الوصف / Description / تفصیل

هذا المجلد يحتوي على نماذج Ruby قائمة بذاتها لإرسال رسائل واتساب عبر واجهة 4Jawaly API باستخدام المكتبة القياسية فقط (net/http, json, base64, uri) بدون أي gems خارجية.

This folder contains standalone Ruby samples for sending WhatsApp messages via the 4Jawaly API using only the standard library (net/http, json, base64, uri) without any external gems.

اس فولڈر میں 4Jawaly API کے ذریعے واٹس ایپ میسجز بھیجنے کے لیے صرف Standard Library استعمال کرتے ہوئے کوئی بیرونی gems کے بغیر خودمختار Ruby نمونے شامل ہیں۔

## الملفات / Files / فائلیں

| الملف | الوظيفة | File | Purpose |
|-------|----------|------|---------|
| `send_text.rb` | إرسال رسالة نصية | send_text.rb | Send text message |
| `send_buttons.rb` | إرسال رسالة بها أزرار تفاعلية | send_buttons.rb | Send interactive buttons message |
| `send_list.rb` | إرسال رسالة بقائمة تفاعلية | send_list.rb | Send interactive list message |
| `send_image.rb` | إرسال صورة | send_image.rb | Send image |
| `send_video.rb` | إرسال فيديو | send_video.rb | Send video |
| `send_audio.rb` | إرسال ملف صوتي | send_audio.rb | Send audio file |
| `send_document.rb` | إرسال مستند | send_document.rb | Send document |

## كيفية التشغيل / How to Run / کیسے چلائیں

1. قم بتعديل المتغيرات في بداية كل ملف:
   - `APP_KEY` - مفتاح التطبيق
   - `API_SECRET` - السر السري
   - `PROJECT_ID` - معرف المشروع
   - `RECIPIENT` - رقم المستلم (مثال: 9665XXXXXXXX)

2. تشغيل الملف من سطر الأوامر:
   ```bash
   ruby send_text.rb
   ```

1. Edit the variables at the top of each file:
   - `APP_KEY` - Application key
   - `API_SECRET` - API secret
   - `PROJECT_ID` - Project ID
   - `RECIPIENT` - Recipient number (e.g., 9665XXXXXXXX)

2. Run the file from the command line:
   ```bash
   ruby send_text.rb
   ```

2. کمانڈ لائن سے فائل چلائیں:
   ```bash
   ruby send_text.rb
   ```

## المتطلبات / Requirements / ضروریات

- Ruby 2.0 أو أحدث
- Ruby 2.0 or above
- Ruby 2.0 یا اس سے اوپر
- المكتبة القياسية فقط (لا حاجة لتثبيت gems)
- Standard library only (no gems to install)
- صرف Standard Library (gems انسٹال کرنے کی ضرورت نہیں)
