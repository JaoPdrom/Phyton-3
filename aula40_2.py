#solucao apresentada em aula

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um outro numero: ')
    operador = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos numeros sao invalidos. ')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido.')
    if len(operador)>1:
        print('Digite apenas um operador.') 


    if operador == '+':
        print('Soma: ', num_1_float + num_2_float)
    if operador == '-':
        print('Subtracao: ', num_1_float - num_2_float)
    if operador == '/':
        if num_2_float!=0:  
            print('Divisao', num_1_float / num_2_float)
        else:
            print('Divisao por zero nao permitida')
    if operador == '*':
        print('Multiplicacao: ', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair == True:
        break