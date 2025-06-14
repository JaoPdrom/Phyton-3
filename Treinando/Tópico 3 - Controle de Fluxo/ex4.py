'''
Crie um programa que funcione como uma calculadora. Ele 
deve apresentar um menu ao usuário:

1. Somar
2. Subtrair
3. Multiplicar
4. Dividir
5. Sair

O programa deve pedir dois números e, em seguida, realizar a 
operação escolhida pelo usuário. Use um laço while True para 
que o programa continue executando até que o usuário escolha a opção "Sair".

O que praticar:
Laço while True, if-elif-else para as opções e o comando break para sair do laço.
'''

numero_1 = int(input('Informe um numero: '))
numero_2 = int(input('Informe um segundo numero: '))

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
        if numero_2 >= 0:
            print('Nao permitido dividir por 0')
        else:
            print(f'{numero_1} / {numero_2} = {numero_1/numero_2}')
    elif operador == 'sair':
        break
    else:
        print('Opcao invalida')