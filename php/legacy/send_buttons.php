<?php
/**
 * إرسال رسالة بأزرار تفاعلية عبر واتساب
 * Send interactive buttons message via WhatsApp
 * واٹس ایپ کے ذریعے انٹرایکٹو بٹن پیغام بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// بناء الطلب - Build request - درخواست بنائیں
$base_url = "https://api-users.4jawaly.com/api/v1/whatsapp/" . $project_id;
$auth = base64_encode($app_key . ":" . $api_secret);

$payload = array(
    "path" => "global",
    "params" => array(
        "url" => "messages",
        "method" => "post",
        "data" => array(
            "messaging_product" => "whatsapp",
            "to" => $recipient,
            "type" => "interactive",
            "interactive" => array(
                "type" => "button",
                "body" => array(
                    "text" => "اختر أحد الخيارات التالية"
                ),
                "action" => array(
                    "buttons" => array(
                        array("type" => "reply", "reply" => array("id" => "btn_yes", "title" => "نعم")),
                        array("type" => "reply", "reply" => array("id" => "btn_no", "title" => "لا")),
                        array("type" => "reply", "reply" => array("id" => "btn_help", "title" => "مساعدة"))
                    )
                )
            )
        )
    )
);

// إرسال الطلب عبر cURL - Send request via cURL - cURL کے ذریعے درخواست بھیجیں
$ch = curl_init($base_url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Content-Type: application/json",
    "Authorization: Basic " . $auth
));

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

// معالجة النتيجة - Handle result - نتیجہ سنبھالیں
if ($error) {
    echo "خطأ في الاتصال: " . $error . "\n";
    echo "Connection error: " . $error . "\n";
    echo "رابطہ میں خرابی: " . $error . "\n";
    exit(1);
}

echo "رمز الاستجابة: " . $http_code . "\n";
echo "Response code: " . $http_code . "\n";
echo "جوابی کوڈ: " . $http_code . "\n";
echo "\nالاستجابة الكاملة:\nFull response:\nمکمل جواب:\n";
echo $response . "\n";
