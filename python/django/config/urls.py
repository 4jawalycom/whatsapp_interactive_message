#!/usr/bin/env python3
# المسارات الرئيسية - Main URL configuration - مرکزی یو آر ایل کنفیگریشن

from django.urls import include, path

urlpatterns = [
    path("whatsapp/", include("urls")),
]
