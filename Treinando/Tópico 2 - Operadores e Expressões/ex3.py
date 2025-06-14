'''
Peça ao usuário para inserir um número inteiro. 
O programa deve exibir True se o número for par e False se for ímpar.

O que praticar: Operador módulo % e o operador de igualdade ==.

Dica:
Um número é par se o resto da sua divisão por 2 for 0.
'''

numero = int(input('Informe um numero: '))

#metodo com if ternario
print('O numero eh par' if numero % 2 == 0 else 'o numero eh impar')

#metodo if "normal"
if numero % 2 == 0:
    print('O numero eh par')
else:
    print('O numero eh impar')