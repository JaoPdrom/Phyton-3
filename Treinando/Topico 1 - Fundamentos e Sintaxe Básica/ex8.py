'''
Crie um programa que pergunte ao usuário um valor em Reais (R$) e a cotação atual do Dólar. 
O programa deve calcular e exibir o valor correspondente em Dólares.

O que praticar:
Manipulação de variáveis float, input() e operações de divisão.
'''

valor_real = float(input('Informe o valor em reais: '))
valor_dolar = float(input('Informe a contacao do dolar: '))

print(f'O valor R${valor_real} em dolar eh {valor_real*valor_dolar}')