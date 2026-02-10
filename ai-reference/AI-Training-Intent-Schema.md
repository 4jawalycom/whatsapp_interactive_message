# ملف تدريب الذكاء الاصطناعي - إرسال رسائل واتساب عبر 4Jawaly API
# AI Training Document - WhatsApp Messages via 4Jawaly API
# هذا المستند مرجع شامل لتدريب نماذج الذكاء الاصطناعي على إرسال رسائل واتساب باستخدام 4Jawaly

---

## أولاً: كيف يحصل المستخدم على بيانات الربط | How to Get Credentials

### رقم المشروع (Project ID)
**مسار الحصول عليه:**
1. الدخول على موقع [4Jawaly](https://www.4jawaly.com) وتسجيل الدخول
2. من القائمة الجانبية اختر: **الواتساب**
3. ادخل على: **رئيسية الواتساب**
4. ستجد هناك **حالة المشروع** و **رقم المشروع (Project ID)**

**Path to get it:**
1. Login to [4Jawaly](https://www.4jawaly.com)
2. From sidebar choose: **WhatsApp**
3. Go to: **WhatsApp Dashboard**
4. You'll find **Project Status** and **Project ID**

### مفتاح التطبيق وكلمة السر (App Key & API Secret)
**مسار الحصول عليهم:**
1. تسجيل الدخول على [4Jawaly](https://www.4jawaly.com)
2. من القائمة: **الإعدادات** → **إعدادات API**
3. ستجد: **App Key** و **API Secret**

---

## ثانياً: معلومات API الأساسية | Core API Info

- **Base URL**: `https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}`
- **Method**: POST
- **Authentication**: Basic Auth → `base64(app_key:api_secret)`
- **Content-Type**: application/json
- **هيكل الطلب الأساسي (Request Wrapper)**:
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "9665XXXXXXXX",
      "type": "نوع الرسالة",
      "...": "البيانات حسب النوع"
    }
  }
}
```

---

## ثالثاً: Intent / Schema - أنواع الرسائل والأوامر المتوقعة

### Intent 1: `send_text` - إرسال رسالة نصية

**أمثلة على أوامر المستخدم:**
- "أرسل رسالة واتساب نصية"
- "ابغى أرسل نص على واتساب"
- "Send a WhatsApp text message"
- "Send text to 966500000000"
- "أرسل للرقم 966512345678 رسالة: مرحبا بك"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم بالصيغة الدولية (مثال: 9665XXXXXXXX) |
| body | string | نعم | نص الرسالة |

**Schema:**
```json
{
  "type": "text",
  "text": {
    "body": "نص الرسالة هنا"
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "text",
      "text": {
        "body": "مرحباً بك في 4Jawaly! كيف يمكننا مساعدتك؟"
      }
    }
  }
}
```

---

### Intent 2: `send_buttons` - إرسال رسالة بأزرار تفاعلية

**أمثلة على أوامر المستخدم:**
- "أرسل رسالة واتساب بأزرار"
- "ابغى أرسل رسالة فيها خيارات"
- "Send WhatsApp message with buttons"
- "أرسل رسالة تفاعلية بـ 3 أزرار"
- "أرسل للعميل رسالة يختار منها نعم أو لا"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| body_text | string | نعم | نص الرسالة الرئيسي |
| buttons | array | نعم | مصفوفة الأزرار (حد أقصى 3) |
| buttons[].id | string | نعم | معرف الزر (فريد) |
| buttons[].title | string | نعم | عنوان الزر (حد أقصى 20 حرف) |

**القيود:**
- حد أقصى **3 أزرار** لكل رسالة
- عنوان الزر لا يتجاوز **20 حرف**

**Schema:**
```json
{
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": {
      "text": "نص الرسالة الرئيسي"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "btn_1",
            "title": "عنوان الزر"
          }
        }
      ]
    }
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "interactive",
      "interactive": {
        "type": "button",
        "body": {
          "text": "هل ترغب في تأكيد الطلب؟"
        },
        "action": {
          "buttons": [
            {"type": "reply", "reply": {"id": "confirm_yes", "title": "نعم، تأكيد"}},
            {"type": "reply", "reply": {"id": "confirm_no", "title": "لا، إلغاء"}},
            {"type": "reply", "reply": {"id": "confirm_later", "title": "لاحقاً"}}
          ]
        }
      }
    }
  }
}
```

---

### Intent 3: `send_list` - إرسال قائمة تفاعلية

**أمثلة على أوامر المستخدم:**
- "أرسل قائمة واتساب"
- "ابغى أرسل قائمة خدمات"
- "Send WhatsApp list message"
- "أرسل رسالة فيها قائمة اختيارات"
- "أرسل للعميل قائمة بالمنتجات"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| header_text | string | لا | عنوان القائمة (حد أقصى 60 حرف) |
| body_text | string | نعم | نص الرسالة (حد أقصى 1024 حرف) |
| footer_text | string | لا | نص التذييل |
| button_label | string | نعم | نص زر فتح القائمة (حد أقصى 20 حرف) |
| sections | array | نعم | أقسام القائمة |
| sections[].title | string | نعم | عنوان القسم (حد أقصى 24 حرف) |
| sections[].rows | array | نعم | عناصر القسم |
| sections[].rows[].id | string | نعم | معرف العنصر (فريد) |
| sections[].rows[].title | string | نعم | عنوان العنصر (حد أقصى 24 حرف) |
| sections[].rows[].description | string | لا | وصف العنصر (حد أقصى 72 حرف) |

**القيود:**
- حد أقصى **10 عناصر** إجمالي في كل الأقسام
- نص الرسالة لا يتجاوز **1024 حرف**
- عنوان زر القائمة لا يتجاوز **20 حرف**
- عنوان القسم لا يتجاوز **24 حرف**
- عنوان العنصر لا يتجاوز **24 حرف**
- وصف العنصر لا يتجاوز **72 حرف**

**Schema:**
```json
{
  "type": "interactive",
  "interactive": {
    "type": "list",
    "header": {"type": "text", "text": "عنوان القائمة"},
    "body": {"text": "نص الرسالة"},
    "footer": {"text": "نص التذييل"},
    "action": {
      "button": "نص زر القائمة",
      "sections": [
        {
          "title": "عنوان القسم",
          "rows": [
            {"id": "row_id", "title": "عنوان العنصر", "description": "وصف العنصر"}
          ]
        }
      ]
    }
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "interactive",
      "interactive": {
        "type": "list",
        "header": {"type": "text", "text": "قائمة الخدمات"},
        "body": {"text": "اختر الخدمة المطلوبة من القائمة أدناه"},
        "footer": {"text": "4Jawaly - فورجوالي"},
        "action": {
          "button": "عرض الخدمات",
          "sections": [
            {
              "title": "خدمات المراسلة",
              "rows": [
                {"id": "svc_sms", "title": "رسائل SMS", "description": "إرسال رسائل نصية جماعية"},
                {"id": "svc_whatsapp", "title": "رسائل واتساب", "description": "إرسال رسائل واتساب تفاعلية"}
              ]
            },
            {
              "title": "الدعم",
              "rows": [
                {"id": "support", "title": "الدعم الفني", "description": "تواصل مع فريق الدعم"},
                {"id": "docs", "title": "التوثيق", "description": "اطلع على وثائق API"}
              ]
            }
          ]
        }
      }
    }
  }
}
```

---

### Intent 4: `send_image` - إرسال صورة

**أمثلة على أوامر المستخدم:**
- "أرسل صورة على واتساب"
- "ابغى أرسل صورة للعميل"
- "Send image via WhatsApp"
- "أرسل صورة المنتج للرقم 966500000000"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| link | string | نعم | رابط الصورة (HTTPS مباشر) |
| caption | string | لا | تعليق على الصورة |

**القيود:**
- الرابط يجب أن يكون **HTTPS مباشر** (بدون إعادة توجيه)
- لا يدعم روابط Google Drive أو Dropbox

**Schema:**
```json
{
  "type": "image",
  "image": {
    "link": "https://example.com/image.jpg",
    "caption": "تعليق اختياري"
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "image",
      "image": {
        "link": "https://www.4jawaly.com/assets/images/logo.png",
        "caption": "شعار فورجوالي"
      }
    }
  }
}
```

---

### Intent 5: `send_video` - إرسال فيديو

**أمثلة على أوامر المستخدم:**
- "أرسل فيديو على واتساب"
- "ابغى أرسل مقطع فيديو"
- "Send video via WhatsApp"
- "أرسل فيديو تعريفي للعميل"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| link | string | نعم | رابط الفيديو (HTTPS مباشر، MP4) |
| caption | string | لا | تعليق على الفيديو |

**القيود:**
- حجم أقصى **16 MB**
- صيغة **MP4** مفضلة
- رابط **HTTPS مباشر** (بدون إعادة توجيه)

**Schema:**
```json
{
  "type": "video",
  "video": {
    "link": "https://example.com/video.mp4",
    "caption": "تعليق اختياري"
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "video",
      "video": {
        "link": "https://example.com/intro-video.mp4",
        "caption": "فيديو تعريفي بخدمات فورجوالي"
      }
    }
  }
}
```

---

### Intent 6: `send_audio` - إرسال ملف صوتي

**أمثلة على أوامر المستخدم:**
- "أرسل ملف صوتي على واتساب"
- "ابغى أرسل تسجيل صوتي"
- "Send audio via WhatsApp"
- "أرسل رسالة صوتية للعميل"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| link | string | نعم | رابط الملف الصوتي (HTTPS مباشر) |

**القيود:**
- حجم أقصى **16 MB**
- صيغ مدعومة: **MP3**, **OGG** (مفضل مع codec opus), **M4A**
- **لا يوجد حقل caption** للملفات الصوتية

**Schema:**
```json
{
  "type": "audio",
  "audio": {
    "link": "https://example.com/audio.mp3"
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "audio",
      "audio": {
        "link": "https://example.com/welcome-message.mp3"
      }
    }
  }
}
```

---

### Intent 7: `send_document` - إرسال مستند

**أمثلة على أوامر المستخدم:**
- "أرسل ملف PDF على واتساب"
- "ابغى أرسل مستند للعميل"
- "Send document via WhatsApp"
- "أرسل فاتورة PDF للرقم 966500000000"
- "أرسل ملف Excel للعميل"

**المعاملات المطلوبة (Parameters):**
| المعامل | النوع | مطلوب | الوصف |
|---------|-------|-------|-------|
| recipient | string | نعم | رقم المستلم |
| link | string | نعم | رابط المستند (HTTPS مباشر) |
| caption | string | لا | تعليق على المستند |
| filename | string | لا | اسم الملف الذي يظهر للمستلم |

**القيود:**
- حجم أقصى **100 MB**
- صيغ مدعومة: **PDF**, **DOCX**, **XLSX**, **TXT**, وغيرها
- رابط **HTTPS مباشر** فقط

**Schema:**
```json
{
  "type": "document",
  "document": {
    "link": "https://example.com/file.pdf",
    "caption": "تعليق اختياري",
    "filename": "اسم_الملف.pdf"
  }
}
```

**مثال طلب كامل:**
```json
{
  "path": "global",
  "params": {
    "url": "messages",
    "method": "post",
    "data": {
      "messaging_product": "whatsapp",
      "to": "966500000000",
      "type": "document",
      "document": {
        "link": "https://example.com/invoice-2024.pdf",
        "caption": "فاتورة شهر يناير 2024",
        "filename": "فاتورة-يناير-2024.pdf"
      }
    }
  }
}
```

---

## رابعاً: أمثلة محادثات تدريبية | Training Conversation Examples

### محادثة 1: إرسال نص بسيط
```
المستخدم: أرسل رسالة واتساب للرقم 966501234567 نصها "مرحبا بك عميلنا الكريم"
البوت: تم إرسال رسالة نصية عبر واتساب إلى 966501234567 بنجاح.
      المحتوى: "مرحبا بك عميلنا الكريم"
