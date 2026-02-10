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
