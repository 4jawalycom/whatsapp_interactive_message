# Flask WhatsApp 4Jawaly API

# تطبيق Flask لإرسال رسائل واتساب عبر 4Jawaly API
# Flask app for sending WhatsApp messages via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کے لیے Flask ایپ

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Python لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Python - WhatsApp 4Jawaly.md`](../../ai-reference/Python%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Python reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Python - WhatsApp 4Jawaly.md`](../../ai-reference/Python%20-%20WhatsApp%204Jawaly.md)

---

## التثبيت - Installation - انسٹالیشن

```bash
# إنشاء بيئة افتراضية - Create virtual environment - ورچوئل ماحول بنائیں
python -m venv venv

# تفعيل البيئة - Activate environment - ماحول چالو کریں
# Linux/macOS:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# تثبيت المتطلبات - Install dependencies - ڈیپنڈنسیز انسٹال کریں
pip install -r requirements.txt
```

---

## إعداد المتغيرات - Environment Setup - ماحولیاتی ترتیبات

إنشاء ملف `.env` أو تصدير المتغيرات:

```bash
export APP_KEY="your_app_key"
export API_SECRET="your_api_secret"
export PROJECT_ID="your_project_id"
```

أو إنشاء ملف `.env` (استخدم `python-dotenv` إن رغبت):

```
APP_KEY=your_app_key
API_SECRET=your_api_secret
PROJECT_ID=your_project_id
```

---

## تشغيل التطبيق - Run Application - ایپ چلائیں

```bash
python app.py
```

الخادم سيعمل على: `http://127.0.0.1:5000`

---

## قائمة المسارات - Route List - روٹ کی فہرست

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/whatsapp/text` | إرسال رسالة نصية - Text message |
| POST | `/whatsapp/buttons` | إرسال أزرار تفاعلية - Interactive buttons |
| POST | `/whatsapp/list` | إرسال قائمة تفاعلية - Interactive list |
| POST | `/whatsapp/image` | إرسال صورة - Image |
| POST | `/whatsapp/video` | إرسال فيديو - Video |
| POST | `/whatsapp/audio` | إرسال ملف صوتي - Audio |
| POST | `/whatsapp/document` | إرسال مستند - Document |

---

## أمثلة curl - cURL Examples - curl کی مثالیں

### 1. Text Message - رسالة نصية - ٹیکسٹ پیغام

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/text \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","body":"نص الرسالة"}'
```

### 2. Interactive Buttons - أزرار تفاعلية - انٹرایکٹو بٹن

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/buttons \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "body_text":"اختر أحد الخيارات التالية",
    "buttons":[
      {"id":"btn_yes","title":"نعم"},
      {"id":"btn_no","title":"لا"},
      {"id":"btn_help","title":"مساعدة"}
    ]
  }'
```

### 3. Interactive List - قائمة تفاعلية - انٹرایکٹو لسٹ

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/list \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "header_text":"قائمة الخدمات",
    "body_text":"اختر الخدمة المطلوبة من القائمة أدناه",
    "footer_text":"4Jawaly Services",
    "button_label":"عرض القائمة",
    "sections":[
      {"title":"الخدمات الأساسية","rows":[
        {"id":"svc_sms","title":"خدمة الرسائل النصية","description":"إرسال رسائل SMS"},
        {"id":"svc_whatsapp","title":"خدمة واتساب","description":"إرسال رسائل واتساب"}
      ]},
      {"title":"الدعم الفني","rows":[
        {"id":"support_ticket","title":"فتح تذكرة دعم","description":"تواصل مع الدعم"}
      ]}
    ]
  }'
```

### 4. Image - صورة - تصویر

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/image \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/image.jpg","caption":"وصف الصورة"}'
```

### 5. Video - فيديو - ویڈیو

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/video \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/video.mp4","caption":"وصف الفيديو"}'
```

### 6. Audio - ملف صوتي - آڈیو

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/audio \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/audio.mp3"}'
```

### 7. Document - مستند - دستاویز

```bash
curl -X POST http://127.0.0.1:5000/whatsapp/document \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/document.pdf","caption":"وصف المستند","filename":"document.pdf"}'
```

---

## API 4Jawaly

- **Base URL:** `https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}`
- **Method:** POST
- **Auth:** Basic Auth (base64(app_key:api_secret))
- **Content-Type:** application/json
