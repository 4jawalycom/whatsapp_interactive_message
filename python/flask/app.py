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
