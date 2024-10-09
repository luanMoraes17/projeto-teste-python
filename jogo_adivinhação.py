import random


def adivinhacao_de_numero():
    numeros_aleatorios = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Olá , seja bem vindo ao jogo de adivinhação!")
    print("Temos um numero escondido entre 1 a 100. Tente acertar em menor tentativas possiveis!")


    while not acertou:
        palpite = int(input("Digite um número jogador: "))
        tentativas += 1

        if palpite < numeros_aleatorios:
            print("O número é maior do que isso,tente novamente")
        elif palpite > numeros_aleatorios:
            print("O número é menor do que isso, tente novamente")
        else:
            acertou = True
            print(f"Parabéns!!! Você acertou o número {numeros_aleatorios} em {tentativas} tentativas.")

 
adivinhacao_de_numero()