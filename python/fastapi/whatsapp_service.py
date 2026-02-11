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

    async def _send_custom_path_request(
        self, path: str, params: dict[str, Any]
    ) -> dict[str, Any]:
        """
        إرسال طلب مسار مخصص - Send custom path request - مخصوص path درخواست بھیجیں
        يستخدمه الموقع وجهة الاتصال (هيكل مختلف عن global)
        Used by location and contact (different structure than global)
        """
        payload = {"path": path, "params": params}
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

    async def send_location(
        self,
        recipient: str,
        lat: float,
        lng: float,
        address: str,
        name: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        إرسال موقع جغرافي - Send location - مقام بھیجیں
        """
        params: dict[str, Any] = {
            "phone": recipient,
            "lat": lat,
            "lng": lng,
            "address": address,
        }
        if name:
            params["name"] = name
        return await self._send_custom_path_request("message/location", params)

    async def send_contact(
        self, recipient: str, contacts: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        إرسال جهة اتصال - Send contact - رابطہ بھیجیں
        contacts: [{"name":{"formatted_name":"...","first_name":"...","last_name":"..."},"phones":[{"phone":"+966...","type":"CELL"}]}]
        """
        return await self._send_custom_path_request(
            "message/contact", {"phone": recipient, "contacts": contacts}
        )
