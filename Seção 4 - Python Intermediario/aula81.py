#funcao lambda, funcao de uma linha

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Olavo', 'sobrenome': 'carvalho'},
    {'nome': 'Guilherme', 'sobrenome': 'Souza'},
    {'nome': 'Joao', 'sobrenome': 'Pedro'},
]

lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Olavo', 'sobrenome': 'carvalho'},
    {'nome': 'Guilherme', 'sobrenome': 'Souza'},
    {'nome': 'Joao', 'sobrenome': 'Pedro'},
]

def exibe(lista):
    for item in lista:
        print(item)
    print()

lista1 = sorted(lista, key=lambda item: item['nome'])
lista1 = sorted(lista, key=lambda item: item['sobrenome'])

exibe(lista1)
exibe(lista2)