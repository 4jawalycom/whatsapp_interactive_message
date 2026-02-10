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
