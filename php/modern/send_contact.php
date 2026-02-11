<?php
/**
 * إرسال جهة اتصال عبر واتساب
 * Send contact via WhatsApp
 * واٹس ایپ کے ذریعے رابطہ بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "966500000000";

// بيانات جهة الاتصال - Contact data - رابطہ کا ڈیٹا
$contacts = [
    [
        "name" => [
            "formatted_name" => "Ahmed Ali",
            "first_name" => "Ahmed",
            "last_name" => "Ali"
        ],
        "phones" => [
            [
                "phone" => "+966501234567",
                "type" => "CELL"
            ]
        ]
    ]
];

// بناء الطلب - Build request - درخواست بنائیں
// ملاحظة: جهة الاتصال تستخدم هيكل طلب مختلف عن الأنواع الأخرى
// Note: Contact uses a different request structure than other types
$base_url = "https://api-users.4jawaly.com/api/v1/whatsapp/{$project_id}";
$auth = base64_encode("{$app_key}:{$api_secret}");

$payload = [
    "path" => "message/contact",
    "params" => [
        "phone" => $recipient,
        "contacts" => $contacts
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
