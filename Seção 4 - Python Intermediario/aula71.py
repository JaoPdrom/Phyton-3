"""
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto, type(resto)) #o *resto vira uma list

# def soma(x, y):
#     return x + y

def soma(*args): #empacota argumentos para enviar a funcao
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)
    return total
        
numeros = 1,2,3,4,5,6
outra_soma = soma(*numeros) #desempacota os argumentos
print(outra_soma)
# print(sum((1,2,3,4,5,6)))