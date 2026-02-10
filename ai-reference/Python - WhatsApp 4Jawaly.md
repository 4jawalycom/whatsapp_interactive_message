# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة بايثون باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Python using 4Jawaly

## معلومات API | API Information
- Base URL: https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
- Method: POST
- Auth: Basic Auth (base64(app_key:api_secret))
- Content-Type: application/json

## أنواع الرسائل المدعومة | Supported Message Types
1. رسالة نصية (Text)
2. أزرار تفاعلية (Interactive Buttons) - حتى 3 أزرار
3. قائمة تفاعلية (Interactive List) - حتى 10 عناصر
4. صورة (Image)
5. فيديو (Video)
6. ملف صوتي (Audio)
7. مستند (Document)

---

## 1. Python مع مكتبة requests (بدون فريموورك)

### إرسال رسالة نصية | send_text.py
```python
#!/usr/bin/env python3
# إرسال رسالة نصية عبر واتساب
# Send text message via WhatsApp
# واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# محتوى الرسالة - Message content - پیغام کا مواد
MESSAGE_BODY = "نص الرسالة"


def send_text_message():
    """إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "text",
                "text": {"body": MESSAGE_BODY},
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_text_message()
```

### إرسال أزرار تفاعلية | send_buttons.py
```python
#!/usr/bin/env python3
# إرسال رسالة بأزرار تفاعلية عبر واتساب
# Send interactive buttons message via WhatsApp
# واٹس ایپ کے ذریعے انٹرایکٹو بٹن پیغام بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"


def send_buttons_message():
    """إرسال رسالة أزرار - Send buttons message - بٹن پیغام بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {"text": "اختر أحد الخيارات التالية"},
                    "action": {
                        "buttons": [
                            {"type": "reply", "reply": {"id": "btn_yes", "title": "نعم"}},
                            {"type": "reply", "reply": {"id": "btn_no", "title": "لا"}},
                            {"type": "reply", "reply": {"id": "btn_help", "title": "مساعدة"}},
                        ]
                    },
                },
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_buttons_message()
```

### إرسال قائمة تفاعلية | send_list.py
```python
#!/usr/bin/env python3
# إرسال رسالة بقائمة تفاعلية عبر واتساب
# Send interactive list message via WhatsApp
# واٹس ایپ کے ذریعے انٹرایکٹو لسٹ پیغام بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"


def send_list_message():
    """إرسال رسالة قائمة - Send list message - لسٹ پیغام بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "header": {"type": "text", "text": "قائمة الخدمات"},
                    "body": {"text": "اختر الخدمة المطلوبة من القائمة أدناه"},
                    "footer": {"text": "4Jawaly Services"},
                    "action": {
                        "button": "عرض القائمة",
                        "sections": [
                            {
                                "title": "الخدمات الأساسية",
                                "rows": [
                                    {
                                        "id": "svc_sms",
                                        "title": "خدمة الرسائل النصية",
                                        "description": "إرسال رسائل SMS للعملاء",
                                    },
                                    {
                                        "id": "svc_whatsapp",
                                        "title": "خدمة واتساب",
                                        "description": "إرسال رسائل واتساب تفاعلية",
                                    },
                                ],
                            },
                            {
                                "title": "الدعم الفني",
                                "rows": [
                                    {
                                        "id": "support_ticket",
                                        "title": "فتح تذكرة دعم",
                                        "description": "تواصل مع فريق الدعم الفني",
                                    },
                                ],
                            },
                        ],
                    },
                },
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_list_message()
```

### إرسال صورة | send_image.py
```python
#!/usr/bin/env python3
# إرسال صورة عبر واتساب
# Send image via WhatsApp
# واٹس ایپ کے ذریعے تصویر بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الصورة والوصف - Image URL and caption - تصویر کا لنک اور کیپشن
IMAGE_URL = "https://example.com/image.jpg"
IMAGE_CAPTION = "وصف الصورة"


def send_image_message():
    """إرسال صورة - Send image - تصویر بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "image",
                "image": {"link": IMAGE_URL, "caption": IMAGE_CAPTION},
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_image_message()
```

### إرسال فيديو | send_video.py
```python
#!/usr/bin/env python3
# إرسال فيديو عبر واتساب
# Send video via WhatsApp
# واٹس ایپ کے ذریعے ویڈیو بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الفيديو والوصف - Video URL and caption - ویڈیو کا لنک اور کیپشن
VIDEO_URL = "https://example.com/video.mp4"
VIDEO_CAPTION = "وصف الفيديو"


def send_video_message():
    """إرسال فيديو - Send video - ویڈیو بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "video",
                "video": {"link": VIDEO_URL, "caption": VIDEO_CAPTION},
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_video_message()
```

