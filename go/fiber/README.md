# 4Jawaly WhatsApp API - Go Fiber Samples
# عينات واتساب 4Jawaly - إطار Fiber
# 4Jawaly WhatsApp API - Fiber فریم ورک نمونے

Samples using **Fiber** web framework with HTTP routes.
عينات باستخدام **Fiber** مع مسارات HTTP.
**Fiber** ویب فریم ورک کے ساتھ نمونے۔

## Installation / التثبيت / انسٹالیشن

```bash
go mod download
```

## Environment Setup / إعداد البيئة / ماحولیاتی سیٹ اپ

Set environment variables / ضبط متغيرات البيئة / ماحولیاتی متغیرات سیٹ کریں:

```bash
export APP_KEY=your_app_key
export API_SECRET=your_api_secret
export PROJECT_ID=your_project_id
export RECIPIENT=9665XXXXXXXX
export PORT=8080
```

## Run / التشغيل / چلائیں

```bash
go run main.go whatsapp_service.go
# or
go run .
```

Server runs on `:8080` by default.

## API Routes / مسارات API / API راستے

| Method | Route | Description |
|--------|-------|-------------|
| POST | /whatsapp/text | إرسال رسالة نصية / Send text |
| POST | /whatsapp/buttons | إرسال أزرار تفاعلية / Send buttons |
| POST | /whatsapp/list | إرسال قائمة تفاعلية / Send list |
| POST | /whatsapp/image | إرسال صورة / Send image |
| POST | /whatsapp/video | إرسال فيديو / Send video |
| POST | /whatsapp/audio | إرسال ملف صوتي / Send audio |
| POST | /whatsapp/document | إرسال مستند / Send document |

## cURL Examples / أمثلة cURL / cURL مثالیں

### Text
```bash
curl -X POST http://localhost:8080/whatsapp/text \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","text":"مرحبا"}'
```

### Buttons
```bash
curl -X POST http://localhost:8080/whatsapp/buttons \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","body":"اختر أحد الخيارات","buttons":[{"type":"reply","reply":{"id":"btn_yes","title":"نعم"}}]}'
```

### List
```bash
curl -X POST http://localhost:8080/whatsapp/list \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","header":"قائمة الخدمات","body":"اختر الخدمة","button":"عرض القائمة"}'
```

### Image
```bash
curl -X POST http://localhost:8080/whatsapp/image \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/image.jpg","caption":"وصف الصورة"}'
```

### Video
```bash
curl -X POST http://localhost:8080/whatsapp/video \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/video.mp4","caption":"وصف الفيديو"}'
```

### Audio
```bash
curl -X POST http://localhost:8080/whatsapp/audio \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/audio.mp3"}'
```

### Document
```bash
curl -X POST http://localhost:8080/whatsapp/document \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","link":"https://example.com/document.pdf","caption":"وصف المستند","filename":"document.pdf"}'
```

Request body can override `to` and message content per request.
