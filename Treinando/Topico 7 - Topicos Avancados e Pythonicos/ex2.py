'''
Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
crie uma nova lista contendo apenas os números pares, 
usando List Comprehension com uma cláusula if.

O que praticar:
Adição de uma condição (if) a uma List Comprehension.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]

print(f'Numeros: {numeros}')
print(f'Pares: {pares}')