// Main entry point / نقطة الدخول الرئيسية / مین انٹری پوائنٹ
// 4Jawaly WhatsApp API - .NET Sample / مثال واتساب 4جوالية / 4جوالی واٹس ایپ نمونہ

using WhatsApp4Jawaly;

// === تكوين / Configuration / کنفیگریشن ===
const string AppKey = "YOUR_APP_KEY";
const string ApiSecret = "YOUR_API_SECRET";
const string ProjectId = "YOUR_PROJECT_ID";
const string Recipient = "9665XXXXXXXX";

var service = new WhatsAppService(AppKey, ApiSecret, ProjectId);

try
{
    // 1. إرسال رسالة نصية / Send text message / ٹیکسٹ میسج بھیجیں
    var textResponse = await service.SendTextAsync(Recipient, "نص الرسالة");
    Console.WriteLine($"[Text] {textResponse}");

    // 2. إرسال أزرار تفاعلية / Send interactive buttons / انٹرایکٹو بٹن بھیجیں
    var buttons = new[] { ("btn_yes", "نعم"), ("btn_no", "لا"), ("btn_help", "مساعدة") };
    var buttonsResponse = await service.SendButtonsAsync(Recipient, "اختر أحد الخيارات التالية", buttons);
    Console.WriteLine($"[Buttons] {buttonsResponse}");

    // 3. إرسال قائمة تفاعلية / Send interactive list / انٹرایکٹو لسٹ بھیجیں
    var sections = new[]
    {
        ("الخدمات الأساسية", new[] {
            ("svc_sms", "خدمة الرسائل النصية", "إرسال رسائل SMS للعملاء"),
            ("svc_whatsapp", "خدمة واتساب", "إرسال رسائل واتساب تفاعلية")
        }),
        ("الدعم الفني", new[] {
            ("support_ticket", "فتح تذكرة دعم", "تواصل مع فريق الدعم الفني")
        })
    };
    var listResponse = await service.SendListAsync(
        Recipient,
        buttonText: "عرض القائمة",
        bodyText: "اختر الخدمة المطلوبة من القائمة أدناه",
        headerText: "قائمة الخدمات",
        footerText: "4Jawaly Services",
        sections);
    Console.WriteLine($"[List] {listResponse}");

    // 4. إرسال صورة / Send image / تصویر بھیجیں
    var imageResponse = await service.SendImageAsync(
        Recipient,
        "https://example.com/image.jpg",
        "وصف الصورة");
    Console.WriteLine($"[Image] {imageResponse}");

    // 5. إرسال فيديو / Send video / ویڈیو بھیجیں
    var videoResponse = await service.SendVideoAsync(
        Recipient,
        "https://example.com/video.mp4",
        "وصف الفيديو");
    Console.WriteLine($"[Video] {videoResponse}");

    // 6. إرسال ملف صوتي / Send audio / آڈیو بھیجیں
    var audioResponse = await service.SendAudioAsync(Recipient, "https://example.com/audio.mp3");
    Console.WriteLine($"[Audio] {audioResponse}");

    // 7. إرسال مستند / Send document / دستاویز بھیجیں
    var documentResponse = await service.SendDocumentAsync(
        Recipient,
        "https://example.com/document.pdf",
        caption: "وصف المستند",
        filename: "document.pdf");
    Console.WriteLine($"[Document] {documentResponse}");
}
catch (Exception ex)
{
    // معالجة الأخطاء / Error handling / نقص کی ہینڈلنگ
    Console.WriteLine($"Error / خطأ / نقص: {ex.Message}");
}
