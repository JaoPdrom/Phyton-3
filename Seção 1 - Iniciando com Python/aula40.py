#calculadora com while

while True:
    #coloca a string em minusculo e verifica se comeca com 's'
    sair = input('Quer sair? [s]im [n]ao ').lower().startswith('s')

    if sair is True:
        break

    num1 = float(input('Informe um numero inteiro: '))
    num2 = float(input('Informe um outro numero inteiro: '))
    operador = input('Informe um operador (+ - / // *): ')

    if operador == '+':
        print(f'A soma de {num1}+{num2} eh: ', num1+num2)
        print(5*'-')
    elif operador == '-':
        print(f'A subtracao de {num1}-{num2} eh: ', num1-num2)
        print(5*'-')
    elif operador == '/':
        if num2 == 0:
            print('Nao eh possivel dividir por zero!')
            print(5*'-')
            continue
        else:
            print(f'A divisao de {num1}/{num2} eh: ', num1/num2)
            print(5*'-')
    elif operador == '//':
        if num2 != 0:
            print(f'A divisao inteira de {num1}/{num2} eh: ', num1//num2)
            print(5*'-')
        else:
            print('Nao eh possivel dividir por zero!')
            print(5*'-')
            continue
    elif operador == '*':
        print(f'A multiplicacao de {num1}*{num2} eh ', num1*num2)
        print(5*'-')
    else:
            print(f'Operador "{operador}" invalido')
            print(5*'-')
