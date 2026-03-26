// importe das bibliotecas
#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>

// conigurações da rede

const char* ssid ="iot"; 
const char* password = "iotsenai502";

#define PIN_LM35       36 // ESP32 pin GPIO36 (ADC0) connected to LM35



// criação do servidor
WebServer server(80); // roda na porta 80 http

float LerTemp(){
  int valor = analogRead(PIN_LM35);
  float tensao = valor * (3.3 / 4095.0);
  float temperatura = tensao * 100.0;
  return temperatura;
}
   
void handleTemp() {
  float temp = LerTemp();
  server.send(200, "text/plain", String(temp));
}

//Função setup 
void setup(){
  Serial.begin(115200);
  pinMode(PIN_LM35, INPUT);
 
  // configurações de acesso 

  WiFi.begin(ssid, password); // inicia a conexão wifi com as variáveis ja definidas
  while (WiFi.status() != WL_CONNECTED){ // wifi status retorna o status da conexão:  Status	Significado WL_CONNECTED	conectado, WL_DISCONNECTED	desconectado, WL_IDLE_STATUS	tentando conectar
    delay(500);
  }

  // rotas
  server.on("/on", handleTemp); 

  server.begin();
}

void loop(){
  server.handleClient();
}
  // Quando essa função roda, ela:

  // verifica se algum cliente tentou conectar

  // lê a requisição HTTP

  // descobre qual rota foi chamada

  // executa a função associada à rota