```

### محادثة 2: إرسال أزرار
```
المستخدم: أرسل رسالة للعميل 966507654321 يختار فيها بين "شراء" أو "استفسار" أو "إلغاء"
البوت: تم إرسال رسالة تفاعلية بـ 3 أزرار إلى 966507654321 بنجاح.
      الأزرار: شراء | استفسار | إلغاء
```

### محادثة 3: إرسال قائمة
```
المستخدم: أرسل قائمة خدمات للعميل 966509876543
البوت: ما هي الخدمات التي تريد عرضها في القائمة؟
المستخدم: قسم "الباقات": باقة أساسية، باقة متقدمة. قسم "الدعم": تذكرة جديدة، اتصل بنا
البوت: تم إرسال قائمة تفاعلية إلى 966509876543 بنجاح.
      الأقسام: الباقات (2 عناصر) | الدعم (2 عناصر)
```

### محادثة 4: إرسال صورة
```
المستخدم: أرسل صورة المنتج https://example.com/product.jpg للرقم 966500001111 مع تعليق "المنتج الجديد"
البوت: تم إرسال صورة عبر واتساب إلى 966500001111 بنجاح.
      التعليق: "المنتج الجديد"
```

### محادثة 5: إرسال مستند
```
المستخدم: أرسل فاتورة PDF للعميل 966500002222 الرابط https://example.com/invoice.pdf
البوت: تم إرسال مستند عبر واتساب إلى 966500002222 بنجاح.
      الملف: invoice.pdf