### إرسال ملف صوتي | send_audio.py
```python
#!/usr/bin/env python3
# إرسال ملف صوتي عبر واتساب
# Send audio file via WhatsApp
# واٹس ایپ کے ذریعے آڈیو فائل بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الملف الصوتي - Audio file URL - آڈیو فائل کا لنک
AUDIO_URL = "https://example.com/audio.mp3"


def send_audio_message():
    """إرسال ملف صوتي - Send audio - آڈیو بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "audio",
                "audio": {"link": AUDIO_URL},
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_audio_message()
```

### إرسال مستند | send_document.py
```python
#!/usr/bin/env python3
# إرسال مستند عبر واتساب
# Send document via WhatsApp
# واٹس ایپ کے ذریعے دستاویز بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط المستند والوصف واسم الملف - Document URL, caption and filename - دستاویز کا لنک، کیپشن اور فائل کا نام
DOCUMENT_URL = "https://example.com/document.pdf"
DOCUMENT_CAPTION = "وصف المستند"
DOCUMENT_FILENAME = "document.pdf"


def send_document_message():
    """إرسال مستند - Send document - دستاویز بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    payload = {
        "path": "global",
        "params": {
            "url": "messages",
            "method": "post",
            "data": {
                "messaging_product": "whatsapp",
                "to": RECIPIENT,
                "type": "document",
                "document": {
                    "link": DOCUMENT_URL,
                    "caption": DOCUMENT_CAPTION,
                    "filename": DOCUMENT_FILENAME,
                },
            },
        },
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {auth_b64}",
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"رمز الاستجابة / Response code / جوابی کوڈ: {response.status_code}")
        print(f"\nالاستجابة / Response / جواب:\n{json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال / Connection error / رابطہ میں خرابی: {e}")
    except json.JSONDecodeError as e:
        print(f"خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: {e}")
        print(f"النص الخام / Raw text / خام متن: {response.text}")


if __name__ == "__main__":
    send_document_message()
```

---

## 2. Python Flask Framework

### خدمة الواتساب | whatsapp_service.py
```python
#!/usr/bin/env python3
# خدمة إرسال رسائل واتساب عبر 4Jawaly API
# WhatsApp messaging service via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کی سروس

import base64
import os
from typing import Optional

import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = os.environ.get("APP_KEY", "your_app_key")
API_SECRET = os.environ.get("API_SECRET", "your_api_secret")
PROJECT_ID = os.environ.get("PROJECT_ID", "your_project_id")
BASE_URL = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"


class WhatsAppService:
    """
    خدمة واتساب - WhatsApp Service - واٹس ایپ سروس
    إرسال جميع أنواع الرسائل عبر 4Jawaly API
    Send all message types via 4Jawaly API
    """

    def __init__(
        self,
        app_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        project_id: Optional[str] = None,
    ):
        """
        إنشاء الخدمة - Constructor - کنسٹرکٹر
        """
        self.app_key = app_key or APP_KEY
        self.api_secret = api_secret or API_SECRET
        self.project_id = project_id or PROJECT_ID
        self.base_url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{self.project_id}"
        auth_string = f"{self.app_key}:{self.api_secret}"
        auth_b64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_b64}",
        }

    def _send_request(self, message_data: dict) -> dict:
        """
        إرسال طلب للـ API - Make API request - API درخواست بھیجیں
        """
        payload = {
            "path": "global",
            "params": {
                "url": "messages",
                "method": "post",
                "data": {
                    "messaging_product": "whatsapp",
                    "to": message_data.get("to", ""),
                    **message_data.get("payload", {}),
                },
            },
        }
        try:
            response = requests.post(
                self.base_url, json=payload, headers=self.headers, timeout=30
            )
            return {"status_code": response.status_code, "data": response.json()}
        except requests.exceptions.RequestException as e:
            return {"error": True, "message": str(e), "status_code": 500}
        except ValueError:
            return {"error": True, "message": "Invalid JSON response", "status_code": 500}

    def send_text(self, recipient: str, body: str) -> dict:
        """
        إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
        """
        return self._send_request(
            {"to": recipient, "payload": {"type": "text", "text": {"body": body}}}
        )

    def send_buttons(
        self, recipient: str, body_text: str, buttons: list[dict[str, str]]
    ) -> dict:
        """
        إرسال رسالة بأزرار تفاعلية - Send interactive buttons - انٹرایکٹو بٹن بھیجیں
        buttons: [{"id":"btn_yes","title":"نعم"}, ...]
        """
        formatted = [
            {"type": "reply", "reply": {"id": b.get("id", ""), "title": b.get("title", "")}}
            for b in buttons
        ]
        return self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "button",
                        "body": {"text": body_text},
                        "action": {"buttons": formatted},
                    },
                },
            }
        )

    def send_list(
        self,
        recipient: str,
        header_text: str,
        body_text: str,
        footer_text: str,
        button_label: str,
        sections: list[dict],
    ) -> dict:
        """
        إرسال رسالة بقائمة تفاعلية - Send interactive list - انٹرایکٹو لسٹ بھیجیں
        """
        return self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "list",
                        "header": {"type": "text", "text": header_text},
                        "body": {"text": body_text},
                        "footer": {"text": footer_text},
                        "action": {"button": button_label, "sections": sections},
                    },
                },
            }
        )

    def send_image(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict:
        """
        إرسال صورة - Send image - تصویر بھیجیں
        """
        image = {"link": link}
        if caption:
            image["caption"] = caption
        return self._send_request(
            {"to": recipient, "payload": {"type": "image", "image": image}}
        )

    def send_video(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict:
        """
        إرسال فيديو - Send video - ویڈیو بھیجیں
        """
        video = {"link": link}
        if caption:
            video["caption"] = caption
        return self._send_request(
            {"to": recipient, "payload": {"type": "video", "video": video}}
        )

    def send_audio(self, recipient: str, link: str) -> dict:
        """
        إرسال ملف صوتي - Send audio - آڈیو بھیجیں
        """
        return self._send_request(
            {
                "to": recipient,
                "payload": {"type": "audio", "audio": {"link": link}},
            }
        )

    def send_document(
        self,
        recipient: str,
        link: str,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> dict:
        """
        إرسال مستند - Send document - دستاویز بھیجیں
        """
        doc = {"link": link}
        if caption:
            doc["caption"] = caption
        if filename:
            doc["filename"] = filename
        return self._send_request(
            {"to": recipient, "payload": {"type": "document", "document": doc}}
        )
```

