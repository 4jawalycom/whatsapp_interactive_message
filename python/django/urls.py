#!/usr/bin/env python3
# مسارات واتساب - WhatsApp URL patterns - واٹس ایپ یو آر ایل پیٹرنز
# تضمين هذا الملف في config/urls.py عبر: path('whatsapp/', include('urls'))
# Include in config/urls.py via: path('whatsapp/', include('urls'))
# config/urls.py میں شامل کریں: path('whatsapp/', include('urls'))

from django.urls import path

from views import (
    send_audio,
    send_buttons,
    send_contact,
    send_document,
    send_image,
    send_list,
    send_location,
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
    path("location", send_location),
    path("contact", send_contact),
]
