from flask import Flask, jsonify
from flask_cors import CORS
import requests

ESP32_BASE_URL = "http://192.168.0.185"

app = Flask(__name__)
CORS(app)


def send_esp32_command(path):
    try:
        response = requests.get(f"{ESP32_BASE_URL}/{path}", timeout=5)

        if response.status_code == 200:
            return True, "Comando enviado para a ESP32."

        if response.status_code == 404:
            return False, "Endpoint nao encontrado na ESP32."

        return False, f"Erro HTTP da ESP32: {response.status_code}"

    except requests.exceptions.ConnectionError:
        return False, "Nao foi possivel conectar com a ESP32."

    except requests.exceptions.Timeout:
        return False, "Tempo de resposta da ESP32 excedido."


@app.get("/api/health")
def health():
    return jsonify({"message": "Backend online"}), 200


@app.post("/api/led/on")
def led_on():
    ok, message = send_esp32_command("on")
    return jsonify({"message": message}), 200 if ok else 502


@app.post("/api/led/off")
def led_off():
    ok, message = send_esp32_command("off")
    return jsonify({"message": message}), 200 if ok else 502


@app.post("/api/led/blink")
def led_blink():
    ok, message = send_esp32_command("piscar")
    return jsonify({"message": message}), 200 if ok else 502


@app.post("/semafaro")
def semafaro():
    ok, message = send_esp32_command("semafaro")
    return jsonify({"message": message}), 200 if ok else 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
