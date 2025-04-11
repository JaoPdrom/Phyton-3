"""
exercicio:
exiba os indices da lista
"""

#solucao 1
lista = ['Maria', 'Luiz', 'Pedro']
indice = 0
for nome in lista:
    print(f'{nome} indice eh: {indice}')
    indice+=1

#solucao 2
lista = ['Maria', 'Luiz', 'Pedro']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])