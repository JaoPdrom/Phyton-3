'''
Crie quatro variáveis, cada uma armazenando um tipo de dado diferente:
1. Um número inteiro (sua idade).
2. Um número de ponto flutuante (sua altura em metros).
3. Um texto (o nome da sua cidade).
4. Um valor booleano (se você gosta ou não de programar, True ou False).
Exiba cada uma dessas variáveis e o tipo de dado de cada uma delas usando a função type().

O que praticar:
Declaração de variáveis de tipos int, float, str, bool e uso da função type()
'''

idade = input('Informe a sua idade: ')
altura = input('Informa a sua altura: ')
cidade = input('Informe a sua cidade: ')
boole = input('Informe um valor True ou False: ')

print(idade, type(idade))
print(altura, type(altura))
print(cidade, type(cidade))
print(boole, type(boole))