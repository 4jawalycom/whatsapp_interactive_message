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
