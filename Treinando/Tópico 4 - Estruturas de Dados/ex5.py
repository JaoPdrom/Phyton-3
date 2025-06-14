'''
Crie uma lista de números inteiros. Use um laço for 
para encontrar o maior e o menor número da lista, sem 
usar as funções max() e min(). Exiba os resultados.

O que praticar:

Iteração sobre uma list, uso de variáveis para guardar o 
estado atual (maior/menor valor encontrado) e lógica condicional.
'''

lista = [1, 2, 2, 3, 4, 4, 4, 5, 100]

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(maior)
print(menor)