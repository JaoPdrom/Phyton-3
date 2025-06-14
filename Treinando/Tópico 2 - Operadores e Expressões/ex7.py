'''
Imagine que você tem uma certa quantidade de doces e quer dividi-los 
igualmente entre um grupo de amigos. Peça ao usuário a quantidade de 
doces e o número de amigos. Calcule e exiba:

1. Quantos doces cada amigo receberá.
2. Quantos doces sobrarão para você.

O que praticar:

Operadores de divisão inteira // e módulo %.
'''

quantidade_doces = float(input('Informe a quantidade de doces: '))
quantidade_pessoas = float(input('Informe a quantidade de pessoas: '))

divisao_exata = quantidade_doces // quantidade_pessoas
resto = quantidade_doces % quantidade_pessoas

print(divisao_exata)
print(resto)