### التطبيق والمسارات | app.py
```python
#!/usr/bin/env python3
# تطبيق Flask لإرسال رسائل واتساب عبر 4Jawaly API
# Flask app for sending WhatsApp messages via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کے لیے Flask ایپ

import os

from flask import Flask, jsonify, request

from whatsapp_service import WhatsAppService

# إعدادات التطبيق - App config - ایپ کی ترتیبات
APP_KEY = os.environ.get("APP_KEY", "your_app_key")
API_SECRET = os.environ.get("API_SECRET", "your_api_secret")
PROJECT_ID = os.environ.get("PROJECT_ID", "your_project_id")

app = Flask(__name__)
service = WhatsAppService(APP_KEY, API_SECRET, PROJECT_ID)


# مسار إرسال رسالة نصية - Text message route - ٹیکسٹ پیغام روٹ
@app.route("/whatsapp/text", methods=["POST"])
def send_text():
    """
    إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
    Body: {"to":"9665XXXXXXXX","body":"نص الرسالة"}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    body = data.get("body", "")
    if not to:
        return jsonify({"error": True, "message": "Missing 'to' field"}), 400
    result = service.send_text(to, body)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال أزرار تفاعلية - Interactive buttons route - انٹرایکٹو بٹن روٹ
@app.route("/whatsapp/buttons", methods=["POST"])
def send_buttons():
    """
    إرسال رسالة بأزرار - Send buttons message - بٹن پیغام بھیجیں
    Body: {"to":"9665XXXXXXXX","body_text":"اختر خيارا","buttons":[{"id":"btn_yes","title":"نعم"}]}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    body_text = data.get("body_text", "اختر أحد الخيارات التالية")
    buttons = data.get("buttons", [{"id": "btn_yes", "title": "نعم"}, {"id": "btn_no", "title": "لا"}])
    if not to:
        return jsonify({"error": True, "message": "Missing 'to' field"}), 400
    result = service.send_buttons(to, body_text, buttons)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال قائمة تفاعلية - Interactive list route - انٹرایکٹو لسٹ روٹ
@app.route("/whatsapp/list", methods=["POST"])
def send_list():
    """
    إرسال رسالة بقائمة - Send list message - لسٹ پیغام بھیجیں
    Body: {"to":"9665XXXXXXXX","header_text":"...","body_text":"...","footer_text":"...","button_label":"...","sections":[...]}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    header_text = data.get("header_text", "قائمة الخدمات")
    body_text = data.get("body_text", "اختر الخدمة المطلوبة")
    footer_text = data.get("footer_text", "4Jawaly Services")
    button_label = data.get("button_label", "عرض القائمة")
    sections = data.get("sections", [])
    if not to:
        return jsonify({"error": True, "message": "Missing 'to' field"}), 400
    result = service.send_list(
        to, header_text, body_text, footer_text, button_label, sections
    )
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال صورة - Image route - تصویر روٹ
@app.route("/whatsapp/image", methods=["POST"])
def send_image():
    """
    إرسال صورة - Send image - تصویر بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://...","caption":"وصف اختياري"}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    if not to or not link:
        return jsonify({"error": True, "message": "Missing 'to' or 'link' field"}), 400
    result = service.send_image(to, link, caption)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال فيديو - Video route - ویڈیو روٹ
@app.route("/whatsapp/video", methods=["POST"])
def send_video():
    """
    إرسال فيديو - Send video - ویڈیو بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://...","caption":"وصف اختياري"}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    if not to or not link:
        return jsonify({"error": True, "message": "Missing 'to' or 'link' field"}), 400
    result = service.send_video(to, link, caption)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال ملف صوتي - Audio route - آڈیو روٹ
@app.route("/whatsapp/audio", methods=["POST"])
def send_audio():
    """
    إرسال ملف صوتي - Send audio - آڈیو بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://..."}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    link = data.get("link", "")
    if not to or not link:
        return jsonify({"error": True, "message": "Missing 'to' or 'link' field"}), 400
    result = service.send_audio(to, link)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


# مسار إرسال مستند - Document route - دستاویز روٹ
@app.route("/whatsapp/document", methods=["POST"])
def send_document():
    """
    إرسال مستند - Send document - دستاویز بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://...","caption":"...","filename":"..."}
    """
    data = request.get_json(silent=True) or {}
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    filename = data.get("filename")
    if not to or not link:
        return jsonify({"error": True, "message": "Missing 'to' or 'link' field"}), 400
    result = service.send_document(to, link, caption, filename)
    if result.get("error"):
        return jsonify(result), result.get("status_code", 500)
    return jsonify(result)


if __name__ == "__main__":
    # تشغيل الخادم - Run server - سرور چلائیں
    app.run(host="0.0.0.0", port=5000, debug=True)
```

