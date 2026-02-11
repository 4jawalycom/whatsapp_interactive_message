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

	// POST /whatsapp/location - إرسال موقع جغرافي - مقام بھیجیں
	app.Post("/whatsapp/location", func(c *fiber.Ctx) error {
		var req struct {
			To      string  `json:"to"`
			Lat     float64 `json:"lat"`
			Lng     float64 `json:"lng"`
			Address string  `json:"address"`
			Name    string  `json:"name"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if req.Address == "" {
			req.Address = "Riyadh, Saudi Arabia"
		}
		if req.Name == "" {
			req.Name = "My Office"
		}
		status, body, err := svc.SendLocation(req.To, req.Lat, req.Lng, req.Address, req.Name)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	// POST /whatsapp/contact - إرسال جهة اتصال - رابطہ بھیجیں
	app.Post("/whatsapp/contact", func(c *fiber.Ctx) error {
		var req struct {
			To       string                   `json:"to"`
			Contacts []map[string]interface{} `json:"contacts"`
		}
		if err := c.BodyParser(&req); err != nil {
			return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{"error": err.Error()})
		}
		if len(req.Contacts) == 0 {
			req.Contacts = []map[string]interface{}{
				{
					"name": map[string]string{
						"formatted_name": "Ahmed Ali",
						"first_name":     "Ahmed",
						"last_name":      "Ali",
					},
					"phones": []map[string]interface{}{
						{"phone": "+966501234567", "type": "CELL"},
					},
				},
			}
		}
		status, body, err := svc.SendContact(req.To, req.Contacts)
		if err != nil {
			return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{"error": err.Error()})
		}
		return c.Status(status).JSON(fiber.Map{"status": status, "response": body})
	})

	port := getEnv("PORT", "8080")
	app.Listen(":" + port)
}
