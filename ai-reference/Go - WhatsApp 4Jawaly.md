# هذا هو الكود المرجعي الصحيح لربط رسائل واتساب التفاعلية بلغة Go باستخدام 4Jawaly
# This is the correct reference code for WhatsApp interactive messages integration in Go using 4Jawaly

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

## 1. Go Standard Library (net/http)

### send_text.go

```go
// Send Text Message - إرسال رسالة نصية - ٹیکسٹ میسج بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey     = "YOUR_APP_KEY"
	apiSecret  = "YOUR_API_SECRET"
	projectID  = "YOUR_PROJECT_ID"
	recipient  = "9665XXXXXXXX"
)

func main() {
	// Request body - جسم الطلب - درخواست کا جسم
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "text",
				"text": map[string]string{
					"body": "نص الرسالة",
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_buttons.go

```go
// Send Interactive Buttons - إرسال أزرار تفاعلية - انٹرایکٹو بٹن بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "interactive",
				"interactive": map[string]interface{}{
					"type": "button",
					"body": map[string]string{
						"text": "اختر أحد الخيارات التالية",
					},
					"action": map[string]interface{}{
						"buttons": []map[string]interface{}{
							{"type": "reply", "reply": map[string]string{"id": "btn_yes", "title": "نعم"}},
							{"type": "reply", "reply": map[string]string{"id": "btn_no", "title": "لا"}},
							{"type": "reply", "reply": map[string]string{"id": "btn_help", "title": "مساعدة"}},
						},
					},
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_list.go

```go
// Send Interactive List - إرسال قائمة تفاعلية - انٹرایکٹو لسٹ بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "interactive",
				"interactive": map[string]interface{}{
					"type": "list",
					"header": map[string]string{
						"type": "text",
						"text": "قائمة الخدمات",
					},
					"body": map[string]string{
						"text": "اختر الخدمة المطلوبة من القائمة أدناه",
					},
					"footer": map[string]string{
						"text": "4Jawaly Services",
					},
					"action": map[string]interface{}{
						"button": "عرض القائمة",
						"sections": []map[string]interface{}{
							{
								"title": "الخدمات الأساسية",
								"rows": []map[string]string{
									{"id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"},
									{"id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"},
								},
							},
							{
								"title": "الدعم الفني",
								"rows": []map[string]string{
									{"id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"},
								},
							},
						},
					},
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_image.go

```go
// Send Image - إرسال صورة - تصویر بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "image",
				"image": map[string]string{
					"link":    "https://example.com/image.jpg",
					"caption": "وصف الصورة",
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_video.go

```go
// Send Video - إرسال فيديو - ویڈیو بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "video",
				"video": map[string]string{
					"link":    "https://example.com/video.mp4",
					"caption": "وصف الفيديو",
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_audio.go

```go
// Send Audio - إرسال ملف صوتي - آڈیو بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "audio",
				"audio": map[string]string{
					"link": "https://example.com/audio.mp3",
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

### send_document.go

```go
// Send Document - إرسال مستند - دستاویز بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// Config - الإعدادات - ترتیبات
const (
	appKey    = "YOUR_APP_KEY"
	apiSecret = "YOUR_API_SECRET"
	projectID = "YOUR_PROJECT_ID"
	recipient = "9665XXXXXXXX"
)

func main() {
	payload := map[string]interface{}{
		"path": "global",
		"params": map[string]interface{}{
			"url":    "messages",
			"method": "post",
			"data": map[string]interface{}{
				"messaging_product": "whatsapp",
				"to":                recipient,
				"type":              "document",
				"document": map[string]string{
					"link":      "https://example.com/document.pdf",
					"caption":   "وصف المستند",
					"filename":  "document.pdf",
				},
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("JSON marshal error: %v\n", err)
		return
	}

	url := fmt.Sprintf("https://api-users.4jawaly.com/api/v1/whatsapp/%s", projectID)
	req, err := http.NewRequest("POST", url, bytes.NewReader(body))
	if err != nil {
		fmt.Printf("Request creation error: %v\n", err)
		return
	}

	auth := base64.StdEncoding.EncodeToString([]byte(appKey + ":" + apiSecret))
	req.Header.Set("Authorization", "Basic "+auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Request failed: %v\n", err)
		return
	}
	defer resp.Body.Close()

	respBody, _ := io.ReadAll(resp.Body)
	fmt.Printf("Status: %d\n", resp.StatusCode)
	fmt.Printf("Response: %s\n", string(respBody))
}
```

---

## 2. Go Gin Framework

### خدمة الواتساب | whatsapp_service.go

```go
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

// NewWhatsAppService creates service - ينشئ الخدمة - سروس بناتا ہے
func NewWhatsAppService() *WhatsAppService {
	appKey := os.Getenv("APP_KEY")
	if appKey == "" {
		appKey = "YOUR_APP_KEY"
	}
	apiSecret := os.Getenv("API_SECRET")
	if apiSecret == "" {
		apiSecret = "YOUR_API_SECRET"
	}
	projectID := os.Getenv("PROJECT_ID")
	if projectID == "" {
		projectID = "YOUR_PROJECT_ID"
	}
	recipient := os.Getenv("RECIPIENT")
	if recipient == "" {
		recipient = "9665XXXXXXXX"
	}
	return &WhatsAppService{
		baseURL:   "https://api-users.4jawaly.com/api/v1/whatsapp",
		appKey:    appKey,
		apiSecret: apiSecret,
		projectID: projectID,
		recipient: recipient,
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
			"type": "button",
			"body":  map[string]string{"text": bodyText},
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
		"type": "image",
		"image": map[string]string{"link": link, "caption": caption},
	}
	return s.sendRequest(data, to)
}

// SendVideo - إرسال فيديو - ویڈیو بھیجیں
func (s *WhatsAppService) SendVideo(to, link, caption string) (int, string, error) {
	data := map[string]interface{}{
		"type": "video",
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
```

### التطبيق الرئيسي | main.go

```go
// 4Jawaly WhatsApp API - Gin Server
// خادم جين لإرسال رسائل واتساب
// واتساب میسجز بھیجنے کے لیے Gin سرور
package main

import (
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	svc := NewWhatsAppService()

	// Routes - المسارات - راستے

	// POST /whatsapp/text - إرسال نص - ٹیکسٹ بھیجیں
	r.POST("/whatsapp/text", func(c *gin.Context) {
		var req struct {
			To   string `json:"to"`
			Text string `json:"text"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Text == "" {
			req.Text = "نص الرسالة"
		}
		status, body, err := svc.SendText(req.To, req.Text)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/buttons - إرسال أزرار - بٹن بھیجیں
	r.POST("/whatsapp/buttons", func(c *gin.Context) {
		var req struct {
			To      string                   `json:"to"`
			Body    string                   `json:"body"`
			Buttons []map[string]interface{} `json:"buttons"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Body == "" {
			req.Body = "اختر أحد الخيارات التالية"
		}
		if len(req.Buttons) == 0 {
			req.Buttons = []map[string]interface{}{
				{"type": "reply", "reply": map[string]string{"id": "btn_yes", "title": "نعم"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_no", "title": "لا"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_help", "title": "مساعدة"}},
			}
		}
		status, body, err := svc.SendButtons(req.To, req.Body, req.Buttons)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/list - إرسال قائمة - لسٹ بھیجیں
	r.POST("/whatsapp/list", func(c *gin.Context) {
		var req struct {
			To       string                   `json:"to"`
			Header   string                   `json:"header"`
			Body     string                   `json:"body"`
			Footer   string                   `json:"footer"`
			Button   string                   `json:"button"`
			Sections []map[string]interface{} `json:"sections"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Header == "" {
			req.Header = "قائمة الخدمات"
		}
		if req.Body == "" {
			req.Body = "اختر الخدمة المطلوبة من القائمة أدناه"
		}
		if req.Footer == "" {
			req.Footer = "4Jawaly Services"
		}
		if req.Button == "" {
			req.Button = "عرض القائمة"
		}
		if len(req.Sections) == 0 {
			req.Sections = []map[string]interface{}{
				{
					"title": "الخدمات الأساسية",
					"rows": []map[string]string{
						{"id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"},
						{"id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"},
					},
				},
				{
					"title": "الدعم الفني",
					"rows": []map[string]string{
						{"id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"},
					},
				},
			}
		}
		status, body, err := svc.SendList(req.To, req.Header, req.Body, req.Footer, req.Button, req.Sections)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/image - إرسال صورة - تصویر بھیجیں
	r.POST("/whatsapp/image", func(c *gin.Context) {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Link == "" {
			req.Link = "https://example.com/image.jpg"
		}
		status, body, err := svc.SendImage(req.To, req.Link, req.Caption)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/video - إرسال فيديو - ویڈیو بھیجیں
	r.POST("/whatsapp/video", func(c *gin.Context) {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Link == "" {
			req.Link = "https://example.com/video.mp4"
		}
		status, body, err := svc.SendVideo(req.To, req.Link, req.Caption)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/audio - إرسال ملف صوتي - آڈیو بھیجیں
	r.POST("/whatsapp/audio", func(c *gin.Context) {
		var req struct {
			To   string `json:"to"`
			Link string `json:"link"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Link == "" {
			req.Link = "https://example.com/audio.mp3"
		}
		status, body, err := svc.SendAudio(req.To, req.Link)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	// POST /whatsapp/document - إرسال مستند - دستاویز بھیجیں
	r.POST("/whatsapp/document", func(c *gin.Context) {
		var req struct {
			To       string `json:"to"`
			Link     string `json:"link"`
			Caption  string `json:"caption"`
			Filename string `json:"filename"`
		}
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		if req.Link == "" {
			req.Link = "https://example.com/document.pdf"
		}
		if req.Filename == "" {
			req.Filename = "document.pdf"
		}
		status, body, err := svc.SendDocument(req.To, req.Link, req.Caption, req.Filename)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
			return
		}
		c.JSON(status, gin.H{"status": status, "response": body})
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	r.Run(":" + port)
}
```

---

## 3. Go Fiber Framework

### خدمة الواتساب | whatsapp_service.go

```go
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
```

### التطبيق الرئيسي | main.go

```go
// 4Jawaly WhatsApp API - Fiber Server
// خادم Fiber لإرسال رسائل واتساب
// واتساب میسجز بھیجنے کے لیے Fiber سرور
package main

import (
	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()
	svc := NewWhatsAppService()

	// Routes - المسارات - راستے

	// POST /whatsapp/text - إرسال نص - ٹیکسٹ بھیجیں
	app.Post("/whatsapp/text", func(c *fiber.Ctx) error {
		var req struct {
			To   string `json:"to"`
			Text string `json:"text"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Text == "" {
			req.Text = "نص الرسالة"
		}
		status, body, err := svc.SendText(req.To, req.Text)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/buttons - إرسال أزرار - بٹن بھیجیں
	app.Post("/whatsapp/buttons", func(c *fiber.Ctx) error {
		var req struct {
			To      string                   `json:"to"`
			Body    string                   `json:"body"`
			Buttons []map[string]interface{} `json:"buttons"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Body == "" {
			req.Body = "اختر أحد الخيارات التالية"
		}
		if len(req.Buttons) == 0 {
			req.Buttons = []map[string]interface{}{
				{"type": "reply", "reply": map[string]string{"id": "btn_yes", "title": "نعم"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_no", "title": "لا"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_help", "title": "مساعدة"}},
			}
		}
		status, body, err := svc.SendButtons(req.To, req.Body, req.Buttons)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/list - إرسال قائمة - لسٹ بھیجیں
	app.Post("/whatsapp/list", func(c *fiber.Ctx) error {
		var req struct {
			To       string                   `json:"to"`
			Header   string                   `json:"header"`
			Body     string                   `json:"body"`
			Footer   string                   `json:"footer"`
			Button   string                   `json:"button"`
			Sections []map[string]interface{} `json:"sections"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Header == "" {
			req.Header = "قائمة الخدمات"
		}
		if req.Body == "" {
			req.Body = "اختر الخدمة المطلوبة من القائمة أدناه"
		}
		if req.Footer == "" {
			req.Footer = "4Jawaly Services"
		}
		if req.Button == "" {
			req.Button = "عرض القائمة"
		}
		if len(req.Sections) == 0 {
			req.Sections = []map[string]interface{}{
				{
					"title": "الخدمات الأساسية",
					"rows": []map[string]string{
						{"id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"},
						{"id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"},
					},
				},
				{
					"title": "الدعم الفني",
					"rows": []map[string]string{
						{"id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"},
					},
				},
			}
		}
		status, body, err := svc.SendList(req.To, req.Header, req.Body, req.Footer, req.Button, req.Sections)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/image - إرسال صورة - تصویر بھیجیں
	app.Post("/whatsapp/image", func(c *fiber.Ctx) error {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/image.jpg"
		}
		status, body, err := svc.SendImage(req.To, req.Link, req.Caption)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/video - إرسال فيديو - ویڈیو بھیجیں
	app.Post("/whatsapp/video", func(c *fiber.Ctx) error {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/video.mp4"
		}
		status, body, err := svc.SendVideo(req.To, req.Link, req.Caption)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/audio - إرسال ملف صوتي - آڈیو بھیجیں
	app.Post("/whatsapp/audio", func(c *fiber.Ctx) error {
		var req struct {
			To   string `json:"to"`
			Link string `json:"link"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/audio.mp3"
		}
		status, body, err := svc.SendAudio(req.To, req.Link)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/document - إرسال مستند - دستاویز بھیجیں
	app.Post("/whatsapp/document", func(c *fiber.Ctx) error {
		var req struct {
			To       string `json:"to"`
			Link     string `json:"link"`
			Caption  string `json:"caption"`
			Filename string `json:"filename"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/document.pdf"
		}
		if req.Filename == "" {
			req.Filename = "document.pdf"
		}
		status, body, err := svc.SendDocument(req.To, req.Link, req.Caption, req.Filename)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	port := getEnv("PORT", "8080")
	app.Listen(":" + port)
}
```

---

## 4. Go Echo Framework

### خدمة الواتساب | whatsapp_service.go

```go
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
```

### التطبيق الرئيسي | main.go

```go
// 4Jawaly WhatsApp API - Echo Server
// خادم Echo لإرسال رسائل واتساب
// واتساب میسجز بھیجنے کے لیے Echo سرور
package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()
	svc := NewWhatsAppService()

	// Routes - المسارات - راستے

	// POST /whatsapp/text - إرسال نص - ٹیکسٹ بھیجیں
	e.POST("/whatsapp/text", func(c echo.Context) error {
		var req struct {
			To   string `json:"to"`
			Text string `json:"text"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Text == "" {
			req.Text = "نص الرسالة"
		}
		status, body, err := svc.SendText(req.To, req.Text)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/buttons - إرسال أزرار - بٹن بھیجیں
	e.POST("/whatsapp/buttons", func(c echo.Context) error {
		var req struct {
			To      string                   `json:"to"`
			Body    string                   `json:"body"`
			Buttons []map[string]interface{} `json:"buttons"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Body == "" {
			req.Body = "اختر أحد الخيارات التالية"
		}
		if len(req.Buttons) == 0 {
			req.Buttons = []map[string]interface{}{
				{"type": "reply", "reply": map[string]string{"id": "btn_yes", "title": "نعم"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_no", "title": "لا"}},
				{"type": "reply", "reply": map[string]string{"id": "btn_help", "title": "مساعدة"}},
			}
		}
		status, body, err := svc.SendButtons(req.To, req.Body, req.Buttons)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/list - إرسال قائمة - لسٹ بھیجیں
	e.POST("/whatsapp/list", func(c echo.Context) error {
		var req struct {
			To       string                   `json:"to"`
			Header   string                   `json:"header"`
			Body     string                   `json:"body"`
			Footer   string                   `json:"footer"`
			Button   string                   `json:"button"`
			Sections []map[string]interface{} `json:"sections"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Header == "" {
			req.Header = "قائمة الخدمات"
		}
		if req.Body == "" {
			req.Body = "اختر الخدمة المطلوبة من القائمة أدناه"
		}
		if req.Footer == "" {
			req.Footer = "4Jawaly Services"
		}
		if req.Button == "" {
			req.Button = "عرض القائمة"
		}
		if len(req.Sections) == 0 {
			req.Sections = []map[string]interface{}{
				{
					"title": "الخدمات الأساسية",
					"rows": []map[string]string{
						{"id": "svc_sms", "title": "خدمة الرسائل النصية", "description": "إرسال رسائل SMS للعملاء"},
						{"id": "svc_whatsapp", "title": "خدمة واتساب", "description": "إرسال رسائل واتساب تفاعلية"},
					},
				},
				{
					"title": "الدعم الفني",
					"rows": []map[string]string{
						{"id": "support_ticket", "title": "فتح تذكرة دعم", "description": "تواصل مع فريق الدعم الفني"},
					},
				},
			}
		}
		status, body, err := svc.SendList(req.To, req.Header, req.Body, req.Footer, req.Button, req.Sections)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/image - إرسال صورة - تصویر بھیجیں
	e.POST("/whatsapp/image", func(c echo.Context) error {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/image.jpg"
		}
		status, body, err := svc.SendImage(req.To, req.Link, req.Caption)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/video - إرسال فيديو - ویڈیو بھیجیں
	e.POST("/whatsapp/video", func(c echo.Context) error {
		var req struct {
			To      string `json:"to"`
			Link    string `json:"link"`
			Caption string `json:"caption"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/video.mp4"
		}
		status, body, err := svc.SendVideo(req.To, req.Link, req.Caption)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/audio - إرسال ملف صوتي - آڈیو بھیجیں
	e.POST("/whatsapp/audio", func(c echo.Context) error {
		var req struct {
			To   string `json:"to"`
			Link string `json:"link"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/audio.mp3"
		}
		status, body, err := svc.SendAudio(req.To, req.Link)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	// POST /whatsapp/document - إرسال مستند - دستاویز بھیجیں
	e.POST("/whatsapp/document", func(c echo.Context) error {
		var req struct {
			To       string `json:"to"`
			Link     string `json:"link"`
			Caption  string `json:"caption"`
			Filename string `json:"filename"`
		}
		if err := c.Bind(&req); err != nil {
			return c.JSON(http.StatusBadRequest, map[string]string{"error": err.Error()})
		}
		if req.Link == "" {
			req.Link = "https://example.com/document.pdf"
		}
		if req.Filename == "" {
			req.Filename = "document.pdf"
		}
		status, body, err := svc.SendDocument(req.To, req.Link, req.Caption, req.Filename)
		if err != nil {
			return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
		}
		return c.JSON(status, map[string]interface{}{"status": status, "response": body})
	})

	port := getEnv("PORT", "8080")
	e.Logger.Fatal(e.Start(":" + port))
}
```