---

## 3. Python Django Framework

### خدمة الواتساب | whatsapp_service.py
```python
#!/usr/bin/env python3
# خدمة إرسال رسائل واتساب عبر 4Jawaly API
# WhatsApp messaging service via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کی سروس

import base64
import os
from typing import Optional

import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = os.environ.get("APP_KEY", "your_app_key")
API_SECRET = os.environ.get("API_SECRET", "your_api_secret")
PROJECT_ID = os.environ.get("PROJECT_ID", "your_project_id")
BASE_URL = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"


class WhatsAppService:
    """
    خدمة واتساب - WhatsApp Service - واٹس ایپ سروس
    إرسال جميع أنواع الرسائل عبر 4Jawaly API
    Send all message types via 4Jawaly API
    """

    def __init__(
        self,
        app_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        project_id: Optional[str] = None,
    ):
        """
        إنشاء الخدمة - Constructor - کنسٹرکٹر
        """
        self.app_key = app_key or APP_KEY
        self.api_secret = api_secret or API_SECRET
        self.project_id = project_id or PROJECT_ID
        self.base_url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{self.project_id}"
        auth_string = f"{self.app_key}:{self.api_secret}"
        auth_b64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_b64}",
        }

    def _send_request(self, message_data: dict) -> dict:
        """
        إرسال طلب للـ API - Make API request - API درخواست بھیجیں
        """
        payload = {
            "path": "global",
            "params": {
                "url": "messages",
                "method": "post",
                "data": {
                    "messaging_product": "whatsapp",
                    "to": message_data.get("to", ""),
                    **message_data.get("payload", {}),
                },
            },
        }
        try:
            response = requests.post(
                self.base_url, json=payload, headers=self.headers, timeout=30
            )
            return {"status_code": response.status_code, "data": response.json()}
        except requests.exceptions.RequestException as e:
            return {"error": True, "message": str(e), "status_code": 500}
        except ValueError:
            return {"error": True, "message": "Invalid JSON response", "status_code": 500}

    def send_text(self, recipient: str, body: str) -> dict:
        """
        إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
        """
        return self._send_request(
            {"to": recipient, "payload": {"type": "text", "text": {"body": body}}}
        )

    def send_buttons(
        self, recipient: str, body_text: str, buttons: list[dict[str, str]]
    ) -> dict:
        """
        إرسال رسالة بأزرار تفاعلية - Send interactive buttons - انٹرایکٹو بٹن بھیجیں
        buttons: [{"id":"btn_yes","title":"نعم"}, ...]
        """
        formatted = [
            {"type": "reply", "reply": {"id": b.get("id", ""), "title": b.get("title", "")}}
            for b in buttons
        ]
        return self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "button",
                        "body": {"text": body_text},
                        "action": {"buttons": formatted},
                    },
                },
            }
        )

    def send_list(
        self,
        recipient: str,
        header_text: str,
        body_text: str,
        footer_text: str,
        button_label: str,
        sections: list[dict],
    ) -> dict:
        """
        إرسال رسالة بقائمة تفاعلية - Send interactive list - انٹرایکٹو لسٹ بھیجیں
        """
        return self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "list",
                        "header": {"type": "text", "text": header_text},
                        "body": {"text": body_text},
                        "footer": {"text": footer_text},
                        "action": {"button": button_label, "sections": sections},
                    },
                },
            }
        )

    def send_image(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict:
        """
        إرسال صورة - Send image - تصویر بھیجیں
        """
        image = {"link": link}
        if caption:
            image["caption"] = caption
        return self._send_request(
            {"to": recipient, "payload": {"type": "image", "image": image}}
        )

    def send_video(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict:
        """
        إرسال فيديو - Send video - ویڈیو بھیجیں
        """
        video = {"link": link}
        if caption:
            video["caption"] = caption
        return self._send_request(
            {"to": recipient, "payload": {"type": "video", "video": video}}
        )

    def send_audio(self, recipient: str, link: str) -> dict:
        """
        إرسال ملف صوتي - Send audio - آڈیو بھیجیں
        """
        return self._send_request(
            {
                "to": recipient,
                "payload": {"type": "audio", "audio": {"link": link}},
            }
        )

    def send_document(
        self,
        recipient: str,
        link: str,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> dict:
        """
        إرسال مستند - Send document - دستاویز بھیجیں
        """
        doc = {"link": link}
        if caption:
            doc["caption"] = caption
        if filename:
            doc["filename"] = filename
        return self._send_request(
            {"to": recipient, "payload": {"type": "document", "document": doc}}
        )
```

