import os
import requests
import time

IP_ESP32 = "http://192.168.0.185"


def menu():

    print(50 * "-")
    print("Seja bem-vindo ao MENU de controle ESP-32".center(50))
    print(50 * "-")

    print("\n1 - Ligar LED")
    print("2 - Desligar LED")
    print("3 - Piscar o LED")


def ligar_led_esp32():

    try:
        response = requests.get(f"{IP_ESP32}/on", timeout=5)

        if response.status_code == 200:
            os.system("cls")

            print(50 * "-")
            print("SEU LED JÁ LIGADO E FUNCIONANDO!".center(50))
            print(50 * "-")

            time.sleep(5)

        elif response.status_code == 404:
            os.system("cls")

            print(50 * "-")
            print("O ENDPOINT NÃO FOI ENCONTRADO, VERIFIQUE A CONEXÃO!".center(50))
            print(f"Erro HTTP: {response.status_code}".center(50))
            print(50 * "-")

            time.sleep(5)

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à ESP32")

    except requests.exceptions.Timeout:
        print("Tempo de resposta excedido")


def desligar_led_esp32():

    try:
        response = requests.get(f"{IP_ESP32}/off", timeout=5)

        if response.status_code == 200:
            os.system("cls")

            print(50 * "-")
            print("SEU LED JÁ ESTÁ DESLIGADO!".center(50))
            print(50 * "-")

            time.sleep(5)

        elif response.status_code == 404:
            os.system("cls")

            print(50 * "-")
            print("O ENDPOINT NÃO FOI ENCONTRADO, VERIFIQUE A CONEXÃO!".center(50))
            print(f"Erro HTTP: {response.status_code}".center(50))
            print(50 * "-")

            time.sleep(5)

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à ESP32")

    except requests.exceptions.Timeout:
        print("Tempo de resposta excedido")


def piscar_led_esp32():

    try:
        response = requests.get(f"{IP_ESP32}/piscar", timeout=5)

        if response.status_code == 200:
            os.system("cls")

            print(50 * "-")
            print("SEU LED JÁ ESTÁ PISCANDO!".center(50))
            print(50 * "-")

            time.sleep(5)

        elif response.status_code == 404:
            os.system("cls")

            print(50 * "-")
            print("O ENDPOINT NÃO FOI ENCONTRADO, VERIFIQUE A CONEXÃO!".center(50))
            print(f"Erro HTTP: {response.status_code}".center(50))
            print(50 * "-")

            time.sleep(5)

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à ESP32")

    except requests.exceptions.Timeout:
        print("Tempo de resposta excedido")

def semafaro_led_esp32():

    try:
        response = requests.get(f"{IP_ESP32}/semafaro", timeout=5)

        if response.status_code == 200:
            os.system("cls")

            print(50 * "-")
            print("SEU LED JÁ ESTÁ DESLIGADO!".center(50))
            print(50 * "-")

            time.sleep(5)

        elif response.status_code == 404:
            os.system("cls")

            print(50 * "-")
            print("O ENDPOINT NÃO FOI ENCONTRADO, VERIFIQUE A CONEXÃO!".center(50))
            print(f"Erro HTTP: {response.status_code}".center(50))
            print(50 * "-")

            time.sleep(5)

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à ESP32")

    except requests.exceptions.Timeout:
        print("Tempo de resposta excedido")


    

        
    

