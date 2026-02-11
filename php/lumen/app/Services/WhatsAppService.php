<?php

/**
 * خدمة إرسال رسائل واتساب عبر 4Jawaly API
 * WhatsApp messaging service via 4Jawaly API
 * 4Jawaly API کے ذریعے واٹس ایپ پیغامات بھیجنے کی سروس
 */

namespace App\Services;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

class WhatsAppService
{
    /** @var Client */
    private Client $client;

    /** @var string عنوان أساسي للـ API - Base API URL - API کا بنیادی URL */
    private string $baseUrl;

    /** @var string بيانات المصادقة - Auth credentials - تصدیق کی معلومات */
    private string $authHeader;

    /**
     * إنشاء الخدمة - Constructor - کنسٹرکٹر
     */
    public function __construct()
    {
        $appKey = env('APP_KEY', '');
        $apiSecret = env('API_SECRET', '');
        $projectId = env('PROJECT_ID', '');

        $this->baseUrl = "https://api-users.4jawaly.com/api/v1/whatsapp/{$projectId}";
        $this->authHeader = 'Basic ' . base64_encode("{$appKey}:{$apiSecret}");

        $this->client = new Client([
            'base_uri' => $this->baseUrl,
            'timeout' => 30,
            'headers' => [
                'Content-Type' => 'application/json',
                'Authorization' => $this->authHeader,
            ],
        ]);
    }

    /**
     * إرسال طلب للـ API - Make API request - API درخواست بھیجیں
     *
     * @param array $messageData بيانات الرسالة - Message data - پیغام کا ڈیٹا
     * @return array استجابة JSON - JSON response - JSON جواب
     */
    private function sendRequest(array $messageData): array
    {
        $payload = [
            'path' => 'global',
            'params' => [
                'url' => 'messages',
                'method' => 'post',
                'data' => array_merge(
                    [
                        'messaging_product' => 'whatsapp',
                        'to' => $messageData['to'] ?? '',
                    ],
                    $messageData['payload'] ?? []
                ),
            ],
        ];

        try {
            $response = $this->client->post('', [
                'json' => $payload,
            ]);
            $body = (string) $response->getBody();
            return json_decode($body, true) ?? ['raw' => $body];
        } catch (GuzzleException $e) {
            return [
                'error' => true,
                'message' => $e->getMessage(),
                'code' => $e->getCode(),
            ];
        }
    }

