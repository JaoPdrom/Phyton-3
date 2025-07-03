'''
Crie uma função chamada valida_numero que recebe três parâmetros: 
numero, minimo e maximo. A função deve retornar True se o numero 
estiver dentro do intervalo (inclusive) e False caso contrário. Em 
seguida, crie outra função chamada pede_numero_valido que continue 
pedindo um número ao usuário até que ele insira um valor válido 
(entre 1 e 100, por exemplo), usando a função valida_numero para a verificação.

O que praticar:
Composição de funções (uma função chamando outra), lógica de validação e laços.
'''

def valida_numero(numero, minimo, maximo):
    return minimo <= numero <= maximo

def pede_numero_valido(minimo=1, maximo=100):
    while True:
        try:
            numero = int(input(f"Digite um numero entre {minimo} e {maximo}: "))
            if valida_numero(numero, minimo, maximo):
                print(f"Numero {numero} eh valido!")
            else:
                print(f"Numero invalido! Tente novamente {minimo} e {maximo}.")
        except ValueError:
            print("Entrada invalida. Digite um numero inteiro.")

pede_numero_valido()