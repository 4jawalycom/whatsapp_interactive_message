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
