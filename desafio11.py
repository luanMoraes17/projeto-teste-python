# DESAFIO -

# Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def nova_lista(lista):
    return lista[1]
print(list(map(nova_lista, pinturas)))