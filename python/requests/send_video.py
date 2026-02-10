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
