#!/usr/bin/env python3
# إرسال جهة اتصال عبر واتساب
# Send contact via WhatsApp
# واٹس ایپ کے ذریعے رابطہ بھیجیں

import base64
import json
import requests

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "966500000000"

# بيانات جهة الاتصال - Contact data - رابطہ کا ڈیٹا
CONTACTS = [
    {
        "name": {
            "formatted_name": "Ahmed Ali",
            "first_name": "Ahmed",
            "last_name": "Ali",
        },
        "phones": [
            {
                "phone": "+966501234567",
                "type": "CELL",
            }
        ],
    }
]


def send_contact_message():
    """إرسال جهة اتصال - Send contact - رابطہ بھیجیں"""
    url = f"https://api-users.4jawaly.com/api/v1/whatsapp/{PROJECT_ID}"
    auth_string = f"{APP_KEY}:{API_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

    # ملاحظة: جهة الاتصال تستخدم هيكل طلب مختلف عن الأنواع الأخرى
    # Note: Contact uses a different request structure than other types
    payload = {
        "path": "message/contact",
        "params": {
            "phone": RECIPIENT,
            "contacts": CONTACTS,
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
    send_contact_message()
