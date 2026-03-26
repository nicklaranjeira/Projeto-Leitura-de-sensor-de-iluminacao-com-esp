from fastapi import FastAPI
import requests

app = FastAPI()

ESP_IP = "http://192.168.0.105/ler"  # muda pro seu IP

@app.get("/temperatura")
def get_temperatura():
    resposta = requests.get(ESP_IP)
    temp = resposta.text
    return {"temperatura": temp}


