// Send Location Message - إرسال موقع جغرافي - مقام بھیجیں
// Uses net/http only - استخدام net/http فقط - صرف net/http استعمال
// Note: Location uses path "message/location" - different from the 7 existing types
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
	recipient = "966500000000"
)

func main() {
	// Request body - جسم الطلب - درخواست کا جسم
	// هيكل مختلف: path message/location مع params مباشرة
	// Different structure: path message/location with direct params
	payload := map[string]interface{}{
		"path": "message/location",
		"params": map[string]interface{}{
			"phone":   recipient,
			"lat":     24.7136,
			"lng":     46.6753,
			"address": "Riyadh, Saudi Arabia",
			"name":    "My Office",
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
