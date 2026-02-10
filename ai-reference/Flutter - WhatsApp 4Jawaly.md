# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Dart/Flutter باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Flutter/Dart using 4Jawaly

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

## التبعيات | pubspec.yaml

```yaml
name: whatsapp_4jawaly
description: 4Jawaly WhatsApp API Flutter/Dart client - عميل واتساب 4جوالي - 4Jawaly WhatsApp API کا Flutter/Dart کلائنٹ
version: 1.0.0

environment:
  sdk: '>=3.0.0 <4.0.0'

dependencies:
  http: ^1.1.0
```

## خدمة الواتساب | whatsapp_service.dart

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

/// WhatsApp Service for 4Jawaly API
/// خدمة واتساب لواجهة 4جوالي
/// 4Jawaly API کے لیے WhatsApp سروس
class WhatsAppService {
  /// App Key - مفتاح التطبيق - ایپ کی
  final String appKey;

  /// API Secret - سر التطبيق - API سیکرٹ
  final String apiSecret;

  /// Project ID - معرف المشروع - پروجیکٹ آئی ڈی
  final String projectId;

  /// Base URL for API - الرابط الأساسي للواجهة - API کا بنیادی URL
  static const String _baseUrl =
      'https://api-users.4jawaly.com/api/v1/whatsapp';

  /// Constructor - المُنشئ - کنسٹرکٹر
  /// [appKey] Application key - مفتاح التطبيق - ایپ کی
  /// [apiSecret] API secret - سر التطبيق - API سیکرٹ
  /// [projectId] Project identifier - معرف المشروع - پروجیکٹ آئی ڈی
  WhatsAppService({
    required this.appKey,
    required this.apiSecret,
    required this.projectId,
  });

  /// Make authenticated API request - تنفيذ طلب API مصادق عليه - تصدیق شدہ API درخواست
  /// [data] Request payload - بيانات الطلب - درخواست کا پے لوڈ
  Future<Map<String, dynamic>> _makeRequest(Map<String, dynamic> data) async {
    try {
      // Create Basic Auth header - إنشاء رأس المصادقة الأساسية - Basic Auth ہیڈر بنائیں
      final credentials = base64Encode(utf8.encode('$appKey:$apiSecret'));
      final authHeader = 'Basic $credentials';

      // Build request body - بناء جسم الطلب - درخواست کا جسم بنائیں
      final body = {
        'path': 'global',
        'params': {
          'url': 'messages',
          'method': 'post',
          'data': data,
        },
      };

      final url = Uri.parse('$_baseUrl/$projectId');
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': authHeader,
        },
        body: jsonEncode(body),
      );

      // Parse response body - تحليل الاستجابة - جواب کا تجزیہ
      dynamic parsedBody;
      try {
        parsedBody = response.body.isEmpty
            ? <String, dynamic>{}
            : jsonDecode(response.body);
      } catch (_) {
        parsedBody = {'raw': response.body};
      }

      return {
        'statusCode': response.statusCode,
        'body': parsedBody,
      };
    } catch (e) {
      return {
        'error': true,
        'message': e.toString(),
      };
    }
  }

  /// Send text message - إرسال رسالة نصية - ٹیکسٹ میسج بھیجیں
  /// [to] Recipient phone (e.g. 9665XXXXXXXX) - رقم المستلم - ٹیلی فون نمبر
  /// [text] Message body - نص الرسالة - میسج کا متن
  Future<Map<String, dynamic>> sendText(String to, String text) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'text',
      'text': {'body': text},
    };
    return _makeRequest(data);
  }

  /// Send interactive buttons - إرسال أزرار تفاعلية - تفاعلی بٹن بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [bodyText] Button list body text - نص جسم القائمة - بٹن کی فہرست کا متن
  /// [buttons] List of {id, title} - قائمة الأزرار - بٹنوں کی فہرست
  Future<Map<String, dynamic>> sendButtons(
    String to,
    String bodyText,
    List<Map<String, String>> buttons,
  ) async {
    final buttonList = buttons
        .map((b) => {
              'type': 'reply',
              'reply': {
                'id': b['id'] ?? '',
                'title': b['title'] ?? '',
              },
            })
        .toList();
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'interactive',
      'interactive': {
        'type': 'button',
        'body': {'text': bodyText},
        'action': {'buttons': buttonList},
      },
    };
    return _makeRequest(data);
  }

  /// Send interactive list - إرسال قائمة تفاعلية - تفاعلی فہرست بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [headerText] List header - عنوان القائمة - فہرست کا ہیڈر
  /// [bodyText] List body - نص جسم القائمة - فہرست کا متن
  /// [footerText] List footer - تذييل القائمة - فہرست کا فوٹر
  /// [buttonText] Action button text - نص زر العرض - بٹن کا متن
  /// [sections] List sections - أقسام القائمة - فہرست کے حصے
  Future<Map<String, dynamic>> sendList(
    String to, {
    required String headerText,
    required String bodyText,
    String? footerText,
    required String buttonText,
    required List<Map<String, dynamic>> sections,
  }) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'interactive',
      'interactive': {
        'type': 'list',
        'header': {'type': 'text', 'text': headerText},
        'body': {'text': bodyText},
        if (footerText != null) 'footer': {'text': footerText},
        'action': {
          'button': buttonText,
          'sections': sections,
        },
      },
    };
    return _makeRequest(data);
  }

  /// Send image - إرسال صورة - تصویر بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [link] Image URL - رابط الصورة - تصویر کا URL
  /// [caption] Optional caption - وصف اختياري - اختیاری کیپشن
  Future<Map<String, dynamic>> sendImage(
    String to,
    String link, {
    String? caption,
  }) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'image',
      'image': {
        'link': link,
        if (caption != null) 'caption': caption,
      },
    };
    return _makeRequest(data);
  }

  /// Send video - إرسال فيديو - ویڈیو بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [link] Video URL - رابط الفيديو - ویڈیو کا URL
  /// [caption] Optional caption - وصف اختياري - اختیاری کیپشن
  Future<Map<String, dynamic>> sendVideo(
    String to,
    String link, {
    String? caption,
  }) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'video',
      'video': {
        'link': link,
        if (caption != null) 'caption': caption,
      },
    };
    return _makeRequest(data);
  }

  /// Send audio - إرسال ملف صوتي - آڈیو بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [link] Audio URL - رابط الملف الصوتي - آڈیو کا URL
  Future<Map<String, dynamic>> sendAudio(String to, String link) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'audio',
      'audio': {'link': link},
    };
    return _makeRequest(data);
  }

  /// Send document - إرسال مستند - دستاویز بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [link] Document URL - رابط المستند - دستاویز کا URL
  /// [caption] Optional caption - وصف اختياري - اختیاری کیپشن
  /// [filename] Optional filename - اسم الملف - اختیاری فائل نام
  Future<Map<String, dynamic>> sendDocument(
    String to,
    String link, {
    String? caption,
    String? filename,
  }) async {
    final data = {
      'messaging_product': 'whatsapp',
      'to': to,
      'type': 'document',
      'document': {
        'link': link,
        if (caption != null) 'caption': caption,
        if (filename != null) 'filename': filename,
      },
    };
    return _makeRequest(data);
  }
}
```

## مثال الاستخدام | example_usage.dart

```dart
import 'whatsapp_service.dart';