### العروض | views.py
```python
#!/usr/bin/env python3
# عرضات إرسال رسائل واتساب عبر 4Jawaly API
# Views for sending WhatsApp messages via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کے لیے ویوز

import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from whatsapp_service import WhatsAppService

# إعدادات التطبيق - App config - ایپ کی ترتیبات
APP_KEY = os.environ.get("APP_KEY", "your_app_key")
API_SECRET = os.environ.get("API_SECRET", "your_api_secret")
PROJECT_ID = os.environ.get("PROJECT_ID", "your_project_id")

service = WhatsAppService(APP_KEY, API_SECRET, PROJECT_ID)


def _parse_json(request):
    """تحليل الجسم JSON - Parse JSON body - JSON باڈی کو پارس کریں"""
    try:
        return json.loads(request.body) if request.body else {}
    except json.JSONDecodeError:
        return {}


@csrf_exempt
@require_http_methods(["POST"])
def send_text(request):
    """
    إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
    Body: {"to":"9665XXXXXXXX","body":"نص الرسالة"}
    """
    data = _parse_json(request)
    to = data.get("to")
    body = data.get("body", "")
    if not to:
        return JsonResponse({"error": True, "message": "Missing 'to' field"}, status=400)
    result = service.send_text(to, body)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_buttons(request):
    """
    إرسال رسالة بأزرار - Send buttons message - بٹن پیغام بھیجیں
    Body: {"to":"9665XXXXXXXX","body_text":"...","buttons":[{"id":"btn_yes","title":"نعم"}]}
    """
    data = _parse_json(request)
    to = data.get("to")
    body_text = data.get("body_text", "اختر أحد الخيارات التالية")
    buttons = data.get("buttons", [{"id": "btn_yes", "title": "نعم"}, {"id": "btn_no", "title": "لا"}])
    if not to:
        return JsonResponse({"error": True, "message": "Missing 'to' field"}, status=400)
    result = service.send_buttons(to, body_text, buttons)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_list(request):
    """
    إرسال رسالة بقائمة - Send list message - لسٹ پیغام بھیجیں
    """
    data = _parse_json(request)
    to = data.get("to")
    header_text = data.get("header_text", "قائمة الخدمات")
    body_text = data.get("body_text", "اختر الخدمة المطلوبة")
    footer_text = data.get("footer_text", "4Jawaly Services")
    button_label = data.get("button_label", "عرض القائمة")
    sections = data.get("sections", [])
    if not to:
        return JsonResponse({"error": True, "message": "Missing 'to' field"}, status=400)
    result = service.send_list(
        to, header_text, body_text, footer_text, button_label, sections
    )
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_image(request):
    """
    إرسال صورة - Send image - تصویر بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://...","caption":"وصف اختياري"}
    """
    data = _parse_json(request)
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    if not to or not link:
        return JsonResponse({"error": True, "message": "Missing 'to' or 'link' field"}, status=400)
    result = service.send_image(to, link, caption)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_video(request):
    """
    إرسال فيديو - Send video - ویڈیو بھیجیں
    """
    data = _parse_json(request)
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    if not to or not link:
        return JsonResponse({"error": True, "message": "Missing 'to' or 'link' field"}, status=400)
    result = service.send_video(to, link, caption)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_audio(request):
    """
    إرسال ملف صوتي - Send audio - آڈیو بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://..."}
    """
    data = _parse_json(request)
    to = data.get("to")
    link = data.get("link", "")
    if not to or not link:
        return JsonResponse({"error": True, "message": "Missing 'to' or 'link' field"}, status=400)
    result = service.send_audio(to, link)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def send_document(request):
    """
    إرسال مستند - Send document - دستاویز بھیجیں
    Body: {"to":"9665XXXXXXXX","link":"https://...","caption":"...","filename":"..."}
    """
    data = _parse_json(request)
    to = data.get("to")
    link = data.get("link", "")
    caption = data.get("caption")
    filename = data.get("filename")
    if not to or not link:
        return JsonResponse({"error": True, "message": "Missing 'to' or 'link' field"}, status=400)
    result = service.send_document(to, link, caption, filename)
    if result.get("error"):
        return JsonResponse(result, status=result.get("status_code", 500))
    return JsonResponse(result)
```

