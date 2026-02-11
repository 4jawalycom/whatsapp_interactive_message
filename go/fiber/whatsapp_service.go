// WhatsApp Service - خدمة واتساب - واتساب سروس
// Sends all 7 message types via 4Jawaly API
// يرسل جميع أنواع الرسائل عبر واتساب 4Jawaly
// 4Jawaly API کے ذریعے تمام 7 میسج اقسام بھیجتا ہے
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

// WhatsAppService handles API calls - يدير استدعاءات API - API کالز handle کرتا ہے
type WhatsAppService struct {
	baseURL   string
	appKey    string
	apiSecret string
	projectID string
	recipient string
}

// getEnv returns env var or default - يُرجع المتغير أو القيمة الافتراضية - env var یا default لوٹاتا ہے
func getEnv(key, defaultVal string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return defaultVal
}

// NewWhatsAppService creates service - ينشئ الخدمة - سروس بناتا ہے
func NewWhatsAppService() *WhatsAppService {
	return &WhatsAppService{
		baseURL:   "https://api-users.4jawaly.com/api/v1/whatsapp",
		appKey:    getEnv("APP_KEY", "YOUR_APP_KEY"),
		apiSecret: getEnv("API_SECRET", "YOUR_API_SECRET"),
		projectID: getEnv("PROJECT_ID", "YOUR_PROJECT_ID"),
		recipient: getEnv("RECIPIENT", "9665XXXXXXXX"),
	}
}

// sendRequest - إرسال طلب - درخواست بھیجیں
func (s *WhatsAppService) sendRequest(data map[string]interface{}, recipient string) (int, string, error) {
	if recipient == "" {
		recipient = s.recipient
	}
	data["messaging_product"] = "whatsapp"
	data["to"] = recipient

	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data":   data,
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		return 0, "", fmt.Errorf("json marshal: %w", err)
	}

	url := fmt.Sprintf("%s/%s", s.baseURL, s.projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		return 0, "", fmt.Errorf("new request: %w", err)
	}

	auth := base64.StdEncoding.EncodeToString([]byte(s.appKey + ":" + s.apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return 0, "", fmt.Errorf("do request: %w", err)
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	return resp.StatusCode, string(respBody), nil
}

// SendText - إرسال نص - ٹیکسٹ بھیجیں
func (s *WhatsAppService) SendText(to, text string) (int, string, error) {
	data := map[string]interface{}{
		"type": "text",
		"text": map[string]string{"body": text},
	}
	return s.sendRequest(data, to)
}

// SendButtons - إرسال أزرار - بٹن بھیجیں
func (s *WhatsAppService) SendButtons(to string, bodyText string, buttons []map[string]interface{}) (int, string, error) {
	data := map[string]interface{}{
		"type": "interactive",
		"interactive": map[string]interface{}{
			"type":   "button",
			"body":   map[string]string{"text": bodyText},
			"action": map[string]interface{}{"buttons": buttons},
		},
	}
	return s.sendRequest(data, to)
}

// SendList - إرسال قائمة - لسٹ بھیجیں
func (s *WhatsAppService) SendList(to string, header, bodyText, footer, button string, sections []map[string]interface{}) (int, string, error) {
	data := map[string]interface{}{
		"type": "interactive",
		"interactive": map[string]interface{}{
			"type":   "list",
			"header": map[string]string{"type": "text", "text": header},
			"body":   map[string]string{"text": bodyText},
			"footer": map[string]string{"text": footer},
			"action": map[string]interface{}{
				"button":   button,
				"sections": sections,
			},
		},
	}
	return s.sendRequest(data, to)
}

// SendImage - إرسال صورة - تصویر بھیجیں
func (s *WhatsAppService) SendImage(to, link, caption string) (int, string, error) {
	data := map[string]interface{}{
		"type":  "image",
		"image": map[string]string{"link": link, "caption": caption},
	}
	return s.sendRequest(data, to)
}

// SendVideo - إرسال فيديو - ویڈیو بھیجیں
func (s *WhatsAppService) SendVideo(to, link, caption string) (int, string, error) {
	data := map[string]interface{}{
		"type":  "video",
		"video": map[string]string{"link": link, "caption": caption},
	}
	return s.sendRequest(data, to)
}

// SendAudio - إرسال ملف صوتي - آڈیو بھیجیں
func (s *WhatsAppService) SendAudio(to, link string) (int, string, error) {
	data := map[string]interface{}{
		"type":  "audio",
		"audio": map[string]string{"link": link},
	}
	return s.sendRequest(data, to)
}

// SendDocument - إرسال مستند - دستاویز بھیجیں
func (s *WhatsAppService) SendDocument(to, link, caption, filename string) (int, string, error) {
	data := map[string]interface{}{
		"type": "document",
		"document": map[string]string{
			"link":     link,
			"caption":  caption,
			"filename": filename,
		},
	}
	return s.sendRequest(data, to)
}

// sendCustomPathRequest - إرسال طلب بمسار مخصص (location/contact)
// Send request with custom path - مخصوص path کے ساتھ درخواست بھیجیں
func (s *WhatsAppService) sendCustomPathRequest(path string, params map[string]interface{}) (int, string, error) {
	if params["phone"] == nil || params["phone"] == "" {
		params["phone"] = s.recipient
	}
	payload := map[string]interface{}{
		"path":   path,
		"params": params,
	}
	body, err := json.Marshal(payload)
	if err != nil {
		return 0, "", fmt.Errorf("json marshal: %w", err)
	}
	url := fmt.Sprintf("%s/%s", s.baseURL, s.projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		return 0, "", fmt.Errorf("new request: %w", err)
	}
	auth := base64.StdEncoding.EncodeToString([]byte(s.appKey + ":" + s.apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return 0, "", fmt.Errorf("do request: %w", err)
	}
	defer resp.Body.Close()
	respBody, _ := io.ReadAll(resp.Body)
	return resp.StatusCode, string(respBody), nil
}

// SendLocation - إرسال موقع جغرافي - مقام بھیجیں
func (s *WhatsAppService) SendLocation(to string, lat, lng float64, address, name string) (int, string, error) {
	if to == "" {
		to = s.recipient
	}
	params := map[string]interface{}{
		"phone":   to,
		"lat":     lat,
		"lng":     lng,
		"address": address,
		"name":    name,
	}
	return s.sendCustomPathRequest("message/location", params)
}

// SendContact - إرسال جهة اتصال - رابطہ بھیجیں
func (s *WhatsAppService) SendContact(to string, contacts []map[string]interface{}) (int, string, error) {
	if to == "" {
		to = s.recipient
	}
	params := map[string]interface{}{
		"phone":    to,
		"contacts": contacts,
	}
	return s.sendCustomPathRequest("message/contact", params)
}
