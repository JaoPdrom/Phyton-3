#enumerate - enumera iteraveis
#cria um tupla para cada valor da lista [(0, 'Maria'), (1, 'Helena'), (2, "Luiz"), (3, 'Joao')]

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

for indice, nome in enumerate(lista): #faz o desempacotamento automatico
    print(indice, nome, lista[indice])

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
    

