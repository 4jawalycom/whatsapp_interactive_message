# نماذج برمجية لإرسال رسائل واتساب التفاعلية - 4Jawaly API
# WhatsApp Interactive Message Code Samples - 4Jawaly API
# واٹس ایپ انٹرایکٹو پیغام کوڈ سیمپلز - 4Jawaly API

---

## نظرة عامة | Overview | جائزہ

هذا المستودع يحتوي على نماذج برمجية جاهزة للاستخدام لإرسال رسائل واتساب عبر [4Jawaly API](https://www.4jawaly.com) بعدة لغات برمجة وفريموركات.

This repository contains ready-to-use code samples for sending WhatsApp messages via the [4Jawaly API](https://www.4jawaly.com) in multiple programming languages and frameworks.

---

## أنواع الرسائل المدعومة | Supported Message Types | معاون پیغام کی اقسام

| # | النوع | Type | قسم |
|---|-------|------|------|
| 1 | رسالة نصية | Text Message | ٹیکسٹ پیغام |
| 2 | أزرار تفاعلية | Interactive Buttons | انٹرایکٹو بٹن |
| 3 | قائمة تفاعلية | Interactive List | انٹرایکٹو لسٹ |
| 4 | صورة | Image | تصویر |
| 5 | فيديو | Video | ویڈیو |
| 6 | ملف صوتي | Audio | آڈیو |
| 7 | مستند | Document | دستاویز |

---

## اللغات والفريموركات المتاحة | Available Languages & Frameworks

### PHP
| المجلد | الوصف | الإصدار |
|--------|-------|---------|
| [`php/modern/`](php/modern/) | PHP حديث مع cURL | PHP 8.x+ |
| [`php/legacy/`](php/legacy/) | PHP متوافق مع الإصدارات القديمة | PHP 5.6 / 7.x |
| [`php/lumen/`](php/lumen/) | Lumen Framework | Lumen 10.x |

### Python
| المجلد | الوصف | المتطلبات |
|--------|-------|-----------|
| [`python/requests/`](python/requests/) | مكتبة requests بدون فريموورك | Python 3.8+ |
| [`python/flask/`](python/flask/) | Flask Framework | Flask 3.x |
| [`python/django/`](python/django/) | Django Framework | Django 5.x |
| [`python/fastapi/`](python/fastapi/) | FastAPI Framework | FastAPI 0.110+ |

### Go
| المجلد | الوصف | المتطلبات |
|--------|-------|-----------|
| [`go/net_http/`](go/net_http/) | المكتبة القياسية net/http | Go 1.21+ |
| [`go/gin/`](go/gin/) | Gin Framework | Gin 1.9+ |
| [`go/fiber/`](go/fiber/) | Fiber Framework | Fiber v2 |
| [`go/echo/`](go/echo/) | Echo Framework | Echo v4 |

### لغات أخرى | Other Languages
| المجلد | الوصف | المتطلبات |
|--------|-------|-----------|
| [`rust/`](rust/) | Rust مع reqwest | Rust 1.75+ |
| [`ruby/`](ruby/) | Ruby مع net/http | Ruby 3.x |
| [`swift/`](swift/) | Swift مع URLSession | Swift 5.9+ |
| [`flutter/`](flutter/) | Flutter/Dart مع http package | Dart 3.x |
| [`kotlin/`](kotlin/) | Kotlin مع OkHttp | Kotlin 1.9+ |
| [`dotnet/`](dotnet/) | C# .NET مع HttpClient | .NET 8.0 |

---

## إعداد API | API Setup | API سیٹ اپ

### 1. الحصول على بيانات الاعتماد | Get Credentials

- `app_key` - مفتاح التطبيق من لوحة تحكم 4Jawaly
- `api_secret` - كلمة سر API من لوحة تحكم 4Jawaly  
- `project_id` - معرف مشروع واتساب من لوحة التحكم

### 2. Base URL

```
https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
```

### 3. المصادقة | Authentication

```
Authorization: Basic base64(app_key:api_secret)
```

### 4. هيكل الطلب | Request Structure

```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "9665XXXXXXXX",
      "type": "text|interactive|image|video|audio|document",
      "...": "حسب نوع الرسالة"
    }
  }
}
```

---

## ملاحظات مهمة | Important Notes | اہم نوٹس

1. **نافذة الـ 24 ساعة**: الرسائل التفاعلية (الأزرار والقوائم) تعمل فقط خلال 24 ساعة من بدء العميل للمحادثة.
2. **الروابط**: يجب أن تكون HTTPS مباشرة (بدون إعادة توجيه).
3. **الأزرار**: حد أقصى 3 أزرار لكل رسالة.
4. **القوائم**: حد أقصى 10 عناصر.
5. **حجم الملفات**: صوت/فيديو 16MB، مستندات 100MB.

---

## الدعم | Support | سپورٹ

- [موقع 4Jawaly](https://www.4jawaly.com)
- [لوحة التحكم](https://api-users.4jawaly.com)
- [التوثيق](https://docs.4jawaly.com)
