# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    resultado = 1
    for numeros in args:
        resultado *= numeros
    return resultado


resultado_final = multiplicador(1,2,3,4,5,6)
print(resultado_final)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} eh impar'
    else:
        return f'{numero} eh impar'

numero = par_impar(1)
print(numero)