    /**
     * إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $body نص الرسالة - Message body - پیغام کا متن
     * @return array
     */
    public function sendText(string $recipient, string $body): array
    {
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'text',
                'text' => ['body' => $body],
            ],
        ]);
    }

    /**
     * إرسال رسالة بأزرار تفاعلية - Send interactive buttons - انٹرایکٹو بٹن بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $bodyText نص الجسم - Body text - جسم کا متن
     * @param array $buttons مصفوفة الأزرار - Buttons array - بٹنوں کا سرے
     * @return array
     */
    public function sendButtons(string $recipient, string $bodyText, array $buttons): array
    {
        $formattedButtons = [];
        foreach ($buttons as $btn) {
            $formattedButtons[] = [
                'type' => 'reply',
                'reply' => [
                    'id' => $btn['id'] ?? '',
                    'title' => $btn['title'] ?? '',
                ],
            ];
        }

        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'interactive',
                'interactive' => [
                    'type' => 'button',
                    'body' => ['text' => $bodyText],
                    'action' => ['buttons' => $formattedButtons],
                ],
            ],
        ]);
    }

    /**
     * إرسال رسالة بقائمة تفاعلية - Send interactive list - انٹرایکٹو لسٹ بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $headerText نص الترويسة - Header text - ہیڈر کا متن
     * @param string $bodyText نص الجسم - Body text - جسم کا متن
     * @param string $footerText نص التذييل - Footer text - فوٹر کا متن
     * @param string $buttonLabel تسمية زر القائمة - List button label - لسٹ بٹن لیبل
     * @param array $sections أقسام القائمة - List sections - لسٹ کے سیکشنز
     * @return array
     */
    public function sendList(
        string $recipient,
        string $headerText,
        string $bodyText,
        string $footerText,
        string $buttonLabel,
        array $sections
    ): array {
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'interactive',
                'interactive' => [
                    'type' => 'list',
                    'header' => ['type' => 'text', 'text' => $headerText],
                    'body' => ['text' => $bodyText],
                    'footer' => ['text' => $footerText],
                    'action' => [
                        'button' => $buttonLabel,
                        'sections' => $sections,
                    ],
                ],
            ],
        ]);
    }

    /**
     * إرسال صورة - Send image - تصویر بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $link رابط الصورة - Image link - تصویر کا لنک
     * @param string|null $caption وصف الصورة - Image caption - تصویر کا کیپشن
     * @return array
     */
    public function sendImage(string $recipient, string $link, ?string $caption = null): array
    {
        $image = ['link' => $link];
        if ($caption !== null) {
            $image['caption'] = $caption;
        }
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'image',
                'image' => $image,
            ],
        ]);
    }

    /**
     * إرسال فيديو - Send video - ویڈیو بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $link رابط الفيديو - Video link - ویڈیو کا لنک
     * @param string|null $caption وصف الفيديو - Video caption - ویڈیو کا کیپشن
     * @return array
     */
    public function sendVideo(string $recipient, string $link, ?string $caption = null): array
    {
        $video = ['link' => $link];
        if ($caption !== null) {
            $video['caption'] = $caption;
        }
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'video',
                'video' => $video,
            ],
        ]);
    }

    /**
     * إرسال ملف صوتي - Send audio - آڈیو بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $link رابط الملف الصوتي - Audio link - آڈیو کا لنک
     * @return array
     */
    public function sendAudio(string $recipient, string $link): array
    {
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'audio',
                'audio' => ['link' => $link],
            ],
        ]);
    }

    /**
     * إرسال مستند - Send document - دستاویز بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param string $link رابط المستند - Document link - دستاویز کا لنک
     * @param string|null $caption وصف المستند - Document caption - دستاویز کا کیپشن
     * @param string|null $filename اسم الملف - Filename - فائل کا نام
     * @return array
     */
    public function sendDocument(
        string $recipient,
        string $link,
        ?string $caption = null,
        ?string $filename = null
    ): array {
        $document = ['link' => $link];
        if ($caption !== null) {
            $document['caption'] = $caption;
        }
        if ($filename !== null) {
            $document['filename'] = $filename;
        }
        return $this->sendRequest([
            'to' => $recipient,
            'payload' => [
                'type' => 'document',
                'document' => $document,
            ],
        ]);
    }

    /**
     * إرسال طلب مسار مخصص - Send custom path request - مخصوص path درخواست بھیجیں
     * يستخدمه الموقع وجهة الاتصال (هيكل مختلف عن global)
     * Used by location and contact (different structure than global)
     *
     * @param string $path مسار الـ API - API path - API path
     * @param array $params المعاملات - Parameters - پیرامیٹرز
     * @return array
     */
    private function sendCustomPathRequest(string $path, array $params): array
    {
        $payload = [
            'path' => $path,
            'params' => $params,
        ];

        try {
            $response = $this->client->post('', [
                'json' => $payload,
            ]);
            $body = (string) $response->getBody();
            return json_decode($body, true) ?? ['raw' => $body];
        } catch (GuzzleException $e) {
            return [
                'error' => true,
                'message' => $e->getMessage(),
                'code' => $e->getCode(),
            ];
        }
    }

    /**
     * إرسال موقع جغرافي - Send location - مقام بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param float $lat خط العرض - Latitude - عرض البلد
     * @param float $lng خط الطول - Longitude - طول البلد
     * @param string $address العنوان - Address - پتہ
     * @param string|null $name اسم الموقع - Location name - مقام کا نام
     * @return array
     */
    public function sendLocation(
        string $recipient,
        float $lat,
        float $lng,
        string $address,
        ?string $name = null
    ): array {
        $params = [
            'phone' => $recipient,
            'lat' => $lat,
            'lng' => $lng,
            'address' => $address,
        ];
        if ($name !== null) {
            $params['name'] = $name;
        }
        return $this->sendCustomPathRequest('message/location', $params);
    }

    /**
     * إرسال جهة اتصال - Send contact - رابطہ بھیجیں
     *
     * @param string $recipient رقم المستلم - Recipient number - وصول کنندہ کا نمبر
     * @param array $contacts مصفوفة جهات الاتصال - Contacts array - رابطے کا سرے
     * @return array
     */
    public function sendContact(string $recipient, array $contacts): array
    {
        return $this->sendCustomPathRequest('message/contact', [
            'phone' => $recipient,
            'contacts' => $contacts,
        ]);
    }
}