```

### محادثة 6: سؤال عن الإعدادات
```
المستخدم: كيف أحصل على رقم مشروع واتساب؟
البوت: للحصول على رقم المشروع (Project ID):
      1. سجل دخول على موقع 4Jawaly (4jawaly.com)
      2. من القائمة الجانبية اختر "الواتساب"
      3. ادخل على "رئيسية الواتساب"
      4. ستجد هناك "حالة المشروع" و "رقم المشروع"
```

### محادثة 7: سؤال عن بيانات API
```
المستخدم: كيف أحصل على App Key و API Secret؟
البوت: للحصول على بيانات API:
      1. سجل دخول على موقع 4Jawaly (4jawaly.com)
      2. من القائمة اختر "الإعدادات" ثم "إعدادات API"
      3. ستجد هناك "App Key" و "API Secret"
```

### محادثة 8: سؤال عن الأكواد الجاهزة
```
المستخدم: أريد كود بايثون لإرسال رسالة واتساب
البوت: يمكنك الاطلاع على الكود المرجعي الكامل لبايثون هنا:
      https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/python
      
      يتوفر كود جاهز باستخدام:
      - requests (بدون فريموورك)
      - Flask
      - Django
      - FastAPI
```

### محادثة 9: سؤال عن اللغات المتاحة
```
المستخدم: ما هي لغات البرمجة المتاحة لربط واتساب؟
البوت: نماذج الكود متاحة في 11 لغة/فريموورك:
      - PHP (حديث 8.x+ / قديم 5.6+ / Lumen)
      - Python (requests / Flask / Django / FastAPI)
      - Go (net/http / Gin / Fiber / Echo)
      - Rust
      - Ruby
      - Swift
      - Flutter/Dart
      - Kotlin
      - C# .NET
      
      الكود متاح على:
      https://github.com/4jawalycom/whatsapp_interactive_message
