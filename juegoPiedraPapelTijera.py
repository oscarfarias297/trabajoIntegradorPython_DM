import random

print("BIENVENIDOS A PIEDRA, PAPEL O TIJERA")
print()

def jugar():

    player = int (input ("Elija 1 para PIEDRA, 2 para Papel, 3 para TIJERA: "))

    ppt = [1, 2, 3]
    
    compu = random.choice(ppt)

    if player == compu:
        return "EMPATADOS! {} ".format(player)

    if es_ganador(player,compu):
        return "Elegiste {} y el oponente {}. GANASTE!!!".format(player,compu)

    return "Elegiste {} y el oponente {}. PERDISTE!".format(player,compu)

def es_ganador(gamer,oponente):
    if (gamer == "1" and oponente == "3") or (gamer == "3" and oponente == "2") or (gamer == "2" and oponente == "1"):
        return True
    return False


if __name__ == "__main__":
    print (jugar())