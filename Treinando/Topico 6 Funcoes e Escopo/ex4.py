'''
Crie uma função chamada potencia que receba dois parâmetros: 
base e expoente. O expoente deve ter um valor padrão de 2. A 
função deve retornar o resultado da base elevada ao expoente.

Chame a função de duas maneiras:

1. Apenas com o argumento base (usando o expoente padrão).
2. Com os argumentos base e expoente.

O que praticar:
Definição de parâmetros com valores padrão (default).
'''

def potencia(base, expoente=2):
    return base ** expoente

print(f'Chamada 1: {potencia(5)}')
print(f'Chamada 1: {potencia(6, 6)}')