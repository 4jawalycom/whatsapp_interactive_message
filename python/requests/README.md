# نماذج بايثون لإرسال رسائل واتساب باستخدام requests
# Python Samples for WhatsApp Interactive Messages using requests
# واٹس ایپ انٹرایکٹو میسجز کے لیے requests استعمال کرتے ہوئے Python نمونے

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Python لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Python - WhatsApp 4Jawaly.md`](../../ai-reference/Python%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Python reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Python - WhatsApp 4Jawaly.md`](../../ai-reference/Python%20-%20WhatsApp%204Jawaly.md)

## الوصف / Description / تفصیل

هذا المجلد يحتوي على نماذج Python قائمة بذاتها لإرسال رسائل واتساب عبر واجهة 4Jawaly API باستخدام مكتبة requests بدون أي إطار عمل.

This folder contains standalone Python samples for sending WhatsApp messages via the 4Jawaly API using the requests library without any framework.

اس فولڈر میں 4Jawaly API کے ذریعے واٹس ایپ میسجز بھیجنے کے لیے requests لائبریری استعمال کرتے ہوئے کوئی فریم ورک کے بغیر خودمختار Python نمونے شامل ہیں۔

## الملفات / Files / فائلیں

| الملف | الوظيفة | File | Purpose |
|-------|----------|------|---------|
| `send_text.py` | إرسال رسالة نصية | send_text.py | Send text message |
| `send_buttons.py` | إرسال رسالة بها أزرار تفاعلية | send_buttons.py | Send interactive buttons message |
| `send_list.py` | إرسال رسالة بقائمة تفاعلية | send_list.py | Send interactive list message |
| `send_image.py` | إرسال صورة | send_image.py | Send image |
| `send_video.py` | إرسال فيديو | send_video.py | Send video |
| `send_audio.py` | إرسال ملف صوتي | send_audio.py | Send audio file |
| `send_document.py` | إرسال مستند | send_document.py | Send document |

## كيفية التشغيل / How to Run / کیسے چلائیں

1. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```

2. قم بتعديل المتغيرات في بداية كل ملف:
   - `APP_KEY` - مفتاح التطبيق
   - `API_SECRET` - السر السري
   - `PROJECT_ID` - معرف المشروع
   - `RECIPIENT` - رقم المستلم (مثال: 9665XXXXXXXX)

3. تشغيل الملف من سطر الأوامر:
   ```bash
   python send_text.py
   ```

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Edit the variables at the top of each file:
   - `APP_KEY` - Application key
   - `API_SECRET` - API secret
   - `PROJECT_ID` - Project ID
   - `RECIPIENT` - Recipient number (e.g., 9665XXXXXXXX)

3. Run the file from the command line:
   ```bash
   python send_text.py
   ```

## المتطلبات / Requirements / ضروریات

- Python 3.6 أو أحدث
- Python 3.6 or above
- Python 3.6 یا اس سے اوپر
- مكتبة requests
- requests library
- requests لائبریری
