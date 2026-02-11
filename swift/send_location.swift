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
    // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
    // هيكل مختلف: path message/location مع params مباشرة
    // Different structure: path message/location with direct params
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
sendLocationMessage()
