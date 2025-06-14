'''
Peça ao usuário para inserir um número N. Use laços aninhados 
(for dentro de for) para desenhar um triângulo retângulo de asteriscos com altura N.

Exemplo para N = 5:

*
*
**
***
****

O que praticar: Laços aninhados e o uso criativo do print().

Dica:
Você pode usar print('*', end='') para não pular de linha.
'''

n = 5

for linha in range(n+1):
    for asterisco in range(linha):
        print('*', end='')
    print()