### المسارات | urls.py
```python
#!/usr/bin/env python3
# مسارات واتساب - WhatsApp URL patterns - واٹس ایپ یو آر ایل پیٹرنز
# تضمين هذا الملف في config/urls.py عبر: path('whatsapp/', include('urls'))
# Include in config/urls.py via: path('whatsapp/', include('urls'))
# config/urls.py میں شامل کریں: path('whatsapp/', include('urls'))

from django.urls import path

from views import (
    send_audio,
    send_buttons,
    send_document,
    send_image,
    send_list,
    send_text,
    send_video,
)

urlpatterns = [
    path("text", send_text),
    path("buttons", send_buttons),
    path("list", send_list),
    path("image", send_image),
    path("video", send_video),
    path("audio", send_audio),
    path("document", send_document),
]
```

---

## 4. Python FastAPI Framework

### خدمة الواتساب | whatsapp_service.py
```python
#!/usr/bin/env python3
# خدمة إرسال رسائل واتساب عبر 4Jawaly API (غير متزامنة)
# WhatsApp messaging service via 4Jawaly API (async)
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کی سروس (غیر ہم وقت ساز)

import base64
import os
from typing import Any, Optional

import httpx


class WhatsAppService:
    """
    خدمة واتساب غير متزامنة - Async WhatsApp Service - غیر ہم وقت ساز واٹس ایپ سروس
    إرسال جميع أنواع الرسائل عبر 4Jawaly API باستخدام httpx
    Send all message types via 4Jawaly API using httpx
    """

    def __init__(
        self,
        app_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        project_id: Optional[str] = None,
    ):
        """
        إنشاء الخدمة - Constructor - کنسٹرکٹر
        """
        self.app_key = app_key or os.environ.get("APP_KEY", "your_app_key")
        self.api_secret = api_secret or os.environ.get("API_SECRET", "your_api_secret")
        self.project_id = project_id or os.environ.get("PROJECT_ID", "your_project_id")
        self.base_url = (
            f"https://api-users.4jawaly.com/api/v1/whatsapp/{self.project_id}"
        )
        auth_string = f"{self.app_key}:{self.api_secret}"
        auth_b64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_b64}",
        }

    async def _send_request(self, message_data: dict[str, Any]) -> dict[str, Any]:
        """
        إرسال طلب للـ API - Make API request - API درخواست بھیجیں
        """
        payload = {
            "path": "global",
            "params": {
                "url": "messages",
                "method": "post",
                "data": {
                    "messaging_product": "whatsapp",
                    "to": message_data.get("to", ""),
                    **message_data.get("payload", {}),
                },
            },
        }
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    self.base_url, json=payload, headers=self.headers
                )
                return {"status_code": response.status_code, "data": response.json()}
        except httpx.RequestError as e:
            return {"error": True, "message": str(e), "status_code": 500}
        except ValueError:
            return {"error": True, "message": "Invalid JSON response", "status_code": 500}

    async def send_text(self, recipient: str, body: str) -> dict[str, Any]:
        """
        إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
        """
        return await self._send_request(
            {"to": recipient, "payload": {"type": "text", "text": {"body": body}}}
        )

    async def send_buttons(
        self, recipient: str, body_text: str, buttons: list[dict[str, str]]
    ) -> dict[str, Any]:
        """
        إرسال رسالة بأزرار تفاعلية - Send interactive buttons - انٹرایکٹو بٹن بھیجیں
        buttons: [{"id":"btn_yes","title":"نعم"}, ...]
        """
        formatted = [
            {"type": "reply", "reply": {"id": b.get("id", ""), "title": b.get("title", "")}}
            for b in buttons
        ]
        return await self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "button",
                        "body": {"text": body_text},
                        "action": {"buttons": formatted},
                    },
                },
            }
        )

    async def send_list(
        self,
        recipient: str,
        header_text: str,
        body_text: str,
        footer_text: str,
        button_label: str,
        sections: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        إرسال رسالة بقائمة تفاعلية - Send interactive list - انٹرایکٹو لسٹ بھیجیں
        """
        return await self._send_request(
            {
                "to": recipient,
                "payload": {
                    "type": "interactive",
                    "interactive": {
                        "type": "list",
                        "header": {"type": "text", "text": header_text},
                        "body": {"text": body_text},
                        "footer": {"text": footer_text},
                        "action": {"button": button_label, "sections": sections},
                    },
                },
            }
        )

    async def send_image(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict[str, Any]:
        """
        إرسال صورة - Send image - تصویر بھیجیں
        """
        image: dict[str, Any] = {"link": link}
        if caption:
            image["caption"] = caption
        return await self._send_request(
            {"to": recipient, "payload": {"type": "image", "image": image}}
        )

    async def send_video(
        self, recipient: str, link: str, caption: Optional[str] = None
    ) -> dict[str, Any]:
        """
        إرسال فيديو - Send video - ویڈیو بھیجیں
        """
        video: dict[str, Any] = {"link": link}
        if caption:
            video["caption"] = caption
        return await self._send_request(
            {"to": recipient, "payload": {"type": "video", "video": video}}
        )

    async def send_audio(self, recipient: str, link: str) -> dict[str, Any]:
        """
        إرسال ملف صوتي - Send audio - آڈیو بھیجیں
        """
        return await self._send_request(
            {
                "to": recipient,
                "payload": {"type": "audio", "audio": {"link": link}},
            }
        )

    async def send_document(
        self,
        recipient: str,
        link: str,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        إرسال مستند - Send document - دستاویز بھیجیں
        """
        doc: dict[str, Any] = {"link": link}
        if caption:
            doc["caption"] = caption
        if filename:
            doc["filename"] = filename
        return await self._send_request(
            {"to": recipient, "payload": {"type": "document", "document": doc}}
        )
```

