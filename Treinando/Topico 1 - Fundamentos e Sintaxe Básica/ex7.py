'''
Escreva um programa que pergunte ao usuário o ano atual e a sua idade. 
Em seguida, o programa deve calcular e exibir o ano em que o usuário nasceu.

O que praticar:

Múltiplos input(), casting com int(), e uma operação de subtração para chegar a um resultado lógico.
'''

idade = int(input("Informe a sua idade: "))
ano = int(input("Informe o ano atual: "))

print('Voce nasceu em:', ano-idade)