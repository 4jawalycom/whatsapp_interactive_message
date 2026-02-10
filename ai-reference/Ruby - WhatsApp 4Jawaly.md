# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Ruby باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Ruby using 4Jawaly

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

## إرسال رسالة نصية | send_text.rb

```ruby
#!/usr/bin/env ruby
# إرسال رسالة نصية عبر واتساب
# Send text message via WhatsApp
# واٹس ایپ کے ذریعے ٹیکسٹ پیغام بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# محتوى الرسالة - Message content - پیغام کا مواد
MESSAGE_BODY = "نص الرسالة"

def send_text_message
  # إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "text",
        text: { body: MESSAGE_BODY }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_text_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال أزرار تفاعلية | send_buttons.rb

```ruby
#!/usr/bin/env ruby
# إرسال رسالة بأزرار تفاعلية عبر واتساب
# Send interactive buttons message via WhatsApp
# واٹس ایپ کے ذریعے انٹرایکٹو بٹن پیغام بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

def send_buttons_message
  # إرسال رسالة أزرار - Send buttons message - بٹن پیغام بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "interactive",
        interactive: {
          type: "button",
          body: { text: "اختر أحد الخيارات التالية" },
          action: {
            buttons: [
              { type: "reply", reply: { id: "btn_yes", title: "نعم" } },
              { type: "reply", reply: { id: "btn_no", title: "لا" } },
              { type: "reply", reply: { id: "btn_help", title: "مساعدة" } }
            ]
          }
        }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_buttons_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال قائمة تفاعلية | send_list.rb

```ruby
#!/usr/bin/env ruby
# إرسال رسالة بقائمة تفاعلية عبر واتساب
# Send interactive list message via WhatsApp
# واٹس ایپ کے ذریعے انٹرایکٹو لسٹ پیغام بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

def send_list_message
  # إرسال رسالة قائمة - Send list message - لسٹ پیغام بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "interactive",
        interactive: {
          type: "list",
          header: { type: "text", text: "قائمة الخدمات" },
          body: { text: "اختر الخدمة المطلوبة من القائمة أدناه" },
          footer: { text: "4Jawaly Services" },
          action: {
            button: "عرض القائمة",
            sections: [
              {
                title: "الخدمات الأساسية",
                rows: [
                  { id: "svc_sms", title: "خدمة الرسائل النصية", description: "إرسال رسائل SMS للعملاء" },
                  { id: "svc_whatsapp", title: "خدمة واتساب", description: "إرسال رسائل واتساب تفاعلية" }
                ]
              },
              {
                title: "الدعم الفني",
                rows: [
                  { id: "support_ticket", title: "فتح تذكرة دعم", description: "تواصل مع فريق الدعم الفني" }
                ]
              }
            ]
          }
        }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_list_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال صورة | send_image.rb

```ruby
#!/usr/bin/env ruby
# إرسال صورة عبر واتساب
# Send image via WhatsApp
# واٹس ایپ کے ذریعے تصویر بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الصورة والوصف - Image URL and caption - تصویر کا لنک اور کیپشن
IMAGE_URL = "https://example.com/image.jpg"
IMAGE_CAPTION = "وصف الصورة"

def send_image_message
  # إرسال صورة - Send image - تصویر بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "image",
        image: { link: IMAGE_URL, caption: IMAGE_CAPTION }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_image_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال فيديو | send_video.rb

```ruby
#!/usr/bin/env ruby
# إرسال فيديو عبر واتساب
# Send video via WhatsApp
# واٹس ایپ کے ذریعے ویڈیو بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الفيديو والوصف - Video URL and caption - ویڈیو کا لنک اور کیپشن
VIDEO_URL = "https://example.com/video.mp4"
VIDEO_CAPTION = "وصف الفيديو"

def send_video_message
  # إرسال فيديو - Send video - ویڈیو بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "video",
        video: { link: VIDEO_URL, caption: VIDEO_CAPTION }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_video_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال ملف صوتي | send_audio.rb

```ruby
#!/usr/bin/env ruby
# إرسال ملف صوتي عبر واتساب
# Send audio file via WhatsApp
# واٹس ایپ کے ذریعے آڈیو فائل بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط الملف الصوتي - Audio file URL - آڈیو فائل کا لنک
AUDIO_URL = "https://example.com/audio.mp3"

def send_audio_message
  # إرسال ملف صوتي - Send audio - آڈیو بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "audio",
        audio: { link: AUDIO_URL }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_audio_message if __FILE__ == $PROGRAM_NAME
```

---

## إرسال مستند | send_document.rb

```ruby
#!/usr/bin/env ruby
# إرسال مستند عبر واتساب
# Send document via WhatsApp
# واٹس ایپ کے ذریعے دستاویز بھیجیں

require "net/http"
require "uri"
require "json"
require "base64"

# إعدادات الاتصال - Connection settings - رابطہ کی ترتیبات
APP_KEY = "your_app_key"
API_SECRET = "your_api_secret"
PROJECT_ID = "your_project_id"
RECIPIENT = "9665XXXXXXXX"

# رابط المستند والوصف واسم الملف - Document URL, caption and filename - دستاویز کا لنک، کیپشن اور فائل کا نام
DOCUMENT_URL = "https://example.com/document.pdf"
DOCUMENT_CAPTION = "وصف المستند"
DOCUMENT_FILENAME = "document.pdf"

def send_document_message
  # إرسال مستند - Send document - دستاویز بھیجیں
  url = URI("https://api-users.4jawaly.com/api/v1/whatsapp/#{PROJECT_ID}")
  auth_string = "#{APP_KEY}:#{API_SECRET}"
  auth_b64 = Base64.strict_encode64(auth_string)

  payload = {
    path: "global",
    params: {
      url: "messages",
      method: "post",
      data: {
        messaging_product: "whatsapp",
        to: RECIPIENT,
        type: "document",
        document: {
          link: DOCUMENT_URL,
          caption: DOCUMENT_CAPTION,
          filename: DOCUMENT_FILENAME
        }
      }
    }
  }

  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = true
  http.verify_mode = OpenSSL::SSL::VERIFY_PEER

  request = Net::HTTP::Post.new(url)
  request["Content-Type"] = "application/json"
  request["Authorization"] = "Basic #{auth_b64}"
  request.body = payload.to_json

  begin
    response = http.request(request)
    puts "رمز الاستجابة / Response code / جوابی کوڈ: #{response.code}"
    puts "\nالاستجابة / Response / جواب:\n#{JSON.pretty_generate(JSON.parse(response.body))}"
  rescue Net::OpenTimeout, Net::ReadTimeout, SocketError => e
    puts "خطأ في الاتصال / Connection error / رابطہ میں خرابی: #{e.message}"
  rescue JSON::ParserError => e
    puts "خطأ في تحليل الاستجابة / Response parse error / جواب کی تشریح میں خرابی: #{e.message}"
    puts "النص الخام / Raw text / خام متن: #{response&.body}"
  end
end

send_document_message if __FILE__ == $PROGRAM_NAME
```
