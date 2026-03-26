# 🌐 ESP32 Web Server - Controle de LED

Este projeto utiliza o ESP32 como servidor web para controlar um LED remotamente através do navegador.

## 📌 Funcionalidades

* 🔛 Ligar o LED
* ⛔ Desligar o LED
* 🔁 Fazer o LED piscar
* 🌍 Acesso via navegador (HTTP)

---

## 🛠️ Tecnologias Utilizadas

* ESP32
* Arduino Framework
* Biblioteca WiFi
* Biblioteca WebServer

---

## ⚙️ Hardware Necessário

* 1x ESP32
* 1x LED (ou usar o LED onboard)
* 1x Resistor (220Ω recomendado)
* Jumpers

---

## 🔌 Esquema de Ligação

* LED positivo → GPIO 2 do ESP32
* LED negativo → Resistor → GND

---

## 🚀 Como Funciona

O ESP32 se conecta a uma rede Wi-Fi e cria um servidor HTTP na porta 80.

Ao acessar diferentes rotas no navegador, o usuário pode controlar o LED:

| Rota     | Ação             |
| -------- | ---------------- |
| `/on`    | Liga o LED       |
| `/off`   | Desliga o LED    |
| `/blink` | Faz o LED piscar |

---

## 🌐 Como Usar

1. Configure o Wi-Fi no código:

```cpp
const char* ssid = "SEU_WIFI";
const char* password = "SUA_SENHA";
```

2. Faça upload do código para o ESP32

3. Abra o Monitor Serial e copie o IP exibido:

```
IP ESP:
192.168.X.X
```

4. Acesse no navegador:

* http://IP_DO_ESP/on
* http://IP_DO_ESP/off
* http://IP_DO_ESP/blink

---


## ⚠️ Observações

* O modo "piscar" utiliza `delay()`, o que pode bloquear temporariamente o servidor.
* Para aplicações mais avançadas, recomenda-se o uso de `millis()`.

---


---

## 👩‍💻 Autora

Projeto desenvolvido por Nicolle Laranjeira 
