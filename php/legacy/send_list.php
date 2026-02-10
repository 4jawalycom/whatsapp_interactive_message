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
                "type" => "list",
                "header" => array(
                    "type" => "text",
                    "text" => "قائمة الخدمات"
                ),
                "body" => array(
                    "text" => "اختر الخدمة المطلوبة من القائمة أدناه"
                ),
                "footer" => array(
                    "text" => "4Jawaly Services"
                ),
                "action" => array(
                    "button" => "عرض القائمة",
                    "sections" => array(
                        array(
                            "title" => "الخدمات الأساسية",
                            "rows" => array(
                                array(
                                    "id" => "svc_sms",
                                    "title" => "خدمة الرسائل النصية",
                                    "description" => "إرسال رسائل SMS للعملاء"
                                ),
                                array(
                                    "id" => "svc_whatsapp",
                                    "title" => "خدمة واتساب",
                                    "description" => "إرسال رسائل واتساب تفاعلية"
                                )
                            )
                        ),
                        array(
                            "title" => "الدعم الفني",
                            "rows" => array(
                                array(
                                    "id" => "support_ticket",
                                    "title" => "فتح تذكرة دعم",
                                    "description" => "تواصل مع فريق الدعم الفني"
                                )
                            )
                        )
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
