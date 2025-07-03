'''
Crie uma função chamada soma_varios que possa receber um número 
indefinido de argumentos numéricos. A função deve retornar a soma 
de todos os números passados como argumento.

O que praticar: Uso de *args para lidar com múltiplos argumentos posicionais.
Dica: A função sum() pode ser útil aqui.
'''

def soma_varios(*args):
    return sum(args)

print(f'A soma dos numeros eh: {soma_varios(1, 2, 3, 4, 5)}')