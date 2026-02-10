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
