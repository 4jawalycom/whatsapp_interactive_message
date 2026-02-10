# 4Jawaly WhatsApp API - Flutter/Dart

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Flutter/Dart لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Flutter - WhatsApp 4Jawaly.md`](../ai-reference/Flutter%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Flutter/Dart reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Flutter - WhatsApp 4Jawaly.md`](../ai-reference/Flutter%20-%20WhatsApp%204Jawaly.md)

Flutter/Dart client for 4Jawaly WhatsApp API using the `http` package.

عميل Flutter/Dart لواجهة واتساب 4جوالي | 4Jawaly WhatsApp API کا Flutter/Dart کلائنٹ

---

## Installation | التثبيت | انسٹالیشن

Add the `http` dependency to your `pubspec.yaml`:

```yaml
dependencies:
  http: ^1.1.0
```

Then run:

```bash
flutter pub get
# or
dart pub get
```

---

## Configuration | الإعداد | ترتیب

Create a `WhatsAppService` instance with your credentials:

```dart
final whatsapp = WhatsAppService(
  appKey: 'YOUR_APP_KEY',
  apiSecret: 'YOUR_API_SECRET',
  projectId: 'YOUR_PROJECT_ID',
);
```

---

## API Reference | مرجع الواجهة | API حوالہ

### Base URL
```
https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
```

### Authentication | المصادقة | توثیق
- **Method:** POST
- **Auth:** Basic Auth header with `base64(app_key:api_secret)`
- **Content-Type:** application/json

### Request Body Wrapper
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "9665XXXXXXXX",
      "type": "<type>",
      ...
    }
  }
}
```

---

## Message Types | أنواع الرسائل | میسج کی اقسام

### 1. Text Message | رسالة نصية | ٹیکسٹ میسج

```dart
final result = await whatsapp.sendText('9665XXXXXXXX', 'نص الرسالة');
```

### 2. Interactive Buttons | أزرار تفاعلية | تفاعلی بٹن

```dart
final result = await whatsapp.sendButtons(
  '9665XXXXXXXX',
  'اختر أحد الخيارات التالية',
  [
    {'id': 'btn_yes', 'title': 'نعم'},
    {'id': 'btn_no', 'title': 'لا'},
    {'id': 'btn_help', 'title': 'مساعدة'},
  ],
);
```

### 3. Interactive List | قائمة تفاعلية | تفاعلی فہرست

```dart
final result = await whatsapp.sendList(
  '9665XXXXXXXX',
  headerText: 'قائمة الخدمات',
  bodyText: 'اختر الخدمة المطلوبة من القائمة أدناه',
  footerText: '4Jawaly Services',
  buttonText: 'عرض القائمة',
  sections: [
    {
      'title': 'الخدمات الأساسية',
      'rows': [
        {
          'id': 'svc_sms',
          'title': 'خدمة الرسائل النصية',
          'description': 'إرسال رسائل SMS للعملاء',
        },
        {
          'id': 'svc_whatsapp',
          'title': 'خدمة واتساب',
          'description': 'إرسال رسائل واتساب تفاعلية',
        },
      ],
    },
    {
      'title': 'الدعم الفني',
      'rows': [
        {
          'id': 'support_ticket',
          'title': 'فتح تذكرة دعم',
          'description': 'تواصل مع فريق الدعم الفني',
        },
      ],
    },
  ],
);
```

### 4. Image | صورة | تصویر

```dart
final result = await whatsapp.sendImage(
  '9665XXXXXXXX',
  'https://example.com/image.jpg',
  caption: 'وصف الصورة',
);
```

### 5. Video | فيديو | ویڈیو

```dart
final result = await whatsapp.sendVideo(
  '9665XXXXXXXX',
  'https://example.com/video.mp4',
  caption: 'وصف الفيديو',
);
```

### 6. Audio | ملف صوتي | آڈیو

```dart
final result = await whatsapp.sendAudio('9665XXXXXXXX', 'https://example.com/audio.mp3');
```

### 7. Document | مستند | دستاویز

```dart
final result = await whatsapp.sendDocument(
  '9665XXXXXXXX',
  'https://example.com/document.pdf',
  caption: 'وصف المستند',
  filename: 'document.pdf',
);
```

---

## Response Format | تنسيق الاستجابة | جواب کی شکل

Each method returns `Future<Map<String, dynamic>>`:

**Success:**
```dart
{
  'statusCode': 200,
  'body': { ... }  // API response
}
```

**Error:**
```dart
{
  'error': true,
  'message': 'Error description'
}
```

---

## Run Example | تشغيل المثال | مثال چلائیں

```bash
dart run example_usage.dart
```

---

## Files | الملفات | فائلیں

| File | Description |
|------|-------------|
| `whatsapp_service.dart` | Main service class with all 7 methods |
| `example_usage.dart` | Usage examples for each method |
| `pubspec.yaml` | Dependencies (http) |

---

## License | الترخيص | لائسنس

4Jawaly ©
