# 4Jawaly WhatsApp API - Go net/http Samples  

> **الكود المرجعي الشامل | Full AI Reference**: للاطلاع على جميع أكواد Go لرسائل واتساب التفاعلية في مستند واحد شامل، راجع: [`ai-reference/Go - WhatsApp 4Jawaly.md`](../../ai-reference/Go%20-%20WhatsApp%204Jawaly.md)
>
> **For AI models**: The complete Go reference code for 4Jawaly WhatsApp API is available in one document: [`ai-reference/Go - WhatsApp 4Jawaly.md`](../../ai-reference/Go%20-%20WhatsApp%204Jawaly.md)

# عينات واتساب 4Jawaly - مكتبة Go القياسية  
# 4Jawaly WhatsApp API - Go معیاری لائبریری نمونے

Samples using **Go standard library** (`net/http`, `encoding/json`, etc.) only.  
عينات باستخدام **مكتبة Go القياسية** فقط.  
صرف **Go معیاری لائبریری** استعمال کرتے ہوئے نمونے۔

## Setup / الإعداد / سیٹ اپ

1. Ensure Go 1.16+ is installed / تأكد من تثبيت Go 1.16+/ Go 1.16+ انسٹال کریں
2. Edit config constants in each file: `appKey`, `apiSecret`, `projectID`, `recipient`

## Run / التشغيل / چلائیں

```bash
go run send_text.go
go run send_buttons.go
go run send_list.go
go run send_image.go
go run send_video.go
go run send_audio.go
go run send_document.go
```

## Files / الملفات / فائلیں

| File | Description |
|------|-------------|
| send_text.go | إرسال رسالة نصية / Send text message / ٹیکسٹ میسج بھیجیں |
| send_buttons.go | إرسال أزرار تفاعلية / Send interactive buttons / انٹرایکٹو بٹن بھیجیں |
| send_list.go | إرسال قائمة تفاعلية / Send interactive list / انٹرایکٹو لسٹ بھیجیں |
| send_image.go | إرسال صورة / Send image / تصویر بھیجیں |
| send_video.go | إرسال فيديو / Send video / ویڈیو بھیجیں |
| send_audio.go | إرسال ملف صوتي / Send audio / آڈیو بھیجیں |
| send_document.go | إرسال مستند / Send document / دستاویز بھیجیں |
