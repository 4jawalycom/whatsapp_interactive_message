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
