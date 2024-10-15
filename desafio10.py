# DESAFIO
# ITERE A LISTA ABAIXO EXIBINDO O NÚMERO DO ÍNDICE + NOME DA FRUTA. PORÉM, QUANDO O ÍNDICE FOR 3, EXIBA 'Nº ÍNDICE + NOME DA FRUTA EM PROMOÇÃO'
frutas = ["Maçã", "Laranja", "Morango", "Limão"]

for indice, fruta in enumerate(frutas,0):
    if indice == 3:
        print(indice, f"{fruta} EM PROMOÇÃO!")
    else:
        print(indice, fruta)