```

---

## خامساً: ملاحظات مهمة للبوت | Important Bot Notes

1. **نافذة الـ 24 ساعة**: الرسائل التفاعلية (أزرار وقوائم) تعمل فقط خلال 24 ساعة من آخر رسالة أرسلها العميل. بعد ذلك يجب استخدام Template Messages المعتمدة من Meta.

2. **صيغة الأرقام**: يجب أن تكون بالصيغة الدولية بدون علامة + (مثال: 966500000000 وليس +966500000000 أو 0500000000).

3. **الروابط**: جميع روابط الوسائط (صور/فيديو/صوت/مستندات) يجب أن تكون:
   - HTTPS (ليس HTTP)
   - روابط مباشرة (ليس روابط مشاركة من Google Drive أو Dropbox)
   - متاحة للعامة (بدون تسجيل دخول)

4. **حدود الأحرف**:
   - نص الرسالة: 4096 حرف
   - نص القائمة (body): 1024 حرف
   - عنوان الزر: 20 حرف
   - عنوان عنصر القائمة: 24 حرف
   - وصف عنصر القائمة: 72 حرف

5. **حدود العناصر**:
   - أزرار: حد أقصى 3
   - عناصر القائمة: حد أقصى 10 (مجموع كل الأقسام)

6. **أحجام الملفات**:
   - صوت: 16 MB
   - فيديو: 16 MB
   - مستندات: 100 MB

---

## سادساً: رابط الكود المرجعي | Reference Code Links

| اللغة | رابط الكود | المستند المرجعي الشامل |
|-------|-----------|----------------------|
| Python | [python/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/python) | [ai-reference/Python](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Python%20-%20WhatsApp%204Jawaly.md) |
| PHP | [php/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/php) | [ai-reference/PHP](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/PHP%20-%20WhatsApp%204Jawaly.md) |
| Go | [go/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/go) | [ai-reference/Go](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Go%20-%20WhatsApp%204Jawaly.md) |
| Rust | [rust/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/rust) | [ai-reference/Rust](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Rust%20-%20WhatsApp%204Jawaly.md) |
| Ruby | [ruby/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/ruby) | [ai-reference/Ruby](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Ruby%20-%20WhatsApp%204Jawaly.md) |
| Swift | [swift/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/swift) | [ai-reference/Swift](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Swift%20-%20WhatsApp%204Jawaly.md) |
| Flutter | [flutter/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/flutter) | [ai-reference/Flutter](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Flutter%20-%20WhatsApp%204Jawaly.md) |
| Kotlin | [kotlin/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/kotlin) | [ai-reference/Kotlin](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/Kotlin%20-%20WhatsApp%204Jawaly.md) |
| .NET | [dotnet/](https://github.com/4jawalycom/whatsapp_interactive_message/tree/main/dotnet) | [ai-reference/DotNet](https://github.com/4jawalycom/whatsapp_interactive_message/blob/main/ai-reference/DotNet%20-%20WhatsApp%204Jawaly.md) |
