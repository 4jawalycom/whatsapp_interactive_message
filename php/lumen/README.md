# عينات رسائل واتساب لـ Lumen
> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد PHP لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/PHP - WhatsApp 4Jawaly.md`](../../ai-reference/PHP%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete PHP reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/PHP - WhatsApp 4Jawaly.md`](../../ai-reference/PHP%20-%20WhatsApp%204Jawaly.md)

# WhatsApp Message Samples for Lumen Framework

---

## التثبيت | Installation

### 1. إنشاء مشروع Lumen جديد | Create new Lumen project

```bash
composer create-project laravel/lumen my-whatsapp-app
cd my-whatsapp-app
```

### 2. تثبيت Guzzle HTTP | Install Guzzle HTTP

```bash
composer require guzzlehttp/guzzle
```

### 3. نسخ الملفات | Copy files

انسخ الملفات التالية إلى مشروعك:

Copy the following files into your project:

| الملف | المسار | File | Path |
|-------|--------|------|------|
| WhatsAppService.php | `app/Services/WhatsAppService.php` | | |
| WhatsAppController.php | `app/Http/Controllers/WhatsAppController.php` | | |
| routes.php | انسخ محتوى إلى `routes/web.php` أو استدعِه | Copy content to `routes/web.php` or require it | |

### 4. تسجيل الخدمة | Register service

في `bootstrap/app.php` أضف:

In `bootstrap/app.php` add:

```php
$app->singleton(App\Services\WhatsAppService::class, function ($app) {
    return new App\Services\WhatsAppService();
});
```

للمسارات، إن لم تكن موجودة في `routes/web.php`، أضف:

For routes, if not in `routes/web.php`, add:

```php
$app->router->group([], function ($router) {
    require __DIR__ . '/../temp/php/lumen/routes.php';
});
```

أو انسخ محتوى `routes.php` مباشرةً داخل `routes/web.php`.

Or copy the contents of `routes.php` directly into `routes/web.php`.

---

## الإعدادات | Configuration

### متغيرات البيئة | Environment variables

أضف إلى ملف `.env`:

Add to your `.env` file:

```env
# 4Jawaly WhatsApp API
APP_KEY=your_app_key
API_SECRET=your_api_secret
PROJECT_ID=your_project_id
```

| المتغير | الوصف | Variable | Description |
|---------|-------|----------|-------------|
| APP_KEY | مفتاح التطبيق من 4Jawaly | | Application key from 4Jawaly |
| API_SECRET | السر السري للـ API | | API secret |
| PROJECT_ID | معرف المشروع | | Project identifier |

---

## قائمة المسارات | Route List

| Method | المسار | النوع | Path | Type |
|--------|--------|------|------|------|
| POST | /whatsapp/text | نص | | Text |
| POST | /whatsapp/buttons | أزرار تفاعلية | | Interactive Buttons |
| POST | /whatsapp/list | قائمة تفاعلية | | Interactive List |
| POST | /whatsapp/image | صورة | | Image |
| POST | /whatsapp/video | فيديو | | Video |
| POST | /whatsapp/audio | صوت | | Audio |
| POST | /whatsapp/document | مستند | | Document |

---

## أمثلة الطلبات | Example Requests

استبدل `YOUR_BASE_URL` برابط تطبيقك (مثلاً `http://localhost:8000`).

Replace `YOUR_BASE_URL` with your app URL (e.g. `http://localhost:8000`).

### 1. إرسال رسالة نصية | Send text message

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/text" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "body": "نص الرسالة"
  }'
```

### 2. إرسال أزرار تفاعلية | Send interactive buttons

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/buttons" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "body": "اختر أحد الخيارات التالية",
    "buttons": [
      {"id": "btn_yes", "title": "نعم"},
      {"id": "btn_no", "title": "لا"},
      {"id": "btn_help", "title": "مساعدة"}
    ]
  }'
```

### 3. إرسال قائمة تفاعلية | Send interactive list

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/list" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "header": "قائمة الخدمات",
    "body": "اختر الخدمة المطلوبة من القائمة أدناه",
    "footer": "4Jawaly Services",
    "button": "عرض القائمة",
    "sections": [
      {
        "title": "الخدمات الأساسية",
        "rows": [
          {"id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"},
          {"id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"}
        ]
      },
      {
        "title": "الدعم الفني",
        "rows": [
          {"id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"}
        ]
      }
    ]
  }'
```

### 4. إرسال صورة | Send image

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/image" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "link": "https://example.com/image.jpg",
    "caption": "وصف الصورة"
  }'
```

### 5. إرسال فيديو | Send video

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/video" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "link": "https://example.com/video.mp4",
    "caption": "وصف الفيديو"
  }'
```

### 6. إرسال ملف صوتي | Send audio

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/audio" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "link": "https://example.com/audio.mp3"
  }'
```

### 7. إرسال مستند | Send document

```bash
curl -X POST "YOUR_BASE_URL/whatsapp/document" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "9665XXXXXXXX",
    "link": "https://example.com/document.pdf",
    "caption": "وصف المستند",
    "filename": "document.pdf"
  }'
```

---

## API 4Jawaly

- **Base URL:** `https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}`
- **Method:** POST
- **Auth:** Basic Auth (base64 من `app_key:api_secret`)

---

## هيكل المشروع | Project Structure

```
app/
├── Http/
│   └── Controllers/
│       └── WhatsAppController.php
└── Services/
    └── WhatsAppService.php
routes/
└── web.php  (أو routes.php)
```

---

## الترخيص | License

عينات لاستخدام 4Jawaly WhatsApp API | Samples for 4Jawaly WhatsApp API usage
