# 4Jawaly WhatsApp API - FastAPI

# واتساب 4Jawaly API - FastAPI

# 4Jawaly واٹس ایپ API - FastAPI

---

إرسال رسائل واتساب عبر 4Jawaly API باستخدام Python FastAPI  
Send WhatsApp messages via 4Jawaly API using Python FastAPI  
4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کے لیے Python FastAPI استعمال کریں

## التثبيت | Installation | تنصیب

```bash
cd temp/python/fastapi
pip install -r requirements.txt
```

## إعداد المتغيرات البيئية | Environment Variables | ماحولیاتی متغیرات

```bash
export APP_KEY="your_app_key"
export API_SECRET="your_api_secret"
export PROJECT_ID="your_project_id"
```

## تشغيل التطبيق | Run the Application | ایپ چلائیں

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

أو | Or | یا:

```bash
python main.py
```

## التوثيق التلقائي | Auto-generated Documentation | خودکار دستاویزات

- **Swagger UI**: http://localhost:8000/docs  
- **ReDoc**: http://localhost:8000/redoc  
- **OpenAPI JSON**: http://localhost:8000/openapi.json  

FastAPI يولّد توثيق API تفاعلياً تلقائياً  
FastAPI auto-generates interactive API documentation  
FastAPI خودکار طور پر تفاعلی API دستاویزات بناتا ہے

---

## مسارات API | API Endpoints | API اینڈ پوائنٹس

| Method | Endpoint | الوصف | Description |
|--------|----------|-------|-------------|
| POST | `/whatsapp/text` | رسالة نصية | Text message |
| POST | `/whatsapp/buttons` | أزرار تفاعلية | Interactive buttons |
| POST | `/whatsapp/list` | قائمة تفاعلية | Interactive list |
| POST | `/whatsapp/image` | صورة | Image |
| POST | `/whatsapp/video` | فيديو | Video |
| POST | `/whatsapp/audio` | ملف صوتي | Audio |
| POST | `/whatsapp/document` | مستند | Document |

---

## أمثلة cURL | cURL Examples | cURL مثالیں

### 1. Text - رسالة نصية - ٹیکسٹ

```bash
curl -X POST http://localhost:8000/whatsapp/text \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","body":"نص الرسالة"}'
```

### 2. Interactive Buttons - أزرار تفاعلية - بٹن

```bash
curl -X POST http://localhost:8000/whatsapp/buttons \
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

### 3. Interactive List - قائمة تفاعلية - لسٹ

```bash
curl -X POST http://localhost:8000/whatsapp/list \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "header_text":"قائمة الخدمات",
    "body_text":"اختر الخدمة المطلوبة من القائمة أدناه",
    "footer_text":"4Jawaly Services",
    "button_label":"عرض القائمة",
    "sections":[
      {
        "title":"الخدمات الأساسية",
        "rows":[
          {"id":"svc_sms","title":"خدمة الرسائل النصية","description":"إرسال رسائل SMS للعملاء"},
          {"id":"svc_whatsapp","title":"خدمة واتساب","description":"إرسال رسائل واتساب تفاعلية"}
        ]
      },
      {
        "title":"الدعم الفني",
        "rows":[
          {"id":"support_ticket","title":"فتح تذكرة دعم","description":"تواصل مع فريق الدعم الفني"}
        ]
      }
    ]
  }'
```

### 4. Image - صورة - تصویر

```bash
curl -X POST http://localhost:8000/whatsapp/image \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "link":"https://example.com/image.jpg",
    "caption":"وصف الصورة"
  }'
```

### 5. Video - فيديو - ویڈیو

```bash
curl -X POST http://localhost:8000/whatsapp/video \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "link":"https://example.com/video.mp4",
    "caption":"وصف الفيديو"
  }'
```

### 6. Audio - ملف صوتي - آڈیو

```bash
curl -X POST http://localhost:8000/whatsapp/audio \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/audio.mp3"}'
```

### 7. Document - مستند - دستاویز

```bash
curl -X POST http://localhost:8000/whatsapp/document \
  -H "Content-Type: application/json" \
  -d '{
    "to":"9665XXXXXXXX",
    "link":"https://example.com/document.pdf",
    "caption":"وصف المستند",
    "filename":"document.pdf"
  }'
```

---

## مواصفات API | API Specification

- **Base URL**: `https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}`
- **Method**: POST
- **Auth**: Basic Auth (base64(app_key:api_secret))
- **Content-Type**: application/json

---

## هيكل الملفات | File Structure | فائل کی ساخت

```
fastapi/
├── main.py              # FastAPI app + routes + Pydantic models
├── whatsapp_service.py  # Async service (httpx)
├── requirements.txt
└── README.md
```
