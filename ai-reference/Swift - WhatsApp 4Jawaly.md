# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Swift باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Swift using 4Jawaly

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
8. موقع جغرافي (Location)
9. جهة اتصال (Contact)

---

## إرسال رسالة نصية | send_text.swift
```swift
#!/usr/bin/env swift
// Send Text Message - إرسال رسالة نصية - ٹیکسٹ میسج بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send text message - إرسال رسالة نصية - ٹیکسٹ میسج بھیجیں
func sendTextMessage() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "text",
                "text": [
                    "body": "نص الرسالة"
                ]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendTextMessage()
```

---

## إرسال أزرار تفاعلية | send_buttons.swift
```swift
#!/usr/bin/env swift
// Send Interactive Buttons - إرسال أزرار تفاعلية - انٹرایکٹو بٹن بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send interactive buttons - إرسال أزرار تفاعلية - انٹرایکٹو بٹن بھیجیں
func sendInteractiveButtons() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "interactive",
                "interactive": [
                    "type": "button",
                    "body": [
                        "text": "اختر أحد الخيارات التالية"
                    ],
                    "action": [
                        "buttons": [
                            ["type": "reply", "reply": ["id": "btn_yes", "title": "نعم"]],
                            ["type": "reply", "reply": ["id": "btn_no", "title": "لا"]],
                            ["type": "reply", "reply": ["id": "btn_help", "title": "مساعدة"]]
                        ]
                    ] as [String: Any]
                ] as [String: Any]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendInteractiveButtons()
```

---

## إرسال قائمة تفاعلية | send_list.swift
```swift
#!/usr/bin/env swift
// Send Interactive List - إرسال قائمة تفاعلية - انٹرایکٹو لسٹ بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send interactive list - إرسال قائمة تفاعلية - انٹرایکٹو لسٹ بھیجیں
func sendInteractiveList() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "interactive",
                "interactive": [
                    "type": "list",
                    "header": [
                        "type": "text",
                        "text": "قائمة الخدمات"
                    ],
                    "body": [
                        "text": "اختر الخدمة المطلوبة من القائمة أدناه"
                    ],
                    "footer": [
                        "text": "4Jawaly Services"
                    ],
                    "action": [
                        "button": "عرض القائمة",
                        "sections": [
                            [
                                "title": "الخدمات الأساسية",
                                "rows": [
                                    ["id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"],
                                    ["id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"]
                                ]
                            ],
                            [
                                "title": "الدعم الفني",
                                "rows": [
                                    ["id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"]
                                ]
                            ]
                        ]
                    ] as [String: Any]
                ] as [String: Any]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendInteractiveList()
```

---

## إرسال صورة | send_image.swift
```swift
#!/usr/bin/env swift
// Send Image - إرسال صورة - تصویر بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send image message - إرسال صورة - تصویر بھیجیں
func sendImageMessage() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "image",
                "image": [
                    "link": "https://example.com/image.jpg",
                    "caption": "وصف الصورة"
                ]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendImageMessage()
```

---

## إرسال فيديو | send_video.swift
```swift
#!/usr/bin/env swift
// Send Video - إرسال فيديو - ویڈیو بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send video message - إرسال فيديو - ویڈیو بھیجیں
func sendVideoMessage() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "video",
                "video": [
                    "link": "https://example.com/video.mp4",
                    "caption": "وصف الفيديو"
                ]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendVideoMessage()
```

---

## إرسال ملف صوتي | send_audio.swift
```swift
#!/usr/bin/env swift
// Send Audio - إرسال ملف صوتي - آڈیو بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send audio message - إرسال ملف صوتي - آڈیو بھیجیں
func sendAudioMessage() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "audio",
                "audio": [
                    "link": "https://example.com/audio.mp3"
                ]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendAudioMessage()
```

---

