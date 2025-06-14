'''
Modifique o exercício 4 (Calculadora Simples). Use um bloco 
try-except para garantir que o programa não quebre se:

1. O usuário digitar algo que não seja um número para os valores.
2. O usuário tentar fazer uma divisão por zero.
    
Exiba mensagens de erro amigáveis para cada caso.

O que praticar:
Uso de try-except para ValueError e ZeroDivisionError.
'''

try:
    numero_1 = int(input('Informe um numero: '))
    numero_2 = int(input('Informe um segundo numero: '))
except ValueError:
    print('Valor inserido esta errado.')
    exit()
    
while True:
    print('Selecione a operacao')
    operador = input('[SOMAR, SUBTRAIR, MULTIPLICAR, DIVIDIR, SAIR]:')
    operador.lower()

    if operador == 'somar':
        print(f'{numero_1} + {numero_2} = {numero_1+numero_2}')
    elif operador == 'subtrair':
        print(f'{numero_1} - {numero_2} = {numero_1-numero_2}')
    elif operador == 'multiplicar':
        print(f'{numero_1} * {numero_2} = {numero_1*numero_2}')

    elif operador == 'dividir':
        try:
            divir = numero_1 / numero_2
            print(f'{numero_1} / {numero_2} = {numero_1/numero_2}')
        except ZeroDivisionError:
            print('Nao permitido dividir por 0')

    elif operador == 'sair':
        break
    else:
        print('Opcao invalida')