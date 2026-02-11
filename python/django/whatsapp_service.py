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

    def _send_custom_path_request(self, path: str, params: dict) -> dict:
        """
        إرسال طلب مسار مخصص - Send custom path request - مخصوص path درخواست بھیجیں
        يستخدمه الموقع وجهة الاتصال (هيكل مختلف عن global)
        Used by location and contact (different structure than global)
        """
        payload = {"path": path, "params": params}
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

    def send_location(
        self,
        recipient: str,
        lat: float,
        lng: float,
        address: str,
        name: Optional[str] = None,
    ) -> dict:
        """
        إرسال موقع جغرافي - Send location - مقام بھیجیں
        """
        params = {
            "phone": recipient,
            "lat": lat,
            "lng": lng,
            "address": address,
        }
        if name:
            params["name"] = name
        return self._send_custom_path_request("message/location", params)

    def send_contact(self, recipient: str, contacts: list) -> dict:
        """
        إرسال جهة اتصال - Send contact - رابطہ بھیجیں
        contacts: [{"name":{"formatted_name":"...","first_name":"...","last_name":"..."},"phones":[{"phone":"+966...","type":"CELL"}]}]
        """
        return self._send_custom_path_request(
            "message/contact", {"phone": recipient, "contacts": contacts}
        )
