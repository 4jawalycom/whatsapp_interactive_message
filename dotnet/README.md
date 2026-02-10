# 4Jawaly WhatsApp API - .NET (C#) Sample

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد C# .NET لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/DotNet - WhatsApp 4Jawaly.md`](../ai-reference/DotNet%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete C# .NET reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/DotNet - WhatsApp 4Jawaly.md`](../ai-reference/DotNet%20-%20WhatsApp%204Jawaly.md)

## 4جوالية واتساب API - عينة .NET

## 4جوالی واٹس ایپ API - .NET نمونہ

---

## Overview / نظرة عامة / جائزہ

This sample demonstrates how to send WhatsApp messages via the 4Jawaly API using .NET 8 and `HttpClient`.

## Requirements / المتطلبات / ضروریات

- .NET 8.0 SDK

## Setup / الإعداد / سیٹ اپ

1. Restore packages:
   ```bash
   dotnet restore
   ```

2. Configure credentials in `Program.cs`:
   - `AppKey` - Your 4Jawaly App Key
   - `ApiSecret` - Your 4Jawaly API Secret
   - `ProjectId` - Your 4Jawaly Project ID
   - `Recipient` - Recipient phone number (e.g. `9665XXXXXXXX`)

## Run / التشغيل / چلائیں

```bash
dotnet run
```

## API Reference / مرجع API / API ریفرنس

### Base URL
```
https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
```

### Authentication / المصادقة / توثیق
- **Method:** Basic Auth
- **Header:** `Authorization: Basic base64(app_key:api_secret)`

### Supported Message Types / أنواع الرسائل المدعومة / سپورٹڈ میسج ٹائپس

| Type | Method | Description |
|------|--------|-------------|
| Text | `SendTextAsync` | Plain text message |
| Interactive Buttons | `SendButtonsAsync` | Up to 3 reply buttons |
| Interactive List | `SendListAsync` | Sections with rows |
| Image | `SendImageAsync` | Image with optional caption |
| Video | `SendVideoAsync` | Video with optional caption |
| Audio | `SendAudioAsync` | Audio file |
| Document | `SendDocumentAsync` | Document with optional caption and filename |

### Example Usage / مثال الاستخدام / استعمال کی مثال

```csharp
var service = new WhatsAppService(AppKey, ApiSecret, ProjectId);

// Text
await service.SendTextAsync(Recipient, "مرحبا!");

// Buttons
await service.SendButtonsAsync(Recipient, "اختر خياراً", new[] {
    ("yes", "نعم"), ("no", "لا")
});

// List
await service.SendListAsync(Recipient, "عرض", "المحتوى", "العنوان", "التذييل", sections);

// Media
await service.SendImageAsync(Recipient, "https://example.com/img.jpg", "وصف");
await service.SendVideoAsync(Recipient, "https://example.com/vid.mp4", "وصف");
await service.SendAudioAsync(Recipient, "https://example.com/audio.mp3");
await service.SendDocumentAsync(Recipient, "https://example.com/doc.pdf", "وصف", "doc.pdf");
```

## License / الترخيص / لائسنس

4Jawaly