### التطبيق الرئيسي | main.py
```python
#!/usr/bin/env python3
# تطبيق FastAPI لإرسال رسائل واتساب عبر 4Jawaly API
# FastAPI app for sending WhatsApp messages via 4Jawaly API
# 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کے لیے FastAPI ایپ

import os
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from whatsapp_service import WhatsAppService

# إعدادات التطبيق - App config - ایپ کی ترتیبات
APP_KEY = os.environ.get("APP_KEY", "your_app_key")
API_SECRET = os.environ.get("API_SECRET", "your_api_secret")
PROJECT_ID = os.environ.get("PROJECT_ID", "your_project_id")

app = FastAPI(
    title="4Jawaly WhatsApp API",
    description="إرسال رسائل واتساب عبر 4Jawaly - Send WhatsApp messages via 4Jawaly",
    version="1.0.0",
)
service = WhatsAppService(APP_KEY, API_SECRET, PROJECT_ID)


# --- Pydantic Models ---
# نماذج Pydantic للتحقق من الطلبات - Request validation models


class TextRequest(BaseModel):
    """طلب رسالة نصية - Text message request - ٹیکسٹ پیغام کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    body: str = Field(..., description="نص الرسالة - Message body - پیغام کا متن")


class ButtonItem(BaseModel):
    """زر تفاعلي - Button item - بٹن آئٹم"""

    id: str = Field(..., description="معرف الزر - Button ID - بٹن کی شناخت")
    title: str = Field(..., description="عنوان الزر - Button title - بٹن کا عنوان")


class ButtonsRequest(BaseModel):
    """طلب رسالة بأزرار - Buttons message request - بٹن پیغام کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    body_text: str = Field(
        default="اختر أحد الخيارات التالية",
        description="نص الرسالة - Body text - جسم کا متن",
    )
    buttons: list[ButtonItem] = Field(
        ...,
        min_length=1,
        max_length=3,
        description="قائمة الأزرار - Buttons list - بٹنوں کی فہرست",
    )


class ListRow(BaseModel):
    """صف في القائمة - List row - فہرست کی صف"""

    id: str = Field(..., description="معرف الصف - Row ID - صف کی شناخت")
    title: str = Field(..., description="عنوان الصف - Row title - صف کا عنوان")
    description: Optional[str] = Field(
        None, description="وصف الصف - Row description - صف کی تفصیل"
    )


class ListSection(BaseModel):
    """قسم في القائمة - List section - فہرست کا حصہ"""

    title: str = Field(..., description="عنوان القسم - Section title - حصہ کا عنوان")
    rows: list[ListRow] = Field(..., description="صفوف القسم - Section rows - حصے کی صفیں")


class ListRequest(BaseModel):
    """طلب رسالة بقائمة - List message request - لسٹ پیغام کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    header_text: str = Field(
        default="قائمة الخدمات",
        description="نص الرأس - Header text - ہیڈر کا متن",
    )
    body_text: str = Field(
        default="اختر الخدمة المطلوبة من القائمة أدناه",
        description="نص الجسم - Body text - جسم کا متن",
    )
    footer_text: str = Field(
        default="4Jawaly Services",
        description="نص التذييل - Footer text - فوٹر کا متن",
    )
    button_label: str = Field(
        default="عرض القائمة",
        description="عنوان زر القائمة - List button label - لسٹ بٹن لیبل",
    )
    sections: list[ListSection] = Field(..., description="أقسام القائمة - List sections")


class ImageRequest(BaseModel):
    """طلب إرسال صورة - Image request - تصویر کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    link: str = Field(..., description="رابط الصورة - Image URL - تصویر کا لنک")
    caption: Optional[str] = Field(None, description="وصف الصورة - Image caption - تصویر کا کیپشن")


class VideoRequest(BaseModel):
    """طلب إرسال فيديو - Video request - ویڈیو کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    link: str = Field(..., description="رابط الفيديو - Video URL - ویڈیو کا لنک")
    caption: Optional[str] = Field(None, description="وصف الفيديو - Video caption - ویڈیو کا کیپشن")


class AudioRequest(BaseModel):
    """طلب إرسال ملف صوتي - Audio request - آڈیو کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    link: str = Field(..., description="رابط الملف الصوتي - Audio URL - آڈیو کا لنک")


class DocumentRequest(BaseModel):
    """طلب إرسال مستند - Document request - دستاویز کی درخواست"""

    to: str = Field(..., description="رقم المستلم - Recipient number - وصول کنندہ نمبر")
    link: str = Field(..., description="رابط المستند - Document URL - دستاویز کا لنک")
    caption: Optional[str] = Field(None, description="وصف المستند - Document caption - دستاویز کا کیپشن")
    filename: Optional[str] = Field(None, description="اسم الملف - Filename - فائل کا نام")


# --- Routes ---
# المسارات - API endpoints


@app.get("/")
async def root():
    """
    الصفحة الرئيسية - Root endpoint - روٹ اینڈ پوائنٹ
    """
    return {"message": "4Jawaly WhatsApp API - استخدم /docs للتوثيق"}


@app.post("/whatsapp/text")
async def send_text(req: TextRequest):
    """
    إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
    """
    result = await service.send_text(req.to, req.body)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/buttons")
async def send_buttons(req: ButtonsRequest):
    """
    إرسال رسالة بأزرار تفاعلية - Send interactive buttons - انٹرایکٹو بٹن بھیجیں
    """
    buttons = [{"id": b.id, "title": b.title} for b in req.buttons]
    result = await service.send_buttons(req.to, req.body_text, buttons)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/list")
async def send_list(req: ListRequest):
    """
    إرسال رسالة بقائمة تفاعلية - Send interactive list - انٹرایکٹو لسٹ بھیجیں
    """
    sections = []
    for s in req.sections:
        rows = []
        for r in s.rows:
            row = {"id": r.id, "title": r.title}
            if r.description is not None:
                row["description"] = r.description
            rows.append(row)
        sections.append({"title": s.title, "rows": rows})
    result = await service.send_list(
        req.to,
        req.header_text,
        req.body_text,
        req.footer_text,
        req.button_label,
        sections,
    )
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/image")
async def send_image(req: ImageRequest):
    """
    إرسال صورة - Send image - تصویر بھیجیں
    """
    result = await service.send_image(req.to, req.link, req.caption)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/video")
async def send_video(req: VideoRequest):
    """
    إرسال فيديو - Send video - ویڈیو بھیجیں
    """
    result = await service.send_video(req.to, req.link, req.caption)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/audio")
async def send_audio(req: AudioRequest):
    """
    إرسال ملف صوتي - Send audio - آڈیو بھیجیں
    """
    result = await service.send_audio(req.to, req.link)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


@app.post("/whatsapp/document")
async def send_document(req: DocumentRequest):
    """
    إرسال مستند - Send document - دستاویز بھیجیں
    """
    result = await service.send_document(req.to, req.link, req.caption, req.filename)
    if result.get("error"):
        raise HTTPException(
            status_code=result.get("status_code", status.HTTP_500_INTERNAL_SERVER_ERROR),
            detail=result.get("message", "API request failed"),
        )
    return result


if __name__ == "__main__":
    import uvicorn

    # تشغيل الخادم - Run server - سرور چلائیں
    uvicorn.run(
        "main:app",
        host=os.environ.get("HOST", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8000")),
        reload=True,
    )
```
