from functions import *

IP_ESP32 = "http://192.1683.0.185"
escolha_usuario = 0

while True:
    
    os.system("cls")

    menu()

    try:
        escolha_usuario = int(input("\nQual a sua escolha hoje?\n->"))

    except ValueError:
        os.system("cls")
        print("\nEntrada invalida. Digite apenas numeros.")
        time.sleep(2)

    
    if escolha_usuario < 0 or escolha_usuario > 3:
        os.system("cls")
        print("Escolha Inválida, números apenas de 1 a 3!")
        time.sleep(2)

    match escolha_usuario:
            
        case 1:
            ligar_led_esp32()
        
        case 2: 
            desligar_led_esp32()

        case 3:
            piscar_led_esp32()

        



