# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة PHP باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in PHP using 4Jawaly

## معلومات API | API Information
- Base URL: https://api-users.4jawaly.com/api/v1/whatsapp/{project_id}
- Method: POST
- Auth: Basic Auth (base64(app_key:api_secret))
- Content-Type: application/json

## أنواع الرسائل المدعومة | Supported Message Types
1. رسالة نصية (Text)
2. أزرار تفاعلية (Interactive Buttons) - حتى 3 أزرار
3. قائمة تفاعلية (Interactive List) - حتى 10 عناصر
4. صورة (Image)
5. فيديو (Video)
6. ملف صوتي (Audio)
7. مستند (Document)

---

## 1. PHP Modern (8.x+)

### إرسال رسالة نصية | send_text.php
```php
<?php
/**
 * إرسال رسالة نصية عبر واتساب
 * Send text message via WhatsApp
 * واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// محتوى الرسالة - Message content - پیغام کا مواد
$message_body = "نص الرسالة";

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
            "type" => "text",
            "text" => [
                "body" => $message_body
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
```

### إرسال أزرار تفاعلية | send_buttons.php
```php
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
                "type" => "button",
                "body" => [
                    "text" => "اختر أحد الخيارات التالية"
                ],
                "action" => [
                    "buttons" => [
                        ["type" => "reply", "reply" => ["id" => "btn_yes", "title" => "نعم"]],
                        ["type" => "reply", "reply" => ["id" => "btn_no", "title" => "لا"]],
                        ["type" => "reply", "reply" => ["id" => "btn_help", "title" => "مساعدة"]]
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
```

### إرسال قائمة تفاعلية | send_list.php
```php
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
```

### إرسال صورة | send_image.php
```php
<?php
/**
 * إرسال صورة عبر واتساب
 * Send image via WhatsApp
 * واٹس ایپ کے ذریعے تصویر بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الصورة والوصف - Image URL and caption - تصویر کا لنک اور کیپشن
$image_url = "https://example.com/image.jpg";
$image_caption = "وصف الصورة";

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
            "type" => "image",
            "image" => [
                "link" => $image_url,
                "caption" => $image_caption
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
```

### إرسال فيديو | send_video.php
```php
<?php
/**
 * إرسال فيديو عبر واتساب
 * Send video via WhatsApp
 * واٹس ایپ کے ذریعے ویڈیو بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الفيديو والوصف - Video URL and caption - ویڈیو کا لنک اور کیپشن
$video_url = "https://example.com/video.mp4";
$video_caption = "وصف الفيديو";

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
            "type" => "video",
            "video" => [
                "link" => $video_url,
                "caption" => $video_caption
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
```

### إرسال ملف صوتي | send_audio.php
```php
<?php
/**
 * إرسال ملف صوتي عبر واتساب
 * Send audio file via WhatsApp
 * واٹس ایپ کے ذریعے آڈیو فائل بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الملف الصوتي - Audio file URL - آڈیو فائل کا لنک
$audio_url = "https://example.com/audio.mp3";

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
            "type" => "audio",
            "audio" => [
                "link" => $audio_url
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
```

### إرسال مستند | send_document.php
```php
<?php
/**
 * إرسال مستند عبر واتساب
 * Send document via WhatsApp
 * واٹس ایپ کے ذریعے دستاویز بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط المستند والوصف واسم الملف - Document URL, caption and filename - دستاویز کا لنک، کیپشن اور فائل کا نام
$document_url = "https://example.com/document.pdf";
$document_caption = "وصف المستند";
$document_filename = "document.pdf";

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
            "type" => "document",
            "document" => [
                "link" => $document_url,
                "caption" => $document_caption,
                "filename" => $document_filename
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
```

---

## 2. PHP Legacy (5.6/7.x)

### إرسال رسالة نصية | send_text.php
```php
<?php
/**
 * إرسال رسالة نصية عبر واتساب
 * Send text message via WhatsApp
 * واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// محتوى الرسالة - Message content - پیغام کا مواد
$message_body = "نص الرسالة";

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
            "type" => "text",
            "text" => array(
                "body" => $message_body
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
```

### إرسال أزرار تفاعلية | send_buttons.php
```php
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
```

### إرسال قائمة تفاعلية | send_list.php
```php
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
```

### إرسال صورة | send_image.php
```php
<?php
/**
 * إرسال صورة عبر واتساب
 * Send image via WhatsApp
 * واٹس ایپ کے ذریعے تصویر بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الصورة والوصف - Image URL and caption - تصویر کا لنک اور کیپشن
$image_url = "https://example.com/image.jpg";
$image_caption = "وصف الصورة";

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
            "type" => "image",
            "image" => array(
                "link" => $image_url,
                "caption" => $image_caption
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
```

