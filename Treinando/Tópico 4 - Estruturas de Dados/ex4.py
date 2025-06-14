'''
Dada a lista numeros = [1, 2, 2, 3, 4, 4, 4, 5, 1], use um set 
para remover os números duplicados e, em seguida, converta o 
resultado de volta para uma lista e exiba-a.

O que praticar:
Conversão entre list e set para remover duplicatas.
'''

lista = [1, 2, 2, 3, 4, 4, 4, 5, 1]
lista_sem_duplicados = list(set(lista))

print(lista_sem_duplicados, type(lista_sem_duplicados))