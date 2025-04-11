"""
listas em python:
list eh mutavel e suporta varios tipos de caracteres
append, insert, pop, del, clear, extend, +

dados mutaveis:
= copia o valor (imutavel)
= aponta para o endereco na memoria (mutavel)
"""
#         0, 1, 2, 3, 4, 5, 6, 7, 8
lista_a = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print('Lista A: ', lista_a)

lista_b = [20, 30, 40, 50]
print('Lista B: ', lista_b)

#concatena a lista_a com a lista_b em uma lista_c
lista_c = lista_a + lista_b
print('Lista C: ', lista_c)

#nao retorna nenhum valor, pois opera diretamente na lista_a
lista_d = lista_a.extend(lista_b)
print('Lista D: ', lista_d)

lista_a.extend(lista_b)
print('Lista A: ', lista_a)

#altera o valor no indice
lista_a[2] = 300
print(lista_a)

#deleta o valor no indice 7 e nao retorna o valor
del lista_a[7] 

#adiciona valores no final da lista
lista_a.append('Append') 
print(lista_a)

#remove o ultimo elemento da lista e retorna o valor
ultimo_valor = lista_a.pop()
print(lista_a, 'Removido, ', ultimo_valor)

#remove o elemento da lista no indice e retorna o valor
ultimo_valor = lista_a.pop(2)
print(lista_a, 'Removido, ', ultimo_valor)

#adiciona um valor em um indice e "empurra" os outros valores
lista_a.insert(0, 'Insert')
print(lista_a)

#limpa a lista
lista_a.clear()
print(lista_a)

lista_e = ['Joao', 'Pedro', True, 1.2]
lista_f = lista_e.copy()
lista_e[0] = 'Qualquer coisa'
print(lista_f)
print(lista_e)