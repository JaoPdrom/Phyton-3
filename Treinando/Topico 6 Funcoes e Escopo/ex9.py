'''
Crie uma função chamada fatorial que receba um número inteiro n 
e retorne seu fatorial. O fatorial de um número é o produto de 
todos os inteiros de 1 até ele mesmo (ex: 5! = 5 * 4 * 3 * 2 * 1 = 120). 
Use um laço para calcular.

O que praticar:
Lógica de programação dentro de uma função, uso de laços e uma variável acumuladora.
'''

def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(f'O fatorial de 5 eh: {fatorial(5)}')

#range(1, n+1)
#partindo de 1 indo ate n + 1