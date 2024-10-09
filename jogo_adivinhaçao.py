import random


#   GERAR UM NUMERO ALEATORIO ENTRE 1 E 100
def adivinhacao_de_numero():
    numeros_aleatorios = random.randint(1, 100)
    tentativas = 0
    acertou = False
 #  CRIAR TITULO PARA O APP   
    print("Olá , seja bem vindo ao jogo de adivinhação!")
    print("Temos um numero escondido entre 1 a 100. Tente acertar em menor tentativas possiveis!")

 #  CRIAR LOOP ATÉ O JOGADOR ADVINHAR O NÚMERO
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

 #  CHAMAR A FUNCAO PARA INICIO DO JOGO
adivinhacao_de_numero()