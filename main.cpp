// importe das bibliotecas
#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>

// configurações da rede
const char* ssid ="iot"; 
const char* password = "iotsenai502";

// criação do servidor
WebServer server(80);

// pino do LED
#define PIN_LED 2

// variável de controle
bool piscando = false;

// 🔹 ligar LED
void handleOn() {
  digitalWrite(PIN_LED, HIGH);
  piscando = false;
  server.send(200, "text/plain", "LED LIGADO");
}

// 🔹 desligar LED
void handleOff() {
  digitalWrite(PIN_LED, LOW);
  piscando = false;
  server.send(200, "text/plain", "LED DESLIGADO");
}

// 🔹 ativar modo piscar
void handleBlink() {
  piscando = true;
  server.send(200, "text/plain", "LED PISCANDO");
}

//Função setup 
void setup(){
  Serial.begin(115200);

  pinMode(PIN_LED, OUTPUT);

  // conexão wifi
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED){
    delay(500);
  }

  // rotas
  server.on("/on", handleOn); 
  server.on("/off", handleOff); 
  server.on("/blink", handleBlink); 

  server.begin();
}

void loop(){
  server.handleClient();

  // lógica do piscar
  if (piscando) {
    digitalWrite(PIN_LED, HIGH);
    delay(500);
    digitalWrite(PIN_LED, LOW);
    delay(500);
  }

  Serial.println("IP ESP:");
  Serial.println(WiFi.localIP()); 
}