## إرسال مستند | send_document.swift
```swift
#!/usr/bin/env swift
// Send Document - إرسال مستند - دستاویز بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "9665XXXXXXXX"

// Send document message - إرسال مستند - دستاویز بھیجیں
func sendDocumentMessage() {
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    let payload: [String: Any] = [
        "path": "global",
        "params": [
            "url": "messages",
            "method": "post",
            "data": [
                "messaging_product": "whatsapp",
                "to": recipient,
                "type": "document",
                "document": [
                    "link": "https://example.com/document.pdf",
                    "caption": "وصف المستند",
                    "filename": "document.pdf"
                ]
            ] as [String: Any]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    // Basic Auth - المصادقة الأساسية - بنیادی تصدیق
    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

// Main execution - التنفيذ الرئيسي - بنیادی عمل
sendDocumentMessage()
```

---

## إرسال موقع جغرافي | send_location.swift
```swift
#!/usr/bin/env swift
// Send Location Message - إرسال موقع جغرافي - مقام بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال
// Note: Location uses path "message/location" - different structure - هيكل مختلف

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "966500000000"

// Location data - بيانات الموقع - مقام کا ڈیٹا
let lat = 24.7136
let lng = 46.6753
let address = "Riyadh, Saudi Arabia"
let name = "My Office"

// Send location message - إرسال موقع جغرافي - مقام بھیجیں
func sendLocationMessage() {
    let payload: [String: Any] = [
        "path": "message/location",
        "params": [
            "phone": recipient,
            "lat": lat,
            "lng": lng,
            "address": address,
            "name": name
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

sendLocationMessage()
```

---

## إرسال جهة اتصال | send_contact.swift
```swift
#!/usr/bin/env swift
// Send Contact Message - إرسال جهة اتصال - رابطہ بھیجیں
// Uses Foundation URLSession only - استخدام Foundation URLSession فقط - صرف Foundation URLSession استعمال
// Note: Contact uses path "message/contact" - different structure - هيكل مختلف

import Foundation

// Config - الإعدادات - ترتیبات
let appKey = "YOUR_APP_KEY"
let apiSecret = "YOUR_API_SECRET"
let projectId = "YOUR_PROJECT_ID"
let recipient = "966500000000"

// Send contact message - إرسال جهة اتصال - رابطہ بھیجیں
func sendContactMessage() {
    let payload: [String: Any] = [
        "path": "message/contact",
        "params": [
            "phone": recipient,
            "contacts": [
                [
                    "name": [
                        "formatted_name": "Ahmed Ali",
                        "first_name": "Ahmed",
                        "last_name": "Ali"
                    ] as [String: String],
                    "phones": [
                        [
                            "phone": "+966501234567",
                            "type": "CELL"
                        ] as [String: String]
                    ] as [[String: String]]
                ] as [String: Any]
            ] as [[String: Any]]
        ] as [String: Any]
    ]

    performRequest(payload: payload)
}

// Perform HTTP POST request - تنفيذ طلب HTTP - HTTP درخواست بھیجیں
func performRequest(payload: [String: Any]) {
    guard let url = URL(string: "https://api-users.4jawaly.com/api/v1/whatsapp/\(projectId)") else {
        print("Invalid URL - عنوان غير صالح - غلط یوآرایل")
        return
    }

    guard let jsonData = try? JSONSerialization.data(withJSONObject: payload) else {
        print("JSON serialization error - خطأ في تحويل JSON - JSON سیریلائزیشن کی خرابی")
        return
    }

    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    let credentials = "\(appKey):\(apiSecret)"
    guard let credData = credentials.data(using: .utf8) else {
        print("Credentials encoding error - خطأ في ترميز الاعتماد - تصدیق کی خرابی")
        return
    }
    let base64Auth = credData.base64EncodedString()
    request.setValue("Basic \(base64Auth)", forHTTPHeaderField: "Authorization")
    request.httpBody = jsonData

    let semaphore = DispatchSemaphore(value: 0)
    var statusCode: Int = 0
    var responseBody: String = ""

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        defer { semaphore.signal() }

        if let error = error {
            print("Request failed - فشل الطلب - درخواست ناکام: \(error.localizedDescription)")
            return
        }

        if let httpResponse = response as? HTTPURLResponse {
            statusCode = httpResponse.statusCode
        }

        if let data = data, let body = String(data: data, encoding: .utf8) {
            responseBody = body
        }
    }
    task.resume()
    semaphore.wait()

    print("Status: \(statusCode)")
    print("Response: \(responseBody)")
}

sendContactMessage()
```
