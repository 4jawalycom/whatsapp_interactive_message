<?php

/**
 * مسارات واتساب - WhatsApp routes - واٹس ایپ روٹس
 *
 * انسخ هذا الملف إلى routes/web.php أو استدعِه من bootstrap/app.php
 * Copy this file to routes/web.php or require it from bootstrap/app.php
 * اس فائل کو routes/web.php میں کاپی کریں یا bootstrap/app.php سے شامل کریں
 */

use App\Http\Controllers\WhatsAppController;

/*
|--------------------------------------------------------------------------
| POST /whatsapp/text - إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/text', [
    'uses' => [WhatsAppController::class, 'sendText'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/buttons - إرسال أزرار تفاعلية - Send buttons - بٹن بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/buttons', [
    'uses' => [WhatsAppController::class, 'sendButtons'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/list - إرسال قائمة تفاعلية - Send list - لسٹ بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/list', [
    'uses' => [WhatsAppController::class, 'sendList'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/image - إرسال صورة - Send image - تصویر بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/image', [
    'uses' => [WhatsAppController::class, 'sendImage'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/video - إرسال فيديو - Send video - ویڈیو بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/video', [
    'uses' => [WhatsAppController::class, 'sendVideo'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/audio - إرسال ملف صوتي - Send audio - آڈیو بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/audio', [
    'uses' => [WhatsAppController::class, 'sendAudio'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/document - إرسال مستند - Send document - دستاویز بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/document', [
    'uses' => [WhatsAppController::class, 'sendDocument'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/location - إرسال موقع جغرافي - Send location - مقام بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/location', [
    'uses' => [WhatsAppController::class, 'sendLocation'],
]);

/*
|--------------------------------------------------------------------------
| POST /whatsapp/contact - إرسال جهة اتصال - Send contact - رابطہ بھیجیں
|--------------------------------------------------------------------------
*/
$router->post('/whatsapp/contact', [
    'uses' => [WhatsAppController::class, 'sendContact'],
]);
