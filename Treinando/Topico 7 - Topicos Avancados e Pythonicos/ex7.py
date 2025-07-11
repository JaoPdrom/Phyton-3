'''
Dada a lista misturada = [1, 'texto', 3.14, True, 4, 'outra string', 5.5], 
crie uma nova lista contendo apenas os números (inteiros e floats) da lista 
original. Use List Comprehension e a função isinstance().

O que praticar
Combinação de List Comprehension com isinstance() para filtragem de tipos.
'''

lista_misturada = [1, 'texto', 3.14, True, 4, 'outra string', 5.5]

numeros = [numero #variavel que recebe o valor do elemento
           for numero in lista_misturada #iterando a lista
           if isinstance(numero, (int, float))] #verifica se eh int ou float
print(numeros)