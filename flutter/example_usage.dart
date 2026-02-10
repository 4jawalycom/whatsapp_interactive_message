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
