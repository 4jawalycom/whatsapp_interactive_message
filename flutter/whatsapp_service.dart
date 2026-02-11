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

  /// Make custom path API request - طلب API مع مسار مخصص - کسٹم پاتھ API درخواست
  /// Used for location/contact - different structure (path + direct params)
  /// [path] API path (e.g. message/location, message/contact) - المسار - API پاتھ
  /// [params] Direct params object - المعاملات المباشرة - براہ راست پیرامیٹرز
  Future<Map<String, dynamic>> _makeCustomPathRequest(
    String path,
    Map<String, dynamic> params,
  ) async {
    try {
      final credentials = base64Encode(utf8.encode('$appKey:$apiSecret'));
      final authHeader = 'Basic $credentials';

      final body = {'path': path, 'params': params};

      final url = Uri.parse('$_baseUrl/$projectId');
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': authHeader,
        },
        body: jsonEncode(body),
      );

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

  /// Send location - إرسال موقع جغرافي - مقام بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [lat] Latitude - خط العرض - عرض البلد
  /// [lng] Longitude - خط الطول - طول البلد
  /// [address] Optional address - العنوان - پتہ (اختیاری)
  /// [name] Optional name - الاسم - نام (اختیاری)
  Future<Map<String, dynamic>> sendLocation(
    String to,
    double lat,
    double lng, {
    String? address,
    String? name,
  }) async {
    final params = <String, dynamic>{
      'phone': to,
      'lat': lat,
      'lng': lng,
    };
    if (address != null) params['address'] = address;
    if (name != null) params['name'] = name;
    return _makeCustomPathRequest('message/location', params);
  }

  /// Send contact - إرسال جهة اتصال - رابطہ بھیجیں
  /// [to] Recipient phone - رقم المستلم - ٹیلی فون نمبر
  /// [contacts] List of contact objects - قائمة جهات الاتصال - رابطوں کی فہرست
  Future<Map<String, dynamic>> sendContact(
    String to,
    List<Map<String, dynamic>> contacts,
  ) async {
    final params = {
      'phone': to,
      'contacts': contacts,
    };
    return _makeCustomPathRequest('message/contact', params);
  }
}
