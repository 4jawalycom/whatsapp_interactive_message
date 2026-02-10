# 4Jawaly WhatsApp API - Go Gin Samples  

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Go لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Go - WhatsApp 4Jawaly.md`](../../ai-reference/Go%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Go reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Go - WhatsApp 4Jawaly.md`](../../ai-reference/Go%20-%20WhatsApp%204Jawaly.md)

# عينات واتساب 4Jawaly - إطار Gin  
# 4Jawaly WhatsApp API - Gin فریم ورک نمونے

Samples using **Gin** web framework with HTTP routes.  
عينات باستخدام **Gin** مع مسارات HTTP.  
**Gin** ویب فریم ورک کے ساتھ نمونے۔

## Setup / الإعداد / سیٹ اپ

```bash
go mod download
```

Set environment variables / ضبط متغيرات البيئة / ماحولیاتی متغیرات سیٹ کریں:

```bash
export APP_KEY=your_app_key
export API_SECRET=your_api_secret
export PROJECT_ID=your_project_id
export RECIPIENT=9665XXXXXXXX
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

## Example Request / مثال طلب / درخواست مثال

```bash
curl -X POST http://localhost:8080/whatsapp/text \
  -H "Content-Type: application/json" \
  -d '{"to":"9665XXXXXXXX","text":"مرحبا"}'
```

Request body can override `to` and message content per request.
