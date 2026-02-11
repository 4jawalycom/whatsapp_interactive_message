using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace WhatsApp4Jawaly;

/// <summary>
/// 4Jawaly WhatsApp API Service / خدمة واتساب 4جوالية / 4جوالی واٹس ایپ سروس
/// </summary>
public class WhatsAppService
{
    private readonly HttpClient _httpClient;
    private readonly string _baseUrl;
    private readonly string _authHeader;

    /// <summary>
    /// Creates a new WhatsAppService instance / إنشاء مثيل جديد للخدمة / نیا سروس انسٹینس بنائیں
    /// </summary>
    /// <param name="appKey">4Jawaly App Key / مفتاح التطبيق / ایپ کی</param>
    /// <param name="apiSecret">4Jawaly API Secret / سر التطبيق / API سیکرٹ</param>
    /// <param name="projectId">4Jawaly Project ID / معرف المشروع / پراجیکٹ آئی ڈی</param>
    public WhatsAppService(string appKey, string apiSecret, string projectId)
    {
        // إنشاء عنوان URL الأساسي / Build base URL / بنیادی URL بنائیں
        _baseUrl = $"https://api-users.4jawaly.com/api/v1/whatsapp/{projectId}";
        _authHeader = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{appKey}:{apiSecret}"));
        _httpClient = new HttpClient();
        _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", _authHeader);
        _httpClient.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
    }

    /// <summary>
    /// Sends custom path API request - طلب API مع مسار مخصص - کسٹم پاتھ API درخواست
    /// Used for location/contact - different structure (path + direct params)
    /// path: message/location or message/contact - المسار - API پاتھ
    /// </summary>
    private async Task<string> MakeCustomPathRequestAsync(string path, JsonObject params)
    {
        try
        {
            var body = new JsonObject
            {
                ["path"] = path,
                ["params"] = params
            };

            var json = JsonSerializer.Serialize(body, new JsonSerializerOptions { WriteIndented = false });
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await _httpClient.PostAsync(_baseUrl, content);

            return await response.Content.ReadAsStringAsync();
        }
        catch (Exception ex)
        {
            throw new InvalidOperationException($"API Request failed / فشل الطلب: {ex.Message}", ex);
        }
    }

    /// <summary>
    /// Sends the API request / إرسال طلب API / API درخواست بھیجیں
    /// </summary>
    private async Task<string> MakeRequestAsync(JsonObject data)
    {
        try
        {
            var body = new JsonObject
            {
                ["path"] = "global",
                ["params"] = new JsonObject
                {
                    ["url"] = "messages",
                    ["method"] = "post",
                    ["data"] = data
                }
            };

            var json = JsonSerializer.Serialize(body, new JsonSerializerOptions { WriteIndented = false });
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await _httpClient.PostAsync(_baseUrl, content);

            return await response.Content.ReadAsStringAsync();
        }
        catch (Exception ex)
        {
            // معالجة الأخطاء / Error handling / نقص کی ہینڈلنگ
            throw new InvalidOperationException($"API Request failed / فشل الطلب: {ex.Message}", ex);
        }
    }

