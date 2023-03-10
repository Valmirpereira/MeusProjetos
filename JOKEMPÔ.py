from random import randint
from time import sleep

print("==" * 30)
print("JOKENPÔ".center(60))
print("==" * 30)

print('''[1] PEDRA
[2] PAPEL
[3] TESOURA
[0] SAIR''')

jogadorVenceu = 0
pcVenceu = 0

while True:
    pc = randint(1, 3)
    jogador = ''
    while jogador not in (1,2,3):
        jogada = input("Sua jogada: ")
        if jogada.isdigit():
            jogador = int(jogada)
            if jogador < 0 or jogador > 3:
                print("Jogada inválida, tente as opções entre 1 e 3")
            if jogador == 0:
                print("Fim de jogo, aguarde o resultado")
        else:
            print("Jogada inválida, tente as opções entre 1 e 3")
    if jogador == 0:
        break

    print("-=" * 30)
    sleep(1)
    print("JO".center(60))
    sleep(1)
    print("KEN".center(60))
    sleep(1)
    print("PÔ".center(60))
    sleep(1)
    print("-=" * 30)

    if pc == 1:
        if jogador == 1:
            print("PC escolheu PEDRA e o jogador escolheu PEDRA")
            print("EMPATE")
        if jogador == 2:
            print("PC escolheu PEDRA e o jogador escolheu PAPEL")
            print("JOGADOR VENCEU")
            jogadorVenceu += 1
        if jogador == 3:
            print("PC escolheu PEDRA e o jogador escolheu TESOURA")
            print("PC VENCEU")
            pcVenceu += 1
    elif pc == 2:
        if jogador == 1:
            print("PC escolheu PAPEL e o jogador escolheu PEDRA")
            print("PC VENCEU")
            pcVenceu += 1
        if jogador == 2:
            print("PC escolheu PAPEL e o jogador escolheu PAPEL")
            print("EMPATE")
        if jogador == 3:
            print("PC escolheu PAPEL e o jogador escolheu TESOURA")
            print("JOGADOR VENCEU")
            jogadorVenceu += 1
    elif pc == 3:
        if jogador == 1:
            print("PC escolheu TESOURA e o jogador escolheu PEDRA")
            print("JOGADOR VENCEU")
            jogadorVenceu += 1
        if jogador == 2:
            print("PC escolheu TESOURA e o jogador escolheu PAPEL")
            print("PC VENCEU")
            pcVenceu += 1
        if jogador == 3:
            print("PC escolheu TESOURA e o jogador escolheu TESOURA")
            print("EMPATE")

print(f"PONTOS PC: {pcVenceu}")
print(f"PONTOS JOGADOR: {jogadorVenceu}")
if pcVenceu < jogadorVenceu:
    print("JOGADOR VENCEU")
if pcVenceu > jogadorVenceu:
    print("PC VENCEU".center(60))
else:
    print("EMPATE")