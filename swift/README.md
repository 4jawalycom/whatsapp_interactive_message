# 4Jawaly WhatsApp API - Swift URLSession Samples
# عينات واتساب 4Jawaly - Swift URLSession
# 4Jawaly WhatsApp API - Swift URLSession نمونے

Samples using **Swift Foundation** (`URLSession`, `JSONSerialization`, etc.) only.  
عينات باستخدام **Foundation** فقط.  
صرف **Foundation** استعمال کرتے ہوئے نمونے۔

## Setup / الإعداد / سیٹ اپ

1. Ensure Swift 5.9+ is installed / تأكد من تثبيت Swift 5.9+ / Swift 5.9+ انسٹال کریں
2. Edit config variables at top of each file: `appKey`, `apiSecret`, `projectId`, `recipient`

## Run / التشغيل / چلائیں

```bash
swift send_text.swift
swift send_buttons.swift
swift send_list.swift
swift send_image.swift
swift send_video.swift
swift send_audio.swift
swift send_document.swift
```

## Files / الملفات / فائلیں

| File | Description |
|------|-------------|
| send_text.swift | إرسال رسالة نصية / Send text message / ٹیکسٹ میسج بھیجیں |
| send_buttons.swift | إرسال أزرار تفاعلية / Send interactive buttons / انٹرایکٹو بٹن بھیجیں |
| send_list.swift | إرسال قائمة تفاعلية / Send interactive list / انٹرایکٹو لسٹ بھیجیں |
| send_image.swift | إرسال صورة / Send image / تصویر بھیجیں |
| send_video.swift | إرسال فيديو / Send video / ویڈیو بھیجیں |
| send_audio.swift | إرسال ملف صوتي / Send audio / آڈیو بھیجیں |
| send_document.swift | إرسال مستند / Send document / دستاویز بھیجیں |

## API Base URL / عنوان الاتصال / API بیس یوآرایل

```
https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
```

Auth: Basic Auth with base64(app_key:api_secret)
