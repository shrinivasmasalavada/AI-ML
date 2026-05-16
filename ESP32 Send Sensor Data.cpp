#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "YOUR_WIFI";
const char* password = "PASSWORD";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
}

void loop() {

  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;
http.begin("http://your-server-ip/data");
    http.addHeader("Content-Type", "application/json");

    String payload = "{\"temperature\":30}";

    int response = http.POST(payload);

    Serial.println(response);

    http.end();
  }

  delay(5000);
}