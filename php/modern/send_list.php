<?php
/**
 * إرسال رسالة بقائمة تفاعلية عبر واتساب
 * Send interactive list message via WhatsApp
 * واٹس ایپ کے ذریعے انٹرایکٹو لسٹ پیغام بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// بناء الطلب - Build request - درخواست بنائیں
$base_url = "https://api-users.4jawaly.com/api/v1/whatsapp/{$project_id}";
$auth = base64_encode("{$app_key}:{$api_secret}");

$payload = [
    "path" => "global",
    "params" => [
        "url" => "messages",
        "method" => "post",
        "data" => [
            "messaging_product" => "whatsapp",
            "to" => $recipient,
            "type" => "interactive",
            "interactive" => [
                "type" => "list",
                "header" => [
                    "type" => "text",
                    "text" => "قائمة الخدمات"
                ],
                "body" => [
                    "text" => "اختر الخدمة المطلوبة من القائمة أدناه"
                ],
                "footer" => [
                    "text" => "4Jawaly Services"
                ],
                "action" => [
                    "button" => "عرض القائمة",
                    "sections" => [
                        [
                            "title" => "الخدمات الأساسية",
                            "rows" => [
                                [
                                    "id" => "svc_sms",
                                    "title" => "خدمة الرسائل النصية",
                                    "description" => "إرسال رسائل SMS للعملاء"
                                ],
                                [
                                    "id" => "svc_whatsapp",
                                    "title" => "خدمة واتساب",
                                    "description" => "إرسال رسائل واتساب تفاعلية"
                                ]
                            ]
                        ],
                        [
                            "title" => "الدعم الفني",
                            "rows" => [
                                [
                                    "id" => "support_ticket",
                                    "title" => "فتح تذكرة دعم",
                                    "description" => "تواصل مع فريق الدعم الفني"
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
];

// إرسال الطلب عبر cURL - Send request via cURL - cURL کے ذریعے درخواست بھیجیں
$ch = curl_init($base_url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => json_encode($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json",
        "Authorization: Basic {$auth}"
    ]
]);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

// معالجة النتيجة - Handle result - نتیجہ سنبھالیں
if ($error) {
    echo "خطأ في الاتصال: {$error}\n";
    echo "Connection error: {$error}\n";
    echo "رابطہ میں خرابی: {$error}\n";
    exit(1);
}

echo "رمز الاستجابة: {$http_code}\n";
echo "Response code: {$http_code}\n";
echo "جوابی کوڈ: {$http_code}\n";
echo "\nالاستجابة الكاملة:\nFull response:\nمکمل جواب:\n";
echo $response . "\n";