### إرسال فيديو | send_video.php
```php
<?php
/**
 * إرسال فيديو عبر واتساب
 * Send video via WhatsApp
 * واٹس ایپ کے ذریعے ویڈیو بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الفيديو والوصف - Video URL and caption - ویڈیو کا لنک اور کیپشن
$video_url = "https://example.com/video.mp4";
$video_caption = "وصف الفيديو";

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
            "type" => "video",
            "video" => array(
                "link" => $video_url,
                "caption" => $video_caption
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
```

### إرسال ملف صوتي | send_audio.php
```php
<?php
/**
 * إرسال ملف صوتي عبر واتساب
 * Send audio file via WhatsApp
 * واٹس ایپ کے ذریعے آڈیو فائل بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط الملف الصوتي - Audio file URL - آڈیو فائل کا لنک
$audio_url = "https://example.com/audio.mp3";

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
            "type" => "audio",
            "audio" => array(
                "link" => $audio_url
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
```

### إرسال مستند | send_document.php
```php
<?php
/**
 * إرسال مستند عبر واتساب
 * Send document via WhatsApp
 * واٹس ایپ کے ذریعے دستاویز بھیجیں
 */

// إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
$app_key = "your_app_key";
$api_secret = "your_api_secret";
$project_id = "your_project_id";
$recipient = "9665XXXXXXXX";

// رابط المستند والوصف واسم الملف - Document URL, caption and filename - دستاویز کا لنک، کیپشن اور فائل کا نام
$document_url = "https://example.com/document.pdf";
$document_caption = "وصف المستند";
$document_filename = "document.pdf";

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
            "type" => "document",
            "document" => array(
                "link" => $document_url,
                "caption" => $document_caption,
                "filename" => $document_filename
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
```

---

## 3. PHP Lumen Framework

### خدمة الواتساب | WhatsAppService.php
```php
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
}
```

### المتحكم | WhatsAppController.php
```php
<?php

/**
 * وحدة تحكم رسائل واتساب - WhatsApp message controller
 * واٹس ایپ پیغامات کنٹرولر
 */

namespace App\Http\Controllers;

use App\Services\WhatsAppService;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class WhatsAppController extends Controller
{
    /** @var WhatsAppService */
    private WhatsAppService $whatsAppService;

    /**
     * حقن الخدمة - Service injection - سروس انجیکشن
     */
    public function __construct(WhatsAppService $whatsAppService)
    {
        $this->whatsAppService = $whatsAppService;
    }

    /**
     * إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendText(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'body' => 'required|string',
        ]);

        $response = $this->whatsAppService->sendText(
            $validated['to'],
            $validated['body']
        );

        return response()->json($response);
    }

    /**
     * إرسال رسالة بأزرار - Send buttons message - بٹن پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendButtons(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'body' => 'required|string',
            'buttons' => 'required|array',
            'buttons.*.id' => 'required|string',
            'buttons.*.title' => 'required|string',
        ]);

        $response = $this->whatsAppService->sendButtons(
            $validated['to'],
            $validated['body'],
            $validated['buttons']
        );

        return response()->json($response);
    }

    /**
     * إرسال رسالة بقائمة - Send list message - لسٹ پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendList(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'header' => 'required|string',
            'body' => 'required|string',
            'footer' => 'required|string',
            'button' => 'required|string',
            'sections' => 'required|array',
            'sections.*.title' => 'required|string',
            'sections.*.rows' => 'required|array',
            'sections.*.rows.*.id' => 'required|string',
            'sections.*.rows.*.title' => 'required|string',
            'sections.*.rows.*.description' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendList(
            $validated['to'],
            $validated['header'],
            $validated['body'],
            $validated['footer'],
            $validated['button'],
            $validated['sections']
        );

        return response()->json($response);
    }

    /**
     * إرسال صورة - Send image - تصویر بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendImage(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendImage(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null
        );

        return response()->json($response);
    }

    /**
     * إرسال فيديو - Send video - ویڈیو بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendVideo(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendVideo(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null
        );

        return response()->json($response);
    }

    /**
     * إرسال ملف صوتي - Send audio - آڈیو بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendAudio(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
        ]);

        $response = $this->whatsAppService->sendAudio(
            $validated['to'],
            $validated['link']
        );

        return response()->json($response);
    }

    /**
     * إرسال مستند - Send document - دستاویز بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendDocument(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
            'filename' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendDocument(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null,
            $validated['filename'] ?? null
        );

        return response()->json($response);
    }
}
```

### المسارات | routes.php
```php
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
```
