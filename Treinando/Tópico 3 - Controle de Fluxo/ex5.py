'''
Peça ao usuário para inserir um número inteiro N. 
Use um laço for para calcular a soma de todos os 
números pares de 0 até N (inclusive).

O que praticar: Laço for, range(), o operador módulo % e uma variável acumuladora.
'''

numero_inteiro = int(input('Informe um numero inteiro: '))
soma = 0

for numero_par in range(numero_inteiro+1):
    if numero_par % 2 == 0:
        soma += numero_par 
print(soma)