    /// <summary>
    /// Sends a text message / إرسال رسالة نصية / ٹیکسٹ میسج بھیجیں
    /// </summary>
    /// <param name="recipient">Phone number (e.g. 9665XXXXXXXX) / رقم الهاتف / فون نمبر</param>
    /// <param name="body">Message text / نص الرسالة / میسج کا متن</param>
    public async Task<string> SendTextAsync(string recipient, string body)
    {
        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "text",
            ["text"] = new JsonObject { ["body"] = body }
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends interactive buttons / إرسال أزرار تفاعلية / انٹرایکٹو بٹن بھیجیں
    /// </summary>
    /// <param name="recipient">Phone number / رقم الهاتف / فون نمبر</param>
    /// <param name="bodyText">Body text / نص المحتوى / باڈی ٹیکسٹ</param>
    /// <param name="buttons">List of (id, title) / قائمة الأزرار / بٹنوں کی فہرست</param>
    public async Task<string> SendButtonsAsync(string recipient, string bodyText, IEnumerable<(string id, string title)> buttons)
    {
        var buttonsArray = new JsonArray();
        foreach (var (id, title) in buttons)
        {
            buttonsArray.Add(new JsonObject
            {
                ["type"] = "reply",
                ["reply"] = new JsonObject { ["id"] = id, ["title"] = title }
            });
        }

        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "interactive",
            ["interactive"] = new JsonObject
            {
                ["type"] = "button",
                ["body"] = new JsonObject { ["text"] = bodyText },
                ["action"] = new JsonObject { ["buttons"] = buttonsArray }
            }
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends interactive list / إرسال قائمة تفاعلية / انٹرایکٹو لسٹ بھیجیں
    /// </summary>
    /// <param name="recipient">Phone number / رقم الهاتف / فون نمبر</param>
    /// <param name="buttonText">List button text / نص زر القائمة / لسٹ بٹن ٹیکسٹ</param>
    /// <param name="bodyText">Body text / نص المحتوى / باڈی ٹیکسٹ</param>
    /// <param name="headerText">Optional header / عنوان اختياري / ہیڈر (اختیاری)</param>
    /// <param name="footerText">Optional footer / تذييل اختياري / فوٹر (اختیاری)</param>
    /// <param name="sections">Sections: Title -> Rows (id, title, description) / الأقسام / سیکشنز</param>
    public async Task<string> SendListAsync(
        string recipient,
        string buttonText,
        string bodyText,
        string? headerText,
        string? footerText,
        IEnumerable<(string sectionTitle, IEnumerable<(string id, string title, string? description)> rows)> sections)
    {
        var sectionsArray = new JsonArray();
        foreach (var (sectionTitle, rows) in sections)
        {
            var rowsArray = new JsonArray();
            foreach (var (id, title, description) in rows)
            {
                var row = new JsonObject { ["id"] = id, ["title"] = title };
                if (!string.IsNullOrEmpty(description))
                    row["description"] = description;
                rowsArray.Add(row);
            }
            sectionsArray.Add(new JsonObject
            {
                ["title"] = sectionTitle,
                ["rows"] = rowsArray
            });
        }

        var interactive = new JsonObject
        {
            ["type"] = "list",
            ["body"] = new JsonObject { ["text"] = bodyText },
            ["action"] = new JsonObject
            {
                ["button"] = buttonText,
                ["sections"] = sectionsArray
            }
        };

        if (!string.IsNullOrEmpty(headerText))
            interactive["header"] = new JsonObject { ["type"] = "text", ["text"] = headerText };
        if (!string.IsNullOrEmpty(footerText))
            interactive["footer"] = new JsonObject { ["text"] = footerText };

        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "interactive",
            ["interactive"] = interactive
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends an image / إرسال صورة / تصویر بھیجیں
    /// </summary>
    public async Task<string> SendImageAsync(string recipient, string link, string? caption = null)
    {
        var image = new JsonObject { ["link"] = link };
        if (!string.IsNullOrEmpty(caption))
            image["caption"] = caption;

        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "image",
            ["image"] = image
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends a video / إرسال فيديو / ویڈیو بھیجیں
    /// </summary>
    public async Task<string> SendVideoAsync(string recipient, string link, string? caption = null)
    {
        var video = new JsonObject { ["link"] = link };
        if (!string.IsNullOrEmpty(caption))
            video["caption"] = caption;

        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "video",
            ["video"] = video
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends audio / إرسال ملف صوتي / آڈیو بھیجیں
    /// </summary>
    public async Task<string> SendAudioAsync(string recipient, string link)
    {
        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "audio",
            ["audio"] = new JsonObject { ["link"] = link }
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends a document / إرسال مستند / دستاویز بھیجیں
    /// </summary>
    public async Task<string> SendDocumentAsync(string recipient, string link, string? caption = null, string? filename = null)
    {
        var document = new JsonObject { ["link"] = link };
        if (!string.IsNullOrEmpty(caption))
            document["caption"] = caption;
        if (!string.IsNullOrEmpty(filename))
            document["filename"] = filename;

        var data = new JsonObject
        {
            ["messaging_product"] = "whatsapp",
            ["to"] = recipient,
            ["type"] = "document",
            ["document"] = document
        };
        return await MakeRequestAsync(data);
    }

    /// <summary>
    /// Sends a location / إرسال موقع جغرافي / مقام بھیجیں
    /// </summary>
    /// <param name="recipient">Phone number - رقم الهاتف - فون نمبر</param>
    /// <param name="lat">Latitude - خط العرض - عرض البلد</param>
    /// <param name="lng">Longitude - خط الطول - طول البلد</param>
    /// <param name="address">Optional address - العنوان - پتہ (اختیاری)</param>
    /// <param name="name">Optional name - الاسم - نام (اختیاری)</param>
    public async Task<string> SendLocationAsync(
        string recipient,
        double lat,
        double lng,
        string? address = null,
        string? name = null)
    {
        var params = new JsonObject
        {
            ["phone"] = recipient,
            ["lat"] = lat,
            ["lng"] = lng
        };
        if (!string.IsNullOrEmpty(address))
            params["address"] = address;
        if (!string.IsNullOrEmpty(name))
            params["name"] = name;
        return await MakeCustomPathRequestAsync("message/location", params);
    }

    /// <summary>
    /// Sends a contact / إرسال جهة اتصال / رابطہ بھیجیں
    /// </summary>
    /// <param name="recipient">Phone number - رقم الهاتف - فون نمبر</param>
    /// <param name="contacts">List of contact objects - قائمة جهات الاتصال - رابطوں کی فہرست</param>
    public async Task<string> SendContactAsync(string recipient, JsonArray contacts)
    {
        var params = new JsonObject
        {
            ["phone"] = recipient,
            ["contacts"] = contacts
        };
        return await MakeCustomPathRequestAsync("message/contact", params);
    }
}
