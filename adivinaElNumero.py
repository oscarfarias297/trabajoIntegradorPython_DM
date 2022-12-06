import random

numero = random.randint(1,100)

intentos = 0

play = True

while play:
    intentos += 1
    if intentos <= 3:
        print("Adivina el número que crees que saldrá. tendrás 3 intentos")
        tiraDado = int(input("Elige un número del 1 al 100?: "))
        if tiraDado == numero:
            print("Has Acertado!!!!")
        else:
            print("Tienes otra oportunidad... te quedan ",3-intentos, "intentos")
    else:
        print("Lo siento, Perditeste, no te preocupes, puedes volver a jugar")
        print("El número del dado es ", numero)
        play = False