/// Example usage of WhatsAppService - مثال استخدام خدمة واتساب - WhatsAppService کے استعمال کی مثال
void main() async {
  // Initialize service - تهيئة الخدمة - سروس شروع کریں
  // إنشاء مثيل WhatsAppService - Create WhatsAppService instance
  final whatsapp = WhatsAppService(
    appKey: 'YOUR_APP_KEY',
    apiSecret: 'YOUR_API_SECRET',
    projectId: 'YOUR_PROJECT_ID',
  );

  // Recipient phone (use with country code, no +) - رقم المستلم - وصول کنندہ کا نمبر
  const to = '9665XXXXXXXX';

  // 1. Send text message - إرسال رسالة نصية - ٹیکسٹ میسج بھیجیں
  final textResult = await whatsapp.sendText(to, 'نص الرسالة');
  print('Text: $textResult');

  // 2. Send interactive buttons - إرسال أزرار تفاعلية - تفاعلی بٹن بھیجیں
  final buttonsResult = await whatsapp.sendButtons(
    to,
    'اختر أحد الخيارات التالية',
    [
      {'id': 'btn_yes', 'title': 'نعم'},
      {'id': 'btn_no', 'title': 'لا'},
      {'id': 'btn_help', 'title': 'مساعدة'},
    ],
  );
  print('Buttons: $buttonsResult');

  // 3. Send interactive list - إرسال قائمة تفاعلية - تفاعلی فہرست بھیجیں
  final listResult = await whatsapp.sendList(
    to,
    headerText: 'قائمة الخدمات',
    bodyText: 'اختر الخدمة المطلوبة من القائمة أدناه',
    footerText: '4Jawaly Services',
    buttonText: 'عرض القائمة',
    sections: [
      {
        'title': 'الخدمات الأساسية',
        'rows': [
          {
            'id': 'svc_sms',
            'title': 'خدمة الرسائل النصية',
            'description': 'إرسال رسائل SMS للعملاء',
          },
          {
            'id': 'svc_whatsapp',
            'title': 'خدمة واتساب',
            'description': 'إرسال رسائل واتساب تفاعلية',
          },
        ],
      },
      {
        'title': 'الدعم الفني',
        'rows': [
          {
            'id': 'support_ticket',
            'title': 'فتح تذكرة دعم',
            'description': 'تواصل مع فريق الدعم الفني',
          },
        ],
      },
    ],
  );
  print('List: $listResult');

  // 4. Send image - إرسال صورة - تصویر بھیجیں
  final imageResult = await whatsapp.sendImage(
    to,
    'https://example.com/image.jpg',
    caption: 'وصف الصورة',
  );
  print('Image: $imageResult');

  // 5. Send video - إرسال فيديو - ویڈیو بھیجیں
  final videoResult = await whatsapp.sendVideo(
    to,
    'https://example.com/video.mp4',
    caption: 'وصف الفيديو',
  );
  print('Video: $videoResult');

  // 6. Send audio - إرسال ملف صوتي - آڈیو بھیجیں
  final audioResult =
      await whatsapp.sendAudio(to, 'https://example.com/audio.mp3');
  print('Audio: $audioResult');

  // 7. Send document - إرسال مستند - دستاویز بھیجیں
  final docResult = await whatsapp.sendDocument(
    to,
    'https://example.com/document.pdf',
    caption: 'وصف المستند',
    filename: 'document.pdf',
  );
  print('Document: $docResult');
}
```
