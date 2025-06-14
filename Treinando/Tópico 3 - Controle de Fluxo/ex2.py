'''
Peça ao usuário para inserir um número inteiro. Em seguida, 
use um laço for para exibir a tabuada desse número, do 1 ao 10.

Exemplo de saída para o número 5:
5 x 1 = 5
5 x 2 = 10
5 x 10 = 50

O que praticar:
Laço for com range(), formatação de strings e input().
'''

numero_inteiro = int(input('Numero: '))

for numero in range(11):
    print(f'{numero_inteiro} x {numero} = {numero_inteiro*numero}')